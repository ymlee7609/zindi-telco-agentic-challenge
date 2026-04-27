# Track A 문제 분석 — test[160]~test[169]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[160] ~ test[169] (10개)

## 목차

1. [문제 160: `04e89b3f-524...`](#160) — single-answer
2. [문제 161: `5efdae65-ef2...`](#161) — single-answer
3. [문제 162: `da5a2248-211...`](#162) — single-answer
4. [문제 163: `4d0e7959-428...`](#163) — multiple-answer
5. [문제 164: `7bd2f82c-87a...`](#164) — single-answer
6. [문제 165: `d8c4075c-440...`](#165) — single-answer
7. [문제 166: `1d613485-cd0...`](#166) — single-answer
8. [문제 167: `eb89c6c7-989...`](#167) — single-answer
9. [문제 168: `c0916fcc-a50...`](#168) — single-answer
10. [문제 169: `e39bdd6a-e8b...`](#169) — single-answer

---

### 문제 160: `04e89b3f-524...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `04e89b3f-524e-44a0-b590-d9c958b63085` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[160] topology](images/test_0160.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3211441_4 and 3255245_2
- `C2`: Press down the tilt angle of 3225624_1 by 4 degrees
- `C3`: Lift the tilt angle  of 3255245_2 by 9 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Increase transmission power for 3255245_2
- `C6`: Check test server and transmission issues
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255245_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225624_1
- `C9`: Lift the tilt angle of 3225624_1 by 4 degrees
- `C10`: Press down the tilt angle  of 3255245_2 by 9 degrees
- `C11`: Add neighbor relationship between 3225624_1 and 3255245_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225624_1
- `C13`: Increase transmission power for 3225624_1
- `C14`: Adjust the azimuth of 3225624_1 by 11 degrees
- `C15`: Decrease A3 Offset threshold for 3255245_2
- `C16`: Decrease transmission power for 3255245_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255245_2
- `C18`: Decrease A3 Offset threshold for 3225624_1
- `C19`: Increase A3 Offset threshold for 3225624_1
- `C20`: Adjust the azimuth of 3255245_2 by 50 degrees
- `C21`: Decrease transmission power for 3225624_1
- `C22`: Increase A3 Offset threshold for 3255245_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.287 | MS1 | 121.4656673854 | 31.1446204514 | 508 | 504990 | -89.85 | 13.80 | 374.89 | 0.16 | 2.38 | 1562 |
| 2024-09-20 22:21:32.241 | MS1 | 121.4656639927 | 31.1446375492 | 508 | 504990 | -88.89 | 13.58 | 369.97 | 0.10 | 2.51 | 1575 |
| 2024-09-20 22:21:33.245 | MS1 | 121.4656612850 | 31.1446367194 | 508 | 504990 | -86.47 | 16.50 | 493.98 | 0.02 | 2.18 | 1578 |
| 2024-09-20 22:21:34.163 | MS1 | 121.4656729712 | 31.1446300728 | 508 | 504990 | -89.22 | 16.84 | 100.39 | 0.01 | 2.13 | 441 |
| 2024-09-20 22:21:35.106 | MS1 | 121.4656685784 | 31.1446183924 | 508 | 504990 | -88.10 | 16.02 | 79.65 | 0.03 | 2.94 | 374 |
| 2024-09-20 22:21:36.208 | MS1 | 121.4656747460 | 31.1446249412 | 508 | 504990 | -88.14 | 14.47 | 79.84 | 0.03 | 2.67 | 471 |
| 2024-09-20 22:21:37.905 | MS1 | 121.4656703784 | 31.1446299230 | 508 | 504990 | -89.48 | 7.90 | 66.26 | 0.05 | 2.98 | 419 |
| 2024-09-20 22:21:38.645 | MS1 | 121.4656629006 | 31.1446194673 | 508 | 504990 | -90.79 | 11.77 | 87.89 | 0.18 | 2.12 | 373 |
| 2024-09-20 22:21:39.343 | MS1 | 121.4656629034 | 31.1446367561 | 508 | 504990 | -90.05 | 12.94 | 58.52 | 0.17 | 2.95 | 355 |
| 2024-09-20 22:21:40.258 | MS1 | 121.4656633369 | 31.1446280872 | 508 | 504990 | -89.27 | 11.28 | 426.83 | 0.18 | 2.90 | 1587 |
| 2024-09-20 22:21:41.788 | MS1 | 121.4656694654 | 31.1446304341 | 508 | 504990 | -92.05 | 8.43 | 436.65 | 0.10 | 2.05 | 1566 |
| 2024-09-20 22:21:42.133 | MS1 | 121.4656712922 | 31.1446313124 | 508 | 504990 | -89.20 | 12.00 | 401.51 | 0.10 | 2.78 | 1587 |

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
| 3211441 | 4 | 121.4707847731 | 31.1495700466 | 141 | 6 | 4 | 48.3 | TDD | 87 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3225624 | 1 | 121.4751800174 | 31.1446839875 | 259 | 1 | 3 | 49.6 | TDD | 508 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3255245 | 2 | 121.4668019344 | 31.1516440745 | 291 | 7 | 11 | 23.1 | TDD | 95 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3274103 | 3 | 121.4745439170 | 31.1488477153 | 70 | 13 | 12 | 48.6 | TDD | 300 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.485 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.503 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.641 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.641 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.338 | NREventA3 | measId:2;ServCellPCI:56;Ser... |
| 2024-09-20 22:21:38.578 | NRHandoverAttempt | SourcePCI:56;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.616 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.627 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.772 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.772 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225624 | 1 | 19.2947 | 11.1558 | -116.2858 | 12.1730 | 93.5054 | 0.0077 | 0.0156 |
| 2024_09_20 22:00 | 3255245 | 2 | 12.4552 | 19.4283 | -115.1772 | 11.0570 | 87.3039 | 0.0112 | 0.0196 |
| 2024_09_20 22:00 | 3274103 | 3 | 9.8360 | 17.6514 | -115.8552 | 19.0552 | 123.6074 | 0.0138 | 0.0142 |
| 2024_09_20 22:00 | 3211441 | 4 | 15.4231 | 8.9173 | -117.8678 | 5.6163 | 144.0018 | 0.0093 | 0.0131 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414415_AA358538 | 504990 | 508 | -89.2 | 504990 | 95 | -86.8 | 504990 | 87 | -101.8 | 504990 | 300 |
| MR_1774414415_31A26D44 | 504990 | 508 | -89.6 | 504990 | 95 | -87.1 | 504990 | 87 | -103.2 | 504990 | 300 |
| MR_1774414415_5E6D8229 | 504990 | 508 | -88.3 | 504990 | 95 | -89.3 | 504990 | 87 | -101.7 | 504990 | 300 |
| MR_1774414415_F1C8EADE | 504990 | 508 | -86.5 | 504990 | 95 | -87.6 | 504990 | 87 | -102.0 | 504990 | 300 |
| MR_1774414415_6F371418 | 504990 | 508 | -87.9 | 504990 | 95 | -88.9 | 504990 | 87 | -103.7 | 504990 | 300 |
| MR_1774414415_A42583D9 | 504990 | 508 | -88.9 | 504990 | 95 | -89.4 | 504990 | 87 | -100.6 | 504990 | 300 |
| MR_1774414415_54A83D42 | 504990 | 508 | -88.9 | 504990 | 95 | -89.8 | 504990 | 87 | -102.4 | 504990 | 300 |
| MR_1774414415_DBEA8E7E | 504990 | 508 | -88.1 | 504990 | 95 | -89.0 | 504990 | 87 | -101.2 | 504990 | 300 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 161: `5efdae65-ef2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5efdae65-ef21-4d82-9633-b0a39e2d2c0a` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[161] topology](images/test_0161.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214145_1
- `C2`: Decrease A3 Offset threshold for 3211351_3
- `C3`: Decrease transmission power for 3211351_3
- `C4`: Lift the tilt angle  of 3211351_3 by 3 degrees
- `C5`: Increase A3 Offset threshold for 3211351_3
- `C6`: Increase transmission power for 3214145_1
- `C7`: Add neighbor relationship between 3214145_1 and 3211351_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214145_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Press down the tilt angle  of 3211351_3 by 3 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211351_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211351_3
- `C13`: Adjust the azimuth of 3214145_1 by 50 degrees
- `C14`: Decrease transmission power for 3214145_1
- `C15`: Decrease A3 Offset threshold for 3214145_1
- `C16`: Add neighbor relationship between 3214919_4 and 3211351_3
- `C17`: Check test server and transmission issues
- `C18`: Lift the tilt angle of 3214145_1 by 10 degrees
- `C19`: Increase transmission power for 3211351_3
- `C20`: Adjust the azimuth of 3211351_3 by 17 degrees
- `C21`: Press down the tilt angle of 3214145_1 by 10 degrees
- `C22`: Increase A3 Offset threshold for 3214145_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.245 | MS1 | 121.4656656405 | 31.1446297493 | 417 | 504990 | -78.76 | 12.08 | 435.55 | 0.12 | 2.28 | 1563 |
| 2024-09-20 22:21:32.782 | MS1 | 121.4656758433 | 31.1446297107 | 417 | 504990 | -78.68 | 17.63 | 557.67 | 0.18 | 2.96 | 1595 |
| 2024-09-20 22:21:33.550 | MS1 | 121.4656583072 | 31.1446240959 | 417 | 504990 | -75.98 | 16.27 | 540.08 | 0.06 | 2.68 | 1596 |
| 2024-09-20 22:21:34.936 | MS1 | 121.4656683674 | 31.1446336756 | 417 | 504990 | -89.66 | -1.91 | 56.36 | 0.18 | 1.44 | 1598 |
| 2024-09-20 22:21:35.806 | MS1 | 121.4656636971 | 31.1446377820 | 417 | 504990 | -91.98 | -0.77 | 62.45 | 0.15 | 1.10 | 1583 |
| 2024-09-20 22:21:36.468 | MS1 | 121.4656723855 | 31.1446364964 | 417 | 504990 | -89.29 | -3.55 | 55.16 | 0.04 | 1.22 | 1595 |
| 2024-09-20 22:21:37.645 | MS1 | 121.4656755721 | 31.1446280417 | 417 | 504990 | -88.62 | -3.57 | 77.37 | 0.17 | 1.26 | 1575 |
| 2024-09-20 22:21:38.712 | MS1 | 121.4656654628 | 31.1446328543 | 417 | 504990 | -82.69 | 15.23 | 447.98 | 0.13 | 1.37 | 1568 |
| 2024-09-20 22:21:39.681 | MS1 | 121.4656631256 | 31.1446298838 | 417 | 504990 | -76.11 | 15.76 | 488.48 | 0.01 | 1.19 | 1566 |
| 2024-09-20 22:21:40.594 | MS1 | 121.4656762895 | 31.1446327429 | 417 | 504990 | -83.89 | 16.04 | 337.42 | 0.19 | 2.43 | 1573 |
| 2024-09-20 22:21:41.969 | MS1 | 121.4656771832 | 31.1446184367 | 417 | 504990 | -81.70 | 16.60 | 494.78 | 0.11 | 2.38 | 1571 |
| 2024-09-20 22:21:42.124 | MS1 | 121.4656671140 | 31.1446327020 | 417 | 504990 | -79.04 | 13.61 | 455.60 | 0.13 | 2.16 | 1590 |

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
| 3211351 | 3 | 121.4758521049 | 31.1517083346 | 248 | 1 | 5 | 33.9 | TDD | 439 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3214145 | 1 | 121.4643666753 | 31.1486275536 | 338 | 11 | 9 | 18.4 | TDD | 417 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3214919 | 4 | 121.4678836037 | 31.1456649126 | 50 | 13 | 4 | 23.1 | TDD | 711 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3223449 | 2 | 121.4652572009 | 31.1487734453 | 136 | 14 | 6 | 28.2 | TDD | 823 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.377 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.401 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.526 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.526 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.211 | NREventA3 | measId:2;ServCellPCI:652;Se... |
| 2024-09-20 22:21:36.211 | NREventA3 | measId:2;ServCellPCI:652;Se... |
| 2024-09-20 22:21:37.211 | NREventA3 | measId:2;ServCellPCI:652;Se... |
| 2024-09-20 22:21:39.711 | NRRRCReestablishAttempt | PCI:652 |
| 2024-09-20 22:21:39.722 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.736 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.873 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.873 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214145 | 1 | 14.7645 | 15.7383 | -114.3334 | 14.1007 | 194.5158 | 0.0081 | 0.1851 |
| 2024_09_20 22:00 | 3223449 | 2 | 9.2842 | 8.6392 | -114.3832 | 15.4886 | 165.1706 | 0.0185 | 0.0152 |
| 2024_09_20 22:00 | 3211351 | 3 | 8.1518 | 5.8475 | -114.7940 | 17.4391 | 186.6901 | 0.0066 | 0.0189 |
| 2024_09_20 22:00 | 3214919 | 4 | 17.5479 | 5.6718 | -116.0049 | 11.4300 | 138.8456 | 0.0082 | 0.0161 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416168_D46AE896 | 504990 | 439 | -85.8 | 504990 | 417 | -89.8 | 504990 | 711 | -91.6 | 504990 | 823 |
| MR_1774416168_AF58D155 | 504990 | 439 | -86.0 | 504990 | 417 | -89.4 | 504990 | 711 | -91.9 | 504990 | 823 |
| MR_1774416168_2753AE80 | 504990 | 417 | -87.9 | 504990 | 439 | -84.1 | 504990 | 711 | -91.6 | 504990 | 823 |
| MR_1774416168_79DAAEA8 | 504990 | 439 | -85.8 | 504990 | 417 | -91.1 | 504990 | 711 | -92.9 | 504990 | 823 |
| MR_1774416168_FD923C05 | 504990 | 439 | -86.1 | 504990 | 417 | -90.3 | 504990 | 711 | -91.2 | 504990 | 823 |
| MR_1774416168_30AD1A58 | 504990 | 417 | -89.8 | 504990 | 439 | -84.0 | 504990 | 711 | -94.0 | 504990 | 823 |
| MR_1774416168_661C3918 | 504990 | 417 | -89.9 | 504990 | 439 | -83.5 | 504990 | 711 | -91.3 | 504990 | 823 |
| MR_1774416168_F3579CF7 | 504990 | 417 | -90.2 | 504990 | 439 | -86.3 | 504990 | 711 | -93.1 | 504990 | 823 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 162: `da5a2248-211...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `da5a2248-2112-43be-9412-1ce570311074` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[162] topology](images/test_0162.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3233273_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233273_1
- `C3`: Check test server and transmission issues
- `C4`: Increase A3 Offset threshold for 3233273_1
- `C5`: Press down the tilt angle of 3233273_1 by 6 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233273_1
- `C7`: Decrease transmission power for 3233273_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242336_2
- `C9`: Increase transmission power for 3242336_2
- `C10`: Lift the tilt angle of 3233273_1 by 6 degrees
- `C11`: Lift the tilt angle  of 3269165_3 by 10 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Add neighbor relationship between 3269165_3 and 3242336_2
- `C14`: Add neighbor relationship between 3233273_1 and 3242336_2
- `C15`: Press down the tilt angle  of 3269165_3 by 10 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242336_2
- `C17`: Decrease transmission power for 3242336_2
- `C18`: Increase A3 Offset threshold for 3242336_2
- `C19`: Adjust the azimuth of 3269165_3 by 50 degrees
- `C20`: Adjust the azimuth of 3233273_1 by 46 degrees
- `C21`: Increase transmission power for 3233273_1
- `C22`: Decrease A3 Offset threshold for 3242336_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.923 | MS1 | 121.4656661332 | 31.1446297819 | 464 | 504990 | -87.03 | 12.38 | 431.00 | 0.04 | 2.58 | 1593 |
| 2024-09-20 22:21:32.841 | MS1 | 121.4656702960 | 31.1446268057 | 464 | 504990 | -88.45 | 12.40 | 551.78 | 0.12 | 2.66 | 1564 |
| 2024-09-20 22:21:33.105 | MS1 | 121.4656628899 | 31.1446357582 | 464 | 504990 | -89.28 | 14.08 | 586.89 | 0.11 | 2.21 | 1599 |
| 2024-09-20 22:21:34.318 | MS1 | 121.4656750912 | 31.1446276998 | 464 | 504990 | -85.69 | 17.53 | 80.10 | 0.06 | 2.99 | 1564 |
| 2024-09-20 22:21:35.187 | MS1 | 121.4656680347 | 31.1446300254 | 464 | 504990 | -86.30 | 16.86 | 90.36 | 0.15 | 2.80 | 1570 |
| 2024-09-20 22:21:36.315 | MS1 | 121.4656646350 | 31.1446210639 | 464 | 504990 | -87.80 | 13.32 | 54.11 | 0.01 | 2.88 | 1570 |
| 2024-09-20 22:21:37.741 | MS1 | 121.4656620261 | 31.1446192776 | 464 | 504990 | -90.14 | 7.67 | 79.99 | 0.04 | 2.39 | 1578 |
| 2024-09-20 22:21:38.919 | MS1 | 121.4656699448 | 31.1446184181 | 464 | 504990 | -93.84 | 7.62 | 93.82 | 0.15 | 2.41 | 1595 |
| 2024-09-20 22:21:39.681 | MS1 | 121.4656697324 | 31.1446207849 | 464 | 504990 | -91.23 | 12.43 | 67.97 | 0.14 | 2.78 | 1565 |
| 2024-09-20 22:21:40.157 | MS1 | 121.4656695029 | 31.1446266727 | 464 | 504990 | -93.52 | 11.55 | 552.65 | 0.09 | 2.55 | 1599 |
| 2024-09-20 22:21:41.208 | MS1 | 121.4656779107 | 31.1446293526 | 464 | 504990 | -90.25 | 7.31 | 394.28 | 0.18 | 2.45 | 1566 |
| 2024-09-20 22:21:42.935 | MS1 | 121.4656650917 | 31.1446232233 | 464 | 504990 | -93.30 | 11.35 | 330.38 | 0.11 | 2.63 | 1576 |

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
| 3233273 | 1 | 121.4671517372 | 31.1559420801 | 140 | 4 | 1 | 34.0 | TDD | 464 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3242018 | 4 | 121.4648363272 | 31.1509608225 | 197 | 10 | 10 | 35.5 | TDD | 6 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3242336 | 2 | 121.4668307438 | 31.1454949076 | 285 | 2 | 8 | 41.1 | TDD | 814 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3269165 | 3 | 121.4757687169 | 31.1478856879 | 318 | 3 | 8 | 37.2 | TDD | 950 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.938 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.961 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.091 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.091 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.745 | NREventA3 | measId:2;ServCellPCI:876;Se... |
| 2024-09-20 22:21:37.985 | NRHandoverAttempt | SourcePCI:876;SourceNR-ARFC... |
| 2024-09-20 22:21:38.028 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.039 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.189 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.189 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233273 | 1 | 82.5933 | 76.8022 | -117.0842 | 12.8979 | 183.6743 | 0.0003 | 0.0086 |
| 2024_09_20 22:00 | 3242336 | 2 | 18.1939 | 10.4408 | -115.5847 | 16.9529 | 92.7217 | 0.0095 | 0.0046 |
| 2024_09_20 22:00 | 3269165 | 3 | 8.4019 | 8.3732 | -116.1854 | 14.5086 | 86.9379 | 0.0151 | 0.0064 |
| 2024_09_20 22:00 | 3242018 | 4 | 6.5455 | 5.7164 | -114.4736 | 16.9847 | 154.1619 | 0.0081 | 0.0114 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415921_5D6444F4 | 504990 | 464 | -84.8 | 504990 | 814 | -96.4 | 504990 | 950 | -97.3 | 504990 | 6 |
| MR_1774415921_BC1F1564 | 504990 | 464 | -83.8 | 504990 | 814 | -93.8 | 504990 | 950 | -98.7 | 504990 | 6 |
| MR_1774415921_DA0D1294 | 504990 | 464 | -86.6 | 504990 | 814 | -94.0 | 504990 | 950 | -99.3 | 504990 | 6 |
| MR_1774415921_02A27A8A | 504990 | 464 | -87.7 | 504990 | 814 | -93.6 | 504990 | 950 | -98.2 | 504990 | 6 |
| MR_1774415921_1834DABC | 504990 | 464 | -87.0 | 504990 | 814 | -94.8 | 504990 | 950 | -97.8 | 504990 | 6 |
| MR_1774415921_B462EE58 | 504990 | 464 | -87.5 | 504990 | 814 | -94.0 | 504990 | 950 | -96.9 | 504990 | 6 |
| MR_1774415921_F6B1A93B | 504990 | 464 | -84.3 | 504990 | 814 | -96.0 | 504990 | 950 | -97.5 | 504990 | 6 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 163: `4d0e7959-428...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4d0e7959-428f-4469-93dc-5a9c7ef5544c` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[163] topology](images/test_0163.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3274010_4
- `C2`: Decrease transmission power for 3274010_4
- `C3`: Decrease A3 Offset threshold for 3243074_3
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243074_3
- `C6`: Lift the tilt angle of 3274010_4 by 5 degrees
- `C7`: Adjust the azimuth of 3274010_4 by 8 degrees
- `C8`: Decrease A3 Offset threshold for 3274010_4
- `C9`: Lift the tilt angle  of 3243074_3 by 3 degrees
- `C10`: Press down the tilt angle of 3274010_4 by 5 degrees
- `C11`: Increase A3 Offset threshold for 3243074_3
- `C12`: Decrease transmission power for 3243074_3
- `C13`: Increase transmission power for 3274010_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243074_3
- `C15`: Check test server and transmission issues
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274010_4
- `C17`: Adjust the azimuth of 3243074_3 by 28 degrees
- `C18`: Increase transmission power for 3243074_3
- `C19`: Add neighbor relationship between 3270516_2 and 3243074_3
- `C20`: Add neighbor relationship between 3274010_4 and 3243074_3
- `C21`: Press down the tilt angle  of 3243074_3 by 3 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274010_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.283 | MS1 | 121.4656730361 | 31.1446348431 | 278 | 504990 | -76.01 | 13.49 | 390.33 | 0.07 | 2.55 | 1581 |
| 2024-09-20 22:21:32.966 | MS1 | 121.4656740806 | 31.1446334399 | 278 | 504990 | -76.45 | 15.68 | 550.63 | 0.04 | 2.72 | 1600 |
| 2024-09-20 22:21:33.786 | MS1 | 121.4656690166 | 31.1446308930 | 278 | 504990 | -83.41 | 15.25 | 376.46 | 0.09 | 2.69 | 1566 |
| 2024-09-20 22:21:34.873 | MS1 | 121.4656616595 | 31.1446255774 | 278 | 504990 | -92.73 | 0.26 | 66.57 | 0.19 | 1.39 | 1574 |
| 2024-09-20 22:21:35.523 | MS1 | 121.4656749735 | 31.1446298266 | 278 | 504990 | -89.08 | 0.06 | 66.29 | 0.09 | 1.03 | 1593 |
| 2024-09-20 22:21:36.408 | MS1 | 121.4656728364 | 31.1446371330 | 278 | 504990 | -90.11 | 0.07 | 57.68 | 0.11 | 1.48 | 1561 |
| 2024-09-20 22:21:37.893 | MS1 | 121.4656747183 | 31.1446375827 | 278 | 504990 | -91.65 | 1.35 | 57.05 | 0.04 | 1.46 | 1578 |
| 2024-09-20 22:21:38.268 | MS1 | 121.4656746069 | 31.1446307549 | 278 | 504990 | -93.52 | 2.49 | 70.19 | 0.10 | 1.39 | 1588 |
| 2024-09-20 22:21:39.764 | MS1 | 121.4656707310 | 31.1446341001 | 278 | 504990 | -87.88 | 0.35 | 57.34 | 0.10 | 1.08 | 1579 |
| 2024-09-20 22:21:40.723 | MS1 | 121.4656691074 | 31.1446365439 | 278 | 504990 | -76.01 | 12.69 | 562.81 | 0.17 | 2.08 | 1596 |
| 2024-09-20 22:21:41.350 | MS1 | 121.4656679041 | 31.1446231171 | 278 | 504990 | -81.41 | 16.07 | 535.56 | 0.09 | 2.94 | 1564 |
| 2024-09-20 22:21:42.197 | MS1 | 121.4656598920 | 31.1446212092 | 278 | 504990 | -84.51 | 17.11 | 464.44 | 0.14 | 2.38 | 1562 |

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
| 3233124 | 1 | 121.4662619866 | 31.1469320453 | 213 | 15 | 9 | 44.9 | TDD | 753 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3243074 | 3 | 121.4688253717 | 31.1559528632 | 221 | 1 | 1 | 39.8 | TDD | 884 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3270516 | 2 | 121.4743795395 | 31.1512723651 | 15 | 0 | 1 | 35.9 | TDD | 347 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3274010 | 4 | 121.4710005043 | 31.1461756718 | 243 | 2 | 0 | 24.5 | TDD | 278 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.474 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.495 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.601 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.601 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233124 | 1 | 16.0368 | 13.2040 | -117.9478 | 12.3315 | 153.0488 | 0.0004 | 0.0199 |
| 2024_09_20 22:00 | 3270516 | 2 | 7.9129 | 12.1635 | -115.9252 | 8.5473 | 84.5107 | 0.0193 | 0.0007 |
| 2024_09_20 22:00 | 3243074 | 3 | 18.6279 | 17.8294 | -115.0416 | 17.3315 | 132.6707 | 0.0006 | 0.0014 |
| 2024_09_20 22:00 | 3274010 | 4 | 8.9959 | 7.8324 | -109.1517 | 5.6154 | 122.7697 | 0.0001 | 0.0191 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415358_093E58CD | 504990 | 884 | -93.9 | 504990 | 278 | -89.0 | 504990 | 347 | -92.4 | 504990 | 753 |
| MR_1774415358_AE691FC4 | 504990 | 884 | -94.3 | 504990 | 278 | -90.4 | 504990 | 347 | -92.2 | 504990 | 753 |
| MR_1774415358_46BBE3C2 | 504990 | 278 | -94.1 | 504990 | 884 | -90.6 | 504990 | 347 | -94.5 | 504990 | 753 |
| MR_1774415358_8DFFEBB8 | 504990 | 278 | -91.7 | 504990 | 884 | -91.3 | 504990 | 347 | -94.8 | 504990 | 753 |
| MR_1774415358_D240641B | 504990 | 884 | -92.1 | 504990 | 278 | -88.1 | 504990 | 347 | -91.7 | 504990 | 753 |
| MR_1774415358_0391CC45 | 504990 | 884 | -91.2 | 504990 | 278 | -88.4 | 504990 | 347 | -93.8 | 504990 | 753 |
| MR_1774415358_33EF8FF6 | 504990 | 884 | -91.2 | 504990 | 278 | -89.4 | 504990 | 347 | -92.2 | 504990 | 753 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 164: `7bd2f82c-87a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7bd2f82c-87ad-40b3-a7e8-a5695b915f43` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[164] topology](images/test_0164.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3225831_2
- `C2`: Check test server and transmission issues
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225831_2
- `C4`: Press down the tilt angle  of 3236374_4 by 6 degrees
- `C5`: Increase A3 Offset threshold for 3236374_4
- `C6`: Lift the tilt angle of 3225831_2 by 10 degrees
- `C7`: Decrease transmission power for 3236374_4
- `C8`: Decrease A3 Offset threshold for 3225831_2
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Increase transmission power for 3236374_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225831_2
- `C12`: Lift the tilt angle  of 3236374_4 by 6 degrees
- `C13`: Decrease A3 Offset threshold for 3236374_4
- `C14`: Adjust the azimuth of 3236374_4 by 50 degrees
- `C15`: Increase transmission power for 3225831_2
- `C16`: Press down the tilt angle of 3225831_2 by 10 degrees
- `C17`: Add neighbor relationship between 3279070_3 and 3236374_4
- `C18`: Adjust the azimuth of 3225831_2 by 34 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236374_4
- `C20`: Increase A3 Offset threshold for 3225831_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236374_4
- `C22`: Add neighbor relationship between 3225831_2 and 3236374_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.109 | MS1 | 121.4656721776 | 31.1446292191 | 476 | 504990 | -88.96 | 12.09 | 482.67 | 0.20 | 2.86 | 1585 |
| 2024-09-20 22:21:32.324 | MS1 | 121.4656657779 | 31.1446334713 | 476 | 504990 | -91.71 | 16.08 | 437.43 | 0.03 | 2.19 | 1576 |
| 2024-09-20 22:21:33.791 | MS1 | 121.4656648616 | 31.1446288393 | 476 | 504990 | -89.88 | 14.93 | 414.30 | 0.04 | 2.60 | 1589 |
| 2024-09-20 22:21:34.789 | MS1 | 121.4656690540 | 31.1446327357 | 476 | 504990 | -91.24 | 16.84 | 97.39 | 0.19 | 2.45 | 333 |
| 2024-09-20 22:21:35.911 | MS1 | 121.4656722368 | 31.1446205053 | 476 | 504990 | -91.20 | 16.84 | 54.10 | 0.19 | 2.18 | 351 |
| 2024-09-20 22:21:36.941 | MS1 | 121.4656683886 | 31.1446233972 | 476 | 504990 | -88.51 | 13.26 | 55.67 | 0.11 | 2.30 | 355 |
| 2024-09-20 22:21:37.497 | MS1 | 121.4656678034 | 31.1446298577 | 476 | 504990 | -92.07 | 8.89 | 58.58 | 0.07 | 2.30 | 441 |
| 2024-09-20 22:21:38.916 | MS1 | 121.4656722800 | 31.1446261472 | 476 | 504990 | -89.26 | 11.11 | 83.81 | 0.19 | 2.24 | 385 |
| 2024-09-20 22:21:39.480 | MS1 | 121.4656711980 | 31.1446275863 | 476 | 504990 | -89.29 | 10.17 | 69.12 | 0.02 | 2.70 | 354 |
| 2024-09-20 22:21:40.848 | MS1 | 121.4656637572 | 31.1446322576 | 476 | 504990 | -91.79 | 10.98 | 420.68 | 0.13 | 2.64 | 1574 |
| 2024-09-20 22:21:41.495 | MS1 | 121.4656682457 | 31.1446325834 | 476 | 504990 | -91.86 | 10.19 | 487.13 | 0.03 | 2.14 | 1580 |
| 2024-09-20 22:21:42.692 | MS1 | 121.4656655118 | 31.1446296480 | 476 | 504990 | -90.09 | 12.96 | 574.42 | 0.04 | 2.97 | 1575 |

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
| 3225831 | 2 | 121.4646392529 | 31.1444621555 | 46 | 10 | 5 | 15.2 | TDD | 476 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3236374 | 4 | 121.4646827195 | 31.1558784711 | 230 | 4 | 9 | 47.3 | TDD | 855 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3250317 | 1 | 121.4692516460 | 31.1459575309 | 341 | 12 | 7 | 38.4 | TDD | 913 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3279070 | 3 | 121.4664332455 | 31.1463086684 | 125 | 5 | 7 | 46.8 | TDD | 804 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.562 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.579 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.684 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.684 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.427 | NREventA3 | measId:2;ServCellPCI:196;Se... |
| 2024-09-20 22:21:38.667 | NRHandoverAttempt | SourcePCI:196;SourceNR-ARFC... |
| 2024-09-20 22:21:38.706 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.721 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.829 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.829 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250317 | 1 | 6.9612 | 14.6064 | -115.5907 | 19.1699 | 86.9526 | 0.0159 | 0.0035 |
| 2024_09_20 22:00 | 3225831 | 2 | 5.7752 | 14.9077 | -114.3719 | 11.6653 | 122.9385 | 0.0037 | 0.0164 |
| 2024_09_20 22:00 | 3279070 | 3 | 18.6027 | 10.2094 | -115.1407 | 18.7075 | 114.3736 | 0.0098 | 0.0062 |
| 2024_09_20 22:00 | 3236374 | 4 | 6.1224 | 13.1318 | -114.1319 | 16.1042 | 135.5370 | 0.0038 | 0.0123 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412524_7A8683FB | 504990 | 476 | -93.0 | 504990 | 855 | -100.1 | 504990 | 804 | -104.9 | 504990 | 913 |
| MR_1774412524_66275A4B | 504990 | 476 | -90.4 | 504990 | 855 | -102.2 | 504990 | 804 | -103.8 | 504990 | 913 |
| MR_1774412524_2E3894B7 | 504990 | 476 | -92.0 | 504990 | 855 | -99.8 | 504990 | 804 | -106.2 | 504990 | 913 |
| MR_1774412524_B0FDD709 | 504990 | 476 | -91.2 | 504990 | 855 | -101.3 | 504990 | 804 | -103.1 | 504990 | 913 |
| MR_1774412524_370538E1 | 504990 | 476 | -90.9 | 504990 | 855 | -101.5 | 504990 | 804 | -104.8 | 504990 | 913 |
| MR_1774412524_5875AA7E | 504990 | 476 | -92.7 | 504990 | 855 | -99.3 | 504990 | 804 | -105.4 | 504990 | 913 |
| MR_1774412524_CCCF5C67 | 504990 | 476 | -93.2 | 504990 | 855 | -102.0 | 504990 | 804 | -104.9 | 504990 | 913 |
| MR_1774412524_50540B07 | 504990 | 476 | -92.6 | 504990 | 855 | -101.9 | 504990 | 804 | -106.6 | 504990 | 913 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 165: `d8c4075c-440...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d8c4075c-440e-45b8-95af-d4d2ca665b1b` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[165] topology](images/test_0165.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3279478_4 and 3241614_1
- `C2`: Increase transmission power for 3241614_1
- `C3`: Increase A3 Offset threshold for 3231951_3
- `C4`: Decrease A3 Offset threshold for 3231951_3
- `C5`: Press down the tilt angle of 3231951_3 by 3 degrees
- `C6`: Adjust the azimuth of 3241614_1 by 50 degrees
- `C7`: Increase A3 Offset threshold for 3241614_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231951_3
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease transmission power for 3241614_1
- `C11`: Check test server and transmission issues
- `C12`: Lift the tilt angle of 3231951_3 by 3 degrees
- `C13`: Press down the tilt angle  of 3241614_1 by 10 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241614_1
- `C15`: Lift the tilt angle  of 3241614_1 by 10 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241614_1
- `C17`: Decrease transmission power for 3231951_3
- `C18`: Adjust the azimuth of 3231951_3 by 34 degrees
- `C19`: Decrease A3 Offset threshold for 3241614_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231951_3
- `C21`: Increase transmission power for 3231951_3
- `C22`: Add neighbor relationship between 3231951_3 and 3241614_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.239 | MS1 | 121.4656743047 | 31.1446334785 | 309 | 504990 | -86.20 | 15.53 | 452.35 | 0.19 | 2.15 | 1586 |
| 2024-09-20 22:21:32.868 | MS1 | 121.4656655158 | 31.1446189320 | 309 | 504990 | -91.83 | 17.76 | 424.70 | 0.01 | 2.20 | 1560 |
| 2024-09-20 22:21:33.910 | MS1 | 121.4656674118 | 31.1446236818 | 309 | 504990 | -87.39 | 12.48 | 357.14 | 0.02 | 2.97 | 1596 |
| 2024-09-20 22:21:34.960 | MS1 | 121.4656598303 | 31.1446363948 | 309 | 504990 | -87.47 | 15.11 | 77.67 | 0.05 | 2.01 | 430 |
| 2024-09-20 22:21:35.903 | MS1 | 121.4656713542 | 31.1446199208 | 309 | 504990 | -85.42 | 14.93 | 74.11 | 0.14 | 2.82 | 391 |
| 2024-09-20 22:21:36.133 | MS1 | 121.4656731061 | 31.1446196127 | 309 | 504990 | -88.29 | 15.50 | 82.90 | 0.00 | 2.73 | 373 |
| 2024-09-20 22:21:37.160 | MS1 | 121.4656710927 | 31.1446269357 | 309 | 504990 | -91.62 | 9.66 | 53.43 | 0.03 | 2.27 | 453 |
| 2024-09-20 22:21:38.590 | MS1 | 121.4656648860 | 31.1446193939 | 309 | 504990 | -91.48 | 7.64 | 69.96 | 0.15 | 2.25 | 444 |
| 2024-09-20 22:21:39.668 | MS1 | 121.4656744788 | 31.1446331015 | 309 | 504990 | -92.15 | 8.78 | 59.43 | 0.01 | 2.89 | 311 |
| 2024-09-20 22:21:40.380 | MS1 | 121.4656595738 | 31.1446191602 | 309 | 504990 | -91.80 | 12.28 | 529.43 | 0.10 | 2.01 | 1593 |
| 2024-09-20 22:21:41.379 | MS1 | 121.4656760083 | 31.1446315293 | 309 | 504990 | -93.62 | 7.07 | 472.24 | 0.08 | 2.29 | 1563 |
| 2024-09-20 22:21:42.522 | MS1 | 121.4656709924 | 31.1446261647 | 309 | 504990 | -89.69 | 11.71 | 438.17 | 0.10 | 2.50 | 1583 |

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
| 3231951 | 3 | 121.4739789958 | 31.1451374514 | 300 | 2 | 7 | 18.9 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3241614 | 1 | 121.4704918918 | 31.1525272710 | 124 | 14 | 7 | 43.4 | TDD | 38 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3250519 | 2 | 121.4732042560 | 31.1546627327 | 109 | 10 | 7 | 43.2 | TDD | 986 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3279478 | 4 | 121.4668643308 | 31.1461724328 | 156 | 13 | 5 | 45.0 | TDD | 694 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.170 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.304 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.304 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.998 | NREventA3 | measId:2;ServCellPCI:496;Se... |
| 2024-09-20 22:21:38.238 | NRHandoverAttempt | SourcePCI:496;SourceNR-ARFC... |
| 2024-09-20 22:21:38.268 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.283 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.394 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.394 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241614 | 1 | 17.3909 | 16.6552 | -115.8428 | 15.9194 | 137.7860 | 0.0023 | 0.0031 |
| 2024_09_20 22:00 | 3250519 | 2 | 11.3258 | 11.1837 | -116.0111 | 14.1623 | 123.7210 | 0.0152 | 0.0183 |
| 2024_09_20 22:00 | 3231951 | 3 | 16.9335 | 8.8441 | -117.2378 | 8.3161 | 190.4290 | 0.0195 | 0.0038 |
| 2024_09_20 22:00 | 3279478 | 4 | 17.9440 | 7.9071 | -116.4207 | 12.3585 | 195.7843 | 0.0042 | 0.0082 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415768_5424AABD | 504990 | 309 | -87.4 | 504990 | 38 | -94.1 | 504990 | 694 | -96.6 | 504990 | 986 |
| MR_1774415768_CAD5E5A2 | 504990 | 309 | -89.0 | 504990 | 38 | -97.6 | 504990 | 694 | -95.6 | 504990 | 986 |
| MR_1774415768_0802316B | 504990 | 309 | -89.2 | 504990 | 38 | -96.2 | 504990 | 694 | -97.8 | 504990 | 986 |
| MR_1774415768_57236D0C | 504990 | 309 | -87.7 | 504990 | 38 | -96.8 | 504990 | 694 | -97.5 | 504990 | 986 |
| MR_1774415768_8ECBDF5A | 504990 | 309 | -87.6 | 504990 | 38 | -95.3 | 504990 | 694 | -96.6 | 504990 | 986 |
| MR_1774415768_199B17AE | 504990 | 309 | -85.8 | 504990 | 38 | -97.0 | 504990 | 694 | -98.2 | 504990 | 986 |
| MR_1774415768_E16AC05C | 504990 | 309 | -86.6 | 504990 | 38 | -94.2 | 504990 | 694 | -96.7 | 504990 | 986 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 166: `1d613485-cd0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1d613485-cd0b-4f81-be5f-a1ebf5831453` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[166] topology](images/test_0166.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3251337_1 by 9 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251337_1
- `C3`: Increase transmission power for 3274001_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251337_1
- `C5`: Decrease A3 Offset threshold for 3274001_2
- `C6`: Increase transmission power for 3251337_1
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Press down the tilt angle  of 3274001_2 by 2 degrees
- `C9`: Decrease A3 Offset threshold for 3251337_1
- `C10`: Add neighbor relationship between 3260279_4 and 3274001_2
- `C11`: Lift the tilt angle of 3251337_1 by 9 degrees
- `C12`: Decrease transmission power for 3274001_2
- `C13`: Check test server and transmission issues
- `C14`: Lift the tilt angle  of 3274001_2 by 2 degrees
- `C15`: Increase A3 Offset threshold for 3274001_2
- `C16`: Add neighbor relationship between 3251337_1 and 3274001_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274001_2
- `C18`: Adjust the azimuth of 3274001_2 by 50 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274001_2
- `C20`: Decrease transmission power for 3251337_1
- `C21`: Increase A3 Offset threshold for 3251337_1
- `C22`: Adjust the azimuth of 3251337_1 by 12 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.456 | MS1 | 121.4656706308 | 31.1446273518 | 272 | 504990 | -87.67 | 15.65 | 462.12 | 0.06 | 2.08 | 1578 |
| 2024-09-20 22:21:32.838 | MS1 | 121.4656770762 | 31.1446213500 | 272 | 504990 | -86.00 | 13.02 | 444.25 | 0.03 | 2.06 | 1576 |
| 2024-09-20 22:21:33.496 | MS1 | 121.4656596293 | 31.1446359172 | 272 | 504990 | -86.88 | 16.65 | 382.84 | 0.04 | 2.95 | 1584 |
| 2024-09-20 22:21:34.707 | MS1 | 121.4656651986 | 31.1446223607 | 272 | 504990 | -88.78 | 17.06 | 57.51 | 0.07 | 2.21 | 1575 |
| 2024-09-20 22:21:35.388 | MS1 | 121.4656596106 | 31.1446201801 | 272 | 504990 | -91.64 | 17.25 | 85.97 | 0.19 | 2.60 | 1572 |
| 2024-09-20 22:21:36.919 | MS1 | 121.4656638419 | 31.1446356849 | 272 | 504990 | -89.95 | 17.88 | 100.09 | 0.08 | 2.97 | 1579 |
| 2024-09-20 22:21:37.557 | MS1 | 121.4656694477 | 31.1446181779 | 272 | 504990 | -90.64 | 7.02 | 60.81 | 0.03 | 2.45 | 1578 |
| 2024-09-20 22:21:38.541 | MS1 | 121.4656743272 | 31.1446330382 | 272 | 504990 | -93.63 | 11.96 | 79.22 | 0.04 | 2.03 | 1594 |
| 2024-09-20 22:21:39.354 | MS1 | 121.4656740144 | 31.1446306871 | 272 | 504990 | -91.69 | 10.31 | 85.39 | 0.01 | 2.52 | 1581 |
| 2024-09-20 22:21:40.830 | MS1 | 121.4656691097 | 31.1446320757 | 272 | 504990 | -92.20 | 8.67 | 463.88 | 0.19 | 2.66 | 1598 |
| 2024-09-20 22:21:41.429 | MS1 | 121.4656775308 | 31.1446318292 | 272 | 504990 | -89.87 | 12.53 | 342.54 | 0.03 | 2.93 | 1560 |
| 2024-09-20 22:21:42.929 | MS1 | 121.4656733754 | 31.1446325817 | 272 | 504990 | -91.17 | 9.23 | 377.26 | 0.10 | 2.45 | 1596 |

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
| 3228756 | 3 | 121.4691921524 | 31.1495209554 | 132 | 9 | 8 | 40.2 | TDD | 19 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3251337 | 1 | 121.4725858441 | 31.1530342028 | 203 | 7 | 8 | 43.4 | TDD | 272 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3260279 | 4 | 121.4709827171 | 31.1460639031 | 49 | 12 | 9 | 45.7 | TDD | 688 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3274001 | 2 | 121.4729658626 | 31.1466414784 | 85 | 0 | 10 | 28.8 | TDD | 17 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.297 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.313 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.447 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.447 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.111 | NREventA3 | measId:2;ServCellPCI:545;Se... |
| 2024-09-20 22:21:38.351 | NRHandoverAttempt | SourcePCI:545;SourceNR-ARFC... |
| 2024-09-20 22:21:38.382 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.397 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.501 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.501 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3251337 | 1 | 93.5358 | 79.4086 | -117.6143 | 12.2562 | 111.6168 | 0.0131 | 0.0081 |
| 2024_09_19 22:00 | 3274001 | 2 | 78.9412 | 93.3111 | -117.9547 | 10.0283 | 110.0877 | 0.0068 | 0.0085 |
| 2024_09_19 22:00 | 3228756 | 3 | 91.9090 | 77.2884 | -116.3053 | 17.7437 | 148.7416 | 0.0100 | 0.0117 |
| 2024_09_19 22:00 | 3260279 | 4 | 92.5342 | 91.3385 | -115.0848 | 9.8898 | 111.3902 | 0.0121 | 0.0193 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414719_177D71FB | 504990 | 272 | -88.4 | 504990 | 17 | -97.4 | 504990 | 688 | -100.1 | 504990 | 19 |
| MR_1774414719_D560D486 | 504990 | 272 | -87.5 | 504990 | 17 | -96.4 | 504990 | 688 | -101.4 | 504990 | 19 |
| MR_1774414719_736C59D2 | 504990 | 272 | -89.3 | 504990 | 17 | -95.6 | 504990 | 688 | -101.2 | 504990 | 19 |
| MR_1774414719_A090E86E | 504990 | 272 | -88.6 | 504990 | 17 | -95.5 | 504990 | 688 | -99.9 | 504990 | 19 |
| MR_1774414719_AEB0BF09 | 504990 | 272 | -87.3 | 504990 | 17 | -98.2 | 504990 | 688 | -100.2 | 504990 | 19 |
| MR_1774414719_DC5AE28F | 504990 | 272 | -90.0 | 504990 | 17 | -98.0 | 504990 | 688 | -98.6 | 504990 | 19 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 167: `eb89c6c7-989...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `eb89c6c7-989f-4e3b-8b74-0c7ca62e4f64` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[167] topology](images/test_0167.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3241834_1
- `C2`: Decrease transmission power for 3279405_4
- `C3`: Press down the tilt angle  of 3241834_1 by 10 degrees
- `C4`: Lift the tilt angle  of 3241834_1 by 10 degrees
- `C5`: Increase A3 Offset threshold for 3241834_1
- `C6`: Adjust the azimuth of 3241834_1 by 50 degrees
- `C7`: Decrease A3 Offset threshold for 3279405_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279405_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241834_1
- `C10`: Increase A3 Offset threshold for 3279405_4
- `C11`: Increase transmission power for 3279405_4
- `C12`: Lift the tilt angle of 3279405_4 by 3 degrees
- `C13`: Decrease transmission power for 3241834_1
- `C14`: Adjust the azimuth of 3279405_4 by 30 degrees
- `C15`: Check test server and transmission issues
- `C16`: Press down the tilt angle of 3279405_4 by 3 degrees
- `C17`: Add neighbor relationship between 3259843_2 and 3241834_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Increase transmission power for 3241834_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279405_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241834_1
- `C22`: Add neighbor relationship between 3279405_4 and 3241834_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.405 | MS1 | 121.4656653952 | 31.1446224862 | 103 | 504990 | -86.17 | 16.54 | 521.93 | 0.07 | 2.98 | 1584 |
| 2024-09-20 22:21:32.529 | MS1 | 121.4656730997 | 31.1446287258 | 103 | 504990 | -89.91 | 13.28 | 304.94 | 0.13 | 2.14 | 1576 |
| 2024-09-20 22:21:33.437 | MS1 | 121.4656687486 | 31.1446203321 | 103 | 504990 | -91.42 | 16.57 | 371.48 | 0.05 | 2.97 | 1590 |
| 2024-09-20 22:21:34.948 | MS1 | 121.4656683275 | 31.1446197194 | 103 | 504990 | -91.30 | 12.02 | 79.49 | 0.51 | 2.63 | 550 |
| 2024-09-20 22:21:35.780 | MS1 | 121.4656688313 | 31.1446222345 | 103 | 504990 | -91.99 | 17.37 | 82.72 | 0.68 | 2.38 | 631 |
| 2024-09-20 22:21:36.515 | MS1 | 121.4656680056 | 31.1446320477 | 103 | 504990 | -85.21 | 14.65 | 90.80 | 0.56 | 2.54 | 580 |
| 2024-09-20 22:21:37.230 | MS1 | 121.4656609711 | 31.1446318451 | 103 | 504990 | -92.99 | 10.53 | 52.11 | 0.59 | 2.33 | 532 |
| 2024-09-20 22:21:38.763 | MS1 | 121.4656608915 | 31.1446252611 | 103 | 504990 | -92.93 | 9.66 | 59.59 | 0.59 | 2.44 | 587 |
| 2024-09-20 22:21:39.479 | MS1 | 121.4656756234 | 31.1446233236 | 103 | 504990 | -91.15 | 12.42 | 86.69 | 0.54 | 2.47 | 512 |
| 2024-09-20 22:21:40.703 | MS1 | 121.4656692203 | 31.1446211991 | 103 | 504990 | -92.80 | 12.59 | 518.23 | 0.09 | 2.52 | 1586 |
| 2024-09-20 22:21:41.526 | MS1 | 121.4656719129 | 31.1446235294 | 103 | 504990 | -93.54 | 11.45 | 548.46 | 0.15 | 2.63 | 1582 |
| 2024-09-20 22:21:42.411 | MS1 | 121.4656726921 | 31.1446235801 | 103 | 504990 | -91.21 | 10.08 | 535.19 | 0.02 | 2.54 | 1571 |

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
| 3241834 | 1 | 121.4645674856 | 31.1552829879 | 9 | 9 | 4 | 18.3 | TDD | 416 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3259843 | 2 | 121.4724534012 | 31.1508359230 | 321 | 13 | 7 | 34.0 | TDD | 585 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3276285 | 3 | 121.4717580394 | 31.1558424050 | 176 | 1 | 7 | 43.3 | TDD | 290 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3279405 | 4 | 121.4658985916 | 31.1489528227 | 213 | 1 | 2 | 18.5 | TDD | 103 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.992 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.015 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.140 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.140 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.851 | NREventA3 | measId:2;ServCellPCI:76;Ser... |
| 2024-09-20 22:21:38.091 | NRHandoverAttempt | SourcePCI:76;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.126 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.137 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.257 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.257 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241834 | 1 | 5.0223 | 9.3364 | -116.3710 | 15.3677 | 187.3949 | 0.0125 | 0.0043 |
| 2024_09_20 22:00 | 3259843 | 2 | 11.0113 | 9.0674 | -116.7554 | 12.2182 | 134.8549 | 0.0092 | 0.0042 |
| 2024_09_20 22:00 | 3276285 | 3 | 16.5212 | 11.1831 | -114.6082 | 17.1253 | 98.8400 | 0.0110 | 0.0198 |
| 2024_09_20 22:00 | 3279405 | 4 | 17.8107 | 11.9064 | -117.5594 | 9.8549 | 146.7619 | 0.0091 | 0.0116 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415599_1F95F506 | 504990 | 103 | -92.2 | 504990 | 416 | -97.2 | 504990 | 585 | -99.5 | 504990 | 290 |
| MR_1774415599_E6899E74 | 504990 | 103 | -93.1 | 504990 | 416 | -100.4 | 504990 | 585 | -102.3 | 504990 | 290 |
| MR_1774415599_80286F63 | 504990 | 103 | -90.3 | 504990 | 416 | -99.9 | 504990 | 585 | -100.3 | 504990 | 290 |
| MR_1774415599_C9E182C7 | 504990 | 103 | -93.2 | 504990 | 416 | -96.7 | 504990 | 585 | -101.0 | 504990 | 290 |
| MR_1774415599_DA08F8AD | 504990 | 103 | -91.1 | 504990 | 416 | -98.7 | 504990 | 585 | -101.7 | 504990 | 290 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 168: `c0916fcc-a50...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c0916fcc-a50e-4dc4-a655-ee1493f2e164` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[168] topology](images/test_0168.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3241279_3 and 3247599_2
- `C2`: Press down the tilt angle of 3239785_4 by 7 degrees
- `C3`: Increase A3 Offset threshold for 3239785_4
- `C4`: Lift the tilt angle of 3239785_4 by 7 degrees
- `C5`: Increase A3 Offset threshold for 3247599_2
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase transmission power for 3239785_4
- `C8`: Decrease transmission power for 3239785_4
- `C9`: Decrease A3 Offset threshold for 3247599_2
- `C10`: Check test server and transmission issues
- `C11`: Press down the tilt angle  of 3247599_2 by 5 degrees
- `C12`: Decrease A3 Offset threshold for 3239785_4
- `C13`: Increase transmission power for 3247599_2
- `C14`: Adjust the azimuth of 3239785_4 by 33 degrees
- `C15`: Decrease transmission power for 3247599_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239785_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239785_4
- `C18`: Lift the tilt angle  of 3247599_2 by 5 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247599_2
- `C20`: Add neighbor relationship between 3239785_4 and 3247599_2
- `C21`: Adjust the azimuth of 3247599_2 by 38 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247599_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.131 | MS1 | 121.4656663997 | 31.1446312331 | 863 | 504990 | -91.86 | 12.81 | 479.49 | 0.01 | 2.06 | 1600 |
| 2024-09-20 22:21:32.493 | MS1 | 121.4656612394 | 31.1446325406 | 863 | 504990 | -87.09 | 12.81 | 317.05 | 0.12 | 2.53 | 1565 |
| 2024-09-20 22:21:33.752 | MS1 | 121.4656597913 | 31.1446199729 | 863 | 504990 | -85.70 | 14.44 | 452.66 | 0.04 | 2.64 | 1597 |
| 2024-09-20 22:21:34.913 | MS1 | 121.4656737934 | 31.1446256357 | 863 | 504990 | -91.86 | 13.41 | 94.00 | 0.06 | 2.64 | 318 |
| 2024-09-20 22:21:35.336 | MS1 | 121.4656779015 | 31.1446287804 | 863 | 504990 | -85.33 | 16.83 | 99.27 | 0.01 | 2.59 | 463 |
| 2024-09-20 22:21:36.907 | MS1 | 121.4656593797 | 31.1446258670 | 863 | 504990 | -89.92 | 12.99 | 97.00 | 0.05 | 2.71 | 431 |
| 2024-09-20 22:21:37.652 | MS1 | 121.4656679082 | 31.1446267227 | 863 | 504990 | -89.66 | 10.04 | 56.55 | 0.11 | 2.77 | 442 |
| 2024-09-20 22:21:38.746 | MS1 | 121.4656741405 | 31.1446312740 | 863 | 504990 | -89.87 | 10.95 | 49.59 | 0.19 | 2.79 | 431 |
| 2024-09-20 22:21:39.155 | MS1 | 121.4656643319 | 31.1446336841 | 863 | 504990 | -90.66 | 8.13 | 96.49 | 0.16 | 2.18 | 373 |
| 2024-09-20 22:21:40.468 | MS1 | 121.4656656608 | 31.1446212882 | 863 | 504990 | -90.36 | 11.91 | 345.05 | 0.00 | 2.65 | 1569 |
| 2024-09-20 22:21:41.592 | MS1 | 121.4656659724 | 31.1446291061 | 863 | 504990 | -91.69 | 11.01 | 415.31 | 0.00 | 2.79 | 1593 |
| 2024-09-20 22:21:42.418 | MS1 | 121.4656711323 | 31.1446283755 | 863 | 504990 | -91.91 | 12.75 | 444.71 | 0.18 | 2.04 | 1595 |

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
| 3239785 | 4 | 121.4644543746 | 31.1478154002 | 195 | 2 | 0 | 33.3 | TDD | 863 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3241279 | 3 | 121.4659801520 | 31.1530300528 | 43 | 11 | 2 | 48.5 | TDD | 206 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3246621 | 1 | 121.4660560972 | 31.1474061271 | 206 | 5 | 12 | 17.1 | TDD | 225 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3247599 | 2 | 121.4752454579 | 31.1463880615 | 296 | 3 | 3 | 36.5 | TDD | 403 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.557 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.575 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.702 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.702 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.375 | NREventA3 | measId:2;ServCellPCI:406;Se... |
| 2024-09-20 22:21:38.615 | NRHandoverAttempt | SourcePCI:406;SourceNR-ARFC... |
| 2024-09-20 22:21:38.661 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.675 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.780 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.780 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246621 | 1 | 9.0846 | 19.3791 | -115.4418 | 8.2549 | 168.8928 | 0.0013 | 0.0062 |
| 2024_09_20 22:00 | 3247599 | 2 | 8.1866 | 11.9379 | -116.3313 | 6.4730 | 119.5298 | 0.0135 | 0.0067 |
| 2024_09_20 22:00 | 3241279 | 3 | 5.2276 | 16.2993 | -116.0691 | 18.9144 | 129.2384 | 0.0196 | 0.0156 |
| 2024_09_20 22:00 | 3239785 | 4 | 10.9657 | 9.7240 | -115.9643 | 7.2542 | 147.6703 | 0.0188 | 0.0079 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412836_CA3629CE | 504990 | 863 | -91.5 | 504990 | 403 | -96.6 | 504990 | 206 | -102.5 | 504990 | 225 |
| MR_1774412836_9C74333C | 504990 | 863 | -90.6 | 504990 | 403 | -95.0 | 504990 | 206 | -104.3 | 504990 | 225 |
| MR_1774412836_7D93F3AA | 504990 | 863 | -90.2 | 504990 | 403 | -93.6 | 504990 | 206 | -103.3 | 504990 | 225 |
| MR_1774412836_FDF20072 | 504990 | 863 | -90.3 | 504990 | 403 | -96.6 | 504990 | 206 | -104.2 | 504990 | 225 |
| MR_1774412836_31C8F758 | 504990 | 863 | -91.0 | 504990 | 403 | -93.4 | 504990 | 206 | -102.6 | 504990 | 225 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 169: `e39bdd6a-e8b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e39bdd6a-e8b1-47af-b52c-ad3fdab990b6` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[169] topology](images/test_0169.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272057_1
- `C2`: Press down the tilt angle of 3272057_1 by 6 degrees
- `C3`: Add neighbor relationship between 3272057_1 and 3216794_3
- `C4`: Increase A3 Offset threshold for 3272057_1
- `C5`: Decrease transmission power for 3272057_1
- `C6`: Add neighbor relationship between 3216146_4 and 3216794_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272057_1
- `C8`: Decrease transmission power for 3216794_3
- `C9`: Increase transmission power for 3216794_3
- `C10`: Lift the tilt angle of 3272057_1 by 6 degrees
- `C11`: Decrease A3 Offset threshold for 3216794_3
- `C12`: Adjust the azimuth of 3216146_4 by 26 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Increase A3 Offset threshold for 3216794_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216794_3
- `C16`: Press down the tilt angle  of 3216146_4 by 10 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216794_3
- `C18`: Decrease A3 Offset threshold for 3272057_1
- `C19`: Lift the tilt angle  of 3216146_4 by 10 degrees
- `C20`: Adjust the azimuth of 3272057_1 by 24 degrees
- `C21`: Check test server and transmission issues
- `C22`: Increase transmission power for 3272057_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.214 | MS1 | 121.4656584006 | 31.1446336592 | 482 | 504990 | -85.61 | 15.93 | 473.26 | 0.02 | 2.29 | 1578 |
| 2024-09-20 22:21:32.953 | MS1 | 121.4656614278 | 31.1446285790 | 482 | 504990 | -90.91 | 17.23 | 461.51 | 0.17 | 2.84 | 1598 |
| 2024-09-20 22:21:33.770 | MS1 | 121.4656613430 | 31.1446358488 | 482 | 504990 | -91.29 | 12.99 | 413.06 | 0.14 | 2.40 | 1583 |
| 2024-09-20 22:21:34.829 | MS1 | 121.4656635755 | 31.1446352827 | 482 | 504990 | -86.97 | 14.11 | 69.23 | 0.11 | 2.04 | 1591 |
| 2024-09-20 22:21:35.624 | MS1 | 121.4656581939 | 31.1446220203 | 482 | 504990 | -91.06 | 17.59 | 84.63 | 0.16 | 2.78 | 1582 |
| 2024-09-20 22:21:36.484 | MS1 | 121.4656761382 | 31.1446331370 | 482 | 504990 | -89.29 | 16.14 | 70.23 | 0.18 | 2.28 | 1566 |
| 2024-09-20 22:21:37.365 | MS1 | 121.4656745725 | 31.1446300893 | 482 | 504990 | -89.43 | 7.35 | 60.78 | 0.12 | 2.62 | 1566 |
| 2024-09-20 22:21:38.254 | MS1 | 121.4656742907 | 31.1446265989 | 482 | 504990 | -91.70 | 7.34 | 90.54 | 0.11 | 2.15 | 1565 |
| 2024-09-20 22:21:39.662 | MS1 | 121.4656672945 | 31.1446227296 | 482 | 504990 | -92.63 | 12.50 | 76.29 | 0.16 | 2.24 | 1579 |
| 2024-09-20 22:21:40.624 | MS1 | 121.4656715112 | 31.1446319208 | 482 | 504990 | -89.73 | 8.99 | 347.55 | 0.06 | 2.89 | 1583 |
| 2024-09-20 22:21:41.506 | MS1 | 121.4656659124 | 31.1446223663 | 482 | 504990 | -93.55 | 10.84 | 339.06 | 0.18 | 2.70 | 1582 |
| 2024-09-20 22:21:42.113 | MS1 | 121.4656719257 | 31.1446231987 | 482 | 504990 | -89.66 | 12.68 | 464.21 | 0.19 | 2.97 | 1585 |

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
| 3216146 | 4 | 121.4739032034 | 31.1446515955 | 25 | 10 | 1 | 16.5 | TDD | 326 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3216794 | 3 | 121.4736450486 | 31.1468730853 | 226 | 8 | 0 | 41.0 | TDD | 613 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3262262 | 2 | 121.4695596731 | 31.1472363509 | 74 | 9 | 9 | 33.0 | TDD | 250 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3272057 | 1 | 121.4735557777 | 31.1514628511 | 201 | 4 | 2 | 36.9 | TDD | 482 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.330 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.354 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.504 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.504 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.215 | NREventA3 | measId:2;ServCellPCI:865;Se... |
| 2024-09-20 22:21:38.455 | NRHandoverAttempt | SourcePCI:865;SourceNR-ARFC... |
| 2024-09-20 22:21:38.500 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.513 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.632 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.632 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272057 | 1 | 81.0881 | 85.2332 | -116.8353 | 7.4496 | 141.0537 | 0.0193 | 0.0081 |
| 2024_09_20 22:00 | 3262262 | 2 | 9.4909 | 15.2133 | -117.8331 | 7.7111 | 105.9863 | 0.0022 | 0.0153 |
| 2024_09_20 22:00 | 3216794 | 3 | 17.3049 | 15.6229 | -117.4107 | 7.8432 | 128.8384 | 0.0035 | 0.0021 |
| 2024_09_20 22:00 | 3216146 | 4 | 15.7656 | 7.3578 | -115.8783 | 9.6832 | 162.7233 | 0.0165 | 0.0184 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415649_ED6F8721 | 504990 | 482 | -88.7 | 504990 | 613 | -92.0 | 504990 | 326 | -101.8 | 504990 | 250 |
| MR_1774415649_AF815DDA | 504990 | 482 | -85.2 | 504990 | 613 | -92.0 | 504990 | 326 | -98.8 | 504990 | 250 |
| MR_1774415649_60F51277 | 504990 | 482 | -88.5 | 504990 | 613 | -93.1 | 504990 | 326 | -100.6 | 504990 | 250 |
| MR_1774415649_79BC03C3 | 504990 | 482 | -85.1 | 504990 | 613 | -90.7 | 504990 | 326 | -102.5 | 504990 | 250 |
| MR_1774415649_0EF98F65 | 504990 | 482 | -86.9 | 504990 | 613 | -93.1 | 504990 | 326 | -101.9 | 504990 | 250 |
| MR_1774415649_28CCD032 | 504990 | 482 | -87.1 | 504990 | 613 | -91.5 | 504990 | 326 | -102.4 | 504990 | 250 |
| MR_1774415649_B5837CEA | 504990 | 482 | -88.1 | 504990 | 613 | -91.2 | 504990 | 326 | -99.8 | 504990 | 250 |
| MR_1774415649_9D7DF25B | 504990 | 482 | -88.4 | 504990 | 613 | -92.6 | 504990 | 326 | -100.0 | 504990 | 250 |

> *... 2개 열 생략 (전체 14열)*

---
