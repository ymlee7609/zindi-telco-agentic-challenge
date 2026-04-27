# Track A 문제 분석 — test[310]~test[319]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[310] ~ test[319] (10개)

## 목차

1. [문제 310: `4a730640-036...`](#310) — single-answer
2. [문제 311: `3e0a4e06-7c4...`](#311) — single-answer
3. [문제 312: `5f626d52-a13...`](#312) — single-answer
4. [문제 313: `362e7e17-936...`](#313) — single-answer
5. [문제 314: `2fd4d917-31b...`](#314) — single-answer
6. [문제 315: `2becd14a-c15...`](#315) — single-answer
7. [문제 316: `206f4053-dc7...`](#316) — single-answer
8. [문제 317: `dfe02cee-859...`](#317) — single-answer
9. [문제 318: `5d036c3c-734...`](#318) — single-answer
10. [문제 319: `b5d68670-276...`](#319) — single-answer

---

### 문제 310: `4a730640-036...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4a730640-0365-4141-a8c1-fe74eb2533ce` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[310] topology](images/test_0310.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221801_4
- `C2`: Decrease transmission power for 3274972_2
- `C3`: Increase transmission power for 3274972_2
- `C4`: Adjust the azimuth of 3274972_2 by 50 degrees
- `C5`: Check test server and transmission issues
- `C6`: Decrease transmission power for 3221801_4
- `C7`: Increase A3 Offset threshold for 3274972_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274972_2
- `C9`: Decrease A3 Offset threshold for 3221801_4
- `C10`: Lift the tilt angle  of 3221801_4 by 3 degrees
- `C11`: Add neighbor relationship between 3274972_2 and 3221801_4
- `C12`: Add neighbor relationship between 3245712_3 and 3221801_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221801_4
- `C14`: Decrease A3 Offset threshold for 3274972_2
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Lift the tilt angle of 3274972_2 by 3 degrees
- `C17`: Increase A3 Offset threshold for 3221801_4
- `C18`: Press down the tilt angle of 3274972_2 by 3 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274972_2
- `C20`: Adjust the azimuth of 3221801_4 by 50 degrees
- `C21`: Press down the tilt angle  of 3221801_4 by 3 degrees
- `C22`: Increase transmission power for 3221801_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.619 | MS1 | 121.4656593560 | 31.1446296058 | 385 | 504990 | -85.42 | 12.86 | 348.15 | 0.16 | 2.54 | 1590 |
| 2024-09-20 22:21:32.884 | MS1 | 121.4656748185 | 31.1446295328 | 385 | 504990 | -85.45 | 13.99 | 416.44 | 0.17 | 2.56 | 1592 |
| 2024-09-20 22:21:33.567 | MS1 | 121.4656741327 | 31.1446285569 | 385 | 504990 | -91.77 | 17.77 | 564.13 | 0.10 | 2.99 | 1576 |
| 2024-09-20 22:21:34.264 | MS1 | 121.4656594005 | 31.1446363172 | 385 | 504990 | -91.71 | 13.85 | 93.91 | 0.55 | 2.03 | 603 |
| 2024-09-20 22:21:35.819 | MS1 | 121.4656591443 | 31.1446256046 | 385 | 504990 | -89.54 | 13.97 | 101.68 | 0.64 | 2.61 | 511 |
| 2024-09-20 22:21:36.784 | MS1 | 121.4656672380 | 31.1446340843 | 385 | 504990 | -86.58 | 12.87 | 54.40 | 0.70 | 2.36 | 653 |
| 2024-09-20 22:21:37.834 | MS1 | 121.4656701141 | 31.1446347873 | 385 | 504990 | -92.51 | 10.07 | 76.90 | 0.57 | 2.53 | 677 |
| 2024-09-20 22:21:38.474 | MS1 | 121.4656668689 | 31.1446303075 | 385 | 504990 | -92.92 | 8.73 | 84.54 | 0.53 | 2.97 | 560 |
| 2024-09-20 22:21:39.637 | MS1 | 121.4656587746 | 31.1446224071 | 385 | 504990 | -93.45 | 12.53 | 69.55 | 0.51 | 2.54 | 666 |
| 2024-09-20 22:21:40.330 | MS1 | 121.4656771383 | 31.1446260490 | 385 | 504990 | -91.98 | 12.95 | 336.05 | 0.17 | 2.27 | 1571 |
| 2024-09-20 22:21:41.134 | MS1 | 121.4656757860 | 31.1446243961 | 385 | 504990 | -92.96 | 11.75 | 516.32 | 0.03 | 2.60 | 1566 |
| 2024-09-20 22:21:42.765 | MS1 | 121.4656635898 | 31.1446328357 | 385 | 504990 | -91.96 | 7.70 | 447.85 | 0.12 | 2.31 | 1569 |

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
| 3221801 | 4 | 121.4697795088 | 31.1460957324 | 138 | 0 | 7 | 22.8 | TDD | 406 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3241388 | 1 | 121.4687734117 | 31.1449459078 | 271 | 13 | 10 | 26.6 | TDD | 472 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3245712 | 3 | 121.4666070332 | 31.1472643881 | 137 | 15 | 1 | 20.1 | TDD | 461 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3274972 | 2 | 121.4724740727 | 31.1559548841 | 257 | 2 | 1 | 30.2 | TDD | 385 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.884 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.906 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.016 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.016 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.743 | NREventA3 | measId:2;ServCellPCI:106;Se... |
| 2024-09-20 22:21:37.983 | NRHandoverAttempt | SourcePCI:106;SourceNR-ARFC... |
| 2024-09-20 22:21:38.025 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.037 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.177 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.177 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241388 | 1 | 10.0786 | 13.0000 | -116.3592 | 10.2476 | 137.4706 | 0.0023 | 0.0165 |
| 2024_09_20 22:00 | 3274972 | 2 | 18.9101 | 13.0043 | -114.4660 | 5.9376 | 184.5356 | 0.0164 | 0.0180 |
| 2024_09_20 22:00 | 3245712 | 3 | 15.6605 | 7.7910 | -117.6501 | 16.0964 | 193.6006 | 0.0174 | 0.0150 |
| 2024_09_20 22:00 | 3221801 | 4 | 19.5277 | 19.3568 | -115.3462 | 6.1963 | 119.9844 | 0.0090 | 0.0156 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413917_8AE58EA4 | 504990 | 385 | -92.1 | 504990 | 406 | -89.3 | 504990 | 461 | -99.2 | 504990 | 472 |
| MR_1774413917_A67916D0 | 504990 | 385 | -92.3 | 504990 | 406 | -90.1 | 504990 | 461 | -99.7 | 504990 | 472 |
| MR_1774413917_9D6553FC | 504990 | 385 | -92.6 | 504990 | 406 | -91.2 | 504990 | 461 | -97.4 | 504990 | 472 |
| MR_1774413917_C5DD7D05 | 504990 | 385 | -93.5 | 504990 | 406 | -91.0 | 504990 | 461 | -97.8 | 504990 | 472 |
| MR_1774413917_1D1D0581 | 504990 | 385 | -92.0 | 504990 | 406 | -91.8 | 504990 | 461 | -97.5 | 504990 | 472 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 311: `3e0a4e06-7c4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3e0a4e06-7c4c-4d62-b133-5f1950c508a5` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[311] topology](images/test_0311.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253848_4
- `C3`: Increase transmission power for 3217715_1
- `C4`: Add neighbor relationship between 3217715_1 and 3253848_4
- `C5`: Press down the tilt angle  of 3253848_4 by 9 degrees
- `C6`: Adjust the azimuth of 3217715_1 by 50 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217715_1
- `C8`: Decrease A3 Offset threshold for 3217715_1
- `C9`: Increase transmission power for 3253848_4
- `C10`: Add neighbor relationship between 3230060_3 and 3253848_4
- `C11`: Check test server and transmission issues
- `C12`: Increase A3 Offset threshold for 3253848_4
- `C13`: Decrease A3 Offset threshold for 3253848_4
- `C14`: Increase A3 Offset threshold for 3217715_1
- `C15`: Decrease transmission power for 3217715_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217715_1
- `C17`: Decrease transmission power for 3253848_4
- `C18`: Adjust the azimuth of 3253848_4 by 50 degrees
- `C19`: Lift the tilt angle  of 3253848_4 by 9 degrees
- `C20`: Press down the tilt angle of 3217715_1 by 3 degrees
- `C21`: Lift the tilt angle of 3217715_1 by 3 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253848_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.756 | MS1 | 121.4656672581 | 31.1446256061 | 729 | 504990 | -85.83 | 16.91 | 569.11 | 0.11 | 2.25 | 1579 |
| 2024-09-20 22:21:32.861 | MS1 | 121.4656716939 | 31.1446215535 | 729 | 504990 | -90.61 | 17.66 | 453.49 | 0.06 | 2.20 | 1580 |
| 2024-09-20 22:21:33.966 | MS1 | 121.4656683344 | 31.1446209402 | 729 | 504990 | -85.24 | 17.35 | 420.01 | 0.05 | 2.67 | 1565 |
| 2024-09-20 22:21:34.262 | MS1 | 121.4656621654 | 31.1446241007 | 729 | 504990 | -85.07 | 14.38 | 62.28 | 0.03 | 2.46 | 1598 |
| 2024-09-20 22:21:35.379 | MS1 | 121.4656604172 | 31.1446237241 | 729 | 504990 | -89.65 | 12.58 | 52.80 | 0.04 | 2.48 | 1568 |
| 2024-09-20 22:21:36.230 | MS1 | 121.4656674433 | 31.1446301880 | 729 | 504990 | -85.83 | 16.98 | 45.00 | 0.03 | 2.79 | 1598 |
| 2024-09-20 22:21:37.752 | MS1 | 121.4656661077 | 31.1446189748 | 729 | 504990 | -93.44 | 7.31 | 58.64 | 0.05 | 2.88 | 1561 |
| 2024-09-20 22:21:38.238 | MS1 | 121.4656680370 | 31.1446260503 | 729 | 504990 | -91.99 | 10.09 | 59.89 | 0.12 | 2.07 | 1577 |
| 2024-09-20 22:21:39.693 | MS1 | 121.4656771367 | 31.1446243025 | 729 | 504990 | -93.83 | 12.65 | 85.39 | 0.10 | 2.05 | 1572 |
| 2024-09-20 22:21:40.204 | MS1 | 121.4656670310 | 31.1446263188 | 729 | 504990 | -93.92 | 11.09 | 552.03 | 0.19 | 2.82 | 1565 |
| 2024-09-20 22:21:41.658 | MS1 | 121.4656585242 | 31.1446278405 | 729 | 504990 | -92.97 | 10.03 | 515.56 | 0.16 | 2.64 | 1571 |
| 2024-09-20 22:21:42.159 | MS1 | 121.4656603010 | 31.1446350658 | 729 | 504990 | -89.29 | 12.97 | 481.29 | 0.12 | 2.46 | 1576 |

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
| 3217715 | 1 | 121.4709211936 | 31.1490518214 | 74 | 2 | 2 | 16.3 | TDD | 729 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3221643 | 2 | 121.4709538661 | 31.1508993123 | 157 | 2 | 12 | 19.8 | TDD | 340 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3230060 | 3 | 121.4653393822 | 31.1558757255 | 18 | 3 | 9 | 47.1 | TDD | 5 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3253848 | 4 | 121.4642865310 | 31.1551662413 | 296 | 8 | 11 | 19.7 | TDD | 70 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.140 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.243 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.243 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.963 | NREventA3 | measId:2;ServCellPCI:982;Se... |
| 2024-09-20 22:21:38.203 | NRHandoverAttempt | SourcePCI:982;SourceNR-ARFC... |
| 2024-09-20 22:21:38.237 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.247 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.385 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.385 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3217715 | 1 | 91.4882 | 94.8146 | -117.2427 | 11.3362 | 140.5349 | 0.0099 | 0.0054 |
| 2024_09_19 22:00 | 3221643 | 2 | 88.8601 | 92.4129 | -117.3011 | 11.0528 | 136.6099 | 0.0107 | 0.0170 |
| 2024_09_19 22:00 | 3230060 | 3 | 76.3599 | 89.2257 | -115.8639 | 14.9796 | 166.3581 | 0.0020 | 0.0177 |
| 2024_09_19 22:00 | 3253848 | 4 | 79.1174 | 75.1959 | -115.1388 | 10.6295 | 176.6837 | 0.0094 | 0.0118 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414034_D4D44DE8 | 504990 | 729 | -86.5 | 504990 | 70 | -86.4 | 504990 | 5 | -96.0 | 504990 | 340 |
| MR_1774414034_A3771F26 | 504990 | 729 | -85.9 | 504990 | 70 | -85.7 | 504990 | 5 | -92.8 | 504990 | 340 |
| MR_1774414034_DD5F2374 | 504990 | 729 | -83.2 | 504990 | 70 | -84.5 | 504990 | 5 | -96.3 | 504990 | 340 |
| MR_1774414034_EA5CF85F | 504990 | 729 | -84.4 | 504990 | 70 | -84.8 | 504990 | 5 | -94.0 | 504990 | 340 |
| MR_1774414034_89F6D04C | 504990 | 729 | -84.7 | 504990 | 70 | -84.5 | 504990 | 5 | -94.5 | 504990 | 340 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 312: `5f626d52-a13...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5f626d52-a13d-4421-a7ed-bd66051af19a` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[312] topology](images/test_0312.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3269155_3 by 50 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase transmission power for 3269155_3
- `C4`: Check test server and transmission issues
- `C5`: Lift the tilt angle of 3269155_3 by 2 degrees
- `C6`: Add neighbor relationship between 3212812_1 and 3247691_4
- `C7`: Increase A3 Offset threshold for 3269155_3
- `C8`: Press down the tilt angle of 3269155_3 by 2 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247691_4
- `C10`: Increase A3 Offset threshold for 3247691_4
- `C11`: Decrease A3 Offset threshold for 3269155_3
- `C12`: Adjust the azimuth of 3247691_4 by 50 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247691_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269155_3
- `C15`: Increase transmission power for 3247691_4
- `C16`: Lift the tilt angle  of 3247691_4 by 1 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269155_3
- `C18`: Decrease transmission power for 3247691_4
- `C19`: Press down the tilt angle  of 3247691_4 by 1 degrees
- `C20`: Decrease transmission power for 3269155_3
- `C21`: Decrease A3 Offset threshold for 3247691_4
- `C22`: Add neighbor relationship between 3269155_3 and 3247691_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.478 | MS1 | 121.4656700315 | 31.1446263213 | 636 | 504990 | -89.70 | 12.20 | 334.74 | 0.14 | 2.54 | 1574 |
| 2024-09-20 22:21:32.513 | MS1 | 121.4656759291 | 31.1446255412 | 636 | 504990 | -86.59 | 17.07 | 344.70 | 0.05 | 2.18 | 1599 |
| 2024-09-20 22:21:33.146 | MS1 | 121.4656600265 | 31.1446269730 | 636 | 504990 | -90.72 | 14.81 | 312.94 | 0.10 | 2.40 | 1598 |
| 2024-09-20 22:21:34.777 | MS1 | 121.4656670776 | 31.1446301857 | 636 | 504990 | -87.92 | 16.16 | 57.33 | 0.19 | 2.20 | 1575 |
| 2024-09-20 22:21:35.756 | MS1 | 121.4656776160 | 31.1446229441 | 636 | 504990 | -90.29 | 16.10 | 88.43 | 0.01 | 2.68 | 1576 |
| 2024-09-20 22:21:36.270 | MS1 | 121.4656755643 | 31.1446221279 | 636 | 504990 | -86.75 | 17.51 | 57.17 | 0.11 | 2.65 | 1564 |
| 2024-09-20 22:21:37.358 | MS1 | 121.4656604065 | 31.1446339550 | 636 | 504990 | -91.80 | 12.17 | 80.04 | 0.13 | 2.98 | 1586 |
| 2024-09-20 22:21:38.572 | MS1 | 121.4656632988 | 31.1446321532 | 636 | 504990 | -92.15 | 11.33 | 73.69 | 0.13 | 2.80 | 1578 |
| 2024-09-20 22:21:39.319 | MS1 | 121.4656653491 | 31.1446200197 | 636 | 504990 | -91.97 | 12.04 | 54.19 | 0.09 | 2.52 | 1564 |
| 2024-09-20 22:21:40.825 | MS1 | 121.4656633682 | 31.1446210630 | 636 | 504990 | -91.30 | 8.53 | 384.06 | 0.15 | 2.63 | 1562 |
| 2024-09-20 22:21:41.987 | MS1 | 121.4656611656 | 31.1446261610 | 636 | 504990 | -93.33 | 12.51 | 422.58 | 0.11 | 2.58 | 1594 |
| 2024-09-20 22:21:42.774 | MS1 | 121.4656762513 | 31.1446345707 | 636 | 504990 | -92.06 | 11.93 | 514.05 | 0.19 | 2.87 | 1578 |

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
| 3212812 | 1 | 121.4744232719 | 31.1525098712 | 334 | 11 | 4 | 25.7 | TDD | 120 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3217973 | 2 | 121.4684407324 | 31.1552120618 | 159 | 2 | 6 | 16.0 | TDD | 947 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3247691 | 4 | 121.4746484075 | 31.1471344210 | 155 | 0 | 0 | 19.2 | TDD | 750 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3269155 | 3 | 121.4684558674 | 31.1506819152 | 122 | 0 | 0 | 23.3 | TDD | 636 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.038 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.057 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.181 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.181 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.920 | NREventA3 | measId:2;ServCellPCI:53;Ser... |
| 2024-09-20 22:21:38.160 | NRHandoverAttempt | SourcePCI:53;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.206 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.216 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.349 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.349 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3212812 | 1 | 91.5709 | 80.5911 | -114.4978 | 19.4130 | 146.4104 | 0.0129 | 0.0172 |
| 2024_09_19 22:00 | 3217973 | 2 | 79.6617 | 88.5783 | -117.7833 | 13.9505 | 180.8611 | 0.0115 | 0.0056 |
| 2024_09_19 22:00 | 3269155 | 3 | 87.5918 | 94.2222 | -114.3220 | 10.5410 | 160.5996 | 0.0030 | 0.0064 |
| 2024_09_19 22:00 | 3247691 | 4 | 86.5108 | 75.7418 | -115.0583 | 5.9340 | 123.9036 | 0.0006 | 0.0164 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412654_BDD6B0C1 | 504990 | 636 | -87.9 | 504990 | 750 | -96.6 | 504990 | 120 | -97.8 | 504990 | 947 |
| MR_1774412654_C0A5B4FC | 504990 | 636 | -88.2 | 504990 | 750 | -93.7 | 504990 | 120 | -99.8 | 504990 | 947 |
| MR_1774412654_395D51E6 | 504990 | 636 | -89.3 | 504990 | 750 | -94.9 | 504990 | 120 | -97.4 | 504990 | 947 |
| MR_1774412654_F59B5C83 | 504990 | 636 | -88.0 | 504990 | 750 | -95.6 | 504990 | 120 | -98.1 | 504990 | 947 |
| MR_1774412654_66D0A795 | 504990 | 636 | -88.0 | 504990 | 750 | -96.0 | 504990 | 120 | -97.9 | 504990 | 947 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 313: `362e7e17-936...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `362e7e17-9362-4ed4-8728-056232f17a3e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[313] topology](images/test_0313.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3259844_1
- `C2`: Lift the tilt angle  of 3259844_1 by 1 degrees
- `C3`: Decrease A3 Offset threshold for 3236932_3
- `C4`: Press down the tilt angle of 3236932_3 by 8 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259844_1
- `C6`: Increase A3 Offset threshold for 3259844_1
- `C7`: Adjust the azimuth of 3259844_1 by 34 degrees
- `C8`: Lift the tilt angle of 3236932_3 by 8 degrees
- `C9`: Check test server and transmission issues
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236932_3
- `C11`: Add neighbor relationship between 3236932_3 and 3259844_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236932_3
- `C13`: Increase transmission power for 3259844_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase A3 Offset threshold for 3236932_3
- `C16`: Decrease A3 Offset threshold for 3259844_1
- `C17`: Add neighbor relationship between 3268390_2 and 3259844_1
- `C18`: Increase transmission power for 3236932_3
- `C19`: Decrease transmission power for 3236932_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259844_1
- `C21`: Adjust the azimuth of 3236932_3 by 50 degrees
- `C22`: Press down the tilt angle  of 3259844_1 by 1 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.661 | MS1 | 121.4656756755 | 31.1446193830 | 901 | 504990 | -78.89 | 16.06 | 496.75 | 0.06 | 2.44 | 1578 |
| 2024-09-20 22:21:32.202 | MS1 | 121.4656631623 | 31.1446229164 | 901 | 504990 | -80.69 | 13.61 | 502.54 | 0.00 | 2.41 | 1598 |
| 2024-09-20 22:21:33.815 | MS1 | 121.4656691210 | 31.1446369051 | 901 | 504990 | -82.83 | 13.39 | 479.52 | 0.08 | 2.39 | 1591 |
| 2024-09-20 22:21:34.511 | MS1 | 121.4656648484 | 31.1446319557 | 901 | 504990 | -94.46 | -1.77 | 33.17 | 0.17 | 1.20 | 1560 |
| 2024-09-20 22:21:35.655 | MS1 | 121.4656627810 | 31.1446373781 | 901 | 504990 | -87.94 | -1.87 | 45.45 | 0.04 | 1.12 | 1583 |
| 2024-09-20 22:21:36.722 | MS1 | 121.4656585692 | 31.1446369956 | 901 | 504990 | -88.33 | -1.61 | 67.07 | 0.05 | 1.17 | 1572 |
| 2024-09-20 22:21:37.253 | MS1 | 121.4656723421 | 31.1446236249 | 901 | 504990 | -85.63 | -2.44 | 39.52 | 0.03 | 1.47 | 1591 |
| 2024-09-20 22:21:38.366 | MS1 | 121.4656688705 | 31.1446280334 | 901 | 504990 | -78.52 | 16.09 | 593.03 | 0.18 | 1.17 | 1587 |
| 2024-09-20 22:21:39.300 | MS1 | 121.4656702857 | 31.1446202187 | 901 | 504990 | -84.10 | 16.90 | 466.39 | 0.05 | 1.33 | 1592 |
| 2024-09-20 22:21:40.805 | MS1 | 121.4656668965 | 31.1446254103 | 901 | 504990 | -75.72 | 17.86 | 375.37 | 0.00 | 2.90 | 1571 |
| 2024-09-20 22:21:41.860 | MS1 | 121.4656584974 | 31.1446341285 | 901 | 504990 | -81.12 | 16.89 | 305.83 | 0.18 | 2.07 | 1596 |
| 2024-09-20 22:21:42.528 | MS1 | 121.4656657476 | 31.1446242656 | 901 | 504990 | -83.44 | 16.62 | 477.57 | 0.10 | 2.79 | 1592 |

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
| 3222286 | 4 | 121.4746385781 | 31.1518592961 | 17 | 2 | 6 | 26.3 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3236932 | 3 | 121.4732801613 | 31.1491239720 | 112 | 6 | 6 | 34.5 | TDD | 901 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3259844 | 1 | 121.4647531339 | 31.1539605756 | 209 | 0 | 8 | 21.6 | TDD | 65 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3268390 | 2 | 121.4720220449 | 31.1473957588 | 19 | 0 | 10 | 45.3 | TDD | 556 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.826 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.848 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.984 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.984 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.711 | NREventA3 | measId:2;ServCellPCI:444;Se... |
| 2024-09-20 22:21:35.711 | NREventA3 | measId:2;ServCellPCI:444;Se... |
| 2024-09-20 22:21:36.711 | NREventA3 | measId:2;ServCellPCI:444;Se... |
| 2024-09-20 22:21:39.211 | NRRRCReestablishAttempt | PCI:444 |
| 2024-09-20 22:21:39.222 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.235 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.364 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.364 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259844 | 1 | 10.5098 | 19.7825 | -117.8152 | 9.6002 | 140.5135 | 0.0021 | 0.0094 |
| 2024_09_20 22:00 | 3268390 | 2 | 6.2143 | 6.6770 | -114.2729 | 10.8920 | 89.4748 | 0.0034 | 0.0064 |
| 2024_09_20 22:00 | 3236932 | 3 | 11.6977 | 5.4468 | -115.1012 | 9.5073 | 177.7560 | 0.0124 | 0.1493 |
| 2024_09_20 22:00 | 3222286 | 4 | 10.4170 | 12.9049 | -116.6587 | 12.9808 | 133.2105 | 0.0071 | 0.0053 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415802_F0305268 | 504990 | 901 | -94.2 | 504990 | 65 | -88.2 | 504990 | 556 | -94.5 | 504990 | 382 |
| MR_1774415802_46239DB3 | 504990 | 901 | -96.2 | 504990 | 65 | -87.4 | 504990 | 556 | -93.1 | 504990 | 382 |
| MR_1774415802_6CC5133F | 504990 | 901 | -93.6 | 504990 | 65 | -89.2 | 504990 | 556 | -93.7 | 504990 | 382 |
| MR_1774415802_7D6EE545 | 504990 | 901 | -95.3 | 504990 | 65 | -90.1 | 504990 | 556 | -94.5 | 504990 | 382 |
| MR_1774415802_24948D89 | 504990 | 901 | -93.7 | 504990 | 65 | -90.4 | 504990 | 556 | -94.5 | 504990 | 382 |
| MR_1774415802_2567A63F | 504990 | 65 | -87.2 | 504990 | 901 | -93.5 | 504990 | 556 | -93.4 | 504990 | 382 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 314: `2fd4d917-31b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2fd4d917-31bc-4ffd-8b7b-4c106417466d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[314] topology](images/test_0314.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262708_3
- `C2`: Increase A3 Offset threshold for 3225291_2
- `C3`: Add neighbor relationship between 3268149_1 and 3225291_2
- `C4`: Decrease A3 Offset threshold for 3225291_2
- `C5`: Adjust the azimuth of 3225291_2 by 19 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225291_2
- `C7`: Add neighbor relationship between 3262708_3 and 3225291_2
- `C8`: Increase transmission power for 3262708_3
- `C9`: Increase transmission power for 3225291_2
- `C10`: Decrease transmission power for 3225291_2
- `C11`: Lift the tilt angle  of 3225291_2 by 5 degrees
- `C12`: Increase A3 Offset threshold for 3262708_3
- `C13`: Check test server and transmission issues
- `C14`: Press down the tilt angle of 3262708_3 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3262708_3
- `C16`: Press down the tilt angle  of 3225291_2 by 5 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262708_3
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease transmission power for 3262708_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225291_2
- `C21`: Adjust the azimuth of 3262708_3 by 50 degrees
- `C22`: Lift the tilt angle of 3262708_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.326 | MS1 | 121.4656687855 | 31.1446235845 | 395 | 504990 | -81.38 | 13.50 | 319.95 | 0.09 | 2.80 | 1599 |
| 2024-09-20 22:21:32.722 | MS1 | 121.4656697431 | 31.1446288444 | 395 | 504990 | -76.75 | 15.51 | 356.38 | 0.02 | 2.30 | 1564 |
| 2024-09-20 22:21:33.295 | MS1 | 121.4656635688 | 31.1446251556 | 395 | 504990 | -77.29 | 13.17 | 400.25 | 0.09 | 2.68 | 1569 |
| 2024-09-20 22:21:34.168 | MS1 | 121.4656617669 | 31.1446206846 | 395 | 504990 | -94.24 | -3.88 | 62.13 | 0.02 | 1.21 | 1598 |
| 2024-09-20 22:21:35.698 | MS1 | 121.4656668151 | 31.1446348833 | 395 | 504990 | -92.82 | -0.04 | 36.41 | 0.07 | 1.20 | 1586 |
| 2024-09-20 22:21:36.647 | MS1 | 121.4656643027 | 31.1446215947 | 395 | 504990 | -86.01 | -2.07 | 40.72 | 0.14 | 1.01 | 1599 |
| 2024-09-20 22:21:37.127 | MS1 | 121.4656733275 | 31.1446254621 | 395 | 504990 | -89.81 | -1.08 | 42.02 | 0.19 | 1.43 | 1579 |
| 2024-09-20 22:21:38.446 | MS1 | 121.4656660251 | 31.1446255390 | 395 | 504990 | -81.74 | 12.27 | 470.32 | 0.03 | 1.36 | 1595 |
| 2024-09-20 22:21:39.656 | MS1 | 121.4656754890 | 31.1446367142 | 395 | 504990 | -82.02 | 12.10 | 407.94 | 0.05 | 1.18 | 1576 |
| 2024-09-20 22:21:40.386 | MS1 | 121.4656684572 | 31.1446277624 | 395 | 504990 | -83.25 | 13.01 | 409.44 | 0.17 | 2.96 | 1584 |
| 2024-09-20 22:21:41.930 | MS1 | 121.4656730194 | 31.1446212397 | 395 | 504990 | -83.69 | 17.70 | 343.89 | 0.04 | 2.70 | 1579 |
| 2024-09-20 22:21:42.656 | MS1 | 121.4656775954 | 31.1446346772 | 395 | 504990 | -76.09 | 15.72 | 412.19 | 0.17 | 2.01 | 1575 |

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
| 3225291 | 2 | 121.4663667702 | 31.1477011507 | 172 | 1 | 7 | 24.2 | TDD | 450 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3237104 | 4 | 121.4737681024 | 31.1544386983 | 194 | 4 | 4 | 21.1 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3262708 | 3 | 121.4651963582 | 31.1466380632 | 327 | 9 | 6 | 23.7 | TDD | 395 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3268149 | 1 | 121.4647363118 | 31.1441869794 | 123 | 1 | 8 | 26.5 | TDD | 126 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.998 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.022 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.146 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.146 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.859 | NREventA3 | measId:2;ServCellPCI:677;Se... |
| 2024-09-20 22:21:35.859 | NREventA3 | measId:2;ServCellPCI:677;Se... |
| 2024-09-20 22:21:36.859 | NREventA3 | measId:2;ServCellPCI:677;Se... |
| 2024-09-20 22:21:39.359 | NRRRCReestablishAttempt | PCI:677 |
| 2024-09-20 22:21:39.371 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.381 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.524 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.524 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268149 | 1 | 18.8196 | 11.3600 | -114.5589 | 9.5342 | 126.5755 | 0.0022 | 0.0192 |
| 2024_09_20 22:00 | 3225291 | 2 | 17.2626 | 7.9681 | -117.4059 | 11.6841 | 127.5797 | 0.0119 | 0.0021 |
| 2024_09_20 22:00 | 3262708 | 3 | 8.1393 | 15.5738 | -115.8909 | 6.1630 | 105.0176 | 0.0173 | 0.1392 |
| 2024_09_20 22:00 | 3237104 | 4 | 18.3703 | 8.7884 | -117.6641 | 13.4661 | 198.6574 | 0.0029 | 0.0108 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413282_B04E2D45 | 504990 | 450 | -88.2 | 504990 | 395 | -93.8 | 504990 | 126 | -90.0 | 504990 | 382 |
| MR_1774413282_804743DC | 504990 | 395 | -94.4 | 504990 | 450 | -89.2 | 504990 | 126 | -89.7 | 504990 | 382 |
| MR_1774413282_B687CABF | 504990 | 395 | -94.9 | 504990 | 450 | -88.1 | 504990 | 126 | -89.6 | 504990 | 382 |
| MR_1774413282_D6B944CB | 504990 | 450 | -86.6 | 504990 | 395 | -95.2 | 504990 | 126 | -90.6 | 504990 | 382 |
| MR_1774413282_6B81EB1D | 504990 | 395 | -94.4 | 504990 | 450 | -87.0 | 504990 | 126 | -89.7 | 504990 | 382 |
| MR_1774413282_DE677233 | 504990 | 395 | -93.6 | 504990 | 450 | -88.4 | 504990 | 126 | -92.9 | 504990 | 382 |
| MR_1774413282_ED94889C | 504990 | 395 | -94.2 | 504990 | 450 | -86.6 | 504990 | 126 | -91.5 | 504990 | 382 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 315: `2becd14a-c15...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2becd14a-c15f-48e5-a5b1-e0767273b294` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[315] topology](images/test_0315.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3279043_3 by 5 degrees
- `C2`: Check test server and transmission issues
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Lift the tilt angle  of 3246136_4 by 10 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216341_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279043_3
- `C7`: Adjust the azimuth of 3279043_3 by 13 degrees
- `C8`: Decrease transmission power for 3279043_3
- `C9`: Adjust the azimuth of 3246136_4 by 50 degrees
- `C10`: Add neighbor relationship between 3246136_4 and 3216341_2
- `C11`: Increase A3 Offset threshold for 3279043_3
- `C12`: Increase transmission power for 3279043_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279043_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216341_2
- `C15`: Decrease transmission power for 3216341_2
- `C16`: Add neighbor relationship between 3279043_3 and 3216341_2
- `C17`: Increase A3 Offset threshold for 3216341_2
- `C18`: Decrease A3 Offset threshold for 3216341_2
- `C19`: Press down the tilt angle  of 3246136_4 by 10 degrees
- `C20`: Press down the tilt angle of 3279043_3 by 5 degrees
- `C21`: Decrease A3 Offset threshold for 3279043_3
- `C22`: Increase transmission power for 3216341_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.146 | MS1 | 121.4656582948 | 31.1446251823 | 226 | 504990 | -89.71 | 12.17 | 474.12 | 0.14 | 2.59 | 1564 |
| 2024-09-20 22:21:32.483 | MS1 | 121.4656649247 | 31.1446309418 | 226 | 504990 | -91.48 | 16.24 | 524.49 | 0.01 | 2.38 | 1590 |
| 2024-09-20 22:21:33.565 | MS1 | 121.4656586987 | 31.1446337798 | 226 | 504990 | -88.20 | 14.00 | 389.75 | 0.02 | 2.19 | 1562 |
| 2024-09-20 22:21:34.502 | MS1 | 121.4656663683 | 31.1446318186 | 226 | 504990 | -89.07 | 16.84 | 79.87 | 0.15 | 2.56 | 1596 |
| 2024-09-20 22:21:35.524 | MS1 | 121.4656678599 | 31.1446186622 | 226 | 504990 | -86.70 | 14.71 | 86.86 | 0.09 | 2.18 | 1570 |
| 2024-09-20 22:21:36.621 | MS1 | 121.4656665835 | 31.1446337876 | 226 | 504990 | -85.37 | 13.76 | 63.32 | 0.00 | 2.40 | 1588 |
| 2024-09-20 22:21:37.310 | MS1 | 121.4656635740 | 31.1446184508 | 226 | 504990 | -93.72 | 10.83 | 71.52 | 0.12 | 2.38 | 1571 |
| 2024-09-20 22:21:38.129 | MS1 | 121.4656625858 | 31.1446340464 | 226 | 504990 | -91.00 | 8.52 | 64.64 | 0.17 | 2.50 | 1588 |
| 2024-09-20 22:21:39.525 | MS1 | 121.4656614484 | 31.1446371817 | 226 | 504990 | -89.47 | 10.14 | 95.45 | 0.17 | 2.36 | 1599 |
| 2024-09-20 22:21:40.361 | MS1 | 121.4656724508 | 31.1446235358 | 226 | 504990 | -91.04 | 9.36 | 545.50 | 0.19 | 2.70 | 1588 |
| 2024-09-20 22:21:41.656 | MS1 | 121.4656724750 | 31.1446342691 | 226 | 504990 | -91.68 | 12.23 | 575.33 | 0.06 | 2.88 | 1576 |
| 2024-09-20 22:21:42.284 | MS1 | 121.4656715833 | 31.1446256180 | 226 | 504990 | -93.25 | 7.31 | 408.25 | 0.06 | 2.06 | 1583 |

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
| 3216341 | 2 | 121.4740211487 | 31.1461222639 | 313 | 10 | 8 | 21.4 | TDD | 423 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3246136 | 4 | 121.4744635506 | 31.1449772398 | 358 | 13 | 11 | 19.2 | TDD | 799 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3255244 | 1 | 121.4684535303 | 31.1551080558 | 257 | 14 | 11 | 35.3 | TDD | 688 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3279043 | 3 | 121.4720181873 | 31.1518499425 | 204 | 2 | 9 | 44.7 | TDD | 226 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.462 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.483 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.616 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.616 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.302 | NREventA3 | measId:2;ServCellPCI:656;Se... |
| 2024-09-20 22:21:38.542 | NRHandoverAttempt | SourcePCI:656;SourceNR-ARFC... |
| 2024-09-20 22:21:38.590 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.600 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.746 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.746 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255244 | 1 | 8.8944 | 8.4418 | -115.3031 | 6.6402 | 166.9743 | 0.0046 | 0.0040 |
| 2024_09_20 22:00 | 3216341 | 2 | 16.4877 | 11.2229 | -116.7609 | 18.7938 | 116.3780 | 0.0168 | 0.0196 |
| 2024_09_20 22:00 | 3279043 | 3 | 91.5800 | 77.2496 | -115.7626 | 15.4627 | 111.9873 | 0.0192 | 0.0048 |
| 2024_09_20 22:00 | 3246136 | 4 | 10.3273 | 11.9016 | -114.2949 | 11.3689 | 99.3432 | 0.0038 | 0.0192 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413927_B51CFDBC | 504990 | 226 | -91.0 | 504990 | 423 | -94.7 | 504990 | 799 | -93.5 | 504990 | 688 |
| MR_1774413927_4E130604 | 504990 | 226 | -90.7 | 504990 | 423 | -94.3 | 504990 | 799 | -94.4 | 504990 | 688 |
| MR_1774413927_2177130F | 504990 | 226 | -87.5 | 504990 | 423 | -92.9 | 504990 | 799 | -93.5 | 504990 | 688 |
| MR_1774413927_8560951F | 504990 | 226 | -88.2 | 504990 | 423 | -93.4 | 504990 | 799 | -95.4 | 504990 | 688 |
| MR_1774413927_4EA56E74 | 504990 | 226 | -89.4 | 504990 | 423 | -93.7 | 504990 | 799 | -95.7 | 504990 | 688 |
| MR_1774413927_D723EE8D | 504990 | 226 | -90.3 | 504990 | 423 | -94.0 | 504990 | 799 | -94.2 | 504990 | 688 |
| MR_1774413927_3C44E409 | 504990 | 226 | -89.0 | 504990 | 423 | -93.8 | 504990 | 799 | -94.7 | 504990 | 688 |
| MR_1774413927_B31A5B07 | 504990 | 226 | -90.3 | 504990 | 423 | -96.7 | 504990 | 799 | -96.1 | 504990 | 688 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 316: `206f4053-dc7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `206f4053-dc76-44ce-9ad2-2cf976818317` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[316] topology](images/test_0316.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3231599_1
- `C2`: Lift the tilt angle of 3219370_4 by 10 degrees
- `C3`: Decrease transmission power for 3231599_1
- `C4`: Increase A3 Offset threshold for 3219370_4
- `C5`: Decrease A3 Offset threshold for 3231599_1
- `C6`: Decrease transmission power for 3219370_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219370_4
- `C8`: Increase transmission power for 3231599_1
- `C9`: Check test server and transmission issues
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219370_4
- `C12`: Increase transmission power for 3219370_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231599_1
- `C14`: Press down the tilt angle  of 3231599_1 by 4 degrees
- `C15`: Adjust the azimuth of 3219370_4 by 50 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231599_1
- `C17`: Add neighbor relationship between 3222050_3 and 3231599_1
- `C18`: Press down the tilt angle of 3219370_4 by 10 degrees
- `C19`: Lift the tilt angle  of 3231599_1 by 4 degrees
- `C20`: Add neighbor relationship between 3219370_4 and 3231599_1
- `C21`: Adjust the azimuth of 3231599_1 by 50 degrees
- `C22`: Decrease A3 Offset threshold for 3219370_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.898 | MS1 | 121.4656709430 | 31.1446252958 | 790 | 504990 | -81.24 | 16.71 | 569.10 | 0.14 | 2.93 | 1580 |
| 2024-09-20 22:21:32.986 | MS1 | 121.4656735259 | 31.1446375669 | 790 | 504990 | -81.76 | 12.91 | 506.02 | 0.15 | 2.52 | 1564 |
| 2024-09-20 22:21:33.627 | MS1 | 121.4656645259 | 31.1446208807 | 790 | 504990 | -82.34 | 13.08 | 525.52 | 0.04 | 2.27 | 1576 |
| 2024-09-20 22:21:34.302 | MS1 | 121.4656714766 | 31.1446185016 | 790 | 504990 | -92.66 | -1.41 | 59.83 | 0.08 | 1.49 | 1596 |
| 2024-09-20 22:21:35.712 | MS1 | 121.4656738871 | 31.1446330683 | 790 | 504990 | -86.15 | -0.26 | 58.08 | 0.19 | 1.25 | 1599 |
| 2024-09-20 22:21:36.579 | MS1 | 121.4656679875 | 31.1446223772 | 790 | 504990 | -89.08 | -0.85 | 67.80 | 0.09 | 1.28 | 1595 |
| 2024-09-20 22:21:37.353 | MS1 | 121.4656616886 | 31.1446284229 | 790 | 504990 | -88.08 | -1.07 | 50.26 | 0.04 | 1.16 | 1588 |
| 2024-09-20 22:21:38.321 | MS1 | 121.4656647263 | 31.1446220170 | 790 | 504990 | -92.34 | -0.98 | 36.56 | 0.10 | 1.08 | 1576 |
| 2024-09-20 22:21:39.621 | MS1 | 121.4656773390 | 31.1446212905 | 355 | 504990 | -83.98 | 12.64 | 185.21 | 0.12 | 1.30 | 1591 |
| 2024-09-20 22:21:40.149 | MS1 | 121.4656716456 | 31.1446192976 | 355 | 504990 | -75.28 | 14.61 | 590.28 | 0.09 | 2.51 | 1577 |
| 2024-09-20 22:21:41.109 | MS1 | 121.4656639722 | 31.1446306129 | 355 | 504990 | -78.37 | 16.07 | 333.97 | 0.00 | 2.44 | 1573 |
| 2024-09-20 22:21:42.804 | MS1 | 121.4656625121 | 31.1446230032 | 355 | 504990 | -76.53 | 16.85 | 520.02 | 0.11 | 2.44 | 1562 |

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
| 3219370 | 4 | 121.4676181113 | 31.1455561057 | 335 | 8 | 3 | 41.2 | TDD | 790 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3222050 | 3 | 121.4747651740 | 31.1515967319 | 129 | 7 | 1 | 16.6 | TDD | 115 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3229751 | 2 | 121.4757983230 | 31.1533258599 | 278 | 0 | 11 | 23.5 | TDD | 857 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3231599 | 1 | 121.4663967687 | 31.1505654112 | 33 | 3 | 11 | 17.2 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.634 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.655 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.776 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.776 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.482 | NREventA3 | measId:2;ServCellPCI:755;Se... |
| 2024-09-20 22:21:38.722 | NRHandoverAttempt | SourcePCI:755;SourceNR-ARFC... |
| 2024-09-20 22:21:38.771 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.784 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.925 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.925 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231599 | 1 | 5.9477 | 10.7585 | -116.1939 | 17.0138 | 114.7558 | 0.0044 | 0.0184 |
| 2024_09_20 22:00 | 3229751 | 2 | 6.0461 | 17.0781 | -114.4146 | 18.7146 | 105.7242 | 0.0068 | 0.0100 |
| 2024_09_20 22:00 | 3222050 | 3 | 19.5005 | 16.5258 | -114.1462 | 7.8090 | 111.0835 | 0.0095 | 0.0100 |
| 2024_09_20 22:00 | 3219370 | 4 | 17.5492 | 12.8440 | -114.3727 | 18.2675 | 96.2533 | 0.0173 | 0.1360 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412026_12063C92 | 504990 | 355 | -89.6 | 504990 | 790 | -94.0 | 504990 | 115 | -91.2 | 504990 | 857 |
| MR_1774412026_9AA2E8AA | 504990 | 355 | -88.9 | 504990 | 790 | -91.3 | 504990 | 115 | -91.3 | 504990 | 857 |
| MR_1774412026_3A18DCCA | 504990 | 790 | -91.6 | 504990 | 355 | -89.4 | 504990 | 115 | -91.2 | 504990 | 857 |
| MR_1774412026_414EE7F6 | 504990 | 790 | -93.4 | 504990 | 355 | -89.2 | 504990 | 115 | -89.0 | 504990 | 857 |
| MR_1774412026_E7E6F7B8 | 504990 | 355 | -89.3 | 504990 | 790 | -93.4 | 504990 | 115 | -90.6 | 504990 | 857 |
| MR_1774412026_B5D19C64 | 504990 | 790 | -93.1 | 504990 | 355 | -89.0 | 504990 | 115 | -89.9 | 504990 | 857 |
| MR_1774412026_77836519 | 504990 | 790 | -91.8 | 504990 | 355 | -88.2 | 504990 | 115 | -91.8 | 504990 | 857 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 317: `dfe02cee-859...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dfe02cee-859f-4f25-bef2-1eaddfbf93ab` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[317] topology](images/test_0317.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3214093_2 and 3250809_1
- `C2`: Decrease transmission power for 3250809_1
- `C3`: Increase A3 Offset threshold for 3250809_1
- `C4`: Add neighbor relationship between 3240113_3 and 3250809_1
- `C5`: Decrease A3 Offset threshold for 3250809_1
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240113_3
- `C8`: Press down the tilt angle  of 3250809_1 by 9 degrees
- `C9`: Lift the tilt angle of 3240113_3 by 2 degrees
- `C10`: Increase transmission power for 3250809_1
- `C11`: Adjust the azimuth of 3240113_3 by 38 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250809_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240113_3
- `C14`: Increase A3 Offset threshold for 3240113_3
- `C15`: Check test server and transmission issues
- `C16`: Press down the tilt angle of 3240113_3 by 2 degrees
- `C17`: Adjust the azimuth of 3250809_1 by 50 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250809_1
- `C19`: Lift the tilt angle  of 3250809_1 by 9 degrees
- `C20`: Increase transmission power for 3240113_3
- `C21`: Decrease A3 Offset threshold for 3240113_3
- `C22`: Decrease transmission power for 3240113_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.774 | MS1 | 121.4656702679 | 31.1446309788 | 531 | 504990 | -85.16 | 13.30 | 391.47 | 0.01 | 2.27 | 1569 |
| 2024-09-20 22:21:32.339 | MS1 | 121.4656629789 | 31.1446343804 | 531 | 504990 | -86.16 | 12.66 | 587.90 | 0.04 | 2.97 | 1573 |
| 2024-09-20 22:21:33.447 | MS1 | 121.4656706474 | 31.1446297391 | 531 | 504990 | -86.91 | 12.59 | 493.54 | 0.19 | 2.41 | 1561 |
| 2024-09-20 22:21:34.270 | MS1 | 121.4656580137 | 31.1446329187 | 531 | 504990 | -90.46 | 13.76 | 106.27 | 0.59 | 2.92 | 518 |
| 2024-09-20 22:21:35.232 | MS1 | 121.4656735096 | 31.1446244279 | 531 | 504990 | -86.69 | 14.67 | 78.25 | 0.70 | 2.17 | 510 |
| 2024-09-20 22:21:36.814 | MS1 | 121.4656652164 | 31.1446354670 | 531 | 504990 | -89.66 | 16.65 | 80.47 | 0.58 | 2.48 | 597 |
| 2024-09-20 22:21:37.152 | MS1 | 121.4656595387 | 31.1446349967 | 531 | 504990 | -91.92 | 10.88 | 85.27 | 0.54 | 2.08 | 600 |
| 2024-09-20 22:21:38.490 | MS1 | 121.4656740231 | 31.1446373293 | 531 | 504990 | -93.85 | 10.30 | 77.43 | 0.62 | 2.74 | 562 |
| 2024-09-20 22:21:39.225 | MS1 | 121.4656693221 | 31.1446358087 | 531 | 504990 | -91.88 | 8.92 | 67.00 | 0.51 | 2.35 | 679 |
| 2024-09-20 22:21:40.667 | MS1 | 121.4656623680 | 31.1446270307 | 531 | 504990 | -93.05 | 9.49 | 314.81 | 0.16 | 2.51 | 1588 |
| 2024-09-20 22:21:41.242 | MS1 | 121.4656606645 | 31.1446279356 | 531 | 504990 | -93.24 | 12.36 | 515.88 | 0.07 | 2.52 | 1572 |
| 2024-09-20 22:21:42.149 | MS1 | 121.4656736163 | 31.1446278345 | 531 | 504990 | -93.72 | 9.00 | 470.85 | 0.04 | 2.90 | 1572 |

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
| 3214093 | 2 | 121.4690956606 | 31.1546750367 | 72 | 8 | 6 | 41.0 | TDD | 378 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3240113 | 3 | 121.4701183609 | 31.1495821341 | 256 | 0 | 10 | 27.3 | TDD | 531 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3250809 | 1 | 121.4718108499 | 31.1449332364 | 106 | 4 | 3 | 49.7 | TDD | 817 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3253235 | 4 | 121.4719412433 | 31.1494223883 | 33 | 6 | 4 | 40.5 | TDD | 975 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.946 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.961 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.078 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.078 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.775 | NREventA3 | measId:2;ServCellPCI:253;Se... |
| 2024-09-20 22:21:38.015 | NRHandoverAttempt | SourcePCI:253;SourceNR-ARFC... |
| 2024-09-20 22:21:38.059 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.074 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.195 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.195 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250809 | 1 | 16.0393 | 5.7918 | -116.9640 | 8.8593 | 110.2540 | 0.0059 | 0.0171 |
| 2024_09_20 22:00 | 3214093 | 2 | 13.5163 | 14.7045 | -117.7977 | 9.0902 | 94.7384 | 0.0193 | 0.0139 |
| 2024_09_20 22:00 | 3240113 | 3 | 16.8432 | 11.8977 | -115.1210 | 15.2084 | 185.4256 | 0.0095 | 0.0105 |
| 2024_09_20 22:00 | 3253235 | 4 | 18.6772 | 10.8752 | -114.1567 | 9.0129 | 86.6215 | 0.0172 | 0.0189 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412453_ECE25F43 | 504990 | 531 | -87.6 | 504990 | 817 | -91.6 | 504990 | 378 | -93.7 | 504990 | 975 |
| MR_1774412453_4F072880 | 504990 | 531 | -88.2 | 504990 | 817 | -91.9 | 504990 | 378 | -94.8 | 504990 | 975 |
| MR_1774412453_148AB3BD | 504990 | 531 | -87.4 | 504990 | 817 | -90.4 | 504990 | 378 | -95.7 | 504990 | 975 |
| MR_1774412453_90F2AA2E | 504990 | 531 | -86.9 | 504990 | 817 | -91.6 | 504990 | 378 | -91.8 | 504990 | 975 |
| MR_1774412453_CBC9725F | 504990 | 531 | -88.0 | 504990 | 817 | -90.9 | 504990 | 378 | -95.7 | 504990 | 975 |
| MR_1774412453_E59C8925 | 504990 | 531 | -85.9 | 504990 | 817 | -90.4 | 504990 | 378 | -94.6 | 504990 | 975 |
| MR_1774412453_C5271A3B | 504990 | 531 | -85.5 | 504990 | 817 | -90.4 | 504990 | 378 | -92.3 | 504990 | 975 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 318: `5d036c3c-734...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5d036c3c-734a-49a1-a7ea-a9c0aac141cd` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[318] topology](images/test_0318.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263521_1
- `C2`: Increase A3 Offset threshold for 3263521_1
- `C3`: Check test server and transmission issues
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Add neighbor relationship between 3253093_2 and 3277986_4
- `C6`: Press down the tilt angle of 3263521_1 by 3 degrees
- `C7`: Increase A3 Offset threshold for 3277986_4
- `C8`: Adjust the azimuth of 3277986_4 by 50 degrees
- `C9`: Decrease transmission power for 3277986_4
- `C10`: Increase transmission power for 3263521_1
- `C11`: Press down the tilt angle  of 3277986_4 by 5 degrees
- `C12`: Lift the tilt angle of 3263521_1 by 3 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277986_4
- `C14`: Adjust the azimuth of 3263521_1 by 44 degrees
- `C15`: Lift the tilt angle  of 3277986_4 by 5 degrees
- `C16`: Decrease A3 Offset threshold for 3277986_4
- `C17`: Decrease transmission power for 3263521_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263521_1
- `C19`: Decrease A3 Offset threshold for 3263521_1
- `C20`: Add neighbor relationship between 3263521_1 and 3277986_4
- `C21`: Increase transmission power for 3277986_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277986_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.991 | MS1 | 121.4656646877 | 31.1446215438 | 472 | 504990 | -88.40 | 13.22 | 526.12 | 0.18 | 2.15 | 1599 |
| 2024-09-20 22:21:32.196 | MS1 | 121.4656695543 | 31.1446210966 | 472 | 504990 | -90.58 | 17.09 | 295.36 | 0.10 | 2.05 | 1589 |
| 2024-09-20 22:21:33.126 | MS1 | 121.4656656990 | 31.1446331723 | 472 | 504990 | -91.66 | 12.89 | 456.27 | 0.16 | 2.16 | 1560 |
| 2024-09-20 22:21:34.885 | MS1 | 121.4656774120 | 31.1446243816 | 472 | 504990 | -85.87 | 17.83 | 79.32 | 0.70 | 2.42 | 661 |
| 2024-09-20 22:21:35.512 | MS1 | 121.4656756947 | 31.1446305496 | 472 | 504990 | -86.61 | 15.52 | 78.86 | 0.62 | 2.13 | 646 |
| 2024-09-20 22:21:36.549 | MS1 | 121.4656749186 | 31.1446268339 | 472 | 504990 | -90.98 | 17.91 | 77.36 | 0.69 | 2.07 | 632 |
| 2024-09-20 22:21:37.532 | MS1 | 121.4656628758 | 31.1446358111 | 472 | 504990 | -90.71 | 10.51 | 88.37 | 0.51 | 2.43 | 532 |
| 2024-09-20 22:21:38.790 | MS1 | 121.4656715926 | 31.1446198567 | 472 | 504990 | -90.04 | 10.11 | 62.14 | 0.69 | 2.92 | 512 |
| 2024-09-20 22:21:39.244 | MS1 | 121.4656761086 | 31.1446185556 | 472 | 504990 | -91.52 | 8.34 | 64.54 | 0.64 | 2.88 | 673 |
| 2024-09-20 22:21:40.768 | MS1 | 121.4656641077 | 31.1446231126 | 472 | 504990 | -90.99 | 7.09 | 385.81 | 0.12 | 2.58 | 1567 |
| 2024-09-20 22:21:41.898 | MS1 | 121.4656597504 | 31.1446294594 | 472 | 504990 | -93.19 | 12.22 | 335.47 | 0.09 | 2.52 | 1575 |
| 2024-09-20 22:21:42.281 | MS1 | 121.4656728277 | 31.1446259941 | 472 | 504990 | -89.39 | 11.43 | 593.35 | 0.18 | 2.97 | 1600 |

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
| 3239659 | 3 | 121.4713015376 | 31.1448956983 | 11 | 10 | 8 | 28.9 | TDD | 459 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3253093 | 2 | 121.4652118131 | 31.1519684813 | 106 | 12 | 2 | 36.6 | TDD | 9 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3263521 | 1 | 121.4738694909 | 31.1472674998 | 205 | 2 | 9 | 16.1 | TDD | 472 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3277986 | 4 | 121.4681438852 | 31.1550573585 | 118 | 3 | 12 | 31.3 | TDD | 860 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.128 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.231 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.231 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.959 | NREventA3 | measId:2;ServCellPCI:162;Se... |
| 2024-09-20 22:21:38.199 | NRHandoverAttempt | SourcePCI:162;SourceNR-ARFC... |
| 2024-09-20 22:21:38.234 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.244 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.370 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.370 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263521 | 1 | 9.5957 | 7.3347 | -114.2289 | 17.1380 | 139.2610 | 0.0080 | 0.0025 |
| 2024_09_20 22:00 | 3253093 | 2 | 17.0578 | 7.7328 | -115.4991 | 12.7913 | 124.7051 | 0.0027 | 0.0147 |
| 2024_09_20 22:00 | 3239659 | 3 | 7.0051 | 9.6655 | -115.0119 | 18.5717 | 101.7720 | 0.0156 | 0.0110 |
| 2024_09_20 22:00 | 3277986 | 4 | 15.4286 | 12.6206 | -115.7220 | 19.5587 | 182.8342 | 0.0122 | 0.0031 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412902_FCE17AE3 | 504990 | 472 | -84.7 | 504990 | 860 | -92.6 | 504990 | 9 | -92.9 | 504990 | 459 |
| MR_1774412902_B167D2CA | 504990 | 472 | -86.9 | 504990 | 860 | -91.8 | 504990 | 9 | -94.2 | 504990 | 459 |
| MR_1774412902_4F1DD885 | 504990 | 472 | -84.0 | 504990 | 860 | -92.6 | 504990 | 9 | -96.0 | 504990 | 459 |
| MR_1774412902_41753560 | 504990 | 472 | -85.2 | 504990 | 860 | -93.5 | 504990 | 9 | -92.9 | 504990 | 459 |
| MR_1774412902_8CB8D3BD | 504990 | 472 | -85.9 | 504990 | 860 | -93.5 | 504990 | 9 | -93.1 | 504990 | 459 |
| MR_1774412902_C4474CAD | 504990 | 472 | -87.8 | 504990 | 860 | -91.7 | 504990 | 9 | -92.6 | 504990 | 459 |
| MR_1774412902_78982C76 | 504990 | 472 | -87.3 | 504990 | 860 | -94.9 | 504990 | 9 | -96.3 | 504990 | 459 |
| MR_1774412902_04E60A22 | 504990 | 472 | -84.9 | 504990 | 860 | -94.7 | 504990 | 9 | -94.0 | 504990 | 459 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 319: `b5d68670-276...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b5d68670-276e-40cb-9e1a-0f41a49c814e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[319] topology](images/test_0319.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3235542_4 by 50 degrees
- `C2`: Decrease transmission power for 3236965_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235542_4
- `C4`: Increase A3 Offset threshold for 3235542_4
- `C5`: Increase transmission power for 3236965_1
- `C6`: Check test server and transmission issues
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Add neighbor relationship between 3236965_1 and 3235542_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235542_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236965_1
- `C11`: Decrease transmission power for 3235542_4
- `C12`: Press down the tilt angle of 3236965_1 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3235542_4
- `C14`: Increase A3 Offset threshold for 3236965_1
- `C15`: Lift the tilt angle of 3236965_1 by 10 degrees
- `C16`: Adjust the azimuth of 3236965_1 by 50 degrees
- `C17`: Decrease A3 Offset threshold for 3236965_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236965_1
- `C19`: Add neighbor relationship between 3264848_2 and 3235542_4
- `C20`: Lift the tilt angle  of 3235542_4 by 10 degrees
- `C21`: Increase transmission power for 3235542_4
- `C22`: Press down the tilt angle  of 3235542_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.856 | MS1 | 121.4656773826 | 31.1446192422 | 848 | 504990 | -89.29 | 16.82 | 387.08 | 0.09 | 2.10 | 1566 |
| 2024-09-20 22:21:32.183 | MS1 | 121.4656714892 | 31.1446200723 | 848 | 504990 | -90.39 | 15.73 | 432.08 | 0.05 | 2.03 | 1562 |
| 2024-09-20 22:21:33.156 | MS1 | 121.4656600951 | 31.1446268937 | 848 | 504990 | -86.43 | 12.30 | 313.70 | 0.07 | 2.75 | 1586 |
| 2024-09-20 22:21:34.186 | MS1 | 121.4656598188 | 31.1446262847 | 848 | 504990 | -88.13 | 14.47 | 67.31 | 0.01 | 2.01 | 461 |
| 2024-09-20 22:21:35.165 | MS1 | 121.4656742136 | 31.1446356525 | 848 | 504990 | -88.68 | 12.13 | 83.47 | 0.11 | 2.55 | 329 |
| 2024-09-20 22:21:36.627 | MS1 | 121.4656713463 | 31.1446264506 | 848 | 504990 | -89.91 | 15.12 | 86.74 | 0.16 | 2.45 | 372 |
| 2024-09-20 22:21:37.668 | MS1 | 121.4656757630 | 31.1446328431 | 848 | 504990 | -89.89 | 8.23 | 103.98 | 0.06 | 2.21 | 433 |
| 2024-09-20 22:21:38.497 | MS1 | 121.4656649950 | 31.1446207784 | 848 | 504990 | -91.91 | 7.56 | 50.16 | 0.06 | 2.37 | 482 |
| 2024-09-20 22:21:39.850 | MS1 | 121.4656679677 | 31.1446256673 | 848 | 504990 | -91.82 | 10.14 | 57.60 | 0.10 | 2.70 | 359 |
| 2024-09-20 22:21:40.343 | MS1 | 121.4656594797 | 31.1446359409 | 848 | 504990 | -89.54 | 12.11 | 310.38 | 0.17 | 2.62 | 1562 |
| 2024-09-20 22:21:41.799 | MS1 | 121.4656652087 | 31.1446340898 | 848 | 504990 | -89.51 | 7.94 | 475.95 | 0.07 | 2.10 | 1585 |
| 2024-09-20 22:21:42.155 | MS1 | 121.4656694992 | 31.1446329478 | 848 | 504990 | -93.76 | 8.55 | 329.56 | 0.04 | 2.71 | 1578 |

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
| 3231107 | 3 | 121.4693152186 | 31.1477644254 | 65 | 12 | 8 | 18.4 | TDD | 104 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3235542 | 4 | 121.4690534533 | 31.1467466429 | 125 | 5 | 5 | 44.3 | TDD | 279 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3236965 | 1 | 121.4751532656 | 31.1527574052 | 81 | 12 | 3 | 33.8 | TDD | 848 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3264848 | 2 | 121.4685260292 | 31.1516523649 | 275 | 0 | 2 | 40.2 | TDD | 721 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.266 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.289 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.411 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.411 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.106 | NREventA3 | measId:2;ServCellPCI:418;Se... |
| 2024-09-20 22:21:38.346 | NRHandoverAttempt | SourcePCI:418;SourceNR-ARFC... |
| 2024-09-20 22:21:38.378 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.391 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.498 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.498 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236965 | 1 | 19.5185 | 11.4917 | -117.1609 | 11.3732 | 192.0434 | 0.0130 | 0.0140 |
| 2024_09_20 22:00 | 3264848 | 2 | 12.4714 | 11.3881 | -116.7430 | 10.8055 | 199.5034 | 0.0179 | 0.0163 |
| 2024_09_20 22:00 | 3231107 | 3 | 7.1264 | 6.3758 | -115.2233 | 9.7483 | 148.6429 | 0.0055 | 0.0175 |
| 2024_09_20 22:00 | 3235542 | 4 | 6.2589 | 15.5110 | -116.7999 | 10.3661 | 185.3454 | 0.0104 | 0.0003 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414231_9E2D0FCA | 504990 | 848 | -87.6 | 504990 | 279 | -92.7 | 504990 | 721 | -97.0 | 504990 | 104 |
| MR_1774414231_E228DD92 | 504990 | 848 | -90.1 | 504990 | 279 | -92.7 | 504990 | 721 | -97.2 | 504990 | 104 |
| MR_1774414231_B0D7B621 | 504990 | 848 | -88.4 | 504990 | 279 | -89.9 | 504990 | 721 | -95.4 | 504990 | 104 |
| MR_1774414231_5509B48D | 504990 | 848 | -89.0 | 504990 | 279 | -89.8 | 504990 | 721 | -99.0 | 504990 | 104 |
| MR_1774414231_1292CF38 | 504990 | 848 | -86.3 | 504990 | 279 | -91.0 | 504990 | 721 | -98.1 | 504990 | 104 |
| MR_1774414231_1E30507C | 504990 | 848 | -89.0 | 504990 | 279 | -88.9 | 504990 | 721 | -96.7 | 504990 | 104 |

> *... 2개 열 생략 (전체 14열)*

---
