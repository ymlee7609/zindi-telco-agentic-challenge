# Track A 문제 분석 — train[10]~train[19]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[10] ~ train[19] (10개)

## 목차

1. [문제 10: `19468668-993...`](#10) — multiple-answer, 정답: C3|C12
2. [문제 11: `e3e0a301-7a0...`](#11) — single-answer, 정답: C16
3. [문제 12: `35bc60da-c36...`](#12) — single-answer, 정답: C15
4. [문제 13: `88f1c45d-96a...`](#13) — single-answer, 정답: C15
5. [문제 14: `4cddc91b-aea...`](#14) — single-answer, 정답: C5
6. [문제 15: `d1fc4519-d75...`](#15) — single-answer, 정답: C14
7. [문제 16: `8685551e-2b8...`](#16) — single-answer, 정답: C10
8. [문제 17: `056addfa-6d1...`](#17) — multiple-answer, 정답: C3|C14
9. [문제 18: `e63c2b60-dbf...`](#18) — single-answer, 정답: C12
10. [문제 19: `1382a74f-d5e...`](#19) — single-answer, 정답: C13

---

### 문제 10: `19468668-993...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `19468668-9934-4be1-aa7a-4c8926b50bc0` |
| Tag | **multiple-answer** |
| 정답 | **C3|C12** |
| C3 의미 | Decrease transmission power for 3220643_4 |
| C12 의미 | Press down the tilt angle  of 3220643_4 by 2 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[10] topology](images/train_0010.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3226039_2
- `C2`: Add neighbor relationship between 3265192_3 and 3220643_4
- `C3`: Decrease transmission power for 3220643_4 **← 정답**
- `C4`: Increase A3 Offset threshold for 3226039_2
- `C5`: Press down the tilt angle of 3226039_2 by 3 degrees
- `C6`: Add neighbor relationship between 3226039_2 and 3220643_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220643_4
- `C8`: Lift the tilt angle  of 3220643_4 by 2 degrees
- `C9`: Increase transmission power for 3226039_2
- `C10`: Decrease A3 Offset threshold for 3220643_4
- `C11`: Lift the tilt angle of 3226039_2 by 3 degrees
- `C12`: Press down the tilt angle  of 3220643_4 by 2 degrees **← 정답**
- `C13`: Check test server and transmission issues
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Adjust the azimuth of 3220643_4 by 6 degrees
- `C16`: Adjust the azimuth of 3226039_2 by 41 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226039_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220643_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226039_2
- `C20`: Decrease transmission power for 3226039_2
- `C21`: Increase transmission power for 3220643_4
- `C22`: Increase A3 Offset threshold for 3220643_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.561 | MS1 | 121.4656637596 | 31.1446367685 | 866 | 504990 | -77.92 | 16.74 | 443.59 | 0.10 | 2.29 | 1571 |
| 2024-09-20 22:21:32.248 | MS1 | 121.4656700719 | 31.1446343154 | 866 | 504990 | -82.01 | 14.42 | 461.18 | 0.14 | 2.73 | 1567 |
| 2024-09-20 22:21:33.501 | MS1 | 121.4656674110 | 31.1446246346 | 866 | 504990 | -78.95 | 13.37 | 429.62 | 0.19 | 2.79 | 1568 |
| 2024-09-20 22:21:34.506 | MS1 | 121.4656706987 | 31.1446339352 | 866 | 504990 | -88.85 | 2.36 | 67.67 | 0.20 | 1.19 | 1592 |
| 2024-09-20 22:21:35.768 | MS1 | 121.4656683179 | 31.1446357749 | 866 | 504990 | -86.36 | 2.84 | 79.95 | 0.11 | 1.48 | 1586 |
| 2024-09-20 22:21:36.404 | MS1 | 121.4656717131 | 31.1446214932 | 866 | 504990 | -87.82 | 2.88 | 53.97 | 0.08 | 1.28 | 1560 |
| 2024-09-20 22:21:37.531 | MS1 | 121.4656737598 | 31.1446359920 | 866 | 504990 | -86.17 | 3.48 | 68.01 | 0.13 | 1.16 | 1583 |
| 2024-09-20 22:21:38.134 | MS1 | 121.4656723891 | 31.1446276511 | 866 | 504990 | -85.30 | 0.43 | 82.48 | 0.00 | 1.35 | 1594 |
| 2024-09-20 22:21:39.939 | MS1 | 121.4656703848 | 31.1446221260 | 866 | 504990 | -93.47 | 3.40 | 68.84 | 0.14 | 1.30 | 1584 |
| 2024-09-20 22:21:40.430 | MS1 | 121.4656612088 | 31.1446332133 | 866 | 504990 | -76.68 | 12.68 | 584.93 | 0.14 | 2.89 | 1583 |
| 2024-09-20 22:21:41.789 | MS1 | 121.4656626021 | 31.1446345859 | 866 | 504990 | -80.30 | 12.83 | 554.14 | 0.05 | 2.43 | 1593 |
| 2024-09-20 22:21:42.717 | MS1 | 121.4656777673 | 31.1446371221 | 866 | 504990 | -80.45 | 16.59 | 457.10 | 0.10 | 2.96 | 1593 |

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
| 3220643 | 4 | 121.4717013861 | 31.1486829503 | 226 | 0 | 8 | 27.5 | TDD | 213 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3226039 | 2 | 121.4747470784 | 31.1452125669 | 307 | 0 | 7 | 44.6 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3252648 | 1 | 121.4682646841 | 31.1490137079 | 207 | 5 | 11 | 37.9 | TDD | 96 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3265192 | 3 | 121.4655276585 | 31.1450937366 | 291 | 11 | 9 | 44.0 | TDD | 116 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.467 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.489 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.593 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.593 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252648 | 1 | 18.9288 | 18.7191 | -115.5852 | 15.2223 | 138.0561 | 0.0125 | 0.0023 |
| 2024_09_20 22:00 | 3226039 | 2 | 12.2483 | 7.8930 | -108.0155 | 17.9807 | 168.0475 | 0.0174 | 0.0063 |
| 2024_09_20 22:00 | 3265192 | 3 | 15.0975 | 14.7090 | -116.1691 | 13.3738 | 186.2087 | 0.0149 | 0.0104 |
| 2024_09_20 22:00 | 3220643 | 4 | 7.4947 | 17.0868 | -116.6309 | 7.4230 | 199.8291 | 0.0021 | 0.0007 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417095_26C55200 | 504990 | 213 | -90.3 | 504990 | 866 | -84.7 | 504990 | 116 | -86.8 | 504990 | 96 |
| MR_1774417095_69B4DC6F | 504990 | 866 | -87.8 | 504990 | 213 | -85.4 | 504990 | 116 | -86.6 | 504990 | 96 |
| MR_1774417095_1A2A5ADE | 504990 | 866 | -89.1 | 504990 | 213 | -85.7 | 504990 | 116 | -87.2 | 504990 | 96 |
| MR_1774417095_4DF2F170 | 504990 | 866 | -89.5 | 504990 | 213 | -85.5 | 504990 | 116 | -88.7 | 504990 | 96 |
| MR_1774417095_B317CB78 | 504990 | 213 | -87.9 | 504990 | 866 | -84.4 | 504990 | 116 | -88.0 | 504990 | 96 |
| MR_1774417095_E35F7737 | 504990 | 213 | -88.2 | 504990 | 866 | -85.9 | 504990 | 116 | -88.6 | 504990 | 96 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 11: `e3e0a301-7a0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e3e0a301-7a05-4b56-884c-4853b56c3c51` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[11] topology](images/train_0011.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3276591_4 by 1 degrees
- `C2`: Add neighbor relationship between 3276591_4 and 3238318_1
- `C3`: Decrease A3 Offset threshold for 3276591_4
- `C4`: Increase transmission power for 3276591_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276591_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238318_1
- `C7`: Lift the tilt angle of 3276591_4 by 1 degrees
- `C8`: Decrease transmission power for 3238318_1
- `C9`: Increase A3 Offset threshold for 3276591_4
- `C10`: Adjust the azimuth of 3238318_1 by 7 degrees
- `C11`: Decrease A3 Offset threshold for 3238318_1
- `C12`: Check test server and transmission issues
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276591_4
- `C14`: Lift the tilt angle  of 3238318_1 by 9 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238318_1
- `C16`: Insufficient data; more data is needed for judgment. **← 정답**
- `C17`: Increase A3 Offset threshold for 3238318_1
- `C18`: Decrease transmission power for 3276591_4
- `C19`: Increase transmission power for 3238318_1
- `C20`: Add neighbor relationship between 3268975_3 and 3238318_1
- `C21`: Adjust the azimuth of 3276591_4 by 50 degrees
- `C22`: Press down the tilt angle  of 3238318_1 by 9 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.760 | MS1 | 121.4656615957 | 31.1446201267 | 421 | 504990 | -88.63 | 17.51 | 556.60 | 0.17 | 2.56 | 1594 |
| 2024-09-20 22:21:32.751 | MS1 | 121.4656675647 | 31.1446219976 | 421 | 504990 | -86.71 | 16.29 | 576.38 | 0.02 | 2.13 | 1586 |
| 2024-09-20 22:21:33.337 | MS1 | 121.4656686279 | 31.1446188013 | 421 | 504990 | -88.98 | 16.81 | 325.00 | 0.14 | 2.29 | 1588 |
| 2024-09-20 22:21:34.841 | MS1 | 121.4656671779 | 31.1446284237 | 421 | 504990 | -87.52 | 13.27 | 98.82 | 0.12 | 2.75 | 1575 |
| 2024-09-20 22:21:35.376 | MS1 | 121.4656646459 | 31.1446234317 | 421 | 504990 | -87.98 | 13.59 | 62.00 | 0.09 | 2.64 | 1572 |
| 2024-09-20 22:21:36.130 | MS1 | 121.4656678615 | 31.1446322113 | 421 | 504990 | -87.11 | 17.91 | 81.27 | 0.02 | 2.01 | 1576 |
| 2024-09-20 22:21:37.706 | MS1 | 121.4656594962 | 31.1446325843 | 421 | 504990 | -89.02 | 8.36 | 83.19 | 0.16 | 2.02 | 1580 |
| 2024-09-20 22:21:38.493 | MS1 | 121.4656583397 | 31.1446226978 | 421 | 504990 | -93.02 | 7.33 | 55.54 | 0.16 | 2.50 | 1576 |
| 2024-09-20 22:21:39.409 | MS1 | 121.4656621481 | 31.1446263409 | 421 | 504990 | -93.61 | 9.62 | 67.22 | 0.07 | 2.30 | 1580 |
| 2024-09-20 22:21:40.175 | MS1 | 121.4656624687 | 31.1446204945 | 421 | 504990 | -93.67 | 9.81 | 484.91 | 0.15 | 2.18 | 1584 |
| 2024-09-20 22:21:41.117 | MS1 | 121.4656648762 | 31.1446300897 | 421 | 504990 | -93.72 | 11.23 | 430.76 | 0.02 | 2.77 | 1599 |
| 2024-09-20 22:21:42.905 | MS1 | 121.4656636038 | 31.1446197250 | 421 | 504990 | -91.31 | 7.20 | 405.55 | 0.19 | 2.64 | 1584 |

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
| 3238318 | 1 | 121.4724958402 | 31.1460696299 | 263 | 7 | 2 | 17.8 | TDD | 648 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3268975 | 3 | 121.4680394249 | 31.1474975264 | 336 | 15 | 5 | 40.6 | TDD | 832 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3272348 | 2 | 121.4714896020 | 31.1497957207 | 94 | 4 | 7 | 18.3 | TDD | 777 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3276591 | 4 | 121.4698222209 | 31.1525898205 | 277 | 0 | 6 | 23.3 | TDD | 421 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.539 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.562 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.687 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.687 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.438 | NREventA3 | measId:2;ServCellPCI:852;Se... |
| 2024-09-20 22:21:38.678 | NRHandoverAttempt | SourcePCI:852;SourceNR-ARFC... |
| 2024-09-20 22:21:38.721 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.735 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.884 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.884 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3238318 | 1 | 79.0020 | 88.9713 | -116.7613 | 13.6429 | 112.9315 | 0.0122 | 0.0099 |
| 2024_09_19 22:00 | 3272348 | 2 | 93.4731 | 88.5339 | -114.3915 | 19.0315 | 85.0518 | 0.0158 | 0.0134 |
| 2024_09_19 22:00 | 3268975 | 3 | 90.8038 | 81.4904 | -114.4869 | 9.0290 | 101.4067 | 0.0033 | 0.0036 |
| 2024_09_19 22:00 | 3276591 | 4 | 91.3536 | 83.3859 | -115.1630 | 8.0609 | 164.6143 | 0.0113 | 0.0064 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416088_8C1BC09F | 504990 | 421 | -88.2 | 504990 | 648 | -90.8 | 504990 | 832 | -99.7 | 504990 | 777 |
| MR_1774416088_671ADA68 | 504990 | 421 | -87.4 | 504990 | 648 | -88.9 | 504990 | 832 | -101.3 | 504990 | 777 |
| MR_1774416088_9C697163 | 504990 | 421 | -86.8 | 504990 | 648 | -91.4 | 504990 | 832 | -101.2 | 504990 | 777 |
| MR_1774416088_EBD133F5 | 504990 | 421 | -88.7 | 504990 | 648 | -92.1 | 504990 | 832 | -101.7 | 504990 | 777 |
| MR_1774416088_3D489AF0 | 504990 | 421 | -88.3 | 504990 | 648 | -91.6 | 504990 | 832 | -102.4 | 504990 | 777 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 12: `35bc60da-c36...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `35bc60da-c36b-41db-bf7c-613ba9cb35a3` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[12] topology](images/train_0012.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3235478_2 and 3250578_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235478_2
- `C3`: Add neighbor relationship between 3274133_1 and 3250578_4
- `C4`: Decrease A3 Offset threshold for 3235478_2
- `C5`: Lift the tilt angle  of 3250578_4 by 10 degrees
- `C6`: Increase transmission power for 3235478_2
- `C7`: Decrease transmission power for 3250578_4
- `C8`: Decrease A3 Offset threshold for 3250578_4
- `C9`: Increase A3 Offset threshold for 3235478_2
- `C10`: Press down the tilt angle of 3235478_2 by 10 degrees
- `C11`: Increase transmission power for 3250578_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250578_4
- `C13`: Lift the tilt angle of 3235478_2 by 10 degrees
- `C14`: Decrease transmission power for 3235478_2
- `C15`: Check test server and transmission issues **← 정답**
- `C16`: Press down the tilt angle  of 3250578_4 by 10 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235478_2
- `C18`: Adjust the azimuth of 3235478_2 by 37 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250578_4
- `C21`: Increase A3 Offset threshold for 3250578_4
- `C22`: Adjust the azimuth of 3250578_4 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.105 | MS1 | 121.4656724921 | 31.1446334705 | 749 | 504990 | -89.78 | 13.76 | 426.78 | 0.02 | 2.41 | 1567 |
| 2024-09-20 22:21:32.572 | MS1 | 121.4656668575 | 31.1446293465 | 749 | 504990 | -87.38 | 16.91 | 536.36 | 0.00 | 2.27 | 1582 |
| 2024-09-20 22:21:33.309 | MS1 | 121.4656597698 | 31.1446246702 | 749 | 504990 | -89.68 | 14.84 | 400.24 | 0.16 | 2.91 | 1599 |
| 2024-09-20 22:21:34.884 | MS1 | 121.4656712629 | 31.1446192795 | 749 | 504990 | -91.49 | 14.21 | 74.59 | 0.17 | 2.68 | 497 |
| 2024-09-20 22:21:35.346 | MS1 | 121.4656638807 | 31.1446319588 | 749 | 504990 | -87.10 | 17.86 | 60.56 | 0.06 | 2.98 | 411 |
| 2024-09-20 22:21:36.453 | MS1 | 121.4656776994 | 31.1446297339 | 749 | 504990 | -89.93 | 14.68 | 82.59 | 0.08 | 2.52 | 482 |
| 2024-09-20 22:21:37.465 | MS1 | 121.4656772123 | 31.1446226946 | 749 | 504990 | -91.27 | 9.08 | 81.76 | 0.11 | 2.84 | 467 |
| 2024-09-20 22:21:38.735 | MS1 | 121.4656722530 | 31.1446191292 | 749 | 504990 | -89.16 | 12.97 | 102.38 | 0.20 | 2.10 | 327 |
| 2024-09-20 22:21:39.305 | MS1 | 121.4656767185 | 31.1446377622 | 749 | 504990 | -91.69 | 8.87 | 75.29 | 0.11 | 2.57 | 344 |
| 2024-09-20 22:21:40.274 | MS1 | 121.4656741624 | 31.1446325329 | 749 | 504990 | -92.17 | 9.64 | 510.05 | 0.09 | 2.23 | 1571 |
| 2024-09-20 22:21:41.427 | MS1 | 121.4656625686 | 31.1446330637 | 749 | 504990 | -93.79 | 7.50 | 399.89 | 0.02 | 2.48 | 1573 |
| 2024-09-20 22:21:42.677 | MS1 | 121.4656757379 | 31.1446234649 | 749 | 504990 | -93.67 | 9.96 | 509.46 | 0.09 | 2.74 | 1596 |

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
| 3235478 | 2 | 121.4682452565 | 31.1491197184 | 169 | 5 | 2 | 47.7 | TDD | 749 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3250578 | 4 | 121.4694214300 | 31.1532742088 | 194 | 9 | 9 | 33.6 | TDD | 925 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3261393 | 3 | 121.4729242992 | 31.1518470160 | 253 | 5 | 0 | 46.6 | TDD | 718 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3274133 | 1 | 121.4658152784 | 31.1539957179 | 263 | 12 | 4 | 27.9 | TDD | 898 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.362 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.380 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.493 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.493 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.258 | NREventA3 | measId:2;ServCellPCI:372;Se... |
| 2024-09-20 22:21:38.498 | NRHandoverAttempt | SourcePCI:372;SourceNR-ARFC... |
| 2024-09-20 22:21:38.531 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.542 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.684 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.684 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274133 | 1 | 9.7008 | 11.4550 | -116.7581 | 18.1605 | 188.9375 | 0.0080 | 0.0149 |
| 2024_09_20 22:00 | 3235478 | 2 | 15.5582 | 17.6784 | -115.0104 | 18.8704 | 170.2079 | 0.0132 | 0.0000 |
| 2024_09_20 22:00 | 3261393 | 3 | 17.6591 | 9.9055 | -114.6588 | 15.1027 | 99.8911 | 0.0117 | 0.0183 |
| 2024_09_20 22:00 | 3250578 | 4 | 13.5381 | 7.9456 | -117.2765 | 15.6992 | 82.7905 | 0.0166 | 0.0060 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416647_7E0F114B | 504990 | 749 | -90.8 | 504990 | 925 | -96.4 | 504990 | 898 | -98.4 | 504990 | 718 |
| MR_1774416647_33D7BB7A | 504990 | 749 | -92.0 | 504990 | 925 | -94.5 | 504990 | 898 | -99.8 | 504990 | 718 |
| MR_1774416647_55BE5A82 | 504990 | 749 | -90.2 | 504990 | 925 | -96.8 | 504990 | 898 | -99.7 | 504990 | 718 |
| MR_1774416647_F94E8C1B | 504990 | 749 | -93.0 | 504990 | 925 | -97.4 | 504990 | 898 | -97.8 | 504990 | 718 |
| MR_1774416647_06F1B4FD | 504990 | 749 | -91.6 | 504990 | 925 | -95.4 | 504990 | 898 | -97.1 | 504990 | 718 |
| MR_1774416647_BDF58AE4 | 504990 | 749 | -89.6 | 504990 | 925 | -98.0 | 504990 | 898 | -97.3 | 504990 | 718 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 13: `88f1c45d-96a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `88f1c45d-96a4-444e-ba6b-66658ec4ad48` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3236632_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[13] topology](images/train_0013.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3246647_2
- `C2`: Increase A3 Offset threshold for 3246647_2
- `C3`: Press down the tilt angle of 3236632_3 by 4 degrees
- `C4`: Adjust the azimuth of 3246647_2 by 50 degrees
- `C5`: Lift the tilt angle  of 3246647_2 by 10 degrees
- `C6`: Increase A3 Offset threshold for 3236632_3
- `C7`: Decrease transmission power for 3236632_3
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246647_2
- `C10`: Adjust the azimuth of 3236632_3 by 36 degrees
- `C11`: Check test server and transmission issues
- `C12`: Decrease A3 Offset threshold for 3246647_2
- `C13`: Add neighbor relationship between 3265850_1 and 3246647_2
- `C14`: Add neighbor relationship between 3236632_3 and 3246647_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236632_3 **← 정답**
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246647_2
- `C17`: Increase transmission power for 3236632_3
- `C18`: Increase transmission power for 3246647_2
- `C19`: Press down the tilt angle  of 3246647_2 by 10 degrees
- `C20`: Decrease A3 Offset threshold for 3236632_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236632_3
- `C22`: Lift the tilt angle of 3236632_3 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.350 | MS1 | 121.4656736476 | 31.1446276716 | 566 | 504990 | -91.91 | 16.43 | 469.72 | 0.16 | 2.55 | 1577 |
| 2024-09-20 22:21:32.837 | MS1 | 121.4656601216 | 31.1446239342 | 566 | 504990 | -90.13 | 14.03 | 350.04 | 0.13 | 2.00 | 1576 |
| 2024-09-20 22:21:33.294 | MS1 | 121.4656757375 | 31.1446207401 | 566 | 504990 | -88.24 | 16.75 | 551.02 | 0.02 | 2.25 | 1589 |
| 2024-09-20 22:21:34.522 | MS1 | 121.4656703150 | 31.1446209816 | 566 | 504990 | -90.45 | 14.40 | 94.65 | 0.61 | 2.74 | 619 |
| 2024-09-20 22:21:35.748 | MS1 | 121.4656742989 | 31.1446233389 | 566 | 504990 | -90.97 | 14.32 | 64.82 | 0.70 | 2.36 | 589 |
| 2024-09-20 22:21:36.736 | MS1 | 121.4656663853 | 31.1446324508 | 566 | 504990 | -87.43 | 14.60 | 89.00 | 0.66 | 2.04 | 547 |
| 2024-09-20 22:21:37.881 | MS1 | 121.4656686749 | 31.1446326286 | 566 | 504990 | -89.48 | 7.95 | 56.22 | 0.67 | 2.85 | 510 |
| 2024-09-20 22:21:38.416 | MS1 | 121.4656698901 | 31.1446194121 | 566 | 504990 | -89.61 | 12.13 | 79.41 | 0.70 | 2.30 | 582 |
| 2024-09-20 22:21:39.913 | MS1 | 121.4656676680 | 31.1446316843 | 566 | 504990 | -91.47 | 10.70 | 87.82 | 0.57 | 2.72 | 655 |
| 2024-09-20 22:21:40.109 | MS1 | 121.4656619940 | 31.1446259595 | 566 | 504990 | -90.03 | 9.74 | 462.45 | 0.01 | 2.30 | 1572 |
| 2024-09-20 22:21:41.288 | MS1 | 121.4656660032 | 31.1446291087 | 566 | 504990 | -91.62 | 10.32 | 368.67 | 0.07 | 2.51 | 1598 |
| 2024-09-20 22:21:42.437 | MS1 | 121.4656607341 | 31.1446184369 | 566 | 504990 | -91.60 | 11.77 | 376.34 | 0.01 | 2.14 | 1600 |

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
| 3236632 | 3 | 121.4681228036 | 31.1490499599 | 241 | 1 | 6 | 27.6 | TDD | 566 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3241234 | 4 | 121.4683350296 | 31.1466303773 | 251 | 9 | 1 | 17.7 | TDD | 751 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3246647 | 2 | 121.4668796053 | 31.1454872207 | 60 | 8 | 9 | 41.3 | TDD | 99 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3265850 | 1 | 121.4701009269 | 31.1481067327 | 206 | 14 | 10 | 36.0 | TDD | 175 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.440 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.460 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.579 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.579 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.259 | NREventA3 | measId:2;ServCellPCI:214;Se... |
| 2024-09-20 22:21:38.499 | NRHandoverAttempt | SourcePCI:214;SourceNR-ARFC... |
| 2024-09-20 22:21:38.541 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.553 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.667 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.667 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265850 | 1 | 19.7725 | 9.6457 | -115.7650 | 18.2391 | 105.8175 | 0.0106 | 0.0165 |
| 2024_09_20 22:00 | 3246647 | 2 | 5.2280 | 16.0162 | -117.2218 | 7.3588 | 121.3786 | 0.0020 | 0.0160 |
| 2024_09_20 22:00 | 3236632 | 3 | 12.4972 | 17.2860 | -115.9706 | 8.5064 | 108.4824 | 0.0066 | 0.0129 |
| 2024_09_20 22:00 | 3241234 | 4 | 17.9430 | 5.1709 | -115.8596 | 16.7714 | 137.4923 | 0.0011 | 0.0009 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415185_D01E878C | 504990 | 566 | -89.5 | 504990 | 99 | -97.9 | 504990 | 175 | -102.9 | 504990 | 751 |
| MR_1774415185_1BA56408 | 504990 | 566 | -92.2 | 504990 | 99 | -96.0 | 504990 | 175 | -102.3 | 504990 | 751 |
| MR_1774415185_89049C10 | 504990 | 566 | -91.7 | 504990 | 99 | -95.6 | 504990 | 175 | -99.3 | 504990 | 751 |
| MR_1774415185_9AD2D832 | 504990 | 566 | -92.2 | 504990 | 99 | -94.8 | 504990 | 175 | -100.5 | 504990 | 751 |
| MR_1774415185_15741D18 | 504990 | 566 | -90.0 | 504990 | 99 | -97.3 | 504990 | 175 | -102.7 | 504990 | 751 |
| MR_1774415185_53531988 | 504990 | 566 | -91.1 | 504990 | 99 | -95.0 | 504990 | 175 | -101.1 | 504990 | 751 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 14: `4cddc91b-aea...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4cddc91b-aead-4afb-9602-8e097267648a` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Lift the tilt angle  of 3224809_4 by 8 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[14] topology](images/train_0014.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3220393_2 and 3221037_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220393_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220393_2
- `C4`: Decrease A3 Offset threshold for 3220393_2
- `C5`: Lift the tilt angle  of 3224809_4 by 8 degrees **← 정답**
- `C6`: Decrease transmission power for 3221037_1
- `C7`: Decrease transmission power for 3220393_2
- `C8`: Increase transmission power for 3220393_2
- `C9`: Adjust the azimuth of 3220393_2 by 0 degrees
- `C10`: Press down the tilt angle  of 3224809_4 by 8 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221037_1
- `C12`: Add neighbor relationship between 3224809_4 and 3221037_1
- `C13`: Increase A3 Offset threshold for 3220393_2
- `C14`: Check test server and transmission issues
- `C15`: Press down the tilt angle of 3220393_2 by 5 degrees
- `C16`: Increase A3 Offset threshold for 3221037_1
- `C17`: Adjust the azimuth of 3224809_4 by 50 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221037_1
- `C19`: Decrease A3 Offset threshold for 3221037_1
- `C20`: Increase transmission power for 3221037_1
- `C21`: Lift the tilt angle of 3220393_2 by 5 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.660 | MS1 | 121.4656654833 | 31.1446241622 | 317 | 504990 | -86.18 | 14.04 | 390.12 | 0.00 | 2.99 | 1589 |
| 2024-09-20 22:21:32.812 | MS1 | 121.4656741935 | 31.1446357618 | 317 | 504990 | -85.48 | 16.67 | 532.65 | 0.12 | 2.97 | 1573 |
| 2024-09-20 22:21:33.632 | MS1 | 121.4656599298 | 31.1446297944 | 317 | 504990 | -90.56 | 13.69 | 471.12 | 0.05 | 2.53 | 1592 |
| 2024-09-20 22:21:34.973 | MS1 | 121.4656593411 | 31.1446336280 | 317 | 504990 | -85.89 | 17.86 | 85.02 | 0.18 | 2.82 | 1596 |
| 2024-09-20 22:21:35.683 | MS1 | 121.4656704469 | 31.1446320189 | 317 | 504990 | -89.88 | 13.56 | 62.98 | 0.05 | 2.69 | 1597 |
| 2024-09-20 22:21:36.998 | MS1 | 121.4656632825 | 31.1446226087 | 317 | 504990 | -87.75 | 16.91 | 66.44 | 0.13 | 2.29 | 1572 |
| 2024-09-20 22:21:37.746 | MS1 | 121.4656746550 | 31.1446227033 | 317 | 504990 | -92.08 | 11.49 | 91.13 | 0.08 | 2.61 | 1577 |
| 2024-09-20 22:21:38.305 | MS1 | 121.4656705866 | 31.1446234151 | 317 | 504990 | -89.71 | 12.61 | 90.09 | 0.02 | 2.78 | 1585 |
| 2024-09-20 22:21:39.591 | MS1 | 121.4656751645 | 31.1446256352 | 317 | 504990 | -89.21 | 7.09 | 54.44 | 0.14 | 2.44 | 1595 |
| 2024-09-20 22:21:40.398 | MS1 | 121.4656708364 | 31.1446276498 | 317 | 504990 | -92.37 | 10.88 | 495.57 | 0.10 | 2.13 | 1578 |
| 2024-09-20 22:21:41.464 | MS1 | 121.4656715191 | 31.1446359763 | 317 | 504990 | -90.34 | 9.27 | 527.92 | 0.02 | 2.45 | 1574 |
| 2024-09-20 22:21:42.325 | MS1 | 121.4656604042 | 31.1446193042 | 317 | 504990 | -89.34 | 8.15 | 294.30 | 0.07 | 2.87 | 1580 |

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
| 3213313 | 3 | 121.4720116841 | 31.1538049777 | 328 | 8 | 9 | 45.1 | TDD | 853 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3220393 | 2 | 121.4749939042 | 31.1454956293 | 264 | 3 | 9 | 29.4 | TDD | 317 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3221037 | 1 | 121.4640336048 | 31.1523527929 | 71 | 6 | 0 | 30.7 | TDD | 210 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3224809 | 4 | 121.4650746134 | 31.1440386484 | 177 | 13 | 0 | 15.8 | TDD | 742 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.743 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.765 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.899 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.899 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.625 | NREventA3 | measId:2;ServCellPCI:672;Se... |
| 2024-09-20 22:21:37.865 | NRHandoverAttempt | SourcePCI:672;SourceNR-ARFC... |
| 2024-09-20 22:21:37.906 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.919 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.028 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.028 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221037 | 1 | 7.0248 | 11.6514 | -114.9876 | 7.1594 | 121.8718 | 0.0165 | 0.0199 |
| 2024_09_20 22:00 | 3220393 | 2 | 85.5357 | 84.6564 | -117.8592 | 8.7151 | 160.1997 | 0.0098 | 0.0085 |
| 2024_09_20 22:00 | 3213313 | 3 | 10.4278 | 18.3643 | -115.7742 | 19.5015 | 103.1458 | 0.0108 | 0.0037 |
| 2024_09_20 22:00 | 3224809 | 4 | 14.9167 | 17.7838 | -114.5812 | 9.5897 | 107.6339 | 0.0004 | 0.0114 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415862_B9D83511 | 504990 | 317 | -87.8 | 504990 | 210 | -88.2 | 504990 | 742 | -99.2 | 504990 | 853 |
| MR_1774415862_1B4E2606 | 504990 | 317 | -87.3 | 504990 | 210 | -87.5 | 504990 | 742 | -99.8 | 504990 | 853 |
| MR_1774415862_AD1BF818 | 504990 | 317 | -86.4 | 504990 | 210 | -88.1 | 504990 | 742 | -100.6 | 504990 | 853 |
| MR_1774415862_916A9F13 | 504990 | 317 | -84.2 | 504990 | 210 | -87.4 | 504990 | 742 | -98.6 | 504990 | 853 |
| MR_1774415862_FC54C4D4 | 504990 | 317 | -86.6 | 504990 | 210 | -86.0 | 504990 | 742 | -100.7 | 504990 | 853 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 15: `d1fc4519-d75...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d1fc4519-d75e-4d63-918d-f145984031e3` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225965_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[15] topology](images/train_0015.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262458_3
- `C2`: Press down the tilt angle  of 3262458_3 by 3 degrees
- `C3`: Decrease transmission power for 3225965_6
- `C4`: Adjust the azimuth of 3262458_3 by 4 degrees
- `C5`: Lift the tilt angle of 3225965_6 by 4 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262458_3
- `C8`: Decrease A3 Offset threshold for 3262458_3
- `C9`: Adjust the azimuth of 3225965_6 by 31 degrees
- `C10`: Increase transmission power for 3225965_6
- `C11`: Lift the tilt angle  of 3262458_3 by 3 degrees
- `C12`: Press down the tilt angle of 3225965_6 by 4 degrees
- `C13`: Check test server and transmission issues
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225965_6 **← 정답**
- `C15`: Add neighbor relationship between 3214684_8 and 3262458_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225965_6
- `C17`: Increase A3 Offset threshold for 3225965_6
- `C18`: Decrease A3 Offset threshold for 3225965_6
- `C19`: Increase A3 Offset threshold for 3262458_3
- `C20`: Decrease transmission power for 3262458_3
- `C21`: Add neighbor relationship between 3225965_6 and 3262458_3
- `C22`: Increase transmission power for 3262458_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.749 | MS1 | 121.4656710991 | 31.1446227863 | 125 | 504990 | -93.72 | 13.75 | 561.76 | 0.13 | 2.62 | 1600 |
| 2024-09-20 22:21:32.987 | MS1 | 121.4656600395 | 31.1446309891 | 796 | 504990 | -95.33 | 11.90 | 320.79 | 0.19 | 2.72 | 1581 |
| 2024-09-20 22:21:33.718 | MS1 | 121.4656609398 | 31.1446262809 | 333 | 504990 | -94.55 | 12.09 | 371.24 | 0.12 | 2.23 | 1579 |
| 2024-09-20 22:21:34.135 | MS1 | 121.4656708618 | 31.1446212766 | 65 | 152650 | -93.74 | 7.73 | 95.53 | 0.08 | 1.87 | 986 |
| 2024-09-20 22:21:35.649 | MS1 | 121.4656647326 | 31.1446349163 | 277 | 152650 | -90.49 | 3.40 | 77.64 | 0.19 | 2.00 | 910 |
| 2024-09-20 22:21:36.894 | MS1 | 121.4656626840 | 31.1446195246 | 740 | 152650 | -93.02 | 3.72 | 94.24 | 0.05 | 1.70 | 932 |
| 2024-09-20 22:21:37.459 | MS1 | 121.4656659271 | 31.1446257463 | 660 | 152650 | -93.64 | 5.24 | 82.89 | 0.06 | 1.97 | 915 |
| 2024-09-20 22:21:38.904 | MS1 | 121.4656605070 | 31.1446190041 | 65 | 152650 | -92.41 | 4.76 | 49.37 | 0.13 | 1.65 | 980 |
| 2024-09-20 22:21:39.670 | MS1 | 121.4656649580 | 31.1446299990 | 277 | 152650 | -88.82 | 2.42 | 104.52 | 0.11 | 1.66 | 967 |
| 2024-09-20 22:21:40.143 | MS1 | 121.4656615476 | 31.1446266656 | 740 | 152650 | -91.31 | 4.76 | 102.56 | 0.11 | 2.18 | 1591 |
| 2024-09-20 22:21:41.916 | MS1 | 121.4656732661 | 31.1446322428 | 660 | 152650 | -87.75 | 5.44 | 71.97 | 0.12 | 2.32 | 1599 |
| 2024-09-20 22:21:42.345 | MS1 | 121.4656675395 | 31.1446246531 | 65 | 152650 | -96.32 | 3.51 | 80.40 | 0.13 | 2.13 | 1584 |

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
| 3214684 | 8 | 121.4745129728 | 31.1472297015 | 288 | 3 | 7 | 11.7 | FDD | 740 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3217337 | 1 | 121.4724606215 | 31.1481791154 | 307 | 12 | 6 | 15.7 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3221437 | 10 | 121.4720549932 | 31.1559657361 | 316 | 0 | 2 | 13.9 | FDD | 147 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3225955 | 5 | 121.4644794218 | 31.1490595265 | 329 | 5 | 5 | 10.4 | TDD | 892 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3225965 | 6 | 121.4720231219 | 31.1444227529 | 303 | 4 | 9 | 2.7 | TDD | 125 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3229924 | 4 | 121.4741969784 | 31.1442701959 | 246 | 12 | 7 | 8.6 | TDD | 333 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3256384 | 13 | 121.4745453914 | 31.1455657173 | 167 | 7 | 3 | 4.2 | FDD | 278 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3259243 | 11 | 121.4641630354 | 31.1551410756 | 263 | 11 | 5 | 21.3 | FDD | 660 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3260132 | 7 | 121.4714983029 | 31.1519338251 | 125 | 2 | 12 | 5.4 | FDD | 65 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3262458 | 3 | 121.4712489024 | 31.1510154154 | 213 | 2 | 6 | 15.8 | TDD | 102 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3267696 | 2 | 121.4676597104 | 31.1544950725 | 168 | 12 | 0 | 7.6 | TDD | 796 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3274737 | 9 | 121.4748546859 | 31.1443049051 | 320 | 14 | 11 | 4.7 | FDD | 904 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3277588 | 12 | 121.4642051038 | 31.1453444406 | 227 | 0 | 9 | 14.1 | FDD | 277 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |

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
| 2024-09-20 22:21:31.654 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.679 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.780 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.780 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.475 | NREventA2 | measId:1;ServCellPCI:941;Se... |
| 2024-09-20 22:21:35.612 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.865 | NREventA5 | measId:3;ServCellPCI:941;Se... |
| 2024-09-20 22:21:35.932 | NRHandoverAttempt | SourcePCI:941;SourceNR-ARFC... |
| 2024-09-20 22:21:35.960 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.971 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.081 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.081 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217337 | 1 | 8.1433 | 11.3689 | -114.9860 | 17.8046 | 159.9134 | 0.0028 | 0.0093 |
| 2024_09_20 22:00 | 3267696 | 2 | 17.6525 | 17.7598 | -115.7527 | 5.3879 | 144.9791 | 0.0104 | 0.0035 |
| 2024_09_20 22:00 | 3262458 | 3 | 15.6775 | 12.7914 | -114.1783 | 7.3100 | 99.5917 | 0.0014 | 0.0020 |
| 2024_09_20 22:00 | 3229924 | 4 | 15.7392 | 11.3945 | -117.2185 | 16.3043 | 154.5131 | 0.0042 | 0.0030 |
| 2024_09_20 22:00 | 3225955 | 5 | 18.1880 | 6.1988 | -116.4873 | 9.1215 | 181.0238 | 0.0191 | 0.0110 |
| 2024_09_20 22:00 | 3225965 | 6 | 17.2910 | 13.8754 | -114.7185 | 13.2863 | 101.2994 | 0.0118 | 0.0162 |
| 2024_09_20 22:00 | 3260132 | 7 | 6.5065 | 17.8503 | -115.1976 | 4.9558 | 24.1227 | 0.0178 | 0.0042 |
| 2024_09_20 22:00 | 3214684 | 8 | 15.2186 | 18.2286 | -117.4394 | 3.6345 | 56.8256 | 0.0162 | 0.0019 |
| 2024_09_20 22:00 | 3274737 | 9 | 11.8280 | 5.8185 | -117.8931 | 4.0448 | 54.0115 | 0.0085 | 0.0092 |
| 2024_09_20 22:00 | 3221437 | 10 | 12.4574 | 7.6706 | -114.0432 | 4.2510 | 38.3371 | 0.0133 | 0.0050 |
| 2024_09_20 22:00 | 3259243 | 11 | 13.2230 | 17.2905 | -114.7846 | 4.7954 | 38.3209 | 0.0103 | 0.0194 |
| 2024_09_20 22:00 | 3277588 | 12 | 14.8748 | 19.8683 | -117.7464 | 3.7844 | 58.8658 | 0.0060 | 0.0002 |
| 2024_09_20 22:00 | 3256384 | 13 | 6.0001 | 17.9233 | -115.3401 | 3.2178 | 56.5753 | 0.0139 | 0.0121 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414585_3CB4CB08 | 152650 | 65 | -94.9 | 152650 | 904 | -97.5 | 152650 | 278 | -102.8 | 152650 | 147 |
| MR_1774414585_6E83D124 | 152650 | 65 | -93.5 | 152650 | 904 | -96.0 | 152650 | 278 | -103.7 | 152650 | 147 |
| MR_1774414585_9B1F6AA5 | 504990 | 333 | -93.0 | 504990 | 102 | -91.3 | 504990 | 892 | -92.7 | 504990 | 866 |
| MR_1774414585_63A4B9B0 | 152650 | 65 | -92.1 | 152650 | 904 | -97.9 | 152650 | 278 | -103.2 | 152650 | 147 |
| MR_1774414585_AEE601C7 | 152650 | 65 | -95.2 | 152650 | 904 | -97.9 | 152650 | 278 | -101.0 | 152650 | 147 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 16: `8685551e-2b8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8685551e-2b89-485c-b430-ba8d8f154dc6` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3260865_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[16] topology](images/train_0016.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3224444_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260865_1
- `C3`: Adjust the azimuth of 3224444_3 by 50 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Increase transmission power for 3260865_1
- `C6`: Decrease transmission power for 3224444_3
- `C7`: Press down the tilt angle  of 3224444_3 by 6 degrees
- `C8`: Decrease transmission power for 3260865_1
- `C9`: Decrease A3 Offset threshold for 3260865_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260865_1 **← 정답**
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224444_3
- `C12`: Increase A3 Offset threshold for 3224444_3
- `C13`: Add neighbor relationship between 3276536_2 and 3224444_3
- `C14`: Adjust the azimuth of 3260865_1 by 43 degrees
- `C15`: Decrease A3 Offset threshold for 3224444_3
- `C16`: Lift the tilt angle  of 3224444_3 by 6 degrees
- `C17`: Lift the tilt angle of 3260865_1 by 3 degrees
- `C18`: Add neighbor relationship between 3260865_1 and 3224444_3
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle of 3260865_1 by 3 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224444_3
- `C22`: Increase A3 Offset threshold for 3260865_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.508 | MS1 | 121.4656714324 | 31.1446315351 | 614 | 504990 | -90.61 | 16.49 | 433.91 | 0.06 | 2.90 | 1577 |
| 2024-09-20 22:21:32.350 | MS1 | 121.4656700353 | 31.1446374920 | 614 | 504990 | -87.13 | 17.31 | 484.54 | 0.05 | 2.54 | 1596 |
| 2024-09-20 22:21:33.398 | MS1 | 121.4656620500 | 31.1446199739 | 614 | 504990 | -85.65 | 13.43 | 495.27 | 0.13 | 2.13 | 1567 |
| 2024-09-20 22:21:34.806 | MS1 | 121.4656639030 | 31.1446319439 | 614 | 504990 | -85.44 | 15.88 | 78.54 | 0.59 | 2.00 | 501 |
| 2024-09-20 22:21:35.507 | MS1 | 121.4656754695 | 31.1446278910 | 614 | 504990 | -91.19 | 13.41 | 77.90 | 0.61 | 2.60 | 585 |
| 2024-09-20 22:21:36.918 | MS1 | 121.4656743273 | 31.1446220671 | 614 | 504990 | -90.06 | 14.50 | 87.32 | 0.62 | 2.90 | 626 |
| 2024-09-20 22:21:37.119 | MS1 | 121.4656765045 | 31.1446307987 | 614 | 504990 | -89.14 | 7.18 | 79.69 | 0.68 | 2.80 | 552 |
| 2024-09-20 22:21:38.886 | MS1 | 121.4656595329 | 31.1446266608 | 614 | 504990 | -90.86 | 7.06 | 63.19 | 0.60 | 2.62 | 513 |
| 2024-09-20 22:21:39.283 | MS1 | 121.4656759251 | 31.1446232163 | 614 | 504990 | -93.14 | 10.16 | 91.23 | 0.70 | 2.73 | 657 |
| 2024-09-20 22:21:40.344 | MS1 | 121.4656767684 | 31.1446317462 | 614 | 504990 | -93.95 | 8.33 | 427.46 | 0.16 | 2.55 | 1597 |
| 2024-09-20 22:21:41.341 | MS1 | 121.4656692251 | 31.1446357200 | 614 | 504990 | -92.92 | 7.96 | 404.35 | 0.19 | 2.61 | 1578 |
| 2024-09-20 22:21:42.905 | MS1 | 121.4656680549 | 31.1446270538 | 614 | 504990 | -92.49 | 11.24 | 320.50 | 0.16 | 2.38 | 1589 |

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
| 3224444 | 3 | 121.4640065926 | 31.1499412785 | 354 | 4 | 2 | 22.0 | TDD | 446 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3240662 | 4 | 121.4665893352 | 31.1454898718 | 88 | 14 | 5 | 24.5 | TDD | 415 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3260865 | 1 | 121.4714064553 | 31.1516608229 | 172 | 2 | 8 | 20.2 | TDD | 614 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3276536 | 2 | 121.4690124971 | 31.1466953450 | 348 | 10 | 11 | 32.6 | TDD | 261 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.524 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.547 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.649 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.649 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.340 | NREventA3 | measId:2;ServCellPCI:456;Se... |
| 2024-09-20 22:21:38.580 | NRHandoverAttempt | SourcePCI:456;SourceNR-ARFC... |
| 2024-09-20 22:21:38.613 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.626 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.747 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.747 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260865 | 1 | 9.9942 | 5.8779 | -115.1302 | 18.9242 | 94.4723 | 0.0031 | 0.0102 |
| 2024_09_20 22:00 | 3276536 | 2 | 14.0042 | 11.4359 | -115.0594 | 9.5399 | 199.1011 | 0.0152 | 0.0015 |
| 2024_09_20 22:00 | 3224444 | 3 | 5.6935 | 16.4083 | -115.7308 | 17.1493 | 94.1265 | 0.0078 | 0.0051 |
| 2024_09_20 22:00 | 3240662 | 4 | 11.2437 | 18.7021 | -114.8607 | 7.0405 | 175.2425 | 0.0059 | 0.0000 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412698_42156FE4 | 504990 | 614 | -85.2 | 504990 | 446 | -91.0 | 504990 | 261 | -94.7 | 504990 | 415 |
| MR_1774412698_CED35660 | 504990 | 614 | -85.7 | 504990 | 446 | -89.4 | 504990 | 261 | -91.5 | 504990 | 415 |
| MR_1774412698_8C02CAC0 | 504990 | 614 | -83.8 | 504990 | 446 | -90.5 | 504990 | 261 | -94.0 | 504990 | 415 |
| MR_1774412698_06495116 | 504990 | 614 | -83.8 | 504990 | 446 | -88.5 | 504990 | 261 | -94.8 | 504990 | 415 |
| MR_1774412698_19BE2B87 | 504990 | 614 | -87.4 | 504990 | 446 | -89.0 | 504990 | 261 | -93.9 | 504990 | 415 |
| MR_1774412698_55EE2C89 | 504990 | 614 | -86.5 | 504990 | 446 | -87.7 | 504990 | 261 | -94.6 | 504990 | 415 |
| MR_1774412698_3494AB20 | 504990 | 614 | -84.1 | 504990 | 446 | -89.0 | 504990 | 261 | -93.6 | 504990 | 415 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 17: `056addfa-6d1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `056addfa-6d17-4c13-a5cc-faabe3d44b80` |
| Tag | **multiple-answer** |
| 정답 | **C3|C14** |
| C3 의미 | Adjust the azimuth of 3273494_1 by 50 degrees |
| C14 의미 | Increase transmission power for 3273494_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[17] topology](images/train_0017.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3231269_4 by 4 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273494_1
- `C3`: Adjust the azimuth of 3273494_1 by 50 degrees **← 정답**
- `C4`: Decrease transmission power for 3231269_4
- `C5`: Increase A3 Offset threshold for 3231269_4
- `C6`: Check test server and transmission issues
- `C7`: Decrease transmission power for 3273494_1
- `C8`: Lift the tilt angle  of 3231269_4 by 4 degrees
- `C9`: Press down the tilt angle of 3273494_1 by 5 degrees
- `C10`: Increase transmission power for 3231269_4
- `C11`: Add neighbor relationship between 3273494_1 and 3231269_4
- `C12`: Lift the tilt angle of 3273494_1 by 5 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231269_4
- `C14`: Increase transmission power for 3273494_1 **← 정답**
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273494_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231269_4
- `C17`: Decrease A3 Offset threshold for 3273494_1
- `C18`: Adjust the azimuth of 3231269_4 by 41 degrees
- `C19`: Increase A3 Offset threshold for 3273494_1
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease A3 Offset threshold for 3231269_4
- `C22`: Add neighbor relationship between 3268508_2 and 3231269_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.904 | MS1 | 121.4656675800 | 31.1446219917 | 827 | 504990 | -86.42 | 14.22 | 303.97 | 0.01 | 2.12 | 1562 |
| 2024-09-20 22:21:32.616 | MS1 | 121.4656686131 | 31.1446303340 | 827 | 504990 | -86.80 | 15.87 | 573.21 | 0.10 | 2.59 | 1590 |
| 2024-09-20 22:21:33.471 | MS1 | 121.4656769347 | 31.1446243489 | 827 | 504990 | -93.27 | 12.41 | 388.03 | 0.00 | 2.42 | 1574 |
| 2024-09-20 22:21:34.610 | MS1 | 121.4656644257 | 31.1446187496 | 827 | 504990 | -108.80 | 1.56 | 32.72 | 0.08 | 1.38 | 1570 |
| 2024-09-20 22:21:35.192 | MS1 | 121.4656670632 | 31.1446278299 | 827 | 504990 | -100.19 | 1.19 | 87.80 | 0.11 | 1.12 | 1575 |
| 2024-09-20 22:21:36.111 | MS1 | 121.4656657840 | 31.1446251585 | 827 | 504990 | -108.66 | -1.42 | 40.74 | 0.04 | 1.13 | 1571 |
| 2024-09-20 22:21:37.409 | MS1 | 121.4656732764 | 31.1446207516 | 827 | 504990 | -104.48 | 0.28 | 31.09 | 0.16 | 1.29 | 1582 |
| 2024-09-20 22:21:38.703 | MS1 | 121.4656771221 | 31.1446208317 | 827 | 504990 | -103.64 | -1.23 | 20.14 | 0.04 | 1.37 | 1564 |
| 2024-09-20 22:21:39.478 | MS1 | 121.4656765222 | 31.1446296266 | 827 | 504990 | -104.94 | -1.15 | 71.49 | 0.08 | 1.45 | 1584 |
| 2024-09-20 22:21:40.531 | MS1 | 121.4656610189 | 31.1446352488 | 827 | 504990 | -86.80 | 14.47 | 305.39 | 0.18 | 2.31 | 1563 |
| 2024-09-20 22:21:41.129 | MS1 | 121.4656603442 | 31.1446323785 | 827 | 504990 | -91.29 | 13.97 | 576.16 | 0.13 | 2.30 | 1570 |
| 2024-09-20 22:21:42.616 | MS1 | 121.4656710880 | 31.1446328997 | 827 | 504990 | -90.82 | 16.00 | 453.28 | 0.12 | 2.70 | 1563 |

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
| 3213593 | 3 | 121.4704340892 | 31.1524394871 | 174 | 0 | 8 | 25.0 | TDD | 1004 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3231269 | 4 | 121.4668322752 | 31.1541955849 | 145 | 2 | 4 | 44.5 | TDD | 507 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3268508 | 2 | 121.4730065830 | 31.1545570263 | 118 | 9 | 7 | 22.4 | TDD | 132 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3273494 | 1 | 121.4748246431 | 31.1510234638 | 307 | 4 | 6 | 23.2 | TDD | 827 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.980 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.005 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.114 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.114 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.379 | NREventA2 | measId:1;ServCellPCI:760;Se... |
| 2024-09-20 22:21:34.488 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273494 | 1 | 6.8823 | 5.9324 | -117.1811 | 6.7581 | 154.2257 | 0.1685 | 0.0021 |
| 2024_09_20 22:00 | 3268508 | 2 | 8.6796 | 13.8638 | -115.3107 | 7.5473 | 115.7321 | 0.0055 | 0.0192 |
| 2024_09_20 22:00 | 3213593 | 3 | 14.6562 | 12.9257 | -116.4888 | 18.2539 | 191.3165 | 0.0151 | 0.0043 |
| 2024_09_20 22:00 | 3231269 | 4 | 17.1189 | 12.3424 | -114.3026 | 5.3005 | 119.6163 | 0.0023 | 0.0054 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416194_03EE1531 | 504990 | 827 | -109.0 | 504990 | 507 | -111.0 | 504990 | 132 | -118.8 | 504990 | 1004 |
| MR_1774416194_4881D418 | 504990 | 827 | -108.4 | 504990 | 507 | -112.9 | 504990 | 132 | -119.2 | 504990 | 1004 |
| MR_1774416194_4AA0F9C4 | 504990 | 827 | -108.7 | 504990 | 507 | -113.0 | 504990 | 132 | -119.8 | 504990 | 1004 |
| MR_1774416194_B09391C2 | 504990 | 827 | -107.5 | 504990 | 507 | -111.1 | 504990 | 132 | -118.1 | 504990 | 1004 |
| MR_1774416194_60E349F3 | 504990 | 827 | -107.9 | 504990 | 507 | -113.2 | 504990 | 132 | -118.0 | 504990 | 1004 |
| MR_1774416194_E7B26E41 | 504990 | 827 | -109.9 | 504990 | 507 | -112.3 | 504990 | 132 | -118.6 | 504990 | 1004 |
| MR_1774416194_06F8AFE2 | 504990 | 827 | -110.2 | 504990 | 507 | -112.3 | 504990 | 132 | -120.7 | 504990 | 1004 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 18: `e63c2b60-dbf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e63c2b60-dbfa-4f5e-8eb2-2ba0ded5a814` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273949_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[18] topology](images/train_0018.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3273949_6
- `C2`: Decrease A3 Offset threshold for 3265590_1
- `C3`: Lift the tilt angle of 3273949_6 by 3 degrees
- `C4`: Decrease transmission power for 3273949_6
- `C5`: Adjust the azimuth of 3265590_1 by 49 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265590_1
- `C7`: Lift the tilt angle  of 3265590_1 by 4 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273949_6
- `C9`: Increase transmission power for 3265590_1
- `C10`: Increase transmission power for 3273949_6
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265590_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273949_6 **← 정답**
- `C13`: Increase A3 Offset threshold for 3265590_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Add neighbor relationship between 3241239_13 and 3265590_1
- `C16`: Add neighbor relationship between 3273949_6 and 3265590_1
- `C17`: Decrease transmission power for 3265590_1
- `C18`: Adjust the azimuth of 3273949_6 by 36 degrees
- `C19`: Increase A3 Offset threshold for 3273949_6
- `C20`: Press down the tilt angle of 3273949_6 by 3 degrees
- `C21`: Press down the tilt angle  of 3265590_1 by 4 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.707 | MS1 | 121.4656628580 | 31.1446372938 | 542 | 504990 | -95.48 | 11.54 | 588.58 | 0.14 | 3.00 | 1572 |
| 2024-09-20 22:21:32.945 | MS1 | 121.4656689564 | 31.1446238824 | 409 | 504990 | -93.55 | 13.18 | 429.42 | 0.19 | 2.75 | 1576 |
| 2024-09-20 22:21:33.489 | MS1 | 121.4656693808 | 31.1446267609 | 411 | 504990 | -95.65 | 12.21 | 393.47 | 0.19 | 2.86 | 1561 |
| 2024-09-20 22:21:34.563 | MS1 | 121.4656740420 | 31.1446184616 | 278 | 152650 | -93.66 | 7.08 | 75.74 | 0.19 | 1.56 | 944 |
| 2024-09-20 22:21:35.984 | MS1 | 121.4656775612 | 31.1446259501 | 904 | 152650 | -89.49 | 2.70 | 96.67 | 0.10 | 1.74 | 900 |
| 2024-09-20 22:21:36.324 | MS1 | 121.4656779455 | 31.1446205815 | 958 | 152650 | -88.24 | 7.23 | 75.63 | 0.13 | 1.66 | 914 |
| 2024-09-20 22:21:37.238 | MS1 | 121.4656666254 | 31.1446294342 | 592 | 152650 | -90.08 | 7.30 | 58.90 | 0.00 | 1.85 | 979 |
| 2024-09-20 22:21:38.759 | MS1 | 121.4656638721 | 31.1446314827 | 278 | 152650 | -90.84 | 2.94 | 90.70 | 0.12 | 1.90 | 924 |
| 2024-09-20 22:21:39.137 | MS1 | 121.4656611064 | 31.1446379419 | 904 | 152650 | -88.23 | 5.26 | 60.93 | 0.20 | 1.67 | 979 |
| 2024-09-20 22:21:40.577 | MS1 | 121.4656598884 | 31.1446277987 | 958 | 152650 | -93.91 | 4.86 | 68.18 | 0.10 | 2.33 | 1577 |
| 2024-09-20 22:21:41.508 | MS1 | 121.4656759863 | 31.1446345262 | 592 | 152650 | -88.66 | 4.61 | 65.90 | 0.18 | 2.74 | 1569 |
| 2024-09-20 22:21:42.783 | MS1 | 121.4656670275 | 31.1446373811 | 278 | 152650 | -94.10 | 7.82 | 69.96 | 0.03 | 2.85 | 1567 |

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
| 3226855 | 5 | 121.4715336974 | 31.1533153698 | 168 | 5 | 8 | 21.8 | TDD | 445 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3228504 | 11 | 121.4647305684 | 31.1481030703 | 70 | 11 | 8 | 13.0 | FDD | 278 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3229920 | 10 | 121.4695458514 | 31.1505753870 | 219 | 12 | 3 | 27.9 | FDD | 592 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3234883 | 2 | 121.4661768878 | 31.1507082936 | 112 | 4 | 0 | 5.8 | TDD | 791 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3237270 | 4 | 121.4657814254 | 31.1551240499 | 243 | 6 | 3 | 14.2 | TDD | 411 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3241239 | 13 | 121.4710423046 | 31.1488364356 | 10 | 7 | 9 | 5.4 | FDD | 958 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3244494 | 3 | 121.4650662985 | 31.1458940079 | 75 | 4 | 4 | 24.8 | TDD | 409 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3256736 | 9 | 121.4733396380 | 31.1483223027 | 330 | 15 | 12 | 6.4 | FDD | 41 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3256861 | 12 | 121.4653254470 | 31.1496418663 | 96 | 6 | 2 | 10.8 | FDD | 346 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3265590 | 1 | 121.4697376521 | 31.1481523891 | 176 | 2 | 0 | 17.1 | TDD | 554 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3273949 | 6 | 121.4718320043 | 31.1515199466 | 253 | 3 | 12 | 8.4 | TDD | 542 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3276177 | 7 | 121.4736140560 | 31.1552621641 | 10 | 5 | 10 | 12.0 | FDD | 227 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3278954 | 8 | 121.4674164961 | 31.1516547403 | 142 | 9 | 2 | 15.2 | FDD | 904 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |

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
| 2024-09-20 22:21:30.866 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.886 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.003 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.003 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.698 | NREventA2 | measId:1;ServCellPCI:703;Se... |
| 2024-09-20 22:21:34.827 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.072 | NREventA5 | measId:3;ServCellPCI:703;Se... |
| 2024-09-20 22:21:35.108 | NRHandoverAttempt | SourcePCI:703;SourceNR-ARFC... |
| 2024-09-20 22:21:35.132 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.143 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.271 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.271 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265590 | 1 | 12.0968 | 6.9289 | -117.4738 | 11.1403 | 187.9716 | 0.0039 | 0.0125 |
| 2024_09_20 22:00 | 3234883 | 2 | 12.1210 | 13.5529 | -115.3343 | 9.4974 | 106.6821 | 0.0023 | 0.0139 |
| 2024_09_20 22:00 | 3244494 | 3 | 13.1638 | 18.7269 | -114.8482 | 12.9630 | 168.6609 | 0.0006 | 0.0065 |
| 2024_09_20 22:00 | 3237270 | 4 | 6.5245 | 10.2497 | -115.9979 | 10.5250 | 160.0438 | 0.0055 | 0.0189 |
| 2024_09_20 22:00 | 3226855 | 5 | 19.4381 | 17.5711 | -115.7387 | 13.8387 | 84.6849 | 0.0072 | 0.0112 |
| 2024_09_20 22:00 | 3273949 | 6 | 13.0365 | 5.9719 | -117.5219 | 13.5826 | 145.4791 | 0.0045 | 0.0025 |
| 2024_09_20 22:00 | 3276177 | 7 | 8.4977 | 18.0804 | -115.1362 | 4.2439 | 33.3784 | 0.0155 | 0.0073 |
| 2024_09_20 22:00 | 3278954 | 8 | 19.5930 | 7.6449 | -115.7188 | 3.4305 | 31.2687 | 0.0092 | 0.0019 |
| 2024_09_20 22:00 | 3256736 | 9 | 16.3937 | 15.0326 | -115.2619 | 3.4892 | 49.4152 | 0.0069 | 0.0092 |
| 2024_09_20 22:00 | 3229920 | 10 | 6.1184 | 16.6963 | -117.5628 | 4.8564 | 55.8715 | 0.0117 | 0.0027 |
| 2024_09_20 22:00 | 3228504 | 11 | 5.1943 | 15.7696 | -116.3085 | 4.7276 | 29.5681 | 0.0022 | 0.0016 |
| 2024_09_20 22:00 | 3256861 | 12 | 16.6908 | 5.3618 | -117.7943 | 4.1332 | 48.3188 | 0.0038 | 0.0163 |
| 2024_09_20 22:00 | 3241239 | 13 | 13.8111 | 14.8787 | -117.4914 | 3.6811 | 43.5907 | 0.0061 | 0.0145 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413719_4566CF5E | 152650 | 278 | -93.5 | 152650 | 227 | -100.4 | 152650 | 41 | -101.7 | 152650 | 346 |
| MR_1774413719_80AE1ECE | 504990 | 411 | -96.2 | 504990 | 554 | -93.6 | 504990 | 791 | -98.9 | 504990 | 445 |
| MR_1774413719_D5A6B37A | 504990 | 411 | -94.5 | 504990 | 554 | -92.3 | 504990 | 791 | -99.1 | 504990 | 445 |
| MR_1774413719_6717BD10 | 152650 | 278 | -93.8 | 152650 | 227 | -100.4 | 152650 | 41 | -101.3 | 152650 | 346 |
| MR_1774413719_9B762253 | 152650 | 278 | -92.3 | 152650 | 227 | -99.1 | 152650 | 41 | -101.9 | 152650 | 346 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 19: `1382a74f-d5e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1382a74f-d5e4-40fa-afe5-e704104c59e1` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[19] topology](images/train_0019.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239117_4
- `C2`: Check test server and transmission issues
- `C3`: Decrease transmission power for 3265249_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265249_1
- `C5`: Adjust the azimuth of 3265249_1 by 50 degrees
- `C6`: Add neighbor relationship between 3238900_2 and 3239117_4
- `C7`: Press down the tilt angle  of 3239117_4 by 10 degrees
- `C8`: Increase transmission power for 3239117_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265249_1
- `C10`: Lift the tilt angle  of 3239117_4 by 10 degrees
- `C11`: Decrease A3 Offset threshold for 3239117_4
- `C12`: Press down the tilt angle of 3265249_1 by 10 degrees
- `C13`: Insufficient data; more data is needed for judgment. **← 정답**
- `C14`: Increase A3 Offset threshold for 3265249_1
- `C15`: Decrease transmission power for 3239117_4
- `C16`: Increase A3 Offset threshold for 3239117_4
- `C17`: Adjust the azimuth of 3239117_4 by 50 degrees
- `C18`: Decrease A3 Offset threshold for 3265249_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239117_4
- `C20`: Lift the tilt angle of 3265249_1 by 10 degrees
- `C21`: Add neighbor relationship between 3265249_1 and 3239117_4
- `C22`: Increase transmission power for 3265249_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.950 | MS1 | 121.4656753207 | 31.1446310613 | 183 | 504990 | -86.48 | 14.02 | 567.41 | 0.09 | 2.63 | 1564 |
| 2024-09-20 22:21:32.306 | MS1 | 121.4656657627 | 31.1446209203 | 183 | 504990 | -91.83 | 16.60 | 361.96 | 0.18 | 2.97 | 1590 |
| 2024-09-20 22:21:33.489 | MS1 | 121.4656615223 | 31.1446307150 | 183 | 504990 | -87.91 | 12.29 | 540.44 | 0.03 | 2.58 | 1594 |
| 2024-09-20 22:21:34.312 | MS1 | 121.4656721242 | 31.1446194708 | 183 | 504990 | -90.20 | 14.92 | 70.98 | 0.16 | 2.43 | 1600 |
| 2024-09-20 22:21:35.871 | MS1 | 121.4656761285 | 31.1446362282 | 183 | 504990 | -87.42 | 12.37 | 55.99 | 0.07 | 2.62 | 1582 |
| 2024-09-20 22:21:36.333 | MS1 | 121.4656656499 | 31.1446204442 | 183 | 504990 | -88.82 | 14.33 | 57.12 | 0.09 | 2.58 | 1562 |
| 2024-09-20 22:21:37.579 | MS1 | 121.4656603789 | 31.1446321068 | 183 | 504990 | -93.81 | 11.25 | 92.08 | 0.13 | 2.35 | 1596 |
| 2024-09-20 22:21:38.867 | MS1 | 121.4656671129 | 31.1446187930 | 183 | 504990 | -89.50 | 8.60 | 94.48 | 0.20 | 2.06 | 1562 |
| 2024-09-20 22:21:39.962 | MS1 | 121.4656594329 | 31.1446224377 | 183 | 504990 | -91.70 | 10.17 | 41.51 | 0.12 | 2.85 | 1596 |
| 2024-09-20 22:21:40.979 | MS1 | 121.4656702329 | 31.1446321739 | 183 | 504990 | -90.99 | 11.84 | 589.66 | 0.11 | 2.96 | 1579 |
| 2024-09-20 22:21:41.961 | MS1 | 121.4656659835 | 31.1446288697 | 183 | 504990 | -93.16 | 12.78 | 376.91 | 0.00 | 2.61 | 1579 |
| 2024-09-20 22:21:42.963 | MS1 | 121.4656762438 | 31.1446192253 | 183 | 504990 | -91.23 | 8.94 | 382.07 | 0.18 | 2.49 | 1576 |

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
| 3238900 | 2 | 121.4678757976 | 31.1527580688 | 327 | 6 | 9 | 39.4 | TDD | 691 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3239117 | 4 | 121.4730795117 | 31.1474856720 | 119 | 12 | 1 | 33.0 | TDD | 623 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3265249 | 1 | 121.4739126784 | 31.1483559617 | 328 | 13 | 3 | 17.2 | TDD | 183 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3267564 | 3 | 121.4707264402 | 31.1518055693 | 278 | 7 | 4 | 20.7 | TDD | 46 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.183 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.204 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.349 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.349 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.026 | NREventA3 | measId:2;ServCellPCI:612;Se... |
| 2024-09-20 22:21:38.266 | NRHandoverAttempt | SourcePCI:612;SourceNR-ARFC... |
| 2024-09-20 22:21:38.304 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.319 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.433 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.433 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3265249 | 1 | 79.1310 | 89.9215 | -114.3598 | 17.5550 | 96.2764 | 0.0072 | 0.0161 |
| 2024_09_19 22:00 | 3238900 | 2 | 84.6698 | 82.0123 | -116.0256 | 7.1057 | 110.5516 | 0.0041 | 0.0153 |
| 2024_09_19 22:00 | 3267564 | 3 | 79.3883 | 79.0428 | -116.5628 | 12.2851 | 83.0797 | 0.0074 | 0.0089 |
| 2024_09_19 22:00 | 3239117 | 4 | 85.3959 | 89.3696 | -115.6533 | 19.8516 | 85.9704 | 0.0129 | 0.0167 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414076_BA72B283 | 504990 | 183 | -90.8 | 504990 | 623 | -96.3 | 504990 | 691 | -105.3 | 504990 | 46 |
| MR_1774414076_78A754B0 | 504990 | 183 | -91.7 | 504990 | 623 | -98.6 | 504990 | 691 | -102.8 | 504990 | 46 |
| MR_1774414076_4B63537E | 504990 | 183 | -91.3 | 504990 | 623 | -98.6 | 504990 | 691 | -104.5 | 504990 | 46 |
| MR_1774414076_2264596A | 504990 | 183 | -89.5 | 504990 | 623 | -98.6 | 504990 | 691 | -103.7 | 504990 | 46 |
| MR_1774414076_56068194 | 504990 | 183 | -88.6 | 504990 | 623 | -97.6 | 504990 | 691 | -106.3 | 504990 | 46 |
| MR_1774414076_131BEC7C | 504990 | 183 | -90.6 | 504990 | 623 | -95.8 | 504990 | 691 | -104.6 | 504990 | 46 |

> *... 2개 열 생략 (전체 14열)*

---
