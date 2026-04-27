# Track A 문제 분석 — test[380]~test[389]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[380] ~ test[389] (10개)

## 목차

1. [문제 380: `19077dd1-dd8...`](#380) — single-answer
2. [문제 381: `e11e78d7-5e8...`](#381) — single-answer
3. [문제 382: `1c0c8a27-a6b...`](#382) — single-answer
4. [문제 383: `cc0dfd0c-787...`](#383) — single-answer
5. [문제 384: `89c591f4-5bb...`](#384) — single-answer
6. [문제 385: `53b4fc0a-3c8...`](#385) — single-answer
7. [문제 386: `e943b1d6-559...`](#386) — multiple-answer
8. [문제 387: `f201f1dc-655...`](#387) — multiple-answer
9. [문제 388: `27eda095-b6c...`](#388) — single-answer
10. [문제 389: `ca01d1a5-79a...`](#389) — single-answer

---

### 문제 380: `19077dd1-dd8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `19077dd1-dd86-40ee-bd61-66dbeaa07335` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[380] topology](images/test_0380.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3262780_2 by 10 degrees
- `C2`: Increase transmission power for 3262780_2
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Adjust the azimuth of 3255917_3 by 50 degrees
- `C5`: Lift the tilt angle of 3255917_3 by 10 degrees
- `C6`: Increase A3 Offset threshold for 3255917_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262780_2
- `C8`: Adjust the azimuth of 3262780_2 by 50 degrees
- `C9`: Lift the tilt angle  of 3262780_2 by 10 degrees
- `C10`: Decrease A3 Offset threshold for 3262780_2
- `C11`: Decrease transmission power for 3255917_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255917_3
- `C13`: Decrease transmission power for 3262780_2
- `C14`: Add neighbor relationship between 3255917_3 and 3262780_2
- `C15`: Add neighbor relationship between 3275208_4 and 3262780_2
- `C16`: Check test server and transmission issues
- `C17`: Press down the tilt angle of 3255917_3 by 10 degrees
- `C18`: Increase transmission power for 3255917_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255917_3
- `C20`: Increase A3 Offset threshold for 3262780_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262780_2
- `C22`: Decrease A3 Offset threshold for 3255917_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.792 | MS1 | 121.4656646594 | 31.1446225849 | 596 | 504990 | -86.52 | 13.34 | 594.12 | 0.18 | 2.35 | 1583 |
| 2024-09-20 22:21:32.517 | MS1 | 121.4656655190 | 31.1446359829 | 596 | 504990 | -87.98 | 12.82 | 345.71 | 0.09 | 2.21 | 1590 |
| 2024-09-20 22:21:33.321 | MS1 | 121.4656736906 | 31.1446223597 | 596 | 504990 | -87.46 | 12.73 | 556.41 | 0.14 | 2.64 | 1571 |
| 2024-09-20 22:21:34.879 | MS1 | 121.4656666373 | 31.1446240882 | 596 | 504990 | -91.89 | 17.86 | 55.71 | 0.05 | 2.38 | 345 |
| 2024-09-20 22:21:35.828 | MS1 | 121.4656723352 | 31.1446311326 | 596 | 504990 | -85.42 | 12.50 | 107.31 | 0.05 | 2.77 | 335 |
| 2024-09-20 22:21:36.638 | MS1 | 121.4656661566 | 31.1446350416 | 596 | 504990 | -89.43 | 15.79 | 59.33 | 0.15 | 2.75 | 308 |
| 2024-09-20 22:21:37.356 | MS1 | 121.4656714826 | 31.1446181826 | 596 | 504990 | -91.62 | 8.30 | 84.10 | 0.14 | 2.56 | 467 |
| 2024-09-20 22:21:38.449 | MS1 | 121.4656640186 | 31.1446347295 | 596 | 504990 | -90.45 | 8.64 | 60.38 | 0.11 | 2.85 | 498 |
| 2024-09-20 22:21:39.660 | MS1 | 121.4656605422 | 31.1446180050 | 596 | 504990 | -92.49 | 8.70 | 84.56 | 0.05 | 2.54 | 329 |
| 2024-09-20 22:21:40.234 | MS1 | 121.4656745597 | 31.1446181906 | 596 | 504990 | -93.18 | 8.43 | 478.87 | 0.01 | 3.00 | 1571 |
| 2024-09-20 22:21:41.954 | MS1 | 121.4656737102 | 31.1446234137 | 596 | 504990 | -92.24 | 7.54 | 447.58 | 0.12 | 2.92 | 1597 |
| 2024-09-20 22:21:42.829 | MS1 | 121.4656683144 | 31.1446199625 | 596 | 504990 | -91.63 | 12.65 | 583.98 | 0.01 | 2.02 | 1579 |

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
| 3220180 | 1 | 121.4693186762 | 31.1483888203 | 250 | 6 | 8 | 43.2 | TDD | 40 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3255917 | 3 | 121.4712797058 | 31.1540131625 | 263 | 10 | 1 | 46.8 | TDD | 596 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3262780 | 2 | 121.4676865017 | 31.1441089891 | 355 | 1 | 5 | 40.3 | TDD | 197 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3275208 | 4 | 121.4748018768 | 31.1493039683 | 266 | 15 | 9 | 23.8 | TDD | 245 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.703 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.720 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.849 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.849 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.600 | NREventA3 | measId:2;ServCellPCI:994;Se... |
| 2024-09-20 22:21:37.840 | NRHandoverAttempt | SourcePCI:994;SourceNR-ARFC... |
| 2024-09-20 22:21:37.889 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.901 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.003 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.003 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220180 | 1 | 8.3399 | 16.9931 | -116.0026 | 13.9976 | 129.9757 | 0.0014 | 0.0084 |
| 2024_09_20 22:00 | 3262780 | 2 | 7.2919 | 12.2558 | -116.0188 | 16.8831 | 102.5266 | 0.0021 | 0.0059 |
| 2024_09_20 22:00 | 3255917 | 3 | 5.9624 | 19.8401 | -115.1142 | 19.9471 | 164.9810 | 0.0068 | 0.0150 |
| 2024_09_20 22:00 | 3275208 | 4 | 16.7611 | 7.3073 | -117.3630 | 8.3352 | 112.4351 | 0.0124 | 0.0100 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412823_E6F9575E | 504990 | 596 | -93.0 | 504990 | 197 | -101.6 | 504990 | 245 | -101.9 | 504990 | 40 |
| MR_1774412823_B4975EAE | 504990 | 596 | -90.7 | 504990 | 197 | -101.8 | 504990 | 245 | -100.7 | 504990 | 40 |
| MR_1774412823_81A7208F | 504990 | 596 | -92.0 | 504990 | 197 | -100.2 | 504990 | 245 | -102.1 | 504990 | 40 |
| MR_1774412823_839944AD | 504990 | 596 | -93.5 | 504990 | 197 | -102.9 | 504990 | 245 | -101.5 | 504990 | 40 |
| MR_1774412823_D2250E18 | 504990 | 596 | -90.0 | 504990 | 197 | -100.6 | 504990 | 245 | -101.9 | 504990 | 40 |
| MR_1774412823_35FC91A2 | 504990 | 596 | -93.0 | 504990 | 197 | -102.5 | 504990 | 245 | -101.1 | 504990 | 40 |
| MR_1774412823_56B1FDF6 | 504990 | 596 | -92.8 | 504990 | 197 | -100.8 | 504990 | 245 | -103.7 | 504990 | 40 |
| MR_1774412823_A15CFAD3 | 504990 | 596 | -90.9 | 504990 | 197 | -102.4 | 504990 | 245 | -103.5 | 504990 | 40 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 381: `e11e78d7-5e8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e11e78d7-5e83-4420-8d92-7359d0b21c3f` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[381] topology](images/test_0381.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3226696_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226696_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266124_1
- `C4`: Decrease transmission power for 3226696_4
- `C5`: Decrease A3 Offset threshold for 3266124_1
- `C6`: Lift the tilt angle  of 3266124_1 by 4 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226696_4
- `C9`: Adjust the azimuth of 3226696_4 by 50 degrees
- `C10`: Press down the tilt angle  of 3266124_1 by 4 degrees
- `C11`: Increase transmission power for 3226696_4
- `C12`: Adjust the azimuth of 3266124_1 by 41 degrees
- `C13`: Increase transmission power for 3266124_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266124_1
- `C15`: Press down the tilt angle of 3226696_4 by 3 degrees
- `C16`: Increase A3 Offset threshold for 3226696_4
- `C17`: Increase A3 Offset threshold for 3266124_1
- `C18`: Check test server and transmission issues
- `C19`: Add neighbor relationship between 3226696_4 and 3266124_1
- `C20`: Lift the tilt angle of 3226696_4 by 3 degrees
- `C21`: Add neighbor relationship between 3264961_3 and 3266124_1
- `C22`: Decrease transmission power for 3266124_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.336 | MS1 | 121.4656662131 | 31.1446187239 | 407 | 504990 | -78.19 | 13.59 | 563.43 | 0.03 | 2.16 | 1575 |
| 2024-09-20 22:21:32.714 | MS1 | 121.4656660170 | 31.1446355330 | 407 | 504990 | -84.85 | 13.42 | 425.59 | 0.18 | 2.21 | 1600 |
| 2024-09-20 22:21:33.816 | MS1 | 121.4656676899 | 31.1446198682 | 407 | 504990 | -81.14 | 14.14 | 450.33 | 0.14 | 2.89 | 1589 |
| 2024-09-20 22:21:34.838 | MS1 | 121.4656701254 | 31.1446220011 | 407 | 504990 | -89.49 | -2.28 | 47.99 | 0.10 | 1.38 | 1569 |
| 2024-09-20 22:21:35.652 | MS1 | 121.4656580530 | 31.1446374916 | 407 | 504990 | -91.24 | -1.16 | 67.16 | 0.06 | 1.16 | 1597 |
| 2024-09-20 22:21:36.469 | MS1 | 121.4656610061 | 31.1446227958 | 407 | 504990 | -85.78 | -3.09 | 31.53 | 0.18 | 1.40 | 1594 |
| 2024-09-20 22:21:37.198 | MS1 | 121.4656751942 | 31.1446307094 | 407 | 504990 | -90.71 | -3.95 | 30.35 | 0.15 | 1.25 | 1591 |
| 2024-09-20 22:21:38.649 | MS1 | 121.4656631079 | 31.1446226100 | 407 | 504990 | -83.30 | 15.89 | 325.34 | 0.14 | 1.41 | 1562 |
| 2024-09-20 22:21:39.732 | MS1 | 121.4656623524 | 31.1446260411 | 407 | 504990 | -83.30 | 13.18 | 411.35 | 0.03 | 1.01 | 1599 |
| 2024-09-20 22:21:40.667 | MS1 | 121.4656682985 | 31.1446213664 | 407 | 504990 | -79.02 | 12.41 | 343.23 | 0.12 | 2.16 | 1599 |
| 2024-09-20 22:21:41.550 | MS1 | 121.4656692111 | 31.1446316856 | 407 | 504990 | -80.78 | 13.16 | 432.33 | 0.09 | 2.51 | 1587 |
| 2024-09-20 22:21:42.614 | MS1 | 121.4656753940 | 31.1446306001 | 407 | 504990 | -77.13 | 16.78 | 599.66 | 0.07 | 2.89 | 1568 |

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
| 3226696 | 4 | 121.4738865862 | 31.1543858171 | 14 | 1 | 8 | 50.0 | TDD | 407 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3264395 | 2 | 121.4692740440 | 31.1549495656 | 306 | 2 | 2 | 18.9 | TDD | 620 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3264961 | 3 | 121.4680696838 | 31.1553094731 | 42 | 7 | 2 | 21.2 | TDD | 765 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3266124 | 1 | 121.4668904192 | 31.1516208453 | 147 | 0 | 3 | 49.6 | TDD | 962 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.077 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.094 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.210 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.210 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.945 | NREventA3 | measId:2;ServCellPCI:591;Se... |
| 2024-09-20 22:21:35.945 | NREventA3 | measId:2;ServCellPCI:591;Se... |
| 2024-09-20 22:21:36.945 | NREventA3 | measId:2;ServCellPCI:591;Se... |
| 2024-09-20 22:21:39.445 | NRRRCReestablishAttempt | PCI:591 |
| 2024-09-20 22:21:39.456 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.466 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.607 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.607 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266124 | 1 | 11.3531 | 9.2949 | -115.8490 | 18.2879 | 169.1511 | 0.0182 | 0.0010 |
| 2024_09_20 22:00 | 3264395 | 2 | 10.7701 | 13.5877 | -114.4191 | 13.4350 | 139.2184 | 0.0067 | 0.0020 |
| 2024_09_20 22:00 | 3264961 | 3 | 11.8769 | 19.5892 | -115.9959 | 12.7875 | 198.0936 | 0.0163 | 0.0153 |
| 2024_09_20 22:00 | 3226696 | 4 | 12.1684 | 12.6786 | -115.1563 | 14.2716 | 124.5999 | 0.0132 | 0.1035 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417116_6829DA34 | 504990 | 407 | -91.0 | 504990 | 962 | -84.4 | 504990 | 765 | -84.6 | 504990 | 620 |
| MR_1774417116_932B1BC4 | 504990 | 962 | -84.1 | 504990 | 407 | -88.0 | 504990 | 765 | -85.1 | 504990 | 620 |
| MR_1774417116_A6B770C6 | 504990 | 407 | -88.4 | 504990 | 962 | -85.8 | 504990 | 765 | -84.2 | 504990 | 620 |
| MR_1774417116_F501C389 | 504990 | 407 | -88.0 | 504990 | 962 | -83.6 | 504990 | 765 | -84.9 | 504990 | 620 |
| MR_1774417116_C6DABEDC | 504990 | 407 | -89.0 | 504990 | 962 | -85.9 | 504990 | 765 | -85.3 | 504990 | 620 |
| MR_1774417116_5C53FD9A | 504990 | 407 | -89.0 | 504990 | 962 | -84.6 | 504990 | 765 | -86.7 | 504990 | 620 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 382: `1c0c8a27-a6b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1c0c8a27-a6be-46fd-ab1f-1d7a753f8859` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[382] topology](images/test_0382.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3218458_3 by 10 degrees
- `C2`: Decrease transmission power for 3248902_2
- `C3`: Increase A3 Offset threshold for 3248902_2
- `C4`: Decrease A3 Offset threshold for 3248902_2
- `C5`: Add neighbor relationship between 3218458_3 and 3248902_2
- `C6`: Decrease A3 Offset threshold for 3218458_3
- `C7`: Increase transmission power for 3248902_2
- `C8`: Lift the tilt angle  of 3248902_2 by 10 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218458_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218458_3
- `C11`: Increase A3 Offset threshold for 3218458_3
- `C12`: Check test server and transmission issues
- `C13`: Decrease transmission power for 3218458_3
- `C14`: Press down the tilt angle  of 3248902_2 by 10 degrees
- `C15`: Adjust the azimuth of 3248902_2 by 0 degrees
- `C16`: Add neighbor relationship between 3234959_1 and 3248902_2
- `C17`: Adjust the azimuth of 3218458_3 by 50 degrees
- `C18`: Press down the tilt angle of 3218458_3 by 10 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248902_2
- `C20`: Increase transmission power for 3218458_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248902_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.377 | MS1 | 121.4656608022 | 31.1446296221 | 884 | 504990 | -90.48 | 15.39 | 485.66 | 0.07 | 2.93 | 1589 |
| 2024-09-20 22:21:32.663 | MS1 | 121.4656707363 | 31.1446234721 | 884 | 504990 | -87.47 | 17.38 | 539.70 | 0.13 | 2.43 | 1566 |
| 2024-09-20 22:21:33.907 | MS1 | 121.4656643003 | 31.1446294340 | 884 | 504990 | -89.97 | 16.35 | 325.39 | 0.07 | 2.38 | 1571 |
| 2024-09-20 22:21:34.998 | MS1 | 121.4656638329 | 31.1446198478 | 884 | 504990 | -90.81 | 13.36 | 62.22 | 0.05 | 2.68 | 328 |
| 2024-09-20 22:21:35.531 | MS1 | 121.4656622470 | 31.1446371921 | 884 | 504990 | -87.08 | 15.20 | 58.93 | 0.09 | 2.58 | 316 |
| 2024-09-20 22:21:36.329 | MS1 | 121.4656669680 | 31.1446320412 | 884 | 504990 | -86.35 | 17.88 | 99.00 | 0.11 | 2.01 | 325 |
| 2024-09-20 22:21:37.440 | MS1 | 121.4656591132 | 31.1446188324 | 884 | 504990 | -90.39 | 11.22 | 85.46 | 0.08 | 2.27 | 459 |
| 2024-09-20 22:21:38.202 | MS1 | 121.4656594156 | 31.1446236913 | 884 | 504990 | -93.42 | 7.61 | 90.75 | 0.14 | 2.83 | 419 |
| 2024-09-20 22:21:39.128 | MS1 | 121.4656695444 | 31.1446329722 | 884 | 504990 | -89.57 | 7.06 | 59.13 | 0.15 | 2.63 | 419 |
| 2024-09-20 22:21:40.333 | MS1 | 121.4656667179 | 31.1446265281 | 884 | 504990 | -91.42 | 9.46 | 490.71 | 0.01 | 2.68 | 1584 |
| 2024-09-20 22:21:41.358 | MS1 | 121.4656700031 | 31.1446323818 | 884 | 504990 | -91.47 | 7.74 | 511.01 | 0.13 | 2.50 | 1568 |
| 2024-09-20 22:21:42.793 | MS1 | 121.4656716267 | 31.1446362893 | 884 | 504990 | -92.86 | 10.50 | 385.29 | 0.16 | 2.04 | 1570 |

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
| 3218458 | 3 | 121.4690591344 | 31.1498330409 | 270 | 9 | 3 | 24.6 | TDD | 884 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3229695 | 4 | 121.4743359135 | 31.1448365977 | 353 | 2 | 6 | 36.9 | TDD | 61 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3234959 | 1 | 121.4666612182 | 31.1465667963 | 326 | 13 | 4 | 21.2 | TDD | 761 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3248902 | 2 | 121.4701176555 | 31.1512476208 | 210 | 10 | 11 | 17.6 | TDD | 357 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.270 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.286 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.429 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.429 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.089 | NREventA3 | measId:2;ServCellPCI:943;Se... |
| 2024-09-20 22:21:38.329 | NRHandoverAttempt | SourcePCI:943;SourceNR-ARFC... |
| 2024-09-20 22:21:38.364 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.376 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.478 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.478 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234959 | 1 | 12.2300 | 9.1338 | -116.9252 | 18.0148 | 115.5503 | 0.0012 | 0.0182 |
| 2024_09_20 22:00 | 3248902 | 2 | 9.1859 | 18.6165 | -116.0792 | 15.2204 | 140.8766 | 0.0035 | 0.0030 |
| 2024_09_20 22:00 | 3218458 | 3 | 17.2408 | 14.6715 | -116.2384 | 11.3440 | 105.2457 | 0.0097 | 0.0074 |
| 2024_09_20 22:00 | 3229695 | 4 | 17.3491 | 9.1068 | -114.8296 | 6.5470 | 83.3856 | 0.0005 | 0.0164 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412253_F487EF8A | 504990 | 884 | -92.5 | 504990 | 357 | -99.4 | 504990 | 761 | -103.6 | 504990 | 61 |
| MR_1774412253_9D02F10B | 504990 | 884 | -92.7 | 504990 | 357 | -99.5 | 504990 | 761 | -102.6 | 504990 | 61 |
| MR_1774412253_BA816238 | 504990 | 884 | -89.6 | 504990 | 357 | -97.6 | 504990 | 761 | -101.9 | 504990 | 61 |
| MR_1774412253_96FB1E38 | 504990 | 884 | -89.2 | 504990 | 357 | -98.7 | 504990 | 761 | -103.9 | 504990 | 61 |
| MR_1774412253_82D1940D | 504990 | 884 | -89.5 | 504990 | 357 | -100.4 | 504990 | 761 | -103.5 | 504990 | 61 |
| MR_1774412253_C695F927 | 504990 | 884 | -89.4 | 504990 | 357 | -99.3 | 504990 | 761 | -105.1 | 504990 | 61 |
| MR_1774412253_6B58400B | 504990 | 884 | -90.6 | 504990 | 357 | -97.9 | 504990 | 761 | -104.0 | 504990 | 61 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 383: `cc0dfd0c-787...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cc0dfd0c-7874-46a6-87d0-ac2e9f260f12` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[383] topology](images/test_0383.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245571_2
- `C2`: Add neighbor relationship between 3212461_3 and 3261773_1
- `C3`: Increase transmission power for 3261773_1
- `C4`: Check test server and transmission issues
- `C5`: Decrease transmission power for 3245571_2
- `C6`: Increase A3 Offset threshold for 3261773_1
- `C7`: Press down the tilt angle of 3245571_2 by 1 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261773_1
- `C9`: Decrease transmission power for 3261773_1
- `C10`: Press down the tilt angle  of 3261773_1 by 10 degrees
- `C11`: Decrease A3 Offset threshold for 3261773_1
- `C12`: Lift the tilt angle of 3245571_2 by 1 degrees
- `C13`: Increase A3 Offset threshold for 3245571_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261773_1
- `C15`: Lift the tilt angle  of 3261773_1 by 10 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase transmission power for 3245571_2
- `C18`: Decrease A3 Offset threshold for 3245571_2
- `C19`: Add neighbor relationship between 3245571_2 and 3261773_1
- `C20`: Adjust the azimuth of 3261773_1 by 50 degrees
- `C21`: Adjust the azimuth of 3245571_2 by 21 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245571_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.464 | MS1 | 121.4656650495 | 31.1446377208 | 162 | 504990 | -87.84 | 12.13 | 489.28 | 0.08 | 2.45 | 1590 |
| 2024-09-20 22:21:32.183 | MS1 | 121.4656758767 | 31.1446347854 | 162 | 504990 | -90.53 | 15.60 | 343.14 | 0.14 | 2.46 | 1579 |
| 2024-09-20 22:21:33.670 | MS1 | 121.4656761959 | 31.1446212640 | 162 | 504990 | -88.32 | 13.59 | 486.35 | 0.11 | 2.54 | 1600 |
| 2024-09-20 22:21:34.941 | MS1 | 121.4656738893 | 31.1446248059 | 162 | 504990 | -89.18 | 16.04 | 59.01 | 0.55 | 2.36 | 619 |
| 2024-09-20 22:21:35.694 | MS1 | 121.4656740375 | 31.1446284293 | 162 | 504990 | -91.35 | 15.76 | 84.08 | 0.64 | 2.45 | 673 |
| 2024-09-20 22:21:36.215 | MS1 | 121.4656633114 | 31.1446361116 | 162 | 504990 | -85.14 | 14.60 | 46.71 | 0.57 | 2.93 | 521 |
| 2024-09-20 22:21:37.857 | MS1 | 121.4656589500 | 31.1446191119 | 162 | 504990 | -89.20 | 7.11 | 107.77 | 0.54 | 2.20 | 550 |
| 2024-09-20 22:21:38.407 | MS1 | 121.4656759914 | 31.1446307835 | 162 | 504990 | -93.40 | 9.10 | 95.88 | 0.59 | 2.80 | 655 |
| 2024-09-20 22:21:39.922 | MS1 | 121.4656604336 | 31.1446298099 | 162 | 504990 | -89.75 | 12.93 | 74.30 | 0.64 | 2.68 | 686 |
| 2024-09-20 22:21:40.688 | MS1 | 121.4656675768 | 31.1446346029 | 162 | 504990 | -93.59 | 8.63 | 455.39 | 0.17 | 2.50 | 1577 |
| 2024-09-20 22:21:41.432 | MS1 | 121.4656779077 | 31.1446267631 | 162 | 504990 | -90.31 | 10.07 | 347.81 | 0.07 | 2.64 | 1594 |
| 2024-09-20 22:21:42.997 | MS1 | 121.4656618783 | 31.1446189167 | 162 | 504990 | -90.88 | 8.55 | 474.63 | 0.15 | 2.99 | 1588 |

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
| 3212461 | 3 | 121.4715764534 | 31.1497539444 | 262 | 7 | 6 | 43.1 | TDD | 50 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3231854 | 4 | 121.4674662146 | 31.1440055724 | 158 | 14 | 1 | 48.0 | TDD | 166 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3245571 | 2 | 121.4759890270 | 31.1526596465 | 207 | 0 | 0 | 22.1 | TDD | 162 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3261773 | 1 | 121.4728139148 | 31.1535488259 | 47 | 8 | 2 | 35.2 | TDD | 961 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.316 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.331 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.431 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.431 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.160 | NREventA3 | measId:2;ServCellPCI:257;Se... |
| 2024-09-20 22:21:38.400 | NRHandoverAttempt | SourcePCI:257;SourceNR-ARFC... |
| 2024-09-20 22:21:38.445 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.458 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.562 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.562 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261773 | 1 | 15.0860 | 9.3694 | -117.3727 | 7.0118 | 87.6747 | 0.0103 | 0.0122 |
| 2024_09_20 22:00 | 3245571 | 2 | 5.6735 | 15.1192 | -114.2970 | 19.6609 | 190.7079 | 0.0198 | 0.0167 |
| 2024_09_20 22:00 | 3212461 | 3 | 5.1893 | 9.3013 | -115.8775 | 12.4744 | 104.6473 | 0.0099 | 0.0095 |
| 2024_09_20 22:00 | 3231854 | 4 | 8.3753 | 6.4115 | -114.9071 | 15.5336 | 128.9318 | 0.0162 | 0.0024 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415124_FD40B52B | 504990 | 162 | -90.8 | 504990 | 961 | -96.1 | 504990 | 50 | -101.7 | 504990 | 166 |
| MR_1774415124_A691C401 | 504990 | 162 | -89.8 | 504990 | 961 | -96.0 | 504990 | 50 | -102.0 | 504990 | 166 |
| MR_1774415124_2A65B97A | 504990 | 162 | -88.5 | 504990 | 961 | -94.2 | 504990 | 50 | -102.0 | 504990 | 166 |
| MR_1774415124_E1AF56C5 | 504990 | 162 | -88.7 | 504990 | 961 | -96.4 | 504990 | 50 | -102.1 | 504990 | 166 |
| MR_1774415124_CD2DF8F0 | 504990 | 162 | -89.2 | 504990 | 961 | -93.4 | 504990 | 50 | -99.9 | 504990 | 166 |
| MR_1774415124_7BFBC6DA | 504990 | 162 | -88.3 | 504990 | 961 | -97.2 | 504990 | 50 | -101.5 | 504990 | 166 |
| MR_1774415124_21E473CA | 504990 | 162 | -87.7 | 504990 | 961 | -95.8 | 504990 | 50 | -101.8 | 504990 | 166 |
| MR_1774415124_A6F70345 | 504990 | 162 | -91.0 | 504990 | 961 | -95.0 | 504990 | 50 | -101.4 | 504990 | 166 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 384: `89c591f4-5bb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `89c591f4-5bbd-4ba4-83a5-d2a8b64e4632` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[384] topology](images/test_0384.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3235087_3
- `C2`: Decrease transmission power for 3210603_4
- `C3`: Add neighbor relationship between 3236232_1 and 3235087_3
- `C4`: Lift the tilt angle of 3210603_4 by 4 degrees
- `C5`: Increase transmission power for 3210603_4
- `C6`: Increase transmission power for 3235087_3
- `C7`: Decrease transmission power for 3235087_3
- `C8`: Adjust the azimuth of 3210603_4 by 13 degrees
- `C9`: Check test server and transmission issues
- `C10`: Press down the tilt angle of 3210603_4 by 4 degrees
- `C11`: Decrease A3 Offset threshold for 3210603_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210603_4
- `C13`: Lift the tilt angle  of 3235087_3 by 7 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235087_3
- `C15`: Increase A3 Offset threshold for 3235087_3
- `C16`: Add neighbor relationship between 3210603_4 and 3235087_3
- `C17`: Press down the tilt angle  of 3235087_3 by 7 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210603_4
- `C19`: Increase A3 Offset threshold for 3210603_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235087_3
- `C21`: Adjust the azimuth of 3235087_3 by 50 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.844 | MS1 | 121.4656686142 | 31.1446300754 | 823 | 504990 | -85.41 | 17.28 | 457.39 | 0.11 | 2.85 | 1577 |
| 2024-09-20 22:21:32.351 | MS1 | 121.4656649391 | 31.1446271476 | 823 | 504990 | -89.01 | 14.34 | 327.38 | 0.06 | 2.05 | 1580 |
| 2024-09-20 22:21:33.602 | MS1 | 121.4656691809 | 31.1446334620 | 823 | 504990 | -86.43 | 12.62 | 467.74 | 0.16 | 2.72 | 1563 |
| 2024-09-20 22:21:34.886 | MS1 | 121.4656693159 | 31.1446279454 | 823 | 504990 | -86.51 | 16.72 | 101.97 | 0.12 | 2.06 | 304 |
| 2024-09-20 22:21:35.226 | MS1 | 121.4656606804 | 31.1446259163 | 823 | 504990 | -85.68 | 13.44 | 66.92 | 0.15 | 2.09 | 464 |
| 2024-09-20 22:21:36.245 | MS1 | 121.4656662106 | 31.1446185097 | 823 | 504990 | -89.18 | 12.83 | 82.18 | 0.18 | 2.52 | 435 |
| 2024-09-20 22:21:37.388 | MS1 | 121.4656639597 | 31.1446220630 | 823 | 504990 | -92.24 | 7.97 | 83.81 | 0.13 | 2.27 | 317 |
| 2024-09-20 22:21:38.941 | MS1 | 121.4656594459 | 31.1446205303 | 823 | 504990 | -91.12 | 9.96 | 66.25 | 0.09 | 2.58 | 316 |
| 2024-09-20 22:21:39.618 | MS1 | 121.4656650727 | 31.1446325733 | 823 | 504990 | -93.60 | 7.78 | 78.13 | 0.14 | 2.74 | 381 |
| 2024-09-20 22:21:40.104 | MS1 | 121.4656716319 | 31.1446311068 | 823 | 504990 | -91.93 | 11.99 | 380.01 | 0.15 | 2.75 | 1586 |
| 2024-09-20 22:21:41.363 | MS1 | 121.4656710103 | 31.1446290901 | 823 | 504990 | -90.82 | 10.27 | 548.96 | 0.11 | 2.27 | 1584 |
| 2024-09-20 22:21:42.394 | MS1 | 121.4656685765 | 31.1446317877 | 823 | 504990 | -93.14 | 7.49 | 407.75 | 0.08 | 2.29 | 1598 |

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
| 3210603 | 4 | 121.4727955382 | 31.1537942840 | 227 | 3 | 9 | 26.0 | TDD | 823 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3235087 | 3 | 121.4645233273 | 31.1517266602 | 20 | 4 | 9 | 39.9 | TDD | 251 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3236232 | 1 | 121.4665492264 | 31.1553037455 | 55 | 1 | 9 | 17.2 | TDD | 120 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3245985 | 2 | 121.4673327476 | 31.1522131865 | 39 | 2 | 7 | 42.3 | TDD | 538 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.568 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.584 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.733 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.733 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.400 | NREventA3 | measId:2;ServCellPCI:897;Se... |
| 2024-09-20 22:21:38.640 | NRHandoverAttempt | SourcePCI:897;SourceNR-ARFC... |
| 2024-09-20 22:21:38.682 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.692 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.801 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.801 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236232 | 1 | 5.3173 | 6.8798 | -115.6364 | 15.6628 | 86.7443 | 0.0008 | 0.0017 |
| 2024_09_20 22:00 | 3245985 | 2 | 15.9167 | 6.1979 | -117.4381 | 6.2768 | 196.2253 | 0.0015 | 0.0021 |
| 2024_09_20 22:00 | 3235087 | 3 | 5.9185 | 8.4547 | -114.9911 | 9.1216 | 127.7156 | 0.0113 | 0.0111 |
| 2024_09_20 22:00 | 3210603 | 4 | 8.5577 | 10.5668 | -114.6506 | 16.2264 | 130.2990 | 0.0197 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416664_3779F311 | 504990 | 823 | -85.2 | 504990 | 251 | -90.4 | 504990 | 120 | -91.5 | 504990 | 538 |
| MR_1774416664_3DEEB824 | 504990 | 823 | -87.0 | 504990 | 251 | -92.5 | 504990 | 120 | -93.6 | 504990 | 538 |
| MR_1774416664_3BB59972 | 504990 | 823 | -85.0 | 504990 | 251 | -91.5 | 504990 | 120 | -92.6 | 504990 | 538 |
| MR_1774416664_B9CDA162 | 504990 | 823 | -84.6 | 504990 | 251 | -90.4 | 504990 | 120 | -91.7 | 504990 | 538 |
| MR_1774416664_56E0DE42 | 504990 | 823 | -84.1 | 504990 | 251 | -92.6 | 504990 | 120 | -90.0 | 504990 | 538 |
| MR_1774416664_0D539930 | 504990 | 823 | -86.4 | 504990 | 251 | -92.2 | 504990 | 120 | -90.6 | 504990 | 538 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 385: `53b4fc0a-3c8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `53b4fc0a-3c84-490b-ac6c-91017df6722e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[385] topology](images/test_0385.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3222580_3
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease A3 Offset threshold for 3215511_1
- `C4`: Press down the tilt angle of 3215511_1 by 10 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215511_1
- `C6`: Increase A3 Offset threshold for 3222580_3
- `C7`: Increase transmission power for 3215511_1
- `C8`: Press down the tilt angle  of 3222580_3 by 10 degrees
- `C9`: Decrease transmission power for 3222580_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215511_1
- `C11`: Adjust the azimuth of 3222580_3 by 50 degrees
- `C12`: Adjust the azimuth of 3215511_1 by 31 degrees
- `C13`: Increase A3 Offset threshold for 3215511_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222580_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222580_3
- `C16`: Add neighbor relationship between 3233129_4 and 3222580_3
- `C17`: Decrease A3 Offset threshold for 3222580_3
- `C18`: Check test server and transmission issues
- `C19`: Lift the tilt angle  of 3222580_3 by 10 degrees
- `C20`: Lift the tilt angle of 3215511_1 by 10 degrees
- `C21`: Decrease transmission power for 3215511_1
- `C22`: Add neighbor relationship between 3215511_1 and 3222580_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.180 | MS1 | 121.4656708681 | 31.1446279096 | 120 | 504990 | -88.02 | 14.55 | 576.37 | 0.17 | 2.75 | 1597 |
| 2024-09-20 22:21:32.551 | MS1 | 121.4656692518 | 31.1446364697 | 120 | 504990 | -85.49 | 15.42 | 529.07 | 0.09 | 2.81 | 1564 |
| 2024-09-20 22:21:33.747 | MS1 | 121.4656674860 | 31.1446252641 | 120 | 504990 | -85.67 | 17.72 | 455.21 | 0.11 | 2.72 | 1585 |
| 2024-09-20 22:21:34.114 | MS1 | 121.4656757551 | 31.1446260281 | 120 | 504990 | -86.10 | 15.89 | 98.87 | 0.11 | 2.35 | 409 |
| 2024-09-20 22:21:35.227 | MS1 | 121.4656763295 | 31.1446245715 | 120 | 504990 | -90.58 | 16.46 | 63.27 | 0.12 | 2.58 | 433 |
| 2024-09-20 22:21:36.313 | MS1 | 121.4656758028 | 31.1446200409 | 120 | 504990 | -87.18 | 17.49 | 41.15 | 0.13 | 2.51 | 478 |
| 2024-09-20 22:21:37.442 | MS1 | 121.4656693680 | 31.1446379326 | 120 | 504990 | -89.68 | 8.48 | 95.69 | 0.15 | 2.56 | 365 |
| 2024-09-20 22:21:38.725 | MS1 | 121.4656630199 | 31.1446250378 | 120 | 504990 | -91.81 | 9.52 | 89.62 | 0.03 | 2.39 | 403 |
| 2024-09-20 22:21:39.971 | MS1 | 121.4656733230 | 31.1446253836 | 120 | 504990 | -89.80 | 10.44 | 75.14 | 0.10 | 2.40 | 436 |
| 2024-09-20 22:21:40.739 | MS1 | 121.4656626044 | 31.1446353879 | 120 | 504990 | -93.18 | 9.82 | 423.90 | 0.16 | 2.09 | 1565 |
| 2024-09-20 22:21:41.332 | MS1 | 121.4656593030 | 31.1446374280 | 120 | 504990 | -91.82 | 8.75 | 416.21 | 0.10 | 2.30 | 1580 |
| 2024-09-20 22:21:42.747 | MS1 | 121.4656724012 | 31.1446225065 | 120 | 504990 | -89.64 | 7.76 | 381.55 | 0.15 | 2.79 | 1587 |

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
| 3215511 | 1 | 121.4665965448 | 31.1486350115 | 222 | 13 | 4 | 27.2 | TDD | 120 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3222580 | 3 | 121.4711387893 | 31.1489416986 | 66 | 13 | 2 | 20.6 | TDD | 267 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3226504 | 2 | 121.4753562666 | 31.1544236936 | 13 | 4 | 5 | 25.6 | TDD | 536 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3233129 | 4 | 121.4698694032 | 31.1442790048 | 204 | 15 | 0 | 46.4 | TDD | 14 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.933 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.952 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.071 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.071 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.795 | NREventA3 | measId:2;ServCellPCI:343;Se... |
| 2024-09-20 22:21:38.035 | NRHandoverAttempt | SourcePCI:343;SourceNR-ARFC... |
| 2024-09-20 22:21:38.073 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.087 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.197 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.197 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215511 | 1 | 5.4132 | 5.3150 | -116.6306 | 12.0099 | 149.4310 | 0.0094 | 0.0024 |
| 2024_09_20 22:00 | 3226504 | 2 | 13.1707 | 11.4381 | -116.6965 | 16.7768 | 98.9055 | 0.0132 | 0.0092 |
| 2024_09_20 22:00 | 3222580 | 3 | 6.2223 | 7.4871 | -114.3508 | 7.9081 | 152.6543 | 0.0066 | 0.0161 |
| 2024_09_20 22:00 | 3233129 | 4 | 13.6930 | 11.7888 | -116.2484 | 19.4317 | 102.5638 | 0.0155 | 0.0185 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415899_CDF881C7 | 504990 | 120 | -85.2 | 504990 | 267 | -88.1 | 504990 | 14 | -101.4 | 504990 | 536 |
| MR_1774415899_4C548433 | 504990 | 120 | -87.7 | 504990 | 267 | -87.7 | 504990 | 14 | -101.1 | 504990 | 536 |
| MR_1774415899_B8C0BDD6 | 504990 | 120 | -84.4 | 504990 | 267 | -88.7 | 504990 | 14 | -98.3 | 504990 | 536 |
| MR_1774415899_A3E1CCAD | 504990 | 120 | -87.1 | 504990 | 267 | -87.3 | 504990 | 14 | -97.5 | 504990 | 536 |
| MR_1774415899_A6CA06EE | 504990 | 120 | -87.8 | 504990 | 267 | -88.3 | 504990 | 14 | -98.5 | 504990 | 536 |
| MR_1774415899_6D064562 | 504990 | 120 | -84.4 | 504990 | 267 | -87.8 | 504990 | 14 | -100.1 | 504990 | 536 |
| MR_1774415899_4EF9C752 | 504990 | 120 | -85.4 | 504990 | 267 | -90.7 | 504990 | 14 | -100.7 | 504990 | 536 |
| MR_1774415899_F3558F29 | 504990 | 120 | -86.8 | 504990 | 267 | -88.0 | 504990 | 14 | -98.0 | 504990 | 536 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 386: `e943b1d6-559...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e943b1d6-5591-45ab-8679-4c5f24687de7` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[386] topology](images/test_0386.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3274817_5
- `C2`: Check test server and transmission issues
- `C3`: Increase transmission power for 3265588_3
- `C4`: Decrease A3 Offset threshold for 3265588_3
- `C5`: Press down the tilt angle  of 3265588_3 by 3 degrees
- `C6`: Decrease transmission power for 3274817_5
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274817_5
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274817_5
- `C9`: Increase A3 Offset threshold for 3265588_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265588_3
- `C11`: Increase A3 Offset threshold for 3274817_5
- `C12`: Add neighbor relationship between 3227619_1 and 3265588_3
- `C13`: Press down the tilt angle of 3274817_5 by 2 degrees
- `C14`: Add neighbor relationship between 3274817_5 and 3265588_3
- `C15`: Increase transmission power for 3274817_5
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265588_3
- `C17`: Adjust the azimuth of 3265588_3 by 37 degrees
- `C18`: Decrease transmission power for 3265588_3
- `C19`: Adjust the azimuth of 3274817_5 by 16 degrees
- `C20`: Lift the tilt angle of 3274817_5 by 2 degrees
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Lift the tilt angle  of 3265588_3 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.695 | MS1 | 121.4656615985 | 31.1446188924 | 564 | 504990 | -77.65 | 17.92 | 343.19 | 0.10 | 2.91 | 1571 |
| 2024-09-20 22:21:32.551 | MS1 | 121.4656760885 | 31.1446268233 | 564 | 504990 | -81.58 | 15.14 | 553.82 | 0.18 | 2.78 | 1582 |
| 2024-09-20 22:21:33.622 | MS1 | 121.4656653814 | 31.1446294848 | 564 | 504990 | -84.56 | 16.69 | 470.47 | 0.16 | 2.12 | 1569 |
| 2024-09-20 22:21:34.589 | MS1 | 121.4656682182 | 31.1446310891 | 332 | 504990 | -85.42 | 3.96 | 52.44 | 0.02 | 1.38 | 1581 |
| 2024-09-20 22:21:35.250 | MS1 | 121.4656669895 | 31.1446248671 | 332 | 504990 | -85.77 | 1.86 | 74.81 | 0.04 | 1.14 | 1590 |
| 2024-09-20 22:21:36.433 | MS1 | 121.4656601930 | 31.1446315752 | 564 | 504990 | -84.65 | 1.86 | 67.47 | 0.14 | 1.47 | 1572 |
| 2024-09-20 22:21:37.281 | MS1 | 121.4656614490 | 31.1446277338 | 564 | 504990 | -83.59 | 2.42 | 47.65 | 0.08 | 1.04 | 1596 |
| 2024-09-20 22:21:38.463 | MS1 | 121.4656730354 | 31.1446216767 | 332 | 504990 | -82.34 | 4.35 | 68.02 | 0.08 | 1.15 | 1580 |
| 2024-09-20 22:21:39.374 | MS1 | 121.4656755612 | 31.1446328982 | 332 | 504990 | -83.66 | 2.16 | 53.15 | 0.12 | 1.12 | 1600 |
| 2024-09-20 22:21:40.693 | MS1 | 121.4656690038 | 31.1446339618 | 332 | 504990 | -77.37 | 12.15 | 309.03 | 0.08 | 2.01 | 1589 |
| 2024-09-20 22:21:41.130 | MS1 | 121.4656649690 | 31.1446209133 | 332 | 504990 | -83.62 | 17.78 | 414.55 | 0.01 | 2.78 | 1586 |
| 2024-09-20 22:21:42.591 | MS1 | 121.4656589295 | 31.1446223632 | 332 | 504990 | -81.19 | 12.90 | 414.33 | 0.03 | 2.32 | 1573 |

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
| 3227619 | 1 | 121.4676900298 | 31.1507947192 | 155 | 9 | 9 | 21.8 | TDD | 649 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3248629 | 2 | 121.4699681185 | 31.1500328527 | 313 | 3 | 1 | 41.2 | TDD | 970 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3265588 | 3 | 121.4674829456 | 31.1486303881 | 238 | 0 | 0 | 27.7 | TDD | 876 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3270798 | 4 | 121.4706624564 | 31.1543321629 | 174 | 6 | 0 | 26.1 | TDD | 332 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3274817 | 5 | 121.4717401748 | 31.1529684107 | 196 | 1 | 12 | 20.2 | TDD | 564 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.381 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.397 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.530 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.530 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.204 | NREventA3 | measId:2;ServCellPCI:614;Se... |
| 2024-09-20 22:21:34.444 | NRHandoverAttempt | SourcePCI:614;SourceNR-ARFC... |
| 2024-09-20 22:21:34.481 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.496 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.632 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.632 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.204 | NREventA3 | measId:2;ServCellPCI:625;Se... |
| 2024-09-20 22:21:36.444 | NRHandoverAttempt | SourcePCI:625;SourceNR-ARFC... |
| 2024-09-20 22:21:36.481 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.492 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.637 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.637 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.204 | NREventA3 | measId:2;ServCellPCI:614;Se... |
| 2024-09-20 22:21:38.444 | NRHandoverAttempt | SourcePCI:614;SourceNR-ARFC... |
| 2024-09-20 22:21:38.476 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.487 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.623 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.623 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227619 | 1 | 18.5504 | 13.9361 | -115.5539 | 12.6189 | 196.2294 | 0.0141 | 0.0031 |
| 2024_09_20 22:00 | 3248629 | 2 | 11.1428 | 7.3052 | -116.2287 | 18.9885 | 198.9644 | 0.0131 | 0.0068 |
| 2024_09_20 22:00 | 3265588 | 3 | 11.0729 | 16.9289 | -116.0689 | 13.4932 | 82.3850 | 0.0093 | 0.0005 |
| 2024_09_20 22:00 | 3270798 | 4 | 15.0831 | 13.4928 | -116.2467 | 16.5885 | 132.3701 | 0.0180 | 0.0066 |
| 2024_09_20 22:00 | 3274817 | 5 | 8.1434 | 15.5214 | -116.2092 | 18.0149 | 141.2059 | 0.0176 | 0.0075 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415023_A0975C44 | 504990 | 332 | -85.7 | 504990 | 564 | -80.4 | 504990 | 876 | -84.7 | 504990 | 649 |
| MR_1774415023_BFDC7A62 | 504990 | 564 | -85.4 | 504990 | 332 | -82.2 | 504990 | 876 | -84.7 | 504990 | 649 |
| MR_1774415023_E1EFFBFA | 504990 | 564 | -86.2 | 504990 | 332 | -80.2 | 504990 | 876 | -86.9 | 504990 | 649 |
| MR_1774415023_4D7AB7AF | 504990 | 332 | -86.5 | 504990 | 564 | -79.1 | 504990 | 876 | -86.2 | 504990 | 649 |
| MR_1774415023_6E4232F1 | 504990 | 332 | -84.0 | 504990 | 564 | -80.8 | 504990 | 876 | -86.0 | 504990 | 649 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 387: `f201f1dc-655...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f201f1dc-6557-447b-a799-3265bdaf667b` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[387] topology](images/test_0387.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245450_1
- `C3`: Press down the tilt angle  of 3245450_1 by 6 degrees
- `C4`: Increase A3 Offset threshold for 3245450_1
- `C5`: Decrease transmission power for 3245450_1
- `C6`: Increase A3 Offset threshold for 3267809_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267809_4
- `C8`: Adjust the azimuth of 3245450_1 by 49 degrees
- `C9`: Lift the tilt angle of 3267809_4 by 10 degrees
- `C10`: Decrease A3 Offset threshold for 3245450_1
- `C11`: Add neighbor relationship between 3267809_4 and 3245450_1
- `C12`: Increase transmission power for 3267809_4
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245450_1
- `C15`: Lift the tilt angle  of 3245450_1 by 6 degrees
- `C16`: Adjust the azimuth of 3267809_4 by 50 degrees
- `C17`: Press down the tilt angle of 3267809_4 by 10 degrees
- `C18`: Increase transmission power for 3245450_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267809_4
- `C20`: Decrease transmission power for 3267809_4
- `C21`: Decrease A3 Offset threshold for 3267809_4
- `C22`: Add neighbor relationship between 3270564_2 and 3245450_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.891 | MS1 | 121.4656721497 | 31.1446205151 | 310 | 504990 | -88.57 | 12.84 | 408.65 | 0.10 | 2.88 | 1595 |
| 2024-09-20 22:21:32.499 | MS1 | 121.4656604185 | 31.1446268735 | 310 | 504990 | -85.64 | 17.62 | 565.05 | 0.00 | 2.24 | 1586 |
| 2024-09-20 22:21:33.213 | MS1 | 121.4656587317 | 31.1446225380 | 310 | 504990 | -91.66 | 12.15 | 322.45 | 0.17 | 2.21 | 1568 |
| 2024-09-20 22:21:34.278 | MS1 | 121.4656727595 | 31.1446280448 | 310 | 504990 | -105.59 | 0.63 | 25.13 | 0.04 | 1.22 | 1587 |
| 2024-09-20 22:21:35.254 | MS1 | 121.4656693836 | 31.1446197010 | 310 | 504990 | -103.86 | -0.92 | 25.44 | 0.04 | 1.13 | 1589 |
| 2024-09-20 22:21:36.687 | MS1 | 121.4656608805 | 31.1446204874 | 310 | 504990 | -105.15 | -1.84 | 28.30 | 0.18 | 1.12 | 1580 |
| 2024-09-20 22:21:37.697 | MS1 | 121.4656619840 | 31.1446356450 | 310 | 504990 | -101.19 | 0.04 | 72.16 | 0.03 | 1.17 | 1579 |
| 2024-09-20 22:21:38.190 | MS1 | 121.4656775124 | 31.1446242127 | 310 | 504990 | -101.42 | -0.73 | 75.06 | 0.19 | 1.18 | 1573 |
| 2024-09-20 22:21:39.607 | MS1 | 121.4656646265 | 31.1446244221 | 310 | 504990 | -101.43 | -0.14 | 30.24 | 0.03 | 1.37 | 1560 |
| 2024-09-20 22:21:40.457 | MS1 | 121.4656730357 | 31.1446282580 | 310 | 504990 | -85.79 | 17.37 | 339.07 | 0.01 | 2.00 | 1597 |
| 2024-09-20 22:21:41.489 | MS1 | 121.4656731056 | 31.1446298644 | 310 | 504990 | -91.63 | 12.40 | 356.06 | 0.13 | 2.52 | 1585 |
| 2024-09-20 22:21:42.890 | MS1 | 121.4656624326 | 31.1446215050 | 310 | 504990 | -89.80 | 12.46 | 548.50 | 0.07 | 2.61 | 1583 |

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
| 3224053 | 3 | 121.4750482091 | 31.1455787352 | 67 | 7 | 7 | 47.0 | TDD | 596 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3245450 | 1 | 121.4652468548 | 31.1527937656 | 128 | 4 | 10 | 25.5 | TDD | 776 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3267809 | 4 | 121.4747545789 | 31.1512494465 | 290 | 11 | 4 | 34.0 | TDD | 310 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3270564 | 2 | 121.4717192432 | 31.1494310151 | 189 | 0 | 10 | 25.5 | TDD | 650 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.525 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.546 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.694 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.694 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.906 | NREventA2 | measId:1;ServCellPCI:676;Se... |
| 2024-09-20 22:21:35.036 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245450 | 1 | 10.0664 | 7.2302 | -115.4296 | 18.3541 | 114.8453 | 0.0133 | 0.0118 |
| 2024_09_20 22:00 | 3270564 | 2 | 17.3478 | 13.1804 | -117.4874 | 6.0163 | 196.4806 | 0.0198 | 0.0070 |
| 2024_09_20 22:00 | 3224053 | 3 | 10.8572 | 11.3146 | -117.1535 | 15.3771 | 150.6377 | 0.0045 | 0.0070 |
| 2024_09_20 22:00 | 3267809 | 4 | 13.7875 | 13.3820 | -117.3477 | 15.9187 | 127.1226 | 0.1212 | 0.0116 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414117_990464EE | 504990 | 310 | -105.0 | 504990 | 776 | -107.7 | 504990 | 650 | -117.5 | 504990 | 596 |
| MR_1774414117_3BC9F623 | 504990 | 310 | -105.2 | 504990 | 776 | -111.2 | 504990 | 650 | -115.9 | 504990 | 596 |
| MR_1774414117_E071760A | 504990 | 310 | -104.2 | 504990 | 776 | -108.4 | 504990 | 650 | -116.8 | 504990 | 596 |
| MR_1774414117_9D6052E3 | 504990 | 310 | -105.8 | 504990 | 776 | -109.7 | 504990 | 650 | -115.5 | 504990 | 596 |
| MR_1774414117_75BD930C | 504990 | 310 | -107.0 | 504990 | 776 | -109.8 | 504990 | 650 | -117.2 | 504990 | 596 |
| MR_1774414117_E4914CF6 | 504990 | 310 | -104.6 | 504990 | 776 | -109.5 | 504990 | 650 | -115.2 | 504990 | 596 |
| MR_1774414117_7EAF2A1B | 504990 | 310 | -106.7 | 504990 | 776 | -109.8 | 504990 | 650 | -115.0 | 504990 | 596 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 388: `27eda095-b6c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `27eda095-b6c0-4743-8881-3acbd7f5148e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[388] topology](images/test_0388.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3256748_2 and 3240520_4
- `C2`: Adjust the azimuth of 3256748_2 by 50 degrees
- `C3`: Decrease A3 Offset threshold for 3233122_3
- `C4`: Decrease transmission power for 3240520_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240520_4
- `C6`: Decrease transmission power for 3233122_3
- `C7`: Press down the tilt angle  of 3256748_2 by 10 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase transmission power for 3233122_3
- `C10`: Increase A3 Offset threshold for 3240520_4
- `C11`: Increase A3 Offset threshold for 3233122_3
- `C12`: Add neighbor relationship between 3233122_3 and 3240520_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233122_3
- `C14`: Decrease A3 Offset threshold for 3240520_4
- `C15`: Adjust the azimuth of 3233122_3 by 39 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240520_4
- `C17`: Press down the tilt angle of 3233122_3 by 2 degrees
- `C18`: Increase transmission power for 3240520_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233122_3
- `C20`: Check test server and transmission issues
- `C21`: Lift the tilt angle  of 3256748_2 by 10 degrees
- `C22`: Lift the tilt angle of 3233122_3 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.196 | MS1 | 121.4656655566 | 31.1446208499 | 302 | 504990 | -90.78 | 17.06 | 504.74 | 0.16 | 2.61 | 1599 |
| 2024-09-20 22:21:32.179 | MS1 | 121.4656610926 | 31.1446330032 | 302 | 504990 | -90.92 | 14.28 | 575.46 | 0.08 | 2.01 | 1561 |
| 2024-09-20 22:21:33.452 | MS1 | 121.4656636920 | 31.1446296077 | 302 | 504990 | -89.33 | 12.16 | 494.44 | 0.10 | 2.36 | 1586 |
| 2024-09-20 22:21:34.192 | MS1 | 121.4656620450 | 31.1446192823 | 302 | 504990 | -89.89 | 16.87 | 69.86 | 0.02 | 2.85 | 1588 |
| 2024-09-20 22:21:35.690 | MS1 | 121.4656701988 | 31.1446218792 | 302 | 504990 | -90.18 | 14.31 | 74.82 | 0.05 | 2.95 | 1575 |
| 2024-09-20 22:21:36.869 | MS1 | 121.4656760315 | 31.1446295767 | 302 | 504990 | -87.74 | 16.43 | 88.93 | 0.13 | 2.49 | 1600 |
| 2024-09-20 22:21:37.841 | MS1 | 121.4656775881 | 31.1446203067 | 302 | 504990 | -89.20 | 9.94 | 52.66 | 0.05 | 2.68 | 1579 |
| 2024-09-20 22:21:38.975 | MS1 | 121.4656750610 | 31.1446353229 | 302 | 504990 | -89.50 | 12.72 | 91.77 | 0.04 | 2.17 | 1592 |
| 2024-09-20 22:21:39.971 | MS1 | 121.4656633343 | 31.1446264960 | 302 | 504990 | -92.11 | 7.71 | 87.42 | 0.02 | 2.98 | 1566 |
| 2024-09-20 22:21:40.396 | MS1 | 121.4656682731 | 31.1446203538 | 302 | 504990 | -90.99 | 10.46 | 479.09 | 0.11 | 2.21 | 1566 |
| 2024-09-20 22:21:41.854 | MS1 | 121.4656592098 | 31.1446239289 | 302 | 504990 | -91.57 | 7.89 | 568.53 | 0.03 | 2.84 | 1595 |
| 2024-09-20 22:21:42.893 | MS1 | 121.4656587820 | 31.1446192000 | 302 | 504990 | -91.19 | 7.32 | 403.39 | 0.08 | 2.29 | 1567 |

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
| 3214653 | 1 | 121.4650277730 | 31.1445670327 | 192 | 8 | 12 | 26.5 | TDD | 641 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3233122 | 3 | 121.4675311746 | 31.1551798854 | 150 | 0 | 6 | 38.5 | TDD | 302 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3240520 | 4 | 121.4708539108 | 31.1466388707 | 179 | 15 | 0 | 36.6 | TDD | 599 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3256748 | 2 | 121.4655000119 | 31.1547176864 | 352 | 0 | 4 | 44.8 | TDD | 845 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.830 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.855 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.961 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.961 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.694 | NREventA3 | measId:2;ServCellPCI:223;Se... |
| 2024-09-20 22:21:37.934 | NRHandoverAttempt | SourcePCI:223;SourceNR-ARFC... |
| 2024-09-20 22:21:37.979 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.992 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.109 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.109 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214653 | 1 | 18.0532 | 17.8561 | -116.2289 | 8.9836 | 165.9430 | 0.0057 | 0.0109 |
| 2024_09_20 22:00 | 3256748 | 2 | 16.3517 | 10.0933 | -115.2243 | 9.4720 | 107.1144 | 0.0048 | 0.0074 |
| 2024_09_20 22:00 | 3233122 | 3 | 79.8662 | 77.7150 | -115.0603 | 9.2915 | 95.8605 | 0.0099 | 0.0170 |
| 2024_09_20 22:00 | 3240520 | 4 | 5.0864 | 12.5620 | -116.4192 | 8.7648 | 173.2131 | 0.0103 | 0.0022 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416500_86FF472A | 504990 | 302 | -88.0 | 504990 | 599 | -100.9 | 504990 | 845 | -102.3 | 504990 | 641 |
| MR_1774416500_2C792BED | 504990 | 302 | -90.7 | 504990 | 599 | -99.8 | 504990 | 845 | -104.9 | 504990 | 641 |
| MR_1774416500_A37BF24D | 504990 | 302 | -91.2 | 504990 | 599 | -99.0 | 504990 | 845 | -103.6 | 504990 | 641 |
| MR_1774416500_E9EFB787 | 504990 | 302 | -89.9 | 504990 | 599 | -101.4 | 504990 | 845 | -104.4 | 504990 | 641 |
| MR_1774416500_E5493ED4 | 504990 | 302 | -91.1 | 504990 | 599 | -98.1 | 504990 | 845 | -104.9 | 504990 | 641 |
| MR_1774416500_03C66D1A | 504990 | 302 | -89.2 | 504990 | 599 | -101.4 | 504990 | 845 | -102.6 | 504990 | 641 |
| MR_1774416500_BE55D3C7 | 504990 | 302 | -88.7 | 504990 | 599 | -101.4 | 504990 | 845 | -102.9 | 504990 | 641 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 389: `ca01d1a5-79a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ca01d1a5-79a8-41c6-9780-e474b27b74cc` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[389] topology](images/test_0389.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3245622_13 and 3252940_4
- `C2`: Lift the tilt angle  of 3252940_4 by 4 degrees
- `C3`: Decrease A3 Offset threshold for 3252940_4
- `C4`: Lift the tilt angle of 3251025_1 by 0 degrees
- `C5`: Increase transmission power for 3251025_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252940_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251025_1
- `C8`: Decrease transmission power for 3252940_4
- `C9`: Decrease transmission power for 3251025_1
- `C10`: Check test server and transmission issues
- `C11`: Adjust the azimuth of 3251025_1 by 18 degrees
- `C12`: Add neighbor relationship between 3251025_1 and 3252940_4
- `C13`: Adjust the azimuth of 3252940_4 by 4 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease A3 Offset threshold for 3251025_1
- `C16`: Press down the tilt angle  of 3252940_4 by 4 degrees
- `C17`: Increase A3 Offset threshold for 3251025_1
- `C18`: Increase transmission power for 3252940_4
- `C19`: Increase A3 Offset threshold for 3252940_4
- `C20`: Press down the tilt angle of 3251025_1 by 0 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251025_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252940_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.401 | MS1 | 121.4656755212 | 31.1446361273 | 551 | 504990 | -95.13 | 13.15 | 433.57 | 0.01 | 2.49 | 1573 |
| 2024-09-20 22:21:32.882 | MS1 | 121.4656681207 | 31.1446257459 | 915 | 504990 | -95.97 | 14.27 | 516.55 | 0.20 | 2.10 | 1595 |
| 2024-09-20 22:21:33.418 | MS1 | 121.4656581484 | 31.1446290775 | 753 | 504990 | -95.49 | 9.33 | 554.82 | 0.12 | 2.34 | 1596 |
| 2024-09-20 22:21:34.136 | MS1 | 121.4656719816 | 31.1446337933 | 371 | 152650 | -96.56 | 4.02 | 49.37 | 0.17 | 1.73 | 911 |
| 2024-09-20 22:21:35.428 | MS1 | 121.4656762332 | 31.1446249981 | 817 | 152650 | -93.90 | 3.79 | 101.17 | 0.12 | 1.89 | 956 |
| 2024-09-20 22:21:36.549 | MS1 | 121.4656630474 | 31.1446333200 | 603 | 152650 | -96.30 | 2.10 | 95.65 | 0.16 | 1.97 | 917 |
| 2024-09-20 22:21:37.509 | MS1 | 121.4656647326 | 31.1446356203 | 752 | 152650 | -95.41 | 6.02 | 58.77 | 0.03 | 1.94 | 914 |
| 2024-09-20 22:21:38.599 | MS1 | 121.4656608635 | 31.1446280676 | 371 | 152650 | -88.36 | 3.47 | 82.72 | 0.03 | 1.53 | 977 |
| 2024-09-20 22:21:39.587 | MS1 | 121.4656714680 | 31.1446323110 | 817 | 152650 | -90.13 | 7.91 | 92.31 | 0.00 | 1.72 | 921 |
| 2024-09-20 22:21:40.143 | MS1 | 121.4656674846 | 31.1446207577 | 603 | 152650 | -87.52 | 4.14 | 81.33 | 0.16 | 2.70 | 1596 |
| 2024-09-20 22:21:41.202 | MS1 | 121.4656765093 | 31.1446230893 | 752 | 152650 | -91.37 | 2.51 | 59.97 | 0.12 | 2.68 | 1572 |
| 2024-09-20 22:21:42.611 | MS1 | 121.4656642640 | 31.1446208268 | 371 | 152650 | -95.71 | 6.78 | 77.09 | 0.02 | 2.99 | 1591 |

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
| 3219876 | 8 | 121.4746926405 | 31.1463872545 | 282 | 0 | 2 | 6.2 | FDD | 752 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3221719 | 12 | 121.4662944127 | 31.1513614482 | 229 | 4 | 2 | 2.8 | FDD | 560 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3235908 | 2 | 121.4718641272 | 31.1545610012 | 319 | 8 | 1 | 2.5 | TDD | 264 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3241209 | 6 | 121.4659043200 | 31.1547284910 | 34 | 11 | 12 | 4.0 | TDD | 915 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3245622 | 13 | 121.4675659444 | 31.1477799707 | 186 | 9 | 4 | 11.6 | FDD | 603 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3246158 | 10 | 121.4717151791 | 31.1468805275 | 136 | 0 | 12 | 2.4 | FDD | 209 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3251025 | 1 | 121.4686209125 | 31.1544943363 | 176 | 0 | 10 | 0.7 | TDD | 551 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3251482 | 11 | 121.4686791090 | 31.1548409330 | 44 | 4 | 2 | 11.9 | FDD | 371 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3252940 | 4 | 121.4688956491 | 31.1451909493 | 263 | 1 | 2 | 17.0 | TDD | 238 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3253360 | 5 | 121.4644169331 | 31.1497440390 | 216 | 13 | 11 | 19.6 | TDD | 753 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3260349 | 3 | 121.4749496838 | 31.1501908911 | 51 | 3 | 4 | 9.1 | TDD | 650 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3267284 | 9 | 121.4692230717 | 31.1492399007 | 210 | 10 | 8 | 3.0 | FDD | 817 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3279636 | 7 | 121.4680469764 | 31.1486936678 | 293 | 13 | 12 | 20.8 | FDD | 616 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |

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
| 2024-09-20 22:21:31.419 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.438 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.587 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.587 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.267 | NREventA2 | measId:1;ServCellPCI:331;Se... |
| 2024-09-20 22:21:35.374 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.668 | NREventA5 | measId:3;ServCellPCI:331;Se... |
| 2024-09-20 22:21:35.746 | NRHandoverAttempt | SourcePCI:331;SourceNR-ARFC... |
| 2024-09-20 22:21:35.770 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.785 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.926 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.926 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251025 | 1 | 19.5186 | 6.9726 | -115.7458 | 5.4202 | 147.7787 | 0.0007 | 0.0061 |
| 2024_09_20 22:00 | 3235908 | 2 | 18.3218 | 10.6056 | -117.8792 | 16.5889 | 100.9425 | 0.0137 | 0.0073 |
| 2024_09_20 22:00 | 3260349 | 3 | 5.2472 | 16.4560 | -117.2344 | 14.4117 | 128.6523 | 0.0060 | 0.0048 |
| 2024_09_20 22:00 | 3252940 | 4 | 8.7768 | 18.9743 | -117.1240 | 8.4693 | 197.4149 | 0.0088 | 0.0091 |
| 2024_09_20 22:00 | 3253360 | 5 | 15.0818 | 14.7964 | -116.0269 | 5.5705 | 98.6570 | 0.0117 | 0.0192 |
| 2024_09_20 22:00 | 3241209 | 6 | 9.8714 | 5.7954 | -117.1333 | 14.4372 | 83.8889 | 0.0036 | 0.0030 |
| 2024_09_20 22:00 | 3279636 | 7 | 19.2650 | 18.8037 | -115.4576 | 3.0195 | 34.5972 | 0.0047 | 0.0129 |
| 2024_09_20 22:00 | 3219876 | 8 | 8.8941 | 19.6278 | -117.4756 | 3.6537 | 49.2734 | 0.0062 | 0.0174 |
| 2024_09_20 22:00 | 3267284 | 9 | 13.3983 | 6.5894 | -114.6226 | 3.8005 | 24.7240 | 0.0158 | 0.0051 |
| 2024_09_20 22:00 | 3246158 | 10 | 8.1154 | 18.3766 | -115.1478 | 4.7039 | 58.7920 | 0.0149 | 0.0064 |
| 2024_09_20 22:00 | 3251482 | 11 | 18.4860 | 14.8190 | -116.9925 | 3.5863 | 57.9385 | 0.0019 | 0.0121 |
| 2024_09_20 22:00 | 3221719 | 12 | 15.7161 | 18.3383 | -116.4822 | 3.5954 | 58.8241 | 0.0156 | 0.0062 |
| 2024_09_20 22:00 | 3245622 | 13 | 6.5907 | 6.7413 | -117.1802 | 4.1682 | 53.1718 | 0.0025 | 0.0178 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412074_E1B0AC94 | 504990 | 753 | -95.2 | 504990 | 238 | -97.2 | 504990 | 650 | -102.2 | 504990 | 264 |
| MR_1774412074_8675716F | 504990 | 753 | -95.7 | 504990 | 238 | -97.7 | 504990 | 650 | -101.9 | 504990 | 264 |
| MR_1774412074_AE6B861D | 152650 | 371 | -95.3 | 152650 | 209 | -97.0 | 152650 | 560 | -103.8 | 152650 | 616 |
| MR_1774412074_1FEA776C | 504990 | 753 | -95.6 | 504990 | 238 | -97.0 | 504990 | 650 | -100.8 | 504990 | 264 |
| MR_1774412074_A964B4F7 | 504990 | 753 | -95.2 | 504990 | 238 | -99.8 | 504990 | 650 | -104.5 | 504990 | 264 |
| MR_1774412074_B1B3776F | 504990 | 753 | -94.7 | 504990 | 238 | -99.4 | 504990 | 650 | -101.9 | 504990 | 264 |
| MR_1774412074_6D953551 | 152650 | 371 | -95.0 | 152650 | 209 | -98.6 | 152650 | 560 | -105.7 | 152650 | 616 |

> *... 2개 열 생략 (전체 14열)*

---
