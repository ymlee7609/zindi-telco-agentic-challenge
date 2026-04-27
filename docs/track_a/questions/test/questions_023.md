# Track A 문제 분석 — test[220]~test[229]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[220] ~ test[229] (10개)

## 목차

1. [문제 220: `048ba1a1-637...`](#220) — single-answer
2. [문제 221: `f6a4dafa-3d3...`](#221) — single-answer
3. [문제 222: `6313fd29-96e...`](#222) — single-answer
4. [문제 223: `e0288b8f-14a...`](#223) — single-answer
5. [문제 224: `01460025-b63...`](#224) — single-answer
6. [문제 225: `44075c68-d11...`](#225) — single-answer
7. [문제 226: `6ff19396-f8c...`](#226) — multiple-answer
8. [문제 227: `6bdaaf60-162...`](#227) — single-answer
9. [문제 228: `3cb19161-fca...`](#228) — single-answer
10. [문제 229: `73a957d1-fa8...`](#229) — single-answer

---

### 문제 220: `048ba1a1-637...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `048ba1a1-6379-4df2-89b1-bb83caa500fa` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[220] topology](images/test_0220.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3272541_2 by 10 degrees
- `C2`: Increase A3 Offset threshold for 3235942_1
- `C3`: Increase transmission power for 3272541_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235942_1
- `C5`: Add neighbor relationship between 3260610_4 and 3235942_1
- `C6`: Decrease transmission power for 3272541_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235942_1
- `C9`: Decrease transmission power for 3235942_1
- `C10`: Increase transmission power for 3235942_1
- `C11`: Press down the tilt angle of 3272541_2 by 10 degrees
- `C12`: Add neighbor relationship between 3272541_2 and 3235942_1
- `C13`: Press down the tilt angle  of 3235942_1 by 6 degrees
- `C14`: Adjust the azimuth of 3272541_2 by 45 degrees
- `C15`: Decrease A3 Offset threshold for 3235942_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272541_2
- `C17`: Increase A3 Offset threshold for 3272541_2
- `C18`: Lift the tilt angle  of 3235942_1 by 6 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272541_2
- `C20`: Check test server and transmission issues
- `C21`: Decrease A3 Offset threshold for 3272541_2
- `C22`: Adjust the azimuth of 3235942_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.473 | MS1 | 121.4656757340 | 31.1446340001 | 298 | 504990 | -85.57 | 12.40 | 341.43 | 0.20 | 2.09 | 1599 |
| 2024-09-20 22:21:32.765 | MS1 | 121.4656585309 | 31.1446340138 | 298 | 504990 | -88.06 | 17.48 | 416.69 | 0.09 | 2.93 | 1592 |
| 2024-09-20 22:21:33.463 | MS1 | 121.4656767257 | 31.1446204173 | 298 | 504990 | -88.82 | 14.44 | 569.75 | 0.04 | 2.31 | 1562 |
| 2024-09-20 22:21:34.581 | MS1 | 121.4656657763 | 31.1446275348 | 298 | 504990 | -86.30 | 17.38 | 78.38 | 0.01 | 2.01 | 1568 |
| 2024-09-20 22:21:35.383 | MS1 | 121.4656701852 | 31.1446183301 | 298 | 504990 | -89.90 | 13.80 | 55.22 | 0.04 | 2.71 | 1582 |
| 2024-09-20 22:21:36.424 | MS1 | 121.4656629628 | 31.1446282682 | 298 | 504990 | -91.78 | 15.91 | 77.73 | 0.02 | 2.21 | 1594 |
| 2024-09-20 22:21:37.292 | MS1 | 121.4656737649 | 31.1446361340 | 298 | 504990 | -91.86 | 8.82 | 68.75 | 0.10 | 2.03 | 1596 |
| 2024-09-20 22:21:38.591 | MS1 | 121.4656738078 | 31.1446313077 | 298 | 504990 | -92.60 | 7.71 | 93.08 | 0.03 | 2.04 | 1585 |
| 2024-09-20 22:21:39.639 | MS1 | 121.4656737838 | 31.1446252350 | 298 | 504990 | -91.88 | 11.61 | 89.39 | 0.03 | 2.30 | 1566 |
| 2024-09-20 22:21:40.620 | MS1 | 121.4656707934 | 31.1446273819 | 298 | 504990 | -89.24 | 8.72 | 465.68 | 0.19 | 2.64 | 1581 |
| 2024-09-20 22:21:41.769 | MS1 | 121.4656721750 | 31.1446323428 | 298 | 504990 | -93.53 | 8.35 | 546.97 | 0.15 | 2.60 | 1582 |
| 2024-09-20 22:21:42.889 | MS1 | 121.4656619734 | 31.1446309294 | 298 | 504990 | -92.57 | 7.75 | 485.57 | 0.06 | 2.55 | 1592 |

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
| 3217698 | 3 | 121.4758677898 | 31.1535858637 | 282 | 12 | 3 | 28.0 | TDD | 53 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3235942 | 1 | 121.4678437974 | 31.1448672842 | 9 | 1 | 2 | 17.9 | TDD | 921 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3260610 | 4 | 121.4693123191 | 31.1546673914 | 314 | 13 | 12 | 26.4 | TDD | 46 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3272541 | 2 | 121.4747164104 | 31.1536978439 | 265 | 15 | 1 | 41.8 | TDD | 298 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.206 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.222 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.323 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.323 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.061 | NREventA3 | measId:2;ServCellPCI:959;Se... |
| 2024-09-20 22:21:38.301 | NRHandoverAttempt | SourcePCI:959;SourceNR-ARFC... |
| 2024-09-20 22:21:38.334 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.347 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.486 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.486 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3235942 | 1 | 78.4863 | 93.4011 | -114.7096 | 14.0586 | 192.6572 | 0.0200 | 0.0029 |
| 2024_09_19 22:00 | 3272541 | 2 | 78.2281 | 85.8254 | -114.2899 | 5.3238 | 137.3111 | 0.0165 | 0.0160 |
| 2024_09_19 22:00 | 3217698 | 3 | 83.0323 | 78.5661 | -116.3827 | 5.2035 | 197.1118 | 0.0027 | 0.0062 |
| 2024_09_19 22:00 | 3260610 | 4 | 80.8377 | 87.2336 | -116.2762 | 18.2218 | 109.7355 | 0.0162 | 0.0184 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412641_BA95547B | 504990 | 298 | -85.7 | 504990 | 921 | -92.5 | 504990 | 46 | -101.4 | 504990 | 53 |
| MR_1774412641_0FA6A9CE | 504990 | 298 | -86.7 | 504990 | 921 | -92.1 | 504990 | 46 | -99.8 | 504990 | 53 |
| MR_1774412641_0293C988 | 504990 | 298 | -85.7 | 504990 | 921 | -90.6 | 504990 | 46 | -99.0 | 504990 | 53 |
| MR_1774412641_A7FDA980 | 504990 | 298 | -87.8 | 504990 | 921 | -91.7 | 504990 | 46 | -101.7 | 504990 | 53 |
| MR_1774412641_4D457046 | 504990 | 298 | -87.5 | 504990 | 921 | -91.2 | 504990 | 46 | -101.8 | 504990 | 53 |
| MR_1774412641_23C83D63 | 504990 | 298 | -85.3 | 504990 | 921 | -91.9 | 504990 | 46 | -101.7 | 504990 | 53 |
| MR_1774412641_9C766FAA | 504990 | 298 | -84.4 | 504990 | 921 | -92.5 | 504990 | 46 | -99.8 | 504990 | 53 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 221: `f6a4dafa-3d3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f6a4dafa-3d34-43b5-855d-9fefaf0b4368` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[221] topology](images/test_0221.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3275817_5 by 4 degrees
- `C2`: Lift the tilt angle of 3229821_1 by 3 degrees
- `C3`: Decrease transmission power for 3275817_5
- `C4`: Add neighbor relationship between 3229821_1 and 3275817_5
- `C5`: Increase A3 Offset threshold for 3229821_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229821_1
- `C7`: Increase transmission power for 3229821_1
- `C8`: Decrease transmission power for 3229821_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229821_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275817_5
- `C12`: Press down the tilt angle of 3229821_1 by 3 degrees
- `C13`: Add neighbor relationship between 3256531_12 and 3275817_5
- `C14`: Press down the tilt angle  of 3275817_5 by 4 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275817_5
- `C16`: Decrease A3 Offset threshold for 3229821_1
- `C17`: Increase A3 Offset threshold for 3275817_5
- `C18`: Adjust the azimuth of 3275817_5 by 41 degrees
- `C19`: Check test server and transmission issues
- `C20`: Adjust the azimuth of 3229821_1 by 20 degrees
- `C21`: Increase transmission power for 3275817_5
- `C22`: Decrease A3 Offset threshold for 3275817_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.441 | MS1 | 121.4656714062 | 31.1446182462 | 360 | 504990 | -93.98 | 10.47 | 308.82 | 0.04 | 2.55 | 1572 |
| 2024-09-20 22:21:32.255 | MS1 | 121.4656592769 | 31.1446235939 | 692 | 504990 | -94.05 | 10.46 | 434.18 | 0.18 | 2.75 | 1590 |
| 2024-09-20 22:21:33.488 | MS1 | 121.4656735564 | 31.1446303009 | 936 | 504990 | -93.70 | 11.65 | 558.59 | 0.04 | 2.61 | 1595 |
| 2024-09-20 22:21:34.654 | MS1 | 121.4656681590 | 31.1446277672 | 411 | 152650 | -89.02 | 6.57 | 75.14 | 0.02 | 1.89 | 931 |
| 2024-09-20 22:21:35.560 | MS1 | 121.4656619252 | 31.1446248803 | 258 | 152650 | -89.26 | 3.02 | 84.56 | 0.04 | 1.64 | 991 |
| 2024-09-20 22:21:36.434 | MS1 | 121.4656590661 | 31.1446273263 | 758 | 152650 | -90.13 | 4.37 | 77.93 | 0.06 | 1.73 | 960 |
| 2024-09-20 22:21:37.373 | MS1 | 121.4656743172 | 31.1446225228 | 232 | 152650 | -90.14 | 5.58 | 67.42 | 0.19 | 1.89 | 905 |
| 2024-09-20 22:21:38.585 | MS1 | 121.4656710914 | 31.1446211272 | 411 | 152650 | -90.64 | 2.35 | 92.61 | 0.14 | 1.77 | 958 |
| 2024-09-20 22:21:39.633 | MS1 | 121.4656601884 | 31.1446201557 | 258 | 152650 | -91.86 | 7.01 | 93.84 | 0.13 | 1.70 | 902 |
| 2024-09-20 22:21:40.162 | MS1 | 121.4656740980 | 31.1446335517 | 758 | 152650 | -94.11 | 5.75 | 70.23 | 0.18 | 2.55 | 1597 |
| 2024-09-20 22:21:41.129 | MS1 | 121.4656700701 | 31.1446366659 | 232 | 152650 | -88.43 | 4.64 | 79.81 | 0.06 | 2.67 | 1590 |
| 2024-09-20 22:21:42.879 | MS1 | 121.4656742195 | 31.1446314993 | 411 | 152650 | -93.38 | 4.31 | 63.48 | 0.12 | 2.38 | 1579 |

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
| 3212772 | 4 | 121.4737134414 | 31.1556453821 | 57 | 6 | 4 | 29.8 | TDD | 820 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3220811 | 11 | 121.4698760904 | 31.1510706696 | 218 | 3 | 9 | 29.0 | FDD | 208 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3221936 | 9 | 121.4652543777 | 31.1440814483 | 173 | 2 | 12 | 22.8 | FDD | 232 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3223766 | 10 | 121.4740653421 | 31.1477723440 | 180 | 8 | 10 | 3.7 | FDD | 40 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3229821 | 1 | 121.4728606578 | 31.1502070469 | 208 | 3 | 7 | 5.7 | TDD | 360 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3233066 | 3 | 121.4656739847 | 31.1446591057 | 30 | 10 | 12 | 23.7 | TDD | 692 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3242302 | 8 | 121.4675149957 | 31.1466571399 | 109 | 9 | 7 | 11.7 | FDD | 258 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3254199 | 13 | 121.4681888958 | 31.1557474185 | 114 | 13 | 0 | 17.5 | FDD | 411 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3255446 | 7 | 121.4729262886 | 31.1522194451 | 154 | 1 | 0 | 12.6 | FDD | 544 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3256531 | 12 | 121.4731255271 | 31.1506691573 | 27 | 2 | 10 | 8.6 | FDD | 758 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3272678 | 6 | 121.4649334508 | 31.1448741918 | 276 | 1 | 3 | 2.3 | TDD | 670 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3275817 | 5 | 121.4718070094 | 31.1440402803 | 235 | 4 | 10 | 2.5 | TDD | 859 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3277334 | 2 | 121.4649341487 | 31.1527614942 | 291 | 11 | 7 | 1.5 | TDD | 936 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.769 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.789 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.889 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.889 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.660 | NREventA2 | measId:1;ServCellPCI:748;Se... |
| 2024-09-20 22:21:34.795 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.090 | NREventA5 | measId:3;ServCellPCI:748;Se... |
| 2024-09-20 22:21:35.146 | NRHandoverAttempt | SourcePCI:748;SourceNR-ARFC... |
| 2024-09-20 22:21:35.185 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.199 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.312 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.312 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229821 | 1 | 6.7842 | 13.5180 | -114.5231 | 6.1389 | 155.1113 | 0.0177 | 0.0170 |
| 2024_09_20 22:00 | 3277334 | 2 | 14.8707 | 8.6476 | -116.8956 | 16.3538 | 185.3848 | 0.0161 | 0.0067 |
| 2024_09_20 22:00 | 3233066 | 3 | 7.7471 | 10.1416 | -114.3952 | 17.4790 | 99.0045 | 0.0124 | 0.0008 |
| 2024_09_20 22:00 | 3212772 | 4 | 8.3328 | 18.3014 | -116.4879 | 14.7674 | 128.9317 | 0.0018 | 0.0051 |
| 2024_09_20 22:00 | 3275817 | 5 | 5.2999 | 11.5675 | -116.1146 | 5.5260 | 117.3402 | 0.0018 | 0.0086 |
| 2024_09_20 22:00 | 3272678 | 6 | 15.9860 | 13.1629 | -114.9945 | 11.1260 | 86.2820 | 0.0186 | 0.0026 |
| 2024_09_20 22:00 | 3255446 | 7 | 5.1975 | 5.8675 | -115.4161 | 4.8426 | 56.0291 | 0.0112 | 0.0170 |
| 2024_09_20 22:00 | 3242302 | 8 | 15.0684 | 9.1521 | -117.5888 | 3.1506 | 54.6173 | 0.0037 | 0.0158 |
| 2024_09_20 22:00 | 3221936 | 9 | 17.9431 | 13.4693 | -115.2258 | 4.4118 | 54.1152 | 0.0100 | 0.0053 |
| 2024_09_20 22:00 | 3223766 | 10 | 13.7164 | 16.8819 | -115.3452 | 3.1642 | 32.1652 | 0.0068 | 0.0038 |
| 2024_09_20 22:00 | 3220811 | 11 | 8.6814 | 14.8927 | -114.1313 | 4.0483 | 50.3140 | 0.0188 | 0.0154 |
| 2024_09_20 22:00 | 3256531 | 12 | 8.6928 | 5.7699 | -116.9972 | 3.6936 | 25.9206 | 0.0074 | 0.0051 |
| 2024_09_20 22:00 | 3254199 | 13 | 17.3292 | 13.8389 | -117.9751 | 3.7084 | 48.0718 | 0.0122 | 0.0105 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413193_CB644158 | 152650 | 411 | -89.4 | 152650 | 40 | -90.0 | 152650 | 544 | -99.6 | 152650 | 208 |
| MR_1774413193_98577207 | 504990 | 936 | -95.4 | 504990 | 859 | -94.2 | 504990 | 670 | -100.6 | 504990 | 820 |
| MR_1774413193_07C966D9 | 504990 | 936 | -94.8 | 504990 | 859 | -94.4 | 504990 | 670 | -102.7 | 504990 | 820 |
| MR_1774413193_5CDA16B4 | 152650 | 411 | -90.0 | 152650 | 40 | -92.0 | 152650 | 544 | -99.1 | 152650 | 208 |
| MR_1774413193_D30C2E6B | 504990 | 936 | -95.0 | 504990 | 859 | -94.1 | 504990 | 670 | -101.2 | 504990 | 820 |
| MR_1774413193_DE95DCC5 | 152650 | 411 | -90.4 | 152650 | 40 | -91.0 | 152650 | 544 | -101.1 | 152650 | 208 |
| MR_1774413193_09890C61 | 152650 | 411 | -87.9 | 152650 | 40 | -93.6 | 152650 | 544 | -99.4 | 152650 | 208 |
| MR_1774413193_5C660B84 | 504990 | 936 | -92.5 | 504990 | 859 | -92.3 | 504990 | 670 | -100.6 | 504990 | 820 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 222: `6313fd29-96e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6313fd29-96ee-4dca-b2be-5665c467cac5` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[222] topology](images/test_0222.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3247907_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245780_2
- `C3`: Check test server and transmission issues
- `C4`: Increase A3 Offset threshold for 3245780_2
- `C5`: Adjust the azimuth of 3247907_3 by 48 degrees
- `C6`: Press down the tilt angle  of 3247907_3 by 3 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247907_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247907_3
- `C9`: Increase A3 Offset threshold for 3247907_3
- `C10`: Decrease A3 Offset threshold for 3245780_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245780_2
- `C12`: Adjust the azimuth of 3245780_2 by 8 degrees
- `C13`: Lift the tilt angle of 3245780_2 by 10 degrees
- `C14`: Lift the tilt angle  of 3247907_3 by 3 degrees
- `C15`: Press down the tilt angle of 3245780_2 by 10 degrees
- `C16`: Increase transmission power for 3245780_2
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase transmission power for 3247907_3
- `C19`: Add neighbor relationship between 3245780_2 and 3247907_3
- `C20`: Add neighbor relationship between 3260949_1 and 3247907_3
- `C21`: Decrease A3 Offset threshold for 3247907_3
- `C22`: Decrease transmission power for 3245780_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.627 | MS1 | 121.4656779712 | 31.1446328602 | 20 | 504990 | -75.17 | 15.13 | 590.92 | 0.14 | 2.51 | 1579 |
| 2024-09-20 22:21:32.602 | MS1 | 121.4656735695 | 31.1446251717 | 20 | 504990 | -76.12 | 17.14 | 338.67 | 0.01 | 2.11 | 1600 |
| 2024-09-20 22:21:33.355 | MS1 | 121.4656679226 | 31.1446243572 | 20 | 504990 | -75.80 | 15.17 | 494.79 | 0.03 | 2.01 | 1577 |
| 2024-09-20 22:21:34.792 | MS1 | 121.4656731272 | 31.1446337175 | 20 | 504990 | -93.45 | -3.58 | 54.88 | 0.12 | 1.46 | 1574 |
| 2024-09-20 22:21:35.463 | MS1 | 121.4656663472 | 31.1446285429 | 20 | 504990 | -91.35 | -3.23 | 34.39 | 0.04 | 1.31 | 1563 |
| 2024-09-20 22:21:36.410 | MS1 | 121.4656741159 | 31.1446250923 | 20 | 504990 | -93.06 | -2.22 | 73.08 | 0.16 | 1.28 | 1565 |
| 2024-09-20 22:21:37.870 | MS1 | 121.4656598718 | 31.1446258092 | 20 | 504990 | -89.26 | -3.03 | 68.22 | 0.11 | 1.31 | 1574 |
| 2024-09-20 22:21:38.521 | MS1 | 121.4656675084 | 31.1446315892 | 20 | 504990 | -79.66 | 17.24 | 575.94 | 0.18 | 1.07 | 1562 |
| 2024-09-20 22:21:39.197 | MS1 | 121.4656701033 | 31.1446322961 | 20 | 504990 | -82.17 | 17.89 | 574.65 | 0.01 | 1.06 | 1589 |
| 2024-09-20 22:21:40.248 | MS1 | 121.4656652778 | 31.1446260729 | 20 | 504990 | -78.41 | 13.61 | 311.12 | 0.19 | 2.85 | 1594 |
| 2024-09-20 22:21:41.973 | MS1 | 121.4656590686 | 31.1446181482 | 20 | 504990 | -78.78 | 13.42 | 577.77 | 0.03 | 2.08 | 1578 |
| 2024-09-20 22:21:42.746 | MS1 | 121.4656608530 | 31.1446357182 | 20 | 504990 | -75.77 | 12.65 | 573.43 | 0.14 | 2.83 | 1599 |

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
| 3223421 | 4 | 121.4668343192 | 31.1488618822 | 18 | 4 | 6 | 18.3 | TDD | 623 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3245780 | 2 | 121.4693025235 | 31.1449049908 | 273 | 9 | 9 | 15.9 | TDD | 20 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3247907 | 3 | 121.4651636565 | 31.1543801360 | 225 | 1 | 5 | 31.1 | TDD | 909 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3260949 | 1 | 121.4703795065 | 31.1526853491 | 203 | 14 | 5 | 33.5 | TDD | 495 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.950 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.973 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.123 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.123 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.835 | NREventA3 | measId:2;ServCellPCI:199;Se... |
| 2024-09-20 22:21:35.835 | NREventA3 | measId:2;ServCellPCI:199;Se... |
| 2024-09-20 22:21:36.835 | NREventA3 | measId:2;ServCellPCI:199;Se... |
| 2024-09-20 22:21:39.335 | NRRRCReestablishAttempt | PCI:199 |
| 2024-09-20 22:21:39.353 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.368 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.500 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.500 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260949 | 1 | 19.4868 | 14.6242 | -116.3832 | 8.9392 | 183.4075 | 0.0096 | 0.0106 |
| 2024_09_20 22:00 | 3245780 | 2 | 5.4708 | 8.4624 | -114.4105 | 8.4270 | 147.4568 | 0.0181 | 0.1558 |
| 2024_09_20 22:00 | 3247907 | 3 | 13.3050 | 18.3304 | -116.5304 | 14.1333 | 90.4780 | 0.0062 | 0.0172 |
| 2024_09_20 22:00 | 3223421 | 4 | 9.3834 | 15.5939 | -114.7560 | 10.6866 | 170.1387 | 0.0112 | 0.0200 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412033_9B7B7F99 | 504990 | 20 | -93.6 | 504990 | 909 | -88.5 | 504990 | 495 | -90.5 | 504990 | 623 |
| MR_1774412033_0C4915E7 | 504990 | 20 | -91.9 | 504990 | 909 | -87.7 | 504990 | 495 | -87.8 | 504990 | 623 |
| MR_1774412033_A32B64E6 | 504990 | 20 | -95.1 | 504990 | 909 | -89.6 | 504990 | 495 | -87.7 | 504990 | 623 |
| MR_1774412033_0FEDD2BD | 504990 | 20 | -94.1 | 504990 | 909 | -88.5 | 504990 | 495 | -90.3 | 504990 | 623 |
| MR_1774412033_45212DE2 | 504990 | 909 | -89.0 | 504990 | 20 | -94.1 | 504990 | 495 | -90.6 | 504990 | 623 |
| MR_1774412033_E01D8D3F | 504990 | 20 | -92.9 | 504990 | 909 | -89.5 | 504990 | 495 | -89.9 | 504990 | 623 |
| MR_1774412033_F071C951 | 504990 | 909 | -89.2 | 504990 | 20 | -93.1 | 504990 | 495 | -90.8 | 504990 | 623 |
| MR_1774412033_EDB2953A | 504990 | 20 | -93.7 | 504990 | 909 | -87.9 | 504990 | 495 | -87.2 | 504990 | 623 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 223: `e0288b8f-14a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e0288b8f-14ad-4f53-88fc-d5075cea9239` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[223] topology](images/test_0223.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3213311_1 and 3255605_2
- `C2`: Increase transmission power for 3242778_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255605_2
- `C4`: Decrease transmission power for 3255605_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255605_2
- `C6`: Decrease transmission power for 3242778_4
- `C7`: Increase transmission power for 3255605_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242778_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242778_4
- `C10`: Adjust the azimuth of 3242778_4 by 50 degrees
- `C11`: Press down the tilt angle of 3242778_4 by 6 degrees
- `C12`: Decrease A3 Offset threshold for 3242778_4
- `C13`: Press down the tilt angle  of 3255605_2 by 10 degrees
- `C14`: Add neighbor relationship between 3242778_4 and 3255605_2
- `C15`: Adjust the azimuth of 3255605_2 by 50 degrees
- `C16`: Increase A3 Offset threshold for 3242778_4
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Lift the tilt angle of 3242778_4 by 6 degrees
- `C19`: Lift the tilt angle  of 3255605_2 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3255605_2
- `C21`: Decrease A3 Offset threshold for 3255605_2
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.706 | MS1 | 121.4656638926 | 31.1446302774 | 399 | 504990 | -76.52 | 15.78 | 324.72 | 0.01 | 2.78 | 1591 |
| 2024-09-20 22:21:32.600 | MS1 | 121.4656613899 | 31.1446326377 | 399 | 504990 | -78.76 | 17.63 | 450.01 | 0.10 | 2.15 | 1572 |
| 2024-09-20 22:21:33.627 | MS1 | 121.4656621113 | 31.1446233837 | 399 | 504990 | -76.80 | 14.91 | 594.75 | 0.11 | 2.93 | 1571 |
| 2024-09-20 22:21:34.949 | MS1 | 121.4656619334 | 31.1446371000 | 399 | 504990 | -90.14 | -1.71 | 55.91 | 0.17 | 1.36 | 1567 |
| 2024-09-20 22:21:35.236 | MS1 | 121.4656583587 | 31.1446283349 | 399 | 504990 | -88.24 | -2.51 | 55.84 | 0.18 | 1.40 | 1575 |
| 2024-09-20 22:21:36.368 | MS1 | 121.4656662685 | 31.1446246256 | 399 | 504990 | -86.99 | -0.64 | 49.77 | 0.17 | 1.19 | 1598 |
| 2024-09-20 22:21:37.661 | MS1 | 121.4656585897 | 31.1446318575 | 399 | 504990 | -87.38 | -1.43 | 29.74 | 0.18 | 1.37 | 1599 |
| 2024-09-20 22:21:38.129 | MS1 | 121.4656705466 | 31.1446223623 | 399 | 504990 | -83.92 | -1.26 | 34.61 | 0.15 | 1.25 | 1562 |
| 2024-09-20 22:21:39.921 | MS1 | 121.4656600736 | 31.1446371956 | 433 | 504990 | -77.30 | 16.21 | 226.63 | 0.06 | 1.41 | 1599 |
| 2024-09-20 22:21:40.820 | MS1 | 121.4656656612 | 31.1446327141 | 433 | 504990 | -76.02 | 12.66 | 393.83 | 0.20 | 2.47 | 1589 |
| 2024-09-20 22:21:41.890 | MS1 | 121.4656655412 | 31.1446301539 | 433 | 504990 | -77.60 | 14.03 | 446.50 | 0.01 | 2.75 | 1568 |
| 2024-09-20 22:21:42.287 | MS1 | 121.4656748447 | 31.1446206531 | 433 | 504990 | -77.04 | 14.78 | 510.96 | 0.03 | 2.37 | 1579 |

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
| 3213311 | 1 | 121.4698057849 | 31.1482653205 | 71 | 4 | 5 | 15.8 | TDD | 65 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3242778 | 4 | 121.4740203065 | 31.1463777452 | 194 | 4 | 3 | 31.2 | TDD | 399 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3255605 | 2 | 121.4658722803 | 31.1442350673 | 178 | 13 | 6 | 40.3 | TDD | 433 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3261657 | 3 | 121.4663162565 | 31.1490072669 | 227 | 15 | 9 | 46.7 | TDD | 140 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.084 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.107 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.229 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.229 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.966 | NREventA3 | measId:2;ServCellPCI:567;Se... |
| 2024-09-20 22:21:38.206 | NRHandoverAttempt | SourcePCI:567;SourceNR-ARFC... |
| 2024-09-20 22:21:38.243 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.254 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.385 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.385 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213311 | 1 | 19.4617 | 13.1030 | -117.5063 | 7.6169 | 190.8207 | 0.0165 | 0.0078 |
| 2024_09_20 22:00 | 3255605 | 2 | 12.0894 | 9.1733 | -114.7794 | 13.6491 | 162.5468 | 0.0149 | 0.0099 |
| 2024_09_20 22:00 | 3261657 | 3 | 9.2193 | 8.9150 | -114.7525 | 11.7293 | 162.1582 | 0.0073 | 0.0028 |
| 2024_09_20 22:00 | 3242778 | 4 | 18.3533 | 5.7553 | -117.7606 | 8.9966 | 80.3454 | 0.0160 | 0.1164 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415793_07E4EC0D | 504990 | 399 | -91.5 | 504990 | 433 | -83.9 | 504990 | 65 | -87.3 | 504990 | 140 |
| MR_1774415793_CB61DCBC | 504990 | 399 | -91.3 | 504990 | 433 | -86.8 | 504990 | 65 | -86.3 | 504990 | 140 |
| MR_1774415793_A8A343BA | 504990 | 399 | -91.6 | 504990 | 433 | -84.7 | 504990 | 65 | -87.1 | 504990 | 140 |
| MR_1774415793_CE2063B4 | 504990 | 399 | -91.5 | 504990 | 433 | -84.9 | 504990 | 65 | -87.5 | 504990 | 140 |
| MR_1774415793_F73B65AD | 504990 | 399 | -90.5 | 504990 | 433 | -84.7 | 504990 | 65 | -87.6 | 504990 | 140 |
| MR_1774415793_3F3C1015 | 504990 | 433 | -86.8 | 504990 | 399 | -92.0 | 504990 | 65 | -85.1 | 504990 | 140 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 224: `01460025-b63...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `01460025-b633-4f96-b70f-77af580fde23` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[224] topology](images/test_0224.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3216603_4 by 11 degrees
- `C2`: Add neighbor relationship between 3212966_2 and 3216603_4
- `C3`: Adjust the azimuth of 3231802_3 by 45 degrees
- `C4`: Decrease transmission power for 3231802_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216603_4
- `C6`: Lift the tilt angle  of 3216603_4 by 10 degrees
- `C7`: Increase A3 Offset threshold for 3216603_4
- `C8`: Press down the tilt angle of 3231802_3 by 4 degrees
- `C9`: Press down the tilt angle  of 3216603_4 by 10 degrees
- `C10`: Increase transmission power for 3231802_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231802_3
- `C12`: Check test server and transmission issues
- `C13`: Decrease transmission power for 3216603_4
- `C14`: Decrease A3 Offset threshold for 3231802_3
- `C15`: Lift the tilt angle of 3231802_3 by 4 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231802_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216603_4
- `C18`: Decrease A3 Offset threshold for 3216603_4
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase A3 Offset threshold for 3231802_3
- `C21`: Increase transmission power for 3216603_4
- `C22`: Add neighbor relationship between 3231802_3 and 3216603_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.473 | MS1 | 121.4656650295 | 31.1446317852 | 814 | 504990 | -90.57 | 14.73 | 457.28 | 0.11 | 2.12 | 1584 |
| 2024-09-20 22:21:32.866 | MS1 | 121.4656705854 | 31.1446330492 | 814 | 504990 | -87.36 | 12.98 | 542.36 | 0.09 | 2.95 | 1574 |
| 2024-09-20 22:21:33.313 | MS1 | 121.4656662217 | 31.1446367890 | 814 | 504990 | -87.87 | 12.54 | 413.99 | 0.02 | 2.01 | 1583 |
| 2024-09-20 22:21:34.345 | MS1 | 121.4656689545 | 31.1446193797 | 814 | 504990 | -85.02 | 15.81 | 86.37 | 0.18 | 2.16 | 409 |
| 2024-09-20 22:21:35.862 | MS1 | 121.4656623245 | 31.1446256188 | 814 | 504990 | -85.86 | 16.68 | 76.94 | 0.14 | 2.55 | 300 |
| 2024-09-20 22:21:36.711 | MS1 | 121.4656733565 | 31.1446225262 | 814 | 504990 | -90.41 | 13.76 | 66.71 | 0.17 | 2.07 | 359 |
| 2024-09-20 22:21:37.123 | MS1 | 121.4656622741 | 31.1446247745 | 814 | 504990 | -91.07 | 8.64 | 44.22 | 0.18 | 2.46 | 313 |
| 2024-09-20 22:21:38.648 | MS1 | 121.4656629587 | 31.1446197428 | 814 | 504990 | -89.44 | 9.89 | 48.74 | 0.11 | 2.98 | 327 |
| 2024-09-20 22:21:39.591 | MS1 | 121.4656580870 | 31.1446308602 | 814 | 504990 | -93.69 | 7.04 | 82.69 | 0.15 | 2.79 | 497 |
| 2024-09-20 22:21:40.935 | MS1 | 121.4656593896 | 31.1446336565 | 814 | 504990 | -89.23 | 9.73 | 516.47 | 0.16 | 2.64 | 1597 |
| 2024-09-20 22:21:41.127 | MS1 | 121.4656665495 | 31.1446265289 | 814 | 504990 | -89.96 | 9.30 | 460.27 | 0.14 | 2.76 | 1566 |
| 2024-09-20 22:21:42.429 | MS1 | 121.4656689428 | 31.1446301252 | 814 | 504990 | -93.45 | 7.24 | 400.62 | 0.15 | 2.32 | 1586 |

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
| 3212966 | 2 | 121.4652882005 | 31.1524279220 | 143 | 2 | 5 | 28.5 | TDD | 669 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3216603 | 4 | 121.4692775015 | 31.1453603502 | 246 | 5 | 6 | 38.1 | TDD | 167 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3226135 | 1 | 121.4754598731 | 31.1447141992 | 359 | 1 | 1 | 46.3 | TDD | 296 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3231802 | 3 | 121.4681382841 | 31.1559785853 | 146 | 3 | 8 | 24.9 | TDD | 814 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.895 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.918 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.026 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.026 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.719 | NREventA3 | measId:2;ServCellPCI:458;Se... |
| 2024-09-20 22:21:37.959 | NRHandoverAttempt | SourcePCI:458;SourceNR-ARFC... |
| 2024-09-20 22:21:37.989 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.000 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.150 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.150 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226135 | 1 | 7.5527 | 10.8490 | -117.0186 | 10.2893 | 114.1178 | 0.0055 | 0.0064 |
| 2024_09_20 22:00 | 3212966 | 2 | 9.3507 | 16.0708 | -114.3382 | 13.5767 | 153.5608 | 0.0027 | 0.0122 |
| 2024_09_20 22:00 | 3231802 | 3 | 9.2394 | 14.2177 | -117.4528 | 7.9732 | 104.5318 | 0.0076 | 0.0166 |
| 2024_09_20 22:00 | 3216603 | 4 | 9.7888 | 10.7702 | -117.4652 | 18.5917 | 181.8937 | 0.0068 | 0.0038 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416254_BA333E0E | 504990 | 814 | -84.4 | 504990 | 167 | -91.1 | 504990 | 669 | -99.0 | 504990 | 296 |
| MR_1774416254_E43977C6 | 504990 | 814 | -84.9 | 504990 | 167 | -89.3 | 504990 | 669 | -99.1 | 504990 | 296 |
| MR_1774416254_9EAB2909 | 504990 | 814 | -83.7 | 504990 | 167 | -88.2 | 504990 | 669 | -96.4 | 504990 | 296 |
| MR_1774416254_5FDF9AF2 | 504990 | 814 | -87.0 | 504990 | 167 | -89.1 | 504990 | 669 | -97.8 | 504990 | 296 |
| MR_1774416254_66FB6E68 | 504990 | 814 | -86.6 | 504990 | 167 | -88.4 | 504990 | 669 | -97.3 | 504990 | 296 |
| MR_1774416254_B2CAF63C | 504990 | 814 | -83.6 | 504990 | 167 | -88.4 | 504990 | 669 | -96.9 | 504990 | 296 |
| MR_1774416254_46294D31 | 504990 | 814 | -87.0 | 504990 | 167 | -87.7 | 504990 | 669 | -99.4 | 504990 | 296 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 225: `44075c68-d11...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `44075c68-d113-4da3-b26c-6816ed868a96` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[225] topology](images/test_0225.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264809_1
- `C2`: Adjust the azimuth of 3264809_1 by 26 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274109_3
- `C4`: Add neighbor relationship between 3264809_1 and 3274109_3
- `C5`: Increase transmission power for 3264809_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264809_1
- `C7`: Lift the tilt angle of 3264809_1 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3264809_1
- `C9`: Increase A3 Offset threshold for 3274109_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274109_3
- `C11`: Lift the tilt angle  of 3274109_3 by 6 degrees
- `C12`: Decrease transmission power for 3274109_3
- `C13`: Add neighbor relationship between 3257646_4 and 3274109_3
- `C14`: Decrease transmission power for 3264809_1
- `C15`: Adjust the azimuth of 3274109_3 by 13 degrees
- `C16`: Check test server and transmission issues
- `C17`: Increase A3 Offset threshold for 3264809_1
- `C18`: Press down the tilt angle of 3264809_1 by 10 degrees
- `C19`: Increase transmission power for 3274109_3
- `C20`: Decrease A3 Offset threshold for 3274109_3
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Press down the tilt angle  of 3274109_3 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.492 | MS1 | 121.4656699506 | 31.1446186178 | 953 | 504990 | -76.06 | 14.00 | 595.14 | 0.08 | 2.76 | 1578 |
| 2024-09-20 22:21:32.117 | MS1 | 121.4656613661 | 31.1446271657 | 953 | 504990 | -77.14 | 15.86 | 327.56 | 0.15 | 2.18 | 1560 |
| 2024-09-20 22:21:33.395 | MS1 | 121.4656760525 | 31.1446328585 | 953 | 504990 | -75.58 | 13.52 | 564.19 | 0.19 | 2.11 | 1584 |
| 2024-09-20 22:21:34.723 | MS1 | 121.4656591380 | 31.1446287130 | 953 | 504990 | -91.91 | -0.79 | 33.26 | 0.12 | 1.41 | 1585 |
| 2024-09-20 22:21:35.254 | MS1 | 121.4656777258 | 31.1446232942 | 953 | 504990 | -90.51 | -0.43 | 43.73 | 0.13 | 1.08 | 1560 |
| 2024-09-20 22:21:36.626 | MS1 | 121.4656697665 | 31.1446291064 | 953 | 504990 | -93.89 | -1.65 | 33.54 | 0.20 | 1.17 | 1600 |
| 2024-09-20 22:21:37.327 | MS1 | 121.4656733854 | 31.1446188748 | 953 | 504990 | -88.35 | -1.01 | 49.94 | 0.12 | 1.48 | 1594 |
| 2024-09-20 22:21:38.689 | MS1 | 121.4656635681 | 31.1446314634 | 953 | 504990 | -82.13 | 14.20 | 443.41 | 0.16 | 1.16 | 1568 |
| 2024-09-20 22:21:39.651 | MS1 | 121.4656580493 | 31.1446186844 | 953 | 504990 | -80.18 | 16.45 | 508.79 | 0.07 | 1.27 | 1577 |
| 2024-09-20 22:21:40.718 | MS1 | 121.4656682027 | 31.1446287934 | 953 | 504990 | -75.68 | 13.88 | 505.46 | 0.09 | 2.03 | 1593 |
| 2024-09-20 22:21:41.561 | MS1 | 121.4656756116 | 31.1446288381 | 953 | 504990 | -76.76 | 15.81 | 434.09 | 0.09 | 2.10 | 1567 |
| 2024-09-20 22:21:42.854 | MS1 | 121.4656710231 | 31.1446328867 | 953 | 504990 | -79.91 | 17.96 | 376.42 | 0.04 | 2.66 | 1582 |

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
| 3257646 | 4 | 121.4725142513 | 31.1450247167 | 277 | 7 | 2 | 33.9 | TDD | 22 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3264809 | 1 | 121.4704136300 | 31.1519550919 | 235 | 10 | 4 | 44.2 | TDD | 953 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3273054 | 2 | 121.4670173052 | 31.1550759018 | 30 | 13 | 5 | 36.9 | TDD | 490 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3274109 | 3 | 121.4660144095 | 31.1493033141 | 197 | 1 | 11 | 42.0 | TDD | 534 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.972 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.098 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.098 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.788 | NREventA3 | measId:2;ServCellPCI:286;Se... |
| 2024-09-20 22:21:35.788 | NREventA3 | measId:2;ServCellPCI:286;Se... |
| 2024-09-20 22:21:36.788 | NREventA3 | measId:2;ServCellPCI:286;Se... |
| 2024-09-20 22:21:39.288 | NRRRCReestablishAttempt | PCI:286 |
| 2024-09-20 22:21:39.301 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.314 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.438 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.438 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264809 | 1 | 8.3238 | 17.4114 | -116.4099 | 16.6724 | 185.7626 | 0.0179 | 0.1126 |
| 2024_09_20 22:00 | 3273054 | 2 | 12.4174 | 19.2696 | -114.8711 | 12.3318 | 84.2671 | 0.0036 | 0.0009 |
| 2024_09_20 22:00 | 3274109 | 3 | 10.8644 | 15.0444 | -115.2142 | 8.6582 | 105.5703 | 0.0187 | 0.0021 |
| 2024_09_20 22:00 | 3257646 | 4 | 10.5890 | 17.9200 | -115.3517 | 10.9660 | 169.5993 | 0.0188 | 0.0049 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415463_084CBB34 | 504990 | 534 | -86.9 | 504990 | 953 | -92.4 | 504990 | 22 | -91.9 | 504990 | 490 |
| MR_1774415463_AB393995 | 504990 | 534 | -88.2 | 504990 | 953 | -91.9 | 504990 | 22 | -92.6 | 504990 | 490 |
| MR_1774415463_FA2B8CBB | 504990 | 953 | -90.7 | 504990 | 534 | -86.0 | 504990 | 22 | -93.7 | 504990 | 490 |
| MR_1774415463_4C1BD1DC | 504990 | 534 | -88.1 | 504990 | 953 | -92.0 | 504990 | 22 | -91.8 | 504990 | 490 |
| MR_1774415463_9127BA4E | 504990 | 953 | -91.1 | 504990 | 534 | -89.0 | 504990 | 22 | -94.2 | 504990 | 490 |
| MR_1774415463_71C50CC5 | 504990 | 953 | -93.5 | 504990 | 534 | -88.0 | 504990 | 22 | -90.8 | 504990 | 490 |
| MR_1774415463_6819557D | 504990 | 534 | -85.6 | 504990 | 953 | -92.6 | 504990 | 22 | -90.7 | 504990 | 490 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 226: `6ff19396-f8c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6ff19396-f8ca-414a-abe3-f05fa2290745` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[226] topology](images/test_0226.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3260398_4 by 6 degrees
- `C2`: Adjust the azimuth of 3276397_2 by 24 degrees
- `C3`: Increase A3 Offset threshold for 3276397_2
- `C4`: Increase A3 Offset threshold for 3260398_4
- `C5`: Add neighbor relationship between 3221619_3 and 3276397_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276397_2
- `C7`: Lift the tilt angle  of 3276397_2 by 1 degrees
- `C8`: Decrease A3 Offset threshold for 3276397_2
- `C9`: Decrease A3 Offset threshold for 3260398_4
- `C10`: Add neighbor relationship between 3260398_4 and 3276397_2
- `C11`: Press down the tilt angle  of 3276397_2 by 1 degrees
- `C12`: Lift the tilt angle of 3260398_4 by 6 degrees
- `C13`: Increase transmission power for 3260398_4
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Adjust the azimuth of 3260398_4 by 34 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276397_2
- `C17`: Increase transmission power for 3276397_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260398_4
- `C19`: Check test server and transmission issues
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260398_4
- `C21`: Decrease transmission power for 3276397_2
- `C22`: Decrease transmission power for 3260398_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.197 | MS1 | 121.4656775650 | 31.1446281777 | 390 | 504990 | -81.65 | 15.62 | 513.54 | 0.05 | 2.63 | 1561 |
| 2024-09-20 22:21:32.515 | MS1 | 121.4656728205 | 31.1446228258 | 390 | 504990 | -77.00 | 17.08 | 434.07 | 0.14 | 2.23 | 1572 |
| 2024-09-20 22:21:33.289 | MS1 | 121.4656757834 | 31.1446372802 | 390 | 504990 | -81.39 | 16.04 | 375.66 | 0.07 | 2.33 | 1578 |
| 2024-09-20 22:21:34.324 | MS1 | 121.4656612989 | 31.1446349127 | 390 | 504990 | -85.71 | 1.98 | 59.74 | 0.09 | 1.01 | 1566 |
| 2024-09-20 22:21:35.441 | MS1 | 121.4656650296 | 31.1446256110 | 390 | 504990 | -87.69 | 0.51 | 70.94 | 0.02 | 1.27 | 1568 |
| 2024-09-20 22:21:36.676 | MS1 | 121.4656695385 | 31.1446321061 | 390 | 504990 | -87.89 | 3.18 | 38.47 | 0.04 | 1.01 | 1600 |
| 2024-09-20 22:21:37.498 | MS1 | 121.4656747949 | 31.1446301455 | 390 | 504990 | -85.78 | 0.39 | 81.39 | 0.06 | 1.28 | 1599 |
| 2024-09-20 22:21:38.895 | MS1 | 121.4656775019 | 31.1446333357 | 390 | 504990 | -88.79 | 1.88 | 81.65 | 0.00 | 1.14 | 1581 |
| 2024-09-20 22:21:39.252 | MS1 | 121.4656604913 | 31.1446259651 | 390 | 504990 | -85.87 | 3.29 | 69.72 | 0.08 | 1.47 | 1597 |
| 2024-09-20 22:21:40.524 | MS1 | 121.4656589923 | 31.1446271969 | 390 | 504990 | -75.81 | 12.63 | 534.10 | 0.04 | 2.55 | 1591 |
| 2024-09-20 22:21:41.541 | MS1 | 121.4656606370 | 31.1446304846 | 390 | 504990 | -80.95 | 15.63 | 518.71 | 0.11 | 2.51 | 1579 |
| 2024-09-20 22:21:42.645 | MS1 | 121.4656677839 | 31.1446275547 | 390 | 504990 | -80.92 | 12.43 | 381.14 | 0.13 | 2.53 | 1585 |

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
| 3221619 | 3 | 121.4724356085 | 31.1555396402 | 80 | 0 | 8 | 45.6 | TDD | 755 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3226824 | 1 | 121.4679482669 | 31.1477689882 | 64 | 13 | 0 | 41.4 | TDD | 304 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3260398 | 4 | 121.4758200760 | 31.1528184390 | 261 | 4 | 0 | 43.3 | TDD | 390 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3276397 | 2 | 121.4703188668 | 31.1505705539 | 190 | 0 | 7 | 18.2 | TDD | 857 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.054 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.072 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.195 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.195 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226824 | 1 | 18.5827 | 5.7544 | -117.9463 | 18.8039 | 181.9847 | 0.0188 | 0.0115 |
| 2024_09_20 22:00 | 3276397 | 2 | 5.0548 | 12.8730 | -116.6330 | 11.6638 | 84.0199 | 0.0100 | 0.0135 |
| 2024_09_20 22:00 | 3221619 | 3 | 9.5810 | 5.8847 | -116.8822 | 14.0151 | 146.9638 | 0.0132 | 0.0095 |
| 2024_09_20 22:00 | 3260398 | 4 | 6.5840 | 12.1947 | -109.3241 | 12.8001 | 110.8833 | 0.0057 | 0.0129 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413261_8F711137 | 504990 | 390 | -86.7 | 504990 | 857 | -82.7 | 504990 | 755 | -87.4 | 504990 | 304 |
| MR_1774413261_ED91B8B7 | 504990 | 857 | -84.2 | 504990 | 390 | -85.6 | 504990 | 755 | -88.7 | 504990 | 304 |
| MR_1774413261_CD8D501E | 504990 | 857 | -86.6 | 504990 | 390 | -85.3 | 504990 | 755 | -86.1 | 504990 | 304 |
| MR_1774413261_93FB2FAD | 504990 | 857 | -85.0 | 504990 | 390 | -83.0 | 504990 | 755 | -87.5 | 504990 | 304 |
| MR_1774413261_AC40384E | 504990 | 390 | -86.6 | 504990 | 857 | -84.7 | 504990 | 755 | -87.3 | 504990 | 304 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 227: `6bdaaf60-162...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6bdaaf60-1628-4045-a667-e1cec698bdb4` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[227] topology](images/test_0227.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3212632_3 by 10 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Press down the tilt angle of 3212632_3 by 10 degrees
- `C4`: Decrease transmission power for 3214250_4
- `C5`: Press down the tilt angle  of 3214250_4 by 10 degrees
- `C6`: Lift the tilt angle  of 3214250_4 by 10 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212632_3
- `C8`: Adjust the azimuth of 3214250_4 by 50 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212632_3
- `C10`: Check test server and transmission issues
- `C11`: Decrease A3 Offset threshold for 3214250_4
- `C12`: Increase A3 Offset threshold for 3214250_4
- `C13`: Increase transmission power for 3214250_4
- `C14`: Increase transmission power for 3212632_3
- `C15`: Increase A3 Offset threshold for 3212632_3
- `C16`: Add neighbor relationship between 3212632_3 and 3214250_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214250_4
- `C18`: Adjust the azimuth of 3212632_3 by 50 degrees
- `C19`: Add neighbor relationship between 3255885_2 and 3214250_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214250_4
- `C21`: Decrease A3 Offset threshold for 3212632_3
- `C22`: Decrease transmission power for 3212632_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.854 | MS1 | 121.4656746326 | 31.1446335624 | 854 | 504990 | -85.22 | 13.08 | 409.65 | 0.14 | 2.47 | 1572 |
| 2024-09-20 22:21:32.204 | MS1 | 121.4656703501 | 31.1446206757 | 854 | 504990 | -90.64 | 15.44 | 472.48 | 0.07 | 2.05 | 1594 |
| 2024-09-20 22:21:33.567 | MS1 | 121.4656779879 | 31.1446304650 | 854 | 504990 | -91.22 | 17.39 | 431.56 | 0.05 | 2.79 | 1583 |
| 2024-09-20 22:21:34.459 | MS1 | 121.4656609044 | 31.1446187912 | 854 | 504990 | -86.87 | 15.61 | 83.47 | 0.19 | 2.11 | 383 |
| 2024-09-20 22:21:35.670 | MS1 | 121.4656586754 | 31.1446196572 | 854 | 504990 | -90.25 | 13.70 | 51.73 | 0.06 | 2.94 | 330 |
| 2024-09-20 22:21:36.146 | MS1 | 121.4656730200 | 31.1446303164 | 854 | 504990 | -89.70 | 13.77 | 71.10 | 0.12 | 2.06 | 485 |
| 2024-09-20 22:21:37.479 | MS1 | 121.4656627783 | 31.1446202557 | 854 | 504990 | -91.82 | 12.87 | 83.31 | 0.11 | 2.15 | 399 |
| 2024-09-20 22:21:38.217 | MS1 | 121.4656771418 | 31.1446276161 | 854 | 504990 | -90.25 | 11.62 | 100.12 | 0.09 | 2.43 | 320 |
| 2024-09-20 22:21:39.244 | MS1 | 121.4656761153 | 31.1446248452 | 854 | 504990 | -92.84 | 10.85 | 57.81 | 0.01 | 2.29 | 474 |
| 2024-09-20 22:21:40.173 | MS1 | 121.4656602195 | 31.1446332677 | 854 | 504990 | -89.10 | 8.21 | 454.04 | 0.15 | 2.79 | 1573 |
| 2024-09-20 22:21:41.840 | MS1 | 121.4656766624 | 31.1446256573 | 854 | 504990 | -90.52 | 7.68 | 585.41 | 0.05 | 2.96 | 1561 |
| 2024-09-20 22:21:42.194 | MS1 | 121.4656609556 | 31.1446292058 | 854 | 504990 | -93.35 | 11.62 | 462.13 | 0.07 | 2.12 | 1569 |

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
| 3212632 | 3 | 121.4674441610 | 31.1467911892 | 67 | 9 | 9 | 21.6 | TDD | 854 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3214250 | 4 | 121.4693315590 | 31.1444285934 | 184 | 15 | 0 | 37.8 | TDD | 703 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3255885 | 2 | 121.4687344252 | 31.1481583297 | 303 | 15 | 12 | 40.9 | TDD | 970 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3279695 | 1 | 121.4654141069 | 31.1456184682 | 166 | 9 | 11 | 36.5 | TDD | 512 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.081 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.105 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.212 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.212 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.950 | NREventA3 | measId:2;ServCellPCI:709;Se... |
| 2024-09-20 22:21:38.190 | NRHandoverAttempt | SourcePCI:709;SourceNR-ARFC... |
| 2024-09-20 22:21:38.228 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.241 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.381 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.381 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279695 | 1 | 9.7236 | 9.4361 | -116.9764 | 18.2932 | 168.6208 | 0.0029 | 0.0120 |
| 2024_09_20 22:00 | 3255885 | 2 | 8.5435 | 6.7130 | -117.9715 | 12.3910 | 113.1149 | 0.0117 | 0.0109 |
| 2024_09_20 22:00 | 3212632 | 3 | 16.7432 | 13.2198 | -117.6365 | 16.2787 | 144.7175 | 0.0091 | 0.0007 |
| 2024_09_20 22:00 | 3214250 | 4 | 8.6866 | 17.6532 | -117.1150 | 11.4810 | 177.3836 | 0.0015 | 0.0199 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416763_6D935802 | 504990 | 854 | -85.7 | 504990 | 703 | -87.6 | 504990 | 970 | -92.9 | 504990 | 512 |
| MR_1774416763_928FD2E2 | 504990 | 854 | -87.3 | 504990 | 703 | -88.6 | 504990 | 970 | -92.7 | 504990 | 512 |
| MR_1774416763_2FBA5EE5 | 504990 | 854 | -86.5 | 504990 | 703 | -87.0 | 504990 | 970 | -95.8 | 504990 | 512 |
| MR_1774416763_AE099C70 | 504990 | 854 | -88.1 | 504990 | 703 | -85.5 | 504990 | 970 | -92.4 | 504990 | 512 |
| MR_1774416763_5C1872AB | 504990 | 854 | -85.4 | 504990 | 703 | -87.5 | 504990 | 970 | -92.9 | 504990 | 512 |
| MR_1774416763_F0167F9D | 504990 | 854 | -85.8 | 504990 | 703 | -87.5 | 504990 | 970 | -92.5 | 504990 | 512 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 228: `3cb19161-fca...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3cb19161-fca9-4ac6-8e50-80dbfe33a544` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[228] topology](images/test_0228.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263169_1
- `C3`: Decrease transmission power for 3277394_2
- `C4`: Increase A3 Offset threshold for 3263169_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease A3 Offset threshold for 3277394_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277394_2
- `C8`: Lift the tilt angle  of 3263169_1 by 5 degrees
- `C9`: Press down the tilt angle  of 3263169_1 by 5 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277394_2
- `C11`: Decrease A3 Offset threshold for 3263169_1
- `C12`: Decrease transmission power for 3263169_1
- `C13`: Increase transmission power for 3277394_2
- `C14`: Adjust the azimuth of 3277394_2 by 11 degrees
- `C15`: Add neighbor relationship between 3233548_3 and 3263169_1
- `C16`: Adjust the azimuth of 3263169_1 by 50 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263169_1
- `C18`: Lift the tilt angle of 3277394_2 by 3 degrees
- `C19`: Increase A3 Offset threshold for 3277394_2
- `C20`: Add neighbor relationship between 3277394_2 and 3263169_1
- `C21`: Increase transmission power for 3263169_1
- `C22`: Press down the tilt angle of 3277394_2 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.127 | MS1 | 121.4656602504 | 31.1446335187 | 658 | 504990 | -81.03 | 16.73 | 420.92 | 0.15 | 3.00 | 1585 |
| 2024-09-20 22:21:32.140 | MS1 | 121.4656733574 | 31.1446266716 | 658 | 504990 | -76.61 | 13.91 | 440.32 | 0.16 | 2.49 | 1584 |
| 2024-09-20 22:21:33.837 | MS1 | 121.4656605345 | 31.1446350492 | 658 | 504990 | -77.35 | 14.86 | 601.49 | 0.12 | 2.96 | 1584 |
| 2024-09-20 22:21:34.684 | MS1 | 121.4656760630 | 31.1446372479 | 658 | 504990 | -88.56 | -0.53 | 64.16 | 0.11 | 1.05 | 1565 |
| 2024-09-20 22:21:35.268 | MS1 | 121.4656657924 | 31.1446339088 | 658 | 504990 | -83.93 | -0.33 | 76.43 | 0.07 | 1.18 | 1585 |
| 2024-09-20 22:21:36.625 | MS1 | 121.4656690645 | 31.1446379698 | 658 | 504990 | -87.64 | -2.62 | 27.77 | 0.10 | 1.34 | 1563 |
| 2024-09-20 22:21:37.486 | MS1 | 121.4656641649 | 31.1446207210 | 658 | 504990 | -88.54 | -3.17 | 69.05 | 0.12 | 1.48 | 1567 |
| 2024-09-20 22:21:38.450 | MS1 | 121.4656701530 | 31.1446256288 | 658 | 504990 | -92.78 | -3.96 | 74.64 | 0.03 | 1.01 | 1560 |
| 2024-09-20 22:21:39.937 | MS1 | 121.4656670060 | 31.1446375663 | 432 | 504990 | -83.01 | 16.11 | 216.56 | 0.06 | 1.29 | 1573 |
| 2024-09-20 22:21:40.867 | MS1 | 121.4656621616 | 31.1446267231 | 432 | 504990 | -81.61 | 13.00 | 465.29 | 0.08 | 2.31 | 1586 |
| 2024-09-20 22:21:41.819 | MS1 | 121.4656730415 | 31.1446254891 | 432 | 504990 | -79.63 | 17.64 | 404.57 | 0.05 | 2.12 | 1597 |
| 2024-09-20 22:21:42.542 | MS1 | 121.4656734667 | 31.1446190197 | 432 | 504990 | -78.78 | 15.89 | 423.31 | 0.18 | 2.76 | 1562 |

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
| 3233548 | 3 | 121.4734754617 | 31.1558103934 | 252 | 9 | 3 | 46.0 | TDD | 182 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3234086 | 4 | 121.4747056468 | 31.1476692095 | 141 | 4 | 9 | 28.8 | TDD | 959 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3263169 | 1 | 121.4709725081 | 31.1483578003 | 60 | 1 | 4 | 44.4 | TDD | 432 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3277394 | 2 | 121.4742987482 | 31.1550989059 | 204 | 2 | 10 | 34.1 | TDD | 658 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.425 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.449 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.553 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.553 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.267 | NREventA3 | measId:2;ServCellPCI:218;Se... |
| 2024-09-20 22:21:38.507 | NRHandoverAttempt | SourcePCI:218;SourceNR-ARFC... |
| 2024-09-20 22:21:38.552 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.562 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.663 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.663 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263169 | 1 | 12.9421 | 5.8984 | -114.7288 | 14.3406 | 196.0300 | 0.0112 | 0.0136 |
| 2024_09_20 22:00 | 3277394 | 2 | 5.1272 | 13.0328 | -115.7948 | 15.0914 | 173.2252 | 0.0085 | 0.1210 |
| 2024_09_20 22:00 | 3233548 | 3 | 17.5778 | 15.4518 | -117.1758 | 14.2368 | 174.1689 | 0.0024 | 0.0180 |
| 2024_09_20 22:00 | 3234086 | 4 | 9.4805 | 18.6965 | -114.7460 | 17.9415 | 158.7607 | 0.0088 | 0.0171 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415568_42078868 | 504990 | 432 | -81.5 | 504990 | 658 | -88.4 | 504990 | 182 | -84.2 | 504990 | 959 |
| MR_1774415568_9DB4AC27 | 504990 | 432 | -83.1 | 504990 | 658 | -89.2 | 504990 | 182 | -85.5 | 504990 | 959 |
| MR_1774415568_13BC8EF8 | 504990 | 658 | -90.4 | 504990 | 432 | -84.8 | 504990 | 182 | -85.0 | 504990 | 959 |
| MR_1774415568_3521EB1D | 504990 | 432 | -83.0 | 504990 | 658 | -89.8 | 504990 | 182 | -83.0 | 504990 | 959 |
| MR_1774415568_7BCAE0CB | 504990 | 658 | -89.6 | 504990 | 432 | -82.7 | 504990 | 182 | -83.2 | 504990 | 959 |
| MR_1774415568_31D788CC | 504990 | 658 | -89.1 | 504990 | 432 | -81.6 | 504990 | 182 | -86.0 | 504990 | 959 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 229: `73a957d1-fa8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `73a957d1-fa8b-43d6-9828-e7c145346e87` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[229] topology](images/test_0229.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3255829_2 by 50 degrees
- `C2`: Press down the tilt angle of 3255829_2 by 10 degrees
- `C3`: Lift the tilt angle of 3255829_2 by 10 degrees
- `C4`: Decrease transmission power for 3255829_2
- `C5`: Increase A3 Offset threshold for 3217225_3
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase transmission power for 3255829_2
- `C8`: Check test server and transmission issues
- `C9`: Add neighbor relationship between 3258384_1 and 3217225_3
- `C10`: Lift the tilt angle  of 3217225_3 by 5 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217225_3
- `C12`: Decrease A3 Offset threshold for 3217225_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255829_2
- `C14`: Adjust the azimuth of 3217225_3 by 42 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255829_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217225_3
- `C17`: Increase A3 Offset threshold for 3255829_2
- `C18`: Decrease A3 Offset threshold for 3255829_2
- `C19`: Add neighbor relationship between 3255829_2 and 3217225_3
- `C20`: Decrease transmission power for 3217225_3
- `C21`: Press down the tilt angle  of 3217225_3 by 5 degrees
- `C22`: Increase transmission power for 3217225_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.410 | MS1 | 121.4656709846 | 31.1446222874 | 249 | 504990 | -76.95 | 12.00 | 319.83 | 0.08 | 2.25 | 1585 |
| 2024-09-20 22:21:32.472 | MS1 | 121.4656767827 | 31.1446347416 | 249 | 504990 | -81.96 | 16.81 | 516.16 | 0.16 | 2.66 | 1589 |
| 2024-09-20 22:21:33.932 | MS1 | 121.4656736067 | 31.1446291707 | 249 | 504990 | -76.01 | 15.85 | 555.27 | 0.19 | 2.80 | 1588 |
| 2024-09-20 22:21:34.644 | MS1 | 121.4656703891 | 31.1446211797 | 249 | 504990 | -90.44 | -2.07 | 42.75 | 0.08 | 1.07 | 1582 |
| 2024-09-20 22:21:35.559 | MS1 | 121.4656741498 | 31.1446189737 | 249 | 504990 | -94.10 | -0.14 | 53.44 | 0.11 | 1.29 | 1593 |
| 2024-09-20 22:21:36.779 | MS1 | 121.4656588107 | 31.1446357859 | 249 | 504990 | -89.91 | -1.87 | 50.81 | 0.17 | 1.50 | 1572 |
| 2024-09-20 22:21:37.443 | MS1 | 121.4656663308 | 31.1446312023 | 249 | 504990 | -86.63 | -2.52 | 69.79 | 0.11 | 1.35 | 1596 |
| 2024-09-20 22:21:38.504 | MS1 | 121.4656634536 | 31.1446353778 | 249 | 504990 | -77.21 | 17.96 | 484.94 | 0.14 | 1.27 | 1575 |
| 2024-09-20 22:21:39.797 | MS1 | 121.4656700647 | 31.1446201493 | 249 | 504990 | -79.10 | 12.39 | 368.11 | 0.12 | 1.43 | 1562 |
| 2024-09-20 22:21:40.389 | MS1 | 121.4656630797 | 31.1446273958 | 249 | 504990 | -76.25 | 16.43 | 352.69 | 0.10 | 2.56 | 1574 |
| 2024-09-20 22:21:41.290 | MS1 | 121.4656705648 | 31.1446198520 | 249 | 504990 | -79.31 | 15.98 | 413.73 | 0.13 | 2.54 | 1597 |
| 2024-09-20 22:21:42.970 | MS1 | 121.4656711793 | 31.1446347935 | 249 | 504990 | -79.42 | 16.63 | 470.32 | 0.00 | 2.81 | 1598 |

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
| 3215763 | 4 | 121.4666761036 | 31.1535879833 | 356 | 12 | 7 | 24.2 | TDD | 579 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3217225 | 3 | 121.4705131834 | 31.1441982595 | 234 | 3 | 1 | 18.2 | TDD | 610 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3255829 | 2 | 121.4663515376 | 31.1528485909 | 97 | 11 | 6 | 40.8 | TDD | 249 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3258384 | 1 | 121.4735033271 | 31.1498982681 | 201 | 9 | 12 | 16.7 | TDD | 392 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.229 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.249 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.352 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.352 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.072 | NREventA3 | measId:2;ServCellPCI:348;Se... |
| 2024-09-20 22:21:36.072 | NREventA3 | measId:2;ServCellPCI:348;Se... |
| 2024-09-20 22:21:37.072 | NREventA3 | measId:2;ServCellPCI:348;Se... |
| 2024-09-20 22:21:39.572 | NRRRCReestablishAttempt | PCI:348 |
| 2024-09-20 22:21:39.583 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.594 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.732 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.732 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258384 | 1 | 6.9962 | 9.9430 | -115.9461 | 9.1295 | 132.6846 | 0.0027 | 0.0138 |
| 2024_09_20 22:00 | 3255829 | 2 | 8.2686 | 8.5831 | -116.7447 | 7.6291 | 179.6433 | 0.0004 | 0.1075 |
| 2024_09_20 22:00 | 3217225 | 3 | 15.0993 | 6.1229 | -116.6292 | 15.8821 | 168.5839 | 0.0017 | 0.0200 |
| 2024_09_20 22:00 | 3215763 | 4 | 8.0566 | 15.2117 | -116.9631 | 9.9453 | 115.3423 | 0.0093 | 0.0040 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413699_B3A2E4EE | 504990 | 610 | -87.7 | 504990 | 249 | -92.4 | 504990 | 392 | -94.3 | 504990 | 579 |
| MR_1774413699_A1A4D487 | 504990 | 610 | -87.4 | 504990 | 249 | -88.9 | 504990 | 392 | -95.6 | 504990 | 579 |
| MR_1774413699_4E5F04B6 | 504990 | 249 | -88.9 | 504990 | 610 | -87.6 | 504990 | 392 | -92.2 | 504990 | 579 |
| MR_1774413699_52DE1957 | 504990 | 610 | -84.1 | 504990 | 249 | -89.5 | 504990 | 392 | -92.7 | 504990 | 579 |
| MR_1774413699_2183D09B | 504990 | 249 | -91.4 | 504990 | 610 | -85.3 | 504990 | 392 | -94.8 | 504990 | 579 |

> *... 2개 열 생략 (전체 14열)*

---
