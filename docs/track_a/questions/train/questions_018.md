# Track A 문제 분석 — train[170]~train[179]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[170] ~ train[179] (10개)

## 목차

1. [문제 170: `f10ee3ee-dfc...`](#170) — single-answer, 정답: C14
2. [문제 171: `4d7a186a-ccb...`](#171) — single-answer, 정답: C8
3. [문제 172: `972f4134-847...`](#172) — multiple-answer, 정답: C4|C16
4. [문제 173: `958efdfd-d94...`](#173) — single-answer, 정답: C1
5. [문제 174: `f417c963-6aa...`](#174) — single-answer, 정답: C10
6. [문제 175: `87506862-d83...`](#175) — single-answer, 정답: C20
7. [문제 176: `8d981055-ccd...`](#176) — multiple-answer, 정답: C3|C4|C16|C18
8. [문제 177: `51f3afc2-1ad...`](#177) — multiple-answer, 정답: C1|C13
9. [문제 178: `70852f60-f06...`](#178) — single-answer, 정답: C16
10. [문제 179: `0ee54769-7e9...`](#179) — multiple-answer, 정답: C12|C20

---

### 문제 170: `f10ee3ee-dfc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f10ee3ee-dfc9-4ddb-8b8a-a6d68363eeaf` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease A3 Offset threshold for 3243159_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[170] topology](images/train_0170.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3243159_1 by 50 degrees
- `C2`: Increase A3 Offset threshold for 3243159_1
- `C3`: Add neighbor relationship between 3243159_1 and 3216249_2
- `C4`: Check test server and transmission issues
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243159_1
- `C6`: Decrease transmission power for 3216249_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216249_2
- `C8`: Lift the tilt angle  of 3216249_2 by 4 degrees
- `C9`: Add neighbor relationship between 3224156_4 and 3216249_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216249_2
- `C11`: Increase transmission power for 3243159_1
- `C12`: Adjust the azimuth of 3216249_2 by 50 degrees
- `C13`: Press down the tilt angle of 3243159_1 by 10 degrees
- `C14`: Decrease A3 Offset threshold for 3243159_1 **← 정답**
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243159_1
- `C16`: Increase transmission power for 3216249_2
- `C17`: Press down the tilt angle  of 3216249_2 by 4 degrees
- `C18`: Increase A3 Offset threshold for 3216249_2
- `C19`: Lift the tilt angle of 3243159_1 by 10 degrees
- `C20`: Decrease transmission power for 3243159_1
- `C21`: Decrease A3 Offset threshold for 3216249_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.836 | MS1 | 121.4656696973 | 31.1446225736 | 538 | 504990 | -75.35 | 14.41 | 455.60 | 0.19 | 2.57 | 1579 |
| 2024-09-20 22:21:32.458 | MS1 | 121.4656739139 | 31.1446189691 | 538 | 504990 | -75.93 | 17.25 | 293.08 | 0.03 | 2.18 | 1583 |
| 2024-09-20 22:21:33.773 | MS1 | 121.4656617440 | 31.1446188999 | 538 | 504990 | -78.19 | 14.62 | 402.03 | 0.20 | 2.23 | 1584 |
| 2024-09-20 22:21:34.825 | MS1 | 121.4656684715 | 31.1446258479 | 538 | 504990 | -84.74 | -3.81 | 75.84 | 0.12 | 1.23 | 1593 |
| 2024-09-20 22:21:35.597 | MS1 | 121.4656646209 | 31.1446204382 | 538 | 504990 | -86.39 | -3.71 | 28.62 | 0.16 | 1.23 | 1581 |
| 2024-09-20 22:21:36.259 | MS1 | 121.4656623542 | 31.1446315429 | 538 | 504990 | -89.67 | -2.25 | 56.53 | 0.15 | 1.12 | 1591 |
| 2024-09-20 22:21:37.673 | MS1 | 121.4656682748 | 31.1446364029 | 538 | 504990 | -84.55 | -2.20 | 75.55 | 0.11 | 1.13 | 1581 |
| 2024-09-20 22:21:38.730 | MS1 | 121.4656758902 | 31.1446182446 | 538 | 504990 | -88.23 | -3.27 | 65.13 | 0.12 | 1.04 | 1566 |
| 2024-09-20 22:21:39.287 | MS1 | 121.4656601434 | 31.1446300558 | 812 | 504990 | -78.99 | 15.23 | 177.54 | 0.14 | 1.06 | 1565 |
| 2024-09-20 22:21:40.300 | MS1 | 121.4656696410 | 31.1446244084 | 812 | 504990 | -84.42 | 13.89 | 368.87 | 0.10 | 2.19 | 1570 |
| 2024-09-20 22:21:41.380 | MS1 | 121.4656603098 | 31.1446349764 | 812 | 504990 | -82.53 | 16.31 | 540.51 | 0.07 | 2.73 | 1587 |
| 2024-09-20 22:21:42.632 | MS1 | 121.4656685867 | 31.1446354416 | 812 | 504990 | -77.66 | 16.85 | 389.82 | 0.13 | 2.84 | 1584 |

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
| 3216249 | 2 | 121.4759873150 | 31.1520444441 | 12 | 2 | 3 | 43.2 | TDD | 812 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3224156 | 4 | 121.4705353236 | 31.1485298027 | 81 | 7 | 8 | 37.2 | TDD | 166 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3236856 | 3 | 121.4661853041 | 31.1510052849 | 299 | 2 | 12 | 44.7 | TDD | 453 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3243159 | 1 | 121.4652735739 | 31.1448034246 | 211 | 0 | 7 | 38.2 | TDD | 538 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.558 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.577 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.687 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.687 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.437 | NREventA3 | measId:2;ServCellPCI:156;Se... |
| 2024-09-20 22:21:38.677 | NRHandoverAttempt | SourcePCI:156;SourceNR-ARFC... |
| 2024-09-20 22:21:38.711 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.725 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.826 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.826 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243159 | 1 | 5.7212 | 9.2349 | -114.9446 | 15.2815 | 116.2955 | 0.0035 | 0.1216 |
| 2024_09_20 22:00 | 3216249 | 2 | 14.7671 | 12.1433 | -115.2825 | 16.6078 | 137.3350 | 0.0045 | 0.0099 |
| 2024_09_20 22:00 | 3236856 | 3 | 11.0848 | 11.3190 | -117.1937 | 19.4378 | 156.0208 | 0.0182 | 0.0080 |
| 2024_09_20 22:00 | 3224156 | 4 | 6.1736 | 9.1423 | -117.9983 | 12.3820 | 134.7968 | 0.0196 | 0.0071 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412106_61E4598F | 504990 | 538 | -86.5 | 504990 | 812 | -79.0 | 504990 | 166 | -79.8 | 504990 | 453 |
| MR_1774412106_031BA40F | 504990 | 538 | -84.4 | 504990 | 812 | -77.0 | 504990 | 166 | -80.9 | 504990 | 453 |
| MR_1774412106_62CD165C | 504990 | 812 | -79.4 | 504990 | 538 | -85.9 | 504990 | 166 | -78.6 | 504990 | 453 |
| MR_1774412106_63394C0E | 504990 | 812 | -78.4 | 504990 | 538 | -83.4 | 504990 | 166 | -82.4 | 504990 | 453 |
| MR_1774412106_903B387F | 504990 | 538 | -83.4 | 504990 | 812 | -76.4 | 504990 | 166 | -80.1 | 504990 | 453 |
| MR_1774412106_9B6A2205 | 504990 | 538 | -85.4 | 504990 | 812 | -76.9 | 504990 | 166 | -78.9 | 504990 | 453 |
| MR_1774412106_00F8751C | 504990 | 538 | -84.9 | 504990 | 812 | -78.7 | 504990 | 166 | -79.6 | 504990 | 453 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 171: `4d7a186a-ccb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4d7a186a-ccb0-472e-8ca7-ec473d102d9b` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3239173_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[171] topology](images/train_0171.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3239173_4 by 3 degrees
- `C2`: Add neighbor relationship between 3244573_3 and 3277402_1
- `C3`: Adjust the azimuth of 3239173_4 by 32 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239173_4
- `C5`: Lift the tilt angle  of 3277402_1 by 4 degrees
- `C6`: Decrease A3 Offset threshold for 3239173_4
- `C7`: Press down the tilt angle of 3239173_4 by 3 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239173_4 **← 정답**
- `C9`: Decrease transmission power for 3239173_4
- `C10`: Press down the tilt angle  of 3277402_1 by 4 degrees
- `C11`: Check test server and transmission issues
- `C12`: Decrease A3 Offset threshold for 3277402_1
- `C13`: Increase transmission power for 3277402_1
- `C14`: Increase A3 Offset threshold for 3239173_4
- `C15`: Increase transmission power for 3239173_4
- `C16`: Add neighbor relationship between 3239173_4 and 3277402_1
- `C17`: Decrease transmission power for 3277402_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277402_1
- `C20`: Adjust the azimuth of 3277402_1 by 50 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277402_1
- `C22`: Increase A3 Offset threshold for 3277402_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.231 | MS1 | 121.4656749066 | 31.1446311902 | 39 | 504990 | -86.13 | 17.44 | 577.18 | 0.11 | 2.19 | 1585 |
| 2024-09-20 22:21:32.946 | MS1 | 121.4656741660 | 31.1446360387 | 39 | 504990 | -90.17 | 17.07 | 418.03 | 0.13 | 2.88 | 1598 |
| 2024-09-20 22:21:33.779 | MS1 | 121.4656601315 | 31.1446203529 | 39 | 504990 | -91.40 | 15.71 | 486.77 | 0.01 | 2.52 | 1569 |
| 2024-09-20 22:21:34.762 | MS1 | 121.4656603423 | 31.1446307200 | 39 | 504990 | -90.11 | 16.25 | 68.82 | 0.58 | 2.17 | 657 |
| 2024-09-20 22:21:35.104 | MS1 | 121.4656676495 | 31.1446343431 | 39 | 504990 | -87.69 | 12.82 | 84.05 | 0.62 | 2.60 | 665 |
| 2024-09-20 22:21:36.135 | MS1 | 121.4656725631 | 31.1446329267 | 39 | 504990 | -85.45 | 13.65 | 71.47 | 0.66 | 2.67 | 591 |
| 2024-09-20 22:21:37.852 | MS1 | 121.4656667534 | 31.1446300197 | 39 | 504990 | -90.84 | 9.73 | 63.18 | 0.54 | 2.96 | 625 |
| 2024-09-20 22:21:38.778 | MS1 | 121.4656679671 | 31.1446290125 | 39 | 504990 | -91.54 | 10.15 | 77.02 | 0.64 | 2.16 | 622 |
| 2024-09-20 22:21:39.987 | MS1 | 121.4656774989 | 31.1446349038 | 39 | 504990 | -92.81 | 12.47 | 84.85 | 0.58 | 2.34 | 562 |
| 2024-09-20 22:21:40.209 | MS1 | 121.4656676610 | 31.1446256834 | 39 | 504990 | -93.20 | 9.02 | 458.72 | 0.05 | 2.80 | 1595 |
| 2024-09-20 22:21:41.821 | MS1 | 121.4656616343 | 31.1446356195 | 39 | 504990 | -91.27 | 9.68 | 454.41 | 0.00 | 2.23 | 1580 |
| 2024-09-20 22:21:42.252 | MS1 | 121.4656717562 | 31.1446375978 | 39 | 504990 | -93.03 | 9.06 | 604.48 | 0.15 | 2.16 | 1595 |

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
| 3239173 | 4 | 121.4645961750 | 31.1520555268 | 141 | 2 | 12 | 20.9 | TDD | 39 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3244573 | 3 | 121.4721979878 | 31.1526576268 | 58 | 4 | 1 | 17.6 | TDD | 369 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3265884 | 2 | 121.4651006834 | 31.1555494330 | 140 | 15 | 11 | 15.5 | TDD | 332 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3277402 | 1 | 121.4718540140 | 31.1463096505 | 17 | 3 | 11 | 15.1 | TDD | 753 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.591 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.699 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.699 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.466 | NREventA3 | measId:2;ServCellPCI:961;Se... |
| 2024-09-20 22:21:38.706 | NRHandoverAttempt | SourcePCI:961;SourceNR-ARFC... |
| 2024-09-20 22:21:38.752 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.766 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.893 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.893 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277402 | 1 | 13.8594 | 12.0362 | -117.7438 | 7.8330 | 174.3413 | 0.0197 | 0.0117 |
| 2024_09_20 22:00 | 3265884 | 2 | 16.3166 | 8.3932 | -115.1120 | 17.6670 | 153.7738 | 0.0030 | 0.0068 |
| 2024_09_20 22:00 | 3244573 | 3 | 16.5052 | 13.7008 | -115.5073 | 15.3716 | 155.5038 | 0.0160 | 0.0050 |
| 2024_09_20 22:00 | 3239173 | 4 | 6.8949 | 16.2686 | -114.0804 | 9.2767 | 131.0819 | 0.0179 | 0.0138 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412048_77D4F536 | 504990 | 39 | -91.3 | 504990 | 753 | -100.9 | 504990 | 369 | -103.3 | 504990 | 332 |
| MR_1774412048_74FE04DF | 504990 | 39 | -90.1 | 504990 | 753 | -97.2 | 504990 | 369 | -103.0 | 504990 | 332 |
| MR_1774412048_2E84DBD3 | 504990 | 39 | -90.1 | 504990 | 753 | -100.3 | 504990 | 369 | -102.8 | 504990 | 332 |
| MR_1774412048_8940F7BF | 504990 | 39 | -91.2 | 504990 | 753 | -99.0 | 504990 | 369 | -101.9 | 504990 | 332 |
| MR_1774412048_392A7800 | 504990 | 39 | -90.8 | 504990 | 753 | -101.0 | 504990 | 369 | -102.3 | 504990 | 332 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 172: `972f4134-847...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `972f4134-847d-4a9e-bfaa-c4db51f0a1e6` |
| Tag | **multiple-answer** |
| 정답 | **C4|C16** |
| C4 의미 | Adjust the azimuth of 3262364_4 by 34 degrees |
| C16 의미 | Increase transmission power for 3262364_4 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[172] topology](images/train_0172.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3264596_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264596_2
- `C3`: Decrease A3 Offset threshold for 3264596_2
- `C4`: Adjust the azimuth of 3262364_4 by 34 degrees **← 정답**
- `C5`: Increase A3 Offset threshold for 3264596_2
- `C6`: Decrease transmission power for 3262364_4
- `C7`: Decrease A3 Offset threshold for 3262364_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264596_2
- `C9`: Add neighbor relationship between 3226007_1 and 3264596_2
- `C10`: Add neighbor relationship between 3262364_4 and 3264596_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262364_4
- `C12`: Press down the tilt angle  of 3264596_2 by 5 degrees
- `C13`: Lift the tilt angle of 3262364_4 by 7 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262364_4
- `C15`: Check test server and transmission issues
- `C16`: Increase transmission power for 3262364_4 **← 정답**
- `C17`: Adjust the azimuth of 3264596_2 by 21 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Increase A3 Offset threshold for 3262364_4
- `C20`: Decrease transmission power for 3264596_2
- `C21`: Press down the tilt angle of 3262364_4 by 7 degrees
- `C22`: Lift the tilt angle  of 3264596_2 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.874 | MS1 | 121.4656662174 | 31.1446194763 | 452 | 504990 | -86.22 | 14.16 | 298.91 | 0.10 | 2.48 | 1561 |
| 2024-09-20 22:21:32.317 | MS1 | 121.4656705404 | 31.1446337472 | 452 | 504990 | -93.24 | 14.01 | 534.85 | 0.06 | 2.31 | 1584 |
| 2024-09-20 22:21:33.378 | MS1 | 121.4656699794 | 31.1446369692 | 452 | 504990 | -90.13 | 16.49 | 327.97 | 0.08 | 2.64 | 1589 |
| 2024-09-20 22:21:34.240 | MS1 | 121.4656638156 | 31.1446206859 | 452 | 504990 | -105.59 | 0.07 | 82.20 | 0.09 | 1.16 | 1571 |
| 2024-09-20 22:21:35.864 | MS1 | 121.4656581948 | 31.1446339695 | 452 | 504990 | -106.69 | 0.12 | 21.47 | 0.12 | 1.06 | 1592 |
| 2024-09-20 22:21:36.294 | MS1 | 121.4656659389 | 31.1446361574 | 452 | 504990 | -106.08 | 0.07 | 62.76 | 0.12 | 1.01 | 1589 |
| 2024-09-20 22:21:37.549 | MS1 | 121.4656655053 | 31.1446230636 | 452 | 504990 | -109.58 | 1.01 | 47.13 | 0.07 | 1.20 | 1600 |
| 2024-09-20 22:21:38.164 | MS1 | 121.4656617087 | 31.1446359422 | 452 | 504990 | -104.40 | 0.31 | 53.61 | 0.18 | 1.07 | 1600 |
| 2024-09-20 22:21:39.896 | MS1 | 121.4656622644 | 31.1446251829 | 452 | 504990 | -105.01 | 1.49 | 71.25 | 0.10 | 1.40 | 1600 |
| 2024-09-20 22:21:40.580 | MS1 | 121.4656649819 | 31.1446250399 | 452 | 504990 | -88.67 | 15.87 | 358.70 | 0.07 | 2.92 | 1581 |
| 2024-09-20 22:21:41.466 | MS1 | 121.4656709503 | 31.1446340936 | 452 | 504990 | -87.07 | 17.89 | 390.03 | 0.17 | 2.89 | 1573 |
| 2024-09-20 22:21:42.473 | MS1 | 121.4656733890 | 31.1446359831 | 452 | 504990 | -87.98 | 14.10 | 315.29 | 0.15 | 2.25 | 1591 |

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
| 3226007 | 1 | 121.4647903724 | 31.1500380421 | 52 | 15 | 12 | 19.4 | TDD | 953 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3229854 | 3 | 121.4662790104 | 31.1452128735 | 228 | 12 | 4 | 19.8 | TDD | 251 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3262364 | 4 | 121.4702452957 | 31.1542917628 | 236 | 6 | 7 | 26.4 | TDD | 452 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3264596 | 2 | 121.4759148516 | 31.1445317959 | 292 | 2 | 8 | 43.8 | TDD | 370 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.450 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.469 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.580 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.580 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.825 | NREventA2 | measId:1;ServCellPCI:144;Se... |
| 2024-09-20 22:21:34.966 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226007 | 1 | 5.4371 | 19.7703 | -116.7648 | 17.3971 | 115.8571 | 0.0145 | 0.0134 |
| 2024_09_20 22:00 | 3264596 | 2 | 17.4664 | 15.9437 | -116.3337 | 11.0765 | 85.7722 | 0.0064 | 0.0186 |
| 2024_09_20 22:00 | 3229854 | 3 | 6.3308 | 19.1962 | -115.2173 | 18.8695 | 131.3810 | 0.0107 | 0.0146 |
| 2024_09_20 22:00 | 3262364 | 4 | 12.4208 | 7.6017 | -117.6792 | 10.6501 | 92.8886 | 0.1769 | 0.0076 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415054_8136178C | 504990 | 452 | -106.6 | 504990 | 370 | -109.7 | 504990 | 953 | -115.7 | 504990 | 251 |
| MR_1774415054_5CBF4D35 | 504990 | 452 | -103.8 | 504990 | 370 | -111.1 | 504990 | 953 | -115.2 | 504990 | 251 |
| MR_1774415054_7D8719EE | 504990 | 452 | -104.0 | 504990 | 370 | -111.4 | 504990 | 953 | -116.7 | 504990 | 251 |
| MR_1774415054_C994C5D2 | 504990 | 452 | -106.6 | 504990 | 370 | -111.5 | 504990 | 953 | -115.5 | 504990 | 251 |
| MR_1774415054_138B973A | 504990 | 452 | -103.8 | 504990 | 370 | -110.1 | 504990 | 953 | -116.7 | 504990 | 251 |
| MR_1774415054_B3F6368E | 504990 | 452 | -106.6 | 504990 | 370 | -111.6 | 504990 | 953 | -117.7 | 504990 | 251 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 173: `958efdfd-d94...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `958efdfd-d949-4117-9052-1f5c57585667` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[173] topology](images/train_0173.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment. **← 정답**
- `C2`: Increase A3 Offset threshold for 3229544_1
- `C3`: Decrease transmission power for 3220067_4
- `C4`: Increase A3 Offset threshold for 3220067_4
- `C5`: Adjust the azimuth of 3220067_4 by 50 degrees
- `C6`: Lift the tilt angle of 3229544_1 by 6 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229544_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220067_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229544_1
- `C10`: Add neighbor relationship between 3229544_1 and 3220067_4
- `C11`: Press down the tilt angle  of 3220067_4 by 10 degrees
- `C12`: Check test server and transmission issues
- `C13`: Decrease A3 Offset threshold for 3220067_4
- `C14`: Add neighbor relationship between 3248898_2 and 3220067_4
- `C15`: Lift the tilt angle  of 3220067_4 by 10 degrees
- `C16`: Increase transmission power for 3220067_4
- `C17`: Adjust the azimuth of 3229544_1 by 2 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220067_4
- `C19`: Decrease transmission power for 3229544_1
- `C20`: Decrease A3 Offset threshold for 3229544_1
- `C21`: Increase transmission power for 3229544_1
- `C22`: Press down the tilt angle of 3229544_1 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.801 | MS1 | 121.4656765934 | 31.1446233681 | 911 | 504990 | -85.76 | 17.00 | 553.73 | 0.15 | 2.56 | 1567 |
| 2024-09-20 22:21:32.669 | MS1 | 121.4656773506 | 31.1446322274 | 911 | 504990 | -91.24 | 15.15 | 575.89 | 0.16 | 2.25 | 1600 |
| 2024-09-20 22:21:33.786 | MS1 | 121.4656691342 | 31.1446326872 | 911 | 504990 | -91.43 | 14.17 | 402.02 | 0.02 | 2.12 | 1595 |
| 2024-09-20 22:21:34.877 | MS1 | 121.4656725148 | 31.1446209353 | 911 | 504990 | -87.54 | 13.45 | 89.03 | 0.02 | 2.25 | 1598 |
| 2024-09-20 22:21:35.260 | MS1 | 121.4656661219 | 31.1446258297 | 911 | 504990 | -90.56 | 13.60 | 77.32 | 0.13 | 2.88 | 1562 |
| 2024-09-20 22:21:36.269 | MS1 | 121.4656742879 | 31.1446250702 | 911 | 504990 | -85.99 | 13.43 | 58.43 | 0.08 | 2.02 | 1573 |
| 2024-09-20 22:21:37.469 | MS1 | 121.4656750860 | 31.1446194940 | 911 | 504990 | -91.44 | 9.39 | 70.77 | 0.16 | 2.13 | 1593 |
| 2024-09-20 22:21:38.498 | MS1 | 121.4656631940 | 31.1446326763 | 911 | 504990 | -93.38 | 12.03 | 72.81 | 0.01 | 2.11 | 1600 |
| 2024-09-20 22:21:39.240 | MS1 | 121.4656665076 | 31.1446306715 | 911 | 504990 | -92.05 | 9.37 | 59.15 | 0.19 | 2.19 | 1590 |
| 2024-09-20 22:21:40.752 | MS1 | 121.4656585276 | 31.1446255220 | 911 | 504990 | -92.42 | 11.13 | 382.74 | 0.17 | 2.33 | 1591 |
| 2024-09-20 22:21:41.923 | MS1 | 121.4656678634 | 31.1446223410 | 911 | 504990 | -93.34 | 11.93 | 337.96 | 0.04 | 2.90 | 1563 |
| 2024-09-20 22:21:42.515 | MS1 | 121.4656667385 | 31.1446239879 | 911 | 504990 | -92.64 | 7.37 | 327.97 | 0.11 | 2.51 | 1579 |

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
| 3220067 | 4 | 121.4665757602 | 31.1447731216 | 86 | 10 | 9 | 28.9 | TDD | 335 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3229544 | 1 | 121.4754004979 | 31.1491292601 | 240 | 4 | 6 | 44.0 | TDD | 911 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3248898 | 2 | 121.4757987873 | 31.1478637927 | 274 | 13 | 6 | 47.7 | TDD | 577 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3279092 | 3 | 121.4758163312 | 31.1510434368 | 332 | 9 | 11 | 20.2 | TDD | 341 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.463 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.485 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.610 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.610 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.335 | NREventA3 | measId:2;ServCellPCI:883;Se... |
| 2024-09-20 22:21:38.575 | NRHandoverAttempt | SourcePCI:883;SourceNR-ARFC... |
| 2024-09-20 22:21:38.622 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.636 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.781 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.781 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3229544 | 1 | 79.8574 | 93.7378 | -115.4579 | 17.8223 | 134.5058 | 0.0046 | 0.0109 |
| 2024_09_19 22:00 | 3248898 | 2 | 76.5605 | 89.5231 | -117.9346 | 16.4110 | 163.2899 | 0.0127 | 0.0009 |
| 2024_09_19 22:00 | 3279092 | 3 | 80.8963 | 91.3098 | -117.3722 | 13.4624 | 169.1382 | 0.0124 | 0.0062 |
| 2024_09_19 22:00 | 3220067 | 4 | 78.6163 | 84.5115 | -115.6628 | 11.6132 | 111.5958 | 0.0172 | 0.0171 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414404_43320236 | 504990 | 911 | -86.5 | 504990 | 335 | -88.4 | 504990 | 577 | -101.4 | 504990 | 341 |
| MR_1774414404_6ECF83D1 | 504990 | 911 | -87.5 | 504990 | 335 | -85.9 | 504990 | 577 | -101.3 | 504990 | 341 |
| MR_1774414404_59EE688B | 504990 | 911 | -86.8 | 504990 | 335 | -88.0 | 504990 | 577 | -100.1 | 504990 | 341 |
| MR_1774414404_4ED55E4E | 504990 | 911 | -85.9 | 504990 | 335 | -87.5 | 504990 | 577 | -101.0 | 504990 | 341 |
| MR_1774414404_6B70887F | 504990 | 911 | -88.8 | 504990 | 335 | -86.3 | 504990 | 577 | -101.7 | 504990 | 341 |
| MR_1774414404_AAEC4A86 | 504990 | 911 | -87.0 | 504990 | 335 | -86.3 | 504990 | 577 | -101.2 | 504990 | 341 |
| MR_1774414404_25F96EEE | 504990 | 911 | -86.7 | 504990 | 335 | -88.4 | 504990 | 577 | -99.7 | 504990 | 341 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 174: `f417c963-6aa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f417c963-6aa8-4f06-b690-3e335fbb202d` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[174] topology](images/train_0174.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3220731_1 and 3273878_2
- `C2`: Adjust the azimuth of 3273878_2 by 47 degrees
- `C3`: Increase A3 Offset threshold for 3273878_2
- `C4`: Decrease A3 Offset threshold for 3273878_2
- `C5`: Add neighbor relationship between 3252883_4 and 3273878_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252883_4
- `C7`: Press down the tilt angle  of 3273878_2 by 7 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273878_2
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Check test server and transmission issues **← 정답**
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252883_4
- `C12`: Decrease transmission power for 3252883_4
- `C13`: Increase transmission power for 3252883_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273878_2
- `C15`: Increase transmission power for 3273878_2
- `C16`: Increase A3 Offset threshold for 3252883_4
- `C17`: Press down the tilt angle of 3252883_4 by 10 degrees
- `C18`: Decrease transmission power for 3273878_2
- `C19`: Lift the tilt angle  of 3273878_2 by 7 degrees
- `C20`: Adjust the azimuth of 3252883_4 by 28 degrees
- `C21`: Decrease A3 Offset threshold for 3252883_4
- `C22`: Lift the tilt angle of 3252883_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.929 | MS1 | 121.4656674045 | 31.1446185803 | 455 | 504990 | -85.47 | 12.60 | 406.02 | 0.18 | 2.34 | 1572 |
| 2024-09-20 22:21:32.579 | MS1 | 121.4656739049 | 31.1446342005 | 455 | 504990 | -86.76 | 15.17 | 502.49 | 0.09 | 2.13 | 1579 |
| 2024-09-20 22:21:33.329 | MS1 | 121.4656639644 | 31.1446199206 | 455 | 504990 | -88.34 | 14.36 | 575.46 | 0.17 | 2.89 | 1594 |
| 2024-09-20 22:21:34.602 | MS1 | 121.4656602223 | 31.1446272765 | 455 | 504990 | -85.39 | 15.71 | 60.71 | 0.16 | 2.82 | 355 |
| 2024-09-20 22:21:35.522 | MS1 | 121.4656651843 | 31.1446224907 | 455 | 504990 | -90.82 | 13.95 | 82.24 | 0.07 | 2.14 | 435 |
| 2024-09-20 22:21:36.349 | MS1 | 121.4656734620 | 31.1446227840 | 455 | 504990 | -86.68 | 14.46 | 62.43 | 0.18 | 2.68 | 300 |
| 2024-09-20 22:21:37.922 | MS1 | 121.4656719195 | 31.1446351887 | 455 | 504990 | -93.00 | 7.70 | 80.18 | 0.19 | 2.75 | 317 |
| 2024-09-20 22:21:38.495 | MS1 | 121.4656764945 | 31.1446211937 | 455 | 504990 | -93.39 | 11.86 | 53.56 | 0.17 | 2.98 | 499 |
| 2024-09-20 22:21:39.460 | MS1 | 121.4656748835 | 31.1446182409 | 455 | 504990 | -90.23 | 11.37 | 87.80 | 0.05 | 2.16 | 380 |
| 2024-09-20 22:21:40.471 | MS1 | 121.4656587504 | 31.1446300252 | 455 | 504990 | -89.79 | 7.46 | 533.61 | 0.14 | 2.23 | 1573 |
| 2024-09-20 22:21:41.324 | MS1 | 121.4656732042 | 31.1446309398 | 455 | 504990 | -89.54 | 11.66 | 509.53 | 0.06 | 2.94 | 1573 |
| 2024-09-20 22:21:42.771 | MS1 | 121.4656592976 | 31.1446194519 | 455 | 504990 | -92.50 | 12.42 | 428.58 | 0.01 | 2.79 | 1592 |

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
| 3220731 | 1 | 121.4687543080 | 31.1478448451 | 279 | 10 | 1 | 42.5 | TDD | 616 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3252883 | 4 | 121.4681703133 | 31.1475727831 | 188 | 14 | 4 | 36.4 | TDD | 455 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3271724 | 3 | 121.4732389112 | 31.1452925245 | 58 | 5 | 9 | 33.2 | TDD | 654 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3273878 | 2 | 121.4659508414 | 31.1519657986 | 135 | 5 | 9 | 25.8 | TDD | 17 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.890 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.914 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.036 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.036 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.720 | NREventA3 | measId:2;ServCellPCI:178;Se... |
| 2024-09-20 22:21:37.960 | NRHandoverAttempt | SourcePCI:178;SourceNR-ARFC... |
| 2024-09-20 22:21:37.997 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.008 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.157 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.157 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220731 | 1 | 7.3276 | 7.4043 | -114.5247 | 5.9317 | 154.5316 | 0.0075 | 0.0082 |
| 2024_09_20 22:00 | 3273878 | 2 | 11.3101 | 18.2599 | -116.9137 | 5.4829 | 198.7010 | 0.0003 | 0.0034 |
| 2024_09_20 22:00 | 3271724 | 3 | 12.6481 | 9.0229 | -117.9882 | 12.1536 | 135.4153 | 0.0042 | 0.0153 |
| 2024_09_20 22:00 | 3252883 | 4 | 12.9449 | 18.3777 | -115.9780 | 10.6849 | 133.9078 | 0.0075 | 0.0193 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415993_F07F2C73 | 504990 | 455 | -86.4 | 504990 | 17 | -91.1 | 504990 | 616 | -93.8 | 504990 | 654 |
| MR_1774415993_55A6CB07 | 504990 | 455 | -86.1 | 504990 | 17 | -91.4 | 504990 | 616 | -93.5 | 504990 | 654 |
| MR_1774415993_B89E91EC | 504990 | 455 | -84.9 | 504990 | 17 | -93.0 | 504990 | 616 | -91.9 | 504990 | 654 |
| MR_1774415993_2A4658DC | 504990 | 455 | -84.3 | 504990 | 17 | -94.5 | 504990 | 616 | -94.1 | 504990 | 654 |
| MR_1774415993_B0D5D094 | 504990 | 455 | -83.4 | 504990 | 17 | -91.6 | 504990 | 616 | -95.2 | 504990 | 654 |
| MR_1774415993_767B2F23 | 504990 | 455 | -83.7 | 504990 | 17 | -94.6 | 504990 | 616 | -91.4 | 504990 | 654 |
| MR_1774415993_1ED158AD | 504990 | 455 | -86.0 | 504990 | 17 | -92.1 | 504990 | 616 | -92.3 | 504990 | 654 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 175: `87506862-d83...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `87506862-d835-4c23-8368-acb5b9e38519` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[175] topology](images/train_0175.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Increase A3 Offset threshold for 3222067_1
- `C3`: Lift the tilt angle  of 3225809_2 by 10 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222067_1
- `C5`: Press down the tilt angle  of 3225809_2 by 10 degrees
- `C6`: Increase transmission power for 3222067_1
- `C7`: Increase transmission power for 3225809_2
- `C8`: Adjust the azimuth of 3222067_1 by 50 degrees
- `C9`: Add neighbor relationship between 3222067_1 and 3225809_2
- `C10`: Decrease transmission power for 3225809_2
- `C11`: Lift the tilt angle of 3222067_1 by 4 degrees
- `C12`: Decrease A3 Offset threshold for 3225809_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222067_1
- `C14`: Add neighbor relationship between 3246263_4 and 3225809_2
- `C15`: Decrease A3 Offset threshold for 3222067_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225809_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225809_2
- `C18`: Adjust the azimuth of 3225809_2 by 50 degrees
- `C19`: Increase A3 Offset threshold for 3225809_2
- `C20`: Insufficient data; more data is needed for judgment. **← 정답**
- `C21`: Decrease transmission power for 3222067_1
- `C22`: Press down the tilt angle of 3222067_1 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.926 | MS1 | 121.4656591975 | 31.1446310534 | 440 | 504990 | -85.51 | 13.12 | 298.86 | 0.03 | 2.08 | 1576 |
| 2024-09-20 22:21:32.104 | MS1 | 121.4656629360 | 31.1446269280 | 440 | 504990 | -88.00 | 13.97 | 497.45 | 0.20 | 2.74 | 1571 |
| 2024-09-20 22:21:33.408 | MS1 | 121.4656710985 | 31.1446294752 | 440 | 504990 | -90.41 | 16.68 | 296.28 | 0.14 | 2.60 | 1584 |
| 2024-09-20 22:21:34.403 | MS1 | 121.4656687211 | 31.1446321279 | 440 | 504990 | -87.69 | 13.14 | 58.16 | 0.12 | 2.18 | 1562 |
| 2024-09-20 22:21:35.250 | MS1 | 121.4656651519 | 31.1446212463 | 440 | 504990 | -89.35 | 16.86 | 56.16 | 0.19 | 2.71 | 1566 |
| 2024-09-20 22:21:36.233 | MS1 | 121.4656665313 | 31.1446218955 | 440 | 504990 | -85.81 | 14.89 | 62.66 | 0.13 | 2.40 | 1570 |
| 2024-09-20 22:21:37.330 | MS1 | 121.4656660436 | 31.1446326220 | 440 | 504990 | -92.45 | 12.97 | 57.33 | 0.12 | 2.75 | 1583 |
| 2024-09-20 22:21:38.515 | MS1 | 121.4656725675 | 31.1446245416 | 440 | 504990 | -91.62 | 9.67 | 69.80 | 0.17 | 2.86 | 1586 |
| 2024-09-20 22:21:39.343 | MS1 | 121.4656706995 | 31.1446357616 | 440 | 504990 | -90.00 | 8.08 | 66.38 | 0.05 | 2.31 | 1569 |
| 2024-09-20 22:21:40.542 | MS1 | 121.4656751678 | 31.1446220644 | 440 | 504990 | -90.28 | 9.35 | 579.07 | 0.13 | 2.71 | 1591 |
| 2024-09-20 22:21:41.918 | MS1 | 121.4656658275 | 31.1446321463 | 440 | 504990 | -92.40 | 9.31 | 364.41 | 0.01 | 2.40 | 1598 |
| 2024-09-20 22:21:42.444 | MS1 | 121.4656621652 | 31.1446248388 | 440 | 504990 | -92.51 | 7.73 | 484.10 | 0.15 | 2.91 | 1580 |

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
| 3222067 | 1 | 121.4718917637 | 31.1485088339 | 10 | 1 | 6 | 44.8 | TDD | 440 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3225809 | 2 | 121.4710832018 | 31.1515409350 | 108 | 14 | 10 | 43.8 | TDD | 843 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3244356 | 3 | 121.4686091962 | 31.1529057760 | 167 | 4 | 3 | 30.3 | TDD | 363 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3246263 | 4 | 121.4713883363 | 31.1470446986 | 352 | 10 | 9 | 31.5 | TDD | 373 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.219 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.240 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.381 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.381 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.042 | NREventA3 | measId:2;ServCellPCI:774;Se... |
| 2024-09-20 22:21:38.282 | NRHandoverAttempt | SourcePCI:774;SourceNR-ARFC... |
| 2024-09-20 22:21:38.327 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.340 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.484 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.484 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3222067 | 1 | 79.6866 | 86.6680 | -117.9908 | 10.6971 | 165.4117 | 0.0153 | 0.0184 |
| 2024_09_19 22:00 | 3225809 | 2 | 86.5592 | 90.2724 | -116.9227 | 12.0589 | 143.7640 | 0.0146 | 0.0171 |
| 2024_09_19 22:00 | 3244356 | 3 | 75.1544 | 77.1983 | -115.1514 | 12.0621 | 185.3316 | 0.0056 | 0.0103 |
| 2024_09_19 22:00 | 3246263 | 4 | 92.2918 | 89.7235 | -116.6172 | 16.5427 | 192.0716 | 0.0049 | 0.0080 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412375_363EBDB9 | 504990 | 440 | -88.1 | 504990 | 843 | -94.1 | 504990 | 373 | -100.5 | 504990 | 363 |
| MR_1774412375_15D82C0C | 504990 | 440 | -87.6 | 504990 | 843 | -94.0 | 504990 | 373 | -100.9 | 504990 | 363 |
| MR_1774412375_7897860F | 504990 | 440 | -88.2 | 504990 | 843 | -92.9 | 504990 | 373 | -99.7 | 504990 | 363 |
| MR_1774412375_1170CC75 | 504990 | 440 | -89.3 | 504990 | 843 | -94.0 | 504990 | 373 | -101.7 | 504990 | 363 |
| MR_1774412375_EE9AF8B0 | 504990 | 440 | -86.4 | 504990 | 843 | -93.3 | 504990 | 373 | -101.6 | 504990 | 363 |
| MR_1774412375_2E1E86DF | 504990 | 440 | -85.8 | 504990 | 843 | -96.7 | 504990 | 373 | -100.2 | 504990 | 363 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 176: `8d981055-ccd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8d981055-ccdd-43a3-b89c-24b902fcd24b` |
| Tag | **multiple-answer** |
| 정답 | **C3|C4|C16|C18** |
| C3 의미 | Decrease transmission power for 3232793_2 |
| C4 의미 | Press down the tilt angle  of 3232793_2 by 5 degrees |
| C16 의미 | Increase A3 Offset threshold for 3232793_2 |
| C18 의미 | Increase A3 Offset threshold for 3278261_5 |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[176] topology](images/train_0176.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3278261_5 by 36 degrees
- `C2`: Adjust the azimuth of 3232793_2 by 9 degrees
- `C3`: Decrease transmission power for 3232793_2 **← 정답**
- `C4`: Press down the tilt angle  of 3232793_2 by 5 degrees **← 정답**
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232793_2
- `C6`: Lift the tilt angle of 3278261_5 by 3 degrees
- `C7`: Decrease A3 Offset threshold for 3232793_2
- `C8`: Press down the tilt angle of 3278261_5 by 3 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232793_2
- `C10`: Increase transmission power for 3278261_5
- `C11`: Decrease A3 Offset threshold for 3278261_5
- `C12`: Add neighbor relationship between 3278261_5 and 3232793_2
- `C13`: Add neighbor relationship between 3248572_4 and 3232793_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278261_5
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Increase A3 Offset threshold for 3232793_2 **← 정답**
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278261_5
- `C18`: Increase A3 Offset threshold for 3278261_5 **← 정답**
- `C19`: Check test server and transmission issues
- `C20`: Decrease transmission power for 3278261_5
- `C21`: Increase transmission power for 3232793_2
- `C22`: Lift the tilt angle  of 3232793_2 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.179 | MS1 | 121.4656673644 | 31.1446192341 | 637 | 504990 | -83.62 | 17.14 | 304.48 | 0.00 | 2.19 | 1583 |
| 2024-09-20 22:21:32.459 | MS1 | 121.4656651066 | 31.1446258088 | 637 | 504990 | -77.35 | 16.63 | 474.07 | 0.05 | 2.49 | 1572 |
| 2024-09-20 22:21:33.315 | MS1 | 121.4656715138 | 31.1446190878 | 637 | 504990 | -76.44 | 13.74 | 320.23 | 0.18 | 2.57 | 1565 |
| 2024-09-20 22:21:34.348 | MS1 | 121.4656644993 | 31.1446256453 | 163 | 504990 | -86.65 | 2.04 | 80.61 | 0.14 | 1.30 | 1578 |
| 2024-09-20 22:21:35.215 | MS1 | 121.4656660598 | 31.1446180503 | 163 | 504990 | -84.90 | 2.19 | 51.14 | 0.04 | 1.42 | 1578 |
| 2024-09-20 22:21:36.633 | MS1 | 121.4656725062 | 31.1446248347 | 637 | 504990 | -87.44 | 3.08 | 41.92 | 0.14 | 1.22 | 1568 |
| 2024-09-20 22:21:37.166 | MS1 | 121.4656655686 | 31.1446304176 | 637 | 504990 | -89.62 | 4.51 | 46.79 | 0.14 | 1.09 | 1597 |
| 2024-09-20 22:21:38.575 | MS1 | 121.4656705914 | 31.1446347088 | 163 | 504990 | -84.82 | 2.13 | 80.17 | 0.05 | 1.40 | 1569 |
| 2024-09-20 22:21:39.586 | MS1 | 121.4656735900 | 31.1446334484 | 163 | 504990 | -85.15 | 1.24 | 61.88 | 0.09 | 1.12 | 1578 |
| 2024-09-20 22:21:40.496 | MS1 | 121.4656587123 | 31.1446246223 | 163 | 504990 | -82.41 | 17.19 | 554.69 | 0.04 | 2.50 | 1569 |
| 2024-09-20 22:21:41.583 | MS1 | 121.4656722754 | 31.1446292918 | 163 | 504990 | -84.77 | 14.12 | 470.04 | 0.05 | 2.67 | 1582 |
| 2024-09-20 22:21:42.810 | MS1 | 121.4656737937 | 31.1446185618 | 163 | 504990 | -79.14 | 13.46 | 512.19 | 0.02 | 2.24 | 1581 |

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
| 3232793 | 2 | 121.4746681274 | 31.1543460687 | 227 | 4 | 7 | 31.3 | TDD | 327 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3248572 | 4 | 121.4666205722 | 31.1533146124 | 285 | 13 | 3 | 43.9 | TDD | 216 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3257787 | 3 | 121.4749323403 | 31.1505783701 | 312 | 3 | 0 | 42.3 | TDD | 691 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3266268 | 1 | 121.4697078843 | 31.1458410470 | 293 | 12 | 11 | 44.9 | TDD | 163 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3278261 | 5 | 121.4735591712 | 31.1484561359 | 276 | 1 | 7 | 27.9 | TDD | 637 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.217 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.240 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.370 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.370 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.035 | NREventA3 | measId:2;ServCellPCI:844;Se... |
| 2024-09-20 22:21:34.275 | NRHandoverAttempt | SourcePCI:844;SourceNR-ARFC... |
| 2024-09-20 22:21:34.307 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.321 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:34.443 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.443 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.035 | NREventA3 | measId:2;ServCellPCI:371;Se... |
| 2024-09-20 22:21:36.275 | NRHandoverAttempt | SourcePCI:371;SourceNR-ARFC... |
| 2024-09-20 22:21:36.314 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.328 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.478 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.478 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.035 | NREventA3 | measId:2;ServCellPCI:844;Se... |
| 2024-09-20 22:21:38.275 | NRHandoverAttempt | SourcePCI:844;SourceNR-ARFC... |
| 2024-09-20 22:21:38.310 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.323 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.452 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.452 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266268 | 1 | 16.1961 | 19.8251 | -115.9139 | 14.9265 | 186.5636 | 0.0032 | 0.0115 |
| 2024_09_20 22:00 | 3232793 | 2 | 7.3821 | 13.4116 | -115.3794 | 8.5945 | 162.4643 | 0.0117 | 0.0106 |
| 2024_09_20 22:00 | 3257787 | 3 | 11.9650 | 7.9392 | -117.3225 | 9.9650 | 137.8200 | 0.0045 | 0.0059 |
| 2024_09_20 22:00 | 3248572 | 4 | 13.7940 | 13.9627 | -115.6318 | 9.3884 | 149.9584 | 0.0028 | 0.0107 |
| 2024_09_20 22:00 | 3278261 | 5 | 19.0470 | 14.3305 | -117.6376 | 7.6186 | 178.9866 | 0.0032 | 0.0170 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415111_4EF2D097 | 504990 | 163 | -86.4 | 504990 | 637 | -85.7 | 504990 | 327 | -86.1 | 504990 | 216 |
| MR_1774415111_9072110A | 504990 | 163 | -85.5 | 504990 | 637 | -85.2 | 504990 | 327 | -87.8 | 504990 | 216 |
| MR_1774415111_CB966856 | 504990 | 163 | -85.7 | 504990 | 637 | -87.7 | 504990 | 327 | -89.2 | 504990 | 216 |
| MR_1774415111_30CD5AD5 | 504990 | 163 | -87.0 | 504990 | 637 | -87.9 | 504990 | 327 | -87.9 | 504990 | 216 |
| MR_1774415111_D24C4EEC | 504990 | 637 | -86.5 | 504990 | 163 | -85.2 | 504990 | 327 | -89.4 | 504990 | 216 |
| MR_1774415111_695DB4EE | 504990 | 163 | -87.1 | 504990 | 637 | -84.5 | 504990 | 327 | -87.4 | 504990 | 216 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 177: `51f3afc2-1ad...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `51f3afc2-1ad3-404a-806f-5736e8e6c548` |
| Tag | **multiple-answer** |
| 정답 | **C1|C13** |
| C1 의미 | Press down the tilt angle  of 3226858_3 by 6 degrees |
| C13 의미 | Decrease transmission power for 3226858_3 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[177] topology](images/train_0177.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3226858_3 by 6 degrees **← 정답**
- `C2`: Check test server and transmission issues
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase transmission power for 3218487_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218487_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226858_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226858_3
- `C8`: Lift the tilt angle  of 3226858_3 by 6 degrees
- `C9`: Decrease A3 Offset threshold for 3218487_4
- `C10`: Add neighbor relationship between 3218487_4 and 3226858_3
- `C11`: Add neighbor relationship between 3273914_2 and 3226858_3
- `C12`: Press down the tilt angle of 3218487_4 by 4 degrees
- `C13`: Decrease transmission power for 3226858_3 **← 정답**
- `C14`: Decrease transmission power for 3218487_4
- `C15`: Lift the tilt angle of 3218487_4 by 4 degrees
- `C16`: Increase transmission power for 3226858_3
- `C17`: Increase A3 Offset threshold for 3218487_4
- `C18`: Adjust the azimuth of 3226858_3 by 5 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218487_4
- `C20`: Decrease A3 Offset threshold for 3226858_3
- `C21`: Adjust the azimuth of 3218487_4 by 41 degrees
- `C22`: Increase A3 Offset threshold for 3226858_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.520 | MS1 | 121.4656697450 | 31.1446338910 | 347 | 504990 | -83.93 | 12.30 | 546.23 | 0.19 | 2.10 | 1585 |
| 2024-09-20 22:21:32.530 | MS1 | 121.4656651197 | 31.1446238844 | 347 | 504990 | -83.46 | 15.24 | 473.77 | 0.02 | 2.93 | 1564 |
| 2024-09-20 22:21:33.673 | MS1 | 121.4656695528 | 31.1446263687 | 347 | 504990 | -77.12 | 16.33 | 417.93 | 0.16 | 2.20 | 1578 |
| 2024-09-20 22:21:34.784 | MS1 | 121.4656684041 | 31.1446233014 | 347 | 504990 | -91.13 | 1.52 | 48.86 | 0.05 | 1.22 | 1562 |
| 2024-09-20 22:21:35.947 | MS1 | 121.4656671084 | 31.1446312527 | 347 | 504990 | -92.55 | 2.21 | 68.66 | 0.17 | 1.08 | 1571 |
| 2024-09-20 22:21:36.894 | MS1 | 121.4656662418 | 31.1446378070 | 347 | 504990 | -91.76 | 3.09 | 81.20 | 0.18 | 1.08 | 1569 |
| 2024-09-20 22:21:37.464 | MS1 | 121.4656679570 | 31.1446320878 | 347 | 504990 | -89.92 | 0.12 | 64.33 | 0.16 | 1.42 | 1599 |
| 2024-09-20 22:21:38.822 | MS1 | 121.4656778424 | 31.1446338840 | 347 | 504990 | -91.89 | 2.56 | 43.85 | 0.06 | 1.36 | 1564 |
| 2024-09-20 22:21:39.798 | MS1 | 121.4656655593 | 31.1446352602 | 347 | 504990 | -93.42 | 3.60 | 76.17 | 0.15 | 1.50 | 1566 |
| 2024-09-20 22:21:40.337 | MS1 | 121.4656623598 | 31.1446342620 | 347 | 504990 | -78.66 | 13.23 | 306.10 | 0.06 | 2.79 | 1567 |
| 2024-09-20 22:21:41.333 | MS1 | 121.4656701661 | 31.1446347143 | 347 | 504990 | -78.03 | 13.59 | 460.02 | 0.06 | 2.66 | 1561 |
| 2024-09-20 22:21:42.841 | MS1 | 121.4656704806 | 31.1446292397 | 347 | 504990 | -78.19 | 16.63 | 551.94 | 0.05 | 2.35 | 1592 |

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
| 3218487 | 4 | 121.4647750738 | 31.1542080523 | 216 | 2 | 1 | 30.2 | TDD | 347 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3226858 | 3 | 121.4739645069 | 31.1479986327 | 250 | 3 | 4 | 41.2 | TDD | 394 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3272136 | 1 | 121.4722407236 | 31.1505326287 | 17 | 3 | 9 | 41.7 | TDD | 96 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3273914 | 2 | 121.4720125941 | 31.1474170850 | 102 | 12 | 6 | 23.7 | TDD | 433 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.162 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.179 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.285 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.285 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272136 | 1 | 8.9346 | 10.7328 | -115.4239 | 17.4603 | 178.6287 | 0.0072 | 0.0147 |
| 2024_09_20 22:00 | 3273914 | 2 | 11.5209 | 18.1806 | -116.9727 | 14.7182 | 174.3852 | 0.0140 | 0.0163 |
| 2024_09_20 22:00 | 3226858 | 3 | 13.3309 | 6.3468 | -114.0457 | 7.0020 | 109.4162 | 0.0073 | 0.0015 |
| 2024_09_20 22:00 | 3218487 | 4 | 9.6381 | 17.8879 | -108.0730 | 9.8665 | 151.7163 | 0.0005 | 0.0136 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412377_FF20ACBC | 504990 | 394 | -90.7 | 504990 | 347 | -86.6 | 504990 | 433 | -91.2 | 504990 | 96 |
| MR_1774412377_7ACB2DD2 | 504990 | 347 | -91.2 | 504990 | 394 | -87.0 | 504990 | 433 | -88.1 | 504990 | 96 |
| MR_1774412377_77CB67E2 | 504990 | 347 | -93.0 | 504990 | 394 | -86.2 | 504990 | 433 | -89.0 | 504990 | 96 |
| MR_1774412377_3CDF8CE1 | 504990 | 347 | -92.7 | 504990 | 394 | -88.0 | 504990 | 433 | -90.6 | 504990 | 96 |
| MR_1774412377_72F380C3 | 504990 | 347 | -91.7 | 504990 | 394 | -87.3 | 504990 | 433 | -87.8 | 504990 | 96 |
| MR_1774412377_7508C28F | 504990 | 394 | -90.5 | 504990 | 347 | -90.0 | 504990 | 433 | -90.0 | 504990 | 96 |
| MR_1774412377_62535B1A | 504990 | 347 | -90.9 | 504990 | 394 | -88.4 | 504990 | 433 | -88.6 | 504990 | 96 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 178: `70852f60-f06...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `70852f60-f066-4b5c-8ddc-d139fb0286fe` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Add neighbor relationship between 3219882_4 and 3247047_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[178] topology](images/train_0178.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219882_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247047_1
- `C3`: Press down the tilt angle  of 3247047_1 by 4 degrees
- `C4`: Lift the tilt angle  of 3247047_1 by 4 degrees
- `C5`: Check test server and transmission issues
- `C6`: Press down the tilt angle of 3219882_4 by 9 degrees
- `C7`: Decrease transmission power for 3219882_4
- `C8`: Increase transmission power for 3219882_4
- `C9`: Lift the tilt angle of 3219882_4 by 9 degrees
- `C10`: Adjust the azimuth of 3219882_4 by 50 degrees
- `C11`: Decrease A3 Offset threshold for 3219882_4
- `C12`: Add neighbor relationship between 3266685_3 and 3247047_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247047_1
- `C14`: Increase A3 Offset threshold for 3247047_1
- `C15`: Increase transmission power for 3247047_1
- `C16`: Add neighbor relationship between 3219882_4 and 3247047_1 **← 정답**
- `C17`: Decrease A3 Offset threshold for 3247047_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219882_4
- `C19`: Increase A3 Offset threshold for 3219882_4
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease transmission power for 3247047_1
- `C22`: Adjust the azimuth of 3247047_1 by 8 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.616 | MS1 | 121.4656657016 | 31.1446321073 | 805 | 504990 | -77.56 | 14.49 | 508.59 | 0.19 | 2.63 | 1565 |
| 2024-09-20 22:21:32.950 | MS1 | 121.4656592057 | 31.1446180248 | 805 | 504990 | -84.78 | 12.46 | 368.50 | 0.17 | 2.30 | 1568 |
| 2024-09-20 22:21:33.822 | MS1 | 121.4656739664 | 31.1446184230 | 805 | 504990 | -81.54 | 17.65 | 312.06 | 0.15 | 2.93 | 1575 |
| 2024-09-20 22:21:34.233 | MS1 | 121.4656609450 | 31.1446283860 | 805 | 504990 | -94.87 | -1.54 | 58.37 | 0.17 | 1.30 | 1595 |
| 2024-09-20 22:21:35.747 | MS1 | 121.4656684250 | 31.1446367292 | 805 | 504990 | -93.78 | -2.78 | 30.73 | 0.09 | 1.12 | 1572 |
| 2024-09-20 22:21:36.693 | MS1 | 121.4656732661 | 31.1446379154 | 805 | 504990 | -88.04 | -0.18 | 59.95 | 0.04 | 1.30 | 1575 |
| 2024-09-20 22:21:37.281 | MS1 | 121.4656611249 | 31.1446229513 | 805 | 504990 | -89.62 | -0.86 | 46.16 | 0.19 | 1.36 | 1591 |
| 2024-09-20 22:21:38.380 | MS1 | 121.4656717675 | 31.1446272383 | 805 | 504990 | -79.67 | 12.08 | 487.74 | 0.19 | 1.26 | 1596 |
| 2024-09-20 22:21:39.398 | MS1 | 121.4656624802 | 31.1446222619 | 805 | 504990 | -79.96 | 14.96 | 576.99 | 0.04 | 1.21 | 1578 |
| 2024-09-20 22:21:40.826 | MS1 | 121.4656706121 | 31.1446221626 | 805 | 504990 | -80.40 | 14.92 | 417.44 | 0.06 | 2.09 | 1592 |
| 2024-09-20 22:21:41.765 | MS1 | 121.4656745763 | 31.1446311858 | 805 | 504990 | -81.12 | 14.91 | 503.69 | 0.04 | 2.15 | 1600 |
| 2024-09-20 22:21:42.698 | MS1 | 121.4656608999 | 31.1446317899 | 805 | 504990 | -75.22 | 13.65 | 334.28 | 0.07 | 2.39 | 1594 |

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
| 3219882 | 4 | 121.4674536857 | 31.1457047976 | 301 | 1 | 1 | 29.1 | TDD | 805 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3247047 | 1 | 121.4733293794 | 31.1458088946 | 252 | 1 | 5 | 42.6 | TDD | 297 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3266685 | 3 | 121.4705054481 | 31.1511391610 | 40 | 10 | 7 | 33.2 | TDD | 3 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3266910 | 2 | 121.4690819378 | 31.1458276176 | 272 | 9 | 3 | 34.6 | TDD | 42 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.105 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.129 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.253 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.253 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.911 | NREventA3 | measId:2;ServCellPCI:281;Se... |
| 2024-09-20 22:21:35.911 | NREventA3 | measId:2;ServCellPCI:281;Se... |
| 2024-09-20 22:21:36.911 | NREventA3 | measId:2;ServCellPCI:281;Se... |
| 2024-09-20 22:21:39.411 | NRRRCReestablishAttempt | PCI:281 |
| 2024-09-20 22:21:39.428 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.441 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.591 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.591 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247047 | 1 | 12.6513 | 17.7550 | -115.1576 | 9.8574 | 186.7347 | 0.0025 | 0.0180 |
| 2024_09_20 22:00 | 3266910 | 2 | 5.9646 | 9.7195 | -117.9810 | 19.6031 | 189.7527 | 0.0198 | 0.0187 |
| 2024_09_20 22:00 | 3266685 | 3 | 17.9526 | 5.2396 | -114.5605 | 5.8080 | 196.7410 | 0.0111 | 0.0179 |
| 2024_09_20 22:00 | 3219882 | 4 | 18.4276 | 8.6636 | -115.0021 | 13.7456 | 100.2088 | 0.0127 | 0.1831 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413161_D990E109 | 504990 | 297 | -90.8 | 504990 | 805 | -93.0 | 504990 | 3 | -93.6 | 504990 | 42 |
| MR_1774413161_7AB3F02E | 504990 | 805 | -95.7 | 504990 | 297 | -91.8 | 504990 | 3 | -95.3 | 504990 | 42 |
| MR_1774413161_9E3CABBE | 504990 | 805 | -95.9 | 504990 | 297 | -92.4 | 504990 | 3 | -93.7 | 504990 | 42 |
| MR_1774413161_54E86EFE | 504990 | 805 | -93.6 | 504990 | 297 | -91.2 | 504990 | 3 | -91.8 | 504990 | 42 |
| MR_1774413161_BFB8E93F | 504990 | 297 | -91.3 | 504990 | 805 | -96.5 | 504990 | 3 | -93.7 | 504990 | 42 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 179: `0ee54769-7e9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0ee54769-7e94-4a7d-ae22-0433ad06a907` |
| Tag | **multiple-answer** |
| 정답 | **C12|C20** |
| C12 의미 | Decrease transmission power for 3226926_3 |
| C20 의미 | Press down the tilt angle  of 3226926_3 by 3 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[179] topology](images/train_0179.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226926_3
- `C2`: Decrease transmission power for 3265203_2
- `C3`: Add neighbor relationship between 3269569_1 and 3226926_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265203_2
- `C5`: Lift the tilt angle  of 3226926_3 by 3 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226926_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265203_2
- `C8`: Decrease A3 Offset threshold for 3226926_3
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Check test server and transmission issues
- `C11`: Increase A3 Offset threshold for 3265203_2
- `C12`: Decrease transmission power for 3226926_3 **← 정답**
- `C13`: Increase A3 Offset threshold for 3226926_3
- `C14`: Decrease A3 Offset threshold for 3265203_2
- `C15`: Press down the tilt angle of 3265203_2 by 3 degrees
- `C16`: Add neighbor relationship between 3265203_2 and 3226926_3
- `C17`: Increase transmission power for 3226926_3
- `C18`: Adjust the azimuth of 3265203_2 by 31 degrees
- `C19`: Lift the tilt angle of 3265203_2 by 3 degrees
- `C20`: Press down the tilt angle  of 3226926_3 by 3 degrees **← 정답**
- `C21`: Increase transmission power for 3265203_2
- `C22`: Adjust the azimuth of 3226926_3 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.330 | MS1 | 121.4656740203 | 31.1446269498 | 353 | 504990 | -77.63 | 14.82 | 440.83 | 0.18 | 2.25 | 1562 |
| 2024-09-20 22:21:32.734 | MS1 | 121.4656586724 | 31.1446293134 | 353 | 504990 | -81.88 | 12.84 | 423.86 | 0.07 | 2.50 | 1581 |
| 2024-09-20 22:21:33.751 | MS1 | 121.4656671519 | 31.1446278499 | 353 | 504990 | -77.55 | 12.10 | 372.66 | 0.14 | 2.22 | 1600 |
| 2024-09-20 22:21:34.486 | MS1 | 121.4656609365 | 31.1446251461 | 353 | 504990 | -91.12 | 1.33 | 44.53 | 0.19 | 1.33 | 1576 |
| 2024-09-20 22:21:35.529 | MS1 | 121.4656635663 | 31.1446271519 | 353 | 504990 | -90.73 | 2.83 | 69.34 | 0.01 | 1.47 | 1571 |
| 2024-09-20 22:21:36.209 | MS1 | 121.4656717848 | 31.1446190506 | 353 | 504990 | -85.39 | 0.81 | 72.75 | 0.14 | 1.20 | 1576 |
| 2024-09-20 22:21:37.567 | MS1 | 121.4656688597 | 31.1446258523 | 353 | 504990 | -90.31 | 2.56 | 74.33 | 0.06 | 1.29 | 1591 |
| 2024-09-20 22:21:38.219 | MS1 | 121.4656747005 | 31.1446369902 | 353 | 504990 | -93.63 | 2.58 | 88.94 | 0.16 | 1.20 | 1561 |
| 2024-09-20 22:21:39.790 | MS1 | 121.4656757252 | 31.1446210713 | 353 | 504990 | -91.07 | 0.06 | 58.84 | 0.12 | 1.45 | 1575 |
| 2024-09-20 22:21:40.333 | MS1 | 121.4656730837 | 31.1446274473 | 353 | 504990 | -81.19 | 12.37 | 446.17 | 0.10 | 2.56 | 1575 |
| 2024-09-20 22:21:41.137 | MS1 | 121.4656681698 | 31.1446299008 | 353 | 504990 | -78.74 | 13.77 | 389.10 | 0.07 | 2.56 | 1585 |
| 2024-09-20 22:21:42.318 | MS1 | 121.4656583791 | 31.1446360191 | 353 | 504990 | -75.29 | 15.67 | 549.01 | 0.04 | 2.24 | 1588 |

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
| 3219563 | 4 | 121.4664503147 | 31.1496218311 | 86 | 11 | 12 | 40.0 | TDD | 696 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3226926 | 3 | 121.4737792319 | 31.1491244347 | 240 | 0 | 3 | 44.4 | TDD | 827 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3265203 | 2 | 121.4759426313 | 31.1481379366 | 279 | 1 | 6 | 43.8 | TDD | 353 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3269569 | 1 | 121.4658356909 | 31.1466375616 | 191 | 8 | 10 | 25.3 | TDD | 896 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.172 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.303 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.303 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269569 | 1 | 12.5949 | 19.8352 | -117.9727 | 10.0637 | 134.7123 | 0.0031 | 0.0164 |
| 2024_09_20 22:00 | 3265203 | 2 | 8.6411 | 18.7504 | -109.0041 | 19.1467 | 177.7278 | 0.0069 | 0.0042 |
| 2024_09_20 22:00 | 3226926 | 3 | 9.1433 | 17.6376 | -117.3639 | 18.3259 | 174.1981 | 0.0043 | 0.0126 |
| 2024_09_20 22:00 | 3219563 | 4 | 12.9194 | 11.2107 | -117.8486 | 8.3444 | 103.6672 | 0.0173 | 0.0011 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412932_3358E77D | 504990 | 353 | -91.7 | 504990 | 827 | -88.2 | 504990 | 896 | -91.0 | 504990 | 696 |
| MR_1774412932_3C4912E1 | 504990 | 353 | -93.0 | 504990 | 827 | -89.3 | 504990 | 896 | -90.0 | 504990 | 696 |
| MR_1774412932_4ECB766D | 504990 | 353 | -93.1 | 504990 | 827 | -89.8 | 504990 | 896 | -92.9 | 504990 | 696 |
| MR_1774412932_D94D8996 | 504990 | 353 | -89.9 | 504990 | 827 | -87.8 | 504990 | 896 | -90.6 | 504990 | 696 |
| MR_1774412932_B4203B71 | 504990 | 353 | -92.8 | 504990 | 827 | -87.8 | 504990 | 896 | -89.4 | 504990 | 696 |
| MR_1774412932_0AEC9FD2 | 504990 | 353 | -90.5 | 504990 | 827 | -89.5 | 504990 | 896 | -89.6 | 504990 | 696 |
| MR_1774412932_31B0D9B3 | 504990 | 353 | -92.5 | 504990 | 827 | -91.4 | 504990 | 896 | -89.3 | 504990 | 696 |
| MR_1774412932_A7E0BE0D | 504990 | 827 | -92.1 | 504990 | 353 | -89.5 | 504990 | 896 | -89.6 | 504990 | 696 |

> *... 2개 열 생략 (전체 14열)*

---
