# Track A 문제 분석 — train[1070]~train[1079]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1070] ~ train[1079] (10개)

## 목차

1. [문제 1070: `4af19ebf-a7d...`](#1070) — single-answer, 정답: C2
2. [문제 1071: `e2e52ba0-11b...`](#1071) — single-answer, 정답: C7
3. [문제 1072: `a0f7e8bf-e28...`](#1072) — single-answer, 정답: C18
4. [문제 1073: `1af44849-e28...`](#1073) — single-answer, 정답: C13
5. [문제 1074: `cbf4272e-2ad...`](#1074) — single-answer, 정답: C1
6. [문제 1075: `ce339496-c3f...`](#1075) — single-answer, 정답: C18
7. [문제 1076: `9181b85b-ae4...`](#1076) — single-answer, 정답: C8
8. [문제 1077: `acbbd8c4-f4d...`](#1077) — single-answer, 정답: C5
9. [문제 1078: `5ee3cd99-283...`](#1078) — single-answer, 정답: C2
10. [문제 1079: `69a595d3-fad...`](#1079) — single-answer, 정답: C2

---

### 문제 1070: `4af19ebf-a7d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4af19ebf-a7d0-4a85-98eb-175c1767918a` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1070] topology](images/train_1070.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3223898_1
- `C2`: Insufficient data; more data is needed for judgment. **← 정답**
- `C3`: Add neighbor relationship between 3224430_3 and 3223898_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277069_2
- `C5`: Check test server and transmission issues
- `C6`: Lift the tilt angle  of 3223898_1 by 10 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223898_1
- `C8`: Increase transmission power for 3223898_1
- `C9`: Increase A3 Offset threshold for 3277069_2
- `C10`: Add neighbor relationship between 3277069_2 and 3223898_1
- `C11`: Adjust the azimuth of 3277069_2 by 50 degrees
- `C12`: Decrease A3 Offset threshold for 3277069_2
- `C13`: Decrease transmission power for 3277069_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277069_2
- `C15`: Lift the tilt angle of 3277069_2 by 7 degrees
- `C16`: Increase A3 Offset threshold for 3223898_1
- `C17`: Increase transmission power for 3277069_2
- `C18`: Decrease A3 Offset threshold for 3223898_1
- `C19`: Adjust the azimuth of 3223898_1 by 50 degrees
- `C20`: Press down the tilt angle  of 3223898_1 by 10 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223898_1
- `C22`: Press down the tilt angle of 3277069_2 by 7 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.852 | MS1 | 121.4656741317 | 31.1446233166 | 378 | 504990 | -86.94 | 14.31 | 558.48 | 0.18 | 2.23 | 1587 |
| 2024-09-20 22:21:32.408 | MS1 | 121.4656731200 | 31.1446257275 | 378 | 504990 | -91.12 | 14.45 | 505.57 | 0.04 | 2.77 | 1590 |
| 2024-09-20 22:21:33.494 | MS1 | 121.4656767396 | 31.1446182777 | 378 | 504990 | -90.48 | 13.95 | 579.28 | 0.17 | 2.63 | 1597 |
| 2024-09-20 22:21:34.101 | MS1 | 121.4656633384 | 31.1446360275 | 378 | 504990 | -88.38 | 16.98 | 81.32 | 0.11 | 2.92 | 1597 |
| 2024-09-20 22:21:35.244 | MS1 | 121.4656773831 | 31.1446379695 | 378 | 504990 | -88.18 | 13.10 | 82.82 | 0.10 | 2.78 | 1576 |
| 2024-09-20 22:21:36.105 | MS1 | 121.4656705054 | 31.1446312478 | 378 | 504990 | -87.09 | 12.62 | 93.16 | 0.01 | 2.85 | 1581 |
| 2024-09-20 22:21:37.390 | MS1 | 121.4656717773 | 31.1446288038 | 378 | 504990 | -90.80 | 8.46 | 44.85 | 0.05 | 2.75 | 1595 |
| 2024-09-20 22:21:38.631 | MS1 | 121.4656694614 | 31.1446218819 | 378 | 504990 | -90.42 | 8.69 | 92.39 | 0.07 | 2.07 | 1593 |
| 2024-09-20 22:21:39.482 | MS1 | 121.4656756277 | 31.1446210963 | 378 | 504990 | -91.68 | 8.51 | 65.61 | 0.15 | 3.00 | 1597 |
| 2024-09-20 22:21:40.584 | MS1 | 121.4656697769 | 31.1446212900 | 378 | 504990 | -92.94 | 8.94 | 405.74 | 0.07 | 2.85 | 1593 |
| 2024-09-20 22:21:41.656 | MS1 | 121.4656710618 | 31.1446190735 | 378 | 504990 | -89.16 | 9.32 | 474.34 | 0.11 | 2.67 | 1598 |
| 2024-09-20 22:21:42.791 | MS1 | 121.4656667750 | 31.1446331367 | 378 | 504990 | -93.76 | 11.67 | 411.93 | 0.05 | 2.03 | 1589 |

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
| 3219507 | 4 | 121.4696133746 | 31.1529367959 | 294 | 7 | 5 | 21.9 | TDD | 984 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3223898 | 1 | 121.4743385762 | 31.1523609281 | 152 | 13 | 1 | 25.1 | TDD | 80 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3224430 | 3 | 121.4753043907 | 31.1498567649 | 40 | 9 | 1 | 29.2 | TDD | 142 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3277069 | 2 | 121.4744175107 | 31.1505700857 | 142 | 5 | 7 | 30.4 | TDD | 378 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.331 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.346 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.463 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.463 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.172 | NREventA3 | measId:2;ServCellPCI:654;Se... |
| 2024-09-20 22:21:38.412 | NRHandoverAttempt | SourcePCI:654;SourceNR-ARFC... |
| 2024-09-20 22:21:38.442 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.455 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.564 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.564 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3223898 | 1 | 79.2974 | 79.2281 | -117.0255 | 14.1364 | 172.7301 | 0.0197 | 0.0048 |
| 2024_09_19 22:00 | 3277069 | 2 | 86.4372 | 80.9104 | -114.8059 | 13.7727 | 194.7615 | 0.0047 | 0.0115 |
| 2024_09_19 22:00 | 3224430 | 3 | 92.6667 | 81.0875 | -117.3651 | 15.1418 | 144.8241 | 0.0072 | 0.0159 |
| 2024_09_19 22:00 | 3219507 | 4 | 80.2214 | 88.4276 | -117.4091 | 10.6434 | 183.0469 | 0.0139 | 0.0064 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413932_4589A3E7 | 504990 | 378 | -88.9 | 504990 | 80 | -90.3 | 504990 | 142 | -94.3 | 504990 | 984 |
| MR_1774413932_20BFF623 | 504990 | 378 | -88.4 | 504990 | 80 | -92.2 | 504990 | 142 | -96.1 | 504990 | 984 |
| MR_1774413932_0DE42C4B | 504990 | 378 | -87.5 | 504990 | 80 | -91.1 | 504990 | 142 | -98.1 | 504990 | 984 |
| MR_1774413932_4F50A94B | 504990 | 378 | -87.8 | 504990 | 80 | -89.9 | 504990 | 142 | -95.5 | 504990 | 984 |
| MR_1774413932_D887670C | 504990 | 378 | -86.9 | 504990 | 80 | -92.7 | 504990 | 142 | -94.6 | 504990 | 984 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1071: `e2e52ba0-11b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e2e52ba0-11be-4101-a98e-ae6ea23e7a41` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Add neighbor relationship between 3268469_2 and 3214366_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1071] topology](images/train_1071.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214366_4
- `C2`: Increase A3 Offset threshold for 3268469_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214366_4
- `C4`: Decrease transmission power for 3214366_4
- `C5`: Press down the tilt angle of 3268469_2 by 10 degrees
- `C6`: Check test server and transmission issues
- `C7`: Add neighbor relationship between 3268469_2 and 3214366_4 **← 정답**
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268469_2
- `C9`: Adjust the azimuth of 3268469_2 by 15 degrees
- `C10`: Increase transmission power for 3214366_4
- `C11`: Lift the tilt angle  of 3214366_4 by 1 degrees
- `C12`: Adjust the azimuth of 3214366_4 by 36 degrees
- `C13`: Decrease A3 Offset threshold for 3268469_2
- `C14`: Add neighbor relationship between 3268252_3 and 3214366_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268469_2
- `C16`: Decrease A3 Offset threshold for 3214366_4
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Lift the tilt angle of 3268469_2 by 10 degrees
- `C19`: Increase transmission power for 3268469_2
- `C20`: Press down the tilt angle  of 3214366_4 by 1 degrees
- `C21`: Decrease transmission power for 3268469_2
- `C22`: Increase A3 Offset threshold for 3214366_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.803 | MS1 | 121.4656633164 | 31.1446373541 | 937 | 504990 | -78.22 | 17.78 | 592.13 | 0.09 | 2.80 | 1590 |
| 2024-09-20 22:21:32.985 | MS1 | 121.4656617107 | 31.1446274801 | 937 | 504990 | -75.43 | 15.67 | 549.66 | 0.16 | 2.65 | 1578 |
| 2024-09-20 22:21:33.249 | MS1 | 121.4656733406 | 31.1446225438 | 937 | 504990 | -80.40 | 15.23 | 318.17 | 0.07 | 2.58 | 1578 |
| 2024-09-20 22:21:34.279 | MS1 | 121.4656762802 | 31.1446200909 | 937 | 504990 | -93.57 | -3.47 | 65.39 | 0.07 | 1.41 | 1595 |
| 2024-09-20 22:21:35.940 | MS1 | 121.4656673637 | 31.1446352455 | 937 | 504990 | -92.13 | -2.28 | 24.15 | 0.03 | 1.23 | 1565 |
| 2024-09-20 22:21:36.927 | MS1 | 121.4656643926 | 31.1446240600 | 937 | 504990 | -89.62 | -2.20 | 61.31 | 0.05 | 1.17 | 1588 |
| 2024-09-20 22:21:37.168 | MS1 | 121.4656641326 | 31.1446362894 | 937 | 504990 | -85.25 | -0.07 | 28.67 | 0.18 | 1.48 | 1563 |
| 2024-09-20 22:21:38.193 | MS1 | 121.4656627615 | 31.1446285558 | 937 | 504990 | -79.33 | 17.78 | 308.33 | 0.07 | 1.06 | 1564 |
| 2024-09-20 22:21:39.640 | MS1 | 121.4656650595 | 31.1446244589 | 937 | 504990 | -82.65 | 17.31 | 462.05 | 0.08 | 1.38 | 1575 |
| 2024-09-20 22:21:40.521 | MS1 | 121.4656763748 | 31.1446181645 | 937 | 504990 | -79.26 | 16.76 | 310.48 | 0.11 | 2.06 | 1562 |
| 2024-09-20 22:21:41.521 | MS1 | 121.4656725516 | 31.1446227114 | 937 | 504990 | -84.78 | 15.82 | 312.75 | 0.16 | 2.96 | 1566 |
| 2024-09-20 22:21:42.726 | MS1 | 121.4656608640 | 31.1446356802 | 937 | 504990 | -81.01 | 14.89 | 364.63 | 0.12 | 2.69 | 1567 |

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
| 3214366 | 4 | 121.4699867558 | 31.1519016509 | 171 | 0 | 3 | 22.1 | TDD | 673 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3263651 | 1 | 121.4693506697 | 31.1487653985 | 273 | 5 | 11 | 33.4 | TDD | 568 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3268252 | 3 | 121.4692823618 | 31.1513792804 | 284 | 7 | 8 | 21.1 | TDD | 898 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3268469 | 2 | 121.4662960851 | 31.1472689044 | 177 | 4 | 9 | 33.6 | TDD | 937 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.940 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.959 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.093 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.093 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.778 | NREventA3 | measId:2;ServCellPCI:464;Se... |
| 2024-09-20 22:21:35.778 | NREventA3 | measId:2;ServCellPCI:464;Se... |
| 2024-09-20 22:21:36.778 | NREventA3 | measId:2;ServCellPCI:464;Se... |
| 2024-09-20 22:21:39.278 | NRRRCReestablishAttempt | PCI:464 |
| 2024-09-20 22:21:39.291 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.302 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.433 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.433 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263651 | 1 | 16.8871 | 14.5994 | -116.5842 | 13.2245 | 116.9331 | 0.0062 | 0.0012 |
| 2024_09_20 22:00 | 3268469 | 2 | 8.9159 | 8.5921 | -114.9437 | 15.6725 | 93.2542 | 0.0078 | 0.1932 |
| 2024_09_20 22:00 | 3268252 | 3 | 5.0772 | 9.9194 | -115.6448 | 16.2558 | 188.8722 | 0.0135 | 0.0029 |
| 2024_09_20 22:00 | 3214366 | 4 | 15.1807 | 17.5854 | -115.9237 | 8.5311 | 93.5852 | 0.0143 | 0.0148 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413631_61A71AC1 | 504990 | 673 | -88.6 | 504990 | 937 | -94.1 | 504990 | 898 | -95.0 | 504990 | 568 |
| MR_1774413631_5D103643 | 504990 | 937 | -93.7 | 504990 | 673 | -89.9 | 504990 | 898 | -93.4 | 504990 | 568 |
| MR_1774413631_F236957E | 504990 | 937 | -92.0 | 504990 | 673 | -91.0 | 504990 | 898 | -94.3 | 504990 | 568 |
| MR_1774413631_E025A78E | 504990 | 937 | -94.9 | 504990 | 673 | -87.7 | 504990 | 898 | -93.2 | 504990 | 568 |
| MR_1774413631_CE2111C0 | 504990 | 937 | -93.6 | 504990 | 673 | -88.3 | 504990 | 898 | -93.9 | 504990 | 568 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1072: `a0f7e8bf-e28...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a0f7e8bf-e280-4d98-a164-2bffe1e0647a` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1072] topology](images/train_1072.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3228526_2 by 17 degrees
- `C2`: Add neighbor relationship between 3240668_3 and 3228526_2
- `C3`: Press down the tilt angle  of 3228526_2 by 10 degrees
- `C4`: Increase transmission power for 3230817_4
- `C5`: Adjust the azimuth of 3230817_4 by 11 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230817_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228526_2
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228526_2
- `C10`: Increase A3 Offset threshold for 3230817_4
- `C11`: Lift the tilt angle of 3230817_4 by 10 degrees
- `C12`: Add neighbor relationship between 3230817_4 and 3228526_2
- `C13`: Increase transmission power for 3228526_2
- `C14`: Decrease transmission power for 3228526_2
- `C15`: Decrease transmission power for 3230817_4
- `C16`: Increase A3 Offset threshold for 3228526_2
- `C17`: Press down the tilt angle of 3230817_4 by 10 degrees
- `C18`: Check test server and transmission issues **← 정답**
- `C19`: Decrease A3 Offset threshold for 3228526_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230817_4
- `C21`: Decrease A3 Offset threshold for 3230817_4
- `C22`: Lift the tilt angle  of 3228526_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.807 | MS1 | 121.4656768664 | 31.1446378021 | 303 | 504990 | -89.48 | 12.92 | 323.24 | 0.02 | 2.75 | 1564 |
| 2024-09-20 22:21:32.628 | MS1 | 121.4656764719 | 31.1446265169 | 303 | 504990 | -89.70 | 15.26 | 361.29 | 0.05 | 2.49 | 1597 |
| 2024-09-20 22:21:33.760 | MS1 | 121.4656702786 | 31.1446211480 | 303 | 504990 | -85.32 | 17.62 | 534.23 | 0.08 | 2.31 | 1582 |
| 2024-09-20 22:21:34.522 | MS1 | 121.4656584280 | 31.1446303146 | 303 | 504990 | -90.63 | 12.69 | 48.59 | 0.02 | 2.26 | 396 |
| 2024-09-20 22:21:35.537 | MS1 | 121.4656748404 | 31.1446253243 | 303 | 504990 | -86.16 | 17.12 | 61.73 | 0.01 | 2.37 | 499 |
| 2024-09-20 22:21:36.478 | MS1 | 121.4656598399 | 31.1446276156 | 303 | 504990 | -89.86 | 16.12 | 93.49 | 0.14 | 2.54 | 412 |
| 2024-09-20 22:21:37.456 | MS1 | 121.4656597855 | 31.1446317480 | 303 | 504990 | -89.15 | 9.41 | 102.44 | 0.15 | 2.52 | 310 |
| 2024-09-20 22:21:38.525 | MS1 | 121.4656638725 | 31.1446283967 | 303 | 504990 | -92.48 | 12.23 | 74.23 | 0.05 | 2.55 | 477 |
| 2024-09-20 22:21:39.270 | MS1 | 121.4656583681 | 31.1446208251 | 303 | 504990 | -91.19 | 8.85 | 94.72 | 0.16 | 3.00 | 404 |
| 2024-09-20 22:21:40.183 | MS1 | 121.4656702024 | 31.1446259524 | 303 | 504990 | -89.32 | 11.92 | 573.75 | 0.16 | 2.88 | 1595 |
| 2024-09-20 22:21:41.328 | MS1 | 121.4656763804 | 31.1446184940 | 303 | 504990 | -93.88 | 12.11 | 460.17 | 0.14 | 2.56 | 1596 |
| 2024-09-20 22:21:42.434 | MS1 | 121.4656749608 | 31.1446375024 | 303 | 504990 | -93.73 | 10.56 | 356.03 | 0.02 | 2.97 | 1582 |

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
| 3211549 | 1 | 121.4750213718 | 31.1445481410 | 97 | 6 | 3 | 49.9 | TDD | 689 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3228526 | 2 | 121.4732999690 | 31.1547287824 | 196 | 11 | 8 | 49.4 | TDD | 266 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3230817 | 4 | 121.4641618290 | 31.1494319002 | 176 | 15 | 0 | 19.6 | TDD | 303 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3240668 | 3 | 121.4698767971 | 31.1473543788 | 190 | 10 | 1 | 26.1 | TDD | 626 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.178 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.199 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.310 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.310 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.007 | NREventA3 | measId:2;ServCellPCI:889;Se... |
| 2024-09-20 22:21:38.247 | NRHandoverAttempt | SourcePCI:889;SourceNR-ARFC... |
| 2024-09-20 22:21:38.293 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.304 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.452 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.452 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211549 | 1 | 14.7653 | 10.5599 | -117.1019 | 15.8403 | 156.3964 | 0.0198 | 0.0184 |
| 2024_09_20 22:00 | 3228526 | 2 | 16.1151 | 17.9932 | -117.6705 | 12.4549 | 82.0462 | 0.0015 | 0.0137 |
| 2024_09_20 22:00 | 3240668 | 3 | 19.1185 | 11.6176 | -117.1364 | 8.4835 | 179.5470 | 0.0174 | 0.0049 |
| 2024_09_20 22:00 | 3230817 | 4 | 9.1545 | 9.4267 | -116.8089 | 15.0006 | 145.0374 | 0.0003 | 0.0126 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413919_DCA6380C | 504990 | 303 | -91.5 | 504990 | 266 | -97.1 | 504990 | 626 | -102.6 | 504990 | 689 |
| MR_1774413919_9ED315E6 | 504990 | 303 | -89.7 | 504990 | 266 | -97.3 | 504990 | 626 | -102.3 | 504990 | 689 |
| MR_1774413919_6C80B334 | 504990 | 303 | -91.0 | 504990 | 266 | -97.4 | 504990 | 626 | -102.6 | 504990 | 689 |
| MR_1774413919_0778B25B | 504990 | 303 | -89.3 | 504990 | 266 | -96.3 | 504990 | 626 | -105.1 | 504990 | 689 |
| MR_1774413919_2CF1A8FF | 504990 | 303 | -91.2 | 504990 | 266 | -96.0 | 504990 | 626 | -105.6 | 504990 | 689 |
| MR_1774413919_5A9A6064 | 504990 | 303 | -92.6 | 504990 | 266 | -96.7 | 504990 | 626 | -105.6 | 504990 | 689 |
| MR_1774413919_55FFA8B6 | 504990 | 303 | -90.0 | 504990 | 266 | -99.0 | 504990 | 626 | -102.1 | 504990 | 689 |
| MR_1774413919_3B01130F | 504990 | 303 | -90.8 | 504990 | 266 | -97.3 | 504990 | 626 | -104.8 | 504990 | 689 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1073: `1af44849-e28...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1af44849-e284-4727-a89e-593aa6b843cd` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1073] topology](images/train_1073.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3220498_2 by 9 degrees
- `C2`: Press down the tilt angle  of 3257970_4 by 10 degrees
- `C3`: Decrease A3 Offset threshold for 3220498_2
- `C4`: Increase transmission power for 3220498_2
- `C5`: Adjust the azimuth of 3220498_2 by 45 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220498_2
- `C8`: Decrease A3 Offset threshold for 3257970_4
- `C9`: Lift the tilt angle  of 3257970_4 by 10 degrees
- `C10`: Adjust the azimuth of 3257970_4 by 50 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257970_4
- `C12`: Increase A3 Offset threshold for 3257970_4
- `C13`: Check test server and transmission issues **← 정답**
- `C14`: Decrease transmission power for 3257970_4
- `C15`: Add neighbor relationship between 3220498_2 and 3257970_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220498_2
- `C17`: Add neighbor relationship between 3210160_3 and 3257970_4
- `C18`: Increase A3 Offset threshold for 3220498_2
- `C19`: Increase transmission power for 3257970_4
- `C20`: Decrease transmission power for 3220498_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257970_4
- `C22`: Lift the tilt angle of 3220498_2 by 9 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.252 | MS1 | 121.4656704978 | 31.1446361082 | 628 | 504990 | -90.93 | 14.07 | 519.07 | 0.11 | 2.48 | 1591 |
| 2024-09-20 22:21:32.355 | MS1 | 121.4656740072 | 31.1446318887 | 628 | 504990 | -90.66 | 12.86 | 408.05 | 0.01 | 2.11 | 1585 |
| 2024-09-20 22:21:33.298 | MS1 | 121.4656609232 | 31.1446343573 | 628 | 504990 | -88.63 | 17.93 | 409.18 | 0.20 | 2.48 | 1595 |
| 2024-09-20 22:21:34.235 | MS1 | 121.4656582038 | 31.1446377216 | 628 | 504990 | -85.97 | 16.02 | 106.01 | 0.16 | 2.61 | 483 |
| 2024-09-20 22:21:35.284 | MS1 | 121.4656658614 | 31.1446197214 | 628 | 504990 | -89.23 | 14.41 | 56.52 | 0.11 | 2.87 | 421 |
| 2024-09-20 22:21:36.497 | MS1 | 121.4656583184 | 31.1446305412 | 628 | 504990 | -91.04 | 17.40 | 75.69 | 0.05 | 2.57 | 339 |
| 2024-09-20 22:21:37.249 | MS1 | 121.4656748621 | 31.1446216239 | 628 | 504990 | -90.46 | 8.04 | 59.84 | 0.12 | 2.11 | 351 |
| 2024-09-20 22:21:38.708 | MS1 | 121.4656675052 | 31.1446342728 | 628 | 504990 | -89.23 | 12.84 | 65.35 | 0.00 | 2.02 | 406 |
| 2024-09-20 22:21:39.544 | MS1 | 121.4656614474 | 31.1446242356 | 628 | 504990 | -92.01 | 7.20 | 79.00 | 0.20 | 2.01 | 300 |
| 2024-09-20 22:21:40.987 | MS1 | 121.4656717997 | 31.1446308281 | 628 | 504990 | -91.33 | 8.02 | 497.29 | 0.07 | 2.67 | 1594 |
| 2024-09-20 22:21:41.813 | MS1 | 121.4656757912 | 31.1446271357 | 628 | 504990 | -92.75 | 9.78 | 446.74 | 0.01 | 2.66 | 1568 |
| 2024-09-20 22:21:42.318 | MS1 | 121.4656607959 | 31.1446302093 | 628 | 504990 | -91.61 | 7.56 | 438.77 | 0.01 | 2.23 | 1589 |

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
| 3210160 | 3 | 121.4683308659 | 31.1470865483 | 18 | 11 | 0 | 15.5 | TDD | 197 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3220498 | 2 | 121.4739681228 | 31.1454044877 | 309 | 7 | 11 | 21.7 | TDD | 628 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3233017 | 1 | 121.4752371800 | 31.1538421545 | 111 | 3 | 12 | 40.0 | TDD | 427 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3257970 | 4 | 121.4660635325 | 31.1471908262 | 77 | 13 | 9 | 21.8 | TDD | 222 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.856 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.871 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.995 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.995 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.731 | NREventA3 | measId:2;ServCellPCI:617;Se... |
| 2024-09-20 22:21:37.971 | NRHandoverAttempt | SourcePCI:617;SourceNR-ARFC... |
| 2024-09-20 22:21:38.015 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.027 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.162 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.162 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233017 | 1 | 8.2426 | 6.9975 | -117.5867 | 19.2581 | 136.1058 | 0.0115 | 0.0014 |
| 2024_09_20 22:00 | 3220498 | 2 | 14.1610 | 14.7974 | -117.0392 | 6.8273 | 179.7511 | 0.0099 | 0.0056 |
| 2024_09_20 22:00 | 3210160 | 3 | 7.5124 | 17.4759 | -115.4396 | 9.3144 | 172.7807 | 0.0108 | 0.0081 |
| 2024_09_20 22:00 | 3257970 | 4 | 19.7391 | 17.7582 | -115.0381 | 17.5906 | 176.7230 | 0.0079 | 0.0194 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415652_BD2FACFB | 504990 | 628 | -88.0 | 504990 | 222 | -95.4 | 504990 | 197 | -100.4 | 504990 | 427 |
| MR_1774415652_F756EC80 | 504990 | 628 | -90.5 | 504990 | 222 | -95.2 | 504990 | 197 | -98.9 | 504990 | 427 |
| MR_1774415652_BF4F2DF1 | 504990 | 628 | -87.5 | 504990 | 222 | -95.0 | 504990 | 197 | -100.4 | 504990 | 427 |
| MR_1774415652_35C0FA97 | 504990 | 628 | -91.1 | 504990 | 222 | -95.4 | 504990 | 197 | -100.0 | 504990 | 427 |
| MR_1774415652_238CB810 | 504990 | 628 | -88.8 | 504990 | 222 | -93.9 | 504990 | 197 | -97.2 | 504990 | 427 |
| MR_1774415652_41C4CE94 | 504990 | 628 | -88.7 | 504990 | 222 | -94.5 | 504990 | 197 | -99.4 | 504990 | 427 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1074: `cbf4272e-2ad...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cbf4272e-2adb-4b8f-a293-f00b483328dd` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1074] topology](images/train_1074.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment. **← 정답**
- `C2`: Adjust the azimuth of 3261988_3 by 9 degrees
- `C3`: Adjust the azimuth of 3219123_1 by 50 degrees
- `C4`: Press down the tilt angle  of 3219123_1 by 10 degrees
- `C5`: Lift the tilt angle of 3261988_3 by 10 degrees
- `C6`: Decrease transmission power for 3219123_1
- `C7`: Press down the tilt angle of 3261988_3 by 10 degrees
- `C8`: Increase A3 Offset threshold for 3219123_1
- `C9`: Increase transmission power for 3219123_1
- `C10`: Add neighbor relationship between 3249623_4 and 3219123_1
- `C11`: Add neighbor relationship between 3261988_3 and 3219123_1
- `C12`: Increase A3 Offset threshold for 3261988_3
- `C13`: Lift the tilt angle  of 3219123_1 by 10 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219123_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261988_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219123_1
- `C17`: Decrease A3 Offset threshold for 3219123_1
- `C18`: Increase transmission power for 3261988_3
- `C19`: Decrease transmission power for 3261988_3
- `C20`: Decrease A3 Offset threshold for 3261988_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261988_3
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.972 | MS1 | 121.4656644750 | 31.1446292424 | 886 | 504990 | -89.60 | 13.83 | 414.65 | 0.01 | 2.54 | 1587 |
| 2024-09-20 22:21:32.336 | MS1 | 121.4656681931 | 31.1446346921 | 886 | 504990 | -89.01 | 16.38 | 345.83 | 0.17 | 2.65 | 1588 |
| 2024-09-20 22:21:33.263 | MS1 | 121.4656686632 | 31.1446193594 | 886 | 504990 | -88.79 | 17.96 | 530.86 | 0.00 | 2.41 | 1598 |
| 2024-09-20 22:21:34.224 | MS1 | 121.4656643944 | 31.1446306142 | 886 | 504990 | -90.98 | 16.44 | 79.29 | 0.17 | 2.57 | 1561 |
| 2024-09-20 22:21:35.626 | MS1 | 121.4656587159 | 31.1446329327 | 886 | 504990 | -91.29 | 16.81 | 95.62 | 0.12 | 2.13 | 1580 |
| 2024-09-20 22:21:36.696 | MS1 | 121.4656742703 | 31.1446237559 | 886 | 504990 | -91.04 | 15.41 | 76.99 | 0.12 | 2.54 | 1562 |
| 2024-09-20 22:21:37.750 | MS1 | 121.4656764558 | 31.1446259483 | 886 | 504990 | -93.37 | 12.37 | 82.86 | 0.11 | 2.06 | 1571 |
| 2024-09-20 22:21:38.389 | MS1 | 121.4656690725 | 31.1446193529 | 886 | 504990 | -93.41 | 9.59 | 67.03 | 0.05 | 2.13 | 1593 |
| 2024-09-20 22:21:39.904 | MS1 | 121.4656645989 | 31.1446294368 | 886 | 504990 | -92.37 | 8.01 | 73.89 | 0.10 | 2.86 | 1579 |
| 2024-09-20 22:21:40.456 | MS1 | 121.4656691788 | 31.1446335773 | 886 | 504990 | -91.22 | 11.77 | 438.49 | 0.05 | 2.19 | 1596 |
| 2024-09-20 22:21:41.547 | MS1 | 121.4656704386 | 31.1446293680 | 886 | 504990 | -91.63 | 8.41 | 306.03 | 0.03 | 2.05 | 1595 |
| 2024-09-20 22:21:42.656 | MS1 | 121.4656748195 | 31.1446282354 | 886 | 504990 | -91.89 | 12.55 | 429.58 | 0.19 | 2.18 | 1561 |

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
| 3219123 | 1 | 121.4749479403 | 31.1452425165 | 212 | 9 | 11 | 36.4 | TDD | 737 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3245360 | 2 | 121.4740598786 | 31.1457076071 | 88 | 0 | 3 | 46.6 | TDD | 474 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3249623 | 4 | 121.4656379309 | 31.1513700178 | 72 | 0 | 1 | 16.0 | TDD | 575 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3261988 | 3 | 121.4700487083 | 31.1448021329 | 276 | 12 | 6 | 22.9 | TDD | 886 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.035 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.057 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.179 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.179 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.911 | NREventA3 | measId:2;ServCellPCI:482;Se... |
| 2024-09-20 22:21:38.151 | NRHandoverAttempt | SourcePCI:482;SourceNR-ARFC... |
| 2024-09-20 22:21:38.199 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.213 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.362 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.362 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3219123 | 1 | 77.0788 | 80.9433 | -116.0846 | 7.9145 | 184.7532 | 0.0107 | 0.0110 |
| 2024_09_19 22:00 | 3245360 | 2 | 85.3984 | 82.8820 | -117.6444 | 15.1647 | 167.0461 | 0.0132 | 0.0166 |
| 2024_09_19 22:00 | 3261988 | 3 | 87.1624 | 83.5024 | -114.1394 | 15.3541 | 144.9485 | 0.0002 | 0.0041 |
| 2024_09_19 22:00 | 3249623 | 4 | 88.3699 | 77.6487 | -114.0626 | 19.2406 | 175.5431 | 0.0141 | 0.0118 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413037_370F9CCF | 504990 | 886 | -89.8 | 504990 | 737 | -97.7 | 504990 | 575 | -103.5 | 504990 | 474 |
| MR_1774413037_C602583C | 504990 | 886 | -90.0 | 504990 | 737 | -100.1 | 504990 | 575 | -102.7 | 504990 | 474 |
| MR_1774413037_51BCE2E1 | 504990 | 886 | -89.4 | 504990 | 737 | -98.6 | 504990 | 575 | -103.4 | 504990 | 474 |
| MR_1774413037_43AED9C7 | 504990 | 886 | -91.3 | 504990 | 737 | -98.2 | 504990 | 575 | -104.6 | 504990 | 474 |
| MR_1774413037_31B4AA4D | 504990 | 886 | -92.5 | 504990 | 737 | -96.6 | 504990 | 575 | -101.7 | 504990 | 474 |
| MR_1774413037_36E56128 | 504990 | 886 | -92.2 | 504990 | 737 | -97.5 | 504990 | 575 | -102.6 | 504990 | 474 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1075: `ce339496-c3f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ce339496-c3ff-41a7-baca-e29172223c5f` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Lift the tilt angle  of 3262506_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1075] topology](images/train_1075.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3268968_4
- `C2`: Add neighbor relationship between 3249017_1 and 3268968_4
- `C3`: Decrease transmission power for 3268968_4
- `C4`: Press down the tilt angle  of 3262506_2 by 10 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268968_4
- `C6`: Adjust the azimuth of 3249017_1 by 4 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249017_1
- `C8`: Check test server and transmission issues
- `C9`: Adjust the azimuth of 3262506_2 by 50 degrees
- `C10`: Increase A3 Offset threshold for 3249017_1
- `C11`: Add neighbor relationship between 3262506_2 and 3268968_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268968_4
- `C13`: Lift the tilt angle of 3249017_1 by 5 degrees
- `C14`: Decrease A3 Offset threshold for 3249017_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249017_1
- `C17`: Increase A3 Offset threshold for 3268968_4
- `C18`: Lift the tilt angle  of 3262506_2 by 10 degrees **← 정답**
- `C19`: Press down the tilt angle of 3249017_1 by 5 degrees
- `C20`: Increase transmission power for 3249017_1
- `C21`: Decrease transmission power for 3249017_1
- `C22`: Decrease A3 Offset threshold for 3268968_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.476 | MS1 | 121.4656748382 | 31.1446304468 | 304 | 504990 | -89.88 | 16.36 | 383.89 | 0.18 | 2.70 | 1560 |
| 2024-09-20 22:21:32.747 | MS1 | 121.4656697653 | 31.1446318443 | 304 | 504990 | -89.45 | 16.41 | 321.55 | 0.11 | 2.15 | 1572 |
| 2024-09-20 22:21:33.539 | MS1 | 121.4656688971 | 31.1446245789 | 304 | 504990 | -90.17 | 12.70 | 514.11 | 0.06 | 2.99 | 1600 |
| 2024-09-20 22:21:34.382 | MS1 | 121.4656669595 | 31.1446374045 | 304 | 504990 | -89.23 | 16.33 | 101.58 | 0.01 | 2.54 | 1585 |
| 2024-09-20 22:21:35.998 | MS1 | 121.4656771098 | 31.1446232213 | 304 | 504990 | -87.07 | 16.90 | 61.63 | 0.09 | 2.98 | 1567 |
| 2024-09-20 22:21:36.641 | MS1 | 121.4656663625 | 31.1446223790 | 304 | 504990 | -86.96 | 15.59 | 85.63 | 0.00 | 2.60 | 1566 |
| 2024-09-20 22:21:37.749 | MS1 | 121.4656614497 | 31.1446335798 | 304 | 504990 | -90.22 | 10.51 | 50.91 | 0.20 | 2.74 | 1562 |
| 2024-09-20 22:21:38.125 | MS1 | 121.4656607321 | 31.1446199931 | 304 | 504990 | -91.06 | 7.32 | 51.46 | 0.06 | 2.48 | 1563 |
| 2024-09-20 22:21:39.941 | MS1 | 121.4656763257 | 31.1446325683 | 304 | 504990 | -91.06 | 11.33 | 74.33 | 0.13 | 2.64 | 1579 |
| 2024-09-20 22:21:40.491 | MS1 | 121.4656583374 | 31.1446254751 | 304 | 504990 | -92.32 | 10.57 | 404.87 | 0.12 | 2.85 | 1599 |
| 2024-09-20 22:21:41.631 | MS1 | 121.4656689842 | 31.1446306310 | 304 | 504990 | -93.76 | 7.83 | 398.85 | 0.07 | 2.66 | 1593 |
| 2024-09-20 22:21:42.129 | MS1 | 121.4656604701 | 31.1446230597 | 304 | 504990 | -93.12 | 10.96 | 578.94 | 0.04 | 2.25 | 1592 |

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
| 3230408 | 3 | 121.4716761243 | 31.1469285293 | 176 | 15 | 8 | 15.6 | TDD | 931 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3249017 | 1 | 121.4692632112 | 31.1440712347 | 284 | 0 | 6 | 28.7 | TDD | 304 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3262506 | 2 | 121.4671153352 | 31.1539454412 | 329 | 4 | 6 | 35.1 | TDD | 442 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3268968 | 4 | 121.4708811580 | 31.1460882362 | 34 | 12 | 6 | 18.1 | TDD | 879 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.193 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.212 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.326 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.326 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.020 | NREventA3 | measId:2;ServCellPCI:777;Se... |
| 2024-09-20 22:21:38.260 | NRHandoverAttempt | SourcePCI:777;SourceNR-ARFC... |
| 2024-09-20 22:21:38.295 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.308 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.435 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.435 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249017 | 1 | 87.5450 | 88.2701 | -115.8085 | 11.7148 | 175.8639 | 0.0148 | 0.0081 |
| 2024_09_20 22:00 | 3262506 | 2 | 8.9387 | 16.3853 | -117.7223 | 17.5487 | 92.1445 | 0.0128 | 0.0161 |
| 2024_09_20 22:00 | 3230408 | 3 | 19.0719 | 15.1538 | -115.4458 | 10.7485 | 199.9779 | 0.0127 | 0.0157 |
| 2024_09_20 22:00 | 3268968 | 4 | 18.6101 | 17.4529 | -114.5823 | 15.8455 | 198.0850 | 0.0017 | 0.0096 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417124_5D922A4E | 504990 | 304 | -88.1 | 504990 | 879 | -97.5 | 504990 | 442 | -97.1 | 504990 | 931 |
| MR_1774417124_E947CDA7 | 504990 | 304 | -86.0 | 504990 | 879 | -98.1 | 504990 | 442 | -96.6 | 504990 | 931 |
| MR_1774417124_69DEEBF9 | 504990 | 304 | -88.1 | 504990 | 879 | -95.0 | 504990 | 442 | -97.3 | 504990 | 931 |
| MR_1774417124_65714F67 | 504990 | 304 | -88.5 | 504990 | 879 | -97.0 | 504990 | 442 | -95.7 | 504990 | 931 |
| MR_1774417124_240EAB18 | 504990 | 304 | -86.9 | 504990 | 879 | -94.6 | 504990 | 442 | -97.2 | 504990 | 931 |
| MR_1774417124_14601BEF | 504990 | 304 | -85.9 | 504990 | 879 | -95.1 | 504990 | 442 | -95.9 | 504990 | 931 |
| MR_1774417124_EA2295D4 | 504990 | 304 | -86.0 | 504990 | 879 | -97.8 | 504990 | 442 | -98.5 | 504990 | 931 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1076: `9181b85b-ae4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9181b85b-ae48-4627-acb6-2020e7c48431` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213121_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1076] topology](images/train_1076.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3249569_13 and 3266505_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266505_2
- `C3`: Add neighbor relationship between 3213121_6 and 3266505_2
- `C4`: Press down the tilt angle  of 3266505_2 by 2 degrees
- `C5`: Decrease A3 Offset threshold for 3213121_6
- `C6`: Adjust the azimuth of 3213121_6 by 41 degrees
- `C7`: Increase transmission power for 3213121_6
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213121_6 **← 정답**
- `C9`: Press down the tilt angle of 3213121_6 by 4 degrees
- `C10`: Increase transmission power for 3266505_2
- `C11`: Decrease A3 Offset threshold for 3266505_2
- `C12`: Check test server and transmission issues
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266505_2
- `C14`: Decrease transmission power for 3266505_2
- `C15`: Increase A3 Offset threshold for 3266505_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213121_6
- `C17`: Increase A3 Offset threshold for 3213121_6
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Lift the tilt angle of 3213121_6 by 4 degrees
- `C20`: Decrease transmission power for 3213121_6
- `C21`: Lift the tilt angle  of 3266505_2 by 2 degrees
- `C22`: Adjust the azimuth of 3266505_2 by 26 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.133 | MS1 | 121.4656660220 | 31.1446288869 | 767 | 504990 | -94.42 | 9.27 | 483.26 | 0.17 | 2.97 | 1597 |
| 2024-09-20 22:21:32.245 | MS1 | 121.4656739685 | 31.1446374901 | 85 | 504990 | -95.85 | 10.18 | 447.05 | 0.07 | 2.46 | 1588 |
| 2024-09-20 22:21:33.135 | MS1 | 121.4656620799 | 31.1446229221 | 606 | 504990 | -95.82 | 11.35 | 382.75 | 0.01 | 2.49 | 1562 |
| 2024-09-20 22:21:34.162 | MS1 | 121.4656592168 | 31.1446232645 | 876 | 152650 | -88.18 | 2.26 | 69.46 | 0.05 | 1.67 | 938 |
| 2024-09-20 22:21:35.352 | MS1 | 121.4656656446 | 31.1446321843 | 1 | 152650 | -92.53 | 6.31 | 83.67 | 0.06 | 1.86 | 965 |
| 2024-09-20 22:21:36.716 | MS1 | 121.4656706898 | 31.1446290245 | 251 | 152650 | -88.18 | 4.35 | 63.66 | 0.13 | 1.81 | 918 |
| 2024-09-20 22:21:37.519 | MS1 | 121.4656620920 | 31.1446276710 | 420 | 152650 | -90.82 | 5.91 | 57.93 | 0.07 | 1.54 | 923 |
| 2024-09-20 22:21:38.101 | MS1 | 121.4656745272 | 31.1446189295 | 876 | 152650 | -88.79 | 4.30 | 46.17 | 0.02 | 1.65 | 975 |
| 2024-09-20 22:21:39.978 | MS1 | 121.4656606150 | 31.1446265625 | 1 | 152650 | -87.98 | 6.66 | 53.18 | 0.01 | 1.73 | 913 |
| 2024-09-20 22:21:40.744 | MS1 | 121.4656695007 | 31.1446327789 | 251 | 152650 | -92.29 | 5.46 | 60.26 | 0.05 | 2.64 | 1563 |
| 2024-09-20 22:21:41.831 | MS1 | 121.4656778322 | 31.1446315278 | 420 | 152650 | -93.88 | 5.61 | 74.25 | 0.00 | 2.44 | 1572 |
| 2024-09-20 22:21:42.291 | MS1 | 121.4656599123 | 31.1446223448 | 876 | 152650 | -90.80 | 3.39 | 92.16 | 0.08 | 2.52 | 1578 |

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
| 3213121 | 6 | 121.4673253859 | 31.1535594774 | 230 | 4 | 1 | 4.0 | TDD | 767 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3213746 | 8 | 121.4687726524 | 31.1466043147 | 156 | 5 | 6 | 18.0 | FDD | 356 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3216758 | 1 | 121.4667728583 | 31.1509890115 | 296 | 14 | 0 | 17.2 | TDD | 11 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3221847 | 12 | 121.4710337548 | 31.1524281947 | 37 | 0 | 7 | 22.3 | FDD | 184 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3224506 | 7 | 121.4753034902 | 31.1518729218 | 94 | 7 | 0 | 2.3 | FDD | 1 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3229518 | 5 | 121.4758631531 | 31.1454894645 | 327 | 5 | 12 | 19.5 | TDD | 606 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3236299 | 10 | 121.4708218146 | 31.1469760948 | 181 | 14 | 4 | 23.3 | FDD | 774 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3242465 | 9 | 121.4709475879 | 31.1486685824 | 355 | 2 | 1 | 29.7 | FDD | 420 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3247327 | 11 | 121.4712119521 | 31.1478076893 | 276 | 0 | 12 | 2.4 | FDD | 876 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3249569 | 13 | 121.4722581571 | 31.1512327557 | 317 | 14 | 1 | 17.4 | FDD | 251 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3258750 | 3 | 121.4664514394 | 31.1483229050 | 310 | 5 | 12 | 25.4 | TDD | 85 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3266505 | 2 | 121.4711884758 | 31.1496664653 | 249 | 1 | 9 | 11.9 | TDD | 114 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3279828 | 4 | 121.4645602132 | 31.1519084448 | 239 | 12 | 9 | 19.8 | TDD | 348 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.343 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.364 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.484 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.484 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.236 | NREventA2 | measId:1;ServCellPCI:174;Se... |
| 2024-09-20 22:21:35.382 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.659 | NREventA5 | measId:3;ServCellPCI:174;Se... |
| 2024-09-20 22:21:35.697 | NRHandoverAttempt | SourcePCI:174;SourceNR-ARFC... |
| 2024-09-20 22:21:35.730 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.742 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.884 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.884 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216758 | 1 | 9.0673 | 14.6236 | -117.4901 | 18.8116 | 81.3924 | 0.0116 | 0.0028 |
| 2024_09_20 22:00 | 3266505 | 2 | 8.4093 | 7.0172 | -114.2277 | 6.0180 | 191.5275 | 0.0173 | 0.0131 |
| 2024_09_20 22:00 | 3258750 | 3 | 16.0817 | 9.5015 | -115.9983 | 16.2070 | 139.7708 | 0.0196 | 0.0046 |
| 2024_09_20 22:00 | 3279828 | 4 | 11.8973 | 8.7763 | -115.5470 | 18.3613 | 139.2552 | 0.0151 | 0.0113 |
| 2024_09_20 22:00 | 3229518 | 5 | 17.4840 | 5.9190 | -114.4366 | 8.1506 | 174.2187 | 0.0024 | 0.0069 |
| 2024_09_20 22:00 | 3213121 | 6 | 15.0777 | 16.5613 | -117.4312 | 19.0598 | 135.5794 | 0.0135 | 0.0029 |
| 2024_09_20 22:00 | 3224506 | 7 | 14.6380 | 17.6339 | -115.3158 | 3.7311 | 32.9164 | 0.0176 | 0.0033 |
| 2024_09_20 22:00 | 3213746 | 8 | 19.8325 | 12.8788 | -115.2619 | 3.6994 | 29.3287 | 0.0029 | 0.0043 |
| 2024_09_20 22:00 | 3242465 | 9 | 12.6731 | 8.9272 | -114.1322 | 3.1494 | 34.4567 | 0.0079 | 0.0117 |
| 2024_09_20 22:00 | 3236299 | 10 | 13.1339 | 5.0019 | -116.1062 | 3.8173 | 30.3751 | 0.0048 | 0.0115 |
| 2024_09_20 22:00 | 3247327 | 11 | 18.5975 | 16.9714 | -114.5165 | 4.2842 | 24.4621 | 0.0073 | 0.0091 |
| 2024_09_20 22:00 | 3221847 | 12 | 10.7240 | 13.9664 | -114.3075 | 4.4526 | 35.3272 | 0.0098 | 0.0146 |
| 2024_09_20 22:00 | 3249569 | 13 | 15.1583 | 14.4899 | -115.2745 | 4.6144 | 30.1718 | 0.0008 | 0.0139 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413262_7CE1546C | 504990 | 606 | -94.2 | 504990 | 114 | -93.2 | 504990 | 348 | -97.9 | 504990 | 11 |
| MR_1774413262_423F0B08 | 504990 | 606 | -97.8 | 504990 | 114 | -94.3 | 504990 | 348 | -98.0 | 504990 | 11 |
| MR_1774413262_D2815CDB | 504990 | 606 | -94.3 | 504990 | 114 | -96.6 | 504990 | 348 | -100.0 | 504990 | 11 |
| MR_1774413262_B4FA449B | 504990 | 606 | -96.1 | 504990 | 114 | -94.8 | 504990 | 348 | -100.3 | 504990 | 11 |
| MR_1774413262_FCF3049B | 152650 | 876 | -86.9 | 152650 | 356 | -96.6 | 152650 | 184 | -96.1 | 152650 | 774 |
| MR_1774413262_8C4BC554 | 152650 | 876 | -89.0 | 152650 | 356 | -93.7 | 152650 | 184 | -97.5 | 152650 | 774 |
| MR_1774413262_86A6290E | 504990 | 606 | -96.8 | 504990 | 114 | -96.1 | 504990 | 348 | -98.6 | 504990 | 11 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1077: `acbbd8c4-f4d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `acbbd8c4-f4d1-4a04-9d32-7aa9ff75e643` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Add neighbor relationship between 3212776_2 and 3237488_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1077] topology](images/train_1077.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase transmission power for 3237488_4
- `C3`: Press down the tilt angle  of 3237488_4 by 6 degrees
- `C4`: Increase transmission power for 3212776_2
- `C5`: Add neighbor relationship between 3212776_2 and 3237488_4 **← 정답**
- `C6`: Increase A3 Offset threshold for 3212776_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212776_2
- `C8`: Decrease transmission power for 3212776_2
- `C9`: Decrease A3 Offset threshold for 3237488_4
- `C10`: Decrease transmission power for 3237488_4
- `C11`: Press down the tilt angle of 3212776_2 by 10 degrees
- `C12`: Lift the tilt angle of 3212776_2 by 10 degrees
- `C13`: Add neighbor relationship between 3216829_1 and 3237488_4
- `C14`: Lift the tilt angle  of 3237488_4 by 6 degrees
- `C15`: Adjust the azimuth of 3237488_4 by 36 degrees
- `C16`: Increase A3 Offset threshold for 3237488_4
- `C17`: Decrease A3 Offset threshold for 3212776_2
- `C18`: Check test server and transmission issues
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212776_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237488_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237488_4
- `C22`: Adjust the azimuth of 3212776_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.191 | MS1 | 121.4656655367 | 31.1446377635 | 627 | 504990 | -78.16 | 12.89 | 383.57 | 0.05 | 2.60 | 1574 |
| 2024-09-20 22:21:32.956 | MS1 | 121.4656730658 | 31.1446378637 | 627 | 504990 | -78.02 | 15.53 | 427.20 | 0.19 | 2.81 | 1580 |
| 2024-09-20 22:21:33.803 | MS1 | 121.4656639453 | 31.1446360992 | 627 | 504990 | -79.63 | 14.73 | 483.67 | 0.13 | 2.25 | 1572 |
| 2024-09-20 22:21:34.781 | MS1 | 121.4656621929 | 31.1446302310 | 627 | 504990 | -94.46 | -2.64 | 61.88 | 0.13 | 1.47 | 1563 |
| 2024-09-20 22:21:35.985 | MS1 | 121.4656630838 | 31.1446232467 | 627 | 504990 | -91.57 | -2.28 | 41.75 | 0.14 | 1.19 | 1564 |
| 2024-09-20 22:21:36.970 | MS1 | 121.4656741308 | 31.1446332121 | 627 | 504990 | -94.85 | -1.05 | 73.32 | 0.06 | 1.38 | 1586 |
| 2024-09-20 22:21:37.253 | MS1 | 121.4656722133 | 31.1446361587 | 627 | 504990 | -92.73 | -0.28 | 50.95 | 0.04 | 1.40 | 1594 |
| 2024-09-20 22:21:38.691 | MS1 | 121.4656731907 | 31.1446245433 | 627 | 504990 | -77.26 | 14.64 | 458.17 | 0.17 | 1.17 | 1587 |
| 2024-09-20 22:21:39.524 | MS1 | 121.4656717627 | 31.1446264611 | 627 | 504990 | -79.73 | 17.96 | 512.17 | 0.09 | 1.29 | 1560 |
| 2024-09-20 22:21:40.724 | MS1 | 121.4656714172 | 31.1446332070 | 627 | 504990 | -80.68 | 14.94 | 590.30 | 0.17 | 2.67 | 1561 |
| 2024-09-20 22:21:41.689 | MS1 | 121.4656764949 | 31.1446199962 | 627 | 504990 | -77.15 | 13.56 | 567.23 | 0.11 | 2.19 | 1565 |
| 2024-09-20 22:21:42.763 | MS1 | 121.4656741602 | 31.1446271465 | 627 | 504990 | -76.96 | 17.46 | 473.67 | 0.17 | 2.08 | 1562 |

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
| 3212776 | 2 | 121.4744171802 | 31.1479025070 | 111 | 13 | 5 | 16.8 | TDD | 627 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3216829 | 1 | 121.4651573858 | 31.1487525575 | 147 | 8 | 11 | 36.5 | TDD | 928 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3237488 | 4 | 121.4647393144 | 31.1518871278 | 138 | 2 | 3 | 49.8 | TDD | 219 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3266783 | 3 | 121.4736868806 | 31.1531394747 | 277 | 2 | 7 | 38.2 | TDD | 157 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.983 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.999 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.145 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.145 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.858 | NREventA3 | measId:2;ServCellPCI:906;Se... |
| 2024-09-20 22:21:35.858 | NREventA3 | measId:2;ServCellPCI:906;Se... |
| 2024-09-20 22:21:36.858 | NREventA3 | measId:2;ServCellPCI:906;Se... |
| 2024-09-20 22:21:39.358 | NRRRCReestablishAttempt | PCI:906 |
| 2024-09-20 22:21:39.371 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.382 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.508 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.508 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216829 | 1 | 9.8589 | 14.5990 | -116.9118 | 19.7466 | 179.6627 | 0.0034 | 0.0022 |
| 2024_09_20 22:00 | 3212776 | 2 | 17.7237 | 12.0769 | -116.9543 | 15.5396 | 198.5688 | 0.0195 | 0.1691 |
| 2024_09_20 22:00 | 3266783 | 3 | 16.2183 | 15.8112 | -116.4042 | 9.2379 | 191.8437 | 0.0096 | 0.0141 |
| 2024_09_20 22:00 | 3237488 | 4 | 7.9009 | 11.5722 | -115.2003 | 19.1923 | 162.6534 | 0.0010 | 0.0020 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415470_D8D1A5F1 | 504990 | 219 | -91.0 | 504990 | 627 | -95.1 | 504990 | 928 | -96.8 | 504990 | 157 |
| MR_1774415470_5FA72784 | 504990 | 627 | -95.7 | 504990 | 219 | -90.6 | 504990 | 928 | -96.7 | 504990 | 157 |
| MR_1774415470_F2CAD801 | 504990 | 627 | -94.1 | 504990 | 219 | -90.2 | 504990 | 928 | -98.5 | 504990 | 157 |
| MR_1774415470_F93D12D5 | 504990 | 627 | -94.1 | 504990 | 219 | -89.9 | 504990 | 928 | -95.1 | 504990 | 157 |
| MR_1774415470_518CF7EA | 504990 | 219 | -90.2 | 504990 | 627 | -94.8 | 504990 | 928 | -94.8 | 504990 | 157 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1078: `5ee3cd99-283...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5ee3cd99-2833-4a53-b04b-cdcfaa8ce637` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Add neighbor relationship between 3218751_1 and 3248390_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1078] topology](images/train_1078.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Add neighbor relationship between 3218751_1 and 3248390_4 **← 정답**
- `C3`: Decrease A3 Offset threshold for 3248390_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218751_1
- `C5`: Decrease A3 Offset threshold for 3218751_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248390_4
- `C7`: Adjust the azimuth of 3218751_1 by 50 degrees
- `C8`: Add neighbor relationship between 3218348_3 and 3248390_4
- `C9`: Increase transmission power for 3248390_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218751_1
- `C11`: Decrease transmission power for 3218751_1
- `C12`: Lift the tilt angle  of 3248390_4 by 5 degrees
- `C13`: Press down the tilt angle  of 3248390_4 by 5 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248390_4
- `C15`: Lift the tilt angle of 3218751_1 by 6 degrees
- `C16`: Decrease transmission power for 3248390_4
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase A3 Offset threshold for 3248390_4
- `C19`: Adjust the azimuth of 3248390_4 by 28 degrees
- `C20`: Increase transmission power for 3218751_1
- `C21`: Press down the tilt angle of 3218751_1 by 6 degrees
- `C22`: Increase A3 Offset threshold for 3218751_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.366 | MS1 | 121.4656646714 | 31.1446374896 | 360 | 504990 | -83.80 | 15.65 | 324.83 | 0.15 | 2.61 | 1564 |
| 2024-09-20 22:21:32.619 | MS1 | 121.4656768796 | 31.1446276731 | 360 | 504990 | -82.66 | 13.16 | 373.79 | 0.04 | 2.90 | 1595 |
| 2024-09-20 22:21:33.586 | MS1 | 121.4656773681 | 31.1446374082 | 360 | 504990 | -83.46 | 12.22 | 455.91 | 0.16 | 2.82 | 1598 |
| 2024-09-20 22:21:34.141 | MS1 | 121.4656660436 | 31.1446229584 | 360 | 504990 | -90.70 | -1.07 | 69.90 | 0.02 | 1.41 | 1581 |
| 2024-09-20 22:21:35.354 | MS1 | 121.4656668602 | 31.1446198385 | 360 | 504990 | -90.72 | -0.83 | 37.61 | 0.05 | 1.37 | 1575 |
| 2024-09-20 22:21:36.450 | MS1 | 121.4656690676 | 31.1446327045 | 360 | 504990 | -86.95 | -2.62 | 49.52 | 0.09 | 1.47 | 1575 |
| 2024-09-20 22:21:37.336 | MS1 | 121.4656631562 | 31.1446300291 | 360 | 504990 | -85.20 | -0.77 | 61.50 | 0.04 | 1.19 | 1560 |
| 2024-09-20 22:21:38.117 | MS1 | 121.4656670543 | 31.1446319670 | 360 | 504990 | -78.00 | 15.51 | 563.66 | 0.01 | 1.09 | 1583 |
| 2024-09-20 22:21:39.397 | MS1 | 121.4656631486 | 31.1446206850 | 360 | 504990 | -76.97 | 17.36 | 560.42 | 0.03 | 1.22 | 1564 |
| 2024-09-20 22:21:40.935 | MS1 | 121.4656688282 | 31.1446281954 | 360 | 504990 | -77.49 | 14.41 | 565.31 | 0.18 | 2.22 | 1593 |
| 2024-09-20 22:21:41.858 | MS1 | 121.4656710202 | 31.1446326064 | 360 | 504990 | -82.16 | 13.18 | 443.72 | 0.03 | 2.93 | 1593 |
| 2024-09-20 22:21:42.847 | MS1 | 121.4656638903 | 31.1446365334 | 360 | 504990 | -75.76 | 17.63 | 521.22 | 0.05 | 2.76 | 1578 |

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
| 3217731 | 2 | 121.4734833495 | 31.1450504669 | 111 | 13 | 6 | 41.9 | TDD | 690 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3218348 | 3 | 121.4680724007 | 31.1543478003 | 76 | 1 | 0 | 21.4 | TDD | 619 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3218751 | 1 | 121.4741218321 | 31.1557865765 | 304 | 5 | 10 | 15.8 | TDD | 360 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3248390 | 4 | 121.4671978014 | 31.1492463926 | 168 | 1 | 7 | 33.5 | TDD | 773 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.811 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.827 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:30.977 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.977 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.611 | NREventA3 | measId:2;ServCellPCI:164;Se... |
| 2024-09-20 22:21:35.611 | NREventA3 | measId:2;ServCellPCI:164;Se... |
| 2024-09-20 22:21:36.611 | NREventA3 | measId:2;ServCellPCI:164;Se... |
| 2024-09-20 22:21:39.111 | NRRRCReestablishAttempt | PCI:164 |
| 2024-09-20 22:21:39.127 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.141 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.269 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.269 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218751 | 1 | 10.4957 | 12.4751 | -117.8714 | 5.4996 | 167.9384 | 0.0120 | 0.1159 |
| 2024_09_20 22:00 | 3217731 | 2 | 16.0199 | 18.0568 | -114.6851 | 14.7650 | 119.5597 | 0.0128 | 0.0088 |
| 2024_09_20 22:00 | 3218348 | 3 | 10.3931 | 8.8634 | -114.7677 | 16.0764 | 138.6027 | 0.0072 | 0.0133 |
| 2024_09_20 22:00 | 3248390 | 4 | 14.6942 | 9.6521 | -115.9116 | 6.3789 | 187.0938 | 0.0178 | 0.0023 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414589_8C0BB1ED | 504990 | 360 | -91.0 | 504990 | 773 | -84.7 | 504990 | 619 | -84.2 | 504990 | 690 |
| MR_1774414589_EA71B86B | 504990 | 360 | -89.2 | 504990 | 773 | -85.0 | 504990 | 619 | -86.9 | 504990 | 690 |
| MR_1774414589_0EF78AC1 | 504990 | 773 | -86.8 | 504990 | 360 | -90.9 | 504990 | 619 | -86.4 | 504990 | 690 |
| MR_1774414589_20664DB1 | 504990 | 360 | -90.5 | 504990 | 773 | -85.9 | 504990 | 619 | -84.6 | 504990 | 690 |
| MR_1774414589_9DDB2F14 | 504990 | 360 | -90.8 | 504990 | 773 | -85.0 | 504990 | 619 | -84.9 | 504990 | 690 |
| MR_1774414589_49BEDA7E | 504990 | 360 | -92.5 | 504990 | 773 | -87.1 | 504990 | 619 | -88.1 | 504990 | 690 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1079: `69a595d3-fad...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `69a595d3-fad2-4886-aa24-c42a18d85c87` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Lift the tilt angle  of 3220960_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1079] topology](images/train_1079.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3240172_4
- `C2`: Lift the tilt angle  of 3220960_1 by 10 degrees **← 정답**
- `C3`: Check test server and transmission issues
- `C4`: Increase A3 Offset threshold for 3240203_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240203_3
- `C6`: Press down the tilt angle  of 3220960_1 by 10 degrees
- `C7`: Decrease A3 Offset threshold for 3240172_4
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase transmission power for 3240203_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240172_4
- `C11`: Decrease transmission power for 3240172_4
- `C12`: Decrease transmission power for 3240203_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240203_3
- `C14`: Decrease A3 Offset threshold for 3240203_3
- `C15`: Adjust the azimuth of 3220960_1 by 20 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240172_4
- `C17`: Increase transmission power for 3240172_4
- `C18`: Press down the tilt angle of 3240172_4 by 3 degrees
- `C19`: Add neighbor relationship between 3220960_1 and 3240203_3
- `C20`: Add neighbor relationship between 3240172_4 and 3240203_3
- `C21`: Lift the tilt angle of 3240172_4 by 3 degrees
- `C22`: Adjust the azimuth of 3240172_4 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.831 | MS1 | 121.4656688108 | 31.1446312013 | 971 | 504990 | -88.18 | 12.60 | 417.56 | 0.03 | 2.78 | 1578 |
| 2024-09-20 22:21:32.448 | MS1 | 121.4656661339 | 31.1446221033 | 971 | 504990 | -87.97 | 15.42 | 433.66 | 0.03 | 2.09 | 1564 |
| 2024-09-20 22:21:33.725 | MS1 | 121.4656642749 | 31.1446294885 | 971 | 504990 | -90.53 | 13.77 | 515.28 | 0.17 | 2.50 | 1568 |
| 2024-09-20 22:21:34.225 | MS1 | 121.4656621542 | 31.1446252039 | 971 | 504990 | -85.36 | 16.44 | 80.52 | 0.13 | 2.95 | 1561 |
| 2024-09-20 22:21:35.771 | MS1 | 121.4656680681 | 31.1446320545 | 971 | 504990 | -87.26 | 16.77 | 70.37 | 0.08 | 2.39 | 1586 |
| 2024-09-20 22:21:36.343 | MS1 | 121.4656674966 | 31.1446311590 | 971 | 504990 | -89.89 | 13.66 | 45.98 | 0.07 | 2.16 | 1577 |
| 2024-09-20 22:21:37.364 | MS1 | 121.4656676010 | 31.1446361033 | 971 | 504990 | -93.14 | 10.45 | 64.10 | 0.17 | 2.33 | 1592 |
| 2024-09-20 22:21:38.702 | MS1 | 121.4656669438 | 31.1446181829 | 971 | 504990 | -90.61 | 9.58 | 87.75 | 0.01 | 2.40 | 1595 |
| 2024-09-20 22:21:39.414 | MS1 | 121.4656688226 | 31.1446311004 | 971 | 504990 | -93.27 | 8.69 | 74.57 | 0.04 | 2.73 | 1570 |
| 2024-09-20 22:21:40.392 | MS1 | 121.4656740514 | 31.1446230471 | 971 | 504990 | -92.64 | 12.59 | 411.19 | 0.10 | 2.11 | 1589 |
| 2024-09-20 22:21:41.206 | MS1 | 121.4656602562 | 31.1446244796 | 971 | 504990 | -91.84 | 12.68 | 446.09 | 0.07 | 2.94 | 1572 |
| 2024-09-20 22:21:42.227 | MS1 | 121.4656597959 | 31.1446323080 | 971 | 504990 | -90.13 | 7.47 | 320.36 | 0.17 | 2.11 | 1581 |

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
| 3220960 | 1 | 121.4658926171 | 31.1532588387 | 14 | 9 | 4 | 25.2 | TDD | 521 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3222198 | 2 | 121.4653482521 | 31.1460219176 | 292 | 7 | 4 | 34.1 | TDD | 787 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3240172 | 4 | 121.4747091456 | 31.1486193284 | 238 | 1 | 11 | 27.6 | TDD | 971 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3240203 | 3 | 121.4744966532 | 31.1500143292 | 215 | 14 | 1 | 48.7 | TDD | 476 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.113 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.138 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.281 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.281 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.927 | NREventA3 | measId:2;ServCellPCI:950;Se... |
| 2024-09-20 22:21:38.167 | NRHandoverAttempt | SourcePCI:950;SourceNR-ARFC... |
| 2024-09-20 22:21:38.213 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.226 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.367 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.367 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220960 | 1 | 15.1472 | 13.5769 | -117.9540 | 12.0769 | 112.4248 | 0.0127 | 0.0015 |
| 2024_09_20 22:00 | 3222198 | 2 | 9.0203 | 17.6599 | -115.3527 | 9.3399 | 138.4162 | 0.0004 | 0.0073 |
| 2024_09_20 22:00 | 3240203 | 3 | 13.9587 | 10.9430 | -117.6050 | 7.7822 | 179.2344 | 0.0154 | 0.0146 |
| 2024_09_20 22:00 | 3240172 | 4 | 78.4104 | 89.5739 | -114.5956 | 6.5613 | 90.8176 | 0.0117 | 0.0040 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416894_FA8D28F3 | 504990 | 971 | -86.0 | 504990 | 476 | -91.5 | 504990 | 521 | -92.3 | 504990 | 787 |
| MR_1774416894_936CCFBF | 504990 | 971 | -84.5 | 504990 | 476 | -93.3 | 504990 | 521 | -94.3 | 504990 | 787 |
| MR_1774416894_00141FD3 | 504990 | 971 | -83.6 | 504990 | 476 | -94.0 | 504990 | 521 | -93.1 | 504990 | 787 |
| MR_1774416894_BD4F192B | 504990 | 971 | -84.2 | 504990 | 476 | -91.8 | 504990 | 521 | -91.9 | 504990 | 787 |
| MR_1774416894_6A8BC76D | 504990 | 971 | -85.0 | 504990 | 476 | -93.0 | 504990 | 521 | -91.2 | 504990 | 787 |

> *... 2개 열 생략 (전체 14열)*

---
