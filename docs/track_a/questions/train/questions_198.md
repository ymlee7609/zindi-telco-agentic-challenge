# Track A 문제 분석 — train[1970]~train[1979]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1970] ~ train[1979] (10개)

## 목차

1. [문제 1970: `4c2ef240-f68...`](#1970) — single-answer, 정답: C9
2. [문제 1971: `c3233313-4c0...`](#1971) — single-answer, 정답: C1
3. [문제 1972: `8adfa00f-eeb...`](#1972) — single-answer, 정답: C12
4. [문제 1973: `20b376e2-7bc...`](#1973) — multiple-answer, 정답: C11|C20
5. [문제 1974: `81f5276f-89b...`](#1974) — single-answer, 정답: C12
6. [문제 1975: `5d95f909-efe...`](#1975) — single-answer, 정답: C15
7. [문제 1976: `1fe89358-b65...`](#1976) — multiple-answer, 정답: C19|C22
8. [문제 1977: `1308e70d-6a2...`](#1977) — single-answer, 정답: C17
9. [문제 1978: `3d452697-9a0...`](#1978) — single-answer, 정답: C10
10. [문제 1979: `da07052d-1ee...`](#1979) — single-answer, 정답: C7

---

### 문제 1970: `4c2ef240-f68...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4c2ef240-f684-4bda-adec-fe6196d6d270` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Lift the tilt angle  of 3229332_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1970] topology](images/train_1970.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3229332_1 and 3261650_3
- `C2`: Add neighbor relationship between 3249539_2 and 3261650_3
- `C3`: Check test server and transmission issues
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249539_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261650_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249539_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Adjust the azimuth of 3249539_2 by 16 degrees
- `C9`: Lift the tilt angle  of 3229332_1 by 10 degrees **← 정답**
- `C10`: Decrease transmission power for 3249539_2
- `C11`: Increase transmission power for 3249539_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261650_3
- `C13`: Press down the tilt angle  of 3229332_1 by 10 degrees
- `C14`: Decrease transmission power for 3261650_3
- `C15`: Decrease A3 Offset threshold for 3249539_2
- `C16`: Increase A3 Offset threshold for 3261650_3
- `C17`: Press down the tilt angle of 3249539_2 by 5 degrees
- `C18`: Lift the tilt angle of 3249539_2 by 5 degrees
- `C19`: Decrease A3 Offset threshold for 3261650_3
- `C20`: Adjust the azimuth of 3229332_1 by 45 degrees
- `C21`: Increase transmission power for 3261650_3
- `C22`: Increase A3 Offset threshold for 3249539_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.887 | MS1 | 121.4656662325 | 31.1446362760 | 827 | 504990 | -85.44 | 13.76 | 312.77 | 0.03 | 2.76 | 1580 |
| 2024-09-20 22:21:32.353 | MS1 | 121.4656707741 | 31.1446267033 | 827 | 504990 | -90.66 | 16.54 | 532.22 | 0.18 | 2.76 | 1593 |
| 2024-09-20 22:21:33.644 | MS1 | 121.4656649515 | 31.1446346208 | 827 | 504990 | -89.36 | 16.70 | 384.29 | 0.05 | 2.07 | 1586 |
| 2024-09-20 22:21:34.326 | MS1 | 121.4656625074 | 31.1446272799 | 827 | 504990 | -86.71 | 14.58 | 62.86 | 0.17 | 2.29 | 1584 |
| 2024-09-20 22:21:35.349 | MS1 | 121.4656733963 | 31.1446335705 | 827 | 504990 | -87.61 | 14.53 | 69.11 | 0.11 | 2.94 | 1568 |
| 2024-09-20 22:21:36.296 | MS1 | 121.4656669003 | 31.1446313294 | 827 | 504990 | -86.97 | 12.51 | 57.60 | 0.14 | 2.99 | 1561 |
| 2024-09-20 22:21:37.537 | MS1 | 121.4656685199 | 31.1446245808 | 827 | 504990 | -90.43 | 7.16 | 61.72 | 0.16 | 2.32 | 1597 |
| 2024-09-20 22:21:38.617 | MS1 | 121.4656726415 | 31.1446341885 | 827 | 504990 | -92.11 | 9.93 | 86.46 | 0.02 | 2.23 | 1575 |
| 2024-09-20 22:21:39.284 | MS1 | 121.4656763459 | 31.1446346004 | 827 | 504990 | -91.68 | 11.77 | 93.33 | 0.09 | 2.17 | 1577 |
| 2024-09-20 22:21:40.928 | MS1 | 121.4656692079 | 31.1446328836 | 827 | 504990 | -91.33 | 9.09 | 332.01 | 0.03 | 2.96 | 1592 |
| 2024-09-20 22:21:41.896 | MS1 | 121.4656749752 | 31.1446211461 | 827 | 504990 | -89.14 | 7.53 | 419.98 | 0.07 | 2.53 | 1590 |
| 2024-09-20 22:21:42.666 | MS1 | 121.4656636253 | 31.1446279688 | 827 | 504990 | -89.99 | 12.20 | 365.60 | 0.09 | 2.22 | 1581 |

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
| 3229332 | 1 | 121.4751638612 | 31.1480189117 | 313 | 6 | 4 | 16.6 | TDD | 657 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3249539 | 2 | 121.4730432191 | 31.1541878131 | 197 | 3 | 10 | 46.2 | TDD | 827 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3261650 | 3 | 121.4649299726 | 31.1486467476 | 216 | 11 | 2 | 39.7 | TDD | 758 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3276086 | 4 | 121.4705005937 | 31.1470487242 | 253 | 7 | 6 | 25.6 | TDD | 715 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.963 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.985 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.111 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.111 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.791 | NREventA3 | measId:2;ServCellPCI:640;Se... |
| 2024-09-20 22:21:38.031 | NRHandoverAttempt | SourcePCI:640;SourceNR-ARFC... |
| 2024-09-20 22:21:38.069 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.079 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.179 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.179 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229332 | 1 | 5.4566 | 18.4285 | -114.8468 | 6.7678 | 153.3035 | 0.0197 | 0.0049 |
| 2024_09_20 22:00 | 3249539 | 2 | 93.3011 | 91.2550 | -116.9004 | 11.0269 | 188.2059 | 0.0118 | 0.0024 |
| 2024_09_20 22:00 | 3261650 | 3 | 10.6819 | 19.5400 | -116.5625 | 9.4499 | 123.7654 | 0.0097 | 0.0015 |
| 2024_09_20 22:00 | 3276086 | 4 | 9.8650 | 10.0395 | -114.1522 | 6.1511 | 173.8982 | 0.0038 | 0.0011 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414923_1B2FE20D | 504990 | 827 | -84.9 | 504990 | 758 | -88.4 | 504990 | 657 | -96.5 | 504990 | 715 |
| MR_1774414923_01AEACC3 | 504990 | 827 | -86.7 | 504990 | 758 | -87.4 | 504990 | 657 | -95.2 | 504990 | 715 |
| MR_1774414923_8E0F7E50 | 504990 | 827 | -85.5 | 504990 | 758 | -87.5 | 504990 | 657 | -94.3 | 504990 | 715 |
| MR_1774414923_B48D3987 | 504990 | 827 | -86.2 | 504990 | 758 | -89.9 | 504990 | 657 | -96.8 | 504990 | 715 |
| MR_1774414923_EFEAE17D | 504990 | 827 | -87.2 | 504990 | 758 | -90.0 | 504990 | 657 | -95.5 | 504990 | 715 |
| MR_1774414923_6166FC97 | 504990 | 827 | -88.3 | 504990 | 758 | -89.1 | 504990 | 657 | -94.4 | 504990 | 715 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1971: `c3233313-4c0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c3233313-4c0a-4049-84e4-9bda7aec1a95` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Lift the tilt angle  of 3224288_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1971] topology](images/train_1971.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3224288_3 by 10 degrees **← 정답**
- `C2`: Adjust the azimuth of 3224288_3 by 50 degrees
- `C3`: Decrease A3 Offset threshold for 3231579_4
- `C4`: Increase transmission power for 3231579_4
- `C5`: Increase A3 Offset threshold for 3231579_4
- `C6`: Press down the tilt angle of 3247294_2 by 3 degrees
- `C7`: Check test server and transmission issues
- `C8`: Adjust the azimuth of 3247294_2 by 43 degrees
- `C9`: Increase A3 Offset threshold for 3247294_2
- `C10`: Add neighbor relationship between 3224288_3 and 3231579_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247294_2
- `C12`: Decrease transmission power for 3231579_4
- `C13`: Decrease transmission power for 3247294_2
- `C14`: Increase transmission power for 3247294_2
- `C15`: Decrease A3 Offset threshold for 3247294_2
- `C16`: Press down the tilt angle  of 3224288_3 by 10 degrees
- `C17`: Add neighbor relationship between 3247294_2 and 3231579_4
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231579_4
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247294_2
- `C21`: Lift the tilt angle of 3247294_2 by 3 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231579_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.488 | MS1 | 121.4656704567 | 31.1446241208 | 418 | 504990 | -85.62 | 16.35 | 535.55 | 0.06 | 2.53 | 1561 |
| 2024-09-20 22:21:32.552 | MS1 | 121.4656615149 | 31.1446308740 | 418 | 504990 | -89.80 | 15.59 | 511.51 | 0.16 | 2.00 | 1567 |
| 2024-09-20 22:21:33.203 | MS1 | 121.4656740713 | 31.1446256110 | 418 | 504990 | -88.38 | 13.17 | 395.28 | 0.15 | 2.98 | 1563 |
| 2024-09-20 22:21:34.465 | MS1 | 121.4656591202 | 31.1446332549 | 418 | 504990 | -88.55 | 16.90 | 77.63 | 0.01 | 2.20 | 1570 |
| 2024-09-20 22:21:35.107 | MS1 | 121.4656598477 | 31.1446213820 | 418 | 504990 | -87.30 | 17.65 | 57.86 | 0.01 | 2.22 | 1584 |
| 2024-09-20 22:21:36.552 | MS1 | 121.4656731481 | 31.1446228947 | 418 | 504990 | -85.63 | 12.37 | 66.65 | 0.05 | 2.52 | 1570 |
| 2024-09-20 22:21:37.698 | MS1 | 121.4656646705 | 31.1446293177 | 418 | 504990 | -89.99 | 12.90 | 67.19 | 0.08 | 2.08 | 1561 |
| 2024-09-20 22:21:38.732 | MS1 | 121.4656590214 | 31.1446273403 | 418 | 504990 | -93.33 | 8.77 | 61.35 | 0.00 | 2.74 | 1579 |
| 2024-09-20 22:21:39.285 | MS1 | 121.4656655874 | 31.1446262195 | 418 | 504990 | -93.35 | 11.28 | 92.24 | 0.06 | 2.97 | 1585 |
| 2024-09-20 22:21:40.968 | MS1 | 121.4656677740 | 31.1446290923 | 418 | 504990 | -92.32 | 7.39 | 340.67 | 0.01 | 2.48 | 1587 |
| 2024-09-20 22:21:41.158 | MS1 | 121.4656595811 | 31.1446245960 | 418 | 504990 | -93.81 | 7.12 | 498.25 | 0.02 | 2.46 | 1560 |
| 2024-09-20 22:21:42.404 | MS1 | 121.4656727176 | 31.1446373604 | 418 | 504990 | -92.20 | 8.35 | 454.98 | 0.02 | 2.38 | 1572 |

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
| 3224288 | 3 | 121.4663295515 | 31.1544459920 | 10 | 10 | 12 | 47.2 | TDD | 315 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3231579 | 4 | 121.4682171403 | 31.1474475877 | 68 | 9 | 10 | 18.3 | TDD | 719 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3247294 | 2 | 121.4739145248 | 31.1542718371 | 173 | 2 | 9 | 28.5 | TDD | 418 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3254305 | 1 | 121.4711935996 | 31.1550910965 | 180 | 3 | 5 | 20.1 | TDD | 193 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.509 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.645 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.645 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.317 | NREventA3 | measId:2;ServCellPCI:116;Se... |
| 2024-09-20 22:21:38.557 | NRHandoverAttempt | SourcePCI:116;SourceNR-ARFC... |
| 2024-09-20 22:21:38.602 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.613 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.749 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.749 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254305 | 1 | 16.2353 | 16.8934 | -114.7259 | 10.3381 | 147.1694 | 0.0013 | 0.0182 |
| 2024_09_20 22:00 | 3247294 | 2 | 85.0121 | 86.8532 | -114.7171 | 8.0909 | 109.7262 | 0.0027 | 0.0033 |
| 2024_09_20 22:00 | 3224288 | 3 | 19.2326 | 7.9613 | -115.5004 | 14.5224 | 162.4832 | 0.0049 | 0.0001 |
| 2024_09_20 22:00 | 3231579 | 4 | 19.4933 | 6.9679 | -114.6750 | 15.6093 | 195.4607 | 0.0129 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414558_6BDDBFE1 | 504990 | 418 | -87.6 | 504990 | 719 | -87.7 | 504990 | 315 | -95.5 | 504990 | 193 |
| MR_1774414558_1D0F2DCF | 504990 | 418 | -90.2 | 504990 | 719 | -88.8 | 504990 | 315 | -93.2 | 504990 | 193 |
| MR_1774414558_0ADAF484 | 504990 | 418 | -89.6 | 504990 | 719 | -88.2 | 504990 | 315 | -94.4 | 504990 | 193 |
| MR_1774414558_EA5DA538 | 504990 | 418 | -86.8 | 504990 | 719 | -89.8 | 504990 | 315 | -93.6 | 504990 | 193 |
| MR_1774414558_B17E0845 | 504990 | 418 | -88.6 | 504990 | 719 | -90.3 | 504990 | 315 | -93.2 | 504990 | 193 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1972: `8adfa00f-eeb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8adfa00f-eeb5-4c36-8b9a-391b33bbe0a9` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271144_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1972] topology](images/train_1972.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3271144_1 by 1 degrees
- `C2`: Lift the tilt angle of 3271144_1 by 1 degrees
- `C3`: Adjust the azimuth of 3215948_6 by 33 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215948_6
- `C5`: Decrease A3 Offset threshold for 3271144_1
- `C6`: Adjust the azimuth of 3271144_1 by 37 degrees
- `C7`: Increase A3 Offset threshold for 3271144_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Lift the tilt angle  of 3215948_6 by 3 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271144_1
- `C11`: Increase A3 Offset threshold for 3215948_6
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271144_1 **← 정답**
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215948_6
- `C14`: Increase transmission power for 3215948_6
- `C15`: Press down the tilt angle  of 3215948_6 by 3 degrees
- `C16`: Add neighbor relationship between 3222817_8 and 3215948_6
- `C17`: Decrease transmission power for 3271144_1
- `C18`: Decrease transmission power for 3215948_6
- `C19`: Increase transmission power for 3271144_1
- `C20`: Check test server and transmission issues
- `C21`: Decrease A3 Offset threshold for 3215948_6
- `C22`: Add neighbor relationship between 3271144_1 and 3215948_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.137 | MS1 | 121.4656697149 | 31.1446233761 | 550 | 504990 | -95.10 | 11.20 | 415.35 | 0.00 | 2.25 | 1577 |
| 2024-09-20 22:21:32.664 | MS1 | 121.4656666944 | 31.1446281501 | 679 | 504990 | -93.84 | 13.57 | 316.54 | 0.12 | 2.82 | 1587 |
| 2024-09-20 22:21:33.896 | MS1 | 121.4656606585 | 31.1446323873 | 107 | 504990 | -94.14 | 10.45 | 328.41 | 0.06 | 2.04 | 1569 |
| 2024-09-20 22:21:34.798 | MS1 | 121.4656745323 | 31.1446186660 | 261 | 152650 | -95.87 | 4.27 | 106.50 | 0.01 | 1.98 | 917 |
| 2024-09-20 22:21:35.857 | MS1 | 121.4656583475 | 31.1446369275 | 170 | 152650 | -94.85 | 5.05 | 49.78 | 0.05 | 1.68 | 962 |
| 2024-09-20 22:21:36.618 | MS1 | 121.4656595648 | 31.1446181049 | 132 | 152650 | -89.69 | 2.87 | 96.39 | 0.01 | 1.67 | 1000 |
| 2024-09-20 22:21:37.575 | MS1 | 121.4656753405 | 31.1446232544 | 200 | 152650 | -87.94 | 2.36 | 59.33 | 0.08 | 1.92 | 908 |
| 2024-09-20 22:21:38.700 | MS1 | 121.4656599272 | 31.1446328597 | 261 | 152650 | -95.97 | 2.91 | 60.87 | 0.16 | 1.60 | 981 |
| 2024-09-20 22:21:39.975 | MS1 | 121.4656588059 | 31.1446342197 | 170 | 152650 | -96.12 | 5.72 | 98.21 | 0.16 | 1.59 | 956 |
| 2024-09-20 22:21:40.389 | MS1 | 121.4656586865 | 31.1446313483 | 132 | 152650 | -88.80 | 7.74 | 61.05 | 0.07 | 2.20 | 1573 |
| 2024-09-20 22:21:41.626 | MS1 | 121.4656662405 | 31.1446311244 | 200 | 152650 | -90.99 | 6.49 | 54.28 | 0.15 | 2.06 | 1585 |
| 2024-09-20 22:21:42.770 | MS1 | 121.4656633184 | 31.1446376585 | 261 | 152650 | -88.52 | 6.17 | 91.45 | 0.14 | 2.98 | 1587 |

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
| 3215645 | 5 | 121.4756952473 | 31.1460670587 | 243 | 10 | 4 | 13.5 | TDD | 398 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3215948 | 6 | 121.4720304263 | 31.1475933677 | 209 | 3 | 7 | 3.6 | TDD | 955 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3216605 | 11 | 121.4662280164 | 31.1496577634 | 345 | 0 | 11 | 29.2 | FDD | 200 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3220683 | 10 | 121.4681458138 | 31.1530339241 | 163 | 0 | 10 | 9.0 | FDD | 551 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3222817 | 8 | 121.4674140882 | 31.1459607155 | 234 | 3 | 5 | 1.1 | FDD | 132 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3226185 | 3 | 121.4686687451 | 31.1474407334 | 257 | 7 | 0 | 23.5 | TDD | 107 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3228168 | 12 | 121.4673155140 | 31.1510121930 | 169 | 12 | 1 | 24.1 | FDD | 170 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3232229 | 13 | 121.4717547497 | 31.1460911045 | 94 | 12 | 1 | 6.0 | FDD | 180 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3233638 | 9 | 121.4730047186 | 31.1511420892 | 90 | 8 | 5 | 16.9 | FDD | 261 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3233655 | 7 | 121.4695936150 | 31.1448302164 | 333 | 4 | 12 | 29.9 | FDD | 385 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3239881 | 4 | 121.4649132310 | 31.1554657778 | 145 | 4 | 0 | 8.1 | TDD | 333 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3253115 | 2 | 121.4686305266 | 31.1468385476 | 99 | 11 | 10 | 8.0 | TDD | 679 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3271144 | 1 | 121.4752774917 | 31.1442158095 | 310 | 0 | 5 | 10.6 | TDD | 550 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.567 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.592 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.733 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.733 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.401 | NREventA2 | measId:1;ServCellPCI:819;Se... |
| 2024-09-20 22:21:35.540 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.758 | NREventA5 | measId:3;ServCellPCI:819;Se... |
| 2024-09-20 22:21:35.821 | NRHandoverAttempt | SourcePCI:819;SourceNR-ARFC... |
| 2024-09-20 22:21:35.859 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.874 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.006 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.006 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271144 | 1 | 15.0584 | 7.4196 | -116.8187 | 19.0618 | 159.7938 | 0.0036 | 0.0172 |
| 2024_09_20 22:00 | 3253115 | 2 | 6.9279 | 18.8537 | -114.0451 | 11.3834 | 166.7563 | 0.0020 | 0.0162 |
| 2024_09_20 22:00 | 3226185 | 3 | 19.2783 | 14.7913 | -117.9263 | 9.6720 | 180.2330 | 0.0074 | 0.0090 |
| 2024_09_20 22:00 | 3239881 | 4 | 9.2638 | 16.1800 | -115.1364 | 10.8755 | 150.7864 | 0.0083 | 0.0173 |
| 2024_09_20 22:00 | 3215645 | 5 | 14.1469 | 12.2378 | -114.6993 | 10.8848 | 178.5741 | 0.0165 | 0.0136 |
| 2024_09_20 22:00 | 3215948 | 6 | 13.6083 | 13.1426 | -116.7397 | 18.6029 | 85.0655 | 0.0046 | 0.0105 |
| 2024_09_20 22:00 | 3233655 | 7 | 9.8763 | 9.1687 | -115.1038 | 3.7052 | 48.4577 | 0.0131 | 0.0163 |
| 2024_09_20 22:00 | 3222817 | 8 | 18.8063 | 8.3986 | -117.7742 | 3.0135 | 44.8878 | 0.0022 | 0.0076 |
| 2024_09_20 22:00 | 3233638 | 9 | 19.6099 | 5.2304 | -116.7126 | 4.7309 | 25.7059 | 0.0191 | 0.0019 |
| 2024_09_20 22:00 | 3220683 | 10 | 13.6183 | 5.4862 | -114.4461 | 3.0875 | 21.4208 | 0.0115 | 0.0172 |
| 2024_09_20 22:00 | 3216605 | 11 | 8.1466 | 18.1534 | -114.6844 | 3.7039 | 41.3047 | 0.0067 | 0.0039 |
| 2024_09_20 22:00 | 3228168 | 12 | 9.3132 | 13.2693 | -117.6167 | 3.4038 | 30.5826 | 0.0078 | 0.0026 |
| 2024_09_20 22:00 | 3232229 | 13 | 16.5793 | 14.5109 | -114.3680 | 3.7174 | 55.7980 | 0.0051 | 0.0059 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415360_ABCF42D7 | 504990 | 107 | -92.4 | 504990 | 955 | -94.5 | 504990 | 398 | -97.9 | 504990 | 333 |
| MR_1774415360_D1F832D5 | 504990 | 107 | -95.7 | 504990 | 955 | -91.2 | 504990 | 398 | -98.4 | 504990 | 333 |
| MR_1774415360_7AB1072F | 504990 | 107 | -95.9 | 504990 | 955 | -92.1 | 504990 | 398 | -99.0 | 504990 | 333 |
| MR_1774415360_25495203 | 504990 | 107 | -93.6 | 504990 | 955 | -91.2 | 504990 | 398 | -99.3 | 504990 | 333 |
| MR_1774415360_366E2F2D | 504990 | 107 | -95.3 | 504990 | 955 | -94.7 | 504990 | 398 | -98.6 | 504990 | 333 |
| MR_1774415360_161C53A6 | 504990 | 107 | -94.5 | 504990 | 955 | -91.6 | 504990 | 398 | -100.0 | 504990 | 333 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1973: `20b376e2-7bc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `20b376e2-7bcd-4655-bd5c-59b01bf5a98a` |
| Tag | **multiple-answer** |
| 정답 | **C11|C20** |
| C11 의미 | Decrease transmission power for 3230412_1 |
| C20 의미 | Press down the tilt angle  of 3230412_1 by 5 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1973] topology](images/train_1973.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Increase transmission power for 3230412_1
- `C3`: Lift the tilt angle of 3234378_4 by 1 degrees
- `C4`: Adjust the azimuth of 3234378_4 by 23 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230412_1
- `C6`: Lift the tilt angle  of 3230412_1 by 5 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234378_4
- `C9`: Decrease transmission power for 3234378_4
- `C10`: Increase A3 Offset threshold for 3230412_1
- `C11`: Decrease transmission power for 3230412_1 **← 정답**
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234378_4
- `C13`: Adjust the azimuth of 3230412_1 by 28 degrees
- `C14`: Increase A3 Offset threshold for 3234378_4
- `C15`: Press down the tilt angle of 3234378_4 by 1 degrees
- `C16`: Add neighbor relationship between 3234378_4 and 3230412_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230412_1
- `C18`: Decrease A3 Offset threshold for 3234378_4
- `C19`: Increase transmission power for 3234378_4
- `C20`: Press down the tilt angle  of 3230412_1 by 5 degrees **← 정답**
- `C21`: Decrease A3 Offset threshold for 3230412_1
- `C22`: Add neighbor relationship between 3271734_2 and 3230412_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.807 | MS1 | 121.4656656243 | 31.1446180566 | 647 | 504990 | -79.50 | 12.55 | 326.13 | 0.17 | 2.48 | 1575 |
| 2024-09-20 22:21:32.526 | MS1 | 121.4656677837 | 31.1446239344 | 647 | 504990 | -84.03 | 15.42 | 430.62 | 0.19 | 2.27 | 1590 |
| 2024-09-20 22:21:33.306 | MS1 | 121.4656740092 | 31.1446202383 | 647 | 504990 | -82.62 | 16.14 | 418.04 | 0.09 | 2.60 | 1582 |
| 2024-09-20 22:21:34.969 | MS1 | 121.4656702740 | 31.1446183802 | 647 | 504990 | -88.50 | 3.94 | 56.11 | 0.00 | 1.31 | 1591 |
| 2024-09-20 22:21:35.283 | MS1 | 121.4656614764 | 31.1446212914 | 647 | 504990 | -93.87 | 2.41 | 50.02 | 0.06 | 1.34 | 1579 |
| 2024-09-20 22:21:36.394 | MS1 | 121.4656689709 | 31.1446225149 | 647 | 504990 | -91.15 | 3.27 | 63.88 | 0.03 | 1.04 | 1567 |
| 2024-09-20 22:21:37.696 | MS1 | 121.4656691040 | 31.1446193640 | 647 | 504990 | -93.57 | 1.86 | 92.97 | 0.19 | 1.08 | 1587 |
| 2024-09-20 22:21:38.799 | MS1 | 121.4656760241 | 31.1446246613 | 647 | 504990 | -88.81 | 2.29 | 59.34 | 0.12 | 1.44 | 1572 |
| 2024-09-20 22:21:39.142 | MS1 | 121.4656592093 | 31.1446187709 | 647 | 504990 | -93.03 | 1.06 | 48.21 | 0.01 | 1.39 | 1584 |
| 2024-09-20 22:21:40.278 | MS1 | 121.4656659791 | 31.1446218516 | 647 | 504990 | -79.21 | 16.56 | 297.92 | 0.04 | 2.69 | 1582 |
| 2024-09-20 22:21:41.922 | MS1 | 121.4656722061 | 31.1446288874 | 647 | 504990 | -80.62 | 13.90 | 401.84 | 0.12 | 2.18 | 1593 |
| 2024-09-20 22:21:42.116 | MS1 | 121.4656691242 | 31.1446317306 | 647 | 504990 | -79.24 | 14.74 | 543.02 | 0.06 | 2.38 | 1593 |

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
| 3230412 | 1 | 121.4643353299 | 31.1502959705 | 141 | 3 | 11 | 22.2 | TDD | 105 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3234378 | 4 | 121.4707307523 | 31.1501738108 | 195 | 0 | 7 | 17.7 | TDD | 647 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3259954 | 3 | 121.4674708207 | 31.1454123840 | 190 | 12 | 3 | 38.6 | TDD | 125 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3271734 | 2 | 121.4698406872 | 31.1538031417 | 249 | 14 | 8 | 30.5 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.399 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.422 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.528 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.528 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230412 | 1 | 19.9800 | 13.8484 | -115.8768 | 10.0127 | 157.0400 | 0.0187 | 0.0088 |
| 2024_09_20 22:00 | 3271734 | 2 | 11.9697 | 14.3104 | -117.6421 | 14.7326 | 116.4592 | 0.0053 | 0.0063 |
| 2024_09_20 22:00 | 3259954 | 3 | 6.5467 | 13.3916 | -117.0047 | 8.4846 | 94.7513 | 0.0065 | 0.0005 |
| 2024_09_20 22:00 | 3234378 | 4 | 18.9774 | 19.7103 | -108.5665 | 10.6444 | 126.5360 | 0.0068 | 0.0034 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414006_D70FD635 | 504990 | 647 | -89.3 | 504990 | 105 | -87.0 | 504990 | 441 | -91.3 | 504990 | 125 |
| MR_1774414006_88AF9C60 | 504990 | 105 | -87.5 | 504990 | 647 | -84.9 | 504990 | 441 | -91.8 | 504990 | 125 |
| MR_1774414006_639DF1F0 | 504990 | 105 | -87.5 | 504990 | 647 | -87.6 | 504990 | 441 | -92.5 | 504990 | 125 |
| MR_1774414006_5505D052 | 504990 | 647 | -88.1 | 504990 | 105 | -87.6 | 504990 | 441 | -91.2 | 504990 | 125 |
| MR_1774414006_8C673630 | 504990 | 647 | -86.8 | 504990 | 105 | -83.9 | 504990 | 441 | -90.4 | 504990 | 125 |
| MR_1774414006_967AD1ED | 504990 | 647 | -89.4 | 504990 | 105 | -86.8 | 504990 | 441 | -89.5 | 504990 | 125 |
| MR_1774414006_803DB6A9 | 504990 | 105 | -88.7 | 504990 | 647 | -84.1 | 504990 | 441 | -92.6 | 504990 | 125 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1974: `81f5276f-89b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `81f5276f-89b1-49bb-9132-c1cff483450a` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Lift the tilt angle  of 3258467_1 by 9 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1974] topology](images/train_1974.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3258467_1 by 9 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271685_3
- `C4`: Decrease A3 Offset threshold for 3264760_4
- `C5`: Press down the tilt angle of 3264760_4 by 2 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264760_4
- `C7`: Check test server and transmission issues
- `C8`: Decrease transmission power for 3264760_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271685_3
- `C10`: Add neighbor relationship between 3264760_4 and 3271685_3
- `C11`: Adjust the azimuth of 3258467_1 by 50 degrees
- `C12`: Lift the tilt angle  of 3258467_1 by 9 degrees **← 정답**
- `C13`: Lift the tilt angle of 3264760_4 by 2 degrees
- `C14`: Decrease A3 Offset threshold for 3271685_3
- `C15`: Decrease transmission power for 3271685_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264760_4
- `C17`: Increase A3 Offset threshold for 3264760_4
- `C18`: Increase transmission power for 3264760_4
- `C19`: Increase transmission power for 3271685_3
- `C20`: Increase A3 Offset threshold for 3271685_3
- `C21`: Add neighbor relationship between 3258467_1 and 3271685_3
- `C22`: Adjust the azimuth of 3264760_4 by 26 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.414 | MS1 | 121.4656695904 | 31.1446261815 | 262 | 504990 | -88.16 | 16.85 | 584.13 | 0.11 | 2.82 | 1600 |
| 2024-09-20 22:21:32.588 | MS1 | 121.4656716894 | 31.1446236889 | 262 | 504990 | -87.47 | 13.89 | 486.93 | 0.05 | 2.06 | 1599 |
| 2024-09-20 22:21:33.301 | MS1 | 121.4656729527 | 31.1446355767 | 262 | 504990 | -85.54 | 14.74 | 354.18 | 0.13 | 2.05 | 1596 |
| 2024-09-20 22:21:34.138 | MS1 | 121.4656682107 | 31.1446220934 | 262 | 504990 | -89.61 | 14.45 | 51.61 | 0.04 | 2.94 | 1592 |
| 2024-09-20 22:21:35.811 | MS1 | 121.4656650806 | 31.1446326800 | 262 | 504990 | -85.39 | 15.97 | 79.61 | 0.05 | 2.97 | 1575 |
| 2024-09-20 22:21:36.646 | MS1 | 121.4656657786 | 31.1446359460 | 262 | 504990 | -85.77 | 14.88 | 72.79 | 0.09 | 2.71 | 1599 |
| 2024-09-20 22:21:37.832 | MS1 | 121.4656629652 | 31.1446344752 | 262 | 504990 | -92.38 | 11.44 | 59.11 | 0.04 | 2.61 | 1574 |
| 2024-09-20 22:21:38.340 | MS1 | 121.4656588942 | 31.1446324811 | 262 | 504990 | -90.80 | 12.19 | 72.77 | 0.12 | 2.60 | 1571 |
| 2024-09-20 22:21:39.244 | MS1 | 121.4656587537 | 31.1446260397 | 262 | 504990 | -89.90 | 8.73 | 57.80 | 0.18 | 2.70 | 1569 |
| 2024-09-20 22:21:40.665 | MS1 | 121.4656705521 | 31.1446215187 | 262 | 504990 | -89.06 | 9.13 | 498.89 | 0.11 | 2.33 | 1579 |
| 2024-09-20 22:21:41.587 | MS1 | 121.4656739799 | 31.1446324151 | 262 | 504990 | -90.86 | 11.83 | 449.12 | 0.04 | 2.83 | 1577 |
| 2024-09-20 22:21:42.849 | MS1 | 121.4656626417 | 31.1446202316 | 262 | 504990 | -92.20 | 12.84 | 568.37 | 0.03 | 2.65 | 1567 |

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
| 3243357 | 2 | 121.4665311085 | 31.1557694389 | 68 | 11 | 10 | 29.9 | TDD | 419 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3258467 | 1 | 121.4707614814 | 31.1463052676 | 138 | 8 | 11 | 23.8 | TDD | 179 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3264760 | 4 | 121.4747420430 | 31.1558675426 | 189 | 1 | 5 | 37.2 | TDD | 262 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3271685 | 3 | 121.4704024246 | 31.1448128636 | 148 | 6 | 8 | 26.8 | TDD | 830 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.986 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.007 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.123 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.123 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.843 | NREventA3 | measId:2;ServCellPCI:126;Se... |
| 2024-09-20 22:21:38.083 | NRHandoverAttempt | SourcePCI:126;SourceNR-ARFC... |
| 2024-09-20 22:21:38.132 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.143 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.270 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.270 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258467 | 1 | 5.1086 | 8.2389 | -115.3256 | 6.0582 | 101.1986 | 0.0138 | 0.0004 |
| 2024_09_20 22:00 | 3243357 | 2 | 7.1489 | 18.6051 | -116.0456 | 7.8750 | 157.2708 | 0.0147 | 0.0171 |
| 2024_09_20 22:00 | 3271685 | 3 | 19.8383 | 15.8820 | -116.0791 | 12.5425 | 174.8883 | 0.0122 | 0.0150 |
| 2024_09_20 22:00 | 3264760 | 4 | 76.9925 | 78.7104 | -115.1844 | 18.0807 | 107.1535 | 0.0187 | 0.0040 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413596_F77421E0 | 504990 | 262 | -88.3 | 504990 | 830 | -95.1 | 504990 | 179 | -98.5 | 504990 | 419 |
| MR_1774413596_BAC2AC74 | 504990 | 262 | -90.5 | 504990 | 830 | -95.4 | 504990 | 179 | -95.7 | 504990 | 419 |
| MR_1774413596_20B3FAEC | 504990 | 262 | -89.1 | 504990 | 830 | -94.6 | 504990 | 179 | -96.5 | 504990 | 419 |
| MR_1774413596_50C65D84 | 504990 | 262 | -91.5 | 504990 | 830 | -94.6 | 504990 | 179 | -96.9 | 504990 | 419 |
| MR_1774413596_192D67E9 | 504990 | 262 | -90.1 | 504990 | 830 | -93.3 | 504990 | 179 | -98.3 | 504990 | 419 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1975: `5d95f909-efe...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5d95f909-efe4-460c-81c7-331f1da97f6c` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease A3 Offset threshold for 3239086_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1975] topology](images/train_1975.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3233582_4
- `C2`: Check test server and transmission issues
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239086_2
- `C4`: Decrease transmission power for 3233582_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239086_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233582_4
- `C7`: Increase transmission power for 3239086_2
- `C8`: Adjust the azimuth of 3239086_2 by 50 degrees
- `C9`: Increase A3 Offset threshold for 3239086_2
- `C10`: Press down the tilt angle of 3239086_2 by 3 degrees
- `C11`: Increase A3 Offset threshold for 3233582_4
- `C12`: Add neighbor relationship between 3215541_3 and 3233582_4
- `C13`: Decrease transmission power for 3239086_2
- `C14`: Add neighbor relationship between 3239086_2 and 3233582_4
- `C15`: Decrease A3 Offset threshold for 3239086_2 **← 정답**
- `C16`: Adjust the azimuth of 3233582_4 by 9 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233582_4
- `C18`: Increase transmission power for 3233582_4
- `C19`: Press down the tilt angle  of 3233582_4 by 10 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Lift the tilt angle of 3239086_2 by 3 degrees
- `C22`: Lift the tilt angle  of 3233582_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.895 | MS1 | 121.4656598332 | 31.1446338573 | 569 | 504990 | -84.82 | 14.06 | 426.26 | 0.18 | 2.70 | 1593 |
| 2024-09-20 22:21:32.466 | MS1 | 121.4656716986 | 31.1446191684 | 569 | 504990 | -81.52 | 16.51 | 362.12 | 0.10 | 2.02 | 1586 |
| 2024-09-20 22:21:33.692 | MS1 | 121.4656737655 | 31.1446201921 | 569 | 504990 | -84.19 | 14.77 | 394.34 | 0.15 | 2.78 | 1590 |
| 2024-09-20 22:21:34.185 | MS1 | 121.4656600903 | 31.1446267030 | 569 | 504990 | -83.04 | -2.08 | 75.17 | 0.07 | 1.23 | 1563 |
| 2024-09-20 22:21:35.505 | MS1 | 121.4656684921 | 31.1446257528 | 569 | 504990 | -87.65 | -1.15 | 59.90 | 0.17 | 1.34 | 1588 |
| 2024-09-20 22:21:36.262 | MS1 | 121.4656723111 | 31.1446188862 | 569 | 504990 | -85.64 | -3.86 | 74.52 | 0.18 | 1.45 | 1564 |
| 2024-09-20 22:21:37.684 | MS1 | 121.4656701554 | 31.1446288888 | 569 | 504990 | -91.38 | -2.96 | 59.52 | 0.18 | 1.39 | 1599 |
| 2024-09-20 22:21:38.716 | MS1 | 121.4656587021 | 31.1446231758 | 569 | 504990 | -90.72 | -0.44 | 50.11 | 0.02 | 1.07 | 1591 |
| 2024-09-20 22:21:39.944 | MS1 | 121.4656612509 | 31.1446294226 | 142 | 504990 | -75.68 | 12.71 | 230.76 | 0.10 | 1.04 | 1570 |
| 2024-09-20 22:21:40.380 | MS1 | 121.4656590417 | 31.1446322173 | 142 | 504990 | -80.57 | 14.86 | 504.80 | 0.02 | 2.10 | 1599 |
| 2024-09-20 22:21:41.926 | MS1 | 121.4656622504 | 31.1446223719 | 142 | 504990 | -77.93 | 12.49 | 428.52 | 0.18 | 2.61 | 1571 |
| 2024-09-20 22:21:42.122 | MS1 | 121.4656766666 | 31.1446298610 | 142 | 504990 | -77.81 | 14.67 | 528.93 | 0.10 | 2.03 | 1572 |

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
| 3215541 | 3 | 121.4707805840 | 31.1554405167 | 154 | 2 | 2 | 45.3 | TDD | 668 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3233582 | 4 | 121.4675014408 | 31.1474767180 | 200 | 7 | 3 | 24.4 | TDD | 142 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3238960 | 1 | 121.4691043232 | 31.1447191416 | 237 | 6 | 9 | 49.2 | TDD | 472 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3239086 | 2 | 121.4732713808 | 31.1474652501 | 325 | 2 | 2 | 17.0 | TDD | 569 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.185 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.203 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.318 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.318 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.016 | NREventA3 | measId:2;ServCellPCI:569;Se... |
| 2024-09-20 22:21:38.256 | NRHandoverAttempt | SourcePCI:569;SourceNR-ARFC... |
| 2024-09-20 22:21:38.301 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.311 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.457 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.457 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238960 | 1 | 5.3915 | 6.4076 | -116.3419 | 5.0249 | 98.7535 | 0.0118 | 0.0175 |
| 2024_09_20 22:00 | 3239086 | 2 | 14.4291 | 16.9863 | -114.5347 | 10.7592 | 147.0489 | 0.0142 | 0.1317 |
| 2024_09_20 22:00 | 3215541 | 3 | 11.7475 | 13.8852 | -116.3559 | 7.1989 | 121.1493 | 0.0125 | 0.0160 |
| 2024_09_20 22:00 | 3233582 | 4 | 8.4089 | 16.5569 | -117.5440 | 8.0776 | 193.3375 | 0.0066 | 0.0190 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414824_F367C000 | 504990 | 569 | -82.9 | 504990 | 142 | -77.6 | 504990 | 668 | -79.4 | 504990 | 472 |
| MR_1774414824_5E3C69D1 | 504990 | 569 | -82.4 | 504990 | 142 | -79.3 | 504990 | 668 | -79.3 | 504990 | 472 |
| MR_1774414824_B22AE486 | 504990 | 142 | -78.2 | 504990 | 569 | -81.3 | 504990 | 668 | -78.3 | 504990 | 472 |
| MR_1774414824_04604BDA | 504990 | 142 | -77.5 | 504990 | 569 | -84.2 | 504990 | 668 | -79.6 | 504990 | 472 |
| MR_1774414824_49E6C4B6 | 504990 | 142 | -78.6 | 504990 | 569 | -81.8 | 504990 | 668 | -78.5 | 504990 | 472 |
| MR_1774414824_97DA3162 | 504990 | 569 | -84.4 | 504990 | 142 | -77.7 | 504990 | 668 | -78.9 | 504990 | 472 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1976: `1fe89358-b65...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1fe89358-b651-4d7d-b0e6-fd8f88d1f173` |
| Tag | **multiple-answer** |
| 정답 | **C19|C22** |
| C19 의미 | Adjust the azimuth of 3250298_3 by 50 degrees |
| C22 의미 | Increase transmission power for 3250298_3 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1976] topology](images/train_1976.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225283_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250298_3
- `C3`: Lift the tilt angle of 3250298_3 by 10 degrees
- `C4`: Decrease A3 Offset threshold for 3225283_2
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase A3 Offset threshold for 3250298_3
- `C7`: Add neighbor relationship between 3250298_3 and 3225283_2
- `C8`: Press down the tilt angle of 3250298_3 by 10 degrees
- `C9`: Lift the tilt angle  of 3225283_2 by 4 degrees
- `C10`: Check test server and transmission issues
- `C11`: Increase transmission power for 3225283_2
- `C12`: Decrease A3 Offset threshold for 3250298_3
- `C13`: Add neighbor relationship between 3266015_1 and 3225283_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225283_2
- `C15`: Press down the tilt angle  of 3225283_2 by 4 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250298_3
- `C17`: Adjust the azimuth of 3225283_2 by 32 degrees
- `C18`: Increase A3 Offset threshold for 3225283_2
- `C19`: Adjust the azimuth of 3250298_3 by 50 degrees **← 정답**
- `C20`: Decrease transmission power for 3225283_2
- `C21`: Decrease transmission power for 3250298_3
- `C22`: Increase transmission power for 3250298_3 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.604 | MS1 | 121.4656586357 | 31.1446249025 | 926 | 504990 | -88.42 | 17.40 | 357.53 | 0.10 | 2.79 | 1568 |
| 2024-09-20 22:21:32.471 | MS1 | 121.4656696150 | 31.1446195437 | 926 | 504990 | -91.70 | 12.92 | 348.59 | 0.11 | 2.24 | 1571 |
| 2024-09-20 22:21:33.582 | MS1 | 121.4656597063 | 31.1446242684 | 926 | 504990 | -94.88 | 16.01 | 562.73 | 0.07 | 2.89 | 1562 |
| 2024-09-20 22:21:34.778 | MS1 | 121.4656716418 | 31.1446217181 | 926 | 504990 | -107.97 | -1.43 | 81.51 | 0.16 | 1.31 | 1585 |
| 2024-09-20 22:21:35.204 | MS1 | 121.4656616432 | 31.1446213130 | 926 | 504990 | -103.90 | 0.62 | 28.24 | 0.10 | 1.32 | 1569 |
| 2024-09-20 22:21:36.432 | MS1 | 121.4656669691 | 31.1446263119 | 926 | 504990 | -103.01 | -0.12 | 50.47 | 0.03 | 1.17 | 1583 |
| 2024-09-20 22:21:37.541 | MS1 | 121.4656616359 | 31.1446239882 | 926 | 504990 | -107.71 | -0.74 | 38.21 | 0.09 | 1.43 | 1580 |
| 2024-09-20 22:21:38.420 | MS1 | 121.4656770447 | 31.1446245202 | 926 | 504990 | -103.90 | -1.99 | 37.97 | 0.03 | 1.45 | 1591 |
| 2024-09-20 22:21:39.879 | MS1 | 121.4656605599 | 31.1446314147 | 926 | 504990 | -100.42 | 0.52 | 29.87 | 0.14 | 1.24 | 1577 |
| 2024-09-20 22:21:40.532 | MS1 | 121.4656660347 | 31.1446189713 | 926 | 504990 | -94.07 | 13.47 | 340.74 | 0.14 | 2.90 | 1586 |
| 2024-09-20 22:21:41.958 | MS1 | 121.4656644197 | 31.1446297649 | 926 | 504990 | -93.98 | 16.77 | 302.45 | 0.14 | 2.49 | 1599 |
| 2024-09-20 22:21:42.655 | MS1 | 121.4656651456 | 31.1446197153 | 926 | 504990 | -92.74 | 17.07 | 418.30 | 0.03 | 2.54 | 1571 |

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
| 3225283 | 2 | 121.4744490162 | 31.1488608142 | 273 | 3 | 9 | 19.1 | TDD | 564 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3241543 | 4 | 121.4640942350 | 31.1478838378 | 111 | 0 | 2 | 18.9 | TDD | 334 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3250298 | 3 | 121.4669363085 | 31.1517554902 | 133 | 7 | 10 | 45.8 | TDD | 926 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3266015 | 1 | 121.4758461317 | 31.1476275578 | 35 | 11 | 3 | 16.9 | TDD | 113 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.318 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.334 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.458 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.458 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.709 | NREventA2 | measId:1;ServCellPCI:918;Se... |
| 2024-09-20 22:21:34.830 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266015 | 1 | 13.5556 | 6.8555 | -115.2202 | 10.4220 | 184.5414 | 0.0103 | 0.0175 |
| 2024_09_20 22:00 | 3225283 | 2 | 12.5083 | 12.2508 | -114.7302 | 16.1178 | 146.3103 | 0.0187 | 0.0143 |
| 2024_09_20 22:00 | 3250298 | 3 | 16.6257 | 9.1959 | -117.8288 | 11.7802 | 194.7964 | 0.1838 | 0.0104 |
| 2024_09_20 22:00 | 3241543 | 4 | 11.0311 | 5.0735 | -115.7275 | 11.6297 | 161.3097 | 0.0087 | 0.0024 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412698_C5A35A85 | 504990 | 926 | -106.4 | 504990 | 564 | -117.5 | 504990 | 113 | -121.4 | 504990 | 334 |
| MR_1774412698_EC421756 | 504990 | 926 | -109.8 | 504990 | 564 | -117.7 | 504990 | 113 | -124.0 | 504990 | 334 |
| MR_1774412698_FE921B21 | 504990 | 926 | -109.2 | 504990 | 564 | -115.0 | 504990 | 113 | -124.9 | 504990 | 334 |
| MR_1774412698_4D479497 | 504990 | 926 | -109.9 | 504990 | 564 | -116.4 | 504990 | 113 | -124.7 | 504990 | 334 |
| MR_1774412698_D7892B4D | 504990 | 926 | -109.6 | 504990 | 564 | -116.3 | 504990 | 113 | -122.3 | 504990 | 334 |
| MR_1774412698_9F332D8F | 504990 | 926 | -109.6 | 504990 | 564 | -115.1 | 504990 | 113 | -123.9 | 504990 | 334 |
| MR_1774412698_F51141CB | 504990 | 926 | -108.5 | 504990 | 564 | -117.6 | 504990 | 113 | -125.0 | 504990 | 334 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1977: `1308e70d-6a2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1308e70d-6a2e-446d-adb1-0ecc9dace304` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Decrease A3 Offset threshold for 3220931_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1977] topology](images/train_1977.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3254264_4 by 10 degrees
- `C2`: Decrease transmission power for 3220931_2
- `C3`: Lift the tilt angle of 3220931_2 by 10 degrees
- `C4`: Decrease A3 Offset threshold for 3254264_4
- `C5`: Press down the tilt angle of 3220931_2 by 10 degrees
- `C6`: Adjust the azimuth of 3220931_2 by 50 degrees
- `C7`: Lift the tilt angle  of 3254264_4 by 10 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease transmission power for 3254264_4
- `C10`: Check test server and transmission issues
- `C11`: Increase A3 Offset threshold for 3254264_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220931_2
- `C13`: Increase transmission power for 3254264_4
- `C14`: Adjust the azimuth of 3254264_4 by 50 degrees
- `C15`: Increase A3 Offset threshold for 3220931_2
- `C16`: Add neighbor relationship between 3221397_3 and 3254264_4
- `C17`: Decrease A3 Offset threshold for 3220931_2 **← 정답**
- `C18`: Add neighbor relationship between 3220931_2 and 3254264_4
- `C19`: Increase transmission power for 3220931_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220931_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254264_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254264_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.554 | MS1 | 121.4656754058 | 31.1446347183 | 954 | 504990 | -79.21 | 15.00 | 329.51 | 0.15 | 2.75 | 1565 |
| 2024-09-20 22:21:32.379 | MS1 | 121.4656607657 | 31.1446218581 | 954 | 504990 | -77.51 | 17.54 | 332.86 | 0.17 | 2.71 | 1562 |
| 2024-09-20 22:21:33.147 | MS1 | 121.4656627927 | 31.1446247520 | 954 | 504990 | -80.06 | 14.69 | 513.51 | 0.02 | 2.76 | 1565 |
| 2024-09-20 22:21:34.376 | MS1 | 121.4656724518 | 31.1446283341 | 954 | 504990 | -90.57 | -2.57 | 22.44 | 0.00 | 1.14 | 1566 |
| 2024-09-20 22:21:35.276 | MS1 | 121.4656641318 | 31.1446182131 | 954 | 504990 | -86.58 | -2.43 | 43.41 | 0.09 | 1.04 | 1574 |
| 2024-09-20 22:21:36.730 | MS1 | 121.4656704879 | 31.1446198206 | 954 | 504990 | -86.34 | -0.66 | 73.90 | 0.08 | 1.26 | 1562 |
| 2024-09-20 22:21:37.654 | MS1 | 121.4656582071 | 31.1446329624 | 954 | 504990 | -83.11 | -2.37 | 37.98 | 0.16 | 1.16 | 1577 |
| 2024-09-20 22:21:38.446 | MS1 | 121.4656678330 | 31.1446184683 | 954 | 504990 | -83.26 | -1.24 | 66.25 | 0.16 | 1.04 | 1567 |
| 2024-09-20 22:21:39.988 | MS1 | 121.4656653486 | 31.1446333765 | 405 | 504990 | -81.87 | 13.66 | 153.45 | 0.11 | 1.42 | 1587 |
| 2024-09-20 22:21:40.986 | MS1 | 121.4656765340 | 31.1446223795 | 405 | 504990 | -78.97 | 14.58 | 521.00 | 0.09 | 2.97 | 1587 |
| 2024-09-20 22:21:41.825 | MS1 | 121.4656673669 | 31.1446262425 | 405 | 504990 | -80.55 | 13.14 | 410.33 | 0.04 | 2.48 | 1585 |
| 2024-09-20 22:21:42.947 | MS1 | 121.4656742698 | 31.1446303445 | 405 | 504990 | -81.68 | 15.05 | 405.75 | 0.03 | 2.24 | 1581 |

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
| 3220931 | 2 | 121.4703798402 | 31.1442186332 | 133 | 10 | 0 | 19.0 | TDD | 954 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3221397 | 3 | 121.4717227877 | 31.1443341997 | 258 | 8 | 1 | 42.1 | TDD | 587 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3246841 | 1 | 121.4656395767 | 31.1460795789 | 6 | 6 | 3 | 45.5 | TDD | 848 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3254264 | 4 | 121.4653635409 | 31.1488090381 | 300 | 11 | 5 | 32.4 | TDD | 405 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.632 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.652 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.780 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.780 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.462 | NREventA3 | measId:2;ServCellPCI:649;Se... |
| 2024-09-20 22:21:38.702 | NRHandoverAttempt | SourcePCI:649;SourceNR-ARFC... |
| 2024-09-20 22:21:38.752 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.764 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.871 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.871 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246841 | 1 | 6.7294 | 7.0715 | -115.9921 | 11.7610 | 90.7010 | 0.0160 | 0.0042 |
| 2024_09_20 22:00 | 3220931 | 2 | 16.6582 | 7.7091 | -114.4674 | 8.4889 | 88.8645 | 0.0012 | 0.1859 |
| 2024_09_20 22:00 | 3221397 | 3 | 14.1992 | 16.3276 | -114.4238 | 10.3705 | 150.7941 | 0.0128 | 0.0136 |
| 2024_09_20 22:00 | 3254264 | 4 | 9.3745 | 14.4037 | -117.4691 | 12.5225 | 188.6354 | 0.0141 | 0.0069 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414742_2E740D2D | 504990 | 954 | -89.4 | 504990 | 405 | -85.9 | 504990 | 587 | -90.9 | 504990 | 848 |
| MR_1774414742_716339AC | 504990 | 405 | -86.5 | 504990 | 954 | -90.7 | 504990 | 587 | -93.7 | 504990 | 848 |
| MR_1774414742_E9A1613C | 504990 | 954 | -89.6 | 504990 | 405 | -86.5 | 504990 | 587 | -90.6 | 504990 | 848 |
| MR_1774414742_9DC11A86 | 504990 | 954 | -90.8 | 504990 | 405 | -87.5 | 504990 | 587 | -94.0 | 504990 | 848 |
| MR_1774414742_13058FA7 | 504990 | 954 | -89.3 | 504990 | 405 | -84.9 | 504990 | 587 | -91.6 | 504990 | 848 |
| MR_1774414742_09323057 | 504990 | 954 | -91.7 | 504990 | 405 | -87.1 | 504990 | 587 | -93.5 | 504990 | 848 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1978: `3d452697-9a0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3d452697-9a05-4413-ad4e-f61a42bdee1f` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3212830_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1978] topology](images/train_1978.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3212830_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216706_3
- `C3`: Add neighbor relationship between 3212830_1 and 3216706_3
- `C4`: Increase A3 Offset threshold for 3216706_3
- `C5`: Lift the tilt angle  of 3216706_3 by 10 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Press down the tilt angle  of 3216706_3 by 10 degrees
- `C8`: Increase transmission power for 3212830_1
- `C9`: Press down the tilt angle of 3212830_1 by 1 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212830_1 **← 정답**
- `C11`: Add neighbor relationship between 3253935_2 and 3216706_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212830_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216706_3
- `C14`: Decrease transmission power for 3216706_3
- `C15`: Decrease A3 Offset threshold for 3216706_3
- `C16`: Increase A3 Offset threshold for 3212830_1
- `C17`: Decrease A3 Offset threshold for 3212830_1
- `C18`: Lift the tilt angle of 3212830_1 by 1 degrees
- `C19`: Increase transmission power for 3216706_3
- `C20`: Adjust the azimuth of 3212830_1 by 5 degrees
- `C21`: Adjust the azimuth of 3216706_3 by 50 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.873 | MS1 | 121.4656745790 | 31.1446350401 | 410 | 504990 | -88.91 | 13.67 | 536.26 | 0.07 | 2.26 | 1593 |
| 2024-09-20 22:21:32.909 | MS1 | 121.4656597694 | 31.1446289387 | 410 | 504990 | -87.32 | 13.99 | 456.41 | 0.09 | 2.91 | 1582 |
| 2024-09-20 22:21:33.549 | MS1 | 121.4656749904 | 31.1446276170 | 410 | 504990 | -86.02 | 17.65 | 334.89 | 0.01 | 2.62 | 1599 |
| 2024-09-20 22:21:34.940 | MS1 | 121.4656738817 | 31.1446223240 | 410 | 504990 | -87.11 | 13.20 | 67.98 | 0.65 | 2.64 | 539 |
| 2024-09-20 22:21:35.505 | MS1 | 121.4656752500 | 31.1446291891 | 410 | 504990 | -86.35 | 12.05 | 66.33 | 0.58 | 2.93 | 645 |
| 2024-09-20 22:21:36.831 | MS1 | 121.4656636203 | 31.1446336314 | 410 | 504990 | -88.70 | 15.24 | 51.53 | 0.63 | 2.49 | 668 |
| 2024-09-20 22:21:37.904 | MS1 | 121.4656632555 | 31.1446269304 | 410 | 504990 | -92.26 | 11.14 | 69.09 | 0.51 | 2.20 | 521 |
| 2024-09-20 22:21:38.214 | MS1 | 121.4656663223 | 31.1446357803 | 410 | 504990 | -93.22 | 8.68 | 92.48 | 0.52 | 2.94 | 530 |
| 2024-09-20 22:21:39.177 | MS1 | 121.4656615103 | 31.1446289353 | 410 | 504990 | -90.75 | 9.66 | 96.05 | 0.61 | 2.20 | 535 |
| 2024-09-20 22:21:40.177 | MS1 | 121.4656715205 | 31.1446342591 | 410 | 504990 | -91.73 | 7.81 | 401.32 | 0.16 | 2.61 | 1593 |
| 2024-09-20 22:21:41.987 | MS1 | 121.4656760192 | 31.1446345047 | 410 | 504990 | -93.90 | 9.37 | 450.04 | 0.19 | 2.47 | 1579 |
| 2024-09-20 22:21:42.419 | MS1 | 121.4656643038 | 31.1446283643 | 410 | 504990 | -89.08 | 7.88 | 399.54 | 0.17 | 2.72 | 1569 |

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
| 3212830 | 1 | 121.4746007525 | 31.1542595201 | 213 | 0 | 0 | 27.8 | TDD | 410 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3216706 | 3 | 121.4653230867 | 31.1442780140 | 268 | 15 | 7 | 16.6 | TDD | 732 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3249038 | 4 | 121.4733970333 | 31.1459846517 | 242 | 15 | 9 | 21.2 | TDD | 327 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3253935 | 2 | 121.4724081820 | 31.1519616628 | 234 | 4 | 1 | 21.6 | TDD | 195 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.588 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.604 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.741 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.741 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.446 | NREventA3 | measId:2;ServCellPCI:58;Ser... |
| 2024-09-20 22:21:38.686 | NRHandoverAttempt | SourcePCI:58;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.719 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.732 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.841 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.841 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212830 | 1 | 17.0824 | 15.0858 | -114.2039 | 19.5605 | 108.3257 | 0.0102 | 0.0009 |
| 2024_09_20 22:00 | 3253935 | 2 | 9.3830 | 12.6090 | -117.6747 | 6.3331 | 156.1147 | 0.0000 | 0.0020 |
| 2024_09_20 22:00 | 3216706 | 3 | 16.7840 | 19.0659 | -114.1980 | 12.5722 | 168.2797 | 0.0021 | 0.0001 |
| 2024_09_20 22:00 | 3249038 | 4 | 8.4528 | 11.2060 | -114.8371 | 12.7543 | 105.2812 | 0.0191 | 0.0071 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414504_1B208FDB | 504990 | 410 | -85.5 | 504990 | 732 | -86.9 | 504990 | 195 | -94.0 | 504990 | 327 |
| MR_1774414504_3E71EFB2 | 504990 | 410 | -88.0 | 504990 | 732 | -88.8 | 504990 | 195 | -92.5 | 504990 | 327 |
| MR_1774414504_C4025B61 | 504990 | 410 | -88.9 | 504990 | 732 | -86.7 | 504990 | 195 | -91.6 | 504990 | 327 |
| MR_1774414504_5DDB95A2 | 504990 | 410 | -87.4 | 504990 | 732 | -86.7 | 504990 | 195 | -94.8 | 504990 | 327 |
| MR_1774414504_0CB0BDEC | 504990 | 410 | -89.1 | 504990 | 732 | -87.4 | 504990 | 195 | -94.9 | 504990 | 327 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1979: `da07052d-1ee...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `da07052d-1ee8-4211-b793-b0171b9c5d73` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3276772_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1979] topology](images/train_1979.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229519_1
- `C3`: Press down the tilt angle  of 3229519_1 by 9 degrees
- `C4`: Check test server and transmission issues
- `C5`: Decrease transmission power for 3276772_3
- `C6`: Lift the tilt angle  of 3229519_1 by 9 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276772_3 **← 정답**
- `C8`: Decrease transmission power for 3229519_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229519_1
- `C10`: Increase transmission power for 3229519_1
- `C11`: Press down the tilt angle of 3276772_3 by 2 degrees
- `C12`: Adjust the azimuth of 3229519_1 by 50 degrees
- `C13`: Add neighbor relationship between 3276772_3 and 3229519_1
- `C14`: Adjust the azimuth of 3276772_3 by 27 degrees
- `C15`: Decrease A3 Offset threshold for 3229519_1
- `C16`: Decrease A3 Offset threshold for 3276772_3
- `C17`: Increase transmission power for 3276772_3
- `C18`: Add neighbor relationship between 3215116_2 and 3229519_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276772_3
- `C20`: Increase A3 Offset threshold for 3276772_3
- `C21`: Lift the tilt angle of 3276772_3 by 2 degrees
- `C22`: Increase A3 Offset threshold for 3229519_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.308 | MS1 | 121.4656655950 | 31.1446250234 | 155 | 504990 | -90.99 | 13.14 | 341.03 | 0.01 | 2.08 | 1582 |
| 2024-09-20 22:21:32.746 | MS1 | 121.4656646945 | 31.1446222543 | 155 | 504990 | -90.40 | 13.11 | 533.49 | 0.11 | 2.44 | 1595 |
| 2024-09-20 22:21:33.206 | MS1 | 121.4656664158 | 31.1446351198 | 155 | 504990 | -86.75 | 16.92 | 447.04 | 0.18 | 2.59 | 1594 |
| 2024-09-20 22:21:34.239 | MS1 | 121.4656674222 | 31.1446250690 | 155 | 504990 | -85.60 | 13.79 | 98.13 | 0.55 | 2.86 | 527 |
| 2024-09-20 22:21:35.145 | MS1 | 121.4656627627 | 31.1446206910 | 155 | 504990 | -91.79 | 17.65 | 81.04 | 0.50 | 2.05 | 675 |
| 2024-09-20 22:21:36.462 | MS1 | 121.4656614029 | 31.1446363375 | 155 | 504990 | -86.01 | 17.67 | 98.47 | 0.69 | 2.32 | 536 |
| 2024-09-20 22:21:37.810 | MS1 | 121.4656602202 | 31.1446340833 | 155 | 504990 | -89.11 | 8.53 | 78.58 | 0.53 | 2.37 | 648 |
| 2024-09-20 22:21:38.494 | MS1 | 121.4656741008 | 31.1446181513 | 155 | 504990 | -89.21 | 8.98 | 73.01 | 0.60 | 2.84 | 555 |
| 2024-09-20 22:21:39.248 | MS1 | 121.4656703454 | 31.1446313061 | 155 | 504990 | -91.33 | 12.70 | 95.66 | 0.68 | 2.25 | 518 |
| 2024-09-20 22:21:40.492 | MS1 | 121.4656628199 | 31.1446341232 | 155 | 504990 | -90.25 | 12.17 | 459.52 | 0.11 | 2.87 | 1596 |
| 2024-09-20 22:21:41.694 | MS1 | 121.4656733322 | 31.1446324563 | 155 | 504990 | -92.52 | 9.71 | 577.95 | 0.12 | 2.07 | 1573 |
| 2024-09-20 22:21:42.769 | MS1 | 121.4656715668 | 31.1446216460 | 155 | 504990 | -93.75 | 10.49 | 553.87 | 0.01 | 2.27 | 1579 |

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
| 3215116 | 2 | 121.4737283151 | 31.1513449844 | 337 | 13 | 2 | 32.3 | TDD | 541 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3229519 | 1 | 121.4745368982 | 31.1525860061 | 55 | 7 | 7 | 43.8 | TDD | 120 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3253676 | 4 | 121.4643916506 | 31.1456075770 | 304 | 3 | 11 | 21.6 | TDD | 781 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3276772 | 3 | 121.4673753782 | 31.1518531448 | 218 | 0 | 1 | 25.0 | TDD | 155 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.842 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.863 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.963 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.963 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.726 | NREventA3 | measId:2;ServCellPCI:458;Se... |
| 2024-09-20 22:21:37.966 | NRHandoverAttempt | SourcePCI:458;SourceNR-ARFC... |
| 2024-09-20 22:21:38.014 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.024 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.163 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.163 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229519 | 1 | 10.9345 | 17.9323 | -114.2279 | 18.7235 | 196.0485 | 0.0146 | 0.0167 |
| 2024_09_20 22:00 | 3215116 | 2 | 13.8633 | 15.3651 | -117.7209 | 5.7210 | 106.3014 | 0.0016 | 0.0145 |
| 2024_09_20 22:00 | 3276772 | 3 | 11.9513 | 10.6504 | -117.0050 | 7.9228 | 82.1173 | 0.0061 | 0.0055 |
| 2024_09_20 22:00 | 3253676 | 4 | 14.4777 | 18.3127 | -117.4160 | 17.2182 | 104.3741 | 0.0196 | 0.0133 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412483_A2B6BD55 | 504990 | 155 | -84.9 | 504990 | 120 | -89.9 | 504990 | 541 | -95.7 | 504990 | 781 |
| MR_1774412483_033D6675 | 504990 | 155 | -84.3 | 504990 | 120 | -86.8 | 504990 | 541 | -96.5 | 504990 | 781 |
| MR_1774412483_61EB8EEA | 504990 | 155 | -85.7 | 504990 | 120 | -86.6 | 504990 | 541 | -96.2 | 504990 | 781 |
| MR_1774412483_D149EA9B | 504990 | 155 | -84.5 | 504990 | 120 | -86.4 | 504990 | 541 | -94.4 | 504990 | 781 |
| MR_1774412483_274FD57E | 504990 | 155 | -86.0 | 504990 | 120 | -86.3 | 504990 | 541 | -94.2 | 504990 | 781 |

> *... 2개 열 생략 (전체 14열)*

---
