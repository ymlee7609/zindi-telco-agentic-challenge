# Track A 문제 분석 — train[980]~train[989]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[980] ~ train[989] (10개)

## 목차

1. [문제 980: `4e8772ee-e47...`](#980) — single-answer, 정답: C3
2. [문제 981: `a9ec59f2-05d...`](#981) — single-answer, 정답: C10
3. [문제 982: `d6cf15dd-ee3...`](#982) — single-answer, 정답: C6
4. [문제 983: `486655f1-ed1...`](#983) — single-answer, 정답: C4
5. [문제 984: `8f75dc83-130...`](#984) — single-answer, 정답: C2
6. [문제 985: `9cdf0db6-271...`](#985) — single-answer, 정답: C21
7. [문제 986: `a62642c2-a74...`](#986) — single-answer, 정답: C12
8. [문제 987: `e29f8915-143...`](#987) — single-answer, 정답: C8
9. [문제 988: `73a04f62-cc7...`](#988) — single-answer, 정답: C1
10. [문제 989: `928269be-a7c...`](#989) — single-answer, 정답: C14

---

### 문제 980: `4e8772ee-e47...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4e8772ee-e47d-4de4-9590-794a145d3f6a` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Add neighbor relationship between 3265500_4 and 3243113_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[980] topology](images/train_0980.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase A3 Offset threshold for 3243113_1
- `C3`: Add neighbor relationship between 3265500_4 and 3243113_1 **← 정답**
- `C4`: Increase A3 Offset threshold for 3265500_4
- `C5`: Decrease transmission power for 3265500_4
- `C6`: Add neighbor relationship between 3272783_2 and 3243113_1
- `C7`: Decrease A3 Offset threshold for 3243113_1
- `C8`: Decrease A3 Offset threshold for 3265500_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243113_1
- `C10`: Adjust the azimuth of 3265500_4 by 50 degrees
- `C11`: Check test server and transmission issues
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243113_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265500_4
- `C14`: Press down the tilt angle of 3265500_4 by 7 degrees
- `C15`: Increase transmission power for 3243113_1
- `C16`: Lift the tilt angle  of 3243113_1 by 5 degrees
- `C17`: Lift the tilt angle of 3265500_4 by 7 degrees
- `C18`: Adjust the azimuth of 3243113_1 by 12 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265500_4
- `C20`: Increase transmission power for 3265500_4
- `C21`: Decrease transmission power for 3243113_1
- `C22`: Press down the tilt angle  of 3243113_1 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.199 | MS1 | 121.4656721809 | 31.1446260348 | 750 | 504990 | -77.19 | 12.61 | 364.08 | 0.08 | 2.14 | 1597 |
| 2024-09-20 22:21:32.596 | MS1 | 121.4656659344 | 31.1446274215 | 750 | 504990 | -75.06 | 13.16 | 372.85 | 0.18 | 2.21 | 1596 |
| 2024-09-20 22:21:33.839 | MS1 | 121.4656763540 | 31.1446326627 | 750 | 504990 | -84.04 | 16.41 | 306.23 | 0.15 | 2.64 | 1599 |
| 2024-09-20 22:21:34.379 | MS1 | 121.4656607507 | 31.1446335451 | 750 | 504990 | -94.92 | -3.26 | 63.99 | 0.01 | 1.45 | 1586 |
| 2024-09-20 22:21:35.605 | MS1 | 121.4656648394 | 31.1446288929 | 750 | 504990 | -93.51 | -2.40 | 59.98 | 0.11 | 1.46 | 1561 |
| 2024-09-20 22:21:36.289 | MS1 | 121.4656673583 | 31.1446280114 | 750 | 504990 | -87.59 | -3.66 | 55.51 | 0.10 | 1.39 | 1564 |
| 2024-09-20 22:21:37.362 | MS1 | 121.4656771594 | 31.1446222073 | 750 | 504990 | -87.66 | -2.19 | 46.59 | 0.12 | 1.49 | 1582 |
| 2024-09-20 22:21:38.363 | MS1 | 121.4656617889 | 31.1446327352 | 750 | 504990 | -75.95 | 12.00 | 529.39 | 0.06 | 1.05 | 1594 |
| 2024-09-20 22:21:39.737 | MS1 | 121.4656626556 | 31.1446186512 | 750 | 504990 | -82.40 | 17.36 | 507.02 | 0.00 | 1.04 | 1593 |
| 2024-09-20 22:21:40.887 | MS1 | 121.4656745414 | 31.1446289743 | 750 | 504990 | -77.85 | 17.47 | 509.36 | 0.09 | 2.02 | 1576 |
| 2024-09-20 22:21:41.805 | MS1 | 121.4656620956 | 31.1446237491 | 750 | 504990 | -78.79 | 17.28 | 335.50 | 0.12 | 2.14 | 1575 |
| 2024-09-20 22:21:42.128 | MS1 | 121.4656610840 | 31.1446226091 | 750 | 504990 | -79.89 | 13.14 | 493.59 | 0.08 | 2.69 | 1567 |

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
| 3243113 | 1 | 121.4712735672 | 31.1485054244 | 243 | 3 | 10 | 22.4 | TDD | 242 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3265500 | 4 | 121.4668032273 | 31.1499347402 | 34 | 5 | 6 | 22.9 | TDD | 750 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3272783 | 2 | 121.4662660251 | 31.1515375516 | 278 | 11 | 5 | 34.5 | TDD | 483 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3278919 | 3 | 121.4745632232 | 31.1512023924 | 325 | 3 | 12 | 49.8 | TDD | 684 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.891 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.916 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.052 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.052 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.705 | NREventA3 | measId:2;ServCellPCI:562;Se... |
| 2024-09-20 22:21:35.705 | NREventA3 | measId:2;ServCellPCI:562;Se... |
| 2024-09-20 22:21:36.705 | NREventA3 | measId:2;ServCellPCI:562;Se... |
| 2024-09-20 22:21:39.205 | NRRRCReestablishAttempt | PCI:562 |
| 2024-09-20 22:21:39.225 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.238 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.388 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.388 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243113 | 1 | 11.8629 | 16.1517 | -114.8745 | 13.0377 | 117.8457 | 0.0127 | 0.0054 |
| 2024_09_20 22:00 | 3272783 | 2 | 18.8319 | 17.5911 | -114.2956 | 17.9751 | 189.7233 | 0.0081 | 0.0134 |
| 2024_09_20 22:00 | 3278919 | 3 | 16.0269 | 8.9330 | -117.5909 | 11.2997 | 139.9445 | 0.0007 | 0.0059 |
| 2024_09_20 22:00 | 3265500 | 4 | 14.2953 | 9.7546 | -115.1336 | 12.9553 | 86.4351 | 0.0105 | 0.1773 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416751_7EBA1522 | 504990 | 242 | -87.4 | 504990 | 750 | -93.9 | 504990 | 483 | -97.8 | 504990 | 684 |
| MR_1774416751_469A0E28 | 504990 | 750 | -93.5 | 504990 | 242 | -89.4 | 504990 | 483 | -98.5 | 504990 | 684 |
| MR_1774416751_4CA76C12 | 504990 | 750 | -96.5 | 504990 | 242 | -87.5 | 504990 | 483 | -97.3 | 504990 | 684 |
| MR_1774416751_69060093 | 504990 | 242 | -89.8 | 504990 | 750 | -96.0 | 504990 | 483 | -99.5 | 504990 | 684 |
| MR_1774416751_0909AEDB | 504990 | 750 | -94.9 | 504990 | 242 | -88.3 | 504990 | 483 | -97.0 | 504990 | 684 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 981: `a9ec59f2-05d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a9ec59f2-05d5-4033-893b-56d4d65f455d` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[981] topology](images/train_0981.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3230491_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230491_4
- `C3`: Lift the tilt angle of 3230491_4 by 5 degrees
- `C4`: Add neighbor relationship between 3278206_1 and 3274485_2
- `C5`: Lift the tilt angle  of 3274485_2 by 10 degrees
- `C6`: Decrease A3 Offset threshold for 3274485_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274485_2
- `C8`: Increase A3 Offset threshold for 3274485_2
- `C9`: Increase transmission power for 3230491_4
- `C10`: Check test server and transmission issues **← 정답**
- `C11`: Decrease transmission power for 3274485_2
- `C12`: Press down the tilt angle of 3230491_4 by 5 degrees
- `C13`: Press down the tilt angle  of 3274485_2 by 10 degrees
- `C14`: Adjust the azimuth of 3230491_4 by 50 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274485_2
- `C16`: Add neighbor relationship between 3230491_4 and 3274485_2
- `C17`: Adjust the azimuth of 3274485_2 by 50 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230491_4
- `C19`: Decrease transmission power for 3230491_4
- `C20`: Increase transmission power for 3274485_2
- `C21`: Decrease A3 Offset threshold for 3230491_4
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.840 | MS1 | 121.4656643155 | 31.1446291338 | 958 | 504990 | -90.89 | 13.69 | 466.25 | 0.19 | 2.31 | 1579 |
| 2024-09-20 22:21:32.302 | MS1 | 121.4656659699 | 31.1446227830 | 958 | 504990 | -90.84 | 16.22 | 330.91 | 0.04 | 2.03 | 1597 |
| 2024-09-20 22:21:33.325 | MS1 | 121.4656704999 | 31.1446190831 | 958 | 504990 | -91.65 | 12.08 | 476.06 | 0.09 | 2.80 | 1563 |
| 2024-09-20 22:21:34.502 | MS1 | 121.4656632446 | 31.1446355595 | 958 | 504990 | -87.77 | 16.17 | 71.06 | 0.06 | 2.87 | 439 |
| 2024-09-20 22:21:35.743 | MS1 | 121.4656703802 | 31.1446334939 | 958 | 504990 | -87.46 | 12.09 | 93.70 | 0.17 | 2.61 | 321 |
| 2024-09-20 22:21:36.116 | MS1 | 121.4656714259 | 31.1446183005 | 958 | 504990 | -86.30 | 13.97 | 76.41 | 0.03 | 2.73 | 329 |
| 2024-09-20 22:21:37.522 | MS1 | 121.4656707336 | 31.1446367501 | 958 | 504990 | -89.07 | 10.55 | 44.73 | 0.09 | 2.17 | 477 |
| 2024-09-20 22:21:38.419 | MS1 | 121.4656738674 | 31.1446374972 | 958 | 504990 | -91.61 | 10.24 | 91.68 | 0.06 | 2.40 | 498 |
| 2024-09-20 22:21:39.791 | MS1 | 121.4656593917 | 31.1446226156 | 958 | 504990 | -92.79 | 12.86 | 104.99 | 0.06 | 2.36 | 471 |
| 2024-09-20 22:21:40.944 | MS1 | 121.4656754236 | 31.1446207088 | 958 | 504990 | -89.50 | 12.09 | 390.90 | 0.04 | 2.22 | 1577 |
| 2024-09-20 22:21:41.420 | MS1 | 121.4656612364 | 31.1446296987 | 958 | 504990 | -93.08 | 9.63 | 523.17 | 0.18 | 2.93 | 1589 |
| 2024-09-20 22:21:42.781 | MS1 | 121.4656642601 | 31.1446251707 | 958 | 504990 | -91.07 | 10.54 | 441.98 | 0.16 | 2.52 | 1579 |

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
| 3230491 | 4 | 121.4717752002 | 31.1459177698 | 95 | 2 | 12 | 27.1 | TDD | 958 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3274108 | 3 | 121.4699015238 | 31.1525521858 | 38 | 10 | 7 | 16.7 | TDD | 901 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3274485 | 2 | 121.4758766587 | 31.1449061441 | 353 | 9 | 0 | 41.7 | TDD | 883 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3278206 | 1 | 121.4675292896 | 31.1500782266 | 344 | 7 | 3 | 18.7 | TDD | 521 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.216 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.346 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.346 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.008 | NREventA3 | measId:2;ServCellPCI:976;Se... |
| 2024-09-20 22:21:38.248 | NRHandoverAttempt | SourcePCI:976;SourceNR-ARFC... |
| 2024-09-20 22:21:38.298 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.310 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.456 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.456 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278206 | 1 | 18.5222 | 7.8032 | -116.6201 | 9.3309 | 196.1729 | 0.0190 | 0.0136 |
| 2024_09_20 22:00 | 3274485 | 2 | 7.6753 | 10.1419 | -117.8502 | 19.9969 | 194.6614 | 0.0156 | 0.0135 |
| 2024_09_20 22:00 | 3274108 | 3 | 15.7192 | 18.0842 | -115.0541 | 5.4927 | 142.6743 | 0.0175 | 0.0125 |
| 2024_09_20 22:00 | 3230491 | 4 | 8.8973 | 11.4320 | -114.1019 | 19.2893 | 196.1715 | 0.0081 | 0.0121 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414108_560CACDD | 504990 | 958 | -88.3 | 504990 | 883 | -93.7 | 504990 | 521 | -101.7 | 504990 | 901 |
| MR_1774414108_BA0CDB95 | 504990 | 958 | -88.6 | 504990 | 883 | -93.3 | 504990 | 521 | -102.8 | 504990 | 901 |
| MR_1774414108_857A4A70 | 504990 | 958 | -88.3 | 504990 | 883 | -92.1 | 504990 | 521 | -100.2 | 504990 | 901 |
| MR_1774414108_30378D30 | 504990 | 958 | -89.1 | 504990 | 883 | -93.8 | 504990 | 521 | -102.5 | 504990 | 901 |
| MR_1774414108_0F464410 | 504990 | 958 | -89.2 | 504990 | 883 | -92.9 | 504990 | 521 | -101.2 | 504990 | 901 |
| MR_1774414108_D86E956C | 504990 | 958 | -87.5 | 504990 | 883 | -93.6 | 504990 | 521 | -101.9 | 504990 | 901 |
| MR_1774414108_A49DC5AE | 504990 | 958 | -89.5 | 504990 | 883 | -95.2 | 504990 | 521 | -100.9 | 504990 | 901 |
| MR_1774414108_9D0AD6B4 | 504990 | 958 | -87.3 | 504990 | 883 | -93.9 | 504990 | 521 | -103.2 | 504990 | 901 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 982: `d6cf15dd-ee3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d6cf15dd-ee31-406a-bf65-cd0bc7011365` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease A3 Offset threshold for 3255083_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[982] topology](images/train_0982.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3255083_3
- `C2`: Add neighbor relationship between 3213726_2 and 3220473_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255083_3
- `C4`: Increase transmission power for 3255083_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220473_1
- `C6`: Decrease A3 Offset threshold for 3255083_3 **← 정답**
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Increase A3 Offset threshold for 3255083_3
- `C9`: Increase transmission power for 3220473_1
- `C10`: Adjust the azimuth of 3220473_1 by 50 degrees
- `C11`: Add neighbor relationship between 3255083_3 and 3220473_1
- `C12`: Adjust the azimuth of 3255083_3 by 50 degrees
- `C13`: Press down the tilt angle of 3255083_3 by 1 degrees
- `C14`: Decrease transmission power for 3220473_1
- `C15`: Check test server and transmission issues
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220473_1
- `C17`: Decrease A3 Offset threshold for 3220473_1
- `C18`: Increase A3 Offset threshold for 3220473_1
- `C19`: Lift the tilt angle  of 3220473_1 by 4 degrees
- `C20`: Lift the tilt angle of 3255083_3 by 1 degrees
- `C21`: Press down the tilt angle  of 3220473_1 by 4 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255083_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.467 | MS1 | 121.4656672509 | 31.1446263712 | 756 | 504990 | -81.07 | 14.30 | 526.46 | 0.14 | 2.49 | 1564 |
| 2024-09-20 22:21:32.349 | MS1 | 121.4656712100 | 31.1446305649 | 756 | 504990 | -80.69 | 12.19 | 475.36 | 0.17 | 2.99 | 1573 |
| 2024-09-20 22:21:33.175 | MS1 | 121.4656677497 | 31.1446192601 | 756 | 504990 | -75.95 | 12.54 | 523.57 | 0.12 | 2.93 | 1566 |
| 2024-09-20 22:21:34.676 | MS1 | 121.4656749189 | 31.1446183659 | 756 | 504990 | -92.96 | -2.84 | 54.78 | 0.12 | 1.15 | 1579 |
| 2024-09-20 22:21:35.302 | MS1 | 121.4656664061 | 31.1446356444 | 756 | 504990 | -90.17 | -3.66 | 66.26 | 0.03 | 1.20 | 1589 |
| 2024-09-20 22:21:36.909 | MS1 | 121.4656641788 | 31.1446193481 | 756 | 504990 | -84.32 | -0.67 | 38.83 | 0.19 | 1.07 | 1585 |
| 2024-09-20 22:21:37.112 | MS1 | 121.4656614254 | 31.1446244690 | 756 | 504990 | -83.69 | -0.59 | 63.99 | 0.08 | 1.36 | 1561 |
| 2024-09-20 22:21:38.778 | MS1 | 121.4656665645 | 31.1446324575 | 756 | 504990 | -92.19 | -3.61 | 37.33 | 0.12 | 1.45 | 1592 |
| 2024-09-20 22:21:39.951 | MS1 | 121.4656776690 | 31.1446266591 | 424 | 504990 | -80.49 | 16.79 | 242.38 | 0.08 | 1.27 | 1587 |
| 2024-09-20 22:21:40.393 | MS1 | 121.4656695013 | 31.1446354161 | 424 | 504990 | -81.80 | 13.30 | 584.06 | 0.18 | 2.66 | 1595 |
| 2024-09-20 22:21:41.651 | MS1 | 121.4656715452 | 31.1446264832 | 424 | 504990 | -75.57 | 15.51 | 350.60 | 0.15 | 2.75 | 1560 |
| 2024-09-20 22:21:42.681 | MS1 | 121.4656615499 | 31.1446285624 | 424 | 504990 | -84.72 | 13.90 | 313.93 | 0.08 | 2.63 | 1600 |

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
| 3213726 | 2 | 121.4698141739 | 31.1497582420 | 296 | 7 | 5 | 49.0 | TDD | 296 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3213751 | 4 | 121.4746688016 | 31.1525815138 | 286 | 8 | 0 | 36.7 | TDD | 28 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3220473 | 1 | 121.4717201942 | 31.1523288319 | 336 | 3 | 7 | 26.3 | TDD | 424 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3255083 | 3 | 121.4656813348 | 31.1523474443 | 303 | 0 | 12 | 18.8 | TDD | 756 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.502 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.524 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.666 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.666 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.388 | NREventA3 | measId:2;ServCellPCI:63;Ser... |
| 2024-09-20 22:21:38.628 | NRHandoverAttempt | SourcePCI:63;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.667 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.677 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.807 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.807 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220473 | 1 | 14.6927 | 9.0153 | -116.0970 | 15.4437 | 94.7194 | 0.0057 | 0.0148 |
| 2024_09_20 22:00 | 3213726 | 2 | 16.9159 | 8.7989 | -115.7945 | 13.9114 | 147.3551 | 0.0168 | 0.0052 |
| 2024_09_20 22:00 | 3255083 | 3 | 17.0912 | 18.7744 | -116.9129 | 8.2014 | 149.2067 | 0.0118 | 0.1700 |
| 2024_09_20 22:00 | 3213751 | 4 | 6.3877 | 7.8352 | -115.3414 | 19.2009 | 144.2868 | 0.0168 | 0.0017 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416741_612E593C | 504990 | 756 | -94.3 | 504990 | 424 | -89.7 | 504990 | 296 | -97.9 | 504990 | 28 |
| MR_1774416741_7E4CE0BD | 504990 | 424 | -88.5 | 504990 | 756 | -94.5 | 504990 | 296 | -95.3 | 504990 | 28 |
| MR_1774416741_3B3B5369 | 504990 | 756 | -94.8 | 504990 | 424 | -89.9 | 504990 | 296 | -94.3 | 504990 | 28 |
| MR_1774416741_0A1A49F6 | 504990 | 756 | -93.1 | 504990 | 424 | -87.0 | 504990 | 296 | -94.9 | 504990 | 28 |
| MR_1774416741_309BCDD8 | 504990 | 756 | -93.9 | 504990 | 424 | -86.4 | 504990 | 296 | -95.6 | 504990 | 28 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 983: `486655f1-ed1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `486655f1-ed13-4746-a305-a4b1c5d7cc67` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Lift the tilt angle  of 3223657_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[983] topology](images/train_0983.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3217842_2
- `C2`: Adjust the azimuth of 3217842_2 by 17 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244191_4
- `C4`: Lift the tilt angle  of 3223657_3 by 10 degrees **← 정답**
- `C5`: Increase A3 Offset threshold for 3217842_2
- `C6`: Increase transmission power for 3244191_4
- `C7`: Lift the tilt angle of 3217842_2 by 2 degrees
- `C8`: Increase transmission power for 3217842_2
- `C9`: Check test server and transmission issues
- `C10`: Adjust the azimuth of 3223657_3 by 50 degrees
- `C11`: Decrease transmission power for 3217842_2
- `C12`: Press down the tilt angle of 3217842_2 by 2 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244191_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217842_2
- `C16`: Increase A3 Offset threshold for 3244191_4
- `C17`: Add neighbor relationship between 3223657_3 and 3244191_4
- `C18`: Decrease A3 Offset threshold for 3244191_4
- `C19`: Decrease transmission power for 3244191_4
- `C20`: Press down the tilt angle  of 3223657_3 by 10 degrees
- `C21`: Add neighbor relationship between 3217842_2 and 3244191_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217842_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.898 | MS1 | 121.4656628301 | 31.1446248136 | 473 | 504990 | -91.62 | 16.69 | 448.79 | 0.07 | 2.07 | 1576 |
| 2024-09-20 22:21:32.916 | MS1 | 121.4656617332 | 31.1446311555 | 473 | 504990 | -91.12 | 14.39 | 574.72 | 0.13 | 2.65 | 1600 |
| 2024-09-20 22:21:33.359 | MS1 | 121.4656657320 | 31.1446192096 | 473 | 504990 | -85.47 | 13.86 | 588.61 | 0.04 | 2.06 | 1571 |
| 2024-09-20 22:21:34.335 | MS1 | 121.4656743276 | 31.1446312460 | 473 | 504990 | -88.63 | 12.06 | 72.22 | 0.05 | 2.50 | 1585 |
| 2024-09-20 22:21:35.911 | MS1 | 121.4656620006 | 31.1446238628 | 473 | 504990 | -87.22 | 14.77 | 81.91 | 0.09 | 2.46 | 1597 |
| 2024-09-20 22:21:36.932 | MS1 | 121.4656727982 | 31.1446188580 | 473 | 504990 | -91.62 | 12.69 | 66.14 | 0.08 | 2.59 | 1568 |
| 2024-09-20 22:21:37.979 | MS1 | 121.4656638573 | 31.1446331684 | 473 | 504990 | -92.84 | 10.49 | 84.36 | 0.03 | 2.57 | 1564 |
| 2024-09-20 22:21:38.582 | MS1 | 121.4656626352 | 31.1446180851 | 473 | 504990 | -90.19 | 12.64 | 77.74 | 0.06 | 2.45 | 1573 |
| 2024-09-20 22:21:39.708 | MS1 | 121.4656760477 | 31.1446260560 | 473 | 504990 | -90.67 | 8.69 | 97.74 | 0.15 | 2.67 | 1564 |
| 2024-09-20 22:21:40.507 | MS1 | 121.4656776445 | 31.1446379837 | 473 | 504990 | -92.44 | 7.48 | 446.14 | 0.03 | 2.94 | 1598 |
| 2024-09-20 22:21:41.173 | MS1 | 121.4656659697 | 31.1446377556 | 473 | 504990 | -92.92 | 8.15 | 488.65 | 0.12 | 2.24 | 1573 |
| 2024-09-20 22:21:42.119 | MS1 | 121.4656716146 | 31.1446336588 | 473 | 504990 | -89.89 | 10.95 | 599.05 | 0.19 | 2.17 | 1598 |

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
| 3217842 | 2 | 121.4743391532 | 31.1489637776 | 223 | 0 | 11 | 32.2 | TDD | 473 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3223657 | 3 | 121.4647404711 | 31.1504681057 | 49 | 9 | 11 | 34.7 | TDD | 357 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3244191 | 4 | 121.4657051739 | 31.1552648031 | 43 | 10 | 11 | 48.4 | TDD | 863 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3277826 | 1 | 121.4709923953 | 31.1546816103 | 91 | 8 | 6 | 40.2 | TDD | 968 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.071 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.091 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.206 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.206 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.892 | NREventA3 | measId:2;ServCellPCI:866;Se... |
| 2024-09-20 22:21:38.132 | NRHandoverAttempt | SourcePCI:866;SourceNR-ARFC... |
| 2024-09-20 22:21:38.174 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.188 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.308 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.308 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277826 | 1 | 6.0949 | 15.2642 | -115.8648 | 19.8937 | 144.5468 | 0.0036 | 0.0175 |
| 2024_09_20 22:00 | 3217842 | 2 | 82.9521 | 87.1547 | -117.2756 | 15.0426 | 148.0167 | 0.0080 | 0.0043 |
| 2024_09_20 22:00 | 3223657 | 3 | 7.1631 | 5.5178 | -116.1371 | 12.5124 | 115.2308 | 0.0054 | 0.0013 |
| 2024_09_20 22:00 | 3244191 | 4 | 17.9818 | 8.0868 | -115.8135 | 13.4498 | 116.8083 | 0.0138 | 0.0014 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412567_D08A412B | 504990 | 473 | -87.2 | 504990 | 863 | -96.4 | 504990 | 357 | -98.9 | 504990 | 968 |
| MR_1774412567_D5DF741F | 504990 | 473 | -89.3 | 504990 | 863 | -95.9 | 504990 | 357 | -98.9 | 504990 | 968 |
| MR_1774412567_5097FEA9 | 504990 | 473 | -89.3 | 504990 | 863 | -94.1 | 504990 | 357 | -98.6 | 504990 | 968 |
| MR_1774412567_6301BBAC | 504990 | 473 | -89.1 | 504990 | 863 | -94.2 | 504990 | 357 | -96.1 | 504990 | 968 |
| MR_1774412567_48649E6F | 504990 | 473 | -89.8 | 504990 | 863 | -92.5 | 504990 | 357 | -98.6 | 504990 | 968 |
| MR_1774412567_3B599A56 | 504990 | 473 | -90.4 | 504990 | 863 | -94.3 | 504990 | 357 | -99.5 | 504990 | 968 |
| MR_1774412567_BAA438B6 | 504990 | 473 | -88.6 | 504990 | 863 | -94.3 | 504990 | 357 | -95.9 | 504990 | 968 |
| MR_1774412567_78017DA9 | 504990 | 473 | -89.8 | 504990 | 863 | -96.4 | 504990 | 357 | -96.7 | 504990 | 968 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 984: `8f75dc83-130...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8f75dc83-1302-40f7-9a34-3b7595f8971e` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[984] topology](images/train_0984.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3233206_1 by 10 degrees
- `C2`: Insufficient data; more data is needed for judgment. **← 정답**
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233206_1
- `C4`: Decrease transmission power for 3276938_3
- `C5`: Increase A3 Offset threshold for 3233206_1
- `C6`: Increase transmission power for 3276938_3
- `C7`: Add neighbor relationship between 3220158_2 and 3233206_1
- `C8`: Add neighbor relationship between 3276938_3 and 3233206_1
- `C9`: Increase A3 Offset threshold for 3276938_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233206_1
- `C11`: Decrease transmission power for 3233206_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276938_3
- `C13`: Adjust the azimuth of 3276938_3 by 50 degrees
- `C14`: Lift the tilt angle of 3276938_3 by 10 degrees
- `C15`: Lift the tilt angle  of 3233206_1 by 10 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276938_3
- `C17`: Decrease A3 Offset threshold for 3276938_3
- `C18`: Adjust the azimuth of 3233206_1 by 50 degrees
- `C19`: Decrease A3 Offset threshold for 3233206_1
- `C20`: Check test server and transmission issues
- `C21`: Increase transmission power for 3233206_1
- `C22`: Press down the tilt angle of 3276938_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.500 | MS1 | 121.4656702844 | 31.1446348537 | 597 | 504990 | -85.98 | 17.21 | 348.11 | 0.11 | 2.03 | 1598 |
| 2024-09-20 22:21:32.684 | MS1 | 121.4656748312 | 31.1446264615 | 597 | 504990 | -89.32 | 16.27 | 335.79 | 0.11 | 2.99 | 1598 |
| 2024-09-20 22:21:33.297 | MS1 | 121.4656689494 | 31.1446273670 | 597 | 504990 | -85.34 | 15.90 | 360.49 | 0.02 | 2.68 | 1579 |
| 2024-09-20 22:21:34.942 | MS1 | 121.4656695767 | 31.1446259392 | 597 | 504990 | -87.96 | 16.87 | 88.56 | 0.14 | 2.99 | 1564 |
| 2024-09-20 22:21:35.794 | MS1 | 121.4656753455 | 31.1446352907 | 597 | 504990 | -85.45 | 12.40 | 67.91 | 0.19 | 2.96 | 1581 |
| 2024-09-20 22:21:36.485 | MS1 | 121.4656758504 | 31.1446267971 | 597 | 504990 | -87.23 | 15.03 | 88.81 | 0.03 | 2.86 | 1586 |
| 2024-09-20 22:21:37.883 | MS1 | 121.4656715922 | 31.1446256775 | 597 | 504990 | -92.59 | 9.63 | 61.25 | 0.20 | 2.49 | 1568 |
| 2024-09-20 22:21:38.107 | MS1 | 121.4656621817 | 31.1446308375 | 597 | 504990 | -89.64 | 8.51 | 91.64 | 0.12 | 2.78 | 1596 |
| 2024-09-20 22:21:39.791 | MS1 | 121.4656620873 | 31.1446333230 | 597 | 504990 | -93.82 | 11.36 | 69.35 | 0.17 | 2.01 | 1595 |
| 2024-09-20 22:21:40.578 | MS1 | 121.4656716024 | 31.1446357440 | 597 | 504990 | -90.58 | 8.59 | 375.26 | 0.10 | 2.45 | 1576 |
| 2024-09-20 22:21:41.276 | MS1 | 121.4656634642 | 31.1446315654 | 597 | 504990 | -92.65 | 11.32 | 324.92 | 0.20 | 2.68 | 1592 |
| 2024-09-20 22:21:42.190 | MS1 | 121.4656699284 | 31.1446326244 | 597 | 504990 | -92.53 | 7.72 | 467.42 | 0.05 | 2.63 | 1565 |

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
| 3220158 | 2 | 121.4740670410 | 31.1497844135 | 89 | 3 | 0 | 32.3 | TDD | 537 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3233206 | 1 | 121.4653830849 | 31.1515608967 | 289 | 10 | 7 | 28.4 | TDD | 640 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3276938 | 3 | 121.4743561707 | 31.1455006586 | 333 | 14 | 3 | 47.9 | TDD | 597 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3279490 | 4 | 121.4712468629 | 31.1487296867 | 53 | 5 | 9 | 33.5 | TDD | 638 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.053 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.177 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.177 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.856 | NREventA3 | measId:2;ServCellPCI:811;Se... |
| 2024-09-20 22:21:38.096 | NRHandoverAttempt | SourcePCI:811;SourceNR-ARFC... |
| 2024-09-20 22:21:38.146 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.161 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.310 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.310 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3233206 | 1 | 87.0869 | 75.2741 | -117.0754 | 9.2714 | 84.0088 | 0.0065 | 0.0019 |
| 2024_09_19 22:00 | 3220158 | 2 | 89.0604 | 84.0682 | -117.3814 | 9.4588 | 117.5843 | 0.0194 | 0.0036 |
| 2024_09_19 22:00 | 3276938 | 3 | 82.7613 | 84.9631 | -117.9958 | 17.5392 | 122.4325 | 0.0006 | 0.0155 |
| 2024_09_19 22:00 | 3279490 | 4 | 90.8758 | 83.1991 | -114.1494 | 5.4546 | 136.1192 | 0.0072 | 0.0160 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414410_442F313E | 504990 | 597 | -87.6 | 504990 | 640 | -87.9 | 504990 | 537 | -96.1 | 504990 | 638 |
| MR_1774414410_A3CF8E7F | 504990 | 597 | -87.6 | 504990 | 640 | -89.4 | 504990 | 537 | -93.8 | 504990 | 638 |
| MR_1774414410_4E5C88A3 | 504990 | 597 | -88.7 | 504990 | 640 | -89.4 | 504990 | 537 | -95.5 | 504990 | 638 |
| MR_1774414410_9C64C150 | 504990 | 597 | -86.0 | 504990 | 640 | -88.3 | 504990 | 537 | -94.8 | 504990 | 638 |
| MR_1774414410_39FFED10 | 504990 | 597 | -86.6 | 504990 | 640 | -88.8 | 504990 | 537 | -95.4 | 504990 | 638 |
| MR_1774414410_01E7057C | 504990 | 597 | -89.0 | 504990 | 640 | -86.6 | 504990 | 537 | -95.6 | 504990 | 638 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 985: `9cdf0db6-271...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9cdf0db6-2714-467f-887c-6e8e9a848150` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Lift the tilt angle  of 3214860_4 by 8 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[985] topology](images/train_0985.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276070_1
- `C3`: Add neighbor relationship between 3214860_4 and 3276070_1
- `C4`: Press down the tilt angle of 3268763_3 by 6 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268763_3
- `C6`: Increase A3 Offset threshold for 3276070_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268763_3
- `C8`: Decrease transmission power for 3276070_1
- `C9`: Increase transmission power for 3268763_3
- `C10`: Press down the tilt angle  of 3214860_4 by 8 degrees
- `C11`: Decrease A3 Offset threshold for 3268763_3
- `C12`: Add neighbor relationship between 3268763_3 and 3276070_1
- `C13`: Lift the tilt angle of 3268763_3 by 6 degrees
- `C14`: Adjust the azimuth of 3214860_4 by 50 degrees
- `C15`: Adjust the azimuth of 3268763_3 by 22 degrees
- `C16`: Decrease A3 Offset threshold for 3276070_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276070_1
- `C18`: Decrease transmission power for 3268763_3
- `C19`: Increase A3 Offset threshold for 3268763_3
- `C20`: Check test server and transmission issues
- `C21`: Lift the tilt angle  of 3214860_4 by 8 degrees **← 정답**
- `C22`: Increase transmission power for 3276070_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.792 | MS1 | 121.4656652242 | 31.1446328153 | 581 | 504990 | -89.30 | 15.31 | 464.53 | 0.08 | 2.80 | 1564 |
| 2024-09-20 22:21:32.674 | MS1 | 121.4656683803 | 31.1446230084 | 581 | 504990 | -87.87 | 14.15 | 586.17 | 0.17 | 2.16 | 1598 |
| 2024-09-20 22:21:33.354 | MS1 | 121.4656610397 | 31.1446287876 | 581 | 504990 | -89.46 | 16.45 | 374.22 | 0.14 | 2.81 | 1562 |
| 2024-09-20 22:21:34.325 | MS1 | 121.4656581261 | 31.1446379345 | 581 | 504990 | -85.27 | 13.77 | 89.62 | 0.07 | 2.88 | 1562 |
| 2024-09-20 22:21:35.618 | MS1 | 121.4656755291 | 31.1446366763 | 581 | 504990 | -91.12 | 13.00 | 47.18 | 0.02 | 2.24 | 1596 |
| 2024-09-20 22:21:36.633 | MS1 | 121.4656609387 | 31.1446319385 | 581 | 504990 | -91.47 | 14.95 | 50.52 | 0.01 | 2.23 | 1562 |
| 2024-09-20 22:21:37.394 | MS1 | 121.4656729989 | 31.1446259403 | 581 | 504990 | -91.00 | 7.64 | 46.55 | 0.19 | 2.17 | 1599 |
| 2024-09-20 22:21:38.202 | MS1 | 121.4656680449 | 31.1446377120 | 581 | 504990 | -89.03 | 10.21 | 93.79 | 0.00 | 2.35 | 1572 |
| 2024-09-20 22:21:39.156 | MS1 | 121.4656767636 | 31.1446225622 | 581 | 504990 | -89.73 | 8.87 | 72.84 | 0.06 | 2.71 | 1593 |
| 2024-09-20 22:21:40.368 | MS1 | 121.4656702340 | 31.1446223346 | 581 | 504990 | -89.72 | 12.32 | 299.04 | 0.02 | 2.33 | 1588 |
| 2024-09-20 22:21:41.857 | MS1 | 121.4656767355 | 31.1446182609 | 581 | 504990 | -91.74 | 8.66 | 343.55 | 0.06 | 2.63 | 1596 |
| 2024-09-20 22:21:42.900 | MS1 | 121.4656597824 | 31.1446327593 | 581 | 504990 | -89.64 | 7.47 | 411.65 | 0.00 | 2.61 | 1562 |

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
| 3213301 | 2 | 121.4719206426 | 31.1520010921 | 308 | 1 | 8 | 44.2 | TDD | 892 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3214860 | 4 | 121.4659855940 | 31.1558587955 | 9 | 10 | 1 | 46.5 | TDD | 84 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3268763 | 3 | 121.4709245453 | 31.1444956301 | 294 | 3 | 4 | 23.2 | TDD | 581 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3276070 | 1 | 121.4699710111 | 31.1465708867 | 186 | 4 | 11 | 31.3 | TDD | 504 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.419 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.442 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.573 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.573 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.249 | NREventA3 | measId:2;ServCellPCI:723;Se... |
| 2024-09-20 22:21:38.489 | NRHandoverAttempt | SourcePCI:723;SourceNR-ARFC... |
| 2024-09-20 22:21:38.534 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.545 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.671 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.671 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276070 | 1 | 12.1080 | 18.3913 | -115.8964 | 19.5197 | 184.6322 | 0.0095 | 0.0040 |
| 2024_09_20 22:00 | 3213301 | 2 | 15.6397 | 5.2455 | -117.2162 | 8.0239 | 109.0497 | 0.0041 | 0.0033 |
| 2024_09_20 22:00 | 3268763 | 3 | 90.0177 | 87.1940 | -115.7648 | 15.5554 | 105.2550 | 0.0022 | 0.0094 |
| 2024_09_20 22:00 | 3214860 | 4 | 5.1590 | 19.5145 | -116.1765 | 13.0690 | 117.0941 | 0.0056 | 0.0005 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416682_8A12F815 | 504990 | 581 | -83.3 | 504990 | 504 | -88.6 | 504990 | 84 | -99.4 | 504990 | 892 |
| MR_1774416682_D9F3268D | 504990 | 581 | -85.7 | 504990 | 504 | -91.8 | 504990 | 84 | -98.7 | 504990 | 892 |
| MR_1774416682_A98DC693 | 504990 | 581 | -86.4 | 504990 | 504 | -90.7 | 504990 | 84 | -100.4 | 504990 | 892 |
| MR_1774416682_88DA3A5A | 504990 | 581 | -86.8 | 504990 | 504 | -88.0 | 504990 | 84 | -100.3 | 504990 | 892 |
| MR_1774416682_C4974087 | 504990 | 581 | -83.9 | 504990 | 504 | -89.7 | 504990 | 84 | -97.8 | 504990 | 892 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 986: `a62642c2-a74...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a62642c2-a74d-4b5d-807c-3e2f61e5add3` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[986] topology](images/train_0986.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3247366_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270546_3
- `C3`: Increase transmission power for 3247366_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270546_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247366_4
- `C6`: Decrease A3 Offset threshold for 3270546_3
- `C7`: Decrease A3 Offset threshold for 3247366_4
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Add neighbor relationship between 3270546_3 and 3247366_4
- `C10`: Press down the tilt angle  of 3247366_4 by 10 degrees
- `C11`: Decrease transmission power for 3247366_4
- `C12`: Check test server and transmission issues **← 정답**
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247366_4
- `C14`: Add neighbor relationship between 3277943_1 and 3247366_4
- `C15`: Press down the tilt angle of 3270546_3 by 10 degrees
- `C16`: Increase transmission power for 3270546_3
- `C17`: Adjust the azimuth of 3270546_3 by 50 degrees
- `C18`: Increase A3 Offset threshold for 3270546_3
- `C19`: Lift the tilt angle of 3270546_3 by 10 degrees
- `C20`: Lift the tilt angle  of 3247366_4 by 10 degrees
- `C21`: Adjust the azimuth of 3247366_4 by 50 degrees
- `C22`: Decrease transmission power for 3270546_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.935 | MS1 | 121.4656608539 | 31.1446301515 | 971 | 504990 | -89.85 | 15.69 | 436.98 | 0.07 | 2.72 | 1592 |
| 2024-09-20 22:21:32.767 | MS1 | 121.4656715234 | 31.1446230422 | 971 | 504990 | -88.63 | 14.65 | 347.68 | 0.17 | 2.61 | 1576 |
| 2024-09-20 22:21:33.910 | MS1 | 121.4656642515 | 31.1446185382 | 971 | 504990 | -91.09 | 13.45 | 549.25 | 0.17 | 2.72 | 1561 |
| 2024-09-20 22:21:34.275 | MS1 | 121.4656604793 | 31.1446238708 | 971 | 504990 | -91.13 | 17.25 | 81.71 | 0.09 | 2.53 | 448 |
| 2024-09-20 22:21:35.814 | MS1 | 121.4656651819 | 31.1446185535 | 971 | 504990 | -91.64 | 15.35 | 99.54 | 0.11 | 2.63 | 342 |
| 2024-09-20 22:21:36.299 | MS1 | 121.4656631084 | 31.1446198546 | 971 | 504990 | -85.25 | 14.00 | 85.99 | 0.10 | 2.79 | 398 |
| 2024-09-20 22:21:37.773 | MS1 | 121.4656585148 | 31.1446373889 | 971 | 504990 | -90.26 | 10.30 | 70.01 | 0.17 | 2.38 | 309 |
| 2024-09-20 22:21:38.968 | MS1 | 121.4656750599 | 31.1446275169 | 971 | 504990 | -91.94 | 8.76 | 62.52 | 0.09 | 2.88 | 473 |
| 2024-09-20 22:21:39.451 | MS1 | 121.4656589520 | 31.1446326604 | 971 | 504990 | -92.10 | 9.81 | 81.85 | 0.19 | 2.68 | 432 |
| 2024-09-20 22:21:40.999 | MS1 | 121.4656660024 | 31.1446280265 | 971 | 504990 | -91.79 | 10.21 | 448.67 | 0.02 | 2.17 | 1580 |
| 2024-09-20 22:21:41.977 | MS1 | 121.4656752312 | 31.1446209589 | 971 | 504990 | -91.17 | 10.30 | 503.44 | 0.13 | 2.73 | 1597 |
| 2024-09-20 22:21:42.217 | MS1 | 121.4656693064 | 31.1446208225 | 971 | 504990 | -92.06 | 8.60 | 585.19 | 0.16 | 2.96 | 1588 |

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
| 3242152 | 2 | 121.4642762067 | 31.1452834489 | 280 | 4 | 12 | 38.0 | TDD | 978 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3247366 | 4 | 121.4740552028 | 31.1519161543 | 5 | 10 | 8 | 45.1 | TDD | 894 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3270546 | 3 | 121.4652595994 | 31.1494840740 | 347 | 15 | 6 | 36.2 | TDD | 971 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3277943 | 1 | 121.4716862804 | 31.1463829438 | 292 | 3 | 10 | 30.0 | TDD | 904 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.954 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.978 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.081 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.081 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.771 | NREventA3 | measId:2;ServCellPCI:967;Se... |
| 2024-09-20 22:21:38.011 | NRHandoverAttempt | SourcePCI:967;SourceNR-ARFC... |
| 2024-09-20 22:21:38.053 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.065 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.198 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.198 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277943 | 1 | 19.0741 | 17.8498 | -116.7952 | 16.3430 | 154.0415 | 0.0189 | 0.0150 |
| 2024_09_20 22:00 | 3242152 | 2 | 19.3696 | 10.5011 | -117.6868 | 19.6159 | 147.7999 | 0.0074 | 0.0035 |
| 2024_09_20 22:00 | 3270546 | 3 | 8.7240 | 6.2518 | -114.5378 | 16.2202 | 152.2205 | 0.0158 | 0.0110 |
| 2024_09_20 22:00 | 3247366 | 4 | 7.0599 | 10.5005 | -114.9753 | 10.8826 | 191.6098 | 0.0075 | 0.0006 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415500_5BF15121 | 504990 | 971 | -89.4 | 504990 | 894 | -90.4 | 504990 | 904 | -96.9 | 504990 | 978 |
| MR_1774415500_A535D0A8 | 504990 | 971 | -91.8 | 504990 | 894 | -90.2 | 504990 | 904 | -96.2 | 504990 | 978 |
| MR_1774415500_CE7DBD53 | 504990 | 971 | -89.6 | 504990 | 894 | -92.2 | 504990 | 904 | -98.4 | 504990 | 978 |
| MR_1774415500_0BBBF58C | 504990 | 971 | -91.4 | 504990 | 894 | -91.3 | 504990 | 904 | -96.8 | 504990 | 978 |
| MR_1774415500_C50676B5 | 504990 | 971 | -90.4 | 504990 | 894 | -91.6 | 504990 | 904 | -95.6 | 504990 | 978 |
| MR_1774415500_36B09C4E | 504990 | 971 | -89.8 | 504990 | 894 | -92.2 | 504990 | 904 | -97.2 | 504990 | 978 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 987: `e29f8915-143...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e29f8915-1439-44c8-9f3e-443bf12a99cc` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Add neighbor relationship between 3263825_1 and 3238440_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[987] topology](images/train_0987.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3263825_1
- `C2`: Decrease A3 Offset threshold for 3263825_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238440_3
- `C4`: Decrease transmission power for 3238440_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263825_1
- `C6`: Press down the tilt angle  of 3238440_3 by 3 degrees
- `C7`: Adjust the azimuth of 3238440_3 by 11 degrees
- `C8`: Add neighbor relationship between 3263825_1 and 3238440_3 **← 정답**
- `C9`: Lift the tilt angle of 3263825_1 by 8 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263825_1
- `C11`: Increase A3 Offset threshold for 3263825_1
- `C12`: Check test server and transmission issues
- `C13`: Add neighbor relationship between 3240876_2 and 3238440_3
- `C14`: Lift the tilt angle  of 3238440_3 by 3 degrees
- `C15`: Press down the tilt angle of 3263825_1 by 8 degrees
- `C16`: Decrease transmission power for 3263825_1
- `C17`: Increase transmission power for 3238440_3
- `C18`: Decrease A3 Offset threshold for 3238440_3
- `C19`: Increase A3 Offset threshold for 3238440_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238440_3
- `C21`: Adjust the azimuth of 3263825_1 by 50 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.467 | MS1 | 121.4656631328 | 31.1446222006 | 296 | 504990 | -83.14 | 13.08 | 510.99 | 0.05 | 2.32 | 1568 |
| 2024-09-20 22:21:32.859 | MS1 | 121.4656684093 | 31.1446354445 | 296 | 504990 | -80.92 | 16.86 | 340.45 | 0.10 | 2.30 | 1592 |
| 2024-09-20 22:21:33.338 | MS1 | 121.4656692151 | 31.1446211210 | 296 | 504990 | -84.78 | 15.17 | 565.14 | 0.13 | 2.06 | 1560 |
| 2024-09-20 22:21:34.803 | MS1 | 121.4656713656 | 31.1446262446 | 296 | 504990 | -85.40 | -1.26 | 49.50 | 0.05 | 1.49 | 1600 |
| 2024-09-20 22:21:35.419 | MS1 | 121.4656598306 | 31.1446248483 | 296 | 504990 | -89.10 | -3.17 | 38.86 | 0.11 | 1.15 | 1596 |
| 2024-09-20 22:21:36.106 | MS1 | 121.4656680723 | 31.1446274940 | 296 | 504990 | -86.17 | -3.06 | 50.55 | 0.18 | 1.10 | 1588 |
| 2024-09-20 22:21:37.979 | MS1 | 121.4656751083 | 31.1446277406 | 296 | 504990 | -92.23 | -3.90 | 55.61 | 0.17 | 1.13 | 1594 |
| 2024-09-20 22:21:38.194 | MS1 | 121.4656729004 | 31.1446328745 | 296 | 504990 | -83.55 | 14.80 | 584.72 | 0.05 | 1.02 | 1581 |
| 2024-09-20 22:21:39.474 | MS1 | 121.4656585475 | 31.1446208549 | 296 | 504990 | -75.67 | 16.66 | 477.52 | 0.10 | 1.05 | 1588 |
| 2024-09-20 22:21:40.554 | MS1 | 121.4656643725 | 31.1446342795 | 296 | 504990 | -83.93 | 14.25 | 437.18 | 0.02 | 2.21 | 1587 |
| 2024-09-20 22:21:41.300 | MS1 | 121.4656613133 | 31.1446199085 | 296 | 504990 | -75.89 | 16.97 | 517.29 | 0.06 | 2.85 | 1591 |
| 2024-09-20 22:21:42.315 | MS1 | 121.4656580905 | 31.1446345750 | 296 | 504990 | -77.36 | 14.61 | 391.88 | 0.15 | 2.55 | 1573 |

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
| 3238440 | 3 | 121.4716222439 | 31.1517958656 | 226 | 0 | 9 | 46.6 | TDD | 747 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3240876 | 2 | 121.4672216189 | 31.1484541723 | 20 | 8 | 8 | 28.8 | TDD | 461 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3263825 | 1 | 121.4683633091 | 31.1524092509 | 20 | 6 | 7 | 31.6 | TDD | 296 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3275931 | 4 | 121.4687653599 | 31.1502188706 | 59 | 10 | 9 | 39.1 | TDD | 453 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.888 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.906 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.056 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.056 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.757 | NREventA3 | measId:2;ServCellPCI:497;Se... |
| 2024-09-20 22:21:35.757 | NREventA3 | measId:2;ServCellPCI:497;Se... |
| 2024-09-20 22:21:36.757 | NREventA3 | measId:2;ServCellPCI:497;Se... |
| 2024-09-20 22:21:39.257 | NRRRCReestablishAttempt | PCI:497 |
| 2024-09-20 22:21:39.271 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.284 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.409 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.409 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263825 | 1 | 14.3498 | 7.9265 | -117.8503 | 5.5903 | 152.7332 | 0.0046 | 0.1140 |
| 2024_09_20 22:00 | 3240876 | 2 | 12.7804 | 17.0112 | -116.2845 | 15.4228 | 199.3490 | 0.0099 | 0.0195 |
| 2024_09_20 22:00 | 3238440 | 3 | 13.7267 | 15.8851 | -116.8554 | 15.5355 | 116.3131 | 0.0078 | 0.0082 |
| 2024_09_20 22:00 | 3275931 | 4 | 10.8870 | 8.2994 | -116.4927 | 13.9310 | 152.7073 | 0.0121 | 0.0096 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415725_47BCD66A | 504990 | 747 | -81.3 | 504990 | 296 | -84.7 | 504990 | 461 | -80.2 | 504990 | 453 |
| MR_1774415725_339CCB8B | 504990 | 296 | -84.7 | 504990 | 747 | -81.3 | 504990 | 461 | -82.0 | 504990 | 453 |
| MR_1774415725_2F6EE0B2 | 504990 | 296 | -83.7 | 504990 | 747 | -81.9 | 504990 | 461 | -79.4 | 504990 | 453 |
| MR_1774415725_DD44E92E | 504990 | 296 | -87.1 | 504990 | 747 | -80.1 | 504990 | 461 | -82.3 | 504990 | 453 |
| MR_1774415725_858E5AE4 | 504990 | 296 | -84.6 | 504990 | 747 | -81.6 | 504990 | 461 | -80.6 | 504990 | 453 |
| MR_1774415725_9ED1A372 | 504990 | 296 | -85.5 | 504990 | 747 | -79.6 | 504990 | 461 | -81.7 | 504990 | 453 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 988: `73a04f62-cc7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `73a04f62-cc7c-4ec4-aa5b-bb40a48da482` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Lift the tilt angle  of 3246546_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[988] topology](images/train_0988.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3246546_3 by 10 degrees **← 정답**
- `C2`: Add neighbor relationship between 3268643_2 and 3271458_1
- `C3`: Decrease transmission power for 3271458_1
- `C4`: Increase transmission power for 3271458_1
- `C5`: Press down the tilt angle of 3268643_2 by 2 degrees
- `C6`: Increase A3 Offset threshold for 3268643_2
- `C7`: Increase A3 Offset threshold for 3271458_1
- `C8`: Increase transmission power for 3268643_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271458_1
- `C10`: Press down the tilt angle  of 3246546_3 by 10 degrees
- `C11`: Adjust the azimuth of 3246546_3 by 50 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271458_1
- `C13`: Add neighbor relationship between 3246546_3 and 3271458_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268643_2
- `C15`: Decrease transmission power for 3268643_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease A3 Offset threshold for 3271458_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268643_2
- `C19`: Check test server and transmission issues
- `C20`: Decrease A3 Offset threshold for 3268643_2
- `C21`: Adjust the azimuth of 3268643_2 by 48 degrees
- `C22`: Lift the tilt angle of 3268643_2 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.139 | MS1 | 121.4656627315 | 31.1446287604 | 273 | 504990 | -85.01 | 17.31 | 596.39 | 0.06 | 2.30 | 1596 |
| 2024-09-20 22:21:32.848 | MS1 | 121.4656739592 | 31.1446180934 | 273 | 504990 | -87.87 | 15.45 | 535.13 | 0.16 | 2.29 | 1561 |
| 2024-09-20 22:21:33.750 | MS1 | 121.4656666618 | 31.1446272571 | 273 | 504990 | -89.91 | 16.59 | 433.20 | 0.20 | 2.41 | 1588 |
| 2024-09-20 22:21:34.424 | MS1 | 121.4656769680 | 31.1446318638 | 273 | 504990 | -87.68 | 12.65 | 41.54 | 0.16 | 2.69 | 1560 |
| 2024-09-20 22:21:35.844 | MS1 | 121.4656641940 | 31.1446317956 | 273 | 504990 | -90.90 | 16.39 | 43.73 | 0.16 | 2.13 | 1587 |
| 2024-09-20 22:21:36.864 | MS1 | 121.4656645013 | 31.1446239693 | 273 | 504990 | -87.47 | 14.57 | 101.32 | 0.19 | 2.43 | 1600 |
| 2024-09-20 22:21:37.181 | MS1 | 121.4656667116 | 31.1446221556 | 273 | 504990 | -90.35 | 12.34 | 80.53 | 0.00 | 2.45 | 1591 |
| 2024-09-20 22:21:38.903 | MS1 | 121.4656607955 | 31.1446205655 | 273 | 504990 | -92.82 | 12.86 | 82.07 | 0.05 | 2.42 | 1586 |
| 2024-09-20 22:21:39.908 | MS1 | 121.4656652165 | 31.1446181514 | 273 | 504990 | -92.17 | 10.50 | 68.48 | 0.06 | 2.40 | 1569 |
| 2024-09-20 22:21:40.405 | MS1 | 121.4656657648 | 31.1446184497 | 273 | 504990 | -92.27 | 9.64 | 535.77 | 0.17 | 2.38 | 1584 |
| 2024-09-20 22:21:41.494 | MS1 | 121.4656726768 | 31.1446359480 | 273 | 504990 | -89.90 | 9.82 | 446.90 | 0.13 | 2.46 | 1586 |
| 2024-09-20 22:21:42.510 | MS1 | 121.4656717888 | 31.1446252176 | 273 | 504990 | -92.18 | 7.19 | 436.92 | 0.05 | 2.92 | 1600 |

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
| 3246546 | 3 | 121.4752389246 | 31.1533756402 | 58 | 14 | 10 | 24.5 | TDD | 673 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3268643 | 2 | 121.4701481199 | 31.1509282700 | 259 | 0 | 3 | 24.9 | TDD | 273 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3271458 | 1 | 121.4720661044 | 31.1475922135 | 54 | 12 | 3 | 36.9 | TDD | 448 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3274363 | 4 | 121.4681874627 | 31.1488600612 | 307 | 6 | 4 | 47.0 | TDD | 271 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.957 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.977 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.096 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.096 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.807 | NREventA3 | measId:2;ServCellPCI:734;Se... |
| 2024-09-20 22:21:38.047 | NRHandoverAttempt | SourcePCI:734;SourceNR-ARFC... |
| 2024-09-20 22:21:38.089 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.103 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.207 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.207 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271458 | 1 | 15.4638 | 10.2122 | -115.5999 | 17.3493 | 131.2764 | 0.0123 | 0.0140 |
| 2024_09_20 22:00 | 3268643 | 2 | 76.6480 | 80.1004 | -117.1564 | 8.3697 | 127.0881 | 0.0039 | 0.0127 |
| 2024_09_20 22:00 | 3246546 | 3 | 18.9960 | 7.2357 | -115.3603 | 13.5861 | 186.1777 | 0.0117 | 0.0146 |
| 2024_09_20 22:00 | 3274363 | 4 | 12.1307 | 16.3673 | -114.0936 | 5.6914 | 103.8928 | 0.0145 | 0.0061 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414072_0EFF6105 | 504990 | 273 | -88.2 | 504990 | 448 | -98.3 | 504990 | 673 | -100.4 | 504990 | 271 |
| MR_1774414072_75455CF7 | 504990 | 273 | -88.8 | 504990 | 448 | -98.3 | 504990 | 673 | -97.9 | 504990 | 271 |
| MR_1774414072_1E44BC7B | 504990 | 273 | -86.3 | 504990 | 448 | -96.1 | 504990 | 673 | -100.8 | 504990 | 271 |
| MR_1774414072_FC59B852 | 504990 | 273 | -88.1 | 504990 | 448 | -96.8 | 504990 | 673 | -101.3 | 504990 | 271 |
| MR_1774414072_A3EA4470 | 504990 | 273 | -86.5 | 504990 | 448 | -95.3 | 504990 | 673 | -98.0 | 504990 | 271 |
| MR_1774414072_3DFF325B | 504990 | 273 | -89.6 | 504990 | 448 | -96.2 | 504990 | 673 | -99.9 | 504990 | 271 |
| MR_1774414072_32B49700 | 504990 | 273 | -89.1 | 504990 | 448 | -95.3 | 504990 | 673 | -98.9 | 504990 | 271 |
| MR_1774414072_6F2B6E48 | 504990 | 273 | -88.6 | 504990 | 448 | -95.8 | 504990 | 673 | -98.8 | 504990 | 271 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 989: `928269be-a7c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `928269be-a7c6-4084-a51d-5e32aad22635` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[989] topology](images/train_0989.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3229723_1 by 6 degrees
- `C2`: Increase A3 Offset threshold for 3221604_2
- `C3`: Lift the tilt angle of 3229723_1 by 6 degrees
- `C4`: Decrease A3 Offset threshold for 3229723_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229723_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221604_2
- `C7`: Press down the tilt angle  of 3221604_2 by 10 degrees
- `C8`: Adjust the azimuth of 3229723_1 by 50 degrees
- `C9`: Decrease A3 Offset threshold for 3221604_2
- `C10`: Decrease transmission power for 3229723_1
- `C11`: Add neighbor relationship between 3229723_1 and 3221604_2
- `C12`: Decrease transmission power for 3221604_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221604_2
- `C14`: Insufficient data; more data is needed for judgment. **← 정답**
- `C15`: Adjust the azimuth of 3221604_2 by 50 degrees
- `C16`: Increase A3 Offset threshold for 3229723_1
- `C17`: Increase transmission power for 3229723_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229723_1
- `C19`: Increase transmission power for 3221604_2
- `C20`: Add neighbor relationship between 3220230_3 and 3221604_2
- `C21`: Check test server and transmission issues
- `C22`: Lift the tilt angle  of 3221604_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.728 | MS1 | 121.4656774275 | 31.1446281319 | 320 | 504990 | -87.33 | 16.88 | 594.72 | 0.08 | 2.97 | 1590 |
| 2024-09-20 22:21:32.758 | MS1 | 121.4656663717 | 31.1446283641 | 320 | 504990 | -86.42 | 12.34 | 544.92 | 0.03 | 2.86 | 1580 |
| 2024-09-20 22:21:33.228 | MS1 | 121.4656739891 | 31.1446250761 | 320 | 504990 | -85.95 | 15.76 | 596.81 | 0.18 | 2.35 | 1595 |
| 2024-09-20 22:21:34.518 | MS1 | 121.4656724937 | 31.1446331501 | 320 | 504990 | -89.02 | 14.53 | 56.98 | 0.19 | 2.87 | 1569 |
| 2024-09-20 22:21:35.979 | MS1 | 121.4656623363 | 31.1446317693 | 320 | 504990 | -86.74 | 16.08 | 61.98 | 0.11 | 2.74 | 1575 |
| 2024-09-20 22:21:36.179 | MS1 | 121.4656647733 | 31.1446289746 | 320 | 504990 | -86.67 | 14.31 | 90.97 | 0.09 | 2.43 | 1568 |
| 2024-09-20 22:21:37.107 | MS1 | 121.4656618307 | 31.1446350720 | 320 | 504990 | -92.10 | 11.78 | 100.32 | 0.20 | 2.59 | 1567 |
| 2024-09-20 22:21:38.984 | MS1 | 121.4656624988 | 31.1446366284 | 320 | 504990 | -90.26 | 11.16 | 62.18 | 0.19 | 3.00 | 1597 |
| 2024-09-20 22:21:39.429 | MS1 | 121.4656687778 | 31.1446235358 | 320 | 504990 | -89.76 | 8.72 | 73.17 | 0.16 | 2.40 | 1581 |
| 2024-09-20 22:21:40.636 | MS1 | 121.4656687572 | 31.1446305832 | 320 | 504990 | -90.67 | 12.64 | 325.69 | 0.12 | 2.67 | 1582 |
| 2024-09-20 22:21:41.741 | MS1 | 121.4656731586 | 31.1446229046 | 320 | 504990 | -92.62 | 9.95 | 413.37 | 0.07 | 2.50 | 1566 |
| 2024-09-20 22:21:42.489 | MS1 | 121.4656699532 | 31.1446281365 | 320 | 504990 | -89.49 | 8.31 | 493.73 | 0.13 | 2.15 | 1589 |

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
| 3220230 | 3 | 121.4706311520 | 31.1556995338 | 139 | 0 | 12 | 38.8 | TDD | 868 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3221604 | 2 | 121.4661406478 | 31.1557971063 | 319 | 12 | 8 | 35.0 | TDD | 545 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3229723 | 1 | 121.4749502396 | 31.1513948222 | 88 | 4 | 5 | 46.5 | TDD | 320 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3277662 | 4 | 121.4722144906 | 31.1503599692 | 217 | 7 | 1 | 22.7 | TDD | 23 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.999 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.015 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.165 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.165 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.861 | NREventA3 | measId:2;ServCellPCI:712;Se... |
| 2024-09-20 22:21:38.101 | NRHandoverAttempt | SourcePCI:712;SourceNR-ARFC... |
| 2024-09-20 22:21:38.151 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.162 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.287 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.287 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3229723 | 1 | 86.3573 | 92.6142 | -115.0387 | 5.5816 | 199.3329 | 0.0058 | 0.0001 |
| 2024_09_19 22:00 | 3221604 | 2 | 83.4969 | 78.3701 | -114.7417 | 7.1278 | 121.0373 | 0.0161 | 0.0198 |
| 2024_09_19 22:00 | 3220230 | 3 | 86.4706 | 86.1745 | -116.0867 | 13.3514 | 151.7487 | 0.0098 | 0.0135 |
| 2024_09_19 22:00 | 3277662 | 4 | 91.9983 | 85.2098 | -114.5633 | 7.6245 | 139.2080 | 0.0080 | 0.0102 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412215_1597AF3D | 504990 | 320 | -90.6 | 504990 | 545 | -90.7 | 504990 | 868 | -97.4 | 504990 | 23 |
| MR_1774412215_DA87B2FC | 504990 | 320 | -88.7 | 504990 | 545 | -90.4 | 504990 | 868 | -95.9 | 504990 | 23 |
| MR_1774412215_5AA43C50 | 504990 | 320 | -89.7 | 504990 | 545 | -88.7 | 504990 | 868 | -98.1 | 504990 | 23 |
| MR_1774412215_FCE4A56F | 504990 | 320 | -87.8 | 504990 | 545 | -89.3 | 504990 | 868 | -98.0 | 504990 | 23 |
| MR_1774412215_634B14F3 | 504990 | 320 | -89.2 | 504990 | 545 | -89.5 | 504990 | 868 | -98.2 | 504990 | 23 |

> *... 2개 열 생략 (전체 14열)*

---
