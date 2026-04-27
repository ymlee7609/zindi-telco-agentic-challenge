# Track A 문제 분석 — train[660]~train[669]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[660] ~ train[669] (10개)

## 목차

1. [문제 660: `a9e4b8ea-c9a...`](#660) — single-answer, 정답: C1
2. [문제 661: `65bcce31-ca4...`](#661) — single-answer, 정답: C14
3. [문제 662: `4c405088-2ed...`](#662) — single-answer, 정답: C21
4. [문제 663: `9763a003-351...`](#663) — single-answer, 정답: C21
5. [문제 664: `279c5537-c12...`](#664) — single-answer, 정답: C19
6. [문제 665: `8930fa73-564...`](#665) — single-answer, 정답: C8
7. [문제 666: `cc8bee0c-013...`](#666) — single-answer, 정답: C12
8. [문제 667: `5a77887c-ac5...`](#667) — single-answer, 정답: C21
9. [문제 668: `c6bc4173-3ab...`](#668) — single-answer, 정답: C10
10. [문제 669: `c309a0b8-520...`](#669) — single-answer, 정답: C9

---

### 문제 660: `a9e4b8ea-c9a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a9e4b8ea-c9a5-4c91-9aef-c361e781a1a7` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3278103_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[660] topology](images/train_0660.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278103_2 **← 정답**
- `C2`: Adjust the azimuth of 3278103_2 by 32 degrees
- `C3`: Add neighbor relationship between 3278103_2 and 3259892_4
- `C4`: Increase transmission power for 3259892_4
- `C5`: Decrease A3 Offset threshold for 3259892_4
- `C6`: Check test server and transmission issues
- `C7`: Decrease transmission power for 3259892_4
- `C8`: Press down the tilt angle of 3278103_2 by 4 degrees
- `C9`: Add neighbor relationship between 3226035_1 and 3259892_4
- `C10`: Press down the tilt angle  of 3259892_4 by 10 degrees
- `C11`: Adjust the azimuth of 3259892_4 by 50 degrees
- `C12`: Decrease A3 Offset threshold for 3278103_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259892_4
- `C14`: Lift the tilt angle of 3278103_2 by 4 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259892_4
- `C17`: Increase A3 Offset threshold for 3259892_4
- `C18`: Decrease transmission power for 3278103_2
- `C19`: Increase A3 Offset threshold for 3278103_2
- `C20`: Lift the tilt angle  of 3259892_4 by 10 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278103_2
- `C22`: Increase transmission power for 3278103_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.808 | MS1 | 121.4656771183 | 31.1446297065 | 683 | 504990 | -89.59 | 13.77 | 476.70 | 0.09 | 2.62 | 1565 |
| 2024-09-20 22:21:32.164 | MS1 | 121.4656771314 | 31.1446256340 | 683 | 504990 | -85.60 | 14.98 | 390.23 | 0.05 | 2.32 | 1586 |
| 2024-09-20 22:21:33.611 | MS1 | 121.4656671597 | 31.1446352507 | 683 | 504990 | -88.57 | 15.37 | 397.71 | 0.19 | 2.56 | 1574 |
| 2024-09-20 22:21:34.388 | MS1 | 121.4656661587 | 31.1446223541 | 683 | 504990 | -91.24 | 14.66 | 97.57 | 0.66 | 2.07 | 676 |
| 2024-09-20 22:21:35.356 | MS1 | 121.4656685285 | 31.1446346432 | 683 | 504990 | -87.07 | 17.51 | 54.69 | 0.50 | 2.43 | 614 |
| 2024-09-20 22:21:36.230 | MS1 | 121.4656627542 | 31.1446203807 | 683 | 504990 | -89.72 | 13.12 | 104.79 | 0.56 | 2.86 | 506 |
| 2024-09-20 22:21:37.657 | MS1 | 121.4656591941 | 31.1446354034 | 683 | 504990 | -91.05 | 9.82 | 77.08 | 0.55 | 2.46 | 512 |
| 2024-09-20 22:21:38.276 | MS1 | 121.4656609209 | 31.1446297298 | 683 | 504990 | -93.72 | 8.67 | 108.70 | 0.69 | 2.89 | 640 |
| 2024-09-20 22:21:39.267 | MS1 | 121.4656668936 | 31.1446237645 | 683 | 504990 | -93.41 | 11.40 | 67.16 | 0.61 | 2.28 | 529 |
| 2024-09-20 22:21:40.426 | MS1 | 121.4656594830 | 31.1446180156 | 683 | 504990 | -89.02 | 11.34 | 310.02 | 0.20 | 2.46 | 1568 |
| 2024-09-20 22:21:41.363 | MS1 | 121.4656720406 | 31.1446379135 | 683 | 504990 | -89.35 | 9.46 | 332.65 | 0.14 | 2.70 | 1578 |
| 2024-09-20 22:21:42.718 | MS1 | 121.4656628939 | 31.1446360243 | 683 | 504990 | -89.90 | 9.46 | 421.18 | 0.01 | 2.83 | 1588 |

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
| 3217527 | 3 | 121.4659888873 | 31.1446483466 | 109 | 6 | 0 | 42.9 | TDD | 429 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3226035 | 1 | 121.4719828704 | 31.1504682784 | 158 | 1 | 6 | 45.6 | TDD | 73 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3259892 | 4 | 121.4673886544 | 31.1543352374 | 119 | 11 | 0 | 27.9 | TDD | 927 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3278103 | 2 | 121.4734856883 | 31.1443860570 | 240 | 2 | 9 | 30.1 | TDD | 683 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.355 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.483 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.483 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.232 | NREventA3 | measId:2;ServCellPCI:434;Se... |
| 2024-09-20 22:21:38.472 | NRHandoverAttempt | SourcePCI:434;SourceNR-ARFC... |
| 2024-09-20 22:21:38.503 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.517 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.617 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.617 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226035 | 1 | 13.2054 | 18.8937 | -115.6392 | 18.8994 | 153.7411 | 0.0077 | 0.0110 |
| 2024_09_20 22:00 | 3278103 | 2 | 11.1258 | 19.1384 | -116.6773 | 10.5915 | 166.1497 | 0.0188 | 0.0139 |
| 2024_09_20 22:00 | 3217527 | 3 | 14.4823 | 19.0111 | -114.7128 | 6.1984 | 174.9843 | 0.0077 | 0.0056 |
| 2024_09_20 22:00 | 3259892 | 4 | 16.0217 | 13.7737 | -116.8599 | 18.4425 | 91.9087 | 0.0174 | 0.0011 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414085_D3B8E6FB | 504990 | 683 | -91.4 | 504990 | 927 | -95.9 | 504990 | 73 | -99.3 | 504990 | 429 |
| MR_1774414085_0D7975BA | 504990 | 683 | -92.8 | 504990 | 927 | -94.8 | 504990 | 73 | -99.0 | 504990 | 429 |
| MR_1774414085_5D3D9C19 | 504990 | 683 | -92.0 | 504990 | 927 | -93.9 | 504990 | 73 | -99.2 | 504990 | 429 |
| MR_1774414085_7D3E270E | 504990 | 683 | -92.4 | 504990 | 927 | -95.8 | 504990 | 73 | -101.0 | 504990 | 429 |
| MR_1774414085_36679B89 | 504990 | 683 | -90.9 | 504990 | 927 | -95.8 | 504990 | 73 | -100.5 | 504990 | 429 |
| MR_1774414085_E7D0C246 | 504990 | 683 | -91.2 | 504990 | 927 | -96.3 | 504990 | 73 | -102.2 | 504990 | 429 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 661: `65bcce31-ca4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `65bcce31-ca48-4651-8ea7-20b4dc83a25d` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease A3 Offset threshold for 3234212_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[661] topology](images/train_0661.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234212_1
- `C2`: Increase A3 Offset threshold for 3272956_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234212_1
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Increase transmission power for 3272956_3
- `C6`: Decrease A3 Offset threshold for 3272956_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272956_3
- `C8`: Add neighbor relationship between 3234212_1 and 3272956_3
- `C9`: Increase transmission power for 3234212_1
- `C10`: Adjust the azimuth of 3234212_1 by 50 degrees
- `C11`: Lift the tilt angle of 3234212_1 by 10 degrees
- `C12`: Press down the tilt angle  of 3272956_3 by 10 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272956_3
- `C14`: Decrease A3 Offset threshold for 3234212_1 **← 정답**
- `C15`: Increase A3 Offset threshold for 3234212_1
- `C16`: Check test server and transmission issues
- `C17`: Press down the tilt angle of 3234212_1 by 10 degrees
- `C18`: Adjust the azimuth of 3272956_3 by 50 degrees
- `C19`: Decrease transmission power for 3272956_3
- `C20`: Add neighbor relationship between 3265119_4 and 3272956_3
- `C21`: Decrease transmission power for 3234212_1
- `C22`: Lift the tilt angle  of 3272956_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.596 | MS1 | 121.4656582248 | 31.1446204393 | 466 | 504990 | -81.89 | 15.97 | 538.24 | 0.12 | 2.04 | 1586 |
| 2024-09-20 22:21:32.452 | MS1 | 121.4656606491 | 31.1446215012 | 466 | 504990 | -80.91 | 12.22 | 508.78 | 0.18 | 2.29 | 1571 |
| 2024-09-20 22:21:33.234 | MS1 | 121.4656582522 | 31.1446228528 | 466 | 504990 | -79.00 | 13.10 | 452.71 | 0.10 | 2.97 | 1592 |
| 2024-09-20 22:21:34.426 | MS1 | 121.4656686977 | 31.1446321753 | 466 | 504990 | -83.07 | -2.72 | 63.20 | 0.15 | 1.23 | 1599 |
| 2024-09-20 22:21:35.743 | MS1 | 121.4656599185 | 31.1446189941 | 466 | 504990 | -84.26 | -1.02 | 48.61 | 0.08 | 1.24 | 1565 |
| 2024-09-20 22:21:36.416 | MS1 | 121.4656746775 | 31.1446272803 | 466 | 504990 | -92.85 | -3.58 | 35.17 | 0.06 | 1.13 | 1588 |
| 2024-09-20 22:21:37.992 | MS1 | 121.4656690183 | 31.1446184983 | 466 | 504990 | -83.92 | -3.20 | 35.72 | 0.19 | 1.07 | 1588 |
| 2024-09-20 22:21:38.209 | MS1 | 121.4656648922 | 31.1446242164 | 466 | 504990 | -89.26 | -0.44 | 66.69 | 0.16 | 1.12 | 1570 |
| 2024-09-20 22:21:39.704 | MS1 | 121.4656599078 | 31.1446328023 | 126 | 504990 | -81.47 | 13.62 | 149.64 | 0.05 | 1.22 | 1598 |
| 2024-09-20 22:21:40.159 | MS1 | 121.4656690131 | 31.1446285943 | 126 | 504990 | -75.83 | 16.44 | 526.38 | 0.02 | 2.42 | 1590 |
| 2024-09-20 22:21:41.708 | MS1 | 121.4656691160 | 31.1446278261 | 126 | 504990 | -80.90 | 16.64 | 312.27 | 0.07 | 2.09 | 1565 |
| 2024-09-20 22:21:42.176 | MS1 | 121.4656764728 | 31.1446304887 | 126 | 504990 | -76.60 | 14.53 | 393.16 | 0.04 | 2.80 | 1573 |

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
| 3234212 | 1 | 121.4748025645 | 31.1496910423 | 118 | 8 | 0 | 27.8 | TDD | 466 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3265119 | 4 | 121.4682462393 | 31.1493665453 | 222 | 13 | 6 | 24.6 | TDD | 386 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3272956 | 3 | 121.4699413469 | 31.1458301875 | 60 | 9 | 2 | 37.9 | TDD | 126 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3279166 | 2 | 121.4725842822 | 31.1523097613 | 166 | 15 | 6 | 40.3 | TDD | 757 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.282 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.297 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.421 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.421 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.178 | NREventA3 | measId:2;ServCellPCI:350;Se... |
| 2024-09-20 22:21:38.418 | NRHandoverAttempt | SourcePCI:350;SourceNR-ARFC... |
| 2024-09-20 22:21:38.459 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.473 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.619 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.619 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234212 | 1 | 16.7654 | 18.0835 | -117.0227 | 14.6374 | 196.3702 | 0.0034 | 0.1520 |
| 2024_09_20 22:00 | 3279166 | 2 | 8.1921 | 5.7085 | -115.8554 | 19.1510 | 193.8857 | 0.0143 | 0.0145 |
| 2024_09_20 22:00 | 3272956 | 3 | 19.0517 | 16.7042 | -114.8284 | 8.3469 | 148.0724 | 0.0138 | 0.0084 |
| 2024_09_20 22:00 | 3265119 | 4 | 15.4845 | 6.1538 | -116.3646 | 11.9006 | 172.5726 | 0.0010 | 0.0067 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416237_0EDFE656 | 504990 | 126 | -81.0 | 504990 | 466 | -84.6 | 504990 | 386 | -83.7 | 504990 | 757 |
| MR_1774416237_2203E52E | 504990 | 466 | -81.3 | 504990 | 126 | -79.5 | 504990 | 386 | -85.8 | 504990 | 757 |
| MR_1774416237_3A1CE687 | 504990 | 466 | -83.1 | 504990 | 126 | -80.4 | 504990 | 386 | -85.0 | 504990 | 757 |
| MR_1774416237_38D56F3B | 504990 | 126 | -77.8 | 504990 | 466 | -83.2 | 504990 | 386 | -84.3 | 504990 | 757 |
| MR_1774416237_81C866C9 | 504990 | 126 | -80.1 | 504990 | 466 | -83.5 | 504990 | 386 | -85.6 | 504990 | 757 |
| MR_1774416237_63362283 | 504990 | 126 | -79.6 | 504990 | 466 | -83.2 | 504990 | 386 | -84.1 | 504990 | 757 |
| MR_1774416237_14FF3A49 | 504990 | 466 | -84.4 | 504990 | 126 | -78.3 | 504990 | 386 | -83.9 | 504990 | 757 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 662: `4c405088-2ed...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4c405088-2ed4-46e6-bb25-200c0452546f` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234857_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[662] topology](images/train_0662.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3225760_5
- `C2`: Increase A3 Offset threshold for 3225760_5
- `C3`: Adjust the azimuth of 3225760_5 by 32 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225760_5
- `C5`: Press down the tilt angle of 3234857_1 by 5 degrees
- `C6`: Press down the tilt angle  of 3225760_5 by 2 degrees
- `C7`: Increase A3 Offset threshold for 3234857_1
- `C8`: Adjust the azimuth of 3234857_1 by 22 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease transmission power for 3234857_1
- `C11`: Lift the tilt angle of 3234857_1 by 5 degrees
- `C12`: Decrease A3 Offset threshold for 3234857_1
- `C13`: Lift the tilt angle  of 3225760_5 by 2 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225760_5
- `C15`: Increase transmission power for 3225760_5
- `C16`: Add neighbor relationship between 3234857_1 and 3225760_5
- `C17`: Check test server and transmission issues
- `C18`: Add neighbor relationship between 3233246_12 and 3225760_5
- `C19`: Decrease A3 Offset threshold for 3225760_5
- `C20`: Increase transmission power for 3234857_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234857_1 **← 정답**
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234857_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.978 | MS1 | 121.4656695811 | 31.1446372754 | 451 | 504990 | -95.08 | 12.94 | 309.74 | 0.15 | 2.37 | 1568 |
| 2024-09-20 22:21:32.101 | MS1 | 121.4656591463 | 31.1446217223 | 510 | 504990 | -94.39 | 9.40 | 329.96 | 0.05 | 2.45 | 1599 |
| 2024-09-20 22:21:33.647 | MS1 | 121.4656589156 | 31.1446378852 | 766 | 504990 | -95.16 | 9.11 | 417.04 | 0.01 | 2.08 | 1581 |
| 2024-09-20 22:21:34.914 | MS1 | 121.4656675078 | 31.1446190096 | 491 | 152650 | -96.67 | 6.12 | 60.06 | 0.15 | 1.74 | 942 |
| 2024-09-20 22:21:35.706 | MS1 | 121.4656608274 | 31.1446259405 | 10 | 152650 | -87.26 | 7.55 | 79.88 | 0.17 | 1.86 | 980 |
| 2024-09-20 22:21:36.741 | MS1 | 121.4656721428 | 31.1446376260 | 179 | 152650 | -91.76 | 5.79 | 66.34 | 0.05 | 1.52 | 900 |
| 2024-09-20 22:21:37.408 | MS1 | 121.4656673109 | 31.1446302173 | 893 | 152650 | -89.40 | 3.50 | 64.18 | 0.06 | 1.81 | 924 |
| 2024-09-20 22:21:38.816 | MS1 | 121.4656676404 | 31.1446375070 | 491 | 152650 | -89.92 | 3.72 | 65.09 | 0.07 | 1.96 | 983 |
| 2024-09-20 22:21:39.758 | MS1 | 121.4656773049 | 31.1446330382 | 10 | 152650 | -89.85 | 2.51 | 87.85 | 0.13 | 1.67 | 948 |
| 2024-09-20 22:21:40.197 | MS1 | 121.4656682464 | 31.1446204443 | 179 | 152650 | -91.99 | 7.92 | 69.68 | 0.13 | 2.08 | 1583 |
| 2024-09-20 22:21:41.519 | MS1 | 121.4656719673 | 31.1446184964 | 893 | 152650 | -94.49 | 4.46 | 73.74 | 0.14 | 2.80 | 1596 |
| 2024-09-20 22:21:42.347 | MS1 | 121.4656778638 | 31.1446194718 | 491 | 152650 | -87.63 | 3.15 | 81.48 | 0.02 | 2.51 | 1594 |

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
| 3215082 | 9 | 121.4675616757 | 31.1483935829 | 109 | 1 | 12 | 24.2 | FDD | 554 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3216294 | 3 | 121.4688477395 | 31.1506075151 | 335 | 0 | 12 | 26.8 | TDD | 431 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3225760 | 5 | 121.4662313449 | 31.1467785241 | 161 | 0 | 10 | 8.2 | TDD | 253 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3225939 | 4 | 121.4730555083 | 31.1546069251 | 142 | 12 | 7 | 26.1 | TDD | 667 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3226655 | 2 | 121.4742487782 | 31.1539073077 | 19 | 12 | 12 | 27.3 | TDD | 766 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3228766 | 11 | 121.4723698931 | 31.1473624457 | 44 | 2 | 7 | 3.3 | FDD | 336 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3233246 | 12 | 121.4695642969 | 31.1482871851 | 281 | 3 | 12 | 2.6 | FDD | 179 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3234857 | 1 | 121.4666056326 | 31.1506285014 | 166 | 3 | 7 | 21.6 | TDD | 451 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3240817 | 6 | 121.4732520809 | 31.1535498630 | 215 | 15 | 6 | 9.0 | TDD | 510 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3241163 | 10 | 121.4710376373 | 31.1543547295 | 4 | 4 | 7 | 12.9 | FDD | 879 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3243833 | 13 | 121.4725323647 | 31.1458869028 | 185 | 12 | 8 | 25.1 | FDD | 893 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3262438 | 8 | 121.4726308368 | 31.1494918350 | 295 | 10 | 10 | 14.6 | FDD | 491 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3266089 | 7 | 121.4759978545 | 31.1553273719 | 190 | 8 | 12 | 1.8 | FDD | 10 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |

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
| 2024-09-20 22:21:31.137 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.155 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.269 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.269 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.006 | NREventA2 | measId:1;ServCellPCI:614;Se... |
| 2024-09-20 22:21:35.121 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.404 | NREventA5 | measId:3;ServCellPCI:614;Se... |
| 2024-09-20 22:21:35.441 | NRHandoverAttempt | SourcePCI:614;SourceNR-ARFC... |
| 2024-09-20 22:21:35.470 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.485 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.591 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.591 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234857 | 1 | 8.7776 | 16.1064 | -116.7497 | 5.3646 | 88.4244 | 0.0126 | 0.0104 |
| 2024_09_20 22:00 | 3226655 | 2 | 7.1804 | 9.9666 | -117.7741 | 10.2992 | 116.8800 | 0.0001 | 0.0060 |
| 2024_09_20 22:00 | 3216294 | 3 | 6.2116 | 19.1353 | -117.4127 | 11.2044 | 170.6041 | 0.0157 | 0.0161 |
| 2024_09_20 22:00 | 3225939 | 4 | 5.2922 | 13.3175 | -114.0145 | 16.4387 | 138.9969 | 0.0016 | 0.0078 |
| 2024_09_20 22:00 | 3225760 | 5 | 12.7927 | 12.5768 | -117.7688 | 10.9635 | 136.1120 | 0.0109 | 0.0165 |
| 2024_09_20 22:00 | 3240817 | 6 | 16.5545 | 5.7847 | -114.2733 | 11.0097 | 137.6261 | 0.0104 | 0.0074 |
| 2024_09_20 22:00 | 3266089 | 7 | 14.0977 | 8.1604 | -115.4516 | 4.6838 | 23.7571 | 0.0148 | 0.0186 |
| 2024_09_20 22:00 | 3262438 | 8 | 8.2171 | 9.8796 | -117.2744 | 3.2256 | 21.1062 | 0.0158 | 0.0153 |
| 2024_09_20 22:00 | 3215082 | 9 | 5.5005 | 13.4050 | -115.0292 | 4.4359 | 36.7568 | 0.0071 | 0.0023 |
| 2024_09_20 22:00 | 3241163 | 10 | 9.0178 | 18.7658 | -115.0578 | 3.0337 | 44.9382 | 0.0045 | 0.0195 |
| 2024_09_20 22:00 | 3228766 | 11 | 19.5462 | 8.1664 | -115.9550 | 4.0302 | 41.1130 | 0.0192 | 0.0158 |
| 2024_09_20 22:00 | 3233246 | 12 | 11.2699 | 17.3832 | -117.4034 | 3.1506 | 32.4357 | 0.0121 | 0.0042 |
| 2024_09_20 22:00 | 3243833 | 13 | 13.0296 | 6.9097 | -114.2444 | 4.6644 | 37.9007 | 0.0056 | 0.0115 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416393_C93917AC | 152650 | 491 | -97.1 | 152650 | 554 | -103.2 | 152650 | 336 | -107.4 | 152650 | 879 |
| MR_1774416393_A03373CB | 152650 | 491 | -97.8 | 152650 | 554 | -102.6 | 152650 | 336 | -107.7 | 152650 | 879 |
| MR_1774416393_BD776D9B | 504990 | 766 | -97.1 | 504990 | 253 | -93.6 | 504990 | 431 | -100.1 | 504990 | 667 |
| MR_1774416393_72993042 | 152650 | 491 | -96.1 | 152650 | 554 | -102.0 | 152650 | 336 | -106.3 | 152650 | 879 |
| MR_1774416393_44036276 | 504990 | 766 | -96.0 | 504990 | 253 | -91.2 | 504990 | 431 | -100.0 | 504990 | 667 |
| MR_1774416393_009BCFAA | 504990 | 766 | -93.8 | 504990 | 253 | -91.2 | 504990 | 431 | -101.7 | 504990 | 667 |
| MR_1774416393_0FEDA07C | 152650 | 491 | -95.1 | 152650 | 554 | -104.8 | 152650 | 336 | -105.6 | 152650 | 879 |
| MR_1774416393_D7190D51 | 504990 | 766 | -95.8 | 504990 | 253 | -93.2 | 504990 | 431 | -100.3 | 504990 | 667 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 663: `9763a003-351...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9763a003-351d-4e51-aaba-3c69cf3664ea` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[663] topology](images/train_0663.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3228780_3 and 3247209_1
- `C2`: Increase A3 Offset threshold for 3250812_4
- `C3`: Add neighbor relationship between 3250812_4 and 3247209_1
- `C4`: Lift the tilt angle of 3250812_4 by 8 degrees
- `C5`: Check test server and transmission issues
- `C6`: Press down the tilt angle of 3250812_4 by 8 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247209_1
- `C8`: Decrease A3 Offset threshold for 3250812_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250812_4
- `C10`: Increase transmission power for 3250812_4
- `C11`: Press down the tilt angle  of 3247209_1 by 8 degrees
- `C12`: Increase A3 Offset threshold for 3247209_1
- `C13`: Lift the tilt angle  of 3247209_1 by 8 degrees
- `C14`: Decrease transmission power for 3247209_1
- `C15`: Decrease transmission power for 3250812_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247209_1
- `C17`: Increase transmission power for 3247209_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250812_4
- `C19`: Decrease A3 Offset threshold for 3247209_1
- `C20`: Adjust the azimuth of 3247209_1 by 10 degrees
- `C21`: Insufficient data; more data is needed for judgment. **← 정답**
- `C22`: Adjust the azimuth of 3250812_4 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.938 | MS1 | 121.4656777447 | 31.1446261704 | 518 | 504990 | -89.40 | 16.81 | 425.55 | 0.15 | 2.64 | 1578 |
| 2024-09-20 22:21:32.791 | MS1 | 121.4656690527 | 31.1446332452 | 518 | 504990 | -85.93 | 16.68 | 472.66 | 0.11 | 2.66 | 1595 |
| 2024-09-20 22:21:33.245 | MS1 | 121.4656619725 | 31.1446222356 | 518 | 504990 | -87.41 | 15.00 | 468.90 | 0.11 | 2.24 | 1586 |
| 2024-09-20 22:21:34.228 | MS1 | 121.4656728687 | 31.1446364376 | 518 | 504990 | -88.80 | 15.76 | 70.43 | 0.03 | 2.18 | 1599 |
| 2024-09-20 22:21:35.920 | MS1 | 121.4656743876 | 31.1446256237 | 518 | 504990 | -88.24 | 16.30 | 99.08 | 0.17 | 2.41 | 1565 |
| 2024-09-20 22:21:36.942 | MS1 | 121.4656663600 | 31.1446287338 | 518 | 504990 | -86.25 | 13.39 | 71.98 | 0.11 | 2.52 | 1585 |
| 2024-09-20 22:21:37.146 | MS1 | 121.4656703196 | 31.1446311638 | 518 | 504990 | -91.51 | 7.07 | 69.02 | 0.07 | 3.00 | 1581 |
| 2024-09-20 22:21:38.639 | MS1 | 121.4656774458 | 31.1446283817 | 518 | 504990 | -91.03 | 7.61 | 83.65 | 0.16 | 2.58 | 1578 |
| 2024-09-20 22:21:39.819 | MS1 | 121.4656626804 | 31.1446286409 | 518 | 504990 | -90.70 | 10.50 | 96.73 | 0.09 | 2.19 | 1560 |
| 2024-09-20 22:21:40.911 | MS1 | 121.4656746588 | 31.1446353848 | 518 | 504990 | -89.39 | 7.32 | 429.94 | 0.09 | 2.94 | 1582 |
| 2024-09-20 22:21:41.655 | MS1 | 121.4656622218 | 31.1446232633 | 518 | 504990 | -92.36 | 11.49 | 399.45 | 0.10 | 2.20 | 1593 |
| 2024-09-20 22:21:42.244 | MS1 | 121.4656741412 | 31.1446252210 | 518 | 504990 | -92.90 | 10.62 | 390.83 | 0.11 | 2.35 | 1575 |

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
| 3228780 | 3 | 121.4666396435 | 31.1522060980 | 15 | 6 | 1 | 37.5 | TDD | 134 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3247209 | 1 | 121.4703814644 | 31.1508115500 | 223 | 5 | 5 | 39.5 | TDD | 250 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3250812 | 4 | 121.4700133520 | 31.1511393531 | 312 | 6 | 4 | 24.2 | TDD | 518 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3278013 | 2 | 121.4724662775 | 31.1542990956 | 203 | 14 | 3 | 35.4 | TDD | 214 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.893 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.915 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.024 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.024 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.787 | NREventA3 | measId:2;ServCellPCI:799;Se... |
| 2024-09-20 22:21:38.027 | NRHandoverAttempt | SourcePCI:799;SourceNR-ARFC... |
| 2024-09-20 22:21:38.076 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.086 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.217 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.217 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3247209 | 1 | 94.5629 | 90.7632 | -117.5132 | 12.6112 | 185.2326 | 0.0020 | 0.0193 |
| 2024_09_19 22:00 | 3278013 | 2 | 93.2517 | 86.8039 | -115.9119 | 9.4720 | 82.9576 | 0.0147 | 0.0069 |
| 2024_09_19 22:00 | 3228780 | 3 | 80.2277 | 90.2690 | -114.0682 | 13.7137 | 84.1944 | 0.0049 | 0.0138 |
| 2024_09_19 22:00 | 3250812 | 4 | 79.5654 | 84.3034 | -114.9743 | 17.8950 | 131.6153 | 0.0100 | 0.0023 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414638_9039134F | 504990 | 518 | -87.1 | 504990 | 250 | -97.6 | 504990 | 134 | -100.4 | 504990 | 214 |
| MR_1774414638_998360A0 | 504990 | 518 | -90.4 | 504990 | 250 | -95.8 | 504990 | 134 | -101.3 | 504990 | 214 |
| MR_1774414638_AF973A13 | 504990 | 518 | -87.4 | 504990 | 250 | -95.0 | 504990 | 134 | -100.6 | 504990 | 214 |
| MR_1774414638_2B4186A7 | 504990 | 518 | -90.4 | 504990 | 250 | -97.5 | 504990 | 134 | -99.0 | 504990 | 214 |
| MR_1774414638_CCC66990 | 504990 | 518 | -88.2 | 504990 | 250 | -94.9 | 504990 | 134 | -100.8 | 504990 | 214 |
| MR_1774414638_E2D102C0 | 504990 | 518 | -88.0 | 504990 | 250 | -95.7 | 504990 | 134 | -99.9 | 504990 | 214 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 664: `279c5537-c12...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `279c5537-c125-4891-beda-9c6462866ccc` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211739_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[664] topology](images/train_0664.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3211739_4 by 5 degrees
- `C2`: Press down the tilt angle  of 3278660_6 by 4 degrees
- `C3`: Increase transmission power for 3211739_4
- `C4`: Decrease transmission power for 3278660_6
- `C5`: Add neighbor relationship between 3211739_4 and 3278660_6
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278660_6
- `C7`: Decrease A3 Offset threshold for 3278660_6
- `C8`: Decrease transmission power for 3211739_4
- `C9`: Add neighbor relationship between 3252776_9 and 3278660_6
- `C10`: Increase transmission power for 3278660_6
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Lift the tilt angle  of 3278660_6 by 4 degrees
- `C13`: Adjust the azimuth of 3278660_6 by 34 degrees
- `C14`: Decrease A3 Offset threshold for 3211739_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211739_4
- `C16`: Adjust the azimuth of 3211739_4 by 20 degrees
- `C17`: Press down the tilt angle of 3211739_4 by 5 degrees
- `C18`: Increase A3 Offset threshold for 3278660_6
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211739_4 **← 정답**
- `C20`: Check test server and transmission issues
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278660_6
- `C22`: Increase A3 Offset threshold for 3211739_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.192 | MS1 | 121.4656698191 | 31.1446223697 | 753 | 504990 | -93.71 | 9.11 | 461.01 | 0.14 | 2.55 | 1561 |
| 2024-09-20 22:21:32.276 | MS1 | 121.4656766294 | 31.1446231780 | 844 | 504990 | -94.53 | 13.48 | 491.48 | 0.17 | 2.71 | 1587 |
| 2024-09-20 22:21:33.946 | MS1 | 121.4656618979 | 31.1446194232 | 977 | 504990 | -94.85 | 12.69 | 413.27 | 0.08 | 2.61 | 1568 |
| 2024-09-20 22:21:34.547 | MS1 | 121.4656729785 | 31.1446258271 | 165 | 152650 | -91.53 | 7.60 | 79.93 | 0.01 | 1.86 | 916 |
| 2024-09-20 22:21:35.178 | MS1 | 121.4656769085 | 31.1446364086 | 216 | 152650 | -87.85 | 7.10 | 103.23 | 0.18 | 1.62 | 904 |
| 2024-09-20 22:21:36.817 | MS1 | 121.4656716135 | 31.1446372425 | 625 | 152650 | -88.07 | 7.22 | 86.32 | 0.19 | 1.59 | 902 |
| 2024-09-20 22:21:37.555 | MS1 | 121.4656678110 | 31.1446290727 | 235 | 152650 | -87.88 | 7.08 | 75.66 | 0.06 | 1.62 | 994 |
| 2024-09-20 22:21:38.494 | MS1 | 121.4656678109 | 31.1446202930 | 165 | 152650 | -87.40 | 2.48 | 65.15 | 0.16 | 1.77 | 986 |
| 2024-09-20 22:21:39.765 | MS1 | 121.4656756185 | 31.1446198946 | 216 | 152650 | -92.68 | 3.95 | 92.73 | 0.18 | 1.82 | 917 |
| 2024-09-20 22:21:40.104 | MS1 | 121.4656759094 | 31.1446359171 | 625 | 152650 | -90.85 | 2.49 | 81.40 | 0.18 | 2.53 | 1572 |
| 2024-09-20 22:21:41.981 | MS1 | 121.4656739710 | 31.1446256577 | 235 | 152650 | -88.94 | 4.35 | 81.72 | 0.18 | 2.38 | 1581 |
| 2024-09-20 22:21:42.597 | MS1 | 121.4656753070 | 31.1446273824 | 165 | 152650 | -94.23 | 5.21 | 71.71 | 0.00 | 2.27 | 1567 |

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
| 3211739 | 4 | 121.4694643621 | 31.1445655430 | 291 | 1 | 5 | 26.8 | TDD | 753 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3226180 | 2 | 121.4735307071 | 31.1475510246 | 224 | 5 | 6 | 3.3 | TDD | 97 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3241625 | 1 | 121.4709315007 | 31.1451520131 | 258 | 8 | 10 | 27.5 | TDD | 832 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3242838 | 8 | 121.4649289036 | 31.1475584570 | 345 | 2 | 1 | 23.9 | FDD | 235 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3246838 | 3 | 121.4715248582 | 31.1471806087 | 59 | 15 | 1 | 18.1 | TDD | 844 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3249372 | 10 | 121.4641018815 | 31.1467415276 | 82 | 4 | 5 | 14.0 | FDD | 216 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3252776 | 9 | 121.4747153494 | 31.1464456089 | 202 | 14 | 10 | 19.0 | FDD | 625 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3259406 | 5 | 121.4718630332 | 31.1545572293 | 66 | 2 | 4 | 27.8 | TDD | 977 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3259888 | 7 | 121.4662675763 | 31.1515990085 | 28 | 14 | 1 | 25.9 | FDD | 165 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3266496 | 11 | 121.4716659168 | 31.1475036341 | 319 | 12 | 7 | 21.1 | FDD | 346 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3266830 | 12 | 121.4640400120 | 31.1537910634 | 279 | 10 | 12 | 11.2 | FDD | 219 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3269029 | 13 | 121.4686849526 | 31.1534645151 | 77 | 8 | 6 | 21.0 | FDD | 890 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3278660 | 6 | 121.4753599771 | 31.1503531215 | 269 | 3 | 12 | 11.6 | TDD | 755 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.322 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.347 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.495 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.495 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.163 | NREventA2 | measId:1;ServCellPCI:945;Se... |
| 2024-09-20 22:21:35.288 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.521 | NREventA5 | measId:3;ServCellPCI:945;Se... |
| 2024-09-20 22:21:35.573 | NRHandoverAttempt | SourcePCI:945;SourceNR-ARFC... |
| 2024-09-20 22:21:35.605 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.619 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.765 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.765 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241625 | 1 | 14.8145 | 7.7387 | -117.1522 | 17.0228 | 198.5912 | 0.0150 | 0.0089 |
| 2024_09_20 22:00 | 3226180 | 2 | 12.0366 | 14.2209 | -115.4206 | 15.2851 | 124.5134 | 0.0034 | 0.0047 |
| 2024_09_20 22:00 | 3246838 | 3 | 13.5641 | 10.4776 | -117.4134 | 6.5919 | 150.0579 | 0.0043 | 0.0155 |
| 2024_09_20 22:00 | 3211739 | 4 | 5.2162 | 13.2465 | -114.1414 | 11.9410 | 97.6741 | 0.0033 | 0.0111 |
| 2024_09_20 22:00 | 3259406 | 5 | 7.5463 | 14.5780 | -115.3371 | 5.7108 | 167.3370 | 0.0044 | 0.0133 |
| 2024_09_20 22:00 | 3278660 | 6 | 6.2905 | 13.5229 | -116.5180 | 14.2925 | 116.5425 | 0.0088 | 0.0087 |
| 2024_09_20 22:00 | 3259888 | 7 | 14.3264 | 18.8986 | -116.3041 | 4.3564 | 31.6357 | 0.0042 | 0.0079 |
| 2024_09_20 22:00 | 3242838 | 8 | 8.2973 | 5.7052 | -115.2344 | 4.2250 | 53.8865 | 0.0160 | 0.0169 |
| 2024_09_20 22:00 | 3252776 | 9 | 15.0631 | 14.4387 | -117.5698 | 4.3782 | 54.9918 | 0.0140 | 0.0016 |
| 2024_09_20 22:00 | 3249372 | 10 | 12.4330 | 16.9874 | -115.7483 | 3.4116 | 21.6943 | 0.0151 | 0.0144 |
| 2024_09_20 22:00 | 3266496 | 11 | 17.6473 | 19.5508 | -114.8506 | 4.5091 | 52.3188 | 0.0101 | 0.0145 |
| 2024_09_20 22:00 | 3266830 | 12 | 9.3702 | 17.7888 | -114.4680 | 3.0624 | 58.9831 | 0.0137 | 0.0151 |
| 2024_09_20 22:00 | 3269029 | 13 | 12.3673 | 8.7123 | -116.5497 | 4.6998 | 33.1122 | 0.0130 | 0.0029 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413092_96161374 | 152650 | 165 | -91.2 | 152650 | 346 | -94.3 | 152650 | 219 | -101.9 | 152650 | 890 |
| MR_1774413092_FA0E341C | 152650 | 165 | -91.9 | 152650 | 346 | -94.4 | 152650 | 219 | -102.3 | 152650 | 890 |
| MR_1774413092_979CE4EF | 504990 | 977 | -95.4 | 504990 | 755 | -93.8 | 504990 | 97 | -93.9 | 504990 | 832 |
| MR_1774413092_1A2DF029 | 504990 | 977 | -95.7 | 504990 | 755 | -93.8 | 504990 | 97 | -93.6 | 504990 | 832 |
| MR_1774413092_019CEE9D | 504990 | 977 | -93.2 | 504990 | 755 | -93.9 | 504990 | 97 | -96.1 | 504990 | 832 |
| MR_1774413092_459CF0B2 | 152650 | 165 | -90.8 | 152650 | 346 | -93.4 | 152650 | 219 | -104.0 | 152650 | 890 |
| MR_1774413092_150E4D96 | 504990 | 977 | -96.5 | 504990 | 755 | -92.8 | 504990 | 97 | -95.5 | 504990 | 832 |
| MR_1774413092_B224EFB7 | 152650 | 165 | -91.2 | 152650 | 346 | -93.8 | 152650 | 219 | -101.2 | 152650 | 890 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 665: `8930fa73-564...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8930fa73-5640-4bb6-8be2-c4a6ddc7311e` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270097_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[665] topology](images/train_0665.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217368_3
- `C2`: Increase transmission power for 3270097_6
- `C3`: Press down the tilt angle  of 3217368_3 by 2 degrees
- `C4`: Check test server and transmission issues
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270097_6
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease A3 Offset threshold for 3217368_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270097_6 **← 정답**
- `C9`: Lift the tilt angle of 3270097_6 by 4 degrees
- `C10`: Adjust the azimuth of 3270097_6 by 35 degrees
- `C11`: Adjust the azimuth of 3217368_3 by 18 degrees
- `C12`: Decrease transmission power for 3270097_6
- `C13`: Add neighbor relationship between 3239051_13 and 3217368_3
- `C14`: Press down the tilt angle of 3270097_6 by 4 degrees
- `C15`: Decrease transmission power for 3217368_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217368_3
- `C17`: Add neighbor relationship between 3270097_6 and 3217368_3
- `C18`: Lift the tilt angle  of 3217368_3 by 2 degrees
- `C19`: Increase transmission power for 3217368_3
- `C20`: Decrease A3 Offset threshold for 3270097_6
- `C21`: Increase A3 Offset threshold for 3270097_6
- `C22`: Increase A3 Offset threshold for 3217368_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.973 | MS1 | 121.4656774078 | 31.1446262758 | 798 | 504990 | -95.03 | 14.72 | 446.39 | 0.03 | 2.50 | 1586 |
| 2024-09-20 22:21:32.558 | MS1 | 121.4656628988 | 31.1446287254 | 135 | 504990 | -95.09 | 14.27 | 442.94 | 0.13 | 2.62 | 1566 |
| 2024-09-20 22:21:33.387 | MS1 | 121.4656681295 | 31.1446212681 | 788 | 504990 | -93.11 | 11.18 | 554.05 | 0.05 | 2.53 | 1592 |
| 2024-09-20 22:21:34.912 | MS1 | 121.4656671400 | 31.1446282417 | 996 | 152650 | -93.10 | 3.52 | 85.75 | 0.19 | 1.79 | 900 |
| 2024-09-20 22:21:35.780 | MS1 | 121.4656594274 | 31.1446365386 | 394 | 152650 | -95.58 | 6.44 | 55.74 | 0.02 | 1.85 | 905 |
| 2024-09-20 22:21:36.856 | MS1 | 121.4656653383 | 31.1446189734 | 510 | 152650 | -95.90 | 6.04 | 89.39 | 0.04 | 1.74 | 911 |
| 2024-09-20 22:21:37.164 | MS1 | 121.4656717950 | 31.1446377054 | 52 | 152650 | -94.60 | 6.29 | 72.56 | 0.01 | 1.76 | 914 |
| 2024-09-20 22:21:38.614 | MS1 | 121.4656698577 | 31.1446190009 | 996 | 152650 | -93.45 | 7.50 | 94.63 | 0.12 | 1.69 | 999 |
| 2024-09-20 22:21:39.520 | MS1 | 121.4656696208 | 31.1446339918 | 394 | 152650 | -89.04 | 6.12 | 91.46 | 0.08 | 1.58 | 991 |
| 2024-09-20 22:21:40.922 | MS1 | 121.4656713167 | 31.1446313346 | 510 | 152650 | -90.06 | 2.22 | 57.89 | 0.02 | 2.24 | 1593 |
| 2024-09-20 22:21:41.347 | MS1 | 121.4656767633 | 31.1446359347 | 52 | 152650 | -92.61 | 7.90 | 82.09 | 0.15 | 2.52 | 1560 |
| 2024-09-20 22:21:42.622 | MS1 | 121.4656702712 | 31.1446367253 | 996 | 152650 | -92.87 | 2.45 | 74.96 | 0.10 | 2.66 | 1594 |

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
| 3217368 | 3 | 121.4734729828 | 31.1541552914 | 233 | 1 | 12 | 26.8 | TDD | 462 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3223666 | 8 | 121.4682189885 | 31.1487630252 | 310 | 14 | 0 | 8.4 | FDD | 995 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3224773 | 9 | 121.4688515052 | 31.1484437516 | 183 | 13 | 1 | 11.2 | FDD | 996 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3229181 | 11 | 121.4746376760 | 31.1523533335 | 99 | 12 | 4 | 16.3 | FDD | 747 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3239051 | 13 | 121.4723022628 | 31.1506349443 | 210 | 5 | 7 | 6.4 | FDD | 510 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3243667 | 10 | 121.4728953119 | 31.1462075547 | 356 | 1 | 2 | 8.4 | FDD | 394 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3255168 | 2 | 121.4686427368 | 31.1504161844 | 102 | 7 | 11 | 8.6 | TDD | 135 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3256889 | 7 | 121.4719239317 | 31.1477431895 | 351 | 14 | 1 | 24.3 | FDD | 864 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3263585 | 1 | 121.4749419669 | 31.1526197422 | 235 | 6 | 5 | 2.9 | TDD | 641 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3268067 | 12 | 121.4698220078 | 31.1539153714 | 146 | 4 | 7 | 12.1 | FDD | 52 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3270097 | 6 | 121.4653847451 | 31.1505326459 | 143 | 3 | 2 | 9.0 | TDD | 798 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3275520 | 4 | 121.4694201914 | 31.1477679218 | 318 | 2 | 5 | 24.4 | TDD | 788 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3279684 | 5 | 121.4699587320 | 31.1507148652 | 287 | 13 | 7 | 8.8 | TDD | 541 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.910 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.028 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.028 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.734 | NREventA2 | measId:1;ServCellPCI:140;Se... |
| 2024-09-20 22:21:34.883 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.108 | NREventA5 | measId:3;ServCellPCI:140;Se... |
| 2024-09-20 22:21:35.184 | NRHandoverAttempt | SourcePCI:140;SourceNR-ARFC... |
| 2024-09-20 22:21:35.212 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.222 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.357 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.357 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263585 | 1 | 16.1113 | 16.9219 | -116.1106 | 10.1837 | 153.2822 | 0.0018 | 0.0150 |
| 2024_09_20 22:00 | 3255168 | 2 | 11.9029 | 10.7930 | -116.9164 | 7.7217 | 163.9765 | 0.0189 | 0.0127 |
| 2024_09_20 22:00 | 3217368 | 3 | 18.3804 | 5.1127 | -114.7493 | 6.1083 | 108.5339 | 0.0121 | 0.0004 |
| 2024_09_20 22:00 | 3275520 | 4 | 10.9893 | 19.3730 | -114.3304 | 10.9752 | 146.4584 | 0.0127 | 0.0125 |
| 2024_09_20 22:00 | 3279684 | 5 | 9.7391 | 16.9515 | -116.9192 | 17.5620 | 162.0236 | 0.0054 | 0.0186 |
| 2024_09_20 22:00 | 3270097 | 6 | 15.3216 | 7.5990 | -116.0337 | 11.8678 | 85.0631 | 0.0153 | 0.0082 |
| 2024_09_20 22:00 | 3256889 | 7 | 17.7350 | 8.8618 | -115.1236 | 4.0674 | 22.6978 | 0.0124 | 0.0135 |
| 2024_09_20 22:00 | 3223666 | 8 | 19.9831 | 8.1441 | -116.8689 | 3.3562 | 55.9109 | 0.0044 | 0.0131 |
| 2024_09_20 22:00 | 3224773 | 9 | 11.2567 | 7.3174 | -114.0167 | 4.9294 | 50.2047 | 0.0003 | 0.0179 |
| 2024_09_20 22:00 | 3243667 | 10 | 18.0033 | 14.8434 | -116.5053 | 4.9928 | 51.7491 | 0.0199 | 0.0048 |
| 2024_09_20 22:00 | 3229181 | 11 | 5.9912 | 14.5723 | -114.8570 | 4.5585 | 27.5680 | 0.0153 | 0.0170 |
| 2024_09_20 22:00 | 3268067 | 12 | 9.9094 | 9.8847 | -117.8494 | 3.1318 | 45.1675 | 0.0011 | 0.0002 |
| 2024_09_20 22:00 | 3239051 | 13 | 7.6015 | 14.4971 | -116.5876 | 3.4106 | 40.4904 | 0.0143 | 0.0053 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416715_6372DF9B | 504990 | 788 | -93.0 | 504990 | 462 | -94.7 | 504990 | 541 | -97.3 | 504990 | 641 |
| MR_1774416715_0E34DAC7 | 152650 | 996 | -91.4 | 152650 | 864 | -98.0 | 152650 | 747 | -104.8 | 152650 | 995 |
| MR_1774416715_1B359EB2 | 504990 | 788 | -95.0 | 504990 | 462 | -95.8 | 504990 | 541 | -98.3 | 504990 | 641 |
| MR_1774416715_9B899CAA | 504990 | 788 | -92.8 | 504990 | 462 | -96.0 | 504990 | 541 | -95.7 | 504990 | 641 |
| MR_1774416715_B6C51D99 | 152650 | 996 | -94.4 | 152650 | 864 | -98.7 | 152650 | 747 | -101.7 | 152650 | 995 |
| MR_1774416715_0C1CA5B7 | 152650 | 996 | -94.7 | 152650 | 864 | -95.2 | 152650 | 747 | -103.0 | 152650 | 995 |
| MR_1774416715_1CE17523 | 152650 | 996 | -94.3 | 152650 | 864 | -98.0 | 152650 | 747 | -105.1 | 152650 | 995 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 666: `cc8bee0c-013...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cc8bee0c-0132-4006-9138-453cbaf99712` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[666] topology](images/train_0666.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3256019_2 by 36 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264351_3
- `C3`: Add neighbor relationship between 3256019_2 and 3264351_3
- `C4`: Decrease transmission power for 3256019_2
- `C5`: Increase A3 Offset threshold for 3264351_3
- `C6`: Lift the tilt angle of 3256019_2 by 10 degrees
- `C7`: Decrease transmission power for 3264351_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256019_2
- `C9`: Add neighbor relationship between 3215362_1 and 3264351_3
- `C10`: Press down the tilt angle of 3256019_2 by 10 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256019_2
- `C12`: Insufficient data; more data is needed for judgment. **← 정답**
- `C13`: Increase transmission power for 3256019_2
- `C14`: Lift the tilt angle  of 3264351_3 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3264351_3
- `C16`: Adjust the azimuth of 3264351_3 by 50 degrees
- `C17`: Increase A3 Offset threshold for 3256019_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264351_3
- `C19`: Decrease A3 Offset threshold for 3256019_2
- `C20`: Press down the tilt angle  of 3264351_3 by 10 degrees
- `C21`: Check test server and transmission issues
- `C22`: Increase transmission power for 3264351_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.720 | MS1 | 121.4656759098 | 31.1446307857 | 60 | 504990 | -88.49 | 17.51 | 564.75 | 0.12 | 2.17 | 1594 |
| 2024-09-20 22:21:32.770 | MS1 | 121.4656630398 | 31.1446183458 | 60 | 504990 | -91.98 | 16.52 | 356.17 | 0.13 | 2.01 | 1593 |
| 2024-09-20 22:21:33.869 | MS1 | 121.4656727422 | 31.1446312220 | 60 | 504990 | -90.93 | 16.54 | 397.36 | 0.13 | 2.10 | 1574 |
| 2024-09-20 22:21:34.785 | MS1 | 121.4656629494 | 31.1446303493 | 60 | 504990 | -90.93 | 15.95 | 71.38 | 0.20 | 2.84 | 1600 |
| 2024-09-20 22:21:35.969 | MS1 | 121.4656728570 | 31.1446299954 | 60 | 504990 | -90.44 | 14.88 | 69.15 | 0.19 | 2.50 | 1598 |
| 2024-09-20 22:21:36.252 | MS1 | 121.4656650269 | 31.1446374778 | 60 | 504990 | -89.62 | 15.77 | 77.19 | 0.01 | 2.98 | 1596 |
| 2024-09-20 22:21:37.321 | MS1 | 121.4656767832 | 31.1446332321 | 60 | 504990 | -91.56 | 12.58 | 96.67 | 0.03 | 2.12 | 1568 |
| 2024-09-20 22:21:38.799 | MS1 | 121.4656734061 | 31.1446196472 | 60 | 504990 | -90.96 | 11.20 | 76.21 | 0.07 | 2.15 | 1565 |
| 2024-09-20 22:21:39.915 | MS1 | 121.4656675821 | 31.1446200768 | 60 | 504990 | -89.55 | 7.08 | 84.78 | 0.04 | 2.25 | 1565 |
| 2024-09-20 22:21:40.395 | MS1 | 121.4656709898 | 31.1446345843 | 60 | 504990 | -89.08 | 12.83 | 445.46 | 0.14 | 2.45 | 1589 |
| 2024-09-20 22:21:41.473 | MS1 | 121.4656713739 | 31.1446329434 | 60 | 504990 | -93.31 | 12.83 | 513.43 | 0.12 | 2.61 | 1589 |
| 2024-09-20 22:21:42.225 | MS1 | 121.4656702316 | 31.1446213145 | 60 | 504990 | -89.31 | 7.11 | 428.55 | 0.13 | 2.10 | 1581 |

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
| 3215362 | 1 | 121.4660297663 | 31.1544043973 | 342 | 5 | 9 | 28.7 | TDD | 539 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3256019 | 2 | 121.4744284778 | 31.1522334439 | 261 | 15 | 5 | 33.3 | TDD | 60 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3263138 | 4 | 121.4660783681 | 31.1506474567 | 94 | 8 | 4 | 23.0 | TDD | 300 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3264351 | 3 | 121.4739577866 | 31.1464690606 | 116 | 10 | 12 | 23.1 | TDD | 149 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.841 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.866 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.985 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.985 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.682 | NREventA3 | measId:2;ServCellPCI:945;Se... |
| 2024-09-20 22:21:37.922 | NRHandoverAttempt | SourcePCI:945;SourceNR-ARFC... |
| 2024-09-20 22:21:37.969 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.984 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.126 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.126 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3215362 | 1 | 83.9366 | 94.3615 | -114.0935 | 5.7974 | 135.3335 | 0.0079 | 0.0133 |
| 2024_09_19 22:00 | 3256019 | 2 | 82.5889 | 88.1265 | -114.7149 | 6.5687 | 153.0403 | 0.0149 | 0.0150 |
| 2024_09_19 22:00 | 3264351 | 3 | 93.5789 | 84.4920 | -116.0344 | 13.4992 | 103.4457 | 0.0118 | 0.0179 |
| 2024_09_19 22:00 | 3263138 | 4 | 82.0729 | 88.1487 | -117.5584 | 12.4355 | 116.3600 | 0.0063 | 0.0120 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413407_E414D559 | 504990 | 60 | -92.6 | 504990 | 149 | -95.7 | 504990 | 539 | -101.0 | 504990 | 300 |
| MR_1774413407_DE82AC1C | 504990 | 60 | -92.3 | 504990 | 149 | -96.1 | 504990 | 539 | -101.6 | 504990 | 300 |
| MR_1774413407_4D0A1730 | 504990 | 60 | -92.7 | 504990 | 149 | -95.7 | 504990 | 539 | -101.0 | 504990 | 300 |
| MR_1774413407_34ED4226 | 504990 | 60 | -90.2 | 504990 | 149 | -96.5 | 504990 | 539 | -98.6 | 504990 | 300 |
| MR_1774413407_BBE19A15 | 504990 | 60 | -90.0 | 504990 | 149 | -98.0 | 504990 | 539 | -99.9 | 504990 | 300 |
| MR_1774413407_ACD22ACD | 504990 | 60 | -88.9 | 504990 | 149 | -97.3 | 504990 | 539 | -99.5 | 504990 | 300 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 667: `5a77887c-ac5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5a77887c-ac5a-41ab-bb0b-343512cc3928` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease A3 Offset threshold for 3228052_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[667] topology](images/train_0667.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228052_4
- `C2`: Add neighbor relationship between 3263809_2 and 3244906_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228052_4
- `C4`: Lift the tilt angle of 3228052_4 by 10 degrees
- `C5`: Press down the tilt angle of 3228052_4 by 10 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244906_1
- `C7`: Lift the tilt angle  of 3244906_1 by 10 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244906_1
- `C9`: Add neighbor relationship between 3228052_4 and 3244906_1
- `C10`: Press down the tilt angle  of 3244906_1 by 10 degrees
- `C11`: Decrease A3 Offset threshold for 3244906_1
- `C12`: Adjust the azimuth of 3228052_4 by 42 degrees
- `C13`: Decrease transmission power for 3228052_4
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Adjust the azimuth of 3244906_1 by 50 degrees
- `C16`: Increase transmission power for 3228052_4
- `C17`: Increase transmission power for 3244906_1
- `C18`: Increase A3 Offset threshold for 3244906_1
- `C19`: Increase A3 Offset threshold for 3228052_4
- `C20`: Check test server and transmission issues
- `C21`: Decrease A3 Offset threshold for 3228052_4 **← 정답**
- `C22`: Decrease transmission power for 3244906_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.151 | MS1 | 121.4656613804 | 31.1446268274 | 526 | 504990 | -77.65 | 15.45 | 328.72 | 0.01 | 2.07 | 1570 |
| 2024-09-20 22:21:32.822 | MS1 | 121.4656623439 | 31.1446182493 | 526 | 504990 | -81.13 | 15.24 | 542.89 | 0.02 | 2.87 | 1582 |
| 2024-09-20 22:21:33.869 | MS1 | 121.4656681751 | 31.1446211065 | 526 | 504990 | -75.26 | 14.13 | 360.95 | 0.18 | 2.11 | 1569 |
| 2024-09-20 22:21:34.675 | MS1 | 121.4656769880 | 31.1446185345 | 526 | 504990 | -86.02 | -1.98 | 51.36 | 0.05 | 1.03 | 1580 |
| 2024-09-20 22:21:35.320 | MS1 | 121.4656685790 | 31.1446259207 | 526 | 504990 | -84.14 | -0.56 | 36.66 | 0.15 | 1.00 | 1569 |
| 2024-09-20 22:21:36.984 | MS1 | 121.4656726175 | 31.1446358884 | 526 | 504990 | -90.09 | -1.80 | 73.44 | 0.14 | 1.31 | 1594 |
| 2024-09-20 22:21:37.460 | MS1 | 121.4656755145 | 31.1446185815 | 526 | 504990 | -84.93 | -2.79 | 51.94 | 0.15 | 1.22 | 1590 |
| 2024-09-20 22:21:38.415 | MS1 | 121.4656740901 | 31.1446257441 | 526 | 504990 | -91.62 | -0.90 | 40.85 | 0.06 | 1.13 | 1571 |
| 2024-09-20 22:21:39.492 | MS1 | 121.4656581309 | 31.1446197998 | 840 | 504990 | -76.84 | 14.49 | 217.72 | 0.09 | 1.13 | 1584 |
| 2024-09-20 22:21:40.308 | MS1 | 121.4656750948 | 31.1446354482 | 840 | 504990 | -81.07 | 17.41 | 546.66 | 0.09 | 2.43 | 1586 |
| 2024-09-20 22:21:41.842 | MS1 | 121.4656626535 | 31.1446216522 | 840 | 504990 | -84.59 | 12.01 | 446.09 | 0.16 | 2.10 | 1589 |
| 2024-09-20 22:21:42.526 | MS1 | 121.4656607870 | 31.1446374231 | 840 | 504990 | -82.94 | 13.29 | 407.21 | 0.08 | 2.21 | 1576 |

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
| 3218777 | 3 | 121.4700424351 | 31.1514128698 | 106 | 14 | 10 | 47.1 | TDD | 222 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3228052 | 4 | 121.4640419804 | 31.1546686022 | 214 | 15 | 1 | 39.5 | TDD | 526 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3244906 | 1 | 121.4650745091 | 31.1456708140 | 270 | 14 | 12 | 46.2 | TDD | 840 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3263809 | 2 | 121.4680835708 | 31.1482089065 | 328 | 11 | 1 | 26.4 | TDD | 608 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.061 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.061 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.755 | NREventA3 | measId:2;ServCellPCI:291;Se... |
| 2024-09-20 22:21:37.995 | NRHandoverAttempt | SourcePCI:291;SourceNR-ARFC... |
| 2024-09-20 22:21:38.026 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.036 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.151 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.151 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244906 | 1 | 18.9599 | 16.5109 | -114.7514 | 16.5919 | 132.9652 | 0.0060 | 0.0194 |
| 2024_09_20 22:00 | 3263809 | 2 | 17.8546 | 17.3054 | -114.5098 | 6.3181 | 130.5878 | 0.0079 | 0.0017 |
| 2024_09_20 22:00 | 3218777 | 3 | 5.7377 | 19.8917 | -115.8146 | 9.8643 | 192.5229 | 0.0146 | 0.0112 |
| 2024_09_20 22:00 | 3228052 | 4 | 12.9896 | 8.4217 | -114.5415 | 11.7244 | 115.5287 | 0.0091 | 0.1842 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416178_AC21769F | 504990 | 840 | -79.2 | 504990 | 526 | -86.7 | 504990 | 608 | -88.2 | 504990 | 222 |
| MR_1774416178_31C58D90 | 504990 | 840 | -80.5 | 504990 | 526 | -84.6 | 504990 | 608 | -88.3 | 504990 | 222 |
| MR_1774416178_6ED4956A | 504990 | 526 | -84.4 | 504990 | 840 | -79.3 | 504990 | 608 | -87.9 | 504990 | 222 |
| MR_1774416178_4C400020 | 504990 | 840 | -80.0 | 504990 | 526 | -84.5 | 504990 | 608 | -88.2 | 504990 | 222 |
| MR_1774416178_26F61FB8 | 504990 | 526 | -86.7 | 504990 | 840 | -80.5 | 504990 | 608 | -88.5 | 504990 | 222 |
| MR_1774416178_7DA53EEF | 504990 | 526 | -87.6 | 504990 | 840 | -81.4 | 504990 | 608 | -84.9 | 504990 | 222 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 668: `c6bc4173-3ab...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c6bc4173-3ab8-47b8-99d7-3b45aa322d2f` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[668] topology](images/train_0668.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272504_1
- `C2`: Adjust the azimuth of 3277997_4 by 50 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Lift the tilt angle of 3277997_4 by 10 degrees
- `C5`: Increase A3 Offset threshold for 3277997_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277997_4
- `C7`: Decrease transmission power for 3277997_4
- `C8`: Adjust the azimuth of 3272504_1 by 50 degrees
- `C9`: Decrease A3 Offset threshold for 3272504_1
- `C10`: Check test server and transmission issues **← 정답**
- `C11`: Increase transmission power for 3277997_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277997_4
- `C13`: Increase A3 Offset threshold for 3272504_1
- `C14`: Decrease transmission power for 3272504_1
- `C15`: Decrease A3 Offset threshold for 3277997_4
- `C16`: Increase transmission power for 3272504_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272504_1
- `C18`: Add neighbor relationship between 3277997_4 and 3272504_1
- `C19`: Press down the tilt angle  of 3272504_1 by 10 degrees
- `C20`: Add neighbor relationship between 3253396_2 and 3272504_1
- `C21`: Lift the tilt angle  of 3272504_1 by 10 degrees
- `C22`: Press down the tilt angle of 3277997_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.701 | MS1 | 121.4656662597 | 31.1446326949 | 963 | 504990 | -86.14 | 16.53 | 599.47 | 0.01 | 2.32 | 1563 |
| 2024-09-20 22:21:32.318 | MS1 | 121.4656688223 | 31.1446343401 | 963 | 504990 | -87.25 | 14.84 | 314.73 | 0.03 | 2.26 | 1596 |
| 2024-09-20 22:21:33.821 | MS1 | 121.4656691463 | 31.1446319483 | 963 | 504990 | -86.71 | 15.31 | 559.13 | 0.03 | 2.22 | 1567 |
| 2024-09-20 22:21:34.168 | MS1 | 121.4656629159 | 31.1446197345 | 963 | 504990 | -90.02 | 17.99 | 49.67 | 0.07 | 2.77 | 415 |
| 2024-09-20 22:21:35.820 | MS1 | 121.4656602822 | 31.1446251130 | 963 | 504990 | -90.81 | 15.28 | 66.95 | 0.02 | 2.92 | 404 |
| 2024-09-20 22:21:36.418 | MS1 | 121.4656626614 | 31.1446286231 | 963 | 504990 | -85.00 | 17.29 | 60.70 | 0.04 | 2.37 | 316 |
| 2024-09-20 22:21:37.139 | MS1 | 121.4656608009 | 31.1446180011 | 963 | 504990 | -90.67 | 9.99 | 72.67 | 0.01 | 2.29 | 414 |
| 2024-09-20 22:21:38.847 | MS1 | 121.4656629299 | 31.1446267750 | 963 | 504990 | -93.39 | 8.85 | 96.17 | 0.15 | 2.97 | 482 |
| 2024-09-20 22:21:39.285 | MS1 | 121.4656595993 | 31.1446246216 | 963 | 504990 | -89.18 | 7.28 | 75.74 | 0.05 | 2.13 | 357 |
| 2024-09-20 22:21:40.257 | MS1 | 121.4656626797 | 31.1446260539 | 963 | 504990 | -93.81 | 8.53 | 338.37 | 0.02 | 2.80 | 1576 |
| 2024-09-20 22:21:41.232 | MS1 | 121.4656594983 | 31.1446342197 | 963 | 504990 | -91.08 | 8.20 | 342.63 | 0.14 | 2.58 | 1571 |
| 2024-09-20 22:21:42.894 | MS1 | 121.4656702364 | 31.1446240397 | 963 | 504990 | -89.64 | 9.91 | 393.18 | 0.19 | 2.59 | 1583 |

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
| 3253396 | 2 | 121.4713144940 | 31.1532945197 | 295 | 12 | 1 | 41.8 | TDD | 867 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3264183 | 3 | 121.4728110470 | 31.1527455127 | 14 | 14 | 4 | 27.3 | TDD | 509 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3272504 | 1 | 121.4736898266 | 31.1535536420 | 308 | 10 | 7 | 44.0 | TDD | 400 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3277997 | 4 | 121.4731483960 | 31.1534469690 | 123 | 13 | 9 | 19.4 | TDD | 963 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.199 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.224 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.331 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.331 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.067 | NREventA3 | measId:2;ServCellPCI:894;Se... |
| 2024-09-20 22:21:38.307 | NRHandoverAttempt | SourcePCI:894;SourceNR-ARFC... |
| 2024-09-20 22:21:38.343 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.358 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.490 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.490 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272504 | 1 | 11.5850 | 6.8768 | -114.0817 | 15.7889 | 150.5806 | 0.0130 | 0.0062 |
| 2024_09_20 22:00 | 3253396 | 2 | 14.6718 | 6.8225 | -117.6150 | 18.5144 | 141.1696 | 0.0048 | 0.0047 |
| 2024_09_20 22:00 | 3264183 | 3 | 5.6696 | 16.6322 | -116.5782 | 19.3769 | 186.8329 | 0.0088 | 0.0164 |
| 2024_09_20 22:00 | 3277997 | 4 | 6.3560 | 14.1877 | -115.6705 | 19.5084 | 106.0198 | 0.0187 | 0.0159 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416859_08FDB5F7 | 504990 | 963 | -88.1 | 504990 | 400 | -98.1 | 504990 | 867 | -99.6 | 504990 | 509 |
| MR_1774416859_3DC36A0F | 504990 | 963 | -90.4 | 504990 | 400 | -98.9 | 504990 | 867 | -99.7 | 504990 | 509 |
| MR_1774416859_94A7B60E | 504990 | 963 | -88.3 | 504990 | 400 | -100.1 | 504990 | 867 | -101.3 | 504990 | 509 |
| MR_1774416859_2E63CE7D | 504990 | 963 | -89.7 | 504990 | 400 | -99.8 | 504990 | 867 | -100.8 | 504990 | 509 |
| MR_1774416859_87D3B79F | 504990 | 963 | -90.2 | 504990 | 400 | -99.4 | 504990 | 867 | -102.0 | 504990 | 509 |
| MR_1774416859_3DFDA567 | 504990 | 963 | -89.6 | 504990 | 400 | -99.2 | 504990 | 867 | -100.9 | 504990 | 509 |
| MR_1774416859_9FF832CE | 504990 | 963 | -90.8 | 504990 | 400 | -98.0 | 504990 | 867 | -99.2 | 504990 | 509 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 669: `c309a0b8-520...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c309a0b8-5200-4504-812b-97085ccca221` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Lift the tilt angle  of 3261731_4 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[669] topology](images/train_0669.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228120_2
- `C2`: Adjust the azimuth of 3261731_4 by 19 degrees
- `C3`: Increase transmission power for 3212447_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212447_1
- `C5`: Adjust the azimuth of 3212447_1 by 6 degrees
- `C6`: Add neighbor relationship between 3212447_1 and 3228120_2
- `C7`: Check test server and transmission issues
- `C8`: Increase A3 Offset threshold for 3212447_1
- `C9`: Lift the tilt angle  of 3261731_4 by 7 degrees **← 정답**
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228120_2
- `C11`: Decrease transmission power for 3212447_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212447_1
- `C13`: Increase transmission power for 3228120_2
- `C14`: Decrease A3 Offset threshold for 3212447_1
- `C15`: Decrease A3 Offset threshold for 3228120_2
- `C16`: Add neighbor relationship between 3261731_4 and 3228120_2
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Press down the tilt angle  of 3261731_4 by 7 degrees
- `C19`: Increase A3 Offset threshold for 3228120_2
- `C20`: Press down the tilt angle of 3212447_1 by 5 degrees
- `C21`: Lift the tilt angle of 3212447_1 by 5 degrees
- `C22`: Decrease transmission power for 3228120_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.362 | MS1 | 121.4656677738 | 31.1446189546 | 344 | 504990 | -87.58 | 14.55 | 436.79 | 0.14 | 2.27 | 1575 |
| 2024-09-20 22:21:32.531 | MS1 | 121.4656673925 | 31.1446308528 | 344 | 504990 | -87.37 | 12.70 | 371.74 | 0.19 | 2.31 | 1600 |
| 2024-09-20 22:21:33.288 | MS1 | 121.4656733045 | 31.1446294432 | 344 | 504990 | -85.51 | 15.19 | 376.15 | 0.01 | 2.22 | 1571 |
| 2024-09-20 22:21:34.330 | MS1 | 121.4656774146 | 31.1446227910 | 344 | 504990 | -87.87 | 16.46 | 98.39 | 0.17 | 2.94 | 1563 |
| 2024-09-20 22:21:35.128 | MS1 | 121.4656722664 | 31.1446293100 | 344 | 504990 | -90.53 | 15.91 | 73.05 | 0.03 | 2.98 | 1571 |
| 2024-09-20 22:21:36.980 | MS1 | 121.4656588566 | 31.1446218023 | 344 | 504990 | -86.82 | 12.46 | 82.02 | 0.19 | 2.42 | 1561 |
| 2024-09-20 22:21:37.679 | MS1 | 121.4656709366 | 31.1446191430 | 344 | 504990 | -90.82 | 12.35 | 93.65 | 0.15 | 2.24 | 1594 |
| 2024-09-20 22:21:38.181 | MS1 | 121.4656651705 | 31.1446231785 | 344 | 504990 | -91.14 | 7.04 | 46.08 | 0.08 | 2.80 | 1592 |
| 2024-09-20 22:21:39.113 | MS1 | 121.4656617308 | 31.1446352390 | 344 | 504990 | -92.87 | 12.79 | 96.90 | 0.10 | 2.99 | 1599 |
| 2024-09-20 22:21:40.744 | MS1 | 121.4656597544 | 31.1446235393 | 344 | 504990 | -89.05 | 10.97 | 594.10 | 0.20 | 2.22 | 1573 |
| 2024-09-20 22:21:41.837 | MS1 | 121.4656646198 | 31.1446275600 | 344 | 504990 | -91.32 | 8.91 | 550.37 | 0.14 | 2.35 | 1583 |
| 2024-09-20 22:21:42.521 | MS1 | 121.4656706211 | 31.1446207469 | 344 | 504990 | -90.51 | 11.30 | 331.59 | 0.04 | 2.70 | 1595 |

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
| 3212447 | 1 | 121.4650585203 | 31.1478838832 | 177 | 0 | 6 | 29.7 | TDD | 344 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3228120 | 2 | 121.4718189924 | 31.1543224183 | 228 | 5 | 0 | 35.2 | TDD | 577 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3261731 | 4 | 121.4738025697 | 31.1526490539 | 299 | 4 | 7 | 30.0 | TDD | 705 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3270192 | 3 | 121.4679556430 | 31.1521692781 | 47 | 8 | 8 | 37.4 | TDD | 259 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.587 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.603 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.737 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.737 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.416 | NREventA3 | measId:2;ServCellPCI:359;Se... |
| 2024-09-20 22:21:38.656 | NRHandoverAttempt | SourcePCI:359;SourceNR-ARFC... |
| 2024-09-20 22:21:38.693 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.705 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.828 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.828 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212447 | 1 | 81.8299 | 88.0230 | -115.3158 | 15.1212 | 106.4002 | 0.0144 | 0.0033 |
| 2024_09_20 22:00 | 3228120 | 2 | 6.1911 | 6.2723 | -114.0399 | 16.1669 | 121.0295 | 0.0112 | 0.0042 |
| 2024_09_20 22:00 | 3270192 | 3 | 13.4388 | 12.7826 | -115.3004 | 18.5836 | 111.8637 | 0.0163 | 0.0194 |
| 2024_09_20 22:00 | 3261731 | 4 | 19.2624 | 8.8826 | -115.8450 | 15.9014 | 188.9321 | 0.0100 | 0.0025 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412882_4EA48BD9 | 504990 | 344 | -89.8 | 504990 | 577 | -93.5 | 504990 | 705 | -95.5 | 504990 | 259 |
| MR_1774412882_381BF7BD | 504990 | 344 | -86.1 | 504990 | 577 | -91.3 | 504990 | 705 | -96.7 | 504990 | 259 |
| MR_1774412882_D3829926 | 504990 | 344 | -86.1 | 504990 | 577 | -91.1 | 504990 | 705 | -96.7 | 504990 | 259 |
| MR_1774412882_0003FEAF | 504990 | 344 | -87.0 | 504990 | 577 | -90.5 | 504990 | 705 | -96.7 | 504990 | 259 |
| MR_1774412882_FF5924C8 | 504990 | 344 | -87.9 | 504990 | 577 | -90.9 | 504990 | 705 | -97.7 | 504990 | 259 |

> *... 2개 열 생략 (전체 14열)*

---
