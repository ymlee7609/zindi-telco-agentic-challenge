# Track A 문제 분석 — test[330]~test[339]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[330] ~ test[339] (10개)

## 목차

1. [문제 330: `88c829f2-3dd...`](#330) — single-answer
2. [문제 331: `5448a0b9-86f...`](#331) — single-answer
3. [문제 332: `1c8cb0f6-fa9...`](#332) — single-answer
4. [문제 333: `71659374-5a0...`](#333) — single-answer
5. [문제 334: `e7bb58ef-23a...`](#334) — single-answer
6. [문제 335: `1cbc400c-5d7...`](#335) — single-answer
7. [문제 336: `0f6e0ddf-43b...`](#336) — single-answer
8. [문제 337: `ed92910e-26f...`](#337) — single-answer
9. [문제 338: `dad40072-ec9...`](#338) — single-answer
10. [문제 339: `ee57f213-477...`](#339) — multiple-answer

---

### 문제 330: `88c829f2-3dd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `88c829f2-3ddc-42c2-9e34-f582acf5bc6f` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[330] topology](images/test_0330.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268234_4
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Lift the tilt angle of 3252184_2 by 10 degrees
- `C4`: Decrease transmission power for 3252184_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252184_2
- `C6`: Increase transmission power for 3268234_4
- `C7`: Lift the tilt angle  of 3268234_4 by 10 degrees
- `C8`: Decrease transmission power for 3268234_4
- `C9`: Press down the tilt angle  of 3268234_4 by 10 degrees
- `C10`: Adjust the azimuth of 3252184_2 by 50 degrees
- `C11`: Decrease A3 Offset threshold for 3252184_2
- `C12`: Check test server and transmission issues
- `C13`: Press down the tilt angle of 3252184_2 by 10 degrees
- `C14`: Decrease A3 Offset threshold for 3268234_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268234_4
- `C16`: Add neighbor relationship between 3252184_2 and 3268234_4
- `C17`: Increase A3 Offset threshold for 3252184_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252184_2
- `C19`: Increase transmission power for 3252184_2
- `C20`: Increase A3 Offset threshold for 3268234_4
- `C21`: Adjust the azimuth of 3268234_4 by 10 degrees
- `C22`: Add neighbor relationship between 3228744_1 and 3268234_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.785 | MS1 | 121.4656731417 | 31.1446281699 | 951 | 504990 | -82.27 | 16.31 | 427.02 | 0.14 | 2.07 | 1586 |
| 2024-09-20 22:21:32.429 | MS1 | 121.4656752944 | 31.1446287239 | 951 | 504990 | -78.78 | 12.07 | 366.88 | 0.10 | 2.06 | 1595 |
| 2024-09-20 22:21:33.391 | MS1 | 121.4656609692 | 31.1446195486 | 951 | 504990 | -83.13 | 14.87 | 478.92 | 0.03 | 2.32 | 1579 |
| 2024-09-20 22:21:34.766 | MS1 | 121.4656756094 | 31.1446184714 | 951 | 504990 | -85.26 | -3.85 | 70.99 | 0.16 | 1.03 | 1581 |
| 2024-09-20 22:21:35.293 | MS1 | 121.4656657327 | 31.1446377412 | 951 | 504990 | -83.40 | -3.40 | 28.04 | 0.14 | 1.38 | 1590 |
| 2024-09-20 22:21:36.250 | MS1 | 121.4656665752 | 31.1446345829 | 951 | 504990 | -92.15 | -2.95 | 58.97 | 0.03 | 1.47 | 1592 |
| 2024-09-20 22:21:37.249 | MS1 | 121.4656736822 | 31.1446281421 | 951 | 504990 | -87.83 | -0.64 | 48.52 | 0.13 | 1.41 | 1566 |
| 2024-09-20 22:21:38.867 | MS1 | 121.4656599316 | 31.1446296718 | 951 | 504990 | -90.44 | -3.59 | 45.75 | 0.02 | 1.50 | 1569 |
| 2024-09-20 22:21:39.638 | MS1 | 121.4656671059 | 31.1446335296 | 751 | 504990 | -78.99 | 15.56 | 251.86 | 0.03 | 1.41 | 1562 |
| 2024-09-20 22:21:40.260 | MS1 | 121.4656712010 | 31.1446330286 | 751 | 504990 | -76.40 | 14.48 | 371.92 | 0.06 | 2.26 | 1594 |
| 2024-09-20 22:21:41.843 | MS1 | 121.4656659741 | 31.1446209935 | 751 | 504990 | -84.50 | 12.03 | 604.70 | 0.05 | 2.17 | 1593 |
| 2024-09-20 22:21:42.164 | MS1 | 121.4656745489 | 31.1446316742 | 751 | 504990 | -79.01 | 12.80 | 371.94 | 0.03 | 2.34 | 1598 |

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
| 3228744 | 1 | 121.4718478419 | 31.1552611153 | 198 | 1 | 6 | 39.1 | TDD | 272 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3241681 | 3 | 121.4682904968 | 31.1526027590 | 46 | 11 | 11 | 21.3 | TDD | 946 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3252184 | 2 | 121.4747128890 | 31.1441295454 | 116 | 7 | 12 | 40.7 | TDD | 951 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3268234 | 4 | 121.4651310580 | 31.1479590736 | 182 | 10 | 9 | 42.9 | TDD | 751 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.583 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.607 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.747 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.747 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.394 | NREventA3 | measId:2;ServCellPCI:286;Se... |
| 2024-09-20 22:21:38.634 | NRHandoverAttempt | SourcePCI:286;SourceNR-ARFC... |
| 2024-09-20 22:21:38.671 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.683 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.812 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.812 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228744 | 1 | 9.5156 | 14.5328 | -115.2130 | 5.0817 | 189.9667 | 0.0185 | 0.0078 |
| 2024_09_20 22:00 | 3252184 | 2 | 16.2764 | 5.7862 | -116.9331 | 9.6158 | 89.0261 | 0.0127 | 0.1634 |
| 2024_09_20 22:00 | 3241681 | 3 | 8.9697 | 8.7419 | -115.6183 | 8.7154 | 117.8944 | 0.0188 | 0.0101 |
| 2024_09_20 22:00 | 3268234 | 4 | 7.1969 | 11.6103 | -114.1998 | 19.0307 | 104.1639 | 0.0120 | 0.0121 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412069_06B4DF42 | 504990 | 751 | -79.7 | 504990 | 951 | -85.7 | 504990 | 272 | -80.9 | 504990 | 946 |
| MR_1774412069_A563B0BC | 504990 | 951 | -86.8 | 504990 | 751 | -80.2 | 504990 | 272 | -79.3 | 504990 | 946 |
| MR_1774412069_0CF6DD78 | 504990 | 951 | -86.5 | 504990 | 751 | -79.1 | 504990 | 272 | -79.4 | 504990 | 946 |
| MR_1774412069_FEB5AB23 | 504990 | 951 | -86.1 | 504990 | 751 | -78.5 | 504990 | 272 | -81.1 | 504990 | 946 |
| MR_1774412069_78E25C0C | 504990 | 951 | -86.5 | 504990 | 751 | -77.9 | 504990 | 272 | -79.8 | 504990 | 946 |
| MR_1774412069_6EC0F740 | 504990 | 951 | -84.3 | 504990 | 751 | -78.5 | 504990 | 272 | -77.7 | 504990 | 946 |
| MR_1774412069_47B32D1F | 504990 | 951 | -84.7 | 504990 | 751 | -80.6 | 504990 | 272 | -78.1 | 504990 | 946 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 331: `5448a0b9-86f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5448a0b9-86fb-484d-bd78-9c84851dfc57` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[331] topology](images/test_0331.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3222483_2 by 6 degrees
- `C2`: Decrease A3 Offset threshold for 3222483_2
- `C3`: Add neighbor relationship between 3273094_3 and 3222483_2
- `C4`: Increase transmission power for 3222483_2
- `C5`: Decrease transmission power for 3222483_2
- `C6`: Decrease transmission power for 3273094_3
- `C7`: Press down the tilt angle of 3273094_3 by 3 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Add neighbor relationship between 3253762_1 and 3222483_2
- `C10`: Increase A3 Offset threshold for 3273094_3
- `C11`: Increase transmission power for 3273094_3
- `C12`: Adjust the azimuth of 3222483_2 by 29 degrees
- `C13`: Increase A3 Offset threshold for 3222483_2
- `C14`: Lift the tilt angle  of 3222483_2 by 6 degrees
- `C15`: Adjust the azimuth of 3273094_3 by 47 degrees
- `C16`: Decrease A3 Offset threshold for 3273094_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222483_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222483_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273094_3
- `C20`: Check test server and transmission issues
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273094_3
- `C22`: Lift the tilt angle of 3273094_3 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.855 | MS1 | 121.4656693854 | 31.1446292207 | 444 | 504990 | -86.44 | 13.20 | 447.74 | 0.18 | 2.46 | 1577 |
| 2024-09-20 22:21:32.235 | MS1 | 121.4656758325 | 31.1446255262 | 444 | 504990 | -91.03 | 13.06 | 569.72 | 0.10 | 2.41 | 1585 |
| 2024-09-20 22:21:33.653 | MS1 | 121.4656631337 | 31.1446191362 | 444 | 504990 | -89.01 | 15.37 | 594.91 | 0.01 | 2.79 | 1574 |
| 2024-09-20 22:21:34.866 | MS1 | 121.4656715250 | 31.1446226751 | 444 | 504990 | -87.73 | 15.47 | 102.66 | 0.54 | 2.58 | 538 |
| 2024-09-20 22:21:35.441 | MS1 | 121.4656673390 | 31.1446224543 | 444 | 504990 | -85.16 | 13.86 | 86.39 | 0.67 | 2.12 | 695 |
| 2024-09-20 22:21:36.822 | MS1 | 121.4656588729 | 31.1446217069 | 444 | 504990 | -85.47 | 15.20 | 80.33 | 0.58 | 2.39 | 508 |
| 2024-09-20 22:21:37.356 | MS1 | 121.4656584991 | 31.1446185688 | 444 | 504990 | -90.00 | 8.75 | 69.79 | 0.58 | 2.69 | 604 |
| 2024-09-20 22:21:38.440 | MS1 | 121.4656635736 | 31.1446182775 | 444 | 504990 | -92.50 | 9.35 | 79.57 | 0.60 | 2.45 | 543 |
| 2024-09-20 22:21:39.951 | MS1 | 121.4656716944 | 31.1446295700 | 444 | 504990 | -93.56 | 8.59 | 98.52 | 0.70 | 2.85 | 514 |
| 2024-09-20 22:21:40.122 | MS1 | 121.4656703030 | 31.1446194622 | 444 | 504990 | -91.13 | 10.24 | 592.89 | 0.12 | 2.54 | 1568 |
| 2024-09-20 22:21:41.647 | MS1 | 121.4656768341 | 31.1446181842 | 444 | 504990 | -93.46 | 12.86 | 460.70 | 0.05 | 2.53 | 1592 |
| 2024-09-20 22:21:42.902 | MS1 | 121.4656720937 | 31.1446330274 | 444 | 504990 | -90.64 | 8.32 | 495.82 | 0.07 | 2.70 | 1598 |

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
| 3210687 | 4 | 121.4729710702 | 31.1559939832 | 270 | 11 | 7 | 22.9 | TDD | 894 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3222483 | 2 | 121.4670926473 | 31.1511910751 | 220 | 4 | 1 | 29.1 | TDD | 771 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3253762 | 1 | 121.4665833404 | 31.1543911243 | 77 | 4 | 7 | 16.5 | TDD | 977 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3273094 | 3 | 121.4729393441 | 31.1446776890 | 316 | 1 | 9 | 27.4 | TDD | 444 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.443 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.459 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.561 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.561 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.261 | NREventA3 | measId:2;ServCellPCI:476;Se... |
| 2024-09-20 22:21:38.501 | NRHandoverAttempt | SourcePCI:476;SourceNR-ARFC... |
| 2024-09-20 22:21:38.533 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.546 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.662 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.662 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253762 | 1 | 10.0838 | 6.8332 | -115.6469 | 19.9455 | 101.5740 | 0.0007 | 0.0196 |
| 2024_09_20 22:00 | 3222483 | 2 | 7.2284 | 18.3484 | -116.0895 | 18.3772 | 139.6533 | 0.0176 | 0.0085 |
| 2024_09_20 22:00 | 3273094 | 3 | 11.9762 | 9.6615 | -115.2335 | 9.8716 | 182.5942 | 0.0020 | 0.0110 |
| 2024_09_20 22:00 | 3210687 | 4 | 12.4207 | 11.1347 | -114.5953 | 9.6905 | 133.4545 | 0.0095 | 0.0109 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414161_A5E3F817 | 504990 | 444 | -86.0 | 504990 | 771 | -91.0 | 504990 | 977 | -100.4 | 504990 | 894 |
| MR_1774414161_C3076274 | 504990 | 444 | -84.9 | 504990 | 771 | -92.3 | 504990 | 977 | -98.7 | 504990 | 894 |
| MR_1774414161_A56396D7 | 504990 | 444 | -84.1 | 504990 | 771 | -94.1 | 504990 | 977 | -97.4 | 504990 | 894 |
| MR_1774414161_3B6DE8F5 | 504990 | 444 | -84.3 | 504990 | 771 | -91.6 | 504990 | 977 | -100.7 | 504990 | 894 |
| MR_1774414161_00B10765 | 504990 | 444 | -85.2 | 504990 | 771 | -94.0 | 504990 | 977 | -100.3 | 504990 | 894 |
| MR_1774414161_668AD575 | 504990 | 444 | -83.2 | 504990 | 771 | -93.3 | 504990 | 977 | -98.4 | 504990 | 894 |
| MR_1774414161_52C11E2A | 504990 | 444 | -86.4 | 504990 | 771 | -93.3 | 504990 | 977 | -97.4 | 504990 | 894 |
| MR_1774414161_83F02A0D | 504990 | 444 | -85.0 | 504990 | 771 | -93.2 | 504990 | 977 | -100.7 | 504990 | 894 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 332: `1c8cb0f6-fa9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1c8cb0f6-fa98-4d86-806b-c5814c279843` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[332] topology](images/test_0332.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3252097_2 by 3 degrees
- `C2`: Adjust the azimuth of 3227585_3 by 50 degrees
- `C3`: Lift the tilt angle  of 3227585_3 by 2 degrees
- `C4`: Increase A3 Offset threshold for 3227585_3
- `C5`: Check test server and transmission issues
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase transmission power for 3227585_3
- `C8`: Increase A3 Offset threshold for 3252097_2
- `C9`: Decrease A3 Offset threshold for 3252097_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252097_2
- `C11`: Decrease A3 Offset threshold for 3227585_3
- `C12`: Decrease transmission power for 3227585_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227585_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227585_3
- `C15`: Increase transmission power for 3252097_2
- `C16`: Press down the tilt angle of 3252097_2 by 3 degrees
- `C17`: Adjust the azimuth of 3252097_2 by 8 degrees
- `C18`: Press down the tilt angle  of 3227585_3 by 2 degrees
- `C19`: Decrease transmission power for 3252097_2
- `C20`: Add neighbor relationship between 3235862_1 and 3227585_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252097_2
- `C22`: Add neighbor relationship between 3252097_2 and 3227585_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.230 | MS1 | 121.4656747635 | 31.1446367465 | 77 | 504990 | -90.88 | 17.58 | 563.15 | 0.01 | 2.14 | 1590 |
| 2024-09-20 22:21:32.226 | MS1 | 121.4656699780 | 31.1446199768 | 77 | 504990 | -88.73 | 15.31 | 464.28 | 0.15 | 2.69 | 1588 |
| 2024-09-20 22:21:33.350 | MS1 | 121.4656765845 | 31.1446256833 | 77 | 504990 | -90.33 | 15.77 | 337.38 | 0.11 | 2.78 | 1597 |
| 2024-09-20 22:21:34.647 | MS1 | 121.4656684000 | 31.1446223397 | 77 | 504990 | -86.92 | 16.84 | 74.90 | 0.55 | 2.99 | 647 |
| 2024-09-20 22:21:35.845 | MS1 | 121.4656621332 | 31.1446374876 | 77 | 504990 | -86.28 | 14.67 | 72.30 | 0.60 | 2.26 | 519 |
| 2024-09-20 22:21:36.941 | MS1 | 121.4656745947 | 31.1446191433 | 77 | 504990 | -87.11 | 13.43 | 74.32 | 0.55 | 2.13 | 541 |
| 2024-09-20 22:21:37.432 | MS1 | 121.4656758559 | 31.1446297613 | 77 | 504990 | -93.77 | 8.29 | 73.49 | 0.67 | 2.81 | 662 |
| 2024-09-20 22:21:38.455 | MS1 | 121.4656716787 | 31.1446235219 | 77 | 504990 | -91.01 | 10.61 | 57.35 | 0.55 | 2.38 | 630 |
| 2024-09-20 22:21:39.523 | MS1 | 121.4656737419 | 31.1446253714 | 77 | 504990 | -91.04 | 12.86 | 73.86 | 0.64 | 2.41 | 508 |
| 2024-09-20 22:21:40.260 | MS1 | 121.4656641560 | 31.1446254176 | 77 | 504990 | -89.14 | 7.30 | 545.74 | 0.13 | 2.63 | 1584 |
| 2024-09-20 22:21:41.231 | MS1 | 121.4656636009 | 31.1446225548 | 77 | 504990 | -93.83 | 9.67 | 492.18 | 0.17 | 2.53 | 1584 |
| 2024-09-20 22:21:42.716 | MS1 | 121.4656655393 | 31.1446233648 | 77 | 504990 | -92.18 | 8.36 | 409.36 | 0.05 | 2.01 | 1585 |

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
| 3221857 | 4 | 121.4652529177 | 31.1487458755 | 84 | 8 | 6 | 45.7 | TDD | 1006 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3227585 | 3 | 121.4708772850 | 31.1501468430 | 150 | 0 | 8 | 26.5 | TDD | 982 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3235862 | 1 | 121.4726970036 | 31.1469473604 | 233 | 12 | 1 | 41.1 | TDD | 18 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3252097 | 2 | 121.4755912087 | 31.1443207902 | 280 | 1 | 11 | 28.3 | TDD | 77 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.630 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.649 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.773 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.773 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.457 | NREventA3 | measId:2;ServCellPCI:738;Se... |
| 2024-09-20 22:21:38.697 | NRHandoverAttempt | SourcePCI:738;SourceNR-ARFC... |
| 2024-09-20 22:21:38.741 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.753 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.867 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.867 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235862 | 1 | 12.1669 | 15.8614 | -116.8527 | 6.2837 | 97.2006 | 0.0168 | 0.0081 |
| 2024_09_20 22:00 | 3252097 | 2 | 8.2413 | 19.0340 | -114.9152 | 6.2726 | 166.6715 | 0.0019 | 0.0052 |
| 2024_09_20 22:00 | 3227585 | 3 | 18.4435 | 17.6691 | -117.5602 | 7.7233 | 90.3906 | 0.0019 | 0.0040 |
| 2024_09_20 22:00 | 3221857 | 4 | 9.2326 | 15.1620 | -117.2656 | 10.0907 | 107.5563 | 0.0025 | 0.0049 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412680_CD199AAF | 504990 | 77 | -85.3 | 504990 | 982 | -96.2 | 504990 | 18 | -94.4 | 504990 | 1006 |
| MR_1774412680_3BC4BD0E | 504990 | 77 | -86.1 | 504990 | 982 | -94.8 | 504990 | 18 | -93.8 | 504990 | 1006 |
| MR_1774412680_90FCE461 | 504990 | 77 | -85.6 | 504990 | 982 | -96.2 | 504990 | 18 | -96.1 | 504990 | 1006 |
| MR_1774412680_D3DE175F | 504990 | 77 | -88.3 | 504990 | 982 | -93.4 | 504990 | 18 | -93.6 | 504990 | 1006 |
| MR_1774412680_39244399 | 504990 | 77 | -85.8 | 504990 | 982 | -93.5 | 504990 | 18 | -94.4 | 504990 | 1006 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 333: `71659374-5a0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `71659374-5a07-415a-9e34-3995ed3b1845` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[333] topology](images/test_0333.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228186_3
- `C2`: Decrease transmission power for 3244182_2
- `C3`: Increase transmission power for 3244182_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244182_2
- `C5`: Check test server and transmission issues
- `C6`: Lift the tilt angle of 3244182_2 by 5 degrees
- `C7`: Increase transmission power for 3228186_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228186_3
- `C9`: Adjust the azimuth of 3228186_3 by 50 degrees
- `C10`: Increase A3 Offset threshold for 3244182_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244182_2
- `C12`: Increase A3 Offset threshold for 3228186_3
- `C13`: Add neighbor relationship between 3257617_1 and 3228186_3
- `C14`: Add neighbor relationship between 3244182_2 and 3228186_3
- `C15`: Press down the tilt angle  of 3228186_3 by 10 degrees
- `C16`: Decrease transmission power for 3228186_3
- `C17`: Decrease A3 Offset threshold for 3244182_2
- `C18`: Decrease A3 Offset threshold for 3228186_3
- `C19`: Lift the tilt angle  of 3228186_3 by 10 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Adjust the azimuth of 3244182_2 by 31 degrees
- `C22`: Press down the tilt angle of 3244182_2 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.479 | MS1 | 121.4656591910 | 31.1446290902 | 986 | 504990 | -90.61 | 13.53 | 373.83 | 0.19 | 2.92 | 1579 |
| 2024-09-20 22:21:32.924 | MS1 | 121.4656612912 | 31.1446187374 | 986 | 504990 | -89.29 | 12.88 | 486.00 | 0.18 | 2.59 | 1565 |
| 2024-09-20 22:21:33.153 | MS1 | 121.4656627827 | 31.1446333099 | 986 | 504990 | -90.26 | 16.29 | 389.65 | 0.05 | 2.19 | 1600 |
| 2024-09-20 22:21:34.151 | MS1 | 121.4656722670 | 31.1446194492 | 986 | 504990 | -87.28 | 17.17 | 64.42 | 0.69 | 2.76 | 517 |
| 2024-09-20 22:21:35.285 | MS1 | 121.4656758025 | 31.1446201612 | 986 | 504990 | -89.60 | 16.24 | 90.06 | 0.52 | 2.67 | 658 |
| 2024-09-20 22:21:36.950 | MS1 | 121.4656585011 | 31.1446217959 | 986 | 504990 | -85.53 | 17.07 | 47.44 | 0.51 | 2.10 | 587 |
| 2024-09-20 22:21:37.119 | MS1 | 121.4656623339 | 31.1446188016 | 986 | 504990 | -93.04 | 11.72 | 97.13 | 0.64 | 2.72 | 625 |
| 2024-09-20 22:21:38.857 | MS1 | 121.4656624215 | 31.1446253853 | 986 | 504990 | -93.18 | 10.45 | 97.92 | 0.54 | 2.57 | 627 |
| 2024-09-20 22:21:39.839 | MS1 | 121.4656638413 | 31.1446332212 | 986 | 504990 | -92.92 | 12.04 | 87.56 | 0.54 | 2.03 | 605 |
| 2024-09-20 22:21:40.219 | MS1 | 121.4656739205 | 31.1446227720 | 986 | 504990 | -89.62 | 11.58 | 384.23 | 0.13 | 2.26 | 1591 |
| 2024-09-20 22:21:41.596 | MS1 | 121.4656644584 | 31.1446339798 | 986 | 504990 | -92.96 | 12.44 | 333.35 | 0.07 | 2.23 | 1573 |
| 2024-09-20 22:21:42.732 | MS1 | 121.4656604839 | 31.1446302593 | 986 | 504990 | -90.50 | 8.52 | 570.46 | 0.11 | 2.51 | 1567 |

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
| 3228186 | 3 | 121.4678389030 | 31.1470570772 | 284 | 15 | 8 | 45.9 | TDD | 317 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3244182 | 2 | 121.4654952126 | 31.1539696819 | 148 | 4 | 10 | 17.5 | TDD | 986 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3245488 | 4 | 121.4747959828 | 31.1441779948 | 254 | 11 | 5 | 48.4 | TDD | 458 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3257617 | 1 | 121.4734541676 | 31.1519781716 | 340 | 14 | 9 | 46.9 | TDD | 313 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.372 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.387 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.533 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.533 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.188 | NREventA3 | measId:2;ServCellPCI:352;Se... |
| 2024-09-20 22:21:38.428 | NRHandoverAttempt | SourcePCI:352;SourceNR-ARFC... |
| 2024-09-20 22:21:38.459 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.471 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.591 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.591 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257617 | 1 | 15.5152 | 5.8032 | -116.0640 | 13.5066 | 112.9977 | 0.0061 | 0.0146 |
| 2024_09_20 22:00 | 3244182 | 2 | 7.7971 | 9.4621 | -116.4514 | 10.8733 | 192.1918 | 0.0035 | 0.0072 |
| 2024_09_20 22:00 | 3228186 | 3 | 8.0880 | 16.9775 | -116.2127 | 7.7862 | 146.7038 | 0.0120 | 0.0148 |
| 2024_09_20 22:00 | 3245488 | 4 | 11.7337 | 17.2915 | -114.6630 | 19.7186 | 86.4703 | 0.0055 | 0.0066 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412503_63AAA695 | 504990 | 986 | -88.8 | 504990 | 317 | -89.1 | 504990 | 313 | -94.8 | 504990 | 458 |
| MR_1774412503_F575CA1B | 504990 | 986 | -85.4 | 504990 | 317 | -90.4 | 504990 | 313 | -96.3 | 504990 | 458 |
| MR_1774412503_DE8586C2 | 504990 | 986 | -86.5 | 504990 | 317 | -86.6 | 504990 | 313 | -97.2 | 504990 | 458 |
| MR_1774412503_E9AFEBC4 | 504990 | 986 | -87.2 | 504990 | 317 | -88.7 | 504990 | 313 | -94.0 | 504990 | 458 |
| MR_1774412503_ED61D965 | 504990 | 986 | -88.9 | 504990 | 317 | -87.1 | 504990 | 313 | -96.3 | 504990 | 458 |
| MR_1774412503_212CF7FD | 504990 | 986 | -85.9 | 504990 | 317 | -88.5 | 504990 | 313 | -97.5 | 504990 | 458 |
| MR_1774412503_AC55630F | 504990 | 986 | -88.7 | 504990 | 317 | -90.0 | 504990 | 313 | -96.3 | 504990 | 458 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 334: `e7bb58ef-23a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e7bb58ef-23ae-47fb-848d-2eace2b41807` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[334] topology](images/test_0334.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258578_1
- `C2`: Add neighbor relationship between 3233685_3 and 3215865_4
- `C3`: Decrease A3 Offset threshold for 3258578_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215865_4
- `C5`: Lift the tilt angle  of 3215865_4 by 10 degrees
- `C6`: Adjust the azimuth of 3215865_4 by 50 degrees
- `C7`: Add neighbor relationship between 3258578_1 and 3215865_4
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase transmission power for 3258578_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215865_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258578_1
- `C12`: Increase transmission power for 3215865_4
- `C13`: Increase A3 Offset threshold for 3215865_4
- `C14`: Check test server and transmission issues
- `C15`: Adjust the azimuth of 3258578_1 by 10 degrees
- `C16`: Decrease transmission power for 3258578_1
- `C17`: Lift the tilt angle of 3258578_1 by 10 degrees
- `C18`: Decrease transmission power for 3215865_4
- `C19`: Press down the tilt angle of 3258578_1 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3258578_1
- `C21`: Press down the tilt angle  of 3215865_4 by 10 degrees
- `C22`: Decrease A3 Offset threshold for 3215865_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.380 | MS1 | 121.4656612542 | 31.1446223643 | 415 | 504990 | -90.29 | 13.28 | 599.92 | 0.07 | 2.58 | 1584 |
| 2024-09-20 22:21:32.718 | MS1 | 121.4656680197 | 31.1446289132 | 415 | 504990 | -85.52 | 16.38 | 409.02 | 0.15 | 2.20 | 1582 |
| 2024-09-20 22:21:33.698 | MS1 | 121.4656765938 | 31.1446206904 | 415 | 504990 | -87.59 | 12.53 | 497.81 | 0.19 | 2.90 | 1589 |
| 2024-09-20 22:21:34.686 | MS1 | 121.4656645795 | 31.1446338277 | 415 | 504990 | -85.77 | 13.67 | 84.35 | 0.12 | 2.09 | 1583 |
| 2024-09-20 22:21:35.951 | MS1 | 121.4656678030 | 31.1446206863 | 415 | 504990 | -88.86 | 13.44 | 79.11 | 0.20 | 2.16 | 1592 |
| 2024-09-20 22:21:36.233 | MS1 | 121.4656583445 | 31.1446268292 | 415 | 504990 | -86.97 | 13.63 | 70.99 | 0.12 | 2.65 | 1584 |
| 2024-09-20 22:21:37.293 | MS1 | 121.4656755524 | 31.1446347506 | 415 | 504990 | -90.34 | 11.02 | 80.88 | 0.09 | 2.75 | 1600 |
| 2024-09-20 22:21:38.928 | MS1 | 121.4656633250 | 31.1446238703 | 415 | 504990 | -89.49 | 11.33 | 63.97 | 0.03 | 2.90 | 1583 |
| 2024-09-20 22:21:39.236 | MS1 | 121.4656754631 | 31.1446373580 | 415 | 504990 | -91.04 | 9.85 | 61.61 | 0.17 | 2.20 | 1569 |
| 2024-09-20 22:21:40.384 | MS1 | 121.4656589369 | 31.1446366581 | 415 | 504990 | -93.55 | 7.89 | 444.68 | 0.13 | 2.97 | 1565 |
| 2024-09-20 22:21:41.408 | MS1 | 121.4656643373 | 31.1446222086 | 415 | 504990 | -90.66 | 9.84 | 383.18 | 0.06 | 2.79 | 1583 |
| 2024-09-20 22:21:42.470 | MS1 | 121.4656706510 | 31.1446242292 | 415 | 504990 | -92.87 | 10.42 | 417.75 | 0.17 | 2.57 | 1600 |

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
| 3212986 | 2 | 121.4705141840 | 31.1515425981 | 327 | 9 | 7 | 48.7 | TDD | 611 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3215865 | 4 | 121.4701838218 | 31.1479694284 | 139 | 11 | 10 | 37.8 | TDD | 23 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3233685 | 3 | 121.4690581490 | 31.1463896500 | 183 | 6 | 12 | 15.1 | TDD | 963 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3258578 | 1 | 121.4664044904 | 31.1543630859 | 194 | 10 | 4 | 44.1 | TDD | 415 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.147 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.163 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.273 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.273 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.981 | NREventA3 | measId:2;ServCellPCI:679;Se... |
| 2024-09-20 22:21:38.221 | NRHandoverAttempt | SourcePCI:679;SourceNR-ARFC... |
| 2024-09-20 22:21:38.252 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.265 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.386 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.386 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3258578 | 1 | 78.9151 | 87.6847 | -114.2427 | 8.3048 | 159.1453 | 0.0160 | 0.0001 |
| 2024_09_19 22:00 | 3212986 | 2 | 82.8658 | 83.1902 | -115.6698 | 6.4302 | 135.4771 | 0.0037 | 0.0036 |
| 2024_09_19 22:00 | 3233685 | 3 | 88.3323 | 93.4181 | -115.6176 | 10.8197 | 85.7321 | 0.0179 | 0.0064 |
| 2024_09_19 22:00 | 3215865 | 4 | 78.1573 | 80.5953 | -114.0682 | 7.0413 | 170.7587 | 0.0102 | 0.0077 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416004_0409A8C9 | 504990 | 415 | -84.2 | 504990 | 23 | -94.7 | 504990 | 963 | -95.3 | 504990 | 611 |
| MR_1774416004_183F66EA | 504990 | 415 | -85.9 | 504990 | 23 | -95.7 | 504990 | 963 | -96.0 | 504990 | 611 |
| MR_1774416004_398F7863 | 504990 | 415 | -85.7 | 504990 | 23 | -96.4 | 504990 | 963 | -94.4 | 504990 | 611 |
| MR_1774416004_8DB8F5F6 | 504990 | 415 | -86.3 | 504990 | 23 | -96.5 | 504990 | 963 | -94.3 | 504990 | 611 |
| MR_1774416004_B06FFE26 | 504990 | 415 | -85.7 | 504990 | 23 | -95.0 | 504990 | 963 | -94.5 | 504990 | 611 |
| MR_1774416004_9867B6E5 | 504990 | 415 | -87.3 | 504990 | 23 | -93.5 | 504990 | 963 | -93.2 | 504990 | 611 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 335: `1cbc400c-5d7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1cbc400c-5d78-458a-972b-a5e9d25f6593` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[335] topology](images/test_0335.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224822_2
- `C3`: Add neighbor relationship between 3259084_4 and 3262542_1
- `C4`: Adjust the azimuth of 3224822_2 by 50 degrees
- `C5`: Decrease transmission power for 3262542_1
- `C6`: Decrease transmission power for 3224822_2
- `C7`: Increase transmission power for 3262542_1
- `C8`: Add neighbor relationship between 3224822_2 and 3262542_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224822_2
- `C11`: Press down the tilt angle of 3224822_2 by 4 degrees
- `C12`: Decrease A3 Offset threshold for 3224822_2
- `C13`: Lift the tilt angle  of 3262542_1 by 5 degrees
- `C14`: Decrease A3 Offset threshold for 3262542_1
- `C15`: Lift the tilt angle of 3224822_2 by 4 degrees
- `C16`: Increase transmission power for 3224822_2
- `C17`: Increase A3 Offset threshold for 3224822_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262542_1
- `C19`: Press down the tilt angle  of 3262542_1 by 5 degrees
- `C20`: Adjust the azimuth of 3262542_1 by 43 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262542_1
- `C22`: Increase A3 Offset threshold for 3262542_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.931 | MS1 | 121.4656677498 | 31.1446302214 | 581 | 504990 | -78.17 | 15.62 | 346.71 | 0.11 | 2.56 | 1560 |
| 2024-09-20 22:21:32.252 | MS1 | 121.4656610343 | 31.1446281826 | 581 | 504990 | -75.06 | 13.96 | 489.03 | 0.00 | 2.46 | 1587 |
| 2024-09-20 22:21:33.135 | MS1 | 121.4656588339 | 31.1446342559 | 581 | 504990 | -76.05 | 17.98 | 333.05 | 0.18 | 2.84 | 1571 |
| 2024-09-20 22:21:34.828 | MS1 | 121.4656709235 | 31.1446213220 | 581 | 504990 | -91.67 | -2.20 | 63.38 | 0.04 | 1.31 | 1599 |
| 2024-09-20 22:21:35.235 | MS1 | 121.4656640209 | 31.1446234271 | 581 | 504990 | -85.77 | -0.83 | 42.92 | 0.16 | 1.18 | 1581 |
| 2024-09-20 22:21:36.370 | MS1 | 121.4656587513 | 31.1446320598 | 581 | 504990 | -86.96 | -0.73 | 35.68 | 0.17 | 1.32 | 1564 |
| 2024-09-20 22:21:37.518 | MS1 | 121.4656590931 | 31.1446365983 | 581 | 504990 | -90.04 | -1.73 | 32.25 | 0.12 | 1.03 | 1583 |
| 2024-09-20 22:21:38.893 | MS1 | 121.4656638563 | 31.1446255522 | 581 | 504990 | -82.70 | 12.07 | 384.35 | 0.15 | 1.21 | 1570 |
| 2024-09-20 22:21:39.579 | MS1 | 121.4656743236 | 31.1446234322 | 581 | 504990 | -75.02 | 17.86 | 565.78 | 0.10 | 1.24 | 1589 |
| 2024-09-20 22:21:40.573 | MS1 | 121.4656705188 | 31.1446371611 | 581 | 504990 | -81.09 | 17.77 | 521.25 | 0.10 | 2.56 | 1586 |
| 2024-09-20 22:21:41.639 | MS1 | 121.4656689261 | 31.1446237154 | 581 | 504990 | -76.72 | 13.27 | 378.11 | 0.07 | 2.76 | 1579 |
| 2024-09-20 22:21:42.479 | MS1 | 121.4656774238 | 31.1446333339 | 581 | 504990 | -84.28 | 15.34 | 569.19 | 0.07 | 2.83 | 1591 |

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
| 3213931 | 3 | 121.4750308822 | 31.1461238317 | 154 | 4 | 6 | 26.1 | TDD | 963 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3224822 | 2 | 121.4696361412 | 31.1518191604 | 104 | 2 | 7 | 27.0 | TDD | 581 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3259084 | 4 | 121.4743429674 | 31.1490948436 | 76 | 6 | 12 | 26.5 | TDD | 943 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3262542 | 1 | 121.4754305646 | 31.1530841738 | 182 | 4 | 2 | 28.3 | TDD | 131 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.982 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.000 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.138 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.138 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.848 | NREventA3 | measId:2;ServCellPCI:67;Ser... |
| 2024-09-20 22:21:35.848 | NREventA3 | measId:2;ServCellPCI:67;Ser... |
| 2024-09-20 22:21:36.848 | NREventA3 | measId:2;ServCellPCI:67;Ser... |
| 2024-09-20 22:21:39.348 | NRRRCReestablishAttempt | PCI:67 |
| 2024-09-20 22:21:39.363 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.375 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.515 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.515 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262542 | 1 | 16.2658 | 17.1334 | -116.1501 | 13.3784 | 153.9113 | 0.0022 | 0.0087 |
| 2024_09_20 22:00 | 3224822 | 2 | 18.6265 | 18.1389 | -114.0054 | 8.6903 | 124.0346 | 0.0070 | 0.1537 |
| 2024_09_20 22:00 | 3213931 | 3 | 9.5062 | 6.1016 | -114.0253 | 19.6756 | 84.7216 | 0.0017 | 0.0039 |
| 2024_09_20 22:00 | 3259084 | 4 | 19.1298 | 8.5254 | -117.9296 | 9.1029 | 109.1602 | 0.0154 | 0.0113 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417182_7AFD1206 | 504990 | 131 | -86.7 | 504990 | 581 | -91.8 | 504990 | 943 | -93.5 | 504990 | 963 |
| MR_1774417182_C5CE3F8F | 504990 | 131 | -88.5 | 504990 | 581 | -89.8 | 504990 | 943 | -95.1 | 504990 | 963 |
| MR_1774417182_0E39BAA3 | 504990 | 131 | -89.0 | 504990 | 581 | -90.9 | 504990 | 943 | -94.6 | 504990 | 963 |
| MR_1774417182_965E0BC5 | 504990 | 581 | -92.5 | 504990 | 131 | -87.1 | 504990 | 943 | -95.8 | 504990 | 963 |
| MR_1774417182_F9A7E427 | 504990 | 581 | -89.9 | 504990 | 131 | -87.5 | 504990 | 943 | -93.0 | 504990 | 963 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 336: `0f6e0ddf-43b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0f6e0ddf-43b4-4898-a963-1b9ba55e8d5d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[336] topology](images/test_0336.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3237675_2 by 4 degrees
- `C2`: Increase transmission power for 3245378_3
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245378_3
- `C5`: Add neighbor relationship between 3237675_2 and 3245378_3
- `C6`: Decrease A3 Offset threshold for 3245378_3
- `C7`: Add neighbor relationship between 3213176_4 and 3245378_3
- `C8`: Adjust the azimuth of 3237675_2 by 50 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237675_2
- `C10`: Adjust the azimuth of 3245378_3 by 50 degrees
- `C11`: Increase A3 Offset threshold for 3245378_3
- `C12`: Lift the tilt angle of 3237675_2 by 4 degrees
- `C13`: Increase transmission power for 3237675_2
- `C14`: Decrease transmission power for 3237675_2
- `C15`: Check test server and transmission issues
- `C16`: Decrease transmission power for 3245378_3
- `C17`: Decrease A3 Offset threshold for 3237675_2
- `C18`: Press down the tilt angle  of 3245378_3 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3237675_2
- `C20`: Lift the tilt angle  of 3245378_3 by 10 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245378_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237675_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.806 | MS1 | 121.4656596430 | 31.1446329685 | 746 | 504990 | -85.09 | 16.84 | 409.39 | 0.05 | 2.79 | 1597 |
| 2024-09-20 22:21:32.848 | MS1 | 121.4656754131 | 31.1446235045 | 746 | 504990 | -85.35 | 13.10 | 571.47 | 0.19 | 2.80 | 1562 |
| 2024-09-20 22:21:33.592 | MS1 | 121.4656603211 | 31.1446213095 | 746 | 504990 | -91.67 | 15.69 | 515.68 | 0.07 | 2.55 | 1590 |
| 2024-09-20 22:21:34.876 | MS1 | 121.4656764161 | 31.1446183772 | 746 | 504990 | -89.28 | 14.54 | 83.25 | 0.07 | 2.27 | 1576 |
| 2024-09-20 22:21:35.794 | MS1 | 121.4656592508 | 31.1446312619 | 746 | 504990 | -86.17 | 15.26 | 82.35 | 0.10 | 2.43 | 1569 |
| 2024-09-20 22:21:36.930 | MS1 | 121.4656717210 | 31.1446295014 | 746 | 504990 | -85.27 | 16.05 | 85.86 | 0.18 | 2.08 | 1590 |
| 2024-09-20 22:21:37.835 | MS1 | 121.4656621401 | 31.1446350915 | 746 | 504990 | -92.21 | 9.41 | 64.16 | 0.19 | 2.01 | 1593 |
| 2024-09-20 22:21:38.606 | MS1 | 121.4656651744 | 31.1446375773 | 746 | 504990 | -92.27 | 11.91 | 49.27 | 0.03 | 2.29 | 1592 |
| 2024-09-20 22:21:39.748 | MS1 | 121.4656659370 | 31.1446306379 | 746 | 504990 | -90.39 | 9.06 | 88.03 | 0.14 | 2.76 | 1561 |
| 2024-09-20 22:21:40.525 | MS1 | 121.4656738560 | 31.1446230571 | 746 | 504990 | -91.96 | 7.71 | 379.62 | 0.09 | 2.04 | 1560 |
| 2024-09-20 22:21:41.925 | MS1 | 121.4656652411 | 31.1446217183 | 746 | 504990 | -93.56 | 11.19 | 407.02 | 0.03 | 2.18 | 1587 |
| 2024-09-20 22:21:42.601 | MS1 | 121.4656600089 | 31.1446286526 | 746 | 504990 | -92.59 | 11.96 | 554.42 | 0.14 | 2.54 | 1562 |

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
| 3213176 | 4 | 121.4663141721 | 31.1548515966 | 99 | 7 | 0 | 20.9 | TDD | 205 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3237675 | 2 | 121.4745282117 | 31.1446579169 | 349 | 3 | 12 | 18.4 | TDD | 746 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3245378 | 3 | 121.4662546413 | 31.1449430409 | 299 | 2 | 5 | 37.8 | TDD | 29 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3275275 | 1 | 121.4685494757 | 31.1509812957 | 353 | 1 | 3 | 17.6 | TDD | 641 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.211 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.228 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.348 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.348 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.035 | NREventA3 | measId:2;ServCellPCI:718;Se... |
| 2024-09-20 22:21:38.275 | NRHandoverAttempt | SourcePCI:718;SourceNR-ARFC... |
| 2024-09-20 22:21:38.318 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.328 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.433 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.433 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3275275 | 1 | 75.2956 | 94.9014 | -116.5562 | 18.9959 | 184.9004 | 0.0029 | 0.0036 |
| 2024_09_19 22:00 | 3237675 | 2 | 94.5246 | 75.3970 | -117.2810 | 11.1440 | 187.4260 | 0.0157 | 0.0067 |
| 2024_09_19 22:00 | 3245378 | 3 | 84.9995 | 83.2153 | -115.3670 | 12.0758 | 158.0296 | 0.0196 | 0.0081 |
| 2024_09_19 22:00 | 3213176 | 4 | 77.1420 | 82.0231 | -117.5886 | 8.4779 | 160.6219 | 0.0187 | 0.0144 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412942_DA64621F | 504990 | 746 | -89.0 | 504990 | 29 | -89.5 | 504990 | 205 | -95.4 | 504990 | 641 |
| MR_1774412942_52EDE758 | 504990 | 746 | -88.1 | 504990 | 29 | -90.9 | 504990 | 205 | -97.9 | 504990 | 641 |
| MR_1774412942_DEDABB9F | 504990 | 746 | -90.4 | 504990 | 29 | -90.9 | 504990 | 205 | -97.5 | 504990 | 641 |
| MR_1774412942_15B88BB9 | 504990 | 746 | -89.2 | 504990 | 29 | -89.0 | 504990 | 205 | -96.7 | 504990 | 641 |
| MR_1774412942_F80FEB43 | 504990 | 746 | -88.7 | 504990 | 29 | -89.0 | 504990 | 205 | -96.0 | 504990 | 641 |
| MR_1774412942_A5B8A5EB | 504990 | 746 | -90.1 | 504990 | 29 | -89.7 | 504990 | 205 | -96.2 | 504990 | 641 |
| MR_1774412942_D977744E | 504990 | 746 | -89.8 | 504990 | 29 | -88.8 | 504990 | 205 | -95.1 | 504990 | 641 |
| MR_1774412942_4A54D104 | 504990 | 746 | -89.0 | 504990 | 29 | -90.4 | 504990 | 205 | -94.6 | 504990 | 641 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 337: `ed92910e-26f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ed92910e-26f8-4889-af52-2a8897453e2f` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[337] topology](images/test_0337.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3229964_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase A3 Offset threshold for 3229964_2
- `C4`: Decrease A3 Offset threshold for 3246228_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246228_1
- `C6`: Lift the tilt angle  of 3246228_1 by 10 degrees
- `C7`: Increase transmission power for 3246228_1
- `C8`: Decrease transmission power for 3229964_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229964_2
- `C10`: Add neighbor relationship between 3229964_2 and 3246228_1
- `C11`: Lift the tilt angle of 3229964_2 by 10 degrees
- `C12`: Increase transmission power for 3229964_2
- `C13`: Adjust the azimuth of 3229964_2 by 13 degrees
- `C14`: Adjust the azimuth of 3246228_1 by 50 degrees
- `C15`: Press down the tilt angle  of 3246228_1 by 10 degrees
- `C16`: Check test server and transmission issues
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229964_2
- `C18`: Decrease transmission power for 3246228_1
- `C19`: Add neighbor relationship between 3215022_3 and 3246228_1
- `C20`: Increase A3 Offset threshold for 3246228_1
- `C21`: Press down the tilt angle of 3229964_2 by 10 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246228_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.314 | MS1 | 121.4656663241 | 31.1446279509 | 370 | 504990 | -90.28 | 13.14 | 459.52 | 0.16 | 2.39 | 1579 |
| 2024-09-20 22:21:32.373 | MS1 | 121.4656728984 | 31.1446264441 | 370 | 504990 | -90.53 | 14.21 | 564.60 | 0.07 | 2.03 | 1564 |
| 2024-09-20 22:21:33.802 | MS1 | 121.4656607453 | 31.1446336308 | 370 | 504990 | -86.30 | 12.96 | 417.68 | 0.12 | 2.51 | 1576 |
| 2024-09-20 22:21:34.294 | MS1 | 121.4656599783 | 31.1446317380 | 370 | 504990 | -86.20 | 17.64 | 65.57 | 0.02 | 2.77 | 444 |
| 2024-09-20 22:21:35.354 | MS1 | 121.4656717141 | 31.1446203547 | 370 | 504990 | -91.60 | 17.09 | 82.71 | 0.18 | 2.40 | 351 |
| 2024-09-20 22:21:36.562 | MS1 | 121.4656763241 | 31.1446373107 | 370 | 504990 | -86.98 | 17.07 | 47.45 | 0.09 | 2.22 | 377 |
| 2024-09-20 22:21:37.636 | MS1 | 121.4656748524 | 31.1446282239 | 370 | 504990 | -91.85 | 9.45 | 83.83 | 0.06 | 2.80 | 329 |
| 2024-09-20 22:21:38.620 | MS1 | 121.4656729078 | 31.1446190388 | 370 | 504990 | -91.95 | 10.96 | 66.84 | 0.06 | 2.11 | 419 |
| 2024-09-20 22:21:39.552 | MS1 | 121.4656709505 | 31.1446192483 | 370 | 504990 | -92.47 | 10.82 | 85.31 | 0.07 | 2.37 | 465 |
| 2024-09-20 22:21:40.371 | MS1 | 121.4656621520 | 31.1446255251 | 370 | 504990 | -93.92 | 8.95 | 442.74 | 0.04 | 2.65 | 1592 |
| 2024-09-20 22:21:41.395 | MS1 | 121.4656604671 | 31.1446313018 | 370 | 504990 | -93.55 | 11.42 | 440.88 | 0.01 | 2.10 | 1569 |
| 2024-09-20 22:21:42.503 | MS1 | 121.4656616357 | 31.1446365815 | 370 | 504990 | -91.68 | 11.67 | 368.24 | 0.11 | 2.49 | 1589 |

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
| 3215022 | 3 | 121.4661083681 | 31.1461950645 | 124 | 6 | 6 | 40.1 | TDD | 741 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3229964 | 2 | 121.4742155099 | 31.1494524050 | 250 | 12 | 9 | 43.0 | TDD | 370 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3245851 | 4 | 121.4706687456 | 31.1488881181 | 0 | 2 | 5 | 20.9 | TDD | 855 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3246228 | 1 | 121.4726612556 | 31.1459613929 | 168 | 9 | 12 | 27.7 | TDD | 64 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.141 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.159 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.280 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.280 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.009 | NREventA3 | measId:2;ServCellPCI:376;Se... |
| 2024-09-20 22:21:38.249 | NRHandoverAttempt | SourcePCI:376;SourceNR-ARFC... |
| 2024-09-20 22:21:38.286 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.300 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.450 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.450 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246228 | 1 | 14.7312 | 14.7863 | -114.7754 | 18.6447 | 148.7768 | 0.0183 | 0.0171 |
| 2024_09_20 22:00 | 3229964 | 2 | 14.3437 | 10.4715 | -115.6315 | 10.7678 | 93.8796 | 0.0023 | 0.0008 |
| 2024_09_20 22:00 | 3215022 | 3 | 11.2281 | 9.4244 | -115.6756 | 8.8877 | 160.5429 | 0.0138 | 0.0160 |
| 2024_09_20 22:00 | 3245851 | 4 | 13.4524 | 6.8027 | -114.3430 | 19.1583 | 108.5229 | 0.0093 | 0.0188 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413388_54B154A4 | 504990 | 370 | -87.2 | 504990 | 64 | -95.8 | 504990 | 741 | -97.7 | 504990 | 855 |
| MR_1774413388_7AC378E5 | 504990 | 370 | -86.0 | 504990 | 64 | -94.4 | 504990 | 741 | -97.5 | 504990 | 855 |
| MR_1774413388_DC525208 | 504990 | 370 | -84.9 | 504990 | 64 | -93.7 | 504990 | 741 | -94.9 | 504990 | 855 |
| MR_1774413388_CBFAE3FD | 504990 | 370 | -86.4 | 504990 | 64 | -95.2 | 504990 | 741 | -97.8 | 504990 | 855 |
| MR_1774413388_75A6FD1D | 504990 | 370 | -86.9 | 504990 | 64 | -95.0 | 504990 | 741 | -98.2 | 504990 | 855 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 338: `dad40072-ec9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dad40072-ec97-4628-9262-9c9be1656a9d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[338] topology](images/test_0338.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3240625_3 by 50 degrees
- `C2`: Check test server and transmission issues
- `C3`: Press down the tilt angle  of 3263147_4 by 5 degrees
- `C4`: Increase A3 Offset threshold for 3263147_4
- `C5`: Decrease A3 Offset threshold for 3240625_3
- `C6`: Increase transmission power for 3240625_3
- `C7`: Decrease A3 Offset threshold for 3263147_4
- `C8`: Add neighbor relationship between 3240625_3 and 3263147_4
- `C9`: Adjust the azimuth of 3263147_4 by 50 degrees
- `C10`: Lift the tilt angle of 3240625_3 by 10 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240625_3
- `C12`: Decrease transmission power for 3240625_3
- `C13`: Add neighbor relationship between 3247613_1 and 3263147_4
- `C14`: Lift the tilt angle  of 3263147_4 by 5 degrees
- `C15`: Increase transmission power for 3263147_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263147_4
- `C17`: Increase A3 Offset threshold for 3240625_3
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263147_4
- `C20`: Press down the tilt angle of 3240625_3 by 10 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240625_3
- `C22`: Decrease transmission power for 3263147_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.421 | MS1 | 121.4656670056 | 31.1446364263 | 439 | 504990 | -89.11 | 12.09 | 497.07 | 0.02 | 2.33 | 1600 |
| 2024-09-20 22:21:32.680 | MS1 | 121.4656745154 | 31.1446368292 | 439 | 504990 | -91.91 | 15.88 | 522.63 | 0.08 | 2.13 | 1573 |
| 2024-09-20 22:21:33.589 | MS1 | 121.4656772531 | 31.1446190974 | 439 | 504990 | -88.49 | 15.53 | 417.46 | 0.11 | 2.83 | 1574 |
| 2024-09-20 22:21:34.969 | MS1 | 121.4656666184 | 31.1446285457 | 439 | 504990 | -87.50 | 14.51 | 90.54 | 0.14 | 2.08 | 1583 |
| 2024-09-20 22:21:35.984 | MS1 | 121.4656596056 | 31.1446365234 | 439 | 504990 | -90.18 | 13.62 | 74.31 | 0.20 | 2.34 | 1570 |
| 2024-09-20 22:21:36.603 | MS1 | 121.4656756326 | 31.1446181891 | 439 | 504990 | -87.71 | 12.43 | 87.74 | 0.10 | 2.20 | 1592 |
| 2024-09-20 22:21:37.589 | MS1 | 121.4656631240 | 31.1446256737 | 439 | 504990 | -92.16 | 10.25 | 90.12 | 0.01 | 2.51 | 1584 |
| 2024-09-20 22:21:38.799 | MS1 | 121.4656734546 | 31.1446317069 | 439 | 504990 | -92.99 | 12.13 | 71.21 | 0.00 | 2.05 | 1600 |
| 2024-09-20 22:21:39.104 | MS1 | 121.4656707153 | 31.1446362006 | 439 | 504990 | -92.04 | 11.08 | 83.06 | 0.05 | 2.40 | 1571 |
| 2024-09-20 22:21:40.754 | MS1 | 121.4656670179 | 31.1446345983 | 439 | 504990 | -90.45 | 12.57 | 514.98 | 0.05 | 2.41 | 1592 |
| 2024-09-20 22:21:41.787 | MS1 | 121.4656701949 | 31.1446333197 | 439 | 504990 | -91.45 | 8.80 | 570.27 | 0.17 | 2.23 | 1570 |
| 2024-09-20 22:21:42.631 | MS1 | 121.4656642129 | 31.1446373451 | 439 | 504990 | -90.50 | 11.12 | 409.29 | 0.12 | 2.19 | 1561 |

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
| 3218212 | 2 | 121.4711304745 | 31.1450844961 | 280 | 7 | 0 | 36.1 | TDD | 594 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3240625 | 3 | 121.4642092038 | 31.1447821010 | 278 | 3 | 5 | 38.4 | TDD | 439 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3247613 | 1 | 121.4686216135 | 31.1474731217 | 140 | 8 | 12 | 15.0 | TDD | 209 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3263147 | 4 | 121.4687807932 | 31.1522048080 | 284 | 2 | 4 | 43.5 | TDD | 455 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.111 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.133 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.237 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.237 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.913 | NREventA3 | measId:2;ServCellPCI:753;Se... |
| 2024-09-20 22:21:38.153 | NRHandoverAttempt | SourcePCI:753;SourceNR-ARFC... |
| 2024-09-20 22:21:38.186 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.200 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.307 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.307 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3247613 | 1 | 89.2535 | 94.3748 | -115.8023 | 7.7171 | 110.1186 | 0.0063 | 0.0048 |
| 2024_09_19 22:00 | 3218212 | 2 | 82.4542 | 81.7277 | -117.8017 | 9.6983 | 154.7152 | 0.0058 | 0.0065 |
| 2024_09_19 22:00 | 3240625 | 3 | 83.3012 | 78.2172 | -115.3328 | 9.0441 | 149.2266 | 0.0054 | 0.0006 |
| 2024_09_19 22:00 | 3263147 | 4 | 90.4677 | 87.1356 | -116.2890 | 9.9193 | 145.4773 | 0.0042 | 0.0023 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413274_E09E055A | 504990 | 439 | -88.4 | 504990 | 455 | -89.5 | 504990 | 209 | -95.7 | 504990 | 594 |
| MR_1774413274_95611BB6 | 504990 | 439 | -86.4 | 504990 | 455 | -88.2 | 504990 | 209 | -96.7 | 504990 | 594 |
| MR_1774413274_793897FB | 504990 | 439 | -88.4 | 504990 | 455 | -91.3 | 504990 | 209 | -96.7 | 504990 | 594 |
| MR_1774413274_8B717B0A | 504990 | 439 | -86.0 | 504990 | 455 | -89.3 | 504990 | 209 | -97.8 | 504990 | 594 |
| MR_1774413274_0B6A8E61 | 504990 | 439 | -89.5 | 504990 | 455 | -91.8 | 504990 | 209 | -96.1 | 504990 | 594 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 339: `ee57f213-477...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ee57f213-477b-4e0a-9663-6fb4f69e921e` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[339] topology](images/test_0339.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3225897_4
- `C2`: Adjust the azimuth of 3225897_4 by 50 degrees
- `C3`: Decrease A3 Offset threshold for 3225897_4
- `C4`: Press down the tilt angle  of 3243062_3 by 3 degrees
- `C5`: Check test server and transmission issues
- `C6`: Decrease transmission power for 3225897_4
- `C7`: Lift the tilt angle of 3225897_4 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3243062_3
- `C9`: Press down the tilt angle of 3225897_4 by 10 degrees
- `C10`: Increase transmission power for 3225897_4
- `C11`: Add neighbor relationship between 3225897_4 and 3243062_3
- `C12`: Increase A3 Offset threshold for 3243062_3
- `C13`: Decrease transmission power for 3243062_3
- `C14`: Add neighbor relationship between 3239759_2 and 3243062_3
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243062_3
- `C17`: Adjust the azimuth of 3243062_3 by 9 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243062_3
- `C19`: Lift the tilt angle  of 3243062_3 by 3 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225897_4
- `C21`: Increase transmission power for 3243062_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225897_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.541 | MS1 | 121.4656638987 | 31.1446219018 | 439 | 504990 | -89.73 | 12.76 | 322.16 | 0.16 | 2.29 | 1590 |
| 2024-09-20 22:21:32.667 | MS1 | 121.4656585001 | 31.1446342012 | 439 | 504990 | -88.32 | 14.10 | 555.93 | 0.15 | 2.48 | 1597 |
| 2024-09-20 22:21:33.803 | MS1 | 121.4656624783 | 31.1446256891 | 439 | 504990 | -92.03 | 17.56 | 397.58 | 0.10 | 2.12 | 1562 |
| 2024-09-20 22:21:34.487 | MS1 | 121.4656671419 | 31.1446231937 | 439 | 504990 | -105.26 | -0.08 | 31.45 | 0.14 | 1.09 | 1560 |
| 2024-09-20 22:21:35.440 | MS1 | 121.4656598364 | 31.1446257790 | 439 | 504990 | -106.73 | 0.29 | 48.64 | 0.10 | 1.25 | 1567 |
| 2024-09-20 22:21:36.428 | MS1 | 121.4656628428 | 31.1446287950 | 439 | 504990 | -101.26 | 0.66 | 23.13 | 0.11 | 1.30 | 1562 |
| 2024-09-20 22:21:37.359 | MS1 | 121.4656661058 | 31.1446370082 | 439 | 504990 | -110.00 | -1.84 | 81.00 | 0.02 | 1.22 | 1596 |
| 2024-09-20 22:21:38.233 | MS1 | 121.4656580627 | 31.1446330766 | 439 | 504990 | -102.74 | -1.09 | 48.20 | 0.16 | 1.31 | 1563 |
| 2024-09-20 22:21:39.456 | MS1 | 121.4656764727 | 31.1446226309 | 439 | 504990 | -101.61 | -0.29 | 45.60 | 0.10 | 1.40 | 1591 |
| 2024-09-20 22:21:40.617 | MS1 | 121.4656598985 | 31.1446339432 | 439 | 504990 | -91.00 | 15.19 | 550.26 | 0.11 | 2.39 | 1574 |
| 2024-09-20 22:21:41.327 | MS1 | 121.4656583283 | 31.1446242332 | 439 | 504990 | -86.32 | 14.07 | 392.49 | 0.10 | 2.91 | 1591 |
| 2024-09-20 22:21:42.493 | MS1 | 121.4656699245 | 31.1446342217 | 439 | 504990 | -90.55 | 15.05 | 605.39 | 0.01 | 2.20 | 1587 |

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
| 3225897 | 4 | 121.4741603229 | 31.1491269085 | 309 | 15 | 12 | 48.3 | TDD | 439 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3239759 | 2 | 121.4721221174 | 31.1512071246 | 239 | 6 | 0 | 25.7 | TDD | 964 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3243062 | 3 | 121.4646178793 | 31.1555308628 | 166 | 1 | 10 | 40.1 | TDD | 357 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3261918 | 1 | 121.4653540036 | 31.1537353483 | 161 | 7 | 4 | 36.1 | TDD | 570 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.032 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.050 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.184 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.184 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.348 | NREventA2 | measId:1;ServCellPCI:380;Se... |
| 2024-09-20 22:21:34.458 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261918 | 1 | 8.5174 | 19.9347 | -116.7791 | 12.2060 | 92.8231 | 0.0057 | 0.0107 |
| 2024_09_20 22:00 | 3239759 | 2 | 11.1130 | 7.6042 | -116.9659 | 7.7627 | 141.1573 | 0.0022 | 0.0031 |
| 2024_09_20 22:00 | 3243062 | 3 | 9.6852 | 6.7405 | -114.7329 | 5.4326 | 159.5839 | 0.0170 | 0.0021 |
| 2024_09_20 22:00 | 3225897 | 4 | 15.4391 | 11.5150 | -114.7625 | 17.4529 | 129.7159 | 0.1662 | 0.0099 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413837_7E5B1761 | 504990 | 439 | -106.1 | 504990 | 357 | -108.4 | 504990 | 964 | -115.3 | 504990 | 570 |
| MR_1774413837_728B32EE | 504990 | 439 | -107.2 | 504990 | 357 | -107.1 | 504990 | 964 | -116.5 | 504990 | 570 |
| MR_1774413837_5F94570B | 504990 | 439 | -105.7 | 504990 | 357 | -109.3 | 504990 | 964 | -113.5 | 504990 | 570 |
| MR_1774413837_CC2D9094 | 504990 | 439 | -105.8 | 504990 | 357 | -109.6 | 504990 | 964 | -116.7 | 504990 | 570 |
| MR_1774413837_4390A5FC | 504990 | 439 | -103.6 | 504990 | 357 | -107.5 | 504990 | 964 | -113.6 | 504990 | 570 |
| MR_1774413837_9334B53D | 504990 | 439 | -105.9 | 504990 | 357 | -107.1 | 504990 | 964 | -116.8 | 504990 | 570 |
| MR_1774413837_7B38CA26 | 504990 | 439 | -104.6 | 504990 | 357 | -109.0 | 504990 | 964 | -115.3 | 504990 | 570 |
| MR_1774413837_232A7D02 | 504990 | 439 | -104.7 | 504990 | 357 | -108.8 | 504990 | 964 | -114.5 | 504990 | 570 |

> *... 2개 열 생략 (전체 14열)*

---
