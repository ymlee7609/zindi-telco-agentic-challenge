# Track A 문제 분석 — test[480]~test[489]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[480] ~ test[489] (10개)

## 목차

1. [문제 480: `2f747ef2-f96...`](#480) — multiple-answer
2. [문제 481: `ec8fae76-aa4...`](#481) — single-answer
3. [문제 482: `b181851b-2d2...`](#482) — multiple-answer
4. [문제 483: `ef0a6aea-c74...`](#483) — single-answer
5. [문제 484: `a416ebda-2f5...`](#484) — multiple-answer
6. [문제 485: `c96e627c-706...`](#485) — single-answer
7. [문제 486: `b822373e-3d9...`](#486) — single-answer
8. [문제 487: `f2269270-770...`](#487) — multiple-answer
9. [문제 488: `0afc34cc-d90...`](#488) — single-answer
10. [문제 489: `923e2a8a-c17...`](#489) — single-answer

---

### 문제 480: `2f747ef2-f96...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2f747ef2-f964-4acf-ad49-bccad40b6ef9` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[480] topology](images/test_0480.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3254618_1
- `C2`: Decrease A3 Offset threshold for 3254618_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212474_2
- `C4`: Lift the tilt angle of 3212474_2 by 3 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212474_2
- `C6`: Adjust the azimuth of 3254618_1 by 40 degrees
- `C7`: Increase transmission power for 3212474_2
- `C8`: Add neighbor relationship between 3212474_2 and 3254618_1
- `C9`: Decrease A3 Offset threshold for 3212474_2
- `C10`: Increase transmission power for 3254618_1
- `C11`: Adjust the azimuth of 3212474_2 by 50 degrees
- `C12`: Increase A3 Offset threshold for 3254618_1
- `C13`: Press down the tilt angle  of 3254618_1 by 4 degrees
- `C14`: Add neighbor relationship between 3264857_3 and 3254618_1
- `C15`: Decrease transmission power for 3212474_2
- `C16`: Lift the tilt angle  of 3254618_1 by 4 degrees
- `C17`: Increase A3 Offset threshold for 3212474_2
- `C18`: Press down the tilt angle of 3212474_2 by 3 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254618_1
- `C20`: Check test server and transmission issues
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254618_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.626 | MS1 | 121.4656776047 | 31.1446204995 | 12 | 504990 | -89.47 | 17.87 | 484.48 | 0.09 | 2.43 | 1581 |
| 2024-09-20 22:21:32.599 | MS1 | 121.4656746622 | 31.1446200128 | 12 | 504990 | -91.05 | 17.81 | 451.25 | 0.09 | 2.32 | 1585 |
| 2024-09-20 22:21:33.103 | MS1 | 121.4656763769 | 31.1446313770 | 12 | 504990 | -88.31 | 17.68 | 442.64 | 0.01 | 2.53 | 1578 |
| 2024-09-20 22:21:34.680 | MS1 | 121.4656649878 | 31.1446274738 | 12 | 504990 | -108.34 | 0.70 | 76.42 | 0.16 | 1.43 | 1599 |
| 2024-09-20 22:21:35.137 | MS1 | 121.4656709777 | 31.1446254056 | 12 | 504990 | -105.25 | 0.65 | 41.99 | 0.14 | 1.04 | 1590 |
| 2024-09-20 22:21:36.330 | MS1 | 121.4656672593 | 31.1446283359 | 12 | 504990 | -108.58 | 1.51 | 75.82 | 0.17 | 1.14 | 1588 |
| 2024-09-20 22:21:37.624 | MS1 | 121.4656692034 | 31.1446241602 | 12 | 504990 | -105.91 | 0.19 | 24.01 | 0.19 | 1.43 | 1599 |
| 2024-09-20 22:21:38.598 | MS1 | 121.4656636489 | 31.1446298911 | 12 | 504990 | -104.31 | 1.50 | 64.10 | 0.04 | 1.44 | 1591 |
| 2024-09-20 22:21:39.380 | MS1 | 121.4656657750 | 31.1446240252 | 12 | 504990 | -105.69 | -1.91 | 46.80 | 0.08 | 1.06 | 1584 |
| 2024-09-20 22:21:40.158 | MS1 | 121.4656695963 | 31.1446369534 | 12 | 504990 | -87.79 | 17.98 | 309.02 | 0.16 | 2.84 | 1564 |
| 2024-09-20 22:21:41.444 | MS1 | 121.4656664241 | 31.1446209572 | 12 | 504990 | -94.41 | 16.31 | 313.73 | 0.03 | 2.06 | 1587 |
| 2024-09-20 22:21:42.364 | MS1 | 121.4656607645 | 31.1446210117 | 12 | 504990 | -86.74 | 15.28 | 553.00 | 0.02 | 2.97 | 1588 |

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
| 3212474 | 2 | 121.4746148418 | 31.1465055545 | 330 | 0 | 3 | 48.5 | TDD | 12 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3213936 | 4 | 121.4719501450 | 31.1450588485 | 234 | 6 | 4 | 40.0 | TDD | 447 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3254618 | 1 | 121.4749664165 | 31.1548431763 | 178 | 3 | 7 | 31.1 | TDD | 51 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3264857 | 3 | 121.4690488832 | 31.1481012203 | 312 | 4 | 7 | 22.2 | TDD | 677 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.548 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.565 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.709 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.709 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.879 | NREventA2 | measId:1;ServCellPCI:343;Se... |
| 2024-09-20 22:21:35.018 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254618 | 1 | 5.5437 | 14.1555 | -117.4532 | 18.1493 | 108.3218 | 0.0156 | 0.0134 |
| 2024_09_20 22:00 | 3212474 | 2 | 16.7436 | 6.3379 | -115.5159 | 10.9826 | 158.8840 | 0.1087 | 0.0010 |
| 2024_09_20 22:00 | 3264857 | 3 | 7.1736 | 18.4083 | -117.3578 | 9.2960 | 179.1696 | 0.0024 | 0.0116 |
| 2024_09_20 22:00 | 3213936 | 4 | 13.7995 | 18.3814 | -114.5504 | 10.3818 | 99.3000 | 0.0050 | 0.0015 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416996_89DC37CB | 504990 | 12 | -108.4 | 504990 | 51 | -111.7 | 504990 | 677 | -117.0 | 504990 | 447 |
| MR_1774416996_E0E5565D | 504990 | 12 | -108.6 | 504990 | 51 | -112.2 | 504990 | 677 | -117.1 | 504990 | 447 |
| MR_1774416996_6F6D614F | 504990 | 12 | -109.5 | 504990 | 51 | -111.7 | 504990 | 677 | -116.7 | 504990 | 447 |
| MR_1774416996_57B2A6DF | 504990 | 12 | -108.9 | 504990 | 51 | -114.9 | 504990 | 677 | -120.0 | 504990 | 447 |
| MR_1774416996_4A33221F | 504990 | 12 | -107.9 | 504990 | 51 | -112.1 | 504990 | 677 | -117.8 | 504990 | 447 |
| MR_1774416996_C2EC4139 | 504990 | 12 | -107.5 | 504990 | 51 | -113.9 | 504990 | 677 | -117.4 | 504990 | 447 |
| MR_1774416996_7DE334D5 | 504990 | 12 | -106.9 | 504990 | 51 | -111.8 | 504990 | 677 | -119.2 | 504990 | 447 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 481: `ec8fae76-aa4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ec8fae76-aa46-426d-9c6b-180de8a76429` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[481] topology](images/test_0481.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3271877_3
- `C2`: Add neighbor relationship between 3241128_4 and 3252509_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271877_3
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Press down the tilt angle  of 3252509_1 by 4 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271877_3
- `C7`: Lift the tilt angle  of 3252509_1 by 4 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252509_1
- `C9`: Increase A3 Offset threshold for 3271877_3
- `C10`: Add neighbor relationship between 3271877_3 and 3252509_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252509_1
- `C12`: Adjust the azimuth of 3252509_1 by 49 degrees
- `C13`: Increase A3 Offset threshold for 3252509_1
- `C14`: Decrease A3 Offset threshold for 3252509_1
- `C15`: Adjust the azimuth of 3271877_3 by 50 degrees
- `C16`: Check test server and transmission issues
- `C17`: Lift the tilt angle of 3271877_3 by 8 degrees
- `C18`: Press down the tilt angle of 3271877_3 by 8 degrees
- `C19`: Decrease A3 Offset threshold for 3271877_3
- `C20`: Decrease transmission power for 3271877_3
- `C21`: Increase transmission power for 3252509_1
- `C22`: Decrease transmission power for 3252509_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.764 | MS1 | 121.4656606465 | 31.1446237928 | 45 | 504990 | -84.53 | 12.69 | 497.54 | 0.15 | 2.04 | 1589 |
| 2024-09-20 22:21:32.128 | MS1 | 121.4656684210 | 31.1446286191 | 45 | 504990 | -76.26 | 16.97 | 402.69 | 0.00 | 2.33 | 1590 |
| 2024-09-20 22:21:33.589 | MS1 | 121.4656771725 | 31.1446195488 | 45 | 504990 | -77.16 | 15.47 | 530.55 | 0.03 | 2.45 | 1572 |
| 2024-09-20 22:21:34.222 | MS1 | 121.4656637261 | 31.1446290915 | 45 | 504990 | -87.01 | -1.82 | 47.26 | 0.11 | 1.08 | 1583 |
| 2024-09-20 22:21:35.974 | MS1 | 121.4656669006 | 31.1446267200 | 45 | 504990 | -87.89 | -0.83 | 40.65 | 0.13 | 1.07 | 1590 |
| 2024-09-20 22:21:36.972 | MS1 | 121.4656614091 | 31.1446319326 | 45 | 504990 | -87.86 | -2.06 | 48.03 | 0.12 | 1.30 | 1570 |
| 2024-09-20 22:21:37.789 | MS1 | 121.4656682145 | 31.1446368415 | 45 | 504990 | -87.89 | -3.29 | 59.17 | 0.08 | 1.09 | 1588 |
| 2024-09-20 22:21:38.315 | MS1 | 121.4656606723 | 31.1446271472 | 45 | 504990 | -75.26 | 13.38 | 459.42 | 0.14 | 1.24 | 1598 |
| 2024-09-20 22:21:39.687 | MS1 | 121.4656684153 | 31.1446309635 | 45 | 504990 | -76.49 | 16.21 | 378.54 | 0.19 | 1.26 | 1576 |
| 2024-09-20 22:21:40.989 | MS1 | 121.4656762750 | 31.1446232168 | 45 | 504990 | -78.39 | 16.68 | 361.87 | 0.19 | 2.27 | 1597 |
| 2024-09-20 22:21:41.255 | MS1 | 121.4656712821 | 31.1446204017 | 45 | 504990 | -79.22 | 15.95 | 309.60 | 0.05 | 2.49 | 1586 |
| 2024-09-20 22:21:42.397 | MS1 | 121.4656598588 | 31.1446372935 | 45 | 504990 | -81.31 | 13.32 | 373.69 | 0.05 | 2.15 | 1587 |

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
| 3219771 | 2 | 121.4647090012 | 31.1456996105 | 355 | 2 | 8 | 33.8 | TDD | 537 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3241128 | 4 | 121.4645741818 | 31.1460420590 | 91 | 8 | 0 | 29.6 | TDD | 622 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3252509 | 1 | 121.4759834879 | 31.1473388822 | 204 | 2 | 4 | 30.7 | TDD | 8 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3271877 | 3 | 121.4700354837 | 31.1501020432 | 283 | 5 | 6 | 41.2 | TDD | 45 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.816 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.950 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.950 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.636 | NREventA3 | measId:2;ServCellPCI:590;Se... |
| 2024-09-20 22:21:35.636 | NREventA3 | measId:2;ServCellPCI:590;Se... |
| 2024-09-20 22:21:36.636 | NREventA3 | measId:2;ServCellPCI:590;Se... |
| 2024-09-20 22:21:39.136 | NRRRCReestablishAttempt | PCI:590 |
| 2024-09-20 22:21:39.147 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.157 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.306 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.306 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252509 | 1 | 13.7174 | 14.7760 | -114.1154 | 15.2816 | 149.4901 | 0.0096 | 0.0067 |
| 2024_09_20 22:00 | 3219771 | 2 | 17.5415 | 11.7600 | -115.9637 | 9.6348 | 127.7793 | 0.0022 | 0.0112 |
| 2024_09_20 22:00 | 3271877 | 3 | 19.3710 | 15.4156 | -114.2009 | 18.3574 | 143.2708 | 0.0129 | 0.1900 |
| 2024_09_20 22:00 | 3241128 | 4 | 14.0103 | 15.2043 | -115.7293 | 13.1924 | 84.1754 | 0.0166 | 0.0012 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415688_6E9D29B7 | 504990 | 45 | -87.5 | 504990 | 8 | -84.9 | 504990 | 622 | -82.9 | 504990 | 537 |
| MR_1774415688_E78BCD05 | 504990 | 8 | -83.8 | 504990 | 45 | -87.1 | 504990 | 622 | -86.7 | 504990 | 537 |
| MR_1774415688_A1DC415C | 504990 | 45 | -85.8 | 504990 | 8 | -82.0 | 504990 | 622 | -85.8 | 504990 | 537 |
| MR_1774415688_328509EE | 504990 | 8 | -81.3 | 504990 | 45 | -85.2 | 504990 | 622 | -85.8 | 504990 | 537 |
| MR_1774415688_26E29114 | 504990 | 8 | -82.0 | 504990 | 45 | -86.9 | 504990 | 622 | -84.0 | 504990 | 537 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 482: `b181851b-2d2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b181851b-2d29-49da-9b85-2b2f7f0df2e4` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[482] topology](images/test_0482.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3247093_5 by 18 degrees
- `C2`: Lift the tilt angle of 3271041_2 by 5 degrees
- `C3`: Add neighbor relationship between 3260806_3 and 3247093_5
- `C4`: Increase A3 Offset threshold for 3271041_2
- `C5`: Increase transmission power for 3247093_5
- `C6`: Decrease transmission power for 3271041_2
- `C7`: Decrease A3 Offset threshold for 3247093_5
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247093_5
- `C9`: Increase A3 Offset threshold for 3247093_5
- `C10`: Increase transmission power for 3271041_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247093_5
- `C12`: Press down the tilt angle  of 3247093_5 by 2 degrees
- `C13`: Lift the tilt angle  of 3247093_5 by 2 degrees
- `C14`: Adjust the azimuth of 3271041_2 by 18 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271041_2
- `C16`: Add neighbor relationship between 3271041_2 and 3247093_5
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271041_2
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Check test server and transmission issues
- `C20`: Decrease transmission power for 3247093_5
- `C21`: Press down the tilt angle of 3271041_2 by 5 degrees
- `C22`: Decrease A3 Offset threshold for 3271041_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.877 | MS1 | 121.4656644745 | 31.1446280273 | 111 | 504990 | -75.55 | 17.77 | 487.35 | 0.11 | 2.20 | 1597 |
| 2024-09-20 22:21:32.293 | MS1 | 121.4656686419 | 31.1446217365 | 111 | 504990 | -75.42 | 12.90 | 446.25 | 0.03 | 2.35 | 1563 |
| 2024-09-20 22:21:33.425 | MS1 | 121.4656660272 | 31.1446297665 | 111 | 504990 | -79.66 | 12.49 | 423.76 | 0.02 | 2.82 | 1569 |
| 2024-09-20 22:21:34.162 | MS1 | 121.4656736081 | 31.1446252642 | 200 | 504990 | -84.32 | 1.69 | 64.62 | 0.12 | 1.20 | 1587 |
| 2024-09-20 22:21:35.196 | MS1 | 121.4656668055 | 31.1446208447 | 200 | 504990 | -82.63 | 2.57 | 42.59 | 0.04 | 1.24 | 1599 |
| 2024-09-20 22:21:36.841 | MS1 | 121.4656702956 | 31.1446305905 | 111 | 504990 | -86.63 | 2.03 | 39.63 | 0.20 | 1.19 | 1563 |
| 2024-09-20 22:21:37.909 | MS1 | 121.4656645507 | 31.1446218138 | 111 | 504990 | -80.24 | 2.39 | 51.76 | 0.13 | 1.49 | 1590 |
| 2024-09-20 22:21:38.979 | MS1 | 121.4656709355 | 31.1446190301 | 200 | 504990 | -84.68 | 1.95 | 49.87 | 0.13 | 1.18 | 1569 |
| 2024-09-20 22:21:39.670 | MS1 | 121.4656602445 | 31.1446290153 | 200 | 504990 | -85.62 | 4.72 | 34.57 | 0.13 | 1.42 | 1562 |
| 2024-09-20 22:21:40.953 | MS1 | 121.4656591255 | 31.1446248354 | 200 | 504990 | -84.72 | 15.87 | 316.75 | 0.05 | 2.24 | 1595 |
| 2024-09-20 22:21:41.831 | MS1 | 121.4656757519 | 31.1446235655 | 200 | 504990 | -78.09 | 17.22 | 458.07 | 0.07 | 2.20 | 1597 |
| 2024-09-20 22:21:42.731 | MS1 | 121.4656677741 | 31.1446315945 | 200 | 504990 | -84.64 | 12.28 | 338.63 | 0.13 | 2.31 | 1575 |

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
| 3210190 | 1 | 121.4645304159 | 31.1508471984 | 53 | 15 | 2 | 20.1 | TDD | 200 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3247093 | 5 | 121.4732219343 | 31.1516239635 | 205 | 1 | 11 | 19.2 | TDD | 573 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3260806 | 3 | 121.4684192034 | 31.1548843395 | 167 | 9 | 5 | 39.9 | TDD | 692 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3271041 | 2 | 121.4742172480 | 31.1456033912 | 280 | 2 | 4 | 48.8 | TDD | 111 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3273191 | 4 | 121.4664388518 | 31.1525867347 | 64 | 14 | 1 | 39.6 | TDD | 731 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.501 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.524 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.626 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.626 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.307 | NREventA3 | measId:2;ServCellPCI:784;Se... |
| 2024-09-20 22:21:34.547 | NRHandoverAttempt | SourcePCI:784;SourceNR-ARFC... |
| 2024-09-20 22:21:34.587 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.597 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:34.733 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.733 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.307 | NREventA3 | measId:2;ServCellPCI:344;Se... |
| 2024-09-20 22:21:36.547 | NRHandoverAttempt | SourcePCI:344;SourceNR-ARFC... |
| 2024-09-20 22:21:36.580 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.595 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.725 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.725 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.307 | NREventA3 | measId:2;ServCellPCI:784;Se... |
| 2024-09-20 22:21:38.547 | NRHandoverAttempt | SourcePCI:784;SourceNR-ARFC... |
| 2024-09-20 22:21:38.592 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.603 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.742 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.742 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210190 | 1 | 7.1709 | 19.0664 | -115.3334 | 7.7679 | 167.7151 | 0.0199 | 0.0161 |
| 2024_09_20 22:00 | 3271041 | 2 | 9.3765 | 16.9207 | -115.9286 | 6.3453 | 84.6181 | 0.0032 | 0.0173 |
| 2024_09_20 22:00 | 3260806 | 3 | 7.1808 | 16.8585 | -114.1872 | 18.4158 | 179.1748 | 0.0044 | 0.0161 |
| 2024_09_20 22:00 | 3273191 | 4 | 16.5437 | 7.5746 | -115.0818 | 9.1273 | 188.6169 | 0.0089 | 0.0061 |
| 2024_09_20 22:00 | 3247093 | 5 | 15.9629 | 11.4803 | -114.1640 | 19.4664 | 141.7235 | 0.0139 | 0.0188 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414003_323353FF | 504990 | 200 | -82.7 | 504990 | 111 | -82.1 | 504990 | 573 | -83.6 | 504990 | 692 |
| MR_1774414003_0A0685E8 | 504990 | 111 | -82.7 | 504990 | 200 | -81.3 | 504990 | 573 | -83.6 | 504990 | 692 |
| MR_1774414003_5B14C45C | 504990 | 200 | -82.9 | 504990 | 111 | -80.6 | 504990 | 573 | -84.5 | 504990 | 692 |
| MR_1774414003_ED3BA735 | 504990 | 111 | -84.5 | 504990 | 200 | -82.1 | 504990 | 573 | -85.5 | 504990 | 692 |
| MR_1774414003_7DC41A7C | 504990 | 111 | -85.8 | 504990 | 200 | -81.6 | 504990 | 573 | -83.8 | 504990 | 692 |
| MR_1774414003_A1D98E4B | 504990 | 200 | -82.7 | 504990 | 111 | -81.2 | 504990 | 573 | -83.9 | 504990 | 692 |
| MR_1774414003_80CB8694 | 504990 | 111 | -85.2 | 504990 | 200 | -80.2 | 504990 | 573 | -83.4 | 504990 | 692 |
| MR_1774414003_679C271F | 504990 | 200 | -85.8 | 504990 | 111 | -82.3 | 504990 | 573 | -82.7 | 504990 | 692 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 483: `ef0a6aea-c74...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ef0a6aea-c74c-4027-8d04-bf8264f1800b` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[483] topology](images/test_0483.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3269769_1 by 4 degrees
- `C2`: Increase transmission power for 3247543_2
- `C3`: Lift the tilt angle  of 3247543_2 by 10 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247543_2
- `C5`: Decrease transmission power for 3269769_1
- `C6`: Decrease A3 Offset threshold for 3247543_2
- `C7`: Adjust the azimuth of 3269769_1 by 19 degrees
- `C8`: Increase A3 Offset threshold for 3247543_2
- `C9`: Lift the tilt angle of 3269769_1 by 4 degrees
- `C10`: Check test server and transmission issues
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269769_1
- `C12`: Decrease A3 Offset threshold for 3269769_1
- `C13`: Press down the tilt angle  of 3247543_2 by 10 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269769_1
- `C15`: Adjust the azimuth of 3247543_2 by 50 degrees
- `C16`: Increase A3 Offset threshold for 3269769_1
- `C17`: Add neighbor relationship between 3257104_4 and 3247543_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247543_2
- `C19`: Add neighbor relationship between 3269769_1 and 3247543_2
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase transmission power for 3269769_1
- `C22`: Decrease transmission power for 3247543_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.197 | MS1 | 121.4656773560 | 31.1446309299 | 202 | 504990 | -87.80 | 14.32 | 578.88 | 0.07 | 2.21 | 1581 |
| 2024-09-20 22:21:32.703 | MS1 | 121.4656596066 | 31.1446368266 | 202 | 504990 | -88.88 | 14.51 | 589.52 | 0.09 | 2.16 | 1600 |
| 2024-09-20 22:21:33.119 | MS1 | 121.4656614002 | 31.1446243062 | 202 | 504990 | -87.56 | 16.98 | 420.56 | 0.03 | 2.31 | 1577 |
| 2024-09-20 22:21:34.453 | MS1 | 121.4656697746 | 31.1446363764 | 202 | 504990 | -91.17 | 16.59 | 91.51 | 0.55 | 2.16 | 624 |
| 2024-09-20 22:21:35.422 | MS1 | 121.4656767535 | 31.1446213707 | 202 | 504990 | -89.01 | 17.41 | 98.63 | 0.62 | 2.21 | 514 |
| 2024-09-20 22:21:36.695 | MS1 | 121.4656618512 | 31.1446363173 | 202 | 504990 | -85.15 | 14.09 | 78.87 | 0.68 | 2.28 | 601 |
| 2024-09-20 22:21:37.662 | MS1 | 121.4656764727 | 31.1446336299 | 202 | 504990 | -93.25 | 7.09 | 70.35 | 0.53 | 2.07 | 552 |
| 2024-09-20 22:21:38.621 | MS1 | 121.4656740366 | 31.1446357952 | 202 | 504990 | -91.08 | 10.25 | 82.97 | 0.52 | 2.96 | 543 |
| 2024-09-20 22:21:39.382 | MS1 | 121.4656730093 | 31.1446225022 | 202 | 504990 | -91.37 | 8.85 | 78.22 | 0.53 | 2.11 | 583 |
| 2024-09-20 22:21:40.296 | MS1 | 121.4656640255 | 31.1446312070 | 202 | 504990 | -91.77 | 10.80 | 512.61 | 0.10 | 2.43 | 1589 |
| 2024-09-20 22:21:41.751 | MS1 | 121.4656751464 | 31.1446195607 | 202 | 504990 | -89.39 | 12.76 | 344.70 | 0.16 | 2.92 | 1596 |
| 2024-09-20 22:21:42.874 | MS1 | 121.4656591230 | 31.1446222635 | 202 | 504990 | -89.10 | 8.79 | 457.86 | 0.20 | 2.71 | 1570 |

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
| 3247543 | 2 | 121.4660912216 | 31.1475079170 | 30 | 11 | 4 | 18.5 | TDD | 501 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3257104 | 4 | 121.4701491414 | 31.1549993563 | 341 | 8 | 1 | 29.7 | TDD | 31 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3269769 | 1 | 121.4653168393 | 31.1528726154 | 159 | 2 | 7 | 27.4 | TDD | 202 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3269888 | 3 | 121.4700772511 | 31.1516717322 | 305 | 2 | 2 | 25.6 | TDD | 518 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.026 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.049 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.173 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.173 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.848 | NREventA3 | measId:2;ServCellPCI:29;Ser... |
| 2024-09-20 22:21:38.088 | NRHandoverAttempt | SourcePCI:29;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.121 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.136 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.272 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.272 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269769 | 1 | 7.2790 | 9.6592 | -115.3342 | 14.5089 | 166.7108 | 0.0058 | 0.0181 |
| 2024_09_20 22:00 | 3247543 | 2 | 17.7500 | 11.0011 | -114.7103 | 10.0437 | 162.1553 | 0.0155 | 0.0001 |
| 2024_09_20 22:00 | 3269888 | 3 | 9.8378 | 8.3535 | -117.7498 | 11.6089 | 156.1100 | 0.0060 | 0.0043 |
| 2024_09_20 22:00 | 3257104 | 4 | 16.1145 | 11.3044 | -114.6435 | 7.2859 | 121.7894 | 0.0168 | 0.0100 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415628_EE1A797E | 504990 | 202 | -90.3 | 504990 | 501 | -97.3 | 504990 | 31 | -98.8 | 504990 | 518 |
| MR_1774415628_C8189614 | 504990 | 202 | -93.0 | 504990 | 501 | -97.9 | 504990 | 31 | -96.6 | 504990 | 518 |
| MR_1774415628_BDA449E2 | 504990 | 202 | -93.1 | 504990 | 501 | -96.2 | 504990 | 31 | -98.8 | 504990 | 518 |
| MR_1774415628_87219BB6 | 504990 | 202 | -90.7 | 504990 | 501 | -98.1 | 504990 | 31 | -97.8 | 504990 | 518 |
| MR_1774415628_5564B29A | 504990 | 202 | -90.5 | 504990 | 501 | -96.8 | 504990 | 31 | -99.5 | 504990 | 518 |
| MR_1774415628_21AE0DDB | 504990 | 202 | -91.5 | 504990 | 501 | -99.5 | 504990 | 31 | -98.7 | 504990 | 518 |
| MR_1774415628_3211542C | 504990 | 202 | -90.4 | 504990 | 501 | -98.1 | 504990 | 31 | -98.0 | 504990 | 518 |
| MR_1774415628_1A5D97E4 | 504990 | 202 | -90.5 | 504990 | 501 | -96.2 | 504990 | 31 | -99.8 | 504990 | 518 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 484: `a416ebda-2f5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a416ebda-2f57-4e20-810b-08863a632d2e` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[484] topology](images/test_0484.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3234620_2 by 17 degrees
- `C2`: Lift the tilt angle  of 3234620_2 by 5 degrees
- `C3`: Decrease transmission power for 3234620_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277275_4
- `C6`: Press down the tilt angle  of 3234620_2 by 5 degrees
- `C7`: Increase transmission power for 3277275_4
- `C8`: Decrease transmission power for 3277275_4
- `C9`: Lift the tilt angle of 3277275_4 by 5 degrees
- `C10`: Increase transmission power for 3234620_2
- `C11`: Add neighbor relationship between 3238781_3 and 3234620_2
- `C12`: Press down the tilt angle of 3277275_4 by 5 degrees
- `C13`: Increase A3 Offset threshold for 3277275_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234620_2
- `C15`: Check test server and transmission issues
- `C16`: Add neighbor relationship between 3277275_4 and 3234620_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277275_4
- `C18`: Decrease A3 Offset threshold for 3234620_2
- `C19`: Decrease A3 Offset threshold for 3277275_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234620_2
- `C21`: Adjust the azimuth of 3277275_4 by 44 degrees
- `C22`: Increase A3 Offset threshold for 3234620_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.126 | MS1 | 121.4656777804 | 31.1446262284 | 230 | 504990 | -78.52 | 12.42 | 408.05 | 0.02 | 2.92 | 1589 |
| 2024-09-20 22:21:32.909 | MS1 | 121.4656594280 | 31.1446268097 | 230 | 504990 | -82.02 | 17.64 | 340.00 | 0.12 | 2.71 | 1562 |
| 2024-09-20 22:21:33.499 | MS1 | 121.4656694066 | 31.1446195068 | 230 | 504990 | -83.22 | 14.02 | 498.23 | 0.17 | 2.55 | 1600 |
| 2024-09-20 22:21:34.644 | MS1 | 121.4656585071 | 31.1446296356 | 230 | 504990 | -87.69 | 2.40 | 63.46 | 0.19 | 1.17 | 1596 |
| 2024-09-20 22:21:35.452 | MS1 | 121.4656731961 | 31.1446274288 | 230 | 504990 | -86.35 | 0.06 | 78.05 | 0.05 | 1.42 | 1584 |
| 2024-09-20 22:21:36.825 | MS1 | 121.4656611784 | 31.1446304147 | 230 | 504990 | -92.08 | 1.00 | 49.41 | 0.05 | 1.33 | 1578 |
| 2024-09-20 22:21:37.308 | MS1 | 121.4656695890 | 31.1446245754 | 230 | 504990 | -89.41 | 3.54 | 73.55 | 0.04 | 1.33 | 1572 |
| 2024-09-20 22:21:38.799 | MS1 | 121.4656737241 | 31.1446259622 | 230 | 504990 | -94.70 | 3.80 | 54.20 | 0.05 | 1.01 | 1595 |
| 2024-09-20 22:21:39.370 | MS1 | 121.4656650698 | 31.1446278191 | 230 | 504990 | -91.53 | 1.88 | 76.30 | 0.09 | 1.26 | 1583 |
| 2024-09-20 22:21:40.903 | MS1 | 121.4656628407 | 31.1446225648 | 230 | 504990 | -78.97 | 13.83 | 451.34 | 0.19 | 2.87 | 1592 |
| 2024-09-20 22:21:41.896 | MS1 | 121.4656677937 | 31.1446349082 | 230 | 504990 | -82.81 | 16.87 | 386.25 | 0.17 | 2.03 | 1600 |
| 2024-09-20 22:21:42.693 | MS1 | 121.4656724511 | 31.1446324460 | 230 | 504990 | -82.87 | 14.13 | 470.47 | 0.09 | 2.88 | 1577 |

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
| 3234620 | 2 | 121.4738754815 | 31.1538841642 | 234 | 3 | 2 | 41.5 | TDD | 839 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3238781 | 3 | 121.4646672966 | 31.1541865743 | 28 | 10 | 5 | 20.6 | TDD | 270 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3262070 | 1 | 121.4706512634 | 31.1528734603 | 71 | 1 | 9 | 37.4 | TDD | 99 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3277275 | 4 | 121.4732839624 | 31.1550834834 | 168 | 4 | 8 | 22.9 | TDD | 230 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.992 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.142 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.142 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262070 | 1 | 12.6526 | 11.0452 | -114.5485 | 10.3245 | 142.1235 | 0.0067 | 0.0017 |
| 2024_09_20 22:00 | 3234620 | 2 | 19.9980 | 10.7253 | -116.2828 | 15.1953 | 182.5472 | 0.0035 | 0.0048 |
| 2024_09_20 22:00 | 3238781 | 3 | 18.9251 | 13.2905 | -114.4609 | 17.3820 | 109.2564 | 0.0042 | 0.0009 |
| 2024_09_20 22:00 | 3277275 | 4 | 18.8492 | 13.4413 | -109.5768 | 12.7172 | 139.3865 | 0.0076 | 0.0184 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413548_6B649D64 | 504990 | 839 | -87.6 | 504990 | 230 | -87.1 | 504990 | 270 | -91.8 | 504990 | 99 |
| MR_1774413548_0EB95238 | 504990 | 230 | -85.9 | 504990 | 839 | -86.9 | 504990 | 270 | -89.0 | 504990 | 99 |
| MR_1774413548_217839C4 | 504990 | 839 | -86.9 | 504990 | 230 | -85.8 | 504990 | 270 | -88.9 | 504990 | 99 |
| MR_1774413548_B2D02B5F | 504990 | 230 | -86.9 | 504990 | 839 | -83.7 | 504990 | 270 | -90.6 | 504990 | 99 |
| MR_1774413548_3C7F9F3D | 504990 | 230 | -85.8 | 504990 | 839 | -83.4 | 504990 | 270 | -88.5 | 504990 | 99 |
| MR_1774413548_F6802962 | 504990 | 839 | -88.9 | 504990 | 230 | -83.4 | 504990 | 270 | -88.8 | 504990 | 99 |
| MR_1774413548_A8560B03 | 504990 | 839 | -86.6 | 504990 | 230 | -84.5 | 504990 | 270 | -91.0 | 504990 | 99 |
| MR_1774413548_C09B26CF | 504990 | 230 | -85.8 | 504990 | 839 | -86.6 | 504990 | 270 | -89.1 | 504990 | 99 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 485: `c96e627c-706...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c96e627c-7062-4b38-a668-1b54b3d956b2` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[485] topology](images/test_0485.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3271041_6 by 4 degrees
- `C2`: Adjust the azimuth of 3233735_5 by 30 degrees
- `C3`: Adjust the azimuth of 3271041_6 by 6 degrees
- `C4`: Decrease A3 Offset threshold for 3271041_6
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271041_6
- `C6`: Decrease transmission power for 3271041_6
- `C7`: Decrease transmission power for 3233735_5
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Lift the tilt angle of 3233735_5 by 5 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233735_5
- `C11`: Add neighbor relationship between 3221734_12 and 3271041_6
- `C12`: Press down the tilt angle of 3233735_5 by 5 degrees
- `C13`: Lift the tilt angle  of 3271041_6 by 4 degrees
- `C14`: Increase A3 Offset threshold for 3233735_5
- `C15`: Increase transmission power for 3233735_5
- `C16`: Increase transmission power for 3271041_6
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271041_6
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233735_5
- `C19`: Check test server and transmission issues
- `C20`: Decrease A3 Offset threshold for 3233735_5
- `C21`: Increase A3 Offset threshold for 3271041_6
- `C22`: Add neighbor relationship between 3233735_5 and 3271041_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.838 | MS1 | 121.4656714784 | 31.1446291770 | 156 | 504990 | -95.74 | 9.28 | 437.28 | 0.15 | 2.06 | 1590 |
| 2024-09-20 22:21:32.201 | MS1 | 121.4656768121 | 31.1446342283 | 501 | 504990 | -94.77 | 14.69 | 586.26 | 0.02 | 2.30 | 1585 |
| 2024-09-20 22:21:33.571 | MS1 | 121.4656731526 | 31.1446286441 | 337 | 504990 | -93.79 | 12.66 | 582.85 | 0.17 | 2.40 | 1594 |
| 2024-09-20 22:21:34.199 | MS1 | 121.4656734331 | 31.1446360033 | 468 | 152650 | -91.02 | 2.21 | 64.81 | 0.03 | 1.66 | 921 |
| 2024-09-20 22:21:35.462 | MS1 | 121.4656684580 | 31.1446330695 | 369 | 152650 | -96.21 | 5.70 | 78.58 | 0.01 | 1.88 | 989 |
| 2024-09-20 22:21:36.547 | MS1 | 121.4656657886 | 31.1446212160 | 149 | 152650 | -94.44 | 4.30 | 82.62 | 0.07 | 1.84 | 994 |
| 2024-09-20 22:21:37.311 | MS1 | 121.4656602640 | 31.1446313232 | 584 | 152650 | -87.16 | 2.73 | 91.40 | 0.07 | 2.00 | 941 |
| 2024-09-20 22:21:38.411 | MS1 | 121.4656674365 | 31.1446337979 | 468 | 152650 | -90.11 | 4.45 | 57.15 | 0.11 | 1.66 | 959 |
| 2024-09-20 22:21:39.836 | MS1 | 121.4656745994 | 31.1446249716 | 369 | 152650 | -94.24 | 4.37 | 69.23 | 0.00 | 1.58 | 966 |
| 2024-09-20 22:21:40.415 | MS1 | 121.4656583589 | 31.1446321647 | 149 | 152650 | -88.79 | 6.64 | 93.08 | 0.09 | 2.15 | 1562 |
| 2024-09-20 22:21:41.862 | MS1 | 121.4656776234 | 31.1446188748 | 584 | 152650 | -92.88 | 4.08 | 66.72 | 0.12 | 2.45 | 1564 |
| 2024-09-20 22:21:42.434 | MS1 | 121.4656704477 | 31.1446330948 | 468 | 152650 | -88.34 | 3.55 | 88.16 | 0.12 | 2.99 | 1586 |

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
| 3218924 | 2 | 121.4718345209 | 31.1520966789 | 208 | 2 | 0 | 20.1 | TDD | 359 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3221263 | 8 | 121.4657492942 | 31.1542138775 | 177 | 10 | 9 | 18.0 | FDD | 999 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3221734 | 12 | 121.4736210490 | 31.1442125829 | 196 | 6 | 10 | 19.9 | FDD | 149 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3233735 | 5 | 121.4671927566 | 31.1516678178 | 161 | 4 | 10 | 12.7 | TDD | 156 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3234059 | 3 | 121.4739617417 | 31.1474854652 | 168 | 3 | 2 | 2.9 | TDD | 337 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3251854 | 1 | 121.4707134974 | 31.1458290107 | 357 | 3 | 12 | 2.5 | TDD | 741 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3253971 | 11 | 121.4678380329 | 31.1540145778 | 212 | 3 | 2 | 8.6 | FDD | 468 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3259404 | 9 | 121.4740736679 | 31.1483307644 | 161 | 10 | 8 | 26.3 | FDD | 584 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3270083 | 13 | 121.4680366589 | 31.1453708263 | 157 | 13 | 12 | 5.5 | FDD | 954 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3271041 | 6 | 121.4726734549 | 31.1558056020 | 214 | 4 | 1 | 3.9 | TDD | 253 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3276197 | 7 | 121.4670511502 | 31.1533088835 | 273 | 11 | 11 | 27.2 | FDD | 227 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3277885 | 4 | 121.4694150228 | 31.1457326901 | 256 | 1 | 11 | 2.2 | TDD | 501 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3279910 | 10 | 121.4656375100 | 31.1513135117 | 359 | 3 | 8 | 9.3 | FDD | 369 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |

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
| 2024-09-20 22:21:31.494 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.509 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.632 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.632 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.387 | NREventA2 | measId:1;ServCellPCI:824;Se... |
| 2024-09-20 22:21:35.489 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.745 | NREventA5 | measId:3;ServCellPCI:824;Se... |
| 2024-09-20 22:21:35.813 | NRHandoverAttempt | SourcePCI:824;SourceNR-ARFC... |
| 2024-09-20 22:21:35.839 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.850 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.970 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.970 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251854 | 1 | 17.6388 | 13.9252 | -116.7462 | 14.5510 | 177.5576 | 0.0048 | 0.0026 |
| 2024_09_20 22:00 | 3218924 | 2 | 14.8715 | 13.7040 | -117.6143 | 8.1752 | 182.2395 | 0.0160 | 0.0138 |
| 2024_09_20 22:00 | 3234059 | 3 | 17.6192 | 5.6106 | -117.0724 | 11.1968 | 137.1204 | 0.0127 | 0.0132 |
| 2024_09_20 22:00 | 3277885 | 4 | 6.5210 | 15.0682 | -115.3191 | 11.7825 | 107.7526 | 0.0195 | 0.0028 |
| 2024_09_20 22:00 | 3233735 | 5 | 7.8722 | 19.5928 | -116.3828 | 12.2017 | 91.3762 | 0.0048 | 0.0126 |
| 2024_09_20 22:00 | 3271041 | 6 | 19.3034 | 11.6873 | -117.1802 | 7.4347 | 89.1965 | 0.0182 | 0.0186 |
| 2024_09_20 22:00 | 3276197 | 7 | 9.7431 | 12.6169 | -114.7740 | 3.2045 | 35.5133 | 0.0059 | 0.0056 |
| 2024_09_20 22:00 | 3221263 | 8 | 17.4468 | 11.8933 | -117.7425 | 3.9301 | 36.9576 | 0.0139 | 0.0069 |
| 2024_09_20 22:00 | 3259404 | 9 | 13.3930 | 5.4906 | -117.2217 | 3.5138 | 51.2057 | 0.0093 | 0.0008 |
| 2024_09_20 22:00 | 3279910 | 10 | 14.9762 | 19.4617 | -117.0162 | 4.8396 | 42.0421 | 0.0041 | 0.0184 |
| 2024_09_20 22:00 | 3253971 | 11 | 19.9501 | 16.5475 | -116.3096 | 4.2004 | 55.2509 | 0.0010 | 0.0158 |
| 2024_09_20 22:00 | 3221734 | 12 | 8.6467 | 5.9279 | -116.8212 | 3.8988 | 21.0474 | 0.0108 | 0.0049 |
| 2024_09_20 22:00 | 3270083 | 13 | 15.1552 | 7.0364 | -117.2308 | 4.1298 | 40.3034 | 0.0167 | 0.0020 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416151_B0E02B6D | 504990 | 337 | -93.0 | 504990 | 253 | -99.4 | 504990 | 359 | -99.3 | 504990 | 741 |
| MR_1774416151_A633CA95 | 504990 | 337 | -91.8 | 504990 | 253 | -99.4 | 504990 | 359 | -99.9 | 504990 | 741 |
| MR_1774416151_AC259A7B | 504990 | 337 | -94.7 | 504990 | 253 | -96.9 | 504990 | 359 | -102.7 | 504990 | 741 |
| MR_1774416151_AD8B2DF3 | 152650 | 468 | -90.6 | 152650 | 954 | -92.0 | 152650 | 227 | -99.3 | 152650 | 999 |
| MR_1774416151_F0944902 | 504990 | 337 | -92.8 | 504990 | 253 | -97.6 | 504990 | 359 | -100.9 | 504990 | 741 |
| MR_1774416151_6444CAD2 | 152650 | 468 | -89.4 | 152650 | 954 | -94.2 | 152650 | 227 | -99.8 | 152650 | 999 |
| MR_1774416151_05C6929A | 504990 | 337 | -92.5 | 504990 | 253 | -96.0 | 504990 | 359 | -100.6 | 504990 | 741 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 486: `b822373e-3d9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b822373e-3d9f-4aa3-ab8a-e16ff8b63ceb` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[486] topology](images/test_0486.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3217042_2
- `C2`: Increase transmission power for 3217042_2
- `C3`: Lift the tilt angle of 3217042_2 by 10 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Press down the tilt angle  of 3278919_3 by 4 degrees
- `C6`: Increase A3 Offset threshold for 3278919_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217042_2
- `C8`: Adjust the azimuth of 3278919_3 by 5 degrees
- `C9`: Increase transmission power for 3278919_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217042_2
- `C11`: Lift the tilt angle  of 3278919_3 by 4 degrees
- `C12`: Decrease A3 Offset threshold for 3278919_3
- `C13`: Decrease transmission power for 3278919_3
- `C14`: Adjust the azimuth of 3217042_2 by 50 degrees
- `C15`: Decrease A3 Offset threshold for 3217042_2
- `C16`: Add neighbor relationship between 3263334_1 and 3278919_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278919_3
- `C18`: Press down the tilt angle of 3217042_2 by 10 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278919_3
- `C20`: Increase A3 Offset threshold for 3217042_2
- `C21`: Add neighbor relationship between 3217042_2 and 3278919_3
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.419 | MS1 | 121.4656605735 | 31.1446378758 | 593 | 504990 | -76.62 | 17.36 | 543.53 | 0.03 | 2.13 | 1586 |
| 2024-09-20 22:21:32.109 | MS1 | 121.4656731679 | 31.1446191196 | 593 | 504990 | -78.19 | 15.05 | 421.60 | 0.05 | 2.79 | 1597 |
| 2024-09-20 22:21:33.353 | MS1 | 121.4656601005 | 31.1446266974 | 593 | 504990 | -81.01 | 17.53 | 322.68 | 0.15 | 2.30 | 1588 |
| 2024-09-20 22:21:34.497 | MS1 | 121.4656716805 | 31.1446252818 | 593 | 504990 | -94.20 | -0.38 | 29.38 | 0.08 | 1.32 | 1561 |
| 2024-09-20 22:21:35.987 | MS1 | 121.4656646015 | 31.1446253284 | 593 | 504990 | -90.34 | -2.81 | 50.72 | 0.19 | 1.14 | 1577 |
| 2024-09-20 22:21:36.717 | MS1 | 121.4656697208 | 31.1446268146 | 593 | 504990 | -88.25 | -0.37 | 72.13 | 0.20 | 1.11 | 1597 |
| 2024-09-20 22:21:37.533 | MS1 | 121.4656760321 | 31.1446223546 | 593 | 504990 | -92.01 | -0.82 | 45.47 | 0.01 | 1.30 | 1580 |
| 2024-09-20 22:21:38.449 | MS1 | 121.4656776963 | 31.1446355286 | 593 | 504990 | -83.52 | 13.39 | 535.28 | 0.11 | 1.15 | 1574 |
| 2024-09-20 22:21:39.222 | MS1 | 121.4656717384 | 31.1446252098 | 593 | 504990 | -75.61 | 12.18 | 335.55 | 0.14 | 1.22 | 1590 |
| 2024-09-20 22:21:40.431 | MS1 | 121.4656654936 | 31.1446375766 | 593 | 504990 | -81.71 | 14.06 | 476.05 | 0.13 | 2.48 | 1562 |
| 2024-09-20 22:21:41.376 | MS1 | 121.4656640759 | 31.1446243327 | 593 | 504990 | -82.54 | 13.13 | 368.29 | 0.11 | 2.82 | 1598 |
| 2024-09-20 22:21:42.531 | MS1 | 121.4656636546 | 31.1446314440 | 593 | 504990 | -76.26 | 17.90 | 558.42 | 0.09 | 2.89 | 1586 |

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
| 3217042 | 2 | 121.4722581938 | 31.1462931436 | 49 | 8 | 10 | 41.9 | TDD | 593 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3245182 | 4 | 121.4712562776 | 31.1524238871 | 235 | 12 | 10 | 24.8 | TDD | 17 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3263334 | 1 | 121.4747044287 | 31.1533589587 | 69 | 15 | 12 | 23.0 | TDD | 536 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3278919 | 3 | 121.4666469453 | 31.1557695119 | 179 | 3 | 4 | 22.9 | TDD | 68 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.256 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.271 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.410 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.410 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.080 | NREventA3 | measId:2;ServCellPCI:463;Se... |
| 2024-09-20 22:21:36.080 | NREventA3 | measId:2;ServCellPCI:463;Se... |
| 2024-09-20 22:21:37.080 | NREventA3 | measId:2;ServCellPCI:463;Se... |
| 2024-09-20 22:21:39.580 | NRRRCReestablishAttempt | PCI:463 |
| 2024-09-20 22:21:39.597 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.612 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.758 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.758 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263334 | 1 | 19.0436 | 15.2191 | -115.6582 | 13.9361 | 175.9598 | 0.0161 | 0.0128 |
| 2024_09_20 22:00 | 3217042 | 2 | 14.0875 | 13.3816 | -114.8516 | 14.6715 | 195.1228 | 0.0112 | 0.1508 |
| 2024_09_20 22:00 | 3278919 | 3 | 13.5184 | 11.3256 | -115.9589 | 7.7647 | 178.0019 | 0.0142 | 0.0095 |
| 2024_09_20 22:00 | 3245182 | 4 | 11.4116 | 12.0538 | -114.4474 | 7.7440 | 143.0329 | 0.0079 | 0.0165 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416839_DE441630 | 504990 | 593 | -95.6 | 504990 | 68 | -88.7 | 504990 | 536 | -90.1 | 504990 | 17 |
| MR_1774416839_E5624767 | 504990 | 68 | -88.3 | 504990 | 593 | -95.6 | 504990 | 536 | -91.7 | 504990 | 17 |
| MR_1774416839_12AB32A2 | 504990 | 593 | -93.2 | 504990 | 68 | -88.9 | 504990 | 536 | -89.8 | 504990 | 17 |
| MR_1774416839_1E7DE393 | 504990 | 68 | -88.6 | 504990 | 593 | -94.1 | 504990 | 536 | -92.4 | 504990 | 17 |
| MR_1774416839_561C28FA | 504990 | 68 | -86.6 | 504990 | 593 | -94.0 | 504990 | 536 | -90.4 | 504990 | 17 |
| MR_1774416839_499F2A01 | 504990 | 593 | -93.4 | 504990 | 68 | -88.4 | 504990 | 536 | -93.0 | 504990 | 17 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 487: `f2269270-770...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f2269270-7706-4777-86fe-19638fb8036b` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[487] topology](images/test_0487.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3222581_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232355_4
- `C3`: Increase transmission power for 3232355_4
- `C4`: Increase A3 Offset threshold for 3222581_1
- `C5`: Increase A3 Offset threshold for 3232355_4
- `C6`: Add neighbor relationship between 3232355_4 and 3222581_1
- `C7`: Decrease transmission power for 3232355_4
- `C8`: Press down the tilt angle  of 3222581_1 by 3 degrees
- `C9`: Decrease A3 Offset threshold for 3232355_4
- `C10`: Lift the tilt angle of 3232355_4 by 4 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Add neighbor relationship between 3272975_2 and 3222581_1
- `C13`: Lift the tilt angle  of 3222581_1 by 3 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222581_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232355_4
- `C16`: Decrease transmission power for 3222581_1
- `C17`: Adjust the azimuth of 3232355_4 by 32 degrees
- `C18`: Adjust the azimuth of 3222581_1 by 5 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222581_1
- `C20`: Press down the tilt angle of 3232355_4 by 4 degrees
- `C21`: Decrease A3 Offset threshold for 3222581_1
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.721 | MS1 | 121.4656710536 | 31.1446312950 | 543 | 504990 | -84.84 | 16.98 | 472.94 | 0.19 | 2.42 | 1584 |
| 2024-09-20 22:21:32.174 | MS1 | 121.4656637809 | 31.1446219853 | 543 | 504990 | -83.82 | 17.01 | 506.89 | 0.01 | 2.73 | 1593 |
| 2024-09-20 22:21:33.629 | MS1 | 121.4656751138 | 31.1446222255 | 543 | 504990 | -79.88 | 12.73 | 449.99 | 0.10 | 2.77 | 1591 |
| 2024-09-20 22:21:34.894 | MS1 | 121.4656778710 | 31.1446232545 | 543 | 504990 | -94.65 | 2.64 | 70.67 | 0.10 | 1.35 | 1569 |
| 2024-09-20 22:21:35.484 | MS1 | 121.4656590764 | 31.1446203651 | 543 | 504990 | -87.27 | 1.50 | 70.36 | 0.16 | 1.30 | 1593 |
| 2024-09-20 22:21:36.973 | MS1 | 121.4656765705 | 31.1446357427 | 543 | 504990 | -87.66 | 1.09 | 46.98 | 0.11 | 1.10 | 1596 |
| 2024-09-20 22:21:37.219 | MS1 | 121.4656672991 | 31.1446276396 | 543 | 504990 | -87.06 | 0.30 | 63.17 | 0.20 | 1.34 | 1564 |
| 2024-09-20 22:21:38.588 | MS1 | 121.4656668850 | 31.1446188125 | 543 | 504990 | -92.89 | 2.98 | 65.36 | 0.15 | 1.05 | 1563 |
| 2024-09-20 22:21:39.816 | MS1 | 121.4656742254 | 31.1446251056 | 543 | 504990 | -85.04 | 1.47 | 67.46 | 0.01 | 1.18 | 1591 |
| 2024-09-20 22:21:40.193 | MS1 | 121.4656729864 | 31.1446227048 | 543 | 504990 | -82.33 | 14.53 | 328.10 | 0.02 | 2.41 | 1594 |
| 2024-09-20 22:21:41.194 | MS1 | 121.4656590673 | 31.1446282622 | 543 | 504990 | -82.94 | 16.79 | 561.29 | 0.15 | 2.05 | 1596 |
| 2024-09-20 22:21:42.820 | MS1 | 121.4656718779 | 31.1446204943 | 543 | 504990 | -76.46 | 14.87 | 367.71 | 0.15 | 2.39 | 1593 |

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
| 3221245 | 3 | 121.4678480993 | 31.1544230925 | 50 | 1 | 8 | 32.0 | TDD | 342 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3222581 | 1 | 121.4667433427 | 31.1553883271 | 190 | 2 | 11 | 21.7 | TDD | 90 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3232355 | 4 | 121.4691199625 | 31.1509789094 | 173 | 0 | 3 | 48.2 | TDD | 543 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3272975 | 2 | 121.4743166879 | 31.1507419374 | 82 | 2 | 1 | 49.6 | TDD | 212 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.200 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.216 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.345 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.345 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222581 | 1 | 12.8303 | 6.9066 | -116.4554 | 5.1644 | 129.1145 | 0.0195 | 0.0119 |
| 2024_09_20 22:00 | 3272975 | 2 | 7.7858 | 5.7285 | -115.3455 | 9.3229 | 106.5671 | 0.0125 | 0.0152 |
| 2024_09_20 22:00 | 3221245 | 3 | 11.2046 | 6.7192 | -114.1572 | 13.7698 | 192.3870 | 0.0153 | 0.0023 |
| 2024_09_20 22:00 | 3232355 | 4 | 18.5295 | 5.6554 | -108.4525 | 15.7692 | 94.5700 | 0.0093 | 0.0125 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415583_D57766EA | 504990 | 90 | -93.1 | 504990 | 543 | -95.2 | 504990 | 212 | -94.1 | 504990 | 342 |
| MR_1774415583_3AC4D06D | 504990 | 543 | -95.6 | 504990 | 90 | -94.0 | 504990 | 212 | -92.9 | 504990 | 342 |
| MR_1774415583_0F34E4C6 | 504990 | 90 | -93.5 | 504990 | 543 | -92.2 | 504990 | 212 | -94.7 | 504990 | 342 |
| MR_1774415583_A61065E6 | 504990 | 543 | -96.0 | 504990 | 90 | -93.7 | 504990 | 212 | -94.1 | 504990 | 342 |
| MR_1774415583_B84A84F8 | 504990 | 543 | -95.1 | 504990 | 90 | -93.9 | 504990 | 212 | -92.6 | 504990 | 342 |
| MR_1774415583_DB169A6A | 504990 | 543 | -94.1 | 504990 | 90 | -93.3 | 504990 | 212 | -92.1 | 504990 | 342 |
| MR_1774415583_A9610C62 | 504990 | 90 | -96.3 | 504990 | 543 | -92.5 | 504990 | 212 | -91.7 | 504990 | 342 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 488: `0afc34cc-d90...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0afc34cc-d900-4ac7-9e4c-f80046460e69` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[488] topology](images/test_0488.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3260815_3 by 6 degrees
- `C2`: Increase A3 Offset threshold for 3277581_1
- `C3`: Check test server and transmission issues
- `C4`: Increase transmission power for 3260815_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277581_1
- `C6`: Lift the tilt angle  of 3277581_1 by 10 degrees
- `C7`: Increase transmission power for 3277581_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260815_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277581_1
- `C10`: Decrease transmission power for 3260815_3
- `C11`: Adjust the azimuth of 3260815_3 by 18 degrees
- `C12`: Add neighbor relationship between 3260815_3 and 3277581_1
- `C13`: Add neighbor relationship between 3217217_4 and 3277581_1
- `C14`: Adjust the azimuth of 3277581_1 by 50 degrees
- `C15`: Increase A3 Offset threshold for 3260815_3
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Press down the tilt angle of 3260815_3 by 6 degrees
- `C18`: Decrease A3 Offset threshold for 3260815_3
- `C19`: Decrease A3 Offset threshold for 3277581_1
- `C20`: Press down the tilt angle  of 3277581_1 by 10 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260815_3
- `C22`: Decrease transmission power for 3277581_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.448 | MS1 | 121.4656773362 | 31.1446200650 | 419 | 504990 | -89.32 | 12.02 | 541.05 | 0.01 | 2.81 | 1568 |
| 2024-09-20 22:21:32.423 | MS1 | 121.4656609111 | 31.1446251383 | 419 | 504990 | -88.39 | 13.88 | 417.68 | 0.08 | 2.03 | 1579 |
| 2024-09-20 22:21:33.176 | MS1 | 121.4656722083 | 31.1446356246 | 419 | 504990 | -85.24 | 13.30 | 368.28 | 0.20 | 2.35 | 1561 |
| 2024-09-20 22:21:34.759 | MS1 | 121.4656620715 | 31.1446335626 | 419 | 504990 | -86.25 | 14.13 | 65.70 | 0.05 | 2.86 | 353 |
| 2024-09-20 22:21:35.456 | MS1 | 121.4656634690 | 31.1446194194 | 419 | 504990 | -89.33 | 13.87 | 68.29 | 0.04 | 2.82 | 464 |
| 2024-09-20 22:21:36.883 | MS1 | 121.4656736632 | 31.1446267641 | 419 | 504990 | -90.63 | 17.06 | 66.81 | 0.12 | 2.32 | 342 |
| 2024-09-20 22:21:37.247 | MS1 | 121.4656604280 | 31.1446345884 | 419 | 504990 | -92.73 | 7.46 | 103.44 | 0.03 | 2.40 | 352 |
| 2024-09-20 22:21:38.881 | MS1 | 121.4656623996 | 31.1446189377 | 419 | 504990 | -89.72 | 7.92 | 53.46 | 0.18 | 2.46 | 467 |
| 2024-09-20 22:21:39.164 | MS1 | 121.4656735065 | 31.1446232641 | 419 | 504990 | -91.46 | 12.16 | 84.31 | 0.10 | 2.11 | 375 |
| 2024-09-20 22:21:40.521 | MS1 | 121.4656593747 | 31.1446246437 | 419 | 504990 | -91.85 | 10.38 | 520.59 | 0.02 | 2.52 | 1590 |
| 2024-09-20 22:21:41.630 | MS1 | 121.4656626219 | 31.1446376557 | 419 | 504990 | -92.85 | 8.50 | 315.05 | 0.15 | 2.52 | 1580 |
| 2024-09-20 22:21:42.595 | MS1 | 121.4656662876 | 31.1446378222 | 419 | 504990 | -92.09 | 12.51 | 584.50 | 0.13 | 2.81 | 1589 |

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
| 3217217 | 4 | 121.4679491295 | 31.1474834635 | 92 | 0 | 9 | 42.9 | TDD | 983 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3231476 | 2 | 121.4640153825 | 31.1547708011 | 285 | 14 | 5 | 26.3 | TDD | 619 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3260815 | 3 | 121.4729529888 | 31.1498819562 | 248 | 5 | 9 | 15.4 | TDD | 419 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3277581 | 1 | 121.4684272264 | 31.1477693741 | 327 | 11 | 10 | 20.3 | TDD | 353 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.218 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.239 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.372 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.372 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.082 | NREventA3 | measId:2;ServCellPCI:772;Se... |
| 2024-09-20 22:21:38.322 | NRHandoverAttempt | SourcePCI:772;SourceNR-ARFC... |
| 2024-09-20 22:21:38.371 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.384 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.527 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.527 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277581 | 1 | 17.8513 | 16.6197 | -115.7193 | 11.5509 | 174.4100 | 0.0199 | 0.0018 |
| 2024_09_20 22:00 | 3231476 | 2 | 8.1228 | 13.7271 | -117.1991 | 5.8740 | 134.0751 | 0.0022 | 0.0093 |
| 2024_09_20 22:00 | 3260815 | 3 | 18.5757 | 18.4584 | -115.7407 | 12.6462 | 157.2838 | 0.0136 | 0.0080 |
| 2024_09_20 22:00 | 3217217 | 4 | 6.6307 | 13.3716 | -116.9026 | 16.2957 | 109.1317 | 0.0028 | 0.0158 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414814_3FCBFB07 | 504990 | 419 | -87.7 | 504990 | 353 | -90.2 | 504990 | 983 | -100.5 | 504990 | 619 |
| MR_1774414814_AA5F89B7 | 504990 | 419 | -86.8 | 504990 | 353 | -91.1 | 504990 | 983 | -98.1 | 504990 | 619 |
| MR_1774414814_725F9CD1 | 504990 | 419 | -86.9 | 504990 | 353 | -92.0 | 504990 | 983 | -100.5 | 504990 | 619 |
| MR_1774414814_CBA24F14 | 504990 | 419 | -86.7 | 504990 | 353 | -89.5 | 504990 | 983 | -101.3 | 504990 | 619 |
| MR_1774414814_B13D0097 | 504990 | 419 | -85.0 | 504990 | 353 | -89.5 | 504990 | 983 | -99.0 | 504990 | 619 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 489: `923e2a8a-c17...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `923e2a8a-c179-4910-a000-bb225c4c9f94` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[489] topology](images/test_0489.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275038_4
- `C2`: Add neighbor relationship between 3279033_2 and 3275038_4
- `C3`: Increase A3 Offset threshold for 3275038_4
- `C4`: Lift the tilt angle of 3279033_2 by 5 degrees
- `C5`: Check test server and transmission issues
- `C6`: Adjust the azimuth of 3279033_2 by 31 degrees
- `C7`: Press down the tilt angle of 3279033_2 by 5 degrees
- `C8`: Add neighbor relationship between 3248494_1 and 3275038_4
- `C9`: Adjust the azimuth of 3275038_4 by 50 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Press down the tilt angle  of 3275038_4 by 7 degrees
- `C12`: Lift the tilt angle  of 3275038_4 by 7 degrees
- `C13`: Decrease transmission power for 3279033_2
- `C14`: Increase A3 Offset threshold for 3279033_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275038_4
- `C16`: Increase transmission power for 3279033_2
- `C17`: Increase transmission power for 3275038_4
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279033_2
- `C19`: Decrease transmission power for 3275038_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279033_2
- `C21`: Decrease A3 Offset threshold for 3275038_4
- `C22`: Decrease A3 Offset threshold for 3279033_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.484 | MS1 | 121.4656621366 | 31.1446292755 | 453 | 504990 | -85.13 | 13.47 | 496.31 | 0.07 | 2.90 | 1562 |
| 2024-09-20 22:21:32.796 | MS1 | 121.4656778428 | 31.1446294997 | 453 | 504990 | -91.81 | 17.78 | 517.01 | 0.19 | 2.75 | 1575 |
| 2024-09-20 22:21:33.263 | MS1 | 121.4656583905 | 31.1446340104 | 453 | 504990 | -89.26 | 14.87 | 444.56 | 0.20 | 2.34 | 1594 |
| 2024-09-20 22:21:34.772 | MS1 | 121.4656637804 | 31.1446367003 | 453 | 504990 | -85.58 | 12.34 | 77.16 | 0.68 | 2.65 | 692 |
| 2024-09-20 22:21:35.360 | MS1 | 121.4656601055 | 31.1446210211 | 453 | 504990 | -91.88 | 15.27 | 83.62 | 0.61 | 2.56 | 552 |
| 2024-09-20 22:21:36.906 | MS1 | 121.4656617174 | 31.1446250748 | 453 | 504990 | -91.99 | 15.11 | 73.05 | 0.53 | 2.39 | 664 |
| 2024-09-20 22:21:37.499 | MS1 | 121.4656744098 | 31.1446185984 | 453 | 504990 | -89.67 | 10.62 | 79.70 | 0.63 | 2.64 | 680 |
| 2024-09-20 22:21:38.311 | MS1 | 121.4656748894 | 31.1446350273 | 453 | 504990 | -91.71 | 7.24 | 47.31 | 0.58 | 2.40 | 611 |
| 2024-09-20 22:21:39.732 | MS1 | 121.4656748743 | 31.1446351487 | 453 | 504990 | -89.24 | 7.21 | 91.64 | 0.68 | 2.51 | 562 |
| 2024-09-20 22:21:40.180 | MS1 | 121.4656615516 | 31.1446193247 | 453 | 504990 | -92.90 | 8.43 | 383.23 | 0.03 | 2.23 | 1569 |
| 2024-09-20 22:21:41.763 | MS1 | 121.4656666925 | 31.1446290766 | 453 | 504990 | -92.63 | 7.63 | 342.82 | 0.03 | 2.04 | 1597 |
| 2024-09-20 22:21:42.143 | MS1 | 121.4656615133 | 31.1446374910 | 453 | 504990 | -91.54 | 9.68 | 419.44 | 0.16 | 2.03 | 1563 |

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
| 3248494 | 1 | 121.4667576740 | 31.1472347599 | 53 | 12 | 1 | 22.7 | TDD | 576 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3271571 | 3 | 121.4640297501 | 31.1510675244 | 52 | 8 | 2 | 29.2 | TDD | 386 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3275038 | 4 | 121.4744822007 | 31.1461654174 | 64 | 6 | 11 | 20.1 | TDD | 637 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3279033 | 2 | 121.4705388462 | 31.1467511807 | 274 | 0 | 11 | 43.3 | TDD | 453 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.835 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.854 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.996 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.996 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.709 | NREventA3 | measId:2;ServCellPCI:349;Se... |
| 2024-09-20 22:21:37.949 | NRHandoverAttempt | SourcePCI:349;SourceNR-ARFC... |
| 2024-09-20 22:21:37.995 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.009 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.124 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.124 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248494 | 1 | 9.6694 | 7.2754 | -115.4790 | 18.1650 | 137.1278 | 0.0172 | 0.0005 |
| 2024_09_20 22:00 | 3279033 | 2 | 7.6344 | 13.3752 | -114.2089 | 7.5794 | 131.4315 | 0.0150 | 0.0066 |
| 2024_09_20 22:00 | 3271571 | 3 | 9.9465 | 10.3204 | -114.6665 | 6.9952 | 182.4993 | 0.0055 | 0.0177 |
| 2024_09_20 22:00 | 3275038 | 4 | 11.8405 | 10.1130 | -114.7989 | 8.8937 | 192.3469 | 0.0028 | 0.0068 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413852_7C649D74 | 504990 | 453 | -85.7 | 504990 | 637 | -90.6 | 504990 | 576 | -96.8 | 504990 | 386 |
| MR_1774413852_A899EB9B | 504990 | 453 | -86.1 | 504990 | 637 | -90.2 | 504990 | 576 | -95.1 | 504990 | 386 |
| MR_1774413852_A6A54C2F | 504990 | 453 | -86.3 | 504990 | 637 | -89.6 | 504990 | 576 | -95.8 | 504990 | 386 |
| MR_1774413852_94956F50 | 504990 | 453 | -85.1 | 504990 | 637 | -91.9 | 504990 | 576 | -97.7 | 504990 | 386 |
| MR_1774413852_0FAD6077 | 504990 | 453 | -87.0 | 504990 | 637 | -90.9 | 504990 | 576 | -96.4 | 504990 | 386 |
| MR_1774413852_E2AD3C8A | 504990 | 453 | -84.8 | 504990 | 637 | -91.8 | 504990 | 576 | -95.7 | 504990 | 386 |
| MR_1774413852_999B812C | 504990 | 453 | -86.1 | 504990 | 637 | -90.7 | 504990 | 576 | -96.3 | 504990 | 386 |

> *... 2개 열 생략 (전체 14열)*

---
