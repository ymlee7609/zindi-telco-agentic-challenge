# Track A 문제 분석 — test[120]~test[129]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[120] ~ test[129] (10개)

## 목차

1. [문제 120: `b6ff0bd0-7dc...`](#120) — single-answer
2. [문제 121: `4c8eb707-664...`](#121) — single-answer
3. [문제 122: `284e3fa1-c8a...`](#122) — single-answer
4. [문제 123: `8c5dae6f-b78...`](#123) — single-answer
5. [문제 124: `7a77f811-99d...`](#124) — single-answer
6. [문제 125: `182b5716-ebb...`](#125) — single-answer
7. [문제 126: `0e98afd0-e86...`](#126) — single-answer
8. [문제 127: `9fe58e8a-2f9...`](#127) — single-answer
9. [문제 128: `68eac603-caa...`](#128) — single-answer
10. [문제 129: `7874bc60-b5f...`](#129) — single-answer

---

### 문제 120: `b6ff0bd0-7dc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b6ff0bd0-7dc5-400c-b4c1-037d23d2f119` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[120] topology](images/test_0120.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3218178_1 by 4 degrees
- `C2`: Lift the tilt angle of 3218178_1 by 4 degrees
- `C3`: Decrease transmission power for 3272108_2
- `C4`: Lift the tilt angle  of 3272108_2 by 6 degrees
- `C5`: Decrease A3 Offset threshold for 3218178_1
- `C6`: Increase A3 Offset threshold for 3272108_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272108_2
- `C8`: Add neighbor relationship between 3218178_1 and 3272108_2
- `C9`: Increase transmission power for 3218178_1
- `C10`: Decrease A3 Offset threshold for 3272108_2
- `C11`: Increase transmission power for 3272108_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272108_2
- `C13`: Increase A3 Offset threshold for 3218178_1
- `C14`: Decrease transmission power for 3218178_1
- `C15`: Press down the tilt angle  of 3272108_2 by 6 degrees
- `C16`: Check test server and transmission issues
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218178_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Adjust the azimuth of 3218178_1 by 33 degrees
- `C20`: Adjust the azimuth of 3272108_2 by 50 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218178_1
- `C22`: Add neighbor relationship between 3229556_3 and 3272108_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.964 | MS1 | 121.4656676279 | 31.1446229655 | 802 | 504990 | -86.61 | 12.70 | 316.96 | 0.08 | 2.80 | 1594 |
| 2024-09-20 22:21:32.563 | MS1 | 121.4656659355 | 31.1446286158 | 802 | 504990 | -89.32 | 17.11 | 329.14 | 0.02 | 2.12 | 1566 |
| 2024-09-20 22:21:33.100 | MS1 | 121.4656699026 | 31.1446355560 | 802 | 504990 | -87.13 | 16.99 | 510.74 | 0.06 | 2.78 | 1599 |
| 2024-09-20 22:21:34.652 | MS1 | 121.4656582968 | 31.1446210936 | 802 | 504990 | -90.92 | 15.11 | 105.24 | 0.50 | 2.64 | 653 |
| 2024-09-20 22:21:35.812 | MS1 | 121.4656646385 | 31.1446223980 | 802 | 504990 | -91.32 | 15.50 | 88.51 | 0.64 | 2.21 | 508 |
| 2024-09-20 22:21:36.134 | MS1 | 121.4656631608 | 31.1446364329 | 802 | 504990 | -86.45 | 13.73 | 78.56 | 0.60 | 2.47 | 554 |
| 2024-09-20 22:21:37.297 | MS1 | 121.4656752797 | 31.1446212780 | 802 | 504990 | -89.79 | 8.05 | 83.84 | 0.69 | 2.77 | 588 |
| 2024-09-20 22:21:38.672 | MS1 | 121.4656745524 | 31.1446302361 | 802 | 504990 | -92.57 | 12.66 | 91.49 | 0.69 | 2.34 | 572 |
| 2024-09-20 22:21:39.213 | MS1 | 121.4656702269 | 31.1446230011 | 802 | 504990 | -89.39 | 10.27 | 76.81 | 0.69 | 2.66 | 579 |
| 2024-09-20 22:21:40.334 | MS1 | 121.4656734589 | 31.1446314605 | 802 | 504990 | -92.92 | 7.25 | 381.00 | 0.08 | 2.08 | 1578 |
| 2024-09-20 22:21:41.707 | MS1 | 121.4656685987 | 31.1446323215 | 802 | 504990 | -92.90 | 11.58 | 451.26 | 0.20 | 2.71 | 1596 |
| 2024-09-20 22:21:42.215 | MS1 | 121.4656591998 | 31.1446283543 | 802 | 504990 | -91.87 | 9.85 | 533.70 | 0.19 | 2.76 | 1587 |

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
| 3218178 | 1 | 121.4671774958 | 31.1498198232 | 161 | 2 | 12 | 16.2 | TDD | 802 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3229556 | 3 | 121.4664619928 | 31.1519591858 | 133 | 7 | 3 | 25.4 | TDD | 804 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3240701 | 4 | 121.4703774973 | 31.1464215395 | 154 | 12 | 0 | 37.5 | TDD | 324 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3272108 | 2 | 121.4733031251 | 31.1544648361 | 299 | 5 | 9 | 17.8 | TDD | 348 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.979 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.979 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.669 | NREventA3 | measId:2;ServCellPCI:751;Se... |
| 2024-09-20 22:21:37.909 | NRHandoverAttempt | SourcePCI:751;SourceNR-ARFC... |
| 2024-09-20 22:21:37.959 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.969 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.095 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.095 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218178 | 1 | 9.0110 | 19.2134 | -117.9816 | 14.7856 | 86.7535 | 0.0047 | 0.0080 |
| 2024_09_20 22:00 | 3272108 | 2 | 12.4297 | 19.2019 | -117.9817 | 8.9844 | 100.2228 | 0.0100 | 0.0196 |
| 2024_09_20 22:00 | 3229556 | 3 | 19.6082 | 18.9887 | -117.2136 | 19.8749 | 142.2788 | 0.0084 | 0.0142 |
| 2024_09_20 22:00 | 3240701 | 4 | 19.6642 | 19.1377 | -114.2630 | 17.4326 | 153.6819 | 0.0178 | 0.0190 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414186_7FFDC9C8 | 504990 | 802 | -90.3 | 504990 | 348 | -94.9 | 504990 | 804 | -102.6 | 504990 | 324 |
| MR_1774414186_68D12186 | 504990 | 802 | -90.6 | 504990 | 348 | -93.1 | 504990 | 804 | -103.4 | 504990 | 324 |
| MR_1774414186_DD5E00F4 | 504990 | 802 | -89.5 | 504990 | 348 | -94.0 | 504990 | 804 | -102.1 | 504990 | 324 |
| MR_1774414186_6FF851A6 | 504990 | 802 | -89.9 | 504990 | 348 | -95.1 | 504990 | 804 | -103.5 | 504990 | 324 |
| MR_1774414186_93E1D4D4 | 504990 | 802 | -90.7 | 504990 | 348 | -92.7 | 504990 | 804 | -102.6 | 504990 | 324 |
| MR_1774414186_F8273549 | 504990 | 802 | -92.4 | 504990 | 348 | -95.6 | 504990 | 804 | -102.7 | 504990 | 324 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 121: `4c8eb707-664...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4c8eb707-6640-4d74-90b1-ed51d9ea8e66` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[121] topology](images/test_0121.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3220198_2
- `C2`: Adjust the azimuth of 3253735_3 by 38 degrees
- `C3`: Increase A3 Offset threshold for 3220198_2
- `C4`: Adjust the azimuth of 3220198_2 by 35 degrees
- `C5`: Increase transmission power for 3220198_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220198_2
- `C7`: Add neighbor relationship between 3236762_4 and 3253735_3
- `C8`: Decrease transmission power for 3220198_2
- `C9`: Check test server and transmission issues
- `C10`: Increase transmission power for 3253735_3
- `C11`: Decrease A3 Offset threshold for 3253735_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253735_3
- `C13`: Increase A3 Offset threshold for 3253735_3
- `C14`: Press down the tilt angle of 3220198_2 by 6 degrees
- `C15`: Lift the tilt angle  of 3253735_3 by 2 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220198_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253735_3
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease transmission power for 3253735_3
- `C20`: Press down the tilt angle  of 3253735_3 by 2 degrees
- `C21`: Add neighbor relationship between 3220198_2 and 3253735_3
- `C22`: Lift the tilt angle of 3220198_2 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.968 | MS1 | 121.4656661064 | 31.1446264349 | 994 | 504990 | -87.50 | 15.13 | 448.09 | 0.02 | 2.19 | 1576 |
| 2024-09-20 22:21:32.276 | MS1 | 121.4656625051 | 31.1446237938 | 994 | 504990 | -89.40 | 15.26 | 481.67 | 0.19 | 2.98 | 1598 |
| 2024-09-20 22:21:33.617 | MS1 | 121.4656718120 | 31.1446327214 | 994 | 504990 | -91.63 | 14.42 | 425.79 | 0.13 | 2.55 | 1580 |
| 2024-09-20 22:21:34.964 | MS1 | 121.4656754523 | 31.1446226784 | 994 | 504990 | -89.50 | 13.68 | 52.15 | 0.03 | 2.68 | 1584 |
| 2024-09-20 22:21:35.931 | MS1 | 121.4656713681 | 31.1446221452 | 994 | 504990 | -91.30 | 16.86 | 60.10 | 0.06 | 2.91 | 1567 |
| 2024-09-20 22:21:36.730 | MS1 | 121.4656626106 | 31.1446187906 | 994 | 504990 | -90.64 | 15.25 | 99.58 | 0.07 | 2.16 | 1575 |
| 2024-09-20 22:21:37.425 | MS1 | 121.4656625359 | 31.1446283984 | 994 | 504990 | -90.21 | 12.58 | 93.53 | 0.19 | 2.72 | 1593 |
| 2024-09-20 22:21:38.139 | MS1 | 121.4656655395 | 31.1446274935 | 994 | 504990 | -89.36 | 7.68 | 88.86 | 0.14 | 2.29 | 1564 |
| 2024-09-20 22:21:39.839 | MS1 | 121.4656631968 | 31.1446234154 | 994 | 504990 | -91.11 | 8.02 | 71.87 | 0.10 | 2.60 | 1565 |
| 2024-09-20 22:21:40.745 | MS1 | 121.4656749007 | 31.1446266979 | 994 | 504990 | -93.24 | 11.02 | 547.57 | 0.06 | 2.47 | 1588 |
| 2024-09-20 22:21:41.625 | MS1 | 121.4656656016 | 31.1446216716 | 994 | 504990 | -93.51 | 10.76 | 385.52 | 0.16 | 2.12 | 1595 |
| 2024-09-20 22:21:42.190 | MS1 | 121.4656750838 | 31.1446247042 | 994 | 504990 | -93.52 | 12.56 | 522.21 | 0.12 | 2.17 | 1568 |

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
| 3220198 | 2 | 121.4682978137 | 31.1500801096 | 237 | 4 | 9 | 20.5 | TDD | 994 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3236762 | 4 | 121.4735757245 | 31.1524638966 | 291 | 4 | 0 | 19.6 | TDD | 414 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3253735 | 3 | 121.4679503954 | 31.1518092293 | 233 | 0 | 7 | 31.9 | TDD | 869 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3274445 | 1 | 121.4744862659 | 31.1457624745 | 195 | 3 | 10 | 31.9 | TDD | 56 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.867 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.891 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.022 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.022 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.673 | NREventA3 | measId:2;ServCellPCI:808;Se... |
| 2024-09-20 22:21:37.913 | NRHandoverAttempt | SourcePCI:808;SourceNR-ARFC... |
| 2024-09-20 22:21:37.957 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.968 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.074 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.074 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3274445 | 1 | 80.1762 | 81.2845 | -116.2167 | 17.1014 | 187.5855 | 0.0101 | 0.0114 |
| 2024_09_19 22:00 | 3220198 | 2 | 91.4013 | 75.6134 | -115.0777 | 19.4061 | 102.0709 | 0.0146 | 0.0129 |
| 2024_09_19 22:00 | 3253735 | 3 | 80.8179 | 91.0043 | -114.8450 | 7.6914 | 80.9333 | 0.0118 | 0.0158 |
| 2024_09_19 22:00 | 3236762 | 4 | 83.5513 | 84.6916 | -115.4012 | 5.4127 | 199.6938 | 0.0031 | 0.0115 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417191_42DDF21F | 504990 | 994 | -89.3 | 504990 | 869 | -93.0 | 504990 | 414 | -95.7 | 504990 | 56 |
| MR_1774417191_A2BFFB18 | 504990 | 994 | -90.5 | 504990 | 869 | -91.7 | 504990 | 414 | -95.3 | 504990 | 56 |
| MR_1774417191_BBB3C4ED | 504990 | 994 | -90.2 | 504990 | 869 | -93.5 | 504990 | 414 | -96.3 | 504990 | 56 |
| MR_1774417191_FC759545 | 504990 | 994 | -88.3 | 504990 | 869 | -92.5 | 504990 | 414 | -95.7 | 504990 | 56 |
| MR_1774417191_111E3EB8 | 504990 | 994 | -90.9 | 504990 | 869 | -92.5 | 504990 | 414 | -95.2 | 504990 | 56 |
| MR_1774417191_18271735 | 504990 | 994 | -89.1 | 504990 | 869 | -95.1 | 504990 | 414 | -95.5 | 504990 | 56 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 122: `284e3fa1-c8a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `284e3fa1-c8ac-4ec0-8d92-2361bd9ac3da` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[122] topology](images/test_0122.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3275531_2
- `C2`: Lift the tilt angle  of 3269362_3 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275531_2
- `C4`: Lift the tilt angle of 3275531_2 by 10 degrees
- `C5`: Add neighbor relationship between 3217113_1 and 3269362_3
- `C6`: Press down the tilt angle  of 3269362_3 by 10 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269362_3
- `C8`: Adjust the azimuth of 3275531_2 by 50 degrees
- `C9`: Increase A3 Offset threshold for 3269362_3
- `C10`: Decrease transmission power for 3269362_3
- `C11`: Press down the tilt angle of 3275531_2 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269362_3
- `C13`: Add neighbor relationship between 3275531_2 and 3269362_3
- `C14`: Decrease A3 Offset threshold for 3269362_3
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Adjust the azimuth of 3269362_3 by 50 degrees
- `C17`: Decrease A3 Offset threshold for 3275531_2
- `C18`: Increase transmission power for 3269362_3
- `C19`: Increase transmission power for 3275531_2
- `C20`: Check test server and transmission issues
- `C21`: Increase A3 Offset threshold for 3275531_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275531_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.650 | MS1 | 121.4656580233 | 31.1446180178 | 813 | 504990 | -90.61 | 14.71 | 310.12 | 0.17 | 2.23 | 1576 |
| 2024-09-20 22:21:32.813 | MS1 | 121.4656779567 | 31.1446225036 | 813 | 504990 | -91.49 | 13.73 | 440.37 | 0.14 | 2.49 | 1567 |
| 2024-09-20 22:21:33.975 | MS1 | 121.4656719600 | 31.1446319505 | 813 | 504990 | -90.36 | 16.19 | 485.16 | 0.02 | 2.10 | 1588 |
| 2024-09-20 22:21:34.686 | MS1 | 121.4656586132 | 31.1446344292 | 813 | 504990 | -90.55 | 14.96 | 59.98 | 0.14 | 2.57 | 1575 |
| 2024-09-20 22:21:35.437 | MS1 | 121.4656635154 | 31.1446341690 | 813 | 504990 | -87.91 | 17.45 | 82.62 | 0.12 | 2.28 | 1584 |
| 2024-09-20 22:21:36.623 | MS1 | 121.4656611284 | 31.1446201990 | 813 | 504990 | -87.04 | 12.40 | 93.57 | 0.07 | 2.84 | 1596 |
| 2024-09-20 22:21:37.281 | MS1 | 121.4656719474 | 31.1446353888 | 813 | 504990 | -89.54 | 12.82 | 95.19 | 0.04 | 2.13 | 1596 |
| 2024-09-20 22:21:38.137 | MS1 | 121.4656734938 | 31.1446242833 | 813 | 504990 | -89.72 | 12.07 | 60.50 | 0.11 | 2.25 | 1598 |
| 2024-09-20 22:21:39.621 | MS1 | 121.4656593058 | 31.1446226962 | 813 | 504990 | -92.93 | 7.93 | 43.02 | 0.03 | 2.08 | 1565 |
| 2024-09-20 22:21:40.440 | MS1 | 121.4656712371 | 31.1446277518 | 813 | 504990 | -92.40 | 9.06 | 377.33 | 0.19 | 2.13 | 1560 |
| 2024-09-20 22:21:41.696 | MS1 | 121.4656664968 | 31.1446258721 | 813 | 504990 | -90.26 | 9.43 | 396.69 | 0.10 | 2.03 | 1594 |
| 2024-09-20 22:21:42.295 | MS1 | 121.4656737306 | 31.1446324036 | 813 | 504990 | -93.60 | 8.92 | 551.59 | 0.11 | 2.33 | 1567 |

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
| 3217113 | 1 | 121.4647481248 | 31.1475062536 | 154 | 12 | 0 | 40.4 | TDD | 688 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3259004 | 4 | 121.4718694085 | 31.1452607439 | 239 | 8 | 12 | 41.7 | TDD | 749 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3269362 | 3 | 121.4695453190 | 31.1442804660 | 65 | 9 | 7 | 27.8 | TDD | 12 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3275531 | 2 | 121.4729867972 | 31.1522311039 | 155 | 15 | 5 | 43.3 | TDD | 813 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.038 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.172 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.172 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.911 | NREventA3 | measId:2;ServCellPCI:177;Se... |
| 2024-09-20 22:21:38.151 | NRHandoverAttempt | SourcePCI:177;SourceNR-ARFC... |
| 2024-09-20 22:21:38.186 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.198 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.321 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.321 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3217113 | 1 | 79.0749 | 80.3234 | -114.0885 | 7.3791 | 112.7881 | 0.0054 | 0.0101 |
| 2024_09_19 22:00 | 3275531 | 2 | 82.9217 | 83.6352 | -116.0735 | 19.8883 | 107.9227 | 0.0183 | 0.0112 |
| 2024_09_19 22:00 | 3269362 | 3 | 88.5849 | 93.4077 | -117.6610 | 12.2483 | 116.5376 | 0.0164 | 0.0087 |
| 2024_09_19 22:00 | 3259004 | 4 | 83.7464 | 86.4864 | -117.3540 | 19.8083 | 123.7167 | 0.0158 | 0.0080 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413020_CCC26017 | 504990 | 813 | -89.7 | 504990 | 12 | -98.8 | 504990 | 688 | -102.3 | 504990 | 749 |
| MR_1774413020_A55FF8AF | 504990 | 813 | -92.2 | 504990 | 12 | -95.3 | 504990 | 688 | -102.8 | 504990 | 749 |
| MR_1774413020_89DF5741 | 504990 | 813 | -91.6 | 504990 | 12 | -98.4 | 504990 | 688 | -102.8 | 504990 | 749 |
| MR_1774413020_32E4BBD6 | 504990 | 813 | -92.4 | 504990 | 12 | -96.0 | 504990 | 688 | -100.2 | 504990 | 749 |
| MR_1774413020_159A2127 | 504990 | 813 | -89.3 | 504990 | 12 | -98.2 | 504990 | 688 | -100.8 | 504990 | 749 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 123: `8c5dae6f-b78...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8c5dae6f-b785-4add-92d3-fc08a0badc29` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[123] topology](images/test_0123.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3253477_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255214_4
- `C3`: Check test server and transmission issues
- `C4`: Decrease transmission power for 3255214_4
- `C5`: Increase transmission power for 3255214_4
- `C6`: Adjust the azimuth of 3253477_1 by 50 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255214_4
- `C9`: Lift the tilt angle  of 3255214_4 by 7 degrees
- `C10`: Increase A3 Offset threshold for 3253477_1
- `C11`: Press down the tilt angle of 3253477_1 by 10 degrees
- `C12`: Press down the tilt angle  of 3255214_4 by 7 degrees
- `C13`: Add neighbor relationship between 3253477_1 and 3255214_4
- `C14`: Increase A3 Offset threshold for 3255214_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253477_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253477_1
- `C17`: Lift the tilt angle of 3253477_1 by 10 degrees
- `C18`: Increase transmission power for 3253477_1
- `C19`: Adjust the azimuth of 3255214_4 by 50 degrees
- `C20`: Decrease A3 Offset threshold for 3255214_4
- `C21`: Add neighbor relationship between 3264863_3 and 3255214_4
- `C22`: Decrease A3 Offset threshold for 3253477_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.376 | MS1 | 121.4656685013 | 31.1446181360 | 704 | 504990 | -87.60 | 17.66 | 329.81 | 0.03 | 2.86 | 1561 |
| 2024-09-20 22:21:32.825 | MS1 | 121.4656760969 | 31.1446191313 | 704 | 504990 | -90.13 | 13.14 | 360.86 | 0.18 | 2.36 | 1594 |
| 2024-09-20 22:21:33.608 | MS1 | 121.4656692945 | 31.1446370875 | 704 | 504990 | -88.91 | 14.12 | 581.83 | 0.07 | 2.33 | 1594 |
| 2024-09-20 22:21:34.502 | MS1 | 121.4656623541 | 31.1446302839 | 704 | 504990 | -89.38 | 17.36 | 90.90 | 0.01 | 2.18 | 1588 |
| 2024-09-20 22:21:35.123 | MS1 | 121.4656600571 | 31.1446330769 | 704 | 504990 | -85.91 | 16.15 | 98.40 | 0.06 | 2.67 | 1594 |
| 2024-09-20 22:21:36.701 | MS1 | 121.4656613111 | 31.1446231980 | 704 | 504990 | -89.60 | 12.79 | 82.56 | 0.09 | 2.48 | 1592 |
| 2024-09-20 22:21:37.831 | MS1 | 121.4656658983 | 31.1446298925 | 704 | 504990 | -89.59 | 12.39 | 101.99 | 0.16 | 2.38 | 1570 |
| 2024-09-20 22:21:38.347 | MS1 | 121.4656742476 | 31.1446257485 | 704 | 504990 | -90.05 | 9.62 | 44.42 | 0.03 | 2.51 | 1588 |
| 2024-09-20 22:21:39.427 | MS1 | 121.4656666346 | 31.1446378654 | 704 | 504990 | -89.56 | 10.01 | 91.64 | 0.12 | 2.99 | 1578 |
| 2024-09-20 22:21:40.114 | MS1 | 121.4656713105 | 31.1446332153 | 704 | 504990 | -89.11 | 11.82 | 395.96 | 0.00 | 2.19 | 1561 |
| 2024-09-20 22:21:41.152 | MS1 | 121.4656707060 | 31.1446353864 | 704 | 504990 | -89.62 | 9.00 | 405.88 | 0.06 | 2.98 | 1564 |
| 2024-09-20 22:21:42.490 | MS1 | 121.4656684985 | 31.1446283997 | 704 | 504990 | -92.04 | 9.14 | 449.67 | 0.11 | 2.63 | 1584 |

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
| 3253477 | 1 | 121.4689423540 | 31.1444098185 | 208 | 9 | 3 | 47.7 | TDD | 704 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3255214 | 4 | 121.4759675989 | 31.1500136734 | 341 | 6 | 6 | 29.0 | TDD | 796 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3264863 | 3 | 121.4704567109 | 31.1470947697 | 327 | 12 | 7 | 36.5 | TDD | 196 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3269291 | 2 | 121.4733048318 | 31.1463227175 | 187 | 4 | 2 | 47.4 | TDD | 218 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.565 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.585 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.688 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.688 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.365 | NREventA3 | measId:2;ServCellPCI:150;Se... |
| 2024-09-20 22:21:38.605 | NRHandoverAttempt | SourcePCI:150;SourceNR-ARFC... |
| 2024-09-20 22:21:38.647 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.658 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.804 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.804 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3253477 | 1 | 91.0115 | 77.4913 | -114.9784 | 16.3475 | 193.8915 | 0.0181 | 0.0021 |
| 2024_09_19 22:00 | 3269291 | 2 | 82.8975 | 93.6421 | -117.3833 | 11.0463 | 156.3495 | 0.0071 | 0.0115 |
| 2024_09_19 22:00 | 3264863 | 3 | 83.1646 | 93.7873 | -116.1887 | 16.2770 | 190.5624 | 0.0144 | 0.0169 |
| 2024_09_19 22:00 | 3255214 | 4 | 83.3733 | 91.2982 | -116.4918 | 16.6866 | 182.1103 | 0.0121 | 0.0048 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413469_68871A52 | 504990 | 704 | -87.8 | 504990 | 796 | -92.4 | 504990 | 196 | -95.1 | 504990 | 218 |
| MR_1774413469_B1BC9C95 | 504990 | 704 | -89.8 | 504990 | 796 | -92.3 | 504990 | 196 | -94.7 | 504990 | 218 |
| MR_1774413469_D1BD5FB7 | 504990 | 704 | -87.9 | 504990 | 796 | -91.0 | 504990 | 196 | -96.3 | 504990 | 218 |
| MR_1774413469_98D6F913 | 504990 | 704 | -89.4 | 504990 | 796 | -94.3 | 504990 | 196 | -96.3 | 504990 | 218 |
| MR_1774413469_75F6F813 | 504990 | 704 | -90.3 | 504990 | 796 | -91.0 | 504990 | 196 | -95.7 | 504990 | 218 |
| MR_1774413469_F0461858 | 504990 | 704 | -90.3 | 504990 | 796 | -92.7 | 504990 | 196 | -96.6 | 504990 | 218 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 124: `7a77f811-99d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7a77f811-99d9-4ad9-97f1-4438a4162cd1` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[124] topology](images/test_0124.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3278920_3 by 50 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272006_4
- `C3`: Increase A3 Offset threshold for 3278920_3
- `C4`: Press down the tilt angle of 3272006_4 by 10 degrees
- `C5`: Add neighbor relationship between 3272006_4 and 3278920_3
- `C6`: Decrease transmission power for 3272006_4
- `C7`: Increase transmission power for 3272006_4
- `C8`: Decrease A3 Offset threshold for 3272006_4
- `C9`: Increase A3 Offset threshold for 3272006_4
- `C10`: Add neighbor relationship between 3275590_1 and 3278920_3
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease transmission power for 3278920_3
- `C13`: Adjust the azimuth of 3272006_4 by 10 degrees
- `C14`: Increase transmission power for 3278920_3
- `C15`: Decrease A3 Offset threshold for 3278920_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278920_3
- `C17`: Press down the tilt angle  of 3278920_3 by 10 degrees
- `C18`: Lift the tilt angle of 3272006_4 by 10 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278920_3
- `C20`: Check test server and transmission issues
- `C21`: Lift the tilt angle  of 3278920_3 by 10 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272006_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.576 | MS1 | 121.4656635072 | 31.1446212512 | 150 | 504990 | -85.30 | 13.01 | 521.71 | 0.13 | 2.60 | 1600 |
| 2024-09-20 22:21:32.946 | MS1 | 121.4656613109 | 31.1446263206 | 150 | 504990 | -88.80 | 14.29 | 306.50 | 0.08 | 2.58 | 1563 |
| 2024-09-20 22:21:33.594 | MS1 | 121.4656768265 | 31.1446281915 | 150 | 504990 | -88.15 | 13.06 | 493.67 | 0.16 | 2.56 | 1581 |
| 2024-09-20 22:21:34.677 | MS1 | 121.4656604998 | 31.1446216418 | 150 | 504990 | -90.68 | 14.57 | 74.64 | 0.01 | 2.20 | 1584 |
| 2024-09-20 22:21:35.548 | MS1 | 121.4656589663 | 31.1446184305 | 150 | 504990 | -91.98 | 12.14 | 74.05 | 0.11 | 2.62 | 1591 |
| 2024-09-20 22:21:36.302 | MS1 | 121.4656657162 | 31.1446301974 | 150 | 504990 | -88.21 | 13.81 | 52.36 | 0.12 | 2.24 | 1565 |
| 2024-09-20 22:21:37.483 | MS1 | 121.4656733146 | 31.1446352936 | 150 | 504990 | -92.97 | 8.89 | 78.77 | 0.07 | 2.71 | 1599 |
| 2024-09-20 22:21:38.487 | MS1 | 121.4656684309 | 31.1446354952 | 150 | 504990 | -91.32 | 12.78 | 53.83 | 0.12 | 2.08 | 1574 |
| 2024-09-20 22:21:39.360 | MS1 | 121.4656643772 | 31.1446355369 | 150 | 504990 | -91.43 | 11.12 | 78.01 | 0.07 | 2.72 | 1566 |
| 2024-09-20 22:21:40.348 | MS1 | 121.4656688259 | 31.1446362183 | 150 | 504990 | -91.46 | 7.12 | 559.34 | 0.19 | 2.54 | 1598 |
| 2024-09-20 22:21:41.765 | MS1 | 121.4656739402 | 31.1446214317 | 150 | 504990 | -93.09 | 11.16 | 455.53 | 0.04 | 2.36 | 1570 |
| 2024-09-20 22:21:42.197 | MS1 | 121.4656636850 | 31.1446376537 | 150 | 504990 | -90.60 | 10.94 | 429.38 | 0.04 | 2.05 | 1579 |

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
| 3241610 | 2 | 121.4651588526 | 31.1502126821 | 97 | 7 | 7 | 17.0 | TDD | 578 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3272006 | 4 | 121.4719026053 | 31.1469225692 | 237 | 9 | 6 | 34.4 | TDD | 150 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3275590 | 1 | 121.4696183357 | 31.1467085337 | 339 | 0 | 8 | 15.5 | TDD | 160 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3278920 | 3 | 121.4740014208 | 31.1449419196 | 166 | 11 | 2 | 19.4 | TDD | 916 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.329 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.350 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.458 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.458 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.202 | NREventA3 | measId:2;ServCellPCI:646;Se... |
| 2024-09-20 22:21:38.442 | NRHandoverAttempt | SourcePCI:646;SourceNR-ARFC... |
| 2024-09-20 22:21:38.492 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.502 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.639 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.639 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3275590 | 1 | 76.0971 | 82.3521 | -115.2274 | 5.6890 | 169.3094 | 0.0110 | 0.0064 |
| 2024_09_19 22:00 | 3241610 | 2 | 80.8313 | 88.9376 | -115.0981 | 16.8513 | 121.5703 | 0.0150 | 0.0014 |
| 2024_09_19 22:00 | 3278920 | 3 | 88.6229 | 81.0806 | -117.9358 | 13.2778 | 159.0095 | 0.0185 | 0.0168 |
| 2024_09_19 22:00 | 3272006 | 4 | 91.4200 | 80.3854 | -116.3381 | 14.4758 | 177.6933 | 0.0057 | 0.0049 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413949_8DEEBE40 | 504990 | 150 | -89.0 | 504990 | 916 | -90.5 | 504990 | 160 | -101.4 | 504990 | 578 |
| MR_1774413949_EAB26B28 | 504990 | 150 | -92.1 | 504990 | 916 | -91.3 | 504990 | 160 | -102.3 | 504990 | 578 |
| MR_1774413949_B2E8F95A | 504990 | 150 | -89.1 | 504990 | 916 | -91.9 | 504990 | 160 | -102.6 | 504990 | 578 |
| MR_1774413949_2E986AB1 | 504990 | 150 | -89.3 | 504990 | 916 | -90.3 | 504990 | 160 | -101.4 | 504990 | 578 |
| MR_1774413949_E4FBD8CC | 504990 | 150 | -89.6 | 504990 | 916 | -91.8 | 504990 | 160 | -103.0 | 504990 | 578 |
| MR_1774413949_8CDAB4A9 | 504990 | 150 | -89.4 | 504990 | 916 | -89.6 | 504990 | 160 | -103.4 | 504990 | 578 |
| MR_1774413949_E13D17B8 | 504990 | 150 | -88.7 | 504990 | 916 | -91.6 | 504990 | 160 | -102.2 | 504990 | 578 |
| MR_1774413949_372DD98C | 504990 | 150 | -90.3 | 504990 | 916 | -91.3 | 504990 | 160 | -103.1 | 504990 | 578 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 125: `182b5716-ebb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `182b5716-ebb1-4963-88f2-bcc1965a22e3` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[125] topology](images/test_0125.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3243443_1
- `C2`: Add neighbor relationship between 3243443_1 and 3220837_2
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243443_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220837_2
- `C6`: Press down the tilt angle of 3243443_1 by 2 degrees
- `C7`: Decrease A3 Offset threshold for 3220837_2
- `C8`: Increase A3 Offset threshold for 3243443_1
- `C9`: Decrease transmission power for 3220837_2
- `C10`: Press down the tilt angle  of 3220837_2 by 9 degrees
- `C11`: Lift the tilt angle of 3243443_1 by 2 degrees
- `C12`: Adjust the azimuth of 3220837_2 by 50 degrees
- `C13`: Increase A3 Offset threshold for 3220837_2
- `C14`: Check test server and transmission issues
- `C15`: Add neighbor relationship between 3262784_3 and 3220837_2
- `C16`: Lift the tilt angle  of 3220837_2 by 9 degrees
- `C17`: Decrease transmission power for 3243443_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243443_1
- `C19`: Adjust the azimuth of 3243443_1 by 35 degrees
- `C20`: Increase transmission power for 3220837_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220837_2
- `C22`: Increase transmission power for 3243443_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.331 | MS1 | 121.4656741496 | 31.1446336183 | 368 | 504990 | -90.94 | 13.50 | 500.56 | 0.02 | 2.35 | 1592 |
| 2024-09-20 22:21:32.223 | MS1 | 121.4656750869 | 31.1446350317 | 368 | 504990 | -89.21 | 17.04 | 582.67 | 0.02 | 2.45 | 1595 |
| 2024-09-20 22:21:33.276 | MS1 | 121.4656617723 | 31.1446286265 | 368 | 504990 | -91.73 | 12.46 | 551.28 | 0.08 | 2.99 | 1586 |
| 2024-09-20 22:21:34.681 | MS1 | 121.4656762987 | 31.1446372948 | 368 | 504990 | -88.63 | 15.05 | 82.20 | 0.60 | 2.59 | 667 |
| 2024-09-20 22:21:35.674 | MS1 | 121.4656768356 | 31.1446197928 | 368 | 504990 | -86.75 | 12.30 | 43.82 | 0.52 | 2.54 | 506 |
| 2024-09-20 22:21:36.210 | MS1 | 121.4656682414 | 31.1446364924 | 368 | 504990 | -87.23 | 14.30 | 71.72 | 0.55 | 2.27 | 674 |
| 2024-09-20 22:21:37.864 | MS1 | 121.4656694884 | 31.1446275403 | 368 | 504990 | -89.15 | 9.74 | 50.23 | 0.53 | 2.51 | 594 |
| 2024-09-20 22:21:38.282 | MS1 | 121.4656643218 | 31.1446233928 | 368 | 504990 | -90.73 | 7.99 | 46.71 | 0.61 | 2.53 | 576 |
| 2024-09-20 22:21:39.830 | MS1 | 121.4656655129 | 31.1446223999 | 368 | 504990 | -89.09 | 9.05 | 90.55 | 0.56 | 2.20 | 588 |
| 2024-09-20 22:21:40.294 | MS1 | 121.4656755867 | 31.1446326008 | 368 | 504990 | -90.98 | 12.63 | 515.48 | 0.13 | 2.76 | 1578 |
| 2024-09-20 22:21:41.144 | MS1 | 121.4656655497 | 31.1446345719 | 368 | 504990 | -93.80 | 8.81 | 600.89 | 0.10 | 2.90 | 1567 |
| 2024-09-20 22:21:42.469 | MS1 | 121.4656614896 | 31.1446311415 | 368 | 504990 | -90.47 | 10.51 | 335.86 | 0.17 | 2.70 | 1567 |

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
| 3220837 | 2 | 121.4738730310 | 31.1502155345 | 34 | 8 | 5 | 21.7 | TDD | 994 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3243443 | 1 | 121.4642175064 | 31.1541035966 | 207 | 0 | 7 | 33.8 | TDD | 368 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3262784 | 3 | 121.4682464222 | 31.1499629041 | 285 | 7 | 4 | 32.8 | TDD | 629 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3277557 | 4 | 121.4729929598 | 31.1508208826 | 97 | 7 | 8 | 36.4 | TDD | 384 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.385 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.401 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.524 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.524 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.265 | NREventA3 | measId:2;ServCellPCI:362;Se... |
| 2024-09-20 22:21:38.505 | NRHandoverAttempt | SourcePCI:362;SourceNR-ARFC... |
| 2024-09-20 22:21:38.538 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.550 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.650 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.650 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243443 | 1 | 7.6080 | 12.8557 | -114.8266 | 8.4802 | 129.6458 | 0.0078 | 0.0157 |
| 2024_09_20 22:00 | 3220837 | 2 | 7.3750 | 5.8601 | -117.5723 | 7.1569 | 184.0434 | 0.0010 | 0.0088 |
| 2024_09_20 22:00 | 3262784 | 3 | 14.2383 | 10.9646 | -116.8976 | 11.5283 | 169.8059 | 0.0033 | 0.0024 |
| 2024_09_20 22:00 | 3277557 | 4 | 6.9583 | 7.0509 | -114.4414 | 5.3200 | 91.3722 | 0.0081 | 0.0066 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412296_06C629D5 | 504990 | 368 | -90.6 | 504990 | 994 | -91.3 | 504990 | 629 | -98.1 | 504990 | 384 |
| MR_1774412296_6E1A1B00 | 504990 | 368 | -89.8 | 504990 | 994 | -89.9 | 504990 | 629 | -97.4 | 504990 | 384 |
| MR_1774412296_7B98FC3E | 504990 | 368 | -87.0 | 504990 | 994 | -90.8 | 504990 | 629 | -101.1 | 504990 | 384 |
| MR_1774412296_B1290CE7 | 504990 | 368 | -88.7 | 504990 | 994 | -91.0 | 504990 | 629 | -97.4 | 504990 | 384 |
| MR_1774412296_354B46BE | 504990 | 368 | -89.3 | 504990 | 994 | -89.7 | 504990 | 629 | -97.4 | 504990 | 384 |
| MR_1774412296_1031CEB8 | 504990 | 368 | -87.9 | 504990 | 994 | -91.2 | 504990 | 629 | -97.2 | 504990 | 384 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 126: `0e98afd0-e86...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0e98afd0-e867-4726-aba7-9a65f715285f` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[126] topology](images/test_0126.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3261872_2
- `C2`: Press down the tilt angle  of 3268099_1 by 10 degrees
- `C3`: Increase A3 Offset threshold for 3261872_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268099_1
- `C5`: Press down the tilt angle of 3261872_2 by 10 degrees
- `C6`: Add neighbor relationship between 3247918_3 and 3268099_1
- `C7`: Decrease transmission power for 3268099_1
- `C8`: Decrease A3 Offset threshold for 3261872_2
- `C9`: Increase A3 Offset threshold for 3268099_1
- `C10`: Increase transmission power for 3261872_2
- `C11`: Lift the tilt angle  of 3268099_1 by 10 degrees
- `C12`: Decrease A3 Offset threshold for 3268099_1
- `C13`: Increase transmission power for 3268099_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Lift the tilt angle of 3261872_2 by 10 degrees
- `C16`: Adjust the azimuth of 3268099_1 by 50 degrees
- `C17`: Check test server and transmission issues
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261872_2
- `C19`: Add neighbor relationship between 3261872_2 and 3268099_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261872_2
- `C21`: Adjust the azimuth of 3261872_2 by 5 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268099_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.699 | MS1 | 121.4656614100 | 31.1446253567 | 804 | 504990 | -80.75 | 13.92 | 525.86 | 0.10 | 2.84 | 1596 |
| 2024-09-20 22:21:32.561 | MS1 | 121.4656661520 | 31.1446196432 | 804 | 504990 | -77.26 | 13.32 | 583.85 | 0.12 | 2.99 | 1576 |
| 2024-09-20 22:21:33.942 | MS1 | 121.4656605707 | 31.1446233673 | 804 | 504990 | -84.05 | 16.91 | 358.48 | 0.07 | 2.48 | 1590 |
| 2024-09-20 22:21:34.337 | MS1 | 121.4656702195 | 31.1446286456 | 804 | 504990 | -89.96 | -3.69 | 63.95 | 0.17 | 1.08 | 1584 |
| 2024-09-20 22:21:35.172 | MS1 | 121.4656635511 | 31.1446367508 | 804 | 504990 | -83.55 | -1.47 | 67.25 | 0.11 | 1.16 | 1588 |
| 2024-09-20 22:21:36.826 | MS1 | 121.4656703076 | 31.1446368710 | 804 | 504990 | -92.31 | -0.01 | 62.13 | 0.16 | 1.37 | 1565 |
| 2024-09-20 22:21:37.233 | MS1 | 121.4656587544 | 31.1446336466 | 804 | 504990 | -83.11 | -1.18 | 61.91 | 0.03 | 1.15 | 1572 |
| 2024-09-20 22:21:38.763 | MS1 | 121.4656656671 | 31.1446185630 | 804 | 504990 | -88.56 | -2.65 | 50.06 | 0.01 | 1.01 | 1587 |
| 2024-09-20 22:21:39.649 | MS1 | 121.4656619148 | 31.1446218444 | 378 | 504990 | -76.89 | 15.88 | 224.23 | 0.12 | 1.19 | 1586 |
| 2024-09-20 22:21:40.114 | MS1 | 121.4656625380 | 31.1446358510 | 378 | 504990 | -77.61 | 13.46 | 523.43 | 0.08 | 2.92 | 1571 |
| 2024-09-20 22:21:41.816 | MS1 | 121.4656620452 | 31.1446222167 | 378 | 504990 | -80.42 | 12.85 | 346.94 | 0.06 | 2.19 | 1565 |
| 2024-09-20 22:21:42.396 | MS1 | 121.4656767775 | 31.1446214116 | 378 | 504990 | -83.15 | 13.09 | 373.99 | 0.03 | 2.94 | 1581 |

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
| 3247918 | 3 | 121.4709349897 | 31.1519040103 | 162 | 11 | 9 | 25.6 | TDD | 586 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3254839 | 4 | 121.4685063569 | 31.1523900694 | 190 | 9 | 1 | 20.5 | TDD | 631 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3261872 | 2 | 121.4642541170 | 31.1444802208 | 78 | 0 | 7 | 48.0 | TDD | 804 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3268099 | 1 | 121.4665543476 | 31.1468903638 | 71 | 13 | 7 | 41.2 | TDD | 378 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.582 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.600 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.738 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.738 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.427 | NREventA3 | measId:2;ServCellPCI:658;Se... |
| 2024-09-20 22:21:38.667 | NRHandoverAttempt | SourcePCI:658;SourceNR-ARFC... |
| 2024-09-20 22:21:38.712 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.725 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.838 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.838 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268099 | 1 | 6.5886 | 6.7020 | -117.0702 | 13.5583 | 83.5272 | 0.0167 | 0.0035 |
| 2024_09_20 22:00 | 3261872 | 2 | 12.2659 | 13.5675 | -115.1290 | 7.5501 | 153.6315 | 0.0107 | 0.1244 |
| 2024_09_20 22:00 | 3247918 | 3 | 11.1486 | 15.3390 | -115.0431 | 6.7530 | 175.1841 | 0.0059 | 0.0159 |
| 2024_09_20 22:00 | 3254839 | 4 | 15.7579 | 12.0727 | -115.0676 | 5.3732 | 166.7897 | 0.0155 | 0.0108 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414504_2EFB1E11 | 504990 | 378 | -84.0 | 504990 | 804 | -89.5 | 504990 | 586 | -86.4 | 504990 | 631 |
| MR_1774414504_4F9BFCAE | 504990 | 804 | -90.2 | 504990 | 378 | -86.5 | 504990 | 586 | -86.8 | 504990 | 631 |
| MR_1774414504_9B813BBA | 504990 | 378 | -86.1 | 504990 | 804 | -89.5 | 504990 | 586 | -88.2 | 504990 | 631 |
| MR_1774414504_D2B775BB | 504990 | 378 | -84.9 | 504990 | 804 | -89.3 | 504990 | 586 | -87.7 | 504990 | 631 |
| MR_1774414504_84EF4CCA | 504990 | 378 | -86.0 | 504990 | 804 | -91.1 | 504990 | 586 | -87.7 | 504990 | 631 |
| MR_1774414504_DAF137E1 | 504990 | 378 | -86.3 | 504990 | 804 | -88.3 | 504990 | 586 | -87.8 | 504990 | 631 |
| MR_1774414504_6E52A9D9 | 504990 | 378 | -86.3 | 504990 | 804 | -91.2 | 504990 | 586 | -86.9 | 504990 | 631 |
| MR_1774414504_4AD1CCDF | 504990 | 804 | -89.3 | 504990 | 378 | -85.3 | 504990 | 586 | -89.1 | 504990 | 631 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 127: `9fe58e8a-2f9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9fe58e8a-2f92-443c-8999-ec304588f46d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[127] topology](images/test_0127.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3270946_1 by 6 degrees
- `C2`: Add neighbor relationship between 3278847_2 and 3266038_3
- `C3`: Decrease transmission power for 3270946_1
- `C4`: Decrease transmission power for 3266038_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266038_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270946_1
- `C7`: Increase A3 Offset threshold for 3266038_3
- `C8`: Decrease A3 Offset threshold for 3266038_3
- `C9`: Lift the tilt angle  of 3266038_3 by 10 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270946_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase transmission power for 3266038_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266038_3
- `C14`: Increase A3 Offset threshold for 3270946_1
- `C15`: Adjust the azimuth of 3266038_3 by 50 degrees
- `C16`: Check test server and transmission issues
- `C17`: Decrease A3 Offset threshold for 3270946_1
- `C18`: Press down the tilt angle  of 3266038_3 by 10 degrees
- `C19`: Increase transmission power for 3270946_1
- `C20`: Lift the tilt angle of 3270946_1 by 2 degrees
- `C21`: Press down the tilt angle of 3270946_1 by 2 degrees
- `C22`: Add neighbor relationship between 3270946_1 and 3266038_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.678 | MS1 | 121.4656754318 | 31.1446361882 | 761 | 504990 | -87.77 | 14.93 | 332.35 | 0.19 | 2.75 | 1587 |
| 2024-09-20 22:21:32.515 | MS1 | 121.4656580069 | 31.1446263226 | 761 | 504990 | -86.82 | 14.96 | 551.97 | 0.10 | 2.96 | 1564 |
| 2024-09-20 22:21:33.261 | MS1 | 121.4656727199 | 31.1446215342 | 761 | 504990 | -90.22 | 17.42 | 560.84 | 0.16 | 2.47 | 1578 |
| 2024-09-20 22:21:34.521 | MS1 | 121.4656712993 | 31.1446271871 | 761 | 504990 | -86.21 | 17.31 | 79.09 | 0.56 | 2.53 | 536 |
| 2024-09-20 22:21:35.302 | MS1 | 121.4656629687 | 31.1446305607 | 761 | 504990 | -85.01 | 16.91 | 62.81 | 0.58 | 2.63 | 615 |
| 2024-09-20 22:21:36.904 | MS1 | 121.4656655317 | 31.1446249235 | 761 | 504990 | -88.95 | 14.13 | 62.01 | 0.50 | 2.95 | 574 |
| 2024-09-20 22:21:37.908 | MS1 | 121.4656635368 | 31.1446216632 | 761 | 504990 | -90.66 | 9.79 | 81.61 | 0.51 | 2.11 | 532 |
| 2024-09-20 22:21:38.187 | MS1 | 121.4656676408 | 31.1446221320 | 761 | 504990 | -92.35 | 12.44 | 92.87 | 0.53 | 2.65 | 606 |
| 2024-09-20 22:21:39.441 | MS1 | 121.4656699949 | 31.1446340798 | 761 | 504990 | -90.68 | 7.50 | 92.35 | 0.58 | 2.81 | 609 |
| 2024-09-20 22:21:40.893 | MS1 | 121.4656776708 | 31.1446347788 | 761 | 504990 | -89.65 | 8.03 | 464.51 | 0.16 | 2.14 | 1579 |
| 2024-09-20 22:21:41.596 | MS1 | 121.4656584998 | 31.1446365575 | 761 | 504990 | -90.37 | 7.10 | 543.32 | 0.04 | 2.03 | 1569 |
| 2024-09-20 22:21:42.401 | MS1 | 121.4656664894 | 31.1446239710 | 761 | 504990 | -93.33 | 8.37 | 409.62 | 0.14 | 2.03 | 1588 |

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
| 3223499 | 4 | 121.4671173789 | 31.1554614941 | 44 | 5 | 9 | 16.8 | TDD | 335 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3266038 | 3 | 121.4662846277 | 31.1520027133 | 85 | 14 | 4 | 44.0 | TDD | 343 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3270946 | 1 | 121.4716035979 | 31.1490075821 | 223 | 0 | 10 | 20.3 | TDD | 761 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3278847 | 2 | 121.4735561161 | 31.1457715621 | 28 | 3 | 8 | 19.2 | TDD | 444 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.491 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.506 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.638 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.638 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.323 | NREventA3 | measId:2;ServCellPCI:455;Se... |
| 2024-09-20 22:21:38.563 | NRHandoverAttempt | SourcePCI:455;SourceNR-ARFC... |
| 2024-09-20 22:21:38.595 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.607 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.757 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.757 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270946 | 1 | 8.2209 | 6.7535 | -117.9900 | 8.5867 | 147.3101 | 0.0035 | 0.0159 |
| 2024_09_20 22:00 | 3278847 | 2 | 17.0623 | 17.3475 | -115.0971 | 7.1775 | 199.1909 | 0.0098 | 0.0056 |
| 2024_09_20 22:00 | 3266038 | 3 | 16.0515 | 17.1393 | -115.3492 | 10.5979 | 187.7361 | 0.0194 | 0.0108 |
| 2024_09_20 22:00 | 3223499 | 4 | 5.5217 | 16.7931 | -116.1224 | 15.5777 | 128.7670 | 0.0135 | 0.0122 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414291_8D566C9F | 504990 | 761 | -85.8 | 504990 | 343 | -92.8 | 504990 | 444 | -94.2 | 504990 | 335 |
| MR_1774414291_C88F6E60 | 504990 | 761 | -85.9 | 504990 | 343 | -91.9 | 504990 | 444 | -93.3 | 504990 | 335 |
| MR_1774414291_C9E80520 | 504990 | 761 | -87.6 | 504990 | 343 | -93.0 | 504990 | 444 | -94.4 | 504990 | 335 |
| MR_1774414291_E120D2EF | 504990 | 761 | -86.9 | 504990 | 343 | -90.5 | 504990 | 444 | -94.2 | 504990 | 335 |
| MR_1774414291_25D62EFB | 504990 | 761 | -86.0 | 504990 | 343 | -91.2 | 504990 | 444 | -93.3 | 504990 | 335 |
| MR_1774414291_A48EC9BD | 504990 | 761 | -84.5 | 504990 | 343 | -92.6 | 504990 | 444 | -90.9 | 504990 | 335 |
| MR_1774414291_2545B75F | 504990 | 761 | -87.0 | 504990 | 343 | -92.7 | 504990 | 444 | -91.6 | 504990 | 335 |
| MR_1774414291_86F070A0 | 504990 | 761 | -84.4 | 504990 | 343 | -90.6 | 504990 | 444 | -91.6 | 504990 | 335 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 128: `68eac603-caa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `68eac603-caac-4c9f-843d-fe1773039a6c` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[128] topology](images/test_0128.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231384_1
- `C2`: Decrease transmission power for 3227289_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227289_4
- `C4`: Add neighbor relationship between 3231384_1 and 3227289_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227289_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Check test server and transmission issues
- `C8`: Increase A3 Offset threshold for 3231384_1
- `C9`: Lift the tilt angle of 3231384_1 by 4 degrees
- `C10`: Increase A3 Offset threshold for 3227289_4
- `C11`: Decrease A3 Offset threshold for 3231384_1
- `C12`: Adjust the azimuth of 3274893_3 by 50 degrees
- `C13`: Adjust the azimuth of 3231384_1 by 21 degrees
- `C14`: Press down the tilt angle of 3231384_1 by 4 degrees
- `C15`: Add neighbor relationship between 3274893_3 and 3227289_4
- `C16`: Decrease A3 Offset threshold for 3227289_4
- `C17`: Increase transmission power for 3227289_4
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231384_1
- `C19`: Increase transmission power for 3231384_1
- `C20`: Press down the tilt angle  of 3274893_3 by 10 degrees
- `C21`: Lift the tilt angle  of 3274893_3 by 10 degrees
- `C22`: Decrease transmission power for 3231384_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.297 | MS1 | 121.4656665085 | 31.1446214079 | 960 | 504990 | -88.24 | 17.63 | 441.53 | 0.14 | 2.49 | 1599 |
| 2024-09-20 22:21:32.599 | MS1 | 121.4656677324 | 31.1446302460 | 960 | 504990 | -87.59 | 16.87 | 503.09 | 0.18 | 2.68 | 1595 |
| 2024-09-20 22:21:33.696 | MS1 | 121.4656724296 | 31.1446228349 | 960 | 504990 | -89.01 | 17.01 | 438.17 | 0.01 | 2.31 | 1579 |
| 2024-09-20 22:21:34.651 | MS1 | 121.4656591591 | 31.1446306736 | 960 | 504990 | -88.34 | 12.61 | 47.56 | 0.05 | 2.64 | 1600 |
| 2024-09-20 22:21:35.203 | MS1 | 121.4656750537 | 31.1446249877 | 960 | 504990 | -87.50 | 15.32 | 57.46 | 0.08 | 2.73 | 1578 |
| 2024-09-20 22:21:36.209 | MS1 | 121.4656590013 | 31.1446342730 | 960 | 504990 | -88.40 | 12.33 | 88.31 | 0.11 | 2.14 | 1579 |
| 2024-09-20 22:21:37.615 | MS1 | 121.4656651280 | 31.1446297946 | 960 | 504990 | -91.20 | 7.21 | 65.80 | 0.09 | 2.99 | 1572 |
| 2024-09-20 22:21:38.564 | MS1 | 121.4656723517 | 31.1446290047 | 960 | 504990 | -89.24 | 9.34 | 102.26 | 0.17 | 2.94 | 1567 |
| 2024-09-20 22:21:39.200 | MS1 | 121.4656773627 | 31.1446249421 | 960 | 504990 | -89.47 | 12.15 | 76.28 | 0.00 | 2.06 | 1590 |
| 2024-09-20 22:21:40.568 | MS1 | 121.4656674438 | 31.1446369316 | 960 | 504990 | -93.60 | 11.16 | 401.98 | 0.13 | 2.62 | 1586 |
| 2024-09-20 22:21:41.619 | MS1 | 121.4656583850 | 31.1446204867 | 960 | 504990 | -92.38 | 9.89 | 364.18 | 0.16 | 2.08 | 1581 |
| 2024-09-20 22:21:42.891 | MS1 | 121.4656647869 | 31.1446352509 | 960 | 504990 | -89.20 | 12.99 | 497.39 | 0.10 | 2.06 | 1582 |

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
| 3227289 | 4 | 121.4703194100 | 31.1524569702 | 156 | 14 | 8 | 31.6 | TDD | 767 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3231384 | 1 | 121.4663473422 | 31.1482794984 | 168 | 2 | 1 | 17.9 | TDD | 960 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3268764 | 2 | 121.4660116070 | 31.1550044171 | 216 | 11 | 2 | 36.3 | TDD | 857 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3274893 | 3 | 121.4675280315 | 31.1478946377 | 20 | 5 | 10 | 49.2 | TDD | 147 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.246 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.268 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.383 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.383 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.094 | NREventA3 | measId:2;ServCellPCI:300;Se... |
| 2024-09-20 22:21:38.334 | NRHandoverAttempt | SourcePCI:300;SourceNR-ARFC... |
| 2024-09-20 22:21:38.372 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.387 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.506 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.506 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231384 | 1 | 76.7103 | 77.4772 | -116.4193 | 7.8047 | 87.7172 | 0.0192 | 0.0144 |
| 2024_09_20 22:00 | 3268764 | 2 | 7.1533 | 14.7517 | -115.6822 | 8.0569 | 137.5693 | 0.0168 | 0.0127 |
| 2024_09_20 22:00 | 3274893 | 3 | 17.7708 | 6.0010 | -114.3526 | 15.1757 | 178.9932 | 0.0042 | 0.0037 |
| 2024_09_20 22:00 | 3227289 | 4 | 7.2343 | 15.8136 | -116.4197 | 16.7535 | 97.1500 | 0.0185 | 0.0115 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413968_75918A47 | 504990 | 960 | -89.5 | 504990 | 767 | -88.5 | 504990 | 147 | -101.7 | 504990 | 857 |
| MR_1774413968_BBA45DFA | 504990 | 960 | -88.8 | 504990 | 767 | -87.1 | 504990 | 147 | -99.8 | 504990 | 857 |
| MR_1774413968_E3162A18 | 504990 | 960 | -88.9 | 504990 | 767 | -89.0 | 504990 | 147 | -100.0 | 504990 | 857 |
| MR_1774413968_2B6782E6 | 504990 | 960 | -88.5 | 504990 | 767 | -89.3 | 504990 | 147 | -100.7 | 504990 | 857 |
| MR_1774413968_F72E7844 | 504990 | 960 | -87.5 | 504990 | 767 | -89.0 | 504990 | 147 | -101.0 | 504990 | 857 |
| MR_1774413968_DE4E7979 | 504990 | 960 | -90.3 | 504990 | 767 | -90.2 | 504990 | 147 | -99.9 | 504990 | 857 |
| MR_1774413968_105EBF59 | 504990 | 960 | -89.3 | 504990 | 767 | -90.0 | 504990 | 147 | -101.9 | 504990 | 857 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 129: `7874bc60-b5f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7874bc60-b5f8-41e4-b7c2-399085a1928d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[129] topology](images/test_0129.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3261966_4 and 3271860_2
- `C2`: Increase transmission power for 3271860_2
- `C3`: Press down the tilt angle of 3261966_4 by 9 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271860_2
- `C5`: Adjust the azimuth of 3271860_2 by 50 degrees
- `C6`: Decrease A3 Offset threshold for 3271860_2
- `C7`: Decrease transmission power for 3271860_2
- `C8`: Lift the tilt angle  of 3271860_2 by 10 degrees
- `C9`: Increase A3 Offset threshold for 3261966_4
- `C10`: Decrease A3 Offset threshold for 3261966_4
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261966_4
- `C13`: Increase transmission power for 3261966_4
- `C14`: Increase A3 Offset threshold for 3271860_2
- `C15`: Lift the tilt angle of 3261966_4 by 9 degrees
- `C16`: Decrease transmission power for 3261966_4
- `C17`: Adjust the azimuth of 3261966_4 by 50 degrees
- `C18`: Press down the tilt angle  of 3271860_2 by 10 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261966_4
- `C20`: Check test server and transmission issues
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271860_2
- `C22`: Add neighbor relationship between 3216254_3 and 3271860_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.264 | MS1 | 121.4656707528 | 31.1446360232 | 223 | 504990 | -78.10 | 12.62 | 557.25 | 0.12 | 2.04 | 1561 |
| 2024-09-20 22:21:32.829 | MS1 | 121.4656725807 | 31.1446293213 | 223 | 504990 | -79.39 | 14.46 | 358.70 | 0.08 | 2.84 | 1578 |
| 2024-09-20 22:21:33.987 | MS1 | 121.4656760147 | 31.1446302564 | 223 | 504990 | -81.86 | 13.18 | 465.32 | 0.09 | 2.21 | 1573 |
| 2024-09-20 22:21:34.190 | MS1 | 121.4656771067 | 31.1446191823 | 223 | 504990 | -84.37 | -3.25 | 59.24 | 0.15 | 1.30 | 1573 |
| 2024-09-20 22:21:35.166 | MS1 | 121.4656615477 | 31.1446316262 | 223 | 504990 | -83.72 | -2.02 | 60.22 | 0.10 | 1.19 | 1599 |
| 2024-09-20 22:21:36.948 | MS1 | 121.4656722238 | 31.1446351946 | 223 | 504990 | -84.89 | -2.29 | 48.65 | 0.03 | 1.02 | 1599 |
| 2024-09-20 22:21:37.844 | MS1 | 121.4656712850 | 31.1446183791 | 223 | 504990 | -87.66 | -1.79 | 66.12 | 0.18 | 1.09 | 1598 |
| 2024-09-20 22:21:38.179 | MS1 | 121.4656676146 | 31.1446379766 | 223 | 504990 | -85.32 | -2.01 | 65.89 | 0.14 | 1.19 | 1586 |
| 2024-09-20 22:21:39.762 | MS1 | 121.4656600738 | 31.1446274192 | 20 | 504990 | -77.88 | 14.23 | 209.20 | 0.14 | 1.08 | 1560 |
| 2024-09-20 22:21:40.913 | MS1 | 121.4656778458 | 31.1446180201 | 20 | 504990 | -83.68 | 13.88 | 386.63 | 0.04 | 2.96 | 1599 |
| 2024-09-20 22:21:41.623 | MS1 | 121.4656698046 | 31.1446255629 | 20 | 504990 | -76.64 | 13.14 | 372.81 | 0.02 | 2.64 | 1585 |
| 2024-09-20 22:21:42.313 | MS1 | 121.4656718757 | 31.1446325998 | 20 | 504990 | -81.57 | 16.12 | 415.11 | 0.07 | 2.31 | 1576 |

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
| 3216254 | 3 | 121.4758210205 | 31.1447550077 | 173 | 7 | 6 | 47.8 | TDD | 302 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3232844 | 1 | 121.4641260975 | 31.1514765525 | 123 | 6 | 4 | 44.3 | TDD | 168 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3261966 | 4 | 121.4685256565 | 31.1477311062 | 294 | 6 | 2 | 25.7 | TDD | 223 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3271860 | 2 | 121.4681645943 | 31.1557319807 | 253 | 10 | 2 | 47.7 | TDD | 20 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.724 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.740 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:30.861 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.861 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.601 | NREventA3 | measId:2;ServCellPCI:917;Se... |
| 2024-09-20 22:21:37.841 | NRHandoverAttempt | SourcePCI:917;SourceNR-ARFC... |
| 2024-09-20 22:21:37.883 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.897 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.022 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.022 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232844 | 1 | 19.0423 | 9.2319 | -114.7422 | 6.3739 | 105.9372 | 0.0017 | 0.0139 |
| 2024_09_20 22:00 | 3271860 | 2 | 12.8031 | 15.0639 | -117.5244 | 7.6460 | 177.6061 | 0.0012 | 0.0194 |
| 2024_09_20 22:00 | 3216254 | 3 | 13.8784 | 16.1207 | -117.0152 | 18.8095 | 153.8476 | 0.0113 | 0.0140 |
| 2024_09_20 22:00 | 3261966 | 4 | 6.1408 | 10.1755 | -114.5473 | 7.4443 | 186.5108 | 0.0013 | 0.1907 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412043_DBB4A96E | 504990 | 20 | -80.1 | 504990 | 223 | -84.0 | 504990 | 302 | -88.9 | 504990 | 168 |
| MR_1774412043_098AE7AB | 504990 | 223 | -82.4 | 504990 | 20 | -80.3 | 504990 | 302 | -87.7 | 504990 | 168 |
| MR_1774412043_4139B4B9 | 504990 | 223 | -85.6 | 504990 | 20 | -81.1 | 504990 | 302 | -87.6 | 504990 | 168 |
| MR_1774412043_23978E61 | 504990 | 20 | -79.3 | 504990 | 223 | -84.7 | 504990 | 302 | -89.8 | 504990 | 168 |
| MR_1774412043_40644A61 | 504990 | 223 | -85.0 | 504990 | 20 | -81.3 | 504990 | 302 | -90.7 | 504990 | 168 |
| MR_1774412043_8BBE09A8 | 504990 | 223 | -85.8 | 504990 | 20 | -77.8 | 504990 | 302 | -87.4 | 504990 | 168 |
| MR_1774412043_A7D76DE0 | 504990 | 223 | -83.8 | 504990 | 20 | -81.1 | 504990 | 302 | -90.3 | 504990 | 168 |

> *... 2개 열 생략 (전체 14열)*

---
