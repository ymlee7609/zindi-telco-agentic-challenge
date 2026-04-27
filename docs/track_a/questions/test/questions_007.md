# Track A 문제 분석 — test[60]~test[69]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[60] ~ test[69] (10개)

## 목차

1. [문제 60: `bc51228a-4d7...`](#60) — single-answer
2. [문제 61: `b013a598-26c...`](#61) — single-answer
3. [문제 62: `37babafe-bf9...`](#62) — single-answer
4. [문제 63: `78ff9e6c-ae8...`](#63) — multiple-answer
5. [문제 64: `7db4595e-509...`](#64) — single-answer
6. [문제 65: `06dde601-83f...`](#65) — single-answer
7. [문제 66: `e1ca3a6b-32d...`](#66) — multiple-answer
8. [문제 67: `21a770ea-10f...`](#67) — single-answer
9. [문제 68: `08a2494c-2a8...`](#68) — multiple-answer
10. [문제 69: `83ab9a55-ae4...`](#69) — single-answer

---

### 문제 60: `bc51228a-4d7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bc51228a-4d7e-48c7-a2fb-8ed9b5383964` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[60] topology](images/test_0060.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3235121_4 by 6 degrees
- `C2`: Adjust the azimuth of 3235121_4 by 31 degrees
- `C3`: Lift the tilt angle  of 3272424_2 by 10 degrees
- `C4`: Increase transmission power for 3235121_4
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235121_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272424_2
- `C8`: Check test server and transmission issues
- `C9`: Decrease A3 Offset threshold for 3272424_2
- `C10`: Decrease transmission power for 3272424_2
- `C11`: Add neighbor relationship between 3235813_1 and 3272424_2
- `C12`: Decrease A3 Offset threshold for 3235121_4
- `C13`: Decrease transmission power for 3235121_4
- `C14`: Increase transmission power for 3272424_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272424_2
- `C16`: Add neighbor relationship between 3235121_4 and 3272424_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235121_4
- `C18`: Increase A3 Offset threshold for 3235121_4
- `C19`: Adjust the azimuth of 3272424_2 by 50 degrees
- `C20`: Increase A3 Offset threshold for 3272424_2
- `C21`: Press down the tilt angle  of 3272424_2 by 10 degrees
- `C22`: Press down the tilt angle of 3235121_4 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.129 | MS1 | 121.4656764616 | 31.1446300625 | 279 | 504990 | -87.05 | 16.83 | 499.00 | 0.20 | 2.75 | 1587 |
| 2024-09-20 22:21:32.678 | MS1 | 121.4656624218 | 31.1446265699 | 279 | 504990 | -86.05 | 13.65 | 556.06 | 0.09 | 2.55 | 1576 |
| 2024-09-20 22:21:33.849 | MS1 | 121.4656726581 | 31.1446266554 | 279 | 504990 | -87.52 | 16.10 | 401.22 | 0.07 | 2.68 | 1599 |
| 2024-09-20 22:21:34.421 | MS1 | 121.4656617021 | 31.1446195601 | 279 | 504990 | -88.21 | 14.09 | 60.42 | 0.65 | 2.93 | 513 |
| 2024-09-20 22:21:35.219 | MS1 | 121.4656689464 | 31.1446182726 | 279 | 504990 | -85.47 | 13.40 | 94.78 | 0.62 | 2.76 | 570 |
| 2024-09-20 22:21:36.339 | MS1 | 121.4656591505 | 31.1446352792 | 279 | 504990 | -85.31 | 17.61 | 95.93 | 0.51 | 2.60 | 639 |
| 2024-09-20 22:21:37.391 | MS1 | 121.4656729199 | 31.1446305901 | 279 | 504990 | -90.74 | 8.38 | 75.02 | 0.67 | 2.47 | 640 |
| 2024-09-20 22:21:38.186 | MS1 | 121.4656683860 | 31.1446236940 | 279 | 504990 | -92.29 | 12.23 | 93.20 | 0.66 | 2.15 | 571 |
| 2024-09-20 22:21:39.236 | MS1 | 121.4656656588 | 31.1446334778 | 279 | 504990 | -90.72 | 8.01 | 92.87 | 0.55 | 2.02 | 513 |
| 2024-09-20 22:21:40.294 | MS1 | 121.4656770286 | 31.1446252307 | 279 | 504990 | -89.21 | 9.23 | 592.72 | 0.03 | 2.68 | 1573 |
| 2024-09-20 22:21:41.574 | MS1 | 121.4656595231 | 31.1446348589 | 279 | 504990 | -91.54 | 11.87 | 487.86 | 0.13 | 2.06 | 1590 |
| 2024-09-20 22:21:42.660 | MS1 | 121.4656637127 | 31.1446291153 | 279 | 504990 | -93.47 | 12.05 | 314.59 | 0.18 | 2.22 | 1597 |

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
| 3235121 | 4 | 121.4726075630 | 31.1452606442 | 233 | 4 | 6 | 22.4 | TDD | 279 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3235813 | 1 | 121.4674857079 | 31.1467050698 | 165 | 12 | 5 | 17.8 | TDD | 304 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3264598 | 3 | 121.4710075074 | 31.1446875483 | 123 | 8 | 1 | 44.1 | TDD | 854 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3272424 | 2 | 121.4679980839 | 31.1499056499 | 0 | 15 | 6 | 42.3 | TDD | 1005 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.500 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.525 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.674 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.674 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.365 | NREventA3 | measId:2;ServCellPCI:951;Se... |
| 2024-09-20 22:21:38.605 | NRHandoverAttempt | SourcePCI:951;SourceNR-ARFC... |
| 2024-09-20 22:21:38.636 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.648 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.749 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.749 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235813 | 1 | 6.0318 | 16.1110 | -114.7031 | 12.9676 | 155.2226 | 0.0109 | 0.0027 |
| 2024_09_20 22:00 | 3272424 | 2 | 19.1694 | 11.6513 | -115.2699 | 12.2489 | 136.9982 | 0.0016 | 0.0170 |
| 2024_09_20 22:00 | 3264598 | 3 | 16.3544 | 11.6826 | -115.5887 | 15.8994 | 166.6333 | 0.0162 | 0.0100 |
| 2024_09_20 22:00 | 3235121 | 4 | 19.6169 | 9.0419 | -114.5958 | 17.2412 | 142.6080 | 0.0078 | 0.0067 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414862_229F4A46 | 504990 | 279 | -87.4 | 504990 | 1005 | -88.9 | 504990 | 304 | -97.4 | 504990 | 854 |
| MR_1774414862_9438F628 | 504990 | 279 | -86.5 | 504990 | 1005 | -89.3 | 504990 | 304 | -96.6 | 504990 | 854 |
| MR_1774414862_C83487CF | 504990 | 279 | -89.4 | 504990 | 1005 | -92.3 | 504990 | 304 | -100.3 | 504990 | 854 |
| MR_1774414862_6B29E5A7 | 504990 | 279 | -90.0 | 504990 | 1005 | -90.5 | 504990 | 304 | -100.0 | 504990 | 854 |
| MR_1774414862_E046DA50 | 504990 | 279 | -88.1 | 504990 | 1005 | -89.2 | 504990 | 304 | -100.3 | 504990 | 854 |
| MR_1774414862_325A1EC2 | 504990 | 279 | -86.6 | 504990 | 1005 | -92.4 | 504990 | 304 | -98.1 | 504990 | 854 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 61: `b013a598-26c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b013a598-26c4-44be-b6a3-741291489b97` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[61] topology](images/test_0061.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Adjust the azimuth of 3269183_1 by 50 degrees
- `C3`: Increase transmission power for 3278292_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269183_1
- `C5`: Decrease transmission power for 3269183_1
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease transmission power for 3278292_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278292_3
- `C9`: Increase A3 Offset threshold for 3278292_3
- `C10`: Press down the tilt angle  of 3269183_1 by 10 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269183_1
- `C12`: Lift the tilt angle  of 3269183_1 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3278292_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278292_3
- `C15`: Add neighbor relationship between 3253965_4 and 3269183_1
- `C16`: Increase transmission power for 3269183_1
- `C17`: Adjust the azimuth of 3278292_3 by 50 degrees
- `C18`: Lift the tilt angle of 3278292_3 by 10 degrees
- `C19`: Add neighbor relationship between 3278292_3 and 3269183_1
- `C20`: Increase A3 Offset threshold for 3269183_1
- `C21`: Decrease A3 Offset threshold for 3269183_1
- `C22`: Press down the tilt angle of 3278292_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.657 | MS1 | 121.4656627332 | 31.1446293408 | 149 | 504990 | -87.42 | 17.79 | 590.94 | 0.01 | 2.55 | 1583 |
| 2024-09-20 22:21:32.768 | MS1 | 121.4656657471 | 31.1446256677 | 149 | 504990 | -85.68 | 13.68 | 520.45 | 0.08 | 2.02 | 1584 |
| 2024-09-20 22:21:33.583 | MS1 | 121.4656620464 | 31.1446201629 | 149 | 504990 | -87.36 | 17.90 | 331.75 | 0.11 | 2.42 | 1562 |
| 2024-09-20 22:21:34.383 | MS1 | 121.4656775539 | 31.1446312681 | 149 | 504990 | -86.39 | 16.18 | 45.71 | 0.18 | 2.26 | 343 |
| 2024-09-20 22:21:35.440 | MS1 | 121.4656591556 | 31.1446317819 | 149 | 504990 | -86.28 | 17.18 | 69.49 | 0.02 | 2.72 | 303 |
| 2024-09-20 22:21:36.566 | MS1 | 121.4656716622 | 31.1446338659 | 149 | 504990 | -87.60 | 17.85 | 76.11 | 0.14 | 2.91 | 312 |
| 2024-09-20 22:21:37.683 | MS1 | 121.4656615953 | 31.1446276144 | 149 | 504990 | -90.77 | 8.14 | 46.94 | 0.18 | 2.10 | 470 |
| 2024-09-20 22:21:38.867 | MS1 | 121.4656670124 | 31.1446293495 | 149 | 504990 | -89.04 | 12.86 | 58.76 | 0.18 | 2.63 | 463 |
| 2024-09-20 22:21:39.549 | MS1 | 121.4656760537 | 31.1446243920 | 149 | 504990 | -89.79 | 9.13 | 40.77 | 0.17 | 2.30 | 494 |
| 2024-09-20 22:21:40.429 | MS1 | 121.4656712471 | 31.1446372208 | 149 | 504990 | -91.02 | 9.17 | 400.08 | 0.11 | 2.37 | 1573 |
| 2024-09-20 22:21:41.700 | MS1 | 121.4656634926 | 31.1446251118 | 149 | 504990 | -93.89 | 9.10 | 449.67 | 0.07 | 2.09 | 1581 |
| 2024-09-20 22:21:42.988 | MS1 | 121.4656736555 | 31.1446276869 | 149 | 504990 | -92.07 | 10.60 | 476.50 | 0.17 | 2.43 | 1583 |

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
| 3253965 | 4 | 121.4698261236 | 31.1459758769 | 311 | 2 | 5 | 16.8 | TDD | 405 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3269183 | 1 | 121.4681285138 | 31.1456298275 | 180 | 1 | 11 | 48.3 | TDD | 282 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3278292 | 3 | 121.4712913303 | 31.1481998650 | 77 | 7 | 8 | 38.1 | TDD | 149 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3279007 | 2 | 121.4677186640 | 31.1512366039 | 167 | 1 | 2 | 42.9 | TDD | 236 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.954 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.979 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.118 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.118 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.798 | NREventA3 | measId:2;ServCellPCI:610;Se... |
| 2024-09-20 22:21:38.038 | NRHandoverAttempt | SourcePCI:610;SourceNR-ARFC... |
| 2024-09-20 22:21:38.073 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.086 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.186 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.186 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269183 | 1 | 14.2825 | 15.6175 | -116.8653 | 18.5540 | 159.6436 | 0.0153 | 0.0115 |
| 2024_09_20 22:00 | 3279007 | 2 | 10.8928 | 11.0551 | -117.4077 | 17.2582 | 176.1405 | 0.0040 | 0.0082 |
| 2024_09_20 22:00 | 3278292 | 3 | 19.1296 | 16.4228 | -116.7212 | 11.6700 | 83.4687 | 0.0101 | 0.0022 |
| 2024_09_20 22:00 | 3253965 | 4 | 9.8870 | 17.9660 | -114.3181 | 18.4071 | 147.8867 | 0.0033 | 0.0044 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413874_24EC4246 | 504990 | 149 | -84.5 | 504990 | 282 | -92.7 | 504990 | 405 | -95.2 | 504990 | 236 |
| MR_1774413874_4B56EFBC | 504990 | 149 | -87.6 | 504990 | 282 | -92.8 | 504990 | 405 | -98.2 | 504990 | 236 |
| MR_1774413874_8EDC80E8 | 504990 | 149 | -88.2 | 504990 | 282 | -93.8 | 504990 | 405 | -94.9 | 504990 | 236 |
| MR_1774413874_F7FD1453 | 504990 | 149 | -87.7 | 504990 | 282 | -95.2 | 504990 | 405 | -97.9 | 504990 | 236 |
| MR_1774413874_E92AB3F6 | 504990 | 149 | -86.3 | 504990 | 282 | -94.7 | 504990 | 405 | -94.9 | 504990 | 236 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 62: `37babafe-bf9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `37babafe-bf9f-448e-b9d4-09a8b8025352` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[62] topology](images/test_0062.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Adjust the azimuth of 3237035_3 by 50 degrees
- `C3`: Decrease A3 Offset threshold for 3279491_1
- `C4`: Press down the tilt angle of 3279491_1 by 8 degrees
- `C5`: Increase A3 Offset threshold for 3279491_1
- `C6`: Check test server and transmission issues
- `C7`: Increase transmission power for 3279491_1
- `C8`: Decrease transmission power for 3237035_3
- `C9`: Decrease transmission power for 3279491_1
- `C10`: Press down the tilt angle  of 3237035_3 by 10 degrees
- `C11`: Add neighbor relationship between 3229579_2 and 3237035_3
- `C12`: Lift the tilt angle of 3279491_1 by 8 degrees
- `C13`: Adjust the azimuth of 3279491_1 by 50 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237035_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279491_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279491_1
- `C17`: Decrease A3 Offset threshold for 3237035_3
- `C18`: Add neighbor relationship between 3279491_1 and 3237035_3
- `C19`: Increase A3 Offset threshold for 3237035_3
- `C20`: Increase transmission power for 3237035_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237035_3
- `C22`: Lift the tilt angle  of 3237035_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.687 | MS1 | 121.4656589580 | 31.1446197567 | 48 | 504990 | -78.68 | 16.52 | 532.21 | 0.15 | 2.77 | 1599 |
| 2024-09-20 22:21:32.670 | MS1 | 121.4656625576 | 31.1446248710 | 48 | 504990 | -81.48 | 15.07 | 374.79 | 0.07 | 2.12 | 1573 |
| 2024-09-20 22:21:33.636 | MS1 | 121.4656722182 | 31.1446221099 | 48 | 504990 | -83.59 | 16.21 | 476.43 | 0.13 | 2.35 | 1575 |
| 2024-09-20 22:21:34.947 | MS1 | 121.4656597876 | 31.1446349057 | 48 | 504990 | -89.88 | -2.63 | 40.93 | 0.05 | 1.32 | 1579 |
| 2024-09-20 22:21:35.253 | MS1 | 121.4656657739 | 31.1446251951 | 48 | 504990 | -84.81 | -2.50 | 37.31 | 0.06 | 1.35 | 1586 |
| 2024-09-20 22:21:36.353 | MS1 | 121.4656683310 | 31.1446279977 | 48 | 504990 | -86.61 | -3.92 | 70.00 | 0.04 | 1.01 | 1571 |
| 2024-09-20 22:21:37.328 | MS1 | 121.4656597914 | 31.1446272018 | 48 | 504990 | -86.06 | -0.69 | 58.50 | 0.17 | 1.24 | 1566 |
| 2024-09-20 22:21:38.257 | MS1 | 121.4656689365 | 31.1446341347 | 48 | 504990 | -85.87 | -1.43 | 52.44 | 0.07 | 1.36 | 1595 |
| 2024-09-20 22:21:39.287 | MS1 | 121.4656747375 | 31.1446238234 | 676 | 504990 | -83.64 | 16.10 | 271.77 | 0.08 | 1.44 | 1585 |
| 2024-09-20 22:21:40.381 | MS1 | 121.4656751141 | 31.1446187730 | 676 | 504990 | -76.46 | 13.32 | 361.79 | 0.09 | 2.93 | 1594 |
| 2024-09-20 22:21:41.551 | MS1 | 121.4656638503 | 31.1446363621 | 676 | 504990 | -84.85 | 16.96 | 344.09 | 0.01 | 2.60 | 1583 |
| 2024-09-20 22:21:42.576 | MS1 | 121.4656590935 | 31.1446256334 | 676 | 504990 | -83.41 | 16.71 | 487.53 | 0.05 | 2.77 | 1575 |

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
| 3229579 | 2 | 121.4706300011 | 31.1530308348 | 62 | 8 | 1 | 21.2 | TDD | 1000 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3237035 | 3 | 121.4689987855 | 31.1507909665 | 298 | 15 | 2 | 23.1 | TDD | 676 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3266530 | 4 | 121.4718367960 | 31.1527696415 | 84 | 8 | 1 | 24.9 | TDD | 140 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3279491 | 1 | 121.4660075532 | 31.1555462835 | 35 | 6 | 7 | 48.1 | TDD | 48 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.268 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.392 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.392 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.130 | NREventA3 | measId:2;ServCellPCI:327;Se... |
| 2024-09-20 22:21:38.370 | NRHandoverAttempt | SourcePCI:327;SourceNR-ARFC... |
| 2024-09-20 22:21:38.400 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.415 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.527 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.527 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279491 | 1 | 15.9237 | 12.2143 | -117.8737 | 17.3225 | 128.2632 | 0.0084 | 0.1348 |
| 2024_09_20 22:00 | 3229579 | 2 | 8.4467 | 15.8705 | -116.6642 | 14.7934 | 85.9612 | 0.0014 | 0.0168 |
| 2024_09_20 22:00 | 3237035 | 3 | 12.5524 | 12.1463 | -116.0835 | 17.7917 | 165.3930 | 0.0158 | 0.0092 |
| 2024_09_20 22:00 | 3266530 | 4 | 10.6824 | 19.7171 | -117.8568 | 7.3796 | 150.5038 | 0.0072 | 0.0165 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413307_0036F589 | 504990 | 48 | -90.9 | 504990 | 676 | -85.8 | 504990 | 1000 | -91.4 | 504990 | 140 |
| MR_1774413307_518DC00E | 504990 | 48 | -89.9 | 504990 | 676 | -86.7 | 504990 | 1000 | -88.6 | 504990 | 140 |
| MR_1774413307_61C74434 | 504990 | 676 | -85.2 | 504990 | 48 | -89.1 | 504990 | 1000 | -89.9 | 504990 | 140 |
| MR_1774413307_79C3B9C5 | 504990 | 48 | -90.6 | 504990 | 676 | -87.1 | 504990 | 1000 | -91.3 | 504990 | 140 |
| MR_1774413307_D500D4E3 | 504990 | 48 | -89.9 | 504990 | 676 | -87.0 | 504990 | 1000 | -88.8 | 504990 | 140 |
| MR_1774413307_1C4D32B2 | 504990 | 48 | -89.7 | 504990 | 676 | -83.6 | 504990 | 1000 | -92.0 | 504990 | 140 |
| MR_1774413307_62EE7EE3 | 504990 | 48 | -88.7 | 504990 | 676 | -87.2 | 504990 | 1000 | -88.8 | 504990 | 140 |
| MR_1774413307_D15306FF | 504990 | 48 | -90.5 | 504990 | 676 | -84.0 | 504990 | 1000 | -91.8 | 504990 | 140 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 63: `78ff9e6c-ae8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `78ff9e6c-ae81-44f8-b0dd-dc2ecc9c8afe` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[63] topology](images/test_0063.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3241285_2
- `C2`: Press down the tilt angle of 3241285_2 by 10 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241285_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Add neighbor relationship between 3221178_4 and 3241880_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241880_3
- `C7`: Increase A3 Offset threshold for 3241880_3
- `C8`: Increase transmission power for 3241880_3
- `C9`: Lift the tilt angle of 3241285_2 by 10 degrees
- `C10`: Decrease transmission power for 3241880_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241880_3
- `C12`: Press down the tilt angle  of 3241880_3 by 3 degrees
- `C13`: Decrease transmission power for 3241285_2
- `C14`: Check test server and transmission issues
- `C15`: Decrease A3 Offset threshold for 3241880_3
- `C16`: Decrease A3 Offset threshold for 3241285_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241285_2
- `C18`: Adjust the azimuth of 3241285_2 by 50 degrees
- `C19`: Add neighbor relationship between 3241285_2 and 3241880_3
- `C20`: Lift the tilt angle  of 3241880_3 by 3 degrees
- `C21`: Increase transmission power for 3241285_2
- `C22`: Adjust the azimuth of 3241880_3 by 15 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.789 | MS1 | 121.4656723706 | 31.1446205090 | 948 | 504990 | -85.13 | 13.07 | 500.21 | 0.16 | 2.30 | 1570 |
| 2024-09-20 22:21:32.690 | MS1 | 121.4656672552 | 31.1446297925 | 948 | 504990 | -93.66 | 16.14 | 431.22 | 0.16 | 2.57 | 1598 |
| 2024-09-20 22:21:33.139 | MS1 | 121.4656642544 | 31.1446185433 | 948 | 504990 | -93.26 | 13.06 | 591.77 | 0.13 | 2.80 | 1566 |
| 2024-09-20 22:21:34.249 | MS1 | 121.4656777034 | 31.1446205202 | 948 | 504990 | -103.18 | 1.37 | 40.99 | 0.11 | 1.34 | 1575 |
| 2024-09-20 22:21:35.557 | MS1 | 121.4656730612 | 31.1446226257 | 948 | 504990 | -107.58 | 1.75 | 23.72 | 0.13 | 1.23 | 1585 |
| 2024-09-20 22:21:36.242 | MS1 | 121.4656655232 | 31.1446196223 | 948 | 504990 | -104.98 | -0.68 | 36.11 | 0.18 | 1.09 | 1594 |
| 2024-09-20 22:21:37.977 | MS1 | 121.4656582133 | 31.1446236208 | 948 | 504990 | -103.82 | -0.35 | 45.07 | 0.14 | 1.49 | 1580 |
| 2024-09-20 22:21:38.301 | MS1 | 121.4656674181 | 31.1446320590 | 948 | 504990 | -101.18 | 1.20 | 30.35 | 0.00 | 1.05 | 1585 |
| 2024-09-20 22:21:39.577 | MS1 | 121.4656699143 | 31.1446230480 | 948 | 504990 | -101.91 | -0.23 | 36.61 | 0.03 | 1.19 | 1599 |
| 2024-09-20 22:21:40.667 | MS1 | 121.4656604262 | 31.1446223454 | 948 | 504990 | -90.39 | 13.91 | 329.17 | 0.10 | 2.33 | 1588 |
| 2024-09-20 22:21:41.358 | MS1 | 121.4656686760 | 31.1446364662 | 948 | 504990 | -85.13 | 17.26 | 430.00 | 0.11 | 2.22 | 1577 |
| 2024-09-20 22:21:42.769 | MS1 | 121.4656639290 | 31.1446189262 | 948 | 504990 | -91.66 | 17.43 | 507.92 | 0.17 | 2.38 | 1581 |

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
| 3221178 | 4 | 121.4738190685 | 31.1463083046 | 192 | 1 | 12 | 28.5 | TDD | 871 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3241285 | 2 | 121.4710928413 | 31.1444929872 | 202 | 7 | 0 | 33.4 | TDD | 948 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3241880 | 3 | 121.4748624550 | 31.1559874793 | 200 | 1 | 4 | 48.8 | TDD | 13 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3267326 | 1 | 121.4721179310 | 31.1558611333 | 129 | 4 | 3 | 22.5 | TDD | 530 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.064 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.178 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.178 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.438 | NREventA2 | measId:1;ServCellPCI:690;Se... |
| 2024-09-20 22:21:34.561 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267326 | 1 | 8.2149 | 5.2347 | -115.0720 | 10.5077 | 99.1945 | 0.0056 | 0.0023 |
| 2024_09_20 22:00 | 3241285 | 2 | 14.3590 | 6.8875 | -114.4113 | 5.6600 | 174.6122 | 0.1888 | 0.0077 |
| 2024_09_20 22:00 | 3241880 | 3 | 16.1846 | 11.4791 | -117.5007 | 6.4758 | 131.8091 | 0.0009 | 0.0021 |
| 2024_09_20 22:00 | 3221178 | 4 | 14.1517 | 15.1857 | -115.3921 | 9.4550 | 174.4741 | 0.0017 | 0.0015 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416981_2FBB75F5 | 504990 | 948 | -102.9 | 504990 | 13 | -109.6 | 504990 | 871 | -115.5 | 504990 | 530 |
| MR_1774416981_1723D353 | 504990 | 948 | -103.7 | 504990 | 13 | -111.9 | 504990 | 871 | -118.1 | 504990 | 530 |
| MR_1774416981_3B7BD313 | 504990 | 948 | -102.4 | 504990 | 13 | -111.6 | 504990 | 871 | -116.9 | 504990 | 530 |
| MR_1774416981_0FD0514C | 504990 | 948 | -101.8 | 504990 | 13 | -108.3 | 504990 | 871 | -116.6 | 504990 | 530 |
| MR_1774416981_D060FA6B | 504990 | 948 | -101.7 | 504990 | 13 | -110.4 | 504990 | 871 | -115.0 | 504990 | 530 |
| MR_1774416981_C4E6E315 | 504990 | 948 | -104.5 | 504990 | 13 | -110.2 | 504990 | 871 | -117.2 | 504990 | 530 |
| MR_1774416981_3DE745E8 | 504990 | 948 | -104.8 | 504990 | 13 | -111.6 | 504990 | 871 | -114.9 | 504990 | 530 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 64: `7db4595e-509...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7db4595e-509b-4947-b1f8-070dc7690da4` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[64] topology](images/test_0064.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3221296_5 by 10 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248168_4
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Lift the tilt angle  of 3248168_4 by 3 degrees
- `C5`: Add neighbor relationship between 3227931_8 and 3248168_4
- `C6`: Adjust the azimuth of 3248168_4 by 31 degrees
- `C7`: Increase A3 Offset threshold for 3221296_5
- `C8`: Press down the tilt angle of 3221296_5 by 3 degrees
- `C9`: Decrease transmission power for 3221296_5
- `C10`: Decrease transmission power for 3248168_4
- `C11`: Check test server and transmission issues
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221296_5
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221296_5
- `C14`: Decrease A3 Offset threshold for 3221296_5
- `C15`: Lift the tilt angle of 3221296_5 by 3 degrees
- `C16`: Add neighbor relationship between 3221296_5 and 3248168_4
- `C17`: Press down the tilt angle  of 3248168_4 by 3 degrees
- `C18`: Increase A3 Offset threshold for 3248168_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248168_4
- `C20`: Increase transmission power for 3248168_4
- `C21`: Increase transmission power for 3221296_5
- `C22`: Decrease A3 Offset threshold for 3248168_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.450 | MS1 | 121.4656763544 | 31.1446202248 | 54 | 504990 | -95.29 | 9.62 | 497.68 | 0.13 | 2.80 | 1598 |
| 2024-09-20 22:21:32.535 | MS1 | 121.4656679031 | 31.1446322791 | 258 | 504990 | -95.65 | 12.35 | 560.92 | 0.10 | 2.10 | 1562 |
| 2024-09-20 22:21:33.228 | MS1 | 121.4656666344 | 31.1446239426 | 445 | 504990 | -94.14 | 9.65 | 302.75 | 0.08 | 2.96 | 1568 |
| 2024-09-20 22:21:34.362 | MS1 | 121.4656620630 | 31.1446200795 | 44 | 152650 | -95.96 | 5.04 | 59.34 | 0.09 | 1.93 | 927 |
| 2024-09-20 22:21:35.934 | MS1 | 121.4656777759 | 31.1446289220 | 623 | 152650 | -92.71 | 3.46 | 73.79 | 0.13 | 1.69 | 931 |
| 2024-09-20 22:21:36.852 | MS1 | 121.4656748415 | 31.1446325513 | 550 | 152650 | -92.40 | 2.87 | 75.61 | 0.12 | 1.58 | 950 |
| 2024-09-20 22:21:37.856 | MS1 | 121.4656721881 | 31.1446361938 | 198 | 152650 | -89.77 | 2.05 | 66.52 | 0.13 | 1.83 | 955 |
| 2024-09-20 22:21:38.576 | MS1 | 121.4656616044 | 31.1446346337 | 44 | 152650 | -95.65 | 7.72 | 85.14 | 0.14 | 1.69 | 973 |
| 2024-09-20 22:21:39.290 | MS1 | 121.4656687435 | 31.1446278245 | 623 | 152650 | -95.74 | 3.43 | 72.11 | 0.08 | 1.82 | 964 |
| 2024-09-20 22:21:40.908 | MS1 | 121.4656777684 | 31.1446370180 | 550 | 152650 | -90.77 | 4.86 | 61.60 | 0.16 | 2.34 | 1596 |
| 2024-09-20 22:21:41.210 | MS1 | 121.4656745038 | 31.1446247917 | 198 | 152650 | -91.45 | 4.96 | 54.38 | 0.12 | 2.49 | 1562 |
| 2024-09-20 22:21:42.922 | MS1 | 121.4656637589 | 31.1446188206 | 44 | 152650 | -89.33 | 6.22 | 80.68 | 0.16 | 2.06 | 1591 |

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
| 3221296 | 5 | 121.4698247782 | 31.1539914021 | 211 | 3 | 4 | 3.9 | TDD | 54 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3226281 | 7 | 121.4667572710 | 31.1492619292 | 177 | 11 | 4 | 21.7 | FDD | 198 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3227931 | 8 | 121.4740752724 | 31.1476308952 | 353 | 10 | 1 | 19.7 | FDD | 550 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3228141 | 9 | 121.4654690235 | 31.1513186840 | 82 | 2 | 1 | 20.4 | FDD | 105 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3230884 | 6 | 121.4698226766 | 31.1498730082 | 6 | 2 | 9 | 4.8 | TDD | 445 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3239104 | 2 | 121.4685591820 | 31.1521196040 | 332 | 0 | 9 | 0.3 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3248065 | 11 | 121.4751722409 | 31.1509443220 | 169 | 9 | 5 | 22.2 | FDD | 623 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3248168 | 4 | 121.4694563451 | 31.1492356708 | 246 | 2 | 5 | 12.5 | TDD | 236 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3248732 | 3 | 121.4714631888 | 31.1498761640 | 356 | 6 | 12 | 21.3 | TDD | 2 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3255500 | 1 | 121.4740559402 | 31.1444749689 | 38 | 0 | 9 | 10.2 | TDD | 865 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3262653 | 12 | 121.4732579993 | 31.1554458173 | 297 | 1 | 3 | 5.3 | FDD | 18 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3266539 | 13 | 121.4654983807 | 31.1472361247 | 246 | 11 | 7 | 27.1 | FDD | 180 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3278188 | 10 | 121.4707754251 | 31.1540125489 | 19 | 10 | 1 | 2.1 | FDD | 44 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |

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
| 2024-09-20 22:21:31.654 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.675 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.808 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.808 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.486 | NREventA2 | measId:1;ServCellPCI:501;Se... |
| 2024-09-20 22:21:35.622 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.908 | NREventA5 | measId:3;ServCellPCI:501;Se... |
| 2024-09-20 22:21:35.986 | NRHandoverAttempt | SourcePCI:501;SourceNR-ARFC... |
| 2024-09-20 22:21:36.008 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.021 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.129 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.129 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255500 | 1 | 17.9727 | 14.0422 | -115.0077 | 17.6318 | 89.3599 | 0.0154 | 0.0088 |
| 2024_09_20 22:00 | 3239104 | 2 | 19.6095 | 14.2267 | -117.1724 | 15.9134 | 87.6097 | 0.0180 | 0.0123 |
| 2024_09_20 22:00 | 3248732 | 3 | 8.8489 | 8.5263 | -114.0585 | 14.3609 | 198.8158 | 0.0165 | 0.0040 |
| 2024_09_20 22:00 | 3248168 | 4 | 8.8681 | 19.9406 | -117.0504 | 5.7696 | 149.4414 | 0.0013 | 0.0015 |
| 2024_09_20 22:00 | 3221296 | 5 | 7.0336 | 6.8532 | -115.7798 | 18.4555 | 137.9029 | 0.0126 | 0.0006 |
| 2024_09_20 22:00 | 3230884 | 6 | 17.5038 | 17.5242 | -117.9811 | 6.9851 | 161.1711 | 0.0079 | 0.0093 |
| 2024_09_20 22:00 | 3226281 | 7 | 11.9708 | 17.5548 | -114.4209 | 4.9813 | 44.5361 | 0.0186 | 0.0044 |
| 2024_09_20 22:00 | 3227931 | 8 | 7.2323 | 8.9150 | -117.4530 | 3.1637 | 33.5772 | 0.0181 | 0.0002 |
| 2024_09_20 22:00 | 3228141 | 9 | 6.8152 | 18.6199 | -114.1438 | 4.0824 | 32.1821 | 0.0188 | 0.0157 |
| 2024_09_20 22:00 | 3278188 | 10 | 14.3777 | 12.9814 | -115.2901 | 4.9543 | 36.8645 | 0.0039 | 0.0196 |
| 2024_09_20 22:00 | 3248065 | 11 | 19.6129 | 18.1966 | -114.5342 | 3.0769 | 33.6528 | 0.0182 | 0.0155 |
| 2024_09_20 22:00 | 3262653 | 12 | 6.4817 | 18.9998 | -116.1286 | 4.9963 | 49.3170 | 0.0039 | 0.0129 |
| 2024_09_20 22:00 | 3266539 | 13 | 13.8458 | 10.0154 | -114.9249 | 3.8025 | 43.0409 | 0.0066 | 0.0170 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413519_80E55597 | 152650 | 44 | -95.5 | 152650 | 180 | -104.8 | 152650 | 105 | -106.6 | 152650 | 18 |
| MR_1774413519_B7B2AF9C | 152650 | 44 | -96.9 | 152650 | 180 | -103.5 | 152650 | 105 | -103.2 | 152650 | 18 |
| MR_1774413519_DA08DEF7 | 504990 | 445 | -93.4 | 504990 | 236 | -93.7 | 504990 | 865 | -100.0 | 504990 | 2 |
| MR_1774413519_4699B932 | 152650 | 44 | -94.0 | 152650 | 180 | -104.5 | 152650 | 105 | -105.1 | 152650 | 18 |
| MR_1774413519_E3867709 | 504990 | 445 | -94.8 | 504990 | 236 | -92.3 | 504990 | 865 | -99.8 | 504990 | 2 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 65: `06dde601-83f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `06dde601-83f3-4aba-a2e4-b73d1fa430bc` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[65] topology](images/test_0065.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3215602_3
- `C2`: Adjust the azimuth of 3254782_1 by 50 degrees
- `C3`: Adjust the azimuth of 3215602_3 by 50 degrees
- `C4`: Check test server and transmission issues
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254782_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215602_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254782_1
- `C8`: Increase transmission power for 3254782_1
- `C9`: Increase A3 Offset threshold for 3254782_1
- `C10`: Add neighbor relationship between 3274117_2 and 3254782_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Add neighbor relationship between 3215602_3 and 3254782_1
- `C13`: Decrease transmission power for 3215602_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215602_3
- `C15`: Decrease A3 Offset threshold for 3254782_1
- `C16`: Press down the tilt angle of 3215602_3 by 6 degrees
- `C17`: Increase transmission power for 3215602_3
- `C18`: Lift the tilt angle  of 3254782_1 by 9 degrees
- `C19`: Decrease A3 Offset threshold for 3215602_3
- `C20`: Decrease transmission power for 3254782_1
- `C21`: Press down the tilt angle  of 3254782_1 by 9 degrees
- `C22`: Lift the tilt angle of 3215602_3 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.234 | MS1 | 121.4656606031 | 31.1446357864 | 804 | 504990 | -86.58 | 14.89 | 403.44 | 0.08 | 2.27 | 1575 |
| 2024-09-20 22:21:32.444 | MS1 | 121.4656627811 | 31.1446367536 | 804 | 504990 | -90.18 | 13.67 | 507.91 | 0.13 | 2.40 | 1572 |
| 2024-09-20 22:21:33.732 | MS1 | 121.4656649822 | 31.1446242893 | 804 | 504990 | -90.57 | 15.35 | 491.24 | 0.15 | 2.90 | 1577 |
| 2024-09-20 22:21:34.990 | MS1 | 121.4656613688 | 31.1446330192 | 804 | 504990 | -88.42 | 14.94 | 95.87 | 0.11 | 2.03 | 1560 |
| 2024-09-20 22:21:35.228 | MS1 | 121.4656692056 | 31.1446349128 | 804 | 504990 | -85.45 | 12.13 | 69.47 | 0.02 | 2.46 | 1591 |
| 2024-09-20 22:21:36.898 | MS1 | 121.4656676007 | 31.1446356015 | 804 | 504990 | -86.02 | 13.09 | 80.65 | 0.13 | 2.18 | 1572 |
| 2024-09-20 22:21:37.549 | MS1 | 121.4656621365 | 31.1446303251 | 804 | 504990 | -90.53 | 7.02 | 103.17 | 0.14 | 2.11 | 1591 |
| 2024-09-20 22:21:38.604 | MS1 | 121.4656740441 | 31.1446308788 | 804 | 504990 | -92.95 | 9.23 | 57.38 | 0.07 | 2.04 | 1585 |
| 2024-09-20 22:21:39.607 | MS1 | 121.4656667025 | 31.1446277433 | 804 | 504990 | -93.25 | 8.70 | 62.23 | 0.11 | 2.40 | 1591 |
| 2024-09-20 22:21:40.508 | MS1 | 121.4656732912 | 31.1446313762 | 804 | 504990 | -91.61 | 8.00 | 401.09 | 0.01 | 2.67 | 1593 |
| 2024-09-20 22:21:41.932 | MS1 | 121.4656731574 | 31.1446275950 | 804 | 504990 | -90.63 | 11.47 | 438.04 | 0.14 | 2.79 | 1568 |
| 2024-09-20 22:21:42.143 | MS1 | 121.4656757320 | 31.1446193142 | 804 | 504990 | -92.42 | 12.38 | 477.02 | 0.11 | 2.36 | 1564 |

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
| 3215602 | 3 | 121.4643049904 | 31.1517853579 | 341 | 4 | 0 | 32.5 | TDD | 804 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3252672 | 4 | 121.4662669791 | 31.1508553707 | 3 | 7 | 6 | 19.5 | TDD | 759 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3254782 | 1 | 121.4750281150 | 31.1450461946 | 85 | 7 | 4 | 31.0 | TDD | 690 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3274117 | 2 | 121.4642635494 | 31.1467962122 | 156 | 13 | 2 | 40.7 | TDD | 420 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.353 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.368 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.492 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.492 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.203 | NREventA3 | measId:2;ServCellPCI:541;Se... |
| 2024-09-20 22:21:38.443 | NRHandoverAttempt | SourcePCI:541;SourceNR-ARFC... |
| 2024-09-20 22:21:38.487 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.501 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.602 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.602 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3254782 | 1 | 88.8070 | 80.3275 | -115.6712 | 19.9829 | 113.5273 | 0.0137 | 0.0018 |
| 2024_09_19 22:00 | 3274117 | 2 | 81.6663 | 81.5955 | -116.1721 | 7.5570 | 152.4695 | 0.0163 | 0.0103 |
| 2024_09_19 22:00 | 3215602 | 3 | 87.2357 | 94.0547 | -116.3189 | 10.0384 | 113.6245 | 0.0176 | 0.0183 |
| 2024_09_19 22:00 | 3252672 | 4 | 82.9234 | 92.8405 | -114.7742 | 9.2234 | 161.5539 | 0.0096 | 0.0089 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416608_0361CA7D | 504990 | 804 | -86.8 | 504990 | 690 | -88.9 | 504990 | 420 | -103.0 | 504990 | 759 |
| MR_1774416608_74866FCC | 504990 | 804 | -89.7 | 504990 | 690 | -89.8 | 504990 | 420 | -104.6 | 504990 | 759 |
| MR_1774416608_199B50F0 | 504990 | 804 | -88.4 | 504990 | 690 | -90.7 | 504990 | 420 | -100.7 | 504990 | 759 |
| MR_1774416608_F864AEC6 | 504990 | 804 | -89.8 | 504990 | 690 | -89.0 | 504990 | 420 | -101.1 | 504990 | 759 |
| MR_1774416608_FF3EEC52 | 504990 | 804 | -88.4 | 504990 | 690 | -90.5 | 504990 | 420 | -104.3 | 504990 | 759 |
| MR_1774416608_42F3AC02 | 504990 | 804 | -86.7 | 504990 | 690 | -91.3 | 504990 | 420 | -101.3 | 504990 | 759 |
| MR_1774416608_FBE72EA8 | 504990 | 804 | -90.3 | 504990 | 690 | -90.0 | 504990 | 420 | -102.9 | 504990 | 759 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 66: `e1ca3a6b-32d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e1ca3a6b-32df-4a80-82c8-52a2b9ed7a95` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[66] topology](images/test_0066.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262117_2
- `C2`: Adjust the azimuth of 3262117_2 by 50 degrees
- `C3`: Decrease transmission power for 3262117_2
- `C4`: Decrease A3 Offset threshold for 3262117_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262117_2
- `C6`: Increase transmission power for 3239361_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239361_3
- `C8`: Press down the tilt angle  of 3239361_3 by 6 degrees
- `C9`: Lift the tilt angle of 3262117_2 by 7 degrees
- `C10`: Add neighbor relationship between 3262117_2 and 3239361_3
- `C11`: Adjust the azimuth of 3239361_3 by 46 degrees
- `C12`: Increase A3 Offset threshold for 3262117_2
- `C13`: Check test server and transmission issues
- `C14`: Increase transmission power for 3262117_2
- `C15`: Decrease transmission power for 3239361_3
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase A3 Offset threshold for 3239361_3
- `C18`: Lift the tilt angle  of 3239361_3 by 6 degrees
- `C19`: Press down the tilt angle of 3262117_2 by 7 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239361_3
- `C21`: Decrease A3 Offset threshold for 3239361_3
- `C22`: Add neighbor relationship between 3261195_1 and 3239361_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.363 | MS1 | 121.4656738443 | 31.1446355022 | 869 | 504990 | -90.89 | 15.31 | 351.19 | 0.15 | 2.06 | 1592 |
| 2024-09-20 22:21:32.724 | MS1 | 121.4656734269 | 31.1446185758 | 869 | 504990 | -88.77 | 16.17 | 495.44 | 0.09 | 2.59 | 1590 |
| 2024-09-20 22:21:33.399 | MS1 | 121.4656738232 | 31.1446189253 | 869 | 504990 | -88.77 | 14.66 | 372.85 | 0.03 | 2.50 | 1587 |
| 2024-09-20 22:21:34.833 | MS1 | 121.4656753851 | 31.1446327366 | 869 | 504990 | -106.77 | 0.96 | 49.00 | 0.08 | 1.37 | 1586 |
| 2024-09-20 22:21:35.569 | MS1 | 121.4656660835 | 31.1446207366 | 869 | 504990 | -107.78 | 0.68 | 26.81 | 0.04 | 1.04 | 1567 |
| 2024-09-20 22:21:36.895 | MS1 | 121.4656693177 | 31.1446314704 | 869 | 504990 | -104.69 | 0.60 | 60.05 | 0.07 | 1.25 | 1580 |
| 2024-09-20 22:21:37.648 | MS1 | 121.4656738010 | 31.1446350930 | 869 | 504990 | -100.01 | -0.53 | 50.88 | 0.13 | 1.44 | 1600 |
| 2024-09-20 22:21:38.480 | MS1 | 121.4656648292 | 31.1446297755 | 869 | 504990 | -101.97 | 1.51 | 54.92 | 0.11 | 1.19 | 1571 |
| 2024-09-20 22:21:39.966 | MS1 | 121.4656598726 | 31.1446379338 | 869 | 504990 | -106.24 | 1.58 | 50.50 | 0.03 | 1.03 | 1575 |
| 2024-09-20 22:21:40.125 | MS1 | 121.4656698648 | 31.1446324365 | 869 | 504990 | -91.00 | 13.90 | 575.03 | 0.08 | 2.85 | 1594 |
| 2024-09-20 22:21:41.732 | MS1 | 121.4656735871 | 31.1446202323 | 869 | 504990 | -94.20 | 16.48 | 383.82 | 0.03 | 2.56 | 1579 |
| 2024-09-20 22:21:42.594 | MS1 | 121.4656632531 | 31.1446321101 | 869 | 504990 | -94.90 | 16.47 | 559.06 | 0.16 | 2.91 | 1565 |

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
| 3239361 | 3 | 121.4642366914 | 31.1557910726 | 220 | 5 | 2 | 16.9 | TDD | 987 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3261195 | 1 | 121.4643946413 | 31.1548586065 | 181 | 2 | 10 | 27.6 | TDD | 640 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3262117 | 2 | 121.4699286336 | 31.1451693338 | 208 | 3 | 2 | 28.4 | TDD | 869 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3269689 | 4 | 121.4670297936 | 31.1463314548 | 97 | 11 | 2 | 35.4 | TDD | 893 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.155 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.176 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.283 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.283 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.516 | NREventA2 | measId:1;ServCellPCI:250;Se... |
| 2024-09-20 22:21:34.665 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261195 | 1 | 10.1765 | 5.4786 | -117.2079 | 6.7154 | 102.0067 | 0.0167 | 0.0175 |
| 2024_09_20 22:00 | 3262117 | 2 | 6.8573 | 15.7600 | -114.1109 | 19.7082 | 139.1260 | 0.1837 | 0.0163 |
| 2024_09_20 22:00 | 3239361 | 3 | 19.9743 | 16.2323 | -117.3459 | 14.4131 | 108.1534 | 0.0092 | 0.0001 |
| 2024_09_20 22:00 | 3269689 | 4 | 18.9077 | 19.0229 | -117.4381 | 9.4948 | 105.4393 | 0.0134 | 0.0099 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412961_9E8E460B | 504990 | 869 | -108.0 | 504990 | 987 | -115.9 | 504990 | 640 | -118.6 | 504990 | 893 |
| MR_1774412961_259D0896 | 504990 | 869 | -106.5 | 504990 | 987 | -113.5 | 504990 | 640 | -119.0 | 504990 | 893 |
| MR_1774412961_D6B3AFF4 | 504990 | 869 | -108.3 | 504990 | 987 | -115.4 | 504990 | 640 | -119.2 | 504990 | 893 |
| MR_1774412961_795909D8 | 504990 | 869 | -105.0 | 504990 | 987 | -112.6 | 504990 | 640 | -120.6 | 504990 | 893 |
| MR_1774412961_419FD610 | 504990 | 869 | -106.8 | 504990 | 987 | -115.9 | 504990 | 640 | -120.1 | 504990 | 893 |
| MR_1774412961_B2080208 | 504990 | 869 | -105.9 | 504990 | 987 | -115.6 | 504990 | 640 | -119.0 | 504990 | 893 |
| MR_1774412961_EC57AA8E | 504990 | 869 | -108.1 | 504990 | 987 | -112.8 | 504990 | 640 | -121.3 | 504990 | 893 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 67: `21a770ea-10f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `21a770ea-10f3-4a02-8fb2-e98c2a6798f0` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[67] topology](images/test_0067.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236796_4
- `C3`: Decrease transmission power for 3236796_4
- `C4`: Increase A3 Offset threshold for 3265446_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265446_3
- `C6`: Increase transmission power for 3236796_4
- `C7`: Add neighbor relationship between 3236796_4 and 3265446_3
- `C8`: Decrease transmission power for 3265446_3
- `C9`: Decrease A3 Offset threshold for 3236796_4
- `C10`: Increase A3 Offset threshold for 3236796_4
- `C11`: Press down the tilt angle  of 3265446_3 by 10 degrees
- `C12`: Lift the tilt angle of 3236796_4 by 6 degrees
- `C13`: Adjust the azimuth of 3236796_4 by 20 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265446_3
- `C15`: Decrease A3 Offset threshold for 3265446_3
- `C16`: Increase transmission power for 3265446_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236796_4
- `C18`: Adjust the azimuth of 3265446_3 by 50 degrees
- `C19`: Press down the tilt angle of 3236796_4 by 6 degrees
- `C20`: Add neighbor relationship between 3218655_2 and 3265446_3
- `C21`: Check test server and transmission issues
- `C22`: Lift the tilt angle  of 3265446_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.914 | MS1 | 121.4656622157 | 31.1446240939 | 692 | 504990 | -81.93 | 12.25 | 591.11 | 0.02 | 2.05 | 1592 |
| 2024-09-20 22:21:32.127 | MS1 | 121.4656758683 | 31.1446215995 | 692 | 504990 | -83.36 | 12.11 | 373.22 | 0.05 | 2.22 | 1594 |
| 2024-09-20 22:21:33.897 | MS1 | 121.4656752585 | 31.1446232813 | 692 | 504990 | -82.01 | 13.49 | 465.80 | 0.09 | 2.14 | 1587 |
| 2024-09-20 22:21:34.402 | MS1 | 121.4656660833 | 31.1446310511 | 692 | 504990 | -84.77 | -3.08 | 58.98 | 0.12 | 1.17 | 1584 |
| 2024-09-20 22:21:35.182 | MS1 | 121.4656767518 | 31.1446323790 | 692 | 504990 | -92.07 | -3.06 | 47.25 | 0.02 | 1.32 | 1581 |
| 2024-09-20 22:21:36.773 | MS1 | 121.4656580498 | 31.1446315226 | 692 | 504990 | -91.17 | -0.36 | 72.76 | 0.11 | 1.47 | 1569 |
| 2024-09-20 22:21:37.901 | MS1 | 121.4656628837 | 31.1446305201 | 692 | 504990 | -92.24 | -3.72 | 67.37 | 0.16 | 1.01 | 1587 |
| 2024-09-20 22:21:38.235 | MS1 | 121.4656622654 | 31.1446202429 | 692 | 504990 | -87.81 | -0.26 | 27.50 | 0.07 | 1.49 | 1562 |
| 2024-09-20 22:21:39.311 | MS1 | 121.4656651310 | 31.1446271992 | 385 | 504990 | -80.66 | 16.61 | 289.64 | 0.02 | 1.46 | 1571 |
| 2024-09-20 22:21:40.567 | MS1 | 121.4656623192 | 31.1446321371 | 385 | 504990 | -83.18 | 14.25 | 446.24 | 0.12 | 2.64 | 1576 |
| 2024-09-20 22:21:41.106 | MS1 | 121.4656769055 | 31.1446186027 | 385 | 504990 | -84.68 | 16.95 | 494.05 | 0.12 | 2.26 | 1588 |
| 2024-09-20 22:21:42.388 | MS1 | 121.4656582924 | 31.1446262768 | 385 | 504990 | -82.06 | 15.73 | 392.22 | 0.12 | 2.56 | 1578 |

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
| 3218655 | 2 | 121.4707619590 | 31.1459122531 | 39 | 3 | 6 | 38.0 | TDD | 337 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3236796 | 4 | 121.4751465596 | 31.1497253302 | 258 | 5 | 12 | 20.2 | TDD | 692 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3265446 | 3 | 121.4676954883 | 31.1449569982 | 135 | 4 | 5 | 45.9 | TDD | 385 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3272019 | 1 | 121.4738578200 | 31.1450064265 | 265 | 13 | 11 | 32.0 | TDD | 48 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.407 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.422 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.524 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.524 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.265 | NREventA3 | measId:2;ServCellPCI:923;Se... |
| 2024-09-20 22:21:38.505 | NRHandoverAttempt | SourcePCI:923;SourceNR-ARFC... |
| 2024-09-20 22:21:38.552 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.563 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.702 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.702 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272019 | 1 | 9.8779 | 12.0125 | -114.2159 | 16.8102 | 152.7932 | 0.0096 | 0.0140 |
| 2024_09_20 22:00 | 3218655 | 2 | 12.8156 | 9.5408 | -117.6596 | 15.4670 | 187.3784 | 0.0167 | 0.0145 |
| 2024_09_20 22:00 | 3265446 | 3 | 17.5828 | 17.7563 | -117.1154 | 12.3237 | 92.0696 | 0.0126 | 0.0063 |
| 2024_09_20 22:00 | 3236796 | 4 | 16.0006 | 6.8527 | -114.6504 | 8.2600 | 103.7619 | 0.0116 | 0.1346 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416418_685A8701 | 504990 | 385 | -79.1 | 504990 | 692 | -83.4 | 504990 | 337 | -86.7 | 504990 | 48 |
| MR_1774416418_62DB8D50 | 504990 | 692 | -85.7 | 504990 | 385 | -80.3 | 504990 | 337 | -90.4 | 504990 | 48 |
| MR_1774416418_5E8D76A9 | 504990 | 385 | -81.8 | 504990 | 692 | -83.8 | 504990 | 337 | -86.9 | 504990 | 48 |
| MR_1774416418_C847EBA5 | 504990 | 692 | -86.1 | 504990 | 385 | -81.6 | 504990 | 337 | -87.7 | 504990 | 48 |
| MR_1774416418_683E5B6B | 504990 | 385 | -81.9 | 504990 | 692 | -85.1 | 504990 | 337 | -88.9 | 504990 | 48 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 68: `08a2494c-2a8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `08a2494c-2a8e-46ea-9817-9429ef801f8a` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[68] topology](images/test_0068.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3225897_4 by 50 degrees
- `C2`: Increase transmission power for 3225897_4
- `C3`: Increase transmission power for 3220432_1
- `C4`: Lift the tilt angle  of 3220432_1 by 3 degrees
- `C5`: Decrease transmission power for 3225897_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase A3 Offset threshold for 3225897_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220432_1
- `C9`: Add neighbor relationship between 3278553_2 and 3220432_1
- `C10`: Decrease A3 Offset threshold for 3225897_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220432_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225897_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225897_4
- `C14`: Press down the tilt angle  of 3220432_1 by 3 degrees
- `C15`: Add neighbor relationship between 3225897_4 and 3220432_1
- `C16`: Decrease A3 Offset threshold for 3220432_1
- `C17`: Decrease transmission power for 3220432_1
- `C18`: Lift the tilt angle of 3225897_4 by 6 degrees
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle of 3225897_4 by 6 degrees
- `C21`: Increase A3 Offset threshold for 3220432_1
- `C22`: Adjust the azimuth of 3220432_1 by 44 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.264 | MS1 | 121.4656756579 | 31.1446311604 | 119 | 504990 | -85.97 | 14.51 | 362.86 | 0.04 | 2.62 | 1592 |
| 2024-09-20 22:21:32.902 | MS1 | 121.4656708980 | 31.1446248933 | 119 | 504990 | -91.42 | 15.68 | 343.72 | 0.02 | 2.29 | 1576 |
| 2024-09-20 22:21:33.565 | MS1 | 121.4656652963 | 31.1446366895 | 119 | 504990 | -91.94 | 13.72 | 546.20 | 0.07 | 2.73 | 1590 |
| 2024-09-20 22:21:34.994 | MS1 | 121.4656697835 | 31.1446242283 | 119 | 504990 | -104.36 | 1.04 | 52.36 | 0.01 | 1.32 | 1598 |
| 2024-09-20 22:21:35.679 | MS1 | 121.4656660794 | 31.1446211234 | 119 | 504990 | -103.27 | 0.48 | 29.56 | 0.17 | 1.17 | 1571 |
| 2024-09-20 22:21:36.123 | MS1 | 121.4656678657 | 31.1446248551 | 119 | 504990 | -109.06 | -0.74 | 41.01 | 0.19 | 1.06 | 1560 |
| 2024-09-20 22:21:37.294 | MS1 | 121.4656634514 | 31.1446342511 | 119 | 504990 | -107.72 | -1.79 | 77.07 | 0.12 | 1.26 | 1587 |
| 2024-09-20 22:21:38.927 | MS1 | 121.4656614596 | 31.1446374632 | 119 | 504990 | -107.76 | 0.71 | 54.33 | 0.17 | 1.14 | 1564 |
| 2024-09-20 22:21:39.353 | MS1 | 121.4656586326 | 31.1446239532 | 119 | 504990 | -104.70 | 1.56 | 64.98 | 0.08 | 1.31 | 1587 |
| 2024-09-20 22:21:40.908 | MS1 | 121.4656611690 | 31.1446319911 | 119 | 504990 | -88.53 | 14.71 | 456.55 | 0.12 | 2.68 | 1575 |
| 2024-09-20 22:21:41.813 | MS1 | 121.4656683612 | 31.1446229478 | 119 | 504990 | -92.43 | 13.18 | 473.58 | 0.12 | 2.94 | 1562 |
| 2024-09-20 22:21:42.785 | MS1 | 121.4656580348 | 31.1446185481 | 119 | 504990 | -85.92 | 15.04 | 435.99 | 0.12 | 2.01 | 1595 |

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
| 3220432 | 1 | 121.4656763574 | 31.1553242384 | 224 | 1 | 9 | 35.9 | TDD | 838 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3225897 | 4 | 121.4735796634 | 31.1462313254 | 328 | 4 | 0 | 24.6 | TDD | 119 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3229786 | 3 | 121.4700592695 | 31.1558040689 | 127 | 11 | 6 | 30.3 | TDD | 715 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3278553 | 2 | 121.4691286026 | 31.1458597825 | 231 | 12 | 4 | 39.8 | TDD | 427 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.060 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.075 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.225 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.225 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.378 | NREventA2 | measId:1;ServCellPCI:488;Se... |
| 2024-09-20 22:21:34.512 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220432 | 1 | 12.7701 | 6.5629 | -116.1396 | 9.5032 | 190.9720 | 0.0058 | 0.0125 |
| 2024_09_20 22:00 | 3278553 | 2 | 19.7888 | 19.1739 | -116.2753 | 17.0697 | 169.7839 | 0.0140 | 0.0054 |
| 2024_09_20 22:00 | 3229786 | 3 | 15.7424 | 13.4661 | -114.9454 | 14.4878 | 88.4883 | 0.0061 | 0.0135 |
| 2024_09_20 22:00 | 3225897 | 4 | 8.8049 | 15.3567 | -114.7565 | 16.7668 | 82.1814 | 0.1981 | 0.0176 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415702_347F8854 | 504990 | 119 | -102.4 | 504990 | 838 | -112.0 | 504990 | 427 | -118.2 | 504990 | 715 |
| MR_1774415702_D72A23D7 | 504990 | 119 | -102.9 | 504990 | 838 | -112.4 | 504990 | 427 | -118.5 | 504990 | 715 |
| MR_1774415702_78862CC7 | 504990 | 119 | -105.6 | 504990 | 838 | -111.9 | 504990 | 427 | -116.3 | 504990 | 715 |
| MR_1774415702_67A4AEC8 | 504990 | 119 | -102.9 | 504990 | 838 | -110.4 | 504990 | 427 | -117.3 | 504990 | 715 |
| MR_1774415702_5E23842C | 504990 | 119 | -106.2 | 504990 | 838 | -114.1 | 504990 | 427 | -117.1 | 504990 | 715 |
| MR_1774415702_C323167B | 504990 | 119 | -104.6 | 504990 | 838 | -111.3 | 504990 | 427 | -117.8 | 504990 | 715 |
| MR_1774415702_C533B855 | 504990 | 119 | -102.6 | 504990 | 838 | -112.4 | 504990 | 427 | -119.6 | 504990 | 715 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 69: `83ab9a55-ae4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `83ab9a55-ae4f-44cc-a353-14dbec2e76a0` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[69] topology](images/test_0069.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Press down the tilt angle  of 3266212_1 by 10 degrees
- `C3`: Press down the tilt angle of 3261582_3 by 10 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266212_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266212_1
- `C6`: Add neighbor relationship between 3214884_2 and 3266212_1
- `C7`: Increase transmission power for 3266212_1
- `C8`: Increase transmission power for 3261582_3
- `C9`: Lift the tilt angle of 3261582_3 by 10 degrees
- `C10`: Decrease transmission power for 3266212_1
- `C11`: Decrease A3 Offset threshold for 3261582_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261582_3
- `C13`: Adjust the azimuth of 3266212_1 by 50 degrees
- `C14`: Add neighbor relationship between 3261582_3 and 3266212_1
- `C15`: Increase A3 Offset threshold for 3261582_3
- `C16`: Increase A3 Offset threshold for 3266212_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261582_3
- `C18`: Decrease A3 Offset threshold for 3266212_1
- `C19`: Adjust the azimuth of 3261582_3 by 50 degrees
- `C20`: Lift the tilt angle  of 3266212_1 by 10 degrees
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease transmission power for 3261582_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.337 | MS1 | 121.4656736962 | 31.1446211619 | 358 | 504990 | -91.71 | 12.84 | 585.66 | 0.13 | 2.23 | 1562 |
| 2024-09-20 22:21:32.932 | MS1 | 121.4656616427 | 31.1446317071 | 358 | 504990 | -88.90 | 16.01 | 523.65 | 0.19 | 2.67 | 1583 |
| 2024-09-20 22:21:33.334 | MS1 | 121.4656609176 | 31.1446210579 | 358 | 504990 | -89.90 | 17.60 | 538.58 | 0.13 | 2.95 | 1562 |
| 2024-09-20 22:21:34.150 | MS1 | 121.4656612382 | 31.1446365192 | 358 | 504990 | -88.13 | 16.84 | 84.48 | 0.06 | 2.04 | 339 |
| 2024-09-20 22:21:35.148 | MS1 | 121.4656762237 | 31.1446375530 | 358 | 504990 | -91.53 | 16.18 | 97.27 | 0.14 | 2.80 | 414 |
| 2024-09-20 22:21:36.872 | MS1 | 121.4656649798 | 31.1446360201 | 358 | 504990 | -86.05 | 12.12 | 86.52 | 0.05 | 2.10 | 461 |
| 2024-09-20 22:21:37.944 | MS1 | 121.4656599337 | 31.1446265483 | 358 | 504990 | -90.73 | 12.95 | 81.91 | 0.10 | 2.62 | 388 |
| 2024-09-20 22:21:38.497 | MS1 | 121.4656730750 | 31.1446352619 | 358 | 504990 | -91.56 | 10.69 | 83.58 | 0.05 | 2.72 | 436 |
| 2024-09-20 22:21:39.222 | MS1 | 121.4656701654 | 31.1446355982 | 358 | 504990 | -91.42 | 10.90 | 53.99 | 0.04 | 2.32 | 446 |
| 2024-09-20 22:21:40.673 | MS1 | 121.4656735117 | 31.1446229971 | 358 | 504990 | -89.39 | 12.58 | 429.23 | 0.03 | 3.00 | 1564 |
| 2024-09-20 22:21:41.373 | MS1 | 121.4656746446 | 31.1446237205 | 358 | 504990 | -89.18 | 12.17 | 404.48 | 0.17 | 2.09 | 1597 |
| 2024-09-20 22:21:42.804 | MS1 | 121.4656721301 | 31.1446258912 | 358 | 504990 | -90.44 | 8.77 | 332.38 | 0.18 | 2.21 | 1599 |

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
| 3214884 | 2 | 121.4696091092 | 31.1525153715 | 142 | 1 | 5 | 23.4 | TDD | 442 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3261582 | 3 | 121.4672925908 | 31.1541597603 | 333 | 11 | 6 | 24.4 | TDD | 358 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3264494 | 4 | 121.4668128454 | 31.1487604224 | 14 | 0 | 3 | 41.2 | TDD | 121 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3266212 | 1 | 121.4735138135 | 31.1460613728 | 47 | 14 | 6 | 46.9 | TDD | 777 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.351 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.375 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.487 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.487 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.179 | NREventA3 | measId:2;ServCellPCI:822;Se... |
| 2024-09-20 22:21:38.419 | NRHandoverAttempt | SourcePCI:822;SourceNR-ARFC... |
| 2024-09-20 22:21:38.469 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.484 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.586 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.586 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266212 | 1 | 16.6744 | 17.0518 | -116.6152 | 13.7454 | 185.6909 | 0.0012 | 0.0116 |
| 2024_09_20 22:00 | 3214884 | 2 | 10.4702 | 14.3975 | -114.4226 | 15.7174 | 170.7831 | 0.0097 | 0.0163 |
| 2024_09_20 22:00 | 3261582 | 3 | 15.7074 | 14.6009 | -117.3630 | 9.8396 | 84.8240 | 0.0139 | 0.0170 |
| 2024_09_20 22:00 | 3264494 | 4 | 7.1312 | 10.3385 | -114.1758 | 10.5721 | 88.8109 | 0.0045 | 0.0018 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416169_A3AB5900 | 504990 | 358 | -88.4 | 504990 | 777 | -92.3 | 504990 | 442 | -101.2 | 504990 | 121 |
| MR_1774416169_0EAD27BB | 504990 | 358 | -89.0 | 504990 | 777 | -93.3 | 504990 | 442 | -100.5 | 504990 | 121 |
| MR_1774416169_B8F42B23 | 504990 | 358 | -89.1 | 504990 | 777 | -91.2 | 504990 | 442 | -99.7 | 504990 | 121 |
| MR_1774416169_84714892 | 504990 | 358 | -87.4 | 504990 | 777 | -92.8 | 504990 | 442 | -98.2 | 504990 | 121 |
| MR_1774416169_217E9A6D | 504990 | 358 | -86.3 | 504990 | 777 | -91.8 | 504990 | 442 | -101.0 | 504990 | 121 |
| MR_1774416169_90CD02FB | 504990 | 358 | -88.5 | 504990 | 777 | -90.6 | 504990 | 442 | -100.1 | 504990 | 121 |
| MR_1774416169_67877BD2 | 504990 | 358 | -87.8 | 504990 | 777 | -92.1 | 504990 | 442 | -98.7 | 504990 | 121 |

> *... 2개 열 생략 (전체 14열)*

---
