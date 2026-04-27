# Track A 문제 분석 — train[710]~train[719]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[710] ~ train[719] (10개)

## 목차

1. [문제 710: `94bd81e2-4fc...`](#710) — single-answer, 정답: C22
2. [문제 711: `ab6178f6-c28...`](#711) — single-answer, 정답: C18
3. [문제 712: `f50ed894-8f4...`](#712) — multiple-answer, 정답: C12|C18
4. [문제 713: `50751921-77e...`](#713) — single-answer, 정답: C21
5. [문제 714: `3d2badbd-6f0...`](#714) — single-answer, 정답: C16
6. [문제 715: `9a5f6799-f92...`](#715) — multiple-answer, 정답: C1|C4|C9|C10
7. [문제 716: `a814a2cd-08a...`](#716) — single-answer, 정답: C7
8. [문제 717: `e8d27f78-dc3...`](#717) — single-answer, 정답: C14
9. [문제 718: `17838df9-2ea...`](#718) — single-answer, 정답: C17
10. [문제 719: `f32f391f-358...`](#719) — single-answer, 정답: C6

---

### 문제 710: `94bd81e2-4fc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `94bd81e2-4fc6-4e20-a535-a95383183406` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[710] topology](images/train_0710.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3246870_2 by 10 degrees
- `C2`: Lift the tilt angle of 3278856_3 by 6 degrees
- `C3`: Increase A3 Offset threshold for 3278856_3
- `C4`: Adjust the azimuth of 3278856_3 by 50 degrees
- `C5`: Increase A3 Offset threshold for 3246870_2
- `C6`: Add neighbor relationship between 3233364_4 and 3246870_2
- `C7`: Increase transmission power for 3278856_3
- `C8`: Decrease A3 Offset threshold for 3246870_2
- `C9`: Decrease A3 Offset threshold for 3278856_3
- `C10`: Increase transmission power for 3246870_2
- `C11`: Press down the tilt angle  of 3246870_2 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278856_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246870_2
- `C14`: Add neighbor relationship between 3278856_3 and 3246870_2
- `C15`: Press down the tilt angle of 3278856_3 by 6 degrees
- `C16`: Decrease transmission power for 3278856_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278856_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246870_2
- `C19`: Adjust the azimuth of 3246870_2 by 19 degrees
- `C20`: Decrease transmission power for 3246870_2
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Check test server and transmission issues **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.831 | MS1 | 121.4656688407 | 31.1446286094 | 326 | 504990 | -90.80 | 17.49 | 361.08 | 0.15 | 2.03 | 1579 |
| 2024-09-20 22:21:32.116 | MS1 | 121.4656603733 | 31.1446355988 | 326 | 504990 | -88.78 | 15.51 | 395.23 | 0.01 | 2.05 | 1585 |
| 2024-09-20 22:21:33.150 | MS1 | 121.4656691644 | 31.1446283492 | 326 | 504990 | -90.85 | 14.16 | 456.81 | 0.00 | 2.50 | 1568 |
| 2024-09-20 22:21:34.553 | MS1 | 121.4656727826 | 31.1446319079 | 326 | 504990 | -91.31 | 13.38 | 54.42 | 0.16 | 2.96 | 410 |
| 2024-09-20 22:21:35.642 | MS1 | 121.4656666254 | 31.1446195729 | 326 | 504990 | -90.36 | 15.75 | 78.13 | 0.04 | 2.47 | 332 |
| 2024-09-20 22:21:36.660 | MS1 | 121.4656723398 | 31.1446341191 | 326 | 504990 | -86.49 | 14.85 | 53.91 | 0.06 | 2.58 | 439 |
| 2024-09-20 22:21:37.820 | MS1 | 121.4656717992 | 31.1446314703 | 326 | 504990 | -90.40 | 10.64 | 66.53 | 0.14 | 2.60 | 423 |
| 2024-09-20 22:21:38.159 | MS1 | 121.4656654166 | 31.1446195906 | 326 | 504990 | -90.54 | 8.72 | 81.33 | 0.12 | 2.18 | 399 |
| 2024-09-20 22:21:39.552 | MS1 | 121.4656735151 | 31.1446277316 | 326 | 504990 | -90.41 | 12.87 | 68.64 | 0.19 | 2.50 | 445 |
| 2024-09-20 22:21:40.346 | MS1 | 121.4656592943 | 31.1446329988 | 326 | 504990 | -89.98 | 11.08 | 565.19 | 0.05 | 2.42 | 1565 |
| 2024-09-20 22:21:41.757 | MS1 | 121.4656768934 | 31.1446221529 | 326 | 504990 | -93.33 | 11.31 | 498.01 | 0.09 | 2.56 | 1573 |
| 2024-09-20 22:21:42.163 | MS1 | 121.4656709700 | 31.1446189786 | 326 | 504990 | -91.97 | 9.53 | 383.16 | 0.02 | 3.00 | 1579 |

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
| 3233364 | 4 | 121.4657144306 | 31.1442101634 | 102 | 15 | 5 | 16.5 | TDD | 847 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3246870 | 2 | 121.4678293988 | 31.1484056102 | 225 | 11 | 11 | 39.9 | TDD | 453 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3269244 | 1 | 121.4714570776 | 31.1557276309 | 213 | 15 | 3 | 39.3 | TDD | 43 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3278856 | 3 | 121.4700083479 | 31.1539797077 | 267 | 5 | 1 | 28.1 | TDD | 326 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.024 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.048 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.160 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.160 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.839 | NREventA3 | measId:2;ServCellPCI:300;Se... |
| 2024-09-20 22:21:38.079 | NRHandoverAttempt | SourcePCI:300;SourceNR-ARFC... |
| 2024-09-20 22:21:38.126 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.141 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.261 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.261 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269244 | 1 | 17.9022 | 13.1612 | -115.6946 | 10.2060 | 89.5569 | 0.0101 | 0.0028 |
| 2024_09_20 22:00 | 3246870 | 2 | 9.6702 | 18.4139 | -115.1557 | 12.5927 | 167.7849 | 0.0090 | 0.0146 |
| 2024_09_20 22:00 | 3278856 | 3 | 9.2686 | 17.3405 | -117.6051 | 10.1643 | 117.9563 | 0.0055 | 0.0142 |
| 2024_09_20 22:00 | 3233364 | 4 | 13.5335 | 9.3232 | -114.6620 | 12.8229 | 152.1731 | 0.0157 | 0.0009 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414685_8EB80833 | 504990 | 326 | -91.2 | 504990 | 453 | -95.6 | 504990 | 847 | -105.2 | 504990 | 43 |
| MR_1774414685_11448BBB | 504990 | 326 | -90.8 | 504990 | 453 | -98.4 | 504990 | 847 | -104.0 | 504990 | 43 |
| MR_1774414685_92C02BDD | 504990 | 326 | -89.6 | 504990 | 453 | -95.9 | 504990 | 847 | -104.6 | 504990 | 43 |
| MR_1774414685_AB177E36 | 504990 | 326 | -91.0 | 504990 | 453 | -96.0 | 504990 | 847 | -105.3 | 504990 | 43 |
| MR_1774414685_D60A03FC | 504990 | 326 | -90.9 | 504990 | 453 | -95.2 | 504990 | 847 | -104.1 | 504990 | 43 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 711: `ab6178f6-c28...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ab6178f6-c283-4166-91c4-2cab3509658c` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3267322_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[711] topology](images/train_0711.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3257464_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267322_2
- `C3`: Decrease transmission power for 3267322_2
- `C4`: Press down the tilt angle of 3267322_2 by 3 degrees
- `C5`: Increase transmission power for 3257464_3
- `C6`: Add neighbor relationship between 3267322_2 and 3257464_3
- `C7`: Lift the tilt angle of 3267322_2 by 3 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257464_3
- `C9`: Decrease A3 Offset threshold for 3267322_2
- `C10`: Adjust the azimuth of 3267322_2 by 2 degrees
- `C11`: Check test server and transmission issues
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease A3 Offset threshold for 3257464_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257464_3
- `C15`: Press down the tilt angle  of 3257464_3 by 10 degrees
- `C16`: Increase transmission power for 3267322_2
- `C17`: Increase A3 Offset threshold for 3257464_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267322_2 **← 정답**
- `C19`: Adjust the azimuth of 3257464_3 by 50 degrees
- `C20`: Lift the tilt angle  of 3257464_3 by 10 degrees
- `C21`: Increase A3 Offset threshold for 3267322_2
- `C22`: Add neighbor relationship between 3215628_4 and 3257464_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.998 | MS1 | 121.4656710015 | 31.1446233236 | 753 | 504990 | -87.05 | 14.77 | 522.13 | 0.06 | 2.05 | 1578 |
| 2024-09-20 22:21:32.534 | MS1 | 121.4656706270 | 31.1446283637 | 753 | 504990 | -85.30 | 16.60 | 363.57 | 0.17 | 2.76 | 1563 |
| 2024-09-20 22:21:33.467 | MS1 | 121.4656602024 | 31.1446343168 | 753 | 504990 | -85.19 | 17.87 | 579.42 | 0.12 | 2.64 | 1576 |
| 2024-09-20 22:21:34.930 | MS1 | 121.4656696908 | 31.1446303832 | 753 | 504990 | -91.01 | 17.91 | 79.51 | 0.65 | 2.74 | 566 |
| 2024-09-20 22:21:35.605 | MS1 | 121.4656598253 | 31.1446325773 | 753 | 504990 | -85.36 | 13.29 | 60.29 | 0.54 | 2.03 | 502 |
| 2024-09-20 22:21:36.764 | MS1 | 121.4656726716 | 31.1446295244 | 753 | 504990 | -91.60 | 16.85 | 82.38 | 0.59 | 2.86 | 548 |
| 2024-09-20 22:21:37.731 | MS1 | 121.4656647494 | 31.1446364113 | 753 | 504990 | -89.66 | 8.74 | 65.51 | 0.60 | 2.17 | 521 |
| 2024-09-20 22:21:38.724 | MS1 | 121.4656755160 | 31.1446362927 | 753 | 504990 | -92.72 | 9.99 | 87.98 | 0.53 | 2.68 | 592 |
| 2024-09-20 22:21:39.201 | MS1 | 121.4656645840 | 31.1446205998 | 753 | 504990 | -93.57 | 9.55 | 65.99 | 0.51 | 2.43 | 665 |
| 2024-09-20 22:21:40.157 | MS1 | 121.4656666103 | 31.1446323092 | 753 | 504990 | -90.64 | 10.77 | 561.81 | 0.06 | 2.51 | 1591 |
| 2024-09-20 22:21:41.208 | MS1 | 121.4656655246 | 31.1446333248 | 753 | 504990 | -93.16 | 9.07 | 521.49 | 0.07 | 2.11 | 1588 |
| 2024-09-20 22:21:42.477 | MS1 | 121.4656647119 | 31.1446254020 | 753 | 504990 | -89.74 | 7.81 | 326.96 | 0.10 | 2.82 | 1592 |

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
| 3215628 | 4 | 121.4708251023 | 31.1549131022 | 305 | 2 | 4 | 39.5 | TDD | 884 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3257464 | 3 | 121.4759354903 | 31.1442179710 | 353 | 10 | 1 | 18.4 | TDD | 962 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3267322 | 2 | 121.4675329208 | 31.1505850041 | 193 | 0 | 9 | 35.1 | TDD | 753 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3277553 | 1 | 121.4673439489 | 31.1538008512 | 297 | 1 | 9 | 29.0 | TDD | 144 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.885 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.901 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.020 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.020 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.778 | NREventA3 | measId:2;ServCellPCI:843;Se... |
| 2024-09-20 22:21:38.018 | NRHandoverAttempt | SourcePCI:843;SourceNR-ARFC... |
| 2024-09-20 22:21:38.057 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.067 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.173 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.173 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277553 | 1 | 10.3335 | 15.0568 | -116.0312 | 7.9104 | 101.0844 | 0.0047 | 0.0011 |
| 2024_09_20 22:00 | 3267322 | 2 | 5.4566 | 10.7749 | -116.9173 | 17.6112 | 88.3546 | 0.0085 | 0.0008 |
| 2024_09_20 22:00 | 3257464 | 3 | 9.2409 | 6.2021 | -116.1750 | 15.8508 | 163.9666 | 0.0028 | 0.0189 |
| 2024_09_20 22:00 | 3215628 | 4 | 11.8555 | 14.7066 | -117.8711 | 16.9780 | 83.9578 | 0.0121 | 0.0076 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414015_9D5C953F | 504990 | 753 | -89.4 | 504990 | 962 | -97.5 | 504990 | 884 | -98.3 | 504990 | 144 |
| MR_1774414015_7B9B4222 | 504990 | 753 | -91.7 | 504990 | 962 | -96.3 | 504990 | 884 | -99.0 | 504990 | 144 |
| MR_1774414015_E3E62AB8 | 504990 | 753 | -91.6 | 504990 | 962 | -96.4 | 504990 | 884 | -98.7 | 504990 | 144 |
| MR_1774414015_9AC2083A | 504990 | 753 | -92.9 | 504990 | 962 | -96.3 | 504990 | 884 | -99.6 | 504990 | 144 |
| MR_1774414015_1F2236F2 | 504990 | 753 | -91.8 | 504990 | 962 | -94.8 | 504990 | 884 | -97.8 | 504990 | 144 |
| MR_1774414015_97B43CD2 | 504990 | 753 | -91.8 | 504990 | 962 | -95.4 | 504990 | 884 | -98.7 | 504990 | 144 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 712: `f50ed894-8f4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f50ed894-8f4a-46c3-aa92-3997bbb2e707` |
| Tag | **multiple-answer** |
| 정답 | **C12|C18** |
| C12 의미 | Increase transmission power for 3234051_4 |
| C18 의미 | Adjust the azimuth of 3234051_4 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[712] topology](images/train_0712.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3234051_4 by 10 degrees
- `C2`: Press down the tilt angle  of 3218267_1 by 6 degrees
- `C3`: Decrease A3 Offset threshold for 3218267_1
- `C4`: Decrease transmission power for 3234051_4
- `C5`: Decrease transmission power for 3218267_1
- `C6`: Adjust the azimuth of 3218267_1 by 29 degrees
- `C7`: Add neighbor relationship between 3266943_2 and 3218267_1
- `C8`: Add neighbor relationship between 3234051_4 and 3218267_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218267_1
- `C10`: Lift the tilt angle  of 3218267_1 by 6 degrees
- `C11`: Press down the tilt angle of 3234051_4 by 10 degrees
- `C12`: Increase transmission power for 3234051_4 **← 정답**
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234051_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218267_1
- `C15`: Check test server and transmission issues
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase A3 Offset threshold for 3234051_4
- `C18`: Adjust the azimuth of 3234051_4 by 50 degrees **← 정답**
- `C19`: Decrease A3 Offset threshold for 3234051_4
- `C20`: Increase A3 Offset threshold for 3218267_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234051_4
- `C22`: Increase transmission power for 3218267_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.757 | MS1 | 121.4656598637 | 31.1446251682 | 950 | 504990 | -93.55 | 12.62 | 602.09 | 0.11 | 2.39 | 1596 |
| 2024-09-20 22:21:32.961 | MS1 | 121.4656736531 | 31.1446245675 | 950 | 504990 | -89.70 | 14.83 | 374.65 | 0.18 | 2.04 | 1599 |
| 2024-09-20 22:21:33.374 | MS1 | 121.4656623602 | 31.1446301903 | 950 | 504990 | -85.86 | 13.56 | 313.20 | 0.05 | 2.19 | 1562 |
| 2024-09-20 22:21:34.960 | MS1 | 121.4656598891 | 31.1446295819 | 950 | 504990 | -103.06 | 1.35 | 56.80 | 0.11 | 1.29 | 1566 |
| 2024-09-20 22:21:35.797 | MS1 | 121.4656719300 | 31.1446296554 | 950 | 504990 | -106.50 | -1.24 | 22.67 | 0.05 | 1.15 | 1575 |
| 2024-09-20 22:21:36.223 | MS1 | 121.4656655914 | 31.1446358939 | 950 | 504990 | -108.13 | 0.25 | 44.00 | 0.12 | 1.00 | 1576 |
| 2024-09-20 22:21:37.193 | MS1 | 121.4656640974 | 31.1446319956 | 950 | 504990 | -109.86 | 0.51 | 35.08 | 0.15 | 1.13 | 1569 |
| 2024-09-20 22:21:38.647 | MS1 | 121.4656646256 | 31.1446255719 | 950 | 504990 | -108.05 | 1.28 | 38.93 | 0.07 | 1.03 | 1583 |
| 2024-09-20 22:21:39.432 | MS1 | 121.4656697709 | 31.1446250419 | 950 | 504990 | -105.42 | 0.02 | 32.28 | 0.14 | 1.12 | 1575 |
| 2024-09-20 22:21:40.610 | MS1 | 121.4656778404 | 31.1446295137 | 950 | 504990 | -92.39 | 17.50 | 555.88 | 0.10 | 2.96 | 1573 |
| 2024-09-20 22:21:41.318 | MS1 | 121.4656715586 | 31.1446316395 | 950 | 504990 | -87.58 | 15.44 | 303.44 | 0.11 | 2.53 | 1565 |
| 2024-09-20 22:21:42.853 | MS1 | 121.4656728509 | 31.1446285818 | 950 | 504990 | -85.80 | 14.11 | 378.51 | 0.05 | 2.09 | 1585 |

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
| 3218267 | 1 | 121.4736427612 | 31.1443684790 | 243 | 3 | 6 | 33.2 | TDD | 657 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3234051 | 4 | 121.4645454957 | 31.1539010827 | 250 | 12 | 8 | 30.9 | TDD | 950 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3266943 | 2 | 121.4640120487 | 31.1539382502 | 122 | 11 | 1 | 48.7 | TDD | 3 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3275624 | 3 | 121.4691859226 | 31.1543534761 | 104 | 2 | 0 | 25.2 | TDD | 773 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.824 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.843 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.980 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.980 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.189 | NREventA2 | measId:1;ServCellPCI:271;Se... |
| 2024-09-20 22:21:34.321 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218267 | 1 | 10.5164 | 8.5134 | -114.8280 | 14.9308 | 198.2626 | 0.0146 | 0.0104 |
| 2024_09_20 22:00 | 3266943 | 2 | 17.8468 | 6.3659 | -117.8841 | 15.4836 | 183.3241 | 0.0079 | 0.0167 |
| 2024_09_20 22:00 | 3275624 | 3 | 9.3857 | 18.9463 | -116.0335 | 11.4239 | 156.6512 | 0.0192 | 0.0030 |
| 2024_09_20 22:00 | 3234051 | 4 | 19.4035 | 5.3131 | -115.6029 | 18.9126 | 112.5158 | 0.1398 | 0.0040 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414007_22774D2A | 504990 | 950 | -104.3 | 504990 | 657 | -107.0 | 504990 | 3 | -116.4 | 504990 | 773 |
| MR_1774414007_FC429F76 | 504990 | 950 | -101.8 | 504990 | 657 | -109.4 | 504990 | 3 | -113.4 | 504990 | 773 |
| MR_1774414007_B99DEA4F | 504990 | 950 | -102.0 | 504990 | 657 | -110.9 | 504990 | 3 | -115.7 | 504990 | 773 |
| MR_1774414007_4266EFAB | 504990 | 950 | -102.0 | 504990 | 657 | -107.0 | 504990 | 3 | -114.8 | 504990 | 773 |
| MR_1774414007_8627DE4B | 504990 | 950 | -102.0 | 504990 | 657 | -108.7 | 504990 | 3 | -113.2 | 504990 | 773 |
| MR_1774414007_C223825C | 504990 | 950 | -102.0 | 504990 | 657 | -109.1 | 504990 | 3 | -114.9 | 504990 | 773 |
| MR_1774414007_C14F2D83 | 504990 | 950 | -104.5 | 504990 | 657 | -107.7 | 504990 | 3 | -113.6 | 504990 | 773 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 713: `50751921-77e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `50751921-77eb-4c84-bd76-90471fa18fba` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Add neighbor relationship between 3211423_3 and 3265273_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[713] topology](images/train_0713.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3265273_2
- `C2`: Add neighbor relationship between 3252519_4 and 3265273_2
- `C3`: Adjust the azimuth of 3265273_2 by 18 degrees
- `C4`: Decrease A3 Offset threshold for 3211423_3
- `C5`: Decrease transmission power for 3211423_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265273_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265273_2
- `C8`: Increase transmission power for 3265273_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211423_3
- `C10`: Increase A3 Offset threshold for 3265273_2
- `C11`: Decrease A3 Offset threshold for 3265273_2
- `C12`: Lift the tilt angle of 3211423_3 by 8 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211423_3
- `C14`: Press down the tilt angle of 3211423_3 by 8 degrees
- `C15`: Increase transmission power for 3211423_3
- `C16`: Adjust the azimuth of 3211423_3 by 41 degrees
- `C17`: Press down the tilt angle  of 3265273_2 by 3 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Lift the tilt angle  of 3265273_2 by 3 degrees
- `C20`: Increase A3 Offset threshold for 3211423_3
- `C21`: Add neighbor relationship between 3211423_3 and 3265273_2 **← 정답**
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.474 | MS1 | 121.4656736617 | 31.1446307294 | 260 | 504990 | -76.25 | 17.29 | 446.45 | 0.06 | 2.41 | 1598 |
| 2024-09-20 22:21:32.803 | MS1 | 121.4656600332 | 31.1446250968 | 260 | 504990 | -79.03 | 16.50 | 412.41 | 0.03 | 2.45 | 1600 |
| 2024-09-20 22:21:33.835 | MS1 | 121.4656677916 | 31.1446368131 | 260 | 504990 | -78.38 | 17.48 | 562.98 | 0.15 | 2.26 | 1569 |
| 2024-09-20 22:21:34.982 | MS1 | 121.4656713332 | 31.1446196247 | 260 | 504990 | -90.74 | -1.56 | 48.35 | 0.17 | 1.21 | 1576 |
| 2024-09-20 22:21:35.254 | MS1 | 121.4656756359 | 31.1446325787 | 260 | 504990 | -87.00 | -0.16 | 44.74 | 0.08 | 1.20 | 1585 |
| 2024-09-20 22:21:36.498 | MS1 | 121.4656692381 | 31.1446249012 | 260 | 504990 | -91.07 | -3.04 | 46.54 | 0.06 | 1.31 | 1569 |
| 2024-09-20 22:21:37.243 | MS1 | 121.4656706898 | 31.1446299578 | 260 | 504990 | -86.61 | -2.36 | 34.24 | 0.06 | 1.24 | 1596 |
| 2024-09-20 22:21:38.657 | MS1 | 121.4656598789 | 31.1446209219 | 260 | 504990 | -81.13 | 16.34 | 398.26 | 0.15 | 1.41 | 1560 |
| 2024-09-20 22:21:39.102 | MS1 | 121.4656658413 | 31.1446359649 | 260 | 504990 | -77.57 | 16.89 | 359.32 | 0.11 | 1.23 | 1568 |
| 2024-09-20 22:21:40.680 | MS1 | 121.4656724344 | 31.1446304882 | 260 | 504990 | -80.56 | 17.14 | 571.47 | 0.02 | 2.14 | 1567 |
| 2024-09-20 22:21:41.190 | MS1 | 121.4656751598 | 31.1446266213 | 260 | 504990 | -83.12 | 15.35 | 309.82 | 0.09 | 2.23 | 1586 |
| 2024-09-20 22:21:42.439 | MS1 | 121.4656659234 | 31.1446214904 | 260 | 504990 | -81.77 | 12.20 | 374.66 | 0.17 | 2.93 | 1591 |

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
| 3211423 | 3 | 121.4744430225 | 31.1535140953 | 261 | 6 | 4 | 36.6 | TDD | 260 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3235212 | 1 | 121.4668204994 | 31.1483036358 | 327 | 9 | 2 | 26.0 | TDD | 592 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3252519 | 4 | 121.4663746580 | 31.1534247181 | 305 | 5 | 11 | 22.8 | TDD | 350 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3265273 | 2 | 121.4652952113 | 31.1547793355 | 196 | 0 | 12 | 49.5 | TDD | 650 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.131 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.152 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.294 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.294 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.002 | NREventA3 | measId:2;ServCellPCI:718;Se... |
| 2024-09-20 22:21:36.002 | NREventA3 | measId:2;ServCellPCI:718;Se... |
| 2024-09-20 22:21:37.002 | NREventA3 | measId:2;ServCellPCI:718;Se... |
| 2024-09-20 22:21:39.502 | NRRRCReestablishAttempt | PCI:718 |
| 2024-09-20 22:21:39.521 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.533 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.678 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.678 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235212 | 1 | 10.6739 | 19.0095 | -115.0510 | 9.0475 | 143.9339 | 0.0022 | 0.0067 |
| 2024_09_20 22:00 | 3265273 | 2 | 15.3115 | 11.1865 | -116.6637 | 8.5842 | 95.0857 | 0.0056 | 0.0162 |
| 2024_09_20 22:00 | 3211423 | 3 | 15.4374 | 13.2253 | -117.4664 | 15.9066 | 112.4329 | 0.0090 | 0.1135 |
| 2024_09_20 22:00 | 3252519 | 4 | 6.8183 | 14.7616 | -116.1335 | 15.8563 | 110.8600 | 0.0013 | 0.0167 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416767_612FBEAA | 504990 | 260 | -89.1 | 504990 | 650 | -85.9 | 504990 | 350 | -90.6 | 504990 | 592 |
| MR_1774416767_B8B9AB1B | 504990 | 260 | -89.6 | 504990 | 650 | -83.8 | 504990 | 350 | -89.3 | 504990 | 592 |
| MR_1774416767_D2F3DD42 | 504990 | 260 | -89.6 | 504990 | 650 | -85.0 | 504990 | 350 | -90.9 | 504990 | 592 |
| MR_1774416767_AA019AE3 | 504990 | 260 | -90.7 | 504990 | 650 | -86.2 | 504990 | 350 | -91.3 | 504990 | 592 |
| MR_1774416767_0CA5B7FE | 504990 | 650 | -85.8 | 504990 | 260 | -91.3 | 504990 | 350 | -88.8 | 504990 | 592 |
| MR_1774416767_58B04AA3 | 504990 | 650 | -85.4 | 504990 | 260 | -89.3 | 504990 | 350 | -88.2 | 504990 | 592 |
| MR_1774416767_414045BF | 504990 | 260 | -90.9 | 504990 | 650 | -84.3 | 504990 | 350 | -89.8 | 504990 | 592 |
| MR_1774416767_EE337D02 | 504990 | 260 | -90.4 | 504990 | 650 | -85.7 | 504990 | 350 | -89.6 | 504990 | 592 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 714: `3d2badbd-6f0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3d2badbd-6f09-484f-b563-644801682598` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Add neighbor relationship between 3279882_3 and 3222272_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[714] topology](images/train_0714.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3279882_3 by 10 degrees
- `C2`: Lift the tilt angle of 3279882_3 by 10 degrees
- `C3`: Increase transmission power for 3222272_1
- `C4`: Lift the tilt angle  of 3222272_1 by 5 degrees
- `C5`: Increase A3 Offset threshold for 3279882_3
- `C6`: Decrease transmission power for 3222272_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222272_1
- `C8`: Decrease transmission power for 3279882_3
- `C9`: Decrease A3 Offset threshold for 3222272_1
- `C10`: Decrease A3 Offset threshold for 3279882_3
- `C11`: Check test server and transmission issues
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279882_3
- `C13`: Press down the tilt angle  of 3222272_1 by 5 degrees
- `C14`: Increase transmission power for 3279882_3
- `C15`: Add neighbor relationship between 3210950_2 and 3222272_1
- `C16`: Add neighbor relationship between 3279882_3 and 3222272_1 **← 정답**
- `C17`: Adjust the azimuth of 3279882_3 by 34 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279882_3
- `C19`: Adjust the azimuth of 3222272_1 by 42 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222272_1
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Increase A3 Offset threshold for 3222272_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.580 | MS1 | 121.4656725620 | 31.1446244038 | 204 | 504990 | -84.53 | 17.06 | 340.29 | 0.03 | 2.53 | 1586 |
| 2024-09-20 22:21:32.649 | MS1 | 121.4656728513 | 31.1446322318 | 204 | 504990 | -84.17 | 12.54 | 421.83 | 0.05 | 2.05 | 1596 |
| 2024-09-20 22:21:33.995 | MS1 | 121.4656642612 | 31.1446323113 | 204 | 504990 | -81.82 | 14.83 | 398.89 | 0.11 | 2.74 | 1598 |
| 2024-09-20 22:21:34.310 | MS1 | 121.4656671375 | 31.1446233745 | 204 | 504990 | -86.70 | -3.36 | 69.61 | 0.05 | 1.34 | 1562 |
| 2024-09-20 22:21:35.389 | MS1 | 121.4656751954 | 31.1446351783 | 204 | 504990 | -85.64 | -3.52 | 70.15 | 0.08 | 1.13 | 1569 |
| 2024-09-20 22:21:36.811 | MS1 | 121.4656643120 | 31.1446254443 | 204 | 504990 | -90.11 | -3.14 | 40.59 | 0.14 | 1.07 | 1574 |
| 2024-09-20 22:21:37.659 | MS1 | 121.4656693590 | 31.1446272276 | 204 | 504990 | -87.44 | -1.67 | 47.55 | 0.19 | 1.14 | 1578 |
| 2024-09-20 22:21:38.825 | MS1 | 121.4656725917 | 31.1446379545 | 204 | 504990 | -75.18 | 12.82 | 354.56 | 0.05 | 1.10 | 1595 |
| 2024-09-20 22:21:39.874 | MS1 | 121.4656622817 | 31.1446251772 | 204 | 504990 | -83.73 | 14.05 | 562.14 | 0.19 | 1.21 | 1582 |
| 2024-09-20 22:21:40.773 | MS1 | 121.4656718051 | 31.1446372936 | 204 | 504990 | -82.92 | 15.62 | 578.68 | 0.04 | 2.52 | 1594 |
| 2024-09-20 22:21:41.882 | MS1 | 121.4656617914 | 31.1446230206 | 204 | 504990 | -84.20 | 12.80 | 343.87 | 0.07 | 2.97 | 1592 |
| 2024-09-20 22:21:42.999 | MS1 | 121.4656686746 | 31.1446231578 | 204 | 504990 | -77.16 | 14.46 | 447.96 | 0.10 | 2.77 | 1584 |

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
| 3210950 | 2 | 121.4741201843 | 31.1504476558 | 168 | 10 | 1 | 24.5 | TDD | 484 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3222272 | 1 | 121.4683541256 | 31.1537708967 | 236 | 3 | 6 | 42.7 | TDD | 682 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3251929 | 4 | 121.4728609232 | 31.1507950681 | 185 | 14 | 8 | 27.2 | TDD | 61 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3279882 | 3 | 121.4659906339 | 31.1541365446 | 216 | 13 | 3 | 30.1 | TDD | 204 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.174 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.196 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.327 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.327 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.009 | NREventA3 | measId:2;ServCellPCI:979;Se... |
| 2024-09-20 22:21:36.009 | NREventA3 | measId:2;ServCellPCI:979;Se... |
| 2024-09-20 22:21:37.009 | NREventA3 | measId:2;ServCellPCI:979;Se... |
| 2024-09-20 22:21:39.509 | NRRRCReestablishAttempt | PCI:979 |
| 2024-09-20 22:21:39.528 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.539 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.686 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.686 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222272 | 1 | 7.4404 | 19.0235 | -117.8645 | 15.7342 | 135.6626 | 0.0133 | 0.0004 |
| 2024_09_20 22:00 | 3210950 | 2 | 13.2006 | 11.0761 | -116.0996 | 7.0508 | 182.7714 | 0.0037 | 0.0034 |
| 2024_09_20 22:00 | 3279882 | 3 | 19.3248 | 19.7414 | -117.1373 | 17.4915 | 170.3893 | 0.0109 | 0.1544 |
| 2024_09_20 22:00 | 3251929 | 4 | 18.7373 | 17.3362 | -114.5989 | 7.9641 | 161.7569 | 0.0063 | 0.0172 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413266_FE1FFBB2 | 504990 | 204 | -87.3 | 504990 | 682 | -81.3 | 504990 | 484 | -85.5 | 504990 | 61 |
| MR_1774413266_A8002174 | 504990 | 204 | -84.9 | 504990 | 682 | -81.1 | 504990 | 484 | -82.4 | 504990 | 61 |
| MR_1774413266_66C3979A | 504990 | 682 | -83.0 | 504990 | 204 | -87.7 | 504990 | 484 | -85.8 | 504990 | 61 |
| MR_1774413266_475B5C99 | 504990 | 682 | -83.3 | 504990 | 204 | -86.4 | 504990 | 484 | -83.7 | 504990 | 61 |
| MR_1774413266_DFD482E8 | 504990 | 682 | -81.3 | 504990 | 204 | -87.5 | 504990 | 484 | -83.4 | 504990 | 61 |
| MR_1774413266_51A23A84 | 504990 | 682 | -83.6 | 504990 | 204 | -85.0 | 504990 | 484 | -84.0 | 504990 | 61 |
| MR_1774413266_2B123030 | 504990 | 682 | -83.0 | 504990 | 204 | -85.0 | 504990 | 484 | -84.1 | 504990 | 61 |
| MR_1774413266_B9E797EF | 504990 | 682 | -82.7 | 504990 | 204 | -85.6 | 504990 | 484 | -82.8 | 504990 | 61 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 715: `9a5f6799-f92...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9a5f6799-f924-4560-aa57-fbae731b69cf` |
| Tag | **multiple-answer** |
| 정답 | **C1|C4|C9|C10** |
| C1 의미 | Decrease transmission power for 3248292_3 |
| C4 의미 | Increase A3 Offset threshold for 3259454_2 |
| C9 의미 | Increase A3 Offset threshold for 3248292_3 |
| C10 의미 | Press down the tilt angle  of 3248292_3 by 3 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[715] topology](images/train_0715.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3248292_3 **← 정답**
- `C2`: Add neighbor relationship between 3259454_2 and 3248292_3
- `C3`: Lift the tilt angle  of 3248292_3 by 3 degrees
- `C4`: Increase A3 Offset threshold for 3259454_2 **← 정답**
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259454_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248292_3
- `C7`: Lift the tilt angle of 3259454_2 by 3 degrees
- `C8`: Adjust the azimuth of 3259454_2 by 45 degrees
- `C9`: Increase A3 Offset threshold for 3248292_3 **← 정답**
- `C10`: Press down the tilt angle  of 3248292_3 by 3 degrees **← 정답**
- `C11`: Adjust the azimuth of 3248292_3 by 21 degrees
- `C12`: Decrease A3 Offset threshold for 3259454_2
- `C13`: Add neighbor relationship between 3276973_1 and 3248292_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248292_3
- `C15`: Check test server and transmission issues
- `C16`: Decrease transmission power for 3259454_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259454_2
- `C18`: Increase transmission power for 3259454_2
- `C19`: Press down the tilt angle of 3259454_2 by 3 degrees
- `C20`: Increase transmission power for 3248292_3
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease A3 Offset threshold for 3248292_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.403 | MS1 | 121.4656704067 | 31.1446182409 | 73 | 504990 | -83.74 | 14.00 | 462.74 | 0.14 | 2.05 | 1570 |
| 2024-09-20 22:21:32.310 | MS1 | 121.4656700995 | 31.1446297991 | 73 | 504990 | -77.79 | 16.42 | 588.51 | 0.06 | 2.73 | 1583 |
| 2024-09-20 22:21:33.618 | MS1 | 121.4656581300 | 31.1446355480 | 73 | 504990 | -82.84 | 12.22 | 473.90 | 0.03 | 2.56 | 1580 |
| 2024-09-20 22:21:34.495 | MS1 | 121.4656636929 | 31.1446326947 | 343 | 504990 | -88.72 | 4.78 | 75.94 | 0.14 | 1.25 | 1584 |
| 2024-09-20 22:21:35.655 | MS1 | 121.4656734615 | 31.1446214184 | 343 | 504990 | -87.04 | 2.26 | 53.64 | 0.09 | 1.45 | 1578 |
| 2024-09-20 22:21:36.574 | MS1 | 121.4656639277 | 31.1446351198 | 73 | 504990 | -85.02 | 4.52 | 55.48 | 0.18 | 1.30 | 1576 |
| 2024-09-20 22:21:37.607 | MS1 | 121.4656708588 | 31.1446344297 | 73 | 504990 | -88.63 | 2.24 | 48.30 | 0.14 | 1.26 | 1560 |
| 2024-09-20 22:21:38.833 | MS1 | 121.4656657326 | 31.1446212182 | 343 | 504990 | -84.86 | 4.74 | 73.25 | 0.11 | 1.08 | 1596 |
| 2024-09-20 22:21:39.485 | MS1 | 121.4656610517 | 31.1446334105 | 343 | 504990 | -87.84 | 2.49 | 69.68 | 0.05 | 1.28 | 1567 |
| 2024-09-20 22:21:40.636 | MS1 | 121.4656659958 | 31.1446245868 | 343 | 504990 | -82.16 | 13.37 | 471.32 | 0.06 | 2.18 | 1592 |
| 2024-09-20 22:21:41.757 | MS1 | 121.4656740543 | 31.1446215751 | 343 | 504990 | -80.46 | 12.04 | 314.50 | 0.08 | 2.19 | 1563 |
| 2024-09-20 22:21:42.753 | MS1 | 121.4656756907 | 31.1446277824 | 343 | 504990 | -76.30 | 14.82 | 514.08 | 0.14 | 2.44 | 1565 |

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
| 3242061 | 4 | 121.4654417999 | 31.1505649830 | 158 | 10 | 9 | 34.1 | TDD | 343 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3248292 | 3 | 121.4659835533 | 31.1509879206 | 203 | 2 | 11 | 18.5 | TDD | 398 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3259454 | 2 | 121.4759350826 | 31.1538322490 | 269 | 2 | 8 | 22.3 | TDD | 73 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3271626 | 5 | 121.4720336274 | 31.1494768163 | 122 | 3 | 1 | 48.9 | TDD | 378 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3276973 | 1 | 121.4722282907 | 31.1468170430 | 29 | 7 | 6 | 40.0 | TDD | 774 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.002 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.017 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.122 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.122 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.835 | NREventA3 | measId:2;ServCellPCI:413;Se... |
| 2024-09-20 22:21:34.075 | NRHandoverAttempt | SourcePCI:413;SourceNR-ARFC... |
| 2024-09-20 22:21:34.117 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.131 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:34.233 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.233 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.835 | NREventA3 | measId:2;ServCellPCI:404;Se... |
| 2024-09-20 22:21:36.075 | NRHandoverAttempt | SourcePCI:404;SourceNR-ARFC... |
| 2024-09-20 22:21:36.124 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.138 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.270 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.270 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.835 | NREventA3 | measId:2;ServCellPCI:413;Se... |
| 2024-09-20 22:21:38.075 | NRHandoverAttempt | SourcePCI:413;SourceNR-ARFC... |
| 2024-09-20 22:21:38.105 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.117 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.239 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.239 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276973 | 1 | 8.5230 | 7.1466 | -117.0468 | 5.4452 | 87.4208 | 0.0102 | 0.0136 |
| 2024_09_20 22:00 | 3259454 | 2 | 16.2062 | 11.2430 | -117.2369 | 7.4501 | 174.4295 | 0.0136 | 0.0095 |
| 2024_09_20 22:00 | 3248292 | 3 | 15.7614 | 8.1701 | -117.9238 | 5.6465 | 124.5565 | 0.0129 | 0.0005 |
| 2024_09_20 22:00 | 3242061 | 4 | 5.8957 | 14.3023 | -114.3242 | 12.5282 | 168.9442 | 0.0047 | 0.0093 |
| 2024_09_20 22:00 | 3271626 | 5 | 8.5424 | 17.1239 | -116.8553 | 11.5184 | 95.4828 | 0.0009 | 0.0160 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416241_4FD3FCA7 | 504990 | 343 | -88.3 | 504990 | 73 | -85.5 | 504990 | 398 | -88.9 | 504990 | 774 |
| MR_1774416241_B3231399 | 504990 | 343 | -90.0 | 504990 | 73 | -82.7 | 504990 | 398 | -88.7 | 504990 | 774 |
| MR_1774416241_2F3AE903 | 504990 | 73 | -90.5 | 504990 | 343 | -85.9 | 504990 | 398 | -89.5 | 504990 | 774 |
| MR_1774416241_F7DB4314 | 504990 | 343 | -87.6 | 504990 | 73 | -83.0 | 504990 | 398 | -88.4 | 504990 | 774 |
| MR_1774416241_71EE058C | 504990 | 343 | -88.2 | 504990 | 73 | -84.5 | 504990 | 398 | -91.4 | 504990 | 774 |
| MR_1774416241_D7C85E58 | 504990 | 343 | -87.4 | 504990 | 73 | -84.6 | 504990 | 398 | -91.5 | 504990 | 774 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 716: `a814a2cd-08a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a814a2cd-08a9-483d-af8f-b0aafa309354` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[716] topology](images/train_0716.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3270132_3 by 10 degrees
- `C2`: Decrease transmission power for 3270132_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251987_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251987_4
- `C5`: Increase A3 Offset threshold for 3270132_3
- `C6`: Increase transmission power for 3270132_3
- `C7`: Insufficient data; more data is needed for judgment. **← 정답**
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270132_3
- `C9`: Increase A3 Offset threshold for 3251987_4
- `C10`: Check test server and transmission issues
- `C11`: Adjust the azimuth of 3270132_3 by 50 degrees
- `C12`: Lift the tilt angle  of 3270132_3 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3270132_3
- `C14`: Add neighbor relationship between 3256755_1 and 3270132_3
- `C15`: Decrease A3 Offset threshold for 3251987_4
- `C16`: Decrease transmission power for 3251987_4
- `C17`: Increase transmission power for 3251987_4
- `C18`: Add neighbor relationship between 3251987_4 and 3270132_3
- `C19`: Adjust the azimuth of 3251987_4 by 50 degrees
- `C20`: Lift the tilt angle of 3251987_4 by 10 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270132_3
- `C22`: Press down the tilt angle of 3251987_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.853 | MS1 | 121.4656763101 | 31.1446244748 | 135 | 504990 | -86.33 | 12.23 | 502.66 | 0.05 | 2.75 | 1576 |
| 2024-09-20 22:21:32.475 | MS1 | 121.4656645319 | 31.1446192974 | 135 | 504990 | -90.36 | 15.03 | 315.57 | 0.07 | 2.22 | 1600 |
| 2024-09-20 22:21:33.823 | MS1 | 121.4656646173 | 31.1446192199 | 135 | 504990 | -86.85 | 17.62 | 444.78 | 0.04 | 2.32 | 1578 |
| 2024-09-20 22:21:34.801 | MS1 | 121.4656602441 | 31.1446241106 | 135 | 504990 | -87.60 | 13.21 | 77.84 | 0.11 | 2.71 | 1588 |
| 2024-09-20 22:21:35.284 | MS1 | 121.4656591546 | 31.1446187175 | 135 | 504990 | -86.25 | 15.85 | 60.95 | 0.12 | 2.80 | 1571 |
| 2024-09-20 22:21:36.969 | MS1 | 121.4656715107 | 31.1446281143 | 135 | 504990 | -87.30 | 14.65 | 80.18 | 0.18 | 2.27 | 1581 |
| 2024-09-20 22:21:37.336 | MS1 | 121.4656605708 | 31.1446338358 | 135 | 504990 | -91.29 | 8.40 | 61.58 | 0.17 | 2.84 | 1571 |
| 2024-09-20 22:21:38.603 | MS1 | 121.4656652906 | 31.1446347683 | 135 | 504990 | -92.47 | 12.41 | 46.48 | 0.19 | 2.25 | 1598 |
| 2024-09-20 22:21:39.486 | MS1 | 121.4656746775 | 31.1446262395 | 135 | 504990 | -91.98 | 8.55 | 66.06 | 0.12 | 2.89 | 1597 |
| 2024-09-20 22:21:40.287 | MS1 | 121.4656612741 | 31.1446320980 | 135 | 504990 | -91.80 | 7.03 | 549.76 | 0.19 | 2.09 | 1578 |
| 2024-09-20 22:21:41.441 | MS1 | 121.4656703234 | 31.1446305314 | 135 | 504990 | -89.40 | 12.30 | 406.18 | 0.11 | 2.38 | 1580 |
| 2024-09-20 22:21:42.882 | MS1 | 121.4656610897 | 31.1446327827 | 135 | 504990 | -93.39 | 7.67 | 419.65 | 0.06 | 2.39 | 1568 |

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
| 3251987 | 4 | 121.4697084066 | 31.1493248576 | 134 | 9 | 2 | 42.4 | TDD | 135 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3256755 | 1 | 121.4758525989 | 31.1543976061 | 96 | 2 | 7 | 49.6 | TDD | 649 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3269565 | 2 | 121.4667833033 | 31.1547806559 | 83 | 1 | 2 | 49.8 | TDD | 130 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3270132 | 3 | 121.4656260575 | 31.1515032218 | 16 | 14 | 7 | 42.6 | TDD | 62 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.315 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.338 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.483 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.483 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.188 | NREventA3 | measId:2;ServCellPCI:711;Se... |
| 2024-09-20 22:21:38.428 | NRHandoverAttempt | SourcePCI:711;SourceNR-ARFC... |
| 2024-09-20 22:21:38.465 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.478 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.603 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.603 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3256755 | 1 | 88.0078 | 81.8062 | -114.9683 | 11.9319 | 143.6678 | 0.0040 | 0.0130 |
| 2024_09_19 22:00 | 3269565 | 2 | 85.4658 | 81.7879 | -114.9434 | 17.3925 | 153.4386 | 0.0113 | 0.0169 |
| 2024_09_19 22:00 | 3270132 | 3 | 75.8158 | 79.9785 | -115.4364 | 9.4512 | 130.9004 | 0.0192 | 0.0112 |
| 2024_09_19 22:00 | 3251987 | 4 | 77.2689 | 87.0132 | -114.8427 | 11.0610 | 168.3812 | 0.0188 | 0.0019 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417003_B40238FF | 504990 | 135 | -87.2 | 504990 | 62 | -90.1 | 504990 | 649 | -100.1 | 504990 | 130 |
| MR_1774417003_AE87F79A | 504990 | 135 | -86.1 | 504990 | 62 | -90.2 | 504990 | 649 | -101.8 | 504990 | 130 |
| MR_1774417003_7728845F | 504990 | 135 | -86.8 | 504990 | 62 | -89.8 | 504990 | 649 | -102.6 | 504990 | 130 |
| MR_1774417003_82D950D1 | 504990 | 135 | -87.7 | 504990 | 62 | -89.9 | 504990 | 649 | -101.4 | 504990 | 130 |
| MR_1774417003_A054331E | 504990 | 135 | -89.4 | 504990 | 62 | -88.5 | 504990 | 649 | -101.8 | 504990 | 130 |
| MR_1774417003_B821BDBF | 504990 | 135 | -86.2 | 504990 | 62 | -89.9 | 504990 | 649 | -100.8 | 504990 | 130 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 717: `e8d27f78-dc3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e8d27f78-dc38-4551-9b1f-3db4520c15b4` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269346_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[717] topology](images/train_0717.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3269346_1 by 1 degrees
- `C2`: Lift the tilt angle  of 3242155_3 by 1 degrees
- `C3`: Adjust the azimuth of 3242155_3 by 1 degrees
- `C4`: Increase transmission power for 3269346_1
- `C5`: Decrease A3 Offset threshold for 3242155_3
- `C6`: Press down the tilt angle of 3269346_1 by 1 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease A3 Offset threshold for 3269346_1
- `C9`: Decrease transmission power for 3269346_1
- `C10`: Add neighbor relationship between 3246414_8 and 3242155_3
- `C11`: Increase A3 Offset threshold for 3242155_3
- `C12`: Adjust the azimuth of 3269346_1 by 8 degrees
- `C13`: Check test server and transmission issues
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269346_1 **← 정답**
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269346_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242155_3
- `C17`: Decrease transmission power for 3242155_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242155_3
- `C19`: Increase A3 Offset threshold for 3269346_1
- `C20`: Press down the tilt angle  of 3242155_3 by 1 degrees
- `C21`: Add neighbor relationship between 3269346_1 and 3242155_3
- `C22`: Increase transmission power for 3242155_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.879 | MS1 | 121.4656721314 | 31.1446244484 | 73 | 504990 | -93.47 | 13.73 | 553.24 | 0.08 | 2.07 | 1593 |
| 2024-09-20 22:21:32.508 | MS1 | 121.4656707840 | 31.1446250445 | 115 | 504990 | -93.81 | 12.59 | 549.46 | 0.13 | 2.24 | 1578 |
| 2024-09-20 22:21:33.914 | MS1 | 121.4656602764 | 31.1446251822 | 339 | 504990 | -93.39 | 10.61 | 363.65 | 0.20 | 2.71 | 1566 |
| 2024-09-20 22:21:34.354 | MS1 | 121.4656770611 | 31.1446255765 | 223 | 152650 | -95.94 | 3.94 | 52.40 | 0.00 | 1.61 | 939 |
| 2024-09-20 22:21:35.930 | MS1 | 121.4656627722 | 31.1446224676 | 204 | 152650 | -96.47 | 2.54 | 83.13 | 0.02 | 1.57 | 915 |
| 2024-09-20 22:21:36.880 | MS1 | 121.4656752352 | 31.1446311790 | 328 | 152650 | -96.49 | 4.03 | 85.49 | 0.05 | 2.00 | 941 |
| 2024-09-20 22:21:37.315 | MS1 | 121.4656620503 | 31.1446324304 | 538 | 152650 | -96.81 | 6.50 | 49.07 | 0.02 | 1.57 | 901 |
| 2024-09-20 22:21:38.648 | MS1 | 121.4656716891 | 31.1446344431 | 223 | 152650 | -96.51 | 5.68 | 73.02 | 0.05 | 2.00 | 916 |
| 2024-09-20 22:21:39.139 | MS1 | 121.4656693569 | 31.1446190516 | 204 | 152650 | -87.65 | 4.34 | 80.14 | 0.19 | 1.63 | 955 |
| 2024-09-20 22:21:40.633 | MS1 | 121.4656645663 | 31.1446253207 | 328 | 152650 | -92.51 | 7.93 | 80.35 | 0.15 | 2.25 | 1571 |
| 2024-09-20 22:21:41.201 | MS1 | 121.4656776226 | 31.1446181529 | 538 | 152650 | -96.65 | 5.02 | 95.52 | 0.01 | 2.89 | 1586 |
| 2024-09-20 22:21:42.486 | MS1 | 121.4656774511 | 31.1446317384 | 223 | 152650 | -96.54 | 5.07 | 83.23 | 0.18 | 2.94 | 1596 |

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
| 3211140 | 10 | 121.4751971586 | 31.1444546315 | 57 | 11 | 9 | 10.2 | FDD | 948 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3211992 | 6 | 121.4715993172 | 31.1546564579 | 337 | 4 | 1 | 29.3 | TDD | 822 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3220726 | 9 | 121.4663346024 | 31.1536946973 | 36 | 4 | 12 | 4.2 | FDD | 204 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3232631 | 11 | 121.4728947937 | 31.1522992720 | 324 | 5 | 9 | 15.6 | FDD | 56 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3233145 | 4 | 121.4646602733 | 31.1460171944 | 132 | 4 | 2 | 26.1 | TDD | 339 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3238808 | 2 | 121.4730922152 | 31.1478719405 | 70 | 1 | 8 | 28.4 | TDD | 522 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3238909 | 7 | 121.4657610286 | 31.1527726763 | 39 | 12 | 5 | 16.1 | FDD | 26 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3242155 | 3 | 121.4706766561 | 31.1501912694 | 219 | 0 | 2 | 15.8 | TDD | 560 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3246414 | 8 | 121.4693582699 | 31.1531803705 | 250 | 13 | 3 | 29.7 | FDD | 328 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3269346 | 1 | 121.4681964610 | 31.1549531156 | 200 | 1 | 4 | 5.8 | TDD | 73 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3270141 | 12 | 121.4743106809 | 31.1480035021 | 172 | 9 | 11 | 11.8 | FDD | 538 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3271088 | 5 | 121.4703133919 | 31.1525888459 | 349 | 0 | 0 | 18.1 | TDD | 115 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3275220 | 13 | 121.4706676566 | 31.1523330097 | 271 | 12 | 0 | 13.3 | FDD | 223 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |

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
| 2024-09-20 22:21:30.779 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.796 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.946 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.946 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.624 | NREventA2 | measId:1;ServCellPCI:238;Se... |
| 2024-09-20 22:21:34.760 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.003 | NREventA5 | measId:3;ServCellPCI:238;Se... |
| 2024-09-20 22:21:35.072 | NRHandoverAttempt | SourcePCI:238;SourceNR-ARFC... |
| 2024-09-20 22:21:35.092 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.103 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.209 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.209 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269346 | 1 | 17.2672 | 6.6603 | -116.6553 | 16.0280 | 111.6989 | 0.0180 | 0.0107 |
| 2024_09_20 22:00 | 3238808 | 2 | 15.4071 | 19.5719 | -117.6023 | 17.4446 | 184.5678 | 0.0040 | 0.0014 |
| 2024_09_20 22:00 | 3242155 | 3 | 8.8415 | 11.9452 | -116.1133 | 9.0346 | 155.4009 | 0.0177 | 0.0153 |
| 2024_09_20 22:00 | 3233145 | 4 | 17.1552 | 6.1704 | -115.4273 | 5.8106 | 193.4833 | 0.0152 | 0.0048 |
| 2024_09_20 22:00 | 3271088 | 5 | 19.6823 | 13.7009 | -115.3720 | 12.6149 | 93.9443 | 0.0020 | 0.0083 |
| 2024_09_20 22:00 | 3211992 | 6 | 11.6045 | 9.2227 | -116.9119 | 17.5879 | 164.0538 | 0.0115 | 0.0136 |
| 2024_09_20 22:00 | 3238909 | 7 | 18.4946 | 13.5942 | -116.9552 | 4.0963 | 49.0222 | 0.0097 | 0.0072 |
| 2024_09_20 22:00 | 3246414 | 8 | 11.1422 | 7.0018 | -116.9729 | 3.0138 | 57.8546 | 0.0109 | 0.0020 |
| 2024_09_20 22:00 | 3220726 | 9 | 13.9382 | 5.7815 | -116.5057 | 3.9920 | 36.6003 | 0.0146 | 0.0057 |
| 2024_09_20 22:00 | 3211140 | 10 | 6.0474 | 18.8795 | -115.2266 | 3.6943 | 45.2126 | 0.0150 | 0.0031 |
| 2024_09_20 22:00 | 3232631 | 11 | 15.6189 | 7.4068 | -116.8964 | 3.6450 | 48.2298 | 0.0139 | 0.0012 |
| 2024_09_20 22:00 | 3270141 | 12 | 13.7986 | 7.5058 | -114.1551 | 4.8678 | 38.5921 | 0.0097 | 0.0180 |
| 2024_09_20 22:00 | 3275220 | 13 | 8.3049 | 10.8430 | -117.4907 | 4.9551 | 54.1534 | 0.0003 | 0.0061 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415989_8FC8E98B | 152650 | 223 | -97.9 | 152650 | 948 | -100.5 | 152650 | 56 | -108.1 | 152650 | 26 |
| MR_1774415989_5EABF624 | 504990 | 339 | -92.6 | 504990 | 560 | -90.9 | 504990 | 522 | -92.8 | 504990 | 822 |
| MR_1774415989_EEA9A37A | 504990 | 339 | -94.9 | 504990 | 560 | -92.7 | 504990 | 522 | -92.8 | 504990 | 822 |
| MR_1774415989_4DDFA62C | 152650 | 223 | -95.2 | 152650 | 948 | -101.7 | 152650 | 56 | -104.8 | 152650 | 26 |
| MR_1774415989_EBC4A445 | 152650 | 223 | -95.4 | 152650 | 948 | -100.3 | 152650 | 56 | -108.1 | 152650 | 26 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 718: `17838df9-2ea...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `17838df9-2eae-4d98-9608-722b5d886a9a` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212064_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[718] topology](images/train_0718.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3242045_12 and 3238708_6
- `C2`: Increase transmission power for 3238708_6
- `C3`: Adjust the azimuth of 3238708_6 by 40 degrees
- `C4`: Add neighbor relationship between 3212064_3 and 3238708_6
- `C5`: Decrease transmission power for 3212064_3
- `C6`: Decrease transmission power for 3238708_6
- `C7`: Check test server and transmission issues
- `C8`: Press down the tilt angle of 3212064_3 by 2 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238708_6
- `C10`: Lift the tilt angle of 3212064_3 by 2 degrees
- `C11`: Increase A3 Offset threshold for 3238708_6
- `C12`: Adjust the azimuth of 3212064_3 by 39 degrees
- `C13`: Press down the tilt angle  of 3238708_6 by 4 degrees
- `C14`: Increase A3 Offset threshold for 3212064_3
- `C15`: Decrease A3 Offset threshold for 3238708_6
- `C16`: Increase transmission power for 3212064_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212064_3 **← 정답**
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238708_6
- `C20`: Decrease A3 Offset threshold for 3212064_3
- `C21`: Lift the tilt angle  of 3238708_6 by 4 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212064_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.999 | MS1 | 121.4656738609 | 31.1446374690 | 617 | 504990 | -94.79 | 10.54 | 475.68 | 0.03 | 2.86 | 1564 |
| 2024-09-20 22:21:32.206 | MS1 | 121.4656688207 | 31.1446326358 | 421 | 504990 | -95.09 | 13.46 | 350.99 | 0.01 | 2.70 | 1579 |
| 2024-09-20 22:21:33.750 | MS1 | 121.4656611049 | 31.1446224437 | 520 | 504990 | -95.82 | 14.18 | 433.66 | 0.18 | 2.23 | 1586 |
| 2024-09-20 22:21:34.484 | MS1 | 121.4656654238 | 31.1446370332 | 642 | 152650 | -91.52 | 7.64 | 94.93 | 0.10 | 1.74 | 990 |
| 2024-09-20 22:21:35.172 | MS1 | 121.4656638639 | 31.1446349115 | 924 | 152650 | -95.89 | 7.16 | 72.54 | 0.04 | 1.58 | 935 |
| 2024-09-20 22:21:36.187 | MS1 | 121.4656697804 | 31.1446206822 | 952 | 152650 | -95.98 | 4.04 | 56.95 | 0.15 | 1.73 | 952 |
| 2024-09-20 22:21:37.364 | MS1 | 121.4656693959 | 31.1446197276 | 87 | 152650 | -92.08 | 7.59 | 65.15 | 0.12 | 1.80 | 924 |
| 2024-09-20 22:21:38.736 | MS1 | 121.4656769435 | 31.1446340163 | 642 | 152650 | -96.85 | 3.71 | 83.41 | 0.17 | 1.76 | 990 |
| 2024-09-20 22:21:39.790 | MS1 | 121.4656680352 | 31.1446319030 | 924 | 152650 | -93.22 | 4.72 | 50.17 | 0.18 | 1.67 | 934 |
| 2024-09-20 22:21:40.118 | MS1 | 121.4656678500 | 31.1446250925 | 952 | 152650 | -94.81 | 7.05 | 95.21 | 0.14 | 2.16 | 1571 |
| 2024-09-20 22:21:41.290 | MS1 | 121.4656749625 | 31.1446261872 | 87 | 152650 | -89.91 | 6.51 | 77.81 | 0.01 | 2.22 | 1589 |
| 2024-09-20 22:21:42.770 | MS1 | 121.4656767204 | 31.1446207050 | 642 | 152650 | -91.37 | 2.32 | 65.50 | 0.16 | 2.52 | 1574 |

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
| 3212064 | 3 | 121.4730543379 | 31.1500691629 | 268 | 1 | 9 | 15.6 | TDD | 617 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3213816 | 7 | 121.4670395471 | 31.1521703401 | 83 | 3 | 10 | 6.4 | FDD | 320 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3215834 | 2 | 121.4685303856 | 31.1547319655 | 261 | 3 | 5 | 21.8 | TDD | 520 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3226320 | 8 | 121.4728346809 | 31.1505690038 | 136 | 10 | 3 | 15.0 | FDD | 642 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3236617 | 9 | 121.4646050298 | 31.1535418253 | 60 | 11 | 11 | 8.2 | FDD | 619 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3238708 | 6 | 121.4707584884 | 31.1488832418 | 186 | 3 | 0 | 6.5 | TDD | 253 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3239550 | 5 | 121.4681273594 | 31.1514252131 | 112 | 9 | 5 | 21.2 | TDD | 828 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3242045 | 12 | 121.4732971189 | 31.1539530656 | 32 | 12 | 6 | 5.0 | FDD | 952 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3244402 | 11 | 121.4729366676 | 31.1460139087 | 354 | 9 | 12 | 2.3 | FDD | 87 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3245847 | 10 | 121.4721718594 | 31.1466267195 | 323 | 5 | 12 | 8.8 | FDD | 402 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3265969 | 1 | 121.4689170434 | 31.1488193703 | 286 | 7 | 1 | 23.9 | TDD | 421 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3278027 | 13 | 121.4708802890 | 31.1507172009 | 256 | 5 | 12 | 3.5 | FDD | 924 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3279488 | 4 | 121.4697656286 | 31.1532291254 | 320 | 13 | 11 | 24.4 | TDD | 682 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.093 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.115 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.264 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.264 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.919 | NREventA2 | measId:1;ServCellPCI:180;Se... |
| 2024-09-20 22:21:35.055 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.279 | NREventA5 | measId:3;ServCellPCI:180;Se... |
| 2024-09-20 22:21:35.330 | NRHandoverAttempt | SourcePCI:180;SourceNR-ARFC... |
| 2024-09-20 22:21:35.351 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.365 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.506 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.506 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265969 | 1 | 10.8826 | 18.9981 | -116.9013 | 6.7839 | 143.4487 | 0.0115 | 0.0194 |
| 2024_09_20 22:00 | 3215834 | 2 | 10.7140 | 14.5877 | -116.8730 | 16.6352 | 138.6748 | 0.0117 | 0.0066 |
| 2024_09_20 22:00 | 3212064 | 3 | 11.6999 | 11.2344 | -116.5905 | 16.0964 | 99.7218 | 0.0199 | 0.0159 |
| 2024_09_20 22:00 | 3279488 | 4 | 12.9263 | 16.6374 | -114.8741 | 19.5793 | 171.4451 | 0.0172 | 0.0090 |
| 2024_09_20 22:00 | 3239550 | 5 | 11.8384 | 14.4269 | -116.3475 | 13.9318 | 185.3462 | 0.0103 | 0.0058 |
| 2024_09_20 22:00 | 3238708 | 6 | 10.5198 | 12.0100 | -114.6892 | 7.8291 | 187.5915 | 0.0095 | 0.0141 |
| 2024_09_20 22:00 | 3213816 | 7 | 7.6707 | 8.1151 | -117.7909 | 4.0472 | 49.1389 | 0.0166 | 0.0078 |
| 2024_09_20 22:00 | 3226320 | 8 | 6.3685 | 15.0927 | -116.8455 | 3.0149 | 24.4398 | 0.0200 | 0.0148 |
| 2024_09_20 22:00 | 3236617 | 9 | 18.9862 | 12.8689 | -114.2660 | 3.4724 | 54.0753 | 0.0143 | 0.0117 |
| 2024_09_20 22:00 | 3245847 | 10 | 11.1121 | 14.3932 | -115.7459 | 4.3979 | 22.4213 | 0.0103 | 0.0032 |
| 2024_09_20 22:00 | 3244402 | 11 | 19.9192 | 16.5848 | -114.8779 | 3.6919 | 54.5209 | 0.0129 | 0.0178 |
| 2024_09_20 22:00 | 3242045 | 12 | 16.1293 | 18.8043 | -117.0070 | 3.6261 | 39.7266 | 0.0090 | 0.0044 |
| 2024_09_20 22:00 | 3278027 | 13 | 8.8446 | 10.5266 | -115.9154 | 3.4986 | 25.6301 | 0.0102 | 0.0164 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413047_ECAB84CA | 504990 | 520 | -93.9 | 504990 | 253 | -99.2 | 504990 | 682 | -103.4 | 504990 | 828 |
| MR_1774413047_97152D6F | 504990 | 520 | -97.4 | 504990 | 253 | -97.9 | 504990 | 682 | -103.7 | 504990 | 828 |
| MR_1774413047_8BED6C49 | 504990 | 520 | -97.2 | 504990 | 253 | -98.4 | 504990 | 682 | -102.7 | 504990 | 828 |
| MR_1774413047_E5257683 | 504990 | 520 | -96.6 | 504990 | 253 | -101.3 | 504990 | 682 | -100.7 | 504990 | 828 |
| MR_1774413047_CE4FF4F6 | 504990 | 520 | -97.0 | 504990 | 253 | -101.5 | 504990 | 682 | -103.6 | 504990 | 828 |
| MR_1774413047_1135188A | 504990 | 520 | -96.7 | 504990 | 253 | -99.4 | 504990 | 682 | -103.6 | 504990 | 828 |
| MR_1774413047_781AA8DF | 504990 | 520 | -95.1 | 504990 | 253 | -100.1 | 504990 | 682 | -100.4 | 504990 | 828 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 719: `f32f391f-358...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f32f391f-3583-40fc-84b6-9a8411a8e7e1` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3214108_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[719] topology](images/train_0719.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3240008_2 and 3219004_4
- `C2`: Lift the tilt angle  of 3219004_4 by 6 degrees
- `C3`: Press down the tilt angle  of 3219004_4 by 6 degrees
- `C4`: Increase A3 Offset threshold for 3219004_4
- `C5`: Increase transmission power for 3219004_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214108_3 **← 정답**
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219004_4
- `C8`: Decrease transmission power for 3219004_4
- `C9`: Decrease transmission power for 3214108_3
- `C10`: Press down the tilt angle of 3214108_3 by 3 degrees
- `C11`: Adjust the azimuth of 3214108_3 by 7 degrees
- `C12`: Adjust the azimuth of 3219004_4 by 50 degrees
- `C13`: Check test server and transmission issues
- `C14`: Increase transmission power for 3214108_3
- `C15`: Lift the tilt angle of 3214108_3 by 3 degrees
- `C16`: Decrease A3 Offset threshold for 3219004_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219004_4
- `C18`: Increase A3 Offset threshold for 3214108_3
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease A3 Offset threshold for 3214108_3
- `C21`: Add neighbor relationship between 3214108_3 and 3219004_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214108_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.276 | MS1 | 121.4656619164 | 31.1446186774 | 950 | 504990 | -89.63 | 14.66 | 495.63 | 0.14 | 2.36 | 1586 |
| 2024-09-20 22:21:32.579 | MS1 | 121.4656635194 | 31.1446286334 | 950 | 504990 | -87.51 | 12.04 | 320.38 | 0.01 | 2.53 | 1596 |
| 2024-09-20 22:21:33.646 | MS1 | 121.4656698091 | 31.1446264728 | 950 | 504990 | -87.41 | 15.08 | 395.34 | 0.08 | 2.63 | 1595 |
| 2024-09-20 22:21:34.165 | MS1 | 121.4656614612 | 31.1446256276 | 950 | 504990 | -86.10 | 16.76 | 92.22 | 0.55 | 2.86 | 700 |
| 2024-09-20 22:21:35.255 | MS1 | 121.4656736565 | 31.1446377733 | 950 | 504990 | -88.84 | 12.62 | 74.72 | 0.57 | 2.08 | 690 |
| 2024-09-20 22:21:36.316 | MS1 | 121.4656623385 | 31.1446311224 | 950 | 504990 | -85.64 | 14.74 | 44.94 | 0.67 | 2.00 | 507 |
| 2024-09-20 22:21:37.745 | MS1 | 121.4656758552 | 31.1446377444 | 950 | 504990 | -93.79 | 9.16 | 76.93 | 0.63 | 2.72 | 671 |
| 2024-09-20 22:21:38.681 | MS1 | 121.4656631513 | 31.1446202347 | 950 | 504990 | -93.27 | 8.98 | 88.88 | 0.60 | 2.64 | 514 |
| 2024-09-20 22:21:39.510 | MS1 | 121.4656659381 | 31.1446343541 | 950 | 504990 | -90.79 | 8.57 | 86.69 | 0.68 | 2.73 | 678 |
| 2024-09-20 22:21:40.904 | MS1 | 121.4656709754 | 31.1446230547 | 950 | 504990 | -89.95 | 7.95 | 548.97 | 0.08 | 2.63 | 1576 |
| 2024-09-20 22:21:41.499 | MS1 | 121.4656626305 | 31.1446350431 | 950 | 504990 | -92.94 | 7.21 | 544.44 | 0.01 | 2.41 | 1591 |
| 2024-09-20 22:21:42.850 | MS1 | 121.4656744891 | 31.1446330762 | 950 | 504990 | -93.08 | 10.53 | 608.73 | 0.09 | 2.54 | 1567 |

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
| 3214108 | 3 | 121.4738020972 | 31.1453009580 | 258 | 2 | 4 | 18.2 | TDD | 950 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3219004 | 4 | 121.4658285403 | 31.1491297995 | 92 | 1 | 0 | 39.9 | TDD | 631 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3240008 | 2 | 121.4717645634 | 31.1459405845 | 53 | 9 | 5 | 49.7 | TDD | 157 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3262456 | 1 | 121.4709450036 | 31.1545438747 | 193 | 1 | 9 | 48.1 | TDD | 939 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.128 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.153 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.253 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.253 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.991 | NREventA3 | measId:2;ServCellPCI:353;Se... |
| 2024-09-20 22:21:38.231 | NRHandoverAttempt | SourcePCI:353;SourceNR-ARFC... |
| 2024-09-20 22:21:38.265 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.279 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.406 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.406 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262456 | 1 | 15.6337 | 17.3825 | -115.8402 | 14.8950 | 84.6744 | 0.0186 | 0.0114 |
| 2024_09_20 22:00 | 3240008 | 2 | 16.5980 | 5.2855 | -116.3400 | 18.0302 | 123.9330 | 0.0155 | 0.0027 |
| 2024_09_20 22:00 | 3214108 | 3 | 16.8787 | 11.3239 | -114.6520 | 5.8513 | 145.2514 | 0.0033 | 0.0137 |
| 2024_09_20 22:00 | 3219004 | 4 | 14.3913 | 17.8941 | -114.7383 | 17.7373 | 189.1749 | 0.0037 | 0.0078 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412265_F3265706 | 504990 | 950 | -86.8 | 504990 | 631 | -95.2 | 504990 | 157 | -97.7 | 504990 | 939 |
| MR_1774412265_E790B21D | 504990 | 950 | -86.9 | 504990 | 631 | -97.2 | 504990 | 157 | -97.9 | 504990 | 939 |
| MR_1774412265_1AD64FE1 | 504990 | 950 | -87.4 | 504990 | 631 | -97.1 | 504990 | 157 | -95.2 | 504990 | 939 |
| MR_1774412265_3355F271 | 504990 | 950 | -86.8 | 504990 | 631 | -94.2 | 504990 | 157 | -94.4 | 504990 | 939 |
| MR_1774412265_40A2B7CC | 504990 | 950 | -87.8 | 504990 | 631 | -95.1 | 504990 | 157 | -97.6 | 504990 | 939 |
| MR_1774412265_BCE94B7D | 504990 | 950 | -85.8 | 504990 | 631 | -94.8 | 504990 | 157 | -95.0 | 504990 | 939 |

> *... 2개 열 생략 (전체 14열)*

---
