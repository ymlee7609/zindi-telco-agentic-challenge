# Track A 문제 분석 — train[1380]~train[1389]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1380] ~ train[1389] (10개)

## 목차

1. [문제 1380: `64943b85-8b5...`](#1380) — multiple-answer, 정답: C14|C19
2. [문제 1381: `4a4f4536-eb3...`](#1381) — single-answer, 정답: C14
3. [문제 1382: `bc2a6c0f-3ff...`](#1382) — single-answer, 정답: C8
4. [문제 1383: `f3ea1a1f-531...`](#1383) — single-answer, 정답: C17
5. [문제 1384: `0576283e-ad0...`](#1384) — single-answer, 정답: C22
6. [문제 1385: `fa53a29e-1ab...`](#1385) — multiple-answer, 정답: C3|C18
7. [문제 1386: `43ade285-aa8...`](#1386) — single-answer, 정답: C6
8. [문제 1387: `527e5d4b-abc...`](#1387) — single-answer, 정답: C22
9. [문제 1388: `422078e9-386...`](#1388) — single-answer, 정답: C22
10. [문제 1389: `1b77d60a-60c...`](#1389) — multiple-answer, 정답: C2|C10|C17|C18

---

### 문제 1380: `64943b85-8b5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `64943b85-8b54-482b-8b64-9a00f4588898` |
| Tag | **multiple-answer** |
| 정답 | **C14|C19** |
| C14 의미 | Increase transmission power for 3266056_4 |
| C19 의미 | Adjust the azimuth of 3266056_4 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1380] topology](images/train_1380.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3266056_4 by 3 degrees
- `C2`: Increase A3 Offset threshold for 3272591_3
- `C3`: Increase A3 Offset threshold for 3266056_4
- `C4`: Adjust the azimuth of 3272591_3 by 19 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266056_4
- `C6`: Decrease transmission power for 3266056_4
- `C7`: Add neighbor relationship between 3266056_4 and 3272591_3
- `C8`: Decrease transmission power for 3272591_3
- `C9`: Press down the tilt angle  of 3272591_3 by 5 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266056_4
- `C11`: Check test server and transmission issues
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Lift the tilt angle  of 3272591_3 by 5 degrees
- `C14`: Increase transmission power for 3266056_4 **← 정답**
- `C15`: Add neighbor relationship between 3212324_2 and 3272591_3
- `C16`: Decrease A3 Offset threshold for 3272591_3
- `C17`: Increase transmission power for 3272591_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272591_3
- `C19`: Adjust the azimuth of 3266056_4 by 50 degrees **← 정답**
- `C20`: Decrease A3 Offset threshold for 3266056_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272591_3
- `C22`: Press down the tilt angle of 3266056_4 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.303 | MS1 | 121.4656727337 | 31.1446230647 | 774 | 504990 | -89.63 | 12.47 | 454.65 | 0.01 | 2.68 | 1593 |
| 2024-09-20 22:21:32.282 | MS1 | 121.4656652944 | 31.1446259173 | 774 | 504990 | -89.86 | 14.75 | 359.79 | 0.05 | 2.18 | 1585 |
| 2024-09-20 22:21:33.190 | MS1 | 121.4656722849 | 31.1446194495 | 774 | 504990 | -86.99 | 12.76 | 400.41 | 0.18 | 2.25 | 1568 |
| 2024-09-20 22:21:34.120 | MS1 | 121.4656710997 | 31.1446295023 | 774 | 504990 | -101.94 | -1.14 | 72.54 | 0.02 | 1.19 | 1591 |
| 2024-09-20 22:21:35.323 | MS1 | 121.4656675900 | 31.1446219589 | 774 | 504990 | -107.25 | 1.53 | 75.85 | 0.16 | 1.18 | 1560 |
| 2024-09-20 22:21:36.524 | MS1 | 121.4656661174 | 31.1446344693 | 774 | 504990 | -109.62 | -1.23 | 30.95 | 0.04 | 1.40 | 1566 |
| 2024-09-20 22:21:37.279 | MS1 | 121.4656726369 | 31.1446260362 | 774 | 504990 | -102.71 | 0.69 | 65.36 | 0.05 | 1.42 | 1573 |
| 2024-09-20 22:21:38.947 | MS1 | 121.4656764074 | 31.1446192575 | 774 | 504990 | -103.49 | -0.25 | 67.98 | 0.16 | 1.42 | 1586 |
| 2024-09-20 22:21:39.220 | MS1 | 121.4656684329 | 31.1446212239 | 774 | 504990 | -105.26 | 0.35 | 23.19 | 0.06 | 1.27 | 1581 |
| 2024-09-20 22:21:40.295 | MS1 | 121.4656645642 | 31.1446191281 | 774 | 504990 | -92.28 | 16.98 | 391.13 | 0.11 | 2.25 | 1590 |
| 2024-09-20 22:21:41.398 | MS1 | 121.4656623956 | 31.1446335571 | 774 | 504990 | -93.00 | 14.18 | 363.53 | 0.18 | 2.90 | 1581 |
| 2024-09-20 22:21:42.482 | MS1 | 121.4656639802 | 31.1446202765 | 774 | 504990 | -90.33 | 14.70 | 309.86 | 0.17 | 2.13 | 1578 |

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
| 3212324 | 2 | 121.4741275634 | 31.1454715534 | 293 | 7 | 4 | 41.7 | TDD | 337 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3234577 | 1 | 121.4647063503 | 31.1471913216 | 62 | 7 | 11 | 24.6 | TDD | 62 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3266056 | 4 | 121.4759702922 | 31.1521339164 | 307 | 1 | 0 | 41.1 | TDD | 774 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3272591 | 3 | 121.4664610277 | 31.1526017389 | 166 | 4 | 12 | 15.9 | TDD | 846 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.220 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.238 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.360 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.360 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.539 | NREventA2 | measId:1;ServCellPCI:579;Se... |
| 2024-09-20 22:21:34.670 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234577 | 1 | 5.1521 | 9.1309 | -114.6531 | 9.0189 | 161.0581 | 0.0076 | 0.0053 |
| 2024_09_20 22:00 | 3212324 | 2 | 7.3463 | 17.9917 | -114.3778 | 9.4072 | 164.8359 | 0.0023 | 0.0013 |
| 2024_09_20 22:00 | 3272591 | 3 | 13.6105 | 13.8272 | -116.2473 | 8.6985 | 168.3006 | 0.0167 | 0.0072 |
| 2024_09_20 22:00 | 3266056 | 4 | 13.1025 | 10.4846 | -114.3236 | 9.5816 | 84.2869 | 0.1926 | 0.0190 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413110_730DAEA7 | 504990 | 774 | -102.7 | 504990 | 846 | -108.1 | 504990 | 337 | -112.9 | 504990 | 62 |
| MR_1774413110_DE57F661 | 504990 | 774 | -103.3 | 504990 | 846 | -108.3 | 504990 | 337 | -111.1 | 504990 | 62 |
| MR_1774413110_EAA714BB | 504990 | 774 | -103.6 | 504990 | 846 | -110.2 | 504990 | 337 | -110.6 | 504990 | 62 |
| MR_1774413110_6472E375 | 504990 | 774 | -102.6 | 504990 | 846 | -110.0 | 504990 | 337 | -112.1 | 504990 | 62 |
| MR_1774413110_5BEAEF5B | 504990 | 774 | -103.6 | 504990 | 846 | -109.6 | 504990 | 337 | -109.8 | 504990 | 62 |
| MR_1774413110_C53DBF42 | 504990 | 774 | -101.1 | 504990 | 846 | -109.4 | 504990 | 337 | -112.3 | 504990 | 62 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1381: `4a4f4536-eb3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4a4f4536-eb36-45ab-b948-08fff6b2ad0b` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Lift the tilt angle  of 3241930_2 by 5 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1381] topology](images/train_1381.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3275368_4
- `C2`: Add neighbor relationship between 3252157_1 and 3275368_4
- `C3`: Lift the tilt angle of 3252157_1 by 6 degrees
- `C4`: Check test server and transmission issues
- `C5`: Decrease transmission power for 3275368_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase transmission power for 3275368_4
- `C8`: Add neighbor relationship between 3241930_2 and 3275368_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275368_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252157_1
- `C11`: Press down the tilt angle of 3252157_1 by 6 degrees
- `C12`: Decrease transmission power for 3252157_1
- `C13`: Adjust the azimuth of 3241930_2 by 25 degrees
- `C14`: Lift the tilt angle  of 3241930_2 by 5 degrees **← 정답**
- `C15`: Adjust the azimuth of 3252157_1 by 20 degrees
- `C16`: Increase A3 Offset threshold for 3252157_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275368_4
- `C18`: Increase A3 Offset threshold for 3275368_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252157_1
- `C20`: Increase transmission power for 3252157_1
- `C21`: Decrease A3 Offset threshold for 3252157_1
- `C22`: Press down the tilt angle  of 3241930_2 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.769 | MS1 | 121.4656671559 | 31.1446244019 | 514 | 504990 | -90.42 | 14.81 | 551.14 | 0.08 | 2.08 | 1595 |
| 2024-09-20 22:21:32.519 | MS1 | 121.4656612792 | 31.1446249627 | 514 | 504990 | -90.47 | 16.06 | 584.45 | 0.05 | 2.65 | 1569 |
| 2024-09-20 22:21:33.987 | MS1 | 121.4656603720 | 31.1446268172 | 514 | 504990 | -88.56 | 13.45 | 358.25 | 0.09 | 2.23 | 1576 |
| 2024-09-20 22:21:34.420 | MS1 | 121.4656773621 | 31.1446256825 | 514 | 504990 | -90.90 | 17.49 | 77.38 | 0.06 | 2.39 | 1587 |
| 2024-09-20 22:21:35.336 | MS1 | 121.4656636666 | 31.1446206108 | 514 | 504990 | -89.66 | 16.02 | 54.43 | 0.09 | 2.13 | 1564 |
| 2024-09-20 22:21:36.873 | MS1 | 121.4656667025 | 31.1446322114 | 514 | 504990 | -89.61 | 16.64 | 69.67 | 0.02 | 2.05 | 1571 |
| 2024-09-20 22:21:37.979 | MS1 | 121.4656595742 | 31.1446366980 | 514 | 504990 | -93.72 | 9.75 | 98.30 | 0.11 | 2.89 | 1568 |
| 2024-09-20 22:21:38.514 | MS1 | 121.4656620136 | 31.1446260908 | 514 | 504990 | -91.59 | 12.06 | 100.98 | 0.14 | 2.12 | 1587 |
| 2024-09-20 22:21:39.548 | MS1 | 121.4656690011 | 31.1446360794 | 514 | 504990 | -92.13 | 9.28 | 61.75 | 0.16 | 2.97 | 1572 |
| 2024-09-20 22:21:40.308 | MS1 | 121.4656718061 | 31.1446214416 | 514 | 504990 | -91.19 | 9.50 | 327.82 | 0.03 | 2.42 | 1591 |
| 2024-09-20 22:21:41.481 | MS1 | 121.4656603198 | 31.1446346273 | 514 | 504990 | -93.93 | 10.74 | 435.48 | 0.19 | 2.36 | 1577 |
| 2024-09-20 22:21:42.226 | MS1 | 121.4656698091 | 31.1446244649 | 514 | 504990 | -90.92 | 7.05 | 578.82 | 0.17 | 2.60 | 1560 |

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
| 3241930 | 2 | 121.4742486347 | 31.1458558350 | 21 | 5 | 8 | 19.2 | TDD | 26 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3243113 | 3 | 121.4737095559 | 31.1475168506 | 125 | 13 | 8 | 40.3 | TDD | 387 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3252157 | 1 | 121.4670179305 | 31.1519648722 | 209 | 3 | 5 | 42.0 | TDD | 514 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3275368 | 4 | 121.4645664714 | 31.1527969279 | 148 | 3 | 8 | 32.1 | TDD | 410 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.907 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.926 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.050 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.050 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.798 | NREventA3 | measId:2;ServCellPCI:157;Se... |
| 2024-09-20 22:21:38.038 | NRHandoverAttempt | SourcePCI:157;SourceNR-ARFC... |
| 2024-09-20 22:21:38.077 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.089 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.189 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.189 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252157 | 1 | 86.2581 | 87.1431 | -117.0151 | 18.5558 | 178.3735 | 0.0006 | 0.0045 |
| 2024_09_20 22:00 | 3241930 | 2 | 9.9491 | 11.0985 | -117.7410 | 10.8580 | 112.5742 | 0.0052 | 0.0029 |
| 2024_09_20 22:00 | 3243113 | 3 | 10.4201 | 5.6290 | -116.7552 | 15.7334 | 138.5179 | 0.0035 | 0.0180 |
| 2024_09_20 22:00 | 3275368 | 4 | 7.6667 | 10.8765 | -115.8489 | 8.5018 | 192.1039 | 0.0109 | 0.0017 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412431_E5693FE0 | 504990 | 514 | -89.0 | 504990 | 410 | -97.1 | 504990 | 26 | -99.5 | 504990 | 387 |
| MR_1774412431_ABC61349 | 504990 | 514 | -89.7 | 504990 | 410 | -97.2 | 504990 | 26 | -102.2 | 504990 | 387 |
| MR_1774412431_8691AB0E | 504990 | 514 | -91.2 | 504990 | 410 | -98.6 | 504990 | 26 | -102.1 | 504990 | 387 |
| MR_1774412431_CF32083B | 504990 | 514 | -89.7 | 504990 | 410 | -96.9 | 504990 | 26 | -98.9 | 504990 | 387 |
| MR_1774412431_17D3DFE7 | 504990 | 514 | -90.0 | 504990 | 410 | -98.3 | 504990 | 26 | -101.2 | 504990 | 387 |
| MR_1774412431_724F0234 | 504990 | 514 | -92.8 | 504990 | 410 | -96.0 | 504990 | 26 | -101.8 | 504990 | 387 |
| MR_1774412431_751D15C1 | 504990 | 514 | -91.7 | 504990 | 410 | -99.2 | 504990 | 26 | -102.1 | 504990 | 387 |
| MR_1774412431_484D3852 | 504990 | 514 | -92.4 | 504990 | 410 | -95.8 | 504990 | 26 | -101.3 | 504990 | 387 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1382: `bc2a6c0f-3ff...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bc2a6c0f-3ff4-464f-82e1-50f38a718437` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1382] topology](images/train_1382.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3276255_1 by 10 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231772_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276255_1
- `C4`: Lift the tilt angle of 3231772_4 by 10 degrees
- `C5`: Decrease A3 Offset threshold for 3231772_4
- `C6`: Increase transmission power for 3231772_4
- `C7`: Check test server and transmission issues
- `C8`: Insufficient data; more data is needed for judgment. **← 정답**
- `C9`: Decrease transmission power for 3231772_4
- `C10`: Add neighbor relationship between 3231772_4 and 3276255_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276255_1
- `C12`: Add neighbor relationship between 3235998_3 and 3276255_1
- `C13`: Increase A3 Offset threshold for 3276255_1
- `C14`: Increase transmission power for 3276255_1
- `C15`: Adjust the azimuth of 3276255_1 by 27 degrees
- `C16`: Adjust the azimuth of 3231772_4 by 50 degrees
- `C17`: Press down the tilt angle of 3231772_4 by 10 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231772_4
- `C19`: Increase A3 Offset threshold for 3231772_4
- `C20`: Press down the tilt angle  of 3276255_1 by 10 degrees
- `C21`: Decrease A3 Offset threshold for 3276255_1
- `C22`: Decrease transmission power for 3276255_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.285 | MS1 | 121.4656684404 | 31.1446379547 | 957 | 504990 | -89.49 | 14.80 | 581.02 | 0.15 | 2.46 | 1588 |
| 2024-09-20 22:21:32.451 | MS1 | 121.4656646850 | 31.1446199196 | 957 | 504990 | -91.38 | 15.52 | 479.61 | 0.19 | 2.36 | 1597 |
| 2024-09-20 22:21:33.711 | MS1 | 121.4656732140 | 31.1446238331 | 957 | 504990 | -87.92 | 16.45 | 527.29 | 0.15 | 2.43 | 1568 |
| 2024-09-20 22:21:34.644 | MS1 | 121.4656773010 | 31.1446325581 | 957 | 504990 | -85.33 | 15.12 | 77.67 | 0.19 | 2.99 | 1565 |
| 2024-09-20 22:21:35.783 | MS1 | 121.4656691441 | 31.1446301458 | 957 | 504990 | -91.97 | 16.76 | 55.52 | 0.12 | 2.92 | 1565 |
| 2024-09-20 22:21:36.908 | MS1 | 121.4656752886 | 31.1446208685 | 957 | 504990 | -87.83 | 13.99 | 95.40 | 0.07 | 2.47 | 1565 |
| 2024-09-20 22:21:37.173 | MS1 | 121.4656582370 | 31.1446243914 | 957 | 504990 | -92.86 | 12.96 | 52.61 | 0.16 | 2.56 | 1569 |
| 2024-09-20 22:21:38.444 | MS1 | 121.4656651948 | 31.1446368897 | 957 | 504990 | -91.85 | 7.32 | 75.27 | 0.18 | 2.42 | 1574 |
| 2024-09-20 22:21:39.675 | MS1 | 121.4656713907 | 31.1446339694 | 957 | 504990 | -90.18 | 10.96 | 70.09 | 0.02 | 2.67 | 1587 |
| 2024-09-20 22:21:40.925 | MS1 | 121.4656613021 | 31.1446316513 | 957 | 504990 | -89.37 | 9.40 | 521.14 | 0.07 | 2.48 | 1582 |
| 2024-09-20 22:21:41.928 | MS1 | 121.4656668481 | 31.1446221091 | 957 | 504990 | -89.54 | 11.86 | 426.59 | 0.19 | 2.36 | 1592 |
| 2024-09-20 22:21:42.457 | MS1 | 121.4656679841 | 31.1446264267 | 957 | 504990 | -92.05 | 9.47 | 478.00 | 0.01 | 2.15 | 1599 |

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
| 3231772 | 4 | 121.4656691854 | 31.1442898058 | 257 | 14 | 12 | 20.8 | TDD | 957 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3235998 | 3 | 121.4679160495 | 31.1440752982 | 210 | 6 | 0 | 23.0 | TDD | 629 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3267292 | 2 | 121.4735957961 | 31.1499087630 | 311 | 14 | 6 | 36.8 | TDD | 724 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3276255 | 1 | 121.4658338299 | 31.1449039212 | 181 | 6 | 1 | 47.6 | TDD | 775 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.160 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.181 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.287 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.287 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.040 | NREventA3 | measId:2;ServCellPCI:446;Se... |
| 2024-09-20 22:21:38.280 | NRHandoverAttempt | SourcePCI:446;SourceNR-ARFC... |
| 2024-09-20 22:21:38.314 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.327 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.467 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.467 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3276255 | 1 | 82.1317 | 81.9134 | -117.0992 | 18.0468 | 104.3775 | 0.0083 | 0.0166 |
| 2024_09_19 22:00 | 3267292 | 2 | 80.1017 | 84.5058 | -117.5465 | 18.5976 | 103.1489 | 0.0170 | 0.0062 |
| 2024_09_19 22:00 | 3235998 | 3 | 76.3064 | 90.0155 | -116.0444 | 16.4294 | 162.0253 | 0.0056 | 0.0135 |
| 2024_09_19 22:00 | 3231772 | 4 | 89.9684 | 77.5361 | -117.0388 | 8.4537 | 148.5541 | 0.0112 | 0.0149 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415729_79BE5087 | 504990 | 957 | -84.5 | 504990 | 775 | -84.2 | 504990 | 629 | -95.0 | 504990 | 724 |
| MR_1774415729_9B627CA9 | 504990 | 957 | -84.5 | 504990 | 775 | -86.6 | 504990 | 629 | -98.1 | 504990 | 724 |
| MR_1774415729_B1397C9F | 504990 | 957 | -85.9 | 504990 | 775 | -86.2 | 504990 | 629 | -94.5 | 504990 | 724 |
| MR_1774415729_FDD24B0B | 504990 | 957 | -85.6 | 504990 | 775 | -83.7 | 504990 | 629 | -95.3 | 504990 | 724 |
| MR_1774415729_6F42C9AA | 504990 | 957 | -84.0 | 504990 | 775 | -87.4 | 504990 | 629 | -96.5 | 504990 | 724 |
| MR_1774415729_F4AAA35F | 504990 | 957 | -83.9 | 504990 | 775 | -87.4 | 504990 | 629 | -96.3 | 504990 | 724 |
| MR_1774415729_62282C04 | 504990 | 957 | -86.0 | 504990 | 775 | -85.1 | 504990 | 629 | -96.9 | 504990 | 724 |
| MR_1774415729_310813F5 | 504990 | 957 | -84.3 | 504990 | 775 | -87.0 | 504990 | 629 | -98.1 | 504990 | 724 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1383: `f3ea1a1f-531...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f3ea1a1f-531e-48c8-a7a0-840246908b67` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261060_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1383] topology](images/train_1383.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3268799_8 and 3279749_5
- `C2`: Decrease transmission power for 3279749_5
- `C3`: Increase transmission power for 3261060_3
- `C4`: Increase A3 Offset threshold for 3279749_5
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261060_3
- `C6`: Adjust the azimuth of 3279749_5 by 38 degrees
- `C7`: Add neighbor relationship between 3261060_3 and 3279749_5
- `C8`: Adjust the azimuth of 3261060_3 by 45 degrees
- `C9`: Decrease A3 Offset threshold for 3261060_3
- `C10`: Lift the tilt angle of 3261060_3 by 2 degrees
- `C11`: Lift the tilt angle  of 3279749_5 by 5 degrees
- `C12`: Increase transmission power for 3279749_5
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279749_5
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase A3 Offset threshold for 3261060_3
- `C16`: Press down the tilt angle  of 3279749_5 by 5 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261060_3 **← 정답**
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279749_5
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle of 3261060_3 by 2 degrees
- `C21`: Decrease transmission power for 3261060_3
- `C22`: Decrease A3 Offset threshold for 3279749_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.452 | MS1 | 121.4656747433 | 31.1446216190 | 398 | 504990 | -95.41 | 13.01 | 553.02 | 0.03 | 2.93 | 1571 |
| 2024-09-20 22:21:32.706 | MS1 | 121.4656581118 | 31.1446324404 | 300 | 504990 | -95.16 | 11.40 | 461.12 | 0.05 | 2.92 | 1591 |
| 2024-09-20 22:21:33.926 | MS1 | 121.4656644207 | 31.1446297493 | 630 | 504990 | -93.40 | 13.53 | 556.46 | 0.05 | 2.60 | 1596 |
| 2024-09-20 22:21:34.509 | MS1 | 121.4656641968 | 31.1446269370 | 853 | 152650 | -92.74 | 6.73 | 48.36 | 0.20 | 1.83 | 957 |
| 2024-09-20 22:21:35.341 | MS1 | 121.4656778786 | 31.1446262308 | 48 | 152650 | -96.59 | 4.07 | 59.81 | 0.05 | 1.66 | 933 |
| 2024-09-20 22:21:36.337 | MS1 | 121.4656744145 | 31.1446348903 | 261 | 152650 | -87.87 | 6.09 | 58.38 | 0.14 | 1.58 | 979 |
| 2024-09-20 22:21:37.220 | MS1 | 121.4656758838 | 31.1446234526 | 77 | 152650 | -92.82 | 3.12 | 90.59 | 0.01 | 1.66 | 995 |
| 2024-09-20 22:21:38.511 | MS1 | 121.4656595479 | 31.1446195210 | 853 | 152650 | -94.41 | 5.18 | 85.41 | 0.06 | 1.82 | 999 |
| 2024-09-20 22:21:39.490 | MS1 | 121.4656652827 | 31.1446294624 | 48 | 152650 | -91.25 | 3.17 | 58.95 | 0.02 | 1.95 | 901 |
| 2024-09-20 22:21:40.285 | MS1 | 121.4656681798 | 31.1446223776 | 261 | 152650 | -87.72 | 6.47 | 79.84 | 0.18 | 2.18 | 1566 |
| 2024-09-20 22:21:41.286 | MS1 | 121.4656611832 | 31.1446321631 | 77 | 152650 | -95.52 | 3.22 | 71.30 | 0.06 | 2.68 | 1566 |
| 2024-09-20 22:21:42.856 | MS1 | 121.4656661892 | 31.1446354127 | 853 | 152650 | -95.40 | 7.18 | 86.30 | 0.03 | 2.35 | 1593 |

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
| 3217682 | 6 | 121.4693967164 | 31.1440511893 | 169 | 14 | 0 | 17.8 | TDD | 351 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3233913 | 7 | 121.4692264212 | 31.1543446682 | 48 | 7 | 7 | 21.1 | FDD | 258 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3250021 | 10 | 121.4659039429 | 31.1446553528 | 325 | 7 | 6 | 28.8 | FDD | 77 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3250036 | 1 | 121.4755478336 | 31.1530701696 | 143 | 2 | 10 | 26.1 | TDD | 296 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3255889 | 11 | 121.4747707457 | 31.1520235240 | 237 | 11 | 10 | 18.6 | FDD | 175 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3256929 | 2 | 121.4697038799 | 31.1453606636 | 281 | 6 | 6 | 23.0 | TDD | 300 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3260871 | 13 | 121.4656939906 | 31.1490534717 | 263 | 8 | 2 | 21.9 | FDD | 853 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3261060 | 3 | 121.4717363533 | 31.1499034259 | 270 | 0 | 11 | 27.6 | TDD | 398 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3268799 | 8 | 121.4694920724 | 31.1480219546 | 142 | 1 | 8 | 10.8 | FDD | 261 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3270799 | 12 | 121.4679905103 | 31.1496145909 | 107 | 11 | 10 | 17.0 | FDD | 48 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3276332 | 9 | 121.4756917144 | 31.1556798827 | 334 | 10 | 9 | 29.7 | FDD | 138 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3278624 | 4 | 121.4655222166 | 31.1509768018 | 243 | 13 | 0 | 22.2 | TDD | 630 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3279749 | 5 | 121.4719593217 | 31.1548715463 | 170 | 5 | 5 | 1.3 | TDD | 123 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.208 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.228 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.360 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.360 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.032 | NREventA2 | measId:1;ServCellPCI:302;Se... |
| 2024-09-20 22:21:35.135 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.406 | NREventA5 | measId:3;ServCellPCI:302;Se... |
| 2024-09-20 22:21:35.443 | NRHandoverAttempt | SourcePCI:302;SourceNR-ARFC... |
| 2024-09-20 22:21:35.469 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.483 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.620 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.620 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250036 | 1 | 7.4827 | 5.8550 | -115.4489 | 5.0694 | 147.8832 | 0.0153 | 0.0170 |
| 2024_09_20 22:00 | 3256929 | 2 | 11.1538 | 15.4294 | -117.0427 | 6.5780 | 155.1454 | 0.0196 | 0.0163 |
| 2024_09_20 22:00 | 3261060 | 3 | 6.8798 | 16.9804 | -117.2709 | 8.8171 | 153.2875 | 0.0018 | 0.0078 |
| 2024_09_20 22:00 | 3278624 | 4 | 10.1276 | 5.0242 | -117.4078 | 18.3348 | 144.1454 | 0.0141 | 0.0131 |
| 2024_09_20 22:00 | 3279749 | 5 | 11.9313 | 9.7457 | -116.7532 | 7.1050 | 197.1940 | 0.0133 | 0.0084 |
| 2024_09_20 22:00 | 3217682 | 6 | 11.2166 | 8.5950 | -115.3599 | 10.1837 | 119.2444 | 0.0137 | 0.0160 |
| 2024_09_20 22:00 | 3233913 | 7 | 7.3598 | 12.1979 | -115.6569 | 4.4739 | 45.4517 | 0.0154 | 0.0199 |
| 2024_09_20 22:00 | 3268799 | 8 | 9.2965 | 5.7589 | -116.8608 | 4.4347 | 50.5715 | 0.0150 | 0.0181 |
| 2024_09_20 22:00 | 3276332 | 9 | 5.5865 | 11.6202 | -114.8685 | 4.9178 | 55.4954 | 0.0043 | 0.0144 |
| 2024_09_20 22:00 | 3250021 | 10 | 18.6363 | 11.8672 | -117.3076 | 3.7033 | 44.8161 | 0.0022 | 0.0048 |
| 2024_09_20 22:00 | 3255889 | 11 | 15.7094 | 12.6058 | -115.7087 | 4.7139 | 58.6637 | 0.0066 | 0.0165 |
| 2024_09_20 22:00 | 3270799 | 12 | 10.8788 | 13.9542 | -117.8017 | 3.6925 | 30.4892 | 0.0108 | 0.0158 |
| 2024_09_20 22:00 | 3260871 | 13 | 5.8718 | 14.7554 | -116.8832 | 3.4915 | 38.9986 | 0.0063 | 0.0181 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416324_F9267EDC | 152650 | 853 | -94.7 | 152650 | 138 | -96.3 | 152650 | 258 | -101.3 | 152650 | 175 |
| MR_1774416324_51A3CB11 | 504990 | 630 | -92.5 | 504990 | 123 | -95.2 | 504990 | 351 | -98.2 | 504990 | 296 |
| MR_1774416324_658F60BA | 504990 | 630 | -92.2 | 504990 | 123 | -92.9 | 504990 | 351 | -95.8 | 504990 | 296 |
| MR_1774416324_E2D49602 | 152650 | 853 | -93.4 | 152650 | 138 | -94.2 | 152650 | 258 | -100.5 | 152650 | 175 |
| MR_1774416324_89970F5C | 504990 | 630 | -93.9 | 504990 | 123 | -92.4 | 504990 | 351 | -98.7 | 504990 | 296 |
| MR_1774416324_8A668CFA | 152650 | 853 | -93.0 | 152650 | 138 | -94.2 | 152650 | 258 | -99.5 | 152650 | 175 |
| MR_1774416324_614C6027 | 504990 | 630 | -93.8 | 504990 | 123 | -93.5 | 504990 | 351 | -96.9 | 504990 | 296 |
| MR_1774416324_1F601F4F | 152650 | 853 | -92.2 | 152650 | 138 | -95.1 | 152650 | 258 | -99.3 | 152650 | 175 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1384: `0576283e-ad0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0576283e-ad00-4c81-b083-2050ec024515` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3233934_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1384] topology](images/train_1384.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3276982_1
- `C2`: Adjust the azimuth of 3233934_2 by 18 degrees
- `C3`: Increase transmission power for 3276982_1
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Increase A3 Offset threshold for 3233934_2
- `C6`: Add neighbor relationship between 3233934_2 and 3276982_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276982_1
- `C8`: Check test server and transmission issues
- `C9`: Press down the tilt angle of 3233934_2 by 3 degrees
- `C10`: Lift the tilt angle  of 3276982_1 by 10 degrees
- `C11`: Decrease A3 Offset threshold for 3233934_2
- `C12`: Increase transmission power for 3233934_2
- `C13`: Decrease transmission power for 3233934_2
- `C14`: Add neighbor relationship between 3271046_4 and 3276982_1
- `C15`: Decrease transmission power for 3276982_1
- `C16`: Adjust the azimuth of 3276982_1 by 50 degrees
- `C17`: Decrease A3 Offset threshold for 3276982_1
- `C18`: Lift the tilt angle of 3233934_2 by 3 degrees
- `C19`: Press down the tilt angle  of 3276982_1 by 10 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276982_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233934_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233934_2 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.353 | MS1 | 121.4656750132 | 31.1446342465 | 459 | 504990 | -91.42 | 13.29 | 483.56 | 0.08 | 2.43 | 1574 |
| 2024-09-20 22:21:32.685 | MS1 | 121.4656697768 | 31.1446329134 | 459 | 504990 | -87.07 | 13.54 | 556.63 | 0.16 | 2.21 | 1587 |
| 2024-09-20 22:21:33.296 | MS1 | 121.4656701641 | 31.1446339794 | 459 | 504990 | -90.23 | 16.20 | 370.59 | 0.12 | 2.46 | 1566 |
| 2024-09-20 22:21:34.614 | MS1 | 121.4656685640 | 31.1446236130 | 459 | 504990 | -87.39 | 13.02 | 66.29 | 0.53 | 2.67 | 601 |
| 2024-09-20 22:21:35.615 | MS1 | 121.4656696271 | 31.1446181117 | 459 | 504990 | -91.95 | 16.19 | 92.21 | 0.58 | 2.84 | 569 |
| 2024-09-20 22:21:36.820 | MS1 | 121.4656609112 | 31.1446194044 | 459 | 504990 | -90.01 | 16.97 | 55.74 | 0.54 | 2.45 | 594 |
| 2024-09-20 22:21:37.281 | MS1 | 121.4656636027 | 31.1446218405 | 459 | 504990 | -92.38 | 12.66 | 61.76 | 0.69 | 2.31 | 506 |
| 2024-09-20 22:21:38.900 | MS1 | 121.4656722990 | 31.1446290658 | 459 | 504990 | -91.27 | 9.00 | 89.59 | 0.66 | 2.23 | 548 |
| 2024-09-20 22:21:39.477 | MS1 | 121.4656627277 | 31.1446354137 | 459 | 504990 | -92.13 | 9.53 | 59.43 | 0.59 | 2.39 | 648 |
| 2024-09-20 22:21:40.438 | MS1 | 121.4656613935 | 31.1446311164 | 459 | 504990 | -89.12 | 11.24 | 555.36 | 0.06 | 2.56 | 1560 |
| 2024-09-20 22:21:41.999 | MS1 | 121.4656773771 | 31.1446243934 | 459 | 504990 | -91.07 | 8.40 | 499.06 | 0.17 | 2.82 | 1598 |
| 2024-09-20 22:21:42.808 | MS1 | 121.4656703493 | 31.1446378643 | 459 | 504990 | -91.20 | 8.72 | 367.56 | 0.11 | 2.16 | 1582 |

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
| 3233934 | 2 | 121.4756616922 | 31.1542458039 | 240 | 1 | 6 | 45.9 | TDD | 459 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3271046 | 4 | 121.4647842716 | 31.1521280911 | 96 | 2 | 9 | 41.6 | TDD | 175 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3275193 | 3 | 121.4693035040 | 31.1529580405 | 126 | 9 | 7 | 34.0 | TDD | 179 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3276982 | 1 | 121.4711990912 | 31.1520805400 | 14 | 7 | 8 | 48.8 | TDD | 25 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.122 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.138 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.268 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.268 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.971 | NREventA3 | measId:2;ServCellPCI:863;Se... |
| 2024-09-20 22:21:38.211 | NRHandoverAttempt | SourcePCI:863;SourceNR-ARFC... |
| 2024-09-20 22:21:38.248 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.262 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.404 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.404 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276982 | 1 | 11.1858 | 6.3156 | -115.0204 | 17.0268 | 123.5914 | 0.0136 | 0.0031 |
| 2024_09_20 22:00 | 3233934 | 2 | 11.6278 | 6.9159 | -116.1253 | 15.9170 | 197.3291 | 0.0143 | 0.0074 |
| 2024_09_20 22:00 | 3275193 | 3 | 12.6741 | 18.8102 | -116.8351 | 18.6790 | 141.6667 | 0.0144 | 0.0184 |
| 2024_09_20 22:00 | 3271046 | 4 | 16.7518 | 18.4931 | -117.6031 | 8.9866 | 129.5810 | 0.0065 | 0.0031 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415078_3307E17E | 504990 | 459 | -88.5 | 504990 | 25 | -89.9 | 504990 | 175 | -95.0 | 504990 | 179 |
| MR_1774415078_098E44C6 | 504990 | 459 | -89.4 | 504990 | 25 | -90.1 | 504990 | 175 | -95.5 | 504990 | 179 |
| MR_1774415078_9AA41242 | 504990 | 459 | -87.8 | 504990 | 25 | -89.8 | 504990 | 175 | -95.4 | 504990 | 179 |
| MR_1774415078_E0842645 | 504990 | 459 | -87.2 | 504990 | 25 | -91.1 | 504990 | 175 | -96.3 | 504990 | 179 |
| MR_1774415078_0AB66BB5 | 504990 | 459 | -85.7 | 504990 | 25 | -91.8 | 504990 | 175 | -94.6 | 504990 | 179 |
| MR_1774415078_C8543E91 | 504990 | 459 | -88.3 | 504990 | 25 | -93.2 | 504990 | 175 | -96.4 | 504990 | 179 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1385: `fa53a29e-1ab...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fa53a29e-1abd-4f04-b9e5-0da7dd04a8e1` |
| Tag | **multiple-answer** |
| 정답 | **C3|C18** |
| C3 의미 | Increase transmission power for 3230997_2 |
| C18 의미 | Adjust the azimuth of 3230997_2 by 25 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1385] topology](images/train_1385.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3230997_2
- `C2`: Add neighbor relationship between 3230997_2 and 3267519_3
- `C3`: Increase transmission power for 3230997_2 **← 정답**
- `C4`: Increase transmission power for 3267519_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230997_2
- `C6`: Check test server and transmission issues
- `C7`: Decrease transmission power for 3267519_3
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Lift the tilt angle of 3230997_2 by 10 degrees
- `C10`: Lift the tilt angle  of 3267519_3 by 4 degrees
- `C11`: Press down the tilt angle of 3230997_2 by 10 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267519_3
- `C13`: Decrease A3 Offset threshold for 3230997_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267519_3
- `C15`: Press down the tilt angle  of 3267519_3 by 4 degrees
- `C16`: Add neighbor relationship between 3277994_1 and 3267519_3
- `C17`: Increase A3 Offset threshold for 3267519_3
- `C18`: Adjust the azimuth of 3230997_2 by 25 degrees **← 정답**
- `C19`: Decrease A3 Offset threshold for 3267519_3
- `C20`: Decrease transmission power for 3230997_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230997_2
- `C22`: Adjust the azimuth of 3267519_3 by 27 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.397 | MS1 | 121.4656693470 | 31.1446288112 | 81 | 504990 | -94.75 | 16.94 | 390.89 | 0.03 | 2.60 | 1589 |
| 2024-09-20 22:21:32.681 | MS1 | 121.4656717918 | 31.1446323636 | 81 | 504990 | -85.71 | 12.74 | 386.33 | 0.08 | 2.72 | 1574 |
| 2024-09-20 22:21:33.663 | MS1 | 121.4656652994 | 31.1446325691 | 81 | 504990 | -90.88 | 13.50 | 432.01 | 0.16 | 2.19 | 1594 |
| 2024-09-20 22:21:34.197 | MS1 | 121.4656633532 | 31.1446307400 | 81 | 504990 | -109.35 | 1.48 | 32.15 | 0.18 | 1.02 | 1583 |
| 2024-09-20 22:21:35.698 | MS1 | 121.4656703259 | 31.1446209238 | 81 | 504990 | -109.98 | 1.41 | 34.41 | 0.08 | 1.29 | 1564 |
| 2024-09-20 22:21:36.824 | MS1 | 121.4656638850 | 31.1446258095 | 81 | 504990 | -105.34 | 1.77 | 66.50 | 0.15 | 1.30 | 1570 |
| 2024-09-20 22:21:37.638 | MS1 | 121.4656693614 | 31.1446194250 | 81 | 504990 | -103.09 | 0.78 | 48.87 | 0.07 | 1.42 | 1600 |
| 2024-09-20 22:21:38.857 | MS1 | 121.4656720483 | 31.1446372608 | 81 | 504990 | -107.40 | 0.53 | 52.85 | 0.05 | 1.28 | 1574 |
| 2024-09-20 22:21:39.235 | MS1 | 121.4656767554 | 31.1446298317 | 81 | 504990 | -109.03 | 1.26 | 69.47 | 0.10 | 1.22 | 1564 |
| 2024-09-20 22:21:40.497 | MS1 | 121.4656602210 | 31.1446296462 | 81 | 504990 | -89.36 | 12.29 | 329.30 | 0.10 | 2.89 | 1569 |
| 2024-09-20 22:21:41.872 | MS1 | 121.4656722950 | 31.1446328510 | 81 | 504990 | -86.47 | 12.35 | 340.79 | 0.04 | 2.73 | 1581 |
| 2024-09-20 22:21:42.620 | MS1 | 121.4656748881 | 31.1446339789 | 81 | 504990 | -85.55 | 15.34 | 406.24 | 0.18 | 2.70 | 1576 |

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
| 3230997 | 2 | 121.4640105843 | 31.1453737267 | 143 | 6 | 3 | 16.0 | TDD | 81 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3260870 | 4 | 121.4759017843 | 31.1488101940 | 336 | 14 | 3 | 18.4 | TDD | 584 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3267519 | 3 | 121.4753346736 | 31.1471547889 | 280 | 2 | 6 | 37.7 | TDD | 171 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3277994 | 1 | 121.4753029531 | 31.1507435186 | 202 | 1 | 0 | 19.3 | TDD | 672 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.056 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.195 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.195 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.428 | NREventA2 | measId:1;ServCellPCI:343;Se... |
| 2024-09-20 22:21:34.545 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277994 | 1 | 7.4156 | 13.1796 | -115.2331 | 15.5343 | 170.7527 | 0.0038 | 0.0149 |
| 2024_09_20 22:00 | 3230997 | 2 | 13.7283 | 10.5124 | -114.3565 | 11.2404 | 124.7816 | 0.1679 | 0.0025 |
| 2024_09_20 22:00 | 3267519 | 3 | 15.4054 | 7.0812 | -115.1709 | 18.4673 | 108.3900 | 0.0064 | 0.0003 |
| 2024_09_20 22:00 | 3260870 | 4 | 15.5483 | 13.2881 | -114.4592 | 19.9218 | 169.8387 | 0.0170 | 0.0119 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412306_89D36701 | 504990 | 81 | -109.5 | 504990 | 171 | -111.7 | 504990 | 672 | -117.9 | 504990 | 584 |
| MR_1774412306_3EB05430 | 504990 | 81 | -107.5 | 504990 | 171 | -115.0 | 504990 | 672 | -121.0 | 504990 | 584 |
| MR_1774412306_30331CD9 | 504990 | 81 | -110.5 | 504990 | 171 | -111.9 | 504990 | 672 | -118.1 | 504990 | 584 |
| MR_1774412306_F622B845 | 504990 | 81 | -109.5 | 504990 | 171 | -112.5 | 504990 | 672 | -121.2 | 504990 | 584 |
| MR_1774412306_DE4797B3 | 504990 | 81 | -110.8 | 504990 | 171 | -114.0 | 504990 | 672 | -119.0 | 504990 | 584 |
| MR_1774412306_F06CFA0B | 504990 | 81 | -108.5 | 504990 | 171 | -112.7 | 504990 | 672 | -119.8 | 504990 | 584 |
| MR_1774412306_D594E03E | 504990 | 81 | -107.8 | 504990 | 171 | -112.6 | 504990 | 672 | -121.0 | 504990 | 584 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1386: `43ade285-aa8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `43ade285-aa8d-4c3b-9345-6ddd29684f5f` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251336_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1386] topology](images/train_1386.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3277683_2 by 18 degrees
- `C2`: Increase A3 Offset threshold for 3277683_2
- `C3`: Increase transmission power for 3277683_2
- `C4`: Increase A3 Offset threshold for 3251336_6
- `C5`: Decrease transmission power for 3277683_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251336_6 **← 정답**
- `C7`: Decrease A3 Offset threshold for 3251336_6
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251336_6
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277683_2
- `C10`: Lift the tilt angle  of 3277683_2 by 5 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Check test server and transmission issues
- `C13`: Decrease A3 Offset threshold for 3277683_2
- `C14`: Press down the tilt angle  of 3277683_2 by 5 degrees
- `C15`: Decrease transmission power for 3251336_6
- `C16`: Add neighbor relationship between 3251336_6 and 3277683_2
- `C17`: Increase transmission power for 3251336_6
- `C18`: Add neighbor relationship between 3235501_9 and 3277683_2
- `C19`: Press down the tilt angle of 3251336_6 by 1 degrees
- `C20`: Lift the tilt angle of 3251336_6 by 1 degrees
- `C21`: Adjust the azimuth of 3251336_6 by 20 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277683_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.396 | MS1 | 121.4656656588 | 31.1446193351 | 444 | 504990 | -93.24 | 14.10 | 556.22 | 0.12 | 2.95 | 1587 |
| 2024-09-20 22:21:32.187 | MS1 | 121.4656779480 | 31.1446273341 | 248 | 504990 | -95.45 | 13.90 | 457.17 | 0.17 | 2.96 | 1580 |
| 2024-09-20 22:21:33.797 | MS1 | 121.4656606515 | 31.1446344263 | 433 | 504990 | -93.80 | 10.35 | 387.08 | 0.07 | 2.26 | 1600 |
| 2024-09-20 22:21:34.463 | MS1 | 121.4656730105 | 31.1446252792 | 219 | 152650 | -87.44 | 2.48 | 80.74 | 0.18 | 1.72 | 991 |
| 2024-09-20 22:21:35.515 | MS1 | 121.4656593179 | 31.1446320278 | 883 | 152650 | -92.50 | 2.19 | 59.16 | 0.09 | 1.51 | 960 |
| 2024-09-20 22:21:36.281 | MS1 | 121.4656705732 | 31.1446190055 | 656 | 152650 | -93.57 | 7.42 | 71.12 | 0.10 | 1.52 | 956 |
| 2024-09-20 22:21:37.317 | MS1 | 121.4656754075 | 31.1446274141 | 606 | 152650 | -94.72 | 5.95 | 86.51 | 0.18 | 1.93 | 915 |
| 2024-09-20 22:21:38.262 | MS1 | 121.4656735904 | 31.1446281188 | 219 | 152650 | -88.06 | 5.48 | 85.68 | 0.11 | 1.57 | 982 |
| 2024-09-20 22:21:39.721 | MS1 | 121.4656597959 | 31.1446358033 | 883 | 152650 | -93.65 | 6.28 | 97.17 | 0.07 | 1.96 | 952 |
| 2024-09-20 22:21:40.541 | MS1 | 121.4656741758 | 31.1446244729 | 656 | 152650 | -95.61 | 3.92 | 49.76 | 0.16 | 2.87 | 1563 |
| 2024-09-20 22:21:41.657 | MS1 | 121.4656652673 | 31.1446231377 | 606 | 152650 | -95.16 | 6.25 | 97.85 | 0.10 | 2.35 | 1567 |
| 2024-09-20 22:21:42.679 | MS1 | 121.4656611014 | 31.1446206618 | 219 | 152650 | -87.18 | 3.66 | 43.15 | 0.04 | 2.47 | 1587 |

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
| 3216394 | 1 | 121.4745142346 | 31.1520148834 | 16 | 14 | 11 | 29.2 | TDD | 997 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3221747 | 10 | 121.4717630629 | 31.1445644929 | 141 | 6 | 11 | 28.3 | FDD | 883 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3235501 | 9 | 121.4686028711 | 31.1541657754 | 269 | 6 | 8 | 7.9 | FDD | 656 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3238745 | 7 | 121.4677681860 | 31.1544634385 | 334 | 1 | 1 | 23.9 | FDD | 350 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3251336 | 6 | 121.4751944652 | 31.1525043295 | 206 | 0 | 10 | 29.5 | TDD | 444 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3252736 | 4 | 121.4661181832 | 31.1498385369 | 105 | 5 | 12 | 29.0 | TDD | 241 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3259656 | 11 | 121.4728015681 | 31.1470514506 | 90 | 8 | 8 | 29.8 | FDD | 219 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3267310 | 3 | 121.4750710548 | 31.1466259698 | 146 | 0 | 7 | 5.3 | TDD | 433 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3275363 | 5 | 121.4690411162 | 31.1469722320 | 290 | 2 | 5 | 8.6 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3277409 | 13 | 121.4719127315 | 31.1497050420 | 299 | 4 | 10 | 29.2 | FDD | 606 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3277683 | 2 | 121.4688929469 | 31.1484507633 | 234 | 3 | 6 | 16.4 | TDD | 842 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3279368 | 12 | 121.4752736035 | 31.1469473119 | 295 | 1 | 3 | 13.3 | FDD | 349 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3279546 | 8 | 121.4727565630 | 31.1516266538 | 201 | 9 | 9 | 7.8 | FDD | 226 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |

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
| 2024-09-20 22:21:31.175 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.190 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.321 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.321 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.044 | NREventA2 | measId:1;ServCellPCI:280;Se... |
| 2024-09-20 22:21:35.163 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.383 | NREventA5 | measId:3;ServCellPCI:280;Se... |
| 2024-09-20 22:21:35.431 | NRHandoverAttempt | SourcePCI:280;SourceNR-ARFC... |
| 2024-09-20 22:21:35.457 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.468 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.587 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.587 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216394 | 1 | 19.3247 | 6.3778 | -116.1415 | 12.6562 | 150.3034 | 0.0019 | 0.0078 |
| 2024_09_20 22:00 | 3277683 | 2 | 16.6442 | 5.1305 | -114.3500 | 8.8828 | 153.7208 | 0.0098 | 0.0038 |
| 2024_09_20 22:00 | 3267310 | 3 | 11.5034 | 14.9456 | -116.8338 | 14.9827 | 94.6090 | 0.0134 | 0.0023 |
| 2024_09_20 22:00 | 3252736 | 4 | 18.8998 | 11.4459 | -114.9044 | 14.0731 | 171.8946 | 0.0035 | 0.0137 |
| 2024_09_20 22:00 | 3275363 | 5 | 8.3805 | 11.0383 | -116.3804 | 19.6823 | 167.6886 | 0.0018 | 0.0170 |
| 2024_09_20 22:00 | 3251336 | 6 | 12.2028 | 12.9366 | -117.9408 | 10.9871 | 175.0522 | 0.0142 | 0.0089 |
| 2024_09_20 22:00 | 3238745 | 7 | 14.7077 | 16.1924 | -117.5273 | 4.2934 | 47.9599 | 0.0097 | 0.0160 |
| 2024_09_20 22:00 | 3279546 | 8 | 14.4218 | 14.3838 | -116.4509 | 4.6972 | 57.4155 | 0.0028 | 0.0014 |
| 2024_09_20 22:00 | 3235501 | 9 | 13.2323 | 7.1514 | -117.8145 | 3.8414 | 55.1269 | 0.0002 | 0.0136 |
| 2024_09_20 22:00 | 3221747 | 10 | 9.3627 | 8.9228 | -116.0622 | 4.3494 | 23.6455 | 0.0160 | 0.0020 |
| 2024_09_20 22:00 | 3259656 | 11 | 16.1363 | 15.0771 | -116.2515 | 3.8971 | 29.0127 | 0.0069 | 0.0109 |
| 2024_09_20 22:00 | 3279368 | 12 | 16.0499 | 12.3870 | -114.3639 | 4.9345 | 36.5504 | 0.0038 | 0.0188 |
| 2024_09_20 22:00 | 3277409 | 13 | 14.2794 | 12.5054 | -115.2238 | 4.2065 | 46.3816 | 0.0114 | 0.0110 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415173_2B233755 | 152650 | 219 | -88.0 | 152650 | 349 | -92.8 | 152650 | 350 | -95.2 | 152650 | 226 |
| MR_1774415173_8D4C006B | 504990 | 433 | -93.0 | 504990 | 842 | -94.0 | 504990 | 241 | -93.3 | 504990 | 997 |
| MR_1774415173_AE77A42E | 504990 | 433 | -92.7 | 504990 | 842 | -91.0 | 504990 | 241 | -92.8 | 504990 | 997 |
| MR_1774415173_0664F55B | 504990 | 433 | -95.2 | 504990 | 842 | -90.7 | 504990 | 241 | -95.8 | 504990 | 997 |
| MR_1774415173_6445F25B | 504990 | 433 | -93.3 | 504990 | 842 | -92.1 | 504990 | 241 | -92.9 | 504990 | 997 |
| MR_1774415173_AF5ED058 | 504990 | 433 | -94.4 | 504990 | 842 | -92.3 | 504990 | 241 | -94.5 | 504990 | 997 |
| MR_1774415173_E28B2EE6 | 152650 | 219 | -88.8 | 152650 | 349 | -91.5 | 152650 | 350 | -94.5 | 152650 | 226 |
| MR_1774415173_307035CA | 152650 | 219 | -88.5 | 152650 | 349 | -93.2 | 152650 | 350 | -97.7 | 152650 | 226 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1387: `527e5d4b-abc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `527e5d4b-abc1-4950-a255-12f55a287b06` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1387] topology](images/train_1387.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3211594_2 by 10 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252430_3
- `C3`: Increase A3 Offset threshold for 3252430_3
- `C4`: Decrease A3 Offset threshold for 3252430_3
- `C5`: Increase transmission power for 3252430_3
- `C6`: Increase transmission power for 3211594_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211594_2
- `C8`: Add neighbor relationship between 3268396_1 and 3252430_3
- `C9`: Press down the tilt angle of 3211594_2 by 10 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252430_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211594_2
- `C12`: Adjust the azimuth of 3211594_2 by 50 degrees
- `C13`: Check test server and transmission issues
- `C14`: Decrease transmission power for 3252430_3
- `C15`: Decrease A3 Offset threshold for 3211594_2
- `C16`: Adjust the azimuth of 3252430_3 by 50 degrees
- `C17`: Increase A3 Offset threshold for 3211594_2
- `C18`: Lift the tilt angle  of 3252430_3 by 10 degrees
- `C19`: Decrease transmission power for 3211594_2
- `C20`: Press down the tilt angle  of 3252430_3 by 10 degrees
- `C21`: Add neighbor relationship between 3211594_2 and 3252430_3
- `C22`: Insufficient data; more data is needed for judgment. **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.202 | MS1 | 121.4656653219 | 31.1446317362 | 467 | 504990 | -89.81 | 14.24 | 490.68 | 0.11 | 2.87 | 1567 |
| 2024-09-20 22:21:32.956 | MS1 | 121.4656757189 | 31.1446268451 | 467 | 504990 | -91.46 | 14.52 | 420.15 | 0.03 | 2.51 | 1598 |
| 2024-09-20 22:21:33.517 | MS1 | 121.4656605297 | 31.1446216873 | 467 | 504990 | -85.73 | 15.82 | 514.62 | 0.02 | 2.52 | 1576 |
| 2024-09-20 22:21:34.875 | MS1 | 121.4656590037 | 31.1446206594 | 467 | 504990 | -89.57 | 16.06 | 90.32 | 0.05 | 2.71 | 1594 |
| 2024-09-20 22:21:35.462 | MS1 | 121.4656736743 | 31.1446335388 | 467 | 504990 | -85.55 | 15.45 | 79.60 | 0.14 | 2.81 | 1600 |
| 2024-09-20 22:21:36.197 | MS1 | 121.4656740573 | 31.1446197388 | 467 | 504990 | -88.60 | 12.82 | 84.77 | 0.01 | 2.72 | 1569 |
| 2024-09-20 22:21:37.838 | MS1 | 121.4656724326 | 31.1446302034 | 467 | 504990 | -93.21 | 12.54 | 94.32 | 0.10 | 2.08 | 1583 |
| 2024-09-20 22:21:38.462 | MS1 | 121.4656635659 | 31.1446269664 | 467 | 504990 | -90.87 | 9.54 | 58.44 | 0.02 | 2.78 | 1561 |
| 2024-09-20 22:21:39.133 | MS1 | 121.4656653922 | 31.1446292397 | 467 | 504990 | -91.82 | 12.49 | 46.62 | 0.13 | 2.77 | 1593 |
| 2024-09-20 22:21:40.939 | MS1 | 121.4656757378 | 31.1446295639 | 467 | 504990 | -89.40 | 12.43 | 443.43 | 0.14 | 2.91 | 1591 |
| 2024-09-20 22:21:41.137 | MS1 | 121.4656768571 | 31.1446306878 | 467 | 504990 | -92.74 | 10.08 | 351.08 | 0.19 | 2.18 | 1595 |
| 2024-09-20 22:21:42.992 | MS1 | 121.4656760913 | 31.1446360450 | 467 | 504990 | -91.22 | 7.04 | 478.02 | 0.12 | 2.53 | 1587 |

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
| 3211594 | 2 | 121.4666960675 | 31.1463139541 | 303 | 12 | 7 | 21.6 | TDD | 467 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3211835 | 4 | 121.4646663506 | 31.1530959029 | 208 | 15 | 10 | 36.9 | TDD | 395 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3252430 | 3 | 121.4706000492 | 31.1470923340 | 330 | 12 | 4 | 42.3 | TDD | 156 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3268396 | 1 | 121.4745641654 | 31.1485043050 | 144 | 6 | 10 | 34.8 | TDD | 16 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.817 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.834 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.939 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.939 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.624 | NREventA3 | measId:2;ServCellPCI:917;Se... |
| 2024-09-20 22:21:37.864 | NRHandoverAttempt | SourcePCI:917;SourceNR-ARFC... |
| 2024-09-20 22:21:37.905 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.917 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.066 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.066 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3268396 | 1 | 79.2455 | 77.6822 | -114.4251 | 10.2374 | 100.2328 | 0.0118 | 0.0156 |
| 2024_09_19 22:00 | 3211594 | 2 | 85.1219 | 76.7699 | -116.6742 | 17.8174 | 188.6850 | 0.0110 | 0.0075 |
| 2024_09_19 22:00 | 3252430 | 3 | 83.6669 | 90.6117 | -114.7612 | 11.1422 | 92.9741 | 0.0142 | 0.0131 |
| 2024_09_19 22:00 | 3211835 | 4 | 92.1613 | 89.0635 | -114.2374 | 11.6430 | 158.2939 | 0.0194 | 0.0020 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412481_56A48488 | 504990 | 467 | -88.2 | 504990 | 156 | -93.4 | 504990 | 16 | -97.9 | 504990 | 395 |
| MR_1774412481_54B82803 | 504990 | 467 | -90.1 | 504990 | 156 | -91.7 | 504990 | 16 | -100.8 | 504990 | 395 |
| MR_1774412481_BB683AD7 | 504990 | 467 | -90.5 | 504990 | 156 | -93.8 | 504990 | 16 | -100.8 | 504990 | 395 |
| MR_1774412481_A56ABDCC | 504990 | 467 | -88.4 | 504990 | 156 | -94.4 | 504990 | 16 | -98.3 | 504990 | 395 |
| MR_1774412481_F966D7BD | 504990 | 467 | -90.7 | 504990 | 156 | -94.1 | 504990 | 16 | -100.2 | 504990 | 395 |
| MR_1774412481_22EA1E62 | 504990 | 467 | -87.7 | 504990 | 156 | -94.2 | 504990 | 16 | -100.5 | 504990 | 395 |
| MR_1774412481_6F42855F | 504990 | 467 | -90.6 | 504990 | 156 | -93.8 | 504990 | 16 | -97.9 | 504990 | 395 |
| MR_1774412481_B8E03287 | 504990 | 467 | -88.8 | 504990 | 156 | -94.2 | 504990 | 16 | -98.4 | 504990 | 395 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1388: `422078e9-386...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `422078e9-386d-4332-a9c4-c9af8312d70b` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease A3 Offset threshold for 3221713_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1388] topology](images/train_1388.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3268055_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268055_3
- `C3`: Lift the tilt angle of 3221713_1 by 10 degrees
- `C4`: Decrease transmission power for 3221713_1
- `C5`: Decrease transmission power for 3268055_3
- `C6`: Press down the tilt angle of 3221713_1 by 10 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221713_1
- `C9`: Press down the tilt angle  of 3268055_3 by 2 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268055_3
- `C11`: Add neighbor relationship between 3251161_4 and 3268055_3
- `C12`: Check test server and transmission issues
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221713_1
- `C14`: Increase A3 Offset threshold for 3221713_1
- `C15`: Increase transmission power for 3221713_1
- `C16`: Adjust the azimuth of 3268055_3 by 50 degrees
- `C17`: Add neighbor relationship between 3221713_1 and 3268055_3
- `C18`: Increase A3 Offset threshold for 3268055_3
- `C19`: Adjust the azimuth of 3221713_1 by 5 degrees
- `C20`: Decrease A3 Offset threshold for 3268055_3
- `C21`: Lift the tilt angle  of 3268055_3 by 2 degrees
- `C22`: Decrease A3 Offset threshold for 3221713_1 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.976 | MS1 | 121.4656771539 | 31.1446219646 | 407 | 504990 | -77.39 | 17.27 | 551.24 | 0.04 | 2.53 | 1561 |
| 2024-09-20 22:21:32.741 | MS1 | 121.4656608761 | 31.1446350393 | 407 | 504990 | -75.42 | 14.19 | 446.58 | 0.09 | 2.64 | 1579 |
| 2024-09-20 22:21:33.770 | MS1 | 121.4656738851 | 31.1446288993 | 407 | 504990 | -83.11 | 17.53 | 566.21 | 0.04 | 2.01 | 1563 |
| 2024-09-20 22:21:34.210 | MS1 | 121.4656631926 | 31.1446262198 | 407 | 504990 | -91.50 | -3.78 | 53.02 | 0.09 | 1.03 | 1565 |
| 2024-09-20 22:21:35.442 | MS1 | 121.4656738550 | 31.1446199832 | 407 | 504990 | -92.12 | -3.98 | 40.92 | 0.14 | 1.45 | 1597 |
| 2024-09-20 22:21:36.209 | MS1 | 121.4656724585 | 31.1446198270 | 407 | 504990 | -90.77 | -0.30 | 47.54 | 0.13 | 1.18 | 1585 |
| 2024-09-20 22:21:37.732 | MS1 | 121.4656775586 | 31.1446226316 | 407 | 504990 | -85.10 | -1.97 | 79.71 | 0.16 | 1.39 | 1580 |
| 2024-09-20 22:21:38.130 | MS1 | 121.4656622435 | 31.1446337772 | 407 | 504990 | -87.98 | -2.16 | 59.60 | 0.17 | 1.17 | 1594 |
| 2024-09-20 22:21:39.503 | MS1 | 121.4656750701 | 31.1446226716 | 133 | 504990 | -81.96 | 16.29 | 254.27 | 0.20 | 1.14 | 1587 |
| 2024-09-20 22:21:40.674 | MS1 | 121.4656668041 | 31.1446302220 | 133 | 504990 | -83.59 | 17.13 | 374.36 | 0.20 | 2.08 | 1581 |
| 2024-09-20 22:21:41.741 | MS1 | 121.4656607837 | 31.1446294820 | 133 | 504990 | -81.59 | 17.67 | 400.78 | 0.02 | 2.65 | 1589 |
| 2024-09-20 22:21:42.915 | MS1 | 121.4656708238 | 31.1446323774 | 133 | 504990 | -77.54 | 12.66 | 503.02 | 0.17 | 2.42 | 1572 |

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
| 3221713 | 1 | 121.4651265580 | 31.1482773561 | 168 | 13 | 4 | 29.5 | TDD | 407 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3251161 | 4 | 121.4686437773 | 31.1480501477 | 19 | 15 | 8 | 47.8 | TDD | 279 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3256837 | 2 | 121.4691798175 | 31.1510214458 | 110 | 13 | 1 | 39.6 | TDD | 315 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3268055 | 3 | 121.4707776238 | 31.1519670629 | 302 | 1 | 6 | 16.7 | TDD | 133 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.525 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.543 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.665 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.665 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.412 | NREventA3 | measId:2;ServCellPCI:617;Se... |
| 2024-09-20 22:21:38.652 | NRHandoverAttempt | SourcePCI:617;SourceNR-ARFC... |
| 2024-09-20 22:21:38.699 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.709 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.826 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.826 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221713 | 1 | 19.9278 | 19.7696 | -116.9326 | 16.3457 | 172.4749 | 0.0137 | 0.1656 |
| 2024_09_20 22:00 | 3256837 | 2 | 19.6864 | 17.3052 | -114.6047 | 16.3076 | 85.2709 | 0.0023 | 0.0100 |
| 2024_09_20 22:00 | 3268055 | 3 | 5.0698 | 17.6364 | -115.4458 | 6.0989 | 185.7911 | 0.0043 | 0.0136 |
| 2024_09_20 22:00 | 3251161 | 4 | 18.6433 | 14.1672 | -115.5914 | 7.9663 | 148.0360 | 0.0156 | 0.0024 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415674_7C4867BF | 504990 | 133 | -85.9 | 504990 | 407 | -92.4 | 504990 | 279 | -92.4 | 504990 | 315 |
| MR_1774415674_D84A9B23 | 504990 | 133 | -87.3 | 504990 | 407 | -93.4 | 504990 | 279 | -90.1 | 504990 | 315 |
| MR_1774415674_12312BA9 | 504990 | 407 | -93.4 | 504990 | 133 | -85.7 | 504990 | 279 | -88.9 | 504990 | 315 |
| MR_1774415674_C6B35AA5 | 504990 | 133 | -87.9 | 504990 | 407 | -89.8 | 504990 | 279 | -90.6 | 504990 | 315 |
| MR_1774415674_B834353E | 504990 | 133 | -88.7 | 504990 | 407 | -89.9 | 504990 | 279 | -90.0 | 504990 | 315 |
| MR_1774415674_22469CE0 | 504990 | 407 | -90.5 | 504990 | 133 | -87.1 | 504990 | 279 | -92.6 | 504990 | 315 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1389: `1b77d60a-60c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1b77d60a-60c4-4cfc-82cd-edd9a42dc97b` |
| Tag | **multiple-answer** |
| 정답 | **C2|C10|C17|C18** |
| C2 의미 | Decrease transmission power for 3262494_5 |
| C10 의미 | Press down the tilt angle  of 3262494_5 by 5 degrees |
| C17 의미 | Increase A3 Offset threshold for 3212258_1 |
| C18 의미 | Increase A3 Offset threshold for 3262494_5 |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1389] topology](images/train_1389.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212258_1
- `C2`: Decrease transmission power for 3262494_5 **← 정답**
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262494_5
- `C4`: Increase transmission power for 3212258_1
- `C5`: Adjust the azimuth of 3212258_1 by 20 degrees
- `C6`: Add neighbor relationship between 3212258_1 and 3262494_5
- `C7`: Add neighbor relationship between 3252602_3 and 3262494_5
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212258_1
- `C9`: Lift the tilt angle of 3212258_1 by 5 degrees
- `C10`: Press down the tilt angle  of 3262494_5 by 5 degrees **← 정답**
- `C11`: Lift the tilt angle  of 3262494_5 by 5 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262494_5
- `C13`: Increase transmission power for 3262494_5
- `C14`: Press down the tilt angle of 3212258_1 by 5 degrees
- `C15`: Check test server and transmission issues
- `C16`: Decrease A3 Offset threshold for 3212258_1
- `C17`: Increase A3 Offset threshold for 3212258_1 **← 정답**
- `C18`: Increase A3 Offset threshold for 3262494_5 **← 정답**
- `C19`: Adjust the azimuth of 3262494_5 by 22 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease A3 Offset threshold for 3262494_5
- `C22`: Decrease transmission power for 3212258_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.816 | MS1 | 121.4656691609 | 31.1446211976 | 928 | 504990 | -76.42 | 15.98 | 602.20 | 0.01 | 2.18 | 1594 |
| 2024-09-20 22:21:32.674 | MS1 | 121.4656707205 | 31.1446217393 | 928 | 504990 | -79.62 | 15.69 | 539.99 | 0.19 | 2.07 | 1568 |
| 2024-09-20 22:21:33.395 | MS1 | 121.4656587743 | 31.1446379499 | 928 | 504990 | -84.42 | 16.48 | 322.25 | 0.15 | 2.92 | 1582 |
| 2024-09-20 22:21:34.877 | MS1 | 121.4656751978 | 31.1446338723 | 30 | 504990 | -82.55 | 1.07 | 51.16 | 0.02 | 1.15 | 1577 |
| 2024-09-20 22:21:35.783 | MS1 | 121.4656761274 | 31.1446240721 | 30 | 504990 | -85.06 | 4.36 | 46.96 | 0.16 | 1.45 | 1565 |
| 2024-09-20 22:21:36.803 | MS1 | 121.4656658685 | 31.1446362089 | 928 | 504990 | -86.56 | 4.33 | 82.21 | 0.05 | 1.35 | 1572 |
| 2024-09-20 22:21:37.981 | MS1 | 121.4656633024 | 31.1446297583 | 928 | 504990 | -87.89 | 4.36 | 75.09 | 0.04 | 1.23 | 1566 |
| 2024-09-20 22:21:38.398 | MS1 | 121.4656737184 | 31.1446324962 | 30 | 504990 | -87.48 | 4.68 | 41.73 | 0.13 | 1.04 | 1575 |
| 2024-09-20 22:21:39.920 | MS1 | 121.4656706810 | 31.1446315427 | 30 | 504990 | -80.56 | 4.31 | 53.53 | 0.10 | 1.12 | 1562 |
| 2024-09-20 22:21:40.508 | MS1 | 121.4656584733 | 31.1446200796 | 30 | 504990 | -77.89 | 13.01 | 567.11 | 0.04 | 2.29 | 1566 |
| 2024-09-20 22:21:41.418 | MS1 | 121.4656642917 | 31.1446321550 | 30 | 504990 | -81.45 | 14.43 | 579.53 | 0.18 | 2.35 | 1578 |
| 2024-09-20 22:21:42.528 | MS1 | 121.4656723589 | 31.1446340478 | 30 | 504990 | -81.29 | 15.84 | 395.16 | 0.00 | 2.83 | 1586 |

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
| 3212258 | 1 | 121.4701019377 | 31.1477603244 | 250 | 0 | 1 | 47.7 | TDD | 928 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3215404 | 2 | 121.4681954933 | 31.1456258609 | 200 | 8 | 8 | 29.4 | TDD | 766 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3216839 | 4 | 121.4687581255 | 31.1546330909 | 27 | 6 | 10 | 35.6 | TDD | 30 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3252602 | 3 | 121.4697545979 | 31.1552876038 | 86 | 12 | 12 | 37.9 | TDD | 24 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3262494 | 5 | 121.4740054591 | 31.1486857911 | 218 | 2 | 5 | 47.4 | TDD | 31 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.102 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.117 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.262 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.262 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.941 | NREventA3 | measId:2;ServCellPCI:170;Se... |
| 2024-09-20 22:21:34.181 | NRHandoverAttempt | SourcePCI:170;SourceNR-ARFC... |
| 2024-09-20 22:21:34.215 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.228 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:34.352 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.352 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.941 | NREventA3 | measId:2;ServCellPCI:401;Se... |
| 2024-09-20 22:21:36.181 | NRHandoverAttempt | SourcePCI:401;SourceNR-ARFC... |
| 2024-09-20 22:21:36.223 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.234 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.377 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.377 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.941 | NREventA3 | measId:2;ServCellPCI:170;Se... |
| 2024-09-20 22:21:38.181 | NRHandoverAttempt | SourcePCI:170;SourceNR-ARFC... |
| 2024-09-20 22:21:38.211 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.224 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.371 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.371 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212258 | 1 | 12.3309 | 6.3390 | -116.3046 | 10.9035 | 122.1002 | 0.0062 | 0.0067 |
| 2024_09_20 22:00 | 3215404 | 2 | 10.2163 | 18.5443 | -114.5915 | 19.4151 | 123.4912 | 0.0046 | 0.0064 |
| 2024_09_20 22:00 | 3252602 | 3 | 10.0811 | 5.3448 | -117.3851 | 12.5532 | 122.4636 | 0.0078 | 0.0114 |
| 2024_09_20 22:00 | 3216839 | 4 | 18.0438 | 11.9008 | -116.3452 | 17.9098 | 194.9434 | 0.0008 | 0.0159 |
| 2024_09_20 22:00 | 3262494 | 5 | 16.3236 | 6.7634 | -114.2780 | 16.6138 | 107.4170 | 0.0048 | 0.0178 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413127_374CBC1F | 504990 | 30 | -81.9 | 504990 | 928 | -80.5 | 504990 | 31 | -91.5 | 504990 | 24 |
| MR_1774413127_ABE9372D | 504990 | 30 | -81.5 | 504990 | 928 | -81.8 | 504990 | 31 | -88.9 | 504990 | 24 |
| MR_1774413127_DFBBBD91 | 504990 | 928 | -80.9 | 504990 | 30 | -82.6 | 504990 | 31 | -89.7 | 504990 | 24 |
| MR_1774413127_EA0BAEE2 | 504990 | 928 | -83.6 | 504990 | 30 | -83.3 | 504990 | 31 | -92.1 | 504990 | 24 |
| MR_1774413127_88E8FA96 | 504990 | 928 | -82.8 | 504990 | 30 | -81.6 | 504990 | 31 | -91.1 | 504990 | 24 |
| MR_1774413127_6A3663D4 | 504990 | 30 | -83.3 | 504990 | 928 | -81.8 | 504990 | 31 | -92.2 | 504990 | 24 |
| MR_1774413127_0FE6096E | 504990 | 30 | -80.6 | 504990 | 928 | -84.2 | 504990 | 31 | -91.7 | 504990 | 24 |

> *... 2개 열 생략 (전체 14열)*

---
