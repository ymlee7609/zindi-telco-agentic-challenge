# Track A 문제 분석 — train[1860]~train[1869]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1860] ~ train[1869] (10개)

## 목차

1. [문제 1860: `1234363d-43a...`](#1860) — single-answer, 정답: C16
2. [문제 1861: `dd2b43b8-a60...`](#1861) — single-answer, 정답: C4
3. [문제 1862: `3d533966-f23...`](#1862) — single-answer, 정답: C19
4. [문제 1863: `f581219f-717...`](#1863) — multiple-answer, 정답: C11|C15
5. [문제 1864: `6b290913-dd6...`](#1864) — single-answer, 정답: C7
6. [문제 1865: `9c5b94cc-536...`](#1865) — single-answer, 정답: C10
7. [문제 1866: `512c6bed-8d7...`](#1866) — single-answer, 정답: C11
8. [문제 1867: `c2280044-90d...`](#1867) — single-answer, 정답: C21
9. [문제 1868: `a3729cf6-80b...`](#1868) — single-answer, 정답: C4
10. [문제 1869: `01bcd85a-c13...`](#1869) — single-answer, 정답: C1

---

### 문제 1860: `1234363d-43a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1234363d-43a0-4b78-8f64-5812706b8c67` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease A3 Offset threshold for 3250962_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1860] topology](images/train_1860.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3222898_2
- `C2`: Check test server and transmission issues
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222898_2
- `C4`: Decrease transmission power for 3222898_2
- `C5`: Add neighbor relationship between 3267249_3 and 3222898_2
- `C6`: Add neighbor relationship between 3250962_1 and 3222898_2
- `C7`: Increase A3 Offset threshold for 3222898_2
- `C8`: Lift the tilt angle  of 3222898_2 by 10 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250962_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250962_1
- `C11`: Adjust the azimuth of 3222898_2 by 50 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222898_2
- `C13`: Increase transmission power for 3250962_1
- `C14`: Press down the tilt angle of 3250962_1 by 10 degrees
- `C15`: Adjust the azimuth of 3250962_1 by 33 degrees
- `C16`: Decrease A3 Offset threshold for 3250962_1 **← 정답**
- `C17`: Press down the tilt angle  of 3222898_2 by 10 degrees
- `C18`: Lift the tilt angle of 3250962_1 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3250962_1
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease A3 Offset threshold for 3222898_2
- `C22`: Decrease transmission power for 3250962_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.180 | MS1 | 121.4656705767 | 31.1446268587 | 328 | 504990 | -79.39 | 12.21 | 313.99 | 0.06 | 2.56 | 1583 |
| 2024-09-20 22:21:32.619 | MS1 | 121.4656588934 | 31.1446268692 | 328 | 504990 | -75.56 | 16.65 | 408.55 | 0.16 | 2.08 | 1562 |
| 2024-09-20 22:21:33.954 | MS1 | 121.4656604643 | 31.1446236980 | 328 | 504990 | -79.34 | 12.95 | 490.98 | 0.13 | 2.36 | 1569 |
| 2024-09-20 22:21:34.124 | MS1 | 121.4656741193 | 31.1446322362 | 328 | 504990 | -88.46 | -3.93 | 39.98 | 0.15 | 1.08 | 1587 |
| 2024-09-20 22:21:35.158 | MS1 | 121.4656690948 | 31.1446240497 | 328 | 504990 | -86.95 | -3.79 | 39.82 | 0.15 | 1.10 | 1571 |
| 2024-09-20 22:21:36.149 | MS1 | 121.4656636816 | 31.1446378672 | 328 | 504990 | -83.28 | -2.69 | 72.13 | 0.03 | 1.09 | 1571 |
| 2024-09-20 22:21:37.696 | MS1 | 121.4656677731 | 31.1446263904 | 328 | 504990 | -83.11 | -0.33 | 54.81 | 0.01 | 1.12 | 1590 |
| 2024-09-20 22:21:38.603 | MS1 | 121.4656730528 | 31.1446346050 | 328 | 504990 | -92.64 | -2.44 | 55.02 | 0.17 | 1.46 | 1595 |
| 2024-09-20 22:21:39.161 | MS1 | 121.4656725611 | 31.1446282530 | 441 | 504990 | -80.84 | 12.26 | 208.96 | 0.13 | 1.30 | 1600 |
| 2024-09-20 22:21:40.820 | MS1 | 121.4656645715 | 31.1446339237 | 441 | 504990 | -77.87 | 14.39 | 400.93 | 0.08 | 2.04 | 1580 |
| 2024-09-20 22:21:41.426 | MS1 | 121.4656720803 | 31.1446371543 | 441 | 504990 | -83.99 | 17.63 | 520.19 | 0.16 | 2.75 | 1574 |
| 2024-09-20 22:21:42.860 | MS1 | 121.4656746353 | 31.1446196344 | 441 | 504990 | -76.46 | 14.39 | 583.94 | 0.11 | 2.24 | 1596 |

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
| 3222898 | 2 | 121.4729119134 | 31.1539864996 | 329 | 12 | 10 | 28.3 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3231757 | 4 | 121.4652605854 | 31.1479038604 | 64 | 3 | 3 | 20.6 | TDD | 333 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3250962 | 1 | 121.4649806077 | 31.1503827131 | 141 | 9 | 12 | 43.9 | TDD | 328 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3267249 | 3 | 121.4694362174 | 31.1458512498 | 38 | 12 | 11 | 47.0 | TDD | 810 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.784 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.799 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.905 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.905 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.658 | NREventA3 | measId:2;ServCellPCI:248;Se... |
| 2024-09-20 22:21:37.898 | NRHandoverAttempt | SourcePCI:248;SourceNR-ARFC... |
| 2024-09-20 22:21:37.933 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.945 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.087 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.087 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250962 | 1 | 5.9998 | 7.7527 | -114.9304 | 14.1954 | 148.6847 | 0.0082 | 0.1615 |
| 2024_09_20 22:00 | 3222898 | 2 | 13.7054 | 16.7154 | -115.5511 | 7.7182 | 148.8701 | 0.0184 | 0.0035 |
| 2024_09_20 22:00 | 3267249 | 3 | 17.2759 | 12.1579 | -116.2022 | 19.9429 | 146.0044 | 0.0142 | 0.0044 |
| 2024_09_20 22:00 | 3231757 | 4 | 19.3869 | 12.2174 | -116.8808 | 8.0641 | 111.2687 | 0.0179 | 0.0157 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414514_2D81F879 | 504990 | 441 | -84.1 | 504990 | 328 | -87.5 | 504990 | 810 | -85.5 | 504990 | 333 |
| MR_1774414514_FE59CC25 | 504990 | 441 | -85.8 | 504990 | 328 | -90.1 | 504990 | 810 | -86.5 | 504990 | 333 |
| MR_1774414514_1AB14097 | 504990 | 441 | -82.1 | 504990 | 328 | -86.8 | 504990 | 810 | -86.2 | 504990 | 333 |
| MR_1774414514_4B84399A | 504990 | 441 | -82.7 | 504990 | 328 | -86.6 | 504990 | 810 | -86.2 | 504990 | 333 |
| MR_1774414514_CAC3533B | 504990 | 328 | -86.7 | 504990 | 441 | -82.4 | 504990 | 810 | -83.8 | 504990 | 333 |
| MR_1774414514_BCB303E6 | 504990 | 328 | -90.0 | 504990 | 441 | -84.7 | 504990 | 810 | -84.9 | 504990 | 333 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1861: `dd2b43b8-a60...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dd2b43b8-a601-4f19-a8ef-b3f329a8d790` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3211601_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1861] topology](images/train_1861.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease A3 Offset threshold for 3221881_4
- `C3`: Lift the tilt angle of 3211601_1 by 2 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211601_1 **← 정답**
- `C5`: Increase transmission power for 3211601_1
- `C6`: Add neighbor relationship between 3211601_1 and 3221881_4
- `C7`: Press down the tilt angle  of 3221881_4 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3211601_1
- `C9`: Add neighbor relationship between 3268150_3 and 3221881_4
- `C10`: Increase transmission power for 3221881_4
- `C11`: Increase A3 Offset threshold for 3211601_1
- `C12`: Lift the tilt angle  of 3221881_4 by 10 degrees
- `C13`: Press down the tilt angle of 3211601_1 by 2 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221881_4
- `C15`: Decrease transmission power for 3221881_4
- `C16`: Increase A3 Offset threshold for 3221881_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211601_1
- `C18`: Decrease transmission power for 3211601_1
- `C19`: Check test server and transmission issues
- `C20`: Adjust the azimuth of 3221881_4 by 50 degrees
- `C21`: Adjust the azimuth of 3211601_1 by 9 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221881_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.698 | MS1 | 121.4656742492 | 31.1446216246 | 488 | 504990 | -89.55 | 15.86 | 355.09 | 0.07 | 2.77 | 1597 |
| 2024-09-20 22:21:32.518 | MS1 | 121.4656758613 | 31.1446189883 | 488 | 504990 | -90.72 | 12.24 | 439.93 | 0.12 | 2.52 | 1573 |
| 2024-09-20 22:21:33.249 | MS1 | 121.4656764929 | 31.1446303906 | 488 | 504990 | -90.34 | 16.41 | 533.19 | 0.10 | 2.50 | 1583 |
| 2024-09-20 22:21:34.325 | MS1 | 121.4656748459 | 31.1446196186 | 488 | 504990 | -88.99 | 13.62 | 86.86 | 0.59 | 2.11 | 684 |
| 2024-09-20 22:21:35.563 | MS1 | 121.4656615169 | 31.1446202023 | 488 | 504990 | -89.34 | 15.66 | 90.43 | 0.53 | 2.50 | 523 |
| 2024-09-20 22:21:36.541 | MS1 | 121.4656602004 | 31.1446322404 | 488 | 504990 | -88.44 | 13.37 | 67.17 | 0.54 | 2.27 | 675 |
| 2024-09-20 22:21:37.678 | MS1 | 121.4656685894 | 31.1446204158 | 488 | 504990 | -89.21 | 8.66 | 65.03 | 0.53 | 2.32 | 560 |
| 2024-09-20 22:21:38.817 | MS1 | 121.4656707749 | 31.1446328211 | 488 | 504990 | -90.73 | 10.09 | 55.72 | 0.55 | 2.70 | 681 |
| 2024-09-20 22:21:39.763 | MS1 | 121.4656743761 | 31.1446188098 | 488 | 504990 | -91.90 | 11.85 | 70.17 | 0.51 | 2.96 | 569 |
| 2024-09-20 22:21:40.872 | MS1 | 121.4656740833 | 31.1446293690 | 488 | 504990 | -93.55 | 8.09 | 585.42 | 0.16 | 2.41 | 1576 |
| 2024-09-20 22:21:41.257 | MS1 | 121.4656613115 | 31.1446262218 | 488 | 504990 | -91.60 | 9.50 | 528.92 | 0.08 | 2.89 | 1584 |
| 2024-09-20 22:21:42.313 | MS1 | 121.4656604277 | 31.1446285763 | 488 | 504990 | -89.16 | 12.72 | 419.45 | 0.14 | 2.73 | 1594 |

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
| 3211601 | 1 | 121.4728376071 | 31.1550043153 | 220 | 0 | 11 | 48.7 | TDD | 488 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3221881 | 4 | 121.4650277977 | 31.1466370855 | 82 | 7 | 12 | 22.6 | TDD | 868 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3249184 | 2 | 121.4726151786 | 31.1537690977 | 283 | 9 | 12 | 15.8 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3268150 | 3 | 121.4664655634 | 31.1476711023 | 93 | 2 | 0 | 23.5 | TDD | 212 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.716 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.737 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.886 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.886 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.609 | NREventA3 | measId:2;ServCellPCI:519;Se... |
| 2024-09-20 22:21:37.849 | NRHandoverAttempt | SourcePCI:519;SourceNR-ARFC... |
| 2024-09-20 22:21:37.887 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.900 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.038 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.038 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211601 | 1 | 7.4807 | 7.9862 | -117.5466 | 11.1805 | 179.5486 | 0.0168 | 0.0103 |
| 2024_09_20 22:00 | 3249184 | 2 | 5.1897 | 16.6343 | -115.2982 | 6.8053 | 159.0067 | 0.0155 | 0.0095 |
| 2024_09_20 22:00 | 3268150 | 3 | 12.6737 | 7.6905 | -117.9398 | 9.0916 | 92.4931 | 0.0146 | 0.0198 |
| 2024_09_20 22:00 | 3221881 | 4 | 8.7588 | 11.0870 | -115.4295 | 6.8038 | 117.6879 | 0.0092 | 0.0180 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416132_53AB24A9 | 504990 | 488 | -88.7 | 504990 | 868 | -89.2 | 504990 | 212 | -95.7 | 504990 | 248 |
| MR_1774416132_76B4ECDB | 504990 | 488 | -87.1 | 504990 | 868 | -88.7 | 504990 | 212 | -96.0 | 504990 | 248 |
| MR_1774416132_19FCD754 | 504990 | 488 | -88.8 | 504990 | 868 | -87.3 | 504990 | 212 | -93.7 | 504990 | 248 |
| MR_1774416132_089208B1 | 504990 | 488 | -87.1 | 504990 | 868 | -90.2 | 504990 | 212 | -94.8 | 504990 | 248 |
| MR_1774416132_BC6E6B69 | 504990 | 488 | -90.1 | 504990 | 868 | -88.9 | 504990 | 212 | -94.8 | 504990 | 248 |
| MR_1774416132_6F665F4C | 504990 | 488 | -88.6 | 504990 | 868 | -89.4 | 504990 | 212 | -95.8 | 504990 | 248 |
| MR_1774416132_0AB4DFC4 | 504990 | 488 | -88.3 | 504990 | 868 | -87.5 | 504990 | 212 | -95.9 | 504990 | 248 |
| MR_1774416132_4B5B3CFF | 504990 | 488 | -90.5 | 504990 | 868 | -90.3 | 504990 | 212 | -95.3 | 504990 | 248 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1862: `3d533966-f23...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3d533966-f23d-46c8-8773-b8e85e3faba0` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3268710_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1862] topology](images/train_1862.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219995_3
- `C2`: Lift the tilt angle  of 3219995_3 by 9 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease transmission power for 3219995_3
- `C5`: Press down the tilt angle of 3268710_4 by 5 degrees
- `C6`: Adjust the azimuth of 3219995_3 by 50 degrees
- `C7`: Increase A3 Offset threshold for 3219995_3
- `C8`: Decrease transmission power for 3268710_4
- `C9`: Lift the tilt angle of 3268710_4 by 5 degrees
- `C10`: Press down the tilt angle  of 3219995_3 by 9 degrees
- `C11`: Add neighbor relationship between 3267415_2 and 3219995_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219995_3
- `C13`: Increase transmission power for 3268710_4
- `C14`: Check test server and transmission issues
- `C15`: Decrease A3 Offset threshold for 3268710_4
- `C16`: Add neighbor relationship between 3268710_4 and 3219995_3
- `C17`: Adjust the azimuth of 3268710_4 by 46 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268710_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268710_4 **← 정답**
- `C20`: Increase A3 Offset threshold for 3268710_4
- `C21`: Increase transmission power for 3219995_3
- `C22`: Decrease A3 Offset threshold for 3219995_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.966 | MS1 | 121.4656618939 | 31.1446298823 | 967 | 504990 | -86.37 | 13.32 | 318.76 | 0.03 | 2.52 | 1577 |
| 2024-09-20 22:21:32.132 | MS1 | 121.4656737984 | 31.1446354603 | 967 | 504990 | -87.29 | 14.45 | 354.99 | 0.08 | 2.19 | 1598 |
| 2024-09-20 22:21:33.412 | MS1 | 121.4656688763 | 31.1446206939 | 967 | 504990 | -89.17 | 16.94 | 553.63 | 0.17 | 2.09 | 1574 |
| 2024-09-20 22:21:34.975 | MS1 | 121.4656766984 | 31.1446305656 | 967 | 504990 | -90.14 | 17.80 | 60.66 | 0.54 | 2.73 | 549 |
| 2024-09-20 22:21:35.356 | MS1 | 121.4656769777 | 31.1446305034 | 967 | 504990 | -89.94 | 16.45 | 63.78 | 0.69 | 2.40 | 650 |
| 2024-09-20 22:21:36.415 | MS1 | 121.4656720387 | 31.1446264867 | 967 | 504990 | -88.86 | 17.41 | 64.27 | 0.61 | 2.11 | 572 |
| 2024-09-20 22:21:37.919 | MS1 | 121.4656773842 | 31.1446288438 | 967 | 504990 | -89.83 | 9.41 | 86.00 | 0.55 | 2.08 | 681 |
| 2024-09-20 22:21:38.501 | MS1 | 121.4656699375 | 31.1446198315 | 967 | 504990 | -91.77 | 12.83 | 84.54 | 0.54 | 2.45 | 700 |
| 2024-09-20 22:21:39.635 | MS1 | 121.4656676977 | 31.1446308965 | 967 | 504990 | -93.47 | 8.81 | 57.90 | 0.59 | 2.58 | 617 |
| 2024-09-20 22:21:40.620 | MS1 | 121.4656614071 | 31.1446287861 | 967 | 504990 | -93.29 | 7.04 | 403.17 | 0.17 | 2.18 | 1591 |
| 2024-09-20 22:21:41.643 | MS1 | 121.4656725901 | 31.1446333664 | 967 | 504990 | -92.49 | 8.61 | 495.59 | 0.10 | 2.99 | 1560 |
| 2024-09-20 22:21:42.993 | MS1 | 121.4656631230 | 31.1446246534 | 967 | 504990 | -92.60 | 10.38 | 531.62 | 0.19 | 2.46 | 1585 |

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
| 3215911 | 1 | 121.4687407510 | 31.1472508450 | 7 | 0 | 12 | 39.1 | TDD | 530 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3219995 | 3 | 121.4734009907 | 31.1510198172 | 334 | 7 | 5 | 30.5 | TDD | 605 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3267415 | 2 | 121.4671362834 | 31.1539283143 | 114 | 8 | 10 | 39.5 | TDD | 668 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3268710 | 4 | 121.4729301372 | 31.1469601048 | 203 | 1 | 8 | 49.8 | TDD | 967 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.325 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.346 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.484 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.484 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.182 | NREventA3 | measId:2;ServCellPCI:313;Se... |
| 2024-09-20 22:21:38.422 | NRHandoverAttempt | SourcePCI:313;SourceNR-ARFC... |
| 2024-09-20 22:21:38.454 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.469 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.583 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.583 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215911 | 1 | 12.2332 | 12.1787 | -117.3295 | 9.3981 | 164.8947 | 0.0150 | 0.0043 |
| 2024_09_20 22:00 | 3267415 | 2 | 16.3156 | 9.2391 | -117.6067 | 17.2912 | 111.0136 | 0.0107 | 0.0141 |
| 2024_09_20 22:00 | 3219995 | 3 | 7.6352 | 5.9541 | -114.3832 | 9.3363 | 110.3936 | 0.0002 | 0.0172 |
| 2024_09_20 22:00 | 3268710 | 4 | 5.8044 | 8.9167 | -117.8210 | 18.5193 | 113.3508 | 0.0070 | 0.0194 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415861_19EAA222 | 504990 | 967 | -90.6 | 504990 | 605 | -92.4 | 504990 | 668 | -102.4 | 504990 | 530 |
| MR_1774415861_4CD3C8B3 | 504990 | 967 | -89.3 | 504990 | 605 | -90.5 | 504990 | 668 | -100.0 | 504990 | 530 |
| MR_1774415861_0FDD708E | 504990 | 967 | -89.4 | 504990 | 605 | -89.3 | 504990 | 668 | -101.9 | 504990 | 530 |
| MR_1774415861_17761F18 | 504990 | 967 | -90.0 | 504990 | 605 | -91.9 | 504990 | 668 | -99.1 | 504990 | 530 |
| MR_1774415861_4B8AC541 | 504990 | 967 | -90.4 | 504990 | 605 | -89.9 | 504990 | 668 | -99.4 | 504990 | 530 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1863: `f581219f-717...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f581219f-7178-4b96-9b16-9eaf341121dd` |
| Tag | **multiple-answer** |
| 정답 | **C11|C15** |
| C11 의미 | Increase transmission power for 3230843_3 |
| C15 의미 | Adjust the azimuth of 3230843_3 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1863] topology](images/train_1863.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3275682_4 by 4 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230843_3
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease A3 Offset threshold for 3275682_4
- `C5`: Add neighbor relationship between 3222515_1 and 3275682_4
- `C6`: Lift the tilt angle of 3230843_3 by 3 degrees
- `C7`: Press down the tilt angle  of 3275682_4 by 4 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275682_4
- `C9`: Increase transmission power for 3275682_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275682_4
- `C11`: Increase transmission power for 3230843_3 **← 정답**
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230843_3
- `C13`: Press down the tilt angle of 3230843_3 by 3 degrees
- `C14`: Decrease transmission power for 3230843_3
- `C15`: Adjust the azimuth of 3230843_3 by 50 degrees **← 정답**
- `C16`: Increase A3 Offset threshold for 3275682_4
- `C17`: Adjust the azimuth of 3275682_4 by 28 degrees
- `C18`: Increase A3 Offset threshold for 3230843_3
- `C19`: Decrease A3 Offset threshold for 3230843_3
- `C20`: Decrease transmission power for 3275682_4
- `C21`: Check test server and transmission issues
- `C22`: Add neighbor relationship between 3230843_3 and 3275682_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.177 | MS1 | 121.4656674396 | 31.1446307869 | 861 | 504990 | -93.43 | 16.01 | 373.89 | 0.14 | 2.48 | 1573 |
| 2024-09-20 22:21:32.989 | MS1 | 121.4656778109 | 31.1446240166 | 861 | 504990 | -88.57 | 16.14 | 499.00 | 0.01 | 2.44 | 1595 |
| 2024-09-20 22:21:33.433 | MS1 | 121.4656644511 | 31.1446274542 | 861 | 504990 | -88.50 | 12.24 | 424.42 | 0.15 | 2.27 | 1590 |
| 2024-09-20 22:21:34.283 | MS1 | 121.4656586246 | 31.1446233204 | 861 | 504990 | -109.35 | 1.92 | 62.12 | 0.02 | 1.44 | 1567 |
| 2024-09-20 22:21:35.494 | MS1 | 121.4656762876 | 31.1446193140 | 861 | 504990 | -103.35 | -0.85 | 33.45 | 0.13 | 1.36 | 1584 |
| 2024-09-20 22:21:36.328 | MS1 | 121.4656651165 | 31.1446346682 | 861 | 504990 | -106.84 | 1.55 | 12.12 | 0.04 | 1.31 | 1573 |
| 2024-09-20 22:21:37.729 | MS1 | 121.4656723181 | 31.1446214019 | 861 | 504990 | -106.73 | -0.13 | 84.79 | 0.17 | 1.07 | 1572 |
| 2024-09-20 22:21:38.571 | MS1 | 121.4656759612 | 31.1446359514 | 861 | 504990 | -106.97 | 1.75 | 16.75 | 0.02 | 1.46 | 1566 |
| 2024-09-20 22:21:39.425 | MS1 | 121.4656642506 | 31.1446340499 | 861 | 504990 | -104.15 | -0.46 | 37.58 | 0.02 | 1.09 | 1569 |
| 2024-09-20 22:21:40.434 | MS1 | 121.4656647805 | 31.1446230192 | 861 | 504990 | -87.30 | 14.11 | 538.17 | 0.12 | 2.44 | 1586 |
| 2024-09-20 22:21:41.678 | MS1 | 121.4656605580 | 31.1446261061 | 861 | 504990 | -87.51 | 12.66 | 561.05 | 0.18 | 2.01 | 1573 |
| 2024-09-20 22:21:42.991 | MS1 | 121.4656709824 | 31.1446196552 | 861 | 504990 | -89.83 | 15.68 | 415.14 | 0.06 | 2.07 | 1560 |

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
| 3222515 | 1 | 121.4720325548 | 31.1535655994 | 211 | 2 | 7 | 47.9 | TDD | 834 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3230843 | 3 | 121.4656979524 | 31.1485004211 | 127 | 0 | 3 | 25.3 | TDD | 861 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3245909 | 2 | 121.4679040127 | 31.1472038410 | 254 | 9 | 12 | 26.7 | TDD | 972 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3275682 | 4 | 121.4714680302 | 31.1533736238 | 238 | 2 | 7 | 35.5 | TDD | 30 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.524 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.540 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.687 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.687 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.883 | NREventA2 | measId:1;ServCellPCI:924;Se... |
| 2024-09-20 22:21:35.023 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222515 | 1 | 11.0521 | 16.8802 | -116.2855 | 11.9871 | 145.4487 | 0.0130 | 0.0156 |
| 2024_09_20 22:00 | 3245909 | 2 | 9.1781 | 15.8188 | -114.6970 | 15.7250 | 194.3339 | 0.0036 | 0.0105 |
| 2024_09_20 22:00 | 3230843 | 3 | 17.6953 | 13.2049 | -117.3243 | 9.7484 | 141.0620 | 0.1206 | 0.0079 |
| 2024_09_20 22:00 | 3275682 | 4 | 8.7529 | 6.6641 | -116.6882 | 12.8885 | 128.0359 | 0.0125 | 0.0181 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415610_5C1930F8 | 504990 | 861 | -107.7 | 504990 | 30 | -117.0 | 504990 | 834 | -123.5 | 504990 | 972 |
| MR_1774415610_4C266C2C | 504990 | 861 | -107.8 | 504990 | 30 | -117.8 | 504990 | 834 | -124.4 | 504990 | 972 |
| MR_1774415610_84FA89D9 | 504990 | 861 | -110.8 | 504990 | 30 | -118.4 | 504990 | 834 | -122.5 | 504990 | 972 |
| MR_1774415610_0F0557E4 | 504990 | 861 | -109.4 | 504990 | 30 | -118.9 | 504990 | 834 | -122.3 | 504990 | 972 |
| MR_1774415610_6D6DCFC3 | 504990 | 861 | -107.9 | 504990 | 30 | -119.2 | 504990 | 834 | -122.8 | 504990 | 972 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1864: `6b290913-dd6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6b290913-dd6e-4fa9-8c07-b977d351e805` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1864] topology](images/train_1864.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3222319_3 by 50 degrees
- `C2`: Increase A3 Offset threshold for 3257926_1
- `C3`: Lift the tilt angle of 3222319_3 by 10 degrees
- `C4`: Decrease transmission power for 3257926_1
- `C5`: Decrease A3 Offset threshold for 3257926_1
- `C6`: Adjust the azimuth of 3257926_1 by 50 degrees
- `C7`: Insufficient data; more data is needed for judgment. **← 정답**
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222319_3
- `C9`: Add neighbor relationship between 3225741_2 and 3257926_1
- `C10`: Check test server and transmission issues
- `C11`: Add neighbor relationship between 3222319_3 and 3257926_1
- `C12`: Decrease transmission power for 3222319_3
- `C13`: Press down the tilt angle of 3222319_3 by 10 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222319_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257926_1
- `C16`: Decrease A3 Offset threshold for 3222319_3
- `C17`: Increase transmission power for 3222319_3
- `C18`: Increase A3 Offset threshold for 3222319_3
- `C19`: Increase transmission power for 3257926_1
- `C20`: Lift the tilt angle  of 3257926_1 by 10 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257926_1
- `C22`: Press down the tilt angle  of 3257926_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.375 | MS1 | 121.4656594793 | 31.1446189576 | 1005 | 504990 | -85.27 | 14.43 | 340.97 | 0.17 | 2.72 | 1564 |
| 2024-09-20 22:21:32.608 | MS1 | 121.4656769747 | 31.1446279638 | 1005 | 504990 | -86.91 | 13.94 | 470.98 | 0.05 | 2.26 | 1599 |
| 2024-09-20 22:21:33.446 | MS1 | 121.4656591658 | 31.1446305425 | 1005 | 504990 | -91.73 | 12.71 | 454.40 | 0.17 | 2.86 | 1566 |
| 2024-09-20 22:21:34.659 | MS1 | 121.4656737818 | 31.1446231015 | 1005 | 504990 | -86.94 | 14.78 | 49.75 | 0.08 | 2.61 | 1598 |
| 2024-09-20 22:21:35.281 | MS1 | 121.4656719325 | 31.1446234274 | 1005 | 504990 | -86.63 | 12.66 | 67.95 | 0.19 | 2.28 | 1588 |
| 2024-09-20 22:21:36.491 | MS1 | 121.4656615623 | 31.1446307362 | 1005 | 504990 | -85.65 | 16.14 | 84.84 | 0.10 | 2.86 | 1595 |
| 2024-09-20 22:21:37.946 | MS1 | 121.4656672349 | 31.1446254783 | 1005 | 504990 | -91.55 | 11.57 | 70.30 | 0.17 | 2.21 | 1592 |
| 2024-09-20 22:21:38.518 | MS1 | 121.4656638328 | 31.1446200173 | 1005 | 504990 | -91.01 | 11.78 | 100.57 | 0.18 | 2.93 | 1584 |
| 2024-09-20 22:21:39.407 | MS1 | 121.4656597643 | 31.1446334806 | 1005 | 504990 | -91.07 | 9.84 | 74.04 | 0.14 | 2.77 | 1562 |
| 2024-09-20 22:21:40.622 | MS1 | 121.4656753209 | 31.1446193832 | 1005 | 504990 | -90.65 | 12.36 | 422.95 | 0.15 | 2.15 | 1594 |
| 2024-09-20 22:21:41.774 | MS1 | 121.4656773991 | 31.1446261097 | 1005 | 504990 | -91.86 | 11.21 | 443.91 | 0.13 | 2.91 | 1600 |
| 2024-09-20 22:21:42.265 | MS1 | 121.4656733702 | 31.1446196848 | 1005 | 504990 | -93.48 | 8.15 | 444.14 | 0.15 | 2.66 | 1562 |

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
| 3222319 | 3 | 121.4652901387 | 31.1473933751 | 310 | 2 | 1 | 46.2 | TDD | 1005 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3224353 | 4 | 121.4664389146 | 31.1474794908 | 182 | 5 | 6 | 19.5 | TDD | 30 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3225741 | 2 | 121.4674451119 | 31.1552977026 | 133 | 15 | 4 | 40.0 | TDD | 570 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3257926 | 1 | 121.4748748090 | 31.1456412127 | 180 | 13 | 11 | 38.8 | TDD | 289 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.107 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.122 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.256 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.256 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.945 | NREventA3 | measId:2;ServCellPCI:206;Se... |
| 2024-09-20 22:21:38.185 | NRHandoverAttempt | SourcePCI:206;SourceNR-ARFC... |
| 2024-09-20 22:21:38.229 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.242 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.382 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.382 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3257926 | 1 | 91.5056 | 82.5568 | -114.1579 | 13.2939 | 110.3245 | 0.0154 | 0.0195 |
| 2024_09_19 22:00 | 3225741 | 2 | 79.0106 | 84.6737 | -115.6762 | 9.5259 | 82.4032 | 0.0187 | 0.0003 |
| 2024_09_19 22:00 | 3222319 | 3 | 82.8276 | 93.5495 | -115.5811 | 6.3777 | 151.4363 | 0.0089 | 0.0154 |
| 2024_09_19 22:00 | 3224353 | 4 | 75.1233 | 89.1146 | -115.5699 | 19.4902 | 182.1116 | 0.0034 | 0.0047 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414264_26F5D145 | 504990 | 1005 | -88.4 | 504990 | 289 | -94.5 | 504990 | 570 | -101.6 | 504990 | 30 |
| MR_1774414264_23FE11CE | 504990 | 1005 | -87.0 | 504990 | 289 | -97.0 | 504990 | 570 | -103.1 | 504990 | 30 |
| MR_1774414264_5603D83E | 504990 | 1005 | -87.7 | 504990 | 289 | -97.2 | 504990 | 570 | -101.3 | 504990 | 30 |
| MR_1774414264_FBF3AD3C | 504990 | 1005 | -88.7 | 504990 | 289 | -97.3 | 504990 | 570 | -100.4 | 504990 | 30 |
| MR_1774414264_79F7A40E | 504990 | 1005 | -85.5 | 504990 | 289 | -95.1 | 504990 | 570 | -102.3 | 504990 | 30 |
| MR_1774414264_037EF8D5 | 504990 | 1005 | -85.0 | 504990 | 289 | -96.2 | 504990 | 570 | -99.5 | 504990 | 30 |
| MR_1774414264_C32B4F5A | 504990 | 1005 | -87.1 | 504990 | 289 | -95.1 | 504990 | 570 | -99.7 | 504990 | 30 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1865: `9c5b94cc-536...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9c5b94cc-536f-449e-86c4-a66df537e4f5` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease A3 Offset threshold for 3274769_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1865] topology](images/train_1865.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274769_1
- `C3`: Add neighbor relationship between 3274769_1 and 3214269_3
- `C4`: Press down the tilt angle of 3274769_1 by 2 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214269_3
- `C6`: Decrease transmission power for 3274769_1
- `C7`: Lift the tilt angle of 3274769_1 by 2 degrees
- `C8`: Press down the tilt angle  of 3214269_3 by 10 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease A3 Offset threshold for 3274769_1 **← 정답**
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214269_3
- `C12`: Increase transmission power for 3214269_3
- `C13`: Add neighbor relationship between 3275682_4 and 3214269_3
- `C14`: Lift the tilt angle  of 3214269_3 by 10 degrees
- `C15`: Adjust the azimuth of 3274769_1 by 45 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274769_1
- `C17`: Decrease transmission power for 3214269_3
- `C18`: Increase A3 Offset threshold for 3274769_1
- `C19`: Increase A3 Offset threshold for 3214269_3
- `C20`: Decrease A3 Offset threshold for 3214269_3
- `C21`: Increase transmission power for 3274769_1
- `C22`: Adjust the azimuth of 3214269_3 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.145 | MS1 | 121.4656679404 | 31.1446218844 | 186 | 504990 | -84.04 | 14.70 | 342.52 | 0.05 | 2.81 | 1583 |
| 2024-09-20 22:21:32.480 | MS1 | 121.4656649364 | 31.1446283523 | 186 | 504990 | -78.11 | 15.89 | 478.59 | 0.05 | 2.62 | 1570 |
| 2024-09-20 22:21:33.163 | MS1 | 121.4656665994 | 31.1446240397 | 186 | 504990 | -79.54 | 14.51 | 556.46 | 0.13 | 2.80 | 1561 |
| 2024-09-20 22:21:34.177 | MS1 | 121.4656772298 | 31.1446294149 | 186 | 504990 | -90.38 | -0.14 | 49.46 | 0.19 | 1.22 | 1587 |
| 2024-09-20 22:21:35.762 | MS1 | 121.4656641505 | 31.1446218257 | 186 | 504990 | -89.80 | -0.98 | 69.41 | 0.04 | 1.25 | 1595 |
| 2024-09-20 22:21:36.822 | MS1 | 121.4656627791 | 31.1446374121 | 186 | 504990 | -83.44 | -1.84 | 43.72 | 0.04 | 1.32 | 1573 |
| 2024-09-20 22:21:37.306 | MS1 | 121.4656648713 | 31.1446334873 | 186 | 504990 | -86.72 | -1.93 | 59.14 | 0.16 | 1.47 | 1596 |
| 2024-09-20 22:21:38.661 | MS1 | 121.4656768097 | 31.1446269892 | 186 | 504990 | -88.50 | -0.34 | 37.63 | 0.10 | 1.37 | 1595 |
| 2024-09-20 22:21:39.115 | MS1 | 121.4656646740 | 31.1446304752 | 510 | 504990 | -80.94 | 17.79 | 165.44 | 0.02 | 1.37 | 1579 |
| 2024-09-20 22:21:40.967 | MS1 | 121.4656745963 | 31.1446218916 | 510 | 504990 | -84.41 | 14.45 | 459.63 | 0.11 | 2.26 | 1573 |
| 2024-09-20 22:21:41.544 | MS1 | 121.4656633923 | 31.1446264326 | 510 | 504990 | -75.30 | 16.62 | 312.98 | 0.16 | 2.85 | 1574 |
| 2024-09-20 22:21:42.799 | MS1 | 121.4656688306 | 31.1446242413 | 510 | 504990 | -82.75 | 13.91 | 472.40 | 0.14 | 2.94 | 1574 |

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
| 3214269 | 3 | 121.4703434416 | 31.1538953289 | 148 | 12 | 5 | 40.3 | TDD | 510 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3252163 | 2 | 121.4669582870 | 31.1557671291 | 241 | 10 | 8 | 35.2 | TDD | 293 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3274769 | 1 | 121.4702086796 | 31.1559877465 | 244 | 1 | 0 | 27.3 | TDD | 186 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3275682 | 4 | 121.4747406027 | 31.1510431840 | 181 | 14 | 12 | 38.3 | TDD | 631 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.411 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.433 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.568 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.568 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.307 | NREventA3 | measId:2;ServCellPCI:884;Se... |
| 2024-09-20 22:21:38.547 | NRHandoverAttempt | SourcePCI:884;SourceNR-ARFC... |
| 2024-09-20 22:21:38.595 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.609 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.725 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.725 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274769 | 1 | 6.7601 | 15.9200 | -116.5282 | 13.1692 | 127.4546 | 0.0013 | 0.1020 |
| 2024_09_20 22:00 | 3252163 | 2 | 18.6612 | 7.9916 | -114.3042 | 5.9385 | 183.8526 | 0.0041 | 0.0095 |
| 2024_09_20 22:00 | 3214269 | 3 | 5.6611 | 14.8711 | -114.9574 | 12.5421 | 136.0321 | 0.0182 | 0.0153 |
| 2024_09_20 22:00 | 3275682 | 4 | 6.8811 | 9.8554 | -115.9354 | 18.8522 | 143.0309 | 0.0197 | 0.0158 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412224_14395312 | 504990 | 186 | -90.1 | 504990 | 510 | -85.4 | 504990 | 631 | -88.6 | 504990 | 293 |
| MR_1774412224_FBF5F2DE | 504990 | 510 | -83.1 | 504990 | 186 | -89.6 | 504990 | 631 | -90.2 | 504990 | 293 |
| MR_1774412224_D9C356A8 | 504990 | 186 | -91.6 | 504990 | 510 | -83.4 | 504990 | 631 | -88.7 | 504990 | 293 |
| MR_1774412224_35C6AE8B | 504990 | 186 | -89.3 | 504990 | 510 | -85.0 | 504990 | 631 | -88.0 | 504990 | 293 |
| MR_1774412224_4055D447 | 504990 | 186 | -90.7 | 504990 | 510 | -83.0 | 504990 | 631 | -87.7 | 504990 | 293 |
| MR_1774412224_B2365FF6 | 504990 | 186 | -91.3 | 504990 | 510 | -84.1 | 504990 | 631 | -90.2 | 504990 | 293 |
| MR_1774412224_357335ED | 504990 | 186 | -92.3 | 504990 | 510 | -84.2 | 504990 | 631 | -88.5 | 504990 | 293 |
| MR_1774412224_B1F65493 | 504990 | 186 | -88.8 | 504990 | 510 | -83.5 | 504990 | 631 | -89.5 | 504990 | 293 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1866: `512c6bed-8d7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `512c6bed-8d70-4bee-9c40-d3d67912c35b` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244287_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1866] topology](images/train_1866.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3244287_3
- `C2`: Increase A3 Offset threshold for 3235197_4
- `C3`: Adjust the azimuth of 3244287_3 by 11 degrees
- `C4`: Add neighbor relationship between 3250394_11 and 3235197_4
- `C5`: Press down the tilt angle  of 3235197_4 by 2 degrees
- `C6`: Press down the tilt angle of 3244287_3 by 4 degrees
- `C7`: Decrease A3 Offset threshold for 3235197_4
- `C8`: Decrease transmission power for 3235197_4
- `C9`: Decrease A3 Offset threshold for 3244287_3
- `C10`: Increase transmission power for 3244287_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244287_3 **← 정답**
- `C12`: Check test server and transmission issues
- `C13`: Lift the tilt angle of 3244287_3 by 4 degrees
- `C14`: Lift the tilt angle  of 3235197_4 by 2 degrees
- `C15`: Add neighbor relationship between 3244287_3 and 3235197_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235197_4
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase A3 Offset threshold for 3244287_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244287_3
- `C20`: Increase transmission power for 3235197_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235197_4
- `C22`: Adjust the azimuth of 3235197_4 by 36 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.270 | MS1 | 121.4656696410 | 31.1446301830 | 588 | 504990 | -94.29 | 9.77 | 435.18 | 0.19 | 2.14 | 1560 |
| 2024-09-20 22:21:32.789 | MS1 | 121.4656663513 | 31.1446290301 | 102 | 504990 | -95.73 | 9.74 | 373.14 | 0.15 | 2.98 | 1593 |
| 2024-09-20 22:21:33.962 | MS1 | 121.4656729452 | 31.1446291172 | 891 | 504990 | -95.81 | 10.17 | 426.68 | 0.01 | 2.66 | 1600 |
| 2024-09-20 22:21:34.724 | MS1 | 121.4656763693 | 31.1446206324 | 726 | 152650 | -90.75 | 4.74 | 58.82 | 0.11 | 1.75 | 928 |
| 2024-09-20 22:21:35.223 | MS1 | 121.4656745704 | 31.1446228239 | 922 | 152650 | -96.05 | 6.78 | 74.62 | 0.06 | 1.86 | 966 |
| 2024-09-20 22:21:36.904 | MS1 | 121.4656745011 | 31.1446241517 | 399 | 152650 | -95.80 | 3.23 | 57.84 | 0.14 | 1.58 | 949 |
| 2024-09-20 22:21:37.417 | MS1 | 121.4656715581 | 31.1446351269 | 161 | 152650 | -93.20 | 4.48 | 94.99 | 0.00 | 1.60 | 999 |
| 2024-09-20 22:21:38.672 | MS1 | 121.4656660227 | 31.1446186757 | 726 | 152650 | -93.39 | 2.77 | 96.24 | 0.08 | 1.55 | 908 |
| 2024-09-20 22:21:39.308 | MS1 | 121.4656729003 | 31.1446331804 | 922 | 152650 | -96.68 | 4.27 | 92.09 | 0.01 | 1.60 | 972 |
| 2024-09-20 22:21:40.243 | MS1 | 121.4656580733 | 31.1446287754 | 399 | 152650 | -92.62 | 6.85 | 66.95 | 0.13 | 2.22 | 1560 |
| 2024-09-20 22:21:41.427 | MS1 | 121.4656758175 | 31.1446221791 | 161 | 152650 | -89.44 | 3.46 | 87.13 | 0.13 | 2.50 | 1565 |
| 2024-09-20 22:21:42.878 | MS1 | 121.4656752166 | 31.1446214215 | 726 | 152650 | -89.78 | 6.02 | 84.68 | 0.16 | 2.58 | 1568 |

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
| 3212752 | 13 | 121.4679130678 | 31.1551681906 | 297 | 6 | 9 | 14.3 | FDD | 922 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3228668 | 10 | 121.4685780055 | 31.1462571839 | 240 | 4 | 10 | 10.0 | FDD | 1005 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3235197 | 4 | 121.4691444160 | 31.1473447438 | 264 | 0 | 3 | 15.6 | TDD | 118 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3244272 | 7 | 121.4688304964 | 31.1477207716 | 35 | 8 | 10 | 2.2 | FDD | 161 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3244287 | 3 | 121.4754877319 | 31.1532062008 | 213 | 4 | 1 | 2.3 | TDD | 588 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3247147 | 5 | 121.4656161558 | 31.1469245891 | 267 | 14 | 8 | 24.4 | TDD | 891 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3249748 | 2 | 121.4665284024 | 31.1480942906 | 128 | 1 | 6 | 10.4 | TDD | 102 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3250394 | 11 | 121.4716956975 | 31.1454146005 | 302 | 4 | 7 | 0.1 | FDD | 399 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3251347 | 6 | 121.4755216341 | 31.1555576764 | 323 | 13 | 11 | 19.6 | TDD | 253 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3258769 | 8 | 121.4651950360 | 31.1460910320 | 103 | 12 | 12 | 10.1 | FDD | 354 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3259332 | 9 | 121.4674875832 | 31.1531839587 | 82 | 15 | 2 | 21.0 | FDD | 394 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3266664 | 1 | 121.4744491594 | 31.1514316128 | 217 | 12 | 1 | 15.3 | TDD | 708 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3267521 | 12 | 121.4731675587 | 31.1528508011 | 181 | 9 | 7 | 17.3 | FDD | 726 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |

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
| 2024-09-20 22:21:31.082 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.104 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.225 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.225 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.885 | NREventA2 | measId:1;ServCellPCI:118;Se... |
| 2024-09-20 22:21:35.023 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.320 | NREventA5 | measId:3;ServCellPCI:118;Se... |
| 2024-09-20 22:21:35.386 | NRHandoverAttempt | SourcePCI:118;SourceNR-ARFC... |
| 2024-09-20 22:21:35.410 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.422 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.530 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.530 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266664 | 1 | 17.0132 | 15.6048 | -117.7864 | 9.3980 | 135.1360 | 0.0072 | 0.0022 |
| 2024_09_20 22:00 | 3249748 | 2 | 13.9879 | 15.4276 | -116.6627 | 10.9888 | 175.1041 | 0.0088 | 0.0158 |
| 2024_09_20 22:00 | 3244287 | 3 | 18.6787 | 8.6308 | -116.8839 | 6.2787 | 100.1077 | 0.0069 | 0.0199 |
| 2024_09_20 22:00 | 3235197 | 4 | 15.1038 | 14.7475 | -114.3995 | 13.1678 | 141.1438 | 0.0182 | 0.0110 |
| 2024_09_20 22:00 | 3247147 | 5 | 9.0449 | 14.3897 | -117.9151 | 10.2686 | 185.8466 | 0.0027 | 0.0052 |
| 2024_09_20 22:00 | 3251347 | 6 | 14.2806 | 10.3399 | -116.2021 | 17.4017 | 97.0527 | 0.0119 | 0.0062 |
| 2024_09_20 22:00 | 3244272 | 7 | 18.8111 | 19.7150 | -114.4594 | 3.7610 | 42.8059 | 0.0126 | 0.0034 |
| 2024_09_20 22:00 | 3258769 | 8 | 15.2903 | 11.4541 | -117.6306 | 3.3664 | 20.7881 | 0.0111 | 0.0181 |
| 2024_09_20 22:00 | 3259332 | 9 | 5.8804 | 10.2181 | -117.1917 | 3.1459 | 35.2314 | 0.0022 | 0.0197 |
| 2024_09_20 22:00 | 3228668 | 10 | 10.6884 | 12.4284 | -115.2674 | 4.3293 | 34.0604 | 0.0104 | 0.0179 |
| 2024_09_20 22:00 | 3250394 | 11 | 9.1695 | 6.1356 | -117.7830 | 4.0042 | 29.2911 | 0.0125 | 0.0077 |
| 2024_09_20 22:00 | 3267521 | 12 | 12.4301 | 5.3210 | -117.3809 | 4.8896 | 27.3580 | 0.0162 | 0.0089 |
| 2024_09_20 22:00 | 3212752 | 13 | 15.4883 | 9.8457 | -117.4501 | 3.9946 | 46.1011 | 0.0156 | 0.0064 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412263_B4A50ADC | 152650 | 726 | -90.8 | 152650 | 394 | -96.7 | 152650 | 1005 | -103.5 | 152650 | 354 |
| MR_1774412263_B0DD936B | 504990 | 891 | -96.8 | 504990 | 118 | -95.0 | 504990 | 708 | -99.3 | 504990 | 253 |
| MR_1774412263_8966891C | 152650 | 726 | -89.7 | 152650 | 394 | -96.8 | 152650 | 1005 | -102.7 | 152650 | 354 |
| MR_1774412263_627C8031 | 504990 | 891 | -95.9 | 504990 | 118 | -95.2 | 504990 | 708 | -98.8 | 504990 | 253 |
| MR_1774412263_14ADF6BE | 504990 | 891 | -96.9 | 504990 | 118 | -94.0 | 504990 | 708 | -96.0 | 504990 | 253 |
| MR_1774412263_A052576B | 152650 | 726 | -90.7 | 152650 | 394 | -97.3 | 152650 | 1005 | -101.7 | 152650 | 354 |
| MR_1774412263_AC8C20E2 | 152650 | 726 | -88.9 | 152650 | 394 | -98.1 | 152650 | 1005 | -100.0 | 152650 | 354 |
| MR_1774412263_7A99EDB9 | 152650 | 726 | -89.4 | 152650 | 394 | -95.0 | 152650 | 1005 | -100.1 | 152650 | 354 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1867: `c2280044-90d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c2280044-90df-4d36-8a68-9b013cc279c0` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease A3 Offset threshold for 3264588_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1867] topology](images/train_1867.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3264588_3 by 10 degrees
- `C2`: Increase transmission power for 3264588_3
- `C3`: Add neighbor relationship between 3264588_3 and 3263729_1
- `C4`: Decrease transmission power for 3264588_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264588_3
- `C6`: Add neighbor relationship between 3266496_4 and 3263729_1
- `C7`: Increase A3 Offset threshold for 3263729_1
- `C8`: Increase transmission power for 3263729_1
- `C9`: Check test server and transmission issues
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263729_1
- `C11`: Decrease A3 Offset threshold for 3263729_1
- `C12`: Decrease transmission power for 3263729_1
- `C13`: Increase A3 Offset threshold for 3264588_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264588_3
- `C15`: Lift the tilt angle  of 3263729_1 by 6 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263729_1
- `C17`: Adjust the azimuth of 3264588_3 by 50 degrees
- `C18`: Press down the tilt angle of 3264588_3 by 10 degrees
- `C19`: Adjust the azimuth of 3263729_1 by 50 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease A3 Offset threshold for 3264588_3 **← 정답**
- `C22`: Press down the tilt angle  of 3263729_1 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.535 | MS1 | 121.4656773150 | 31.1446350431 | 485 | 504990 | -77.98 | 12.79 | 324.18 | 0.07 | 2.90 | 1572 |
| 2024-09-20 22:21:32.732 | MS1 | 121.4656694027 | 31.1446320003 | 485 | 504990 | -82.58 | 17.06 | 487.51 | 0.20 | 2.74 | 1564 |
| 2024-09-20 22:21:33.728 | MS1 | 121.4656716503 | 31.1446259668 | 485 | 504990 | -81.83 | 13.54 | 379.08 | 0.19 | 2.91 | 1581 |
| 2024-09-20 22:21:34.265 | MS1 | 121.4656751358 | 31.1446349849 | 485 | 504990 | -86.48 | -3.65 | 43.34 | 0.13 | 1.18 | 1594 |
| 2024-09-20 22:21:35.848 | MS1 | 121.4656602808 | 31.1446286566 | 485 | 504990 | -85.40 | -1.93 | 58.45 | 0.19 | 1.45 | 1569 |
| 2024-09-20 22:21:36.233 | MS1 | 121.4656614404 | 31.1446234585 | 485 | 504990 | -91.88 | -1.85 | 40.30 | 0.04 | 1.01 | 1577 |
| 2024-09-20 22:21:37.629 | MS1 | 121.4656676462 | 31.1446227778 | 485 | 504990 | -92.26 | -1.70 | 65.52 | 0.18 | 1.07 | 1569 |
| 2024-09-20 22:21:38.315 | MS1 | 121.4656674753 | 31.1446378049 | 485 | 504990 | -90.80 | -1.02 | 45.80 | 0.05 | 1.28 | 1584 |
| 2024-09-20 22:21:39.291 | MS1 | 121.4656676116 | 31.1446336803 | 936 | 504990 | -78.33 | 16.30 | 277.85 | 0.09 | 1.12 | 1583 |
| 2024-09-20 22:21:40.175 | MS1 | 121.4656711568 | 31.1446284189 | 936 | 504990 | -85.00 | 15.38 | 329.77 | 0.10 | 2.93 | 1576 |
| 2024-09-20 22:21:41.629 | MS1 | 121.4656589266 | 31.1446195861 | 936 | 504990 | -83.45 | 13.29 | 348.23 | 0.02 | 2.66 | 1579 |
| 2024-09-20 22:21:42.175 | MS1 | 121.4656604892 | 31.1446238346 | 936 | 504990 | -75.45 | 12.81 | 502.10 | 0.20 | 2.19 | 1572 |

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
| 3247371 | 2 | 121.4651435889 | 31.1517712155 | 142 | 2 | 11 | 42.6 | TDD | 996 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3263729 | 1 | 121.4681539304 | 31.1502852078 | 302 | 2 | 7 | 48.8 | TDD | 936 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3264588 | 3 | 121.4653396113 | 31.1558242839 | 90 | 14 | 4 | 46.5 | TDD | 485 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3266496 | 4 | 121.4683323997 | 31.1511396620 | 69 | 0 | 6 | 17.9 | TDD | 828 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.042 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.058 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.176 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.176 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.905 | NREventA3 | measId:2;ServCellPCI:698;Se... |
| 2024-09-20 22:21:38.145 | NRHandoverAttempt | SourcePCI:698;SourceNR-ARFC... |
| 2024-09-20 22:21:38.180 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.190 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.322 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.322 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263729 | 1 | 11.6348 | 7.8569 | -115.0352 | 10.0147 | 197.0519 | 0.0053 | 0.0182 |
| 2024_09_20 22:00 | 3247371 | 2 | 17.0091 | 14.6254 | -115.0975 | 5.1807 | 170.6786 | 0.0134 | 0.0147 |
| 2024_09_20 22:00 | 3264588 | 3 | 12.9828 | 14.7653 | -116.6146 | 5.7543 | 138.6688 | 0.0134 | 0.1711 |
| 2024_09_20 22:00 | 3266496 | 4 | 18.4229 | 12.0013 | -115.9219 | 7.7432 | 188.4272 | 0.0171 | 0.0099 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415366_64F461A3 | 504990 | 936 | -81.8 | 504990 | 485 | -85.0 | 504990 | 828 | -82.2 | 504990 | 996 |
| MR_1774415366_CAFADE52 | 504990 | 936 | -79.0 | 504990 | 485 | -85.8 | 504990 | 828 | -83.1 | 504990 | 996 |
| MR_1774415366_017EDF1B | 504990 | 485 | -84.8 | 504990 | 936 | -80.7 | 504990 | 828 | -85.1 | 504990 | 996 |
| MR_1774415366_17AD8604 | 504990 | 485 | -85.2 | 504990 | 936 | -81.8 | 504990 | 828 | -81.4 | 504990 | 996 |
| MR_1774415366_24975A83 | 504990 | 936 | -80.8 | 504990 | 485 | -88.4 | 504990 | 828 | -83.8 | 504990 | 996 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1868: `a3729cf6-80b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a3729cf6-80b1-4966-a316-cded20abb537` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1868] topology](images/train_1868.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3211510_4 and 3259296_1
- `C2`: Decrease transmission power for 3259296_1
- `C3`: Lift the tilt angle  of 3259296_1 by 6 degrees
- `C4`: Insufficient data; more data is needed for judgment. **← 정답**
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259296_1
- `C6`: Decrease A3 Offset threshold for 3259296_1
- `C7`: Increase A3 Offset threshold for 3259296_1
- `C8`: Press down the tilt angle of 3215556_3 by 10 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215556_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259296_1
- `C11`: Increase transmission power for 3259296_1
- `C12`: Press down the tilt angle  of 3259296_1 by 6 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215556_3
- `C14`: Lift the tilt angle of 3215556_3 by 10 degrees
- `C15`: Check test server and transmission issues
- `C16`: Adjust the azimuth of 3259296_1 by 50 degrees
- `C17`: Adjust the azimuth of 3215556_3 by 50 degrees
- `C18`: Add neighbor relationship between 3215556_3 and 3259296_1
- `C19`: Decrease A3 Offset threshold for 3215556_3
- `C20`: Increase transmission power for 3215556_3
- `C21`: Decrease transmission power for 3215556_3
- `C22`: Increase A3 Offset threshold for 3215556_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.460 | MS1 | 121.4656713083 | 31.1446262509 | 373 | 504990 | -86.89 | 13.76 | 339.37 | 0.15 | 2.02 | 1590 |
| 2024-09-20 22:21:32.245 | MS1 | 121.4656634193 | 31.1446227625 | 373 | 504990 | -90.77 | 17.34 | 545.20 | 0.13 | 2.77 | 1589 |
| 2024-09-20 22:21:33.722 | MS1 | 121.4656690222 | 31.1446223730 | 373 | 504990 | -90.80 | 13.62 | 399.75 | 0.10 | 2.24 | 1564 |
| 2024-09-20 22:21:34.500 | MS1 | 121.4656700023 | 31.1446216928 | 373 | 504990 | -90.02 | 17.02 | 74.07 | 0.13 | 2.36 | 1562 |
| 2024-09-20 22:21:35.163 | MS1 | 121.4656581162 | 31.1446299359 | 373 | 504990 | -87.72 | 16.17 | 85.81 | 0.12 | 2.06 | 1575 |
| 2024-09-20 22:21:36.897 | MS1 | 121.4656588616 | 31.1446379096 | 373 | 504990 | -91.73 | 12.88 | 75.73 | 0.03 | 2.88 | 1584 |
| 2024-09-20 22:21:37.679 | MS1 | 121.4656694925 | 31.1446318525 | 373 | 504990 | -91.00 | 9.67 | 85.05 | 0.13 | 2.93 | 1570 |
| 2024-09-20 22:21:38.822 | MS1 | 121.4656723438 | 31.1446298398 | 373 | 504990 | -90.33 | 12.56 | 69.87 | 0.00 | 2.56 | 1590 |
| 2024-09-20 22:21:39.600 | MS1 | 121.4656770127 | 31.1446334842 | 373 | 504990 | -93.38 | 11.77 | 73.84 | 0.07 | 2.88 | 1573 |
| 2024-09-20 22:21:40.530 | MS1 | 121.4656760269 | 31.1446323558 | 373 | 504990 | -92.67 | 12.20 | 541.22 | 0.01 | 2.66 | 1560 |
| 2024-09-20 22:21:41.357 | MS1 | 121.4656673277 | 31.1446257157 | 373 | 504990 | -89.22 | 7.94 | 526.71 | 0.06 | 2.10 | 1560 |
| 2024-09-20 22:21:42.384 | MS1 | 121.4656744945 | 31.1446338583 | 373 | 504990 | -93.75 | 8.73 | 556.05 | 0.11 | 2.29 | 1561 |

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
| 3211510 | 4 | 121.4748805645 | 31.1508727805 | 247 | 5 | 6 | 21.6 | TDD | 918 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3215556 | 3 | 121.4688479602 | 31.1558224287 | 22 | 11 | 0 | 34.7 | TDD | 373 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3259296 | 1 | 121.4655858898 | 31.1488422569 | 270 | 1 | 4 | 37.7 | TDD | 707 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3260686 | 2 | 121.4709468948 | 31.1545710665 | 206 | 7 | 5 | 42.9 | TDD | 324 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.409 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.430 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.552 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.552 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.218 | NREventA3 | measId:2;ServCellPCI:635;Se... |
| 2024-09-20 22:21:38.458 | NRHandoverAttempt | SourcePCI:635;SourceNR-ARFC... |
| 2024-09-20 22:21:38.498 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.509 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.655 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.655 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3259296 | 1 | 89.3993 | 90.4059 | -115.6603 | 5.2313 | 92.0476 | 0.0026 | 0.0013 |
| 2024_09_19 22:00 | 3260686 | 2 | 77.2479 | 87.1594 | -117.6214 | 9.3358 | 194.0807 | 0.0107 | 0.0112 |
| 2024_09_19 22:00 | 3215556 | 3 | 84.4131 | 88.3381 | -117.2078 | 18.4080 | 121.6385 | 0.0162 | 0.0187 |
| 2024_09_19 22:00 | 3211510 | 4 | 75.3319 | 94.6366 | -117.4860 | 19.9858 | 180.7842 | 0.0181 | 0.0078 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416865_433E0013 | 504990 | 373 | -91.3 | 504990 | 707 | -90.6 | 504990 | 918 | -96.1 | 504990 | 324 |
| MR_1774416865_80EE2EE3 | 504990 | 373 | -88.4 | 504990 | 707 | -90.0 | 504990 | 918 | -97.5 | 504990 | 324 |
| MR_1774416865_6A90A4CA | 504990 | 373 | -89.9 | 504990 | 707 | -91.8 | 504990 | 918 | -98.6 | 504990 | 324 |
| MR_1774416865_A87DE4C9 | 504990 | 373 | -91.2 | 504990 | 707 | -89.6 | 504990 | 918 | -95.9 | 504990 | 324 |
| MR_1774416865_0B9DEBB1 | 504990 | 373 | -88.2 | 504990 | 707 | -93.3 | 504990 | 918 | -98.4 | 504990 | 324 |
| MR_1774416865_4CE73837 | 504990 | 373 | -89.1 | 504990 | 707 | -89.8 | 504990 | 918 | -96.5 | 504990 | 324 |
| MR_1774416865_7C56C9FE | 504990 | 373 | -91.6 | 504990 | 707 | -92.3 | 504990 | 918 | -98.2 | 504990 | 324 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1869: `01bcd85a-c13...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `01bcd85a-c138-4a68-a8ca-708aa806ec29` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Lift the tilt angle  of 3222725_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1869] topology](images/train_1869.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3222725_1 by 10 degrees **← 정답**
- `C2`: Decrease A3 Offset threshold for 3259721_2
- `C3`: Add neighbor relationship between 3268453_3 and 3259721_2
- `C4`: Decrease transmission power for 3268453_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259721_2
- `C6`: Decrease transmission power for 3259721_2
- `C7`: Press down the tilt angle  of 3222725_1 by 10 degrees
- `C8`: Press down the tilt angle of 3268453_3 by 6 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Adjust the azimuth of 3268453_3 by 17 degrees
- `C11`: Adjust the azimuth of 3222725_1 by 50 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268453_3
- `C13`: Add neighbor relationship between 3222725_1 and 3259721_2
- `C14`: Increase transmission power for 3259721_2
- `C15`: Increase A3 Offset threshold for 3268453_3
- `C16`: Check test server and transmission issues
- `C17`: Decrease A3 Offset threshold for 3268453_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268453_3
- `C19`: Increase transmission power for 3268453_3
- `C20`: Increase A3 Offset threshold for 3259721_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259721_2
- `C22`: Lift the tilt angle of 3268453_3 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.397 | MS1 | 121.4656728715 | 31.1446250716 | 583 | 504990 | -86.99 | 16.51 | 495.16 | 0.19 | 2.20 | 1581 |
| 2024-09-20 22:21:32.299 | MS1 | 121.4656749332 | 31.1446196069 | 583 | 504990 | -87.54 | 12.78 | 419.95 | 0.05 | 2.77 | 1561 |
| 2024-09-20 22:21:33.742 | MS1 | 121.4656750062 | 31.1446190931 | 583 | 504990 | -91.81 | 12.00 | 432.86 | 0.06 | 2.38 | 1598 |
| 2024-09-20 22:21:34.655 | MS1 | 121.4656693702 | 31.1446240970 | 583 | 504990 | -87.14 | 17.01 | 96.96 | 0.03 | 2.85 | 1589 |
| 2024-09-20 22:21:35.320 | MS1 | 121.4656607557 | 31.1446212191 | 583 | 504990 | -91.47 | 17.94 | 80.24 | 0.11 | 2.92 | 1570 |
| 2024-09-20 22:21:36.921 | MS1 | 121.4656590149 | 31.1446340882 | 583 | 504990 | -91.34 | 14.64 | 53.95 | 0.14 | 2.66 | 1561 |
| 2024-09-20 22:21:37.231 | MS1 | 121.4656620861 | 31.1446295285 | 583 | 504990 | -91.21 | 12.25 | 57.19 | 0.05 | 2.14 | 1577 |
| 2024-09-20 22:21:38.242 | MS1 | 121.4656734446 | 31.1446260735 | 583 | 504990 | -93.47 | 10.68 | 56.82 | 0.05 | 2.00 | 1583 |
| 2024-09-20 22:21:39.697 | MS1 | 121.4656617628 | 31.1446263006 | 583 | 504990 | -91.29 | 7.70 | 85.89 | 0.05 | 2.24 | 1578 |
| 2024-09-20 22:21:40.289 | MS1 | 121.4656629645 | 31.1446269544 | 583 | 504990 | -89.01 | 9.56 | 299.03 | 0.03 | 2.17 | 1591 |
| 2024-09-20 22:21:41.572 | MS1 | 121.4656749573 | 31.1446225516 | 583 | 504990 | -92.45 | 8.75 | 372.50 | 0.04 | 2.55 | 1583 |
| 2024-09-20 22:21:42.646 | MS1 | 121.4656714281 | 31.1446275822 | 583 | 504990 | -92.01 | 7.11 | 442.41 | 0.09 | 2.46 | 1595 |

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
| 3222725 | 1 | 121.4688672528 | 31.1443772564 | 69 | 15 | 6 | 36.5 | TDD | 987 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3258079 | 4 | 121.4663366698 | 31.1539672747 | 274 | 1 | 10 | 32.2 | TDD | 999 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3259721 | 2 | 121.4720724143 | 31.1527921538 | 334 | 14 | 10 | 33.2 | TDD | 428 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3268453 | 3 | 121.4641979653 | 31.1545659666 | 156 | 5 | 1 | 18.3 | TDD | 583 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.744 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.760 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:30.898 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.898 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.641 | NREventA3 | measId:2;ServCellPCI:837;Se... |
| 2024-09-20 22:21:37.881 | NRHandoverAttempt | SourcePCI:837;SourceNR-ARFC... |
| 2024-09-20 22:21:37.913 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.923 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.056 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.056 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222725 | 1 | 11.1267 | 10.9475 | -114.8195 | 12.4514 | 138.2277 | 0.0099 | 0.0085 |
| 2024_09_20 22:00 | 3259721 | 2 | 7.1988 | 13.5738 | -115.7648 | 5.3223 | 197.0667 | 0.0101 | 0.0073 |
| 2024_09_20 22:00 | 3268453 | 3 | 81.6310 | 76.4617 | -117.4531 | 13.5112 | 128.1562 | 0.0028 | 0.0176 |
| 2024_09_20 22:00 | 3258079 | 4 | 7.6559 | 16.6035 | -117.2653 | 13.9530 | 128.1965 | 0.0177 | 0.0010 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415303_34C579D4 | 504990 | 583 | -85.1 | 504990 | 428 | -88.1 | 504990 | 987 | -100.8 | 504990 | 999 |
| MR_1774415303_3E8D6234 | 504990 | 583 | -89.0 | 504990 | 428 | -88.4 | 504990 | 987 | -99.3 | 504990 | 999 |
| MR_1774415303_64D65C69 | 504990 | 583 | -87.0 | 504990 | 428 | -87.0 | 504990 | 987 | -101.4 | 504990 | 999 |
| MR_1774415303_CC6F39CB | 504990 | 583 | -88.6 | 504990 | 428 | -89.3 | 504990 | 987 | -100.5 | 504990 | 999 |
| MR_1774415303_3E1C7613 | 504990 | 583 | -88.0 | 504990 | 428 | -89.5 | 504990 | 987 | -101.9 | 504990 | 999 |
| MR_1774415303_3E6B7D52 | 504990 | 583 | -87.5 | 504990 | 428 | -89.5 | 504990 | 987 | -102.3 | 504990 | 999 |
| MR_1774415303_D542FD48 | 504990 | 583 | -87.7 | 504990 | 428 | -87.3 | 504990 | 987 | -102.3 | 504990 | 999 |
| MR_1774415303_F60AA141 | 504990 | 583 | -86.9 | 504990 | 428 | -90.0 | 504990 | 987 | -100.2 | 504990 | 999 |

> *... 2개 열 생략 (전체 14열)*

---
