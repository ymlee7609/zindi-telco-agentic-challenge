# Track A 문제 분석 — train[1980]~train[1989]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1980] ~ train[1989] (10개)

## 목차

1. [문제 1980: `d063664e-04a...`](#1980) — multiple-answer, 정답: C6|C10
2. [문제 1981: `d5f13c2c-25b...`](#1981) — single-answer, 정답: C8
3. [문제 1982: `b1fdc766-451...`](#1982) — single-answer, 정답: C6
4. [문제 1983: `91145a8b-32b...`](#1983) — single-answer, 정답: C21
5. [문제 1984: `2e324d3d-6f6...`](#1984) — multiple-answer, 정답: C14|C19
6. [문제 1985: `1af10cf0-d48...`](#1985) — multiple-answer, 정답: C1|C12|C20|C21
7. [문제 1986: `a0c6c2d5-6bb...`](#1986) — single-answer, 정답: C5
8. [문제 1987: `8b3fe37f-9fe...`](#1987) — single-answer, 정답: C21
9. [문제 1988: `67b07e0e-985...`](#1988) — single-answer, 정답: C12
10. [문제 1989: `78172d11-358...`](#1989) — single-answer, 정답: C18

---

### 문제 1980: `d063664e-04a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d063664e-04ab-4dd7-9d5c-02fbbfdcea62` |
| Tag | **multiple-answer** |
| 정답 | **C6|C10** |
| C6 의미 | Decrease transmission power for 3274099_4 |
| C10 의미 | Press down the tilt angle  of 3274099_4 by 3 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1980] topology](images/train_1980.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3248445_3 by 4 degrees
- `C2`: Decrease A3 Offset threshold for 3248445_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248445_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248445_3
- `C5`: Increase transmission power for 3274099_4
- `C6`: Decrease transmission power for 3274099_4 **← 정답**
- `C7`: Increase A3 Offset threshold for 3274099_4
- `C8`: Add neighbor relationship between 3252134_2 and 3274099_4
- `C9`: Increase A3 Offset threshold for 3248445_3
- `C10`: Press down the tilt angle  of 3274099_4 by 3 degrees **← 정답**
- `C11`: Check test server and transmission issues
- `C12`: Increase transmission power for 3248445_3
- `C13`: Lift the tilt angle of 3248445_3 by 4 degrees
- `C14`: Adjust the azimuth of 3274099_4 by 13 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Add neighbor relationship between 3248445_3 and 3274099_4
- `C17`: Decrease transmission power for 3248445_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274099_4
- `C19`: Decrease A3 Offset threshold for 3274099_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274099_4
- `C21`: Lift the tilt angle  of 3274099_4 by 3 degrees
- `C22`: Adjust the azimuth of 3248445_3 by 18 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.152 | MS1 | 121.4656691790 | 31.1446210178 | 941 | 504990 | -81.12 | 16.83 | 592.32 | 0.11 | 2.11 | 1588 |
| 2024-09-20 22:21:32.196 | MS1 | 121.4656739865 | 31.1446222281 | 941 | 504990 | -76.81 | 12.24 | 412.34 | 0.16 | 2.04 | 1573 |
| 2024-09-20 22:21:33.353 | MS1 | 121.4656708895 | 31.1446231861 | 941 | 504990 | -75.43 | 15.17 | 556.25 | 0.06 | 2.70 | 1573 |
| 2024-09-20 22:21:34.334 | MS1 | 121.4656628839 | 31.1446358859 | 941 | 504990 | -88.63 | 2.65 | 80.98 | 0.17 | 1.38 | 1583 |
| 2024-09-20 22:21:35.193 | MS1 | 121.4656773774 | 31.1446288600 | 941 | 504990 | -89.79 | 1.47 | 71.21 | 0.10 | 1.00 | 1595 |
| 2024-09-20 22:21:36.987 | MS1 | 121.4656712875 | 31.1446375341 | 941 | 504990 | -92.16 | 2.37 | 69.56 | 0.18 | 1.30 | 1600 |
| 2024-09-20 22:21:37.199 | MS1 | 121.4656602647 | 31.1446307268 | 941 | 504990 | -87.79 | 0.17 | 71.05 | 0.12 | 1.19 | 1595 |
| 2024-09-20 22:21:38.806 | MS1 | 121.4656693287 | 31.1446305433 | 941 | 504990 | -87.45 | 2.48 | 82.43 | 0.06 | 1.35 | 1593 |
| 2024-09-20 22:21:39.739 | MS1 | 121.4656592086 | 31.1446333457 | 941 | 504990 | -91.48 | 3.41 | 64.62 | 0.08 | 1.32 | 1567 |
| 2024-09-20 22:21:40.160 | MS1 | 121.4656685448 | 31.1446212665 | 941 | 504990 | -80.64 | 17.79 | 321.77 | 0.01 | 2.07 | 1600 |
| 2024-09-20 22:21:41.305 | MS1 | 121.4656654252 | 31.1446212759 | 941 | 504990 | -84.32 | 13.68 | 444.84 | 0.05 | 2.67 | 1590 |
| 2024-09-20 22:21:42.973 | MS1 | 121.4656674121 | 31.1446329050 | 941 | 504990 | -75.73 | 16.18 | 552.96 | 0.03 | 2.06 | 1582 |

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
| 3231436 | 1 | 121.4689985755 | 31.1488861299 | 146 | 12 | 5 | 24.9 | TDD | 218 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3248445 | 3 | 121.4675769098 | 31.1540464821 | 208 | 3 | 4 | 18.7 | TDD | 941 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3252134 | 2 | 121.4661882840 | 31.1454942245 | 232 | 0 | 0 | 35.3 | TDD | 314 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3274099 | 4 | 121.4748815993 | 31.1528504786 | 211 | 1 | 2 | 44.6 | TDD | 138 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.057 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.079 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.179 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.179 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231436 | 1 | 6.7866 | 16.5964 | -116.8322 | 16.2994 | 103.0222 | 0.0063 | 0.0159 |
| 2024_09_20 22:00 | 3252134 | 2 | 17.5124 | 17.7722 | -114.9178 | 19.6833 | 188.0834 | 0.0062 | 0.0023 |
| 2024_09_20 22:00 | 3248445 | 3 | 12.7419 | 7.3616 | -108.3184 | 8.6199 | 88.9600 | 0.0165 | 0.0153 |
| 2024_09_20 22:00 | 3274099 | 4 | 10.2204 | 15.8412 | -116.0150 | 9.1580 | 166.3559 | 0.0120 | 0.0109 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414651_A4D15A08 | 504990 | 941 | -88.7 | 504990 | 138 | -89.4 | 504990 | 314 | -89.3 | 504990 | 218 |
| MR_1774414651_61243EEA | 504990 | 941 | -87.7 | 504990 | 138 | -87.5 | 504990 | 314 | -87.9 | 504990 | 218 |
| MR_1774414651_4F8CA70C | 504990 | 138 | -87.4 | 504990 | 941 | -89.8 | 504990 | 314 | -90.8 | 504990 | 218 |
| MR_1774414651_2C7DAD39 | 504990 | 941 | -88.8 | 504990 | 138 | -89.9 | 504990 | 314 | -90.5 | 504990 | 218 |
| MR_1774414651_CF05FD2C | 504990 | 138 | -86.9 | 504990 | 941 | -91.1 | 504990 | 314 | -87.8 | 504990 | 218 |
| MR_1774414651_92DB185B | 504990 | 138 | -88.8 | 504990 | 941 | -88.5 | 504990 | 314 | -89.1 | 504990 | 218 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1981: `d5f13c2c-25b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d5f13c2c-25b4-4815-8605-2a9be40d11f9` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1981] topology](images/train_1981.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3248370_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248370_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248370_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277614_1
- `C5`: Add neighbor relationship between 3248370_2 and 3277614_1
- `C6`: Lift the tilt angle  of 3277614_1 by 10 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Check test server and transmission issues **← 정답**
- `C9`: Increase A3 Offset threshold for 3277614_1
- `C10`: Lift the tilt angle of 3248370_2 by 6 degrees
- `C11`: Increase transmission power for 3248370_2
- `C12`: Adjust the azimuth of 3248370_2 by 50 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277614_1
- `C14`: Increase transmission power for 3277614_1
- `C15`: Add neighbor relationship between 3210553_4 and 3277614_1
- `C16`: Press down the tilt angle  of 3277614_1 by 10 degrees
- `C17`: Press down the tilt angle of 3248370_2 by 6 degrees
- `C18`: Decrease A3 Offset threshold for 3277614_1
- `C19`: Decrease transmission power for 3277614_1
- `C20`: Decrease transmission power for 3248370_2
- `C21`: Decrease A3 Offset threshold for 3248370_2
- `C22`: Adjust the azimuth of 3277614_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.737 | MS1 | 121.4656629396 | 31.1446210744 | 559 | 504990 | -87.10 | 13.47 | 583.85 | 0.16 | 2.99 | 1593 |
| 2024-09-20 22:21:32.291 | MS1 | 121.4656666118 | 31.1446223625 | 559 | 504990 | -86.99 | 14.50 | 386.43 | 0.15 | 2.96 | 1598 |
| 2024-09-20 22:21:33.215 | MS1 | 121.4656666886 | 31.1446317643 | 559 | 504990 | -90.57 | 13.25 | 523.34 | 0.10 | 2.70 | 1588 |
| 2024-09-20 22:21:34.719 | MS1 | 121.4656635775 | 31.1446283918 | 559 | 504990 | -90.84 | 16.57 | 50.24 | 0.19 | 2.83 | 480 |
| 2024-09-20 22:21:35.280 | MS1 | 121.4656755604 | 31.1446301037 | 559 | 504990 | -85.27 | 12.54 | 57.38 | 0.12 | 2.00 | 391 |
| 2024-09-20 22:21:36.308 | MS1 | 121.4656749861 | 31.1446355276 | 559 | 504990 | -85.04 | 17.30 | 95.75 | 0.13 | 2.14 | 400 |
| 2024-09-20 22:21:37.301 | MS1 | 121.4656634950 | 31.1446346269 | 559 | 504990 | -91.64 | 7.53 | 52.94 | 0.03 | 2.81 | 404 |
| 2024-09-20 22:21:38.959 | MS1 | 121.4656680514 | 31.1446362428 | 559 | 504990 | -89.66 | 12.83 | 72.52 | 0.08 | 2.75 | 408 |
| 2024-09-20 22:21:39.936 | MS1 | 121.4656662166 | 31.1446189544 | 559 | 504990 | -90.05 | 12.28 | 64.52 | 0.18 | 2.47 | 476 |
| 2024-09-20 22:21:40.477 | MS1 | 121.4656611777 | 31.1446334974 | 559 | 504990 | -89.81 | 10.81 | 524.78 | 0.09 | 2.77 | 1584 |
| 2024-09-20 22:21:41.631 | MS1 | 121.4656680955 | 31.1446297875 | 559 | 504990 | -93.23 | 12.02 | 388.29 | 0.06 | 2.52 | 1599 |
| 2024-09-20 22:21:42.750 | MS1 | 121.4656664884 | 31.1446365890 | 559 | 504990 | -89.27 | 12.20 | 311.62 | 0.07 | 2.17 | 1589 |

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
| 3210553 | 4 | 121.4695315609 | 31.1513402371 | 30 | 7 | 8 | 23.8 | TDD | 262 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3248370 | 2 | 121.4689302365 | 31.1539846467 | 147 | 5 | 4 | 27.2 | TDD | 559 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3256757 | 3 | 121.4751769853 | 31.1505758848 | 257 | 0 | 1 | 40.6 | TDD | 494 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3277614 | 1 | 121.4665713537 | 31.1450343668 | 328 | 8 | 4 | 37.1 | TDD | 491 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.591 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.615 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.761 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.761 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.461 | NREventA3 | measId:2;ServCellPCI:357;Se... |
| 2024-09-20 22:21:38.701 | NRHandoverAttempt | SourcePCI:357;SourceNR-ARFC... |
| 2024-09-20 22:21:38.741 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.753 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.896 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.896 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277614 | 1 | 10.4962 | 16.9682 | -115.9116 | 18.9600 | 157.2062 | 0.0029 | 0.0108 |
| 2024_09_20 22:00 | 3248370 | 2 | 6.0097 | 16.0637 | -116.9928 | 16.8898 | 84.5115 | 0.0133 | 0.0178 |
| 2024_09_20 22:00 | 3256757 | 3 | 5.6000 | 9.1476 | -117.3657 | 11.5807 | 134.9103 | 0.0027 | 0.0079 |
| 2024_09_20 22:00 | 3210553 | 4 | 6.9695 | 17.1394 | -117.0108 | 7.0352 | 126.1633 | 0.0078 | 0.0184 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413882_7E55463E | 504990 | 559 | -91.5 | 504990 | 491 | -95.7 | 504990 | 262 | -98.2 | 504990 | 494 |
| MR_1774413882_77760922 | 504990 | 559 | -92.2 | 504990 | 491 | -98.5 | 504990 | 262 | -98.7 | 504990 | 494 |
| MR_1774413882_0CCAD5EF | 504990 | 559 | -92.3 | 504990 | 491 | -97.9 | 504990 | 262 | -97.0 | 504990 | 494 |
| MR_1774413882_B881FA25 | 504990 | 559 | -91.0 | 504990 | 491 | -96.0 | 504990 | 262 | -100.1 | 504990 | 494 |
| MR_1774413882_2F06BC7E | 504990 | 559 | -90.6 | 504990 | 491 | -99.1 | 504990 | 262 | -98.6 | 504990 | 494 |
| MR_1774413882_ED53CE45 | 504990 | 559 | -92.1 | 504990 | 491 | -98.2 | 504990 | 262 | -97.4 | 504990 | 494 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1982: `b1fdc766-451...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b1fdc766-4516-47c4-80bf-564091867d9e` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease A3 Offset threshold for 3221911_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1982] topology](images/train_1982.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3233399_4
- `C2`: Increase A3 Offset threshold for 3221911_1
- `C3`: Lift the tilt angle  of 3233399_4 by 7 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221911_1
- `C5`: Add neighbor relationship between 3221911_1 and 3233399_4
- `C6`: Decrease A3 Offset threshold for 3221911_1 **← 정답**
- `C7`: Press down the tilt angle of 3221911_1 by 10 degrees
- `C8`: Press down the tilt angle  of 3233399_4 by 7 degrees
- `C9`: Check test server and transmission issues
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233399_4
- `C12`: Decrease transmission power for 3221911_1
- `C13`: Increase transmission power for 3221911_1
- `C14`: Adjust the azimuth of 3221911_1 by 47 degrees
- `C15`: Decrease transmission power for 3233399_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233399_4
- `C17`: Add neighbor relationship between 3227935_3 and 3233399_4
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221911_1
- `C19`: Adjust the azimuth of 3233399_4 by 50 degrees
- `C20`: Lift the tilt angle of 3221911_1 by 10 degrees
- `C21`: Decrease A3 Offset threshold for 3233399_4
- `C22`: Increase transmission power for 3233399_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.215 | MS1 | 121.4656734901 | 31.1446210395 | 426 | 504990 | -76.90 | 17.33 | 537.46 | 0.08 | 2.72 | 1593 |
| 2024-09-20 22:21:32.121 | MS1 | 121.4656679773 | 31.1446261211 | 426 | 504990 | -81.16 | 13.79 | 367.68 | 0.03 | 2.21 | 1583 |
| 2024-09-20 22:21:33.897 | MS1 | 121.4656748503 | 31.1446199126 | 426 | 504990 | -76.11 | 13.64 | 360.11 | 0.16 | 2.87 | 1595 |
| 2024-09-20 22:21:34.913 | MS1 | 121.4656748535 | 31.1446365419 | 426 | 504990 | -83.66 | -1.83 | 58.82 | 0.06 | 1.29 | 1566 |
| 2024-09-20 22:21:35.499 | MS1 | 121.4656749818 | 31.1446343677 | 426 | 504990 | -87.86 | -3.71 | 67.54 | 0.11 | 1.17 | 1579 |
| 2024-09-20 22:21:36.881 | MS1 | 121.4656732929 | 31.1446181047 | 426 | 504990 | -91.99 | -3.23 | 59.18 | 0.12 | 1.40 | 1561 |
| 2024-09-20 22:21:37.439 | MS1 | 121.4656728918 | 31.1446354523 | 426 | 504990 | -87.36 | -1.60 | 52.30 | 0.19 | 1.05 | 1586 |
| 2024-09-20 22:21:38.177 | MS1 | 121.4656620882 | 31.1446364011 | 426 | 504990 | -85.58 | -1.14 | 48.43 | 0.03 | 1.30 | 1573 |
| 2024-09-20 22:21:39.142 | MS1 | 121.4656738614 | 31.1446243542 | 815 | 504990 | -84.65 | 12.79 | 237.19 | 0.11 | 1.18 | 1564 |
| 2024-09-20 22:21:40.178 | MS1 | 121.4656665195 | 31.1446190758 | 815 | 504990 | -83.90 | 14.10 | 425.39 | 0.11 | 2.53 | 1563 |
| 2024-09-20 22:21:41.143 | MS1 | 121.4656683241 | 31.1446211807 | 815 | 504990 | -80.41 | 13.34 | 441.88 | 0.15 | 2.67 | 1598 |
| 2024-09-20 22:21:42.958 | MS1 | 121.4656617001 | 31.1446274748 | 815 | 504990 | -75.60 | 13.92 | 541.98 | 0.09 | 2.14 | 1595 |

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
| 3221911 | 1 | 121.4666785645 | 31.1482993792 | 146 | 5 | 3 | 38.6 | TDD | 426 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3226744 | 2 | 121.4680210218 | 31.1449162134 | 137 | 6 | 0 | 15.4 | TDD | 473 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3227935 | 3 | 121.4758651800 | 31.1476828553 | 223 | 5 | 9 | 32.3 | TDD | 162 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3233399 | 4 | 121.4697221342 | 31.1524821563 | 312 | 6 | 2 | 21.8 | TDD | 815 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.283 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.306 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.424 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.424 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.102 | NREventA3 | measId:2;ServCellPCI:456;Se... |
| 2024-09-20 22:21:38.342 | NRHandoverAttempt | SourcePCI:456;SourceNR-ARFC... |
| 2024-09-20 22:21:38.372 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.386 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.503 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.503 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221911 | 1 | 17.1226 | 5.7012 | -116.7782 | 16.3675 | 152.1930 | 0.0095 | 0.1739 |
| 2024_09_20 22:00 | 3226744 | 2 | 10.6669 | 10.8517 | -116.3836 | 6.6653 | 93.9865 | 0.0057 | 0.0045 |
| 2024_09_20 22:00 | 3227935 | 3 | 16.0107 | 15.0948 | -116.1473 | 16.9165 | 139.1449 | 0.0168 | 0.0122 |
| 2024_09_20 22:00 | 3233399 | 4 | 9.9887 | 9.7012 | -116.7011 | 9.2164 | 183.2116 | 0.0047 | 0.0062 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414067_C54F1800 | 504990 | 426 | -82.4 | 504990 | 815 | -77.8 | 504990 | 162 | -84.8 | 504990 | 473 |
| MR_1774414067_3B4CB852 | 504990 | 426 | -83.4 | 504990 | 815 | -79.3 | 504990 | 162 | -86.9 | 504990 | 473 |
| MR_1774414067_FEE55A64 | 504990 | 426 | -82.1 | 504990 | 815 | -77.7 | 504990 | 162 | -87.1 | 504990 | 473 |
| MR_1774414067_5677BAA0 | 504990 | 815 | -77.4 | 504990 | 426 | -85.5 | 504990 | 162 | -86.9 | 504990 | 473 |
| MR_1774414067_68516521 | 504990 | 815 | -77.6 | 504990 | 426 | -83.2 | 504990 | 162 | -87.1 | 504990 | 473 |
| MR_1774414067_51DC07D6 | 504990 | 815 | -79.8 | 504990 | 426 | -84.6 | 504990 | 162 | -85.9 | 504990 | 473 |
| MR_1774414067_31CA398C | 504990 | 815 | -81.0 | 504990 | 426 | -83.8 | 504990 | 162 | -83.4 | 504990 | 473 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1983: `91145a8b-32b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `91145a8b-32b3-4478-86f8-0a0f38ac4fe6` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229133_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1983] topology](images/train_1983.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3229133_5 by 2 degrees
- `C2`: Lift the tilt angle  of 3224349_3 by 5 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224349_3
- `C4`: Press down the tilt angle  of 3224349_3 by 5 degrees
- `C5`: Adjust the azimuth of 3229133_5 by 4 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229133_5
- `C7`: Increase transmission power for 3229133_5
- `C8`: Increase transmission power for 3224349_3
- `C9`: Add neighbor relationship between 3229133_5 and 3224349_3
- `C10`: Decrease transmission power for 3224349_3
- `C11`: Check test server and transmission issues
- `C12`: Decrease A3 Offset threshold for 3229133_5
- `C13`: Adjust the azimuth of 3224349_3 by 10 degrees
- `C14`: Press down the tilt angle of 3229133_5 by 2 degrees
- `C15`: Increase A3 Offset threshold for 3229133_5
- `C16`: Decrease transmission power for 3229133_5
- `C17`: Add neighbor relationship between 3241985_10 and 3224349_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224349_3
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase A3 Offset threshold for 3224349_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229133_5 **← 정답**
- `C22`: Decrease A3 Offset threshold for 3224349_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.844 | MS1 | 121.4656700190 | 31.1446272940 | 605 | 504990 | -94.50 | 13.56 | 328.59 | 0.11 | 2.27 | 1560 |
| 2024-09-20 22:21:32.385 | MS1 | 121.4656682382 | 31.1446369454 | 790 | 504990 | -95.90 | 12.41 | 350.49 | 0.10 | 2.72 | 1588 |
| 2024-09-20 22:21:33.327 | MS1 | 121.4656598083 | 31.1446357380 | 507 | 504990 | -95.88 | 9.09 | 531.16 | 0.01 | 2.97 | 1595 |
| 2024-09-20 22:21:34.628 | MS1 | 121.4656688297 | 31.1446321388 | 948 | 152650 | -93.90 | 3.15 | 85.91 | 0.15 | 1.93 | 905 |
| 2024-09-20 22:21:35.308 | MS1 | 121.4656589408 | 31.1446193616 | 587 | 152650 | -93.14 | 6.41 | 82.62 | 0.12 | 1.59 | 928 |
| 2024-09-20 22:21:36.460 | MS1 | 121.4656685679 | 31.1446374981 | 336 | 152650 | -89.47 | 4.82 | 90.27 | 0.06 | 1.70 | 905 |
| 2024-09-20 22:21:37.699 | MS1 | 121.4656627160 | 31.1446337372 | 341 | 152650 | -95.87 | 7.93 | 72.45 | 0.14 | 1.68 | 907 |
| 2024-09-20 22:21:38.913 | MS1 | 121.4656738857 | 31.1446326478 | 948 | 152650 | -91.74 | 6.39 | 95.17 | 0.18 | 1.65 | 908 |
| 2024-09-20 22:21:39.936 | MS1 | 121.4656715566 | 31.1446192421 | 587 | 152650 | -94.75 | 7.10 | 96.37 | 0.01 | 1.83 | 967 |
| 2024-09-20 22:21:40.485 | MS1 | 121.4656686003 | 31.1446305669 | 336 | 152650 | -96.78 | 2.94 | 57.19 | 0.06 | 2.31 | 1567 |
| 2024-09-20 22:21:41.434 | MS1 | 121.4656773441 | 31.1446181698 | 341 | 152650 | -93.81 | 6.28 | 88.71 | 0.07 | 2.42 | 1567 |
| 2024-09-20 22:21:42.432 | MS1 | 121.4656595802 | 31.1446351318 | 948 | 152650 | -92.43 | 7.95 | 63.09 | 0.00 | 2.02 | 1594 |

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
| 3216874 | 11 | 121.4738218577 | 31.1519332132 | 308 | 7 | 0 | 3.7 | FDD | 880 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3224349 | 3 | 121.4712326055 | 31.1458784455 | 265 | 3 | 11 | 19.5 | TDD | 312 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3229133 | 5 | 121.4650403938 | 31.1484241487 | 176 | 0 | 7 | 17.4 | TDD | 605 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3234229 | 4 | 121.4670023753 | 31.1553383270 | 199 | 10 | 0 | 29.6 | TDD | 507 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3240893 | 6 | 121.4669131953 | 31.1528815733 | 179 | 9 | 12 | 23.8 | TDD | 126 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3241985 | 10 | 121.4685201520 | 31.1482842970 | 43 | 0 | 4 | 4.1 | FDD | 336 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3245430 | 2 | 121.4721460654 | 31.1516997622 | 237 | 4 | 7 | 7.0 | TDD | 790 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3253948 | 8 | 121.4691033411 | 31.1512428955 | 262 | 10 | 12 | 5.3 | FDD | 587 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3257058 | 7 | 121.4640479684 | 31.1511036098 | 279 | 3 | 0 | 6.4 | FDD | 386 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3266355 | 1 | 121.4685481707 | 31.1490884228 | 256 | 12 | 12 | 5.4 | TDD | 739 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3273910 | 13 | 121.4719600498 | 31.1519276977 | 25 | 5 | 7 | 23.7 | FDD | 341 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3277430 | 12 | 121.4718739908 | 31.1444489741 | 238 | 8 | 11 | 2.3 | FDD | 948 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3279307 | 9 | 121.4660852233 | 31.1485708943 | 152 | 3 | 2 | 8.7 | FDD | 748 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |

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
| 2024-09-20 22:21:30.956 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.975 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.118 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.118 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.796 | NREventA2 | measId:1;ServCellPCI:778;Se... |
| 2024-09-20 22:21:34.943 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.239 | NREventA5 | measId:3;ServCellPCI:778;Se... |
| 2024-09-20 22:21:35.305 | NRHandoverAttempt | SourcePCI:778;SourceNR-ARFC... |
| 2024-09-20 22:21:35.346 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.358 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.507 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.507 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266355 | 1 | 9.2719 | 9.1484 | -114.3069 | 13.5544 | 128.9925 | 0.0006 | 0.0017 |
| 2024_09_20 22:00 | 3245430 | 2 | 6.9382 | 16.4910 | -115.5487 | 10.7988 | 169.7146 | 0.0175 | 0.0031 |
| 2024_09_20 22:00 | 3224349 | 3 | 11.5422 | 17.3001 | -116.8982 | 9.2637 | 175.1314 | 0.0144 | 0.0105 |
| 2024_09_20 22:00 | 3234229 | 4 | 5.1453 | 16.8255 | -116.6793 | 11.2055 | 155.3228 | 0.0159 | 0.0143 |
| 2024_09_20 22:00 | 3229133 | 5 | 16.1515 | 16.7152 | -114.2197 | 18.3393 | 198.7340 | 0.0012 | 0.0113 |
| 2024_09_20 22:00 | 3240893 | 6 | 11.3851 | 6.5117 | -115.0056 | 18.6576 | 120.3877 | 0.0046 | 0.0126 |
| 2024_09_20 22:00 | 3257058 | 7 | 19.0996 | 18.6242 | -114.3614 | 4.6031 | 56.6032 | 0.0148 | 0.0131 |
| 2024_09_20 22:00 | 3253948 | 8 | 15.9303 | 15.1261 | -115.5419 | 4.7981 | 34.7362 | 0.0184 | 0.0082 |
| 2024_09_20 22:00 | 3279307 | 9 | 6.7286 | 17.4201 | -114.6963 | 3.9433 | 32.0819 | 0.0190 | 0.0178 |
| 2024_09_20 22:00 | 3241985 | 10 | 19.8382 | 8.7273 | -114.8283 | 3.8642 | 21.5051 | 0.0011 | 0.0110 |
| 2024_09_20 22:00 | 3216874 | 11 | 12.1739 | 16.9685 | -114.0528 | 3.7824 | 32.1949 | 0.0162 | 0.0082 |
| 2024_09_20 22:00 | 3277430 | 12 | 18.7307 | 11.9364 | -115.3414 | 3.4575 | 36.7127 | 0.0156 | 0.0105 |
| 2024_09_20 22:00 | 3273910 | 13 | 5.7125 | 18.6161 | -117.3855 | 4.7445 | 26.0605 | 0.0021 | 0.0038 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413407_8630A87A | 504990 | 507 | -97.6 | 504990 | 312 | -95.2 | 504990 | 126 | -102.6 | 504990 | 739 |
| MR_1774413407_E16CE435 | 152650 | 948 | -92.8 | 152650 | 748 | -99.8 | 152650 | 880 | -100.6 | 152650 | 386 |
| MR_1774413407_7275CB23 | 504990 | 507 | -94.8 | 504990 | 312 | -95.8 | 504990 | 126 | -99.9 | 504990 | 739 |
| MR_1774413407_BB16D965 | 504990 | 507 | -94.8 | 504990 | 312 | -94.7 | 504990 | 126 | -103.3 | 504990 | 739 |
| MR_1774413407_0E7886AD | 504990 | 507 | -95.5 | 504990 | 312 | -93.4 | 504990 | 126 | -102.0 | 504990 | 739 |
| MR_1774413407_F2383602 | 152650 | 948 | -93.3 | 152650 | 748 | -97.3 | 152650 | 880 | -102.3 | 152650 | 386 |
| MR_1774413407_4FEA9F4B | 152650 | 948 | -94.4 | 152650 | 748 | -100.5 | 152650 | 880 | -103.1 | 152650 | 386 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1984: `2e324d3d-6f6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2e324d3d-6f65-44f6-a65e-855f16302715` |
| Tag | **multiple-answer** |
| 정답 | **C14|C19** |
| C14 의미 | Increase transmission power for 3247772_1 |
| C19 의미 | Adjust the azimuth of 3247772_1 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1984] topology](images/train_1984.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3247772_1
- `C2`: Check test server and transmission issues
- `C3`: Press down the tilt angle of 3247772_1 by 6 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247772_1
- `C5`: Increase A3 Offset threshold for 3270333_4
- `C6`: Decrease A3 Offset threshold for 3270333_4
- `C7`: Increase A3 Offset threshold for 3247772_1
- `C8`: Add neighbor relationship between 3247772_1 and 3270333_4
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Lift the tilt angle of 3247772_1 by 6 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270333_4
- `C12`: Increase transmission power for 3270333_4
- `C13`: Decrease transmission power for 3270333_4
- `C14`: Increase transmission power for 3247772_1 **← 정답**
- `C15`: Decrease A3 Offset threshold for 3247772_1
- `C16`: Adjust the azimuth of 3270333_4 by 40 degrees
- `C17`: Press down the tilt angle  of 3270333_4 by 3 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270333_4
- `C19`: Adjust the azimuth of 3247772_1 by 50 degrees **← 정답**
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247772_1
- `C21`: Add neighbor relationship between 3264392_2 and 3270333_4
- `C22`: Lift the tilt angle  of 3270333_4 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.331 | MS1 | 121.4656772994 | 31.1446202023 | 616 | 504990 | -86.34 | 13.89 | 351.66 | 0.07 | 2.86 | 1561 |
| 2024-09-20 22:21:32.467 | MS1 | 121.4656649783 | 31.1446184204 | 616 | 504990 | -85.97 | 13.88 | 372.39 | 0.05 | 2.61 | 1584 |
| 2024-09-20 22:21:33.805 | MS1 | 121.4656669040 | 31.1446349270 | 616 | 504990 | -88.44 | 12.68 | 580.01 | 0.03 | 2.63 | 1563 |
| 2024-09-20 22:21:34.269 | MS1 | 121.4656670519 | 31.1446356192 | 616 | 504990 | -100.56 | -0.95 | 42.22 | 0.04 | 1.02 | 1570 |
| 2024-09-20 22:21:35.810 | MS1 | 121.4656709823 | 31.1446241025 | 616 | 504990 | -109.17 | -1.24 | 34.55 | 0.03 | 1.47 | 1573 |
| 2024-09-20 22:21:36.191 | MS1 | 121.4656620273 | 31.1446305724 | 616 | 504990 | -104.96 | -1.80 | 52.49 | 0.04 | 1.25 | 1578 |
| 2024-09-20 22:21:37.643 | MS1 | 121.4656746651 | 31.1446181296 | 616 | 504990 | -102.19 | -1.16 | 72.29 | 0.10 | 1.38 | 1561 |
| 2024-09-20 22:21:38.943 | MS1 | 121.4656692960 | 31.1446353408 | 616 | 504990 | -108.37 | -0.50 | 28.86 | 0.02 | 1.45 | 1577 |
| 2024-09-20 22:21:39.663 | MS1 | 121.4656719258 | 31.1446339945 | 616 | 504990 | -109.66 | 0.86 | 78.97 | 0.08 | 1.06 | 1596 |
| 2024-09-20 22:21:40.100 | MS1 | 121.4656620561 | 31.1446367072 | 616 | 504990 | -90.56 | 14.77 | 532.95 | 0.10 | 2.44 | 1578 |
| 2024-09-20 22:21:41.340 | MS1 | 121.4656712501 | 31.1446315112 | 616 | 504990 | -93.19 | 15.06 | 387.61 | 0.06 | 2.78 | 1574 |
| 2024-09-20 22:21:42.343 | MS1 | 121.4656656004 | 31.1446329720 | 616 | 504990 | -94.36 | 16.11 | 557.09 | 0.09 | 2.02 | 1600 |

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
| 3247772 | 1 | 121.4691598391 | 31.1523750679 | 148 | 4 | 1 | 34.3 | TDD | 616 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3263658 | 3 | 121.4697282142 | 31.1455369472 | 304 | 14 | 10 | 35.6 | TDD | 602 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3264392 | 2 | 121.4660650502 | 31.1446220947 | 98 | 13 | 10 | 28.6 | TDD | 113 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3270333 | 4 | 121.4759243580 | 31.1448654754 | 309 | 1 | 4 | 27.9 | TDD | 972 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.476 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.495 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.640 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.640 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.808 | NREventA2 | measId:1;ServCellPCI:140;Se... |
| 2024-09-20 22:21:34.944 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247772 | 1 | 17.3173 | 18.6349 | -114.7112 | 16.0463 | 176.3872 | 0.1935 | 0.0091 |
| 2024_09_20 22:00 | 3264392 | 2 | 16.5393 | 15.3757 | -115.5644 | 15.1865 | 172.3634 | 0.0141 | 0.0187 |
| 2024_09_20 22:00 | 3263658 | 3 | 7.7920 | 17.4270 | -117.4195 | 15.7093 | 82.5499 | 0.0150 | 0.0060 |
| 2024_09_20 22:00 | 3270333 | 4 | 8.6360 | 12.5117 | -117.1917 | 13.1550 | 91.9893 | 0.0096 | 0.0014 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416966_6CB51093 | 504990 | 616 | -100.3 | 504990 | 972 | -107.0 | 504990 | 113 | -113.1 | 504990 | 602 |
| MR_1774416966_840635E1 | 504990 | 616 | -100.9 | 504990 | 972 | -106.9 | 504990 | 113 | -112.2 | 504990 | 602 |
| MR_1774416966_1EA75C9C | 504990 | 616 | -101.0 | 504990 | 972 | -108.0 | 504990 | 113 | -115.0 | 504990 | 602 |
| MR_1774416966_B8F23A65 | 504990 | 616 | -102.3 | 504990 | 972 | -106.5 | 504990 | 113 | -113.9 | 504990 | 602 |
| MR_1774416966_E2CD3021 | 504990 | 616 | -100.7 | 504990 | 972 | -106.6 | 504990 | 113 | -115.4 | 504990 | 602 |
| MR_1774416966_64583C79 | 504990 | 616 | -100.7 | 504990 | 972 | -108.2 | 504990 | 113 | -114.3 | 504990 | 602 |
| MR_1774416966_2B69A1BE | 504990 | 616 | -100.0 | 504990 | 972 | -109.0 | 504990 | 113 | -114.0 | 504990 | 602 |
| MR_1774416966_A9BE8D79 | 504990 | 616 | -101.1 | 504990 | 972 | -107.1 | 504990 | 113 | -114.9 | 504990 | 602 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1985: `1af10cf0-d48...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1af10cf0-d489-46b2-b4ae-20c1b74d12aa` |
| Tag | **multiple-answer** |
| 정답 | **C1|C12|C20|C21** |
| C1 의미 | Increase A3 Offset threshold for 3275999_3 |
| C12 의미 | Decrease transmission power for 3217288_5 |
| C20 의미 | Press down the tilt angle  of 3217288_5 by 5 degrees |
| C21 의미 | Increase A3 Offset threshold for 3217288_5 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1985] topology](images/train_1985.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3275999_3 **← 정답**
- `C2`: Decrease A3 Offset threshold for 3217288_5
- `C3`: Add neighbor relationship between 3275999_3 and 3217288_5
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275999_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217288_5
- `C6`: Lift the tilt angle  of 3217288_5 by 5 degrees
- `C7`: Increase transmission power for 3275999_3
- `C8`: Lift the tilt angle of 3275999_3 by 4 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Add neighbor relationship between 3236687_1 and 3217288_5
- `C11`: Adjust the azimuth of 3217288_5 by 30 degrees
- `C12`: Decrease transmission power for 3217288_5 **← 정답**
- `C13`: Adjust the azimuth of 3275999_3 by 22 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217288_5
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275999_3
- `C16`: Decrease A3 Offset threshold for 3275999_3
- `C17`: Decrease transmission power for 3275999_3
- `C18`: Press down the tilt angle of 3275999_3 by 4 degrees
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle  of 3217288_5 by 5 degrees **← 정답**
- `C21`: Increase A3 Offset threshold for 3217288_5 **← 정답**
- `C22`: Increase transmission power for 3217288_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.976 | MS1 | 121.4656647374 | 31.1446365412 | 271 | 504990 | -78.98 | 16.55 | 374.73 | 0.17 | 2.73 | 1563 |
| 2024-09-20 22:21:32.511 | MS1 | 121.4656708643 | 31.1446213705 | 271 | 504990 | -77.33 | 16.03 | 467.88 | 0.18 | 2.84 | 1574 |
| 2024-09-20 22:21:33.101 | MS1 | 121.4656599129 | 31.1446241119 | 271 | 504990 | -77.58 | 16.61 | 405.57 | 0.03 | 2.96 | 1576 |
| 2024-09-20 22:21:34.829 | MS1 | 121.4656581110 | 31.1446213901 | 88 | 504990 | -86.52 | 1.24 | 36.94 | 0.06 | 1.26 | 1565 |
| 2024-09-20 22:21:35.708 | MS1 | 121.4656689771 | 31.1446199084 | 88 | 504990 | -86.81 | 3.84 | 49.04 | 0.18 | 1.39 | 1565 |
| 2024-09-20 22:21:36.293 | MS1 | 121.4656772055 | 31.1446362853 | 271 | 504990 | -86.85 | 2.60 | 83.49 | 0.03 | 1.11 | 1563 |
| 2024-09-20 22:21:37.759 | MS1 | 121.4656767302 | 31.1446324962 | 271 | 504990 | -88.35 | 1.86 | 38.79 | 0.15 | 1.32 | 1599 |
| 2024-09-20 22:21:38.132 | MS1 | 121.4656611259 | 31.1446323847 | 88 | 504990 | -82.68 | 1.19 | 71.03 | 0.06 | 1.01 | 1576 |
| 2024-09-20 22:21:39.316 | MS1 | 121.4656661879 | 31.1446290107 | 88 | 504990 | -84.45 | 2.63 | 68.72 | 0.11 | 1.08 | 1589 |
| 2024-09-20 22:21:40.877 | MS1 | 121.4656777487 | 31.1446202616 | 88 | 504990 | -84.52 | 12.01 | 404.08 | 0.18 | 2.07 | 1590 |
| 2024-09-20 22:21:41.255 | MS1 | 121.4656735632 | 31.1446356339 | 88 | 504990 | -79.70 | 14.48 | 504.19 | 0.04 | 2.93 | 1569 |
| 2024-09-20 22:21:42.210 | MS1 | 121.4656614273 | 31.1446270002 | 88 | 504990 | -80.42 | 12.89 | 325.74 | 0.05 | 2.83 | 1570 |

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
| 3210300 | 2 | 121.4714997095 | 31.1554604372 | 298 | 9 | 1 | 49.3 | TDD | 333 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3217288 | 5 | 121.4653924362 | 31.1522210321 | 208 | 3 | 1 | 23.9 | TDD | 798 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3236687 | 1 | 121.4708484843 | 31.1517521748 | 161 | 7 | 10 | 36.2 | TDD | 714 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3249366 | 4 | 121.4689300077 | 31.1454351070 | 109 | 8 | 5 | 39.5 | TDD | 88 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3275999 | 3 | 121.4732375968 | 31.1502276310 | 251 | 2 | 9 | 35.3 | TDD | 271 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.853 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.868 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.983 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.983 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.666 | NREventA3 | measId:2;ServCellPCI:441;Se... |
| 2024-09-20 22:21:33.906 | NRHandoverAttempt | SourcePCI:441;SourceNR-ARFC... |
| 2024-09-20 22:21:33.954 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:33.967 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:34.077 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.077 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.666 | NREventA3 | measId:2;ServCellPCI:898;Se... |
| 2024-09-20 22:21:35.906 | NRHandoverAttempt | SourcePCI:898;SourceNR-ARFC... |
| 2024-09-20 22:21:35.942 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.957 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.090 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.090 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.666 | NREventA3 | measId:2;ServCellPCI:441;Se... |
| 2024-09-20 22:21:37.906 | NRHandoverAttempt | SourcePCI:441;SourceNR-ARFC... |
| 2024-09-20 22:21:37.942 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.954 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.068 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.068 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236687 | 1 | 17.5460 | 9.5500 | -117.3681 | 18.8574 | 197.8892 | 0.0089 | 0.0196 |
| 2024_09_20 22:00 | 3210300 | 2 | 16.9597 | 15.8937 | -116.0909 | 16.8857 | 145.9261 | 0.0083 | 0.0180 |
| 2024_09_20 22:00 | 3275999 | 3 | 9.8386 | 13.7478 | -116.5388 | 10.2128 | 113.5488 | 0.0156 | 0.0162 |
| 2024_09_20 22:00 | 3249366 | 4 | 5.4691 | 13.1380 | -114.6165 | 8.1548 | 145.1037 | 0.0135 | 0.0191 |
| 2024_09_20 22:00 | 3217288 | 5 | 15.4189 | 8.1058 | -116.8666 | 5.1306 | 123.7003 | 0.0096 | 0.0037 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415000_B22E9FAE | 504990 | 271 | -86.6 | 504990 | 88 | -87.2 | 504990 | 798 | -91.2 | 504990 | 714 |
| MR_1774415000_CDB684DA | 504990 | 271 | -85.3 | 504990 | 88 | -87.6 | 504990 | 798 | -92.1 | 504990 | 714 |
| MR_1774415000_692EA225 | 504990 | 88 | -85.5 | 504990 | 271 | -86.7 | 504990 | 798 | -91.2 | 504990 | 714 |
| MR_1774415000_C21CC8C9 | 504990 | 88 | -84.5 | 504990 | 271 | -87.6 | 504990 | 798 | -91.0 | 504990 | 714 |
| MR_1774415000_B6DC81AC | 504990 | 88 | -85.0 | 504990 | 271 | -87.0 | 504990 | 798 | -90.7 | 504990 | 714 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1986: `a0c6c2d5-6bb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a0c6c2d5-6bbd-4cbf-882d-32766ef81011` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3264744_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1986] topology](images/train_1986.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3264744_4
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Adjust the azimuth of 3219732_2 by 50 degrees
- `C4`: Add neighbor relationship between 3216430_1 and 3219732_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264744_4 **← 정답**
- `C6`: Add neighbor relationship between 3264744_4 and 3219732_2
- `C7`: Increase A3 Offset threshold for 3264744_4
- `C8`: Press down the tilt angle of 3264744_4 by 3 degrees
- `C9`: Decrease transmission power for 3264744_4
- `C10`: Adjust the azimuth of 3264744_4 by 35 degrees
- `C11`: Increase transmission power for 3219732_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219732_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219732_2
- `C14`: Lift the tilt angle of 3264744_4 by 3 degrees
- `C15`: Check test server and transmission issues
- `C16`: Press down the tilt angle  of 3219732_2 by 7 degrees
- `C17`: Lift the tilt angle  of 3219732_2 by 7 degrees
- `C18`: Decrease A3 Offset threshold for 3264744_4
- `C19`: Decrease A3 Offset threshold for 3219732_2
- `C20`: Decrease transmission power for 3219732_2
- `C21`: Increase A3 Offset threshold for 3219732_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264744_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.608 | MS1 | 121.4656708014 | 31.1446315122 | 758 | 504990 | -86.20 | 13.15 | 490.59 | 0.10 | 2.95 | 1566 |
| 2024-09-20 22:21:32.141 | MS1 | 121.4656724937 | 31.1446299553 | 758 | 504990 | -86.03 | 13.89 | 345.09 | 0.15 | 2.91 | 1596 |
| 2024-09-20 22:21:33.694 | MS1 | 121.4656765378 | 31.1446284415 | 758 | 504990 | -87.24 | 16.60 | 552.49 | 0.03 | 2.54 | 1582 |
| 2024-09-20 22:21:34.279 | MS1 | 121.4656625704 | 31.1446269251 | 758 | 504990 | -87.24 | 16.67 | 69.66 | 0.68 | 2.68 | 605 |
| 2024-09-20 22:21:35.625 | MS1 | 121.4656688043 | 31.1446301876 | 758 | 504990 | -91.36 | 14.91 | 99.22 | 0.66 | 2.67 | 587 |
| 2024-09-20 22:21:36.205 | MS1 | 121.4656707056 | 31.1446311411 | 758 | 504990 | -87.75 | 17.51 | 88.64 | 0.62 | 2.88 | 633 |
| 2024-09-20 22:21:37.503 | MS1 | 121.4656696429 | 31.1446189271 | 758 | 504990 | -92.81 | 9.92 | 84.65 | 0.59 | 2.71 | 550 |
| 2024-09-20 22:21:38.157 | MS1 | 121.4656646714 | 31.1446330514 | 758 | 504990 | -91.18 | 12.99 | 93.55 | 0.62 | 2.29 | 515 |
| 2024-09-20 22:21:39.973 | MS1 | 121.4656611754 | 31.1446374596 | 758 | 504990 | -89.35 | 9.03 | 64.07 | 0.66 | 2.63 | 673 |
| 2024-09-20 22:21:40.968 | MS1 | 121.4656670233 | 31.1446313779 | 758 | 504990 | -93.82 | 7.38 | 497.79 | 0.13 | 2.36 | 1574 |
| 2024-09-20 22:21:41.717 | MS1 | 121.4656762038 | 31.1446274470 | 758 | 504990 | -92.49 | 12.33 | 561.45 | 0.13 | 2.40 | 1599 |
| 2024-09-20 22:21:42.113 | MS1 | 121.4656636030 | 31.1446212113 | 758 | 504990 | -91.38 | 8.30 | 393.04 | 0.11 | 2.86 | 1600 |

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
| 3216430 | 1 | 121.4709592269 | 31.1463998012 | 206 | 10 | 9 | 46.5 | TDD | 602 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3219732 | 2 | 121.4672151953 | 31.1554854639 | 72 | 6 | 1 | 24.5 | TDD | 53 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3222051 | 3 | 121.4752546407 | 31.1456284496 | 311 | 1 | 8 | 29.0 | TDD | 102 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3264744 | 4 | 121.4693663234 | 31.1527376467 | 236 | 1 | 11 | 35.0 | TDD | 758 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.333 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.356 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.495 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.495 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.177 | NREventA3 | measId:2;ServCellPCI:838;Se... |
| 2024-09-20 22:21:38.417 | NRHandoverAttempt | SourcePCI:838;SourceNR-ARFC... |
| 2024-09-20 22:21:38.467 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.477 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.591 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.591 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216430 | 1 | 19.2037 | 9.3152 | -114.3075 | 17.2581 | 121.3211 | 0.0155 | 0.0036 |
| 2024_09_20 22:00 | 3219732 | 2 | 9.8699 | 6.2899 | -116.5128 | 7.6925 | 160.5305 | 0.0176 | 0.0148 |
| 2024_09_20 22:00 | 3222051 | 3 | 13.0338 | 7.0275 | -114.8411 | 14.9304 | 172.8053 | 0.0103 | 0.0087 |
| 2024_09_20 22:00 | 3264744 | 4 | 10.8572 | 18.8261 | -114.6608 | 12.8271 | 168.4986 | 0.0153 | 0.0163 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412229_536E5D54 | 504990 | 758 | -89.1 | 504990 | 53 | -91.2 | 504990 | 602 | -97.8 | 504990 | 102 |
| MR_1774412229_B01C8ED9 | 504990 | 758 | -88.7 | 504990 | 53 | -91.5 | 504990 | 602 | -98.6 | 504990 | 102 |
| MR_1774412229_85EC4B08 | 504990 | 758 | -86.4 | 504990 | 53 | -89.5 | 504990 | 602 | -97.8 | 504990 | 102 |
| MR_1774412229_5CBA2D99 | 504990 | 758 | -87.3 | 504990 | 53 | -87.7 | 504990 | 602 | -101.3 | 504990 | 102 |
| MR_1774412229_673B56E5 | 504990 | 758 | -87.7 | 504990 | 53 | -91.2 | 504990 | 602 | -98.3 | 504990 | 102 |
| MR_1774412229_77A85FF6 | 504990 | 758 | -88.9 | 504990 | 53 | -89.3 | 504990 | 602 | -100.6 | 504990 | 102 |
| MR_1774412229_4D97C37C | 504990 | 758 | -85.6 | 504990 | 53 | -90.4 | 504990 | 602 | -98.5 | 504990 | 102 |
| MR_1774412229_1825D803 | 504990 | 758 | -87.9 | 504990 | 53 | -87.7 | 504990 | 602 | -100.7 | 504990 | 102 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1987: `8b3fe37f-9fe...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8b3fe37f-9fed-4ca1-bc09-937ca5437c06` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1987] topology](images/train_1987.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3219258_1
- `C2`: Decrease A3 Offset threshold for 3219258_1
- `C3`: Lift the tilt angle  of 3222517_3 by 10 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219258_1
- `C5`: Press down the tilt angle of 3219258_1 by 10 degrees
- `C6`: Decrease transmission power for 3222517_3
- `C7`: Increase A3 Offset threshold for 3219258_1
- `C8`: Increase transmission power for 3222517_3
- `C9`: Lift the tilt angle of 3219258_1 by 10 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Add neighbor relationship between 3219258_1 and 3222517_3
- `C12`: Increase A3 Offset threshold for 3222517_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222517_3
- `C14`: Adjust the azimuth of 3219258_1 by 50 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222517_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219258_1
- `C17`: Add neighbor relationship between 3239534_2 and 3222517_3
- `C18`: Decrease transmission power for 3219258_1
- `C19`: Press down the tilt angle  of 3222517_3 by 10 degrees
- `C20`: Adjust the azimuth of 3222517_3 by 50 degrees
- `C21`: Check test server and transmission issues **← 정답**
- `C22`: Decrease A3 Offset threshold for 3222517_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.327 | MS1 | 121.4656649667 | 31.1446369878 | 488 | 504990 | -86.53 | 14.91 | 579.15 | 0.05 | 2.73 | 1584 |
| 2024-09-20 22:21:32.524 | MS1 | 121.4656599615 | 31.1446309390 | 488 | 504990 | -86.58 | 13.75 | 560.57 | 0.06 | 2.58 | 1564 |
| 2024-09-20 22:21:33.113 | MS1 | 121.4656616010 | 31.1446289476 | 488 | 504990 | -87.70 | 15.09 | 461.50 | 0.02 | 2.22 | 1582 |
| 2024-09-20 22:21:34.776 | MS1 | 121.4656762276 | 31.1446269324 | 488 | 504990 | -85.28 | 13.89 | 79.29 | 0.12 | 2.64 | 442 |
| 2024-09-20 22:21:35.845 | MS1 | 121.4656756911 | 31.1446327275 | 488 | 504990 | -89.06 | 15.80 | 85.50 | 0.10 | 2.13 | 405 |
| 2024-09-20 22:21:36.761 | MS1 | 121.4656735745 | 31.1446253731 | 488 | 504990 | -85.48 | 15.63 | 101.48 | 0.16 | 2.03 | 378 |
| 2024-09-20 22:21:37.603 | MS1 | 121.4656610866 | 31.1446365297 | 488 | 504990 | -89.14 | 10.06 | 53.71 | 0.13 | 2.08 | 380 |
| 2024-09-20 22:21:38.329 | MS1 | 121.4656755808 | 31.1446214174 | 488 | 504990 | -91.57 | 8.96 | 78.46 | 0.18 | 2.76 | 457 |
| 2024-09-20 22:21:39.368 | MS1 | 121.4656685618 | 31.1446211432 | 488 | 504990 | -91.15 | 11.07 | 52.70 | 0.18 | 2.57 | 413 |
| 2024-09-20 22:21:40.675 | MS1 | 121.4656621385 | 31.1446184288 | 488 | 504990 | -90.70 | 8.93 | 425.46 | 0.10 | 2.03 | 1562 |
| 2024-09-20 22:21:41.257 | MS1 | 121.4656655271 | 31.1446284831 | 488 | 504990 | -89.00 | 7.59 | 424.09 | 0.00 | 2.93 | 1573 |
| 2024-09-20 22:21:42.658 | MS1 | 121.4656761362 | 31.1446225623 | 488 | 504990 | -89.75 | 8.31 | 311.37 | 0.12 | 2.23 | 1566 |

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
| 3219258 | 1 | 121.4650583545 | 31.1460692230 | 341 | 10 | 8 | 31.6 | TDD | 488 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3222517 | 3 | 121.4741121572 | 31.1476442478 | 99 | 8 | 0 | 29.1 | TDD | 403 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3239534 | 2 | 121.4686147347 | 31.1476407075 | 316 | 4 | 1 | 48.5 | TDD | 298 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3250012 | 4 | 121.4673736286 | 31.1506965768 | 340 | 14 | 9 | 49.5 | TDD | 591 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.090 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.111 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.237 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.237 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.958 | NREventA3 | measId:2;ServCellPCI:734;Se... |
| 2024-09-20 22:21:38.198 | NRHandoverAttempt | SourcePCI:734;SourceNR-ARFC... |
| 2024-09-20 22:21:38.243 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.254 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.359 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.359 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219258 | 1 | 7.4637 | 16.9966 | -116.7878 | 12.6549 | 91.9902 | 0.0119 | 0.0176 |
| 2024_09_20 22:00 | 3239534 | 2 | 14.8627 | 7.9706 | -114.3883 | 9.8424 | 166.0147 | 0.0163 | 0.0111 |
| 2024_09_20 22:00 | 3222517 | 3 | 12.4427 | 12.5098 | -116.2260 | 11.4779 | 169.9543 | 0.0021 | 0.0101 |
| 2024_09_20 22:00 | 3250012 | 4 | 14.1781 | 13.2979 | -117.2120 | 12.0894 | 91.5045 | 0.0124 | 0.0085 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412033_54574C3D | 504990 | 488 | -85.1 | 504990 | 403 | -86.7 | 504990 | 298 | -92.3 | 504990 | 591 |
| MR_1774412033_FC50E6FF | 504990 | 488 | -87.1 | 504990 | 403 | -86.1 | 504990 | 298 | -94.2 | 504990 | 591 |
| MR_1774412033_9CA86654 | 504990 | 488 | -85.0 | 504990 | 403 | -87.6 | 504990 | 298 | -93.3 | 504990 | 591 |
| MR_1774412033_77A8C99C | 504990 | 488 | -85.6 | 504990 | 403 | -85.7 | 504990 | 298 | -92.0 | 504990 | 591 |
| MR_1774412033_149FB0E4 | 504990 | 488 | -84.3 | 504990 | 403 | -86.2 | 504990 | 298 | -94.0 | 504990 | 591 |
| MR_1774412033_12831B0A | 504990 | 488 | -85.0 | 504990 | 403 | -85.7 | 504990 | 298 | -92.8 | 504990 | 591 |
| MR_1774412033_F36CD800 | 504990 | 488 | -86.1 | 504990 | 403 | -85.9 | 504990 | 298 | -93.7 | 504990 | 591 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1988: `67b07e0e-985...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `67b07e0e-985c-41ea-8af3-5a4c4c597052` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3270772_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1988] topology](images/train_1988.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3279492_3 by 50 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270772_1
- `C3`: Adjust the azimuth of 3270772_1 by 10 degrees
- `C4`: Press down the tilt angle  of 3279492_3 by 2 degrees
- `C5`: Lift the tilt angle of 3270772_1 by 4 degrees
- `C6`: Increase transmission power for 3270772_1
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Add neighbor relationship between 3262665_2 and 3279492_3
- `C9`: Decrease transmission power for 3270772_1
- `C10`: Decrease A3 Offset threshold for 3279492_3
- `C11`: Increase A3 Offset threshold for 3270772_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270772_1 **← 정답**
- `C13`: Decrease A3 Offset threshold for 3270772_1
- `C14`: Increase A3 Offset threshold for 3279492_3
- `C15`: Check test server and transmission issues
- `C16`: Decrease transmission power for 3279492_3
- `C17`: Lift the tilt angle  of 3279492_3 by 2 degrees
- `C18`: Add neighbor relationship between 3270772_1 and 3279492_3
- `C19`: Increase transmission power for 3279492_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279492_3
- `C21`: Press down the tilt angle of 3270772_1 by 4 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279492_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.218 | MS1 | 121.4656740584 | 31.1446339136 | 778 | 504990 | -90.27 | 16.64 | 484.11 | 0.17 | 2.17 | 1582 |
| 2024-09-20 22:21:32.521 | MS1 | 121.4656751540 | 31.1446185042 | 778 | 504990 | -87.88 | 16.92 | 329.69 | 0.06 | 2.88 | 1587 |
| 2024-09-20 22:21:33.649 | MS1 | 121.4656680150 | 31.1446201698 | 778 | 504990 | -91.57 | 12.77 | 326.86 | 0.11 | 2.21 | 1596 |
| 2024-09-20 22:21:34.900 | MS1 | 121.4656739195 | 31.1446286888 | 778 | 504990 | -88.34 | 16.40 | 57.14 | 0.52 | 2.72 | 530 |
| 2024-09-20 22:21:35.409 | MS1 | 121.4656633206 | 31.1446370905 | 778 | 504990 | -90.33 | 15.67 | 102.14 | 0.67 | 2.25 | 603 |
| 2024-09-20 22:21:36.883 | MS1 | 121.4656617959 | 31.1446276081 | 778 | 504990 | -86.83 | 15.04 | 76.58 | 0.61 | 2.05 | 573 |
| 2024-09-20 22:21:37.701 | MS1 | 121.4656701403 | 31.1446358276 | 778 | 504990 | -91.89 | 11.92 | 65.16 | 0.55 | 2.25 | 620 |
| 2024-09-20 22:21:38.794 | MS1 | 121.4656648937 | 31.1446289293 | 778 | 504990 | -91.28 | 8.99 | 96.71 | 0.56 | 2.90 | 519 |
| 2024-09-20 22:21:39.467 | MS1 | 121.4656609954 | 31.1446288256 | 778 | 504990 | -91.46 | 10.29 | 78.98 | 0.53 | 2.13 | 677 |
| 2024-09-20 22:21:40.210 | MS1 | 121.4656705403 | 31.1446221397 | 778 | 504990 | -90.46 | 10.79 | 368.61 | 0.03 | 2.60 | 1590 |
| 2024-09-20 22:21:41.535 | MS1 | 121.4656690036 | 31.1446234628 | 778 | 504990 | -91.45 | 8.28 | 535.77 | 0.03 | 2.14 | 1585 |
| 2024-09-20 22:21:42.751 | MS1 | 121.4656591954 | 31.1446347344 | 778 | 504990 | -90.27 | 11.72 | 543.73 | 0.14 | 2.40 | 1575 |

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
| 3235171 | 4 | 121.4746439279 | 31.1524407670 | 170 | 10 | 6 | 29.8 | TDD | 335 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3262665 | 2 | 121.4740165522 | 31.1543624478 | 172 | 14 | 10 | 29.9 | TDD | 540 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3270772 | 1 | 121.4733989971 | 31.1542109293 | 205 | 3 | 6 | 22.1 | TDD | 778 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3279492 | 3 | 121.4689713718 | 31.1493578713 | 334 | 0 | 12 | 20.3 | TDD | 623 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.129 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.146 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.255 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.255 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.992 | NREventA3 | measId:2;ServCellPCI:155;Se... |
| 2024-09-20 22:21:38.232 | NRHandoverAttempt | SourcePCI:155;SourceNR-ARFC... |
| 2024-09-20 22:21:38.280 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.294 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.405 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.405 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270772 | 1 | 18.9557 | 12.1294 | -117.2811 | 13.5906 | 92.3862 | 0.0072 | 0.0088 |
| 2024_09_20 22:00 | 3262665 | 2 | 11.5439 | 17.2913 | -117.0620 | 14.8798 | 159.2348 | 0.0080 | 0.0170 |
| 2024_09_20 22:00 | 3279492 | 3 | 11.1841 | 15.5620 | -114.2669 | 5.7223 | 150.2197 | 0.0080 | 0.0009 |
| 2024_09_20 22:00 | 3235171 | 4 | 6.6064 | 11.0794 | -116.1190 | 7.2845 | 196.3454 | 0.0044 | 0.0063 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416685_C5D7DBAB | 504990 | 778 | -88.3 | 504990 | 623 | -97.0 | 504990 | 540 | -97.4 | 504990 | 335 |
| MR_1774416685_A28174A5 | 504990 | 778 | -86.8 | 504990 | 623 | -95.1 | 504990 | 540 | -97.4 | 504990 | 335 |
| MR_1774416685_4E40910B | 504990 | 778 | -88.4 | 504990 | 623 | -95.0 | 504990 | 540 | -98.2 | 504990 | 335 |
| MR_1774416685_02A12BEF | 504990 | 778 | -90.2 | 504990 | 623 | -95.7 | 504990 | 540 | -98.1 | 504990 | 335 |
| MR_1774416685_3351B9C0 | 504990 | 778 | -88.6 | 504990 | 623 | -97.4 | 504990 | 540 | -97.8 | 504990 | 335 |
| MR_1774416685_BA73B8D9 | 504990 | 778 | -90.0 | 504990 | 623 | -95.1 | 504990 | 540 | -97.8 | 504990 | 335 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1989: `78172d11-358...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `78172d11-3589-44b2-876b-9fdfbf4ae626` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Decrease A3 Offset threshold for 3228767_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1989] topology](images/train_1989.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3269556_4
- `C2`: Increase A3 Offset threshold for 3228767_2
- `C3`: Increase A3 Offset threshold for 3269556_4
- `C4`: Decrease A3 Offset threshold for 3269556_4
- `C5`: Adjust the azimuth of 3228767_2 by 50 degrees
- `C6`: Decrease transmission power for 3228767_2
- `C7`: Lift the tilt angle  of 3269556_4 by 1 degrees
- `C8`: Add neighbor relationship between 3261722_3 and 3269556_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228767_2
- `C10`: Check test server and transmission issues
- `C11`: Lift the tilt angle of 3228767_2 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228767_2
- `C13`: Press down the tilt angle of 3228767_2 by 10 degrees
- `C14`: Decrease transmission power for 3269556_4
- `C15`: Add neighbor relationship between 3228767_2 and 3269556_4
- `C16`: Increase transmission power for 3228767_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269556_4
- `C18`: Decrease A3 Offset threshold for 3228767_2 **← 정답**
- `C19`: Adjust the azimuth of 3269556_4 by 47 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Press down the tilt angle  of 3269556_4 by 1 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269556_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.441 | MS1 | 121.4656604530 | 31.1446236131 | 641 | 504990 | -77.98 | 13.38 | 387.93 | 0.06 | 2.31 | 1565 |
| 2024-09-20 22:21:32.908 | MS1 | 121.4656662424 | 31.1446272307 | 641 | 504990 | -82.10 | 14.96 | 465.94 | 0.03 | 2.57 | 1577 |
| 2024-09-20 22:21:33.841 | MS1 | 121.4656667087 | 31.1446340614 | 641 | 504990 | -80.83 | 17.08 | 321.39 | 0.02 | 2.90 | 1561 |
| 2024-09-20 22:21:34.897 | MS1 | 121.4656744057 | 31.1446353889 | 641 | 504990 | -90.86 | -3.16 | 53.16 | 0.15 | 1.17 | 1582 |
| 2024-09-20 22:21:35.744 | MS1 | 121.4656684046 | 31.1446221268 | 641 | 504990 | -87.57 | -2.96 | 46.58 | 0.11 | 1.08 | 1584 |
| 2024-09-20 22:21:36.106 | MS1 | 121.4656611542 | 31.1446188017 | 641 | 504990 | -85.14 | -0.78 | 61.18 | 0.04 | 1.16 | 1598 |
| 2024-09-20 22:21:37.586 | MS1 | 121.4656669078 | 31.1446242316 | 641 | 504990 | -83.11 | -2.11 | 27.85 | 0.17 | 1.36 | 1582 |
| 2024-09-20 22:21:38.350 | MS1 | 121.4656680881 | 31.1446222822 | 641 | 504990 | -86.84 | -3.07 | 70.90 | 0.06 | 1.33 | 1580 |
| 2024-09-20 22:21:39.295 | MS1 | 121.4656655414 | 31.1446260328 | 365 | 504990 | -77.05 | 12.86 | 260.41 | 0.10 | 1.17 | 1573 |
| 2024-09-20 22:21:40.569 | MS1 | 121.4656625016 | 31.1446206006 | 365 | 504990 | -79.39 | 15.46 | 420.11 | 0.06 | 2.03 | 1573 |
| 2024-09-20 22:21:41.620 | MS1 | 121.4656645730 | 31.1446201824 | 365 | 504990 | -84.61 | 14.49 | 394.91 | 0.03 | 2.43 | 1579 |
| 2024-09-20 22:21:42.350 | MS1 | 121.4656600965 | 31.1446209994 | 365 | 504990 | -82.58 | 13.89 | 328.75 | 0.20 | 2.65 | 1583 |

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
| 3228767 | 2 | 121.4690242646 | 31.1475443536 | 143 | 14 | 5 | 28.0 | TDD | 641 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3260277 | 1 | 121.4721459141 | 31.1479127132 | 152 | 5 | 8 | 24.3 | TDD | 680 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3261722 | 3 | 121.4727728319 | 31.1534355302 | 177 | 7 | 3 | 40.2 | TDD | 82 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3269556 | 4 | 121.4740717558 | 31.1485650081 | 194 | 0 | 0 | 17.2 | TDD | 365 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.375 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.395 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.519 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.519 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.251 | NREventA3 | measId:2;ServCellPCI:385;Se... |
| 2024-09-20 22:21:38.491 | NRHandoverAttempt | SourcePCI:385;SourceNR-ARFC... |
| 2024-09-20 22:21:38.539 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.553 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.684 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.684 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260277 | 1 | 16.0948 | 12.9394 | -115.5953 | 15.6779 | 118.0119 | 0.0175 | 0.0043 |
| 2024_09_20 22:00 | 3228767 | 2 | 14.2773 | 11.1559 | -114.0341 | 16.2942 | 183.9420 | 0.0159 | 0.1278 |
| 2024_09_20 22:00 | 3261722 | 3 | 18.9247 | 14.7343 | -114.1279 | 14.9906 | 119.6181 | 0.0003 | 0.0155 |
| 2024_09_20 22:00 | 3269556 | 4 | 16.2584 | 8.4988 | -115.9088 | 11.1762 | 195.3260 | 0.0147 | 0.0142 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414116_AA23DAF5 | 504990 | 641 | -90.2 | 504990 | 365 | -84.7 | 504990 | 82 | -85.6 | 504990 | 680 |
| MR_1774414116_5379BC49 | 504990 | 641 | -91.0 | 504990 | 365 | -84.9 | 504990 | 82 | -84.1 | 504990 | 680 |
| MR_1774414116_CA1D58A1 | 504990 | 641 | -90.9 | 504990 | 365 | -83.9 | 504990 | 82 | -85.3 | 504990 | 680 |
| MR_1774414116_943BBE0A | 504990 | 365 | -84.3 | 504990 | 641 | -91.9 | 504990 | 82 | -86.5 | 504990 | 680 |
| MR_1774414116_70BD6178 | 504990 | 365 | -86.6 | 504990 | 641 | -91.5 | 504990 | 82 | -84.4 | 504990 | 680 |

> *... 2개 열 생략 (전체 14열)*

---
