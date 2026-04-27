# Track A 문제 분석 — test[150]~test[159]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[150] ~ test[159] (10개)

## 목차

1. [문제 150: `fcf851e4-659...`](#150) — multiple-answer
2. [문제 151: `58a4dfc1-0c5...`](#151) — single-answer
3. [문제 152: `a27443a4-96c...`](#152) — multiple-answer
4. [문제 153: `84112bf4-76b...`](#153) — single-answer
5. [문제 154: `82167500-f42...`](#154) — single-answer
6. [문제 155: `da418ba2-d74...`](#155) — single-answer
7. [문제 156: `6a69251a-4d7...`](#156) — single-answer
8. [문제 157: `0b3595bd-565...`](#157) — single-answer
9. [문제 158: `145a5ef5-557...`](#158) — single-answer
10. [문제 159: `5e736544-ed5...`](#159) — multiple-answer

---

### 문제 150: `fcf851e4-659...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fcf851e4-6599-4318-9e11-0dd37a111772` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[150] topology](images/test_0150.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3271082_1 by 6 degrees
- `C2`: Increase A3 Offset threshold for 3276558_3
- `C3`: Add neighbor relationship between 3237951_2 and 3276558_3
- `C4`: Decrease transmission power for 3276558_3
- `C5`: Press down the tilt angle  of 3276558_3 by 4 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271082_1
- `C7`: Adjust the azimuth of 3271082_1 by 46 degrees
- `C8`: Adjust the azimuth of 3276558_3 by 24 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276558_3
- `C10`: Decrease A3 Offset threshold for 3271082_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Lift the tilt angle  of 3276558_3 by 4 degrees
- `C13`: Decrease A3 Offset threshold for 3276558_3
- `C14`: Increase A3 Offset threshold for 3271082_1
- `C15`: Check test server and transmission issues
- `C16`: Press down the tilt angle of 3271082_1 by 6 degrees
- `C17`: Increase transmission power for 3271082_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276558_3
- `C19`: Decrease transmission power for 3271082_1
- `C20`: Increase transmission power for 3276558_3
- `C21`: Add neighbor relationship between 3271082_1 and 3276558_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271082_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.286 | MS1 | 121.4656709593 | 31.1446353731 | 33 | 504990 | -79.10 | 14.99 | 424.66 | 0.17 | 2.76 | 1563 |
| 2024-09-20 22:21:32.643 | MS1 | 121.4656777890 | 31.1446226094 | 33 | 504990 | -76.32 | 15.71 | 510.87 | 0.11 | 2.97 | 1578 |
| 2024-09-20 22:21:33.824 | MS1 | 121.4656659078 | 31.1446341883 | 33 | 504990 | -82.37 | 14.26 | 557.58 | 0.14 | 2.85 | 1563 |
| 2024-09-20 22:21:34.459 | MS1 | 121.4656769060 | 31.1446300815 | 33 | 504990 | -91.70 | 3.13 | 68.15 | 0.19 | 1.47 | 1569 |
| 2024-09-20 22:21:35.369 | MS1 | 121.4656776781 | 31.1446376830 | 33 | 504990 | -92.06 | 3.29 | 90.25 | 0.10 | 1.24 | 1586 |
| 2024-09-20 22:21:36.482 | MS1 | 121.4656777368 | 31.1446197921 | 33 | 504990 | -87.35 | 2.47 | 47.14 | 0.06 | 1.35 | 1573 |
| 2024-09-20 22:21:37.941 | MS1 | 121.4656673112 | 31.1446289958 | 33 | 504990 | -91.44 | 1.81 | 65.70 | 0.14 | 1.45 | 1572 |
| 2024-09-20 22:21:38.756 | MS1 | 121.4656771164 | 31.1446368339 | 33 | 504990 | -88.38 | 3.10 | 52.25 | 0.14 | 1.26 | 1585 |
| 2024-09-20 22:21:39.857 | MS1 | 121.4656689135 | 31.1446205552 | 33 | 504990 | -91.10 | 3.75 | 51.71 | 0.06 | 1.03 | 1574 |
| 2024-09-20 22:21:40.718 | MS1 | 121.4656627779 | 31.1446373128 | 33 | 504990 | -78.92 | 16.19 | 383.29 | 0.18 | 2.02 | 1561 |
| 2024-09-20 22:21:41.161 | MS1 | 121.4656736724 | 31.1446269488 | 33 | 504990 | -83.54 | 12.07 | 481.96 | 0.10 | 2.45 | 1589 |
| 2024-09-20 22:21:42.916 | MS1 | 121.4656644858 | 31.1446347159 | 33 | 504990 | -84.09 | 16.90 | 337.69 | 0.19 | 2.75 | 1588 |

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
| 3237951 | 2 | 121.4758167961 | 31.1458784996 | 69 | 1 | 2 | 42.6 | TDD | 705 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3245048 | 4 | 121.4659488601 | 31.1549044780 | 119 | 0 | 1 | 16.1 | TDD | 927 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3271082 | 1 | 121.4746958850 | 31.1546799834 | 263 | 4 | 2 | 46.6 | TDD | 33 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3276558 | 3 | 121.4733612190 | 31.1449381247 | 291 | 1 | 11 | 42.5 | TDD | 822 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.143 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.166 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.305 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.305 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271082 | 1 | 19.0541 | 8.9151 | -108.3471 | 9.3111 | 93.6428 | 0.0092 | 0.0099 |
| 2024_09_20 22:00 | 3237951 | 2 | 9.3406 | 8.5955 | -116.7607 | 8.1983 | 161.0814 | 0.0126 | 0.0060 |
| 2024_09_20 22:00 | 3276558 | 3 | 17.5382 | 5.3532 | -117.1847 | 12.0752 | 118.3766 | 0.0037 | 0.0099 |
| 2024_09_20 22:00 | 3245048 | 4 | 10.8504 | 10.7047 | -115.8600 | 15.7372 | 178.0453 | 0.0076 | 0.0113 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413651_33EFEE11 | 504990 | 33 | -92.1 | 504990 | 822 | -86.7 | 504990 | 705 | -93.4 | 504990 | 927 |
| MR_1774413651_AA8DA426 | 504990 | 33 | -91.8 | 504990 | 822 | -89.3 | 504990 | 705 | -90.6 | 504990 | 927 |
| MR_1774413651_C9056B1A | 504990 | 822 | -92.0 | 504990 | 33 | -89.1 | 504990 | 705 | -90.9 | 504990 | 927 |
| MR_1774413651_1465E157 | 504990 | 822 | -91.2 | 504990 | 33 | -89.5 | 504990 | 705 | -92.5 | 504990 | 927 |
| MR_1774413651_14097B7B | 504990 | 33 | -89.9 | 504990 | 822 | -88.1 | 504990 | 705 | -91.0 | 504990 | 927 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 151: `58a4dfc1-0c5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `58a4dfc1-0c52-4595-96ce-21a791553e16` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[151] topology](images/test_0151.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3232507_4 by 50 degrees
- `C2`: Increase A3 Offset threshold for 3232507_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256118_1
- `C4`: Decrease transmission power for 3232507_4
- `C5`: Increase transmission power for 3256118_1
- `C6`: Adjust the azimuth of 3256118_1 by 5 degrees
- `C7`: Press down the tilt angle  of 3232507_4 by 4 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256118_1
- `C9`: Increase transmission power for 3232507_4
- `C10`: Decrease transmission power for 3256118_1
- `C11`: Decrease A3 Offset threshold for 3232507_4
- `C12`: Lift the tilt angle  of 3232507_4 by 4 degrees
- `C13`: Increase A3 Offset threshold for 3256118_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232507_4
- `C15`: Lift the tilt angle of 3256118_1 by 4 degrees
- `C16`: Decrease A3 Offset threshold for 3256118_1
- `C17`: Add neighbor relationship between 3272911_2 and 3232507_4
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232507_4
- `C20`: Check test server and transmission issues
- `C21`: Add neighbor relationship between 3256118_1 and 3232507_4
- `C22`: Press down the tilt angle of 3256118_1 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.623 | MS1 | 121.4656749670 | 31.1446368428 | 840 | 504990 | -86.17 | 16.18 | 304.71 | 0.20 | 2.18 | 1579 |
| 2024-09-20 22:21:32.187 | MS1 | 121.4656759192 | 31.1446284566 | 840 | 504990 | -88.76 | 17.63 | 560.92 | 0.17 | 2.98 | 1599 |
| 2024-09-20 22:21:33.563 | MS1 | 121.4656710859 | 31.1446351844 | 840 | 504990 | -86.75 | 13.89 | 418.79 | 0.11 | 2.46 | 1570 |
| 2024-09-20 22:21:34.997 | MS1 | 121.4656677448 | 31.1446348067 | 840 | 504990 | -89.67 | 17.46 | 81.75 | 0.66 | 2.19 | 500 |
| 2024-09-20 22:21:35.350 | MS1 | 121.4656754001 | 31.1446276243 | 840 | 504990 | -87.15 | 15.78 | 80.75 | 0.62 | 2.30 | 535 |
| 2024-09-20 22:21:36.352 | MS1 | 121.4656732870 | 31.1446300857 | 840 | 504990 | -88.90 | 16.07 | 54.07 | 0.65 | 2.71 | 544 |
| 2024-09-20 22:21:37.620 | MS1 | 121.4656593840 | 31.1446322384 | 840 | 504990 | -91.78 | 11.30 | 78.90 | 0.57 | 2.40 | 671 |
| 2024-09-20 22:21:38.110 | MS1 | 121.4656740361 | 31.1446208464 | 840 | 504990 | -93.06 | 9.30 | 102.84 | 0.58 | 2.68 | 590 |
| 2024-09-20 22:21:39.938 | MS1 | 121.4656670279 | 31.1446217268 | 840 | 504990 | -90.18 | 11.31 | 97.98 | 0.68 | 2.24 | 557 |
| 2024-09-20 22:21:40.135 | MS1 | 121.4656685553 | 31.1446362055 | 840 | 504990 | -89.25 | 11.54 | 507.87 | 0.02 | 2.67 | 1584 |
| 2024-09-20 22:21:41.731 | MS1 | 121.4656666024 | 31.1446316711 | 840 | 504990 | -93.52 | 7.72 | 603.97 | 0.12 | 2.86 | 1560 |
| 2024-09-20 22:21:42.794 | MS1 | 121.4656660508 | 31.1446266025 | 840 | 504990 | -92.05 | 11.89 | 496.99 | 0.18 | 2.44 | 1600 |

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
| 3232507 | 4 | 121.4672173565 | 31.1488063910 | 2 | 1 | 11 | 24.4 | TDD | 782 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3256118 | 1 | 121.4734051314 | 31.1558774097 | 205 | 3 | 7 | 36.0 | TDD | 840 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3272911 | 2 | 121.4651953089 | 31.1502269054 | 176 | 12 | 7 | 30.1 | TDD | 353 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3275509 | 3 | 121.4737283098 | 31.1530699089 | 91 | 11 | 2 | 43.2 | TDD | 414 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.618 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.637 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.755 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.755 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.497 | NREventA3 | measId:2;ServCellPCI:932;Se... |
| 2024-09-20 22:21:38.737 | NRHandoverAttempt | SourcePCI:932;SourceNR-ARFC... |
| 2024-09-20 22:21:38.784 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.799 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.927 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.927 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256118 | 1 | 8.2905 | 8.6744 | -115.2907 | 7.5082 | 111.1716 | 0.0045 | 0.0117 |
| 2024_09_20 22:00 | 3272911 | 2 | 17.2195 | 18.5039 | -114.2953 | 18.6817 | 169.8255 | 0.0167 | 0.0028 |
| 2024_09_20 22:00 | 3275509 | 3 | 19.5883 | 8.6522 | -116.2759 | 9.1824 | 117.9888 | 0.0152 | 0.0154 |
| 2024_09_20 22:00 | 3232507 | 4 | 16.6321 | 6.0878 | -114.5710 | 10.3847 | 157.0339 | 0.0117 | 0.0011 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414369_586F8480 | 504990 | 840 | -89.8 | 504990 | 782 | -97.8 | 504990 | 353 | -101.7 | 504990 | 414 |
| MR_1774414369_B325AEE7 | 504990 | 840 | -91.4 | 504990 | 782 | -98.6 | 504990 | 353 | -101.6 | 504990 | 414 |
| MR_1774414369_D7624728 | 504990 | 840 | -88.6 | 504990 | 782 | -98.0 | 504990 | 353 | -102.3 | 504990 | 414 |
| MR_1774414369_F2610B1C | 504990 | 840 | -87.7 | 504990 | 782 | -96.2 | 504990 | 353 | -103.7 | 504990 | 414 |
| MR_1774414369_65D8A9CD | 504990 | 840 | -90.1 | 504990 | 782 | -96.8 | 504990 | 353 | -102.4 | 504990 | 414 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 152: `a27443a4-96c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a27443a4-96c8-4cb7-b496-1b99aae9c67a` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[152] topology](images/test_0152.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3257988_1
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Lift the tilt angle of 3258954_3 by 10 degrees
- `C4`: Check test server and transmission issues
- `C5`: Increase transmission power for 3258954_3
- `C6`: Decrease A3 Offset threshold for 3258954_3
- `C7`: Press down the tilt angle of 3258954_3 by 10 degrees
- `C8`: Decrease transmission power for 3258954_3
- `C9`: Lift the tilt angle  of 3257988_1 by 1 degrees
- `C10`: Increase A3 Offset threshold for 3258954_3
- `C11`: Decrease transmission power for 3257988_1
- `C12`: Add neighbor relationship between 3258954_3 and 3257988_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258954_3
- `C14`: Adjust the azimuth of 3258954_3 by 25 degrees
- `C15`: Press down the tilt angle  of 3257988_1 by 1 degrees
- `C16`: Add neighbor relationship between 3233541_2 and 3257988_1
- `C17`: Increase A3 Offset threshold for 3257988_1
- `C18`: Increase transmission power for 3257988_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258954_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257988_1
- `C21`: Adjust the azimuth of 3257988_1 by 44 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257988_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.900 | MS1 | 121.4656597383 | 31.1446331028 | 14 | 504990 | -90.53 | 17.08 | 376.90 | 0.20 | 2.65 | 1592 |
| 2024-09-20 22:21:32.774 | MS1 | 121.4656773326 | 31.1446361501 | 14 | 504990 | -94.43 | 12.64 | 418.27 | 0.06 | 2.89 | 1581 |
| 2024-09-20 22:21:33.778 | MS1 | 121.4656618900 | 31.1446292365 | 14 | 504990 | -90.11 | 12.93 | 364.32 | 0.13 | 2.41 | 1563 |
| 2024-09-20 22:21:34.679 | MS1 | 121.4656641115 | 31.1446279417 | 14 | 504990 | -105.84 | 0.07 | 43.43 | 0.16 | 1.06 | 1574 |
| 2024-09-20 22:21:35.501 | MS1 | 121.4656663813 | 31.1446313591 | 14 | 504990 | -108.40 | 1.94 | 47.70 | 0.16 | 1.43 | 1589 |
| 2024-09-20 22:21:36.115 | MS1 | 121.4656752622 | 31.1446185024 | 14 | 504990 | -105.21 | -0.03 | 70.06 | 0.19 | 1.37 | 1561 |
| 2024-09-20 22:21:37.680 | MS1 | 121.4656744252 | 31.1446183958 | 14 | 504990 | -104.25 | 0.39 | 59.18 | 0.17 | 1.35 | 1588 |
| 2024-09-20 22:21:38.209 | MS1 | 121.4656727481 | 31.1446220736 | 14 | 504990 | -109.04 | 0.32 | 14.90 | 0.19 | 1.32 | 1561 |
| 2024-09-20 22:21:39.348 | MS1 | 121.4656682217 | 31.1446239214 | 14 | 504990 | -106.73 | -0.18 | 42.77 | 0.09 | 1.05 | 1587 |
| 2024-09-20 22:21:40.226 | MS1 | 121.4656676414 | 31.1446350139 | 14 | 504990 | -92.72 | 12.46 | 319.12 | 0.03 | 2.68 | 1564 |
| 2024-09-20 22:21:41.984 | MS1 | 121.4656606440 | 31.1446258406 | 14 | 504990 | -86.42 | 12.89 | 304.23 | 0.02 | 2.76 | 1593 |
| 2024-09-20 22:21:42.378 | MS1 | 121.4656617298 | 31.1446364824 | 14 | 504990 | -93.57 | 12.94 | 587.96 | 0.12 | 2.79 | 1582 |

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
| 3233541 | 2 | 121.4655339379 | 31.1460426911 | 73 | 13 | 12 | 48.7 | TDD | 973 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3253777 | 4 | 121.4682747892 | 31.1541883630 | 328 | 12 | 12 | 15.3 | TDD | 791 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3257988 | 1 | 121.4753747963 | 31.1511753379 | 276 | 0 | 6 | 15.1 | TDD | 575 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3258954 | 3 | 121.4657938126 | 31.1462035400 | 209 | 11 | 0 | 35.4 | TDD | 14 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.613 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.736 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.736 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.985 | NREventA2 | measId:1;ServCellPCI:525;Se... |
| 2024-09-20 22:21:35.089 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257988 | 1 | 15.1974 | 18.5094 | -117.9838 | 18.7940 | 147.6368 | 0.0022 | 0.0099 |
| 2024_09_20 22:00 | 3233541 | 2 | 7.9126 | 15.8203 | -115.0678 | 12.9130 | 97.9436 | 0.0031 | 0.0027 |
| 2024_09_20 22:00 | 3258954 | 3 | 9.8514 | 10.5608 | -117.7447 | 7.7230 | 163.7424 | 0.1487 | 0.0128 |
| 2024_09_20 22:00 | 3253777 | 4 | 14.2548 | 12.3846 | -116.8107 | 18.3387 | 172.9249 | 0.0043 | 0.0128 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412163_156BCD53 | 504990 | 14 | -105.0 | 504990 | 575 | -110.2 | 504990 | 973 | -117.2 | 504990 | 791 |
| MR_1774412163_72A7DD92 | 504990 | 14 | -104.6 | 504990 | 575 | -111.3 | 504990 | 973 | -119.1 | 504990 | 791 |
| MR_1774412163_86CD6EC6 | 504990 | 14 | -104.1 | 504990 | 575 | -110.1 | 504990 | 973 | -116.0 | 504990 | 791 |
| MR_1774412163_2E7A7D23 | 504990 | 14 | -103.8 | 504990 | 575 | -111.5 | 504990 | 973 | -115.4 | 504990 | 791 |
| MR_1774412163_790EA654 | 504990 | 14 | -103.8 | 504990 | 575 | -113.3 | 504990 | 973 | -117.7 | 504990 | 791 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 153: `84112bf4-76b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `84112bf4-76b6-4d3c-bbba-54ae026d0b51` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[153] topology](images/test_0153.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3274820_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270093_1
- `C4`: Adjust the azimuth of 3274820_2 by 8 degrees
- `C5`: Increase transmission power for 3274820_2
- `C6`: Adjust the azimuth of 3270093_1 by 34 degrees
- `C7`: Decrease A3 Offset threshold for 3274820_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270093_1
- `C9`: Increase A3 Offset threshold for 3274820_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274820_2
- `C11`: Press down the tilt angle of 3270093_1 by 5 degrees
- `C12`: Press down the tilt angle  of 3274820_2 by 10 degrees
- `C13`: Lift the tilt angle  of 3274820_2 by 10 degrees
- `C14`: Check test server and transmission issues
- `C15`: Decrease transmission power for 3270093_1
- `C16`: Increase transmission power for 3270093_1
- `C17`: Add neighbor relationship between 3263108_3 and 3274820_2
- `C18`: Lift the tilt angle of 3270093_1 by 5 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274820_2
- `C20`: Increase A3 Offset threshold for 3270093_1
- `C21`: Decrease A3 Offset threshold for 3270093_1
- `C22`: Add neighbor relationship between 3270093_1 and 3274820_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.983 | MS1 | 121.4656691704 | 31.1446199576 | 648 | 504990 | -89.12 | 14.22 | 605.97 | 0.09 | 2.51 | 1562 |
| 2024-09-20 22:21:32.170 | MS1 | 121.4656745440 | 31.1446266725 | 648 | 504990 | -91.96 | 13.58 | 423.37 | 0.05 | 2.91 | 1577 |
| 2024-09-20 22:21:33.468 | MS1 | 121.4656774709 | 31.1446258473 | 648 | 504990 | -88.60 | 14.95 | 461.45 | 0.05 | 2.24 | 1568 |
| 2024-09-20 22:21:34.424 | MS1 | 121.4656752389 | 31.1446332153 | 648 | 504990 | -85.97 | 15.66 | 89.93 | 0.52 | 2.09 | 521 |
| 2024-09-20 22:21:35.773 | MS1 | 121.4656761741 | 31.1446236574 | 648 | 504990 | -91.27 | 14.65 | 93.04 | 0.60 | 2.56 | 632 |
| 2024-09-20 22:21:36.686 | MS1 | 121.4656646524 | 31.1446188412 | 648 | 504990 | -88.06 | 17.44 | 88.16 | 0.52 | 2.87 | 654 |
| 2024-09-20 22:21:37.263 | MS1 | 121.4656754632 | 31.1446239331 | 648 | 504990 | -89.45 | 7.06 | 102.47 | 0.65 | 2.41 | 641 |
| 2024-09-20 22:21:38.696 | MS1 | 121.4656770626 | 31.1446194207 | 648 | 504990 | -90.92 | 7.13 | 82.04 | 0.66 | 2.30 | 682 |
| 2024-09-20 22:21:39.945 | MS1 | 121.4656717797 | 31.1446254727 | 648 | 504990 | -90.02 | 9.28 | 70.41 | 0.70 | 2.37 | 698 |
| 2024-09-20 22:21:40.965 | MS1 | 121.4656734207 | 31.1446212841 | 648 | 504990 | -90.05 | 11.34 | 366.66 | 0.07 | 2.51 | 1584 |
| 2024-09-20 22:21:41.644 | MS1 | 121.4656716931 | 31.1446366226 | 648 | 504990 | -89.67 | 12.17 | 482.93 | 0.14 | 2.83 | 1599 |
| 2024-09-20 22:21:42.533 | MS1 | 121.4656599371 | 31.1446258208 | 648 | 504990 | -91.45 | 12.04 | 579.64 | 0.12 | 2.56 | 1568 |

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
| 3231147 | 4 | 121.4662284345 | 31.1527712794 | 59 | 14 | 4 | 34.0 | TDD | 510 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3263108 | 3 | 121.4724618786 | 31.1441718389 | 340 | 11 | 8 | 47.5 | TDD | 758 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3270093 | 1 | 121.4738026903 | 31.1529175994 | 186 | 3 | 3 | 35.5 | TDD | 648 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3274820 | 2 | 121.4695087924 | 31.1444023372 | 266 | 15 | 3 | 39.3 | TDD | 700 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.545 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.561 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.697 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.697 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.436 | NREventA3 | measId:2;ServCellPCI:767;Se... |
| 2024-09-20 22:21:38.676 | NRHandoverAttempt | SourcePCI:767;SourceNR-ARFC... |
| 2024-09-20 22:21:38.710 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.723 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.848 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.848 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270093 | 1 | 5.8800 | 17.9471 | -114.7060 | 18.7452 | 156.2843 | 0.0115 | 0.0102 |
| 2024_09_20 22:00 | 3274820 | 2 | 8.4105 | 11.3817 | -115.6461 | 8.4230 | 90.8881 | 0.0082 | 0.0184 |
| 2024_09_20 22:00 | 3263108 | 3 | 9.4730 | 6.7601 | -115.8705 | 8.8892 | 121.4727 | 0.0154 | 0.0166 |
| 2024_09_20 22:00 | 3231147 | 4 | 6.7444 | 10.7823 | -114.8388 | 5.7973 | 127.5317 | 0.0114 | 0.0147 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413515_5F3E961F | 504990 | 648 | -86.6 | 504990 | 700 | -88.7 | 504990 | 758 | -99.9 | 504990 | 510 |
| MR_1774413515_37DC9DF8 | 504990 | 648 | -86.0 | 504990 | 700 | -89.1 | 504990 | 758 | -99.9 | 504990 | 510 |
| MR_1774413515_F6F72819 | 504990 | 648 | -86.2 | 504990 | 700 | -91.2 | 504990 | 758 | -99.2 | 504990 | 510 |
| MR_1774413515_3DEB8419 | 504990 | 648 | -87.3 | 504990 | 700 | -89.3 | 504990 | 758 | -97.3 | 504990 | 510 |
| MR_1774413515_C53426A4 | 504990 | 648 | -86.6 | 504990 | 700 | -91.4 | 504990 | 758 | -97.0 | 504990 | 510 |
| MR_1774413515_1B90AFA2 | 504990 | 648 | -84.1 | 504990 | 700 | -91.2 | 504990 | 758 | -97.8 | 504990 | 510 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 154: `82167500-f42...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `82167500-f425-4e89-be2d-ce82b46841b2` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[154] topology](images/test_0154.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Increase transmission power for 3225836_1
- `C3`: Decrease A3 Offset threshold for 3211417_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211417_4
- `C5`: Add neighbor relationship between 3257157_3 and 3225836_1
- `C6`: Press down the tilt angle of 3211417_4 by 10 degrees
- `C7`: Decrease A3 Offset threshold for 3225836_1
- `C8`: Increase transmission power for 3211417_4
- `C9`: Increase A3 Offset threshold for 3211417_4
- `C10`: Decrease transmission power for 3225836_1
- `C11`: Lift the tilt angle of 3211417_4 by 10 degrees
- `C12`: Increase A3 Offset threshold for 3225836_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225836_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225836_1
- `C15`: Adjust the azimuth of 3211417_4 by 50 degrees
- `C16`: Lift the tilt angle  of 3225836_1 by 10 degrees
- `C17`: Decrease transmission power for 3211417_4
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211417_4
- `C19`: Press down the tilt angle  of 3225836_1 by 10 degrees
- `C20`: Add neighbor relationship between 3211417_4 and 3225836_1
- `C21`: Adjust the azimuth of 3225836_1 by 50 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.157 | MS1 | 121.4656662628 | 31.1446289018 | 805 | 504990 | -76.04 | 14.24 | 526.25 | 0.18 | 2.79 | 1574 |
| 2024-09-20 22:21:32.286 | MS1 | 121.4656745143 | 31.1446313007 | 805 | 504990 | -77.68 | 15.80 | 358.83 | 0.19 | 2.99 | 1573 |
| 2024-09-20 22:21:33.795 | MS1 | 121.4656598972 | 31.1446249263 | 805 | 504990 | -77.06 | 13.02 | 590.22 | 0.03 | 2.95 | 1587 |
| 2024-09-20 22:21:34.535 | MS1 | 121.4656643595 | 31.1446292565 | 805 | 504990 | -91.28 | -0.77 | 29.79 | 0.10 | 1.15 | 1591 |
| 2024-09-20 22:21:35.236 | MS1 | 121.4656692590 | 31.1446368047 | 805 | 504990 | -84.72 | -3.98 | 47.03 | 0.15 | 1.28 | 1564 |
| 2024-09-20 22:21:36.850 | MS1 | 121.4656657431 | 31.1446280457 | 805 | 504990 | -85.20 | -3.99 | 32.49 | 0.02 | 1.24 | 1583 |
| 2024-09-20 22:21:37.784 | MS1 | 121.4656737026 | 31.1446196388 | 805 | 504990 | -85.17 | -3.36 | 44.49 | 0.16 | 1.26 | 1574 |
| 2024-09-20 22:21:38.890 | MS1 | 121.4656666576 | 31.1446379916 | 805 | 504990 | -91.62 | -2.67 | 41.09 | 0.02 | 1.28 | 1567 |
| 2024-09-20 22:21:39.402 | MS1 | 121.4656696213 | 31.1446295814 | 289 | 504990 | -81.20 | 13.32 | 194.29 | 0.02 | 1.40 | 1591 |
| 2024-09-20 22:21:40.375 | MS1 | 121.4656635418 | 31.1446302483 | 289 | 504990 | -80.71 | 13.71 | 395.36 | 0.10 | 2.63 | 1567 |
| 2024-09-20 22:21:41.265 | MS1 | 121.4656766572 | 31.1446219358 | 289 | 504990 | -78.71 | 12.49 | 386.04 | 0.19 | 2.35 | 1572 |
| 2024-09-20 22:21:42.665 | MS1 | 121.4656608164 | 31.1446196235 | 289 | 504990 | -80.16 | 12.22 | 331.66 | 0.03 | 2.19 | 1566 |

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
| 3211417 | 4 | 121.4655019692 | 31.1538887533 | 50 | 12 | 3 | 49.0 | TDD | 805 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3225836 | 1 | 121.4721863566 | 31.1519565066 | 135 | 15 | 10 | 23.1 | TDD | 289 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3231758 | 2 | 121.4653755584 | 31.1536699505 | 123 | 3 | 9 | 28.1 | TDD | 59 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3257157 | 3 | 121.4650476129 | 31.1440892997 | 128 | 8 | 11 | 35.3 | TDD | 932 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.241 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.256 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.373 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.373 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.083 | NREventA3 | measId:2;ServCellPCI:851;Se... |
| 2024-09-20 22:21:38.323 | NRHandoverAttempt | SourcePCI:851;SourceNR-ARFC... |
| 2024-09-20 22:21:38.361 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.374 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.479 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.479 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225836 | 1 | 19.6710 | 11.3582 | -114.9121 | 19.9546 | 147.8263 | 0.0127 | 0.0124 |
| 2024_09_20 22:00 | 3231758 | 2 | 19.0712 | 14.7861 | -117.9820 | 13.4084 | 183.6242 | 0.0109 | 0.0064 |
| 2024_09_20 22:00 | 3257157 | 3 | 10.5481 | 9.9481 | -115.2375 | 11.3419 | 102.5915 | 0.0193 | 0.0004 |
| 2024_09_20 22:00 | 3211417 | 4 | 14.7332 | 8.4477 | -114.1518 | 18.2779 | 108.1817 | 0.0143 | 0.1123 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413198_2CC5BC30 | 504990 | 289 | -87.7 | 504990 | 805 | -90.2 | 504990 | 932 | -84.5 | 504990 | 59 |
| MR_1774413198_015713A5 | 504990 | 805 | -91.3 | 504990 | 289 | -84.4 | 504990 | 932 | -87.5 | 504990 | 59 |
| MR_1774413198_90D9975C | 504990 | 805 | -92.3 | 504990 | 289 | -84.0 | 504990 | 932 | -85.2 | 504990 | 59 |
| MR_1774413198_A9AE0F2B | 504990 | 289 | -86.0 | 504990 | 805 | -89.5 | 504990 | 932 | -84.7 | 504990 | 59 |
| MR_1774413198_B965F027 | 504990 | 805 | -90.6 | 504990 | 289 | -85.3 | 504990 | 932 | -86.2 | 504990 | 59 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 155: `da418ba2-d74...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `da418ba2-d746-4441-ad6d-6f44cebb38cd` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[155] topology](images/test_0155.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228975_3
- `C2`: Decrease transmission power for 3228975_3
- `C3`: Lift the tilt angle  of 3228975_3 by 0 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271575_5
- `C5`: Increase A3 Offset threshold for 3271575_5
- `C6`: Adjust the azimuth of 3228975_3 by 24 degrees
- `C7`: Press down the tilt angle  of 3228975_3 by 0 degrees
- `C8`: Lift the tilt angle of 3271575_5 by 6 degrees
- `C9`: Decrease transmission power for 3271575_5
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271575_5
- `C11`: Press down the tilt angle of 3271575_5 by 6 degrees
- `C12`: Add neighbor relationship between 3233214_13 and 3228975_3
- `C13`: Increase transmission power for 3271575_5
- `C14`: Add neighbor relationship between 3271575_5 and 3228975_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228975_3
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase transmission power for 3228975_3
- `C18`: Check test server and transmission issues
- `C19`: Adjust the azimuth of 3271575_5 by 2 degrees
- `C20`: Decrease A3 Offset threshold for 3271575_5
- `C21`: Increase A3 Offset threshold for 3228975_3
- `C22`: Decrease A3 Offset threshold for 3228975_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.568 | MS1 | 121.4656759273 | 31.1446339304 | 86 | 504990 | -94.13 | 9.13 | 352.04 | 0.04 | 2.68 | 1568 |
| 2024-09-20 22:21:32.254 | MS1 | 121.4656720538 | 31.1446312756 | 129 | 504990 | -93.61 | 11.49 | 542.85 | 0.16 | 2.93 | 1575 |
| 2024-09-20 22:21:33.521 | MS1 | 121.4656700672 | 31.1446325861 | 224 | 504990 | -95.86 | 9.50 | 497.01 | 0.17 | 2.04 | 1586 |
| 2024-09-20 22:21:34.377 | MS1 | 121.4656590604 | 31.1446356310 | 490 | 152650 | -87.54 | 3.66 | 56.51 | 0.12 | 1.65 | 971 |
| 2024-09-20 22:21:35.834 | MS1 | 121.4656619874 | 31.1446363306 | 492 | 152650 | -92.13 | 5.19 | 63.10 | 0.01 | 1.85 | 911 |
| 2024-09-20 22:21:36.300 | MS1 | 121.4656747738 | 31.1446345003 | 536 | 152650 | -90.58 | 5.50 | 60.76 | 0.17 | 1.66 | 973 |
| 2024-09-20 22:21:37.881 | MS1 | 121.4656608814 | 31.1446363911 | 150 | 152650 | -90.30 | 7.59 | 58.37 | 0.15 | 1.99 | 928 |
| 2024-09-20 22:21:38.199 | MS1 | 121.4656670591 | 31.1446196281 | 490 | 152650 | -90.88 | 4.39 | 92.61 | 0.14 | 1.76 | 933 |
| 2024-09-20 22:21:39.111 | MS1 | 121.4656768650 | 31.1446348975 | 492 | 152650 | -96.77 | 2.08 | 74.35 | 0.06 | 1.57 | 997 |
| 2024-09-20 22:21:40.279 | MS1 | 121.4656701357 | 31.1446267111 | 536 | 152650 | -90.39 | 4.29 | 87.31 | 0.11 | 2.54 | 1584 |
| 2024-09-20 22:21:41.855 | MS1 | 121.4656697368 | 31.1446355554 | 150 | 152650 | -91.15 | 6.60 | 66.67 | 0.05 | 2.95 | 1573 |
| 2024-09-20 22:21:42.622 | MS1 | 121.4656765805 | 31.1446291750 | 490 | 152650 | -87.36 | 4.44 | 61.92 | 0.03 | 2.09 | 1599 |

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
| 3217900 | 12 | 121.4666416716 | 31.1473377114 | 148 | 4 | 2 | 14.3 | FDD | 471 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3223170 | 11 | 121.4702938715 | 31.1537136401 | 116 | 7 | 9 | 14.8 | FDD | 150 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3224780 | 2 | 121.4652277221 | 31.1523644872 | 14 | 14 | 6 | 23.2 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3228154 | 10 | 121.4741367845 | 31.1500330611 | 260 | 15 | 4 | 2.4 | FDD | 465 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3228975 | 3 | 121.4712017883 | 31.1547472101 | 181 | 0 | 7 | 7.5 | TDD | 705 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3233214 | 13 | 121.4722399158 | 31.1497045120 | 196 | 14 | 3 | 20.2 | FDD | 536 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3234569 | 7 | 121.4675753331 | 31.1519979241 | 108 | 3 | 6 | 23.4 | FDD | 490 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3242071 | 8 | 121.4738993105 | 31.1489052229 | 134 | 2 | 7 | 20.2 | FDD | 492 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3242453 | 6 | 121.4697704032 | 31.1477795575 | 94 | 2 | 2 | 20.8 | TDD | 699 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3246213 | 9 | 121.4663813957 | 31.1535221810 | 210 | 1 | 2 | 14.9 | FDD | 686 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3257293 | 4 | 121.4736283244 | 31.1480076605 | 266 | 3 | 5 | 18.0 | TDD | 169 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3264176 | 1 | 121.4718673210 | 31.1459153872 | 135 | 3 | 10 | 28.4 | TDD | 224 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3271575 | 5 | 121.4697724957 | 31.1453847718 | 256 | 5 | 1 | 5.0 | TDD | 86 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.387 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.407 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.519 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.519 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.239 | NREventA2 | measId:1;ServCellPCI:429;Se... |
| 2024-09-20 22:21:35.362 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.607 | NREventA5 | measId:3;ServCellPCI:429;Se... |
| 2024-09-20 22:21:35.644 | NRHandoverAttempt | SourcePCI:429;SourceNR-ARFC... |
| 2024-09-20 22:21:35.673 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.687 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.834 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.834 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264176 | 1 | 13.5865 | 13.9398 | -116.2282 | 8.3815 | 193.4723 | 0.0114 | 0.0024 |
| 2024_09_20 22:00 | 3224780 | 2 | 14.0241 | 15.5035 | -114.7678 | 14.7994 | 136.2972 | 0.0177 | 0.0075 |
| 2024_09_20 22:00 | 3228975 | 3 | 8.6370 | 5.8881 | -117.4251 | 17.5039 | 103.0242 | 0.0176 | 0.0169 |
| 2024_09_20 22:00 | 3257293 | 4 | 16.8551 | 15.2444 | -115.1749 | 14.4483 | 118.2839 | 0.0074 | 0.0045 |
| 2024_09_20 22:00 | 3271575 | 5 | 16.7626 | 5.6902 | -115.7655 | 18.3034 | 99.3462 | 0.0069 | 0.0058 |
| 2024_09_20 22:00 | 3242453 | 6 | 6.0736 | 17.1116 | -116.8318 | 16.7483 | 183.8615 | 0.0056 | 0.0026 |
| 2024_09_20 22:00 | 3234569 | 7 | 10.3175 | 13.5281 | -115.7200 | 4.8182 | 38.4107 | 0.0184 | 0.0144 |
| 2024_09_20 22:00 | 3242071 | 8 | 9.1528 | 16.9506 | -115.0629 | 3.7301 | 49.6827 | 0.0120 | 0.0104 |
| 2024_09_20 22:00 | 3246213 | 9 | 19.8266 | 6.0771 | -116.0504 | 3.8232 | 48.4260 | 0.0079 | 0.0020 |
| 2024_09_20 22:00 | 3228154 | 10 | 16.7636 | 5.7039 | -116.2526 | 3.7820 | 56.4576 | 0.0163 | 0.0126 |
| 2024_09_20 22:00 | 3223170 | 11 | 19.5304 | 13.2151 | -117.4297 | 4.4497 | 40.6658 | 0.0126 | 0.0087 |
| 2024_09_20 22:00 | 3217900 | 12 | 14.1576 | 18.8831 | -114.7420 | 4.7893 | 55.9370 | 0.0107 | 0.0024 |
| 2024_09_20 22:00 | 3233214 | 13 | 7.7882 | 7.6330 | -116.0127 | 3.1788 | 40.9081 | 0.0176 | 0.0036 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416777_1A2A89F2 | 152650 | 490 | -89.2 | 152650 | 471 | -91.8 | 152650 | 465 | -97.9 | 152650 | 686 |
| MR_1774416777_4EC2B5AB | 152650 | 490 | -86.1 | 152650 | 471 | -91.7 | 152650 | 465 | -98.9 | 152650 | 686 |
| MR_1774416777_29C923B6 | 152650 | 490 | -87.3 | 152650 | 471 | -92.0 | 152650 | 465 | -97.9 | 152650 | 686 |
| MR_1774416777_B8396889 | 152650 | 490 | -87.5 | 152650 | 471 | -91.8 | 152650 | 465 | -96.7 | 152650 | 686 |
| MR_1774416777_F2B44A55 | 504990 | 224 | -96.4 | 504990 | 705 | -93.3 | 504990 | 169 | -98.6 | 504990 | 699 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 156: `6a69251a-4d7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6a69251a-4d70-4458-9e34-87effccf0d01` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[156] topology](images/test_0156.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3216440_3 by 5 degrees
- `C2`: Increase transmission power for 3255820_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255820_4
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Increase A3 Offset threshold for 3276961_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255820_4
- `C7`: Lift the tilt angle  of 3216440_3 by 5 degrees
- `C8`: Adjust the azimuth of 3276961_2 by 0 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276961_2
- `C10`: Decrease A3 Offset threshold for 3276961_2
- `C11`: Decrease transmission power for 3276961_2
- `C12`: Check test server and transmission issues
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276961_2
- `C14`: Press down the tilt angle of 3276961_2 by 5 degrees
- `C15`: Add neighbor relationship between 3276961_2 and 3255820_4
- `C16`: Lift the tilt angle of 3276961_2 by 5 degrees
- `C17`: Add neighbor relationship between 3216440_3 and 3255820_4
- `C18`: Decrease A3 Offset threshold for 3255820_4
- `C19`: Increase transmission power for 3276961_2
- `C20`: Increase A3 Offset threshold for 3255820_4
- `C21`: Decrease transmission power for 3255820_4
- `C22`: Adjust the azimuth of 3216440_3 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.719 | MS1 | 121.4656739217 | 31.1446308569 | 995 | 504990 | -91.31 | 13.82 | 452.14 | 0.09 | 2.70 | 1599 |
| 2024-09-20 22:21:32.783 | MS1 | 121.4656599157 | 31.1446275193 | 995 | 504990 | -90.02 | 16.16 | 520.94 | 0.13 | 2.91 | 1567 |
| 2024-09-20 22:21:33.765 | MS1 | 121.4656707506 | 31.1446230861 | 995 | 504990 | -86.90 | 17.12 | 421.17 | 0.01 | 2.18 | 1571 |
| 2024-09-20 22:21:34.532 | MS1 | 121.4656772183 | 31.1446250547 | 995 | 504990 | -90.07 | 16.45 | 71.95 | 0.09 | 2.17 | 1564 |
| 2024-09-20 22:21:35.147 | MS1 | 121.4656601201 | 31.1446325720 | 995 | 504990 | -90.35 | 17.09 | 61.90 | 0.02 | 2.62 | 1565 |
| 2024-09-20 22:21:36.857 | MS1 | 121.4656771901 | 31.1446346604 | 995 | 504990 | -91.97 | 14.18 | 46.80 | 0.12 | 2.28 | 1564 |
| 2024-09-20 22:21:37.505 | MS1 | 121.4656679743 | 31.1446347551 | 995 | 504990 | -91.10 | 9.35 | 56.27 | 0.14 | 2.89 | 1580 |
| 2024-09-20 22:21:38.373 | MS1 | 121.4656629438 | 31.1446195291 | 995 | 504990 | -91.24 | 10.90 | 59.46 | 0.16 | 2.39 | 1590 |
| 2024-09-20 22:21:39.173 | MS1 | 121.4656707369 | 31.1446338656 | 995 | 504990 | -90.50 | 12.71 | 60.96 | 0.08 | 2.52 | 1589 |
| 2024-09-20 22:21:40.632 | MS1 | 121.4656666842 | 31.1446224763 | 995 | 504990 | -91.84 | 10.60 | 607.82 | 0.06 | 2.63 | 1577 |
| 2024-09-20 22:21:41.906 | MS1 | 121.4656750505 | 31.1446262783 | 995 | 504990 | -92.89 | 7.05 | 603.97 | 0.10 | 2.19 | 1591 |
| 2024-09-20 22:21:42.174 | MS1 | 121.4656697235 | 31.1446249662 | 995 | 504990 | -90.30 | 10.46 | 388.61 | 0.09 | 2.62 | 1577 |

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
| 3211479 | 1 | 121.4752966113 | 31.1550705723 | 214 | 10 | 1 | 40.4 | TDD | 98 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3216440 | 3 | 121.4673416991 | 31.1477002048 | 57 | 10 | 5 | 26.9 | TDD | 868 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3255820 | 4 | 121.4728075448 | 31.1455653715 | 37 | 3 | 3 | 24.3 | TDD | 77 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3276961 | 2 | 121.4677989274 | 31.1544918145 | 190 | 3 | 11 | 42.4 | TDD | 995 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.818 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.835 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.939 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.939 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.622 | NREventA3 | measId:2;ServCellPCI:596;Se... |
| 2024-09-20 22:21:37.862 | NRHandoverAttempt | SourcePCI:596;SourceNR-ARFC... |
| 2024-09-20 22:21:37.892 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.902 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.030 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.030 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211479 | 1 | 8.9888 | 16.1403 | -115.9808 | 5.4116 | 104.3426 | 0.0034 | 0.0036 |
| 2024_09_20 22:00 | 3276961 | 2 | 77.9025 | 82.4039 | -117.1228 | 12.5533 | 118.0278 | 0.0092 | 0.0116 |
| 2024_09_20 22:00 | 3216440 | 3 | 15.2869 | 15.4768 | -117.6466 | 12.2656 | 168.5649 | 0.0158 | 0.0005 |
| 2024_09_20 22:00 | 3255820 | 4 | 8.4693 | 6.5820 | -115.1210 | 12.8784 | 125.7960 | 0.0069 | 0.0163 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415983_F97BDE76 | 504990 | 995 | -88.2 | 504990 | 77 | -97.7 | 504990 | 868 | -96.1 | 504990 | 98 |
| MR_1774415983_FCFFD9B8 | 504990 | 995 | -89.3 | 504990 | 77 | -96.4 | 504990 | 868 | -95.4 | 504990 | 98 |
| MR_1774415983_9893BCE7 | 504990 | 995 | -91.7 | 504990 | 77 | -96.8 | 504990 | 868 | -97.9 | 504990 | 98 |
| MR_1774415983_3094F6B7 | 504990 | 995 | -90.6 | 504990 | 77 | -97.4 | 504990 | 868 | -98.2 | 504990 | 98 |
| MR_1774415983_F34D4CA8 | 504990 | 995 | -90.2 | 504990 | 77 | -97.4 | 504990 | 868 | -95.7 | 504990 | 98 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 157: `0b3595bd-565...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0b3595bd-5654-43ef-bb58-07c6351866ab` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[157] topology](images/test_0157.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3269772_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264710_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269772_4
- `C4`: Add neighbor relationship between 3273984_2 and 3264710_3
- `C5`: Lift the tilt angle of 3269772_4 by 3 degrees
- `C6`: Lift the tilt angle  of 3264710_3 by 10 degrees
- `C7`: Adjust the azimuth of 3269772_4 by 31 degrees
- `C8`: Decrease A3 Offset threshold for 3264710_3
- `C9`: Increase transmission power for 3269772_4
- `C10`: Decrease transmission power for 3269772_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264710_3
- `C12`: Press down the tilt angle  of 3264710_3 by 10 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269772_4
- `C14`: Press down the tilt angle of 3269772_4 by 3 degrees
- `C15`: Increase A3 Offset threshold for 3269772_4
- `C16`: Increase transmission power for 3264710_3
- `C17`: Decrease transmission power for 3264710_3
- `C18`: Adjust the azimuth of 3264710_3 by 42 degrees
- `C19`: Check test server and transmission issues
- `C20`: Increase A3 Offset threshold for 3264710_3
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Add neighbor relationship between 3269772_4 and 3264710_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.132 | MS1 | 121.4656709082 | 31.1446212929 | 303 | 504990 | -89.77 | 16.88 | 428.40 | 0.06 | 2.62 | 1582 |
| 2024-09-20 22:21:32.488 | MS1 | 121.4656712771 | 31.1446227124 | 303 | 504990 | -87.48 | 16.44 | 541.21 | 0.05 | 2.75 | 1577 |
| 2024-09-20 22:21:33.802 | MS1 | 121.4656592536 | 31.1446205512 | 303 | 504990 | -87.50 | 14.26 | 527.41 | 0.10 | 2.61 | 1575 |
| 2024-09-20 22:21:34.146 | MS1 | 121.4656753956 | 31.1446249392 | 303 | 504990 | -90.71 | 13.34 | 89.00 | 0.56 | 2.28 | 546 |
| 2024-09-20 22:21:35.777 | MS1 | 121.4656709361 | 31.1446222193 | 303 | 504990 | -85.74 | 12.76 | 78.31 | 0.64 | 2.17 | 683 |
| 2024-09-20 22:21:36.495 | MS1 | 121.4656667630 | 31.1446249429 | 303 | 504990 | -89.89 | 13.57 | 78.88 | 0.65 | 2.18 | 520 |
| 2024-09-20 22:21:37.445 | MS1 | 121.4656644818 | 31.1446265412 | 303 | 504990 | -90.55 | 12.11 | 61.74 | 0.51 | 2.91 | 597 |
| 2024-09-20 22:21:38.610 | MS1 | 121.4656773511 | 31.1446282761 | 303 | 504990 | -92.11 | 11.58 | 93.15 | 0.67 | 2.45 | 683 |
| 2024-09-20 22:21:39.371 | MS1 | 121.4656664321 | 31.1446354655 | 303 | 504990 | -93.15 | 11.86 | 91.75 | 0.66 | 2.70 | 580 |
| 2024-09-20 22:21:40.838 | MS1 | 121.4656618064 | 31.1446218940 | 303 | 504990 | -90.54 | 8.19 | 577.22 | 0.03 | 2.29 | 1592 |
| 2024-09-20 22:21:41.947 | MS1 | 121.4656739497 | 31.1446188048 | 303 | 504990 | -89.29 | 11.93 | 389.65 | 0.14 | 2.51 | 1562 |
| 2024-09-20 22:21:42.669 | MS1 | 121.4656779471 | 31.1446272498 | 303 | 504990 | -93.20 | 9.79 | 429.43 | 0.16 | 2.95 | 1564 |

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
| 3262311 | 1 | 121.4670371706 | 31.1483360841 | 32 | 15 | 0 | 33.7 | TDD | 625 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3264710 | 3 | 121.4640691388 | 31.1503039138 | 124 | 12 | 6 | 28.6 | TDD | 668 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3269772 | 4 | 121.4722291633 | 31.1468558119 | 217 | 0 | 12 | 30.0 | TDD | 303 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3273984 | 2 | 121.4646222183 | 31.1489292807 | 134 | 13 | 8 | 41.2 | TDD | 690 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.644 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.663 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.786 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.786 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.459 | NREventA3 | measId:2;ServCellPCI:235;Se... |
| 2024-09-20 22:21:38.699 | NRHandoverAttempt | SourcePCI:235;SourceNR-ARFC... |
| 2024-09-20 22:21:38.749 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.761 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.887 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.887 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262311 | 1 | 14.7277 | 13.3034 | -114.5535 | 17.6412 | 146.9727 | 0.0057 | 0.0150 |
| 2024_09_20 22:00 | 3273984 | 2 | 12.2433 | 8.7263 | -115.5034 | 16.3105 | 107.9651 | 0.0022 | 0.0091 |
| 2024_09_20 22:00 | 3264710 | 3 | 12.4004 | 19.4322 | -116.5350 | 17.5088 | 142.9839 | 0.0105 | 0.0007 |
| 2024_09_20 22:00 | 3269772 | 4 | 13.6804 | 15.0487 | -115.3533 | 8.8177 | 169.8714 | 0.0107 | 0.0095 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412844_EF93146E | 504990 | 303 | -90.6 | 504990 | 668 | -97.4 | 504990 | 690 | -97.8 | 504990 | 625 |
| MR_1774412844_625FFCC4 | 504990 | 303 | -91.9 | 504990 | 668 | -97.7 | 504990 | 690 | -98.6 | 504990 | 625 |
| MR_1774412844_9B8CE4AF | 504990 | 303 | -89.2 | 504990 | 668 | -98.7 | 504990 | 690 | -99.7 | 504990 | 625 |
| MR_1774412844_8730634D | 504990 | 303 | -92.1 | 504990 | 668 | -98.7 | 504990 | 690 | -98.6 | 504990 | 625 |
| MR_1774412844_1944DCBC | 504990 | 303 | -91.2 | 504990 | 668 | -97.8 | 504990 | 690 | -97.7 | 504990 | 625 |
| MR_1774412844_C5AB6D36 | 504990 | 303 | -89.0 | 504990 | 668 | -97.3 | 504990 | 690 | -98.6 | 504990 | 625 |
| MR_1774412844_952E797F | 504990 | 303 | -91.4 | 504990 | 668 | -95.7 | 504990 | 690 | -97.2 | 504990 | 625 |
| MR_1774412844_798992E3 | 504990 | 303 | -89.8 | 504990 | 668 | -98.6 | 504990 | 690 | -101.0 | 504990 | 625 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 158: `145a5ef5-557...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `145a5ef5-5576-487b-9d01-c82ba24ea60f` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[158] topology](images/test_0158.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3225973_1
- `C2`: Increase transmission power for 3210553_2
- `C3`: Decrease transmission power for 3210553_2
- `C4`: Decrease A3 Offset threshold for 3225973_1
- `C5`: Decrease A3 Offset threshold for 3210553_2
- `C6`: Increase A3 Offset threshold for 3210553_2
- `C7`: Decrease transmission power for 3225973_1
- `C8`: Adjust the azimuth of 3210553_2 by 50 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Lift the tilt angle  of 3225973_1 by 10 degrees
- `C11`: Increase A3 Offset threshold for 3225973_1
- `C12`: Add neighbor relationship between 3210553_2 and 3225973_1
- `C13`: Check test server and transmission issues
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225973_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210553_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210553_2
- `C17`: Lift the tilt angle of 3210553_2 by 10 degrees
- `C18`: Add neighbor relationship between 3249291_3 and 3225973_1
- `C19`: Press down the tilt angle  of 3225973_1 by 10 degrees
- `C20`: Adjust the azimuth of 3225973_1 by 50 degrees
- `C21`: Press down the tilt angle of 3210553_2 by 10 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225973_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.651 | MS1 | 121.4656581852 | 31.1446188634 | 571 | 504990 | -88.43 | 14.41 | 596.17 | 0.07 | 2.80 | 1565 |
| 2024-09-20 22:21:32.725 | MS1 | 121.4656749950 | 31.1446367392 | 571 | 504990 | -87.49 | 15.16 | 312.02 | 0.12 | 2.01 | 1564 |
| 2024-09-20 22:21:33.555 | MS1 | 121.4656693528 | 31.1446202848 | 571 | 504990 | -85.08 | 12.79 | 553.94 | 0.07 | 2.56 | 1562 |
| 2024-09-20 22:21:34.770 | MS1 | 121.4656702722 | 31.1446251201 | 571 | 504990 | -87.91 | 13.47 | 94.30 | 0.19 | 2.67 | 375 |
| 2024-09-20 22:21:35.291 | MS1 | 121.4656737220 | 31.1446215136 | 571 | 504990 | -89.98 | 16.10 | 82.88 | 0.04 | 2.33 | 376 |
| 2024-09-20 22:21:36.505 | MS1 | 121.4656660884 | 31.1446298150 | 571 | 504990 | -87.70 | 13.45 | 89.38 | 0.10 | 2.06 | 322 |
| 2024-09-20 22:21:37.873 | MS1 | 121.4656673936 | 31.1446197073 | 571 | 504990 | -90.99 | 11.69 | 91.66 | 0.07 | 2.19 | 391 |
| 2024-09-20 22:21:38.698 | MS1 | 121.4656659741 | 31.1446191475 | 571 | 504990 | -92.34 | 9.38 | 62.21 | 0.03 | 2.38 | 318 |
| 2024-09-20 22:21:39.324 | MS1 | 121.4656682657 | 31.1446346770 | 571 | 504990 | -91.09 | 9.74 | 62.53 | 0.01 | 2.46 | 373 |
| 2024-09-20 22:21:40.813 | MS1 | 121.4656647530 | 31.1446377596 | 571 | 504990 | -93.41 | 7.54 | 513.77 | 0.04 | 2.91 | 1588 |
| 2024-09-20 22:21:41.336 | MS1 | 121.4656700228 | 31.1446293825 | 571 | 504990 | -89.92 | 9.88 | 347.30 | 0.18 | 2.45 | 1598 |
| 2024-09-20 22:21:42.996 | MS1 | 121.4656700856 | 31.1446204233 | 571 | 504990 | -89.65 | 9.38 | 364.20 | 0.07 | 2.94 | 1577 |

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
| 3210553 | 2 | 121.4676700219 | 31.1472636244 | 291 | 9 | 12 | 33.3 | TDD | 571 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3225973 | 1 | 121.4751691484 | 31.1451743528 | 110 | 14 | 7 | 34.6 | TDD | 609 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3249291 | 3 | 121.4752696611 | 31.1485634745 | 280 | 2 | 8 | 32.6 | TDD | 764 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3272372 | 4 | 121.4645130097 | 31.1483391492 | 40 | 9 | 3 | 26.7 | TDD | 261 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.532 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.554 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.670 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.670 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.385 | NREventA3 | measId:2;ServCellPCI:565;Se... |
| 2024-09-20 22:21:38.625 | NRHandoverAttempt | SourcePCI:565;SourceNR-ARFC... |
| 2024-09-20 22:21:38.665 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.680 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.790 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.790 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225973 | 1 | 12.7840 | 17.7581 | -115.8564 | 7.3328 | 185.6796 | 0.0148 | 0.0164 |
| 2024_09_20 22:00 | 3210553 | 2 | 6.6522 | 14.5048 | -114.3599 | 11.5344 | 108.5136 | 0.0081 | 0.0186 |
| 2024_09_20 22:00 | 3249291 | 3 | 14.1870 | 8.5564 | -117.1784 | 10.5470 | 192.8949 | 0.0172 | 0.0193 |
| 2024_09_20 22:00 | 3272372 | 4 | 7.8873 | 11.5910 | -116.7026 | 17.6427 | 172.6764 | 0.0079 | 0.0048 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414741_4621AEB8 | 504990 | 571 | -87.3 | 504990 | 609 | -95.4 | 504990 | 764 | -98.8 | 504990 | 261 |
| MR_1774414741_15AF844B | 504990 | 571 | -87.3 | 504990 | 609 | -94.7 | 504990 | 764 | -98.2 | 504990 | 261 |
| MR_1774414741_07EFF750 | 504990 | 571 | -87.5 | 504990 | 609 | -93.1 | 504990 | 764 | -100.3 | 504990 | 261 |
| MR_1774414741_14EA36F0 | 504990 | 571 | -87.3 | 504990 | 609 | -94.6 | 504990 | 764 | -98.0 | 504990 | 261 |
| MR_1774414741_72D86FFE | 504990 | 571 | -87.3 | 504990 | 609 | -96.3 | 504990 | 764 | -99.3 | 504990 | 261 |
| MR_1774414741_465EF055 | 504990 | 571 | -89.3 | 504990 | 609 | -96.2 | 504990 | 764 | -99.0 | 504990 | 261 |
| MR_1774414741_D0844A4E | 504990 | 571 | -88.2 | 504990 | 609 | -94.7 | 504990 | 764 | -99.2 | 504990 | 261 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 159: `5e736544-ed5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5e736544-ed52-46a8-b504-841c7f3110d6` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[159] topology](images/test_0159.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3265542_1
- `C2`: Lift the tilt angle  of 3265542_1 by 4 degrees
- `C3`: Increase transmission power for 3235113_5
- `C4`: Decrease A3 Offset threshold for 3235113_5
- `C5`: Press down the tilt angle  of 3265542_1 by 4 degrees
- `C6`: Decrease transmission power for 3265542_1
- `C7`: Decrease transmission power for 3235113_5
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265542_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235113_5
- `C10`: Adjust the azimuth of 3235113_5 by 8 degrees
- `C11`: Add neighbor relationship between 3270837_3 and 3265542_1
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Increase transmission power for 3265542_1
- `C14`: Increase A3 Offset threshold for 3235113_5
- `C15`: Increase A3 Offset threshold for 3265542_1
- `C16`: Add neighbor relationship between 3235113_5 and 3265542_1
- `C17`: Press down the tilt angle of 3235113_5 by 6 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265542_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235113_5
- `C20`: Lift the tilt angle of 3235113_5 by 6 degrees
- `C21`: Check test server and transmission issues
- `C22`: Adjust the azimuth of 3265542_1 by 36 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.769 | MS1 | 121.4656602698 | 31.1446326632 | 286 | 504990 | -84.14 | 12.91 | 521.88 | 0.20 | 2.05 | 1568 |
| 2024-09-20 22:21:32.342 | MS1 | 121.4656688512 | 31.1446245920 | 286 | 504990 | -83.66 | 12.66 | 331.58 | 0.11 | 2.87 | 1576 |
| 2024-09-20 22:21:33.828 | MS1 | 121.4656746086 | 31.1446304120 | 286 | 504990 | -75.82 | 17.80 | 522.54 | 0.00 | 2.34 | 1597 |
| 2024-09-20 22:21:34.710 | MS1 | 121.4656777925 | 31.1446267531 | 148 | 504990 | -88.00 | 4.45 | 69.75 | 0.14 | 1.16 | 1590 |
| 2024-09-20 22:21:35.514 | MS1 | 121.4656665226 | 31.1446328849 | 148 | 504990 | -86.26 | 1.86 | 45.75 | 0.06 | 1.05 | 1586 |
| 2024-09-20 22:21:36.347 | MS1 | 121.4656667685 | 31.1446363519 | 286 | 504990 | -81.57 | 4.16 | 38.50 | 0.13 | 1.10 | 1567 |
| 2024-09-20 22:21:37.573 | MS1 | 121.4656653397 | 31.1446345434 | 286 | 504990 | -81.12 | 3.92 | 49.08 | 0.13 | 1.43 | 1574 |
| 2024-09-20 22:21:38.619 | MS1 | 121.4656705014 | 31.1446357016 | 148 | 504990 | -88.66 | 1.88 | 79.57 | 0.16 | 1.30 | 1592 |
| 2024-09-20 22:21:39.593 | MS1 | 121.4656607526 | 31.1446336060 | 148 | 504990 | -83.82 | 1.90 | 54.57 | 0.11 | 1.45 | 1580 |
| 2024-09-20 22:21:40.972 | MS1 | 121.4656713913 | 31.1446278767 | 148 | 504990 | -76.81 | 13.09 | 495.43 | 0.12 | 2.29 | 1573 |
| 2024-09-20 22:21:41.577 | MS1 | 121.4656755355 | 31.1446219603 | 148 | 504990 | -81.68 | 15.28 | 571.25 | 0.12 | 2.72 | 1583 |
| 2024-09-20 22:21:42.409 | MS1 | 121.4656747705 | 31.1446275099 | 148 | 504990 | -81.11 | 12.95 | 516.31 | 0.13 | 2.61 | 1577 |

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
| 3215191 | 4 | 121.4738778538 | 31.1471484554 | 180 | 6 | 8 | 44.3 | TDD | 571 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3222997 | 2 | 121.4735086198 | 31.1493365507 | 3 | 9 | 5 | 38.5 | TDD | 148 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3235113 | 5 | 121.4754966216 | 31.1531891935 | 233 | 4 | 5 | 44.2 | TDD | 286 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3265542 | 1 | 121.4689254636 | 31.1475970302 | 187 | 0 | 5 | 30.2 | TDD | 135 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3270837 | 3 | 121.4741968344 | 31.1518400146 | 127 | 2 | 3 | 22.9 | TDD | 596 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.342 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.472 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.472 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.161 | NREventA3 | measId:2;ServCellPCI:961;Se... |
| 2024-09-20 22:21:34.401 | NRHandoverAttempt | SourcePCI:961;SourceNR-ARFC... |
| 2024-09-20 22:21:34.433 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.447 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:34.575 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.575 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.161 | NREventA3 | measId:2;ServCellPCI:634;Se... |
| 2024-09-20 22:21:36.401 | NRHandoverAttempt | SourcePCI:634;SourceNR-ARFC... |
| 2024-09-20 22:21:36.441 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.456 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.569 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.569 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.161 | NREventA3 | measId:2;ServCellPCI:961;Se... |
| 2024-09-20 22:21:38.401 | NRHandoverAttempt | SourcePCI:961;SourceNR-ARFC... |
| 2024-09-20 22:21:38.450 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.461 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.606 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.606 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265542 | 1 | 15.9265 | 19.7367 | -114.2512 | 14.9045 | 101.4041 | 0.0160 | 0.0068 |
| 2024_09_20 22:00 | 3222997 | 2 | 17.6530 | 19.2866 | -117.3119 | 14.8654 | 119.2493 | 0.0080 | 0.0181 |
| 2024_09_20 22:00 | 3270837 | 3 | 10.1399 | 10.2008 | -116.3729 | 12.1299 | 189.9127 | 0.0117 | 0.0149 |
| 2024_09_20 22:00 | 3215191 | 4 | 9.7576 | 14.4370 | -115.3848 | 16.9749 | 168.9667 | 0.0170 | 0.0007 |
| 2024_09_20 22:00 | 3235113 | 5 | 14.0458 | 11.1786 | -115.6060 | 6.6833 | 82.1099 | 0.0158 | 0.0095 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412101_86D51406 | 504990 | 148 | -89.5 | 504990 | 286 | -86.5 | 504990 | 135 | -89.8 | 504990 | 596 |
| MR_1774412101_AFAFFDAC | 504990 | 286 | -87.3 | 504990 | 148 | -88.2 | 504990 | 135 | -89.7 | 504990 | 596 |
| MR_1774412101_0468A0A2 | 504990 | 148 | -89.4 | 504990 | 286 | -87.7 | 504990 | 135 | -90.8 | 504990 | 596 |
| MR_1774412101_C8579ABB | 504990 | 286 | -86.8 | 504990 | 148 | -85.9 | 504990 | 135 | -90.7 | 504990 | 596 |
| MR_1774412101_38A09924 | 504990 | 286 | -88.2 | 504990 | 148 | -86.5 | 504990 | 135 | -90.0 | 504990 | 596 |

> *... 2개 열 생략 (전체 14열)*

---
