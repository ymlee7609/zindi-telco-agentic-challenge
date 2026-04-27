# Track A 문제 분석 — test[410]~test[419]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[410] ~ test[419] (10개)

## 목차

1. [문제 410: `7fd88f00-290...`](#410) — single-answer
2. [문제 411: `aceb0717-8db...`](#411) — single-answer
3. [문제 412: `9877a44c-d71...`](#412) — single-answer
4. [문제 413: `06a1c19a-2f0...`](#413) — single-answer
5. [문제 414: `7ae7f4a7-dbf...`](#414) — single-answer
6. [문제 415: `56f0c845-88f...`](#415) — single-answer
7. [문제 416: `113b97c5-e23...`](#416) — single-answer
8. [문제 417: `4866d7bf-6bb...`](#417) — single-answer
9. [문제 418: `f83c3a67-108...`](#418) — single-answer
10. [문제 419: `852494de-d19...`](#419) — single-answer

---

### 문제 410: `7fd88f00-290...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7fd88f00-290e-4275-b4fb-10cefa39292d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[410] topology](images/test_0410.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3250252_1 and 3262677_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262677_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214651_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214651_2
- `C5`: Add neighbor relationship between 3214651_2 and 3262677_4
- `C6`: Increase A3 Offset threshold for 3214651_2
- `C7`: Decrease transmission power for 3262677_4
- `C8`: Increase transmission power for 3262677_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262677_4
- `C10`: Press down the tilt angle of 3214651_2 by 10 degrees
- `C11`: Increase A3 Offset threshold for 3262677_4
- `C12`: Press down the tilt angle  of 3262677_4 by 3 degrees
- `C13`: Lift the tilt angle  of 3262677_4 by 3 degrees
- `C14`: Decrease A3 Offset threshold for 3214651_2
- `C15`: Lift the tilt angle of 3214651_2 by 10 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Adjust the azimuth of 3262677_4 by 35 degrees
- `C18`: Decrease A3 Offset threshold for 3262677_4
- `C19`: Check test server and transmission issues
- `C20`: Decrease transmission power for 3214651_2
- `C21`: Increase transmission power for 3214651_2
- `C22`: Adjust the azimuth of 3214651_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.869 | MS1 | 121.4656614640 | 31.1446302312 | 898 | 504990 | -84.18 | 16.93 | 299.56 | 0.11 | 2.32 | 1579 |
| 2024-09-20 22:21:32.141 | MS1 | 121.4656668026 | 31.1446307059 | 898 | 504990 | -82.20 | 15.99 | 549.86 | 0.03 | 2.30 | 1574 |
| 2024-09-20 22:21:33.926 | MS1 | 121.4656605241 | 31.1446336429 | 898 | 504990 | -84.51 | 15.27 | 331.94 | 0.15 | 2.82 | 1595 |
| 2024-09-20 22:21:34.610 | MS1 | 121.4656617044 | 31.1446379186 | 898 | 504990 | -85.94 | -1.63 | 42.10 | 0.19 | 1.42 | 1597 |
| 2024-09-20 22:21:35.858 | MS1 | 121.4656750769 | 31.1446252579 | 898 | 504990 | -87.13 | -2.81 | 45.64 | 0.12 | 1.08 | 1583 |
| 2024-09-20 22:21:36.934 | MS1 | 121.4656715819 | 31.1446292901 | 898 | 504990 | -86.06 | -0.33 | 49.30 | 0.16 | 1.39 | 1561 |
| 2024-09-20 22:21:37.817 | MS1 | 121.4656665732 | 31.1446328860 | 898 | 504990 | -89.40 | -3.84 | 38.14 | 0.11 | 1.12 | 1591 |
| 2024-09-20 22:21:38.509 | MS1 | 121.4656758637 | 31.1446362629 | 898 | 504990 | -82.76 | 15.02 | 475.27 | 0.10 | 1.00 | 1589 |
| 2024-09-20 22:21:39.263 | MS1 | 121.4656598101 | 31.1446270468 | 898 | 504990 | -84.21 | 14.94 | 493.68 | 0.08 | 1.06 | 1587 |
| 2024-09-20 22:21:40.270 | MS1 | 121.4656747188 | 31.1446184870 | 898 | 504990 | -78.57 | 13.98 | 514.03 | 0.01 | 2.97 | 1588 |
| 2024-09-20 22:21:41.970 | MS1 | 121.4656607337 | 31.1446297471 | 898 | 504990 | -82.87 | 17.54 | 380.68 | 0.04 | 2.22 | 1587 |
| 2024-09-20 22:21:42.909 | MS1 | 121.4656686839 | 31.1446217109 | 898 | 504990 | -78.58 | 17.52 | 374.02 | 0.03 | 2.48 | 1596 |

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
| 3214651 | 2 | 121.4646986085 | 31.1559627259 | 256 | 12 | 10 | 23.4 | TDD | 898 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3223437 | 3 | 121.4667877277 | 31.1558940817 | 314 | 15 | 4 | 27.7 | TDD | 389 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3250252 | 1 | 121.4680770852 | 31.1468050905 | 261 | 11 | 6 | 39.6 | TDD | 161 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3262677 | 4 | 121.4735325453 | 31.1555435123 | 177 | 1 | 6 | 42.8 | TDD | 582 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.667 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.692 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.842 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.842 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.494 | NREventA3 | measId:2;ServCellPCI:374;Se... |
| 2024-09-20 22:21:36.494 | NREventA3 | measId:2;ServCellPCI:374;Se... |
| 2024-09-20 22:21:37.494 | NREventA3 | measId:2;ServCellPCI:374;Se... |
| 2024-09-20 22:21:39.994 | NRRRCReestablishAttempt | PCI:374 |
| 2024-09-20 22:21:40.005 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:40.020 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:40.163 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.163 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250252 | 1 | 9.7326 | 8.1100 | -117.4515 | 10.3491 | 128.6098 | 0.0023 | 0.0109 |
| 2024_09_20 22:00 | 3214651 | 2 | 5.0000 | 12.1562 | -117.4815 | 16.5742 | 191.2093 | 0.0181 | 0.1355 |
| 2024_09_20 22:00 | 3223437 | 3 | 14.2545 | 5.2643 | -114.6354 | 19.8619 | 143.6815 | 0.0141 | 0.0169 |
| 2024_09_20 22:00 | 3262677 | 4 | 12.8056 | 14.9725 | -116.7587 | 15.8306 | 113.0148 | 0.0029 | 0.0180 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414217_F1C4CAF5 | 504990 | 898 | -86.2 | 504990 | 582 | -79.3 | 504990 | 161 | -84.1 | 504990 | 389 |
| MR_1774414217_93F14A67 | 504990 | 898 | -86.7 | 504990 | 582 | -79.0 | 504990 | 161 | -82.8 | 504990 | 389 |
| MR_1774414217_39C4CAEA | 504990 | 582 | -82.1 | 504990 | 898 | -86.8 | 504990 | 161 | -83.9 | 504990 | 389 |
| MR_1774414217_E03B34CE | 504990 | 582 | -78.7 | 504990 | 898 | -85.4 | 504990 | 161 | -83.5 | 504990 | 389 |
| MR_1774414217_BBCF2DD8 | 504990 | 898 | -84.1 | 504990 | 582 | -81.9 | 504990 | 161 | -82.1 | 504990 | 389 |
| MR_1774414217_C8A38C6E | 504990 | 582 | -80.4 | 504990 | 898 | -84.1 | 504990 | 161 | -83.4 | 504990 | 389 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 411: `aceb0717-8db...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `aceb0717-8db8-4035-8338-f00b10d9b76b` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[411] topology](images/test_0411.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215732_1
- `C2`: Decrease A3 Offset threshold for 3251735_4
- `C3`: Adjust the azimuth of 3251735_4 by 50 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215732_1
- `C5`: Press down the tilt angle  of 3251735_4 by 10 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease transmission power for 3251735_4
- `C8`: Lift the tilt angle of 3215732_1 by 2 degrees
- `C9`: Add neighbor relationship between 3215732_1 and 3251735_4
- `C10`: Decrease A3 Offset threshold for 3215732_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251735_4
- `C12`: Decrease transmission power for 3215732_1
- `C13`: Add neighbor relationship between 3272569_2 and 3251735_4
- `C14`: Increase A3 Offset threshold for 3251735_4
- `C15`: Check test server and transmission issues
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251735_4
- `C17`: Adjust the azimuth of 3215732_1 by 14 degrees
- `C18`: Lift the tilt angle  of 3251735_4 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3215732_1
- `C20`: Press down the tilt angle of 3215732_1 by 2 degrees
- `C21`: Increase transmission power for 3215732_1
- `C22`: Increase transmission power for 3251735_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.453 | MS1 | 121.4656680662 | 31.1446322522 | 66 | 504990 | -86.27 | 15.57 | 576.88 | 0.13 | 2.00 | 1588 |
| 2024-09-20 22:21:32.186 | MS1 | 121.4656682272 | 31.1446305116 | 66 | 504990 | -91.81 | 17.89 | 382.10 | 0.03 | 2.52 | 1597 |
| 2024-09-20 22:21:33.410 | MS1 | 121.4656645224 | 31.1446263836 | 66 | 504990 | -88.06 | 12.98 | 496.34 | 0.13 | 2.65 | 1569 |
| 2024-09-20 22:21:34.479 | MS1 | 121.4656625005 | 31.1446244721 | 66 | 504990 | -90.92 | 17.89 | 65.87 | 0.69 | 2.21 | 630 |
| 2024-09-20 22:21:35.494 | MS1 | 121.4656765347 | 31.1446371162 | 66 | 504990 | -87.69 | 16.97 | 73.30 | 0.63 | 2.06 | 520 |
| 2024-09-20 22:21:36.727 | MS1 | 121.4656661657 | 31.1446301031 | 66 | 504990 | -91.00 | 15.41 | 54.80 | 0.58 | 2.62 | 648 |
| 2024-09-20 22:21:37.703 | MS1 | 121.4656724309 | 31.1446294948 | 66 | 504990 | -91.62 | 11.76 | 99.02 | 0.56 | 2.24 | 557 |
| 2024-09-20 22:21:38.640 | MS1 | 121.4656615009 | 31.1446312367 | 66 | 504990 | -91.48 | 11.85 | 64.70 | 0.67 | 2.82 | 623 |
| 2024-09-20 22:21:39.327 | MS1 | 121.4656713677 | 31.1446378353 | 66 | 504990 | -93.29 | 12.92 | 90.29 | 0.64 | 2.26 | 593 |
| 2024-09-20 22:21:40.804 | MS1 | 121.4656687135 | 31.1446292151 | 66 | 504990 | -92.01 | 10.65 | 531.89 | 0.05 | 2.51 | 1580 |
| 2024-09-20 22:21:41.825 | MS1 | 121.4656778176 | 31.1446191722 | 66 | 504990 | -92.13 | 8.07 | 394.43 | 0.00 | 2.26 | 1574 |
| 2024-09-20 22:21:42.419 | MS1 | 121.4656668904 | 31.1446343745 | 66 | 504990 | -91.45 | 9.14 | 560.16 | 0.02 | 2.82 | 1598 |

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
| 3215732 | 1 | 121.4668745535 | 31.1527152396 | 173 | 0 | 10 | 28.9 | TDD | 66 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3251735 | 4 | 121.4689712190 | 31.1478765363 | 29 | 6 | 2 | 39.0 | TDD | 470 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3271534 | 3 | 121.4730554715 | 31.1492334203 | 120 | 14 | 12 | 41.8 | TDD | 253 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3272569 | 2 | 121.4752112111 | 31.1477291332 | 213 | 14 | 3 | 18.8 | TDD | 547 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.236 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.254 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.370 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.370 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.066 | NREventA3 | measId:2;ServCellPCI:730;Se... |
| 2024-09-20 22:21:38.306 | NRHandoverAttempt | SourcePCI:730;SourceNR-ARFC... |
| 2024-09-20 22:21:38.342 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.352 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.458 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.458 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215732 | 1 | 9.3125 | 14.0262 | -114.7795 | 16.1194 | 144.2478 | 0.0184 | 0.0088 |
| 2024_09_20 22:00 | 3272569 | 2 | 18.8795 | 5.8241 | -114.8675 | 19.6884 | 87.3960 | 0.0020 | 0.0029 |
| 2024_09_20 22:00 | 3271534 | 3 | 19.1106 | 12.3194 | -114.4918 | 7.9749 | 134.2611 | 0.0032 | 0.0030 |
| 2024_09_20 22:00 | 3251735 | 4 | 8.0160 | 10.5245 | -116.1773 | 12.3362 | 130.0062 | 0.0190 | 0.0008 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415225_524E194D | 504990 | 66 | -89.2 | 504990 | 470 | -97.2 | 504990 | 547 | -100.0 | 504990 | 253 |
| MR_1774415225_C27FF8DB | 504990 | 66 | -91.6 | 504990 | 470 | -98.7 | 504990 | 547 | -99.1 | 504990 | 253 |
| MR_1774415225_54B57572 | 504990 | 66 | -92.1 | 504990 | 470 | -97.4 | 504990 | 547 | -99.0 | 504990 | 253 |
| MR_1774415225_8CA75A7F | 504990 | 66 | -89.3 | 504990 | 470 | -97.0 | 504990 | 547 | -102.0 | 504990 | 253 |
| MR_1774415225_19DB70DA | 504990 | 66 | -90.2 | 504990 | 470 | -97.1 | 504990 | 547 | -100.3 | 504990 | 253 |
| MR_1774415225_B8480B6F | 504990 | 66 | -92.1 | 504990 | 470 | -97.9 | 504990 | 547 | -99.7 | 504990 | 253 |
| MR_1774415225_649FD52D | 504990 | 66 | -89.7 | 504990 | 470 | -100.5 | 504990 | 547 | -101.2 | 504990 | 253 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 412: `9877a44c-d71...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9877a44c-d716-4b19-b0f0-cca37cf0ec76` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[412] topology](images/test_0412.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3270841_4
- `C2`: Press down the tilt angle  of 3270841_4 by 10 degrees
- `C3`: Decrease A3 Offset threshold for 3270841_4
- `C4`: Lift the tilt angle of 3218790_3 by 2 degrees
- `C5`: Increase transmission power for 3218790_3
- `C6`: Add neighbor relationship between 3227372_2 and 3270841_4
- `C7`: Adjust the azimuth of 3270841_4 by 50 degrees
- `C8`: Decrease transmission power for 3270841_4
- `C9`: Lift the tilt angle  of 3270841_4 by 10 degrees
- `C10`: Press down the tilt angle of 3218790_3 by 2 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Add neighbor relationship between 3218790_3 and 3270841_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270841_4
- `C14`: Check test server and transmission issues
- `C15`: Increase A3 Offset threshold for 3218790_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270841_4
- `C17`: Increase A3 Offset threshold for 3270841_4
- `C18`: Decrease A3 Offset threshold for 3218790_3
- `C19`: Decrease transmission power for 3218790_3
- `C20`: Adjust the azimuth of 3218790_3 by 36 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218790_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218790_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.810 | MS1 | 121.4656659185 | 31.1446298064 | 389 | 504990 | -90.08 | 17.36 | 551.16 | 0.02 | 2.98 | 1576 |
| 2024-09-20 22:21:32.147 | MS1 | 121.4656762233 | 31.1446225883 | 389 | 504990 | -90.12 | 17.97 | 331.40 | 0.06 | 2.52 | 1578 |
| 2024-09-20 22:21:33.751 | MS1 | 121.4656635039 | 31.1446277650 | 389 | 504990 | -91.95 | 15.08 | 573.09 | 0.18 | 2.09 | 1585 |
| 2024-09-20 22:21:34.908 | MS1 | 121.4656751174 | 31.1446195069 | 389 | 504990 | -86.80 | 16.11 | 50.25 | 0.65 | 2.76 | 693 |
| 2024-09-20 22:21:35.664 | MS1 | 121.4656745358 | 31.1446195059 | 389 | 504990 | -86.05 | 15.79 | 51.13 | 0.52 | 2.91 | 664 |
| 2024-09-20 22:21:36.494 | MS1 | 121.4656660452 | 31.1446186464 | 389 | 504990 | -90.37 | 14.13 | 58.97 | 0.59 | 2.31 | 571 |
| 2024-09-20 22:21:37.573 | MS1 | 121.4656707390 | 31.1446307300 | 389 | 504990 | -90.01 | 8.69 | 58.78 | 0.66 | 2.36 | 648 |
| 2024-09-20 22:21:38.150 | MS1 | 121.4656684038 | 31.1446250498 | 389 | 504990 | -89.53 | 8.40 | 90.90 | 0.67 | 2.83 | 605 |
| 2024-09-20 22:21:39.247 | MS1 | 121.4656721505 | 31.1446367495 | 389 | 504990 | -91.64 | 10.69 | 70.55 | 0.63 | 2.50 | 602 |
| 2024-09-20 22:21:40.807 | MS1 | 121.4656767114 | 31.1446191344 | 389 | 504990 | -90.11 | 8.23 | 491.48 | 0.10 | 2.42 | 1569 |
| 2024-09-20 22:21:41.130 | MS1 | 121.4656620275 | 31.1446209020 | 389 | 504990 | -90.21 | 10.65 | 418.58 | 0.17 | 2.68 | 1581 |
| 2024-09-20 22:21:42.109 | MS1 | 121.4656588947 | 31.1446308654 | 389 | 504990 | -93.58 | 10.03 | 583.42 | 0.04 | 2.98 | 1589 |

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
| 3218790 | 3 | 121.4745027975 | 31.1460851447 | 223 | 0 | 11 | 35.1 | TDD | 389 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3227372 | 2 | 121.4750808216 | 31.1471653062 | 93 | 0 | 7 | 19.7 | TDD | 453 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3270841 | 4 | 121.4759313702 | 31.1532719920 | 120 | 15 | 7 | 32.7 | TDD | 437 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3277314 | 1 | 121.4715053348 | 31.1536126133 | 274 | 15 | 11 | 16.2 | TDD | 140 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.976 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.001 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.138 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.138 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.820 | NREventA3 | measId:2;ServCellPCI:626;Se... |
| 2024-09-20 22:21:38.060 | NRHandoverAttempt | SourcePCI:626;SourceNR-ARFC... |
| 2024-09-20 22:21:38.091 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.102 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.207 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.207 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277314 | 1 | 18.0471 | 17.3108 | -114.3212 | 6.8053 | 190.8387 | 0.0162 | 0.0023 |
| 2024_09_20 22:00 | 3227372 | 2 | 9.1232 | 6.0814 | -116.6370 | 17.0696 | 182.0585 | 0.0019 | 0.0068 |
| 2024_09_20 22:00 | 3218790 | 3 | 18.8745 | 16.3207 | -116.7629 | 13.3382 | 84.9736 | 0.0129 | 0.0155 |
| 2024_09_20 22:00 | 3270841 | 4 | 16.4926 | 5.0116 | -114.4801 | 8.8872 | 92.6748 | 0.0079 | 0.0093 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416929_C4441CD1 | 504990 | 389 | -86.0 | 504990 | 437 | -90.2 | 504990 | 453 | -101.7 | 504990 | 140 |
| MR_1774416929_9D1E9063 | 504990 | 389 | -85.3 | 504990 | 437 | -89.6 | 504990 | 453 | -100.8 | 504990 | 140 |
| MR_1774416929_6171DE19 | 504990 | 389 | -85.4 | 504990 | 437 | -89.4 | 504990 | 453 | -99.7 | 504990 | 140 |
| MR_1774416929_64BACD14 | 504990 | 389 | -85.0 | 504990 | 437 | -90.0 | 504990 | 453 | -99.3 | 504990 | 140 |
| MR_1774416929_3DE9467B | 504990 | 389 | -88.4 | 504990 | 437 | -89.8 | 504990 | 453 | -100.2 | 504990 | 140 |
| MR_1774416929_EC5022D1 | 504990 | 389 | -87.3 | 504990 | 437 | -90.2 | 504990 | 453 | -102.9 | 504990 | 140 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 413: `06a1c19a-2f0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `06a1c19a-2f07-4255-8361-5aaffcafa190` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[413] topology](images/test_0413.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3270055_1 by 10 degrees
- `C2`: Decrease A3 Offset threshold for 3271659_4
- `C3`: Lift the tilt angle  of 3270055_1 by 10 degrees
- `C4`: Decrease A3 Offset threshold for 3270055_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271659_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271659_4
- `C7`: Increase A3 Offset threshold for 3270055_1
- `C8`: Press down the tilt angle of 3271659_4 by 10 degrees
- `C9`: Add neighbor relationship between 3271659_4 and 3270055_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270055_1
- `C11`: Increase transmission power for 3271659_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270055_1
- `C13`: Increase A3 Offset threshold for 3271659_4
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease transmission power for 3270055_1
- `C16`: Decrease transmission power for 3271659_4
- `C17`: Increase transmission power for 3270055_1
- `C18`: Add neighbor relationship between 3222333_3 and 3270055_1
- `C19`: Adjust the azimuth of 3271659_4 by 50 degrees
- `C20`: Adjust the azimuth of 3270055_1 by 48 degrees
- `C21`: Lift the tilt angle of 3271659_4 by 10 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.504 | MS1 | 121.4656624123 | 31.1446378128 | 495 | 504990 | -77.22 | 16.08 | 595.85 | 0.18 | 2.13 | 1580 |
| 2024-09-20 22:21:32.350 | MS1 | 121.4656744113 | 31.1446302084 | 495 | 504990 | -76.63 | 15.42 | 359.13 | 0.13 | 2.93 | 1598 |
| 2024-09-20 22:21:33.326 | MS1 | 121.4656667928 | 31.1446251577 | 495 | 504990 | -75.64 | 12.88 | 442.08 | 0.02 | 2.97 | 1574 |
| 2024-09-20 22:21:34.515 | MS1 | 121.4656698270 | 31.1446189845 | 495 | 504990 | -91.01 | -2.85 | 41.32 | 0.17 | 1.26 | 1566 |
| 2024-09-20 22:21:35.984 | MS1 | 121.4656660020 | 31.1446222656 | 495 | 504990 | -84.48 | -2.57 | 45.05 | 0.01 | 1.10 | 1586 |
| 2024-09-20 22:21:36.695 | MS1 | 121.4656689706 | 31.1446187628 | 495 | 504990 | -91.13 | -1.80 | 74.51 | 0.07 | 1.25 | 1574 |
| 2024-09-20 22:21:37.648 | MS1 | 121.4656710338 | 31.1446233122 | 495 | 504990 | -83.57 | -0.07 | 35.91 | 0.04 | 1.33 | 1581 |
| 2024-09-20 22:21:38.503 | MS1 | 121.4656711144 | 31.1446210628 | 495 | 504990 | -91.50 | -0.22 | 69.08 | 0.19 | 1.00 | 1582 |
| 2024-09-20 22:21:39.579 | MS1 | 121.4656612764 | 31.1446203713 | 916 | 504990 | -75.19 | 15.70 | 274.18 | 0.10 | 1.19 | 1588 |
| 2024-09-20 22:21:40.570 | MS1 | 121.4656727315 | 31.1446363445 | 916 | 504990 | -82.69 | 13.22 | 403.29 | 0.11 | 2.58 | 1571 |
| 2024-09-20 22:21:41.914 | MS1 | 121.4656777994 | 31.1446366695 | 916 | 504990 | -75.46 | 16.02 | 455.02 | 0.15 | 2.56 | 1563 |
| 2024-09-20 22:21:42.258 | MS1 | 121.4656702575 | 31.1446205313 | 916 | 504990 | -77.71 | 14.60 | 312.01 | 0.10 | 2.20 | 1576 |

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
| 3222333 | 3 | 121.4681874860 | 31.1557255628 | 3 | 13 | 0 | 35.9 | TDD | 60 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3251174 | 2 | 121.4670096749 | 31.1466734052 | 143 | 15 | 10 | 37.5 | TDD | 965 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3270055 | 1 | 121.4711810454 | 31.1497328516 | 175 | 9 | 7 | 47.3 | TDD | 916 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3271659 | 4 | 121.4678462328 | 31.1459241958 | 39 | 7 | 7 | 31.3 | TDD | 495 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.667 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.684 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.811 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.811 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.491 | NREventA3 | measId:2;ServCellPCI:40;Ser... |
| 2024-09-20 22:21:38.731 | NRHandoverAttempt | SourcePCI:40;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.771 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.781 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.923 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.923 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270055 | 1 | 17.1453 | 18.3151 | -117.6038 | 19.0786 | 158.0586 | 0.0160 | 0.0072 |
| 2024_09_20 22:00 | 3251174 | 2 | 8.3281 | 19.5767 | -115.2710 | 6.5711 | 167.7972 | 0.0085 | 0.0027 |
| 2024_09_20 22:00 | 3222333 | 3 | 13.2583 | 8.3187 | -117.7984 | 18.6881 | 129.5468 | 0.0157 | 0.0063 |
| 2024_09_20 22:00 | 3271659 | 4 | 18.1693 | 12.2272 | -117.5635 | 11.3958 | 169.5102 | 0.0020 | 0.1198 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412716_315A9097 | 504990 | 916 | -87.2 | 504990 | 495 | -90.9 | 504990 | 60 | -93.4 | 504990 | 965 |
| MR_1774412716_AAB51F44 | 504990 | 916 | -86.6 | 504990 | 495 | -91.1 | 504990 | 60 | -91.6 | 504990 | 965 |
| MR_1774412716_29BE9086 | 504990 | 495 | -90.1 | 504990 | 916 | -85.4 | 504990 | 60 | -92.2 | 504990 | 965 |
| MR_1774412716_FD194EB2 | 504990 | 495 | -90.0 | 504990 | 916 | -86.5 | 504990 | 60 | -93.5 | 504990 | 965 |
| MR_1774412716_86DC5C6B | 504990 | 495 | -89.7 | 504990 | 916 | -85.9 | 504990 | 60 | -91.6 | 504990 | 965 |
| MR_1774412716_F360D35C | 504990 | 495 | -89.5 | 504990 | 916 | -85.5 | 504990 | 60 | -93.8 | 504990 | 965 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 414: `7ae7f4a7-dbf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7ae7f4a7-dbfa-4300-8e22-827ac42f2cbd` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[414] topology](images/test_0414.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3254915_2 by 8 degrees
- `C2`: Lift the tilt angle of 3253887_3 by 3 degrees
- `C3`: Decrease A3 Offset threshold for 3253887_3
- `C4`: Check test server and transmission issues
- `C5`: Add neighbor relationship between 3237411_1 and 3254915_2
- `C6`: Lift the tilt angle  of 3254915_2 by 8 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253887_3
- `C8`: Increase A3 Offset threshold for 3253887_3
- `C9`: Increase transmission power for 3254915_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Adjust the azimuth of 3253887_3 by 50 degrees
- `C12`: Increase transmission power for 3253887_3
- `C13`: Add neighbor relationship between 3253887_3 and 3254915_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254915_2
- `C15`: Decrease transmission power for 3253887_3
- `C16`: Adjust the azimuth of 3254915_2 by 50 degrees
- `C17`: Decrease transmission power for 3254915_2
- `C18`: Increase A3 Offset threshold for 3254915_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253887_3
- `C20`: Decrease A3 Offset threshold for 3254915_2
- `C21`: Press down the tilt angle of 3253887_3 by 3 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254915_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.456 | MS1 | 121.4656725060 | 31.1446350759 | 60 | 504990 | -89.39 | 16.97 | 361.36 | 0.05 | 2.86 | 1588 |
| 2024-09-20 22:21:32.386 | MS1 | 121.4656659152 | 31.1446225204 | 60 | 504990 | -87.32 | 13.78 | 405.41 | 0.17 | 2.37 | 1594 |
| 2024-09-20 22:21:33.647 | MS1 | 121.4656604150 | 31.1446296701 | 60 | 504990 | -86.14 | 17.79 | 487.63 | 0.03 | 2.37 | 1580 |
| 2024-09-20 22:21:34.353 | MS1 | 121.4656679097 | 31.1446321386 | 60 | 504990 | -86.14 | 13.77 | 62.18 | 0.07 | 2.85 | 488 |
| 2024-09-20 22:21:35.675 | MS1 | 121.4656746954 | 31.1446255147 | 60 | 504990 | -90.06 | 15.17 | 83.48 | 0.04 | 2.42 | 303 |
| 2024-09-20 22:21:36.245 | MS1 | 121.4656594489 | 31.1446232488 | 60 | 504990 | -86.00 | 12.27 | 68.57 | 0.12 | 2.03 | 349 |
| 2024-09-20 22:21:37.673 | MS1 | 121.4656609308 | 31.1446274715 | 60 | 504990 | -90.32 | 12.90 | 80.74 | 0.20 | 2.69 | 402 |
| 2024-09-20 22:21:38.554 | MS1 | 121.4656744090 | 31.1446253509 | 60 | 504990 | -89.50 | 10.64 | 96.45 | 0.02 | 2.99 | 449 |
| 2024-09-20 22:21:39.725 | MS1 | 121.4656683518 | 31.1446316964 | 60 | 504990 | -89.83 | 12.30 | 101.76 | 0.17 | 2.79 | 381 |
| 2024-09-20 22:21:40.862 | MS1 | 121.4656717266 | 31.1446295734 | 60 | 504990 | -92.17 | 9.07 | 446.13 | 0.11 | 2.56 | 1577 |
| 2024-09-20 22:21:41.837 | MS1 | 121.4656603040 | 31.1446329784 | 60 | 504990 | -91.18 | 10.70 | 310.47 | 0.04 | 2.73 | 1581 |
| 2024-09-20 22:21:42.102 | MS1 | 121.4656589519 | 31.1446201263 | 60 | 504990 | -89.19 | 10.47 | 451.65 | 0.09 | 2.52 | 1565 |

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
| 3224421 | 4 | 121.4690443784 | 31.1500380146 | 48 | 14 | 8 | 20.0 | TDD | 412 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3237411 | 1 | 121.4675388864 | 31.1458146708 | 62 | 11 | 9 | 36.3 | TDD | 625 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3253887 | 3 | 121.4756696059 | 31.1455892372 | 142 | 2 | 8 | 24.0 | TDD | 60 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3254915 | 2 | 121.4656160010 | 31.1496969268 | 276 | 6 | 12 | 17.7 | TDD | 555 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.437 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.452 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.576 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.576 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.319 | NREventA3 | measId:2;ServCellPCI:548;Se... |
| 2024-09-20 22:21:38.559 | NRHandoverAttempt | SourcePCI:548;SourceNR-ARFC... |
| 2024-09-20 22:21:38.591 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.604 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.716 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.716 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237411 | 1 | 19.0290 | 17.2578 | -116.8155 | 14.9556 | 81.6120 | 0.0052 | 0.0173 |
| 2024_09_20 22:00 | 3254915 | 2 | 10.0443 | 14.9192 | -115.9141 | 8.0969 | 124.6607 | 0.0083 | 0.0136 |
| 2024_09_20 22:00 | 3253887 | 3 | 12.3570 | 13.6956 | -115.9099 | 10.3497 | 171.2407 | 0.0153 | 0.0104 |
| 2024_09_20 22:00 | 3224421 | 4 | 17.8632 | 12.2116 | -117.0849 | 6.2254 | 172.0718 | 0.0073 | 0.0188 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415132_672B28F7 | 504990 | 60 | -87.5 | 504990 | 555 | -85.2 | 504990 | 625 | -98.8 | 504990 | 412 |
| MR_1774415132_23A6540D | 504990 | 60 | -86.1 | 504990 | 555 | -86.3 | 504990 | 625 | -101.1 | 504990 | 412 |
| MR_1774415132_B00FFA5F | 504990 | 60 | -84.2 | 504990 | 555 | -87.9 | 504990 | 625 | -100.4 | 504990 | 412 |
| MR_1774415132_72A90A04 | 504990 | 60 | -85.5 | 504990 | 555 | -87.7 | 504990 | 625 | -98.9 | 504990 | 412 |
| MR_1774415132_5780B88C | 504990 | 60 | -86.6 | 504990 | 555 | -86.5 | 504990 | 625 | -100.1 | 504990 | 412 |
| MR_1774415132_63545D1B | 504990 | 60 | -84.2 | 504990 | 555 | -87.9 | 504990 | 625 | -101.8 | 504990 | 412 |
| MR_1774415132_B6A2A4F2 | 504990 | 60 | -87.7 | 504990 | 555 | -89.0 | 504990 | 625 | -99.1 | 504990 | 412 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 415: `56f0c845-88f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `56f0c845-88f6-4e85-bad6-2bee62524801` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[415] topology](images/test_0415.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250096_4
- `C2`: Adjust the azimuth of 3269315_3 by 12 degrees
- `C3`: Decrease transmission power for 3269315_3
- `C4`: Increase transmission power for 3250096_4
- `C5`: Press down the tilt angle of 3250096_4 by 8 degrees
- `C6`: Decrease transmission power for 3250096_4
- `C7`: Increase transmission power for 3269315_3
- `C8`: Add neighbor relationship between 3214923_1 and 3269315_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250096_4
- `C10`: Press down the tilt angle  of 3269315_3 by 1 degrees
- `C11`: Decrease A3 Offset threshold for 3269315_3
- `C12`: Lift the tilt angle of 3250096_4 by 8 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269315_3
- `C14`: Increase A3 Offset threshold for 3250096_4
- `C15`: Check test server and transmission issues
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269315_3
- `C17`: Increase A3 Offset threshold for 3269315_3
- `C18`: Decrease A3 Offset threshold for 3250096_4
- `C19`: Adjust the azimuth of 3250096_4 by 50 degrees
- `C20`: Add neighbor relationship between 3250096_4 and 3269315_3
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Lift the tilt angle  of 3269315_3 by 1 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.646 | MS1 | 121.4656604621 | 31.1446192184 | 399 | 504990 | -83.10 | 15.72 | 423.39 | 0.19 | 2.96 | 1579 |
| 2024-09-20 22:21:32.762 | MS1 | 121.4656623240 | 31.1446225676 | 399 | 504990 | -81.16 | 16.94 | 311.58 | 0.13 | 2.88 | 1595 |
| 2024-09-20 22:21:33.488 | MS1 | 121.4656641940 | 31.1446295207 | 399 | 504990 | -81.01 | 12.69 | 563.29 | 0.07 | 2.62 | 1600 |
| 2024-09-20 22:21:34.704 | MS1 | 121.4656592931 | 31.1446180249 | 399 | 504990 | -87.08 | -0.97 | 41.37 | 0.02 | 1.45 | 1577 |
| 2024-09-20 22:21:35.380 | MS1 | 121.4656620950 | 31.1446298985 | 399 | 504990 | -88.36 | -2.64 | 35.06 | 0.05 | 1.28 | 1582 |
| 2024-09-20 22:21:36.817 | MS1 | 121.4656585959 | 31.1446215169 | 399 | 504990 | -91.15 | -0.68 | 23.07 | 0.17 | 1.13 | 1583 |
| 2024-09-20 22:21:37.475 | MS1 | 121.4656643078 | 31.1446273997 | 399 | 504990 | -85.39 | -1.70 | 27.10 | 0.00 | 1.32 | 1564 |
| 2024-09-20 22:21:38.940 | MS1 | 121.4656623488 | 31.1446304043 | 399 | 504990 | -83.49 | 16.14 | 526.16 | 0.11 | 1.13 | 1588 |
| 2024-09-20 22:21:39.954 | MS1 | 121.4656715941 | 31.1446240037 | 399 | 504990 | -76.40 | 14.90 | 427.63 | 0.14 | 1.25 | 1593 |
| 2024-09-20 22:21:40.623 | MS1 | 121.4656690761 | 31.1446303297 | 399 | 504990 | -83.07 | 13.90 | 303.90 | 0.08 | 2.19 | 1597 |
| 2024-09-20 22:21:41.949 | MS1 | 121.4656596902 | 31.1446199429 | 399 | 504990 | -79.57 | 12.59 | 455.84 | 0.17 | 2.85 | 1599 |
| 2024-09-20 22:21:42.770 | MS1 | 121.4656606590 | 31.1446204255 | 399 | 504990 | -79.67 | 17.28 | 427.60 | 0.15 | 2.44 | 1580 |

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
| 3214923 | 1 | 121.4747888327 | 31.1517728236 | 269 | 11 | 7 | 30.8 | TDD | 978 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3233551 | 2 | 121.4646813738 | 31.1443278848 | 206 | 4 | 7 | 17.4 | TDD | 36 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3250096 | 4 | 121.4755201557 | 31.1443272569 | 220 | 5 | 3 | 41.1 | TDD | 399 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3269315 | 3 | 121.4689352482 | 31.1552903528 | 207 | 0 | 1 | 17.7 | TDD | 90 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.395 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.412 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.560 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.560 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.240 | NREventA3 | measId:2;ServCellPCI:759;Se... |
| 2024-09-20 22:21:36.240 | NREventA3 | measId:2;ServCellPCI:759;Se... |
| 2024-09-20 22:21:37.240 | NREventA3 | measId:2;ServCellPCI:759;Se... |
| 2024-09-20 22:21:39.740 | NRRRCReestablishAttempt | PCI:759 |
| 2024-09-20 22:21:39.756 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.767 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.897 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.897 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214923 | 1 | 9.2720 | 6.9123 | -114.0904 | 19.7961 | 182.8075 | 0.0040 | 0.0042 |
| 2024_09_20 22:00 | 3233551 | 2 | 8.8859 | 18.2306 | -114.3941 | 13.7095 | 125.0812 | 0.0177 | 0.0123 |
| 2024_09_20 22:00 | 3269315 | 3 | 9.8034 | 18.5210 | -114.0479 | 6.6028 | 168.4567 | 0.0192 | 0.0069 |
| 2024_09_20 22:00 | 3250096 | 4 | 6.2912 | 11.9892 | -116.8844 | 6.9587 | 182.9274 | 0.0155 | 0.1269 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412429_9C723A32 | 504990 | 399 | -88.4 | 504990 | 90 | -81.8 | 504990 | 978 | -89.9 | 504990 | 36 |
| MR_1774412429_2795E56E | 504990 | 399 | -86.3 | 504990 | 90 | -80.7 | 504990 | 978 | -92.6 | 504990 | 36 |
| MR_1774412429_E1004F90 | 504990 | 399 | -86.5 | 504990 | 90 | -80.4 | 504990 | 978 | -92.4 | 504990 | 36 |
| MR_1774412429_ECAFCCFE | 504990 | 399 | -89.0 | 504990 | 90 | -81.9 | 504990 | 978 | -92.6 | 504990 | 36 |
| MR_1774412429_A814B44D | 504990 | 90 | -80.4 | 504990 | 399 | -87.8 | 504990 | 978 | -89.8 | 504990 | 36 |
| MR_1774412429_F6B3FFAE | 504990 | 399 | -86.6 | 504990 | 90 | -81.3 | 504990 | 978 | -90.8 | 504990 | 36 |
| MR_1774412429_BA7E6F2A | 504990 | 399 | -86.5 | 504990 | 90 | -81.4 | 504990 | 978 | -92.9 | 504990 | 36 |
| MR_1774412429_42E9601B | 504990 | 399 | -87.0 | 504990 | 90 | -82.0 | 504990 | 978 | -90.7 | 504990 | 36 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 416: `113b97c5-e23...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `113b97c5-e231-4e88-bc81-7831b869771f` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[416] topology](images/test_0416.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3270836_4
- `C2`: Decrease transmission power for 3260895_2
- `C3`: Lift the tilt angle of 3260895_2 by 9 degrees
- `C4`: Adjust the azimuth of 3260895_2 by 50 degrees
- `C5`: Check test server and transmission issues
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270836_4
- `C8`: Press down the tilt angle  of 3270836_4 by 3 degrees
- `C9`: Add neighbor relationship between 3260895_2 and 3270836_4
- `C10`: Adjust the azimuth of 3270836_4 by 50 degrees
- `C11`: Increase transmission power for 3270836_4
- `C12`: Increase A3 Offset threshold for 3270836_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270836_4
- `C14`: Increase transmission power for 3260895_2
- `C15`: Decrease A3 Offset threshold for 3270836_4
- `C16`: Increase A3 Offset threshold for 3260895_2
- `C17`: Decrease A3 Offset threshold for 3260895_2
- `C18`: Press down the tilt angle of 3260895_2 by 9 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260895_2
- `C20`: Lift the tilt angle  of 3270836_4 by 3 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260895_2
- `C22`: Add neighbor relationship between 3240152_3 and 3270836_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.274 | MS1 | 121.4656598153 | 31.1446346014 | 551 | 504990 | -77.54 | 15.21 | 322.97 | 0.17 | 2.84 | 1584 |
| 2024-09-20 22:21:32.134 | MS1 | 121.4656595227 | 31.1446193431 | 551 | 504990 | -78.01 | 12.75 | 551.23 | 0.00 | 2.12 | 1562 |
| 2024-09-20 22:21:33.553 | MS1 | 121.4656662726 | 31.1446363635 | 551 | 504990 | -76.17 | 15.86 | 498.32 | 0.15 | 2.19 | 1564 |
| 2024-09-20 22:21:34.472 | MS1 | 121.4656607816 | 31.1446253738 | 551 | 504990 | -92.15 | -0.06 | 31.27 | 0.03 | 1.44 | 1599 |
| 2024-09-20 22:21:35.833 | MS1 | 121.4656762848 | 31.1446257389 | 551 | 504990 | -83.62 | -0.03 | 38.91 | 0.13 | 1.15 | 1562 |
| 2024-09-20 22:21:36.796 | MS1 | 121.4656755624 | 31.1446207546 | 551 | 504990 | -85.14 | -0.14 | 38.56 | 0.16 | 1.39 | 1597 |
| 2024-09-20 22:21:37.924 | MS1 | 121.4656606033 | 31.1446364609 | 551 | 504990 | -88.41 | -3.20 | 41.28 | 0.12 | 1.12 | 1563 |
| 2024-09-20 22:21:38.449 | MS1 | 121.4656581864 | 31.1446346375 | 551 | 504990 | -83.83 | -2.23 | 49.83 | 0.01 | 1.45 | 1565 |
| 2024-09-20 22:21:39.173 | MS1 | 121.4656709116 | 31.1446215424 | 535 | 504990 | -83.39 | 12.26 | 180.03 | 0.02 | 1.09 | 1586 |
| 2024-09-20 22:21:40.336 | MS1 | 121.4656665641 | 31.1446236082 | 535 | 504990 | -80.70 | 13.89 | 342.10 | 0.19 | 2.47 | 1569 |
| 2024-09-20 22:21:41.391 | MS1 | 121.4656656344 | 31.1446347318 | 535 | 504990 | -82.56 | 14.42 | 599.70 | 0.18 | 2.66 | 1594 |
| 2024-09-20 22:21:42.546 | MS1 | 121.4656765926 | 31.1446246321 | 535 | 504990 | -79.29 | 12.81 | 576.97 | 0.15 | 2.89 | 1596 |

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
| 3240152 | 3 | 121.4690280287 | 31.1487574649 | 163 | 11 | 4 | 28.5 | TDD | 229 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3260895 | 2 | 121.4709182864 | 31.1484359693 | 40 | 5 | 0 | 48.2 | TDD | 551 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3270836 | 4 | 121.4743048327 | 31.1521808504 | 26 | 2 | 4 | 17.0 | TDD | 535 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3275656 | 1 | 121.4663791791 | 31.1507587894 | 107 | 9 | 3 | 48.0 | TDD | 497 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.796 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.816 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.936 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.936 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.633 | NREventA3 | measId:2;ServCellPCI:888;Se... |
| 2024-09-20 22:21:37.873 | NRHandoverAttempt | SourcePCI:888;SourceNR-ARFC... |
| 2024-09-20 22:21:37.918 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.932 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.039 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.039 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275656 | 1 | 16.0367 | 12.3512 | -117.0044 | 19.1716 | 199.0179 | 0.0074 | 0.0064 |
| 2024_09_20 22:00 | 3260895 | 2 | 15.6489 | 9.7738 | -117.8362 | 19.0078 | 85.9620 | 0.0035 | 0.1253 |
| 2024_09_20 22:00 | 3240152 | 3 | 19.1538 | 14.0895 | -115.2254 | 9.8983 | 90.1522 | 0.0015 | 0.0021 |
| 2024_09_20 22:00 | 3270836 | 4 | 9.2004 | 10.6623 | -117.0884 | 13.1594 | 86.6320 | 0.0031 | 0.0159 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414708_2C36C178 | 504990 | 551 | -93.4 | 504990 | 535 | -87.7 | 504990 | 229 | -85.9 | 504990 | 497 |
| MR_1774414708_5CE9B9C7 | 504990 | 551 | -90.8 | 504990 | 535 | -87.2 | 504990 | 229 | -89.0 | 504990 | 497 |
| MR_1774414708_870EC8D5 | 504990 | 535 | -86.7 | 504990 | 551 | -91.6 | 504990 | 229 | -88.0 | 504990 | 497 |
| MR_1774414708_EF3BCCE5 | 504990 | 535 | -87.0 | 504990 | 551 | -90.6 | 504990 | 229 | -88.8 | 504990 | 497 |
| MR_1774414708_4EF32F01 | 504990 | 535 | -86.2 | 504990 | 551 | -93.5 | 504990 | 229 | -88.1 | 504990 | 497 |
| MR_1774414708_E1B90696 | 504990 | 551 | -91.7 | 504990 | 535 | -87.1 | 504990 | 229 | -89.6 | 504990 | 497 |
| MR_1774414708_E254C5EF | 504990 | 551 | -93.4 | 504990 | 535 | -87.4 | 504990 | 229 | -86.5 | 504990 | 497 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 417: `4866d7bf-6bb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4866d7bf-6bbb-40e6-9ab0-616e44e5de3e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[417] topology](images/test_0417.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3222154_2
- `C2`: Lift the tilt angle  of 3270604_1 by 10 degrees
- `C3`: Decrease A3 Offset threshold for 3270604_1
- `C4`: Decrease transmission power for 3222154_2
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270604_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222154_2
- `C8`: Press down the tilt angle  of 3270604_1 by 10 degrees
- `C9`: Add neighbor relationship between 3245431_3 and 3270604_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222154_2
- `C11`: Increase A3 Offset threshold for 3270604_1
- `C12`: Increase transmission power for 3270604_1
- `C13`: Check test server and transmission issues
- `C14`: Decrease transmission power for 3270604_1
- `C15`: Adjust the azimuth of 3270604_1 by 14 degrees
- `C16`: Lift the tilt angle of 3222154_2 by 10 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270604_1
- `C18`: Decrease A3 Offset threshold for 3222154_2
- `C19`: Adjust the azimuth of 3222154_2 by 50 degrees
- `C20`: Add neighbor relationship between 3222154_2 and 3270604_1
- `C21`: Press down the tilt angle of 3222154_2 by 10 degrees
- `C22`: Increase transmission power for 3222154_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.513 | MS1 | 121.4656686013 | 31.1446200310 | 331 | 504990 | -76.98 | 15.34 | 531.00 | 0.09 | 2.71 | 1561 |
| 2024-09-20 22:21:32.857 | MS1 | 121.4656678773 | 31.1446298626 | 331 | 504990 | -77.39 | 16.95 | 443.58 | 0.04 | 2.31 | 1584 |
| 2024-09-20 22:21:33.733 | MS1 | 121.4656718011 | 31.1446346965 | 331 | 504990 | -84.13 | 13.95 | 314.90 | 0.14 | 2.72 | 1575 |
| 2024-09-20 22:21:34.400 | MS1 | 121.4656681127 | 31.1446286454 | 331 | 504990 | -89.12 | -1.14 | 55.02 | 0.16 | 1.39 | 1589 |
| 2024-09-20 22:21:35.799 | MS1 | 121.4656586216 | 31.1446241790 | 331 | 504990 | -85.00 | -2.72 | 46.73 | 0.07 | 1.02 | 1600 |
| 2024-09-20 22:21:36.969 | MS1 | 121.4656674922 | 31.1446365930 | 331 | 504990 | -91.04 | -0.06 | 43.54 | 0.19 | 1.32 | 1586 |
| 2024-09-20 22:21:37.188 | MS1 | 121.4656751660 | 31.1446312937 | 331 | 504990 | -88.92 | -0.42 | 33.69 | 0.08 | 1.49 | 1572 |
| 2024-09-20 22:21:38.435 | MS1 | 121.4656618083 | 31.1446317414 | 331 | 504990 | -87.71 | -3.70 | 64.61 | 0.03 | 1.10 | 1569 |
| 2024-09-20 22:21:39.646 | MS1 | 121.4656637861 | 31.1446240865 | 576 | 504990 | -75.23 | 17.33 | 260.05 | 0.19 | 1.32 | 1562 |
| 2024-09-20 22:21:40.939 | MS1 | 121.4656723581 | 31.1446233938 | 576 | 504990 | -77.93 | 15.37 | 343.46 | 0.18 | 2.13 | 1567 |
| 2024-09-20 22:21:41.858 | MS1 | 121.4656735789 | 31.1446323065 | 576 | 504990 | -81.14 | 16.81 | 382.53 | 0.05 | 2.94 | 1572 |
| 2024-09-20 22:21:42.168 | MS1 | 121.4656585135 | 31.1446180491 | 576 | 504990 | -78.01 | 13.66 | 561.12 | 0.19 | 2.55 | 1595 |

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
| 3220055 | 4 | 121.4725058993 | 31.1449979028 | 330 | 4 | 12 | 27.8 | TDD | 902 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3222154 | 2 | 121.4716269268 | 31.1488604079 | 88 | 13 | 7 | 40.2 | TDD | 331 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3245431 | 3 | 121.4714487513 | 31.1447112276 | 271 | 12 | 0 | 18.3 | TDD | 77 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3270604 | 1 | 121.4750510943 | 31.1519078756 | 214 | 11 | 10 | 27.9 | TDD | 576 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.612 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.630 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.773 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.773 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.477 | NREventA3 | measId:2;ServCellPCI:382;Se... |
| 2024-09-20 22:21:38.717 | NRHandoverAttempt | SourcePCI:382;SourceNR-ARFC... |
| 2024-09-20 22:21:38.759 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.769 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.898 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.898 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270604 | 1 | 16.1101 | 13.5817 | -115.2685 | 18.6106 | 148.6512 | 0.0171 | 0.0171 |
| 2024_09_20 22:00 | 3222154 | 2 | 12.6175 | 12.5378 | -117.1700 | 8.3370 | 138.0810 | 0.0018 | 0.1541 |
| 2024_09_20 22:00 | 3245431 | 3 | 5.5193 | 19.0875 | -116.8306 | 15.0997 | 174.6448 | 0.0167 | 0.0026 |
| 2024_09_20 22:00 | 3220055 | 4 | 16.7182 | 17.0844 | -117.3689 | 9.7249 | 112.0454 | 0.0103 | 0.0153 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413650_2E346E18 | 504990 | 576 | -84.0 | 504990 | 331 | -89.7 | 504990 | 77 | -84.5 | 504990 | 902 |
| MR_1774413650_FD174DDF | 504990 | 331 | -88.8 | 504990 | 576 | -83.1 | 504990 | 77 | -83.5 | 504990 | 902 |
| MR_1774413650_68EC051B | 504990 | 576 | -81.3 | 504990 | 331 | -87.8 | 504990 | 77 | -85.8 | 504990 | 902 |
| MR_1774413650_C2C56AA4 | 504990 | 576 | -84.1 | 504990 | 331 | -87.9 | 504990 | 77 | -83.0 | 504990 | 902 |
| MR_1774413650_16016D39 | 504990 | 576 | -83.8 | 504990 | 331 | -87.6 | 504990 | 77 | -83.4 | 504990 | 902 |
| MR_1774413650_9C780864 | 504990 | 576 | -81.4 | 504990 | 331 | -88.8 | 504990 | 77 | -85.3 | 504990 | 902 |
| MR_1774413650_7EBA156C | 504990 | 331 | -90.8 | 504990 | 576 | -83.3 | 504990 | 77 | -84.6 | 504990 | 902 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 418: `f83c3a67-108...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f83c3a67-1086-4156-a6ae-6f970c4e1849` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[418] topology](images/test_0418.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3216186_2
- `C2`: Increase A3 Offset threshold for 3227807_4
- `C3`: Press down the tilt angle of 3227807_4 by 5 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216186_2
- `C5`: Lift the tilt angle  of 3216186_2 by 2 degrees
- `C6`: Lift the tilt angle of 3227807_4 by 5 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227807_4
- `C8`: Adjust the azimuth of 3216186_2 by 16 degrees
- `C9`: Add neighbor relationship between 3255037_1 and 3216186_2
- `C10`: Decrease A3 Offset threshold for 3227807_4
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Adjust the azimuth of 3227807_4 by 50 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216186_2
- `C14`: Press down the tilt angle  of 3216186_2 by 2 degrees
- `C15`: Add neighbor relationship between 3227807_4 and 3216186_2
- `C16`: Increase transmission power for 3227807_4
- `C17`: Increase transmission power for 3216186_2
- `C18`: Increase A3 Offset threshold for 3216186_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227807_4
- `C20`: Check test server and transmission issues
- `C21`: Decrease transmission power for 3216186_2
- `C22`: Decrease transmission power for 3227807_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.778 | MS1 | 121.4656717206 | 31.1446212704 | 244 | 504990 | -79.70 | 14.22 | 411.83 | 0.01 | 2.01 | 1585 |
| 2024-09-20 22:21:32.110 | MS1 | 121.4656628034 | 31.1446205633 | 244 | 504990 | -79.30 | 15.62 | 335.91 | 0.14 | 2.55 | 1597 |
| 2024-09-20 22:21:33.867 | MS1 | 121.4656684481 | 31.1446358710 | 244 | 504990 | -75.91 | 17.16 | 350.66 | 0.07 | 2.48 | 1572 |
| 2024-09-20 22:21:34.303 | MS1 | 121.4656642986 | 31.1446277970 | 244 | 504990 | -90.41 | -0.50 | 63.65 | 0.12 | 1.36 | 1598 |
| 2024-09-20 22:21:35.360 | MS1 | 121.4656770631 | 31.1446193051 | 244 | 504990 | -86.36 | -0.46 | 30.56 | 0.05 | 1.25 | 1565 |
| 2024-09-20 22:21:36.908 | MS1 | 121.4656587656 | 31.1446255511 | 244 | 504990 | -88.87 | -0.73 | 58.47 | 0.04 | 1.28 | 1593 |
| 2024-09-20 22:21:37.117 | MS1 | 121.4656717631 | 31.1446269954 | 244 | 504990 | -88.10 | -2.04 | 24.32 | 0.10 | 1.45 | 1583 |
| 2024-09-20 22:21:38.754 | MS1 | 121.4656727932 | 31.1446321748 | 244 | 504990 | -83.46 | 12.22 | 356.55 | 0.01 | 1.26 | 1568 |
| 2024-09-20 22:21:39.955 | MS1 | 121.4656647028 | 31.1446316294 | 244 | 504990 | -79.99 | 14.35 | 523.35 | 0.13 | 1.24 | 1563 |
| 2024-09-20 22:21:40.820 | MS1 | 121.4656618197 | 31.1446239702 | 244 | 504990 | -84.89 | 14.76 | 361.23 | 0.08 | 2.39 | 1587 |
| 2024-09-20 22:21:41.107 | MS1 | 121.4656749971 | 31.1446379487 | 244 | 504990 | -77.58 | 16.50 | 458.26 | 0.18 | 2.29 | 1570 |
| 2024-09-20 22:21:42.568 | MS1 | 121.4656582873 | 31.1446200278 | 244 | 504990 | -75.71 | 12.15 | 413.21 | 0.08 | 2.63 | 1567 |

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
| 3216186 | 2 | 121.4720417331 | 31.1551034763 | 191 | 1 | 9 | 25.5 | TDD | 657 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3227807 | 4 | 121.4709170797 | 31.1459673768 | 322 | 0 | 7 | 49.3 | TDD | 244 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3242205 | 3 | 121.4659491884 | 31.1484648797 | 99 | 8 | 5 | 28.2 | TDD | 938 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3255037 | 1 | 121.4750263213 | 31.1536436132 | 177 | 5 | 6 | 26.8 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.873 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.892 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.037 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.037 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.735 | NREventA3 | measId:2;ServCellPCI:292;Se... |
| 2024-09-20 22:21:35.735 | NREventA3 | measId:2;ServCellPCI:292;Se... |
| 2024-09-20 22:21:36.735 | NREventA3 | measId:2;ServCellPCI:292;Se... |
| 2024-09-20 22:21:39.235 | NRRRCReestablishAttempt | PCI:292 |
| 2024-09-20 22:21:39.245 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.258 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.401 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.401 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255037 | 1 | 12.7084 | 10.5573 | -115.3199 | 7.5243 | 134.5932 | 0.0031 | 0.0096 |
| 2024_09_20 22:00 | 3216186 | 2 | 14.8450 | 6.1688 | -115.8414 | 14.0204 | 166.9076 | 0.0086 | 0.0114 |
| 2024_09_20 22:00 | 3242205 | 3 | 13.8344 | 14.0809 | -116.0656 | 7.7537 | 87.5113 | 0.0062 | 0.0087 |
| 2024_09_20 22:00 | 3227807 | 4 | 19.4686 | 14.8360 | -114.5922 | 18.5301 | 126.3767 | 0.0198 | 0.1181 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414279_7FDE1154 | 504990 | 244 | -92.3 | 504990 | 657 | -86.9 | 504990 | 176 | -89.8 | 504990 | 938 |
| MR_1774414279_8CF38218 | 504990 | 244 | -89.3 | 504990 | 657 | -87.9 | 504990 | 176 | -91.6 | 504990 | 938 |
| MR_1774414279_9182D2A1 | 504990 | 244 | -88.6 | 504990 | 657 | -87.0 | 504990 | 176 | -92.8 | 504990 | 938 |
| MR_1774414279_BFB3458E | 504990 | 244 | -89.3 | 504990 | 657 | -84.9 | 504990 | 176 | -90.8 | 504990 | 938 |
| MR_1774414279_C17DF46B | 504990 | 244 | -88.9 | 504990 | 657 | -86.9 | 504990 | 176 | -89.7 | 504990 | 938 |
| MR_1774414279_5B2B082C | 504990 | 657 | -86.9 | 504990 | 244 | -91.7 | 504990 | 176 | -92.9 | 504990 | 938 |
| MR_1774414279_B7285CFF | 504990 | 657 | -87.8 | 504990 | 244 | -91.3 | 504990 | 176 | -89.8 | 504990 | 938 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 419: `852494de-d19...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `852494de-d192-4edc-b0f8-42475a4d8e4b` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[419] topology](images/test_0419.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3255037_3 and 3277312_4
- `C2`: Adjust the azimuth of 3255037_3 by 50 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease A3 Offset threshold for 3248945_2
- `C5`: Add neighbor relationship between 3248945_2 and 3277312_4
- `C6`: Increase A3 Offset threshold for 3277312_4
- `C7`: Lift the tilt angle  of 3255037_3 by 10 degrees
- `C8`: Lift the tilt angle of 3248945_2 by 1 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277312_4
- `C10`: Decrease transmission power for 3248945_2
- `C11`: Press down the tilt angle of 3248945_2 by 1 degrees
- `C12`: Decrease transmission power for 3277312_4
- `C13`: Decrease A3 Offset threshold for 3277312_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277312_4
- `C15`: Increase transmission power for 3277312_4
- `C16`: Check test server and transmission issues
- `C17`: Press down the tilt angle  of 3255037_3 by 10 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248945_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248945_2
- `C20`: Increase A3 Offset threshold for 3248945_2
- `C21`: Adjust the azimuth of 3248945_2 by 13 degrees
- `C22`: Increase transmission power for 3248945_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.548 | MS1 | 121.4656640182 | 31.1446214173 | 989 | 504990 | -90.10 | 15.09 | 402.94 | 0.18 | 2.86 | 1595 |
| 2024-09-20 22:21:32.237 | MS1 | 121.4656640457 | 31.1446286444 | 989 | 504990 | -90.83 | 16.70 | 413.43 | 0.11 | 2.91 | 1560 |
| 2024-09-20 22:21:33.234 | MS1 | 121.4656677036 | 31.1446214631 | 989 | 504990 | -91.94 | 12.80 | 571.25 | 0.13 | 2.89 | 1586 |
| 2024-09-20 22:21:34.774 | MS1 | 121.4656678147 | 31.1446204819 | 989 | 504990 | -89.91 | 16.25 | 60.80 | 0.05 | 2.63 | 1588 |
| 2024-09-20 22:21:35.339 | MS1 | 121.4656770310 | 31.1446306932 | 989 | 504990 | -90.98 | 17.76 | 63.65 | 0.16 | 2.66 | 1581 |
| 2024-09-20 22:21:36.196 | MS1 | 121.4656765337 | 31.1446329787 | 989 | 504990 | -91.52 | 13.97 | 80.54 | 0.18 | 2.32 | 1599 |
| 2024-09-20 22:21:37.590 | MS1 | 121.4656765866 | 31.1446342193 | 989 | 504990 | -92.00 | 10.21 | 61.02 | 0.15 | 2.72 | 1590 |
| 2024-09-20 22:21:38.249 | MS1 | 121.4656661785 | 31.1446207137 | 989 | 504990 | -91.09 | 9.69 | 103.90 | 0.03 | 2.81 | 1598 |
| 2024-09-20 22:21:39.192 | MS1 | 121.4656741313 | 31.1446223933 | 989 | 504990 | -90.94 | 11.83 | 72.67 | 0.06 | 2.08 | 1585 |
| 2024-09-20 22:21:40.912 | MS1 | 121.4656743340 | 31.1446343639 | 989 | 504990 | -91.52 | 9.99 | 333.40 | 0.14 | 2.64 | 1595 |
| 2024-09-20 22:21:41.496 | MS1 | 121.4656777117 | 31.1446305761 | 989 | 504990 | -90.99 | 12.73 | 475.37 | 0.18 | 2.98 | 1570 |
| 2024-09-20 22:21:42.693 | MS1 | 121.4656723420 | 31.1446286580 | 989 | 504990 | -89.07 | 10.01 | 344.43 | 0.11 | 2.23 | 1570 |

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
| 3228572 | 1 | 121.4649253151 | 31.1512398036 | 260 | 14 | 8 | 21.6 | TDD | 640 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3248945 | 2 | 121.4640712266 | 31.1559659353 | 160 | 0 | 7 | 20.6 | TDD | 989 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3255037 | 3 | 121.4709099378 | 31.1516823099 | 0 | 7 | 4 | 37.6 | TDD | 94 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3277312 | 4 | 121.4658283130 | 31.1449386561 | 138 | 6 | 4 | 37.7 | TDD | 631 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.798 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.814 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:30.938 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.938 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.650 | NREventA3 | measId:2;ServCellPCI:123;Se... |
| 2024-09-20 22:21:37.890 | NRHandoverAttempt | SourcePCI:123;SourceNR-ARFC... |
| 2024-09-20 22:21:37.930 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.945 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.045 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.045 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228572 | 1 | 15.3592 | 8.0860 | -117.1728 | 12.8032 | 170.2142 | 0.0039 | 0.0053 |
| 2024_09_20 22:00 | 3248945 | 2 | 90.3727 | 76.5995 | -117.1012 | 19.2307 | 176.8856 | 0.0105 | 0.0029 |
| 2024_09_20 22:00 | 3255037 | 3 | 14.7394 | 18.3836 | -117.9097 | 15.6979 | 196.1501 | 0.0070 | 0.0035 |
| 2024_09_20 22:00 | 3277312 | 4 | 19.9290 | 10.2388 | -114.8426 | 8.1494 | 141.6489 | 0.0200 | 0.0111 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412232_82133193 | 504990 | 989 | -89.0 | 504990 | 631 | -101.1 | 504990 | 94 | -102.5 | 504990 | 640 |
| MR_1774412232_3D6702F5 | 504990 | 989 | -88.4 | 504990 | 631 | -98.3 | 504990 | 94 | -103.6 | 504990 | 640 |
| MR_1774412232_960072EF | 504990 | 989 | -90.8 | 504990 | 631 | -98.7 | 504990 | 94 | -103.5 | 504990 | 640 |
| MR_1774412232_52595ADF | 504990 | 989 | -89.3 | 504990 | 631 | -99.9 | 504990 | 94 | -102.7 | 504990 | 640 |
| MR_1774412232_0714E7B6 | 504990 | 989 | -89.3 | 504990 | 631 | -98.8 | 504990 | 94 | -104.3 | 504990 | 640 |

> *... 2개 열 생략 (전체 14열)*

---
