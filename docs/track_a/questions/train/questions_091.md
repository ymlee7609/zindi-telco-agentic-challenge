# Track A 문제 분석 — train[900]~train[909]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[900] ~ train[909] (10개)

## 목차

1. [문제 900: `20630587-1c8...`](#900) — single-answer, 정답: C5
2. [문제 901: `a6888003-570...`](#901) — single-answer, 정답: C6
3. [문제 902: `d43790c0-6c3...`](#902) — single-answer, 정답: C18
4. [문제 903: `fb815bd5-1ed...`](#903) — single-answer, 정답: C1
5. [문제 904: `63c62e2a-c89...`](#904) — single-answer, 정답: C21
6. [문제 905: `79d78f6d-b45...`](#905) — single-answer, 정답: C17
7. [문제 906: `6383aeb7-76a...`](#906) — single-answer, 정답: C15
8. [문제 907: `b210019c-c3d...`](#907) — single-answer, 정답: C9
9. [문제 908: `d7fb948b-2bc...`](#908) — single-answer, 정답: C21
10. [문제 909: `751a5052-93d...`](#909) — single-answer, 정답: C6

---

### 문제 900: `20630587-1c8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `20630587-1c80-45a9-ae92-5e0a7044ea9c` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[900] topology](images/train_0900.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3242074_1 and 3216837_2
- `C2`: Increase transmission power for 3242074_1
- `C3`: Increase transmission power for 3216837_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242074_1
- `C5`: Insufficient data; more data is needed for judgment. **← 정답**
- `C6`: Press down the tilt angle of 3242074_1 by 9 degrees
- `C7`: Add neighbor relationship between 3246375_3 and 3216837_2
- `C8`: Decrease transmission power for 3242074_1
- `C9`: Adjust the azimuth of 3216837_2 by 50 degrees
- `C10`: Decrease A3 Offset threshold for 3216837_2
- `C11`: Decrease transmission power for 3216837_2
- `C12`: Adjust the azimuth of 3242074_1 by 12 degrees
- `C13`: Press down the tilt angle  of 3216837_2 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216837_2
- `C15`: Check test server and transmission issues
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216837_2
- `C17`: Increase A3 Offset threshold for 3242074_1
- `C18`: Lift the tilt angle  of 3216837_2 by 10 degrees
- `C19`: Lift the tilt angle of 3242074_1 by 9 degrees
- `C20`: Decrease A3 Offset threshold for 3242074_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242074_1
- `C22`: Increase A3 Offset threshold for 3216837_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.854 | MS1 | 121.4656676716 | 31.1446374305 | 225 | 504990 | -89.07 | 13.80 | 451.68 | 0.08 | 2.06 | 1561 |
| 2024-09-20 22:21:32.623 | MS1 | 121.4656706529 | 31.1446370361 | 225 | 504990 | -86.04 | 14.93 | 505.30 | 0.01 | 2.18 | 1595 |
| 2024-09-20 22:21:33.298 | MS1 | 121.4656688412 | 31.1446334489 | 225 | 504990 | -89.63 | 16.62 | 305.17 | 0.09 | 2.58 | 1597 |
| 2024-09-20 22:21:34.420 | MS1 | 121.4656715093 | 31.1446249951 | 225 | 504990 | -88.63 | 17.89 | 104.25 | 0.03 | 2.63 | 1598 |
| 2024-09-20 22:21:35.237 | MS1 | 121.4656738940 | 31.1446232934 | 225 | 504990 | -86.33 | 12.00 | 73.86 | 0.15 | 2.53 | 1587 |
| 2024-09-20 22:21:36.331 | MS1 | 121.4656702557 | 31.1446283752 | 225 | 504990 | -86.55 | 17.09 | 58.13 | 0.11 | 2.59 | 1600 |
| 2024-09-20 22:21:37.464 | MS1 | 121.4656760814 | 31.1446367412 | 225 | 504990 | -92.93 | 10.21 | 99.22 | 0.18 | 2.26 | 1580 |
| 2024-09-20 22:21:38.163 | MS1 | 121.4656587998 | 31.1446243701 | 225 | 504990 | -93.20 | 11.83 | 93.87 | 0.19 | 2.18 | 1583 |
| 2024-09-20 22:21:39.873 | MS1 | 121.4656619144 | 31.1446378467 | 225 | 504990 | -92.41 | 9.31 | 52.34 | 0.15 | 2.76 | 1583 |
| 2024-09-20 22:21:40.877 | MS1 | 121.4656617755 | 31.1446342366 | 225 | 504990 | -90.87 | 7.33 | 432.40 | 0.14 | 2.26 | 1575 |
| 2024-09-20 22:21:41.899 | MS1 | 121.4656699061 | 31.1446213578 | 225 | 504990 | -89.84 | 12.77 | 312.02 | 0.06 | 2.25 | 1571 |
| 2024-09-20 22:21:42.847 | MS1 | 121.4656602489 | 31.1446282419 | 225 | 504990 | -93.44 | 9.78 | 334.05 | 0.01 | 2.09 | 1600 |

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
| 3216837 | 2 | 121.4691293273 | 31.1473781936 | 68 | 9 | 10 | 26.7 | TDD | 333 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3234925 | 4 | 121.4738288428 | 31.1540555092 | 326 | 12 | 8 | 15.2 | TDD | 399 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3242074 | 1 | 121.4689308221 | 31.1493461172 | 223 | 5 | 10 | 40.1 | TDD | 225 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3246375 | 3 | 121.4663828934 | 31.1481821593 | 144 | 10 | 9 | 15.9 | TDD | 233 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.511 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.527 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.634 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.634 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.362 | NREventA3 | measId:2;ServCellPCI:343;Se... |
| 2024-09-20 22:21:38.602 | NRHandoverAttempt | SourcePCI:343;SourceNR-ARFC... |
| 2024-09-20 22:21:38.635 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.646 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.770 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.770 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3242074 | 1 | 85.3820 | 76.0699 | -114.3894 | 17.8570 | 151.7244 | 0.0039 | 0.0018 |
| 2024_09_19 22:00 | 3216837 | 2 | 82.5431 | 80.9478 | -114.1198 | 7.6256 | 125.8147 | 0.0101 | 0.0000 |
| 2024_09_19 22:00 | 3246375 | 3 | 81.2726 | 76.5885 | -116.1838 | 14.6525 | 133.2654 | 0.0147 | 0.0005 |
| 2024_09_19 22:00 | 3234925 | 4 | 82.5564 | 80.1217 | -117.1370 | 18.4569 | 151.9939 | 0.0033 | 0.0128 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415789_EBF3D4D1 | 504990 | 225 | -85.6 | 504990 | 333 | -87.4 | 504990 | 233 | -94.7 | 504990 | 399 |
| MR_1774415789_37B2BC1E | 504990 | 225 | -87.9 | 504990 | 333 | -90.5 | 504990 | 233 | -93.7 | 504990 | 399 |
| MR_1774415789_5ACBD1A7 | 504990 | 225 | -87.3 | 504990 | 333 | -87.0 | 504990 | 233 | -93.0 | 504990 | 399 |
| MR_1774415789_205B172C | 504990 | 225 | -85.4 | 504990 | 333 | -89.3 | 504990 | 233 | -93.5 | 504990 | 399 |
| MR_1774415789_851D13D9 | 504990 | 225 | -87.2 | 504990 | 333 | -88.9 | 504990 | 233 | -93.3 | 504990 | 399 |
| MR_1774415789_E0F645B1 | 504990 | 225 | -84.8 | 504990 | 333 | -88.1 | 504990 | 233 | -94.6 | 504990 | 399 |
| MR_1774415789_BD6CC47F | 504990 | 225 | -86.1 | 504990 | 333 | -89.4 | 504990 | 233 | -95.0 | 504990 | 399 |
| MR_1774415789_24055996 | 504990 | 225 | -86.6 | 504990 | 333 | -86.8 | 504990 | 233 | -92.0 | 504990 | 399 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 901: `a6888003-570...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a6888003-570d-4721-a1c2-5cd3f9dce8e5` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Lift the tilt angle  of 3275791_1 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[901] topology](images/train_0901.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3275791_1 and 3233474_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233474_4
- `C3`: Add neighbor relationship between 3240687_3 and 3233474_4
- `C4`: Press down the tilt angle  of 3275791_1 by 7 degrees
- `C5`: Adjust the azimuth of 3275791_1 by 50 degrees
- `C6`: Lift the tilt angle  of 3275791_1 by 7 degrees **← 정답**
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240687_3
- `C8`: Increase transmission power for 3240687_3
- `C9`: Lift the tilt angle of 3240687_3 by 2 degrees
- `C10`: Decrease A3 Offset threshold for 3233474_4
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase A3 Offset threshold for 3240687_3
- `C13`: Press down the tilt angle of 3240687_3 by 2 degrees
- `C14`: Check test server and transmission issues
- `C15`: Decrease transmission power for 3240687_3
- `C16`: Decrease transmission power for 3233474_4
- `C17`: Increase A3 Offset threshold for 3233474_4
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233474_4
- `C19`: Adjust the azimuth of 3240687_3 by 45 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240687_3
- `C21`: Increase transmission power for 3233474_4
- `C22`: Decrease A3 Offset threshold for 3240687_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.725 | MS1 | 121.4656733987 | 31.1446315359 | 278 | 504990 | -88.41 | 14.29 | 515.06 | 0.05 | 2.77 | 1585 |
| 2024-09-20 22:21:32.207 | MS1 | 121.4656681620 | 31.1446223860 | 278 | 504990 | -88.63 | 17.93 | 595.38 | 0.06 | 2.63 | 1589 |
| 2024-09-20 22:21:33.374 | MS1 | 121.4656604935 | 31.1446335573 | 278 | 504990 | -87.21 | 15.20 | 309.31 | 0.17 | 2.40 | 1570 |
| 2024-09-20 22:21:34.881 | MS1 | 121.4656681981 | 31.1446261177 | 278 | 504990 | -86.11 | 16.26 | 77.53 | 0.03 | 2.94 | 1568 |
| 2024-09-20 22:21:35.694 | MS1 | 121.4656628485 | 31.1446201863 | 278 | 504990 | -90.10 | 15.42 | 74.89 | 0.09 | 2.56 | 1597 |
| 2024-09-20 22:21:36.583 | MS1 | 121.4656726712 | 31.1446334547 | 278 | 504990 | -89.50 | 14.04 | 105.63 | 0.14 | 2.64 | 1583 |
| 2024-09-20 22:21:37.981 | MS1 | 121.4656686869 | 31.1446370557 | 278 | 504990 | -93.82 | 9.70 | 82.81 | 0.09 | 2.49 | 1578 |
| 2024-09-20 22:21:38.552 | MS1 | 121.4656779724 | 31.1446352364 | 278 | 504990 | -93.02 | 9.61 | 79.49 | 0.11 | 2.27 | 1595 |
| 2024-09-20 22:21:39.109 | MS1 | 121.4656728637 | 31.1446194620 | 278 | 504990 | -93.10 | 12.43 | 61.19 | 0.10 | 2.93 | 1563 |
| 2024-09-20 22:21:40.364 | MS1 | 121.4656588985 | 31.1446269291 | 278 | 504990 | -91.12 | 12.31 | 383.91 | 0.10 | 2.36 | 1592 |
| 2024-09-20 22:21:41.714 | MS1 | 121.4656669746 | 31.1446190439 | 278 | 504990 | -91.74 | 9.66 | 391.25 | 0.03 | 2.20 | 1585 |
| 2024-09-20 22:21:42.823 | MS1 | 121.4656638554 | 31.1446193503 | 278 | 504990 | -92.65 | 8.75 | 322.73 | 0.00 | 2.97 | 1598 |

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
| 3233474 | 4 | 121.4758642894 | 31.1508650449 | 165 | 6 | 2 | 29.7 | TDD | 383 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3240687 | 3 | 121.4686513455 | 31.1503895789 | 159 | 1 | 8 | 16.0 | TDD | 278 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3242684 | 2 | 121.4685611448 | 31.1505550291 | 309 | 7 | 6 | 22.8 | TDD | 373 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3275791 | 1 | 121.4668511240 | 31.1451662227 | 26 | 12 | 9 | 33.5 | TDD | 541 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.320 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.339 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.486 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.486 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.123 | NREventA3 | measId:2;ServCellPCI:809;Se... |
| 2024-09-20 22:21:38.363 | NRHandoverAttempt | SourcePCI:809;SourceNR-ARFC... |
| 2024-09-20 22:21:38.412 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.426 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.558 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.558 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275791 | 1 | 7.7643 | 15.2948 | -117.1140 | 16.5986 | 107.5550 | 0.0163 | 0.0058 |
| 2024_09_20 22:00 | 3242684 | 2 | 17.5804 | 17.2277 | -115.2848 | 16.5102 | 189.2303 | 0.0009 | 0.0152 |
| 2024_09_20 22:00 | 3240687 | 3 | 79.2942 | 84.6754 | -116.4231 | 9.1746 | 100.7990 | 0.0058 | 0.0113 |
| 2024_09_20 22:00 | 3233474 | 4 | 9.2081 | 12.4571 | -116.3820 | 7.7174 | 167.3928 | 0.0127 | 0.0007 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415717_6C46F3ED | 504990 | 278 | -85.7 | 504990 | 383 | -94.5 | 504990 | 541 | -93.9 | 504990 | 373 |
| MR_1774415717_2921A070 | 504990 | 278 | -84.4 | 504990 | 383 | -91.5 | 504990 | 541 | -94.8 | 504990 | 373 |
| MR_1774415717_BDB55F70 | 504990 | 278 | -88.1 | 504990 | 383 | -93.9 | 504990 | 541 | -94.0 | 504990 | 373 |
| MR_1774415717_909699EE | 504990 | 278 | -87.9 | 504990 | 383 | -93.3 | 504990 | 541 | -94.4 | 504990 | 373 |
| MR_1774415717_8779012F | 504990 | 278 | -87.8 | 504990 | 383 | -94.3 | 504990 | 541 | -94.8 | 504990 | 373 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 902: `d43790c0-6c3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d43790c0-6c35-442a-8dc6-484d676648f9` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[902] topology](images/train_0902.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3225722_3 and 3218306_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246136_2
- `C3`: Decrease A3 Offset threshold for 3218306_1
- `C4`: Decrease transmission power for 3246136_2
- `C5`: Decrease transmission power for 3218306_1
- `C6`: Lift the tilt angle of 3246136_2 by 2 degrees
- `C7`: Increase A3 Offset threshold for 3246136_2
- `C8`: Adjust the azimuth of 3218306_1 by 8 degrees
- `C9`: Increase A3 Offset threshold for 3218306_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246136_2
- `C11`: Press down the tilt angle of 3246136_2 by 2 degrees
- `C12`: Increase transmission power for 3246136_2
- `C13`: Decrease A3 Offset threshold for 3246136_2
- `C14`: Press down the tilt angle  of 3218306_1 by 4 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218306_1
- `C16`: Add neighbor relationship between 3246136_2 and 3218306_1
- `C17`: Check test server and transmission issues
- `C18`: Insufficient data; more data is needed for judgment. **← 정답**
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218306_1
- `C20`: Lift the tilt angle  of 3218306_1 by 4 degrees
- `C21`: Adjust the azimuth of 3246136_2 by 39 degrees
- `C22`: Increase transmission power for 3218306_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.395 | MS1 | 121.4656608519 | 31.1446337545 | 250 | 504990 | -90.24 | 13.37 | 325.61 | 0.05 | 2.41 | 1596 |
| 2024-09-20 22:21:32.843 | MS1 | 121.4656774974 | 31.1446220468 | 250 | 504990 | -88.74 | 12.04 | 513.22 | 0.18 | 2.20 | 1595 |
| 2024-09-20 22:21:33.337 | MS1 | 121.4656629991 | 31.1446304230 | 250 | 504990 | -88.73 | 15.46 | 316.24 | 0.18 | 2.77 | 1594 |
| 2024-09-20 22:21:34.885 | MS1 | 121.4656732258 | 31.1446241653 | 250 | 504990 | -91.25 | 17.73 | 62.27 | 0.02 | 2.72 | 1560 |
| 2024-09-20 22:21:35.764 | MS1 | 121.4656694094 | 31.1446197371 | 250 | 504990 | -88.24 | 16.15 | 80.25 | 0.13 | 2.32 | 1560 |
| 2024-09-20 22:21:36.593 | MS1 | 121.4656648088 | 31.1446338173 | 250 | 504990 | -87.73 | 12.09 | 90.86 | 0.06 | 2.87 | 1597 |
| 2024-09-20 22:21:37.279 | MS1 | 121.4656606097 | 31.1446243049 | 250 | 504990 | -89.47 | 10.92 | 60.91 | 0.00 | 2.75 | 1562 |
| 2024-09-20 22:21:38.714 | MS1 | 121.4656650178 | 31.1446369733 | 250 | 504990 | -91.89 | 7.12 | 101.94 | 0.04 | 2.96 | 1597 |
| 2024-09-20 22:21:39.255 | MS1 | 121.4656697295 | 31.1446292323 | 250 | 504990 | -92.58 | 8.32 | 61.19 | 0.16 | 2.33 | 1590 |
| 2024-09-20 22:21:40.956 | MS1 | 121.4656688002 | 31.1446209408 | 250 | 504990 | -91.19 | 12.07 | 304.64 | 0.12 | 2.63 | 1570 |
| 2024-09-20 22:21:41.387 | MS1 | 121.4656659901 | 31.1446238766 | 250 | 504990 | -93.23 | 7.77 | 507.27 | 0.13 | 2.33 | 1578 |
| 2024-09-20 22:21:42.361 | MS1 | 121.4656612014 | 31.1446216605 | 250 | 504990 | -93.94 | 9.73 | 560.52 | 0.17 | 2.50 | 1592 |

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
| 3214647 | 4 | 121.4696188387 | 31.1542912465 | 318 | 10 | 3 | 23.3 | TDD | 187 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3218306 | 1 | 121.4682902349 | 31.1514838420 | 190 | 3 | 2 | 19.1 | TDD | 337 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3225722 | 3 | 121.4750956703 | 31.1514557177 | 19 | 11 | 4 | 37.5 | TDD | 123 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3246136 | 2 | 121.4730537386 | 31.1554220483 | 249 | 0 | 1 | 41.1 | TDD | 250 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.305 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.323 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.457 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.457 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.116 | NREventA3 | measId:2;ServCellPCI:1005;S... |
| 2024-09-20 22:21:38.356 | NRHandoverAttempt | SourcePCI:1005;SourceNR-ARF... |
| 2024-09-20 22:21:38.386 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.398 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.544 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.544 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3218306 | 1 | 88.4333 | 84.5348 | -114.8594 | 5.5934 | 160.6281 | 0.0038 | 0.0151 |
| 2024_09_19 22:00 | 3246136 | 2 | 91.8316 | 77.8957 | -117.8477 | 10.5968 | 148.5942 | 0.0089 | 0.0083 |
| 2024_09_19 22:00 | 3225722 | 3 | 91.4101 | 88.1175 | -117.1704 | 6.2033 | 85.8327 | 0.0189 | 0.0170 |
| 2024_09_19 22:00 | 3214647 | 4 | 82.7687 | 86.5411 | -115.2841 | 18.0462 | 142.0155 | 0.0103 | 0.0001 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417123_079444CA | 504990 | 250 | -90.7 | 504990 | 337 | -96.4 | 504990 | 123 | -103.3 | 504990 | 187 |
| MR_1774417123_717A1107 | 504990 | 250 | -90.8 | 504990 | 337 | -96.4 | 504990 | 123 | -106.1 | 504990 | 187 |
| MR_1774417123_7F09A08F | 504990 | 250 | -92.2 | 504990 | 337 | -96.1 | 504990 | 123 | -103.3 | 504990 | 187 |
| MR_1774417123_8BD72817 | 504990 | 250 | -91.7 | 504990 | 337 | -97.6 | 504990 | 123 | -102.9 | 504990 | 187 |
| MR_1774417123_E6439F0C | 504990 | 250 | -91.4 | 504990 | 337 | -94.3 | 504990 | 123 | -106.1 | 504990 | 187 |
| MR_1774417123_868D1CDB | 504990 | 250 | -90.6 | 504990 | 337 | -95.3 | 504990 | 123 | -104.7 | 504990 | 187 |
| MR_1774417123_5C875499 | 504990 | 250 | -91.8 | 504990 | 337 | -96.0 | 504990 | 123 | -105.9 | 504990 | 187 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 903: `fb815bd5-1ed...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fb815bd5-1ed0-4fe9-bec9-16d43acfaa62` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3256753_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[903] topology](images/train_0903.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256753_2 **← 정답**
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230414_3
- `C3`: Press down the tilt angle  of 3230414_3 by 9 degrees
- `C4`: Lift the tilt angle  of 3230414_3 by 9 degrees
- `C5`: Increase transmission power for 3230414_3
- `C6`: Add neighbor relationship between 3267086_1 and 3230414_3
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256753_2
- `C9`: Increase transmission power for 3256753_2
- `C10`: Decrease A3 Offset threshold for 3256753_2
- `C11`: Adjust the azimuth of 3256753_2 by 6 degrees
- `C12`: Decrease transmission power for 3230414_3
- `C13`: Adjust the azimuth of 3230414_3 by 50 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230414_3
- `C15`: Increase A3 Offset threshold for 3256753_2
- `C16`: Press down the tilt angle of 3256753_2 by 2 degrees
- `C17`: Increase A3 Offset threshold for 3230414_3
- `C18`: Decrease transmission power for 3256753_2
- `C19`: Decrease A3 Offset threshold for 3230414_3
- `C20`: Add neighbor relationship between 3256753_2 and 3230414_3
- `C21`: Lift the tilt angle of 3256753_2 by 2 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.213 | MS1 | 121.4656593758 | 31.1446298103 | 802 | 504990 | -88.40 | 14.65 | 365.05 | 0.05 | 2.52 | 1588 |
| 2024-09-20 22:21:32.198 | MS1 | 121.4656678632 | 31.1446218206 | 802 | 504990 | -90.24 | 12.00 | 372.45 | 0.00 | 2.07 | 1581 |
| 2024-09-20 22:21:33.348 | MS1 | 121.4656742002 | 31.1446307759 | 802 | 504990 | -88.93 | 16.93 | 390.91 | 0.12 | 2.31 | 1571 |
| 2024-09-20 22:21:34.763 | MS1 | 121.4656635855 | 31.1446201724 | 802 | 504990 | -85.04 | 13.48 | 47.09 | 0.66 | 2.71 | 606 |
| 2024-09-20 22:21:35.632 | MS1 | 121.4656737128 | 31.1446244509 | 802 | 504990 | -91.95 | 15.87 | 46.18 | 0.59 | 2.50 | 506 |
| 2024-09-20 22:21:36.246 | MS1 | 121.4656779349 | 31.1446194944 | 802 | 504990 | -87.49 | 16.16 | 92.11 | 0.67 | 2.09 | 553 |
| 2024-09-20 22:21:37.622 | MS1 | 121.4656667839 | 31.1446225122 | 802 | 504990 | -89.41 | 8.74 | 82.64 | 0.68 | 2.83 | 623 |
| 2024-09-20 22:21:38.173 | MS1 | 121.4656583650 | 31.1446302599 | 802 | 504990 | -91.41 | 11.49 | 60.56 | 0.59 | 2.70 | 691 |
| 2024-09-20 22:21:39.648 | MS1 | 121.4656727805 | 31.1446208264 | 802 | 504990 | -91.04 | 12.41 | 88.92 | 0.67 | 2.20 | 501 |
| 2024-09-20 22:21:40.693 | MS1 | 121.4656628713 | 31.1446184005 | 802 | 504990 | -93.67 | 12.28 | 564.85 | 0.02 | 2.87 | 1592 |
| 2024-09-20 22:21:41.259 | MS1 | 121.4656693137 | 31.1446289598 | 802 | 504990 | -93.17 | 11.86 | 437.22 | 0.06 | 3.00 | 1592 |
| 2024-09-20 22:21:42.277 | MS1 | 121.4656751417 | 31.1446260373 | 802 | 504990 | -90.04 | 7.81 | 488.77 | 0.13 | 2.27 | 1569 |

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
| 3230414 | 3 | 121.4742988947 | 31.1503270935 | 72 | 7 | 12 | 36.6 | TDD | 125 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3256753 | 2 | 121.4746056750 | 31.1479348194 | 241 | 1 | 7 | 20.0 | TDD | 802 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3266837 | 4 | 121.4732652611 | 31.1471269554 | 177 | 15 | 3 | 29.1 | TDD | 45 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3267086 | 1 | 121.4748978646 | 31.1512075326 | 33 | 6 | 3 | 48.1 | TDD | 873 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.482 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.499 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.608 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.608 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.333 | NREventA3 | measId:2;ServCellPCI:111;Se... |
| 2024-09-20 22:21:38.573 | NRHandoverAttempt | SourcePCI:111;SourceNR-ARFC... |
| 2024-09-20 22:21:38.608 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.622 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.751 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.751 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267086 | 1 | 8.6109 | 19.4322 | -114.0465 | 15.9713 | 177.9147 | 0.0068 | 0.0018 |
| 2024_09_20 22:00 | 3256753 | 2 | 10.7843 | 14.0586 | -114.4269 | 15.0742 | 127.6800 | 0.0061 | 0.0123 |
| 2024_09_20 22:00 | 3230414 | 3 | 6.2195 | 13.5322 | -114.9418 | 10.1792 | 168.8752 | 0.0063 | 0.0130 |
| 2024_09_20 22:00 | 3266837 | 4 | 9.8290 | 19.9236 | -115.6283 | 19.6085 | 93.3934 | 0.0070 | 0.0167 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414068_821281BB | 504990 | 802 | -86.0 | 504990 | 125 | -92.7 | 504990 | 873 | -98.2 | 504990 | 45 |
| MR_1774414068_AB94F62D | 504990 | 802 | -83.9 | 504990 | 125 | -93.3 | 504990 | 873 | -96.4 | 504990 | 45 |
| MR_1774414068_74842D1B | 504990 | 802 | -84.2 | 504990 | 125 | -95.6 | 504990 | 873 | -96.6 | 504990 | 45 |
| MR_1774414068_2D98FE82 | 504990 | 802 | -86.6 | 504990 | 125 | -94.1 | 504990 | 873 | -95.5 | 504990 | 45 |
| MR_1774414068_05E4C235 | 504990 | 802 | -86.8 | 504990 | 125 | -95.3 | 504990 | 873 | -96.1 | 504990 | 45 |
| MR_1774414068_8788C372 | 504990 | 802 | -85.8 | 504990 | 125 | -93.8 | 504990 | 873 | -97.5 | 504990 | 45 |
| MR_1774414068_39B21237 | 504990 | 802 | -85.0 | 504990 | 125 | -94.1 | 504990 | 873 | -96.2 | 504990 | 45 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 904: `63c62e2a-c89...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `63c62e2a-c896-4242-bb36-e85a093c1d65` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3245556_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[904] topology](images/train_0904.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3245556_3 by 18 degrees
- `C2`: Press down the tilt angle of 3245556_3 by 2 degrees
- `C3`: Press down the tilt angle  of 3221861_1 by 10 degrees
- `C4`: Increase A3 Offset threshold for 3221861_1
- `C5`: Add neighbor relationship between 3265829_4 and 3221861_1
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221861_1
- `C8`: Add neighbor relationship between 3245556_3 and 3221861_1
- `C9`: Increase A3 Offset threshold for 3245556_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245556_3
- `C11`: Increase transmission power for 3245556_3
- `C12`: Lift the tilt angle  of 3221861_1 by 10 degrees
- `C13`: Decrease transmission power for 3221861_1
- `C14`: Adjust the azimuth of 3221861_1 by 50 degrees
- `C15`: Decrease A3 Offset threshold for 3221861_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221861_1
- `C17`: Decrease transmission power for 3245556_3
- `C18`: Check test server and transmission issues
- `C19`: Lift the tilt angle of 3245556_3 by 2 degrees
- `C20`: Increase transmission power for 3221861_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245556_3 **← 정답**
- `C22`: Decrease A3 Offset threshold for 3245556_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.966 | MS1 | 121.4656750006 | 31.1446331975 | 413 | 504990 | -89.93 | 17.67 | 476.85 | 0.12 | 2.58 | 1594 |
| 2024-09-20 22:21:32.788 | MS1 | 121.4656641986 | 31.1446286027 | 413 | 504990 | -90.73 | 13.39 | 539.33 | 0.13 | 2.15 | 1587 |
| 2024-09-20 22:21:33.913 | MS1 | 121.4656620848 | 31.1446349656 | 413 | 504990 | -85.08 | 12.56 | 434.82 | 0.11 | 2.11 | 1595 |
| 2024-09-20 22:21:34.718 | MS1 | 121.4656744569 | 31.1446257673 | 413 | 504990 | -87.28 | 16.85 | 51.11 | 0.50 | 2.82 | 691 |
| 2024-09-20 22:21:35.531 | MS1 | 121.4656606769 | 31.1446204371 | 413 | 504990 | -90.42 | 15.60 | 70.43 | 0.56 | 2.67 | 597 |
| 2024-09-20 22:21:36.890 | MS1 | 121.4656744311 | 31.1446287535 | 413 | 504990 | -90.44 | 16.96 | 54.81 | 0.69 | 2.95 | 569 |
| 2024-09-20 22:21:37.675 | MS1 | 121.4656634730 | 31.1446285640 | 413 | 504990 | -89.35 | 11.06 | 62.07 | 0.55 | 2.84 | 550 |
| 2024-09-20 22:21:38.879 | MS1 | 121.4656667431 | 31.1446374338 | 413 | 504990 | -92.72 | 9.19 | 54.30 | 0.65 | 2.54 | 620 |
| 2024-09-20 22:21:39.544 | MS1 | 121.4656586929 | 31.1446337702 | 413 | 504990 | -91.35 | 11.37 | 89.95 | 0.54 | 2.31 | 639 |
| 2024-09-20 22:21:40.580 | MS1 | 121.4656606699 | 31.1446257518 | 413 | 504990 | -93.48 | 12.14 | 397.13 | 0.16 | 2.38 | 1596 |
| 2024-09-20 22:21:41.539 | MS1 | 121.4656676995 | 31.1446312943 | 413 | 504990 | -91.26 | 8.08 | 529.74 | 0.17 | 2.73 | 1564 |
| 2024-09-20 22:21:42.182 | MS1 | 121.4656638431 | 31.1446200157 | 413 | 504990 | -90.54 | 7.26 | 553.50 | 0.19 | 2.18 | 1596 |

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
| 3221861 | 1 | 121.4669565771 | 31.1536031877 | 357 | 9 | 10 | 17.0 | TDD | 151 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3245556 | 3 | 121.4690725263 | 31.1529469882 | 181 | 0 | 0 | 35.8 | TDD | 413 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3265829 | 4 | 121.4673626306 | 31.1554852278 | 79 | 7 | 10 | 31.0 | TDD | 239 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3278980 | 2 | 121.4741959252 | 31.1462279261 | 115 | 6 | 1 | 38.4 | TDD | 739 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.185 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.203 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.329 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.329 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.022 | NREventA3 | measId:2;ServCellPCI:188;Se... |
| 2024-09-20 22:21:38.262 | NRHandoverAttempt | SourcePCI:188;SourceNR-ARFC... |
| 2024-09-20 22:21:38.307 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.321 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.446 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.446 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221861 | 1 | 8.4338 | 19.5001 | -117.5172 | 17.4073 | 103.9991 | 0.0021 | 0.0095 |
| 2024_09_20 22:00 | 3278980 | 2 | 5.9367 | 13.5271 | -115.7915 | 14.1524 | 180.8851 | 0.0017 | 0.0023 |
| 2024_09_20 22:00 | 3245556 | 3 | 17.2775 | 17.3934 | -114.0381 | 15.7870 | 172.7156 | 0.0082 | 0.0086 |
| 2024_09_20 22:00 | 3265829 | 4 | 14.0062 | 13.8170 | -114.3569 | 13.4144 | 98.7361 | 0.0066 | 0.0136 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414621_AD890F70 | 504990 | 413 | -88.2 | 504990 | 151 | -90.1 | 504990 | 239 | -100.3 | 504990 | 739 |
| MR_1774414621_3C1F0158 | 504990 | 413 | -88.5 | 504990 | 151 | -90.4 | 504990 | 239 | -104.0 | 504990 | 739 |
| MR_1774414621_696BEC43 | 504990 | 413 | -86.4 | 504990 | 151 | -89.4 | 504990 | 239 | -100.3 | 504990 | 739 |
| MR_1774414621_70A2610E | 504990 | 413 | -88.6 | 504990 | 151 | -87.9 | 504990 | 239 | -100.9 | 504990 | 739 |
| MR_1774414621_7DBE909C | 504990 | 413 | -88.2 | 504990 | 151 | -90.6 | 504990 | 239 | -103.7 | 504990 | 739 |
| MR_1774414621_A1411111 | 504990 | 413 | -88.2 | 504990 | 151 | -89.4 | 504990 | 239 | -103.5 | 504990 | 739 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 905: `79d78f6d-b45...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `79d78f6d-b453-42cc-b0f9-acbb5ffc5dbb` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Decrease A3 Offset threshold for 3262048_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[905] topology](images/train_0905.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3262048_1 and 3261843_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261843_2
- `C3`: Increase transmission power for 3261843_2
- `C4`: Decrease A3 Offset threshold for 3261843_2
- `C5`: Adjust the azimuth of 3261843_2 by 50 degrees
- `C6`: Decrease transmission power for 3262048_1
- `C7`: Check test server and transmission issues
- `C8`: Press down the tilt angle of 3262048_1 by 9 degrees
- `C9`: Press down the tilt angle  of 3261843_2 by 9 degrees
- `C10`: Adjust the azimuth of 3262048_1 by 50 degrees
- `C11`: Lift the tilt angle  of 3261843_2 by 9 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262048_1
- `C13`: Increase A3 Offset threshold for 3262048_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Lift the tilt angle of 3262048_1 by 9 degrees
- `C16`: Decrease transmission power for 3261843_2
- `C17`: Decrease A3 Offset threshold for 3262048_1 **← 정답**
- `C18`: Increase transmission power for 3262048_1
- `C19`: Add neighbor relationship between 3273237_4 and 3261843_2
- `C20`: Increase A3 Offset threshold for 3261843_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261843_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262048_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.329 | MS1 | 121.4656648465 | 31.1446297836 | 453 | 504990 | -83.53 | 12.79 | 409.29 | 0.15 | 2.91 | 1561 |
| 2024-09-20 22:21:32.922 | MS1 | 121.4656748493 | 31.1446356683 | 453 | 504990 | -80.61 | 17.18 | 386.80 | 0.16 | 2.01 | 1594 |
| 2024-09-20 22:21:33.509 | MS1 | 121.4656684384 | 31.1446266680 | 453 | 504990 | -81.55 | 16.19 | 317.77 | 0.15 | 2.86 | 1566 |
| 2024-09-20 22:21:34.203 | MS1 | 121.4656718122 | 31.1446276559 | 453 | 504990 | -91.75 | -2.14 | 43.77 | 0.12 | 1.21 | 1589 |
| 2024-09-20 22:21:35.404 | MS1 | 121.4656611160 | 31.1446298680 | 453 | 504990 | -90.75 | -1.19 | 59.62 | 0.08 | 1.35 | 1566 |
| 2024-09-20 22:21:36.785 | MS1 | 121.4656590968 | 31.1446356848 | 453 | 504990 | -84.53 | -2.85 | 39.35 | 0.13 | 1.48 | 1577 |
| 2024-09-20 22:21:37.205 | MS1 | 121.4656591913 | 31.1446312217 | 453 | 504990 | -87.70 | -1.33 | 52.71 | 0.20 | 1.32 | 1567 |
| 2024-09-20 22:21:38.828 | MS1 | 121.4656699084 | 31.1446286302 | 453 | 504990 | -88.46 | -1.61 | 69.35 | 0.01 | 1.24 | 1581 |
| 2024-09-20 22:21:39.546 | MS1 | 121.4656635470 | 31.1446360313 | 233 | 504990 | -79.68 | 17.26 | 219.75 | 0.18 | 1.36 | 1591 |
| 2024-09-20 22:21:40.505 | MS1 | 121.4656655797 | 31.1446250632 | 233 | 504990 | -76.55 | 17.46 | 421.30 | 0.17 | 2.70 | 1593 |
| 2024-09-20 22:21:41.250 | MS1 | 121.4656731594 | 31.1446277440 | 233 | 504990 | -75.97 | 13.26 | 434.51 | 0.16 | 2.47 | 1600 |
| 2024-09-20 22:21:42.767 | MS1 | 121.4656622640 | 31.1446183109 | 233 | 504990 | -78.75 | 14.71 | 464.28 | 0.13 | 2.28 | 1586 |

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
| 3261843 | 2 | 121.4744913396 | 31.1500715130 | 18 | 7 | 8 | 40.9 | TDD | 233 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3262048 | 1 | 121.4701046437 | 31.1476475131 | 338 | 6 | 9 | 25.5 | TDD | 453 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3273237 | 4 | 121.4672545311 | 31.1532199828 | 184 | 7 | 4 | 17.1 | TDD | 807 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3274095 | 3 | 121.4702741156 | 31.1524081879 | 100 | 5 | 10 | 27.1 | TDD | 357 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.951 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.966 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.092 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.092 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.818 | NREventA3 | measId:2;ServCellPCI:672;Se... |
| 2024-09-20 22:21:38.058 | NRHandoverAttempt | SourcePCI:672;SourceNR-ARFC... |
| 2024-09-20 22:21:38.094 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.106 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.248 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.248 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262048 | 1 | 7.8924 | 7.6934 | -115.8831 | 7.6744 | 105.4589 | 0.0015 | 0.1555 |
| 2024_09_20 22:00 | 3261843 | 2 | 6.6094 | 12.3000 | -116.7032 | 17.2884 | 114.6314 | 0.0130 | 0.0022 |
| 2024_09_20 22:00 | 3274095 | 3 | 17.4997 | 5.0727 | -117.5443 | 17.7177 | 98.9760 | 0.0031 | 0.0128 |
| 2024_09_20 22:00 | 3273237 | 4 | 10.7458 | 18.4142 | -114.4055 | 5.8625 | 129.4161 | 0.0102 | 0.0173 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415142_F6BE650D | 504990 | 233 | -88.5 | 504990 | 453 | -92.4 | 504990 | 807 | -92.8 | 504990 | 357 |
| MR_1774415142_69AEC673 | 504990 | 453 | -90.5 | 504990 | 233 | -86.6 | 504990 | 807 | -90.5 | 504990 | 357 |
| MR_1774415142_AA6DD541 | 504990 | 233 | -86.0 | 504990 | 453 | -92.4 | 504990 | 807 | -90.8 | 504990 | 357 |
| MR_1774415142_C9DED06A | 504990 | 453 | -91.0 | 504990 | 233 | -86.8 | 504990 | 807 | -89.7 | 504990 | 357 |
| MR_1774415142_154CB38E | 504990 | 453 | -90.5 | 504990 | 233 | -87.6 | 504990 | 807 | -92.5 | 504990 | 357 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 906: `6383aeb7-76a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6383aeb7-76aa-4855-9f64-08b10ee26e98` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Add neighbor relationship between 3278937_2 and 3224643_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[906] topology](images/train_0906.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3224643_4 by 47 degrees
- `C2`: Add neighbor relationship between 3278204_1 and 3224643_4
- `C3`: Press down the tilt angle  of 3224643_4 by 4 degrees
- `C4`: Adjust the azimuth of 3278937_2 by 50 degrees
- `C5`: Increase A3 Offset threshold for 3224643_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224643_4
- `C7`: Increase transmission power for 3224643_4
- `C8`: Increase transmission power for 3278937_2
- `C9`: Decrease A3 Offset threshold for 3224643_4
- `C10`: Lift the tilt angle  of 3224643_4 by 4 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278937_2
- `C12`: Lift the tilt angle of 3278937_2 by 10 degrees
- `C13`: Check test server and transmission issues
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Add neighbor relationship between 3278937_2 and 3224643_4 **← 정답**
- `C16`: Decrease A3 Offset threshold for 3278937_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224643_4
- `C18`: Increase A3 Offset threshold for 3278937_2
- `C19`: Decrease transmission power for 3278937_2
- `C20`: Decrease transmission power for 3224643_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278937_2
- `C22`: Press down the tilt angle of 3278937_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.995 | MS1 | 121.4656685380 | 31.1446262223 | 493 | 504990 | -80.95 | 17.59 | 453.88 | 0.15 | 2.92 | 1576 |
| 2024-09-20 22:21:32.833 | MS1 | 121.4656625923 | 31.1446283308 | 493 | 504990 | -80.57 | 14.91 | 562.82 | 0.02 | 2.61 | 1586 |
| 2024-09-20 22:21:33.198 | MS1 | 121.4656722578 | 31.1446238904 | 493 | 504990 | -81.86 | 14.51 | 456.58 | 0.02 | 2.99 | 1588 |
| 2024-09-20 22:21:34.213 | MS1 | 121.4656697125 | 31.1446228971 | 493 | 504990 | -94.10 | -2.53 | 54.77 | 0.06 | 1.44 | 1579 |
| 2024-09-20 22:21:35.939 | MS1 | 121.4656717355 | 31.1446207472 | 493 | 504990 | -90.49 | -2.31 | 35.92 | 0.16 | 1.33 | 1575 |
| 2024-09-20 22:21:36.754 | MS1 | 121.4656683459 | 31.1446358236 | 493 | 504990 | -86.12 | -2.91 | 68.10 | 0.04 | 1.06 | 1581 |
| 2024-09-20 22:21:37.484 | MS1 | 121.4656658060 | 31.1446207669 | 493 | 504990 | -94.64 | -0.81 | 37.01 | 0.13 | 1.34 | 1593 |
| 2024-09-20 22:21:38.980 | MS1 | 121.4656678501 | 31.1446250754 | 493 | 504990 | -83.47 | 16.78 | 296.96 | 0.01 | 1.28 | 1584 |
| 2024-09-20 22:21:39.578 | MS1 | 121.4656658123 | 31.1446247244 | 493 | 504990 | -78.52 | 15.74 | 531.25 | 0.06 | 1.20 | 1593 |
| 2024-09-20 22:21:40.470 | MS1 | 121.4656676208 | 31.1446202140 | 493 | 504990 | -82.85 | 14.78 | 569.32 | 0.20 | 2.40 | 1567 |
| 2024-09-20 22:21:41.462 | MS1 | 121.4656673399 | 31.1446316356 | 493 | 504990 | -80.68 | 14.20 | 469.19 | 0.04 | 2.72 | 1572 |
| 2024-09-20 22:21:42.810 | MS1 | 121.4656611785 | 31.1446373195 | 493 | 504990 | -78.34 | 13.40 | 511.77 | 0.14 | 2.66 | 1563 |

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
| 3224643 | 4 | 121.4755252914 | 31.1496453972 | 192 | 3 | 7 | 26.1 | TDD | 6 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3255070 | 3 | 121.4662539942 | 31.1505656694 | 319 | 15 | 2 | 36.5 | TDD | 110 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3278204 | 1 | 121.4687707857 | 31.1540250553 | 232 | 6 | 4 | 39.0 | TDD | 609 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3278937 | 2 | 121.4673487655 | 31.1509318950 | 35 | 10 | 12 | 36.8 | TDD | 493 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.658 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.674 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.783 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.783 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.496 | NREventA3 | measId:2;ServCellPCI:544;Se... |
| 2024-09-20 22:21:36.496 | NREventA3 | measId:2;ServCellPCI:544;Se... |
| 2024-09-20 22:21:37.496 | NREventA3 | measId:2;ServCellPCI:544;Se... |
| 2024-09-20 22:21:39.996 | NRRRCReestablishAttempt | PCI:544 |
| 2024-09-20 22:21:40.012 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:40.023 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:40.153 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.153 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278204 | 1 | 13.2644 | 19.2231 | -114.5418 | 11.0997 | 128.7677 | 0.0024 | 0.0003 |
| 2024_09_20 22:00 | 3278937 | 2 | 9.6287 | 9.3502 | -117.6699 | 16.7964 | 194.3247 | 0.0199 | 0.1191 |
| 2024_09_20 22:00 | 3255070 | 3 | 10.3182 | 7.8021 | -117.3337 | 8.4373 | 155.8656 | 0.0014 | 0.0036 |
| 2024_09_20 22:00 | 3224643 | 4 | 11.1871 | 13.2039 | -117.6071 | 18.9804 | 166.4689 | 0.0092 | 0.0145 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413458_7CCBC2F1 | 504990 | 493 | -92.4 | 504990 | 6 | -90.3 | 504990 | 609 | -93.8 | 504990 | 110 |
| MR_1774413458_4733EA19 | 504990 | 493 | -93.3 | 504990 | 6 | -91.5 | 504990 | 609 | -91.5 | 504990 | 110 |
| MR_1774413458_170D3E81 | 504990 | 6 | -88.6 | 504990 | 493 | -95.5 | 504990 | 609 | -93.5 | 504990 | 110 |
| MR_1774413458_58E7A2A9 | 504990 | 6 | -91.4 | 504990 | 493 | -92.8 | 504990 | 609 | -92.2 | 504990 | 110 |
| MR_1774413458_1D240FDC | 504990 | 6 | -88.8 | 504990 | 493 | -92.8 | 504990 | 609 | -93.7 | 504990 | 110 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 907: `b210019c-c3d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b210019c-c3db-4f6b-82d5-320002e5ba87` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[907] topology](images/train_0907.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3223539_3
- `C2`: Add neighbor relationship between 3223539_3 and 3215183_2
- `C3`: Adjust the azimuth of 3215183_2 by 50 degrees
- `C4`: Increase transmission power for 3215183_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215183_2
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase transmission power for 3223539_3
- `C8`: Press down the tilt angle of 3223539_3 by 10 degrees
- `C9`: Check test server and transmission issues **← 정답**
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223539_3
- `C11`: Increase A3 Offset threshold for 3215183_2
- `C12`: Decrease transmission power for 3215183_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223539_3
- `C14`: Add neighbor relationship between 3211869_1 and 3215183_2
- `C15`: Lift the tilt angle  of 3215183_2 by 10 degrees
- `C16`: Press down the tilt angle  of 3215183_2 by 10 degrees
- `C17`: Lift the tilt angle of 3223539_3 by 10 degrees
- `C18`: Decrease A3 Offset threshold for 3215183_2
- `C19`: Increase A3 Offset threshold for 3223539_3
- `C20`: Adjust the azimuth of 3223539_3 by 50 degrees
- `C21`: Decrease transmission power for 3223539_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215183_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.704 | MS1 | 121.4656728196 | 31.1446209236 | 661 | 504990 | -90.02 | 15.33 | 494.72 | 0.04 | 2.38 | 1589 |
| 2024-09-20 22:21:32.662 | MS1 | 121.4656643652 | 31.1446197900 | 661 | 504990 | -88.67 | 12.25 | 540.24 | 0.09 | 2.38 | 1600 |
| 2024-09-20 22:21:33.616 | MS1 | 121.4656765633 | 31.1446314162 | 661 | 504990 | -86.79 | 16.43 | 471.64 | 0.13 | 2.97 | 1598 |
| 2024-09-20 22:21:34.111 | MS1 | 121.4656651287 | 31.1446360522 | 661 | 504990 | -88.68 | 16.64 | 53.56 | 0.05 | 2.61 | 305 |
| 2024-09-20 22:21:35.749 | MS1 | 121.4656767574 | 31.1446347274 | 661 | 504990 | -87.83 | 15.97 | 102.49 | 0.10 | 2.70 | 409 |
| 2024-09-20 22:21:36.622 | MS1 | 121.4656640435 | 31.1446378573 | 661 | 504990 | -89.96 | 14.78 | 47.34 | 0.15 | 2.72 | 413 |
| 2024-09-20 22:21:37.651 | MS1 | 121.4656691537 | 31.1446350066 | 661 | 504990 | -90.49 | 11.48 | 79.34 | 0.15 | 2.65 | 470 |
| 2024-09-20 22:21:38.500 | MS1 | 121.4656626005 | 31.1446234792 | 661 | 504990 | -91.82 | 12.97 | 76.03 | 0.19 | 2.27 | 439 |
| 2024-09-20 22:21:39.623 | MS1 | 121.4656718842 | 31.1446254132 | 661 | 504990 | -90.03 | 11.84 | 78.49 | 0.04 | 2.72 | 364 |
| 2024-09-20 22:21:40.353 | MS1 | 121.4656722043 | 31.1446320505 | 661 | 504990 | -93.23 | 10.16 | 419.02 | 0.09 | 2.40 | 1586 |
| 2024-09-20 22:21:41.968 | MS1 | 121.4656724356 | 31.1446209350 | 661 | 504990 | -92.18 | 10.98 | 512.83 | 0.08 | 2.90 | 1594 |
| 2024-09-20 22:21:42.779 | MS1 | 121.4656730728 | 31.1446247918 | 661 | 504990 | -90.78 | 12.13 | 485.60 | 0.05 | 2.87 | 1564 |

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
| 3211869 | 1 | 121.4674273990 | 31.1527445651 | 271 | 4 | 11 | 38.9 | TDD | 848 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3215183 | 2 | 121.4664978613 | 31.1529797463 | 247 | 10 | 10 | 20.2 | TDD | 69 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3223539 | 3 | 121.4651492443 | 31.1559217584 | 337 | 10 | 0 | 43.3 | TDD | 661 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3271066 | 4 | 121.4703713722 | 31.1531167961 | 248 | 13 | 12 | 38.6 | TDD | 759 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.882 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.907 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.021 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.021 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.757 | NREventA3 | measId:2;ServCellPCI:283;Se... |
| 2024-09-20 22:21:37.997 | NRHandoverAttempt | SourcePCI:283;SourceNR-ARFC... |
| 2024-09-20 22:21:38.044 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.058 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.192 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.192 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211869 | 1 | 14.9793 | 9.8350 | -114.4922 | 10.3113 | 83.7548 | 0.0156 | 0.0097 |
| 2024_09_20 22:00 | 3215183 | 2 | 13.2283 | 11.0914 | -117.4804 | 10.3495 | 150.9132 | 0.0096 | 0.0120 |
| 2024_09_20 22:00 | 3223539 | 3 | 14.8014 | 15.3755 | -114.6089 | 15.8958 | 121.2018 | 0.0197 | 0.0121 |
| 2024_09_20 22:00 | 3271066 | 4 | 17.1554 | 8.6646 | -114.2237 | 15.2734 | 145.5154 | 0.0074 | 0.0118 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416446_6D407FAE | 504990 | 661 | -87.3 | 504990 | 69 | -96.9 | 504990 | 848 | -103.2 | 504990 | 759 |
| MR_1774416446_D89109E9 | 504990 | 661 | -88.4 | 504990 | 69 | -98.2 | 504990 | 848 | -100.7 | 504990 | 759 |
| MR_1774416446_60ED2ADF | 504990 | 661 | -90.5 | 504990 | 69 | -95.6 | 504990 | 848 | -103.9 | 504990 | 759 |
| MR_1774416446_003704D0 | 504990 | 661 | -89.0 | 504990 | 69 | -95.6 | 504990 | 848 | -101.9 | 504990 | 759 |
| MR_1774416446_43E6A12F | 504990 | 661 | -89.2 | 504990 | 69 | -96.5 | 504990 | 848 | -102.3 | 504990 | 759 |
| MR_1774416446_5D7F9102 | 504990 | 661 | -87.3 | 504990 | 69 | -97.8 | 504990 | 848 | -101.8 | 504990 | 759 |
| MR_1774416446_2BA449B7 | 504990 | 661 | -87.8 | 504990 | 69 | -96.5 | 504990 | 848 | -102.6 | 504990 | 759 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 908: `d7fb948b-2bc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d7fb948b-2bc2-4e26-b227-361ed3720dd7` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Add neighbor relationship between 3253642_2 and 3270573_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[908] topology](images/train_0908.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253642_2
- `C2`: Increase A3 Offset threshold for 3270573_1
- `C3`: Increase A3 Offset threshold for 3253642_2
- `C4`: Lift the tilt angle of 3253642_2 by 2 degrees
- `C5`: Decrease transmission power for 3253642_2
- `C6`: Decrease A3 Offset threshold for 3270573_1
- `C7`: Increase transmission power for 3253642_2
- `C8`: Check test server and transmission issues
- `C9`: Lift the tilt angle  of 3270573_1 by 2 degrees
- `C10`: Adjust the azimuth of 3253642_2 by 50 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253642_2
- `C12`: Decrease A3 Offset threshold for 3253642_2
- `C13`: Press down the tilt angle  of 3270573_1 by 2 degrees
- `C14`: Increase transmission power for 3270573_1
- `C15`: Decrease transmission power for 3270573_1
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Adjust the azimuth of 3270573_1 by 20 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270573_1
- `C19`: Add neighbor relationship between 3222873_3 and 3270573_1
- `C20`: Press down the tilt angle of 3253642_2 by 2 degrees
- `C21`: Add neighbor relationship between 3253642_2 and 3270573_1 **← 정답**
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270573_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.724 | MS1 | 121.4656585819 | 31.1446311133 | 949 | 504990 | -80.79 | 13.49 | 316.43 | 0.05 | 2.84 | 1571 |
| 2024-09-20 22:21:32.783 | MS1 | 121.4656617569 | 31.1446262675 | 949 | 504990 | -76.62 | 16.40 | 584.10 | 0.13 | 2.42 | 1599 |
| 2024-09-20 22:21:33.870 | MS1 | 121.4656658296 | 31.1446246027 | 949 | 504990 | -80.64 | 14.94 | 552.76 | 0.20 | 2.11 | 1594 |
| 2024-09-20 22:21:34.819 | MS1 | 121.4656585889 | 31.1446199043 | 949 | 504990 | -94.01 | -0.11 | 43.04 | 0.05 | 1.20 | 1582 |
| 2024-09-20 22:21:35.715 | MS1 | 121.4656737201 | 31.1446294605 | 949 | 504990 | -88.82 | -0.30 | 39.84 | 0.10 | 1.11 | 1588 |
| 2024-09-20 22:21:36.684 | MS1 | 121.4656735247 | 31.1446199787 | 949 | 504990 | -94.69 | -3.75 | 42.79 | 0.14 | 1.20 | 1560 |
| 2024-09-20 22:21:37.183 | MS1 | 121.4656709780 | 31.1446214252 | 949 | 504990 | -86.33 | -0.99 | 62.54 | 0.05 | 1.10 | 1595 |
| 2024-09-20 22:21:38.164 | MS1 | 121.4656664312 | 31.1446366597 | 949 | 504990 | -82.54 | 17.33 | 302.51 | 0.11 | 1.06 | 1573 |
| 2024-09-20 22:21:39.648 | MS1 | 121.4656699477 | 31.1446361965 | 949 | 504990 | -76.28 | 12.93 | 476.25 | 0.10 | 1.06 | 1592 |
| 2024-09-20 22:21:40.586 | MS1 | 121.4656655229 | 31.1446355023 | 949 | 504990 | -81.00 | 12.28 | 546.32 | 0.01 | 2.44 | 1561 |
| 2024-09-20 22:21:41.598 | MS1 | 121.4656643681 | 31.1446192564 | 949 | 504990 | -83.81 | 17.66 | 466.29 | 0.12 | 2.22 | 1590 |
| 2024-09-20 22:21:42.343 | MS1 | 121.4656686078 | 31.1446190808 | 949 | 504990 | -84.97 | 12.11 | 527.82 | 0.11 | 2.81 | 1578 |

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
| 3214030 | 4 | 121.4712053292 | 31.1473512952 | 151 | 6 | 8 | 36.1 | TDD | 437 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3222873 | 3 | 121.4719868257 | 31.1481376141 | 29 | 1 | 2 | 18.5 | TDD | 470 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3253642 | 2 | 121.4752384373 | 31.1467148148 | 135 | 1 | 10 | 21.7 | TDD | 949 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3270573 | 1 | 121.4718820664 | 31.1529378046 | 193 | 0 | 1 | 35.4 | TDD | 393 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.192 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.210 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.359 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.359 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.060 | NREventA3 | measId:2;ServCellPCI:260;Se... |
| 2024-09-20 22:21:36.060 | NREventA3 | measId:2;ServCellPCI:260;Se... |
| 2024-09-20 22:21:37.060 | NREventA3 | measId:2;ServCellPCI:260;Se... |
| 2024-09-20 22:21:39.560 | NRRRCReestablishAttempt | PCI:260 |
| 2024-09-20 22:21:39.577 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.588 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.733 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.733 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270573 | 1 | 7.1448 | 18.3347 | -115.0559 | 11.0175 | 112.9977 | 0.0011 | 0.0101 |
| 2024_09_20 22:00 | 3253642 | 2 | 17.6606 | 6.9240 | -116.5887 | 10.2561 | 137.7048 | 0.0074 | 0.1624 |
| 2024_09_20 22:00 | 3222873 | 3 | 16.1948 | 8.5137 | -114.3833 | 11.2790 | 174.0057 | 0.0083 | 0.0142 |
| 2024_09_20 22:00 | 3214030 | 4 | 13.2324 | 16.6322 | -116.0440 | 9.2164 | 87.4474 | 0.0048 | 0.0016 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414824_66AF31E9 | 504990 | 949 | -93.7 | 504990 | 393 | -88.1 | 504990 | 470 | -98.3 | 504990 | 437 |
| MR_1774414824_B905E615 | 504990 | 393 | -87.7 | 504990 | 949 | -93.7 | 504990 | 470 | -99.6 | 504990 | 437 |
| MR_1774414824_B210E209 | 504990 | 949 | -95.0 | 504990 | 393 | -89.6 | 504990 | 470 | -100.4 | 504990 | 437 |
| MR_1774414824_C1A1F2B0 | 504990 | 949 | -93.2 | 504990 | 393 | -86.3 | 504990 | 470 | -99.9 | 504990 | 437 |
| MR_1774414824_A185C8D0 | 504990 | 949 | -95.9 | 504990 | 393 | -89.0 | 504990 | 470 | -97.8 | 504990 | 437 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 909: `751a5052-93d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `751a5052-93d4-4cc0-a423-f7c37debdaf9` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3266736_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[909] topology](images/train_0909.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3228767_4 by 10 degrees
- `C2`: Lift the tilt angle of 3266736_1 by 5 degrees
- `C3`: Adjust the azimuth of 3228767_4 by 50 degrees
- `C4`: Increase transmission power for 3266736_1
- `C5`: Adjust the azimuth of 3266736_1 by 14 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266736_1 **← 정답**
- `C7`: Press down the tilt angle of 3266736_1 by 5 degrees
- `C8`: Lift the tilt angle  of 3228767_4 by 10 degrees
- `C9`: Increase transmission power for 3228767_4
- `C10`: Add neighbor relationship between 3263992_3 and 3228767_4
- `C11`: Decrease transmission power for 3228767_4
- `C12`: Check test server and transmission issues
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228767_4
- `C14`: Decrease transmission power for 3266736_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228767_4
- `C16`: Decrease A3 Offset threshold for 3266736_1
- `C17`: Increase A3 Offset threshold for 3266736_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266736_1
- `C20`: Decrease A3 Offset threshold for 3228767_4
- `C21`: Add neighbor relationship between 3266736_1 and 3228767_4
- `C22`: Increase A3 Offset threshold for 3228767_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.592 | MS1 | 121.4656691893 | 31.1446222963 | 31 | 504990 | -89.12 | 17.34 | 319.72 | 0.08 | 2.56 | 1592 |
| 2024-09-20 22:21:32.937 | MS1 | 121.4656698274 | 31.1446189739 | 31 | 504990 | -91.15 | 13.84 | 555.14 | 0.11 | 2.13 | 1563 |
| 2024-09-20 22:21:33.147 | MS1 | 121.4656776751 | 31.1446299613 | 31 | 504990 | -88.72 | 12.96 | 310.32 | 0.14 | 2.24 | 1579 |
| 2024-09-20 22:21:34.127 | MS1 | 121.4656657188 | 31.1446217971 | 31 | 504990 | -87.14 | 17.61 | 77.09 | 0.66 | 2.46 | 525 |
| 2024-09-20 22:21:35.174 | MS1 | 121.4656668740 | 31.1446251881 | 31 | 504990 | -85.64 | 14.39 | 84.54 | 0.53 | 2.69 | 573 |
| 2024-09-20 22:21:36.936 | MS1 | 121.4656720720 | 31.1446265315 | 31 | 504990 | -87.57 | 16.33 | 90.14 | 0.62 | 2.91 | 582 |
| 2024-09-20 22:21:37.501 | MS1 | 121.4656591740 | 31.1446256267 | 31 | 504990 | -90.14 | 12.96 | 69.05 | 0.70 | 2.84 | 684 |
| 2024-09-20 22:21:38.361 | MS1 | 121.4656600064 | 31.1446280519 | 31 | 504990 | -89.14 | 10.59 | 54.09 | 0.55 | 2.18 | 602 |
| 2024-09-20 22:21:39.207 | MS1 | 121.4656706054 | 31.1446359513 | 31 | 504990 | -90.46 | 8.63 | 90.94 | 0.69 | 2.46 | 689 |
| 2024-09-20 22:21:40.132 | MS1 | 121.4656747411 | 31.1446334087 | 31 | 504990 | -90.50 | 11.18 | 465.33 | 0.17 | 2.38 | 1578 |
| 2024-09-20 22:21:41.946 | MS1 | 121.4656727172 | 31.1446243955 | 31 | 504990 | -91.55 | 7.90 | 334.91 | 0.18 | 2.64 | 1568 |
| 2024-09-20 22:21:42.522 | MS1 | 121.4656706333 | 31.1446228740 | 31 | 504990 | -90.96 | 7.35 | 572.49 | 0.19 | 2.11 | 1581 |

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
| 3225188 | 2 | 121.4668320718 | 31.1481241038 | 168 | 8 | 8 | 19.5 | TDD | 836 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3228767 | 4 | 121.4680689810 | 31.1544024572 | 21 | 9 | 3 | 33.6 | TDD | 437 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3263992 | 3 | 121.4693272516 | 31.1548981020 | 145 | 6 | 11 | 42.8 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3266736 | 1 | 121.4672639869 | 31.1535838018 | 175 | 3 | 4 | 27.7 | TDD | 31 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.196 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.219 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.325 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.325 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.030 | NREventA3 | measId:2;ServCellPCI:810;Se... |
| 2024-09-20 22:21:38.270 | NRHandoverAttempt | SourcePCI:810;SourceNR-ARFC... |
| 2024-09-20 22:21:38.308 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.322 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.436 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.436 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266736 | 1 | 15.0741 | 9.2071 | -117.4044 | 19.1367 | 100.9017 | 0.0066 | 0.0051 |
| 2024_09_20 22:00 | 3225188 | 2 | 9.5664 | 10.8976 | -114.8088 | 7.0009 | 136.7290 | 0.0157 | 0.0117 |
| 2024_09_20 22:00 | 3263992 | 3 | 13.2199 | 7.0782 | -117.2605 | 7.6955 | 179.9495 | 0.0127 | 0.0128 |
| 2024_09_20 22:00 | 3228767 | 4 | 9.6375 | 13.6129 | -114.7718 | 12.4477 | 134.3061 | 0.0182 | 0.0198 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414936_036ECACC | 504990 | 31 | -86.9 | 504990 | 437 | -88.3 | 504990 | 309 | -96.3 | 504990 | 836 |
| MR_1774414936_FBCCCE27 | 504990 | 31 | -85.8 | 504990 | 437 | -87.5 | 504990 | 309 | -95.0 | 504990 | 836 |
| MR_1774414936_21B07F50 | 504990 | 31 | -86.1 | 504990 | 437 | -89.7 | 504990 | 309 | -96.6 | 504990 | 836 |
| MR_1774414936_360C0FF2 | 504990 | 31 | -86.7 | 504990 | 437 | -90.3 | 504990 | 309 | -97.8 | 504990 | 836 |
| MR_1774414936_CCFCF162 | 504990 | 31 | -88.1 | 504990 | 437 | -89.2 | 504990 | 309 | -96.2 | 504990 | 836 |

> *... 2개 열 생략 (전체 14열)*

---
