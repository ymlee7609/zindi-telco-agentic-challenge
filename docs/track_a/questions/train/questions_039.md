# Track A 문제 분석 — train[380]~train[389]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[380] ~ train[389] (10개)

## 목차

1. [문제 380: `daf76f2e-e2c...`](#380) — single-answer, 정답: C5
2. [문제 381: `74b2c1dc-d2e...`](#381) — single-answer, 정답: C2
3. [문제 382: `3295f277-0c7...`](#382) — single-answer, 정답: C22
4. [문제 383: `924149c8-913...`](#383) — multiple-answer, 정답: C8|C18
5. [문제 384: `da562a7c-d6f...`](#384) — single-answer, 정답: C15
6. [문제 385: `291af336-b67...`](#385) — single-answer, 정답: C20
7. [문제 386: `1a2cbb91-8a6...`](#386) — single-answer, 정답: C6
8. [문제 387: `c69eec7e-5ae...`](#387) — single-answer, 정답: C5
9. [문제 388: `32e23862-229...`](#388) — single-answer, 정답: C15
10. [문제 389: `866091f6-49d...`](#389) — single-answer, 정답: C18

---

### 문제 380: `daf76f2e-e2c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `daf76f2e-e2c9-4442-8dd1-3e85fd801ac1` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[380] topology](images/train_0380.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3256131_3 by 4 degrees
- `C2`: Add neighbor relationship between 3218847_2 and 3256131_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256131_3
- `C4`: Press down the tilt angle of 3218847_2 by 10 degrees
- `C5`: Insufficient data; more data is needed for judgment. **← 정답**
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256131_3
- `C7`: Check test server and transmission issues
- `C8`: Adjust the azimuth of 3256131_3 by 50 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218847_2
- `C10`: Increase A3 Offset threshold for 3256131_3
- `C11`: Increase transmission power for 3256131_3
- `C12`: Lift the tilt angle of 3218847_2 by 10 degrees
- `C13`: Add neighbor relationship between 3231337_4 and 3256131_3
- `C14`: Increase transmission power for 3218847_2
- `C15`: Decrease transmission power for 3218847_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218847_2
- `C17`: Lift the tilt angle  of 3256131_3 by 4 degrees
- `C18`: Increase A3 Offset threshold for 3218847_2
- `C19`: Decrease transmission power for 3256131_3
- `C20`: Adjust the azimuth of 3218847_2 by 50 degrees
- `C21`: Decrease A3 Offset threshold for 3256131_3
- `C22`: Decrease A3 Offset threshold for 3218847_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.531 | MS1 | 121.4656776902 | 31.1446211277 | 891 | 504990 | -91.00 | 17.01 | 462.98 | 0.17 | 2.23 | 1593 |
| 2024-09-20 22:21:32.472 | MS1 | 121.4656628124 | 31.1446358675 | 891 | 504990 | -89.64 | 13.55 | 363.65 | 0.15 | 2.71 | 1600 |
| 2024-09-20 22:21:33.235 | MS1 | 121.4656599463 | 31.1446286062 | 891 | 504990 | -90.40 | 13.67 | 419.95 | 0.07 | 2.47 | 1587 |
| 2024-09-20 22:21:34.646 | MS1 | 121.4656731753 | 31.1446276266 | 891 | 504990 | -91.48 | 14.27 | 81.57 | 0.02 | 2.60 | 1577 |
| 2024-09-20 22:21:35.738 | MS1 | 121.4656713012 | 31.1446207981 | 891 | 504990 | -89.38 | 17.00 | 52.26 | 0.14 | 2.39 | 1591 |
| 2024-09-20 22:21:36.637 | MS1 | 121.4656630521 | 31.1446284258 | 891 | 504990 | -89.19 | 15.15 | 102.73 | 0.09 | 2.96 | 1580 |
| 2024-09-20 22:21:37.458 | MS1 | 121.4656702007 | 31.1446324020 | 891 | 504990 | -90.47 | 8.15 | 68.11 | 0.13 | 2.32 | 1566 |
| 2024-09-20 22:21:38.698 | MS1 | 121.4656700308 | 31.1446365338 | 891 | 504990 | -89.50 | 10.26 | 87.77 | 0.16 | 2.64 | 1561 |
| 2024-09-20 22:21:39.183 | MS1 | 121.4656606147 | 31.1446280693 | 891 | 504990 | -90.86 | 9.01 | 64.85 | 0.12 | 2.79 | 1576 |
| 2024-09-20 22:21:40.146 | MS1 | 121.4656735939 | 31.1446182942 | 891 | 504990 | -92.08 | 12.13 | 322.82 | 0.05 | 2.75 | 1576 |
| 2024-09-20 22:21:41.885 | MS1 | 121.4656754662 | 31.1446186468 | 891 | 504990 | -92.33 | 12.11 | 322.71 | 0.16 | 2.06 | 1574 |
| 2024-09-20 22:21:42.212 | MS1 | 121.4656708187 | 31.1446370058 | 891 | 504990 | -91.15 | 7.35 | 408.66 | 0.18 | 2.64 | 1565 |

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
| 3218847 | 2 | 121.4680235342 | 31.1453756862 | 305 | 0 | 1 | 40.7 | TDD | 891 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3231337 | 4 | 121.4756322095 | 31.1493809422 | 353 | 14 | 10 | 37.3 | TDD | 647 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3256131 | 3 | 121.4751903142 | 31.1544002656 | 305 | 3 | 5 | 20.6 | TDD | 301 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3265070 | 1 | 121.4750229903 | 31.1531234026 | 228 | 8 | 2 | 37.2 | TDD | 962 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.573 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.595 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.719 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.719 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.442 | NREventA3 | measId:2;ServCellPCI:274;Se... |
| 2024-09-20 22:21:38.682 | NRHandoverAttempt | SourcePCI:274;SourceNR-ARFC... |
| 2024-09-20 22:21:38.717 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.730 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.844 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.844 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3265070 | 1 | 80.0267 | 78.6657 | -115.6506 | 8.8889 | 176.5101 | 0.0063 | 0.0101 |
| 2024_09_19 22:00 | 3218847 | 2 | 78.8068 | 79.4649 | -114.3262 | 18.1069 | 130.5242 | 0.0026 | 0.0095 |
| 2024_09_19 22:00 | 3256131 | 3 | 89.8886 | 89.7510 | -114.4667 | 15.7978 | 172.5903 | 0.0058 | 0.0168 |
| 2024_09_19 22:00 | 3231337 | 4 | 83.7052 | 75.5116 | -115.6773 | 14.3236 | 125.1917 | 0.0004 | 0.0074 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412689_CEB314C4 | 504990 | 891 | -91.0 | 504990 | 301 | -92.5 | 504990 | 647 | -104.4 | 504990 | 962 |
| MR_1774412689_BCAC7D4C | 504990 | 891 | -92.9 | 504990 | 301 | -95.9 | 504990 | 647 | -106.2 | 504990 | 962 |
| MR_1774412689_D648166A | 504990 | 891 | -89.8 | 504990 | 301 | -94.1 | 504990 | 647 | -106.3 | 504990 | 962 |
| MR_1774412689_2A546907 | 504990 | 891 | -91.2 | 504990 | 301 | -96.1 | 504990 | 647 | -106.1 | 504990 | 962 |
| MR_1774412689_ED76589D | 504990 | 891 | -91.8 | 504990 | 301 | -95.6 | 504990 | 647 | -106.1 | 504990 | 962 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 381: `74b2c1dc-d2e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `74b2c1dc-d2e2-4f5c-85a5-01bd52debf5b` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[381] topology](images/train_0381.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3232304_4 by 50 degrees
- `C2`: Insufficient data; more data is needed for judgment. **← 정답**
- `C3`: Decrease A3 Offset threshold for 3226885_2
- `C4`: Decrease transmission power for 3226885_2
- `C5`: Add neighbor relationship between 3260645_3 and 3232304_4
- `C6`: Increase A3 Offset threshold for 3232304_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232304_4
- `C8`: Increase transmission power for 3232304_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226885_2
- `C10`: Lift the tilt angle  of 3232304_4 by 10 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232304_4
- `C12`: Increase transmission power for 3226885_2
- `C13`: Decrease transmission power for 3232304_4
- `C14`: Check test server and transmission issues
- `C15`: Lift the tilt angle of 3226885_2 by 8 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226885_2
- `C17`: Press down the tilt angle of 3226885_2 by 8 degrees
- `C18`: Add neighbor relationship between 3226885_2 and 3232304_4
- `C19`: Press down the tilt angle  of 3232304_4 by 10 degrees
- `C20`: Decrease A3 Offset threshold for 3232304_4
- `C21`: Adjust the azimuth of 3226885_2 by 50 degrees
- `C22`: Increase A3 Offset threshold for 3226885_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.724 | MS1 | 121.4656712864 | 31.1446234230 | 599 | 504990 | -87.40 | 17.46 | 416.14 | 0.16 | 2.28 | 1575 |
| 2024-09-20 22:21:32.190 | MS1 | 121.4656734309 | 31.1446287731 | 599 | 504990 | -91.62 | 17.70 | 358.75 | 0.10 | 2.42 | 1562 |
| 2024-09-20 22:21:33.218 | MS1 | 121.4656729623 | 31.1446337316 | 599 | 504990 | -90.53 | 12.81 | 561.72 | 0.19 | 2.26 | 1564 |
| 2024-09-20 22:21:34.605 | MS1 | 121.4656607942 | 31.1446232058 | 599 | 504990 | -85.59 | 17.36 | 71.21 | 0.15 | 2.79 | 1599 |
| 2024-09-20 22:21:35.176 | MS1 | 121.4656774807 | 31.1446378234 | 599 | 504990 | -87.40 | 13.77 | 82.74 | 0.13 | 2.53 | 1579 |
| 2024-09-20 22:21:36.722 | MS1 | 121.4656600197 | 31.1446300719 | 599 | 504990 | -91.46 | 13.37 | 76.62 | 0.04 | 2.04 | 1597 |
| 2024-09-20 22:21:37.105 | MS1 | 121.4656580336 | 31.1446367300 | 599 | 504990 | -93.51 | 10.98 | 54.50 | 0.09 | 2.94 | 1560 |
| 2024-09-20 22:21:38.996 | MS1 | 121.4656666756 | 31.1446294759 | 599 | 504990 | -93.88 | 10.57 | 55.96 | 0.15 | 2.40 | 1590 |
| 2024-09-20 22:21:39.699 | MS1 | 121.4656645059 | 31.1446184945 | 599 | 504990 | -89.27 | 12.33 | 62.87 | 0.19 | 2.29 | 1575 |
| 2024-09-20 22:21:40.831 | MS1 | 121.4656652837 | 31.1446236411 | 599 | 504990 | -89.57 | 9.01 | 572.28 | 0.10 | 2.49 | 1575 |
| 2024-09-20 22:21:41.576 | MS1 | 121.4656640360 | 31.1446269670 | 599 | 504990 | -91.90 | 7.03 | 600.46 | 0.16 | 2.98 | 1588 |
| 2024-09-20 22:21:42.150 | MS1 | 121.4656716124 | 31.1446182390 | 599 | 504990 | -90.86 | 12.51 | 419.74 | 0.05 | 2.50 | 1585 |

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
| 3226885 | 2 | 121.4748098414 | 31.1483029192 | 76 | 7 | 4 | 24.7 | TDD | 599 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3232304 | 4 | 121.4650130723 | 31.1444089896 | 143 | 5 | 6 | 15.2 | TDD | 567 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3260645 | 3 | 121.4700096004 | 31.1455539561 | 281 | 7 | 3 | 41.1 | TDD | 638 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3275399 | 1 | 121.4714007938 | 31.1490229477 | 205 | 3 | 8 | 33.4 | TDD | 706 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.863 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.885 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.007 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.007 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.762 | NREventA3 | measId:2;ServCellPCI:199;Se... |
| 2024-09-20 22:21:38.002 | NRHandoverAttempt | SourcePCI:199;SourceNR-ARFC... |
| 2024-09-20 22:21:38.038 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.051 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.170 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.170 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3275399 | 1 | 89.2526 | 91.0470 | -116.7971 | 9.0387 | 93.4714 | 0.0172 | 0.0027 |
| 2024_09_19 22:00 | 3226885 | 2 | 92.3941 | 88.1725 | -115.4154 | 16.1965 | 110.0386 | 0.0119 | 0.0078 |
| 2024_09_19 22:00 | 3260645 | 3 | 84.8566 | 84.5531 | -117.1491 | 16.8730 | 136.5742 | 0.0012 | 0.0071 |
| 2024_09_19 22:00 | 3232304 | 4 | 89.0637 | 91.9021 | -116.4165 | 12.5657 | 175.8618 | 0.0166 | 0.0016 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413591_391AEE65 | 504990 | 599 | -84.1 | 504990 | 567 | -88.1 | 504990 | 638 | -98.8 | 504990 | 706 |
| MR_1774413591_C5111D07 | 504990 | 599 | -86.5 | 504990 | 567 | -89.3 | 504990 | 638 | -94.9 | 504990 | 706 |
| MR_1774413591_AA67CB3C | 504990 | 599 | -86.5 | 504990 | 567 | -86.0 | 504990 | 638 | -97.8 | 504990 | 706 |
| MR_1774413591_914B2DD2 | 504990 | 599 | -87.3 | 504990 | 567 | -86.2 | 504990 | 638 | -96.5 | 504990 | 706 |
| MR_1774413591_54207FE1 | 504990 | 599 | -84.3 | 504990 | 567 | -86.0 | 504990 | 638 | -97.3 | 504990 | 706 |
| MR_1774413591_EE876160 | 504990 | 599 | -85.9 | 504990 | 567 | -88.5 | 504990 | 638 | -96.5 | 504990 | 706 |
| MR_1774413591_152B7F24 | 504990 | 599 | -85.4 | 504990 | 567 | -86.2 | 504990 | 638 | -98.1 | 504990 | 706 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 382: `3295f277-0c7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3295f277-0c79-457a-a2bd-c26122c99c59` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275521_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[382] topology](images/train_0382.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3263969_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263969_3
- `C3`: Adjust the azimuth of 3263969_3 by 27 degrees
- `C4`: Add neighbor relationship between 3228001_11 and 3263969_3
- `C5`: Add neighbor relationship between 3275521_1 and 3263969_3
- `C6`: Lift the tilt angle  of 3263969_3 by 5 degrees
- `C7`: Increase A3 Offset threshold for 3263969_3
- `C8`: Lift the tilt angle of 3275521_1 by 4 degrees
- `C9`: Decrease transmission power for 3275521_1
- `C10`: Increase A3 Offset threshold for 3275521_1
- `C11`: Decrease transmission power for 3263969_3
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease A3 Offset threshold for 3263969_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275521_1
- `C15`: Press down the tilt angle of 3275521_1 by 4 degrees
- `C16`: Increase transmission power for 3275521_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263969_3
- `C18`: Adjust the azimuth of 3275521_1 by 1 degrees
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle  of 3263969_3 by 5 degrees
- `C21`: Decrease A3 Offset threshold for 3275521_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275521_1 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.900 | MS1 | 121.4656628263 | 31.1446271734 | 34 | 504990 | -94.47 | 14.97 | 305.24 | 0.00 | 2.12 | 1572 |
| 2024-09-20 22:21:32.326 | MS1 | 121.4656744154 | 31.1446344077 | 607 | 504990 | -95.46 | 11.48 | 450.56 | 0.04 | 2.51 | 1569 |
| 2024-09-20 22:21:33.760 | MS1 | 121.4656582877 | 31.1446297540 | 698 | 504990 | -95.03 | 10.80 | 370.15 | 0.09 | 2.73 | 1592 |
| 2024-09-20 22:21:34.407 | MS1 | 121.4656627580 | 31.1446188025 | 817 | 152650 | -87.78 | 7.62 | 99.05 | 0.04 | 2.00 | 900 |
| 2024-09-20 22:21:35.488 | MS1 | 121.4656644073 | 31.1446258947 | 826 | 152650 | -95.68 | 6.99 | 79.80 | 0.12 | 1.82 | 990 |
| 2024-09-20 22:21:36.111 | MS1 | 121.4656667202 | 31.1446318043 | 531 | 152650 | -88.31 | 3.92 | 78.37 | 0.09 | 1.98 | 952 |
| 2024-09-20 22:21:37.912 | MS1 | 121.4656597457 | 31.1446369482 | 688 | 152650 | -92.31 | 5.72 | 90.09 | 0.14 | 1.92 | 983 |
| 2024-09-20 22:21:38.727 | MS1 | 121.4656751292 | 31.1446316049 | 817 | 152650 | -95.62 | 2.20 | 64.27 | 0.00 | 1.64 | 971 |
| 2024-09-20 22:21:39.384 | MS1 | 121.4656769154 | 31.1446323795 | 826 | 152650 | -89.98 | 6.32 | 76.96 | 0.09 | 1.86 | 927 |
| 2024-09-20 22:21:40.336 | MS1 | 121.4656680367 | 31.1446207940 | 531 | 152650 | -92.90 | 3.57 | 65.86 | 0.13 | 2.96 | 1590 |
| 2024-09-20 22:21:41.702 | MS1 | 121.4656599840 | 31.1446335551 | 688 | 152650 | -95.74 | 4.02 | 81.74 | 0.04 | 2.64 | 1589 |
| 2024-09-20 22:21:42.745 | MS1 | 121.4656734741 | 31.1446331682 | 817 | 152650 | -94.31 | 5.80 | 57.09 | 0.16 | 2.52 | 1569 |

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
| 3211761 | 13 | 121.4701069094 | 31.1520083329 | 293 | 5 | 5 | 10.8 | FDD | 413 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3214232 | 6 | 121.4693127647 | 31.1478230315 | 188 | 11 | 5 | 17.9 | TDD | 607 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3214464 | 2 | 121.4689071596 | 31.1504893476 | 314 | 12 | 4 | 3.0 | TDD | 684 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3221178 | 5 | 121.4660289233 | 31.1513776565 | 327 | 5 | 6 | 20.9 | TDD | 698 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3228001 | 11 | 121.4755578699 | 31.1558276996 | 189 | 7 | 10 | 1.2 | FDD | 531 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3229129 | 4 | 121.4646900271 | 31.1514333929 | 289 | 12 | 3 | 23.3 | TDD | 595 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3233908 | 9 | 121.4640015091 | 31.1462519590 | 49 | 3 | 12 | 25.1 | FDD | 817 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3249282 | 8 | 121.4641790077 | 31.1456753577 | 222 | 10 | 2 | 26.4 | FDD | 688 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3257042 | 10 | 121.4687359432 | 31.1522219014 | 235 | 12 | 9 | 13.5 | FDD | 81 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3257971 | 12 | 121.4726853393 | 31.1467224915 | 295 | 14 | 12 | 20.0 | FDD | 826 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3263969 | 3 | 121.4738693847 | 31.1443678494 | 245 | 4 | 3 | 19.0 | TDD | 208 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3275521 | 1 | 121.4652692874 | 31.1506150000 | 176 | 3 | 4 | 13.9 | TDD | 34 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3277868 | 7 | 121.4695701495 | 31.1487052852 | 343 | 8 | 0 | 18.3 | FDD | 335 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |

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
| 2024-09-20 22:21:31.238 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.361 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.361 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.059 | NREventA2 | measId:1;ServCellPCI:281;Se... |
| 2024-09-20 22:21:35.191 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.400 | NREventA5 | measId:3;ServCellPCI:281;Se... |
| 2024-09-20 22:21:35.430 | NRHandoverAttempt | SourcePCI:281;SourceNR-ARFC... |
| 2024-09-20 22:21:35.451 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.463 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.601 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.601 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275521 | 1 | 8.6090 | 11.5785 | -115.0771 | 18.3423 | 99.5694 | 0.0071 | 0.0173 |
| 2024_09_20 22:00 | 3214464 | 2 | 18.3211 | 19.7535 | -115.8675 | 7.8990 | 197.7425 | 0.0062 | 0.0033 |
| 2024_09_20 22:00 | 3263969 | 3 | 9.0357 | 15.5641 | -117.9400 | 18.6703 | 129.1376 | 0.0132 | 0.0175 |
| 2024_09_20 22:00 | 3229129 | 4 | 6.9862 | 16.2181 | -117.9571 | 5.7955 | 113.6219 | 0.0192 | 0.0023 |
| 2024_09_20 22:00 | 3221178 | 5 | 14.8442 | 12.9290 | -115.3879 | 13.6298 | 167.4084 | 0.0196 | 0.0118 |
| 2024_09_20 22:00 | 3214232 | 6 | 13.5934 | 18.6447 | -117.8836 | 19.8600 | 142.7004 | 0.0156 | 0.0093 |
| 2024_09_20 22:00 | 3277868 | 7 | 6.4554 | 14.0218 | -114.1846 | 4.0153 | 58.3601 | 0.0092 | 0.0169 |
| 2024_09_20 22:00 | 3249282 | 8 | 8.8458 | 18.8325 | -116.1474 | 4.1285 | 53.0336 | 0.0023 | 0.0195 |
| 2024_09_20 22:00 | 3233908 | 9 | 6.0038 | 10.1089 | -115.6616 | 3.2835 | 55.0210 | 0.0124 | 0.0086 |
| 2024_09_20 22:00 | 3257042 | 10 | 18.3906 | 13.0931 | -114.5950 | 3.3293 | 37.0470 | 0.0033 | 0.0176 |
| 2024_09_20 22:00 | 3228001 | 11 | 6.5730 | 13.3415 | -117.8922 | 4.8400 | 53.1423 | 0.0133 | 0.0048 |
| 2024_09_20 22:00 | 3257971 | 12 | 5.6650 | 13.1990 | -117.1370 | 4.5370 | 53.4892 | 0.0008 | 0.0192 |
| 2024_09_20 22:00 | 3211761 | 13 | 13.1949 | 12.0025 | -117.2978 | 3.8173 | 47.3595 | 0.0091 | 0.0022 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414557_8409537C | 504990 | 698 | -96.8 | 504990 | 208 | -94.3 | 504990 | 595 | -98.2 | 504990 | 684 |
| MR_1774414557_44C27545 | 504990 | 698 | -97.0 | 504990 | 208 | -93.5 | 504990 | 595 | -99.3 | 504990 | 684 |
| MR_1774414557_70A466A2 | 152650 | 817 | -86.2 | 152650 | 413 | -95.6 | 152650 | 335 | -97.3 | 152650 | 81 |
| MR_1774414557_72DE7B8D | 504990 | 698 | -95.4 | 504990 | 208 | -92.9 | 504990 | 595 | -99.9 | 504990 | 684 |
| MR_1774414557_E5E2D87D | 504990 | 698 | -95.3 | 504990 | 208 | -93.3 | 504990 | 595 | -98.9 | 504990 | 684 |
| MR_1774414557_199DDA1B | 504990 | 698 | -94.1 | 504990 | 208 | -91.3 | 504990 | 595 | -100.6 | 504990 | 684 |
| MR_1774414557_C05B4DF6 | 152650 | 817 | -87.5 | 152650 | 413 | -95.4 | 152650 | 335 | -97.5 | 152650 | 81 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 383: `924149c8-913...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `924149c8-9132-47da-917e-a2130bd3b0fb` |
| Tag | **multiple-answer** |
| 정답 | **C8|C18** |
| C8 의미 | Increase transmission power for 3257784_1 |
| C18 의미 | Adjust the azimuth of 3257784_1 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[383] topology](images/train_0383.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235232_4
- `C2`: Add neighbor relationship between 3257784_1 and 3235232_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257784_1
- `C4`: Add neighbor relationship between 3246503_3 and 3235232_4
- `C5`: Press down the tilt angle of 3257784_1 by 5 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235232_4
- `C7`: Lift the tilt angle of 3257784_1 by 5 degrees
- `C8`: Increase transmission power for 3257784_1 **← 정답**
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257784_1
- `C10`: Press down the tilt angle  of 3235232_4 by 4 degrees
- `C11`: Decrease transmission power for 3235232_4
- `C12`: Increase transmission power for 3235232_4
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Lift the tilt angle  of 3235232_4 by 4 degrees
- `C15`: Decrease A3 Offset threshold for 3235232_4
- `C16`: Decrease A3 Offset threshold for 3257784_1
- `C17`: Increase A3 Offset threshold for 3257784_1
- `C18`: Adjust the azimuth of 3257784_1 by 50 degrees **← 정답**
- `C19`: Increase A3 Offset threshold for 3235232_4
- `C20`: Check test server and transmission issues
- `C21`: Adjust the azimuth of 3235232_4 by 18 degrees
- `C22`: Decrease transmission power for 3257784_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.874 | MS1 | 121.4656587476 | 31.1446215956 | 906 | 504990 | -86.44 | 13.21 | 431.39 | 0.16 | 2.15 | 1588 |
| 2024-09-20 22:21:32.552 | MS1 | 121.4656707298 | 31.1446369982 | 906 | 504990 | -86.67 | 14.77 | 548.38 | 0.08 | 2.22 | 1573 |
| 2024-09-20 22:21:33.922 | MS1 | 121.4656768705 | 31.1446318074 | 906 | 504990 | -85.28 | 16.19 | 457.21 | 0.06 | 2.99 | 1572 |
| 2024-09-20 22:21:34.439 | MS1 | 121.4656707353 | 31.1446289688 | 906 | 504990 | -105.50 | -0.95 | 61.09 | 0.04 | 1.20 | 1573 |
| 2024-09-20 22:21:35.635 | MS1 | 121.4656719446 | 31.1446254250 | 906 | 504990 | -109.53 | -1.11 | 35.17 | 0.13 | 1.32 | 1592 |
| 2024-09-20 22:21:36.590 | MS1 | 121.4656650023 | 31.1446301121 | 906 | 504990 | -108.46 | 1.67 | 71.69 | 0.10 | 1.46 | 1574 |
| 2024-09-20 22:21:37.357 | MS1 | 121.4656643338 | 31.1446369587 | 906 | 504990 | -109.21 | 0.75 | 62.84 | 0.14 | 1.05 | 1598 |
| 2024-09-20 22:21:38.285 | MS1 | 121.4656649991 | 31.1446232098 | 906 | 504990 | -107.52 | -1.04 | 70.81 | 0.13 | 1.46 | 1600 |
| 2024-09-20 22:21:39.886 | MS1 | 121.4656582090 | 31.1446278079 | 906 | 504990 | -106.97 | -1.80 | 35.77 | 0.03 | 1.35 | 1582 |
| 2024-09-20 22:21:40.216 | MS1 | 121.4656765949 | 31.1446189735 | 906 | 504990 | -92.36 | 16.05 | 593.38 | 0.13 | 2.45 | 1600 |
| 2024-09-20 22:21:41.301 | MS1 | 121.4656681519 | 31.1446350643 | 906 | 504990 | -89.20 | 16.34 | 342.48 | 0.11 | 2.88 | 1572 |
| 2024-09-20 22:21:42.244 | MS1 | 121.4656692587 | 31.1446375330 | 906 | 504990 | -88.12 | 14.32 | 317.74 | 0.03 | 2.36 | 1576 |

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
| 3235232 | 4 | 121.4728043210 | 31.1444633751 | 290 | 1 | 2 | 35.1 | TDD | 319 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3242791 | 2 | 121.4655307862 | 31.1449533291 | 212 | 0 | 3 | 32.0 | TDD | 899 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3246503 | 3 | 121.4676557937 | 31.1470226574 | 323 | 4 | 2 | 40.4 | TDD | 260 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3257784 | 1 | 121.4653563638 | 31.1535278281 | 241 | 3 | 5 | 33.1 | TDD | 906 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.424 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.446 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.584 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.584 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.788 | NREventA2 | measId:1;ServCellPCI:679;Se... |
| 2024-09-20 22:21:34.898 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257784 | 1 | 7.5557 | 9.6588 | -117.7731 | 6.1434 | 80.4837 | 0.1615 | 0.0118 |
| 2024_09_20 22:00 | 3242791 | 2 | 8.7092 | 6.0368 | -114.4756 | 7.9562 | 174.5051 | 0.0070 | 0.0098 |
| 2024_09_20 22:00 | 3246503 | 3 | 7.4313 | 16.5578 | -115.1978 | 10.0581 | 164.8716 | 0.0173 | 0.0025 |
| 2024_09_20 22:00 | 3235232 | 4 | 17.4252 | 11.5486 | -115.5704 | 6.6172 | 112.2411 | 0.0143 | 0.0091 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413513_D9613B76 | 504990 | 906 | -106.6 | 504990 | 319 | -113.1 | 504990 | 260 | -116.2 | 504990 | 899 |
| MR_1774413513_50B47E87 | 504990 | 906 | -106.3 | 504990 | 319 | -111.5 | 504990 | 260 | -117.4 | 504990 | 899 |
| MR_1774413513_D00F6F23 | 504990 | 906 | -103.8 | 504990 | 319 | -111.3 | 504990 | 260 | -116.9 | 504990 | 899 |
| MR_1774413513_1B6321ED | 504990 | 906 | -103.6 | 504990 | 319 | -110.0 | 504990 | 260 | -117.1 | 504990 | 899 |
| MR_1774413513_47472595 | 504990 | 906 | -106.1 | 504990 | 319 | -111.1 | 504990 | 260 | -119.4 | 504990 | 899 |
| MR_1774413513_50E2B125 | 504990 | 906 | -105.6 | 504990 | 319 | -111.6 | 504990 | 260 | -116.5 | 504990 | 899 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 384: `da562a7c-d6f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `da562a7c-d6fc-4649-88e6-abce115f3159` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[384] topology](images/train_0384.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3250958_1 and 3277620_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277620_4
- `C3`: Press down the tilt angle  of 3277620_4 by 10 degrees
- `C4`: Press down the tilt angle of 3250958_1 by 10 degrees
- `C5`: Check test server and transmission issues
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277620_4
- `C7`: Increase transmission power for 3250958_1
- `C8`: Adjust the azimuth of 3277620_4 by 50 degrees
- `C9`: Increase A3 Offset threshold for 3277620_4
- `C10`: Increase A3 Offset threshold for 3250958_1
- `C11`: Decrease A3 Offset threshold for 3250958_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250958_1
- `C13`: Decrease A3 Offset threshold for 3277620_4
- `C14`: Decrease transmission power for 3250958_1
- `C15`: Insufficient data; more data is needed for judgment. **← 정답**
- `C16`: Lift the tilt angle of 3250958_1 by 10 degrees
- `C17`: Decrease transmission power for 3277620_4
- `C18`: Lift the tilt angle  of 3277620_4 by 10 degrees
- `C19`: Increase transmission power for 3277620_4
- `C20`: Adjust the azimuth of 3250958_1 by 50 degrees
- `C21`: Add neighbor relationship between 3214972_2 and 3277620_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250958_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.171 | MS1 | 121.4656701294 | 31.1446193755 | 432 | 504990 | -88.32 | 14.52 | 395.01 | 0.17 | 2.30 | 1585 |
| 2024-09-20 22:21:32.779 | MS1 | 121.4656582586 | 31.1446310255 | 432 | 504990 | -86.81 | 13.18 | 521.12 | 0.14 | 2.60 | 1581 |
| 2024-09-20 22:21:33.947 | MS1 | 121.4656719703 | 31.1446353467 | 432 | 504990 | -91.99 | 12.07 | 343.61 | 0.03 | 2.26 | 1586 |
| 2024-09-20 22:21:34.493 | MS1 | 121.4656600565 | 31.1446186263 | 432 | 504990 | -89.77 | 13.17 | 90.49 | 0.06 | 2.28 | 1591 |
| 2024-09-20 22:21:35.465 | MS1 | 121.4656624486 | 31.1446215754 | 432 | 504990 | -90.17 | 14.60 | 67.94 | 0.04 | 2.13 | 1562 |
| 2024-09-20 22:21:36.450 | MS1 | 121.4656656697 | 31.1446347294 | 432 | 504990 | -86.64 | 12.27 | 89.80 | 0.18 | 2.63 | 1584 |
| 2024-09-20 22:21:37.855 | MS1 | 121.4656741363 | 31.1446250520 | 432 | 504990 | -93.66 | 8.70 | 80.59 | 0.13 | 2.82 | 1574 |
| 2024-09-20 22:21:38.225 | MS1 | 121.4656610015 | 31.1446252378 | 432 | 504990 | -89.82 | 12.61 | 71.70 | 0.12 | 2.07 | 1576 |
| 2024-09-20 22:21:39.837 | MS1 | 121.4656582545 | 31.1446372595 | 432 | 504990 | -92.80 | 8.14 | 91.09 | 0.16 | 2.38 | 1591 |
| 2024-09-20 22:21:40.630 | MS1 | 121.4656654975 | 31.1446372815 | 432 | 504990 | -91.14 | 12.80 | 423.09 | 0.01 | 2.78 | 1574 |
| 2024-09-20 22:21:41.274 | MS1 | 121.4656583922 | 31.1446189571 | 432 | 504990 | -93.00 | 10.18 | 522.46 | 0.07 | 2.92 | 1581 |
| 2024-09-20 22:21:42.741 | MS1 | 121.4656725455 | 31.1446291485 | 432 | 504990 | -89.60 | 7.78 | 471.78 | 0.18 | 2.76 | 1573 |

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
| 3214972 | 2 | 121.4696038610 | 31.1474485152 | 132 | 12 | 4 | 37.1 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3250958 | 1 | 121.4695049297 | 31.1474699100 | 313 | 10 | 2 | 17.3 | TDD | 432 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3265571 | 3 | 121.4721952490 | 31.1501284060 | 132 | 9 | 7 | 40.4 | TDD | 160 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3277620 | 4 | 121.4758243499 | 31.1479392717 | 321 | 9 | 4 | 45.2 | TDD | 751 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.817 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.955 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.955 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.680 | NREventA3 | measId:2;ServCellPCI:322;Se... |
| 2024-09-20 22:21:37.920 | NRHandoverAttempt | SourcePCI:322;SourceNR-ARFC... |
| 2024-09-20 22:21:37.969 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.981 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.110 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.110 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3250958 | 1 | 92.3942 | 79.7090 | -114.8804 | 6.5364 | 115.8037 | 0.0186 | 0.0022 |
| 2024_09_19 22:00 | 3214972 | 2 | 86.2147 | 87.9831 | -115.3567 | 7.6064 | 110.6176 | 0.0006 | 0.0120 |
| 2024_09_19 22:00 | 3265571 | 3 | 82.3769 | 77.1485 | -117.7397 | 18.7620 | 137.9114 | 0.0161 | 0.0058 |
| 2024_09_19 22:00 | 3277620 | 4 | 91.0471 | 77.0134 | -117.6019 | 7.5855 | 110.4393 | 0.0172 | 0.0192 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415354_68E94B19 | 504990 | 432 | -89.3 | 504990 | 751 | -92.7 | 504990 | 866 | -95.2 | 504990 | 160 |
| MR_1774415354_4CAF9C6C | 504990 | 432 | -90.1 | 504990 | 751 | -95.0 | 504990 | 866 | -95.2 | 504990 | 160 |
| MR_1774415354_19E3764F | 504990 | 432 | -88.4 | 504990 | 751 | -93.4 | 504990 | 866 | -97.3 | 504990 | 160 |
| MR_1774415354_78B2F914 | 504990 | 432 | -89.0 | 504990 | 751 | -95.4 | 504990 | 866 | -96.1 | 504990 | 160 |
| MR_1774415354_840D2E37 | 504990 | 432 | -89.2 | 504990 | 751 | -92.2 | 504990 | 866 | -98.7 | 504990 | 160 |
| MR_1774415354_DC085C6B | 504990 | 432 | -89.6 | 504990 | 751 | -95.1 | 504990 | 866 | -97.2 | 504990 | 160 |
| MR_1774415354_57F86BEE | 504990 | 432 | -88.1 | 504990 | 751 | -92.7 | 504990 | 866 | -97.6 | 504990 | 160 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 385: `291af336-b67...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `291af336-b675-4951-91e2-af4acfa95372` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3243147_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[385] topology](images/train_0385.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3210429_4
- `C2`: Add neighbor relationship between 3236529_3 and 3210429_4
- `C3`: Increase transmission power for 3243147_1
- `C4`: Lift the tilt angle  of 3210429_4 by 10 degrees
- `C5`: Adjust the azimuth of 3210429_4 by 23 degrees
- `C6`: Decrease A3 Offset threshold for 3243147_1
- `C7`: Decrease transmission power for 3243147_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243147_1
- `C9`: Decrease A3 Offset threshold for 3210429_4
- `C10`: Press down the tilt angle  of 3210429_4 by 10 degrees
- `C11`: Increase A3 Offset threshold for 3243147_1
- `C12`: Lift the tilt angle of 3243147_1 by 3 degrees
- `C13`: Press down the tilt angle of 3243147_1 by 3 degrees
- `C14`: Increase A3 Offset threshold for 3210429_4
- `C15`: Check test server and transmission issues
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210429_4
- `C17`: Adjust the azimuth of 3243147_1 by 40 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210429_4
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243147_1 **← 정답**
- `C21`: Add neighbor relationship between 3243147_1 and 3210429_4
- `C22`: Decrease transmission power for 3210429_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.524 | MS1 | 121.4656700496 | 31.1446214314 | 113 | 504990 | -85.27 | 15.15 | 572.46 | 0.01 | 3.00 | 1588 |
| 2024-09-20 22:21:32.644 | MS1 | 121.4656750760 | 31.1446318809 | 113 | 504990 | -87.63 | 15.10 | 339.42 | 0.03 | 2.21 | 1561 |
| 2024-09-20 22:21:33.447 | MS1 | 121.4656655519 | 31.1446268473 | 113 | 504990 | -87.22 | 12.06 | 312.53 | 0.12 | 2.51 | 1582 |
| 2024-09-20 22:21:34.258 | MS1 | 121.4656713813 | 31.1446212678 | 113 | 504990 | -87.94 | 12.76 | 81.95 | 0.50 | 2.89 | 587 |
| 2024-09-20 22:21:35.356 | MS1 | 121.4656767256 | 31.1446266919 | 113 | 504990 | -86.69 | 16.57 | 82.94 | 0.59 | 2.60 | 560 |
| 2024-09-20 22:21:36.143 | MS1 | 121.4656674182 | 31.1446320875 | 113 | 504990 | -91.70 | 17.54 | 57.91 | 0.62 | 2.42 | 617 |
| 2024-09-20 22:21:37.225 | MS1 | 121.4656690885 | 31.1446182309 | 113 | 504990 | -91.00 | 8.59 | 66.64 | 0.70 | 2.51 | 539 |
| 2024-09-20 22:21:38.173 | MS1 | 121.4656606555 | 31.1446262888 | 113 | 504990 | -89.62 | 10.88 | 96.27 | 0.62 | 2.35 | 660 |
| 2024-09-20 22:21:39.416 | MS1 | 121.4656740896 | 31.1446314861 | 113 | 504990 | -91.64 | 9.77 | 93.03 | 0.64 | 2.47 | 693 |
| 2024-09-20 22:21:40.370 | MS1 | 121.4656712287 | 31.1446302500 | 113 | 504990 | -93.20 | 10.90 | 433.15 | 0.20 | 2.27 | 1564 |
| 2024-09-20 22:21:41.549 | MS1 | 121.4656632572 | 31.1446372678 | 113 | 504990 | -91.06 | 8.53 | 562.94 | 0.02 | 2.55 | 1574 |
| 2024-09-20 22:21:42.822 | MS1 | 121.4656678954 | 31.1446323623 | 113 | 504990 | -93.67 | 12.65 | 440.32 | 0.19 | 2.76 | 1586 |

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
| 3210429 | 4 | 121.4655929844 | 31.1448494459 | 141 | 13 | 9 | 19.8 | TDD | 662 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3236529 | 3 | 121.4714813843 | 31.1511097802 | 145 | 8 | 8 | 20.9 | TDD | 723 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3243147 | 1 | 121.4749968129 | 31.1530184854 | 264 | 1 | 5 | 49.4 | TDD | 113 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3247352 | 2 | 121.4672288352 | 31.1527849325 | 50 | 9 | 2 | 29.2 | TDD | 178 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.010 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.034 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.140 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.140 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.829 | NREventA3 | measId:2;ServCellPCI:261;Se... |
| 2024-09-20 22:21:38.069 | NRHandoverAttempt | SourcePCI:261;SourceNR-ARFC... |
| 2024-09-20 22:21:38.114 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.126 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.230 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.230 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243147 | 1 | 19.5321 | 17.4952 | -116.9822 | 17.9045 | 83.6923 | 0.0061 | 0.0172 |
| 2024_09_20 22:00 | 3247352 | 2 | 13.5647 | 17.2328 | -116.0125 | 14.5342 | 112.5521 | 0.0114 | 0.0162 |
| 2024_09_20 22:00 | 3236529 | 3 | 13.1458 | 6.0028 | -116.9978 | 16.3762 | 97.9848 | 0.0071 | 0.0138 |
| 2024_09_20 22:00 | 3210429 | 4 | 11.8624 | 7.0328 | -117.1177 | 10.0679 | 168.0880 | 0.0149 | 0.0038 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416431_E5DF38CE | 504990 | 113 | -89.7 | 504990 | 662 | -97.0 | 504990 | 723 | -101.4 | 504990 | 178 |
| MR_1774416431_D67BFBC0 | 504990 | 113 | -89.2 | 504990 | 662 | -96.0 | 504990 | 723 | -100.9 | 504990 | 178 |
| MR_1774416431_4010DAD7 | 504990 | 113 | -87.9 | 504990 | 662 | -99.5 | 504990 | 723 | -100.0 | 504990 | 178 |
| MR_1774416431_B19A1CBF | 504990 | 113 | -87.6 | 504990 | 662 | -98.9 | 504990 | 723 | -103.0 | 504990 | 178 |
| MR_1774416431_C6D9CAF2 | 504990 | 113 | -89.6 | 504990 | 662 | -96.1 | 504990 | 723 | -100.2 | 504990 | 178 |
| MR_1774416431_BA5F5ED3 | 504990 | 113 | -86.2 | 504990 | 662 | -98.2 | 504990 | 723 | -99.8 | 504990 | 178 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 386: `1a2cbb91-8a6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1a2cbb91-8a6e-4978-9798-ac273f5f3c4c` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Lift the tilt angle  of 3248314_4 by 5 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[386] topology](images/train_0386.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245454_3
- `C2`: Adjust the azimuth of 3248314_4 by 35 degrees
- `C3`: Adjust the azimuth of 3245454_3 by 48 degrees
- `C4`: Decrease transmission power for 3245454_3
- `C5`: Check test server and transmission issues
- `C6`: Lift the tilt angle  of 3248314_4 by 5 degrees **← 정답**
- `C7`: Add neighbor relationship between 3245454_3 and 3277319_2
- `C8`: Press down the tilt angle  of 3248314_4 by 5 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277319_2
- `C10`: Press down the tilt angle of 3245454_3 by 4 degrees
- `C11`: Lift the tilt angle of 3245454_3 by 4 degrees
- `C12`: Decrease transmission power for 3277319_2
- `C13`: Add neighbor relationship between 3248314_4 and 3277319_2
- `C14`: Increase A3 Offset threshold for 3277319_2
- `C15`: Increase transmission power for 3277319_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245454_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277319_2
- `C18`: Decrease A3 Offset threshold for 3277319_2
- `C19`: Decrease A3 Offset threshold for 3245454_3
- `C20`: Increase A3 Offset threshold for 3245454_3
- `C21`: Increase transmission power for 3245454_3
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.610 | MS1 | 121.4656677032 | 31.1446315635 | 31 | 504990 | -91.21 | 16.65 | 581.66 | 0.14 | 2.22 | 1561 |
| 2024-09-20 22:21:32.669 | MS1 | 121.4656715545 | 31.1446231232 | 31 | 504990 | -91.65 | 12.94 | 512.41 | 0.03 | 2.92 | 1593 |
| 2024-09-20 22:21:33.475 | MS1 | 121.4656611029 | 31.1446287651 | 31 | 504990 | -90.63 | 12.19 | 499.01 | 0.03 | 2.90 | 1587 |
| 2024-09-20 22:21:34.182 | MS1 | 121.4656765390 | 31.1446243989 | 31 | 504990 | -86.41 | 16.04 | 62.41 | 0.07 | 2.02 | 1573 |
| 2024-09-20 22:21:35.916 | MS1 | 121.4656592144 | 31.1446310871 | 31 | 504990 | -87.78 | 12.19 | 82.70 | 0.14 | 2.75 | 1566 |
| 2024-09-20 22:21:36.216 | MS1 | 121.4656589028 | 31.1446222723 | 31 | 504990 | -86.14 | 14.72 | 41.24 | 0.15 | 2.50 | 1582 |
| 2024-09-20 22:21:37.244 | MS1 | 121.4656760158 | 31.1446234500 | 31 | 504990 | -93.97 | 8.99 | 84.53 | 0.09 | 2.98 | 1572 |
| 2024-09-20 22:21:38.405 | MS1 | 121.4656661465 | 31.1446379907 | 31 | 504990 | -89.48 | 7.31 | 71.32 | 0.07 | 2.66 | 1582 |
| 2024-09-20 22:21:39.206 | MS1 | 121.4656656641 | 31.1446290411 | 31 | 504990 | -89.27 | 10.05 | 50.58 | 0.10 | 2.57 | 1592 |
| 2024-09-20 22:21:40.740 | MS1 | 121.4656604824 | 31.1446315745 | 31 | 504990 | -92.84 | 7.77 | 566.83 | 0.10 | 2.35 | 1586 |
| 2024-09-20 22:21:41.422 | MS1 | 121.4656700701 | 31.1446226384 | 31 | 504990 | -92.96 | 11.07 | 576.76 | 0.02 | 2.23 | 1562 |
| 2024-09-20 22:21:42.394 | MS1 | 121.4656680832 | 31.1446215540 | 31 | 504990 | -91.96 | 10.26 | 368.29 | 0.09 | 2.63 | 1600 |

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
| 3242394 | 1 | 121.4719023924 | 31.1520202122 | 174 | 2 | 9 | 41.6 | TDD | 123 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3245454 | 3 | 121.4655457923 | 31.1525766108 | 227 | 3 | 3 | 19.4 | TDD | 31 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3248314 | 4 | 121.4741550396 | 31.1468781535 | 95 | 1 | 12 | 36.4 | TDD | 1007 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3277319 | 2 | 121.4731659401 | 31.1451643613 | 230 | 2 | 7 | 33.8 | TDD | 271 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.456 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.579 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.579 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.285 | NREventA3 | measId:2;ServCellPCI:875;Se... |
| 2024-09-20 22:21:38.525 | NRHandoverAttempt | SourcePCI:875;SourceNR-ARFC... |
| 2024-09-20 22:21:38.566 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.579 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.721 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.721 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242394 | 1 | 14.9205 | 17.7971 | -114.3531 | 6.5274 | 84.8029 | 0.0175 | 0.0145 |
| 2024_09_20 22:00 | 3277319 | 2 | 15.3262 | 13.7178 | -116.6874 | 19.2843 | 108.5830 | 0.0165 | 0.0046 |
| 2024_09_20 22:00 | 3245454 | 3 | 79.7494 | 81.4840 | -116.0040 | 5.8541 | 182.0576 | 0.0198 | 0.0106 |
| 2024_09_20 22:00 | 3248314 | 4 | 12.3040 | 11.0721 | -117.1598 | 7.5076 | 119.1513 | 0.0130 | 0.0187 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413287_C88654AC | 504990 | 31 | -88.4 | 504990 | 271 | -88.5 | 504990 | 1007 | -95.5 | 504990 | 123 |
| MR_1774413287_4533B90D | 504990 | 31 | -88.1 | 504990 | 271 | -90.4 | 504990 | 1007 | -95.6 | 504990 | 123 |
| MR_1774413287_164DE606 | 504990 | 31 | -84.5 | 504990 | 271 | -86.9 | 504990 | 1007 | -95.0 | 504990 | 123 |
| MR_1774413287_43146DBE | 504990 | 31 | -87.3 | 504990 | 271 | -87.0 | 504990 | 1007 | -98.1 | 504990 | 123 |
| MR_1774413287_7DB940C5 | 504990 | 31 | -85.0 | 504990 | 271 | -87.6 | 504990 | 1007 | -94.8 | 504990 | 123 |
| MR_1774413287_FAA988D8 | 504990 | 31 | -85.2 | 504990 | 271 | -86.7 | 504990 | 1007 | -95.9 | 504990 | 123 |
| MR_1774413287_F1C38C3E | 504990 | 31 | -87.6 | 504990 | 271 | -90.5 | 504990 | 1007 | -98.4 | 504990 | 123 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 387: `c69eec7e-5ae...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c69eec7e-5aea-4f34-966b-29ce2fe649c4` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Lift the tilt angle  of 3251860_2 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[387] topology](images/train_0387.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3242981_3
- `C2`: Decrease A3 Offset threshold for 3220381_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220381_1
- `C4`: Check test server and transmission issues
- `C5`: Lift the tilt angle  of 3251860_2 by 7 degrees **← 정답**
- `C6`: Increase transmission power for 3220381_1
- `C7`: Increase transmission power for 3242981_3
- `C8`: Lift the tilt angle of 3220381_1 by 4 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242981_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242981_3
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase A3 Offset threshold for 3220381_1
- `C13`: Adjust the azimuth of 3251860_2 by 50 degrees
- `C14`: Increase A3 Offset threshold for 3242981_3
- `C15`: Press down the tilt angle of 3220381_1 by 4 degrees
- `C16`: Decrease A3 Offset threshold for 3242981_3
- `C17`: Press down the tilt angle  of 3251860_2 by 7 degrees
- `C18`: Adjust the azimuth of 3220381_1 by 19 degrees
- `C19`: Add neighbor relationship between 3220381_1 and 3242981_3
- `C20`: Decrease transmission power for 3220381_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220381_1
- `C22`: Add neighbor relationship between 3251860_2 and 3242981_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.372 | MS1 | 121.4656725983 | 31.1446372408 | 466 | 504990 | -89.70 | 13.11 | 547.97 | 0.07 | 2.87 | 1570 |
| 2024-09-20 22:21:32.966 | MS1 | 121.4656630282 | 31.1446293867 | 466 | 504990 | -90.95 | 15.62 | 561.64 | 0.06 | 2.79 | 1590 |
| 2024-09-20 22:21:33.929 | MS1 | 121.4656730393 | 31.1446276162 | 466 | 504990 | -87.82 | 14.23 | 558.93 | 0.05 | 2.85 | 1569 |
| 2024-09-20 22:21:34.920 | MS1 | 121.4656651002 | 31.1446254780 | 466 | 504990 | -87.70 | 12.79 | 63.94 | 0.15 | 2.19 | 1563 |
| 2024-09-20 22:21:35.359 | MS1 | 121.4656682411 | 31.1446216324 | 466 | 504990 | -92.00 | 17.62 | 88.75 | 0.06 | 2.43 | 1594 |
| 2024-09-20 22:21:36.426 | MS1 | 121.4656752396 | 31.1446279606 | 466 | 504990 | -86.25 | 15.66 | 89.01 | 0.10 | 2.49 | 1561 |
| 2024-09-20 22:21:37.542 | MS1 | 121.4656709010 | 31.1446344284 | 466 | 504990 | -93.73 | 9.90 | 60.70 | 0.03 | 2.68 | 1561 |
| 2024-09-20 22:21:38.140 | MS1 | 121.4656723795 | 31.1446276968 | 466 | 504990 | -92.71 | 10.07 | 81.80 | 0.12 | 2.24 | 1582 |
| 2024-09-20 22:21:39.809 | MS1 | 121.4656662909 | 31.1446238958 | 466 | 504990 | -93.79 | 8.79 | 64.21 | 0.17 | 2.89 | 1590 |
| 2024-09-20 22:21:40.728 | MS1 | 121.4656755685 | 31.1446245342 | 466 | 504990 | -91.03 | 7.15 | 494.99 | 0.19 | 2.35 | 1560 |
| 2024-09-20 22:21:41.380 | MS1 | 121.4656753306 | 31.1446255753 | 466 | 504990 | -93.64 | 12.82 | 553.29 | 0.18 | 2.40 | 1576 |
| 2024-09-20 22:21:42.842 | MS1 | 121.4656765597 | 31.1446325965 | 466 | 504990 | -90.77 | 10.51 | 418.72 | 0.04 | 2.49 | 1571 |

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
| 3220381 | 1 | 121.4706138286 | 31.1503948583 | 235 | 2 | 0 | 25.3 | TDD | 466 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3242981 | 3 | 121.4665442121 | 31.1500665900 | 64 | 3 | 1 | 40.3 | TDD | 654 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3251860 | 2 | 121.4675984311 | 31.1448157311 | 48 | 13 | 9 | 25.6 | TDD | 67 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3254476 | 4 | 121.4736494029 | 31.1520067691 | 101 | 15 | 10 | 36.7 | TDD | 919 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.068 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.088 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.192 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.192 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.926 | NREventA3 | measId:2;ServCellPCI:525;Se... |
| 2024-09-20 22:21:38.166 | NRHandoverAttempt | SourcePCI:525;SourceNR-ARFC... |
| 2024-09-20 22:21:38.200 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.214 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.320 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.320 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220381 | 1 | 77.4733 | 79.9624 | -114.6108 | 7.7337 | 164.6487 | 0.0045 | 0.0138 |
| 2024_09_20 22:00 | 3251860 | 2 | 15.6270 | 16.5468 | -117.6808 | 17.5192 | 162.7887 | 0.0081 | 0.0101 |
| 2024_09_20 22:00 | 3242981 | 3 | 8.7228 | 6.6864 | -117.2893 | 17.6291 | 162.5278 | 0.0193 | 0.0085 |
| 2024_09_20 22:00 | 3254476 | 4 | 10.1025 | 19.9283 | -116.2501 | 16.3694 | 110.4694 | 0.0046 | 0.0164 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416213_1C9E56CD | 504990 | 466 | -87.7 | 504990 | 654 | -92.2 | 504990 | 67 | -96.5 | 504990 | 919 |
| MR_1774416213_13CB7E53 | 504990 | 466 | -89.7 | 504990 | 654 | -92.3 | 504990 | 67 | -97.2 | 504990 | 919 |
| MR_1774416213_96B2189A | 504990 | 466 | -87.5 | 504990 | 654 | -92.1 | 504990 | 67 | -95.1 | 504990 | 919 |
| MR_1774416213_E0DF5FD9 | 504990 | 466 | -86.3 | 504990 | 654 | -93.1 | 504990 | 67 | -97.1 | 504990 | 919 |
| MR_1774416213_38A39F0E | 504990 | 466 | -89.6 | 504990 | 654 | -93.1 | 504990 | 67 | -95.1 | 504990 | 919 |
| MR_1774416213_78E27902 | 504990 | 466 | -86.5 | 504990 | 654 | -95.1 | 504990 | 67 | -97.1 | 504990 | 919 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 388: `32e23862-229...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `32e23862-2293-4c76-8796-04ae4a74ee41` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease A3 Offset threshold for 3215866_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[388] topology](images/train_0388.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3210527_3 by 10 degrees
- `C2`: Adjust the azimuth of 3210527_3 by 45 degrees
- `C3`: Increase transmission power for 3210527_3
- `C4`: Add neighbor relationship between 3215866_1 and 3210527_3
- `C5`: Increase A3 Offset threshold for 3210527_3
- `C6`: Check test server and transmission issues
- `C7`: Add neighbor relationship between 3231608_4 and 3210527_3
- `C8`: Decrease A3 Offset threshold for 3210527_3
- `C9`: Adjust the azimuth of 3215866_1 by 50 degrees
- `C10`: Increase A3 Offset threshold for 3215866_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210527_3
- `C12`: Decrease transmission power for 3210527_3
- `C13`: Press down the tilt angle of 3215866_1 by 10 degrees
- `C14`: Decrease transmission power for 3215866_1
- `C15`: Decrease A3 Offset threshold for 3215866_1 **← 정답**
- `C16`: Lift the tilt angle of 3215866_1 by 10 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215866_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215866_1
- `C19`: Increase transmission power for 3215866_1
- `C20`: Press down the tilt angle  of 3210527_3 by 10 degrees
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210527_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.958 | MS1 | 121.4656670926 | 31.1446212320 | 890 | 504990 | -79.37 | 16.01 | 419.81 | 0.14 | 2.15 | 1586 |
| 2024-09-20 22:21:32.778 | MS1 | 121.4656724575 | 31.1446304313 | 890 | 504990 | -82.93 | 16.66 | 320.94 | 0.12 | 2.17 | 1562 |
| 2024-09-20 22:21:33.129 | MS1 | 121.4656704243 | 31.1446222974 | 890 | 504990 | -77.28 | 17.27 | 454.37 | 0.14 | 2.53 | 1560 |
| 2024-09-20 22:21:34.614 | MS1 | 121.4656739993 | 31.1446364419 | 890 | 504990 | -85.60 | -2.68 | 71.99 | 0.13 | 1.01 | 1581 |
| 2024-09-20 22:21:35.934 | MS1 | 121.4656610250 | 31.1446190167 | 890 | 504990 | -89.30 | -0.74 | 67.38 | 0.15 | 1.28 | 1563 |
| 2024-09-20 22:21:36.832 | MS1 | 121.4656755421 | 31.1446189095 | 890 | 504990 | -87.50 | -2.72 | 67.38 | 0.14 | 1.10 | 1580 |
| 2024-09-20 22:21:37.112 | MS1 | 121.4656777461 | 31.1446356139 | 890 | 504990 | -84.99 | -0.60 | 41.56 | 0.11 | 1.04 | 1595 |
| 2024-09-20 22:21:38.640 | MS1 | 121.4656588718 | 31.1446269518 | 890 | 504990 | -85.15 | -2.12 | 43.65 | 0.06 | 1.04 | 1565 |
| 2024-09-20 22:21:39.402 | MS1 | 121.4656715615 | 31.1446345901 | 76 | 504990 | -76.40 | 17.23 | 254.29 | 0.11 | 1.34 | 1594 |
| 2024-09-20 22:21:40.546 | MS1 | 121.4656665247 | 31.1446250955 | 76 | 504990 | -77.69 | 12.03 | 476.25 | 0.12 | 2.62 | 1586 |
| 2024-09-20 22:21:41.183 | MS1 | 121.4656766360 | 31.1446247915 | 76 | 504990 | -75.54 | 15.57 | 495.19 | 0.02 | 2.58 | 1593 |
| 2024-09-20 22:21:42.228 | MS1 | 121.4656726586 | 31.1446299343 | 76 | 504990 | -79.09 | 14.52 | 374.79 | 0.04 | 2.45 | 1574 |

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
| 3210527 | 3 | 121.4655822739 | 31.1478686976 | 224 | 14 | 3 | 45.9 | TDD | 76 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3215866 | 1 | 121.4694601460 | 31.1511307519 | 278 | 8 | 9 | 49.2 | TDD | 890 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3231608 | 4 | 121.4664361675 | 31.1478833939 | 25 | 4 | 2 | 37.1 | TDD | 511 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3236901 | 2 | 121.4652741986 | 31.1550629141 | 150 | 8 | 9 | 24.6 | TDD | 282 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.492 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.626 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.626 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.304 | NREventA3 | measId:2;ServCellPCI:464;Se... |
| 2024-09-20 22:21:38.544 | NRHandoverAttempt | SourcePCI:464;SourceNR-ARFC... |
| 2024-09-20 22:21:38.580 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.593 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.743 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.743 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215866 | 1 | 13.8828 | 8.0357 | -116.7018 | 7.1721 | 170.4162 | 0.0143 | 0.1129 |
| 2024_09_20 22:00 | 3236901 | 2 | 19.7064 | 17.5587 | -115.9932 | 16.6945 | 112.9690 | 0.0058 | 0.0024 |
| 2024_09_20 22:00 | 3210527 | 3 | 5.5143 | 10.0115 | -114.1576 | 10.4387 | 150.0397 | 0.0013 | 0.0076 |
| 2024_09_20 22:00 | 3231608 | 4 | 14.3527 | 13.8126 | -117.7758 | 12.1517 | 97.1651 | 0.0109 | 0.0181 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415561_768984DB | 504990 | 890 | -85.0 | 504990 | 76 | -79.7 | 504990 | 511 | -84.3 | 504990 | 282 |
| MR_1774415561_747DB93E | 504990 | 890 | -87.1 | 504990 | 76 | -81.3 | 504990 | 511 | -88.0 | 504990 | 282 |
| MR_1774415561_934D5437 | 504990 | 76 | -82.1 | 504990 | 890 | -84.0 | 504990 | 511 | -84.5 | 504990 | 282 |
| MR_1774415561_DCD63563 | 504990 | 890 | -86.9 | 504990 | 76 | -82.2 | 504990 | 511 | -88.3 | 504990 | 282 |
| MR_1774415561_2CE88E40 | 504990 | 890 | -87.3 | 504990 | 76 | -83.0 | 504990 | 511 | -87.9 | 504990 | 282 |
| MR_1774415561_53CE1718 | 504990 | 76 | -83.2 | 504990 | 890 | -87.5 | 504990 | 511 | -86.0 | 504990 | 282 |
| MR_1774415561_6E195B72 | 504990 | 76 | -82.9 | 504990 | 890 | -84.7 | 504990 | 511 | -85.9 | 504990 | 282 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 389: `866091f6-49d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `866091f6-49d9-4f55-9a19-dad3a79fbbfb` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3233545_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[389] topology](images/train_0389.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3233545_3
- `C2`: Decrease transmission power for 3233545_3
- `C3`: Press down the tilt angle of 3233545_3 by 1 degrees
- `C4`: Add neighbor relationship between 3233545_3 and 3278282_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278282_4
- `C6`: Press down the tilt angle  of 3278282_4 by 10 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278282_4
- `C8`: Decrease transmission power for 3278282_4
- `C9`: Increase A3 Offset threshold for 3233545_3
- `C10`: Increase transmission power for 3233545_3
- `C11`: Increase transmission power for 3278282_4
- `C12`: Check test server and transmission issues
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Lift the tilt angle  of 3278282_4 by 10 degrees
- `C15`: Lift the tilt angle of 3233545_3 by 1 degrees
- `C16`: Adjust the azimuth of 3278282_4 by 50 degrees
- `C17`: Adjust the azimuth of 3233545_3 by 7 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233545_3 **← 정답**
- `C19`: Decrease A3 Offset threshold for 3278282_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233545_3
- `C21`: Add neighbor relationship between 3213689_2 and 3278282_4
- `C22`: Increase A3 Offset threshold for 3278282_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.620 | MS1 | 121.4656681018 | 31.1446373743 | 493 | 504990 | -91.45 | 14.03 | 353.24 | 0.00 | 2.20 | 1560 |
| 2024-09-20 22:21:32.153 | MS1 | 121.4656654402 | 31.1446310332 | 493 | 504990 | -87.75 | 13.66 | 536.72 | 0.07 | 2.77 | 1573 |
| 2024-09-20 22:21:33.245 | MS1 | 121.4656754433 | 31.1446210009 | 493 | 504990 | -88.63 | 13.71 | 573.99 | 0.19 | 2.16 | 1573 |
| 2024-09-20 22:21:34.313 | MS1 | 121.4656623238 | 31.1446352396 | 493 | 504990 | -87.96 | 17.97 | 99.24 | 0.64 | 2.45 | 519 |
| 2024-09-20 22:21:35.793 | MS1 | 121.4656679239 | 31.1446247926 | 493 | 504990 | -89.68 | 13.82 | 53.36 | 0.61 | 2.59 | 693 |
| 2024-09-20 22:21:36.239 | MS1 | 121.4656592929 | 31.1446376363 | 493 | 504990 | -86.50 | 14.03 | 81.63 | 0.54 | 2.43 | 548 |
| 2024-09-20 22:21:37.164 | MS1 | 121.4656737885 | 31.1446197808 | 493 | 504990 | -90.46 | 10.55 | 77.42 | 0.58 | 2.55 | 684 |
| 2024-09-20 22:21:38.929 | MS1 | 121.4656650443 | 31.1446283425 | 493 | 504990 | -93.14 | 12.02 | 82.49 | 0.52 | 2.39 | 561 |
| 2024-09-20 22:21:39.892 | MS1 | 121.4656778177 | 31.1446263777 | 493 | 504990 | -92.49 | 11.15 | 87.59 | 0.56 | 2.07 | 578 |
| 2024-09-20 22:21:40.745 | MS1 | 121.4656716113 | 31.1446260482 | 493 | 504990 | -93.63 | 8.37 | 408.67 | 0.04 | 2.33 | 1571 |
| 2024-09-20 22:21:41.415 | MS1 | 121.4656588444 | 31.1446204103 | 493 | 504990 | -89.22 | 10.20 | 579.78 | 0.08 | 2.74 | 1586 |
| 2024-09-20 22:21:42.113 | MS1 | 121.4656676847 | 31.1446238691 | 493 | 504990 | -91.95 | 9.45 | 488.89 | 0.06 | 2.00 | 1593 |

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
| 3213689 | 2 | 121.4643836238 | 31.1550229860 | 245 | 0 | 9 | 46.5 | TDD | 36 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3233545 | 3 | 121.4737687755 | 31.1551665994 | 220 | 0 | 3 | 23.2 | TDD | 493 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3260889 | 1 | 121.4711767689 | 31.1545487542 | 304 | 12 | 2 | 46.1 | TDD | 217 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3278282 | 4 | 121.4746762585 | 31.1441236676 | 217 | 10 | 5 | 20.6 | TDD | 759 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.031 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.054 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.181 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.181 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.843 | NREventA3 | measId:2;ServCellPCI:617;Se... |
| 2024-09-20 22:21:38.083 | NRHandoverAttempt | SourcePCI:617;SourceNR-ARFC... |
| 2024-09-20 22:21:38.128 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.139 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.280 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.280 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260889 | 1 | 8.5299 | 19.0799 | -116.7831 | 17.3548 | 177.1360 | 0.0016 | 0.0103 |
| 2024_09_20 22:00 | 3213689 | 2 | 9.3823 | 19.9754 | -114.8633 | 13.9053 | 114.4185 | 0.0180 | 0.0076 |
| 2024_09_20 22:00 | 3233545 | 3 | 13.7584 | 14.8775 | -115.3670 | 12.6699 | 154.1909 | 0.0035 | 0.0153 |
| 2024_09_20 22:00 | 3278282 | 4 | 15.1766 | 8.9878 | -114.1738 | 5.5975 | 94.7024 | 0.0131 | 0.0065 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414254_D781FEC7 | 504990 | 493 | -87.7 | 504990 | 759 | -91.4 | 504990 | 36 | -98.2 | 504990 | 217 |
| MR_1774414254_C3D1CC8F | 504990 | 493 | -89.4 | 504990 | 759 | -91.5 | 504990 | 36 | -98.0 | 504990 | 217 |
| MR_1774414254_37C1EFC1 | 504990 | 493 | -86.5 | 504990 | 759 | -90.6 | 504990 | 36 | -98.1 | 504990 | 217 |
| MR_1774414254_2626332B | 504990 | 493 | -89.1 | 504990 | 759 | -90.5 | 504990 | 36 | -99.8 | 504990 | 217 |
| MR_1774414254_1AF144B2 | 504990 | 493 | -88.0 | 504990 | 759 | -91.9 | 504990 | 36 | -100.0 | 504990 | 217 |

> *... 2개 열 생략 (전체 14열)*

---
