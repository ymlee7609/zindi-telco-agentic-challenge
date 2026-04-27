# Track A 문제 분석 — train[500]~train[509]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[500] ~ train[509] (10개)

## 목차

1. [문제 500: `3e9146f6-4c3...`](#500) — single-answer, 정답: C14
2. [문제 501: `501da18b-d28...`](#501) — single-answer, 정답: C2
3. [문제 502: `1ee1bd01-916...`](#502) — single-answer, 정답: C13
4. [문제 503: `77f6be24-ed2...`](#503) — single-answer, 정답: C20
5. [문제 504: `6436821b-da8...`](#504) — single-answer, 정답: C14
6. [문제 505: `6c1acdca-fe5...`](#505) — single-answer, 정답: C16
7. [문제 506: `e73e80e6-9b5...`](#506) — multiple-answer, 정답: C12|C14
8. [문제 507: `bc5fda34-f8a...`](#507) — single-answer, 정답: C14
9. [문제 508: `7e6844f5-d1b...`](#508) — multiple-answer, 정답: C2|C4|C10|C12
10. [문제 509: `df7b2bff-ce2...`](#509) — single-answer, 정답: C9

---

### 문제 500: `3e9146f6-4c3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3e9146f6-4c36-43a7-96f4-26e5e2bb645f` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[500] topology](images/train_0500.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3217877_4
- `C2`: Check test server and transmission issues
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217877_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217877_4
- `C5`: Adjust the azimuth of 3217877_4 by 50 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269126_1
- `C7`: Increase transmission power for 3269126_1
- `C8`: Decrease transmission power for 3269126_1
- `C9`: Add neighbor relationship between 3217877_4 and 3269126_1
- `C10`: Press down the tilt angle  of 3269126_1 by 6 degrees
- `C11`: Decrease A3 Offset threshold for 3269126_1
- `C12`: Press down the tilt angle of 3217877_4 by 4 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269126_1
- `C14`: Insufficient data; more data is needed for judgment. **← 정답**
- `C15`: Adjust the azimuth of 3269126_1 by 11 degrees
- `C16`: Add neighbor relationship between 3231405_3 and 3269126_1
- `C17`: Lift the tilt angle  of 3269126_1 by 6 degrees
- `C18`: Lift the tilt angle of 3217877_4 by 4 degrees
- `C19`: Increase A3 Offset threshold for 3217877_4
- `C20`: Decrease transmission power for 3217877_4
- `C21`: Increase A3 Offset threshold for 3269126_1
- `C22`: Increase transmission power for 3217877_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.813 | MS1 | 121.4656664741 | 31.1446346727 | 871 | 504990 | -90.89 | 12.76 | 600.46 | 0.01 | 2.09 | 1586 |
| 2024-09-20 22:21:32.854 | MS1 | 121.4656681273 | 31.1446264660 | 871 | 504990 | -86.74 | 12.85 | 516.49 | 0.17 | 2.06 | 1565 |
| 2024-09-20 22:21:33.325 | MS1 | 121.4656683844 | 31.1446224731 | 871 | 504990 | -90.74 | 16.17 | 393.43 | 0.12 | 2.56 | 1588 |
| 2024-09-20 22:21:34.515 | MS1 | 121.4656744638 | 31.1446268104 | 871 | 504990 | -85.86 | 12.78 | 68.58 | 0.08 | 2.60 | 1579 |
| 2024-09-20 22:21:35.177 | MS1 | 121.4656629692 | 31.1446364444 | 871 | 504990 | -89.92 | 17.36 | 88.69 | 0.08 | 2.95 | 1580 |
| 2024-09-20 22:21:36.942 | MS1 | 121.4656624387 | 31.1446275321 | 871 | 504990 | -87.53 | 13.48 | 74.04 | 0.10 | 2.39 | 1560 |
| 2024-09-20 22:21:37.164 | MS1 | 121.4656642316 | 31.1446256909 | 871 | 504990 | -90.92 | 9.59 | 58.67 | 0.04 | 2.66 | 1596 |
| 2024-09-20 22:21:38.705 | MS1 | 121.4656651915 | 31.1446230491 | 871 | 504990 | -93.19 | 12.16 | 98.49 | 0.06 | 2.25 | 1587 |
| 2024-09-20 22:21:39.411 | MS1 | 121.4656778738 | 31.1446187567 | 871 | 504990 | -89.03 | 12.61 | 66.52 | 0.04 | 2.25 | 1576 |
| 2024-09-20 22:21:40.979 | MS1 | 121.4656718812 | 31.1446225634 | 871 | 504990 | -89.99 | 10.87 | 541.65 | 0.02 | 2.09 | 1563 |
| 2024-09-20 22:21:41.181 | MS1 | 121.4656688835 | 31.1446358312 | 871 | 504990 | -89.32 | 12.91 | 407.29 | 0.15 | 2.35 | 1570 |
| 2024-09-20 22:21:42.577 | MS1 | 121.4656762421 | 31.1446284840 | 871 | 504990 | -90.29 | 11.11 | 328.23 | 0.08 | 2.97 | 1592 |

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
| 3217877 | 4 | 121.4665245552 | 31.1491613644 | 322 | 0 | 10 | 36.1 | TDD | 871 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3231405 | 3 | 121.4661801707 | 31.1532834985 | 323 | 5 | 0 | 19.8 | TDD | 93 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3269126 | 1 | 121.4668189935 | 31.1546896474 | 197 | 5 | 3 | 20.0 | TDD | 117 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3279494 | 2 | 121.4678497130 | 31.1527221279 | 88 | 0 | 5 | 44.5 | TDD | 260 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.072 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.095 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.228 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.228 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.928 | NREventA3 | measId:2;ServCellPCI:35;Ser... |
| 2024-09-20 22:21:38.168 | NRHandoverAttempt | SourcePCI:35;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.211 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.221 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.354 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.354 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3269126 | 1 | 83.7643 | 79.1652 | -114.0482 | 13.2121 | 153.5166 | 0.0097 | 0.0020 |
| 2024_09_19 22:00 | 3279494 | 2 | 89.0130 | 84.2749 | -114.2532 | 15.2282 | 113.1090 | 0.0123 | 0.0195 |
| 2024_09_19 22:00 | 3231405 | 3 | 91.3349 | 76.4707 | -114.0770 | 13.0506 | 165.7123 | 0.0018 | 0.0051 |
| 2024_09_19 22:00 | 3217877 | 4 | 83.7582 | 89.9118 | -116.4456 | 18.5353 | 113.3585 | 0.0046 | 0.0147 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414684_8B0BF6B2 | 504990 | 871 | -86.6 | 504990 | 117 | -95.5 | 504990 | 93 | -97.7 | 504990 | 260 |
| MR_1774414684_438B1F98 | 504990 | 871 | -84.5 | 504990 | 117 | -92.8 | 504990 | 93 | -98.4 | 504990 | 260 |
| MR_1774414684_CCF2DE03 | 504990 | 871 | -84.8 | 504990 | 117 | -96.4 | 504990 | 93 | -98.9 | 504990 | 260 |
| MR_1774414684_606D3D39 | 504990 | 871 | -85.1 | 504990 | 117 | -93.3 | 504990 | 93 | -98.3 | 504990 | 260 |
| MR_1774414684_FD6AFCD4 | 504990 | 871 | -86.1 | 504990 | 117 | -96.3 | 504990 | 93 | -97.0 | 504990 | 260 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 501: `501da18b-d28...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `501da18b-d282-4163-ab0c-e03f53418fd4` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3275777_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[501] topology](images/train_0501.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3275777_4 by 30 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275777_4 **← 정답**
- `C3`: Add neighbor relationship between 3256443_3 and 3278167_2
- `C4`: Press down the tilt angle of 3275777_4 by 3 degrees
- `C5`: Increase transmission power for 3278167_2
- `C6`: Lift the tilt angle of 3275777_4 by 3 degrees
- `C7`: Decrease transmission power for 3275777_4
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278167_2
- `C10`: Increase A3 Offset threshold for 3275777_4
- `C11`: Decrease A3 Offset threshold for 3275777_4
- `C12`: Decrease transmission power for 3278167_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275777_4
- `C14`: Increase transmission power for 3275777_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278167_2
- `C16`: Decrease A3 Offset threshold for 3278167_2
- `C17`: Lift the tilt angle  of 3278167_2 by 6 degrees
- `C18`: Add neighbor relationship between 3275777_4 and 3278167_2
- `C19`: Adjust the azimuth of 3278167_2 by 50 degrees
- `C20`: Increase A3 Offset threshold for 3278167_2
- `C21`: Press down the tilt angle  of 3278167_2 by 6 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.673 | MS1 | 121.4656645588 | 31.1446200343 | 513 | 504990 | -88.78 | 13.90 | 398.79 | 0.07 | 2.92 | 1594 |
| 2024-09-20 22:21:32.671 | MS1 | 121.4656728915 | 31.1446336227 | 513 | 504990 | -88.09 | 12.72 | 388.18 | 0.10 | 2.98 | 1570 |
| 2024-09-20 22:21:33.147 | MS1 | 121.4656640148 | 31.1446248955 | 513 | 504990 | -89.16 | 15.71 | 511.97 | 0.11 | 2.96 | 1590 |
| 2024-09-20 22:21:34.357 | MS1 | 121.4656682565 | 31.1446260739 | 513 | 504990 | -85.30 | 14.59 | 52.59 | 0.51 | 2.67 | 594 |
| 2024-09-20 22:21:35.457 | MS1 | 121.4656597588 | 31.1446321869 | 513 | 504990 | -90.25 | 12.57 | 66.45 | 0.69 | 2.14 | 660 |
| 2024-09-20 22:21:36.247 | MS1 | 121.4656584920 | 31.1446271358 | 513 | 504990 | -89.39 | 15.26 | 98.67 | 0.58 | 2.69 | 676 |
| 2024-09-20 22:21:37.133 | MS1 | 121.4656646828 | 31.1446208708 | 513 | 504990 | -89.06 | 12.44 | 58.44 | 0.68 | 2.83 | 656 |
| 2024-09-20 22:21:38.779 | MS1 | 121.4656690478 | 31.1446348639 | 513 | 504990 | -91.03 | 11.33 | 46.04 | 0.55 | 2.47 | 654 |
| 2024-09-20 22:21:39.524 | MS1 | 121.4656761960 | 31.1446245352 | 513 | 504990 | -92.77 | 9.80 | 56.48 | 0.54 | 2.15 | 558 |
| 2024-09-20 22:21:40.413 | MS1 | 121.4656711624 | 31.1446311253 | 513 | 504990 | -89.13 | 12.23 | 555.48 | 0.14 | 2.70 | 1572 |
| 2024-09-20 22:21:41.204 | MS1 | 121.4656765645 | 31.1446201074 | 513 | 504990 | -93.63 | 12.63 | 410.91 | 0.08 | 2.52 | 1600 |
| 2024-09-20 22:21:42.858 | MS1 | 121.4656583801 | 31.1446290629 | 513 | 504990 | -90.46 | 11.84 | 320.31 | 0.04 | 2.39 | 1576 |

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
| 3211595 | 1 | 121.4695848672 | 31.1450232907 | 323 | 6 | 5 | 47.9 | TDD | 833 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3256443 | 3 | 121.4663063967 | 31.1508640559 | 91 | 4 | 5 | 43.1 | TDD | 990 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3275777 | 4 | 121.4665595346 | 31.1517482784 | 216 | 2 | 9 | 19.4 | TDD | 513 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3278167 | 2 | 121.4680091667 | 31.1523637087 | 48 | 4 | 4 | 35.2 | TDD | 1002 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.888 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.910 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.056 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.056 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.723 | NREventA3 | measId:2;ServCellPCI:590;Se... |
| 2024-09-20 22:21:37.963 | NRHandoverAttempt | SourcePCI:590;SourceNR-ARFC... |
| 2024-09-20 22:21:38.011 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.024 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.137 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.137 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211595 | 1 | 19.8579 | 9.8463 | -116.9590 | 12.2335 | 121.7939 | 0.0118 | 0.0175 |
| 2024_09_20 22:00 | 3278167 | 2 | 5.6004 | 15.3140 | -116.8718 | 11.8681 | 100.7283 | 0.0044 | 0.0050 |
| 2024_09_20 22:00 | 3256443 | 3 | 17.8390 | 8.8420 | -115.3560 | 18.8200 | 95.1214 | 0.0086 | 0.0195 |
| 2024_09_20 22:00 | 3275777 | 4 | 6.4636 | 17.5847 | -117.7367 | 7.3344 | 98.6879 | 0.0117 | 0.0175 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413790_15A6F98A | 504990 | 513 | -86.0 | 504990 | 1002 | -89.3 | 504990 | 990 | -91.1 | 504990 | 833 |
| MR_1774413790_B845AE7E | 504990 | 513 | -84.5 | 504990 | 1002 | -87.2 | 504990 | 990 | -91.8 | 504990 | 833 |
| MR_1774413790_F1D06F04 | 504990 | 513 | -84.4 | 504990 | 1002 | -88.2 | 504990 | 990 | -92.2 | 504990 | 833 |
| MR_1774413790_B1BF13B0 | 504990 | 513 | -86.0 | 504990 | 1002 | -87.7 | 504990 | 990 | -91.3 | 504990 | 833 |
| MR_1774413790_F04064C7 | 504990 | 513 | -86.6 | 504990 | 1002 | -88.0 | 504990 | 990 | -92.5 | 504990 | 833 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 502: `1ee1bd01-916...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1ee1bd01-9169-4307-908f-45a538656298` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Lift the tilt angle  of 3255069_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[502] topology](images/train_0502.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3272539_3
- `C2`: Increase A3 Offset threshold for 3219215_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272539_3
- `C4`: Decrease A3 Offset threshold for 3219215_2
- `C5`: Lift the tilt angle of 3272539_3 by 3 degrees
- `C6`: Decrease A3 Offset threshold for 3272539_3
- `C7`: Add neighbor relationship between 3255069_1 and 3219215_2
- `C8`: Increase transmission power for 3272539_3
- `C9`: Increase transmission power for 3219215_2
- `C10`: Check test server and transmission issues
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272539_3
- `C12`: Press down the tilt angle  of 3255069_1 by 10 degrees
- `C13`: Lift the tilt angle  of 3255069_1 by 10 degrees **← 정답**
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219215_2
- `C15`: Add neighbor relationship between 3272539_3 and 3219215_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219215_2
- `C17`: Adjust the azimuth of 3255069_1 by 50 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Adjust the azimuth of 3272539_3 by 10 degrees
- `C20`: Decrease transmission power for 3219215_2
- `C21`: Press down the tilt angle of 3272539_3 by 3 degrees
- `C22`: Increase A3 Offset threshold for 3272539_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.876 | MS1 | 121.4656759329 | 31.1446374440 | 898 | 504990 | -88.12 | 13.70 | 426.54 | 0.12 | 2.41 | 1566 |
| 2024-09-20 22:21:32.445 | MS1 | 121.4656586930 | 31.1446270505 | 898 | 504990 | -87.37 | 15.09 | 484.28 | 0.15 | 2.66 | 1592 |
| 2024-09-20 22:21:33.695 | MS1 | 121.4656641660 | 31.1446190907 | 898 | 504990 | -85.42 | 13.48 | 561.56 | 0.15 | 2.59 | 1570 |
| 2024-09-20 22:21:34.196 | MS1 | 121.4656598106 | 31.1446222406 | 898 | 504990 | -91.40 | 14.96 | 55.34 | 0.19 | 2.65 | 1579 |
| 2024-09-20 22:21:35.733 | MS1 | 121.4656737032 | 31.1446216280 | 898 | 504990 | -90.40 | 12.72 | 89.94 | 0.06 | 2.92 | 1575 |
| 2024-09-20 22:21:36.361 | MS1 | 121.4656676536 | 31.1446355155 | 898 | 504990 | -85.79 | 13.58 | 84.87 | 0.13 | 2.97 | 1563 |
| 2024-09-20 22:21:37.476 | MS1 | 121.4656773740 | 31.1446267151 | 898 | 504990 | -91.09 | 11.27 | 61.79 | 0.03 | 2.51 | 1588 |
| 2024-09-20 22:21:38.971 | MS1 | 121.4656725110 | 31.1446180494 | 898 | 504990 | -90.69 | 10.77 | 94.25 | 0.19 | 2.04 | 1568 |
| 2024-09-20 22:21:39.434 | MS1 | 121.4656703404 | 31.1446331348 | 898 | 504990 | -93.17 | 10.02 | 78.37 | 0.19 | 2.69 | 1588 |
| 2024-09-20 22:21:40.888 | MS1 | 121.4656640407 | 31.1446341676 | 898 | 504990 | -91.72 | 11.68 | 468.18 | 0.19 | 2.16 | 1590 |
| 2024-09-20 22:21:41.364 | MS1 | 121.4656661777 | 31.1446327781 | 898 | 504990 | -93.44 | 9.30 | 387.29 | 0.12 | 2.70 | 1563 |
| 2024-09-20 22:21:42.377 | MS1 | 121.4656768046 | 31.1446231089 | 898 | 504990 | -90.00 | 10.45 | 515.52 | 0.08 | 2.38 | 1570 |

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
| 3219215 | 2 | 121.4657812150 | 31.1485733111 | 350 | 4 | 10 | 45.1 | TDD | 628 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3255069 | 1 | 121.4662502168 | 31.1497874713 | 334 | 15 | 1 | 30.9 | TDD | 304 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3263711 | 4 | 121.4723480141 | 31.1539486700 | 30 | 3 | 6 | 24.7 | TDD | 380 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3272539 | 3 | 121.4723032836 | 31.1552241150 | 218 | 2 | 0 | 24.0 | TDD | 898 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.507 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.526 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.675 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.675 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.381 | NREventA3 | measId:2;ServCellPCI:864;Se... |
| 2024-09-20 22:21:38.621 | NRHandoverAttempt | SourcePCI:864;SourceNR-ARFC... |
| 2024-09-20 22:21:38.659 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.672 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.815 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.815 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255069 | 1 | 16.4166 | 14.1850 | -114.7729 | 12.9180 | 127.3007 | 0.0102 | 0.0191 |
| 2024_09_20 22:00 | 3219215 | 2 | 6.4755 | 14.7280 | -117.4139 | 5.9529 | 136.1876 | 0.0100 | 0.0183 |
| 2024_09_20 22:00 | 3272539 | 3 | 88.7904 | 93.2778 | -115.9529 | 11.3316 | 160.0705 | 0.0146 | 0.0160 |
| 2024_09_20 22:00 | 3263711 | 4 | 7.5614 | 8.3123 | -117.4041 | 6.5778 | 165.8240 | 0.0007 | 0.0159 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412582_2068BEE5 | 504990 | 898 | -89.9 | 504990 | 628 | -92.8 | 504990 | 304 | -98.7 | 504990 | 380 |
| MR_1774412582_E02494E0 | 504990 | 898 | -89.7 | 504990 | 628 | -93.2 | 504990 | 304 | -98.9 | 504990 | 380 |
| MR_1774412582_0040D089 | 504990 | 898 | -89.4 | 504990 | 628 | -92.3 | 504990 | 304 | -99.4 | 504990 | 380 |
| MR_1774412582_C507049A | 504990 | 898 | -92.3 | 504990 | 628 | -93.6 | 504990 | 304 | -99.6 | 504990 | 380 |
| MR_1774412582_3B9A6E5B | 504990 | 898 | -91.9 | 504990 | 628 | -90.8 | 504990 | 304 | -100.9 | 504990 | 380 |
| MR_1774412582_AB50A90B | 504990 | 898 | -93.2 | 504990 | 628 | -93.8 | 504990 | 304 | -99.8 | 504990 | 380 |
| MR_1774412582_41AC2802 | 504990 | 898 | -92.6 | 504990 | 628 | -92.7 | 504990 | 304 | -99.8 | 504990 | 380 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 503: `77f6be24-ed2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `77f6be24-ed23-4d85-932a-0da22adc3909` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Add neighbor relationship between 3267931_1 and 3226707_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[503] topology](images/train_0503.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267931_1
- `C3`: Increase A3 Offset threshold for 3226707_3
- `C4`: Lift the tilt angle  of 3226707_3 by 5 degrees
- `C5`: Check test server and transmission issues
- `C6`: Press down the tilt angle of 3267931_1 by 10 degrees
- `C7`: Add neighbor relationship between 3237083_2 and 3226707_3
- `C8`: Lift the tilt angle of 3267931_1 by 10 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226707_3
- `C10`: Increase A3 Offset threshold for 3267931_1
- `C11`: Increase transmission power for 3226707_3
- `C12`: Decrease A3 Offset threshold for 3226707_3
- `C13`: Press down the tilt angle  of 3226707_3 by 5 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226707_3
- `C15`: Decrease transmission power for 3226707_3
- `C16`: Decrease transmission power for 3267931_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267931_1
- `C18`: Decrease A3 Offset threshold for 3267931_1
- `C19`: Adjust the azimuth of 3226707_3 by 49 degrees
- `C20`: Add neighbor relationship between 3267931_1 and 3226707_3 **← 정답**
- `C21`: Increase transmission power for 3267931_1
- `C22`: Adjust the azimuth of 3267931_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.214 | MS1 | 121.4656718361 | 31.1446231194 | 248 | 504990 | -81.25 | 13.56 | 477.89 | 0.15 | 2.49 | 1599 |
| 2024-09-20 22:21:32.963 | MS1 | 121.4656602047 | 31.1446228079 | 248 | 504990 | -83.25 | 17.92 | 393.60 | 0.02 | 2.17 | 1586 |
| 2024-09-20 22:21:33.920 | MS1 | 121.4656681856 | 31.1446234785 | 248 | 504990 | -80.34 | 17.67 | 516.83 | 0.13 | 2.56 | 1587 |
| 2024-09-20 22:21:34.704 | MS1 | 121.4656653931 | 31.1446267947 | 248 | 504990 | -92.67 | -2.03 | 55.63 | 0.11 | 1.01 | 1568 |
| 2024-09-20 22:21:35.890 | MS1 | 121.4656696193 | 31.1446275797 | 248 | 504990 | -89.16 | -2.59 | 40.94 | 0.03 | 1.26 | 1593 |
| 2024-09-20 22:21:36.755 | MS1 | 121.4656692500 | 31.1446270957 | 248 | 504990 | -86.76 | -1.15 | 48.30 | 0.10 | 1.10 | 1583 |
| 2024-09-20 22:21:37.121 | MS1 | 121.4656759608 | 31.1446193184 | 248 | 504990 | -85.21 | -1.85 | 66.82 | 0.09 | 1.33 | 1560 |
| 2024-09-20 22:21:38.255 | MS1 | 121.4656704198 | 31.1446336562 | 248 | 504990 | -79.20 | 12.67 | 395.44 | 0.01 | 1.45 | 1583 |
| 2024-09-20 22:21:39.480 | MS1 | 121.4656755910 | 31.1446318331 | 248 | 504990 | -77.63 | 13.76 | 310.97 | 0.02 | 1.46 | 1575 |
| 2024-09-20 22:21:40.724 | MS1 | 121.4656664023 | 31.1446210090 | 248 | 504990 | -84.54 | 13.92 | 452.01 | 0.11 | 2.68 | 1589 |
| 2024-09-20 22:21:41.382 | MS1 | 121.4656615611 | 31.1446281755 | 248 | 504990 | -77.86 | 13.27 | 503.31 | 0.11 | 2.85 | 1586 |
| 2024-09-20 22:21:42.340 | MS1 | 121.4656777846 | 31.1446321193 | 248 | 504990 | -76.53 | 17.91 | 502.43 | 0.17 | 2.38 | 1593 |

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
| 3226707 | 3 | 121.4697081040 | 31.1471427147 | 185 | 2 | 8 | 25.6 | TDD | 114 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3237083 | 2 | 121.4692412639 | 31.1513214578 | 43 | 14 | 6 | 19.7 | TDD | 520 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3267481 | 4 | 121.4686447907 | 31.1470200274 | 235 | 12 | 2 | 43.4 | TDD | 387 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3267931 | 1 | 121.4697556886 | 31.1504773830 | 100 | 13 | 9 | 26.4 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.034 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.049 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.176 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.176 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.933 | NREventA3 | measId:2;ServCellPCI:313;Se... |
| 2024-09-20 22:21:35.933 | NREventA3 | measId:2;ServCellPCI:313;Se... |
| 2024-09-20 22:21:36.933 | NREventA3 | measId:2;ServCellPCI:313;Se... |
| 2024-09-20 22:21:39.433 | NRRRCReestablishAttempt | PCI:313 |
| 2024-09-20 22:21:39.450 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.460 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.582 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.582 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267931 | 1 | 6.7353 | 8.9676 | -114.1402 | 13.4930 | 129.3036 | 0.0066 | 0.1161 |
| 2024_09_20 22:00 | 3237083 | 2 | 5.2941 | 10.4141 | -117.6139 | 10.8745 | 192.0224 | 0.0092 | 0.0029 |
| 2024_09_20 22:00 | 3226707 | 3 | 14.4366 | 19.9333 | -114.9813 | 13.3373 | 180.3664 | 0.0183 | 0.0114 |
| 2024_09_20 22:00 | 3267481 | 4 | 10.0537 | 5.0564 | -116.1344 | 10.8220 | 188.3755 | 0.0130 | 0.0060 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412388_D9CD0670 | 504990 | 248 | -92.3 | 504990 | 114 | -88.2 | 504990 | 520 | -88.8 | 504990 | 387 |
| MR_1774412388_75CE4D86 | 504990 | 248 | -94.4 | 504990 | 114 | -88.5 | 504990 | 520 | -89.7 | 504990 | 387 |
| MR_1774412388_4DE99C78 | 504990 | 114 | -88.6 | 504990 | 248 | -91.2 | 504990 | 520 | -91.7 | 504990 | 387 |
| MR_1774412388_69CDC75F | 504990 | 114 | -85.6 | 504990 | 248 | -94.6 | 504990 | 520 | -89.6 | 504990 | 387 |
| MR_1774412388_729C2C40 | 504990 | 248 | -91.7 | 504990 | 114 | -86.0 | 504990 | 520 | -90.3 | 504990 | 387 |
| MR_1774412388_96E5D8D4 | 504990 | 248 | -93.7 | 504990 | 114 | -85.3 | 504990 | 520 | -89.9 | 504990 | 387 |
| MR_1774412388_3A5FC76F | 504990 | 114 | -86.3 | 504990 | 248 | -91.2 | 504990 | 520 | -92.1 | 504990 | 387 |
| MR_1774412388_9ABD4910 | 504990 | 114 | -87.6 | 504990 | 248 | -91.5 | 504990 | 520 | -91.6 | 504990 | 387 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 504: `6436821b-da8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6436821b-da84-4251-970a-54062d813c12` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[504] topology](images/train_0504.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3252701_4
- `C2`: Press down the tilt angle  of 3232783_2 by 10 degrees
- `C3`: Increase transmission power for 3252701_4
- `C4`: Press down the tilt angle of 3252701_4 by 10 degrees
- `C5`: Adjust the azimuth of 3232783_2 by 27 degrees
- `C6`: Decrease A3 Offset threshold for 3232783_2
- `C7`: Add neighbor relationship between 3252701_4 and 3232783_2
- `C8`: Increase A3 Offset threshold for 3232783_2
- `C9`: Add neighbor relationship between 3214837_3 and 3232783_2
- `C10`: Lift the tilt angle  of 3232783_2 by 10 degrees
- `C11`: Increase transmission power for 3232783_2
- `C12`: Decrease A3 Offset threshold for 3252701_4
- `C13`: Check test server and transmission issues
- `C14`: Insufficient data; more data is needed for judgment. **← 정답**
- `C15`: Decrease transmission power for 3252701_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252701_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232783_2
- `C18`: Decrease transmission power for 3232783_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232783_2
- `C20`: Lift the tilt angle of 3252701_4 by 10 degrees
- `C21`: Adjust the azimuth of 3252701_4 by 50 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252701_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.788 | MS1 | 121.4656742956 | 31.1446201136 | 271 | 504990 | -91.10 | 14.95 | 337.55 | 0.15 | 2.83 | 1564 |
| 2024-09-20 22:21:32.642 | MS1 | 121.4656589974 | 31.1446259154 | 271 | 504990 | -85.47 | 15.04 | 529.84 | 0.16 | 2.69 | 1586 |
| 2024-09-20 22:21:33.412 | MS1 | 121.4656755196 | 31.1446284969 | 271 | 504990 | -90.98 | 17.21 | 373.73 | 0.10 | 2.21 | 1581 |
| 2024-09-20 22:21:34.827 | MS1 | 121.4656716633 | 31.1446263883 | 271 | 504990 | -87.48 | 17.99 | 78.37 | 0.09 | 2.98 | 1579 |
| 2024-09-20 22:21:35.655 | MS1 | 121.4656757425 | 31.1446304894 | 271 | 504990 | -88.19 | 12.90 | 99.96 | 0.02 | 2.62 | 1573 |
| 2024-09-20 22:21:36.194 | MS1 | 121.4656642057 | 31.1446269872 | 271 | 504990 | -91.17 | 17.64 | 63.34 | 0.02 | 2.20 | 1564 |
| 2024-09-20 22:21:37.930 | MS1 | 121.4656610467 | 31.1446244160 | 271 | 504990 | -89.65 | 7.18 | 76.86 | 0.15 | 2.67 | 1591 |
| 2024-09-20 22:21:38.691 | MS1 | 121.4656762783 | 31.1446235657 | 271 | 504990 | -89.03 | 11.29 | 95.51 | 0.08 | 2.88 | 1583 |
| 2024-09-20 22:21:39.393 | MS1 | 121.4656608734 | 31.1446340612 | 271 | 504990 | -91.87 | 12.60 | 89.35 | 0.07 | 2.75 | 1576 |
| 2024-09-20 22:21:40.919 | MS1 | 121.4656618127 | 31.1446243651 | 271 | 504990 | -93.08 | 8.50 | 386.78 | 0.09 | 2.42 | 1565 |
| 2024-09-20 22:21:41.775 | MS1 | 121.4656599887 | 31.1446364411 | 271 | 504990 | -91.63 | 7.81 | 389.83 | 0.06 | 2.18 | 1592 |
| 2024-09-20 22:21:42.667 | MS1 | 121.4656607120 | 31.1446201317 | 271 | 504990 | -93.99 | 10.42 | 485.74 | 0.08 | 2.44 | 1579 |

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
| 3213436 | 1 | 121.4677270800 | 31.1544866411 | 59 | 10 | 0 | 46.6 | TDD | 425 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3214837 | 3 | 121.4735950672 | 31.1512180685 | 311 | 11 | 10 | 30.4 | TDD | 747 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3232783 | 2 | 121.4741549543 | 31.1487701392 | 213 | 11 | 1 | 15.6 | TDD | 346 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3252701 | 4 | 121.4684643176 | 31.1509100399 | 284 | 9 | 4 | 37.6 | TDD | 271 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.016 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.037 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.184 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.184 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.845 | NREventA3 | measId:2;ServCellPCI:802;Se... |
| 2024-09-20 22:21:38.085 | NRHandoverAttempt | SourcePCI:802;SourceNR-ARFC... |
| 2024-09-20 22:21:38.125 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.139 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.263 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.263 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3213436 | 1 | 89.5090 | 78.0808 | -116.7734 | 13.3024 | 128.5617 | 0.0124 | 0.0162 |
| 2024_09_19 22:00 | 3232783 | 2 | 81.8832 | 82.1226 | -115.5331 | 10.9706 | 96.1958 | 0.0122 | 0.0106 |
| 2024_09_19 22:00 | 3214837 | 3 | 85.3942 | 89.7578 | -117.3339 | 11.0866 | 107.1310 | 0.0056 | 0.0188 |
| 2024_09_19 22:00 | 3252701 | 4 | 90.0326 | 79.5996 | -114.2577 | 5.9996 | 142.5596 | 0.0052 | 0.0017 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412414_3F2BA6D4 | 504990 | 271 | -88.4 | 504990 | 346 | -91.8 | 504990 | 747 | -100.1 | 504990 | 425 |
| MR_1774412414_EA5824D5 | 504990 | 271 | -86.4 | 504990 | 346 | -92.2 | 504990 | 747 | -99.7 | 504990 | 425 |
| MR_1774412414_14990DE7 | 504990 | 271 | -87.9 | 504990 | 346 | -91.7 | 504990 | 747 | -99.6 | 504990 | 425 |
| MR_1774412414_02A8797D | 504990 | 271 | -87.4 | 504990 | 346 | -93.6 | 504990 | 747 | -98.6 | 504990 | 425 |
| MR_1774412414_A1BD7433 | 504990 | 271 | -87.4 | 504990 | 346 | -95.4 | 504990 | 747 | -99.3 | 504990 | 425 |
| MR_1774412414_75162377 | 504990 | 271 | -86.4 | 504990 | 346 | -94.4 | 504990 | 747 | -98.6 | 504990 | 425 |
| MR_1774412414_7C4C6B6E | 504990 | 271 | -87.9 | 504990 | 346 | -92.0 | 504990 | 747 | -97.6 | 504990 | 425 |
| MR_1774412414_AD5C3930 | 504990 | 271 | -85.7 | 504990 | 346 | -95.5 | 504990 | 747 | -99.2 | 504990 | 425 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 505: `6c1acdca-fe5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6c1acdca-fe5e-4320-99d0-3eb7cc37c243` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Lift the tilt angle  of 3218205_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[505] topology](images/train_0505.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3223435_4 by 3 degrees
- `C2`: Increase transmission power for 3223435_4
- `C3`: Adjust the azimuth of 3223435_4 by 22 degrees
- `C4`: Add neighbor relationship between 3218205_1 and 3273728_3
- `C5`: Add neighbor relationship between 3223435_4 and 3273728_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273728_3
- `C7`: Decrease transmission power for 3223435_4
- `C8`: Decrease A3 Offset threshold for 3223435_4
- `C9`: Check test server and transmission issues
- `C10`: Decrease transmission power for 3273728_3
- `C11`: Lift the tilt angle of 3223435_4 by 3 degrees
- `C12`: Decrease A3 Offset threshold for 3273728_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273728_3
- `C14`: Press down the tilt angle  of 3218205_1 by 10 degrees
- `C15`: Increase A3 Offset threshold for 3273728_3
- `C16`: Lift the tilt angle  of 3218205_1 by 10 degrees **← 정답**
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223435_4
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223435_4
- `C20`: Adjust the azimuth of 3218205_1 by 14 degrees
- `C21`: Increase A3 Offset threshold for 3223435_4
- `C22`: Increase transmission power for 3273728_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.746 | MS1 | 121.4656686273 | 31.1446242890 | 22 | 504990 | -88.39 | 14.82 | 478.40 | 0.12 | 2.43 | 1588 |
| 2024-09-20 22:21:32.672 | MS1 | 121.4656649882 | 31.1446192226 | 22 | 504990 | -90.60 | 16.34 | 473.80 | 0.17 | 2.21 | 1576 |
| 2024-09-20 22:21:33.205 | MS1 | 121.4656603668 | 31.1446180257 | 22 | 504990 | -85.27 | 14.66 | 306.88 | 0.12 | 2.97 | 1581 |
| 2024-09-20 22:21:34.556 | MS1 | 121.4656650567 | 31.1446209861 | 22 | 504990 | -91.53 | 14.43 | 65.59 | 0.03 | 2.56 | 1561 |
| 2024-09-20 22:21:35.973 | MS1 | 121.4656614638 | 31.1446242726 | 22 | 504990 | -91.04 | 12.25 | 99.87 | 0.16 | 2.30 | 1589 |
| 2024-09-20 22:21:36.604 | MS1 | 121.4656750352 | 31.1446231227 | 22 | 504990 | -89.29 | 14.87 | 71.86 | 0.11 | 2.32 | 1563 |
| 2024-09-20 22:21:37.880 | MS1 | 121.4656605438 | 31.1446341710 | 22 | 504990 | -92.38 | 9.71 | 63.26 | 0.01 | 2.98 | 1575 |
| 2024-09-20 22:21:38.353 | MS1 | 121.4656631847 | 31.1446226652 | 22 | 504990 | -90.55 | 11.66 | 76.59 | 0.01 | 2.93 | 1572 |
| 2024-09-20 22:21:39.247 | MS1 | 121.4656754678 | 31.1446242557 | 22 | 504990 | -89.27 | 11.57 | 50.40 | 0.03 | 2.18 | 1581 |
| 2024-09-20 22:21:40.846 | MS1 | 121.4656681456 | 31.1446234195 | 22 | 504990 | -92.87 | 9.26 | 466.08 | 0.06 | 2.56 | 1592 |
| 2024-09-20 22:21:41.242 | MS1 | 121.4656683531 | 31.1446367488 | 22 | 504990 | -89.58 | 9.66 | 511.63 | 0.01 | 2.81 | 1589 |
| 2024-09-20 22:21:42.607 | MS1 | 121.4656723992 | 31.1446240237 | 22 | 504990 | -89.22 | 8.60 | 575.33 | 0.03 | 2.94 | 1586 |

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
| 3218205 | 1 | 121.4705327156 | 31.1442542994 | 140 | 5 | 6 | 49.8 | TDD | 594 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3223435 | 4 | 121.4714603238 | 31.1547333729 | 184 | 2 | 7 | 32.3 | TDD | 22 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3236882 | 2 | 121.4696903045 | 31.1515871406 | 4 | 14 | 2 | 40.3 | TDD | 668 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3273728 | 3 | 121.4677738904 | 31.1460854144 | 245 | 3 | 7 | 37.1 | TDD | 629 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.501 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.521 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.642 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.642 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.394 | NREventA3 | measId:2;ServCellPCI:996;Se... |
| 2024-09-20 22:21:38.634 | NRHandoverAttempt | SourcePCI:996;SourceNR-ARFC... |
| 2024-09-20 22:21:38.682 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.696 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.839 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.839 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218205 | 1 | 12.4324 | 17.9203 | -116.3737 | 9.7376 | 133.2941 | 0.0061 | 0.0106 |
| 2024_09_20 22:00 | 3236882 | 2 | 6.2684 | 13.7987 | -114.6044 | 8.0736 | 115.8478 | 0.0088 | 0.0026 |
| 2024_09_20 22:00 | 3273728 | 3 | 11.2599 | 16.1919 | -116.2816 | 8.0255 | 167.7604 | 0.0161 | 0.0059 |
| 2024_09_20 22:00 | 3223435 | 4 | 92.8614 | 83.1377 | -117.4778 | 19.0185 | 129.3348 | 0.0135 | 0.0189 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413986_E0F912CA | 504990 | 22 | -90.1 | 504990 | 629 | -100.4 | 504990 | 594 | -100.3 | 504990 | 668 |
| MR_1774413986_6D9EACFA | 504990 | 22 | -92.0 | 504990 | 629 | -98.3 | 504990 | 594 | -101.3 | 504990 | 668 |
| MR_1774413986_669CB151 | 504990 | 22 | -91.2 | 504990 | 629 | -100.7 | 504990 | 594 | -101.9 | 504990 | 668 |
| MR_1774413986_B8F74990 | 504990 | 22 | -91.5 | 504990 | 629 | -99.1 | 504990 | 594 | -99.4 | 504990 | 668 |
| MR_1774413986_4CE1FFAC | 504990 | 22 | -89.7 | 504990 | 629 | -98.8 | 504990 | 594 | -101.6 | 504990 | 668 |
| MR_1774413986_9EF426A8 | 504990 | 22 | -91.8 | 504990 | 629 | -98.3 | 504990 | 594 | -100.9 | 504990 | 668 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 506: `e73e80e6-9b5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e73e80e6-9b54-49b5-ac41-f0be8df545e4` |
| Tag | **multiple-answer** |
| 정답 | **C12|C14** |
| C12 의미 | Increase transmission power for 3214908_4 |
| C14 의미 | Adjust the azimuth of 3214908_4 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[506] topology](images/train_0506.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3260911_2 and 3250895_3
- `C2`: Check test server and transmission issues
- `C3`: Add neighbor relationship between 3214908_4 and 3250895_3
- `C4`: Press down the tilt angle  of 3250895_3 by 1 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214908_4
- `C7`: Decrease transmission power for 3214908_4
- `C8`: Decrease A3 Offset threshold for 3250895_3
- `C9`: Lift the tilt angle of 3214908_4 by 10 degrees
- `C10`: Adjust the azimuth of 3250895_3 by 9 degrees
- `C11`: Increase A3 Offset threshold for 3214908_4
- `C12`: Increase transmission power for 3214908_4 **← 정답**
- `C13`: Decrease transmission power for 3250895_3
- `C14`: Adjust the azimuth of 3214908_4 by 50 degrees **← 정답**
- `C15`: Decrease A3 Offset threshold for 3214908_4
- `C16`: Increase transmission power for 3250895_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250895_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214908_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250895_3
- `C20`: Increase A3 Offset threshold for 3250895_3
- `C21`: Press down the tilt angle of 3214908_4 by 10 degrees
- `C22`: Lift the tilt angle  of 3250895_3 by 1 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.987 | MS1 | 121.4656746018 | 31.1446305161 | 76 | 504990 | -88.62 | 17.78 | 485.47 | 0.16 | 2.11 | 1582 |
| 2024-09-20 22:21:32.724 | MS1 | 121.4656591376 | 31.1446244190 | 76 | 504990 | -92.60 | 13.37 | 526.92 | 0.04 | 2.45 | 1573 |
| 2024-09-20 22:21:33.105 | MS1 | 121.4656640452 | 31.1446269084 | 76 | 504990 | -93.46 | 17.56 | 448.63 | 0.15 | 2.37 | 1578 |
| 2024-09-20 22:21:34.775 | MS1 | 121.4656725934 | 31.1446315674 | 76 | 504990 | -100.15 | 1.39 | 79.16 | 0.19 | 1.40 | 1578 |
| 2024-09-20 22:21:35.272 | MS1 | 121.4656629797 | 31.1446373330 | 76 | 504990 | -103.46 | -1.05 | 36.46 | 0.16 | 1.25 | 1589 |
| 2024-09-20 22:21:36.776 | MS1 | 121.4656771787 | 31.1446363762 | 76 | 504990 | -102.92 | -1.92 | 48.99 | 0.15 | 1.23 | 1571 |
| 2024-09-20 22:21:37.108 | MS1 | 121.4656597744 | 31.1446192345 | 76 | 504990 | -100.54 | 0.23 | 32.94 | 0.04 | 1.49 | 1574 |
| 2024-09-20 22:21:38.164 | MS1 | 121.4656685166 | 31.1446345403 | 76 | 504990 | -107.96 | 0.78 | 59.78 | 0.07 | 1.35 | 1595 |
| 2024-09-20 22:21:39.786 | MS1 | 121.4656749148 | 31.1446185504 | 76 | 504990 | -103.91 | 1.01 | 48.42 | 0.19 | 1.16 | 1568 |
| 2024-09-20 22:21:40.380 | MS1 | 121.4656728580 | 31.1446266621 | 76 | 504990 | -89.55 | 12.37 | 538.90 | 0.04 | 2.41 | 1581 |
| 2024-09-20 22:21:41.559 | MS1 | 121.4656605220 | 31.1446244732 | 76 | 504990 | -90.86 | 17.80 | 572.40 | 0.08 | 2.91 | 1586 |
| 2024-09-20 22:21:42.845 | MS1 | 121.4656687465 | 31.1446279211 | 76 | 504990 | -86.26 | 17.12 | 342.19 | 0.18 | 2.70 | 1592 |

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
| 3214908 | 4 | 121.4649118270 | 31.1453486132 | 207 | 4 | 9 | 42.4 | TDD | 76 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3240591 | 1 | 121.4743148305 | 31.1538461461 | 351 | 4 | 4 | 31.5 | TDD | 424 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3250895 | 3 | 121.4671633206 | 31.1558188260 | 178 | 0 | 0 | 22.4 | TDD | 884 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3260911 | 2 | 121.4645945780 | 31.1478910449 | 289 | 10 | 8 | 23.5 | TDD | 51 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.739 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.759 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.875 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.875 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.103 | NREventA2 | measId:1;ServCellPCI:608;Se... |
| 2024-09-20 22:21:34.241 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240591 | 1 | 12.4176 | 11.0350 | -117.4144 | 10.9938 | 179.7579 | 0.0097 | 0.0095 |
| 2024_09_20 22:00 | 3260911 | 2 | 5.1048 | 5.0399 | -117.9495 | 19.0070 | 135.3632 | 0.0128 | 0.0091 |
| 2024_09_20 22:00 | 3250895 | 3 | 6.7728 | 18.1779 | -115.8613 | 6.6081 | 164.0591 | 0.0025 | 0.0163 |
| 2024_09_20 22:00 | 3214908 | 4 | 19.7011 | 13.6056 | -117.0927 | 6.2491 | 111.2475 | 0.1257 | 0.0165 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412974_FE6928D7 | 504990 | 76 | -99.8 | 504990 | 884 | -104.8 | 504990 | 51 | -105.1 | 504990 | 424 |
| MR_1774412974_C5B49B41 | 504990 | 76 | -99.0 | 504990 | 884 | -102.6 | 504990 | 51 | -107.2 | 504990 | 424 |
| MR_1774412974_A01794D0 | 504990 | 76 | -101.7 | 504990 | 884 | -102.9 | 504990 | 51 | -105.5 | 504990 | 424 |
| MR_1774412974_5E566EFB | 504990 | 76 | -99.9 | 504990 | 884 | -101.5 | 504990 | 51 | -107.6 | 504990 | 424 |
| MR_1774412974_E0F6713A | 504990 | 76 | -100.6 | 504990 | 884 | -104.4 | 504990 | 51 | -105.9 | 504990 | 424 |
| MR_1774412974_0074C8C4 | 504990 | 76 | -100.6 | 504990 | 884 | -102.0 | 504990 | 51 | -108.4 | 504990 | 424 |
| MR_1774412974_B45F03A6 | 504990 | 76 | -100.3 | 504990 | 884 | -104.4 | 504990 | 51 | -105.8 | 504990 | 424 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 507: `bc5fda34-f8a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bc5fda34-f8ae-47e5-8382-8931fec80a05` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3240688_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[507] topology](images/train_0507.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3240688_4
- `C2`: Adjust the azimuth of 3279509_2 by 50 degrees
- `C3`: Lift the tilt angle  of 3279509_2 by 6 degrees
- `C4`: Check test server and transmission issues
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279509_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240688_4
- `C7`: Adjust the azimuth of 3240688_4 by 38 degrees
- `C8`: Increase transmission power for 3279509_2
- `C9`: Decrease A3 Offset threshold for 3240688_4
- `C10`: Add neighbor relationship between 3240688_4 and 3279509_2
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Add neighbor relationship between 3277522_3 and 3279509_2
- `C13`: Press down the tilt angle  of 3279509_2 by 6 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240688_4 **← 정답**
- `C15`: Press down the tilt angle of 3240688_4 by 2 degrees
- `C16`: Lift the tilt angle of 3240688_4 by 2 degrees
- `C17`: Increase transmission power for 3240688_4
- `C18`: Decrease A3 Offset threshold for 3279509_2
- `C19`: Increase A3 Offset threshold for 3240688_4
- `C20`: Decrease transmission power for 3279509_2
- `C21`: Increase A3 Offset threshold for 3279509_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279509_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.834 | MS1 | 121.4656754930 | 31.1446181434 | 925 | 504990 | -89.31 | 14.96 | 317.11 | 0.01 | 2.61 | 1595 |
| 2024-09-20 22:21:32.198 | MS1 | 121.4656595452 | 31.1446232845 | 925 | 504990 | -88.33 | 14.87 | 551.86 | 0.18 | 2.25 | 1569 |
| 2024-09-20 22:21:33.352 | MS1 | 121.4656647228 | 31.1446311157 | 925 | 504990 | -91.62 | 12.70 | 358.67 | 0.14 | 2.88 | 1565 |
| 2024-09-20 22:21:34.863 | MS1 | 121.4656746597 | 31.1446215641 | 925 | 504990 | -88.80 | 16.54 | 80.37 | 0.53 | 2.42 | 676 |
| 2024-09-20 22:21:35.507 | MS1 | 121.4656635176 | 31.1446215850 | 925 | 504990 | -86.24 | 14.26 | 52.78 | 0.53 | 2.89 | 646 |
| 2024-09-20 22:21:36.348 | MS1 | 121.4656612818 | 31.1446297364 | 925 | 504990 | -88.01 | 17.31 | 64.00 | 0.62 | 2.90 | 652 |
| 2024-09-20 22:21:37.735 | MS1 | 121.4656630544 | 31.1446305086 | 925 | 504990 | -90.35 | 8.89 | 70.71 | 0.58 | 3.00 | 699 |
| 2024-09-20 22:21:38.505 | MS1 | 121.4656695226 | 31.1446322702 | 925 | 504990 | -89.54 | 7.75 | 89.74 | 0.50 | 2.21 | 577 |
| 2024-09-20 22:21:39.212 | MS1 | 121.4656710517 | 31.1446361011 | 925 | 504990 | -91.80 | 11.05 | 73.84 | 0.55 | 2.18 | 652 |
| 2024-09-20 22:21:40.231 | MS1 | 121.4656771414 | 31.1446210584 | 925 | 504990 | -91.03 | 8.37 | 430.26 | 0.02 | 2.23 | 1580 |
| 2024-09-20 22:21:41.261 | MS1 | 121.4656679255 | 31.1446360461 | 925 | 504990 | -89.52 | 7.31 | 511.16 | 0.05 | 2.61 | 1584 |
| 2024-09-20 22:21:42.739 | MS1 | 121.4656731919 | 31.1446287775 | 925 | 504990 | -91.86 | 12.73 | 589.06 | 0.01 | 2.06 | 1571 |

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
| 3217711 | 1 | 121.4670960901 | 31.1460099230 | 281 | 9 | 10 | 22.3 | TDD | 889 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3240688 | 4 | 121.4748665693 | 31.1506177069 | 195 | 0 | 0 | 39.1 | TDD | 925 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3277522 | 3 | 121.4719212147 | 31.1503500984 | 60 | 15 | 9 | 43.0 | TDD | 508 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3279509 | 2 | 121.4667320294 | 31.1538713494 | 355 | 4 | 10 | 32.8 | TDD | 338 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.124 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.139 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.285 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.285 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.933 | NREventA3 | measId:2;ServCellPCI:318;Se... |
| 2024-09-20 22:21:38.173 | NRHandoverAttempt | SourcePCI:318;SourceNR-ARFC... |
| 2024-09-20 22:21:38.223 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.236 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.344 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.344 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217711 | 1 | 11.4405 | 17.9432 | -114.3131 | 19.3219 | 162.9756 | 0.0095 | 0.0061 |
| 2024_09_20 22:00 | 3279509 | 2 | 7.0694 | 17.3947 | -117.8454 | 9.4245 | 182.7900 | 0.0036 | 0.0002 |
| 2024_09_20 22:00 | 3277522 | 3 | 11.5468 | 9.0313 | -117.8199 | 14.5377 | 104.6068 | 0.0118 | 0.0008 |
| 2024_09_20 22:00 | 3240688 | 4 | 6.9269 | 18.9649 | -117.7988 | 17.4338 | 175.4152 | 0.0061 | 0.0190 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412502_5824CAB9 | 504990 | 925 | -90.1 | 504990 | 338 | -91.1 | 504990 | 508 | -96.8 | 504990 | 889 |
| MR_1774412502_85BBBC23 | 504990 | 925 | -90.2 | 504990 | 338 | -92.9 | 504990 | 508 | -98.0 | 504990 | 889 |
| MR_1774412502_52DC3C22 | 504990 | 925 | -88.0 | 504990 | 338 | -90.8 | 504990 | 508 | -99.4 | 504990 | 889 |
| MR_1774412502_4E0B86B4 | 504990 | 925 | -88.4 | 504990 | 338 | -93.8 | 504990 | 508 | -97.1 | 504990 | 889 |
| MR_1774412502_C24B654A | 504990 | 925 | -87.4 | 504990 | 338 | -92.7 | 504990 | 508 | -96.5 | 504990 | 889 |
| MR_1774412502_F4A0E34C | 504990 | 925 | -88.6 | 504990 | 338 | -92.9 | 504990 | 508 | -97.3 | 504990 | 889 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 508: `7e6844f5-d1b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7e6844f5-d1b8-4690-b54c-89bd236b1aed` |
| Tag | **multiple-answer** |
| 정답 | **C2|C4|C10|C12** |
| C2 의미 | Press down the tilt angle  of 3278503_4 by 4 degrees |
| C4 의미 | Increase A3 Offset threshold for 3278503_4 |
| C10 의미 | Increase A3 Offset threshold for 3213440_1 |
| C12 의미 | Decrease transmission power for 3278503_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[508] topology](images/train_0508.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213440_1
- `C2`: Press down the tilt angle  of 3278503_4 by 4 degrees **← 정답**
- `C3`: Lift the tilt angle  of 3278503_4 by 4 degrees
- `C4`: Increase A3 Offset threshold for 3278503_4 **← 정답**
- `C5`: Decrease transmission power for 3213440_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213440_1
- `C7`: Add neighbor relationship between 3247070_5 and 3278503_4
- `C8`: Adjust the azimuth of 3278503_4 by 40 degrees
- `C9`: Decrease A3 Offset threshold for 3213440_1
- `C10`: Increase A3 Offset threshold for 3213440_1 **← 정답**
- `C11`: Decrease A3 Offset threshold for 3278503_4
- `C12`: Decrease transmission power for 3278503_4 **← 정답**
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278503_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278503_4
- `C15`: Check test server and transmission issues
- `C16`: Lift the tilt angle of 3213440_1 by 2 degrees
- `C17`: Press down the tilt angle of 3213440_1 by 2 degrees
- `C18`: Increase transmission power for 3278503_4
- `C19`: Adjust the azimuth of 3213440_1 by 43 degrees
- `C20`: Add neighbor relationship between 3213440_1 and 3278503_4
- `C21`: Increase transmission power for 3213440_1
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.825 | MS1 | 121.4656675354 | 31.1446260242 | 69 | 504990 | -82.96 | 17.16 | 428.97 | 0.08 | 2.70 | 1587 |
| 2024-09-20 22:21:32.670 | MS1 | 121.4656635930 | 31.1446348665 | 69 | 504990 | -76.11 | 17.87 | 425.41 | 0.05 | 2.50 | 1590 |
| 2024-09-20 22:21:33.135 | MS1 | 121.4656638374 | 31.1446254998 | 69 | 504990 | -76.40 | 17.86 | 526.43 | 0.14 | 2.81 | 1589 |
| 2024-09-20 22:21:34.760 | MS1 | 121.4656754906 | 31.1446199267 | 335 | 504990 | -86.61 | 3.06 | 74.04 | 0.15 | 1.20 | 1560 |
| 2024-09-20 22:21:35.481 | MS1 | 121.4656740188 | 31.1446369800 | 335 | 504990 | -86.65 | 3.01 | 50.03 | 0.07 | 1.23 | 1567 |
| 2024-09-20 22:21:36.382 | MS1 | 121.4656733407 | 31.1446207844 | 69 | 504990 | -84.88 | 4.82 | 66.41 | 0.07 | 1.48 | 1598 |
| 2024-09-20 22:21:37.714 | MS1 | 121.4656652907 | 31.1446286418 | 69 | 504990 | -85.97 | 2.69 | 42.08 | 0.16 | 1.12 | 1562 |
| 2024-09-20 22:21:38.143 | MS1 | 121.4656660064 | 31.1446370735 | 335 | 504990 | -87.88 | 4.17 | 49.10 | 0.05 | 1.48 | 1584 |
| 2024-09-20 22:21:39.791 | MS1 | 121.4656725574 | 31.1446234344 | 335 | 504990 | -87.54 | 4.97 | 67.23 | 0.19 | 1.02 | 1585 |
| 2024-09-20 22:21:40.414 | MS1 | 121.4656732137 | 31.1446201628 | 335 | 504990 | -80.71 | 14.19 | 322.47 | 0.10 | 2.60 | 1568 |
| 2024-09-20 22:21:41.599 | MS1 | 121.4656612813 | 31.1446339006 | 335 | 504990 | -81.19 | 16.08 | 526.26 | 0.17 | 2.98 | 1590 |
| 2024-09-20 22:21:42.840 | MS1 | 121.4656652771 | 31.1446247533 | 335 | 504990 | -79.04 | 16.70 | 410.20 | 0.19 | 2.14 | 1566 |

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
| 3211309 | 2 | 121.4646680599 | 31.1501279350 | 267 | 13 | 3 | 45.6 | TDD | 425 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3213440 | 1 | 121.4740710074 | 31.1520519998 | 181 | 1 | 12 | 28.2 | TDD | 69 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3247070 | 5 | 121.4726948401 | 31.1556794729 | 308 | 12 | 12 | 16.8 | TDD | 571 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3278503 | 4 | 121.4658041604 | 31.1552592157 | 141 | 2 | 11 | 33.1 | TDD | 753 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3278662 | 3 | 121.4724044319 | 31.1493578534 | 111 | 4 | 7 | 35.3 | TDD | 335 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.379 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.397 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.503 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.503 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.181 | NREventA3 | measId:2;ServCellPCI:549;Se... |
| 2024-09-20 22:21:34.421 | NRHandoverAttempt | SourcePCI:549;SourceNR-ARFC... |
| 2024-09-20 22:21:34.455 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.465 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:34.572 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.572 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.181 | NREventA3 | measId:2;ServCellPCI:792;Se... |
| 2024-09-20 22:21:36.421 | NRHandoverAttempt | SourcePCI:792;SourceNR-ARFC... |
| 2024-09-20 22:21:36.471 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.486 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.591 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.591 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.181 | NREventA3 | measId:2;ServCellPCI:549;Se... |
| 2024-09-20 22:21:38.421 | NRHandoverAttempt | SourcePCI:549;SourceNR-ARFC... |
| 2024-09-20 22:21:38.465 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.478 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.622 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.622 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213440 | 1 | 7.1762 | 13.5965 | -116.4050 | 13.8431 | 102.1122 | 0.0045 | 0.0065 |
| 2024_09_20 22:00 | 3211309 | 2 | 12.6851 | 8.8338 | -114.0619 | 17.9745 | 167.6361 | 0.0186 | 0.0133 |
| 2024_09_20 22:00 | 3278662 | 3 | 8.7978 | 16.3283 | -114.7632 | 9.3017 | 151.3621 | 0.0194 | 0.0037 |
| 2024_09_20 22:00 | 3278503 | 4 | 14.3263 | 14.5015 | -117.6307 | 15.8464 | 164.3362 | 0.0175 | 0.0167 |
| 2024_09_20 22:00 | 3247070 | 5 | 13.0662 | 16.0984 | -115.4379 | 11.5442 | 111.0402 | 0.0037 | 0.0094 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414303_E0E55339 | 504990 | 69 | -84.9 | 504990 | 335 | -86.0 | 504990 | 753 | -89.9 | 504990 | 571 |
| MR_1774414303_4C9F1484 | 504990 | 335 | -84.7 | 504990 | 69 | -86.3 | 504990 | 753 | -86.8 | 504990 | 571 |
| MR_1774414303_D890B323 | 504990 | 69 | -88.1 | 504990 | 335 | -88.4 | 504990 | 753 | -88.8 | 504990 | 571 |
| MR_1774414303_742518FB | 504990 | 335 | -85.6 | 504990 | 69 | -86.0 | 504990 | 753 | -87.9 | 504990 | 571 |
| MR_1774414303_14E72D4C | 504990 | 335 | -87.5 | 504990 | 69 | -88.4 | 504990 | 753 | -87.4 | 504990 | 571 |
| MR_1774414303_D60A9DD7 | 504990 | 69 | -86.1 | 504990 | 335 | -88.3 | 504990 | 753 | -88.2 | 504990 | 571 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 509: `df7b2bff-ce2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `df7b2bff-ce20-400a-b4b4-98edbf62c535` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3249636_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[509] topology](images/train_0509.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247758_4
- `C2`: Decrease transmission power for 3249636_2
- `C3`: Decrease A3 Offset threshold for 3249636_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Press down the tilt angle  of 3247758_4 by 10 degrees
- `C6`: Increase transmission power for 3247758_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247758_4
- `C8`: Increase A3 Offset threshold for 3249636_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249636_2 **← 정답**
- `C10`: Lift the tilt angle of 3249636_2 by 2 degrees
- `C11`: Decrease transmission power for 3247758_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249636_2
- `C13`: Decrease A3 Offset threshold for 3247758_4
- `C14`: Lift the tilt angle  of 3247758_4 by 10 degrees
- `C15`: Adjust the azimuth of 3247758_4 by 50 degrees
- `C16`: Add neighbor relationship between 3223098_1 and 3247758_4
- `C17`: Check test server and transmission issues
- `C18`: Add neighbor relationship between 3249636_2 and 3247758_4
- `C19`: Increase transmission power for 3249636_2
- `C20`: Press down the tilt angle of 3249636_2 by 2 degrees
- `C21`: Increase A3 Offset threshold for 3247758_4
- `C22`: Adjust the azimuth of 3249636_2 by 21 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.522 | MS1 | 121.4656666973 | 31.1446313851 | 835 | 504990 | -86.09 | 15.57 | 431.48 | 0.05 | 2.26 | 1599 |
| 2024-09-20 22:21:32.627 | MS1 | 121.4656656492 | 31.1446323337 | 835 | 504990 | -87.05 | 13.05 | 354.74 | 0.10 | 2.48 | 1590 |
| 2024-09-20 22:21:33.237 | MS1 | 121.4656754022 | 31.1446239109 | 835 | 504990 | -85.30 | 14.53 | 403.21 | 0.06 | 2.08 | 1563 |
| 2024-09-20 22:21:34.289 | MS1 | 121.4656617404 | 31.1446308342 | 835 | 504990 | -86.62 | 15.90 | 91.56 | 0.66 | 2.58 | 650 |
| 2024-09-20 22:21:35.826 | MS1 | 121.4656651486 | 31.1446331777 | 835 | 504990 | -87.56 | 15.20 | 79.97 | 0.55 | 2.82 | 600 |
| 2024-09-20 22:21:36.568 | MS1 | 121.4656731674 | 31.1446318680 | 835 | 504990 | -90.39 | 15.69 | 81.32 | 0.69 | 2.49 | 549 |
| 2024-09-20 22:21:37.133 | MS1 | 121.4656581493 | 31.1446322233 | 835 | 504990 | -89.96 | 11.33 | 77.94 | 0.52 | 2.21 | 611 |
| 2024-09-20 22:21:38.950 | MS1 | 121.4656639656 | 31.1446293829 | 835 | 504990 | -93.69 | 12.13 | 99.53 | 0.50 | 2.54 | 553 |
| 2024-09-20 22:21:39.378 | MS1 | 121.4656763949 | 31.1446275329 | 835 | 504990 | -93.46 | 7.64 | 63.31 | 0.68 | 2.73 | 691 |
| 2024-09-20 22:21:40.544 | MS1 | 121.4656779177 | 31.1446210299 | 835 | 504990 | -92.05 | 10.57 | 460.40 | 0.07 | 2.17 | 1567 |
| 2024-09-20 22:21:41.400 | MS1 | 121.4656596676 | 31.1446369064 | 835 | 504990 | -91.03 | 8.87 | 498.62 | 0.17 | 2.43 | 1590 |
| 2024-09-20 22:21:42.706 | MS1 | 121.4656667435 | 31.1446304243 | 835 | 504990 | -89.55 | 12.32 | 455.48 | 0.08 | 2.38 | 1586 |

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
| 3218551 | 3 | 121.4699410243 | 31.1534418110 | 43 | 14 | 0 | 16.4 | TDD | 454 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3223098 | 1 | 121.4701828025 | 31.1518055806 | 16 | 5 | 7 | 42.4 | TDD | 682 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3247758 | 4 | 121.4660348471 | 31.1440840792 | 175 | 2 | 12 | 15.3 | TDD | 223 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3249636 | 2 | 121.4732820551 | 31.1541875419 | 235 | 1 | 4 | 24.2 | TDD | 835 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.062 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.079 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.187 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.187 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.917 | NREventA3 | measId:2;ServCellPCI:202;Se... |
| 2024-09-20 22:21:38.157 | NRHandoverAttempt | SourcePCI:202;SourceNR-ARFC... |
| 2024-09-20 22:21:38.201 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.215 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.333 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.333 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223098 | 1 | 17.6743 | 10.5541 | -116.9061 | 13.2288 | 90.0031 | 0.0111 | 0.0083 |
| 2024_09_20 22:00 | 3249636 | 2 | 16.6089 | 13.9930 | -115.7057 | 7.8340 | 129.3668 | 0.0072 | 0.0195 |
| 2024_09_20 22:00 | 3218551 | 3 | 15.5743 | 11.6783 | -114.4684 | 11.5114 | 94.7311 | 0.0118 | 0.0040 |
| 2024_09_20 22:00 | 3247758 | 4 | 19.8793 | 13.3318 | -114.0877 | 18.6243 | 94.2616 | 0.0015 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413968_B5059F6D | 504990 | 835 | -85.3 | 504990 | 223 | -94.5 | 504990 | 682 | -94.0 | 504990 | 454 |
| MR_1774413968_AFE93A58 | 504990 | 835 | -85.7 | 504990 | 223 | -92.7 | 504990 | 682 | -95.0 | 504990 | 454 |
| MR_1774413968_8A9DBEE9 | 504990 | 835 | -85.3 | 504990 | 223 | -94.4 | 504990 | 682 | -94.2 | 504990 | 454 |
| MR_1774413968_5E562F0D | 504990 | 835 | -86.2 | 504990 | 223 | -92.0 | 504990 | 682 | -94.8 | 504990 | 454 |
| MR_1774413968_2D2074F7 | 504990 | 835 | -86.1 | 504990 | 223 | -92.4 | 504990 | 682 | -95.6 | 504990 | 454 |
| MR_1774413968_18D0556D | 504990 | 835 | -87.9 | 504990 | 223 | -94.0 | 504990 | 682 | -93.6 | 504990 | 454 |
| MR_1774413968_CEBFC791 | 504990 | 835 | -85.4 | 504990 | 223 | -92.8 | 504990 | 682 | -96.2 | 504990 | 454 |
| MR_1774413968_EDA9C1C2 | 504990 | 835 | -85.3 | 504990 | 223 | -91.3 | 504990 | 682 | -93.7 | 504990 | 454 |

> *... 2개 열 생략 (전체 14열)*

---
