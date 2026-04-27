# Track A 문제 분석 — train[1420]~train[1429]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1420] ~ train[1429] (10개)

## 목차

1. [문제 1420: `ed1ee4e0-390...`](#1420) — multiple-answer, 정답: C4|C14
2. [문제 1421: `ed7c8519-baa...`](#1421) — single-answer, 정답: C15
3. [문제 1422: `26df7f6a-56a...`](#1422) — single-answer, 정답: C18
4. [문제 1423: `bfc3cb0e-532...`](#1423) — single-answer, 정답: C7
5. [문제 1424: `14af84ef-669...`](#1424) — single-answer, 정답: C18
6. [문제 1425: `85273fbf-31f...`](#1425) — single-answer, 정답: C7
7. [문제 1426: `aac9ff74-a9f...`](#1426) — multiple-answer, 정답: C5|C21
8. [문제 1427: `6c06d6b5-3d4...`](#1427) — multiple-answer, 정답: C10|C15
9. [문제 1428: `7c5c904d-5d1...`](#1428) — single-answer, 정답: C14
10. [문제 1429: `afec168e-e21...`](#1429) — single-answer, 정답: C4

---

### 문제 1420: `ed1ee4e0-390...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ed1ee4e0-390e-437e-a609-b13729af3e88` |
| Tag | **multiple-answer** |
| 정답 | **C4|C14** |
| C4 의미 | Decrease transmission power for 3254650_1 |
| C14 의미 | Press down the tilt angle  of 3254650_1 by 4 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1420] topology](images/train_1420.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3254650_1
- `C2`: Adjust the azimuth of 3254650_1 by 7 degrees
- `C3`: Check test server and transmission issues
- `C4`: Decrease transmission power for 3254650_1 **← 정답**
- `C5`: Adjust the azimuth of 3214588_2 by 9 degrees
- `C6`: Press down the tilt angle of 3214588_2 by 3 degrees
- `C7`: Decrease A3 Offset threshold for 3254650_1
- `C8`: Increase transmission power for 3214588_2
- `C9`: Increase A3 Offset threshold for 3254650_1
- `C10`: Lift the tilt angle of 3214588_2 by 3 degrees
- `C11`: Decrease transmission power for 3214588_2
- `C12`: Add neighbor relationship between 3214588_2 and 3254650_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214588_2
- `C14`: Press down the tilt angle  of 3254650_1 by 4 degrees **← 정답**
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254650_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254650_1
- `C17`: Decrease A3 Offset threshold for 3214588_2
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Lift the tilt angle  of 3254650_1 by 4 degrees
- `C20`: Increase A3 Offset threshold for 3214588_2
- `C21`: Add neighbor relationship between 3247147_4 and 3254650_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214588_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.282 | MS1 | 121.4656695556 | 31.1446197091 | 788 | 504990 | -75.99 | 14.23 | 526.90 | 0.17 | 2.78 | 1583 |
| 2024-09-20 22:21:32.398 | MS1 | 121.4656583360 | 31.1446298210 | 788 | 504990 | -77.57 | 12.46 | 547.42 | 0.16 | 2.47 | 1567 |
| 2024-09-20 22:21:33.506 | MS1 | 121.4656715713 | 31.1446189843 | 788 | 504990 | -76.41 | 13.41 | 311.52 | 0.16 | 2.81 | 1582 |
| 2024-09-20 22:21:34.541 | MS1 | 121.4656615577 | 31.1446201334 | 788 | 504990 | -91.95 | 2.32 | 62.26 | 0.09 | 1.13 | 1580 |
| 2024-09-20 22:21:35.736 | MS1 | 121.4656777927 | 31.1446301462 | 788 | 504990 | -85.28 | 3.35 | 48.12 | 0.10 | 1.35 | 1570 |
| 2024-09-20 22:21:36.474 | MS1 | 121.4656582801 | 31.1446299518 | 788 | 504990 | -85.98 | 3.80 | 95.16 | 0.06 | 1.12 | 1571 |
| 2024-09-20 22:21:37.107 | MS1 | 121.4656651825 | 31.1446290904 | 788 | 504990 | -93.03 | 3.64 | 49.70 | 0.05 | 1.37 | 1564 |
| 2024-09-20 22:21:38.249 | MS1 | 121.4656621988 | 31.1446264810 | 788 | 504990 | -88.47 | 0.53 | 77.44 | 0.10 | 1.11 | 1583 |
| 2024-09-20 22:21:39.444 | MS1 | 121.4656623427 | 31.1446202967 | 788 | 504990 | -93.07 | 3.97 | 92.49 | 0.19 | 1.01 | 1568 |
| 2024-09-20 22:21:40.200 | MS1 | 121.4656734624 | 31.1446288798 | 788 | 504990 | -83.14 | 14.57 | 309.30 | 0.18 | 2.69 | 1560 |
| 2024-09-20 22:21:41.434 | MS1 | 121.4656662029 | 31.1446369782 | 788 | 504990 | -82.10 | 14.50 | 453.75 | 0.20 | 2.13 | 1573 |
| 2024-09-20 22:21:42.821 | MS1 | 121.4656684130 | 31.1446312809 | 788 | 504990 | -82.05 | 13.66 | 574.19 | 0.16 | 2.71 | 1562 |

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
| 3214588 | 2 | 121.4679795769 | 31.1531080363 | 184 | 2 | 6 | 19.6 | TDD | 788 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3227154 | 3 | 121.4677467812 | 31.1455322565 | 234 | 7 | 1 | 42.0 | TDD | 341 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3247147 | 4 | 121.4751434624 | 31.1509772036 | 65 | 10 | 7 | 18.1 | TDD | 997 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3254650 | 1 | 121.4734770659 | 31.1479636649 | 236 | 1 | 4 | 40.5 | TDD | 113 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.600 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.620 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.758 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.758 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254650 | 1 | 7.2780 | 6.3982 | -115.0052 | 13.6892 | 170.1834 | 0.0175 | 0.0031 |
| 2024_09_20 22:00 | 3214588 | 2 | 11.2682 | 11.2267 | -109.7458 | 16.0251 | 198.9656 | 0.0104 | 0.0005 |
| 2024_09_20 22:00 | 3227154 | 3 | 8.9744 | 11.3379 | -117.8409 | 12.1680 | 199.9075 | 0.0073 | 0.0198 |
| 2024_09_20 22:00 | 3247147 | 4 | 6.2886 | 19.5487 | -115.9646 | 16.7937 | 169.3435 | 0.0023 | 0.0067 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414524_50CFA2EB | 504990 | 788 | -90.1 | 504990 | 113 | -90.4 | 504990 | 997 | -91.0 | 504990 | 341 |
| MR_1774414524_4A5789C6 | 504990 | 788 | -92.0 | 504990 | 113 | -92.5 | 504990 | 997 | -91.9 | 504990 | 341 |
| MR_1774414524_73B1F03A | 504990 | 788 | -90.4 | 504990 | 113 | -88.6 | 504990 | 997 | -91.9 | 504990 | 341 |
| MR_1774414524_D9097AEB | 504990 | 113 | -90.5 | 504990 | 788 | -92.1 | 504990 | 997 | -90.8 | 504990 | 341 |
| MR_1774414524_4F735970 | 504990 | 113 | -91.6 | 504990 | 788 | -92.6 | 504990 | 997 | -93.7 | 504990 | 341 |
| MR_1774414524_8B4913AA | 504990 | 113 | -91.9 | 504990 | 788 | -91.8 | 504990 | 997 | -92.1 | 504990 | 341 |
| MR_1774414524_64676A35 | 504990 | 113 | -92.3 | 504990 | 788 | -91.1 | 504990 | 997 | -91.8 | 504990 | 341 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1421: `ed7c8519-baa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ed7c8519-baa1-4fde-96a3-e2abebac2716` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease A3 Offset threshold for 3243683_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1421] topology](images/train_1421.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3243683_3 by 50 degrees
- `C2`: Add neighbor relationship between 3243683_3 and 3250347_2
- `C3`: Decrease A3 Offset threshold for 3250347_2
- `C4`: Increase A3 Offset threshold for 3250347_2
- `C5`: Check test server and transmission issues
- `C6`: Increase transmission power for 3250347_2
- `C7`: Increase transmission power for 3243683_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243683_3
- `C9`: Adjust the azimuth of 3250347_2 by 50 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease transmission power for 3250347_2
- `C12`: Press down the tilt angle of 3243683_3 by 10 degrees
- `C13`: Increase A3 Offset threshold for 3243683_3
- `C14`: Press down the tilt angle  of 3250347_2 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3243683_3 **← 정답**
- `C16`: Decrease transmission power for 3243683_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243683_3
- `C18`: Add neighbor relationship between 3250139_1 and 3250347_2
- `C19`: Lift the tilt angle  of 3250347_2 by 10 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250347_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250347_2
- `C22`: Lift the tilt angle of 3243683_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.674 | MS1 | 121.4656673968 | 31.1446369616 | 238 | 504990 | -84.09 | 16.37 | 581.28 | 0.02 | 2.57 | 1593 |
| 2024-09-20 22:21:32.437 | MS1 | 121.4656753857 | 31.1446264899 | 238 | 504990 | -77.62 | 12.66 | 528.10 | 0.01 | 2.27 | 1590 |
| 2024-09-20 22:21:33.802 | MS1 | 121.4656614902 | 31.1446186161 | 238 | 504990 | -81.25 | 16.02 | 343.91 | 0.03 | 2.72 | 1566 |
| 2024-09-20 22:21:34.430 | MS1 | 121.4656705627 | 31.1446339760 | 238 | 504990 | -84.83 | -0.09 | 67.15 | 0.03 | 1.24 | 1566 |
| 2024-09-20 22:21:35.814 | MS1 | 121.4656692527 | 31.1446374782 | 238 | 504990 | -84.58 | -2.91 | 36.64 | 0.07 | 1.09 | 1580 |
| 2024-09-20 22:21:36.924 | MS1 | 121.4656705038 | 31.1446262386 | 238 | 504990 | -86.53 | -2.17 | 79.01 | 0.13 | 1.20 | 1594 |
| 2024-09-20 22:21:37.316 | MS1 | 121.4656772072 | 31.1446216639 | 238 | 504990 | -87.34 | -1.78 | 65.25 | 0.20 | 1.42 | 1589 |
| 2024-09-20 22:21:38.844 | MS1 | 121.4656589959 | 31.1446314847 | 238 | 504990 | -89.40 | -0.55 | 44.84 | 0.12 | 1.40 | 1570 |
| 2024-09-20 22:21:39.820 | MS1 | 121.4656707504 | 31.1446340478 | 989 | 504990 | -81.22 | 14.46 | 223.04 | 0.02 | 1.37 | 1570 |
| 2024-09-20 22:21:40.673 | MS1 | 121.4656687325 | 31.1446294224 | 989 | 504990 | -80.41 | 14.56 | 590.34 | 0.01 | 2.10 | 1574 |
| 2024-09-20 22:21:41.101 | MS1 | 121.4656730726 | 31.1446357785 | 989 | 504990 | -80.69 | 15.77 | 601.97 | 0.07 | 2.83 | 1592 |
| 2024-09-20 22:21:42.104 | MS1 | 121.4656665867 | 31.1446243901 | 989 | 504990 | -80.04 | 15.24 | 518.29 | 0.02 | 2.65 | 1587 |

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
| 3243683 | 3 | 121.4683506382 | 31.1481500133 | 98 | 7 | 0 | 33.3 | TDD | 238 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3250139 | 1 | 121.4675448509 | 31.1511594032 | 115 | 5 | 5 | 34.2 | TDD | 640 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3250347 | 2 | 121.4752717133 | 31.1513197113 | 286 | 15 | 0 | 24.6 | TDD | 989 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3264144 | 4 | 121.4717282684 | 31.1501555541 | 326 | 9 | 0 | 19.6 | TDD | 397 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.337 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.360 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.490 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.490 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.197 | NREventA3 | measId:2;ServCellPCI:849;Se... |
| 2024-09-20 22:21:38.437 | NRHandoverAttempt | SourcePCI:849;SourceNR-ARFC... |
| 2024-09-20 22:21:38.484 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.494 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.605 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.605 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250139 | 1 | 12.6685 | 13.9927 | -114.9065 | 8.0709 | 154.7665 | 0.0178 | 0.0147 |
| 2024_09_20 22:00 | 3250347 | 2 | 7.9807 | 13.5855 | -116.6152 | 11.8509 | 167.6366 | 0.0148 | 0.0010 |
| 2024_09_20 22:00 | 3243683 | 3 | 16.9308 | 19.6082 | -114.8561 | 11.7260 | 192.5612 | 0.0199 | 0.1261 |
| 2024_09_20 22:00 | 3264144 | 4 | 9.3353 | 12.2167 | -117.2104 | 7.8948 | 183.0879 | 0.0040 | 0.0104 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412952_F0E83F47 | 504990 | 989 | -79.8 | 504990 | 238 | -84.1 | 504990 | 640 | -81.4 | 504990 | 397 |
| MR_1774412952_9257D0BB | 504990 | 238 | -85.7 | 504990 | 989 | -78.1 | 504990 | 640 | -80.6 | 504990 | 397 |
| MR_1774412952_28CA7999 | 504990 | 238 | -84.6 | 504990 | 989 | -79.1 | 504990 | 640 | -83.2 | 504990 | 397 |
| MR_1774412952_03E17F28 | 504990 | 238 | -83.2 | 504990 | 989 | -78.7 | 504990 | 640 | -81.5 | 504990 | 397 |
| MR_1774412952_FB50B183 | 504990 | 238 | -84.8 | 504990 | 989 | -77.3 | 504990 | 640 | -83.7 | 504990 | 397 |
| MR_1774412952_E2EEEB7C | 504990 | 989 | -79.2 | 504990 | 238 | -86.5 | 504990 | 640 | -81.6 | 504990 | 397 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1422: `26df7f6a-56a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `26df7f6a-56ac-4ac1-b3d0-2a83d7eda88d` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1422] topology](images/train_1422.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3242580_1
- `C2`: Press down the tilt angle of 3224167_2 by 8 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242580_1
- `C4`: Decrease A3 Offset threshold for 3224167_2
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease transmission power for 3224167_2
- `C7`: Adjust the azimuth of 3224167_2 by 13 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224167_2
- `C9`: Increase transmission power for 3224167_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242580_1
- `C11`: Increase A3 Offset threshold for 3224167_2
- `C12`: Adjust the azimuth of 3242580_1 by 50 degrees
- `C13`: Add neighbor relationship between 3224167_2 and 3242580_1
- `C14`: Decrease A3 Offset threshold for 3242580_1
- `C15`: Add neighbor relationship between 3267527_4 and 3242580_1
- `C16`: Increase A3 Offset threshold for 3242580_1
- `C17`: Decrease transmission power for 3242580_1
- `C18`: Check test server and transmission issues **← 정답**
- `C19`: Press down the tilt angle  of 3242580_1 by 10 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224167_2
- `C21`: Lift the tilt angle of 3224167_2 by 8 degrees
- `C22`: Lift the tilt angle  of 3242580_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.768 | MS1 | 121.4656646860 | 31.1446199736 | 546 | 504990 | -86.73 | 16.76 | 509.64 | 0.08 | 2.59 | 1598 |
| 2024-09-20 22:21:32.458 | MS1 | 121.4656757745 | 31.1446307467 | 546 | 504990 | -87.75 | 13.02 | 423.98 | 0.18 | 2.40 | 1578 |
| 2024-09-20 22:21:33.145 | MS1 | 121.4656648280 | 31.1446272705 | 546 | 504990 | -90.67 | 17.41 | 497.51 | 0.18 | 2.09 | 1598 |
| 2024-09-20 22:21:34.316 | MS1 | 121.4656632591 | 31.1446182194 | 546 | 504990 | -90.38 | 16.41 | 74.68 | 0.13 | 2.73 | 428 |
| 2024-09-20 22:21:35.186 | MS1 | 121.4656770544 | 31.1446237268 | 546 | 504990 | -85.36 | 14.48 | 78.29 | 0.15 | 2.83 | 404 |
| 2024-09-20 22:21:36.876 | MS1 | 121.4656682852 | 31.1446194322 | 546 | 504990 | -91.29 | 16.49 | 43.41 | 0.03 | 2.65 | 441 |
| 2024-09-20 22:21:37.473 | MS1 | 121.4656730888 | 31.1446362651 | 546 | 504990 | -93.37 | 9.23 | 58.65 | 0.13 | 2.65 | 358 |
| 2024-09-20 22:21:38.213 | MS1 | 121.4656594472 | 31.1446295078 | 546 | 504990 | -89.26 | 7.51 | 85.75 | 0.16 | 2.71 | 421 |
| 2024-09-20 22:21:39.170 | MS1 | 121.4656654329 | 31.1446313259 | 546 | 504990 | -90.14 | 10.10 | 71.66 | 0.07 | 2.51 | 347 |
| 2024-09-20 22:21:40.531 | MS1 | 121.4656726864 | 31.1446233598 | 546 | 504990 | -91.92 | 11.06 | 531.63 | 0.18 | 2.25 | 1574 |
| 2024-09-20 22:21:41.774 | MS1 | 121.4656622258 | 31.1446353976 | 546 | 504990 | -90.02 | 12.35 | 320.70 | 0.04 | 2.37 | 1591 |
| 2024-09-20 22:21:42.487 | MS1 | 121.4656765645 | 31.1446211715 | 546 | 504990 | -89.30 | 11.65 | 576.39 | 0.12 | 2.89 | 1573 |

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
| 3224167 | 2 | 121.4649946247 | 31.1470113550 | 179 | 2 | 6 | 28.3 | TDD | 546 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3242580 | 1 | 121.4642140883 | 31.1541286475 | 312 | 12 | 12 | 30.1 | TDD | 480 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3248999 | 3 | 121.4646981297 | 31.1483143371 | 151 | 7 | 5 | 45.0 | TDD | 77 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3267527 | 4 | 121.4668187017 | 31.1464922261 | 159 | 11 | 2 | 28.6 | TDD | 830 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.475 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.500 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.629 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.629 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.367 | NREventA3 | measId:2;ServCellPCI:18;Ser... |
| 2024-09-20 22:21:38.607 | NRHandoverAttempt | SourcePCI:18;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.638 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.652 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.764 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.764 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242580 | 1 | 7.9074 | 9.3531 | -114.6805 | 12.9061 | 198.4179 | 0.0008 | 0.0176 |
| 2024_09_20 22:00 | 3224167 | 2 | 8.2298 | 7.4649 | -115.1728 | 5.4437 | 128.0876 | 0.0150 | 0.0056 |
| 2024_09_20 22:00 | 3248999 | 3 | 5.7831 | 14.4546 | -116.9765 | 12.6700 | 192.0501 | 0.0010 | 0.0096 |
| 2024_09_20 22:00 | 3267527 | 4 | 11.5696 | 18.5974 | -117.6279 | 7.7908 | 170.5474 | 0.0048 | 0.0003 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417184_D23B28D8 | 504990 | 546 | -92.4 | 504990 | 480 | -90.9 | 504990 | 830 | -103.0 | 504990 | 77 |
| MR_1774417184_86848CB2 | 504990 | 546 | -90.0 | 504990 | 480 | -88.8 | 504990 | 830 | -100.3 | 504990 | 77 |
| MR_1774417184_C5F08818 | 504990 | 546 | -90.1 | 504990 | 480 | -90.1 | 504990 | 830 | -102.8 | 504990 | 77 |
| MR_1774417184_7E1347A1 | 504990 | 546 | -89.7 | 504990 | 480 | -88.5 | 504990 | 830 | -100.3 | 504990 | 77 |
| MR_1774417184_18255361 | 504990 | 546 | -91.2 | 504990 | 480 | -90.6 | 504990 | 830 | -100.5 | 504990 | 77 |
| MR_1774417184_4BF5BA04 | 504990 | 546 | -91.7 | 504990 | 480 | -88.2 | 504990 | 830 | -102.5 | 504990 | 77 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1423: `bfc3cb0e-532...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bfc3cb0e-5326-4bb9-9278-bc1e85cf22f6` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Lift the tilt angle  of 3261600_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1423] topology](images/train_1423.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3261600_2 by 50 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221011_1
- `C3`: Add neighbor relationship between 3261600_2 and 3266467_3
- `C4`: Increase transmission power for 3266467_3
- `C5`: Decrease A3 Offset threshold for 3221011_1
- `C6`: Lift the tilt angle of 3221011_1 by 1 degrees
- `C7`: Lift the tilt angle  of 3261600_2 by 10 degrees **← 정답**
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease A3 Offset threshold for 3266467_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266467_3
- `C11`: Add neighbor relationship between 3221011_1 and 3266467_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266467_3
- `C13`: Press down the tilt angle of 3221011_1 by 1 degrees
- `C14`: Decrease transmission power for 3221011_1
- `C15`: Adjust the azimuth of 3221011_1 by 5 degrees
- `C16`: Increase A3 Offset threshold for 3266467_3
- `C17`: Increase A3 Offset threshold for 3221011_1
- `C18`: Increase transmission power for 3221011_1
- `C19`: Check test server and transmission issues
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221011_1
- `C21`: Press down the tilt angle  of 3261600_2 by 10 degrees
- `C22`: Decrease transmission power for 3266467_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.240 | MS1 | 121.4656586415 | 31.1446366932 | 649 | 504990 | -89.41 | 14.59 | 380.46 | 0.03 | 2.21 | 1564 |
| 2024-09-20 22:21:32.237 | MS1 | 121.4656640088 | 31.1446203792 | 649 | 504990 | -91.53 | 16.76 | 350.10 | 0.07 | 2.92 | 1579 |
| 2024-09-20 22:21:33.972 | MS1 | 121.4656670576 | 31.1446281136 | 649 | 504990 | -87.57 | 12.89 | 589.90 | 0.01 | 2.79 | 1586 |
| 2024-09-20 22:21:34.774 | MS1 | 121.4656725025 | 31.1446203581 | 649 | 504990 | -85.09 | 12.05 | 70.31 | 0.08 | 2.02 | 1565 |
| 2024-09-20 22:21:35.679 | MS1 | 121.4656676390 | 31.1446195409 | 649 | 504990 | -91.36 | 13.99 | 91.01 | 0.04 | 2.61 | 1564 |
| 2024-09-20 22:21:36.553 | MS1 | 121.4656693636 | 31.1446289368 | 649 | 504990 | -91.49 | 14.86 | 91.94 | 0.19 | 2.74 | 1580 |
| 2024-09-20 22:21:37.419 | MS1 | 121.4656610556 | 31.1446350192 | 649 | 504990 | -89.17 | 7.19 | 74.65 | 0.07 | 2.49 | 1573 |
| 2024-09-20 22:21:38.223 | MS1 | 121.4656605184 | 31.1446277290 | 649 | 504990 | -91.44 | 11.26 | 90.53 | 0.01 | 2.49 | 1569 |
| 2024-09-20 22:21:39.180 | MS1 | 121.4656690956 | 31.1446184050 | 649 | 504990 | -89.52 | 10.70 | 91.96 | 0.05 | 2.90 | 1589 |
| 2024-09-20 22:21:40.163 | MS1 | 121.4656759811 | 31.1446347854 | 649 | 504990 | -93.55 | 10.21 | 370.72 | 0.00 | 2.51 | 1567 |
| 2024-09-20 22:21:41.466 | MS1 | 121.4656619754 | 31.1446253931 | 649 | 504990 | -92.70 | 9.84 | 480.33 | 0.06 | 2.59 | 1569 |
| 2024-09-20 22:21:42.186 | MS1 | 121.4656584127 | 31.1446206750 | 649 | 504990 | -89.84 | 9.00 | 316.54 | 0.16 | 2.30 | 1583 |

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
| 3221011 | 1 | 121.4641863382 | 31.1541345054 | 167 | 0 | 6 | 15.1 | TDD | 649 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3261600 | 2 | 121.4666542725 | 31.1482563420 | 280 | 13 | 12 | 47.2 | TDD | 657 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3266467 | 3 | 121.4659786400 | 31.1507541134 | 298 | 8 | 6 | 40.8 | TDD | 444 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3273360 | 4 | 121.4715140955 | 31.1495084457 | 8 | 9 | 9 | 15.3 | TDD | 676 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.490 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.509 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.623 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.623 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.327 | NREventA3 | measId:2;ServCellPCI:448;Se... |
| 2024-09-20 22:21:38.567 | NRHandoverAttempt | SourcePCI:448;SourceNR-ARFC... |
| 2024-09-20 22:21:38.603 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.617 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.723 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.723 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221011 | 1 | 76.0645 | 81.6027 | -117.4008 | 7.6196 | 132.7661 | 0.0026 | 0.0049 |
| 2024_09_20 22:00 | 3261600 | 2 | 12.5739 | 16.8465 | -117.4468 | 6.8293 | 172.4269 | 0.0180 | 0.0025 |
| 2024_09_20 22:00 | 3266467 | 3 | 9.0417 | 5.4656 | -116.2096 | 19.3447 | 88.8090 | 0.0079 | 0.0113 |
| 2024_09_20 22:00 | 3273360 | 4 | 5.2489 | 10.5046 | -117.1919 | 18.2643 | 159.6463 | 0.0024 | 0.0116 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412938_9B1AAE1B | 504990 | 649 | -84.7 | 504990 | 444 | -82.9 | 504990 | 657 | -90.8 | 504990 | 676 |
| MR_1774412938_E418BAFB | 504990 | 649 | -84.7 | 504990 | 444 | -85.1 | 504990 | 657 | -89.3 | 504990 | 676 |
| MR_1774412938_C5F77691 | 504990 | 649 | -86.5 | 504990 | 444 | -84.0 | 504990 | 657 | -90.6 | 504990 | 676 |
| MR_1774412938_3D3126C0 | 504990 | 649 | -83.4 | 504990 | 444 | -84.6 | 504990 | 657 | -89.8 | 504990 | 676 |
| MR_1774412938_8CB19F56 | 504990 | 649 | -83.3 | 504990 | 444 | -84.2 | 504990 | 657 | -90.2 | 504990 | 676 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1424: `14af84ef-669...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `14af84ef-669c-4de5-a43e-fe0744d4af3a` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1424] topology](images/train_1424.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3218216_2
- `C2`: Adjust the azimuth of 3218489_1 by 50 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218489_1
- `C4`: Lift the tilt angle of 3218216_2 by 9 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218489_1
- `C6`: Increase transmission power for 3218489_1
- `C7`: Decrease A3 Offset threshold for 3218216_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218216_2
- `C9`: Press down the tilt angle of 3218216_2 by 9 degrees
- `C10`: Add neighbor relationship between 3218216_2 and 3218489_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218216_2
- `C12`: Adjust the azimuth of 3218216_2 by 50 degrees
- `C13`: Press down the tilt angle  of 3218489_1 by 9 degrees
- `C14`: Add neighbor relationship between 3218753_4 and 3218489_1
- `C15`: Lift the tilt angle  of 3218489_1 by 9 degrees
- `C16`: Increase A3 Offset threshold for 3218216_2
- `C17`: Increase A3 Offset threshold for 3218489_1
- `C18`: Insufficient data; more data is needed for judgment. **← 정답**
- `C19`: Check test server and transmission issues
- `C20`: Decrease A3 Offset threshold for 3218489_1
- `C21`: Decrease transmission power for 3218216_2
- `C22`: Decrease transmission power for 3218489_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.416 | MS1 | 121.4656717033 | 31.1446328303 | 474 | 504990 | -88.38 | 14.66 | 387.74 | 0.17 | 2.67 | 1590 |
| 2024-09-20 22:21:32.899 | MS1 | 121.4656694913 | 31.1446292006 | 474 | 504990 | -87.94 | 12.11 | 427.44 | 0.02 | 2.48 | 1590 |
| 2024-09-20 22:21:33.276 | MS1 | 121.4656643338 | 31.1446305381 | 474 | 504990 | -86.02 | 17.21 | 305.44 | 0.20 | 2.87 | 1564 |
| 2024-09-20 22:21:34.377 | MS1 | 121.4656593759 | 31.1446299305 | 474 | 504990 | -85.61 | 14.79 | 65.19 | 0.04 | 2.07 | 1563 |
| 2024-09-20 22:21:35.770 | MS1 | 121.4656669895 | 31.1446248677 | 474 | 504990 | -85.05 | 13.86 | 56.72 | 0.08 | 2.70 | 1591 |
| 2024-09-20 22:21:36.933 | MS1 | 121.4656651210 | 31.1446331302 | 474 | 504990 | -87.66 | 17.17 | 98.56 | 0.17 | 2.27 | 1582 |
| 2024-09-20 22:21:37.288 | MS1 | 121.4656758856 | 31.1446219395 | 474 | 504990 | -91.94 | 7.82 | 60.40 | 0.07 | 2.53 | 1572 |
| 2024-09-20 22:21:38.158 | MS1 | 121.4656630974 | 31.1446248953 | 474 | 504990 | -90.34 | 8.48 | 89.99 | 0.10 | 2.04 | 1584 |
| 2024-09-20 22:21:39.433 | MS1 | 121.4656765824 | 31.1446208685 | 474 | 504990 | -91.32 | 10.82 | 48.95 | 0.10 | 2.92 | 1568 |
| 2024-09-20 22:21:40.762 | MS1 | 121.4656764085 | 31.1446377021 | 474 | 504990 | -93.60 | 10.81 | 332.45 | 0.10 | 2.58 | 1560 |
| 2024-09-20 22:21:41.245 | MS1 | 121.4656653016 | 31.1446239627 | 474 | 504990 | -89.23 | 12.55 | 576.25 | 0.19 | 2.36 | 1589 |
| 2024-09-20 22:21:42.980 | MS1 | 121.4656687527 | 31.1446270198 | 474 | 504990 | -92.35 | 8.17 | 530.21 | 0.18 | 2.51 | 1584 |

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
| 3218216 | 2 | 121.4642245523 | 31.1543568777 | 18 | 7 | 5 | 29.9 | TDD | 474 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3218489 | 1 | 121.4640365246 | 31.1478884047 | 262 | 2 | 5 | 46.1 | TDD | 496 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3218753 | 4 | 121.4691352910 | 31.1558036272 | 244 | 11 | 12 | 22.2 | TDD | 366 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3249134 | 3 | 121.4732341967 | 31.1491861616 | 109 | 4 | 3 | 16.6 | TDD | 620 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.754 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.772 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.877 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.877 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.646 | NREventA3 | measId:2;ServCellPCI:475;Se... |
| 2024-09-20 22:21:37.886 | NRHandoverAttempt | SourcePCI:475;SourceNR-ARFC... |
| 2024-09-20 22:21:37.928 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.938 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.042 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.042 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3218489 | 1 | 82.9005 | 76.4243 | -115.0567 | 14.1680 | 192.6757 | 0.0033 | 0.0083 |
| 2024_09_19 22:00 | 3218216 | 2 | 77.6119 | 91.5715 | -116.0178 | 5.7414 | 112.3902 | 0.0130 | 0.0034 |
| 2024_09_19 22:00 | 3249134 | 3 | 77.4088 | 75.0727 | -116.1573 | 18.7678 | 124.2178 | 0.0132 | 0.0074 |
| 2024_09_19 22:00 | 3218753 | 4 | 83.0055 | 75.7767 | -115.4161 | 13.3021 | 108.5188 | 0.0156 | 0.0115 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416293_997B1FC5 | 504990 | 474 | -84.6 | 504990 | 496 | -93.9 | 504990 | 366 | -94.3 | 504990 | 620 |
| MR_1774416293_3EE99041 | 504990 | 474 | -83.9 | 504990 | 496 | -94.7 | 504990 | 366 | -94.4 | 504990 | 620 |
| MR_1774416293_51A7EE9A | 504990 | 474 | -85.5 | 504990 | 496 | -93.8 | 504990 | 366 | -95.5 | 504990 | 620 |
| MR_1774416293_6AC7CA02 | 504990 | 474 | -86.1 | 504990 | 496 | -95.5 | 504990 | 366 | -96.2 | 504990 | 620 |
| MR_1774416293_8EF5BCD6 | 504990 | 474 | -86.5 | 504990 | 496 | -95.5 | 504990 | 366 | -93.6 | 504990 | 620 |
| MR_1774416293_A55B5E1F | 504990 | 474 | -87.5 | 504990 | 496 | -91.9 | 504990 | 366 | -96.5 | 504990 | 620 |
| MR_1774416293_834A1839 | 504990 | 474 | -85.0 | 504990 | 496 | -95.7 | 504990 | 366 | -93.6 | 504990 | 620 |
| MR_1774416293_B96D272E | 504990 | 474 | -84.5 | 504990 | 496 | -95.2 | 504990 | 366 | -96.3 | 504990 | 620 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1425: `85273fbf-31f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `85273fbf-31f5-4d08-9b68-91c606116615` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Lift the tilt angle  of 3277004_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1425] topology](images/train_1425.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220133_2
- `C2`: Check test server and transmission issues
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Press down the tilt angle  of 3277004_3 by 10 degrees
- `C5`: Lift the tilt angle of 3220133_2 by 3 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213124_4
- `C7`: Lift the tilt angle  of 3277004_3 by 10 degrees **← 정답**
- `C8`: Decrease A3 Offset threshold for 3213124_4
- `C9`: Decrease transmission power for 3220133_2
- `C10`: Adjust the azimuth of 3277004_3 by 50 degrees
- `C11`: Decrease A3 Offset threshold for 3220133_2
- `C12`: Decrease transmission power for 3213124_4
- `C13`: Adjust the azimuth of 3220133_2 by 5 degrees
- `C14`: Increase transmission power for 3213124_4
- `C15`: Add neighbor relationship between 3220133_2 and 3213124_4
- `C16`: Increase A3 Offset threshold for 3220133_2
- `C17`: Increase transmission power for 3220133_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220133_2
- `C19`: Press down the tilt angle of 3220133_2 by 3 degrees
- `C20`: Increase A3 Offset threshold for 3213124_4
- `C21`: Add neighbor relationship between 3277004_3 and 3213124_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213124_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.130 | MS1 | 121.4656703705 | 31.1446231822 | 740 | 504990 | -90.41 | 15.18 | 348.55 | 0.14 | 2.11 | 1572 |
| 2024-09-20 22:21:32.920 | MS1 | 121.4656622452 | 31.1446269810 | 740 | 504990 | -88.46 | 17.09 | 405.00 | 0.10 | 2.75 | 1592 |
| 2024-09-20 22:21:33.695 | MS1 | 121.4656671402 | 31.1446224221 | 740 | 504990 | -90.02 | 14.15 | 555.14 | 0.08 | 2.00 | 1567 |
| 2024-09-20 22:21:34.384 | MS1 | 121.4656638804 | 31.1446339826 | 740 | 504990 | -88.61 | 15.48 | 55.71 | 0.04 | 2.80 | 1592 |
| 2024-09-20 22:21:35.550 | MS1 | 121.4656663000 | 31.1446228884 | 740 | 504990 | -85.38 | 12.79 | 90.05 | 0.11 | 2.09 | 1560 |
| 2024-09-20 22:21:36.615 | MS1 | 121.4656615094 | 31.1446234206 | 740 | 504990 | -86.91 | 14.82 | 87.69 | 0.00 | 2.98 | 1584 |
| 2024-09-20 22:21:37.805 | MS1 | 121.4656755169 | 31.1446302137 | 740 | 504990 | -92.94 | 10.71 | 77.12 | 0.08 | 2.84 | 1568 |
| 2024-09-20 22:21:38.406 | MS1 | 121.4656775567 | 31.1446279671 | 740 | 504990 | -91.82 | 10.90 | 75.58 | 0.03 | 2.86 | 1581 |
| 2024-09-20 22:21:39.615 | MS1 | 121.4656727594 | 31.1446251202 | 740 | 504990 | -91.83 | 10.57 | 65.88 | 0.19 | 2.50 | 1576 |
| 2024-09-20 22:21:40.585 | MS1 | 121.4656672041 | 31.1446208844 | 740 | 504990 | -91.49 | 7.40 | 424.95 | 0.19 | 2.78 | 1599 |
| 2024-09-20 22:21:41.222 | MS1 | 121.4656648755 | 31.1446303795 | 740 | 504990 | -91.40 | 10.51 | 317.11 | 0.02 | 2.87 | 1598 |
| 2024-09-20 22:21:42.470 | MS1 | 121.4656768574 | 31.1446237896 | 740 | 504990 | -90.70 | 12.79 | 441.16 | 0.16 | 2.83 | 1579 |

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
| 3213124 | 4 | 121.4677826024 | 31.1464047320 | 17 | 6 | 4 | 40.9 | TDD | 774 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3220133 | 2 | 121.4739369220 | 31.1510643215 | 223 | 1 | 10 | 41.6 | TDD | 740 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3240704 | 1 | 121.4754103025 | 31.1455136588 | 284 | 11 | 0 | 26.6 | TDD | 218 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3277004 | 3 | 121.4672250458 | 31.1529767440 | 4 | 5 | 0 | 16.0 | TDD | 765 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.876 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.896 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.035 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.035 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.738 | NREventA3 | measId:2;ServCellPCI:785;Se... |
| 2024-09-20 22:21:37.978 | NRHandoverAttempt | SourcePCI:785;SourceNR-ARFC... |
| 2024-09-20 22:21:38.015 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.030 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.153 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.153 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240704 | 1 | 11.1614 | 18.5970 | -116.1667 | 10.9417 | 115.2340 | 0.0192 | 0.0116 |
| 2024_09_20 22:00 | 3220133 | 2 | 80.2240 | 93.8925 | -117.8939 | 7.3571 | 178.4062 | 0.0113 | 0.0169 |
| 2024_09_20 22:00 | 3277004 | 3 | 5.3068 | 18.1152 | -117.8418 | 15.7487 | 125.8957 | 0.0141 | 0.0177 |
| 2024_09_20 22:00 | 3213124 | 4 | 7.2189 | 9.4938 | -115.0999 | 13.2288 | 166.4020 | 0.0139 | 0.0128 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416029_ED6CFD64 | 504990 | 740 | -88.1 | 504990 | 774 | -95.2 | 504990 | 765 | -99.2 | 504990 | 218 |
| MR_1774416029_BE172FA5 | 504990 | 740 | -87.4 | 504990 | 774 | -92.1 | 504990 | 765 | -99.8 | 504990 | 218 |
| MR_1774416029_D54CCD18 | 504990 | 740 | -88.8 | 504990 | 774 | -94.4 | 504990 | 765 | -98.3 | 504990 | 218 |
| MR_1774416029_B3FFF07E | 504990 | 740 | -87.7 | 504990 | 774 | -94.2 | 504990 | 765 | -98.8 | 504990 | 218 |
| MR_1774416029_012B72F6 | 504990 | 740 | -88.0 | 504990 | 774 | -94.7 | 504990 | 765 | -99.3 | 504990 | 218 |
| MR_1774416029_06CC0E62 | 504990 | 740 | -90.0 | 504990 | 774 | -94.0 | 504990 | 765 | -96.4 | 504990 | 218 |
| MR_1774416029_089F0289 | 504990 | 740 | -90.5 | 504990 | 774 | -92.0 | 504990 | 765 | -98.9 | 504990 | 218 |
| MR_1774416029_207727EC | 504990 | 740 | -89.5 | 504990 | 774 | -94.0 | 504990 | 765 | -99.6 | 504990 | 218 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1426: `aac9ff74-a9f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `aac9ff74-a9fe-4aaa-887c-f1b5b72a3f0f` |
| Tag | **multiple-answer** |
| 정답 | **C5|C21** |
| C5 의미 | Press down the tilt angle  of 3263699_3 by 3 degrees |
| C21 의미 | Decrease transmission power for 3263699_3 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1426] topology](images/train_1426.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3263699_3
- `C2`: Lift the tilt angle  of 3263699_3 by 3 degrees
- `C3`: Increase transmission power for 3223303_1
- `C4`: Lift the tilt angle of 3223303_1 by 3 degrees
- `C5`: Press down the tilt angle  of 3263699_3 by 3 degrees **← 정답**
- `C6`: Increase A3 Offset threshold for 3263699_3
- `C7`: Decrease transmission power for 3223303_1
- `C8`: Check test server and transmission issues
- `C9`: Add neighbor relationship between 3223303_1 and 3263699_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223303_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263699_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223303_1
- `C13`: Adjust the azimuth of 3223303_1 by 44 degrees
- `C14`: Adjust the azimuth of 3263699_3 by 1 degrees
- `C15`: Decrease A3 Offset threshold for 3263699_3
- `C16`: Press down the tilt angle of 3223303_1 by 3 degrees
- `C17`: Increase A3 Offset threshold for 3223303_1
- `C18`: Add neighbor relationship between 3277354_2 and 3263699_3
- `C19`: Decrease A3 Offset threshold for 3223303_1
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease transmission power for 3263699_3 **← 정답**
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263699_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.348 | MS1 | 121.4656672316 | 31.1446291693 | 529 | 504990 | -83.93 | 12.05 | 560.97 | 0.08 | 2.11 | 1578 |
| 2024-09-20 22:21:32.611 | MS1 | 121.4656669903 | 31.1446240028 | 529 | 504990 | -80.52 | 12.68 | 428.42 | 0.17 | 2.60 | 1600 |
| 2024-09-20 22:21:33.737 | MS1 | 121.4656704277 | 31.1446364586 | 529 | 504990 | -83.66 | 16.07 | 430.12 | 0.05 | 2.56 | 1591 |
| 2024-09-20 22:21:34.852 | MS1 | 121.4656714350 | 31.1446305791 | 529 | 504990 | -88.17 | 0.35 | 63.11 | 0.02 | 1.46 | 1569 |
| 2024-09-20 22:21:35.910 | MS1 | 121.4656600271 | 31.1446222051 | 529 | 504990 | -87.34 | 2.73 | 52.16 | 0.04 | 1.36 | 1566 |
| 2024-09-20 22:21:36.431 | MS1 | 121.4656668813 | 31.1446202434 | 529 | 504990 | -88.59 | 2.32 | 47.73 | 0.11 | 1.30 | 1577 |
| 2024-09-20 22:21:37.697 | MS1 | 121.4656583560 | 31.1446262968 | 529 | 504990 | -94.31 | 0.42 | 63.97 | 0.19 | 1.39 | 1591 |
| 2024-09-20 22:21:38.493 | MS1 | 121.4656728166 | 31.1446201368 | 529 | 504990 | -94.27 | 2.62 | 53.90 | 0.07 | 1.14 | 1579 |
| 2024-09-20 22:21:39.246 | MS1 | 121.4656727690 | 31.1446231370 | 529 | 504990 | -88.28 | 0.22 | 77.59 | 0.14 | 1.02 | 1560 |
| 2024-09-20 22:21:40.453 | MS1 | 121.4656695682 | 31.1446217429 | 529 | 504990 | -82.59 | 17.16 | 325.68 | 0.19 | 2.05 | 1597 |
| 2024-09-20 22:21:41.199 | MS1 | 121.4656704024 | 31.1446307419 | 529 | 504990 | -76.14 | 12.17 | 488.62 | 0.08 | 2.54 | 1586 |
| 2024-09-20 22:21:42.992 | MS1 | 121.4656586341 | 31.1446253837 | 529 | 504990 | -80.48 | 13.55 | 498.58 | 0.19 | 2.98 | 1561 |

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
| 3223303 | 1 | 121.4746714444 | 31.1497362618 | 192 | 1 | 4 | 27.5 | TDD | 529 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3254593 | 4 | 121.4700148614 | 31.1446808804 | 257 | 11 | 4 | 32.9 | TDD | 941 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3263699 | 3 | 121.4643049562 | 31.1555036581 | 173 | 2 | 11 | 19.1 | TDD | 249 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3277354 | 2 | 121.4644290349 | 31.1456021253 | 355 | 9 | 11 | 35.3 | TDD | 59 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.376 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.392 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.515 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.515 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223303 | 1 | 5.2141 | 12.8923 | -108.6642 | 8.7744 | 83.9761 | 0.0057 | 0.0195 |
| 2024_09_20 22:00 | 3277354 | 2 | 10.1425 | 5.0647 | -114.0832 | 17.4057 | 100.2273 | 0.0037 | 0.0069 |
| 2024_09_20 22:00 | 3263699 | 3 | 17.3636 | 16.6233 | -115.3518 | 7.2289 | 109.5687 | 0.0129 | 0.0192 |
| 2024_09_20 22:00 | 3254593 | 4 | 17.7319 | 18.3080 | -114.7280 | 14.7395 | 169.4213 | 0.0076 | 0.0092 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416040_8041C8AE | 504990 | 249 | -87.8 | 504990 | 529 | -83.2 | 504990 | 59 | -86.4 | 504990 | 941 |
| MR_1774416040_9B830CD2 | 504990 | 529 | -88.2 | 504990 | 249 | -84.6 | 504990 | 59 | -86.3 | 504990 | 941 |
| MR_1774416040_D3C6F35C | 504990 | 249 | -87.3 | 504990 | 529 | -85.5 | 504990 | 59 | -89.8 | 504990 | 941 |
| MR_1774416040_40C3C2C9 | 504990 | 249 | -90.0 | 504990 | 529 | -83.7 | 504990 | 59 | -89.6 | 504990 | 941 |
| MR_1774416040_EACBC575 | 504990 | 529 | -86.5 | 504990 | 249 | -84.5 | 504990 | 59 | -87.4 | 504990 | 941 |
| MR_1774416040_1AE28BEC | 504990 | 249 | -89.2 | 504990 | 529 | -84.8 | 504990 | 59 | -86.1 | 504990 | 941 |
| MR_1774416040_A5C63062 | 504990 | 249 | -86.9 | 504990 | 529 | -85.8 | 504990 | 59 | -87.2 | 504990 | 941 |
| MR_1774416040_72680705 | 504990 | 529 | -87.8 | 504990 | 249 | -84.7 | 504990 | 59 | -89.2 | 504990 | 941 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1427: `6c06d6b5-3d4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6c06d6b5-3d41-4885-b589-e5c35941faa2` |
| Tag | **multiple-answer** |
| 정답 | **C10|C15** |
| C10 의미 | Decrease transmission power for 3279731_4 |
| C15 의미 | Press down the tilt angle  of 3279731_4 by 2 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1427] topology](images/train_1427.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3237377_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279731_4
- `C3`: Increase A3 Offset threshold for 3237377_1
- `C4`: Decrease A3 Offset threshold for 3279731_4
- `C5`: Press down the tilt angle of 3237377_1 by 2 degrees
- `C6`: Check test server and transmission issues
- `C7`: Add neighbor relationship between 3237377_1 and 3279731_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237377_1
- `C9`: Lift the tilt angle of 3237377_1 by 2 degrees
- `C10`: Decrease transmission power for 3279731_4 **← 정답**
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237377_1
- `C12`: Decrease A3 Offset threshold for 3237377_1
- `C13`: Adjust the azimuth of 3237377_1 by 27 degrees
- `C14`: Increase transmission power for 3279731_4
- `C15`: Press down the tilt angle  of 3279731_4 by 2 degrees **← 정답**
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease transmission power for 3237377_1
- `C18`: Lift the tilt angle  of 3279731_4 by 2 degrees
- `C19`: Increase A3 Offset threshold for 3279731_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279731_4
- `C21`: Add neighbor relationship between 3210931_2 and 3279731_4
- `C22`: Adjust the azimuth of 3279731_4 by 8 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.725 | MS1 | 121.4656636850 | 31.1446204786 | 787 | 504990 | -75.44 | 12.29 | 416.17 | 0.10 | 2.83 | 1575 |
| 2024-09-20 22:21:32.322 | MS1 | 121.4656618109 | 31.1446207943 | 787 | 504990 | -78.30 | 13.16 | 522.70 | 0.14 | 2.03 | 1565 |
| 2024-09-20 22:21:33.913 | MS1 | 121.4656723729 | 31.1446188188 | 787 | 504990 | -82.71 | 16.74 | 426.82 | 0.04 | 2.59 | 1584 |
| 2024-09-20 22:21:34.316 | MS1 | 121.4656635981 | 31.1446289232 | 787 | 504990 | -86.96 | 3.38 | 76.56 | 0.20 | 1.30 | 1570 |
| 2024-09-20 22:21:35.513 | MS1 | 121.4656682189 | 31.1446346572 | 787 | 504990 | -91.38 | 2.45 | 73.87 | 0.08 | 1.13 | 1584 |
| 2024-09-20 22:21:36.617 | MS1 | 121.4656687319 | 31.1446222237 | 787 | 504990 | -93.17 | 1.68 | 67.09 | 0.08 | 1.14 | 1574 |
| 2024-09-20 22:21:37.739 | MS1 | 121.4656670483 | 31.1446296057 | 787 | 504990 | -85.13 | 3.21 | 34.36 | 0.09 | 1.26 | 1587 |
| 2024-09-20 22:21:38.496 | MS1 | 121.4656601702 | 31.1446196219 | 787 | 504990 | -86.64 | 0.63 | 78.47 | 0.20 | 1.46 | 1600 |
| 2024-09-20 22:21:39.717 | MS1 | 121.4656630530 | 31.1446371098 | 787 | 504990 | -86.38 | 3.30 | 47.11 | 0.17 | 1.16 | 1592 |
| 2024-09-20 22:21:40.807 | MS1 | 121.4656590062 | 31.1446379826 | 787 | 504990 | -81.19 | 13.17 | 464.23 | 0.18 | 2.90 | 1580 |
| 2024-09-20 22:21:41.334 | MS1 | 121.4656659795 | 31.1446183956 | 787 | 504990 | -80.72 | 17.44 | 318.45 | 0.18 | 2.97 | 1563 |
| 2024-09-20 22:21:42.259 | MS1 | 121.4656643422 | 31.1446338407 | 787 | 504990 | -80.89 | 17.00 | 521.12 | 0.17 | 2.34 | 1595 |

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
| 3210931 | 2 | 121.4706197575 | 31.1516273673 | 51 | 2 | 7 | 35.1 | TDD | 795 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3237377 | 1 | 121.4734821592 | 31.1447420082 | 296 | 1 | 11 | 15.2 | TDD | 787 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3274192 | 3 | 121.4717415174 | 31.1491716688 | 119 | 6 | 2 | 23.4 | TDD | 420 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3279731 | 4 | 121.4681634060 | 31.1508104826 | 207 | 0 | 10 | 26.3 | TDD | 1006 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.878 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.899 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.016 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.016 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237377 | 1 | 11.6930 | 16.8478 | -109.2330 | 14.2282 | 108.3322 | 0.0102 | 0.0099 |
| 2024_09_20 22:00 | 3210931 | 2 | 18.7750 | 13.7503 | -114.7965 | 13.4219 | 139.7986 | 0.0135 | 0.0155 |
| 2024_09_20 22:00 | 3274192 | 3 | 14.1375 | 8.0948 | -116.0522 | 19.0557 | 179.4255 | 0.0071 | 0.0024 |
| 2024_09_20 22:00 | 3279731 | 4 | 5.5238 | 16.0616 | -116.3219 | 19.5265 | 87.7218 | 0.0121 | 0.0173 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414619_3987F2CF | 504990 | 787 | -85.4 | 504990 | 1006 | -84.8 | 504990 | 795 | -87.5 | 504990 | 420 |
| MR_1774414619_2AF25D7B | 504990 | 1006 | -85.1 | 504990 | 787 | -81.8 | 504990 | 795 | -84.4 | 504990 | 420 |
| MR_1774414619_947B5FAE | 504990 | 787 | -86.5 | 504990 | 1006 | -83.3 | 504990 | 795 | -84.0 | 504990 | 420 |
| MR_1774414619_5B0A0D4A | 504990 | 787 | -85.6 | 504990 | 1006 | -83.0 | 504990 | 795 | -84.9 | 504990 | 420 |
| MR_1774414619_70DDA589 | 504990 | 787 | -88.4 | 504990 | 1006 | -84.5 | 504990 | 795 | -87.0 | 504990 | 420 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1428: `7c5c904d-5d1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7c5c904d-5d11-42db-a1ba-d31b7c7a31e5` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3258695_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1428] topology](images/train_1428.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3235278_4
- `C2`: Press down the tilt angle  of 3235278_4 by 10 degrees
- `C3`: Decrease A3 Offset threshold for 3258695_2
- `C4`: Add neighbor relationship between 3258695_2 and 3235278_4
- `C5`: Increase transmission power for 3235278_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235278_4
- `C7`: Add neighbor relationship between 3228625_1 and 3235278_4
- `C8`: Adjust the azimuth of 3235278_4 by 50 degrees
- `C9`: Decrease A3 Offset threshold for 3235278_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235278_4
- `C11`: Decrease transmission power for 3258695_2
- `C12`: Lift the tilt angle  of 3235278_4 by 10 degrees
- `C13`: Lift the tilt angle of 3258695_2 by 4 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258695_2 **← 정답**
- `C15`: Increase transmission power for 3258695_2
- `C16`: Increase A3 Offset threshold for 3235278_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258695_2
- `C18`: Increase A3 Offset threshold for 3258695_2
- `C19`: Check test server and transmission issues
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Press down the tilt angle of 3258695_2 by 4 degrees
- `C22`: Adjust the azimuth of 3258695_2 by 14 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.368 | MS1 | 121.4656721998 | 31.1446280028 | 841 | 504990 | -88.48 | 16.45 | 539.18 | 0.17 | 2.71 | 1599 |
| 2024-09-20 22:21:32.199 | MS1 | 121.4656603426 | 31.1446297409 | 841 | 504990 | -85.38 | 16.85 | 531.93 | 0.09 | 2.09 | 1583 |
| 2024-09-20 22:21:33.636 | MS1 | 121.4656584512 | 31.1446205558 | 841 | 504990 | -85.79 | 17.14 | 394.88 | 0.14 | 2.17 | 1594 |
| 2024-09-20 22:21:34.923 | MS1 | 121.4656735178 | 31.1446185998 | 841 | 504990 | -89.21 | 16.64 | 73.54 | 0.69 | 2.17 | 562 |
| 2024-09-20 22:21:35.786 | MS1 | 121.4656676718 | 31.1446373348 | 841 | 504990 | -87.38 | 15.35 | 63.17 | 0.62 | 2.35 | 595 |
| 2024-09-20 22:21:36.575 | MS1 | 121.4656772203 | 31.1446296851 | 841 | 504990 | -86.24 | 16.97 | 58.37 | 0.60 | 2.98 | 661 |
| 2024-09-20 22:21:37.997 | MS1 | 121.4656677897 | 31.1446254754 | 841 | 504990 | -93.42 | 8.75 | 81.46 | 0.53 | 2.64 | 664 |
| 2024-09-20 22:21:38.384 | MS1 | 121.4656646395 | 31.1446255478 | 841 | 504990 | -90.80 | 9.55 | 43.11 | 0.51 | 2.47 | 572 |
| 2024-09-20 22:21:39.328 | MS1 | 121.4656764786 | 31.1446279172 | 841 | 504990 | -93.03 | 11.91 | 54.64 | 0.69 | 2.35 | 611 |
| 2024-09-20 22:21:40.490 | MS1 | 121.4656585905 | 31.1446351747 | 841 | 504990 | -92.46 | 9.84 | 343.22 | 0.01 | 2.05 | 1585 |
| 2024-09-20 22:21:41.338 | MS1 | 121.4656704118 | 31.1446316131 | 841 | 504990 | -92.06 | 7.93 | 553.58 | 0.18 | 2.25 | 1595 |
| 2024-09-20 22:21:42.943 | MS1 | 121.4656773448 | 31.1446277081 | 841 | 504990 | -93.15 | 11.85 | 364.79 | 0.11 | 2.46 | 1569 |

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
| 3228625 | 1 | 121.4650606284 | 31.1549744217 | 32 | 9 | 3 | 48.9 | TDD | 984 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3235278 | 4 | 121.4703528874 | 31.1558933379 | 26 | 10 | 7 | 43.7 | TDD | 915 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3253070 | 3 | 121.4747027743 | 31.1502714858 | 144 | 5 | 7 | 40.5 | TDD | 690 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3258695 | 2 | 121.4670397057 | 31.1507988425 | 177 | 1 | 5 | 33.5 | TDD | 841 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.050 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.071 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.187 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.187 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.879 | NREventA3 | measId:2;ServCellPCI:723;Se... |
| 2024-09-20 22:21:38.119 | NRHandoverAttempt | SourcePCI:723;SourceNR-ARFC... |
| 2024-09-20 22:21:38.169 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.183 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.328 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.328 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228625 | 1 | 6.9368 | 7.1942 | -115.8486 | 13.4984 | 153.1910 | 0.0022 | 0.0088 |
| 2024_09_20 22:00 | 3258695 | 2 | 8.6734 | 17.6370 | -114.2677 | 17.5105 | 182.7918 | 0.0156 | 0.0047 |
| 2024_09_20 22:00 | 3253070 | 3 | 16.1315 | 6.8896 | -116.9212 | 5.6734 | 121.6508 | 0.0080 | 0.0081 |
| 2024_09_20 22:00 | 3235278 | 4 | 14.6591 | 14.2406 | -114.9586 | 9.5008 | 94.0556 | 0.0110 | 0.0196 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412512_A83971E4 | 504990 | 841 | -90.7 | 504990 | 915 | -96.1 | 504990 | 984 | -97.1 | 504990 | 690 |
| MR_1774412512_792800E2 | 504990 | 841 | -89.5 | 504990 | 915 | -97.6 | 504990 | 984 | -98.2 | 504990 | 690 |
| MR_1774412512_8E740766 | 504990 | 841 | -88.5 | 504990 | 915 | -98.1 | 504990 | 984 | -97.4 | 504990 | 690 |
| MR_1774412512_B96B2938 | 504990 | 841 | -90.3 | 504990 | 915 | -98.5 | 504990 | 984 | -99.8 | 504990 | 690 |
| MR_1774412512_E0CEE0F6 | 504990 | 841 | -91.2 | 504990 | 915 | -97.8 | 504990 | 984 | -100.9 | 504990 | 690 |
| MR_1774412512_49F4D434 | 504990 | 841 | -90.4 | 504990 | 915 | -95.6 | 504990 | 984 | -99.6 | 504990 | 690 |
| MR_1774412512_DB474B44 | 504990 | 841 | -90.1 | 504990 | 915 | -97.5 | 504990 | 984 | -100.0 | 504990 | 690 |
| MR_1774412512_25AE5CA6 | 504990 | 841 | -90.9 | 504990 | 915 | -97.0 | 504990 | 984 | -99.6 | 504990 | 690 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1429: `afec168e-e21...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `afec168e-e21b-4e90-bb91-d48efb7d9baf` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Add neighbor relationship between 3243269_3 and 3218239_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1429] topology](images/train_1429.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3218239_2
- `C2`: Decrease transmission power for 3243269_3
- `C3`: Decrease A3 Offset threshold for 3218239_2
- `C4`: Add neighbor relationship between 3243269_3 and 3218239_2 **← 정답**
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218239_2
- `C6`: Lift the tilt angle  of 3218239_2 by 4 degrees
- `C7`: Press down the tilt angle  of 3218239_2 by 4 degrees
- `C8`: Press down the tilt angle of 3243269_3 by 10 degrees
- `C9`: Check test server and transmission issues
- `C10`: Increase A3 Offset threshold for 3243269_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218239_2
- `C12`: Decrease transmission power for 3218239_2
- `C13`: Decrease A3 Offset threshold for 3243269_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243269_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243269_3
- `C16`: Adjust the azimuth of 3218239_2 by 30 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Add neighbor relationship between 3270932_1 and 3218239_2
- `C19`: Adjust the azimuth of 3243269_3 by 50 degrees
- `C20`: Lift the tilt angle of 3243269_3 by 10 degrees
- `C21`: Increase A3 Offset threshold for 3218239_2
- `C22`: Increase transmission power for 3243269_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.352 | MS1 | 121.4656752699 | 31.1446262314 | 110 | 504990 | -80.32 | 12.41 | 339.64 | 0.17 | 2.15 | 1599 |
| 2024-09-20 22:21:32.307 | MS1 | 121.4656718648 | 31.1446234968 | 110 | 504990 | -78.19 | 16.69 | 533.32 | 0.16 | 2.73 | 1568 |
| 2024-09-20 22:21:33.818 | MS1 | 121.4656673583 | 31.1446332986 | 110 | 504990 | -80.59 | 17.00 | 552.81 | 0.04 | 2.27 | 1577 |
| 2024-09-20 22:21:34.995 | MS1 | 121.4656583492 | 31.1446252954 | 110 | 504990 | -85.97 | -2.67 | 72.97 | 0.08 | 1.14 | 1591 |
| 2024-09-20 22:21:35.199 | MS1 | 121.4656693610 | 31.1446322066 | 110 | 504990 | -94.59 | -0.03 | 65.24 | 0.04 | 1.20 | 1592 |
| 2024-09-20 22:21:36.592 | MS1 | 121.4656649383 | 31.1446270345 | 110 | 504990 | -85.16 | -1.65 | 50.55 | 0.04 | 1.10 | 1596 |
| 2024-09-20 22:21:37.471 | MS1 | 121.4656749031 | 31.1446327062 | 110 | 504990 | -86.76 | -1.14 | 40.58 | 0.08 | 1.38 | 1575 |
| 2024-09-20 22:21:38.270 | MS1 | 121.4656705159 | 31.1446261368 | 110 | 504990 | -77.64 | 14.28 | 574.03 | 0.16 | 1.14 | 1564 |
| 2024-09-20 22:21:39.438 | MS1 | 121.4656674325 | 31.1446224768 | 110 | 504990 | -82.76 | 17.67 | 537.24 | 0.09 | 1.10 | 1593 |
| 2024-09-20 22:21:40.280 | MS1 | 121.4656670935 | 31.1446346758 | 110 | 504990 | -77.82 | 13.68 | 489.39 | 0.15 | 2.44 | 1593 |
| 2024-09-20 22:21:41.667 | MS1 | 121.4656596840 | 31.1446285226 | 110 | 504990 | -82.59 | 16.09 | 562.99 | 0.16 | 2.47 | 1572 |
| 2024-09-20 22:21:42.450 | MS1 | 121.4656653426 | 31.1446355196 | 110 | 504990 | -79.44 | 14.73 | 453.46 | 0.06 | 2.62 | 1581 |

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
| 3218239 | 2 | 121.4734228593 | 31.1553565230 | 242 | 3 | 0 | 35.1 | TDD | 411 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3243269 | 3 | 121.4698397457 | 31.1469062327 | 0 | 11 | 4 | 41.7 | TDD | 110 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3270932 | 1 | 121.4649634004 | 31.1453808087 | 101 | 10 | 11 | 18.4 | TDD | 568 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3276957 | 4 | 121.4720538604 | 31.1470968244 | 44 | 8 | 0 | 43.5 | TDD | 167 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.799 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.819 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.943 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.943 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.620 | NREventA3 | measId:2;ServCellPCI:258;Se... |
| 2024-09-20 22:21:35.620 | NREventA3 | measId:2;ServCellPCI:258;Se... |
| 2024-09-20 22:21:36.620 | NREventA3 | measId:2;ServCellPCI:258;Se... |
| 2024-09-20 22:21:39.120 | NRRRCReestablishAttempt | PCI:258 |
| 2024-09-20 22:21:39.137 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.148 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.273 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.273 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270932 | 1 | 5.9908 | 16.3172 | -116.4278 | 6.7584 | 118.4265 | 0.0055 | 0.0157 |
| 2024_09_20 22:00 | 3218239 | 2 | 6.6534 | 5.4608 | -117.8929 | 8.4645 | 199.6269 | 0.0162 | 0.0156 |
| 2024_09_20 22:00 | 3243269 | 3 | 6.3897 | 11.4765 | -115.4535 | 5.5980 | 135.3385 | 0.0176 | 0.1449 |
| 2024_09_20 22:00 | 3276957 | 4 | 7.6718 | 5.3945 | -115.1082 | 7.0130 | 102.8551 | 0.0049 | 0.0119 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411971_EC79F2C4 | 504990 | 110 | -84.4 | 504990 | 411 | -82.5 | 504990 | 568 | -85.2 | 504990 | 167 |
| MR_1774411971_D83320D9 | 504990 | 411 | -80.8 | 504990 | 110 | -85.8 | 504990 | 568 | -86.2 | 504990 | 167 |
| MR_1774411971_2AE72F8F | 504990 | 110 | -86.5 | 504990 | 411 | -80.6 | 504990 | 568 | -87.6 | 504990 | 167 |
| MR_1774411971_27A91111 | 504990 | 110 | -85.6 | 504990 | 411 | -80.3 | 504990 | 568 | -89.1 | 504990 | 167 |
| MR_1774411971_E6F986E0 | 504990 | 110 | -85.5 | 504990 | 411 | -81.8 | 504990 | 568 | -87.4 | 504990 | 167 |
| MR_1774411971_A87A4187 | 504990 | 411 | -83.8 | 504990 | 110 | -87.8 | 504990 | 568 | -85.9 | 504990 | 167 |
| MR_1774411971_BEC91D2A | 504990 | 110 | -85.9 | 504990 | 411 | -83.5 | 504990 | 568 | -85.2 | 504990 | 167 |
| MR_1774411971_1EABAFAB | 504990 | 110 | -86.6 | 504990 | 411 | -83.7 | 504990 | 568 | -85.6 | 504990 | 167 |

> *... 2개 열 생략 (전체 14열)*

---
