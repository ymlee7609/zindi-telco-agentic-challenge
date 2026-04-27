# Track A 문제 분석 — test[430]~test[439]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[430] ~ test[439] (10개)

## 목차

1. [문제 430: `ba03de5c-387...`](#430) — single-answer
2. [문제 431: `20ceba42-006...`](#431) — single-answer
3. [문제 432: `0c778413-a8d...`](#432) — single-answer
4. [문제 433: `61d117ca-f7d...`](#433) — multiple-answer
5. [문제 434: `cd7425c1-f24...`](#434) — single-answer
6. [문제 435: `13332a50-9e8...`](#435) — single-answer
7. [문제 436: `83cee0ce-2bb...`](#436) — multiple-answer
8. [문제 437: `ad0b061e-912...`](#437) — single-answer
9. [문제 438: `e3217eba-56b...`](#438) — multiple-answer
10. [문제 439: `8a5359c1-ae6...`](#439) — multiple-answer

---

### 문제 430: `ba03de5c-387...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ba03de5c-3874-4be5-a820-91ff6e2c66dc` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[430] topology](images/test_0430.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263865_2
- `C2`: Decrease transmission power for 3263865_2
- `C3`: Check test server and transmission issues
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227620_4
- `C5`: Lift the tilt angle  of 3263865_2 by 10 degrees
- `C6`: Press down the tilt angle of 3227620_4 by 6 degrees
- `C7`: Decrease A3 Offset threshold for 3263865_2
- `C8`: Increase transmission power for 3227620_4
- `C9`: Press down the tilt angle  of 3263865_2 by 10 degrees
- `C10`: Decrease transmission power for 3227620_4
- `C11`: Adjust the azimuth of 3263865_2 by 50 degrees
- `C12`: Decrease A3 Offset threshold for 3227620_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263865_2
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase A3 Offset threshold for 3263865_2
- `C16`: Increase A3 Offset threshold for 3227620_4
- `C17`: Lift the tilt angle of 3227620_4 by 6 degrees
- `C18`: Add neighbor relationship between 3227620_4 and 3263865_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227620_4
- `C20`: Adjust the azimuth of 3227620_4 by 50 degrees
- `C21`: Add neighbor relationship between 3247710_1 and 3263865_2
- `C22`: Increase transmission power for 3263865_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.427 | MS1 | 121.4656614396 | 31.1446193234 | 478 | 504990 | -81.75 | 12.23 | 457.28 | 0.11 | 2.23 | 1578 |
| 2024-09-20 22:21:32.654 | MS1 | 121.4656686892 | 31.1446225031 | 478 | 504990 | -77.12 | 17.70 | 512.40 | 0.06 | 2.76 | 1600 |
| 2024-09-20 22:21:33.195 | MS1 | 121.4656757568 | 31.1446228518 | 478 | 504990 | -80.05 | 12.93 | 444.90 | 0.01 | 2.59 | 1583 |
| 2024-09-20 22:21:34.362 | MS1 | 121.4656634096 | 31.1446352248 | 478 | 504990 | -84.82 | -0.70 | 72.29 | 0.11 | 1.26 | 1574 |
| 2024-09-20 22:21:35.159 | MS1 | 121.4656585764 | 31.1446311054 | 478 | 504990 | -86.27 | -0.45 | 68.73 | 0.06 | 1.03 | 1579 |
| 2024-09-20 22:21:36.729 | MS1 | 121.4656747658 | 31.1446246283 | 478 | 504990 | -85.09 | -2.88 | 27.45 | 0.04 | 1.13 | 1600 |
| 2024-09-20 22:21:37.899 | MS1 | 121.4656593780 | 31.1446281665 | 478 | 504990 | -83.83 | -2.78 | 59.26 | 0.16 | 1.37 | 1581 |
| 2024-09-20 22:21:38.521 | MS1 | 121.4656732149 | 31.1446182353 | 478 | 504990 | -89.36 | -0.14 | 63.68 | 0.13 | 1.32 | 1593 |
| 2024-09-20 22:21:39.256 | MS1 | 121.4656588979 | 31.1446266515 | 76 | 504990 | -80.37 | 13.67 | 269.82 | 0.13 | 1.04 | 1592 |
| 2024-09-20 22:21:40.574 | MS1 | 121.4656591849 | 31.1446371497 | 76 | 504990 | -81.23 | 13.97 | 490.36 | 0.08 | 2.02 | 1594 |
| 2024-09-20 22:21:41.318 | MS1 | 121.4656686750 | 31.1446270175 | 76 | 504990 | -82.94 | 12.74 | 472.70 | 0.13 | 2.10 | 1562 |
| 2024-09-20 22:21:42.234 | MS1 | 121.4656597017 | 31.1446288613 | 76 | 504990 | -77.16 | 15.46 | 337.58 | 0.19 | 2.61 | 1590 |

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
| 3227620 | 4 | 121.4685520829 | 31.1532042081 | 119 | 3 | 8 | 48.7 | TDD | 478 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3228246 | 3 | 121.4656402465 | 31.1553147389 | 207 | 7 | 5 | 44.5 | TDD | 261 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3247710 | 1 | 121.4726460968 | 31.1471750895 | 24 | 10 | 0 | 20.0 | TDD | 304 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3263865 | 2 | 121.4686947437 | 31.1556085340 | 334 | 15 | 10 | 24.3 | TDD | 76 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.930 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.950 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.088 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.088 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.755 | NREventA3 | measId:2;ServCellPCI:160;Se... |
| 2024-09-20 22:21:37.995 | NRHandoverAttempt | SourcePCI:160;SourceNR-ARFC... |
| 2024-09-20 22:21:38.042 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.055 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.157 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.157 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247710 | 1 | 17.9633 | 12.6426 | -115.6317 | 10.6118 | 165.1651 | 0.0040 | 0.0176 |
| 2024_09_20 22:00 | 3263865 | 2 | 18.2039 | 7.7703 | -117.5846 | 15.5675 | 127.4478 | 0.0189 | 0.0120 |
| 2024_09_20 22:00 | 3228246 | 3 | 5.1939 | 5.3070 | -117.7739 | 11.3462 | 146.6903 | 0.0026 | 0.0093 |
| 2024_09_20 22:00 | 3227620 | 4 | 12.2962 | 8.6683 | -117.1509 | 7.9272 | 155.8090 | 0.0115 | 0.1375 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414803_618578A6 | 504990 | 478 | -86.5 | 504990 | 76 | -78.3 | 504990 | 304 | -83.8 | 504990 | 261 |
| MR_1774414803_9CD6F60A | 504990 | 76 | -78.7 | 504990 | 478 | -83.9 | 504990 | 304 | -82.2 | 504990 | 261 |
| MR_1774414803_C95BD6E9 | 504990 | 478 | -84.3 | 504990 | 76 | -78.9 | 504990 | 304 | -83.2 | 504990 | 261 |
| MR_1774414803_DB09C379 | 504990 | 478 | -84.6 | 504990 | 76 | -79.5 | 504990 | 304 | -83.7 | 504990 | 261 |
| MR_1774414803_2E979587 | 504990 | 76 | -79.1 | 504990 | 478 | -85.0 | 504990 | 304 | -83.1 | 504990 | 261 |
| MR_1774414803_25524AF2 | 504990 | 478 | -85.3 | 504990 | 76 | -80.9 | 504990 | 304 | -84.4 | 504990 | 261 |
| MR_1774414803_86D338D3 | 504990 | 76 | -78.9 | 504990 | 478 | -84.1 | 504990 | 304 | -83.2 | 504990 | 261 |
| MR_1774414803_C042F9D8 | 504990 | 76 | -80.3 | 504990 | 478 | -83.5 | 504990 | 304 | -84.3 | 504990 | 261 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 431: `20ceba42-006...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `20ceba42-006a-4a62-9738-27fb476facab` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[431] topology](images/test_0431.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248443_2
- `C2`: Decrease A3 Offset threshold for 3249787_4
- `C3`: Check test server and transmission issues
- `C4`: Increase A3 Offset threshold for 3249787_4
- `C5`: Decrease A3 Offset threshold for 3248443_2
- `C6`: Adjust the azimuth of 3248443_2 by 50 degrees
- `C7`: Adjust the azimuth of 3249787_4 by 50 degrees
- `C8`: Lift the tilt angle  of 3248443_2 by 10 degrees
- `C9`: Increase transmission power for 3249787_4
- `C10`: Increase transmission power for 3248443_2
- `C11`: Add neighbor relationship between 3221173_1 and 3248443_2
- `C12`: Increase A3 Offset threshold for 3248443_2
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248443_2
- `C15`: Decrease transmission power for 3249787_4
- `C16`: Lift the tilt angle of 3249787_4 by 10 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249787_4
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249787_4
- `C19`: Decrease transmission power for 3248443_2
- `C20`: Press down the tilt angle of 3249787_4 by 10 degrees
- `C21`: Press down the tilt angle  of 3248443_2 by 10 degrees
- `C22`: Add neighbor relationship between 3249787_4 and 3248443_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.942 | MS1 | 121.4656776668 | 31.1446232967 | 550 | 504990 | -76.66 | 13.21 | 366.86 | 0.01 | 2.84 | 1589 |
| 2024-09-20 22:21:32.447 | MS1 | 121.4656779081 | 31.1446265928 | 550 | 504990 | -84.95 | 15.80 | 335.86 | 0.13 | 2.24 | 1596 |
| 2024-09-20 22:21:33.812 | MS1 | 121.4656716590 | 31.1446234169 | 550 | 504990 | -82.55 | 12.86 | 449.28 | 0.06 | 2.06 | 1585 |
| 2024-09-20 22:21:34.983 | MS1 | 121.4656762469 | 31.1446354905 | 550 | 504990 | -86.55 | -1.73 | 31.59 | 0.05 | 1.28 | 1588 |
| 2024-09-20 22:21:35.591 | MS1 | 121.4656765929 | 31.1446287435 | 550 | 504990 | -92.72 | -1.65 | 44.80 | 0.04 | 1.36 | 1576 |
| 2024-09-20 22:21:36.464 | MS1 | 121.4656778294 | 31.1446187688 | 550 | 504990 | -92.70 | -3.38 | 47.76 | 0.12 | 1.12 | 1585 |
| 2024-09-20 22:21:37.778 | MS1 | 121.4656741101 | 31.1446321983 | 550 | 504990 | -83.78 | -1.37 | 51.07 | 0.05 | 1.24 | 1564 |
| 2024-09-20 22:21:38.147 | MS1 | 121.4656747450 | 31.1446305892 | 550 | 504990 | -87.66 | -3.16 | 42.34 | 0.04 | 1.11 | 1560 |
| 2024-09-20 22:21:39.189 | MS1 | 121.4656743787 | 31.1446279863 | 913 | 504990 | -79.89 | 13.35 | 268.26 | 0.07 | 1.08 | 1591 |
| 2024-09-20 22:21:40.329 | MS1 | 121.4656777775 | 31.1446252837 | 913 | 504990 | -84.62 | 17.93 | 398.54 | 0.10 | 2.57 | 1574 |
| 2024-09-20 22:21:41.172 | MS1 | 121.4656778462 | 31.1446202013 | 913 | 504990 | -80.65 | 12.64 | 322.84 | 0.06 | 2.25 | 1569 |
| 2024-09-20 22:21:42.909 | MS1 | 121.4656711725 | 31.1446210692 | 913 | 504990 | -81.74 | 14.48 | 373.40 | 0.08 | 2.97 | 1574 |

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
| 3221173 | 1 | 121.4700178719 | 31.1442834616 | 326 | 12 | 8 | 31.8 | TDD | 8 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3240603 | 3 | 121.4700055137 | 31.1441680926 | 285 | 12 | 4 | 37.3 | TDD | 450 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3248443 | 2 | 121.4750422480 | 31.1535450968 | 306 | 9 | 10 | 26.1 | TDD | 913 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3249787 | 4 | 121.4750086955 | 31.1547828763 | 4 | 9 | 5 | 46.4 | TDD | 550 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.299 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.320 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.447 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.447 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.129 | NREventA3 | measId:2;ServCellPCI:460;Se... |
| 2024-09-20 22:21:38.369 | NRHandoverAttempt | SourcePCI:460;SourceNR-ARFC... |
| 2024-09-20 22:21:38.406 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.419 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.537 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.537 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221173 | 1 | 18.7160 | 15.6234 | -117.4534 | 6.3285 | 152.2171 | 0.0116 | 0.0140 |
| 2024_09_20 22:00 | 3248443 | 2 | 17.2347 | 12.3535 | -116.3721 | 13.6604 | 135.6544 | 0.0138 | 0.0155 |
| 2024_09_20 22:00 | 3240603 | 3 | 6.9049 | 19.2032 | -117.6082 | 7.5022 | 145.5420 | 0.0059 | 0.0101 |
| 2024_09_20 22:00 | 3249787 | 4 | 16.0117 | 13.0588 | -116.4409 | 18.9646 | 129.7236 | 0.0138 | 0.1215 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413835_77E4F9D8 | 504990 | 913 | -80.1 | 504990 | 550 | -86.2 | 504990 | 8 | -80.6 | 504990 | 450 |
| MR_1774413835_99A167F9 | 504990 | 913 | -79.1 | 504990 | 550 | -85.2 | 504990 | 8 | -80.3 | 504990 | 450 |
| MR_1774413835_7944B6CD | 504990 | 550 | -88.0 | 504990 | 913 | -80.9 | 504990 | 8 | -79.3 | 504990 | 450 |
| MR_1774413835_6CCEEFF8 | 504990 | 550 | -85.9 | 504990 | 913 | -79.3 | 504990 | 8 | -82.3 | 504990 | 450 |
| MR_1774413835_71F9BFF2 | 504990 | 550 | -85.1 | 504990 | 913 | -82.0 | 504990 | 8 | -81.6 | 504990 | 450 |
| MR_1774413835_95F31AE4 | 504990 | 550 | -86.4 | 504990 | 913 | -78.7 | 504990 | 8 | -82.5 | 504990 | 450 |
| MR_1774413835_1F67A512 | 504990 | 913 | -81.8 | 504990 | 550 | -85.1 | 504990 | 8 | -80.0 | 504990 | 450 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 432: `0c778413-a8d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0c778413-a8d8-44aa-a7ec-d70d1c85edfe` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[432] topology](images/test_0432.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3279184_3 and 3253044_1
- `C2`: Lift the tilt angle of 3239479_4 by 4 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase transmission power for 3239479_4
- `C5`: Press down the tilt angle  of 3253044_1 by 4 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239479_4
- `C7`: Decrease transmission power for 3239479_4
- `C8`: Increase transmission power for 3253044_1
- `C9`: Decrease transmission power for 3253044_1
- `C10`: Adjust the azimuth of 3239479_4 by 50 degrees
- `C11`: Increase A3 Offset threshold for 3253044_1
- `C12`: Check test server and transmission issues
- `C13`: Decrease A3 Offset threshold for 3239479_4
- `C14`: Decrease A3 Offset threshold for 3253044_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253044_1
- `C16`: Lift the tilt angle  of 3253044_1 by 4 degrees
- `C17`: Adjust the azimuth of 3253044_1 by 23 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253044_1
- `C19`: Press down the tilt angle of 3239479_4 by 4 degrees
- `C20`: Add neighbor relationship between 3239479_4 and 3253044_1
- `C21`: Increase A3 Offset threshold for 3239479_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239479_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.988 | MS1 | 121.4656765609 | 31.1446225497 | 679 | 504990 | -84.23 | 14.92 | 471.63 | 0.04 | 2.98 | 1595 |
| 2024-09-20 22:21:32.447 | MS1 | 121.4656618513 | 31.1446329968 | 679 | 504990 | -80.92 | 13.29 | 491.21 | 0.13 | 2.27 | 1560 |
| 2024-09-20 22:21:33.149 | MS1 | 121.4656754098 | 31.1446334114 | 679 | 504990 | -76.42 | 16.96 | 537.46 | 0.12 | 2.44 | 1575 |
| 2024-09-20 22:21:34.617 | MS1 | 121.4656679179 | 31.1446316149 | 679 | 504990 | -87.64 | -3.63 | 34.67 | 0.20 | 1.14 | 1572 |
| 2024-09-20 22:21:35.902 | MS1 | 121.4656768712 | 31.1446219235 | 679 | 504990 | -94.98 | -3.12 | 75.75 | 0.05 | 1.44 | 1590 |
| 2024-09-20 22:21:36.504 | MS1 | 121.4656646254 | 31.1446286692 | 679 | 504990 | -86.59 | -0.86 | 44.03 | 0.10 | 1.49 | 1575 |
| 2024-09-20 22:21:37.560 | MS1 | 121.4656710176 | 31.1446315138 | 679 | 504990 | -87.62 | -2.78 | 46.96 | 0.07 | 1.43 | 1599 |
| 2024-09-20 22:21:38.187 | MS1 | 121.4656711171 | 31.1446249070 | 679 | 504990 | -84.84 | 13.58 | 476.43 | 0.00 | 1.19 | 1591 |
| 2024-09-20 22:21:39.636 | MS1 | 121.4656691358 | 31.1446186938 | 679 | 504990 | -81.67 | 17.46 | 362.19 | 0.17 | 1.04 | 1574 |
| 2024-09-20 22:21:40.558 | MS1 | 121.4656656133 | 31.1446289025 | 679 | 504990 | -82.42 | 14.92 | 388.88 | 0.14 | 2.72 | 1595 |
| 2024-09-20 22:21:41.803 | MS1 | 121.4656642630 | 31.1446193982 | 679 | 504990 | -84.25 | 15.08 | 378.23 | 0.20 | 2.56 | 1592 |
| 2024-09-20 22:21:42.546 | MS1 | 121.4656647334 | 31.1446300095 | 679 | 504990 | -77.71 | 12.21 | 553.59 | 0.06 | 2.36 | 1574 |

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
| 3239479 | 4 | 121.4730529433 | 31.1458179739 | 318 | 0 | 9 | 44.1 | TDD | 679 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3253044 | 1 | 121.4745085836 | 31.1486844484 | 219 | 3 | 0 | 24.3 | TDD | 116 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3261472 | 2 | 121.4739578077 | 31.1532469846 | 332 | 12 | 10 | 15.2 | TDD | 242 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3279184 | 3 | 121.4704132878 | 31.1508214391 | 211 | 12 | 8 | 15.9 | TDD | 628 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.275 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.375 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.375 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.112 | NREventA3 | measId:2;ServCellPCI:26;Ser... |
| 2024-09-20 22:21:36.112 | NREventA3 | measId:2;ServCellPCI:26;Ser... |
| 2024-09-20 22:21:37.112 | NREventA3 | measId:2;ServCellPCI:26;Ser... |
| 2024-09-20 22:21:39.612 | NRRRCReestablishAttempt | PCI:26 |
| 2024-09-20 22:21:39.623 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.638 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.759 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.759 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253044 | 1 | 7.5272 | 14.3951 | -117.0265 | 10.5163 | 97.2518 | 0.0055 | 0.0047 |
| 2024_09_20 22:00 | 3261472 | 2 | 5.8340 | 16.0208 | -117.8489 | 11.5697 | 179.9226 | 0.0065 | 0.0017 |
| 2024_09_20 22:00 | 3279184 | 3 | 7.0660 | 19.9393 | -117.6767 | 19.1734 | 82.5634 | 0.0193 | 0.0012 |
| 2024_09_20 22:00 | 3239479 | 4 | 19.4915 | 19.1668 | -115.1392 | 11.5620 | 140.5056 | 0.0089 | 0.1171 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415912_20E57544 | 504990 | 679 | -87.5 | 504990 | 116 | -81.7 | 504990 | 628 | -89.7 | 504990 | 242 |
| MR_1774415912_9A1381C7 | 504990 | 116 | -83.4 | 504990 | 679 | -89.2 | 504990 | 628 | -89.7 | 504990 | 242 |
| MR_1774415912_168BEA84 | 504990 | 679 | -88.9 | 504990 | 116 | -80.9 | 504990 | 628 | -91.3 | 504990 | 242 |
| MR_1774415912_D4795A9C | 504990 | 116 | -82.1 | 504990 | 679 | -87.0 | 504990 | 628 | -91.4 | 504990 | 242 |
| MR_1774415912_ABA8C59B | 504990 | 116 | -82.0 | 504990 | 679 | -87.3 | 504990 | 628 | -89.5 | 504990 | 242 |
| MR_1774415912_CE626599 | 504990 | 116 | -82.6 | 504990 | 679 | -86.4 | 504990 | 628 | -91.8 | 504990 | 242 |
| MR_1774415912_5C413C8C | 504990 | 679 | -87.7 | 504990 | 116 | -84.3 | 504990 | 628 | -92.7 | 504990 | 242 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 433: `61d117ca-f7d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `61d117ca-f7d6-4bb4-941a-99d9394012dd` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[433] topology](images/test_0433.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230401_2
- `C2`: Add neighbor relationship between 3278841_3 and 3230401_2
- `C3`: Add neighbor relationship between 3263946_5 and 3230401_2
- `C4`: Increase transmission power for 3263946_5
- `C5`: Lift the tilt angle of 3263946_5 by 1 degrees
- `C6`: Adjust the azimuth of 3230401_2 by 8 degrees
- `C7`: Press down the tilt angle of 3263946_5 by 1 degrees
- `C8`: Adjust the azimuth of 3263946_5 by 5 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263946_5
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263946_5
- `C11`: Increase A3 Offset threshold for 3230401_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Lift the tilt angle  of 3230401_2 by 4 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230401_2
- `C15`: Decrease A3 Offset threshold for 3230401_2
- `C16`: Decrease transmission power for 3263946_5
- `C17`: Decrease A3 Offset threshold for 3263946_5
- `C18`: Increase transmission power for 3230401_2
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle  of 3230401_2 by 4 degrees
- `C21`: Increase A3 Offset threshold for 3263946_5
- `C22`: Decrease transmission power for 3230401_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.553 | MS1 | 121.4656630202 | 31.1446285766 | 923 | 504990 | -81.46 | 13.11 | 449.05 | 0.02 | 2.71 | 1600 |
| 2024-09-20 22:21:32.478 | MS1 | 121.4656701234 | 31.1446317891 | 923 | 504990 | -76.54 | 13.90 | 543.12 | 0.10 | 2.53 | 1588 |
| 2024-09-20 22:21:33.964 | MS1 | 121.4656642796 | 31.1446357023 | 923 | 504990 | -80.98 | 12.81 | 502.06 | 0.03 | 2.94 | 1599 |
| 2024-09-20 22:21:34.705 | MS1 | 121.4656690105 | 31.1446333150 | 290 | 504990 | -83.46 | 2.52 | 42.70 | 0.12 | 1.31 | 1591 |
| 2024-09-20 22:21:35.772 | MS1 | 121.4656688113 | 31.1446292940 | 290 | 504990 | -84.20 | 1.12 | 70.30 | 0.03 | 1.36 | 1594 |
| 2024-09-20 22:21:36.411 | MS1 | 121.4656632260 | 31.1446307507 | 923 | 504990 | -89.08 | 4.11 | 57.60 | 0.15 | 1.41 | 1587 |
| 2024-09-20 22:21:37.755 | MS1 | 121.4656690502 | 31.1446278843 | 923 | 504990 | -82.04 | 2.47 | 32.20 | 0.09 | 1.20 | 1592 |
| 2024-09-20 22:21:38.637 | MS1 | 121.4656705787 | 31.1446184076 | 290 | 504990 | -85.33 | 4.18 | 66.09 | 0.03 | 1.21 | 1597 |
| 2024-09-20 22:21:39.126 | MS1 | 121.4656608163 | 31.1446299031 | 290 | 504990 | -89.69 | 4.54 | 37.02 | 0.17 | 1.23 | 1600 |
| 2024-09-20 22:21:40.683 | MS1 | 121.4656765910 | 31.1446219845 | 290 | 504990 | -76.26 | 14.02 | 405.76 | 0.05 | 2.22 | 1571 |
| 2024-09-20 22:21:41.625 | MS1 | 121.4656681910 | 31.1446351477 | 290 | 504990 | -77.57 | 15.86 | 527.61 | 0.02 | 2.12 | 1597 |
| 2024-09-20 22:21:42.831 | MS1 | 121.4656683228 | 31.1446346800 | 290 | 504990 | -81.95 | 14.79 | 493.39 | 0.13 | 2.37 | 1575 |

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
| 3230401 | 2 | 121.4752225256 | 31.1466675208 | 248 | 2 | 3 | 32.5 | TDD | 260 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3231645 | 1 | 121.4708422505 | 31.1455306023 | 313 | 2 | 1 | 30.8 | TDD | 290 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3255170 | 4 | 121.4676103944 | 31.1477908984 | 177 | 3 | 6 | 44.2 | TDD | 147 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3263946 | 5 | 121.4745809545 | 31.1479566161 | 241 | 0 | 7 | 18.6 | TDD | 923 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3278841 | 3 | 121.4673730936 | 31.1492765594 | 335 | 15 | 3 | 42.5 | TDD | 935 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.619 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.639 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.746 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.746 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.473 | NREventA3 | measId:2;ServCellPCI:155;Se... |
| 2024-09-20 22:21:34.713 | NRHandoverAttempt | SourcePCI:155;SourceNR-ARFC... |
| 2024-09-20 22:21:34.758 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.773 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.891 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.891 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.473 | NREventA3 | measId:2;ServCellPCI:608;Se... |
| 2024-09-20 22:21:36.713 | NRHandoverAttempt | SourcePCI:608;SourceNR-ARFC... |
| 2024-09-20 22:21:36.755 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.770 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.917 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.917 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.473 | NREventA3 | measId:2;ServCellPCI:155;Se... |
| 2024-09-20 22:21:38.713 | NRHandoverAttempt | SourcePCI:155;SourceNR-ARFC... |
| 2024-09-20 22:21:38.744 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.759 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.864 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.864 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231645 | 1 | 13.2948 | 13.6738 | -115.4422 | 16.4619 | 128.2987 | 0.0028 | 0.0161 |
| 2024_09_20 22:00 | 3230401 | 2 | 15.9440 | 5.1217 | -116.7015 | 8.8745 | 156.8943 | 0.0139 | 0.0185 |
| 2024_09_20 22:00 | 3278841 | 3 | 17.7028 | 8.6513 | -116.8708 | 5.5775 | 111.1859 | 0.0163 | 0.0093 |
| 2024_09_20 22:00 | 3255170 | 4 | 8.7157 | 13.0894 | -116.7031 | 14.3669 | 113.1353 | 0.0072 | 0.0104 |
| 2024_09_20 22:00 | 3263946 | 5 | 9.8060 | 12.7355 | -115.6628 | 8.6386 | 183.6947 | 0.0017 | 0.0056 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413291_B47297B3 | 504990 | 290 | -83.8 | 504990 | 923 | -83.7 | 504990 | 260 | -92.0 | 504990 | 935 |
| MR_1774413291_3F8D8159 | 504990 | 290 | -83.9 | 504990 | 923 | -84.9 | 504990 | 260 | -93.1 | 504990 | 935 |
| MR_1774413291_D356DCA2 | 504990 | 290 | -84.7 | 504990 | 923 | -84.2 | 504990 | 260 | -89.5 | 504990 | 935 |
| MR_1774413291_9147AEAF | 504990 | 290 | -84.2 | 504990 | 923 | -86.2 | 504990 | 260 | -90.3 | 504990 | 935 |
| MR_1774413291_B85B10FB | 504990 | 923 | -84.0 | 504990 | 290 | -86.3 | 504990 | 260 | -92.7 | 504990 | 935 |
| MR_1774413291_A0647660 | 504990 | 290 | -85.0 | 504990 | 923 | -84.1 | 504990 | 260 | -91.7 | 504990 | 935 |
| MR_1774413291_93D38B0F | 504990 | 290 | -83.7 | 504990 | 923 | -83.5 | 504990 | 260 | -93.1 | 504990 | 935 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 434: `cd7425c1-f24...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cd7425c1-f243-43f4-8b73-fefb9ae47553` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[434] topology](images/test_0434.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245603_2
- `C2`: Add neighbor relationship between 3227368_4 and 3245603_2
- `C3`: Adjust the azimuth of 3227368_4 by 50 degrees
- `C4`: Adjust the azimuth of 3245603_2 by 50 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227368_4
- `C6`: Press down the tilt angle  of 3245603_2 by 3 degrees
- `C7`: Decrease transmission power for 3245603_2
- `C8`: Press down the tilt angle of 3227368_4 by 9 degrees
- `C9`: Decrease transmission power for 3227368_4
- `C10`: Increase A3 Offset threshold for 3227368_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245603_2
- `C12`: Lift the tilt angle  of 3245603_2 by 3 degrees
- `C13`: Check test server and transmission issues
- `C14`: Lift the tilt angle of 3227368_4 by 9 degrees
- `C15`: Add neighbor relationship between 3217498_3 and 3245603_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease A3 Offset threshold for 3227368_4
- `C18`: Increase transmission power for 3245603_2
- `C19`: Increase A3 Offset threshold for 3245603_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227368_4
- `C21`: Decrease A3 Offset threshold for 3245603_2
- `C22`: Increase transmission power for 3227368_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.786 | MS1 | 121.4656705883 | 31.1446295696 | 629 | 504990 | -85.93 | 14.87 | 513.34 | 0.17 | 2.03 | 1567 |
| 2024-09-20 22:21:32.573 | MS1 | 121.4656633414 | 31.1446354958 | 629 | 504990 | -88.14 | 14.37 | 400.85 | 0.04 | 2.00 | 1586 |
| 2024-09-20 22:21:33.858 | MS1 | 121.4656686217 | 31.1446369135 | 629 | 504990 | -89.11 | 17.34 | 460.60 | 0.00 | 2.10 | 1585 |
| 2024-09-20 22:21:34.286 | MS1 | 121.4656755717 | 31.1446363841 | 629 | 504990 | -89.76 | 15.82 | 84.91 | 0.02 | 2.85 | 322 |
| 2024-09-20 22:21:35.302 | MS1 | 121.4656593783 | 31.1446263324 | 629 | 504990 | -88.31 | 17.42 | 98.53 | 0.18 | 2.31 | 314 |
| 2024-09-20 22:21:36.539 | MS1 | 121.4656734804 | 31.1446272809 | 629 | 504990 | -88.43 | 14.80 | 56.69 | 0.07 | 2.69 | 361 |
| 2024-09-20 22:21:37.578 | MS1 | 121.4656632386 | 31.1446316377 | 629 | 504990 | -93.61 | 8.53 | 49.69 | 0.19 | 2.49 | 491 |
| 2024-09-20 22:21:38.661 | MS1 | 121.4656682574 | 31.1446299672 | 629 | 504990 | -89.76 | 9.36 | 65.47 | 0.02 | 2.12 | 442 |
| 2024-09-20 22:21:39.513 | MS1 | 121.4656587418 | 31.1446288730 | 629 | 504990 | -93.16 | 10.43 | 68.38 | 0.01 | 2.84 | 455 |
| 2024-09-20 22:21:40.181 | MS1 | 121.4656767719 | 31.1446268890 | 629 | 504990 | -89.97 | 12.69 | 447.08 | 0.09 | 2.84 | 1565 |
| 2024-09-20 22:21:41.949 | MS1 | 121.4656752560 | 31.1446326507 | 629 | 504990 | -89.23 | 8.72 | 342.67 | 0.03 | 2.18 | 1594 |
| 2024-09-20 22:21:42.129 | MS1 | 121.4656627817 | 31.1446190114 | 629 | 504990 | -90.69 | 10.09 | 410.68 | 0.13 | 2.41 | 1597 |

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
| 3217498 | 3 | 121.4711500747 | 31.1500057129 | 236 | 7 | 1 | 30.7 | TDD | 643 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3220724 | 1 | 121.4733361423 | 31.1555290749 | 141 | 15 | 10 | 21.2 | TDD | 1000 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3227368 | 4 | 121.4726735570 | 31.1526039717 | 294 | 6 | 1 | 49.3 | TDD | 629 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3245603 | 2 | 121.4723615628 | 31.1524965368 | 359 | 2 | 10 | 19.2 | TDD | 121 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.323 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.344 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.476 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.476 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.189 | NREventA3 | measId:2;ServCellPCI:329;Se... |
| 2024-09-20 22:21:38.429 | NRHandoverAttempt | SourcePCI:329;SourceNR-ARFC... |
| 2024-09-20 22:21:38.462 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.475 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.602 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.602 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220724 | 1 | 15.2330 | 6.6664 | -115.8643 | 15.2296 | 134.7129 | 0.0068 | 0.0070 |
| 2024_09_20 22:00 | 3245603 | 2 | 6.5566 | 19.0951 | -115.6502 | 17.1537 | 80.0184 | 0.0061 | 0.0035 |
| 2024_09_20 22:00 | 3217498 | 3 | 6.8107 | 15.3842 | -116.2917 | 6.1562 | 126.3171 | 0.0111 | 0.0186 |
| 2024_09_20 22:00 | 3227368 | 4 | 13.9069 | 12.4421 | -115.9565 | 9.6058 | 151.9113 | 0.0159 | 0.0198 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412713_1D505A87 | 504990 | 629 | -88.9 | 504990 | 121 | -95.3 | 504990 | 643 | -102.6 | 504990 | 1000 |
| MR_1774412713_8FA956F9 | 504990 | 629 | -90.3 | 504990 | 121 | -92.3 | 504990 | 643 | -104.1 | 504990 | 1000 |
| MR_1774412713_262857C1 | 504990 | 629 | -89.9 | 504990 | 121 | -92.4 | 504990 | 643 | -102.0 | 504990 | 1000 |
| MR_1774412713_85C767F9 | 504990 | 629 | -89.4 | 504990 | 121 | -92.5 | 504990 | 643 | -104.0 | 504990 | 1000 |
| MR_1774412713_F6CBBFFF | 504990 | 629 | -91.2 | 504990 | 121 | -95.9 | 504990 | 643 | -104.0 | 504990 | 1000 |
| MR_1774412713_C015C33A | 504990 | 629 | -88.2 | 504990 | 121 | -95.1 | 504990 | 643 | -104.6 | 504990 | 1000 |
| MR_1774412713_4463344E | 504990 | 629 | -90.4 | 504990 | 121 | -94.7 | 504990 | 643 | -103.7 | 504990 | 1000 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 435: `13332a50-9e8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `13332a50-9e81-482b-8e42-09fac1d1dc20` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[435] topology](images/test_0435.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3256479_2
- `C2`: Press down the tilt angle  of 3262377_1 by 10 degrees
- `C3`: Lift the tilt angle  of 3262377_1 by 10 degrees
- `C4`: Press down the tilt angle of 3256479_2 by 4 degrees
- `C5`: Lift the tilt angle of 3256479_2 by 4 degrees
- `C6`: Add neighbor relationship between 3247189_3 and 3262377_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262377_1
- `C8`: Increase A3 Offset threshold for 3262377_1
- `C9`: Decrease transmission power for 3262377_1
- `C10`: Decrease A3 Offset threshold for 3262377_1
- `C11`: Decrease transmission power for 3256479_2
- `C12`: Increase A3 Offset threshold for 3256479_2
- `C13`: Check test server and transmission issues
- `C14`: Decrease A3 Offset threshold for 3256479_2
- `C15`: Add neighbor relationship between 3256479_2 and 3262377_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256479_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262377_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256479_2
- `C19`: Adjust the azimuth of 3256479_2 by 50 degrees
- `C20`: Increase transmission power for 3262377_1
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Adjust the azimuth of 3262377_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.408 | MS1 | 121.4656641109 | 31.1446242783 | 945 | 504990 | -86.05 | 15.19 | 588.72 | 0.15 | 2.40 | 1569 |
| 2024-09-20 22:21:32.730 | MS1 | 121.4656715530 | 31.1446293586 | 945 | 504990 | -85.32 | 15.45 | 380.47 | 0.07 | 2.80 | 1595 |
| 2024-09-20 22:21:33.146 | MS1 | 121.4656674234 | 31.1446274825 | 945 | 504990 | -89.64 | 17.35 | 347.26 | 0.12 | 2.75 | 1579 |
| 2024-09-20 22:21:34.884 | MS1 | 121.4656682706 | 31.1446232036 | 945 | 504990 | -89.10 | 12.36 | 69.17 | 0.16 | 2.03 | 316 |
| 2024-09-20 22:21:35.758 | MS1 | 121.4656632105 | 31.1446198518 | 945 | 504990 | -91.47 | 15.20 | 68.05 | 0.13 | 2.15 | 465 |
| 2024-09-20 22:21:36.770 | MS1 | 121.4656668039 | 31.1446295156 | 945 | 504990 | -88.16 | 14.23 | 84.46 | 0.12 | 2.10 | 497 |
| 2024-09-20 22:21:37.853 | MS1 | 121.4656694903 | 31.1446332335 | 945 | 504990 | -92.90 | 7.24 | 90.43 | 0.10 | 2.20 | 491 |
| 2024-09-20 22:21:38.792 | MS1 | 121.4656779839 | 31.1446365071 | 945 | 504990 | -92.89 | 8.18 | 62.72 | 0.02 | 2.75 | 399 |
| 2024-09-20 22:21:39.614 | MS1 | 121.4656622333 | 31.1446321273 | 945 | 504990 | -90.57 | 11.68 | 83.11 | 0.06 | 2.81 | 496 |
| 2024-09-20 22:21:40.209 | MS1 | 121.4656753897 | 31.1446213157 | 945 | 504990 | -89.03 | 9.39 | 387.37 | 0.02 | 2.05 | 1590 |
| 2024-09-20 22:21:41.180 | MS1 | 121.4656633280 | 31.1446332141 | 945 | 504990 | -91.15 | 10.05 | 550.64 | 0.17 | 2.27 | 1591 |
| 2024-09-20 22:21:42.402 | MS1 | 121.4656690131 | 31.1446319352 | 945 | 504990 | -92.02 | 11.57 | 589.33 | 0.09 | 2.28 | 1575 |

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
| 3247189 | 3 | 121.4708766939 | 31.1493918544 | 193 | 6 | 7 | 49.8 | TDD | 228 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3256479 | 2 | 121.4642278375 | 31.1497134685 | 299 | 0 | 1 | 38.2 | TDD | 945 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3262377 | 1 | 121.4670112424 | 31.1489779161 | 133 | 6 | 8 | 47.6 | TDD | 128 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3264404 | 4 | 121.4732479576 | 31.1525208218 | 345 | 9 | 3 | 21.4 | TDD | 191 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.869 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.887 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.036 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.036 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.746 | NREventA3 | measId:2;ServCellPCI:608;Se... |
| 2024-09-20 22:21:37.986 | NRHandoverAttempt | SourcePCI:608;SourceNR-ARFC... |
| 2024-09-20 22:21:38.018 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.032 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.143 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.143 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262377 | 1 | 13.8161 | 8.9150 | -116.8637 | 8.9625 | 179.6288 | 0.0160 | 0.0109 |
| 2024_09_20 22:00 | 3256479 | 2 | 10.0993 | 16.8797 | -114.2314 | 18.6202 | 134.0614 | 0.0077 | 0.0187 |
| 2024_09_20 22:00 | 3247189 | 3 | 11.3600 | 17.3728 | -114.4414 | 15.3592 | 167.3736 | 0.0028 | 0.0078 |
| 2024_09_20 22:00 | 3264404 | 4 | 6.4317 | 15.4000 | -115.1565 | 8.5401 | 156.4089 | 0.0159 | 0.0100 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413145_1DB3FC40 | 504990 | 945 | -87.3 | 504990 | 128 | -89.0 | 504990 | 228 | -101.1 | 504990 | 191 |
| MR_1774413145_97958C6B | 504990 | 945 | -90.9 | 504990 | 128 | -89.2 | 504990 | 228 | -102.5 | 504990 | 191 |
| MR_1774413145_3E20D28D | 504990 | 945 | -88.1 | 504990 | 128 | -89.5 | 504990 | 228 | -101.2 | 504990 | 191 |
| MR_1774413145_26EFDD91 | 504990 | 945 | -88.1 | 504990 | 128 | -89.9 | 504990 | 228 | -102.0 | 504990 | 191 |
| MR_1774413145_F80A212A | 504990 | 945 | -90.8 | 504990 | 128 | -90.6 | 504990 | 228 | -103.1 | 504990 | 191 |
| MR_1774413145_A7123598 | 504990 | 945 | -87.8 | 504990 | 128 | -91.3 | 504990 | 228 | -103.6 | 504990 | 191 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 436: `83cee0ce-2bb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `83cee0ce-2bbf-482e-94e5-1910a7ce7688` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[436] topology](images/test_0436.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3253042_3
- `C2`: Increase transmission power for 3253042_3
- `C3`: Press down the tilt angle of 3253042_3 by 10 degrees
- `C4`: Lift the tilt angle  of 3228448_2 by 1 degrees
- `C5`: Increase A3 Offset threshold for 3253042_3
- `C6`: Lift the tilt angle of 3253042_3 by 10 degrees
- `C7`: Press down the tilt angle  of 3228448_2 by 1 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228448_2
- `C9`: Add neighbor relationship between 3253042_3 and 3228448_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228448_2
- `C11`: Increase transmission power for 3228448_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253042_3
- `C13`: Decrease transmission power for 3228448_2
- `C14`: Add neighbor relationship between 3249792_1 and 3228448_2
- `C15`: Adjust the azimuth of 3228448_2 by 20 degrees
- `C16`: Adjust the azimuth of 3253042_3 by 30 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253042_3
- `C18`: Increase A3 Offset threshold for 3228448_2
- `C19`: Check test server and transmission issues
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease A3 Offset threshold for 3253042_3
- `C22`: Decrease A3 Offset threshold for 3228448_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.117 | MS1 | 121.4656728820 | 31.1446315790 | 437 | 504990 | -88.94 | 16.82 | 564.70 | 0.15 | 2.06 | 1576 |
| 2024-09-20 22:21:32.692 | MS1 | 121.4656772042 | 31.1446358720 | 437 | 504990 | -92.83 | 15.37 | 581.14 | 0.05 | 2.38 | 1582 |
| 2024-09-20 22:21:33.318 | MS1 | 121.4656678565 | 31.1446308550 | 437 | 504990 | -85.53 | 13.86 | 486.11 | 0.14 | 2.83 | 1598 |
| 2024-09-20 22:21:34.506 | MS1 | 121.4656759240 | 31.1446313466 | 437 | 504990 | -107.76 | 1.34 | 31.03 | 0.01 | 1.31 | 1565 |
| 2024-09-20 22:21:35.285 | MS1 | 121.4656729137 | 31.1446241787 | 437 | 504990 | -102.34 | -1.18 | 67.25 | 0.04 | 1.38 | 1590 |
| 2024-09-20 22:21:36.455 | MS1 | 121.4656608712 | 31.1446346019 | 437 | 504990 | -102.31 | 0.04 | 56.88 | 0.19 | 1.43 | 1578 |
| 2024-09-20 22:21:37.302 | MS1 | 121.4656718426 | 31.1446247662 | 437 | 504990 | -104.96 | -0.76 | 53.66 | 0.11 | 1.02 | 1589 |
| 2024-09-20 22:21:38.258 | MS1 | 121.4656609741 | 31.1446364640 | 437 | 504990 | -100.73 | -0.04 | 26.34 | 0.06 | 1.32 | 1583 |
| 2024-09-20 22:21:39.403 | MS1 | 121.4656749390 | 31.1446335016 | 437 | 504990 | -106.33 | -1.97 | 22.47 | 0.18 | 1.47 | 1581 |
| 2024-09-20 22:21:40.443 | MS1 | 121.4656679963 | 31.1446359258 | 437 | 504990 | -92.73 | 16.19 | 579.24 | 0.18 | 2.73 | 1576 |
| 2024-09-20 22:21:41.959 | MS1 | 121.4656617263 | 31.1446350793 | 437 | 504990 | -88.82 | 12.71 | 359.10 | 0.13 | 2.48 | 1581 |
| 2024-09-20 22:21:42.318 | MS1 | 121.4656625529 | 31.1446277313 | 437 | 504990 | -89.15 | 13.41 | 581.31 | 0.11 | 2.37 | 1600 |

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
| 3228448 | 2 | 121.4748432875 | 31.1548352327 | 198 | 0 | 12 | 29.5 | TDD | 535 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3249792 | 1 | 121.4694546870 | 31.1505729752 | 160 | 8 | 6 | 18.9 | TDD | 347 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3253042 | 3 | 121.4647170205 | 31.1479297812 | 136 | 5 | 6 | 44.9 | TDD | 437 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3275328 | 4 | 121.4756375382 | 31.1489260873 | 123 | 12 | 11 | 40.8 | TDD | 183 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.500 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.607 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.607 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.800 | NREventA2 | measId:1;ServCellPCI:700;Se... |
| 2024-09-20 22:21:34.909 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249792 | 1 | 13.1464 | 11.4139 | -114.0554 | 17.7321 | 198.6916 | 0.0129 | 0.0021 |
| 2024_09_20 22:00 | 3228448 | 2 | 9.1637 | 17.0912 | -117.7674 | 11.0587 | 99.2316 | 0.0099 | 0.0119 |
| 2024_09_20 22:00 | 3253042 | 3 | 16.8135 | 5.4683 | -116.6041 | 9.8576 | 125.4670 | 0.1274 | 0.0151 |
| 2024_09_20 22:00 | 3275328 | 4 | 6.0747 | 17.3595 | -115.4161 | 8.9531 | 97.4446 | 0.0137 | 0.0143 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413334_C3238475 | 504990 | 437 | -108.7 | 504990 | 535 | -110.2 | 504990 | 347 | -116.3 | 504990 | 183 |
| MR_1774413334_19A1A93C | 504990 | 437 | -109.1 | 504990 | 535 | -111.8 | 504990 | 347 | -116.8 | 504990 | 183 |
| MR_1774413334_C5186A9D | 504990 | 437 | -106.3 | 504990 | 535 | -111.3 | 504990 | 347 | -117.4 | 504990 | 183 |
| MR_1774413334_50C7AD4F | 504990 | 437 | -107.6 | 504990 | 535 | -112.8 | 504990 | 347 | -118.4 | 504990 | 183 |
| MR_1774413334_AE08151A | 504990 | 437 | -107.0 | 504990 | 535 | -111.2 | 504990 | 347 | -116.9 | 504990 | 183 |
| MR_1774413334_A84E916B | 504990 | 437 | -109.2 | 504990 | 535 | -112.0 | 504990 | 347 | -120.0 | 504990 | 183 |
| MR_1774413334_925E2E70 | 504990 | 437 | -109.6 | 504990 | 535 | -112.4 | 504990 | 347 | -118.5 | 504990 | 183 |
| MR_1774413334_0BF716FC | 504990 | 437 | -108.1 | 504990 | 535 | -110.2 | 504990 | 347 | -118.4 | 504990 | 183 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 437: `ad0b061e-912...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ad0b061e-9122-41fa-940b-3f8348a42138` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[437] topology](images/test_0437.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3253241_3 by 50 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253241_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237366_4
- `C4`: Increase A3 Offset threshold for 3237366_4
- `C5`: Decrease A3 Offset threshold for 3237366_4
- `C6`: Decrease A3 Offset threshold for 3253241_3
- `C7`: Add neighbor relationship between 3253241_3 and 3237366_4
- `C8`: Decrease transmission power for 3253241_3
- `C9`: Press down the tilt angle of 3253241_3 by 5 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease transmission power for 3237366_4
- `C12`: Increase A3 Offset threshold for 3253241_3
- `C13`: Increase transmission power for 3237366_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237366_4
- `C15`: Adjust the azimuth of 3237366_4 by 50 degrees
- `C16`: Add neighbor relationship between 3211853_2 and 3237366_4
- `C17`: Lift the tilt angle  of 3237366_4 by 10 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253241_3
- `C19`: Increase transmission power for 3253241_3
- `C20`: Press down the tilt angle  of 3237366_4 by 10 degrees
- `C21`: Lift the tilt angle of 3253241_3 by 5 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.660 | MS1 | 121.4656761845 | 31.1446222433 | 732 | 504990 | -75.79 | 16.90 | 510.26 | 0.14 | 2.05 | 1578 |
| 2024-09-20 22:21:32.823 | MS1 | 121.4656712765 | 31.1446228054 | 732 | 504990 | -79.87 | 16.96 | 341.71 | 0.11 | 2.01 | 1567 |
| 2024-09-20 22:21:33.727 | MS1 | 121.4656606058 | 31.1446376914 | 732 | 504990 | -81.57 | 14.41 | 347.52 | 0.00 | 2.26 | 1581 |
| 2024-09-20 22:21:34.639 | MS1 | 121.4656654427 | 31.1446183698 | 732 | 504990 | -86.31 | -1.77 | 36.51 | 0.11 | 1.41 | 1574 |
| 2024-09-20 22:21:35.567 | MS1 | 121.4656762934 | 31.1446230317 | 732 | 504990 | -83.02 | -0.11 | 77.61 | 0.04 | 1.06 | 1579 |
| 2024-09-20 22:21:36.892 | MS1 | 121.4656741148 | 31.1446212015 | 732 | 504990 | -87.93 | -0.06 | 61.39 | 0.07 | 1.36 | 1576 |
| 2024-09-20 22:21:37.939 | MS1 | 121.4656595221 | 31.1446348744 | 732 | 504990 | -89.13 | -0.06 | 59.20 | 0.16 | 1.19 | 1573 |
| 2024-09-20 22:21:38.981 | MS1 | 121.4656620676 | 31.1446256111 | 732 | 504990 | -86.85 | -3.13 | 35.96 | 0.05 | 1.22 | 1597 |
| 2024-09-20 22:21:39.242 | MS1 | 121.4656763280 | 31.1446279133 | 397 | 504990 | -81.90 | 16.81 | 161.06 | 0.11 | 1.30 | 1576 |
| 2024-09-20 22:21:40.994 | MS1 | 121.4656629588 | 31.1446189764 | 397 | 504990 | -77.20 | 13.50 | 582.67 | 0.11 | 3.00 | 1568 |
| 2024-09-20 22:21:41.610 | MS1 | 121.4656622169 | 31.1446379446 | 397 | 504990 | -79.92 | 13.47 | 529.67 | 0.03 | 2.82 | 1585 |
| 2024-09-20 22:21:42.699 | MS1 | 121.4656616870 | 31.1446346513 | 397 | 504990 | -76.24 | 15.17 | 354.71 | 0.19 | 2.94 | 1579 |

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
| 3211853 | 2 | 121.4692886902 | 31.1549066952 | 278 | 7 | 11 | 26.0 | TDD | 777 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3237366 | 4 | 121.4704548805 | 31.1474169064 | 90 | 14 | 12 | 24.8 | TDD | 397 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3248840 | 1 | 121.4736602281 | 31.1464151455 | 141 | 12 | 0 | 36.2 | TDD | 728 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3253241 | 3 | 121.4759965649 | 31.1526512525 | 339 | 4 | 5 | 31.8 | TDD | 732 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.146 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.168 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.279 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.279 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.984 | NREventA3 | measId:2;ServCellPCI:506;Se... |
| 2024-09-20 22:21:38.224 | NRHandoverAttempt | SourcePCI:506;SourceNR-ARFC... |
| 2024-09-20 22:21:38.273 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.283 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.419 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.419 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248840 | 1 | 11.0676 | 11.4642 | -115.3243 | 12.7164 | 191.6467 | 0.0009 | 0.0126 |
| 2024_09_20 22:00 | 3211853 | 2 | 19.2410 | 16.1613 | -116.8492 | 6.1004 | 128.2483 | 0.0061 | 0.0134 |
| 2024_09_20 22:00 | 3253241 | 3 | 18.8408 | 5.4953 | -115.6168 | 19.5115 | 102.6130 | 0.0179 | 0.1999 |
| 2024_09_20 22:00 | 3237366 | 4 | 12.2187 | 16.1482 | -114.3933 | 8.7300 | 191.9853 | 0.0016 | 0.0036 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414769_A27AED12 | 504990 | 732 | -87.7 | 504990 | 397 | -80.8 | 504990 | 777 | -82.9 | 504990 | 728 |
| MR_1774414769_26A20EEE | 504990 | 732 | -86.4 | 504990 | 397 | -77.4 | 504990 | 777 | -81.5 | 504990 | 728 |
| MR_1774414769_85F3ED35 | 504990 | 397 | -81.0 | 504990 | 732 | -84.4 | 504990 | 777 | -79.8 | 504990 | 728 |
| MR_1774414769_C1CB62DB | 504990 | 732 | -87.3 | 504990 | 397 | -79.2 | 504990 | 777 | -79.3 | 504990 | 728 |
| MR_1774414769_0F58C8E5 | 504990 | 732 | -84.5 | 504990 | 397 | -81.1 | 504990 | 777 | -81.0 | 504990 | 728 |
| MR_1774414769_6EF58D28 | 504990 | 732 | -86.4 | 504990 | 397 | -80.1 | 504990 | 777 | -82.2 | 504990 | 728 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 438: `e3217eba-56b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e3217eba-56be-49c0-ac3b-78fc298dcf55` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[438] topology](images/test_0438.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Add neighbor relationship between 3277641_1 and 3235169_4
- `C3`: Increase A3 Offset threshold for 3235169_4
- `C4`: Adjust the azimuth of 3235169_4 by 24 degrees
- `C5`: Check test server and transmission issues
- `C6`: Press down the tilt angle of 3262258_2 by 10 degrees
- `C7`: Lift the tilt angle of 3262258_2 by 10 degrees
- `C8`: Decrease transmission power for 3262258_2
- `C9`: Press down the tilt angle  of 3235169_4 by 5 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235169_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262258_2
- `C12`: Decrease transmission power for 3235169_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235169_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262258_2
- `C15`: Add neighbor relationship between 3262258_2 and 3235169_4
- `C16`: Decrease A3 Offset threshold for 3235169_4
- `C17`: Increase A3 Offset threshold for 3262258_2
- `C18`: Increase transmission power for 3235169_4
- `C19`: Lift the tilt angle  of 3235169_4 by 5 degrees
- `C20`: Adjust the azimuth of 3262258_2 by 46 degrees
- `C21`: Increase transmission power for 3262258_2
- `C22`: Decrease A3 Offset threshold for 3262258_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.341 | MS1 | 121.4656738080 | 31.1446335211 | 548 | 504990 | -90.59 | 15.50 | 487.18 | 0.11 | 2.67 | 1573 |
| 2024-09-20 22:21:32.320 | MS1 | 121.4656641290 | 31.1446237576 | 548 | 504990 | -91.76 | 13.92 | 343.31 | 0.07 | 2.91 | 1595 |
| 2024-09-20 22:21:33.182 | MS1 | 121.4656637801 | 31.1446361166 | 548 | 504990 | -89.69 | 13.29 | 349.25 | 0.09 | 2.85 | 1599 |
| 2024-09-20 22:21:34.701 | MS1 | 121.4656768689 | 31.1446247372 | 548 | 504990 | -100.29 | -1.97 | 37.23 | 0.19 | 1.06 | 1591 |
| 2024-09-20 22:21:35.967 | MS1 | 121.4656699915 | 31.1446315021 | 548 | 504990 | -108.20 | -1.14 | 27.77 | 0.14 | 1.46 | 1593 |
| 2024-09-20 22:21:36.895 | MS1 | 121.4656605089 | 31.1446272476 | 548 | 504990 | -104.28 | 1.09 | 79.48 | 0.11 | 1.35 | 1588 |
| 2024-09-20 22:21:37.438 | MS1 | 121.4656625476 | 31.1446231148 | 548 | 504990 | -103.98 | -1.98 | 56.83 | 0.02 | 1.32 | 1598 |
| 2024-09-20 22:21:38.186 | MS1 | 121.4656747478 | 31.1446358186 | 548 | 504990 | -103.23 | -0.91 | 51.93 | 0.14 | 1.47 | 1599 |
| 2024-09-20 22:21:39.500 | MS1 | 121.4656600155 | 31.1446369066 | 548 | 504990 | -109.23 | 0.98 | 77.26 | 0.01 | 1.21 | 1568 |
| 2024-09-20 22:21:40.338 | MS1 | 121.4656636545 | 31.1446242977 | 548 | 504990 | -89.79 | 13.12 | 398.91 | 0.10 | 2.20 | 1600 |
| 2024-09-20 22:21:41.820 | MS1 | 121.4656723478 | 31.1446291922 | 548 | 504990 | -91.83 | 12.95 | 362.46 | 0.08 | 2.15 | 1597 |
| 2024-09-20 22:21:42.701 | MS1 | 121.4656602786 | 31.1446269958 | 548 | 504990 | -91.61 | 17.85 | 532.69 | 0.19 | 2.63 | 1568 |

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
| 3215201 | 3 | 121.4694372309 | 31.1480054996 | 328 | 3 | 6 | 41.6 | TDD | 678 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3235169 | 4 | 121.4700816075 | 31.1558610336 | 223 | 4 | 6 | 32.0 | TDD | 750 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3262258 | 2 | 121.4682658354 | 31.1443100567 | 232 | 1 | 9 | 45.4 | TDD | 548 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3277641 | 1 | 121.4668327359 | 31.1463647473 | 302 | 8 | 10 | 26.2 | TDD | 832 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.838 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.859 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.983 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.983 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.221 | NREventA2 | measId:1;ServCellPCI:677;Se... |
| 2024-09-20 22:21:34.344 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277641 | 1 | 17.0083 | 13.9715 | -114.5908 | 14.8284 | 177.3694 | 0.0047 | 0.0055 |
| 2024_09_20 22:00 | 3262258 | 2 | 7.3761 | 8.5219 | -115.6862 | 9.3004 | 197.2567 | 0.1539 | 0.0028 |
| 2024_09_20 22:00 | 3215201 | 3 | 15.2830 | 8.6288 | -114.7184 | 18.0697 | 100.6936 | 0.0044 | 0.0041 |
| 2024_09_20 22:00 | 3235169 | 4 | 9.4679 | 5.5342 | -114.8843 | 9.9104 | 156.3639 | 0.0004 | 0.0116 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415430_0599D007 | 504990 | 548 | -102.1 | 504990 | 750 | -104.1 | 504990 | 832 | -111.0 | 504990 | 678 |
| MR_1774415430_22C13490 | 504990 | 548 | -99.9 | 504990 | 750 | -101.8 | 504990 | 832 | -109.9 | 504990 | 678 |
| MR_1774415430_18BE93BF | 504990 | 548 | -101.6 | 504990 | 750 | -105.0 | 504990 | 832 | -111.6 | 504990 | 678 |
| MR_1774415430_8789604C | 504990 | 548 | -101.3 | 504990 | 750 | -103.1 | 504990 | 832 | -112.8 | 504990 | 678 |
| MR_1774415430_FB5D6BAC | 504990 | 548 | -100.7 | 504990 | 750 | -103.9 | 504990 | 832 | -112.7 | 504990 | 678 |
| MR_1774415430_DA030307 | 504990 | 548 | -99.2 | 504990 | 750 | -102.9 | 504990 | 832 | -109.3 | 504990 | 678 |
| MR_1774415430_FDBE145F | 504990 | 548 | -102.1 | 504990 | 750 | -103.2 | 504990 | 832 | -109.7 | 504990 | 678 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 439: `8a5359c1-ae6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8a5359c1-ae64-48e6-9bf4-2e75a9062d93` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[439] topology](images/test_0439.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3274858_1
- `C2`: Increase transmission power for 3274858_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278724_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274858_1
- `C5`: Decrease transmission power for 3278724_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274858_1
- `C7`: Decrease A3 Offset threshold for 3274858_1
- `C8`: Adjust the azimuth of 3278724_3 by 25 degrees
- `C9`: Add neighbor relationship between 3271092_2 and 3278724_3
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Press down the tilt angle  of 3278724_3 by 5 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278724_3
- `C13`: Decrease transmission power for 3274858_1
- `C14`: Check test server and transmission issues
- `C15`: Add neighbor relationship between 3274858_1 and 3278724_3
- `C16`: Lift the tilt angle  of 3278724_3 by 5 degrees
- `C17`: Press down the tilt angle of 3274858_1 by 10 degrees
- `C18`: Increase A3 Offset threshold for 3278724_3
- `C19`: Increase transmission power for 3278724_3
- `C20`: Lift the tilt angle of 3274858_1 by 10 degrees
- `C21`: Decrease A3 Offset threshold for 3278724_3
- `C22`: Adjust the azimuth of 3274858_1 by 43 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.722 | MS1 | 121.4656749057 | 31.1446259104 | 232 | 504990 | -88.14 | 17.78 | 308.03 | 0.18 | 2.48 | 1589 |
| 2024-09-20 22:21:32.652 | MS1 | 121.4656650079 | 31.1446301431 | 232 | 504990 | -89.38 | 16.08 | 556.12 | 0.12 | 2.89 | 1560 |
| 2024-09-20 22:21:33.559 | MS1 | 121.4656616173 | 31.1446223382 | 232 | 504990 | -85.08 | 15.88 | 407.78 | 0.08 | 2.06 | 1594 |
| 2024-09-20 22:21:34.870 | MS1 | 121.4656672750 | 31.1446244052 | 232 | 504990 | -104.92 | 1.77 | 33.38 | 0.09 | 1.02 | 1590 |
| 2024-09-20 22:21:35.143 | MS1 | 121.4656613287 | 31.1446245892 | 232 | 504990 | -100.66 | 0.50 | 16.94 | 0.11 | 1.02 | 1587 |
| 2024-09-20 22:21:36.792 | MS1 | 121.4656740281 | 31.1446317694 | 232 | 504990 | -101.65 | -1.18 | 59.69 | 0.01 | 1.39 | 1592 |
| 2024-09-20 22:21:37.274 | MS1 | 121.4656589137 | 31.1446203575 | 232 | 504990 | -104.57 | 0.35 | 46.72 | 0.10 | 1.20 | 1595 |
| 2024-09-20 22:21:38.978 | MS1 | 121.4656606657 | 31.1446231616 | 232 | 504990 | -102.16 | -1.21 | 34.85 | 0.09 | 1.45 | 1575 |
| 2024-09-20 22:21:39.960 | MS1 | 121.4656774421 | 31.1446271572 | 232 | 504990 | -109.52 | 1.34 | 70.97 | 0.17 | 1.18 | 1584 |
| 2024-09-20 22:21:40.281 | MS1 | 121.4656773453 | 31.1446233900 | 232 | 504990 | -93.03 | 16.20 | 385.71 | 0.19 | 2.56 | 1582 |
| 2024-09-20 22:21:41.186 | MS1 | 121.4656601035 | 31.1446239730 | 232 | 504990 | -88.57 | 13.99 | 353.20 | 0.03 | 2.02 | 1580 |
| 2024-09-20 22:21:42.648 | MS1 | 121.4656741873 | 31.1446271307 | 232 | 504990 | -88.71 | 12.79 | 538.30 | 0.10 | 3.00 | 1586 |

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
| 3224834 | 4 | 121.4755546344 | 31.1448442650 | 1 | 6 | 6 | 32.7 | TDD | 447 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3271092 | 2 | 121.4750888760 | 31.1460157132 | 77 | 0 | 1 | 31.5 | TDD | 233 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3274858 | 1 | 121.4665415445 | 31.1537944568 | 228 | 8 | 3 | 29.5 | TDD | 232 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3278724 | 3 | 121.4751134426 | 31.1463775888 | 283 | 3 | 11 | 30.1 | TDD | 491 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.223 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.238 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.372 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.372 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.599 | NREventA2 | measId:1;ServCellPCI:381;Se... |
| 2024-09-20 22:21:34.701 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274858 | 1 | 12.5133 | 8.9768 | -115.9713 | 8.2082 | 117.1814 | 0.1576 | 0.0132 |
| 2024_09_20 22:00 | 3271092 | 2 | 19.9201 | 11.0495 | -114.8780 | 10.7704 | 114.5025 | 0.0140 | 0.0125 |
| 2024_09_20 22:00 | 3278724 | 3 | 11.1771 | 9.4321 | -114.4845 | 9.9602 | 153.7720 | 0.0145 | 0.0103 |
| 2024_09_20 22:00 | 3224834 | 4 | 7.9225 | 6.0787 | -115.5809 | 14.3367 | 163.9909 | 0.0091 | 0.0197 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415700_01DD1280 | 504990 | 232 | -105.6 | 504990 | 491 | -108.3 | 504990 | 233 | -112.8 | 504990 | 447 |
| MR_1774415700_DD1BCB63 | 504990 | 232 | -106.1 | 504990 | 491 | -109.7 | 504990 | 233 | -113.3 | 504990 | 447 |
| MR_1774415700_8DAA95D8 | 504990 | 232 | -103.5 | 504990 | 491 | -107.2 | 504990 | 233 | -113.0 | 504990 | 447 |
| MR_1774415700_2A1291B1 | 504990 | 232 | -103.5 | 504990 | 491 | -110.6 | 504990 | 233 | -113.2 | 504990 | 447 |
| MR_1774415700_9EB7A567 | 504990 | 232 | -106.5 | 504990 | 491 | -107.2 | 504990 | 233 | -111.7 | 504990 | 447 |
| MR_1774415700_703F1F8B | 504990 | 232 | -103.6 | 504990 | 491 | -107.2 | 504990 | 233 | -113.8 | 504990 | 447 |

> *... 2개 열 생략 (전체 14열)*

---
