# Track A 문제 분석 — train[1490]~train[1499]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1490] ~ train[1499] (10개)

## 목차

1. [문제 1490: `b8356801-8ab...`](#1490) — single-answer, 정답: C2
2. [문제 1491: `8b408022-bc1...`](#1491) — single-answer, 정답: C19
3. [문제 1492: `15885477-788...`](#1492) — single-answer, 정답: C5
4. [문제 1493: `5c6f0168-eb5...`](#1493) — single-answer, 정답: C3
5. [문제 1494: `94af0e29-0ca...`](#1494) — single-answer, 정답: C2
6. [문제 1495: `ff185a7f-ea3...`](#1495) — single-answer, 정답: C11
7. [문제 1496: `e8b5bde9-116...`](#1496) — single-answer, 정답: C21
8. [문제 1497: `2ffbfb42-5ca...`](#1497) — single-answer, 정답: C13
9. [문제 1498: `d7b6dc94-61b...`](#1498) — single-answer, 정답: C19
10. [문제 1499: `ea1d036c-15e...`](#1499) — multiple-answer, 정답: C1|C9|C16|C18

---

### 문제 1490: `b8356801-8ab...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b8356801-8abe-41d1-8ec6-d45590b355dd` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1490] topology](images/train_1490.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248299_2
- `C2`: Insufficient data; more data is needed for judgment. **← 정답**
- `C3`: Increase A3 Offset threshold for 3248299_2
- `C4`: Add neighbor relationship between 3220962_3 and 3242915_1
- `C5`: Add neighbor relationship between 3248299_2 and 3242915_1
- `C6`: Increase transmission power for 3248299_2
- `C7`: Lift the tilt angle of 3248299_2 by 10 degrees
- `C8`: Press down the tilt angle  of 3242915_1 by 10 degrees
- `C9`: Decrease A3 Offset threshold for 3248299_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242915_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242915_1
- `C12`: Increase A3 Offset threshold for 3242915_1
- `C13`: Adjust the azimuth of 3242915_1 by 50 degrees
- `C14`: Adjust the azimuth of 3248299_2 by 50 degrees
- `C15`: Decrease transmission power for 3248299_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248299_2
- `C17`: Lift the tilt angle  of 3242915_1 by 10 degrees
- `C18`: Decrease A3 Offset threshold for 3242915_1
- `C19`: Increase transmission power for 3242915_1
- `C20`: Press down the tilt angle of 3248299_2 by 10 degrees
- `C21`: Check test server and transmission issues
- `C22`: Decrease transmission power for 3242915_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.141 | MS1 | 121.4656680305 | 31.1446183276 | 676 | 504990 | -86.13 | 15.28 | 516.68 | 0.16 | 2.42 | 1594 |
| 2024-09-20 22:21:32.573 | MS1 | 121.4656608829 | 31.1446295599 | 676 | 504990 | -91.99 | 17.11 | 322.91 | 0.11 | 2.51 | 1569 |
| 2024-09-20 22:21:33.930 | MS1 | 121.4656602416 | 31.1446287549 | 676 | 504990 | -89.82 | 15.35 | 397.54 | 0.13 | 2.82 | 1578 |
| 2024-09-20 22:21:34.213 | MS1 | 121.4656638121 | 31.1446251089 | 676 | 504990 | -87.16 | 12.36 | 66.56 | 0.04 | 2.64 | 1588 |
| 2024-09-20 22:21:35.480 | MS1 | 121.4656701592 | 31.1446195900 | 676 | 504990 | -88.39 | 16.62 | 94.00 | 0.08 | 2.74 | 1596 |
| 2024-09-20 22:21:36.915 | MS1 | 121.4656592828 | 31.1446340371 | 676 | 504990 | -88.78 | 14.86 | 94.81 | 0.05 | 2.65 | 1575 |
| 2024-09-20 22:21:37.905 | MS1 | 121.4656728584 | 31.1446268560 | 676 | 504990 | -91.28 | 12.52 | 94.68 | 0.18 | 2.49 | 1590 |
| 2024-09-20 22:21:38.881 | MS1 | 121.4656734260 | 31.1446249508 | 676 | 504990 | -91.22 | 7.44 | 89.90 | 0.02 | 2.59 | 1567 |
| 2024-09-20 22:21:39.122 | MS1 | 121.4656708866 | 31.1446283021 | 676 | 504990 | -90.59 | 8.53 | 67.25 | 0.18 | 2.16 | 1575 |
| 2024-09-20 22:21:40.846 | MS1 | 121.4656729300 | 31.1446212897 | 676 | 504990 | -91.13 | 7.95 | 321.96 | 0.10 | 2.77 | 1578 |
| 2024-09-20 22:21:41.767 | MS1 | 121.4656669691 | 31.1446272841 | 676 | 504990 | -92.85 | 9.04 | 579.36 | 0.12 | 2.30 | 1573 |
| 2024-09-20 22:21:42.899 | MS1 | 121.4656697193 | 31.1446234006 | 676 | 504990 | -93.88 | 7.82 | 549.03 | 0.10 | 2.48 | 1585 |

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
| 3220962 | 3 | 121.4728110610 | 31.1473941951 | 297 | 2 | 5 | 26.9 | TDD | 113 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3242915 | 1 | 121.4685895474 | 31.1446072899 | 208 | 12 | 0 | 37.3 | TDD | 257 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3248299 | 2 | 121.4692217994 | 31.1473031369 | 167 | 8 | 5 | 23.0 | TDD | 676 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3279863 | 4 | 121.4699477834 | 31.1544499687 | 249 | 2 | 0 | 32.9 | TDD | 199 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.794 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.810 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:30.934 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.934 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.666 | NREventA3 | measId:2;ServCellPCI:854;Se... |
| 2024-09-20 22:21:37.906 | NRHandoverAttempt | SourcePCI:854;SourceNR-ARFC... |
| 2024-09-20 22:21:37.936 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.947 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.061 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.061 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3242915 | 1 | 84.9492 | 91.3944 | -114.8300 | 9.4768 | 133.2360 | 0.0063 | 0.0067 |
| 2024_09_19 22:00 | 3248299 | 2 | 88.6317 | 93.1984 | -116.1940 | 10.6727 | 183.7277 | 0.0013 | 0.0015 |
| 2024_09_19 22:00 | 3220962 | 3 | 92.7544 | 85.3222 | -114.2502 | 17.9020 | 192.2248 | 0.0062 | 0.0096 |
| 2024_09_19 22:00 | 3279863 | 4 | 90.1821 | 94.9881 | -117.7793 | 5.0397 | 175.8303 | 0.0025 | 0.0081 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415279_0F7BA66F | 504990 | 676 | -85.3 | 504990 | 257 | -89.6 | 504990 | 113 | -102.0 | 504990 | 199 |
| MR_1774415279_565C1C96 | 504990 | 676 | -85.3 | 504990 | 257 | -90.1 | 504990 | 113 | -102.0 | 504990 | 199 |
| MR_1774415279_A585CB10 | 504990 | 676 | -88.6 | 504990 | 257 | -92.7 | 504990 | 113 | -102.3 | 504990 | 199 |
| MR_1774415279_9ADF373C | 504990 | 676 | -85.8 | 504990 | 257 | -91.9 | 504990 | 113 | -102.1 | 504990 | 199 |
| MR_1774415279_592B3264 | 504990 | 676 | -85.7 | 504990 | 257 | -89.3 | 504990 | 113 | -100.7 | 504990 | 199 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1491: `8b408022-bc1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8b408022-bc13-4d7d-a374-c2de22bf084f` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1491] topology](images/train_1491.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3241442_3
- `C2`: Press down the tilt angle  of 3210619_1 by 6 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241442_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210619_1
- `C5`: Increase transmission power for 3210619_1
- `C6`: Increase A3 Offset threshold for 3241442_3
- `C7`: Add neighbor relationship between 3241442_3 and 3210619_1
- `C8`: Add neighbor relationship between 3264186_2 and 3210619_1
- `C9`: Lift the tilt angle  of 3210619_1 by 6 degrees
- `C10`: Decrease transmission power for 3210619_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase A3 Offset threshold for 3210619_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210619_1
- `C14`: Lift the tilt angle of 3241442_3 by 10 degrees
- `C15`: Increase transmission power for 3241442_3
- `C16`: Adjust the azimuth of 3241442_3 by 35 degrees
- `C17`: Press down the tilt angle of 3241442_3 by 10 degrees
- `C18`: Decrease transmission power for 3241442_3
- `C19`: Check test server and transmission issues **← 정답**
- `C20`: Adjust the azimuth of 3210619_1 by 29 degrees
- `C21`: Decrease A3 Offset threshold for 3210619_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241442_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.869 | MS1 | 121.4656716486 | 31.1446327071 | 854 | 504990 | -89.42 | 14.45 | 463.84 | 0.14 | 2.72 | 1598 |
| 2024-09-20 22:21:32.427 | MS1 | 121.4656662727 | 31.1446229550 | 854 | 504990 | -90.50 | 14.09 | 483.90 | 0.20 | 2.97 | 1568 |
| 2024-09-20 22:21:33.359 | MS1 | 121.4656737217 | 31.1446333401 | 854 | 504990 | -88.60 | 13.04 | 447.76 | 0.13 | 2.77 | 1594 |
| 2024-09-20 22:21:34.640 | MS1 | 121.4656595469 | 31.1446208048 | 854 | 504990 | -90.35 | 15.68 | 88.54 | 0.10 | 2.20 | 472 |
| 2024-09-20 22:21:35.522 | MS1 | 121.4656705054 | 31.1446234200 | 854 | 504990 | -90.85 | 14.10 | 86.17 | 0.00 | 2.37 | 449 |
| 2024-09-20 22:21:36.662 | MS1 | 121.4656588492 | 31.1446248526 | 854 | 504990 | -89.41 | 17.85 | 78.66 | 0.20 | 2.68 | 351 |
| 2024-09-20 22:21:37.418 | MS1 | 121.4656736618 | 31.1446278668 | 854 | 504990 | -89.65 | 10.57 | 64.01 | 0.14 | 2.54 | 331 |
| 2024-09-20 22:21:38.658 | MS1 | 121.4656615625 | 31.1446283110 | 854 | 504990 | -92.55 | 12.84 | 93.72 | 0.06 | 2.67 | 475 |
| 2024-09-20 22:21:39.604 | MS1 | 121.4656635052 | 31.1446306979 | 854 | 504990 | -89.64 | 7.80 | 57.65 | 0.19 | 2.04 | 422 |
| 2024-09-20 22:21:40.358 | MS1 | 121.4656613847 | 31.1446212530 | 854 | 504990 | -90.38 | 12.02 | 478.48 | 0.19 | 2.25 | 1566 |
| 2024-09-20 22:21:41.349 | MS1 | 121.4656740299 | 31.1446354137 | 854 | 504990 | -89.72 | 7.98 | 341.77 | 0.14 | 2.92 | 1576 |
| 2024-09-20 22:21:42.811 | MS1 | 121.4656585151 | 31.1446238291 | 854 | 504990 | -93.63 | 12.08 | 452.78 | 0.12 | 2.08 | 1583 |

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
| 3210619 | 1 | 121.4672381346 | 31.1486698349 | 169 | 2 | 1 | 31.6 | TDD | 613 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3241442 | 3 | 121.4740402566 | 31.1523515395 | 258 | 11 | 12 | 35.2 | TDD | 854 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3250160 | 4 | 121.4749718532 | 31.1556222512 | 232 | 2 | 7 | 32.9 | TDD | 215 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3264186 | 2 | 121.4654510246 | 31.1497739256 | 130 | 13 | 10 | 20.4 | TDD | 845 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.060 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.078 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.211 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.211 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.885 | NREventA3 | measId:2;ServCellPCI:14;Ser... |
| 2024-09-20 22:21:38.125 | NRHandoverAttempt | SourcePCI:14;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.157 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.172 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.306 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.306 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210619 | 1 | 12.7860 | 9.3148 | -115.1274 | 7.6603 | 194.7427 | 0.0073 | 0.0005 |
| 2024_09_20 22:00 | 3264186 | 2 | 7.8279 | 7.0467 | -116.1011 | 16.3590 | 173.2886 | 0.0001 | 0.0131 |
| 2024_09_20 22:00 | 3241442 | 3 | 19.7646 | 13.5705 | -116.5979 | 9.4525 | 107.0515 | 0.0179 | 0.0154 |
| 2024_09_20 22:00 | 3250160 | 4 | 5.7776 | 14.1616 | -116.1664 | 9.1403 | 85.4220 | 0.0139 | 0.0066 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415970_970AC03A | 504990 | 854 | -92.1 | 504990 | 613 | -97.1 | 504990 | 845 | -99.7 | 504990 | 215 |
| MR_1774415970_2BE092D5 | 504990 | 854 | -91.7 | 504990 | 613 | -98.6 | 504990 | 845 | -97.4 | 504990 | 215 |
| MR_1774415970_0AECAF98 | 504990 | 854 | -89.0 | 504990 | 613 | -96.7 | 504990 | 845 | -97.8 | 504990 | 215 |
| MR_1774415970_5CDDE80F | 504990 | 854 | -88.7 | 504990 | 613 | -95.7 | 504990 | 845 | -100.3 | 504990 | 215 |
| MR_1774415970_74058752 | 504990 | 854 | -91.3 | 504990 | 613 | -96.8 | 504990 | 845 | -97.0 | 504990 | 215 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1492: `15885477-788...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `15885477-7883-4883-bdb4-33426fe6dc0a` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Add neighbor relationship between 3218322_4 and 3213525_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1492] topology](images/train_1492.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218322_4
- `C2`: Lift the tilt angle of 3218322_4 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218322_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213525_1
- `C5`: Add neighbor relationship between 3218322_4 and 3213525_1 **← 정답**
- `C6`: Decrease A3 Offset threshold for 3218322_4
- `C7`: Adjust the azimuth of 3218322_4 by 29 degrees
- `C8`: Lift the tilt angle  of 3213525_1 by 5 degrees
- `C9`: Adjust the azimuth of 3213525_1 by 36 degrees
- `C10`: Decrease transmission power for 3213525_1
- `C11`: Press down the tilt angle  of 3213525_1 by 5 degrees
- `C12`: Check test server and transmission issues
- `C13`: Increase A3 Offset threshold for 3213525_1
- `C14`: Decrease transmission power for 3218322_4
- `C15`: Add neighbor relationship between 3252222_3 and 3213525_1
- `C16`: Increase A3 Offset threshold for 3218322_4
- `C17`: Increase transmission power for 3213525_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213525_1
- `C20`: Decrease A3 Offset threshold for 3213525_1
- `C21`: Press down the tilt angle of 3218322_4 by 10 degrees
- `C22`: Increase transmission power for 3218322_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.256 | MS1 | 121.4656687980 | 31.1446323559 | 47 | 504990 | -81.92 | 16.31 | 450.61 | 0.04 | 2.44 | 1597 |
| 2024-09-20 22:21:32.227 | MS1 | 121.4656675421 | 31.1446255775 | 47 | 504990 | -80.87 | 13.56 | 330.36 | 0.12 | 2.39 | 1582 |
| 2024-09-20 22:21:33.246 | MS1 | 121.4656626065 | 31.1446181381 | 47 | 504990 | -75.36 | 15.17 | 483.01 | 0.15 | 2.56 | 1599 |
| 2024-09-20 22:21:34.239 | MS1 | 121.4656643679 | 31.1446285550 | 47 | 504990 | -90.66 | -1.85 | 59.94 | 0.16 | 1.40 | 1600 |
| 2024-09-20 22:21:35.715 | MS1 | 121.4656687508 | 31.1446307602 | 47 | 504990 | -93.32 | -0.14 | 51.70 | 0.07 | 1.10 | 1590 |
| 2024-09-20 22:21:36.850 | MS1 | 121.4656716369 | 31.1446208821 | 47 | 504990 | -92.27 | -3.12 | 63.02 | 0.11 | 1.26 | 1564 |
| 2024-09-20 22:21:37.534 | MS1 | 121.4656583056 | 31.1446256889 | 47 | 504990 | -90.87 | -1.06 | 67.61 | 0.13 | 1.21 | 1587 |
| 2024-09-20 22:21:38.572 | MS1 | 121.4656779480 | 31.1446241357 | 47 | 504990 | -80.79 | 16.29 | 569.70 | 0.09 | 1.41 | 1570 |
| 2024-09-20 22:21:39.766 | MS1 | 121.4656657097 | 31.1446243202 | 47 | 504990 | -82.88 | 14.13 | 579.99 | 0.03 | 1.12 | 1591 |
| 2024-09-20 22:21:40.660 | MS1 | 121.4656615148 | 31.1446326000 | 47 | 504990 | -80.97 | 14.29 | 515.84 | 0.05 | 2.08 | 1595 |
| 2024-09-20 22:21:41.531 | MS1 | 121.4656712762 | 31.1446198510 | 47 | 504990 | -82.64 | 16.80 | 557.68 | 0.16 | 2.53 | 1593 |
| 2024-09-20 22:21:42.179 | MS1 | 121.4656768323 | 31.1446236571 | 47 | 504990 | -76.50 | 15.39 | 488.17 | 0.17 | 2.77 | 1579 |

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
| 3213525 | 1 | 121.4678386859 | 31.1494410737 | 165 | 1 | 5 | 37.5 | TDD | 456 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3218322 | 4 | 121.4686984351 | 31.1445051320 | 244 | 2 | 3 | 41.7 | TDD | 47 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3233050 | 2 | 121.4705438374 | 31.1449095582 | 111 | 0 | 3 | 26.4 | TDD | 603 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3252222 | 3 | 121.4696366626 | 31.1461933170 | 151 | 1 | 5 | 22.0 | TDD | 230 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.844 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.866 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.989 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.989 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.726 | NREventA3 | measId:2;ServCellPCI:726;Se... |
| 2024-09-20 22:21:35.726 | NREventA3 | measId:2;ServCellPCI:726;Se... |
| 2024-09-20 22:21:36.726 | NREventA3 | measId:2;ServCellPCI:726;Se... |
| 2024-09-20 22:21:39.226 | NRRRCReestablishAttempt | PCI:726 |
| 2024-09-20 22:21:39.244 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.258 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.404 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.404 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213525 | 1 | 14.0166 | 7.8816 | -116.3457 | 18.8580 | 190.2308 | 0.0059 | 0.0094 |
| 2024_09_20 22:00 | 3233050 | 2 | 5.8923 | 11.2494 | -117.9275 | 11.6759 | 182.3303 | 0.0118 | 0.0123 |
| 2024_09_20 22:00 | 3252222 | 3 | 11.9404 | 18.8534 | -115.6722 | 16.9525 | 137.6394 | 0.0136 | 0.0032 |
| 2024_09_20 22:00 | 3218322 | 4 | 12.6344 | 9.8466 | -115.7919 | 6.9295 | 158.2392 | 0.0154 | 0.1315 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413543_FC5919C1 | 504990 | 47 | -91.6 | 504990 | 456 | -87.1 | 504990 | 230 | -93.3 | 504990 | 603 |
| MR_1774413543_D179D677 | 504990 | 47 | -91.9 | 504990 | 456 | -86.4 | 504990 | 230 | -92.9 | 504990 | 603 |
| MR_1774413543_D18E0D30 | 504990 | 456 | -84.7 | 504990 | 47 | -89.4 | 504990 | 230 | -94.6 | 504990 | 603 |
| MR_1774413543_183B3E7E | 504990 | 456 | -84.7 | 504990 | 47 | -91.3 | 504990 | 230 | -93.4 | 504990 | 603 |
| MR_1774413543_74B44EA5 | 504990 | 47 | -91.2 | 504990 | 456 | -85.0 | 504990 | 230 | -93.4 | 504990 | 603 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1493: `5c6f0168-eb5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5c6f0168-eb5d-47e6-8352-d6612755f1bc` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Lift the tilt angle  of 3269177_3 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1493] topology](images/train_1493.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220329_4
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Lift the tilt angle  of 3269177_3 by 7 degrees **← 정답**
- `C4`: Decrease A3 Offset threshold for 3221496_1
- `C5`: Adjust the azimuth of 3220329_4 by 50 degrees
- `C6`: Increase A3 Offset threshold for 3220329_4
- `C7`: Increase A3 Offset threshold for 3221496_1
- `C8`: Add neighbor relationship between 3269177_3 and 3221496_1
- `C9`: Decrease transmission power for 3220329_4
- `C10`: Check test server and transmission issues
- `C11`: Add neighbor relationship between 3220329_4 and 3221496_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221496_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221496_1
- `C14`: Decrease transmission power for 3221496_1
- `C15`: Decrease A3 Offset threshold for 3220329_4
- `C16`: Increase transmission power for 3221496_1
- `C17`: Increase transmission power for 3220329_4
- `C18`: Adjust the azimuth of 3269177_3 by 50 degrees
- `C19`: Lift the tilt angle of 3220329_4 by 5 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220329_4
- `C21`: Press down the tilt angle of 3220329_4 by 5 degrees
- `C22`: Press down the tilt angle  of 3269177_3 by 7 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.340 | MS1 | 121.4656733369 | 31.1446258206 | 420 | 504990 | -90.25 | 12.46 | 542.26 | 0.10 | 2.23 | 1597 |
| 2024-09-20 22:21:32.838 | MS1 | 121.4656744867 | 31.1446198136 | 420 | 504990 | -88.81 | 14.82 | 543.63 | 0.18 | 2.61 | 1577 |
| 2024-09-20 22:21:33.266 | MS1 | 121.4656690672 | 31.1446208444 | 420 | 504990 | -86.82 | 17.55 | 434.03 | 0.14 | 2.44 | 1599 |
| 2024-09-20 22:21:34.128 | MS1 | 121.4656644501 | 31.1446343385 | 420 | 504990 | -91.02 | 16.98 | 63.23 | 0.03 | 2.62 | 1593 |
| 2024-09-20 22:21:35.605 | MS1 | 121.4656741544 | 31.1446215202 | 420 | 504990 | -90.82 | 16.44 | 70.78 | 0.18 | 2.06 | 1566 |
| 2024-09-20 22:21:36.610 | MS1 | 121.4656688565 | 31.1446263891 | 420 | 504990 | -91.61 | 13.74 | 94.02 | 0.01 | 3.00 | 1594 |
| 2024-09-20 22:21:37.620 | MS1 | 121.4656761476 | 31.1446299404 | 420 | 504990 | -89.69 | 7.86 | 99.97 | 0.08 | 2.09 | 1586 |
| 2024-09-20 22:21:38.155 | MS1 | 121.4656584538 | 31.1446320986 | 420 | 504990 | -90.55 | 10.25 | 90.64 | 0.02 | 2.15 | 1596 |
| 2024-09-20 22:21:39.639 | MS1 | 121.4656621860 | 31.1446318305 | 420 | 504990 | -92.38 | 10.96 | 52.01 | 0.13 | 2.59 | 1573 |
| 2024-09-20 22:21:40.472 | MS1 | 121.4656658414 | 31.1446321270 | 420 | 504990 | -92.37 | 8.70 | 487.07 | 0.12 | 2.68 | 1574 |
| 2024-09-20 22:21:41.732 | MS1 | 121.4656758466 | 31.1446358210 | 420 | 504990 | -93.67 | 11.67 | 493.51 | 0.04 | 2.85 | 1567 |
| 2024-09-20 22:21:42.808 | MS1 | 121.4656609929 | 31.1446290390 | 420 | 504990 | -92.11 | 7.01 | 522.69 | 0.08 | 2.17 | 1560 |

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
| 3220329 | 4 | 121.4680055422 | 31.1527071367 | 144 | 3 | 5 | 28.8 | TDD | 420 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3221496 | 1 | 121.4640846503 | 31.1503711105 | 243 | 4 | 6 | 35.6 | TDD | 417 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3229762 | 2 | 121.4758577153 | 31.1516924812 | 224 | 14 | 3 | 31.3 | TDD | 913 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3269177 | 3 | 121.4719566889 | 31.1463626672 | 342 | 1 | 0 | 46.4 | TDD | 427 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.267 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.415 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.415 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.089 | NREventA3 | measId:2;ServCellPCI:706;Se... |
| 2024-09-20 22:21:38.329 | NRHandoverAttempt | SourcePCI:706;SourceNR-ARFC... |
| 2024-09-20 22:21:38.373 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.388 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.513 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.513 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221496 | 1 | 7.4968 | 11.8431 | -117.3608 | 17.3419 | 156.7343 | 0.0192 | 0.0060 |
| 2024_09_20 22:00 | 3229762 | 2 | 13.5097 | 14.2003 | -116.8903 | 14.2072 | 103.7539 | 0.0078 | 0.0098 |
| 2024_09_20 22:00 | 3269177 | 3 | 18.4298 | 9.5371 | -115.2607 | 10.8221 | 153.7817 | 0.0159 | 0.0185 |
| 2024_09_20 22:00 | 3220329 | 4 | 88.0389 | 89.5179 | -117.4701 | 12.2036 | 88.0501 | 0.0156 | 0.0137 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414982_7EC383CB | 504990 | 420 | -89.5 | 504990 | 417 | -97.9 | 504990 | 427 | -100.8 | 504990 | 913 |
| MR_1774414982_80569255 | 504990 | 420 | -91.2 | 504990 | 417 | -96.6 | 504990 | 427 | -101.0 | 504990 | 913 |
| MR_1774414982_0EB38828 | 504990 | 420 | -89.3 | 504990 | 417 | -97.6 | 504990 | 427 | -100.8 | 504990 | 913 |
| MR_1774414982_27AFFB72 | 504990 | 420 | -91.8 | 504990 | 417 | -99.3 | 504990 | 427 | -102.1 | 504990 | 913 |
| MR_1774414982_C27C01AF | 504990 | 420 | -89.5 | 504990 | 417 | -99.3 | 504990 | 427 | -100.4 | 504990 | 913 |
| MR_1774414982_B4B53084 | 504990 | 420 | -92.0 | 504990 | 417 | -97.3 | 504990 | 427 | -100.7 | 504990 | 913 |
| MR_1774414982_B3FCF5A6 | 504990 | 420 | -91.5 | 504990 | 417 | -96.4 | 504990 | 427 | -99.9 | 504990 | 913 |
| MR_1774414982_7913546D | 504990 | 420 | -91.6 | 504990 | 417 | -98.9 | 504990 | 427 | -99.1 | 504990 | 913 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1494: `94af0e29-0ca...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `94af0e29-0ca0-4a3d-b3bf-d8de4e937ab0` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Add neighbor relationship between 3228129_4 and 3268707_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1494] topology](images/train_1494.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3228129_4
- `C2`: Add neighbor relationship between 3228129_4 and 3268707_2 **← 정답**
- `C3`: Lift the tilt angle  of 3268707_2 by 2 degrees
- `C4`: Decrease A3 Offset threshold for 3268707_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228129_4
- `C6`: Increase transmission power for 3268707_2
- `C7`: Adjust the azimuth of 3228129_4 by 50 degrees
- `C8`: Press down the tilt angle of 3228129_4 by 10 degrees
- `C9`: Check test server and transmission issues
- `C10`: Increase A3 Offset threshold for 3228129_4
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Adjust the azimuth of 3268707_2 by 41 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268707_2
- `C14`: Lift the tilt angle of 3228129_4 by 10 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228129_4
- `C16`: Increase A3 Offset threshold for 3268707_2
- `C17`: Press down the tilt angle  of 3268707_2 by 2 degrees
- `C18`: Decrease transmission power for 3268707_2
- `C19`: Increase transmission power for 3228129_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268707_2
- `C21`: Decrease A3 Offset threshold for 3228129_4
- `C22`: Add neighbor relationship between 3243323_3 and 3268707_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.707 | MS1 | 121.4656709271 | 31.1446263577 | 47 | 504990 | -83.58 | 14.56 | 505.54 | 0.18 | 2.25 | 1586 |
| 2024-09-20 22:21:32.210 | MS1 | 121.4656752056 | 31.1446247665 | 47 | 504990 | -79.94 | 13.31 | 542.83 | 0.11 | 2.25 | 1562 |
| 2024-09-20 22:21:33.409 | MS1 | 121.4656600826 | 31.1446274235 | 47 | 504990 | -84.49 | 16.32 | 357.93 | 0.09 | 2.82 | 1563 |
| 2024-09-20 22:21:34.935 | MS1 | 121.4656735581 | 31.1446216489 | 47 | 504990 | -86.13 | -0.02 | 33.01 | 0.16 | 1.24 | 1577 |
| 2024-09-20 22:21:35.286 | MS1 | 121.4656616297 | 31.1446240743 | 47 | 504990 | -93.66 | -2.21 | 29.59 | 0.10 | 1.48 | 1596 |
| 2024-09-20 22:21:36.242 | MS1 | 121.4656593674 | 31.1446311502 | 47 | 504990 | -93.64 | -3.79 | 31.83 | 0.14 | 1.09 | 1579 |
| 2024-09-20 22:21:37.112 | MS1 | 121.4656681159 | 31.1446333014 | 47 | 504990 | -89.80 | -2.15 | 52.92 | 0.13 | 1.35 | 1574 |
| 2024-09-20 22:21:38.286 | MS1 | 121.4656624696 | 31.1446306122 | 47 | 504990 | -83.94 | 15.58 | 339.87 | 0.12 | 1.25 | 1600 |
| 2024-09-20 22:21:39.384 | MS1 | 121.4656769412 | 31.1446264478 | 47 | 504990 | -79.79 | 16.37 | 539.37 | 0.09 | 1.47 | 1584 |
| 2024-09-20 22:21:40.280 | MS1 | 121.4656661875 | 31.1446374559 | 47 | 504990 | -81.50 | 14.38 | 325.19 | 0.15 | 2.85 | 1572 |
| 2024-09-20 22:21:41.513 | MS1 | 121.4656624841 | 31.1446259723 | 47 | 504990 | -78.11 | 13.42 | 490.92 | 0.15 | 2.79 | 1593 |
| 2024-09-20 22:21:42.239 | MS1 | 121.4656633751 | 31.1446370548 | 47 | 504990 | -80.10 | 17.39 | 432.34 | 0.03 | 2.74 | 1574 |

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
| 3228129 | 4 | 121.4661993910 | 31.1484709252 | 269 | 7 | 12 | 29.2 | TDD | 47 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3243323 | 3 | 121.4739183832 | 31.1467308137 | 36 | 14 | 9 | 23.8 | TDD | 117 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3262055 | 1 | 121.4702492990 | 31.1526522153 | 67 | 2 | 6 | 28.8 | TDD | 106 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3268707 | 2 | 121.4739032760 | 31.1551127055 | 255 | 1 | 4 | 28.8 | TDD | 315 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.241 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.260 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.406 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.406 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.128 | NREventA3 | measId:2;ServCellPCI:157;Se... |
| 2024-09-20 22:21:36.128 | NREventA3 | measId:2;ServCellPCI:157;Se... |
| 2024-09-20 22:21:37.128 | NREventA3 | measId:2;ServCellPCI:157;Se... |
| 2024-09-20 22:21:39.628 | NRRRCReestablishAttempt | PCI:157 |
| 2024-09-20 22:21:39.648 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.663 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.789 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.789 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262055 | 1 | 19.8162 | 12.3568 | -114.3002 | 16.5650 | 179.9423 | 0.0038 | 0.0132 |
| 2024_09_20 22:00 | 3268707 | 2 | 18.1874 | 10.7643 | -114.0375 | 15.9621 | 134.8297 | 0.0093 | 0.0063 |
| 2024_09_20 22:00 | 3243323 | 3 | 6.3486 | 6.0186 | -116.0398 | 12.9021 | 171.4536 | 0.0014 | 0.0071 |
| 2024_09_20 22:00 | 3228129 | 4 | 5.7187 | 8.1656 | -116.4923 | 11.3701 | 82.3600 | 0.0073 | 0.1795 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417146_36577A94 | 504990 | 47 | -87.6 | 504990 | 315 | -80.3 | 504990 | 117 | -90.5 | 504990 | 106 |
| MR_1774417146_6750D49F | 504990 | 47 | -84.5 | 504990 | 315 | -81.6 | 504990 | 117 | -89.3 | 504990 | 106 |
| MR_1774417146_7D659BCC | 504990 | 47 | -86.0 | 504990 | 315 | -80.9 | 504990 | 117 | -88.3 | 504990 | 106 |
| MR_1774417146_5B838F62 | 504990 | 315 | -81.6 | 504990 | 47 | -84.9 | 504990 | 117 | -89.2 | 504990 | 106 |
| MR_1774417146_3EFD1DFE | 504990 | 47 | -84.7 | 504990 | 315 | -80.7 | 504990 | 117 | -87.9 | 504990 | 106 |
| MR_1774417146_4D1383EF | 504990 | 315 | -80.4 | 504990 | 47 | -85.9 | 504990 | 117 | -87.8 | 504990 | 106 |
| MR_1774417146_5F8A399C | 504990 | 315 | -80.5 | 504990 | 47 | -88.1 | 504990 | 117 | -87.3 | 504990 | 106 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1495: `ff185a7f-ea3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ff185a7f-ea33-41be-8143-a3bb1aa3e4ea` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1495] topology](images/train_1495.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3213463_2 by 2 degrees
- `C2`: Adjust the azimuth of 3265497_4 by 50 degrees
- `C3`: Lift the tilt angle of 3265497_4 by 10 degrees
- `C4`: Increase A3 Offset threshold for 3265497_4
- `C5`: Lift the tilt angle  of 3213463_2 by 2 degrees
- `C6`: Increase transmission power for 3265497_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213463_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265497_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265497_4
- `C10`: Decrease A3 Offset threshold for 3265497_4
- `C11`: Insufficient data; more data is needed for judgment. **← 정답**
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213463_2
- `C13`: Decrease transmission power for 3265497_4
- `C14`: Decrease transmission power for 3213463_2
- `C15`: Add neighbor relationship between 3232766_3 and 3213463_2
- `C16`: Increase A3 Offset threshold for 3213463_2
- `C17`: Adjust the azimuth of 3213463_2 by 50 degrees
- `C18`: Increase transmission power for 3213463_2
- `C19`: Press down the tilt angle of 3265497_4 by 10 degrees
- `C20`: Add neighbor relationship between 3265497_4 and 3213463_2
- `C21`: Check test server and transmission issues
- `C22`: Decrease A3 Offset threshold for 3213463_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.900 | MS1 | 121.4656593954 | 31.1446271232 | 219 | 504990 | -91.64 | 15.25 | 591.20 | 0.12 | 2.59 | 1573 |
| 2024-09-20 22:21:32.959 | MS1 | 121.4656707152 | 31.1446231261 | 219 | 504990 | -91.30 | 16.10 | 355.53 | 0.03 | 2.24 | 1580 |
| 2024-09-20 22:21:33.684 | MS1 | 121.4656684210 | 31.1446205109 | 219 | 504990 | -91.34 | 13.73 | 482.36 | 0.09 | 2.79 | 1571 |
| 2024-09-20 22:21:34.844 | MS1 | 121.4656686859 | 31.1446263144 | 219 | 504990 | -90.24 | 13.64 | 76.21 | 0.00 | 2.48 | 1577 |
| 2024-09-20 22:21:35.861 | MS1 | 121.4656625402 | 31.1446302194 | 219 | 504990 | -88.58 | 17.88 | 78.97 | 0.14 | 2.70 | 1584 |
| 2024-09-20 22:21:36.467 | MS1 | 121.4656679596 | 31.1446315816 | 219 | 504990 | -85.49 | 17.89 | 74.74 | 0.15 | 2.32 | 1564 |
| 2024-09-20 22:21:37.277 | MS1 | 121.4656735380 | 31.1446342506 | 219 | 504990 | -89.46 | 9.47 | 44.78 | 0.06 | 2.43 | 1577 |
| 2024-09-20 22:21:38.700 | MS1 | 121.4656744577 | 31.1446330818 | 219 | 504990 | -92.68 | 11.51 | 76.62 | 0.18 | 2.51 | 1565 |
| 2024-09-20 22:21:39.991 | MS1 | 121.4656674999 | 31.1446358852 | 219 | 504990 | -90.51 | 10.22 | 61.07 | 0.14 | 2.91 | 1594 |
| 2024-09-20 22:21:40.307 | MS1 | 121.4656775452 | 31.1446232767 | 219 | 504990 | -90.58 | 11.42 | 314.85 | 0.17 | 2.64 | 1599 |
| 2024-09-20 22:21:41.426 | MS1 | 121.4656749550 | 31.1446336924 | 219 | 504990 | -91.43 | 12.28 | 400.60 | 0.10 | 2.75 | 1595 |
| 2024-09-20 22:21:42.292 | MS1 | 121.4656590545 | 31.1446347808 | 219 | 504990 | -93.34 | 7.78 | 537.16 | 0.15 | 2.69 | 1580 |

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
| 3213463 | 2 | 121.4744884502 | 31.1532342588 | 119 | 1 | 2 | 18.2 | TDD | 682 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3222943 | 1 | 121.4679992449 | 31.1495070846 | 221 | 10 | 11 | 16.9 | TDD | 374 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3232766 | 3 | 121.4718300638 | 31.1494689157 | 213 | 7 | 1 | 49.5 | TDD | 283 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3265497 | 4 | 121.4647675827 | 31.1535054663 | 290 | 14 | 11 | 22.2 | TDD | 219 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.645 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.667 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.781 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.781 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.494 | NREventA3 | measId:2;ServCellPCI:852;Se... |
| 2024-09-20 22:21:38.734 | NRHandoverAttempt | SourcePCI:852;SourceNR-ARFC... |
| 2024-09-20 22:21:38.780 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.790 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.900 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.900 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3222943 | 1 | 94.5074 | 81.4030 | -117.3194 | 19.5479 | 154.8214 | 0.0050 | 0.0137 |
| 2024_09_19 22:00 | 3213463 | 2 | 89.6688 | 76.8223 | -117.9346 | 11.0289 | 149.9838 | 0.0048 | 0.0106 |
| 2024_09_19 22:00 | 3232766 | 3 | 90.8613 | 83.2451 | -117.4590 | 10.0655 | 144.5569 | 0.0101 | 0.0171 |
| 2024_09_19 22:00 | 3265497 | 4 | 78.1039 | 85.7155 | -114.1568 | 19.1253 | 136.1713 | 0.0165 | 0.0112 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416984_5BC1A0C1 | 504990 | 219 | -91.4 | 504990 | 682 | -96.5 | 504990 | 283 | -100.7 | 504990 | 374 |
| MR_1774416984_5F14129C | 504990 | 219 | -89.1 | 504990 | 682 | -95.5 | 504990 | 283 | -99.8 | 504990 | 374 |
| MR_1774416984_869B51C0 | 504990 | 219 | -92.2 | 504990 | 682 | -95.4 | 504990 | 283 | -100.3 | 504990 | 374 |
| MR_1774416984_CED348B1 | 504990 | 219 | -89.4 | 504990 | 682 | -94.6 | 504990 | 283 | -102.5 | 504990 | 374 |
| MR_1774416984_40DE5FD0 | 504990 | 219 | -88.8 | 504990 | 682 | -94.1 | 504990 | 283 | -99.9 | 504990 | 374 |
| MR_1774416984_0E61A791 | 504990 | 219 | -91.1 | 504990 | 682 | -97.8 | 504990 | 283 | -102.3 | 504990 | 374 |
| MR_1774416984_73E5AA2D | 504990 | 219 | -89.8 | 504990 | 682 | -95.5 | 504990 | 283 | -100.4 | 504990 | 374 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1496: `e8b5bde9-116...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e8b5bde9-116a-4b73-acb2-374b79e42c09` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275955_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1496] topology](images/train_1496.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3271483_1
- `C2`: Decrease transmission power for 3275955_2
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Lift the tilt angle of 3275955_2 by 5 degrees
- `C5`: Adjust the azimuth of 3271483_1 by 31 degrees
- `C6`: Adjust the azimuth of 3275955_2 by 22 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275955_2
- `C8`: Press down the tilt angle  of 3271483_1 by 4 degrees
- `C9`: Add neighbor relationship between 3275955_2 and 3271483_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271483_1
- `C11`: Increase transmission power for 3271483_1
- `C12`: Add neighbor relationship between 3254641_10 and 3271483_1
- `C13`: Increase A3 Offset threshold for 3275955_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271483_1
- `C15`: Press down the tilt angle of 3275955_2 by 5 degrees
- `C16`: Decrease A3 Offset threshold for 3275955_2
- `C17`: Increase transmission power for 3275955_2
- `C18`: Check test server and transmission issues
- `C19`: Lift the tilt angle  of 3271483_1 by 4 degrees
- `C20`: Decrease transmission power for 3271483_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275955_2 **← 정답**
- `C22`: Increase A3 Offset threshold for 3271483_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.840 | MS1 | 121.4656595216 | 31.1446207119 | 107 | 504990 | -95.80 | 10.27 | 338.64 | 0.19 | 2.37 | 1578 |
| 2024-09-20 22:21:32.966 | MS1 | 121.4656667671 | 31.1446191553 | 502 | 504990 | -93.54 | 12.05 | 422.89 | 0.10 | 2.24 | 1578 |
| 2024-09-20 22:21:33.830 | MS1 | 121.4656762524 | 31.1446207299 | 638 | 504990 | -93.38 | 10.72 | 338.19 | 0.02 | 2.20 | 1589 |
| 2024-09-20 22:21:34.670 | MS1 | 121.4656627198 | 31.1446272761 | 524 | 152650 | -88.46 | 5.76 | 75.00 | 0.06 | 1.73 | 915 |
| 2024-09-20 22:21:35.573 | MS1 | 121.4656714318 | 31.1446229307 | 355 | 152650 | -88.78 | 6.12 | 72.85 | 0.12 | 1.65 | 934 |
| 2024-09-20 22:21:36.979 | MS1 | 121.4656771739 | 31.1446203202 | 521 | 152650 | -88.20 | 2.86 | 67.86 | 0.03 | 1.78 | 961 |
| 2024-09-20 22:21:37.341 | MS1 | 121.4656746446 | 31.1446307667 | 896 | 152650 | -88.63 | 6.16 | 61.85 | 0.02 | 1.65 | 918 |
| 2024-09-20 22:21:38.827 | MS1 | 121.4656623636 | 31.1446323479 | 524 | 152650 | -96.40 | 3.88 | 96.51 | 0.10 | 1.54 | 928 |
| 2024-09-20 22:21:39.854 | MS1 | 121.4656736799 | 31.1446247329 | 355 | 152650 | -87.08 | 4.64 | 72.58 | 0.07 | 2.00 | 906 |
| 2024-09-20 22:21:40.294 | MS1 | 121.4656677876 | 31.1446357972 | 521 | 152650 | -88.79 | 3.68 | 78.94 | 0.03 | 2.86 | 1580 |
| 2024-09-20 22:21:41.291 | MS1 | 121.4656673488 | 31.1446180455 | 896 | 152650 | -87.60 | 6.74 | 79.59 | 0.18 | 2.51 | 1599 |
| 2024-09-20 22:21:42.888 | MS1 | 121.4656753346 | 31.1446329494 | 524 | 152650 | -94.13 | 7.22 | 99.46 | 0.15 | 2.29 | 1577 |

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
| 3211724 | 7 | 121.4649767495 | 31.1483834665 | 133 | 3 | 8 | 27.3 | FDD | 896 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3220612 | 8 | 121.4733824049 | 31.1505910725 | 232 | 4 | 3 | 15.4 | FDD | 355 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3227522 | 5 | 121.4682832355 | 31.1559233702 | 183 | 6 | 4 | 5.8 | TDD | 957 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3236029 | 13 | 121.4654795561 | 31.1458973012 | 19 | 9 | 2 | 7.2 | FDD | 524 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3239664 | 4 | 121.4641272063 | 31.1501812108 | 273 | 0 | 9 | 13.0 | TDD | 988 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3245356 | 9 | 121.4715070728 | 31.1440729329 | 341 | 9 | 0 | 10.9 | FDD | 644 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3247266 | 6 | 121.4756791227 | 31.1485884300 | 229 | 8 | 0 | 29.2 | TDD | 638 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3254641 | 10 | 121.4687732735 | 31.1474594035 | 27 | 9 | 11 | 29.6 | FDD | 521 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3271483 | 1 | 121.4743882624 | 31.1453287691 | 234 | 4 | 2 | 3.2 | TDD | 870 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3275896 | 11 | 121.4683198200 | 31.1489492234 | 108 | 2 | 12 | 27.4 | FDD | 713 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3275955 | 2 | 121.4753596149 | 31.1507626245 | 256 | 5 | 3 | 5.6 | TDD | 107 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3279254 | 3 | 121.4648483812 | 31.1524104569 | 131 | 4 | 8 | 29.1 | TDD | 502 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3279425 | 12 | 121.4658803288 | 31.1532205319 | 135 | 7 | 4 | 9.1 | FDD | 203 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |

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
| 2024-09-20 22:21:30.820 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.839 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.949 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.949 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.620 | NREventA2 | measId:1;ServCellPCI:397;Se... |
| 2024-09-20 22:21:34.757 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.032 | NREventA5 | measId:3;ServCellPCI:397;Se... |
| 2024-09-20 22:21:35.109 | NRHandoverAttempt | SourcePCI:397;SourceNR-ARFC... |
| 2024-09-20 22:21:35.139 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.149 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.268 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.268 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271483 | 1 | 9.8988 | 11.1874 | -116.6118 | 7.3431 | 155.9500 | 0.0146 | 0.0124 |
| 2024_09_20 22:00 | 3275955 | 2 | 11.8975 | 12.9400 | -114.4114 | 18.9458 | 153.4395 | 0.0064 | 0.0164 |
| 2024_09_20 22:00 | 3279254 | 3 | 9.4127 | 19.5616 | -117.0214 | 11.6232 | 132.2301 | 0.0111 | 0.0110 |
| 2024_09_20 22:00 | 3239664 | 4 | 16.1463 | 6.4193 | -114.0053 | 11.9769 | 107.3077 | 0.0159 | 0.0142 |
| 2024_09_20 22:00 | 3227522 | 5 | 17.7729 | 10.2313 | -115.1646 | 18.3075 | 102.7715 | 0.0034 | 0.0037 |
| 2024_09_20 22:00 | 3247266 | 6 | 17.9942 | 14.4252 | -117.2373 | 16.6371 | 108.2419 | 0.0038 | 0.0006 |
| 2024_09_20 22:00 | 3211724 | 7 | 10.6614 | 14.1541 | -114.1146 | 3.9525 | 30.0342 | 0.0186 | 0.0178 |
| 2024_09_20 22:00 | 3220612 | 8 | 13.8750 | 19.4013 | -114.7130 | 4.1814 | 23.3211 | 0.0097 | 0.0066 |
| 2024_09_20 22:00 | 3245356 | 9 | 14.0867 | 19.6521 | -117.8571 | 3.2609 | 34.9977 | 0.0148 | 0.0066 |
| 2024_09_20 22:00 | 3254641 | 10 | 19.2752 | 10.9060 | -114.3397 | 3.0446 | 30.6080 | 0.0010 | 0.0200 |
| 2024_09_20 22:00 | 3275896 | 11 | 7.7948 | 18.4331 | -117.0373 | 4.9515 | 49.4626 | 0.0043 | 0.0092 |
| 2024_09_20 22:00 | 3279425 | 12 | 17.3637 | 18.8401 | -114.9117 | 3.4623 | 27.1300 | 0.0171 | 0.0145 |
| 2024_09_20 22:00 | 3236029 | 13 | 19.1499 | 13.7439 | -117.8935 | 4.6180 | 20.9421 | 0.0117 | 0.0146 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413748_110717AB | 152650 | 524 | -87.3 | 152650 | 644 | -93.4 | 152650 | 713 | -99.1 | 152650 | 203 |
| MR_1774413748_3BF72CD1 | 504990 | 638 | -95.2 | 504990 | 870 | -94.5 | 504990 | 988 | -98.0 | 504990 | 957 |
| MR_1774413748_8F686733 | 504990 | 638 | -91.4 | 504990 | 870 | -93.6 | 504990 | 988 | -97.7 | 504990 | 957 |
| MR_1774413748_072DA6FE | 152650 | 524 | -86.8 | 152650 | 644 | -94.6 | 152650 | 713 | -98.0 | 152650 | 203 |
| MR_1774413748_F36572AE | 504990 | 638 | -92.8 | 504990 | 870 | -93.5 | 504990 | 988 | -98.3 | 504990 | 957 |
| MR_1774413748_A46FF9D4 | 152650 | 524 | -86.7 | 152650 | 644 | -95.4 | 152650 | 713 | -98.3 | 152650 | 203 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1497: `2ffbfb42-5ca...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2ffbfb42-5ca8-43d6-891a-9fe0b696b1b2` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1497] topology](images/train_1497.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3212229_1
- `C2`: Decrease A3 Offset threshold for 3216478_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212229_1
- `C4`: Increase transmission power for 3212229_1
- `C5`: Add neighbor relationship between 3216478_3 and 3212229_1
- `C6`: Add neighbor relationship between 3242016_2 and 3212229_1
- `C7`: Increase A3 Offset threshold for 3212229_1
- `C8`: Decrease A3 Offset threshold for 3212229_1
- `C9`: Adjust the azimuth of 3212229_1 by 2 degrees
- `C10`: Check test server and transmission issues
- `C11`: Lift the tilt angle  of 3212229_1 by 10 degrees
- `C12`: Decrease transmission power for 3216478_3
- `C13`: Insufficient data; more data is needed for judgment. **← 정답**
- `C14`: Adjust the azimuth of 3216478_3 by 22 degrees
- `C15`: Press down the tilt angle  of 3212229_1 by 10 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216478_3
- `C17`: Press down the tilt angle of 3216478_3 by 10 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212229_1
- `C19`: Increase A3 Offset threshold for 3216478_3
- `C20`: Lift the tilt angle of 3216478_3 by 10 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216478_3
- `C22`: Increase transmission power for 3216478_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.903 | MS1 | 121.4656680693 | 31.1446280073 | 494 | 504990 | -87.27 | 15.84 | 370.27 | 0.01 | 2.05 | 1579 |
| 2024-09-20 22:21:32.937 | MS1 | 121.4656673407 | 31.1446204992 | 494 | 504990 | -88.04 | 14.25 | 397.30 | 0.01 | 2.70 | 1582 |
| 2024-09-20 22:21:33.300 | MS1 | 121.4656704306 | 31.1446195282 | 494 | 504990 | -87.20 | 15.72 | 548.88 | 0.16 | 2.62 | 1561 |
| 2024-09-20 22:21:34.391 | MS1 | 121.4656696078 | 31.1446352301 | 494 | 504990 | -90.22 | 13.79 | 63.08 | 0.13 | 2.49 | 1579 |
| 2024-09-20 22:21:35.340 | MS1 | 121.4656660151 | 31.1446305415 | 494 | 504990 | -87.22 | 17.89 | 66.63 | 0.14 | 2.87 | 1597 |
| 2024-09-20 22:21:36.743 | MS1 | 121.4656756202 | 31.1446329582 | 494 | 504990 | -85.58 | 12.67 | 79.97 | 0.02 | 2.73 | 1596 |
| 2024-09-20 22:21:37.178 | MS1 | 121.4656672946 | 31.1446310180 | 494 | 504990 | -93.28 | 9.34 | 79.78 | 0.13 | 2.75 | 1593 |
| 2024-09-20 22:21:38.976 | MS1 | 121.4656671524 | 31.1446350444 | 494 | 504990 | -93.54 | 9.47 | 66.92 | 0.18 | 2.93 | 1561 |
| 2024-09-20 22:21:39.990 | MS1 | 121.4656763011 | 31.1446271503 | 494 | 504990 | -90.29 | 9.16 | 71.54 | 0.02 | 2.13 | 1563 |
| 2024-09-20 22:21:40.735 | MS1 | 121.4656660125 | 31.1446314852 | 494 | 504990 | -89.41 | 10.73 | 523.07 | 0.12 | 2.34 | 1570 |
| 2024-09-20 22:21:41.328 | MS1 | 121.4656612961 | 31.1446344005 | 494 | 504990 | -91.20 | 7.19 | 476.13 | 0.05 | 2.27 | 1588 |
| 2024-09-20 22:21:42.172 | MS1 | 121.4656586626 | 31.1446260948 | 494 | 504990 | -91.49 | 11.09 | 336.90 | 0.16 | 2.47 | 1575 |

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
| 3212229 | 1 | 121.4732340071 | 31.1462437401 | 258 | 15 | 6 | 48.5 | TDD | 586 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3216478 | 3 | 121.4685878810 | 31.1536892773 | 173 | 15 | 6 | 49.6 | TDD | 494 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3242016 | 2 | 121.4691058597 | 31.1473807537 | 179 | 1 | 0 | 23.7 | TDD | 197 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3277393 | 4 | 121.4674684104 | 31.1552328958 | 9 | 12 | 4 | 34.4 | TDD | 431 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.552 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.576 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.712 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.712 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.368 | NREventA3 | measId:2;ServCellPCI:1;Serv... |
| 2024-09-20 22:21:38.608 | NRHandoverAttempt | SourcePCI:1;SourceNR-ARFCN:... |
| 2024-09-20 22:21:38.642 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.653 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.782 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.782 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3212229 | 1 | 75.2092 | 85.4506 | -114.5497 | 5.3908 | 175.3034 | 0.0010 | 0.0101 |
| 2024_09_19 22:00 | 3242016 | 2 | 82.2772 | 84.4854 | -114.1451 | 6.7984 | 176.7482 | 0.0031 | 0.0068 |
| 2024_09_19 22:00 | 3216478 | 3 | 89.6699 | 81.5233 | -116.7718 | 11.0399 | 115.2113 | 0.0173 | 0.0080 |
| 2024_09_19 22:00 | 3277393 | 4 | 93.5615 | 83.1015 | -115.5690 | 19.9284 | 194.5897 | 0.0003 | 0.0124 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417039_0EB0F3D2 | 504990 | 494 | -91.6 | 504990 | 586 | -96.4 | 504990 | 197 | -97.8 | 504990 | 431 |
| MR_1774417039_90D7CD2F | 504990 | 494 | -89.6 | 504990 | 586 | -95.1 | 504990 | 197 | -99.9 | 504990 | 431 |
| MR_1774417039_0E38C563 | 504990 | 494 | -90.6 | 504990 | 586 | -95.0 | 504990 | 197 | -98.2 | 504990 | 431 |
| MR_1774417039_E5403276 | 504990 | 494 | -88.4 | 504990 | 586 | -95.3 | 504990 | 197 | -99.0 | 504990 | 431 |
| MR_1774417039_8685F609 | 504990 | 494 | -91.9 | 504990 | 586 | -96.5 | 504990 | 197 | -100.4 | 504990 | 431 |
| MR_1774417039_8D694DDC | 504990 | 494 | -92.0 | 504990 | 586 | -98.1 | 504990 | 197 | -99.5 | 504990 | 431 |
| MR_1774417039_3544D1AE | 504990 | 494 | -88.6 | 504990 | 586 | -97.5 | 504990 | 197 | -98.9 | 504990 | 431 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1498: `d7b6dc94-61b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d7b6dc94-61b8-4d02-9133-48f4aa8e03c4` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Add neighbor relationship between 3254189_1 and 3237083_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1498] topology](images/train_1498.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237083_4
- `C2`: Increase A3 Offset threshold for 3237083_4
- `C3`: Increase transmission power for 3254189_1
- `C4`: Adjust the azimuth of 3237083_4 by 43 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237083_4
- `C6`: Lift the tilt angle of 3254189_1 by 4 degrees
- `C7`: Lift the tilt angle  of 3237083_4 by 3 degrees
- `C8`: Decrease transmission power for 3254189_1
- `C9`: Press down the tilt angle of 3254189_1 by 4 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254189_1
- `C11`: Increase transmission power for 3237083_4
- `C12`: Check test server and transmission issues
- `C13`: Increase A3 Offset threshold for 3254189_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Press down the tilt angle  of 3237083_4 by 3 degrees
- `C16`: Decrease A3 Offset threshold for 3254189_1
- `C17`: Decrease A3 Offset threshold for 3237083_4
- `C18`: Add neighbor relationship between 3239891_3 and 3237083_4
- `C19`: Add neighbor relationship between 3254189_1 and 3237083_4 **← 정답**
- `C20`: Decrease transmission power for 3237083_4
- `C21`: Adjust the azimuth of 3254189_1 by 50 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254189_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.267 | MS1 | 121.4656672769 | 31.1446310549 | 296 | 504990 | -84.56 | 16.60 | 582.93 | 0.09 | 2.73 | 1568 |
| 2024-09-20 22:21:32.975 | MS1 | 121.4656739156 | 31.1446215061 | 296 | 504990 | -78.17 | 13.33 | 394.95 | 0.09 | 2.76 | 1575 |
| 2024-09-20 22:21:33.997 | MS1 | 121.4656652220 | 31.1446356307 | 296 | 504990 | -82.43 | 15.12 | 444.82 | 0.11 | 2.55 | 1568 |
| 2024-09-20 22:21:34.389 | MS1 | 121.4656592918 | 31.1446231430 | 296 | 504990 | -92.11 | -2.48 | 65.14 | 0.03 | 1.50 | 1579 |
| 2024-09-20 22:21:35.243 | MS1 | 121.4656725348 | 31.1446325164 | 296 | 504990 | -85.20 | -2.05 | 53.54 | 0.07 | 1.49 | 1588 |
| 2024-09-20 22:21:36.737 | MS1 | 121.4656658132 | 31.1446320753 | 296 | 504990 | -85.67 | -0.77 | 60.56 | 0.03 | 1.16 | 1569 |
| 2024-09-20 22:21:37.721 | MS1 | 121.4656646541 | 31.1446240181 | 296 | 504990 | -94.44 | -3.94 | 48.24 | 0.05 | 1.40 | 1570 |
| 2024-09-20 22:21:38.264 | MS1 | 121.4656680928 | 31.1446224734 | 296 | 504990 | -79.20 | 15.07 | 577.99 | 0.16 | 1.01 | 1575 |
| 2024-09-20 22:21:39.858 | MS1 | 121.4656609542 | 31.1446273559 | 296 | 504990 | -81.08 | 13.73 | 375.95 | 0.08 | 1.13 | 1561 |
| 2024-09-20 22:21:40.596 | MS1 | 121.4656603276 | 31.1446330650 | 296 | 504990 | -81.61 | 17.74 | 582.23 | 0.09 | 2.16 | 1576 |
| 2024-09-20 22:21:41.529 | MS1 | 121.4656779888 | 31.1446289333 | 296 | 504990 | -76.67 | 16.45 | 591.64 | 0.14 | 2.95 | 1576 |
| 2024-09-20 22:21:42.993 | MS1 | 121.4656721771 | 31.1446222747 | 296 | 504990 | -84.53 | 15.83 | 538.37 | 0.08 | 2.67 | 1582 |

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
| 3228655 | 2 | 121.4687568856 | 31.1539062535 | 55 | 6 | 9 | 27.4 | TDD | 217 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3237083 | 4 | 121.4733086510 | 31.1506226367 | 270 | 1 | 4 | 34.0 | TDD | 702 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3239891 | 3 | 121.4680826251 | 31.1455427772 | 119 | 10 | 2 | 36.3 | TDD | 624 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3254189 | 1 | 121.4742079234 | 31.1482523016 | 5 | 2 | 3 | 27.5 | TDD | 296 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.994 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.013 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.147 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.147 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.834 | NREventA3 | measId:2;ServCellPCI:770;Se... |
| 2024-09-20 22:21:35.834 | NREventA3 | measId:2;ServCellPCI:770;Se... |
| 2024-09-20 22:21:36.834 | NREventA3 | measId:2;ServCellPCI:770;Se... |
| 2024-09-20 22:21:39.334 | NRRRCReestablishAttempt | PCI:770 |
| 2024-09-20 22:21:39.347 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.359 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.505 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.505 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254189 | 1 | 13.3613 | 8.8152 | -114.4503 | 5.7910 | 107.2058 | 0.0169 | 0.1297 |
| 2024_09_20 22:00 | 3228655 | 2 | 12.7550 | 13.3788 | -116.0142 | 19.7502 | 112.6227 | 0.0199 | 0.0156 |
| 2024_09_20 22:00 | 3239891 | 3 | 8.6495 | 14.9083 | -117.8708 | 12.4945 | 144.9798 | 0.0175 | 0.0014 |
| 2024_09_20 22:00 | 3237083 | 4 | 17.6095 | 18.0146 | -117.4024 | 10.1065 | 112.1365 | 0.0007 | 0.0054 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414903_158EC055 | 504990 | 296 | -93.4 | 504990 | 702 | -86.9 | 504990 | 624 | -93.0 | 504990 | 217 |
| MR_1774414903_96D8F664 | 504990 | 296 | -94.0 | 504990 | 702 | -86.6 | 504990 | 624 | -91.7 | 504990 | 217 |
| MR_1774414903_F3F69599 | 504990 | 702 | -87.9 | 504990 | 296 | -92.6 | 504990 | 624 | -90.9 | 504990 | 217 |
| MR_1774414903_D86D96D1 | 504990 | 296 | -91.1 | 504990 | 702 | -87.6 | 504990 | 624 | -89.3 | 504990 | 217 |
| MR_1774414903_C9709B5E | 504990 | 296 | -93.7 | 504990 | 702 | -88.4 | 504990 | 624 | -91.9 | 504990 | 217 |
| MR_1774414903_520D3DE8 | 504990 | 702 | -84.8 | 504990 | 296 | -91.6 | 504990 | 624 | -89.3 | 504990 | 217 |
| MR_1774414903_94C4B5EB | 504990 | 296 | -92.5 | 504990 | 702 | -87.6 | 504990 | 624 | -91.6 | 504990 | 217 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1499: `ea1d036c-15e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ea1d036c-15ee-4fb4-a4f7-1a6616344356` |
| Tag | **multiple-answer** |
| 정답 | **C1|C9|C16|C18** |
| C1 의미 | Decrease transmission power for 3278033_4 |
| C9 의미 | Increase A3 Offset threshold for 3278033_4 |
| C16 의미 | Increase A3 Offset threshold for 3268172_3 |
| C18 의미 | Press down the tilt angle  of 3278033_4 by 3 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1499] topology](images/train_1499.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3278033_4 **← 정답**
- `C2`: Decrease A3 Offset threshold for 3278033_4
- `C3`: Press down the tilt angle of 3268172_3 by 3 degrees
- `C4`: Lift the tilt angle of 3268172_3 by 3 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278033_4
- `C6`: Decrease transmission power for 3268172_3
- `C7`: Add neighbor relationship between 3259522_2 and 3278033_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268172_3
- `C9`: Increase A3 Offset threshold for 3278033_4 **← 정답**
- `C10`: Adjust the azimuth of 3268172_3 by 24 degrees
- `C11`: Increase transmission power for 3268172_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268172_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278033_4
- `C14`: Decrease A3 Offset threshold for 3268172_3
- `C15`: Adjust the azimuth of 3278033_4 by 27 degrees
- `C16`: Increase A3 Offset threshold for 3268172_3 **← 정답**
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Press down the tilt angle  of 3278033_4 by 3 degrees **← 정답**
- `C19`: Check test server and transmission issues
- `C20`: Increase transmission power for 3278033_4
- `C21`: Lift the tilt angle  of 3278033_4 by 3 degrees
- `C22`: Add neighbor relationship between 3268172_3 and 3278033_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.316 | MS1 | 121.4656750084 | 31.1446248843 | 17 | 504990 | -76.13 | 12.12 | 504.37 | 0.11 | 2.13 | 1585 |
| 2024-09-20 22:21:32.217 | MS1 | 121.4656733177 | 31.1446348816 | 17 | 504990 | -84.99 | 16.18 | 560.99 | 0.15 | 2.60 | 1586 |
| 2024-09-20 22:21:33.643 | MS1 | 121.4656599749 | 31.1446285264 | 17 | 504990 | -77.44 | 16.60 | 413.00 | 0.18 | 2.15 | 1575 |
| 2024-09-20 22:21:34.913 | MS1 | 121.4656581301 | 31.1446230159 | 422 | 504990 | -80.80 | 2.77 | 35.07 | 0.10 | 1.06 | 1589 |
| 2024-09-20 22:21:35.726 | MS1 | 121.4656610871 | 31.1446211496 | 422 | 504990 | -84.58 | 2.10 | 83.30 | 0.15 | 1.29 | 1574 |
| 2024-09-20 22:21:36.401 | MS1 | 121.4656741080 | 31.1446221559 | 17 | 504990 | -89.03 | 3.69 | 61.70 | 0.16 | 1.02 | 1590 |
| 2024-09-20 22:21:37.910 | MS1 | 121.4656746872 | 31.1446212194 | 17 | 504990 | -88.52 | 4.12 | 61.14 | 0.07 | 1.24 | 1582 |
| 2024-09-20 22:21:38.920 | MS1 | 121.4656669312 | 31.1446369448 | 422 | 504990 | -83.61 | 3.53 | 45.49 | 0.18 | 1.30 | 1589 |
| 2024-09-20 22:21:39.922 | MS1 | 121.4656669004 | 31.1446188452 | 422 | 504990 | -81.49 | 2.24 | 58.54 | 0.15 | 1.23 | 1560 |
| 2024-09-20 22:21:40.686 | MS1 | 121.4656738937 | 31.1446299728 | 422 | 504990 | -81.96 | 13.77 | 363.27 | 0.18 | 2.64 | 1600 |
| 2024-09-20 22:21:41.868 | MS1 | 121.4656708060 | 31.1446217435 | 422 | 504990 | -79.02 | 17.19 | 492.94 | 0.11 | 2.18 | 1597 |
| 2024-09-20 22:21:42.568 | MS1 | 121.4656627239 | 31.1446326226 | 422 | 504990 | -81.32 | 16.88 | 427.73 | 0.13 | 2.23 | 1583 |

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
| 3216341 | 1 | 121.4667167902 | 31.1452198125 | 213 | 5 | 6 | 20.5 | TDD | 422 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3259522 | 2 | 121.4728949476 | 31.1454284345 | 16 | 13 | 2 | 43.0 | TDD | 299 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3262893 | 5 | 121.4669212053 | 31.1492472999 | 338 | 13 | 6 | 35.8 | TDD | 124 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3268172 | 3 | 121.4734043166 | 31.1466051086 | 229 | 0 | 1 | 45.8 | TDD | 17 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3278033 | 4 | 121.4664006702 | 31.1543106169 | 157 | 1 | 0 | 33.6 | TDD | 692 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.943 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.961 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.072 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.072 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.781 | NREventA3 | measId:2;ServCellPCI:288;Se... |
| 2024-09-20 22:21:34.021 | NRHandoverAttempt | SourcePCI:288;SourceNR-ARFC... |
| 2024-09-20 22:21:34.067 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.082 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.200 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.200 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.781 | NREventA3 | measId:2;ServCellPCI:721;Se... |
| 2024-09-20 22:21:36.021 | NRHandoverAttempt | SourcePCI:721;SourceNR-ARFC... |
| 2024-09-20 22:21:36.063 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.077 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.211 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.211 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.781 | NREventA3 | measId:2;ServCellPCI:288;Se... |
| 2024-09-20 22:21:38.021 | NRHandoverAttempt | SourcePCI:288;SourceNR-ARFC... |
| 2024-09-20 22:21:38.062 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.076 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.206 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.206 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216341 | 1 | 15.7046 | 18.5235 | -114.5141 | 7.3097 | 187.7001 | 0.0066 | 0.0096 |
| 2024_09_20 22:00 | 3259522 | 2 | 19.6215 | 14.9446 | -115.7344 | 17.9249 | 137.4281 | 0.0031 | 0.0011 |
| 2024_09_20 22:00 | 3268172 | 3 | 13.2187 | 5.1004 | -115.0374 | 8.1827 | 174.1365 | 0.0055 | 0.0153 |
| 2024_09_20 22:00 | 3278033 | 4 | 15.7067 | 7.4053 | -117.3681 | 9.7850 | 154.5231 | 0.0104 | 0.0005 |
| 2024_09_20 22:00 | 3262893 | 5 | 18.5589 | 15.8359 | -115.9590 | 15.7006 | 136.8865 | 0.0101 | 0.0011 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416540_C5230A75 | 504990 | 17 | -78.8 | 504990 | 422 | -82.7 | 504990 | 692 | -82.5 | 504990 | 299 |
| MR_1774416540_C1DB0A83 | 504990 | 422 | -81.4 | 504990 | 17 | -80.5 | 504990 | 692 | -84.5 | 504990 | 299 |
| MR_1774416540_0312560C | 504990 | 17 | -82.2 | 504990 | 422 | -80.6 | 504990 | 692 | -83.7 | 504990 | 299 |
| MR_1774416540_D2C0721C | 504990 | 17 | -80.9 | 504990 | 422 | -83.8 | 504990 | 692 | -83.3 | 504990 | 299 |
| MR_1774416540_F8EB2A6E | 504990 | 422 | -80.8 | 504990 | 17 | -82.1 | 504990 | 692 | -82.2 | 504990 | 299 |

> *... 2개 열 생략 (전체 14열)*

---
