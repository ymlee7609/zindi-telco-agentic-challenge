# Track A 문제 분석 — train[160]~train[169]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[160] ~ train[169] (10개)

## 목차

1. [문제 160: `aef92a22-bc1...`](#160) — multiple-answer, 정답: C13|C19
2. [문제 161: `7fdcabdf-d7b...`](#161) — single-answer, 정답: C13
3. [문제 162: `db8dfecf-6d4...`](#162) — single-answer, 정답: C3
4. [문제 163: `6f97dc5e-a33...`](#163) — multiple-answer, 정답: C15|C20
5. [문제 164: `7555f9df-398...`](#164) — single-answer, 정답: C14
6. [문제 165: `2e2611ba-a7e...`](#165) — single-answer, 정답: C20
7. [문제 166: `e4f02195-e1d...`](#166) — single-answer, 정답: C22
8. [문제 167: `5799cccd-553...`](#167) — single-answer, 정답: C16
9. [문제 168: `a209bd11-149...`](#168) — multiple-answer, 정답: C9|C15
10. [문제 169: `b08cd826-2b3...`](#169) — single-answer, 정답: C8

---

### 문제 160: `aef92a22-bc1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `aef92a22-bc1f-4a57-b905-6cbd8b8518b1` |
| Tag | **multiple-answer** |
| 정답 | **C13|C19** |
| C13 의미 | Increase transmission power for 3225184_3 |
| C19 의미 | Adjust the azimuth of 3225184_3 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[160] topology](images/train_0160.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3279288_2 and 3249231_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225184_3
- `C3`: Increase transmission power for 3249231_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249231_1
- `C5`: Lift the tilt angle  of 3249231_1 by 4 degrees
- `C6`: Add neighbor relationship between 3225184_3 and 3249231_1
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Press down the tilt angle of 3225184_3 by 10 degrees
- `C9`: Decrease transmission power for 3225184_3
- `C10`: Decrease transmission power for 3249231_1
- `C11`: Increase A3 Offset threshold for 3249231_1
- `C12`: Decrease A3 Offset threshold for 3249231_1
- `C13`: Increase transmission power for 3225184_3 **← 정답**
- `C14`: Increase A3 Offset threshold for 3225184_3
- `C15`: Decrease A3 Offset threshold for 3225184_3
- `C16`: Check test server and transmission issues
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225184_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249231_1
- `C19`: Adjust the azimuth of 3225184_3 by 50 degrees **← 정답**
- `C20`: Press down the tilt angle  of 3249231_1 by 4 degrees
- `C21`: Lift the tilt angle of 3225184_3 by 10 degrees
- `C22`: Adjust the azimuth of 3249231_1 by 35 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.403 | MS1 | 121.4656628305 | 31.1446187043 | 845 | 504990 | -89.87 | 17.79 | 382.75 | 0.00 | 2.64 | 1593 |
| 2024-09-20 22:21:32.218 | MS1 | 121.4656659615 | 31.1446220197 | 845 | 504990 | -86.14 | 12.80 | 444.09 | 0.11 | 2.47 | 1593 |
| 2024-09-20 22:21:33.598 | MS1 | 121.4656741811 | 31.1446302431 | 845 | 504990 | -86.20 | 15.03 | 409.22 | 0.10 | 2.54 | 1587 |
| 2024-09-20 22:21:34.118 | MS1 | 121.4656725063 | 31.1446346960 | 845 | 504990 | -108.07 | 1.49 | 77.27 | 0.03 | 1.23 | 1591 |
| 2024-09-20 22:21:35.152 | MS1 | 121.4656595850 | 31.1446310580 | 845 | 504990 | -109.01 | -0.24 | 27.76 | 0.03 | 1.41 | 1572 |
| 2024-09-20 22:21:36.665 | MS1 | 121.4656659175 | 31.1446260424 | 845 | 504990 | -107.15 | -1.45 | 64.27 | 0.05 | 1.45 | 1572 |
| 2024-09-20 22:21:37.859 | MS1 | 121.4656718693 | 31.1446341333 | 845 | 504990 | -100.48 | -1.10 | 17.81 | 0.18 | 1.24 | 1587 |
| 2024-09-20 22:21:38.717 | MS1 | 121.4656671300 | 31.1446292317 | 845 | 504990 | -102.65 | -0.15 | 74.25 | 0.15 | 1.26 | 1564 |
| 2024-09-20 22:21:39.545 | MS1 | 121.4656768377 | 31.1446222484 | 845 | 504990 | -102.39 | -1.32 | 28.49 | 0.07 | 1.32 | 1577 |
| 2024-09-20 22:21:40.764 | MS1 | 121.4656666271 | 31.1446249265 | 845 | 504990 | -92.03 | 12.09 | 331.21 | 0.19 | 2.63 | 1569 |
| 2024-09-20 22:21:41.425 | MS1 | 121.4656626275 | 31.1446367297 | 845 | 504990 | -86.91 | 16.14 | 577.37 | 0.16 | 2.17 | 1569 |
| 2024-09-20 22:21:42.472 | MS1 | 121.4656606430 | 31.1446260205 | 845 | 504990 | -88.24 | 17.98 | 457.97 | 0.07 | 2.54 | 1581 |

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
| 3225184 | 3 | 121.4651781494 | 31.1472743229 | 107 | 11 | 1 | 33.7 | TDD | 845 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3236138 | 4 | 121.4679859145 | 31.1530118668 | 323 | 9 | 11 | 30.8 | TDD | 390 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3249231 | 1 | 121.4740098861 | 31.1466718269 | 289 | 2 | 1 | 22.9 | TDD | 864 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3279288 | 2 | 121.4759924968 | 31.1524535802 | 231 | 6 | 0 | 36.2 | TDD | 320 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.782 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.805 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.938 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.938 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.164 | NREventA2 | measId:1;ServCellPCI:172;Se... |
| 2024-09-20 22:21:34.312 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249231 | 1 | 17.3489 | 14.6045 | -114.0242 | 18.2850 | 154.7989 | 0.0177 | 0.0191 |
| 2024_09_20 22:00 | 3279288 | 2 | 15.5517 | 9.5576 | -117.0736 | 6.5480 | 143.9071 | 0.0158 | 0.0054 |
| 2024_09_20 22:00 | 3225184 | 3 | 17.6309 | 10.8321 | -115.0867 | 7.9656 | 145.8360 | 0.1253 | 0.0125 |
| 2024_09_20 22:00 | 3236138 | 4 | 9.8262 | 19.0912 | -114.6699 | 14.4342 | 149.8191 | 0.0049 | 0.0040 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414004_EC9B19F6 | 504990 | 845 | -107.5 | 504990 | 864 | -112.7 | 504990 | 320 | -116.7 | 504990 | 390 |
| MR_1774414004_093E3392 | 504990 | 845 | -109.1 | 504990 | 864 | -112.6 | 504990 | 320 | -117.7 | 504990 | 390 |
| MR_1774414004_8A2C2F4E | 504990 | 845 | -107.2 | 504990 | 864 | -112.8 | 504990 | 320 | -118.9 | 504990 | 390 |
| MR_1774414004_9C1DF221 | 504990 | 845 | -108.4 | 504990 | 864 | -110.0 | 504990 | 320 | -115.6 | 504990 | 390 |
| MR_1774414004_15E03581 | 504990 | 845 | -106.7 | 504990 | 864 | -111.1 | 504990 | 320 | -118.8 | 504990 | 390 |
| MR_1774414004_5109F3AC | 504990 | 845 | -107.9 | 504990 | 864 | -113.3 | 504990 | 320 | -115.4 | 504990 | 390 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 161: `7fdcabdf-d7b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7fdcabdf-d7b9-4a71-bf22-2243ad2bd6dc` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271564_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[161] topology](images/train_0161.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease transmission power for 3271564_2
- `C3`: Decrease transmission power for 3217871_1
- `C4`: Add neighbor relationship between 3271564_2 and 3217871_1
- `C5`: Adjust the azimuth of 3217871_1 by 13 degrees
- `C6`: Decrease A3 Offset threshold for 3271564_2
- `C7`: Increase transmission power for 3271564_2
- `C8`: Lift the tilt angle of 3271564_2 by 2 degrees
- `C9`: Check test server and transmission issues
- `C10`: Increase A3 Offset threshold for 3271564_2
- `C11`: Adjust the azimuth of 3271564_2 by 22 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217871_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271564_2 **← 정답**
- `C14`: Decrease A3 Offset threshold for 3217871_1
- `C15`: Increase A3 Offset threshold for 3217871_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217871_1
- `C17`: Press down the tilt angle of 3271564_2 by 2 degrees
- `C18`: Press down the tilt angle  of 3217871_1 by 2 degrees
- `C19`: Increase transmission power for 3217871_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271564_2
- `C21`: Lift the tilt angle  of 3217871_1 by 2 degrees
- `C22`: Add neighbor relationship between 3228935_8 and 3217871_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.726 | MS1 | 121.4656598197 | 31.1446186857 | 647 | 504990 | -95.46 | 10.34 | 300.35 | 0.04 | 2.16 | 1597 |
| 2024-09-20 22:21:32.982 | MS1 | 121.4656742145 | 31.1446374289 | 688 | 504990 | -95.48 | 11.81 | 560.11 | 0.05 | 2.21 | 1572 |
| 2024-09-20 22:21:33.619 | MS1 | 121.4656721558 | 31.1446329435 | 45 | 504990 | -94.99 | 11.19 | 528.78 | 0.03 | 2.48 | 1579 |
| 2024-09-20 22:21:34.543 | MS1 | 121.4656774231 | 31.1446329116 | 768 | 152650 | -89.19 | 7.77 | 61.18 | 0.13 | 1.68 | 920 |
| 2024-09-20 22:21:35.639 | MS1 | 121.4656656423 | 31.1446344777 | 834 | 152650 | -87.16 | 2.96 | 59.96 | 0.10 | 1.78 | 900 |
| 2024-09-20 22:21:36.743 | MS1 | 121.4656698232 | 31.1446316367 | 993 | 152650 | -92.42 | 4.20 | 66.13 | 0.03 | 1.62 | 990 |
| 2024-09-20 22:21:37.320 | MS1 | 121.4656762617 | 31.1446330565 | 79 | 152650 | -91.19 | 6.70 | 64.73 | 0.12 | 1.99 | 947 |
| 2024-09-20 22:21:38.778 | MS1 | 121.4656608128 | 31.1446320856 | 768 | 152650 | -89.96 | 4.11 | 95.26 | 0.13 | 1.67 | 917 |
| 2024-09-20 22:21:39.647 | MS1 | 121.4656595397 | 31.1446339273 | 834 | 152650 | -92.42 | 5.93 | 87.71 | 0.10 | 1.70 | 906 |
| 2024-09-20 22:21:40.241 | MS1 | 121.4656662135 | 31.1446292627 | 993 | 152650 | -91.40 | 6.09 | 85.24 | 0.20 | 2.86 | 1575 |
| 2024-09-20 22:21:41.217 | MS1 | 121.4656777442 | 31.1446210193 | 79 | 152650 | -95.12 | 6.50 | 60.80 | 0.15 | 2.77 | 1580 |
| 2024-09-20 22:21:42.715 | MS1 | 121.4656607035 | 31.1446299866 | 768 | 152650 | -94.32 | 5.04 | 65.08 | 0.15 | 2.40 | 1566 |

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
| 3211294 | 3 | 121.4747271921 | 31.1484289754 | 219 | 13 | 2 | 14.7 | TDD | 749 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3217871 | 1 | 121.4723858449 | 31.1466957667 | 237 | 0 | 4 | 28.4 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3228146 | 13 | 121.4727613787 | 31.1468060873 | 180 | 13 | 0 | 1.1 | FDD | 25 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3228935 | 8 | 121.4695451300 | 31.1485702285 | 341 | 15 | 11 | 1.1 | FDD | 993 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3232476 | 9 | 121.4733797539 | 31.1505339353 | 227 | 12 | 5 | 15.7 | FDD | 834 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3241096 | 6 | 121.4712382027 | 31.1556841292 | 16 | 10 | 11 | 10.9 | TDD | 690 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3243810 | 5 | 121.4729048652 | 31.1517154523 | 69 | 12 | 11 | 16.3 | TDD | 688 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3252489 | 7 | 121.4730297366 | 31.1504376446 | 163 | 5 | 1 | 19.7 | FDD | 768 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3262222 | 11 | 121.4663596384 | 31.1504531798 | 121 | 8 | 4 | 8.8 | FDD | 79 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3263245 | 4 | 121.4739971750 | 31.1558848951 | 274 | 14 | 2 | 18.9 | TDD | 45 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3271564 | 2 | 121.4744823373 | 31.1480616209 | 268 | 2 | 9 | 6.3 | TDD | 647 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3275316 | 10 | 121.4668293563 | 31.1484244473 | 268 | 8 | 12 | 0.8 | FDD | 323 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3277537 | 12 | 121.4720398571 | 31.1476725637 | 208 | 8 | 7 | 11.8 | FDD | 815 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |

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
| 2024-09-20 22:21:31.089 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.105 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.208 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.208 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.926 | NREventA2 | measId:1;ServCellPCI:347;Se... |
| 2024-09-20 22:21:35.045 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.266 | NREventA5 | measId:3;ServCellPCI:347;Se... |
| 2024-09-20 22:21:35.326 | NRHandoverAttempt | SourcePCI:347;SourceNR-ARFC... |
| 2024-09-20 22:21:35.355 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.366 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.513 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.513 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217871 | 1 | 11.4488 | 9.4889 | -117.4642 | 15.4891 | 188.8948 | 0.0092 | 0.0128 |
| 2024_09_20 22:00 | 3271564 | 2 | 15.7447 | 7.0476 | -116.3056 | 10.9486 | 150.1151 | 0.0072 | 0.0019 |
| 2024_09_20 22:00 | 3211294 | 3 | 9.8960 | 8.1147 | -116.8556 | 19.7163 | 117.5958 | 0.0099 | 0.0002 |
| 2024_09_20 22:00 | 3263245 | 4 | 18.5470 | 7.5586 | -114.0704 | 12.1211 | 126.0749 | 0.0010 | 0.0130 |
| 2024_09_20 22:00 | 3243810 | 5 | 5.5654 | 6.0157 | -116.3587 | 11.8598 | 134.4674 | 0.0034 | 0.0024 |
| 2024_09_20 22:00 | 3241096 | 6 | 16.6304 | 14.7644 | -114.8526 | 6.8446 | 169.8162 | 0.0023 | 0.0126 |
| 2024_09_20 22:00 | 3252489 | 7 | 6.8597 | 15.7530 | -115.7457 | 4.7398 | 48.6598 | 0.0100 | 0.0039 |
| 2024_09_20 22:00 | 3228935 | 8 | 5.1224 | 14.4546 | -117.7429 | 3.6568 | 44.8529 | 0.0140 | 0.0043 |
| 2024_09_20 22:00 | 3232476 | 9 | 11.6672 | 16.6748 | -115.7507 | 3.8834 | 36.5762 | 0.0127 | 0.0067 |
| 2024_09_20 22:00 | 3275316 | 10 | 16.6497 | 16.6892 | -115.8611 | 4.1697 | 53.4189 | 0.0087 | 0.0119 |
| 2024_09_20 22:00 | 3262222 | 11 | 19.5441 | 5.6322 | -117.6863 | 4.3992 | 53.6020 | 0.0094 | 0.0195 |
| 2024_09_20 22:00 | 3277537 | 12 | 6.3900 | 12.2071 | -114.4792 | 3.9593 | 55.5127 | 0.0127 | 0.0040 |
| 2024_09_20 22:00 | 3228146 | 13 | 19.2315 | 8.3408 | -117.0177 | 4.6330 | 24.4685 | 0.0087 | 0.0068 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416986_FF439151 | 152650 | 768 | -89.4 | 152650 | 323 | -93.9 | 152650 | 815 | -96.4 | 152650 | 25 |
| MR_1774416986_35681385 | 152650 | 768 | -87.2 | 152650 | 323 | -94.2 | 152650 | 815 | -96.2 | 152650 | 25 |
| MR_1774416986_8B25A983 | 152650 | 768 | -87.2 | 152650 | 323 | -93.9 | 152650 | 815 | -97.8 | 152650 | 25 |
| MR_1774416986_C33D88C0 | 152650 | 768 | -90.9 | 152650 | 323 | -94.6 | 152650 | 815 | -97.2 | 152650 | 25 |
| MR_1774416986_22789DAC | 504990 | 45 | -94.6 | 504990 | 355 | -91.8 | 504990 | 749 | -94.8 | 504990 | 690 |
| MR_1774416986_FFC6743A | 152650 | 768 | -90.6 | 152650 | 323 | -94.1 | 152650 | 815 | -96.4 | 152650 | 25 |
| MR_1774416986_7240C530 | 152650 | 768 | -87.6 | 152650 | 323 | -93.4 | 152650 | 815 | -97.2 | 152650 | 25 |
| MR_1774416986_C72C1246 | 504990 | 45 | -94.2 | 504990 | 355 | -90.8 | 504990 | 749 | -97.4 | 504990 | 690 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 162: `db8dfecf-6d4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `db8dfecf-6d42-4fec-bb49-6d427539da64` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[162] topology](images/train_0162.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3279314_4 and 3257701_3
- `C2`: Increase A3 Offset threshold for 3257701_3
- `C3`: Insufficient data; more data is needed for judgment. **← 정답**
- `C4`: Increase A3 Offset threshold for 3279314_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279314_4
- `C6`: Decrease A3 Offset threshold for 3279314_4
- `C7`: Adjust the azimuth of 3279314_4 by 50 degrees
- `C8`: Decrease A3 Offset threshold for 3257701_3
- `C9`: Decrease transmission power for 3279314_4
- `C10`: Check test server and transmission issues
- `C11`: Press down the tilt angle of 3279314_4 by 10 degrees
- `C12`: Lift the tilt angle of 3279314_4 by 10 degrees
- `C13`: Increase transmission power for 3279314_4
- `C14`: Add neighbor relationship between 3270804_2 and 3257701_3
- `C15`: Adjust the azimuth of 3257701_3 by 50 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257701_3
- `C17`: Lift the tilt angle  of 3257701_3 by 10 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279314_4
- `C19`: Decrease transmission power for 3257701_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257701_3
- `C21`: Increase transmission power for 3257701_3
- `C22`: Press down the tilt angle  of 3257701_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.629 | MS1 | 121.4656599266 | 31.1446337741 | 415 | 504990 | -85.81 | 15.76 | 434.66 | 0.20 | 2.97 | 1591 |
| 2024-09-20 22:21:32.660 | MS1 | 121.4656661045 | 31.1446348342 | 415 | 504990 | -87.41 | 13.34 | 497.47 | 0.08 | 2.29 | 1581 |
| 2024-09-20 22:21:33.279 | MS1 | 121.4656615708 | 31.1446192640 | 415 | 504990 | -90.31 | 17.77 | 554.09 | 0.18 | 2.20 | 1564 |
| 2024-09-20 22:21:34.236 | MS1 | 121.4656740105 | 31.1446253293 | 415 | 504990 | -89.32 | 14.22 | 89.72 | 0.18 | 2.76 | 1568 |
| 2024-09-20 22:21:35.528 | MS1 | 121.4656689231 | 31.1446255236 | 415 | 504990 | -88.89 | 17.82 | 93.69 | 0.10 | 2.61 | 1598 |
| 2024-09-20 22:21:36.445 | MS1 | 121.4656690998 | 31.1446181792 | 415 | 504990 | -91.33 | 14.73 | 102.34 | 0.19 | 2.42 | 1589 |
| 2024-09-20 22:21:37.571 | MS1 | 121.4656726469 | 31.1446302802 | 415 | 504990 | -93.09 | 12.50 | 58.01 | 0.01 | 2.19 | 1560 |
| 2024-09-20 22:21:38.367 | MS1 | 121.4656626738 | 31.1446271133 | 415 | 504990 | -91.87 | 10.36 | 72.98 | 0.01 | 2.45 | 1588 |
| 2024-09-20 22:21:39.749 | MS1 | 121.4656586627 | 31.1446358246 | 415 | 504990 | -90.84 | 8.40 | 89.04 | 0.03 | 2.94 | 1590 |
| 2024-09-20 22:21:40.688 | MS1 | 121.4656718968 | 31.1446288119 | 415 | 504990 | -92.56 | 12.15 | 389.94 | 0.14 | 2.74 | 1594 |
| 2024-09-20 22:21:41.781 | MS1 | 121.4656652095 | 31.1446236832 | 415 | 504990 | -91.46 | 9.00 | 345.89 | 0.13 | 2.07 | 1564 |
| 2024-09-20 22:21:42.983 | MS1 | 121.4656714376 | 31.1446234076 | 415 | 504990 | -92.89 | 11.42 | 346.77 | 0.20 | 2.85 | 1576 |

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
| 3257701 | 3 | 121.4730467104 | 31.1520132499 | 140 | 14 | 6 | 21.2 | TDD | 782 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3269375 | 1 | 121.4696021539 | 31.1476025063 | 86 | 13 | 4 | 24.4 | TDD | 816 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3270804 | 2 | 121.4711327011 | 31.1488798738 | 131 | 8 | 5 | 39.4 | TDD | 545 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3279314 | 4 | 121.4661193264 | 31.1466779759 | 295 | 12 | 8 | 44.0 | TDD | 415 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.423 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.438 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.553 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.553 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.247 | NREventA3 | measId:2;ServCellPCI:406;Se... |
| 2024-09-20 22:21:38.487 | NRHandoverAttempt | SourcePCI:406;SourceNR-ARFC... |
| 2024-09-20 22:21:38.530 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.543 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.667 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.667 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3269375 | 1 | 85.3688 | 84.5240 | -116.2985 | 19.5697 | 139.7809 | 0.0108 | 0.0189 |
| 2024_09_19 22:00 | 3270804 | 2 | 76.7021 | 77.3398 | -116.2789 | 7.5483 | 104.5802 | 0.0041 | 0.0131 |
| 2024_09_19 22:00 | 3257701 | 3 | 84.0900 | 87.8050 | -114.9185 | 12.4276 | 178.0007 | 0.0083 | 0.0045 |
| 2024_09_19 22:00 | 3279314 | 4 | 78.5223 | 86.1063 | -115.2239 | 16.5961 | 113.5830 | 0.0141 | 0.0116 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415782_F165D45B | 504990 | 415 | -90.7 | 504990 | 782 | -93.1 | 504990 | 545 | -100.3 | 504990 | 816 |
| MR_1774415782_D4A7F4C8 | 504990 | 415 | -91.1 | 504990 | 782 | -93.0 | 504990 | 545 | -96.9 | 504990 | 816 |
| MR_1774415782_2F38C451 | 504990 | 415 | -87.5 | 504990 | 782 | -91.1 | 504990 | 545 | -100.6 | 504990 | 816 |
| MR_1774415782_886606E7 | 504990 | 415 | -90.5 | 504990 | 782 | -95.0 | 504990 | 545 | -98.4 | 504990 | 816 |
| MR_1774415782_393BBEC3 | 504990 | 415 | -89.5 | 504990 | 782 | -92.6 | 504990 | 545 | -98.1 | 504990 | 816 |
| MR_1774415782_E470E68B | 504990 | 415 | -90.9 | 504990 | 782 | -92.3 | 504990 | 545 | -100.1 | 504990 | 816 |
| MR_1774415782_33C60B46 | 504990 | 415 | -91.1 | 504990 | 782 | -93.3 | 504990 | 545 | -99.1 | 504990 | 816 |
| MR_1774415782_71CE0367 | 504990 | 415 | -89.1 | 504990 | 782 | -92.9 | 504990 | 545 | -97.8 | 504990 | 816 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 163: `6f97dc5e-a33...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6f97dc5e-a33f-4ea4-a65f-df3c12608def` |
| Tag | **multiple-answer** |
| 정답 | **C15|C20** |
| C15 의미 | Decrease transmission power for 3269234_4 |
| C20 의미 | Press down the tilt angle  of 3269234_4 by 4 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[163] topology](images/train_0163.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Lift the tilt angle  of 3269234_4 by 4 degrees
- `C3`: Check test server and transmission issues
- `C4`: Increase transmission power for 3269234_4
- `C5`: Press down the tilt angle of 3229228_1 by 3 degrees
- `C6`: Increase A3 Offset threshold for 3229228_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229228_1
- `C8`: Decrease A3 Offset threshold for 3229228_1
- `C9`: Increase transmission power for 3229228_1
- `C10`: Decrease transmission power for 3229228_1
- `C11`: Lift the tilt angle of 3229228_1 by 3 degrees
- `C12`: Adjust the azimuth of 3269234_4 by 28 degrees
- `C13`: Add neighbor relationship between 3266723_3 and 3269234_4
- `C14`: Decrease A3 Offset threshold for 3269234_4
- `C15`: Decrease transmission power for 3269234_4 **← 정답**
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269234_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269234_4
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229228_1
- `C19`: Add neighbor relationship between 3229228_1 and 3269234_4
- `C20`: Press down the tilt angle  of 3269234_4 by 4 degrees **← 정답**
- `C21`: Adjust the azimuth of 3229228_1 by 9 degrees
- `C22`: Increase A3 Offset threshold for 3269234_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.793 | MS1 | 121.4656690302 | 31.1446325314 | 571 | 504990 | -80.68 | 16.63 | 350.04 | 0.11 | 2.98 | 1573 |
| 2024-09-20 22:21:32.419 | MS1 | 121.4656600896 | 31.1446242748 | 571 | 504990 | -82.54 | 12.86 | 541.43 | 0.10 | 2.08 | 1586 |
| 2024-09-20 22:21:33.293 | MS1 | 121.4656689384 | 31.1446269231 | 571 | 504990 | -83.32 | 12.52 | 590.01 | 0.09 | 2.86 | 1575 |
| 2024-09-20 22:21:34.678 | MS1 | 121.4656733894 | 31.1446253788 | 571 | 504990 | -90.54 | 2.50 | 47.53 | 0.02 | 1.38 | 1570 |
| 2024-09-20 22:21:35.501 | MS1 | 121.4656763833 | 31.1446257821 | 571 | 504990 | -92.20 | 0.33 | 47.29 | 0.15 | 1.03 | 1562 |
| 2024-09-20 22:21:36.950 | MS1 | 121.4656762847 | 31.1446270581 | 571 | 504990 | -92.30 | 3.00 | 74.29 | 0.10 | 1.35 | 1561 |
| 2024-09-20 22:21:37.182 | MS1 | 121.4656623478 | 31.1446335946 | 571 | 504990 | -94.64 | 2.81 | 68.23 | 0.15 | 1.27 | 1581 |
| 2024-09-20 22:21:38.713 | MS1 | 121.4656746916 | 31.1446323792 | 571 | 504990 | -86.86 | 3.10 | 56.88 | 0.00 | 1.39 | 1563 |
| 2024-09-20 22:21:39.557 | MS1 | 121.4656733737 | 31.1446317041 | 571 | 504990 | -85.31 | 2.39 | 61.23 | 0.06 | 1.13 | 1594 |
| 2024-09-20 22:21:40.158 | MS1 | 121.4656778947 | 31.1446235593 | 571 | 504990 | -81.52 | 13.90 | 471.29 | 0.12 | 2.09 | 1571 |
| 2024-09-20 22:21:41.674 | MS1 | 121.4656712794 | 31.1446249145 | 571 | 504990 | -84.83 | 17.90 | 305.54 | 0.05 | 2.46 | 1587 |
| 2024-09-20 22:21:42.671 | MS1 | 121.4656746594 | 31.1446221086 | 571 | 504990 | -81.23 | 12.41 | 589.66 | 0.09 | 2.92 | 1565 |

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
| 3229228 | 1 | 121.4748068650 | 31.1478507816 | 239 | 1 | 0 | 29.8 | TDD | 571 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3266723 | 3 | 121.4717545610 | 31.1467243161 | 259 | 10 | 3 | 42.6 | TDD | 732 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3269234 | 4 | 121.4743368611 | 31.1456087602 | 290 | 3 | 11 | 16.1 | TDD | 238 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3271237 | 2 | 121.4651660990 | 31.1487575813 | 202 | 0 | 11 | 40.9 | TDD | 515 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.591 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.611 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.712 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.712 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229228 | 1 | 8.0655 | 13.4565 | -108.1838 | 7.3017 | 126.3549 | 0.0127 | 0.0143 |
| 2024_09_20 22:00 | 3271237 | 2 | 7.0006 | 13.6306 | -114.8942 | 17.4034 | 138.0132 | 0.0075 | 0.0182 |
| 2024_09_20 22:00 | 3266723 | 3 | 12.0198 | 16.4839 | -114.7374 | 13.4017 | 120.7131 | 0.0055 | 0.0090 |
| 2024_09_20 22:00 | 3269234 | 4 | 18.0645 | 18.0701 | -115.5416 | 16.8152 | 160.2103 | 0.0133 | 0.0077 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415127_8FA86780 | 504990 | 238 | -91.3 | 504990 | 571 | -88.0 | 504990 | 732 | -88.9 | 504990 | 515 |
| MR_1774415127_D996C3C7 | 504990 | 571 | -90.3 | 504990 | 238 | -86.5 | 504990 | 732 | -88.2 | 504990 | 515 |
| MR_1774415127_BE0A6F46 | 504990 | 238 | -90.6 | 504990 | 571 | -87.6 | 504990 | 732 | -87.4 | 504990 | 515 |
| MR_1774415127_6B69D990 | 504990 | 571 | -90.7 | 504990 | 238 | -88.2 | 504990 | 732 | -89.7 | 504990 | 515 |
| MR_1774415127_6AF128A3 | 504990 | 571 | -91.2 | 504990 | 238 | -86.5 | 504990 | 732 | -90.2 | 504990 | 515 |
| MR_1774415127_595FBEE6 | 504990 | 571 | -88.7 | 504990 | 238 | -88.2 | 504990 | 732 | -88.6 | 504990 | 515 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 164: `7555f9df-398...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7555f9df-398c-4a86-a388-0db845ef6822` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253541_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[164] topology](images/train_0164.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3253541_5
- `C2`: Decrease A3 Offset threshold for 3265717_2
- `C3`: Add neighbor relationship between 3227672_8 and 3265717_2
- `C4`: Adjust the azimuth of 3265717_2 by 26 degrees
- `C5`: Increase transmission power for 3253541_5
- `C6`: Check test server and transmission issues
- `C7`: Press down the tilt angle of 3253541_5 by 5 degrees
- `C8`: Increase transmission power for 3265717_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265717_2
- `C10`: Lift the tilt angle  of 3265717_2 by 5 degrees
- `C11`: Press down the tilt angle  of 3265717_2 by 5 degrees
- `C12`: Lift the tilt angle of 3253541_5 by 5 degrees
- `C13`: Decrease transmission power for 3265717_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253541_5 **← 정답**
- `C15`: Decrease transmission power for 3253541_5
- `C16`: Increase A3 Offset threshold for 3253541_5
- `C17`: Add neighbor relationship between 3253541_5 and 3265717_2
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265717_2
- `C20`: Increase A3 Offset threshold for 3265717_2
- `C21`: Adjust the azimuth of 3253541_5 by 46 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253541_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.948 | MS1 | 121.4656721913 | 31.1446181742 | 184 | 504990 | -95.64 | 12.35 | 359.02 | 0.09 | 2.86 | 1565 |
| 2024-09-20 22:21:32.994 | MS1 | 121.4656612324 | 31.1446246984 | 680 | 504990 | -93.98 | 12.59 | 398.73 | 0.20 | 2.82 | 1587 |
| 2024-09-20 22:21:33.225 | MS1 | 121.4656618856 | 31.1446277433 | 146 | 504990 | -93.28 | 14.15 | 396.08 | 0.09 | 2.30 | 1568 |
| 2024-09-20 22:21:34.762 | MS1 | 121.4656723822 | 31.1446356511 | 924 | 152650 | -88.28 | 6.76 | 66.96 | 0.05 | 1.77 | 950 |
| 2024-09-20 22:21:35.178 | MS1 | 121.4656685764 | 31.1446305007 | 688 | 152650 | -95.43 | 4.70 | 76.44 | 0.14 | 1.51 | 918 |
| 2024-09-20 22:21:36.132 | MS1 | 121.4656644663 | 31.1446309870 | 389 | 152650 | -89.17 | 7.28 | 83.81 | 0.19 | 1.73 | 925 |
| 2024-09-20 22:21:37.884 | MS1 | 121.4656590326 | 31.1446226360 | 437 | 152650 | -89.84 | 6.86 | 73.67 | 0.05 | 1.52 | 977 |
| 2024-09-20 22:21:38.912 | MS1 | 121.4656619403 | 31.1446300033 | 924 | 152650 | -87.36 | 6.19 | 75.50 | 0.09 | 1.53 | 974 |
| 2024-09-20 22:21:39.382 | MS1 | 121.4656741536 | 31.1446218260 | 688 | 152650 | -90.47 | 2.86 | 87.15 | 0.07 | 1.87 | 919 |
| 2024-09-20 22:21:40.936 | MS1 | 121.4656661161 | 31.1446265803 | 389 | 152650 | -92.00 | 3.37 | 68.66 | 0.08 | 2.67 | 1574 |
| 2024-09-20 22:21:41.433 | MS1 | 121.4656626439 | 31.1446355493 | 437 | 152650 | -93.20 | 4.46 | 51.84 | 0.10 | 2.80 | 1587 |
| 2024-09-20 22:21:42.162 | MS1 | 121.4656711575 | 31.1446288399 | 924 | 152650 | -91.34 | 3.64 | 84.51 | 0.01 | 2.12 | 1597 |

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
| 3214218 | 6 | 121.4667171093 | 31.1470025255 | 343 | 3 | 11 | 1.5 | TDD | 413 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3227672 | 8 | 121.4750049658 | 31.1534227786 | 251 | 13 | 12 | 18.9 | FDD | 389 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3229742 | 11 | 121.4655425172 | 31.1460698519 | 5 | 0 | 9 | 28.2 | FDD | 688 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3237239 | 10 | 121.4700192661 | 31.1543771529 | 347 | 1 | 7 | 12.4 | FDD | 874 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3242739 | 13 | 121.4723612504 | 31.1500576990 | 267 | 15 | 2 | 7.2 | FDD | 924 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3249017 | 3 | 121.4746426625 | 31.1446303920 | 206 | 14 | 12 | 17.6 | TDD | 146 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3250476 | 7 | 121.4727280703 | 31.1517546534 | 231 | 0 | 10 | 5.3 | FDD | 35 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3252431 | 9 | 121.4717172503 | 31.1539226113 | 81 | 4 | 3 | 8.3 | FDD | 359 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3253541 | 5 | 121.4717088804 | 31.1469597863 | 200 | 3 | 3 | 24.6 | TDD | 184 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3261849 | 4 | 121.4682668629 | 31.1535664622 | 129 | 0 | 6 | 13.9 | TDD | 980 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3265717 | 2 | 121.4673646361 | 31.1516190132 | 218 | 5 | 0 | 3.3 | TDD | 589 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3267047 | 12 | 121.4669930038 | 31.1458481404 | 131 | 6 | 3 | 0.4 | FDD | 437 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3276289 | 1 | 121.4676341731 | 31.1499134214 | 138 | 10 | 10 | 28.1 | TDD | 680 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.167 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.183 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.284 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.284 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.055 | NREventA2 | measId:1;ServCellPCI:52;Ser... |
| 2024-09-20 22:21:35.187 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.451 | NREventA5 | measId:3;ServCellPCI:52;Ser... |
| 2024-09-20 22:21:35.490 | NRHandoverAttempt | SourcePCI:52;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.534 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.545 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.675 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.675 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276289 | 1 | 6.9964 | 18.3728 | -115.8001 | 6.7105 | 127.2224 | 0.0045 | 0.0073 |
| 2024_09_20 22:00 | 3265717 | 2 | 11.8858 | 9.1683 | -114.3434 | 13.5400 | 96.3356 | 0.0175 | 0.0133 |
| 2024_09_20 22:00 | 3249017 | 3 | 15.6218 | 16.2163 | -114.2006 | 6.7587 | 188.8518 | 0.0168 | 0.0077 |
| 2024_09_20 22:00 | 3261849 | 4 | 7.6791 | 14.5894 | -115.0533 | 11.9171 | 176.8311 | 0.0012 | 0.0101 |
| 2024_09_20 22:00 | 3253541 | 5 | 18.4767 | 10.8063 | -117.3710 | 19.6980 | 111.6772 | 0.0163 | 0.0148 |
| 2024_09_20 22:00 | 3214218 | 6 | 16.0852 | 16.6196 | -114.6964 | 9.3061 | 187.0336 | 0.0114 | 0.0017 |
| 2024_09_20 22:00 | 3250476 | 7 | 18.7200 | 19.0755 | -114.1717 | 4.0744 | 29.5959 | 0.0068 | 0.0183 |
| 2024_09_20 22:00 | 3227672 | 8 | 12.4782 | 6.0193 | -114.5197 | 4.7512 | 46.0100 | 0.0056 | 0.0018 |
| 2024_09_20 22:00 | 3252431 | 9 | 16.5212 | 19.1510 | -115.0576 | 3.3393 | 28.6393 | 0.0144 | 0.0137 |
| 2024_09_20 22:00 | 3237239 | 10 | 15.4873 | 12.1190 | -117.6413 | 4.0430 | 45.7487 | 0.0143 | 0.0178 |
| 2024_09_20 22:00 | 3229742 | 11 | 11.4552 | 18.1124 | -115.2644 | 3.2338 | 47.3890 | 0.0020 | 0.0110 |
| 2024_09_20 22:00 | 3267047 | 12 | 10.9729 | 16.8386 | -116.5368 | 3.0130 | 55.7194 | 0.0015 | 0.0176 |
| 2024_09_20 22:00 | 3242739 | 13 | 15.1002 | 6.0247 | -114.3101 | 3.4288 | 57.8811 | 0.0093 | 0.0002 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417203_64690F86 | 504990 | 146 | -92.6 | 504990 | 589 | -93.0 | 504990 | 413 | -96.6 | 504990 | 980 |
| MR_1774417203_70C16506 | 152650 | 924 | -89.7 | 152650 | 35 | -94.5 | 152650 | 874 | -96.0 | 152650 | 359 |
| MR_1774417203_F2E83A6A | 152650 | 924 | -89.9 | 152650 | 35 | -93.5 | 152650 | 874 | -96.9 | 152650 | 359 |
| MR_1774417203_2F19F11E | 152650 | 924 | -90.1 | 152650 | 35 | -96.1 | 152650 | 874 | -95.9 | 152650 | 359 |
| MR_1774417203_128036DA | 504990 | 146 | -94.1 | 504990 | 589 | -95.4 | 504990 | 413 | -99.5 | 504990 | 980 |
| MR_1774417203_5AD4A4CD | 504990 | 146 | -94.9 | 504990 | 589 | -93.5 | 504990 | 413 | -98.3 | 504990 | 980 |
| MR_1774417203_7878A8CC | 152650 | 924 | -88.8 | 152650 | 35 | -95.6 | 152650 | 874 | -94.7 | 152650 | 359 |
| MR_1774417203_97983BA7 | 504990 | 146 | -93.8 | 504990 | 589 | -92.9 | 504990 | 413 | -99.6 | 504990 | 980 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 165: `2e2611ba-a7e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2e2611ba-a7e4-4fd0-9bb4-ccf2b6ef7650` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Lift the tilt angle  of 3228003_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[165] topology](images/train_0165.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233320_2
- `C2`: Decrease transmission power for 3268075_1
- `C3`: Add neighbor relationship between 3228003_3 and 3268075_1
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Add neighbor relationship between 3233320_2 and 3268075_1
- `C6`: Adjust the azimuth of 3228003_3 by 38 degrees
- `C7`: Decrease A3 Offset threshold for 3268075_1
- `C8`: Press down the tilt angle of 3233320_2 by 3 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268075_1
- `C10`: Check test server and transmission issues
- `C11`: Increase transmission power for 3233320_2
- `C12`: Increase transmission power for 3268075_1
- `C13`: Increase A3 Offset threshold for 3233320_2
- `C14`: Decrease A3 Offset threshold for 3233320_2
- `C15`: Decrease transmission power for 3233320_2
- `C16`: Press down the tilt angle  of 3228003_3 by 10 degrees
- `C17`: Lift the tilt angle of 3233320_2 by 3 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268075_1
- `C19`: Adjust the azimuth of 3233320_2 by 22 degrees
- `C20`: Lift the tilt angle  of 3228003_3 by 10 degrees **← 정답**
- `C21`: Increase A3 Offset threshold for 3268075_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233320_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.179 | MS1 | 121.4656779799 | 31.1446311611 | 170 | 504990 | -87.22 | 16.24 | 331.47 | 0.10 | 2.31 | 1594 |
| 2024-09-20 22:21:32.372 | MS1 | 121.4656641622 | 31.1446364435 | 170 | 504990 | -89.97 | 16.91 | 395.69 | 0.04 | 2.23 | 1584 |
| 2024-09-20 22:21:33.691 | MS1 | 121.4656715700 | 31.1446271779 | 170 | 504990 | -91.97 | 15.95 | 475.17 | 0.03 | 2.97 | 1575 |
| 2024-09-20 22:21:34.615 | MS1 | 121.4656677150 | 31.1446316067 | 170 | 504990 | -88.40 | 17.41 | 101.54 | 0.07 | 2.20 | 1587 |
| 2024-09-20 22:21:35.804 | MS1 | 121.4656702372 | 31.1446207149 | 170 | 504990 | -86.94 | 16.52 | 82.63 | 0.06 | 2.93 | 1590 |
| 2024-09-20 22:21:36.473 | MS1 | 121.4656779732 | 31.1446341770 | 170 | 504990 | -88.73 | 17.49 | 86.38 | 0.02 | 2.81 | 1581 |
| 2024-09-20 22:21:37.737 | MS1 | 121.4656742198 | 31.1446276913 | 170 | 504990 | -91.15 | 7.31 | 77.89 | 0.13 | 2.51 | 1584 |
| 2024-09-20 22:21:38.795 | MS1 | 121.4656646790 | 31.1446379119 | 170 | 504990 | -89.97 | 9.40 | 52.03 | 0.14 | 2.59 | 1562 |
| 2024-09-20 22:21:39.671 | MS1 | 121.4656704300 | 31.1446322044 | 170 | 504990 | -92.66 | 7.27 | 79.72 | 0.12 | 2.33 | 1591 |
| 2024-09-20 22:21:40.175 | MS1 | 121.4656642586 | 31.1446200414 | 170 | 504990 | -92.00 | 11.61 | 377.88 | 0.13 | 2.48 | 1579 |
| 2024-09-20 22:21:41.841 | MS1 | 121.4656719244 | 31.1446192920 | 170 | 504990 | -92.76 | 8.62 | 569.99 | 0.02 | 2.67 | 1586 |
| 2024-09-20 22:21:42.648 | MS1 | 121.4656652780 | 31.1446220126 | 170 | 504990 | -89.31 | 7.51 | 327.39 | 0.07 | 2.28 | 1579 |

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
| 3228003 | 3 | 121.4738318570 | 31.1462629625 | 59 | 8 | 12 | 34.3 | TDD | 162 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3233320 | 2 | 121.4735302939 | 31.1504628192 | 207 | 0 | 12 | 44.5 | TDD | 170 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3268075 | 1 | 121.4661226410 | 31.1444033407 | 263 | 5 | 5 | 31.9 | TDD | 264 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3275155 | 4 | 121.4665706430 | 31.1503975608 | 225 | 9 | 2 | 39.7 | TDD | 833 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.991 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.007 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.146 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.146 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.837 | NREventA3 | measId:2;ServCellPCI:534;Se... |
| 2024-09-20 22:21:38.077 | NRHandoverAttempt | SourcePCI:534;SourceNR-ARFC... |
| 2024-09-20 22:21:38.108 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.119 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.247 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.247 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268075 | 1 | 12.8817 | 19.8822 | -116.1192 | 19.0714 | 181.8895 | 0.0184 | 0.0032 |
| 2024_09_20 22:00 | 3233320 | 2 | 86.9637 | 89.7002 | -116.2682 | 11.7447 | 174.5490 | 0.0108 | 0.0102 |
| 2024_09_20 22:00 | 3228003 | 3 | 5.3498 | 14.6343 | -117.8765 | 5.7167 | 83.8595 | 0.0014 | 0.0022 |
| 2024_09_20 22:00 | 3275155 | 4 | 17.1729 | 18.7120 | -115.9166 | 13.8725 | 87.4494 | 0.0058 | 0.0048 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416500_5A22E6D6 | 504990 | 170 | -87.3 | 504990 | 264 | -94.5 | 504990 | 162 | -99.6 | 504990 | 833 |
| MR_1774416500_FDA926AF | 504990 | 170 | -86.3 | 504990 | 264 | -96.8 | 504990 | 162 | -99.1 | 504990 | 833 |
| MR_1774416500_B97DA198 | 504990 | 170 | -85.4 | 504990 | 264 | -94.2 | 504990 | 162 | -99.9 | 504990 | 833 |
| MR_1774416500_B05EE92E | 504990 | 170 | -85.1 | 504990 | 264 | -96.8 | 504990 | 162 | -98.5 | 504990 | 833 |
| MR_1774416500_9045F0C1 | 504990 | 170 | -86.1 | 504990 | 264 | -96.8 | 504990 | 162 | -99.5 | 504990 | 833 |
| MR_1774416500_F0D76FF6 | 504990 | 170 | -87.2 | 504990 | 264 | -97.2 | 504990 | 162 | -98.6 | 504990 | 833 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 166: `e4f02195-e1d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e4f02195-e1df-4013-8ebf-74c6ef0ac897` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[166] topology](images/train_0166.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3245856_2 by 10 degrees
- `C2`: Increase A3 Offset threshold for 3279625_4
- `C3`: Add neighbor relationship between 3279514_1 and 3245856_2
- `C4`: Increase transmission power for 3245856_2
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase transmission power for 3279625_4
- `C7`: Lift the tilt angle  of 3245856_2 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3279625_4
- `C9`: Add neighbor relationship between 3279625_4 and 3245856_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279625_4
- `C11`: Press down the tilt angle of 3279625_4 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279625_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245856_2
- `C14`: Adjust the azimuth of 3279625_4 by 50 degrees
- `C15`: Decrease transmission power for 3279625_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245856_2
- `C17`: Lift the tilt angle of 3279625_4 by 10 degrees
- `C18`: Decrease A3 Offset threshold for 3245856_2
- `C19`: Adjust the azimuth of 3245856_2 by 50 degrees
- `C20`: Increase A3 Offset threshold for 3245856_2
- `C21`: Decrease transmission power for 3245856_2
- `C22`: Check test server and transmission issues **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.667 | MS1 | 121.4656724489 | 31.1446321563 | 207 | 504990 | -90.77 | 13.55 | 566.66 | 0.07 | 2.97 | 1570 |
| 2024-09-20 22:21:32.612 | MS1 | 121.4656738140 | 31.1446316516 | 207 | 504990 | -90.10 | 12.89 | 369.82 | 0.01 | 2.67 | 1588 |
| 2024-09-20 22:21:33.233 | MS1 | 121.4656674184 | 31.1446193383 | 207 | 504990 | -89.56 | 12.52 | 540.65 | 0.03 | 2.25 | 1568 |
| 2024-09-20 22:21:34.121 | MS1 | 121.4656664700 | 31.1446310567 | 207 | 504990 | -91.13 | 14.97 | 55.91 | 0.19 | 2.02 | 410 |
| 2024-09-20 22:21:35.353 | MS1 | 121.4656759552 | 31.1446247420 | 207 | 504990 | -86.92 | 13.95 | 88.31 | 0.04 | 2.78 | 332 |
| 2024-09-20 22:21:36.219 | MS1 | 121.4656765351 | 31.1446238517 | 207 | 504990 | -90.06 | 16.23 | 67.71 | 0.12 | 2.49 | 497 |
| 2024-09-20 22:21:37.457 | MS1 | 121.4656690697 | 31.1446235081 | 207 | 504990 | -92.64 | 9.73 | 65.15 | 0.08 | 2.55 | 392 |
| 2024-09-20 22:21:38.398 | MS1 | 121.4656593007 | 31.1446306799 | 207 | 504990 | -89.38 | 7.79 | 87.72 | 0.15 | 2.87 | 472 |
| 2024-09-20 22:21:39.690 | MS1 | 121.4656641380 | 31.1446314423 | 207 | 504990 | -93.34 | 9.74 | 72.67 | 0.04 | 2.39 | 425 |
| 2024-09-20 22:21:40.997 | MS1 | 121.4656595180 | 31.1446231938 | 207 | 504990 | -94.00 | 8.24 | 428.85 | 0.19 | 2.37 | 1571 |
| 2024-09-20 22:21:41.875 | MS1 | 121.4656708378 | 31.1446256530 | 207 | 504990 | -89.46 | 12.91 | 367.00 | 0.08 | 2.90 | 1572 |
| 2024-09-20 22:21:42.660 | MS1 | 121.4656605291 | 31.1446312439 | 207 | 504990 | -93.06 | 8.11 | 523.96 | 0.03 | 2.85 | 1585 |

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
| 3245856 | 2 | 121.4721015243 | 31.1496738964 | 107 | 12 | 3 | 21.2 | TDD | 201 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3250623 | 3 | 121.4677154890 | 31.1490399752 | 52 | 0 | 8 | 27.2 | TDD | 537 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3279514 | 1 | 121.4705797958 | 31.1497567142 | 55 | 2 | 1 | 26.9 | TDD | 512 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3279625 | 4 | 121.4650027317 | 31.1445597111 | 22 | 3 | 1 | 36.2 | TDD | 207 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.953 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.953 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.674 | NREventA3 | measId:2;ServCellPCI:756;Se... |
| 2024-09-20 22:21:37.914 | NRHandoverAttempt | SourcePCI:756;SourceNR-ARFC... |
| 2024-09-20 22:21:37.951 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.963 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.078 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.078 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279514 | 1 | 12.1219 | 17.9318 | -116.8115 | 15.1041 | 116.7659 | 0.0052 | 0.0193 |
| 2024_09_20 22:00 | 3245856 | 2 | 14.6110 | 12.3409 | -114.5917 | 10.6279 | 193.1103 | 0.0012 | 0.0188 |
| 2024_09_20 22:00 | 3250623 | 3 | 16.6343 | 18.1391 | -116.1123 | 7.6003 | 117.7931 | 0.0130 | 0.0198 |
| 2024_09_20 22:00 | 3279625 | 4 | 18.7418 | 16.0309 | -114.5094 | 16.3934 | 152.9896 | 0.0155 | 0.0020 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415628_FA4EAF85 | 504990 | 207 | -89.7 | 504990 | 201 | -96.0 | 504990 | 512 | -104.7 | 504990 | 537 |
| MR_1774415628_2109DF9B | 504990 | 207 | -91.9 | 504990 | 201 | -96.1 | 504990 | 512 | -104.4 | 504990 | 537 |
| MR_1774415628_D44DE4DB | 504990 | 207 | -92.9 | 504990 | 201 | -94.6 | 504990 | 512 | -104.0 | 504990 | 537 |
| MR_1774415628_7BCC81BB | 504990 | 207 | -90.8 | 504990 | 201 | -96.3 | 504990 | 512 | -106.2 | 504990 | 537 |
| MR_1774415628_0B0803DA | 504990 | 207 | -89.8 | 504990 | 201 | -98.1 | 504990 | 512 | -105.5 | 504990 | 537 |
| MR_1774415628_278BDF63 | 504990 | 207 | -91.2 | 504990 | 201 | -95.6 | 504990 | 512 | -105.9 | 504990 | 537 |
| MR_1774415628_D60EA8E8 | 504990 | 207 | -92.8 | 504990 | 201 | -96.0 | 504990 | 512 | -105.8 | 504990 | 537 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 167: `5799cccd-553...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5799cccd-553f-4492-8bf2-038b17de7619` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Add neighbor relationship between 3238821_1 and 3262356_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[167] topology](images/train_0167.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3262356_4
- `C2`: Increase A3 Offset threshold for 3238821_1
- `C3`: Press down the tilt angle  of 3262356_4 by 4 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238821_1
- `C5`: Decrease transmission power for 3238821_1
- `C6`: Check test server and transmission issues
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238821_1
- `C8`: Decrease transmission power for 3262356_4
- `C9`: Increase transmission power for 3262356_4
- `C10`: Increase transmission power for 3238821_1
- `C11`: Adjust the azimuth of 3262356_4 by 15 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262356_4
- `C13`: Press down the tilt angle of 3238821_1 by 10 degrees
- `C14`: Adjust the azimuth of 3238821_1 by 29 degrees
- `C15`: Decrease A3 Offset threshold for 3262356_4
- `C16`: Add neighbor relationship between 3238821_1 and 3262356_4 **← 정답**
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262356_4
- `C18`: Lift the tilt angle  of 3262356_4 by 4 degrees
- `C19`: Decrease A3 Offset threshold for 3238821_1
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Add neighbor relationship between 3254319_3 and 3262356_4
- `C22`: Lift the tilt angle of 3238821_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.797 | MS1 | 121.4656721693 | 31.1446319002 | 156 | 504990 | -82.53 | 16.46 | 501.39 | 0.13 | 2.82 | 1562 |
| 2024-09-20 22:21:32.565 | MS1 | 121.4656715409 | 31.1446196635 | 156 | 504990 | -78.87 | 16.84 | 474.40 | 0.08 | 2.12 | 1595 |
| 2024-09-20 22:21:33.871 | MS1 | 121.4656662947 | 31.1446273044 | 156 | 504990 | -77.57 | 14.23 | 463.08 | 0.15 | 2.90 | 1560 |
| 2024-09-20 22:21:34.741 | MS1 | 121.4656685895 | 31.1446328941 | 156 | 504990 | -92.26 | -3.21 | 38.95 | 0.04 | 1.29 | 1577 |
| 2024-09-20 22:21:35.424 | MS1 | 121.4656703376 | 31.1446198115 | 156 | 504990 | -91.08 | -0.99 | 54.93 | 0.16 | 1.40 | 1599 |
| 2024-09-20 22:21:36.251 | MS1 | 121.4656670377 | 31.1446255509 | 156 | 504990 | -90.57 | -3.47 | 31.92 | 0.07 | 1.37 | 1594 |
| 2024-09-20 22:21:37.952 | MS1 | 121.4656681863 | 31.1446255973 | 156 | 504990 | -86.69 | -1.69 | 62.74 | 0.05 | 1.26 | 1572 |
| 2024-09-20 22:21:38.710 | MS1 | 121.4656634746 | 31.1446303777 | 156 | 504990 | -78.49 | 12.56 | 546.39 | 0.17 | 1.33 | 1578 |
| 2024-09-20 22:21:39.466 | MS1 | 121.4656653482 | 31.1446282515 | 156 | 504990 | -82.46 | 12.69 | 599.26 | 0.13 | 1.37 | 1570 |
| 2024-09-20 22:21:40.649 | MS1 | 121.4656778866 | 31.1446379159 | 156 | 504990 | -81.17 | 14.89 | 522.10 | 0.17 | 2.09 | 1565 |
| 2024-09-20 22:21:41.664 | MS1 | 121.4656587625 | 31.1446279583 | 156 | 504990 | -79.91 | 14.47 | 403.12 | 0.18 | 2.83 | 1599 |
| 2024-09-20 22:21:42.864 | MS1 | 121.4656690269 | 31.1446312905 | 156 | 504990 | -81.39 | 14.04 | 557.94 | 0.01 | 2.83 | 1588 |

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
| 3216538 | 2 | 121.4706267802 | 31.1548721853 | 255 | 11 | 6 | 24.5 | TDD | 475 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3238821 | 1 | 121.4718626384 | 31.1479139214 | 267 | 14 | 10 | 30.0 | TDD | 156 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3254319 | 3 | 121.4698953666 | 31.1530086553 | 162 | 2 | 5 | 17.2 | TDD | 436 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3262356 | 4 | 121.4721100489 | 31.1530533668 | 198 | 3 | 6 | 19.7 | TDD | 511 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.830 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.847 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.981 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.981 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.688 | NREventA3 | measId:2;ServCellPCI:85;Ser... |
| 2024-09-20 22:21:35.688 | NREventA3 | measId:2;ServCellPCI:85;Ser... |
| 2024-09-20 22:21:36.688 | NREventA3 | measId:2;ServCellPCI:85;Ser... |
| 2024-09-20 22:21:39.188 | NRRRCReestablishAttempt | PCI:85 |
| 2024-09-20 22:21:39.199 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.210 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.356 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.356 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238821 | 1 | 8.0867 | 18.2304 | -114.8661 | 12.1334 | 145.1550 | 0.0064 | 0.1331 |
| 2024_09_20 22:00 | 3216538 | 2 | 10.9293 | 15.2731 | -116.6450 | 14.8646 | 176.2573 | 0.0042 | 0.0155 |
| 2024_09_20 22:00 | 3254319 | 3 | 12.7460 | 19.7322 | -116.8867 | 7.3467 | 187.6459 | 0.0106 | 0.0139 |
| 2024_09_20 22:00 | 3262356 | 4 | 12.6680 | 13.0111 | -117.7424 | 12.0993 | 103.0924 | 0.0148 | 0.0008 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416833_91B0639F | 504990 | 156 | -93.1 | 504990 | 511 | -86.4 | 504990 | 436 | -92.7 | 504990 | 475 |
| MR_1774416833_20F9C989 | 504990 | 156 | -90.5 | 504990 | 511 | -85.6 | 504990 | 436 | -92.5 | 504990 | 475 |
| MR_1774416833_7F5F5711 | 504990 | 156 | -92.1 | 504990 | 511 | -87.2 | 504990 | 436 | -95.8 | 504990 | 475 |
| MR_1774416833_0901CD6D | 504990 | 156 | -93.2 | 504990 | 511 | -86.3 | 504990 | 436 | -93.2 | 504990 | 475 |
| MR_1774416833_63DD0DFA | 504990 | 511 | -87.1 | 504990 | 156 | -90.9 | 504990 | 436 | -95.0 | 504990 | 475 |
| MR_1774416833_3493FA4C | 504990 | 156 | -91.8 | 504990 | 511 | -85.5 | 504990 | 436 | -94.6 | 504990 | 475 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 168: `a209bd11-149...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a209bd11-1494-412b-a315-d272d0b0256b` |
| Tag | **multiple-answer** |
| 정답 | **C9|C15** |
| C9 의미 | Increase transmission power for 3264471_3 |
| C15 의미 | Adjust the azimuth of 3264471_3 by 39 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[168] topology](images/train_0168.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264471_3
- `C2`: Adjust the azimuth of 3220518_1 by 20 degrees
- `C3`: Press down the tilt angle of 3264471_3 by 7 degrees
- `C4`: Decrease A3 Offset threshold for 3220518_1
- `C5`: Press down the tilt angle  of 3220518_1 by 4 degrees
- `C6`: Check test server and transmission issues
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220518_1
- `C8`: Increase A3 Offset threshold for 3220518_1
- `C9`: Increase transmission power for 3264471_3 **← 정답**
- `C10`: Add neighbor relationship between 3264471_3 and 3220518_1
- `C11`: Decrease transmission power for 3264471_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220518_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264471_3
- `C14`: Lift the tilt angle  of 3220518_1 by 4 degrees
- `C15`: Adjust the azimuth of 3264471_3 by 39 degrees **← 정답**
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Lift the tilt angle of 3264471_3 by 7 degrees
- `C18`: Increase transmission power for 3220518_1
- `C19`: Increase A3 Offset threshold for 3264471_3
- `C20`: Decrease A3 Offset threshold for 3264471_3
- `C21`: Add neighbor relationship between 3210829_4 and 3220518_1
- `C22`: Decrease transmission power for 3220518_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.770 | MS1 | 121.4656663283 | 31.1446374185 | 990 | 504990 | -85.69 | 13.31 | 447.24 | 0.19 | 2.61 | 1582 |
| 2024-09-20 22:21:32.641 | MS1 | 121.4656741787 | 31.1446379407 | 990 | 504990 | -94.80 | 13.22 | 382.26 | 0.04 | 2.85 | 1574 |
| 2024-09-20 22:21:33.897 | MS1 | 121.4656721564 | 31.1446227362 | 990 | 504990 | -86.10 | 15.32 | 355.89 | 0.18 | 2.65 | 1586 |
| 2024-09-20 22:21:34.398 | MS1 | 121.4656654289 | 31.1446338852 | 990 | 504990 | -106.23 | 1.24 | 74.11 | 0.14 | 1.29 | 1586 |
| 2024-09-20 22:21:35.606 | MS1 | 121.4656726471 | 31.1446342338 | 990 | 504990 | -101.71 | 1.35 | 28.40 | 0.03 | 1.31 | 1583 |
| 2024-09-20 22:21:36.279 | MS1 | 121.4656640715 | 31.1446200366 | 990 | 504990 | -104.20 | -0.73 | 17.90 | 0.11 | 1.34 | 1575 |
| 2024-09-20 22:21:37.547 | MS1 | 121.4656596332 | 31.1446286893 | 990 | 504990 | -108.36 | 0.49 | 50.08 | 0.03 | 1.38 | 1571 |
| 2024-09-20 22:21:38.154 | MS1 | 121.4656775325 | 31.1446342365 | 990 | 504990 | -102.32 | 0.94 | 78.63 | 0.06 | 1.20 | 1590 |
| 2024-09-20 22:21:39.805 | MS1 | 121.4656723483 | 31.1446203834 | 990 | 504990 | -103.46 | 1.06 | 32.03 | 0.05 | 1.18 | 1578 |
| 2024-09-20 22:21:40.811 | MS1 | 121.4656701359 | 31.1446347380 | 990 | 504990 | -90.62 | 13.79 | 454.12 | 0.16 | 2.85 | 1583 |
| 2024-09-20 22:21:41.772 | MS1 | 121.4656737061 | 31.1446268243 | 990 | 504990 | -85.31 | 17.21 | 389.55 | 0.07 | 2.91 | 1586 |
| 2024-09-20 22:21:42.678 | MS1 | 121.4656676952 | 31.1446202360 | 990 | 504990 | -91.76 | 12.05 | 398.74 | 0.08 | 2.02 | 1576 |

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
| 3210829 | 4 | 121.4751124586 | 31.1511284304 | 217 | 13 | 7 | 27.4 | TDD | 454 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3220518 | 1 | 121.4672566588 | 31.1540434308 | 168 | 2 | 1 | 41.6 | TDD | 972 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3264471 | 3 | 121.4743177618 | 31.1495474606 | 275 | 4 | 11 | 43.2 | TDD | 990 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3277794 | 2 | 121.4743611739 | 31.1503235008 | 59 | 6 | 11 | 18.3 | TDD | 164 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.762 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.781 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.918 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.918 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.138 | NREventA2 | measId:1;ServCellPCI:733;Se... |
| 2024-09-20 22:21:34.254 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220518 | 1 | 7.7485 | 7.2694 | -115.6923 | 7.5552 | 120.2586 | 0.0080 | 0.0088 |
| 2024_09_20 22:00 | 3277794 | 2 | 7.1107 | 14.2493 | -117.7985 | 10.2740 | 158.1678 | 0.0013 | 0.0051 |
| 2024_09_20 22:00 | 3264471 | 3 | 18.4064 | 15.4719 | -114.1422 | 12.5528 | 125.3751 | 0.1081 | 0.0139 |
| 2024_09_20 22:00 | 3210829 | 4 | 17.5669 | 18.6701 | -114.3977 | 17.9611 | 120.1222 | 0.0028 | 0.0021 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412738_7FD86823 | 504990 | 990 | -105.0 | 504990 | 972 | -109.1 | 504990 | 454 | -116.7 | 504990 | 164 |
| MR_1774412738_4C07EC77 | 504990 | 990 | -107.5 | 504990 | 972 | -111.2 | 504990 | 454 | -118.8 | 504990 | 164 |
| MR_1774412738_FA672B59 | 504990 | 990 | -104.4 | 504990 | 972 | -109.9 | 504990 | 454 | -118.2 | 504990 | 164 |
| MR_1774412738_8AC96B2E | 504990 | 990 | -105.9 | 504990 | 972 | -111.7 | 504990 | 454 | -116.3 | 504990 | 164 |
| MR_1774412738_BB41DB7D | 504990 | 990 | -106.0 | 504990 | 972 | -113.0 | 504990 | 454 | -117.0 | 504990 | 164 |
| MR_1774412738_BC659DD6 | 504990 | 990 | -105.1 | 504990 | 972 | -110.6 | 504990 | 454 | -118.7 | 504990 | 164 |
| MR_1774412738_0F484402 | 504990 | 990 | -105.8 | 504990 | 972 | -111.5 | 504990 | 454 | -116.7 | 504990 | 164 |
| MR_1774412738_1607F485 | 504990 | 990 | -107.5 | 504990 | 972 | -112.2 | 504990 | 454 | -116.7 | 504990 | 164 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 169: `b08cd826-2b3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b08cd826-2b3e-4a5e-8b23-ea7412148501` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[169] topology](images/train_0169.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3276630_4
- `C2`: Adjust the azimuth of 3215931_3 by 23 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215931_3
- `C4`: Increase transmission power for 3276630_4
- `C5`: Press down the tilt angle of 3276630_4 by 1 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276630_4
- `C7`: Lift the tilt angle  of 3215931_3 by 10 degrees
- `C8`: Insufficient data; more data is needed for judgment. **← 정답**
- `C9`: Decrease transmission power for 3215931_3
- `C10`: Adjust the azimuth of 3276630_4 by 24 degrees
- `C11`: Increase transmission power for 3215931_3
- `C12`: Lift the tilt angle of 3276630_4 by 1 degrees
- `C13`: Increase A3 Offset threshold for 3276630_4
- `C14`: Add neighbor relationship between 3270738_1 and 3215931_3
- `C15`: Decrease A3 Offset threshold for 3215931_3
- `C16`: Decrease transmission power for 3276630_4
- `C17`: Check test server and transmission issues
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215931_3
- `C19`: Add neighbor relationship between 3276630_4 and 3215931_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276630_4
- `C21`: Increase A3 Offset threshold for 3215931_3
- `C22`: Press down the tilt angle  of 3215931_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.471 | MS1 | 121.4656751894 | 31.1446180670 | 820 | 504990 | -88.47 | 16.91 | 570.40 | 0.04 | 2.32 | 1588 |
| 2024-09-20 22:21:32.731 | MS1 | 121.4656638689 | 31.1446351491 | 820 | 504990 | -91.17 | 12.18 | 307.58 | 0.13 | 2.67 | 1562 |
| 2024-09-20 22:21:33.549 | MS1 | 121.4656748427 | 31.1446362940 | 820 | 504990 | -91.83 | 13.64 | 525.51 | 0.18 | 2.07 | 1599 |
| 2024-09-20 22:21:34.330 | MS1 | 121.4656757142 | 31.1446295847 | 820 | 504990 | -88.12 | 12.45 | 100.69 | 0.02 | 2.88 | 1564 |
| 2024-09-20 22:21:35.784 | MS1 | 121.4656717603 | 31.1446250124 | 820 | 504990 | -91.07 | 14.38 | 70.74 | 0.19 | 2.71 | 1586 |
| 2024-09-20 22:21:36.648 | MS1 | 121.4656610659 | 31.1446265115 | 820 | 504990 | -87.67 | 14.25 | 92.51 | 0.12 | 2.47 | 1584 |
| 2024-09-20 22:21:37.623 | MS1 | 121.4656720531 | 31.1446343588 | 820 | 504990 | -90.90 | 10.10 | 66.20 | 0.12 | 2.05 | 1560 |
| 2024-09-20 22:21:38.108 | MS1 | 121.4656708487 | 31.1446226940 | 820 | 504990 | -92.38 | 11.90 | 56.47 | 0.13 | 2.62 | 1581 |
| 2024-09-20 22:21:39.304 | MS1 | 121.4656769205 | 31.1446233451 | 820 | 504990 | -93.06 | 9.91 | 64.14 | 0.07 | 2.59 | 1592 |
| 2024-09-20 22:21:40.984 | MS1 | 121.4656737700 | 31.1446219638 | 820 | 504990 | -92.36 | 12.27 | 585.97 | 0.01 | 2.16 | 1591 |
| 2024-09-20 22:21:41.409 | MS1 | 121.4656664142 | 31.1446293676 | 820 | 504990 | -90.31 | 8.72 | 603.98 | 0.19 | 2.97 | 1581 |
| 2024-09-20 22:21:42.146 | MS1 | 121.4656659298 | 31.1446281585 | 820 | 504990 | -91.65 | 12.99 | 480.78 | 0.08 | 2.07 | 1595 |

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
| 3215931 | 3 | 121.4682285725 | 31.1538839318 | 170 | 11 | 4 | 37.4 | TDD | 429 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3228615 | 2 | 121.4699063376 | 31.1444288583 | 270 | 9 | 9 | 15.6 | TDD | 972 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3270738 | 1 | 121.4751376052 | 31.1553160928 | 134 | 1 | 0 | 30.5 | TDD | 62 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3276630 | 4 | 121.4758459882 | 31.1530674769 | 250 | 0 | 5 | 26.7 | TDD | 820 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.466 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.488 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.588 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.588 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.328 | NREventA3 | measId:2;ServCellPCI:421;Se... |
| 2024-09-20 22:21:38.568 | NRHandoverAttempt | SourcePCI:421;SourceNR-ARFC... |
| 2024-09-20 22:21:38.611 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.623 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.755 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.755 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3270738 | 1 | 78.5144 | 94.0511 | -117.4405 | 17.9022 | 101.5638 | 0.0199 | 0.0037 |
| 2024_09_19 22:00 | 3228615 | 2 | 91.4461 | 92.8057 | -115.1550 | 9.3421 | 164.0255 | 0.0130 | 0.0001 |
| 2024_09_19 22:00 | 3215931 | 3 | 90.7090 | 79.5962 | -116.0127 | 5.4710 | 136.9920 | 0.0045 | 0.0097 |
| 2024_09_19 22:00 | 3276630 | 4 | 86.6211 | 80.5753 | -114.3056 | 11.5072 | 95.1043 | 0.0086 | 0.0131 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415025_F7DB4482 | 504990 | 820 | -89.7 | 504990 | 429 | -97.9 | 504990 | 62 | -98.3 | 504990 | 972 |
| MR_1774415025_A3760C35 | 504990 | 820 | -92.4 | 504990 | 429 | -100.4 | 504990 | 62 | -99.4 | 504990 | 972 |
| MR_1774415025_5D1500C1 | 504990 | 820 | -92.9 | 504990 | 429 | -99.0 | 504990 | 62 | -101.7 | 504990 | 972 |
| MR_1774415025_61B660E9 | 504990 | 820 | -90.9 | 504990 | 429 | -99.6 | 504990 | 62 | -98.0 | 504990 | 972 |
| MR_1774415025_14809778 | 504990 | 820 | -91.0 | 504990 | 429 | -100.0 | 504990 | 62 | -98.9 | 504990 | 972 |
| MR_1774415025_737CE857 | 504990 | 820 | -91.4 | 504990 | 429 | -99.9 | 504990 | 62 | -101.5 | 504990 | 972 |
| MR_1774415025_456CA769 | 504990 | 820 | -92.7 | 504990 | 429 | -97.7 | 504990 | 62 | -99.0 | 504990 | 972 |
| MR_1774415025_6A7E0B70 | 504990 | 820 | -90.9 | 504990 | 429 | -98.8 | 504990 | 62 | -101.7 | 504990 | 972 |

> *... 2개 열 생략 (전체 14열)*

---
