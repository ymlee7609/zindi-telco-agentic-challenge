# Track A 문제 분석 — train[590]~train[599]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[590] ~ train[599] (10개)

## 목차

1. [문제 590: `853579e8-f57...`](#590) — single-answer, 정답: C14
2. [문제 591: `73fe4a26-25b...`](#591) — single-answer, 정답: C1
3. [문제 592: `afd0d62d-c6f...`](#592) — multiple-answer, 정답: C4|C11
4. [문제 593: `1685f7e5-ec8...`](#593) — multiple-answer, 정답: C7|C14
5. [문제 594: `1f31fa25-2fa...`](#594) — single-answer, 정답: C3
6. [문제 595: `c7946f43-3ce...`](#595) — single-answer, 정답: C12
7. [문제 596: `eee1493f-f1e...`](#596) — single-answer, 정답: C14
8. [문제 597: `55870f87-ba8...`](#597) — single-answer, 정답: C9
9. [문제 598: `c587ce54-be8...`](#598) — single-answer, 정답: C18
10. [문제 599: `3a1c22dc-b4b...`](#599) — multiple-answer, 정답: C10|C21

---

### 문제 590: `853579e8-f57...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `853579e8-f575-4dbe-9a98-027dfe954401` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Add neighbor relationship between 3227290_4 and 3247283_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[590] topology](images/train_0590.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3247283_1 by 3 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247283_1
- `C3`: Press down the tilt angle  of 3247283_1 by 3 degrees
- `C4`: Increase A3 Offset threshold for 3247283_1
- `C5`: Decrease A3 Offset threshold for 3247283_1
- `C6`: Decrease transmission power for 3227290_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227290_4
- `C8`: Lift the tilt angle of 3227290_4 by 6 degrees
- `C9`: Add neighbor relationship between 3249911_2 and 3247283_1
- `C10`: Increase transmission power for 3227290_4
- `C11`: Decrease A3 Offset threshold for 3227290_4
- `C12`: Increase A3 Offset threshold for 3227290_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227290_4
- `C14`: Add neighbor relationship between 3227290_4 and 3247283_1 **← 정답**
- `C15`: Adjust the azimuth of 3227290_4 by 50 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247283_1
- `C17`: Adjust the azimuth of 3247283_1 by 17 degrees
- `C18`: Increase transmission power for 3247283_1
- `C19`: Press down the tilt angle of 3227290_4 by 6 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Check test server and transmission issues
- `C22`: Decrease transmission power for 3247283_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.216 | MS1 | 121.4656585713 | 31.1446294782 | 351 | 504990 | -81.18 | 17.40 | 488.65 | 0.00 | 2.52 | 1590 |
| 2024-09-20 22:21:32.904 | MS1 | 121.4656732783 | 31.1446240419 | 351 | 504990 | -76.54 | 14.24 | 549.57 | 0.02 | 2.94 | 1597 |
| 2024-09-20 22:21:33.587 | MS1 | 121.4656679506 | 31.1446280560 | 351 | 504990 | -83.35 | 12.98 | 465.45 | 0.15 | 2.38 | 1578 |
| 2024-09-20 22:21:34.563 | MS1 | 121.4656598380 | 31.1446298721 | 351 | 504990 | -92.16 | -0.66 | 49.26 | 0.01 | 1.02 | 1600 |
| 2024-09-20 22:21:35.734 | MS1 | 121.4656726518 | 31.1446334986 | 351 | 504990 | -89.50 | -0.31 | 69.25 | 0.03 | 1.06 | 1563 |
| 2024-09-20 22:21:36.834 | MS1 | 121.4656606604 | 31.1446261537 | 351 | 504990 | -85.32 | -0.79 | 40.05 | 0.00 | 1.02 | 1599 |
| 2024-09-20 22:21:37.792 | MS1 | 121.4656694021 | 31.1446189578 | 351 | 504990 | -92.71 | -1.65 | 74.75 | 0.13 | 1.44 | 1560 |
| 2024-09-20 22:21:38.269 | MS1 | 121.4656667302 | 31.1446300407 | 351 | 504990 | -78.72 | 13.66 | 382.58 | 0.01 | 1.13 | 1585 |
| 2024-09-20 22:21:39.840 | MS1 | 121.4656609199 | 31.1446365746 | 351 | 504990 | -81.38 | 13.65 | 551.35 | 0.18 | 1.38 | 1570 |
| 2024-09-20 22:21:40.199 | MS1 | 121.4656718968 | 31.1446195702 | 351 | 504990 | -77.39 | 16.58 | 357.73 | 0.18 | 2.42 | 1588 |
| 2024-09-20 22:21:41.802 | MS1 | 121.4656599140 | 31.1446327313 | 351 | 504990 | -80.07 | 14.79 | 519.52 | 0.18 | 2.42 | 1562 |
| 2024-09-20 22:21:42.982 | MS1 | 121.4656607529 | 31.1446316647 | 351 | 504990 | -75.67 | 17.23 | 339.20 | 0.03 | 2.36 | 1564 |

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
| 3227290 | 4 | 121.4685727183 | 31.1488749701 | 138 | 3 | 10 | 24.3 | TDD | 351 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3232452 | 3 | 121.4688501985 | 31.1494910266 | 113 | 9 | 9 | 34.1 | TDD | 262 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3247283 | 1 | 121.4661961372 | 31.1548678473 | 166 | 2 | 10 | 15.7 | TDD | 617 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3249911 | 2 | 121.4665077028 | 31.1532468533 | 211 | 6 | 4 | 42.5 | TDD | 493 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.904 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.920 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.044 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.044 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.752 | NREventA3 | measId:2;ServCellPCI:82;Ser... |
| 2024-09-20 22:21:35.752 | NREventA3 | measId:2;ServCellPCI:82;Ser... |
| 2024-09-20 22:21:36.752 | NREventA3 | measId:2;ServCellPCI:82;Ser... |
| 2024-09-20 22:21:39.252 | NRRRCReestablishAttempt | PCI:82 |
| 2024-09-20 22:21:39.271 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.282 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.406 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.406 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247283 | 1 | 5.6518 | 12.5125 | -116.8061 | 10.6556 | 111.6439 | 0.0041 | 0.0060 |
| 2024_09_20 22:00 | 3249911 | 2 | 9.5441 | 19.5394 | -115.6861 | 11.9251 | 133.4702 | 0.0175 | 0.0098 |
| 2024_09_20 22:00 | 3232452 | 3 | 8.0064 | 15.4300 | -116.3328 | 5.4203 | 82.9062 | 0.0001 | 0.0025 |
| 2024_09_20 22:00 | 3227290 | 4 | 14.0308 | 6.9179 | -115.2532 | 13.9851 | 135.1163 | 0.0038 | 0.1022 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414608_557DF496 | 504990 | 351 | -91.6 | 504990 | 617 | -88.1 | 504990 | 493 | -89.4 | 504990 | 262 |
| MR_1774414608_18C9A7D8 | 504990 | 617 | -88.4 | 504990 | 351 | -92.8 | 504990 | 493 | -90.0 | 504990 | 262 |
| MR_1774414608_4B7640F8 | 504990 | 617 | -88.4 | 504990 | 351 | -91.1 | 504990 | 493 | -90.5 | 504990 | 262 |
| MR_1774414608_A577C3B8 | 504990 | 351 | -91.0 | 504990 | 617 | -86.7 | 504990 | 493 | -92.3 | 504990 | 262 |
| MR_1774414608_83E70192 | 504990 | 351 | -91.3 | 504990 | 617 | -89.3 | 504990 | 493 | -90.7 | 504990 | 262 |
| MR_1774414608_CFAAF2AC | 504990 | 351 | -90.7 | 504990 | 617 | -88.6 | 504990 | 493 | -89.6 | 504990 | 262 |
| MR_1774414608_12091168 | 504990 | 351 | -93.6 | 504990 | 617 | -87.1 | 504990 | 493 | -89.2 | 504990 | 262 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 591: `73fe4a26-25b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `73fe4a26-25b6-4e93-9b46-e1caf93c37cb` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Decrease A3 Offset threshold for 3273709_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[591] topology](images/train_0591.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3273709_3 **← 정답**
- `C2`: Lift the tilt angle  of 3246828_2 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273709_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246828_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273709_3
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase transmission power for 3273709_3
- `C8`: Lift the tilt angle of 3273709_3 by 8 degrees
- `C9`: Add neighbor relationship between 3277016_4 and 3246828_2
- `C10`: Add neighbor relationship between 3273709_3 and 3246828_2
- `C11`: Decrease transmission power for 3246828_2
- `C12`: Increase A3 Offset threshold for 3246828_2
- `C13`: Press down the tilt angle  of 3246828_2 by 10 degrees
- `C14`: Check test server and transmission issues
- `C15`: Press down the tilt angle of 3273709_3 by 8 degrees
- `C16`: Increase A3 Offset threshold for 3273709_3
- `C17`: Decrease A3 Offset threshold for 3246828_2
- `C18`: Adjust the azimuth of 3246828_2 by 50 degrees
- `C19`: Decrease transmission power for 3273709_3
- `C20`: Adjust the azimuth of 3273709_3 by 50 degrees
- `C21`: Increase transmission power for 3246828_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246828_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.315 | MS1 | 121.4656767063 | 31.1446349981 | 661 | 504990 | -79.45 | 15.40 | 463.43 | 0.02 | 2.32 | 1597 |
| 2024-09-20 22:21:32.207 | MS1 | 121.4656658904 | 31.1446196508 | 661 | 504990 | -84.45 | 12.83 | 344.75 | 0.08 | 2.05 | 1588 |
| 2024-09-20 22:21:33.616 | MS1 | 121.4656617289 | 31.1446346790 | 661 | 504990 | -77.50 | 16.07 | 471.51 | 0.01 | 2.17 | 1562 |
| 2024-09-20 22:21:34.180 | MS1 | 121.4656702952 | 31.1446333367 | 661 | 504990 | -87.07 | -0.88 | 77.55 | 0.06 | 1.32 | 1588 |
| 2024-09-20 22:21:35.190 | MS1 | 121.4656678324 | 31.1446307452 | 661 | 504990 | -90.22 | -2.27 | 63.08 | 0.15 | 1.09 | 1574 |
| 2024-09-20 22:21:36.956 | MS1 | 121.4656749822 | 31.1446303671 | 661 | 504990 | -83.90 | -2.47 | 41.25 | 0.11 | 1.16 | 1566 |
| 2024-09-20 22:21:37.160 | MS1 | 121.4656590841 | 31.1446188067 | 661 | 504990 | -87.22 | -0.18 | 33.61 | 0.04 | 1.19 | 1589 |
| 2024-09-20 22:21:38.800 | MS1 | 121.4656702315 | 31.1446344931 | 661 | 504990 | -87.81 | -3.19 | 54.50 | 0.13 | 1.41 | 1590 |
| 2024-09-20 22:21:39.930 | MS1 | 121.4656704391 | 31.1446247370 | 611 | 504990 | -76.25 | 15.82 | 207.86 | 0.17 | 1.13 | 1584 |
| 2024-09-20 22:21:40.166 | MS1 | 121.4656597321 | 31.1446200596 | 611 | 504990 | -84.84 | 13.18 | 547.13 | 0.19 | 2.67 | 1563 |
| 2024-09-20 22:21:41.175 | MS1 | 121.4656584586 | 31.1446335740 | 611 | 504990 | -82.78 | 13.84 | 486.74 | 0.06 | 2.36 | 1567 |
| 2024-09-20 22:21:42.753 | MS1 | 121.4656661729 | 31.1446183840 | 611 | 504990 | -79.37 | 14.28 | 413.17 | 0.04 | 2.81 | 1583 |

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
| 3246828 | 2 | 121.4747593673 | 31.1472894609 | 158 | 8 | 2 | 35.5 | TDD | 611 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3250721 | 1 | 121.4699477101 | 31.1496362320 | 117 | 0 | 7 | 31.3 | TDD | 609 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3273709 | 3 | 121.4693071898 | 31.1484194109 | 62 | 5 | 11 | 26.3 | TDD | 661 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3277016 | 4 | 121.4648981057 | 31.1546219020 | 293 | 13 | 0 | 36.1 | TDD | 574 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.843 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.866 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.016 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.016 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.731 | NREventA3 | measId:2;ServCellPCI:383;Se... |
| 2024-09-20 22:21:37.971 | NRHandoverAttempt | SourcePCI:383;SourceNR-ARFC... |
| 2024-09-20 22:21:38.013 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.026 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.155 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.155 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250721 | 1 | 13.5633 | 9.8492 | -115.6961 | 9.9991 | 182.8242 | 0.0188 | 0.0063 |
| 2024_09_20 22:00 | 3246828 | 2 | 6.4134 | 14.5429 | -114.0172 | 9.2758 | 189.5860 | 0.0169 | 0.0149 |
| 2024_09_20 22:00 | 3273709 | 3 | 19.3030 | 8.2920 | -117.8976 | 15.4817 | 123.5228 | 0.0129 | 0.1415 |
| 2024_09_20 22:00 | 3277016 | 4 | 15.6621 | 8.6182 | -114.1487 | 5.9460 | 113.4019 | 0.0120 | 0.0171 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415764_22FC9608 | 504990 | 611 | -80.6 | 504990 | 661 | -86.9 | 504990 | 574 | -86.5 | 504990 | 609 |
| MR_1774415764_F41329C5 | 504990 | 661 | -86.8 | 504990 | 611 | -82.0 | 504990 | 574 | -83.3 | 504990 | 609 |
| MR_1774415764_E59F6C7A | 504990 | 611 | -80.8 | 504990 | 661 | -86.0 | 504990 | 574 | -83.6 | 504990 | 609 |
| MR_1774415764_599309E0 | 504990 | 661 | -88.9 | 504990 | 611 | -83.1 | 504990 | 574 | -84.4 | 504990 | 609 |
| MR_1774415764_4180C08C | 504990 | 611 | -83.4 | 504990 | 661 | -88.8 | 504990 | 574 | -83.7 | 504990 | 609 |
| MR_1774415764_45229809 | 504990 | 611 | -82.2 | 504990 | 661 | -88.1 | 504990 | 574 | -84.2 | 504990 | 609 |
| MR_1774415764_10134714 | 504990 | 611 | -83.5 | 504990 | 661 | -88.1 | 504990 | 574 | -84.3 | 504990 | 609 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 592: `afd0d62d-c6f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `afd0d62d-c6fc-4967-b130-d182960125ad` |
| Tag | **multiple-answer** |
| 정답 | **C4|C11** |
| C4 의미 | Adjust the azimuth of 3213963_1 by 48 degrees |
| C11 의미 | Increase transmission power for 3213963_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[592] topology](images/train_0592.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3233056_2 by 3 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233056_2
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Adjust the azimuth of 3213963_1 by 48 degrees **← 정답**
- `C5`: Lift the tilt angle of 3213963_1 by 10 degrees
- `C6`: Decrease transmission power for 3233056_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213963_1
- `C8`: Press down the tilt angle of 3213963_1 by 10 degrees
- `C9`: Increase transmission power for 3233056_2
- `C10`: Adjust the azimuth of 3233056_2 by 10 degrees
- `C11`: Increase transmission power for 3213963_1 **← 정답**
- `C12`: Press down the tilt angle  of 3233056_2 by 3 degrees
- `C13`: Decrease A3 Offset threshold for 3213963_1
- `C14`: Add neighbor relationship between 3213963_1 and 3233056_2
- `C15`: Increase A3 Offset threshold for 3233056_2
- `C16`: Check test server and transmission issues
- `C17`: Decrease transmission power for 3213963_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213963_1
- `C19`: Increase A3 Offset threshold for 3213963_1
- `C20`: Decrease A3 Offset threshold for 3233056_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233056_2
- `C22`: Add neighbor relationship between 3212311_3 and 3233056_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.557 | MS1 | 121.4656618652 | 31.1446339103 | 453 | 504990 | -88.77 | 12.27 | 547.21 | 0.11 | 2.38 | 1581 |
| 2024-09-20 22:21:32.795 | MS1 | 121.4656622669 | 31.1446326318 | 453 | 504990 | -89.11 | 17.35 | 436.50 | 0.03 | 2.63 | 1585 |
| 2024-09-20 22:21:33.392 | MS1 | 121.4656687145 | 31.1446216183 | 453 | 504990 | -85.81 | 14.93 | 343.57 | 0.03 | 2.12 | 1576 |
| 2024-09-20 22:21:34.468 | MS1 | 121.4656767784 | 31.1446230590 | 453 | 504990 | -106.82 | 0.68 | 60.39 | 0.01 | 1.19 | 1577 |
| 2024-09-20 22:21:35.440 | MS1 | 121.4656611294 | 31.1446252218 | 453 | 504990 | -108.28 | -0.07 | 34.07 | 0.14 | 1.02 | 1566 |
| 2024-09-20 22:21:36.963 | MS1 | 121.4656672371 | 31.1446374892 | 453 | 504990 | -104.77 | -0.37 | 70.08 | 0.09 | 1.27 | 1574 |
| 2024-09-20 22:21:37.637 | MS1 | 121.4656725659 | 31.1446336633 | 453 | 504990 | -108.65 | -1.51 | 47.43 | 0.13 | 1.49 | 1594 |
| 2024-09-20 22:21:38.262 | MS1 | 121.4656613099 | 31.1446329367 | 453 | 504990 | -102.65 | 0.65 | 77.49 | 0.15 | 1.38 | 1597 |
| 2024-09-20 22:21:39.336 | MS1 | 121.4656680576 | 31.1446356681 | 453 | 504990 | -106.02 | -0.05 | 63.24 | 0.20 | 1.02 | 1574 |
| 2024-09-20 22:21:40.901 | MS1 | 121.4656667773 | 31.1446198045 | 453 | 504990 | -90.57 | 15.47 | 327.33 | 0.13 | 2.43 | 1595 |
| 2024-09-20 22:21:41.807 | MS1 | 121.4656598551 | 31.1446361927 | 453 | 504990 | -85.79 | 12.06 | 498.75 | 0.17 | 2.09 | 1596 |
| 2024-09-20 22:21:42.790 | MS1 | 121.4656719434 | 31.1446351498 | 453 | 504990 | -93.59 | 16.23 | 532.37 | 0.10 | 2.45 | 1581 |

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
| 3212311 | 3 | 121.4685382314 | 31.1528606531 | 256 | 10 | 3 | 15.2 | TDD | 964 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3213963 | 1 | 121.4641187594 | 31.1441537966 | 22 | 3 | 5 | 18.9 | TDD | 453 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3233056 | 2 | 121.4706491632 | 31.1532735848 | 216 | 2 | 10 | 21.3 | TDD | 260 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3258411 | 4 | 121.4646284211 | 31.1447069373 | 144 | 15 | 5 | 42.9 | TDD | 277 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.965 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.083 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.083 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.318 | NREventA2 | measId:1;ServCellPCI:543;Se... |
| 2024-09-20 22:21:34.420 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213963 | 1 | 9.2681 | 19.6861 | -114.9160 | 14.9067 | 111.6580 | 0.1378 | 0.0142 |
| 2024_09_20 22:00 | 3233056 | 2 | 8.4719 | 16.4750 | -116.8394 | 13.3063 | 109.2144 | 0.0087 | 0.0010 |
| 2024_09_20 22:00 | 3212311 | 3 | 19.7168 | 18.8361 | -115.6973 | 12.3283 | 154.0170 | 0.0060 | 0.0013 |
| 2024_09_20 22:00 | 3258411 | 4 | 17.9366 | 5.9801 | -115.9629 | 8.1638 | 101.2582 | 0.0014 | 0.0135 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415616_6A1CA307 | 504990 | 453 | -107.3 | 504990 | 260 | -111.1 | 504990 | 964 | -118.3 | 504990 | 277 |
| MR_1774415616_ACC46BC5 | 504990 | 453 | -107.1 | 504990 | 260 | -112.4 | 504990 | 964 | -119.1 | 504990 | 277 |
| MR_1774415616_C41040A2 | 504990 | 453 | -105.4 | 504990 | 260 | -114.4 | 504990 | 964 | -118.4 | 504990 | 277 |
| MR_1774415616_FCEF0D37 | 504990 | 453 | -106.3 | 504990 | 260 | -112.1 | 504990 | 964 | -120.4 | 504990 | 277 |
| MR_1774415616_F39291FD | 504990 | 453 | -107.1 | 504990 | 260 | -111.9 | 504990 | 964 | -119.3 | 504990 | 277 |
| MR_1774415616_E56AAEFF | 504990 | 453 | -106.2 | 504990 | 260 | -114.5 | 504990 | 964 | -119.4 | 504990 | 277 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 593: `1685f7e5-ec8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1685f7e5-ec8d-4798-9551-3dda0cff9dfb` |
| Tag | **multiple-answer** |
| 정답 | **C7|C14** |
| C7 의미 | Adjust the azimuth of 3235811_2 by 50 degrees |
| C14 의미 | Increase transmission power for 3235811_2 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[593] topology](images/train_0593.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3214416_3 by 46 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214416_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214416_3
- `C4`: Lift the tilt angle of 3235811_2 by 10 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235811_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235811_2
- `C7`: Adjust the azimuth of 3235811_2 by 50 degrees **← 정답**
- `C8`: Increase A3 Offset threshold for 3214416_3
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease A3 Offset threshold for 3235811_2
- `C11`: Check test server and transmission issues
- `C12`: Increase A3 Offset threshold for 3235811_2
- `C13`: Lift the tilt angle  of 3214416_3 by 4 degrees
- `C14`: Increase transmission power for 3235811_2 **← 정답**
- `C15`: Press down the tilt angle  of 3214416_3 by 4 degrees
- `C16`: Decrease A3 Offset threshold for 3214416_3
- `C17`: Increase transmission power for 3214416_3
- `C18`: Add neighbor relationship between 3235811_2 and 3214416_3
- `C19`: Press down the tilt angle of 3235811_2 by 10 degrees
- `C20`: Decrease transmission power for 3235811_2
- `C21`: Decrease transmission power for 3214416_3
- `C22`: Add neighbor relationship between 3212576_4 and 3214416_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.503 | MS1 | 121.4656667487 | 31.1446185962 | 809 | 504990 | -92.61 | 12.30 | 327.00 | 0.11 | 2.80 | 1592 |
| 2024-09-20 22:21:32.561 | MS1 | 121.4656617999 | 31.1446188312 | 809 | 504990 | -89.68 | 14.24 | 505.48 | 0.04 | 2.17 | 1595 |
| 2024-09-20 22:21:33.250 | MS1 | 121.4656611765 | 31.1446340249 | 809 | 504990 | -88.11 | 13.03 | 293.57 | 0.06 | 2.73 | 1565 |
| 2024-09-20 22:21:34.407 | MS1 | 121.4656618425 | 31.1446291366 | 809 | 504990 | -101.21 | 1.43 | 66.23 | 0.19 | 1.21 | 1585 |
| 2024-09-20 22:21:35.675 | MS1 | 121.4656697398 | 31.1446294346 | 809 | 504990 | -105.49 | 1.00 | 45.77 | 0.11 | 1.49 | 1588 |
| 2024-09-20 22:21:36.475 | MS1 | 121.4656749884 | 31.1446335102 | 809 | 504990 | -106.38 | 1.82 | 65.04 | 0.10 | 1.13 | 1584 |
| 2024-09-20 22:21:37.187 | MS1 | 121.4656734896 | 31.1446271295 | 809 | 504990 | -100.07 | -1.00 | 86.75 | 0.08 | 1.22 | 1574 |
| 2024-09-20 22:21:38.808 | MS1 | 121.4656702696 | 31.1446311258 | 809 | 504990 | -108.72 | -0.33 | 32.22 | 0.10 | 1.34 | 1599 |
| 2024-09-20 22:21:39.740 | MS1 | 121.4656590099 | 31.1446280593 | 809 | 504990 | -107.95 | -0.10 | 61.27 | 0.20 | 1.31 | 1593 |
| 2024-09-20 22:21:40.709 | MS1 | 121.4656682083 | 31.1446241627 | 809 | 504990 | -94.90 | 12.62 | 396.97 | 0.11 | 2.50 | 1581 |
| 2024-09-20 22:21:41.694 | MS1 | 121.4656621399 | 31.1446282387 | 809 | 504990 | -94.92 | 13.89 | 554.81 | 0.01 | 2.49 | 1572 |
| 2024-09-20 22:21:42.202 | MS1 | 121.4656687833 | 31.1446195166 | 809 | 504990 | -92.92 | 14.78 | 356.46 | 0.17 | 2.34 | 1586 |

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
| 3212576 | 4 | 121.4751837483 | 31.1444601264 | 1 | 0 | 3 | 43.3 | TDD | 502 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3214416 | 3 | 121.4663615442 | 31.1502407701 | 232 | 0 | 12 | 39.8 | TDD | 301 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3235811 | 2 | 121.4641400646 | 31.1493564871 | 93 | 13 | 9 | 22.1 | TDD | 809 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3245612 | 1 | 121.4675494983 | 31.1555097161 | 182 | 11 | 5 | 41.6 | TDD | 416 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.065 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.088 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.194 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.194 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.384 | NREventA2 | measId:1;ServCellPCI:333;Se... |
| 2024-09-20 22:21:34.498 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245612 | 1 | 7.9274 | 8.8774 | -116.5820 | 7.9011 | 181.3465 | 0.0040 | 0.0170 |
| 2024_09_20 22:00 | 3235811 | 2 | 6.8990 | 19.5814 | -117.4562 | 8.0907 | 155.6735 | 0.1958 | 0.0113 |
| 2024_09_20 22:00 | 3214416 | 3 | 5.4326 | 10.8423 | -114.1127 | 6.0326 | 144.4861 | 0.0175 | 0.0085 |
| 2024_09_20 22:00 | 3212576 | 4 | 6.3669 | 5.8302 | -114.4169 | 10.0477 | 149.0862 | 0.0174 | 0.0071 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415415_7C8860BE | 504990 | 809 | -102.3 | 504990 | 301 | -106.9 | 504990 | 502 | -109.2 | 504990 | 416 |
| MR_1774415415_BECD0697 | 504990 | 809 | -100.2 | 504990 | 301 | -107.3 | 504990 | 502 | -112.6 | 504990 | 416 |
| MR_1774415415_0276DFEC | 504990 | 809 | -100.4 | 504990 | 301 | -108.1 | 504990 | 502 | -109.5 | 504990 | 416 |
| MR_1774415415_01630F7B | 504990 | 809 | -100.0 | 504990 | 301 | -105.8 | 504990 | 502 | -111.4 | 504990 | 416 |
| MR_1774415415_5C03D22D | 504990 | 809 | -100.2 | 504990 | 301 | -107.0 | 504990 | 502 | -111.7 | 504990 | 416 |
| MR_1774415415_3E7EE1A0 | 504990 | 809 | -102.0 | 504990 | 301 | -106.8 | 504990 | 502 | -111.9 | 504990 | 416 |
| MR_1774415415_F1B94E8E | 504990 | 809 | -99.6 | 504990 | 301 | -106.9 | 504990 | 502 | -110.0 | 504990 | 416 |
| MR_1774415415_F1842434 | 504990 | 809 | -102.8 | 504990 | 301 | -107.1 | 504990 | 502 | -109.1 | 504990 | 416 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 594: `1f31fa25-2fa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1f31fa25-2fa0-4fd4-b573-db9b8778031c` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease A3 Offset threshold for 3225084_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[594] topology](images/train_0594.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3259694_4 by 50 degrees
- `C2`: Lift the tilt angle of 3225084_3 by 10 degrees
- `C3`: Decrease A3 Offset threshold for 3225084_3 **← 정답**
- `C4`: Add neighbor relationship between 3249292_1 and 3259694_4
- `C5`: Decrease A3 Offset threshold for 3259694_4
- `C6`: Check test server and transmission issues
- `C7`: Increase transmission power for 3259694_4
- `C8`: Press down the tilt angle  of 3259694_4 by 9 degrees
- `C9`: Increase transmission power for 3225084_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259694_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225084_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259694_4
- `C13`: Press down the tilt angle of 3225084_3 by 10 degrees
- `C14`: Adjust the azimuth of 3225084_3 by 19 degrees
- `C15`: Decrease transmission power for 3225084_3
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Add neighbor relationship between 3225084_3 and 3259694_4
- `C18`: Increase A3 Offset threshold for 3259694_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225084_3
- `C20`: Increase A3 Offset threshold for 3225084_3
- `C21`: Decrease transmission power for 3259694_4
- `C22`: Lift the tilt angle  of 3259694_4 by 9 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.264 | MS1 | 121.4656776812 | 31.1446317876 | 375 | 504990 | -84.57 | 15.04 | 540.05 | 0.13 | 2.18 | 1595 |
| 2024-09-20 22:21:32.119 | MS1 | 121.4656684397 | 31.1446300888 | 375 | 504990 | -79.57 | 15.31 | 554.52 | 0.10 | 2.87 | 1577 |
| 2024-09-20 22:21:33.591 | MS1 | 121.4656600754 | 31.1446192947 | 375 | 504990 | -76.32 | 15.64 | 406.67 | 0.14 | 2.43 | 1560 |
| 2024-09-20 22:21:34.747 | MS1 | 121.4656752305 | 31.1446218954 | 375 | 504990 | -84.79 | -2.31 | 49.74 | 0.19 | 1.08 | 1599 |
| 2024-09-20 22:21:35.417 | MS1 | 121.4656612377 | 31.1446197728 | 375 | 504990 | -92.61 | -2.59 | 45.83 | 0.02 | 1.27 | 1597 |
| 2024-09-20 22:21:36.427 | MS1 | 121.4656590970 | 31.1446196134 | 375 | 504990 | -86.38 | -3.61 | 40.52 | 0.04 | 1.09 | 1582 |
| 2024-09-20 22:21:37.891 | MS1 | 121.4656704784 | 31.1446358487 | 375 | 504990 | -83.05 | -3.48 | 42.07 | 0.01 | 1.03 | 1574 |
| 2024-09-20 22:21:38.978 | MS1 | 121.4656661320 | 31.1446228585 | 375 | 504990 | -92.86 | -2.07 | 56.59 | 0.13 | 1.23 | 1598 |
| 2024-09-20 22:21:39.209 | MS1 | 121.4656600701 | 31.1446191254 | 499 | 504990 | -80.07 | 12.04 | 271.70 | 0.10 | 1.15 | 1585 |
| 2024-09-20 22:21:40.280 | MS1 | 121.4656585490 | 31.1446302920 | 499 | 504990 | -81.76 | 15.58 | 404.82 | 0.04 | 2.91 | 1571 |
| 2024-09-20 22:21:41.503 | MS1 | 121.4656593284 | 31.1446244729 | 499 | 504990 | -76.02 | 12.25 | 483.92 | 0.17 | 2.31 | 1575 |
| 2024-09-20 22:21:42.684 | MS1 | 121.4656739973 | 31.1446194623 | 499 | 504990 | -78.77 | 13.27 | 580.59 | 0.09 | 2.54 | 1567 |

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
| 3220142 | 2 | 121.4671362899 | 31.1471295678 | 264 | 6 | 7 | 24.3 | TDD | 11 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3225084 | 3 | 121.4688673764 | 31.1527617425 | 218 | 8 | 3 | 40.4 | TDD | 375 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3249292 | 1 | 121.4709909861 | 31.1522676141 | 195 | 9 | 12 | 20.5 | TDD | 520 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3259694 | 4 | 121.4667625843 | 31.1522968066 | 242 | 8 | 1 | 15.6 | TDD | 499 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.366 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.386 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.493 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.493 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.257 | NREventA3 | measId:2;ServCellPCI:518;Se... |
| 2024-09-20 22:21:38.497 | NRHandoverAttempt | SourcePCI:518;SourceNR-ARFC... |
| 2024-09-20 22:21:38.539 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.549 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.686 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.686 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249292 | 1 | 13.0816 | 14.9279 | -116.3474 | 10.7499 | 127.3986 | 0.0155 | 0.0121 |
| 2024_09_20 22:00 | 3220142 | 2 | 8.2437 | 19.5799 | -114.2543 | 5.9749 | 189.5057 | 0.0163 | 0.0104 |
| 2024_09_20 22:00 | 3225084 | 3 | 13.4632 | 11.4970 | -115.4208 | 15.0052 | 135.7448 | 0.0146 | 0.1501 |
| 2024_09_20 22:00 | 3259694 | 4 | 5.7518 | 19.2256 | -114.9827 | 7.5068 | 154.3475 | 0.0006 | 0.0093 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413498_CDFDAC5D | 504990 | 375 | -85.6 | 504990 | 499 | -77.5 | 504990 | 520 | -89.9 | 504990 | 11 |
| MR_1774413498_BB9F920D | 504990 | 375 | -83.0 | 504990 | 499 | -78.9 | 504990 | 520 | -87.1 | 504990 | 11 |
| MR_1774413498_A9BCE708 | 504990 | 499 | -78.6 | 504990 | 375 | -86.2 | 504990 | 520 | -88.1 | 504990 | 11 |
| MR_1774413498_B060C555 | 504990 | 499 | -81.0 | 504990 | 375 | -82.9 | 504990 | 520 | -89.3 | 504990 | 11 |
| MR_1774413498_DDB09FC3 | 504990 | 499 | -78.1 | 504990 | 375 | -86.6 | 504990 | 520 | -89.3 | 504990 | 11 |
| MR_1774413498_945F9CB1 | 504990 | 499 | -77.9 | 504990 | 375 | -86.8 | 504990 | 520 | -87.6 | 504990 | 11 |
| MR_1774413498_52274954 | 504990 | 375 | -84.3 | 504990 | 499 | -81.1 | 504990 | 520 | -88.6 | 504990 | 11 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 595: `c7946f43-3ce...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c7946f43-3cea-43a2-b146-8ce872a08b28` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease A3 Offset threshold for 3219143_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[595] topology](images/train_0595.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3219143_3 and 3268187_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219143_3
- `C3`: Decrease transmission power for 3268187_1
- `C4`: Increase A3 Offset threshold for 3219143_3
- `C5`: Decrease A3 Offset threshold for 3268187_1
- `C6`: Lift the tilt angle of 3219143_3 by 8 degrees
- `C7`: Increase transmission power for 3268187_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Press down the tilt angle  of 3268187_1 by 5 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268187_1
- `C11`: Increase A3 Offset threshold for 3268187_1
- `C12`: Decrease A3 Offset threshold for 3219143_3 **← 정답**
- `C13`: Increase transmission power for 3219143_3
- `C14`: Decrease transmission power for 3219143_3
- `C15`: Press down the tilt angle of 3219143_3 by 8 degrees
- `C16`: Adjust the azimuth of 3219143_3 by 50 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268187_1
- `C18`: Check test server and transmission issues
- `C19`: Adjust the azimuth of 3268187_1 by 34 degrees
- `C20`: Lift the tilt angle  of 3268187_1 by 5 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219143_3
- `C22`: Add neighbor relationship between 3273697_2 and 3268187_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.884 | MS1 | 121.4656645896 | 31.1446221445 | 701 | 504990 | -77.79 | 12.03 | 437.55 | 0.04 | 2.62 | 1567 |
| 2024-09-20 22:21:32.365 | MS1 | 121.4656720443 | 31.1446377766 | 701 | 504990 | -81.75 | 15.99 | 582.21 | 0.14 | 2.90 | 1568 |
| 2024-09-20 22:21:33.885 | MS1 | 121.4656752950 | 31.1446309389 | 701 | 504990 | -75.48 | 17.90 | 566.47 | 0.03 | 2.44 | 1584 |
| 2024-09-20 22:21:34.234 | MS1 | 121.4656707940 | 31.1446301017 | 701 | 504990 | -92.72 | -2.61 | 65.65 | 0.01 | 1.02 | 1594 |
| 2024-09-20 22:21:35.420 | MS1 | 121.4656595248 | 31.1446349079 | 701 | 504990 | -91.79 | -0.95 | 59.63 | 0.08 | 1.43 | 1596 |
| 2024-09-20 22:21:36.225 | MS1 | 121.4656684636 | 31.1446202634 | 701 | 504990 | -87.86 | -0.50 | 41.85 | 0.07 | 1.03 | 1596 |
| 2024-09-20 22:21:37.742 | MS1 | 121.4656619926 | 31.1446219774 | 701 | 504990 | -85.56 | -1.80 | 40.02 | 0.10 | 1.02 | 1576 |
| 2024-09-20 22:21:38.178 | MS1 | 121.4656618061 | 31.1446352275 | 701 | 504990 | -91.75 | -2.90 | 71.53 | 0.17 | 1.02 | 1580 |
| 2024-09-20 22:21:39.878 | MS1 | 121.4656650890 | 31.1446351727 | 369 | 504990 | -84.89 | 12.78 | 193.48 | 0.14 | 1.17 | 1570 |
| 2024-09-20 22:21:40.963 | MS1 | 121.4656654932 | 31.1446286720 | 369 | 504990 | -80.11 | 14.89 | 402.23 | 0.08 | 2.79 | 1581 |
| 2024-09-20 22:21:41.922 | MS1 | 121.4656582886 | 31.1446317037 | 369 | 504990 | -84.17 | 12.46 | 484.18 | 0.07 | 2.69 | 1579 |
| 2024-09-20 22:21:42.667 | MS1 | 121.4656733708 | 31.1446216809 | 369 | 504990 | -75.31 | 12.65 | 577.72 | 0.08 | 2.02 | 1583 |

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
| 3219143 | 3 | 121.4745337163 | 31.1497099094 | 39 | 5 | 8 | 49.1 | TDD | 701 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3268187 | 1 | 121.4645318779 | 31.1532452279 | 208 | 3 | 11 | 34.5 | TDD | 369 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3269083 | 4 | 121.4687076835 | 31.1507019717 | 144 | 1 | 10 | 30.2 | TDD | 166 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3273697 | 2 | 121.4674409822 | 31.1469027498 | 193 | 14 | 5 | 26.9 | TDD | 393 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.410 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.429 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.560 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.560 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.223 | NREventA3 | measId:2;ServCellPCI:566;Se... |
| 2024-09-20 22:21:38.463 | NRHandoverAttempt | SourcePCI:566;SourceNR-ARFC... |
| 2024-09-20 22:21:38.501 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.513 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.634 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.634 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268187 | 1 | 11.8507 | 14.0403 | -116.6036 | 8.3829 | 192.7838 | 0.0197 | 0.0013 |
| 2024_09_20 22:00 | 3273697 | 2 | 5.0869 | 19.4361 | -117.8186 | 15.7541 | 127.8486 | 0.0146 | 0.0133 |
| 2024_09_20 22:00 | 3219143 | 3 | 11.4452 | 10.4188 | -116.4146 | 17.3100 | 182.2968 | 0.0113 | 0.1155 |
| 2024_09_20 22:00 | 3269083 | 4 | 5.9560 | 7.4659 | -116.1461 | 15.1326 | 162.8430 | 0.0124 | 0.0127 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415057_3D474CCD | 504990 | 369 | -86.8 | 504990 | 701 | -93.7 | 504990 | 393 | -93.7 | 504990 | 166 |
| MR_1774415057_26437799 | 504990 | 369 | -88.7 | 504990 | 701 | -93.7 | 504990 | 393 | -94.1 | 504990 | 166 |
| MR_1774415057_B7131B05 | 504990 | 369 | -90.5 | 504990 | 701 | -92.7 | 504990 | 393 | -92.8 | 504990 | 166 |
| MR_1774415057_9C6D95E3 | 504990 | 369 | -90.4 | 504990 | 701 | -93.3 | 504990 | 393 | -93.9 | 504990 | 166 |
| MR_1774415057_277EEB53 | 504990 | 701 | -93.2 | 504990 | 369 | -87.1 | 504990 | 393 | -95.2 | 504990 | 166 |
| MR_1774415057_7CAD9FA0 | 504990 | 701 | -92.1 | 504990 | 369 | -89.0 | 504990 | 393 | -92.7 | 504990 | 166 |
| MR_1774415057_9252A775 | 504990 | 369 | -88.6 | 504990 | 701 | -92.7 | 504990 | 393 | -95.6 | 504990 | 166 |
| MR_1774415057_A9732480 | 504990 | 701 | -94.6 | 504990 | 369 | -89.7 | 504990 | 393 | -92.8 | 504990 | 166 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 596: `eee1493f-f1e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `eee1493f-f1e6-4227-aa98-a21224d5a2ee` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease A3 Offset threshold for 3279977_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[596] topology](images/train_0596.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279977_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247879_4
- `C3`: Lift the tilt angle  of 3247879_4 by 5 degrees
- `C4`: Add neighbor relationship between 3259469_1 and 3247879_4
- `C5`: Lift the tilt angle of 3279977_2 by 10 degrees
- `C6`: Press down the tilt angle  of 3247879_4 by 5 degrees
- `C7`: Increase transmission power for 3247879_4
- `C8`: Adjust the azimuth of 3247879_4 by 18 degrees
- `C9`: Decrease A3 Offset threshold for 3247879_4
- `C10`: Decrease transmission power for 3279977_2
- `C11`: Press down the tilt angle of 3279977_2 by 10 degrees
- `C12`: Check test server and transmission issues
- `C13`: Increase A3 Offset threshold for 3247879_4
- `C14`: Decrease A3 Offset threshold for 3279977_2 **← 정답**
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279977_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247879_4
- `C17`: Increase A3 Offset threshold for 3279977_2
- `C18`: Increase transmission power for 3279977_2
- `C19`: Decrease transmission power for 3247879_4
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Add neighbor relationship between 3279977_2 and 3247879_4
- `C22`: Adjust the azimuth of 3279977_2 by 31 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.428 | MS1 | 121.4656761903 | 31.1446346291 | 682 | 504990 | -81.85 | 14.89 | 580.69 | 0.04 | 2.03 | 1568 |
| 2024-09-20 22:21:32.297 | MS1 | 121.4656596113 | 31.1446264425 | 682 | 504990 | -77.90 | 17.31 | 389.05 | 0.10 | 2.59 | 1572 |
| 2024-09-20 22:21:33.691 | MS1 | 121.4656670374 | 31.1446371296 | 682 | 504990 | -77.27 | 13.16 | 436.35 | 0.04 | 2.54 | 1599 |
| 2024-09-20 22:21:34.777 | MS1 | 121.4656745248 | 31.1446204809 | 682 | 504990 | -86.46 | -0.73 | 41.50 | 0.04 | 1.38 | 1592 |
| 2024-09-20 22:21:35.443 | MS1 | 121.4656626506 | 31.1446186402 | 682 | 504990 | -83.36 | -0.97 | 21.85 | 0.13 | 1.46 | 1580 |
| 2024-09-20 22:21:36.292 | MS1 | 121.4656583118 | 31.1446304654 | 682 | 504990 | -89.09 | -1.55 | 75.42 | 0.14 | 1.39 | 1578 |
| 2024-09-20 22:21:37.619 | MS1 | 121.4656658350 | 31.1446254625 | 682 | 504990 | -84.11 | -0.88 | 39.48 | 0.08 | 1.34 | 1597 |
| 2024-09-20 22:21:38.775 | MS1 | 121.4656721945 | 31.1446244512 | 682 | 504990 | -91.11 | -0.58 | 53.02 | 0.13 | 1.48 | 1591 |
| 2024-09-20 22:21:39.742 | MS1 | 121.4656661521 | 31.1446358473 | 950 | 504990 | -82.08 | 12.08 | 217.17 | 0.15 | 1.46 | 1562 |
| 2024-09-20 22:21:40.424 | MS1 | 121.4656653455 | 31.1446315200 | 950 | 504990 | -79.64 | 12.18 | 361.07 | 0.19 | 2.24 | 1563 |
| 2024-09-20 22:21:41.750 | MS1 | 121.4656635888 | 31.1446340947 | 950 | 504990 | -77.23 | 15.36 | 483.52 | 0.02 | 2.06 | 1567 |
| 2024-09-20 22:21:42.889 | MS1 | 121.4656666647 | 31.1446369133 | 950 | 504990 | -80.15 | 13.46 | 483.54 | 0.10 | 2.19 | 1597 |

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
| 3245039 | 3 | 121.4686537215 | 31.1496189097 | 355 | 11 | 10 | 48.8 | TDD | 341 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3247879 | 4 | 121.4741664115 | 31.1537330488 | 201 | 4 | 8 | 23.4 | TDD | 950 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3259469 | 1 | 121.4722195563 | 31.1494240186 | 7 | 12 | 8 | 22.9 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3279977 | 2 | 121.4663848115 | 31.1544354613 | 215 | 14 | 5 | 17.1 | TDD | 682 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.115 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.132 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.272 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.272 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.999 | NREventA3 | measId:2;ServCellPCI:601;Se... |
| 2024-09-20 22:21:38.239 | NRHandoverAttempt | SourcePCI:601;SourceNR-ARFC... |
| 2024-09-20 22:21:38.272 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.282 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.417 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.417 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259469 | 1 | 19.1334 | 9.1343 | -116.3457 | 13.8496 | 112.9814 | 0.0067 | 0.0182 |
| 2024_09_20 22:00 | 3279977 | 2 | 14.6997 | 16.9617 | -116.4117 | 12.4378 | 196.3579 | 0.0084 | 0.1021 |
| 2024_09_20 22:00 | 3245039 | 3 | 7.2079 | 18.6465 | -117.4703 | 15.3042 | 89.3280 | 0.0176 | 0.0002 |
| 2024_09_20 22:00 | 3247879 | 4 | 5.0597 | 15.3754 | -115.5183 | 14.9814 | 130.5802 | 0.0009 | 0.0168 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414933_A2A644EE | 504990 | 682 | -85.2 | 504990 | 950 | -83.4 | 504990 | 441 | -83.7 | 504990 | 341 |
| MR_1774414933_EE9B3AE6 | 504990 | 950 | -82.3 | 504990 | 682 | -84.9 | 504990 | 441 | -83.0 | 504990 | 341 |
| MR_1774414933_34CF13F7 | 504990 | 682 | -86.8 | 504990 | 950 | -80.6 | 504990 | 441 | -85.9 | 504990 | 341 |
| MR_1774414933_D0E2EA23 | 504990 | 682 | -87.7 | 504990 | 950 | -82.8 | 504990 | 441 | -86.8 | 504990 | 341 |
| MR_1774414933_8B1941B3 | 504990 | 682 | -85.3 | 504990 | 950 | -81.9 | 504990 | 441 | -85.1 | 504990 | 341 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 597: `55870f87-ba8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `55870f87-ba8e-4ad2-af0e-c0d6745083c3` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[597] topology](images/train_0597.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3263391_2
- `C2`: Adjust the azimuth of 3263391_2 by 50 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263391_2
- `C4`: Decrease A3 Offset threshold for 3263391_2
- `C5`: Press down the tilt angle  of 3263391_2 by 9 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247506_3
- `C7`: Decrease A3 Offset threshold for 3247506_3
- `C8`: Increase transmission power for 3247506_3
- `C9`: Insufficient data; more data is needed for judgment. **← 정답**
- `C10`: Increase A3 Offset threshold for 3263391_2
- `C11`: Check test server and transmission issues
- `C12`: Add neighbor relationship between 3247927_1 and 3263391_2
- `C13`: Decrease transmission power for 3263391_2
- `C14`: Adjust the azimuth of 3247506_3 by 8 degrees
- `C15`: Decrease transmission power for 3247506_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247506_3
- `C17`: Increase A3 Offset threshold for 3247506_3
- `C18`: Add neighbor relationship between 3247506_3 and 3263391_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263391_2
- `C20`: Lift the tilt angle  of 3263391_2 by 9 degrees
- `C21`: Press down the tilt angle of 3247506_3 by 10 degrees
- `C22`: Lift the tilt angle of 3247506_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.299 | MS1 | 121.4656746123 | 31.1446187378 | 309 | 504990 | -89.77 | 15.05 | 493.19 | 0.02 | 2.06 | 1576 |
| 2024-09-20 22:21:32.449 | MS1 | 121.4656633255 | 31.1446325409 | 309 | 504990 | -87.96 | 13.74 | 461.54 | 0.03 | 2.35 | 1562 |
| 2024-09-20 22:21:33.724 | MS1 | 121.4656747396 | 31.1446338796 | 309 | 504990 | -87.67 | 13.07 | 401.64 | 0.13 | 2.29 | 1564 |
| 2024-09-20 22:21:34.693 | MS1 | 121.4656630473 | 31.1446378052 | 309 | 504990 | -87.25 | 12.21 | 80.36 | 0.03 | 2.25 | 1563 |
| 2024-09-20 22:21:35.982 | MS1 | 121.4656694731 | 31.1446271991 | 309 | 504990 | -85.34 | 17.40 | 81.14 | 0.18 | 2.23 | 1593 |
| 2024-09-20 22:21:36.871 | MS1 | 121.4656757240 | 31.1446262169 | 309 | 504990 | -86.02 | 13.39 | 101.83 | 0.13 | 2.95 | 1597 |
| 2024-09-20 22:21:37.811 | MS1 | 121.4656762480 | 31.1446225824 | 309 | 504990 | -93.10 | 10.17 | 79.85 | 0.10 | 2.59 | 1589 |
| 2024-09-20 22:21:38.813 | MS1 | 121.4656591265 | 31.1446268904 | 309 | 504990 | -91.51 | 10.25 | 79.15 | 0.03 | 2.86 | 1593 |
| 2024-09-20 22:21:39.349 | MS1 | 121.4656663047 | 31.1446261313 | 309 | 504990 | -91.71 | 8.49 | 66.67 | 0.08 | 2.12 | 1599 |
| 2024-09-20 22:21:40.187 | MS1 | 121.4656746601 | 31.1446199446 | 309 | 504990 | -93.91 | 12.62 | 328.76 | 0.15 | 2.32 | 1578 |
| 2024-09-20 22:21:41.541 | MS1 | 121.4656768068 | 31.1446269571 | 309 | 504990 | -91.83 | 8.80 | 494.60 | 0.05 | 2.94 | 1563 |
| 2024-09-20 22:21:42.364 | MS1 | 121.4656716880 | 31.1446240785 | 309 | 504990 | -91.48 | 8.82 | 381.41 | 0.14 | 2.56 | 1566 |

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
| 3230234 | 4 | 121.4752765287 | 31.1534898079 | 53 | 12 | 11 | 17.8 | TDD | 423 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3247506 | 3 | 121.4651171256 | 31.1444460324 | 77 | 3 | 1 | 21.0 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3247927 | 1 | 121.4711245740 | 31.1487836121 | 122 | 8 | 10 | 48.6 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3263391 | 2 | 121.4738237925 | 31.1466773896 | 175 | 7 | 8 | 30.2 | TDD | 907 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.110 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.128 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.229 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.229 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.949 | NREventA3 | measId:2;ServCellPCI:278;Se... |
| 2024-09-20 22:21:38.189 | NRHandoverAttempt | SourcePCI:278;SourceNR-ARFC... |
| 2024-09-20 22:21:38.226 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.240 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.345 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.345 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3247927 | 1 | 75.5893 | 92.0330 | -115.2384 | 6.3164 | 150.7573 | 0.0106 | 0.0154 |
| 2024_09_19 22:00 | 3263391 | 2 | 86.6792 | 78.6628 | -117.5782 | 15.2921 | 136.6575 | 0.0035 | 0.0063 |
| 2024_09_19 22:00 | 3247506 | 3 | 91.7481 | 76.5916 | -115.6319 | 16.0910 | 165.9370 | 0.0130 | 0.0183 |
| 2024_09_19 22:00 | 3230234 | 4 | 80.3967 | 91.5318 | -117.3427 | 18.2061 | 91.8103 | 0.0160 | 0.0054 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412725_E40AE8E2 | 504990 | 309 | -85.3 | 504990 | 907 | -92.2 | 504990 | 355 | -93.1 | 504990 | 423 |
| MR_1774412725_C22E4EFD | 504990 | 309 | -87.3 | 504990 | 907 | -90.7 | 504990 | 355 | -92.9 | 504990 | 423 |
| MR_1774412725_01DB1D47 | 504990 | 309 | -85.6 | 504990 | 907 | -89.7 | 504990 | 355 | -94.1 | 504990 | 423 |
| MR_1774412725_EA03B64F | 504990 | 309 | -86.7 | 504990 | 907 | -91.5 | 504990 | 355 | -94.3 | 504990 | 423 |
| MR_1774412725_1527B06F | 504990 | 309 | -86.4 | 504990 | 907 | -90.5 | 504990 | 355 | -95.0 | 504990 | 423 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 598: `c587ce54-be8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c587ce54-be89-43e7-8ad7-6358fc6c0b79` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3248901_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[598] topology](images/train_0598.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3248901_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217089_1
- `C3`: Add neighbor relationship between 3258246_2 and 3217089_1
- `C4`: Decrease A3 Offset threshold for 3217089_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217089_1
- `C6`: Press down the tilt angle of 3248901_3 by 6 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248901_3
- `C8`: Increase transmission power for 3217089_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease transmission power for 3217089_1
- `C11`: Lift the tilt angle of 3248901_3 by 6 degrees
- `C12`: Add neighbor relationship between 3248901_3 and 3217089_1
- `C13`: Press down the tilt angle  of 3217089_1 by 7 degrees
- `C14`: Increase transmission power for 3248901_3
- `C15`: Decrease A3 Offset threshold for 3248901_3
- `C16`: Adjust the azimuth of 3248901_3 by 32 degrees
- `C17`: Lift the tilt angle  of 3217089_1 by 7 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248901_3 **← 정답**
- `C19`: Increase A3 Offset threshold for 3248901_3
- `C20`: Check test server and transmission issues
- `C21`: Adjust the azimuth of 3217089_1 by 50 degrees
- `C22`: Increase A3 Offset threshold for 3217089_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.606 | MS1 | 121.4656624374 | 31.1446294137 | 524 | 504990 | -91.84 | 12.65 | 589.08 | 0.12 | 2.68 | 1577 |
| 2024-09-20 22:21:32.908 | MS1 | 121.4656759175 | 31.1446344772 | 524 | 504990 | -91.22 | 17.22 | 437.46 | 0.16 | 2.22 | 1585 |
| 2024-09-20 22:21:33.710 | MS1 | 121.4656777617 | 31.1446228938 | 524 | 504990 | -87.05 | 16.52 | 563.44 | 0.11 | 2.42 | 1586 |
| 2024-09-20 22:21:34.672 | MS1 | 121.4656615293 | 31.1446256042 | 524 | 504990 | -87.13 | 17.60 | 91.36 | 0.59 | 2.33 | 693 |
| 2024-09-20 22:21:35.976 | MS1 | 121.4656699856 | 31.1446348589 | 524 | 504990 | -88.16 | 13.04 | 57.76 | 0.59 | 2.29 | 599 |
| 2024-09-20 22:21:36.150 | MS1 | 121.4656740462 | 31.1446186489 | 524 | 504990 | -85.36 | 13.21 | 76.36 | 0.56 | 2.27 | 559 |
| 2024-09-20 22:21:37.420 | MS1 | 121.4656651530 | 31.1446331938 | 524 | 504990 | -89.28 | 10.05 | 94.34 | 0.66 | 2.19 | 624 |
| 2024-09-20 22:21:38.449 | MS1 | 121.4656741052 | 31.1446340507 | 524 | 504990 | -91.40 | 9.13 | 84.07 | 0.55 | 2.26 | 672 |
| 2024-09-20 22:21:39.904 | MS1 | 121.4656726483 | 31.1446208017 | 524 | 504990 | -92.07 | 11.38 | 65.87 | 0.51 | 2.81 | 679 |
| 2024-09-20 22:21:40.550 | MS1 | 121.4656587484 | 31.1446313624 | 524 | 504990 | -93.20 | 8.31 | 593.22 | 0.08 | 2.29 | 1589 |
| 2024-09-20 22:21:41.588 | MS1 | 121.4656702437 | 31.1446320517 | 524 | 504990 | -93.67 | 11.63 | 567.09 | 0.10 | 2.61 | 1583 |
| 2024-09-20 22:21:42.967 | MS1 | 121.4656617153 | 31.1446364063 | 524 | 504990 | -90.20 | 11.61 | 398.09 | 0.13 | 2.01 | 1561 |

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
| 3217089 | 1 | 121.4687182287 | 31.1492592122 | 107 | 5 | 6 | 22.2 | TDD | 505 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3242115 | 4 | 121.4741253744 | 31.1532211076 | 311 | 3 | 7 | 40.3 | TDD | 710 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3248901 | 3 | 121.4749630757 | 31.1553579676 | 249 | 5 | 0 | 17.7 | TDD | 524 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3258246 | 2 | 121.4698775341 | 31.1487734963 | 288 | 6 | 12 | 30.7 | TDD | 146 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.920 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.944 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.061 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.061 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.755 | NREventA3 | measId:2;ServCellPCI:908;Se... |
| 2024-09-20 22:21:37.995 | NRHandoverAttempt | SourcePCI:908;SourceNR-ARFC... |
| 2024-09-20 22:21:38.031 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.046 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.176 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.176 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217089 | 1 | 17.9965 | 15.8864 | -114.1641 | 14.9458 | 198.0784 | 0.0144 | 0.0040 |
| 2024_09_20 22:00 | 3258246 | 2 | 12.3980 | 12.8163 | -116.9918 | 12.5128 | 181.1761 | 0.0022 | 0.0008 |
| 2024_09_20 22:00 | 3248901 | 3 | 16.9211 | 15.9936 | -116.0954 | 16.7092 | 96.2743 | 0.0194 | 0.0174 |
| 2024_09_20 22:00 | 3242115 | 4 | 8.7460 | 11.9235 | -116.3536 | 10.4129 | 187.4934 | 0.0033 | 0.0045 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412715_4B231993 | 504990 | 524 | -87.5 | 504990 | 505 | -96.2 | 504990 | 146 | -94.5 | 504990 | 710 |
| MR_1774412715_27F1BE3D | 504990 | 524 | -85.6 | 504990 | 505 | -95.8 | 504990 | 146 | -94.6 | 504990 | 710 |
| MR_1774412715_F3A5469F | 504990 | 524 | -88.3 | 504990 | 505 | -92.3 | 504990 | 146 | -96.2 | 504990 | 710 |
| MR_1774412715_909056B7 | 504990 | 524 | -85.3 | 504990 | 505 | -94.3 | 504990 | 146 | -95.6 | 504990 | 710 |
| MR_1774412715_A86D2740 | 504990 | 524 | -88.4 | 504990 | 505 | -95.0 | 504990 | 146 | -97.6 | 504990 | 710 |
| MR_1774412715_13CB2D9A | 504990 | 524 | -86.0 | 504990 | 505 | -92.9 | 504990 | 146 | -97.3 | 504990 | 710 |
| MR_1774412715_E91CAE8F | 504990 | 524 | -87.8 | 504990 | 505 | -94.4 | 504990 | 146 | -95.7 | 504990 | 710 |
| MR_1774412715_0D41F6A7 | 504990 | 524 | -87.9 | 504990 | 505 | -95.1 | 504990 | 146 | -94.4 | 504990 | 710 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 599: `3a1c22dc-b4b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3a1c22dc-b4bc-43d5-af1c-c71feebd9377` |
| Tag | **multiple-answer** |
| 정답 | **C10|C21** |
| C10 의미 | Decrease transmission power for 3224559_3 |
| C21 의미 | Press down the tilt angle  of 3224559_3 by 1 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[599] topology](images/train_0599.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3227149_4 and 3224559_3
- `C2`: Check test server and transmission issues
- `C3`: Adjust the azimuth of 3224559_3 by 25 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224559_3
- `C5`: Lift the tilt angle of 3226047_1 by 2 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224559_3
- `C7`: Decrease A3 Offset threshold for 3224559_3
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase transmission power for 3226047_1
- `C10`: Decrease transmission power for 3224559_3 **← 정답**
- `C11`: Increase transmission power for 3224559_3
- `C12`: Press down the tilt angle of 3226047_1 by 2 degrees
- `C13`: Lift the tilt angle  of 3224559_3 by 1 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226047_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226047_1
- `C16`: Increase A3 Offset threshold for 3226047_1
- `C17`: Adjust the azimuth of 3226047_1 by 34 degrees
- `C18`: Add neighbor relationship between 3226047_1 and 3224559_3
- `C19`: Decrease A3 Offset threshold for 3226047_1
- `C20`: Increase A3 Offset threshold for 3224559_3
- `C21`: Press down the tilt angle  of 3224559_3 by 1 degrees **← 정답**
- `C22`: Decrease transmission power for 3226047_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.936 | MS1 | 121.4656607395 | 31.1446246049 | 498 | 504990 | -82.38 | 14.45 | 461.37 | 0.15 | 2.90 | 1594 |
| 2024-09-20 22:21:32.234 | MS1 | 121.4656740912 | 31.1446224277 | 498 | 504990 | -84.85 | 17.60 | 411.81 | 0.05 | 2.03 | 1589 |
| 2024-09-20 22:21:33.887 | MS1 | 121.4656733779 | 31.1446300429 | 498 | 504990 | -84.52 | 15.63 | 564.15 | 0.17 | 2.40 | 1582 |
| 2024-09-20 22:21:34.978 | MS1 | 121.4656644062 | 31.1446222285 | 498 | 504990 | -92.02 | 3.51 | 72.96 | 0.11 | 1.13 | 1590 |
| 2024-09-20 22:21:35.294 | MS1 | 121.4656770726 | 31.1446205029 | 498 | 504990 | -89.19 | 1.81 | 47.29 | 0.03 | 1.13 | 1564 |
| 2024-09-20 22:21:36.602 | MS1 | 121.4656743009 | 31.1446300659 | 498 | 504990 | -86.31 | 1.54 | 54.28 | 0.17 | 1.45 | 1594 |
| 2024-09-20 22:21:37.507 | MS1 | 121.4656740437 | 31.1446290126 | 498 | 504990 | -89.11 | 3.71 | 89.33 | 0.06 | 1.15 | 1588 |
| 2024-09-20 22:21:38.256 | MS1 | 121.4656772431 | 31.1446346183 | 498 | 504990 | -91.18 | 1.67 | 51.93 | 0.14 | 1.46 | 1592 |
| 2024-09-20 22:21:39.620 | MS1 | 121.4656707439 | 31.1446317450 | 498 | 504990 | -89.88 | 1.54 | 81.61 | 0.09 | 1.35 | 1578 |
| 2024-09-20 22:21:40.356 | MS1 | 121.4656668953 | 31.1446205602 | 498 | 504990 | -78.79 | 17.36 | 416.54 | 0.16 | 2.73 | 1600 |
| 2024-09-20 22:21:41.917 | MS1 | 121.4656769618 | 31.1446203313 | 498 | 504990 | -76.94 | 15.63 | 487.80 | 0.10 | 2.73 | 1592 |
| 2024-09-20 22:21:42.850 | MS1 | 121.4656634882 | 31.1446240836 | 498 | 504990 | -83.87 | 16.57 | 358.91 | 0.14 | 2.49 | 1567 |

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
| 3224559 | 3 | 121.4641502444 | 31.1536233365 | 197 | 0 | 8 | 25.3 | TDD | 852 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3226047 | 1 | 121.4653054041 | 31.1539053957 | 212 | 0 | 12 | 39.3 | TDD | 498 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3227149 | 4 | 121.4652705589 | 31.1543838543 | 30 | 13 | 5 | 16.3 | TDD | 863 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3261694 | 2 | 121.4691130579 | 31.1511479703 | 113 | 15 | 6 | 17.0 | TDD | 371 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.784 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.799 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.907 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.907 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226047 | 1 | 11.4248 | 5.6983 | -108.0454 | 5.0826 | 184.3441 | 0.0166 | 0.0090 |
| 2024_09_20 22:00 | 3261694 | 2 | 8.1534 | 17.6926 | -117.6809 | 5.6787 | 145.1684 | 0.0004 | 0.0108 |
| 2024_09_20 22:00 | 3224559 | 3 | 17.3861 | 6.6080 | -115.0900 | 18.7674 | 192.6741 | 0.0175 | 0.0008 |
| 2024_09_20 22:00 | 3227149 | 4 | 9.6157 | 11.1175 | -114.0893 | 13.4652 | 122.9055 | 0.0011 | 0.0036 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413313_7D37DDFD | 504990 | 498 | -93.5 | 504990 | 852 | -94.4 | 504990 | 863 | -94.7 | 504990 | 371 |
| MR_1774413313_01E54BE3 | 504990 | 852 | -91.5 | 504990 | 498 | -94.3 | 504990 | 863 | -95.2 | 504990 | 371 |
| MR_1774413313_03CDEEF6 | 504990 | 852 | -93.2 | 504990 | 498 | -93.3 | 504990 | 863 | -93.9 | 504990 | 371 |
| MR_1774413313_E2FDDA0C | 504990 | 852 | -90.3 | 504990 | 498 | -94.6 | 504990 | 863 | -93.3 | 504990 | 371 |
| MR_1774413313_A55112B3 | 504990 | 852 | -92.1 | 504990 | 498 | -91.2 | 504990 | 863 | -95.5 | 504990 | 371 |
| MR_1774413313_6CA8045C | 504990 | 498 | -93.9 | 504990 | 852 | -93.1 | 504990 | 863 | -92.6 | 504990 | 371 |
| MR_1774413313_111E4E8D | 504990 | 498 | -93.4 | 504990 | 852 | -93.1 | 504990 | 863 | -94.7 | 504990 | 371 |

> *... 2개 열 생략 (전체 14열)*

---
