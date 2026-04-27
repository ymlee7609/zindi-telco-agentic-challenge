# Track A 문제 분석 — train[360]~train[369]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[360] ~ train[369] (10개)

## 목차

1. [문제 360: `3e734610-526...`](#360) — single-answer, 정답: C3
2. [문제 361: `0332b8ff-9f9...`](#361) — single-answer, 정답: C1
3. [문제 362: `6b6ec09e-002...`](#362) — single-answer, 정답: C6
4. [문제 363: `d5b5f1d4-7bc...`](#363) — multiple-answer, 정답: C1|C16
5. [문제 364: `79fbdaa7-571...`](#364) — single-answer, 정답: C13
6. [문제 365: `5dba2223-360...`](#365) — single-answer, 정답: C12
7. [문제 366: `30e54992-82e...`](#366) — single-answer, 정답: C4
8. [문제 367: `031a9fec-2c8...`](#367) — single-answer, 정답: C22
9. [문제 368: `068940fb-765...`](#368) — multiple-answer, 정답: C2|C22
10. [문제 369: `b2f508b0-c91...`](#369) — single-answer, 정답: C15

---

### 문제 360: `3e734610-526...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3e734610-5265-449e-8ca2-0976b525cd37` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[360] topology](images/train_0360.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231457_1
- `C2`: Increase transmission power for 3231457_1
- `C3`: Check test server and transmission issues **← 정답**
- `C4`: Add neighbor relationship between 3232330_3 and 3231457_1
- `C5`: Lift the tilt angle of 3232330_3 by 10 degrees
- `C6`: Decrease transmission power for 3232330_3
- `C7`: Increase transmission power for 3232330_3
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Press down the tilt angle of 3232330_3 by 10 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232330_3
- `C11`: Press down the tilt angle  of 3231457_1 by 3 degrees
- `C12`: Decrease A3 Offset threshold for 3231457_1
- `C13`: Add neighbor relationship between 3260045_2 and 3231457_1
- `C14`: Lift the tilt angle  of 3231457_1 by 3 degrees
- `C15`: Decrease transmission power for 3231457_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232330_3
- `C17`: Increase A3 Offset threshold for 3232330_3
- `C18`: Decrease A3 Offset threshold for 3232330_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231457_1
- `C20`: Adjust the azimuth of 3231457_1 by 50 degrees
- `C21`: Adjust the azimuth of 3232330_3 by 50 degrees
- `C22`: Increase A3 Offset threshold for 3231457_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.555 | MS1 | 121.4656749821 | 31.1446342091 | 702 | 504990 | -88.34 | 15.24 | 505.12 | 0.19 | 2.43 | 1577 |
| 2024-09-20 22:21:32.937 | MS1 | 121.4656669904 | 31.1446205263 | 702 | 504990 | -86.96 | 14.11 | 485.89 | 0.08 | 2.34 | 1581 |
| 2024-09-20 22:21:33.896 | MS1 | 121.4656693102 | 31.1446181976 | 702 | 504990 | -86.48 | 15.87 | 389.07 | 0.03 | 2.00 | 1575 |
| 2024-09-20 22:21:34.636 | MS1 | 121.4656693063 | 31.1446330160 | 702 | 504990 | -90.01 | 12.83 | 65.36 | 0.01 | 2.37 | 382 |
| 2024-09-20 22:21:35.617 | MS1 | 121.4656650022 | 31.1446327574 | 702 | 504990 | -85.58 | 12.09 | 79.36 | 0.11 | 2.39 | 354 |
| 2024-09-20 22:21:36.316 | MS1 | 121.4656646741 | 31.1446229836 | 702 | 504990 | -90.54 | 15.44 | 77.11 | 0.12 | 2.09 | 448 |
| 2024-09-20 22:21:37.354 | MS1 | 121.4656703954 | 31.1446313823 | 702 | 504990 | -92.09 | 9.53 | 61.16 | 0.11 | 2.92 | 484 |
| 2024-09-20 22:21:38.633 | MS1 | 121.4656756707 | 31.1446295399 | 702 | 504990 | -92.27 | 8.40 | 49.94 | 0.12 | 2.41 | 488 |
| 2024-09-20 22:21:39.272 | MS1 | 121.4656699579 | 31.1446249567 | 702 | 504990 | -90.35 | 12.05 | 85.99 | 0.01 | 2.04 | 454 |
| 2024-09-20 22:21:40.733 | MS1 | 121.4656769932 | 31.1446243911 | 702 | 504990 | -92.38 | 8.98 | 509.62 | 0.16 | 2.02 | 1582 |
| 2024-09-20 22:21:41.935 | MS1 | 121.4656681702 | 31.1446253348 | 702 | 504990 | -93.97 | 9.42 | 528.38 | 0.09 | 2.90 | 1570 |
| 2024-09-20 22:21:42.289 | MS1 | 121.4656732221 | 31.1446326853 | 702 | 504990 | -91.53 | 10.17 | 404.83 | 0.11 | 2.31 | 1582 |

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
| 3218049 | 4 | 121.4648205234 | 31.1488508501 | 289 | 3 | 8 | 33.6 | TDD | 639 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3231457 | 1 | 121.4656832005 | 31.1505654751 | 246 | 1 | 7 | 18.3 | TDD | 864 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3232330 | 3 | 121.4687243032 | 31.1457225191 | 349 | 7 | 9 | 16.2 | TDD | 702 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3260045 | 2 | 121.4680612412 | 31.1547781574 | 144 | 7 | 7 | 36.2 | TDD | 90 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.652 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.670 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.807 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.807 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.478 | NREventA3 | measId:2;ServCellPCI:629;Se... |
| 2024-09-20 22:21:38.718 | NRHandoverAttempt | SourcePCI:629;SourceNR-ARFC... |
| 2024-09-20 22:21:38.762 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.773 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.923 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.923 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231457 | 1 | 12.3709 | 14.7205 | -115.6626 | 16.8754 | 116.5604 | 0.0027 | 0.0014 |
| 2024_09_20 22:00 | 3260045 | 2 | 11.7481 | 15.3499 | -114.9579 | 7.8250 | 163.8078 | 0.0157 | 0.0156 |
| 2024_09_20 22:00 | 3232330 | 3 | 19.5483 | 15.8950 | -115.2381 | 18.0396 | 152.9721 | 0.0151 | 0.0123 |
| 2024_09_20 22:00 | 3218049 | 4 | 11.1659 | 11.2853 | -117.5849 | 5.1816 | 192.1715 | 0.0166 | 0.0129 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412746_4FDCBA15 | 504990 | 702 | -91.3 | 504990 | 864 | -97.5 | 504990 | 90 | -102.9 | 504990 | 639 |
| MR_1774412746_19DFB86A | 504990 | 702 | -89.4 | 504990 | 864 | -100.6 | 504990 | 90 | -102.7 | 504990 | 639 |
| MR_1774412746_7FC25B4E | 504990 | 702 | -91.8 | 504990 | 864 | -99.4 | 504990 | 90 | -102.3 | 504990 | 639 |
| MR_1774412746_66398E6B | 504990 | 702 | -90.9 | 504990 | 864 | -101.0 | 504990 | 90 | -102.6 | 504990 | 639 |
| MR_1774412746_C123585D | 504990 | 702 | -90.4 | 504990 | 864 | -100.7 | 504990 | 90 | -103.9 | 504990 | 639 |
| MR_1774412746_BDE0C022 | 504990 | 702 | -88.4 | 504990 | 864 | -97.5 | 504990 | 90 | -104.1 | 504990 | 639 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 361: `0332b8ff-9f9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0332b8ff-9f9d-498b-a1cb-008a8f894cc0` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[361] topology](images/train_0361.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues **← 정답**
- `C2`: Press down the tilt angle  of 3263183_1 by 10 degrees
- `C3`: Increase transmission power for 3263183_1
- `C4`: Decrease A3 Offset threshold for 3222779_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222779_4
- `C6`: Decrease transmission power for 3263183_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222779_4
- `C8`: Increase A3 Offset threshold for 3222779_4
- `C9`: Press down the tilt angle of 3222779_4 by 10 degrees
- `C10`: Add neighbor relationship between 3222779_4 and 3263183_1
- `C11`: Decrease A3 Offset threshold for 3263183_1
- `C12`: Increase A3 Offset threshold for 3263183_1
- `C13`: Lift the tilt angle  of 3263183_1 by 10 degrees
- `C14`: Increase transmission power for 3222779_4
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Lift the tilt angle of 3222779_4 by 10 degrees
- `C17`: Adjust the azimuth of 3263183_1 by 30 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263183_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263183_1
- `C20`: Adjust the azimuth of 3222779_4 by 50 degrees
- `C21`: Decrease transmission power for 3222779_4
- `C22`: Add neighbor relationship between 3232382_2 and 3263183_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.464 | MS1 | 121.4656599936 | 31.1446351363 | 415 | 504990 | -88.64 | 12.79 | 554.26 | 0.15 | 2.92 | 1593 |
| 2024-09-20 22:21:32.839 | MS1 | 121.4656588548 | 31.1446319624 | 415 | 504990 | -90.81 | 12.65 | 497.81 | 0.19 | 2.38 | 1591 |
| 2024-09-20 22:21:33.890 | MS1 | 121.4656591774 | 31.1446276675 | 415 | 504990 | -90.22 | 17.06 | 548.01 | 0.12 | 2.98 | 1591 |
| 2024-09-20 22:21:34.681 | MS1 | 121.4656685489 | 31.1446271750 | 415 | 504990 | -91.76 | 16.80 | 94.22 | 0.12 | 2.03 | 304 |
| 2024-09-20 22:21:35.510 | MS1 | 121.4656582340 | 31.1446309052 | 415 | 504990 | -85.17 | 16.87 | 91.44 | 0.10 | 2.55 | 437 |
| 2024-09-20 22:21:36.386 | MS1 | 121.4656603802 | 31.1446349433 | 415 | 504990 | -90.66 | 14.34 | 62.19 | 0.08 | 2.92 | 461 |
| 2024-09-20 22:21:37.177 | MS1 | 121.4656670122 | 31.1446320821 | 415 | 504990 | -93.30 | 11.28 | 91.00 | 0.19 | 2.31 | 403 |
| 2024-09-20 22:21:38.448 | MS1 | 121.4656741634 | 31.1446298857 | 415 | 504990 | -93.82 | 7.27 | 75.33 | 0.18 | 2.33 | 382 |
| 2024-09-20 22:21:39.102 | MS1 | 121.4656721403 | 31.1446368879 | 415 | 504990 | -93.86 | 9.09 | 55.87 | 0.12 | 2.22 | 369 |
| 2024-09-20 22:21:40.727 | MS1 | 121.4656737992 | 31.1446297350 | 415 | 504990 | -90.00 | 10.82 | 311.60 | 0.08 | 2.76 | 1592 |
| 2024-09-20 22:21:41.970 | MS1 | 121.4656720097 | 31.1446223937 | 415 | 504990 | -89.75 | 8.32 | 536.41 | 0.02 | 2.78 | 1592 |
| 2024-09-20 22:21:42.824 | MS1 | 121.4656627915 | 31.1446222530 | 415 | 504990 | -90.01 | 10.22 | 362.24 | 0.16 | 2.11 | 1599 |

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
| 3213434 | 3 | 121.4727282790 | 31.1546630023 | 239 | 4 | 2 | 28.2 | TDD | 91 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3222779 | 4 | 121.4673422842 | 31.1499339582 | 91 | 8 | 9 | 28.9 | TDD | 415 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3232382 | 2 | 121.4727326957 | 31.1489501971 | 197 | 6 | 9 | 45.6 | TDD | 170 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3263183 | 1 | 121.4685770748 | 31.1440629419 | 253 | 7 | 2 | 18.4 | TDD | 608 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.438 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.461 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.590 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.590 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.299 | NREventA3 | measId:2;ServCellPCI:435;Se... |
| 2024-09-20 22:21:38.539 | NRHandoverAttempt | SourcePCI:435;SourceNR-ARFC... |
| 2024-09-20 22:21:38.575 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.590 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.727 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.727 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263183 | 1 | 7.2993 | 5.4396 | -117.9917 | 13.5395 | 115.9348 | 0.0013 | 0.0018 |
| 2024_09_20 22:00 | 3232382 | 2 | 19.6274 | 15.5767 | -114.3581 | 5.3820 | 128.4503 | 0.0113 | 0.0027 |
| 2024_09_20 22:00 | 3213434 | 3 | 5.9212 | 10.5603 | -117.2139 | 13.5599 | 172.3785 | 0.0030 | 0.0172 |
| 2024_09_20 22:00 | 3222779 | 4 | 15.5711 | 9.6220 | -117.2409 | 13.5024 | 181.5604 | 0.0106 | 0.0060 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415611_FD94DE32 | 504990 | 415 | -91.6 | 504990 | 608 | -96.2 | 504990 | 170 | -107.2 | 504990 | 91 |
| MR_1774415611_C5411164 | 504990 | 415 | -90.3 | 504990 | 608 | -97.4 | 504990 | 170 | -104.6 | 504990 | 91 |
| MR_1774415611_79E95D67 | 504990 | 415 | -93.4 | 504990 | 608 | -98.8 | 504990 | 170 | -105.1 | 504990 | 91 |
| MR_1774415611_194FC5DE | 504990 | 415 | -90.3 | 504990 | 608 | -96.3 | 504990 | 170 | -105.7 | 504990 | 91 |
| MR_1774415611_6E628B7E | 504990 | 415 | -90.5 | 504990 | 608 | -95.3 | 504990 | 170 | -105.6 | 504990 | 91 |
| MR_1774415611_F93930D6 | 504990 | 415 | -91.5 | 504990 | 608 | -99.0 | 504990 | 170 | -105.3 | 504990 | 91 |
| MR_1774415611_747E6A48 | 504990 | 415 | -89.8 | 504990 | 608 | -98.7 | 504990 | 170 | -104.4 | 504990 | 91 |
| MR_1774415611_1BC33794 | 504990 | 415 | -93.7 | 504990 | 608 | -98.2 | 504990 | 170 | -107.1 | 504990 | 91 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 362: `6b6ec09e-002...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6b6ec09e-002a-444f-9609-4ff9b77d4c77` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Lift the tilt angle  of 3236297_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[362] topology](images/train_0362.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3210944_3
- `C2`: Decrease transmission power for 3259307_1
- `C3`: Increase transmission power for 3259307_1
- `C4`: Check test server and transmission issues
- `C5`: Decrease transmission power for 3210944_3
- `C6`: Lift the tilt angle  of 3236297_4 by 10 degrees **← 정답**
- `C7`: Adjust the azimuth of 3259307_1 by 38 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase A3 Offset threshold for 3210944_3
- `C10`: Decrease A3 Offset threshold for 3259307_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259307_1
- `C12`: Add neighbor relationship between 3259307_1 and 3210944_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210944_3
- `C14`: Press down the tilt angle  of 3236297_4 by 10 degrees
- `C15`: Press down the tilt angle of 3259307_1 by 5 degrees
- `C16`: Lift the tilt angle of 3259307_1 by 5 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210944_3
- `C18`: Adjust the azimuth of 3236297_4 by 50 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259307_1
- `C20`: Add neighbor relationship between 3236297_4 and 3210944_3
- `C21`: Increase A3 Offset threshold for 3259307_1
- `C22`: Increase transmission power for 3210944_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.542 | MS1 | 121.4656661631 | 31.1446256070 | 552 | 504990 | -86.54 | 17.34 | 500.57 | 0.03 | 2.02 | 1567 |
| 2024-09-20 22:21:32.235 | MS1 | 121.4656607292 | 31.1446202959 | 552 | 504990 | -88.83 | 17.69 | 552.44 | 0.18 | 2.54 | 1580 |
| 2024-09-20 22:21:33.703 | MS1 | 121.4656659432 | 31.1446247282 | 552 | 504990 | -85.38 | 15.42 | 369.85 | 0.18 | 2.70 | 1561 |
| 2024-09-20 22:21:34.233 | MS1 | 121.4656657629 | 31.1446333612 | 552 | 504990 | -89.66 | 16.70 | 53.27 | 0.11 | 2.22 | 1565 |
| 2024-09-20 22:21:35.326 | MS1 | 121.4656658494 | 31.1446324027 | 552 | 504990 | -87.96 | 16.51 | 72.98 | 0.14 | 2.58 | 1574 |
| 2024-09-20 22:21:36.201 | MS1 | 121.4656693382 | 31.1446250849 | 552 | 504990 | -86.11 | 13.88 | 79.09 | 0.04 | 2.89 | 1567 |
| 2024-09-20 22:21:37.790 | MS1 | 121.4656691519 | 31.1446322614 | 552 | 504990 | -89.43 | 11.71 | 98.65 | 0.01 | 2.58 | 1585 |
| 2024-09-20 22:21:38.426 | MS1 | 121.4656609902 | 31.1446234589 | 552 | 504990 | -93.52 | 8.64 | 85.27 | 0.19 | 2.25 | 1569 |
| 2024-09-20 22:21:39.302 | MS1 | 121.4656709711 | 31.1446190600 | 552 | 504990 | -89.44 | 8.89 | 80.42 | 0.12 | 2.89 | 1599 |
| 2024-09-20 22:21:40.653 | MS1 | 121.4656691727 | 31.1446201668 | 552 | 504990 | -91.65 | 9.77 | 448.00 | 0.20 | 2.23 | 1565 |
| 2024-09-20 22:21:41.420 | MS1 | 121.4656749076 | 31.1446192002 | 552 | 504990 | -93.01 | 11.92 | 563.23 | 0.11 | 2.63 | 1582 |
| 2024-09-20 22:21:42.165 | MS1 | 121.4656631163 | 31.1446202244 | 552 | 504990 | -91.98 | 8.96 | 581.79 | 0.17 | 2.11 | 1583 |

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
| 3210944 | 3 | 121.4684513809 | 31.1525791037 | 325 | 8 | 4 | 29.7 | TDD | 699 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3235906 | 2 | 121.4651097294 | 31.1555678533 | 356 | 13 | 7 | 48.1 | TDD | 560 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3236297 | 4 | 121.4665716775 | 31.1447260594 | 195 | 10 | 2 | 49.9 | TDD | 789 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3259307 | 1 | 121.4755419506 | 31.1555616900 | 256 | 4 | 5 | 39.3 | TDD | 552 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.251 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.267 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.413 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.413 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.058 | NREventA3 | measId:2;ServCellPCI:698;Se... |
| 2024-09-20 22:21:38.298 | NRHandoverAttempt | SourcePCI:698;SourceNR-ARFC... |
| 2024-09-20 22:21:38.342 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.357 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.464 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.464 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259307 | 1 | 87.3634 | 85.3325 | -116.1967 | 13.2145 | 157.0820 | 0.0009 | 0.0198 |
| 2024_09_20 22:00 | 3235906 | 2 | 10.4775 | 15.7571 | -117.9506 | 8.9375 | 80.9141 | 0.0074 | 0.0093 |
| 2024_09_20 22:00 | 3210944 | 3 | 12.3450 | 19.8033 | -114.1540 | 11.7358 | 169.5406 | 0.0106 | 0.0052 |
| 2024_09_20 22:00 | 3236297 | 4 | 7.8715 | 19.2442 | -116.1134 | 9.3543 | 154.0810 | 0.0122 | 0.0122 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414740_4F689748 | 504990 | 552 | -89.2 | 504990 | 699 | -94.3 | 504990 | 789 | -102.5 | 504990 | 560 |
| MR_1774414740_4E7584B9 | 504990 | 552 | -90.7 | 504990 | 699 | -94.8 | 504990 | 789 | -103.1 | 504990 | 560 |
| MR_1774414740_AFB62FE8 | 504990 | 552 | -90.1 | 504990 | 699 | -97.0 | 504990 | 789 | -104.6 | 504990 | 560 |
| MR_1774414740_4752B2F1 | 504990 | 552 | -91.3 | 504990 | 699 | -96.6 | 504990 | 789 | -103.4 | 504990 | 560 |
| MR_1774414740_830C54A0 | 504990 | 552 | -90.3 | 504990 | 699 | -94.9 | 504990 | 789 | -103.3 | 504990 | 560 |
| MR_1774414740_BECBED65 | 504990 | 552 | -91.5 | 504990 | 699 | -96.3 | 504990 | 789 | -102.5 | 504990 | 560 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 363: `d5b5f1d4-7bc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d5b5f1d4-7bc0-4a37-a410-2b12361a1e9c` |
| Tag | **multiple-answer** |
| 정답 | **C1|C16** |
| C1 의미 | Adjust the azimuth of 3225607_1 by 39 degrees |
| C16 의미 | Increase transmission power for 3225607_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[363] topology](images/train_0363.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3225607_1 by 39 degrees **← 정답**
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225607_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Press down the tilt angle of 3225607_1 by 10 degrees
- `C5`: Increase transmission power for 3266207_2
- `C6`: Decrease A3 Offset threshold for 3266207_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266207_2
- `C8`: Check test server and transmission issues
- `C9`: Decrease transmission power for 3266207_2
- `C10`: Lift the tilt angle of 3225607_1 by 10 degrees
- `C11`: Decrease transmission power for 3225607_1
- `C12`: Decrease A3 Offset threshold for 3225607_1
- `C13`: Increase A3 Offset threshold for 3225607_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266207_2
- `C15`: Press down the tilt angle  of 3266207_2 by 5 degrees
- `C16`: Increase transmission power for 3225607_1 **← 정답**
- `C17`: Increase A3 Offset threshold for 3266207_2
- `C18`: Adjust the azimuth of 3266207_2 by 2 degrees
- `C19`: Add neighbor relationship between 3225607_1 and 3266207_2
- `C20`: Lift the tilt angle  of 3266207_2 by 5 degrees
- `C21`: Add neighbor relationship between 3219429_4 and 3266207_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225607_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.861 | MS1 | 121.4656686052 | 31.1446316136 | 80 | 504990 | -94.95 | 15.71 | 348.65 | 0.07 | 2.32 | 1588 |
| 2024-09-20 22:21:32.115 | MS1 | 121.4656613011 | 31.1446208111 | 80 | 504990 | -94.11 | 17.05 | 433.39 | 0.05 | 2.98 | 1565 |
| 2024-09-20 22:21:33.771 | MS1 | 121.4656773503 | 31.1446369882 | 80 | 504990 | -86.98 | 17.84 | 398.46 | 0.16 | 2.34 | 1591 |
| 2024-09-20 22:21:34.993 | MS1 | 121.4656692808 | 31.1446286241 | 80 | 504990 | -101.41 | 0.50 | 28.73 | 0.05 | 1.10 | 1586 |
| 2024-09-20 22:21:35.525 | MS1 | 121.4656692039 | 31.1446323341 | 80 | 504990 | -100.99 | -1.87 | 60.29 | 0.07 | 1.07 | 1570 |
| 2024-09-20 22:21:36.404 | MS1 | 121.4656620335 | 31.1446355430 | 80 | 504990 | -106.18 | 0.91 | 38.27 | 0.20 | 1.33 | 1574 |
| 2024-09-20 22:21:37.761 | MS1 | 121.4656627261 | 31.1446300127 | 80 | 504990 | -101.52 | -0.92 | 39.45 | 0.04 | 1.26 | 1576 |
| 2024-09-20 22:21:38.480 | MS1 | 121.4656585676 | 31.1446347109 | 80 | 504990 | -106.22 | -1.51 | 54.54 | 0.17 | 1.41 | 1574 |
| 2024-09-20 22:21:39.196 | MS1 | 121.4656685283 | 31.1446222883 | 80 | 504990 | -107.04 | -0.84 | 14.78 | 0.02 | 1.41 | 1584 |
| 2024-09-20 22:21:40.671 | MS1 | 121.4656722241 | 31.1446231477 | 80 | 504990 | -86.27 | 15.51 | 526.88 | 0.13 | 2.45 | 1597 |
| 2024-09-20 22:21:41.423 | MS1 | 121.4656718167 | 31.1446330437 | 80 | 504990 | -86.08 | 14.70 | 506.03 | 0.12 | 2.41 | 1585 |
| 2024-09-20 22:21:42.873 | MS1 | 121.4656720414 | 31.1446207463 | 80 | 504990 | -94.27 | 16.66 | 440.80 | 0.12 | 2.46 | 1600 |

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
| 3219429 | 4 | 121.4699383636 | 31.1493865194 | 194 | 10 | 10 | 40.1 | TDD | 925 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3223505 | 3 | 121.4643867364 | 31.1491279317 | 0 | 13 | 6 | 25.9 | TDD | 714 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3225607 | 1 | 121.4674701911 | 31.1458018510 | 272 | 4 | 5 | 44.2 | TDD | 80 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3266207 | 2 | 121.4652923815 | 31.1551461958 | 176 | 4 | 0 | 15.7 | TDD | 121 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.186 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.202 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.343 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.343 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.488 | NREventA2 | measId:1;ServCellPCI:128;Se... |
| 2024-09-20 22:21:34.631 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225607 | 1 | 19.9483 | 10.1088 | -114.2662 | 7.8397 | 116.0915 | 0.1625 | 0.0100 |
| 2024_09_20 22:00 | 3266207 | 2 | 10.2271 | 16.9057 | -116.1921 | 14.9795 | 179.8133 | 0.0005 | 0.0141 |
| 2024_09_20 22:00 | 3223505 | 3 | 6.1653 | 16.7521 | -117.4505 | 14.9125 | 168.7869 | 0.0153 | 0.0088 |
| 2024_09_20 22:00 | 3219429 | 4 | 6.9922 | 9.0181 | -116.4248 | 16.9169 | 193.3880 | 0.0067 | 0.0113 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413109_DAED112B | 504990 | 80 | -99.8 | 504990 | 121 | -105.5 | 504990 | 925 | -106.6 | 504990 | 714 |
| MR_1774413109_C88B9600 | 504990 | 80 | -103.0 | 504990 | 121 | -106.1 | 504990 | 925 | -105.9 | 504990 | 714 |
| MR_1774413109_265CBD20 | 504990 | 80 | -101.7 | 504990 | 121 | -103.7 | 504990 | 925 | -106.2 | 504990 | 714 |
| MR_1774413109_15B36BCA | 504990 | 80 | -100.4 | 504990 | 121 | -104.7 | 504990 | 925 | -109.1 | 504990 | 714 |
| MR_1774413109_4A517D4A | 504990 | 80 | -102.8 | 504990 | 121 | -103.2 | 504990 | 925 | -107.8 | 504990 | 714 |
| MR_1774413109_BF0A4B5E | 504990 | 80 | -101.0 | 504990 | 121 | -106.0 | 504990 | 925 | -109.8 | 504990 | 714 |
| MR_1774413109_BAD58F70 | 504990 | 80 | -99.4 | 504990 | 121 | -106.3 | 504990 | 925 | -108.1 | 504990 | 714 |
| MR_1774413109_C76E10D8 | 504990 | 80 | -103.0 | 504990 | 121 | -102.6 | 504990 | 925 | -109.7 | 504990 | 714 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 364: `79fbdaa7-571...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `79fbdaa7-571f-4b54-be3b-a70a6d0d5fa4` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[364] topology](images/train_0364.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3254036_3
- `C2`: Lift the tilt angle of 3271107_1 by 10 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271107_1
- `C4`: Increase A3 Offset threshold for 3271107_1
- `C5`: Adjust the azimuth of 3254036_3 by 50 degrees
- `C6`: Increase transmission power for 3254036_3
- `C7`: Press down the tilt angle  of 3254036_3 by 9 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254036_3
- `C9`: Adjust the azimuth of 3271107_1 by 20 degrees
- `C10`: Decrease transmission power for 3271107_1
- `C11`: Lift the tilt angle  of 3254036_3 by 9 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Check test server and transmission issues **← 정답**
- `C14`: Decrease A3 Offset threshold for 3271107_1
- `C15`: Add neighbor relationship between 3271107_1 and 3254036_3
- `C16`: Press down the tilt angle of 3271107_1 by 10 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254036_3
- `C18`: Increase A3 Offset threshold for 3254036_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271107_1
- `C20`: Add neighbor relationship between 3272590_4 and 3254036_3
- `C21`: Decrease A3 Offset threshold for 3254036_3
- `C22`: Increase transmission power for 3271107_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.660 | MS1 | 121.4656650522 | 31.1446184456 | 414 | 504990 | -91.16 | 17.91 | 537.18 | 0.09 | 2.32 | 1578 |
| 2024-09-20 22:21:32.478 | MS1 | 121.4656772590 | 31.1446236140 | 414 | 504990 | -91.39 | 14.56 | 519.37 | 0.08 | 2.28 | 1565 |
| 2024-09-20 22:21:33.586 | MS1 | 121.4656630644 | 31.1446371940 | 414 | 504990 | -87.51 | 15.87 | 599.93 | 0.09 | 2.09 | 1560 |
| 2024-09-20 22:21:34.553 | MS1 | 121.4656750910 | 31.1446290888 | 414 | 504990 | -85.80 | 14.98 | 68.69 | 0.16 | 2.13 | 482 |
| 2024-09-20 22:21:35.236 | MS1 | 121.4656583608 | 31.1446245130 | 414 | 504990 | -90.24 | 13.67 | 56.11 | 0.03 | 2.18 | 456 |
| 2024-09-20 22:21:36.158 | MS1 | 121.4656723648 | 31.1446340310 | 414 | 504990 | -90.45 | 16.33 | 101.09 | 0.13 | 2.49 | 456 |
| 2024-09-20 22:21:37.965 | MS1 | 121.4656694989 | 31.1446348667 | 414 | 504990 | -93.96 | 10.42 | 57.36 | 0.09 | 2.96 | 313 |
| 2024-09-20 22:21:38.597 | MS1 | 121.4656634748 | 31.1446237793 | 414 | 504990 | -92.20 | 9.20 | 65.41 | 0.05 | 2.68 | 351 |
| 2024-09-20 22:21:39.593 | MS1 | 121.4656719963 | 31.1446335378 | 414 | 504990 | -92.59 | 10.40 | 100.93 | 0.04 | 2.34 | 420 |
| 2024-09-20 22:21:40.166 | MS1 | 121.4656612226 | 31.1446299327 | 414 | 504990 | -93.93 | 12.20 | 488.54 | 0.18 | 2.11 | 1571 |
| 2024-09-20 22:21:41.527 | MS1 | 121.4656766310 | 31.1446274869 | 414 | 504990 | -92.88 | 9.48 | 321.81 | 0.15 | 2.63 | 1573 |
| 2024-09-20 22:21:42.267 | MS1 | 121.4656600412 | 31.1446338577 | 414 | 504990 | -92.93 | 8.80 | 569.28 | 0.17 | 2.80 | 1568 |

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
| 3222796 | 2 | 121.4704585998 | 31.1456260084 | 84 | 4 | 1 | 34.6 | TDD | 826 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3254036 | 3 | 121.4724390673 | 31.1498190967 | 130 | 8 | 9 | 15.8 | TDD | 715 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3271107 | 1 | 121.4678098947 | 31.1514018368 | 175 | 12 | 8 | 33.8 | TDD | 414 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3272590 | 4 | 121.4717029354 | 31.1491663483 | 198 | 8 | 0 | 22.9 | TDD | 166 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.195 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.212 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.343 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.343 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.075 | NREventA3 | measId:2;ServCellPCI:975;Se... |
| 2024-09-20 22:21:38.315 | NRHandoverAttempt | SourcePCI:975;SourceNR-ARFC... |
| 2024-09-20 22:21:38.358 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.372 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.503 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.503 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271107 | 1 | 7.7139 | 9.1028 | -116.7015 | 7.2866 | 137.6812 | 0.0106 | 0.0149 |
| 2024_09_20 22:00 | 3222796 | 2 | 16.9483 | 9.4927 | -117.2523 | 13.9868 | 172.8766 | 0.0032 | 0.0183 |
| 2024_09_20 22:00 | 3254036 | 3 | 7.8583 | 14.3095 | -117.4560 | 18.1263 | 153.0506 | 0.0043 | 0.0035 |
| 2024_09_20 22:00 | 3272590 | 4 | 7.6842 | 19.1044 | -115.6525 | 11.0656 | 142.0466 | 0.0118 | 0.0072 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415262_75D0556D | 504990 | 414 | -84.3 | 504990 | 715 | -92.0 | 504990 | 166 | -95.3 | 504990 | 826 |
| MR_1774415262_B74895A6 | 504990 | 414 | -85.6 | 504990 | 715 | -94.2 | 504990 | 166 | -92.6 | 504990 | 826 |
| MR_1774415262_2E0DDC72 | 504990 | 414 | -85.4 | 504990 | 715 | -91.7 | 504990 | 166 | -93.1 | 504990 | 826 |
| MR_1774415262_752752C3 | 504990 | 414 | -87.0 | 504990 | 715 | -94.4 | 504990 | 166 | -93.2 | 504990 | 826 |
| MR_1774415262_B50C15B5 | 504990 | 414 | -84.9 | 504990 | 715 | -93.1 | 504990 | 166 | -92.6 | 504990 | 826 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 365: `5dba2223-360...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5dba2223-3600-42f0-8242-e9c388542f62` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[365] topology](images/train_0365.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3239311_4
- `C2`: Press down the tilt angle  of 3239311_4 by 10 degrees
- `C3`: Increase A3 Offset threshold for 3239311_4
- `C4`: Decrease transmission power for 3239311_4
- `C5`: Adjust the azimuth of 3239311_4 by 50 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239311_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239311_4
- `C8`: Lift the tilt angle  of 3239311_4 by 10 degrees
- `C9`: Decrease transmission power for 3239891_3
- `C10`: Increase transmission power for 3239891_3
- `C11`: Lift the tilt angle of 3239891_3 by 10 degrees
- `C12`: Insufficient data; more data is needed for judgment. **← 정답**
- `C13`: Press down the tilt angle of 3239891_3 by 10 degrees
- `C14`: Increase A3 Offset threshold for 3239891_3
- `C15`: Check test server and transmission issues
- `C16`: Add neighbor relationship between 3239891_3 and 3239311_4
- `C17`: Add neighbor relationship between 3268675_1 and 3239311_4
- `C18`: Decrease A3 Offset threshold for 3239891_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239891_3
- `C20`: Adjust the azimuth of 3239891_3 by 39 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239891_3
- `C22`: Decrease A3 Offset threshold for 3239311_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.984 | MS1 | 121.4656666066 | 31.1446248746 | 251 | 504990 | -88.40 | 12.46 | 423.81 | 0.03 | 2.81 | 1564 |
| 2024-09-20 22:21:32.489 | MS1 | 121.4656750684 | 31.1446294973 | 251 | 504990 | -91.37 | 16.08 | 573.33 | 0.13 | 2.13 | 1587 |
| 2024-09-20 22:21:33.106 | MS1 | 121.4656612868 | 31.1446369291 | 251 | 504990 | -85.27 | 16.00 | 437.30 | 0.06 | 2.07 | 1562 |
| 2024-09-20 22:21:34.993 | MS1 | 121.4656706756 | 31.1446198895 | 251 | 504990 | -88.60 | 12.30 | 103.99 | 0.04 | 2.82 | 1584 |
| 2024-09-20 22:21:35.580 | MS1 | 121.4656625098 | 31.1446324903 | 251 | 504990 | -87.38 | 12.44 | 68.45 | 0.12 | 2.26 | 1579 |
| 2024-09-20 22:21:36.358 | MS1 | 121.4656776321 | 31.1446334534 | 251 | 504990 | -89.45 | 16.64 | 98.94 | 0.05 | 2.08 | 1573 |
| 2024-09-20 22:21:37.788 | MS1 | 121.4656673600 | 31.1446332837 | 251 | 504990 | -91.20 | 9.46 | 76.08 | 0.17 | 2.64 | 1591 |
| 2024-09-20 22:21:38.368 | MS1 | 121.4656623893 | 31.1446209629 | 251 | 504990 | -93.49 | 11.37 | 53.87 | 0.05 | 2.64 | 1576 |
| 2024-09-20 22:21:39.370 | MS1 | 121.4656742022 | 31.1446233847 | 251 | 504990 | -92.85 | 9.37 | 45.18 | 0.07 | 2.22 | 1596 |
| 2024-09-20 22:21:40.896 | MS1 | 121.4656601913 | 31.1446319728 | 251 | 504990 | -89.48 | 9.08 | 389.65 | 0.01 | 2.90 | 1596 |
| 2024-09-20 22:21:41.125 | MS1 | 121.4656764903 | 31.1446376165 | 251 | 504990 | -92.55 | 9.81 | 323.00 | 0.15 | 2.12 | 1570 |
| 2024-09-20 22:21:42.400 | MS1 | 121.4656603274 | 31.1446214929 | 251 | 504990 | -92.59 | 11.26 | 563.40 | 0.03 | 2.57 | 1586 |

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
| 3215278 | 2 | 121.4717112018 | 31.1535174182 | 275 | 7 | 7 | 26.1 | TDD | 138 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3239311 | 4 | 121.4647064746 | 31.1463132473 | 40 | 3 | 3 | 37.3 | TDD | 869 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3239891 | 3 | 121.4675523480 | 31.1457441884 | 274 | 10 | 7 | 23.2 | TDD | 251 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3268675 | 1 | 121.4753866314 | 31.1518799608 | 2 | 4 | 0 | 30.8 | TDD | 977 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.820 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.835 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.954 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.954 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.719 | NREventA3 | measId:2;ServCellPCI:48;Ser... |
| 2024-09-20 22:21:37.959 | NRHandoverAttempt | SourcePCI:48;SourceNR-ARFCN... |
| 2024-09-20 22:21:37.992 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.005 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.151 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.151 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3268675 | 1 | 78.9615 | 83.8746 | -116.3086 | 10.8795 | 97.1222 | 0.0175 | 0.0001 |
| 2024_09_19 22:00 | 3215278 | 2 | 90.8924 | 84.5068 | -117.3975 | 6.8189 | 151.8457 | 0.0177 | 0.0079 |
| 2024_09_19 22:00 | 3239891 | 3 | 92.9356 | 80.9311 | -116.4370 | 14.6316 | 167.4203 | 0.0055 | 0.0022 |
| 2024_09_19 22:00 | 3239311 | 4 | 81.6468 | 80.9191 | -116.0803 | 12.9382 | 100.0159 | 0.0050 | 0.0013 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412279_4109958D | 504990 | 251 | -88.8 | 504990 | 869 | -93.1 | 504990 | 977 | -98.0 | 504990 | 138 |
| MR_1774412279_2BBF2D4E | 504990 | 251 | -87.5 | 504990 | 869 | -96.2 | 504990 | 977 | -98.7 | 504990 | 138 |
| MR_1774412279_E7A57723 | 504990 | 251 | -86.5 | 504990 | 869 | -95.9 | 504990 | 977 | -98.0 | 504990 | 138 |
| MR_1774412279_1DEFE165 | 504990 | 251 | -89.3 | 504990 | 869 | -92.6 | 504990 | 977 | -98.3 | 504990 | 138 |
| MR_1774412279_3B7D0712 | 504990 | 251 | -89.2 | 504990 | 869 | -95.3 | 504990 | 977 | -98.9 | 504990 | 138 |
| MR_1774412279_5DEC93C6 | 504990 | 251 | -88.5 | 504990 | 869 | -95.5 | 504990 | 977 | -97.3 | 504990 | 138 |
| MR_1774412279_E9A41B9D | 504990 | 251 | -86.3 | 504990 | 869 | -92.4 | 504990 | 977 | -96.9 | 504990 | 138 |
| MR_1774412279_353D534A | 504990 | 251 | -89.0 | 504990 | 869 | -92.6 | 504990 | 977 | -99.5 | 504990 | 138 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 366: `30e54992-82e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `30e54992-82e7-45f1-afbe-1b96e87278fe` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244107_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[366] topology](images/train_0366.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease A3 Offset threshold for 3278134_5
- `C3`: Decrease A3 Offset threshold for 3244107_6
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244107_6 **← 정답**
- `C5`: Increase A3 Offset threshold for 3278134_5
- `C6`: Decrease transmission power for 3244107_6
- `C7`: Add neighbor relationship between 3244107_6 and 3278134_5
- `C8`: Lift the tilt angle of 3244107_6 by 3 degrees
- `C9`: Adjust the azimuth of 3244107_6 by 30 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278134_5
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278134_5
- `C12`: Press down the tilt angle of 3244107_6 by 3 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244107_6
- `C14`: Add neighbor relationship between 3264980_13 and 3278134_5
- `C15`: Increase transmission power for 3278134_5
- `C16`: Press down the tilt angle  of 3278134_5 by 2 degrees
- `C17`: Increase A3 Offset threshold for 3244107_6
- `C18`: Adjust the azimuth of 3278134_5 by 5 degrees
- `C19`: Increase transmission power for 3244107_6
- `C20`: Lift the tilt angle  of 3278134_5 by 2 degrees
- `C21`: Decrease transmission power for 3278134_5
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.737 | MS1 | 121.4656641942 | 31.1446341409 | 62 | 504990 | -93.99 | 14.38 | 499.62 | 0.13 | 2.61 | 1564 |
| 2024-09-20 22:21:32.150 | MS1 | 121.4656630572 | 31.1446263233 | 591 | 504990 | -95.17 | 9.38 | 416.05 | 0.13 | 2.14 | 1575 |
| 2024-09-20 22:21:33.797 | MS1 | 121.4656729551 | 31.1446182926 | 773 | 504990 | -95.49 | 12.58 | 398.66 | 0.19 | 2.57 | 1582 |
| 2024-09-20 22:21:34.226 | MS1 | 121.4656587027 | 31.1446331009 | 649 | 152650 | -96.74 | 2.76 | 65.28 | 0.19 | 1.50 | 934 |
| 2024-09-20 22:21:35.524 | MS1 | 121.4656651715 | 31.1446258950 | 463 | 152650 | -93.35 | 6.27 | 97.68 | 0.13 | 1.76 | 997 |
| 2024-09-20 22:21:36.329 | MS1 | 121.4656737963 | 31.1446329534 | 26 | 152650 | -95.31 | 3.09 | 95.92 | 0.08 | 1.78 | 914 |
| 2024-09-20 22:21:37.185 | MS1 | 121.4656779542 | 31.1446221127 | 625 | 152650 | -92.59 | 3.84 | 75.62 | 0.19 | 1.63 | 925 |
| 2024-09-20 22:21:38.605 | MS1 | 121.4656621930 | 31.1446331706 | 649 | 152650 | -91.11 | 7.57 | 62.97 | 0.11 | 1.84 | 969 |
| 2024-09-20 22:21:39.828 | MS1 | 121.4656751700 | 31.1446314157 | 463 | 152650 | -90.47 | 3.34 | 83.96 | 0.18 | 1.59 | 922 |
| 2024-09-20 22:21:40.192 | MS1 | 121.4656745004 | 31.1446358336 | 26 | 152650 | -88.90 | 3.88 | 66.12 | 0.04 | 2.38 | 1574 |
| 2024-09-20 22:21:41.811 | MS1 | 121.4656600316 | 31.1446281381 | 625 | 152650 | -93.77 | 3.97 | 68.79 | 0.08 | 2.60 | 1585 |
| 2024-09-20 22:21:42.766 | MS1 | 121.4656742275 | 31.1446315152 | 649 | 152650 | -96.09 | 5.06 | 66.69 | 0.02 | 2.89 | 1598 |

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
| 3210955 | 2 | 121.4663097611 | 31.1541096995 | 321 | 8 | 3 | 3.4 | TDD | 773 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3213556 | 7 | 121.4736903553 | 31.1547456021 | 117 | 8 | 1 | 17.3 | FDD | 322 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3221750 | 9 | 121.4672194344 | 31.1512778167 | 104 | 15 | 0 | 3.3 | FDD | 463 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3244107 | 6 | 121.4733111686 | 31.1504779628 | 198 | 2 | 4 | 14.2 | TDD | 62 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3250392 | 4 | 121.4688506733 | 31.1509969009 | 184 | 11 | 8 | 23.6 | TDD | 984 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3250764 | 3 | 121.4650377366 | 31.1492617586 | 245 | 15 | 5 | 24.2 | TDD | 591 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3255155 | 1 | 121.4685291972 | 31.1452296231 | 273 | 12 | 2 | 22.4 | TDD | 225 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3261476 | 11 | 121.4656353780 | 31.1452409555 | 49 | 3 | 3 | 9.5 | FDD | 754 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3264188 | 12 | 121.4657589633 | 31.1556920277 | 241 | 13 | 6 | 6.2 | FDD | 177 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3264980 | 13 | 121.4672018910 | 31.1465130572 | 194 | 5 | 4 | 23.4 | FDD | 26 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3266028 | 10 | 121.4675029852 | 31.1482173213 | 315 | 5 | 9 | 18.4 | FDD | 625 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3278134 | 5 | 121.4656967187 | 31.1500892805 | 175 | 1 | 12 | 11.5 | TDD | 986 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3278906 | 8 | 121.4754645750 | 31.1542900300 | 289 | 0 | 4 | 24.5 | FDD | 649 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |

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
| 2024-09-20 22:21:31.562 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.577 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.692 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.692 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.409 | NREventA2 | measId:1;ServCellPCI:919;Se... |
| 2024-09-20 22:21:35.548 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.760 | NREventA5 | measId:3;ServCellPCI:919;Se... |
| 2024-09-20 22:21:35.800 | NRHandoverAttempt | SourcePCI:919;SourceNR-ARFC... |
| 2024-09-20 22:21:35.824 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.834 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.953 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.953 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255155 | 1 | 11.8198 | 5.9572 | -115.3594 | 19.3534 | 188.8693 | 0.0011 | 0.0033 |
| 2024_09_20 22:00 | 3210955 | 2 | 7.4349 | 14.8670 | -117.9353 | 9.2678 | 188.3530 | 0.0123 | 0.0089 |
| 2024_09_20 22:00 | 3250764 | 3 | 7.7056 | 5.3294 | -116.4171 | 12.8777 | 165.1808 | 0.0004 | 0.0191 |
| 2024_09_20 22:00 | 3250392 | 4 | 16.9477 | 8.3793 | -116.7502 | 18.4307 | 155.5050 | 0.0161 | 0.0080 |
| 2024_09_20 22:00 | 3278134 | 5 | 7.9633 | 18.6155 | -115.2288 | 19.9889 | 180.4634 | 0.0166 | 0.0002 |
| 2024_09_20 22:00 | 3244107 | 6 | 9.7915 | 11.9325 | -116.1511 | 11.0706 | 154.2270 | 0.0099 | 0.0014 |
| 2024_09_20 22:00 | 3213556 | 7 | 5.1894 | 18.5197 | -116.3119 | 4.7823 | 51.0712 | 0.0089 | 0.0125 |
| 2024_09_20 22:00 | 3278906 | 8 | 18.8149 | 9.7660 | -117.8954 | 3.9265 | 36.9411 | 0.0178 | 0.0185 |
| 2024_09_20 22:00 | 3221750 | 9 | 9.3423 | 7.1824 | -116.8143 | 4.4653 | 57.8916 | 0.0027 | 0.0168 |
| 2024_09_20 22:00 | 3266028 | 10 | 17.5570 | 16.1428 | -115.8544 | 4.9339 | 27.8101 | 0.0080 | 0.0158 |
| 2024_09_20 22:00 | 3261476 | 11 | 12.0591 | 16.6519 | -117.0045 | 3.4494 | 22.3470 | 0.0165 | 0.0161 |
| 2024_09_20 22:00 | 3264188 | 12 | 7.4193 | 16.2436 | -116.8602 | 4.8826 | 40.4822 | 0.0150 | 0.0131 |
| 2024_09_20 22:00 | 3264980 | 13 | 12.0331 | 13.6891 | -114.0650 | 3.8111 | 36.4567 | 0.0139 | 0.0162 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413503_6AF9DD8A | 504990 | 773 | -96.9 | 504990 | 986 | -91.6 | 504990 | 225 | -100.1 | 504990 | 984 |
| MR_1774413503_09EED58F | 152650 | 649 | -97.1 | 152650 | 754 | -100.1 | 152650 | 322 | -102.7 | 152650 | 177 |
| MR_1774413503_99B042FB | 152650 | 649 | -95.2 | 152650 | 754 | -100.0 | 152650 | 322 | -104.2 | 152650 | 177 |
| MR_1774413503_354548E2 | 152650 | 649 | -97.9 | 152650 | 754 | -102.3 | 152650 | 322 | -102.0 | 152650 | 177 |
| MR_1774413503_56FC8D0C | 152650 | 649 | -98.2 | 152650 | 754 | -101.3 | 152650 | 322 | -104.8 | 152650 | 177 |
| MR_1774413503_6150A16D | 152650 | 649 | -97.0 | 152650 | 754 | -102.1 | 152650 | 322 | -101.7 | 152650 | 177 |
| MR_1774413503_BFCF4F8C | 504990 | 773 | -96.3 | 504990 | 986 | -91.6 | 504990 | 225 | -98.1 | 504990 | 984 |
| MR_1774413503_D6BA04C7 | 152650 | 649 | -95.4 | 152650 | 754 | -101.9 | 152650 | 322 | -104.9 | 152650 | 177 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 367: `031a9fec-2c8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `031a9fec-2c89-4cbe-a485-868109b6b290` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Add neighbor relationship between 3240440_1 and 3255917_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[367] topology](images/train_0367.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3255917_2 by 3 degrees
- `C2`: Decrease A3 Offset threshold for 3240440_1
- `C3`: Check test server and transmission issues
- `C4`: Adjust the azimuth of 3255917_2 by 5 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240440_1
- `C6`: Increase transmission power for 3255917_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease A3 Offset threshold for 3255917_2
- `C9`: Decrease transmission power for 3240440_1
- `C10`: Increase A3 Offset threshold for 3255917_2
- `C11`: Add neighbor relationship between 3272338_4 and 3255917_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255917_2
- `C13`: Increase A3 Offset threshold for 3240440_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255917_2
- `C15`: Increase transmission power for 3240440_1
- `C16`: Decrease transmission power for 3255917_2
- `C17`: Press down the tilt angle  of 3255917_2 by 3 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240440_1
- `C19`: Press down the tilt angle of 3240440_1 by 10 degrees
- `C20`: Lift the tilt angle of 3240440_1 by 10 degrees
- `C21`: Adjust the azimuth of 3240440_1 by 49 degrees
- `C22`: Add neighbor relationship between 3240440_1 and 3255917_2 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.138 | MS1 | 121.4656581447 | 31.1446231613 | 464 | 504990 | -75.62 | 15.11 | 527.01 | 0.20 | 2.35 | 1595 |
| 2024-09-20 22:21:32.452 | MS1 | 121.4656671394 | 31.1446207713 | 464 | 504990 | -75.35 | 14.89 | 378.47 | 0.15 | 2.80 | 1595 |
| 2024-09-20 22:21:33.286 | MS1 | 121.4656599415 | 31.1446330379 | 464 | 504990 | -75.51 | 17.89 | 359.60 | 0.09 | 2.55 | 1595 |
| 2024-09-20 22:21:34.503 | MS1 | 121.4656775116 | 31.1446240509 | 464 | 504990 | -90.99 | -2.05 | 64.14 | 0.00 | 1.48 | 1586 |
| 2024-09-20 22:21:35.752 | MS1 | 121.4656599784 | 31.1446274021 | 464 | 504990 | -90.25 | -1.54 | 49.94 | 0.13 | 1.21 | 1584 |
| 2024-09-20 22:21:36.832 | MS1 | 121.4656662911 | 31.1446276270 | 464 | 504990 | -92.58 | -2.75 | 38.92 | 0.01 | 1.09 | 1590 |
| 2024-09-20 22:21:37.962 | MS1 | 121.4656722249 | 31.1446364332 | 464 | 504990 | -90.40 | -0.71 | 62.36 | 0.12 | 1.32 | 1589 |
| 2024-09-20 22:21:38.981 | MS1 | 121.4656769362 | 31.1446235606 | 464 | 504990 | -82.76 | 14.39 | 473.88 | 0.15 | 1.44 | 1586 |
| 2024-09-20 22:21:39.148 | MS1 | 121.4656636894 | 31.1446181421 | 464 | 504990 | -81.88 | 17.46 | 450.01 | 0.19 | 1.41 | 1596 |
| 2024-09-20 22:21:40.311 | MS1 | 121.4656779538 | 31.1446217329 | 464 | 504990 | -80.78 | 14.99 | 562.33 | 0.07 | 2.32 | 1563 |
| 2024-09-20 22:21:41.879 | MS1 | 121.4656631031 | 31.1446182351 | 464 | 504990 | -84.13 | 13.72 | 468.93 | 0.02 | 2.55 | 1586 |
| 2024-09-20 22:21:42.173 | MS1 | 121.4656752318 | 31.1446247221 | 464 | 504990 | -77.70 | 16.98 | 499.00 | 0.16 | 2.17 | 1563 |

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
| 3240440 | 1 | 121.4677006838 | 31.1478738392 | 257 | 15 | 5 | 46.4 | TDD | 464 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3255917 | 2 | 121.4657204987 | 31.1529171562 | 175 | 0 | 10 | 50.0 | TDD | 229 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3262967 | 3 | 121.4719005291 | 31.1537861321 | 69 | 7 | 8 | 34.3 | TDD | 318 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3272338 | 4 | 121.4654944196 | 31.1545299174 | 71 | 6 | 12 | 21.1 | TDD | 486 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.925 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.947 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.059 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.059 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.756 | NREventA3 | measId:2;ServCellPCI:533;Se... |
| 2024-09-20 22:21:35.756 | NREventA3 | measId:2;ServCellPCI:533;Se... |
| 2024-09-20 22:21:36.756 | NREventA3 | measId:2;ServCellPCI:533;Se... |
| 2024-09-20 22:21:39.256 | NRRRCReestablishAttempt | PCI:533 |
| 2024-09-20 22:21:39.274 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.288 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.427 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.427 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240440 | 1 | 7.8853 | 17.4485 | -114.6167 | 14.1499 | 165.5854 | 0.0104 | 0.1958 |
| 2024_09_20 22:00 | 3255917 | 2 | 13.0333 | 15.8156 | -116.5331 | 8.9871 | 166.6825 | 0.0001 | 0.0107 |
| 2024_09_20 22:00 | 3262967 | 3 | 19.9675 | 13.6319 | -116.6529 | 14.7885 | 82.1257 | 0.0171 | 0.0159 |
| 2024_09_20 22:00 | 3272338 | 4 | 13.3231 | 12.6863 | -114.1552 | 17.9608 | 136.9634 | 0.0013 | 0.0173 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413697_0E83F74B | 504990 | 464 | -92.7 | 504990 | 229 | -85.4 | 504990 | 486 | -89.1 | 504990 | 318 |
| MR_1774413697_3C644B7A | 504990 | 464 | -92.6 | 504990 | 229 | -84.4 | 504990 | 486 | -90.5 | 504990 | 318 |
| MR_1774413697_CD94A73D | 504990 | 464 | -90.2 | 504990 | 229 | -87.1 | 504990 | 486 | -88.8 | 504990 | 318 |
| MR_1774413697_37FC43DB | 504990 | 229 | -86.0 | 504990 | 464 | -90.0 | 504990 | 486 | -87.6 | 504990 | 318 |
| MR_1774413697_E9D4FE5A | 504990 | 464 | -90.0 | 504990 | 229 | -84.6 | 504990 | 486 | -88.5 | 504990 | 318 |
| MR_1774413697_65555C4F | 504990 | 229 | -83.9 | 504990 | 464 | -92.0 | 504990 | 486 | -90.4 | 504990 | 318 |
| MR_1774413697_3254BCCF | 504990 | 229 | -87.7 | 504990 | 464 | -91.5 | 504990 | 486 | -90.9 | 504990 | 318 |
| MR_1774413697_06CF9FC2 | 504990 | 464 | -92.2 | 504990 | 229 | -86.2 | 504990 | 486 | -89.0 | 504990 | 318 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 368: `068940fb-765...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `068940fb-7659-4446-ab1f-c044c814e215` |
| Tag | **multiple-answer** |
| 정답 | **C2|C22** |
| C2 의미 | Increase transmission power for 3269395_2 |
| C22 의미 | Adjust the azimuth of 3269395_2 by 29 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[368] topology](images/train_0368.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3246528_1
- `C2`: Increase transmission power for 3269395_2 **← 정답**
- `C3`: Decrease A3 Offset threshold for 3269395_2
- `C4`: Decrease transmission power for 3269395_2
- `C5`: Lift the tilt angle  of 3246528_1 by 3 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase A3 Offset threshold for 3269395_2
- `C8`: Check test server and transmission issues
- `C9`: Add neighbor relationship between 3254851_4 and 3246528_1
- `C10`: Increase transmission power for 3246528_1
- `C11`: Press down the tilt angle  of 3246528_1 by 3 degrees
- `C12`: Lift the tilt angle of 3269395_2 by 10 degrees
- `C13`: Press down the tilt angle of 3269395_2 by 10 degrees
- `C14`: Increase A3 Offset threshold for 3246528_1
- `C15`: Adjust the azimuth of 3246528_1 by 15 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269395_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246528_1
- `C18`: Decrease transmission power for 3246528_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246528_1
- `C20`: Add neighbor relationship between 3269395_2 and 3246528_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269395_2
- `C22`: Adjust the azimuth of 3269395_2 by 29 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.197 | MS1 | 121.4656699013 | 31.1446279253 | 379 | 504990 | -93.11 | 16.88 | 365.92 | 0.18 | 2.34 | 1577 |
| 2024-09-20 22:21:32.343 | MS1 | 121.4656589994 | 31.1446215358 | 379 | 504990 | -93.26 | 12.28 | 564.97 | 0.17 | 2.97 | 1572 |
| 2024-09-20 22:21:33.745 | MS1 | 121.4656736922 | 31.1446327862 | 379 | 504990 | -85.81 | 16.79 | 522.95 | 0.05 | 2.95 | 1560 |
| 2024-09-20 22:21:34.883 | MS1 | 121.4656696625 | 31.1446251423 | 379 | 504990 | -103.19 | -1.84 | 60.75 | 0.12 | 1.08 | 1586 |
| 2024-09-20 22:21:35.907 | MS1 | 121.4656733127 | 31.1446305897 | 379 | 504990 | -103.66 | 1.85 | 47.61 | 0.14 | 1.11 | 1569 |
| 2024-09-20 22:21:36.104 | MS1 | 121.4656671684 | 31.1446242070 | 379 | 504990 | -108.95 | 0.33 | 56.92 | 0.06 | 1.19 | 1595 |
| 2024-09-20 22:21:37.873 | MS1 | 121.4656648895 | 31.1446261680 | 379 | 504990 | -100.71 | 1.70 | 68.74 | 0.10 | 1.46 | 1599 |
| 2024-09-20 22:21:38.720 | MS1 | 121.4656677513 | 31.1446300830 | 379 | 504990 | -104.68 | -1.78 | 43.08 | 0.10 | 1.34 | 1577 |
| 2024-09-20 22:21:39.548 | MS1 | 121.4656615582 | 31.1446366706 | 379 | 504990 | -105.96 | 1.79 | 51.72 | 0.09 | 1.45 | 1583 |
| 2024-09-20 22:21:40.779 | MS1 | 121.4656755494 | 31.1446318992 | 379 | 504990 | -87.27 | 15.19 | 354.10 | 0.10 | 2.04 | 1578 |
| 2024-09-20 22:21:41.149 | MS1 | 121.4656705281 | 31.1446210994 | 379 | 504990 | -94.90 | 17.36 | 401.25 | 0.15 | 2.85 | 1578 |
| 2024-09-20 22:21:42.228 | MS1 | 121.4656749348 | 31.1446322551 | 379 | 504990 | -86.04 | 12.71 | 567.14 | 0.14 | 2.84 | 1566 |

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
| 3246528 | 1 | 121.4663044335 | 31.1553823133 | 198 | 1 | 8 | 47.3 | TDD | 928 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3254851 | 4 | 121.4669280990 | 31.1453372628 | 68 | 14 | 0 | 27.7 | TDD | 924 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3269395 | 2 | 121.4758945125 | 31.1496113543 | 269 | 13 | 7 | 43.5 | TDD | 379 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3274784 | 3 | 121.4665224824 | 31.1466109043 | 272 | 4 | 11 | 19.2 | TDD | 299 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.857 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.872 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.013 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.013 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.228 | NREventA2 | measId:1;ServCellPCI:981;Se... |
| 2024-09-20 22:21:34.375 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246528 | 1 | 11.3467 | 11.2385 | -114.0228 | 5.6777 | 191.1699 | 0.0098 | 0.0054 |
| 2024_09_20 22:00 | 3269395 | 2 | 8.2221 | 6.3380 | -115.7477 | 8.9300 | 180.0534 | 0.1812 | 0.0013 |
| 2024_09_20 22:00 | 3274784 | 3 | 9.6060 | 12.8792 | -117.3349 | 15.4992 | 123.4382 | 0.0082 | 0.0194 |
| 2024_09_20 22:00 | 3254851 | 4 | 14.3148 | 14.4374 | -115.9943 | 19.5877 | 129.4058 | 0.0005 | 0.0121 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415019_42CE7932 | 504990 | 379 | -101.3 | 504990 | 928 | -106.9 | 504990 | 924 | -112.2 | 504990 | 299 |
| MR_1774415019_D85CA5C5 | 504990 | 379 | -101.5 | 504990 | 928 | -107.8 | 504990 | 924 | -111.8 | 504990 | 299 |
| MR_1774415019_C1DA4A16 | 504990 | 379 | -103.4 | 504990 | 928 | -108.4 | 504990 | 924 | -111.4 | 504990 | 299 |
| MR_1774415019_865273C5 | 504990 | 379 | -102.0 | 504990 | 928 | -106.3 | 504990 | 924 | -113.5 | 504990 | 299 |
| MR_1774415019_1576B6ED | 504990 | 379 | -104.3 | 504990 | 928 | -106.7 | 504990 | 924 | -113.2 | 504990 | 299 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 369: `b2f508b0-c91...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b2f508b0-c91e-46cc-b72d-225c6fbb42c9` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[369] topology](images/train_0369.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3264528_1 by 9 degrees
- `C2`: Decrease A3 Offset threshold for 3264528_1
- `C3`: Adjust the azimuth of 3264528_1 by 50 degrees
- `C4`: Increase A3 Offset threshold for 3258127_2
- `C5`: Decrease A3 Offset threshold for 3258127_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264528_1
- `C7`: Press down the tilt angle  of 3264528_1 by 9 degrees
- `C8`: Increase transmission power for 3264528_1
- `C9`: Add neighbor relationship between 3258127_2 and 3264528_1
- `C10`: Adjust the azimuth of 3258127_2 by 50 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258127_2
- `C12`: Lift the tilt angle of 3258127_2 by 9 degrees
- `C13`: Press down the tilt angle of 3258127_2 by 9 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264528_1
- `C15`: Check test server and transmission issues **← 정답**
- `C16`: Decrease transmission power for 3258127_2
- `C17`: Decrease transmission power for 3264528_1
- `C18`: Add neighbor relationship between 3236274_4 and 3264528_1
- `C19`: Increase transmission power for 3258127_2
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258127_2
- `C22`: Increase A3 Offset threshold for 3264528_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.482 | MS1 | 121.4656681485 | 31.1446297535 | 481 | 504990 | -86.38 | 12.89 | 473.50 | 0.07 | 2.70 | 1597 |
| 2024-09-20 22:21:32.670 | MS1 | 121.4656768897 | 31.1446345755 | 481 | 504990 | -88.15 | 14.75 | 464.71 | 0.07 | 2.46 | 1564 |
| 2024-09-20 22:21:33.615 | MS1 | 121.4656735860 | 31.1446257036 | 481 | 504990 | -86.87 | 15.19 | 508.95 | 0.01 | 2.94 | 1584 |
| 2024-09-20 22:21:34.980 | MS1 | 121.4656760435 | 31.1446294076 | 481 | 504990 | -85.65 | 15.98 | 53.39 | 0.18 | 2.29 | 477 |
| 2024-09-20 22:21:35.653 | MS1 | 121.4656712057 | 31.1446338447 | 481 | 504990 | -86.78 | 17.07 | 102.04 | 0.06 | 2.03 | 373 |
| 2024-09-20 22:21:36.300 | MS1 | 121.4656687395 | 31.1446295826 | 481 | 504990 | -87.27 | 12.83 | 84.82 | 0.12 | 2.60 | 304 |
| 2024-09-20 22:21:37.775 | MS1 | 121.4656593711 | 31.1446263033 | 481 | 504990 | -91.59 | 9.15 | 63.29 | 0.17 | 2.09 | 349 |
| 2024-09-20 22:21:38.270 | MS1 | 121.4656583046 | 31.1446336061 | 481 | 504990 | -92.59 | 9.01 | 97.03 | 0.02 | 2.70 | 418 |
| 2024-09-20 22:21:39.841 | MS1 | 121.4656695801 | 31.1446377343 | 481 | 504990 | -90.53 | 12.07 | 69.09 | 0.02 | 2.13 | 461 |
| 2024-09-20 22:21:40.826 | MS1 | 121.4656695231 | 31.1446274959 | 481 | 504990 | -89.57 | 7.30 | 425.61 | 0.13 | 2.41 | 1586 |
| 2024-09-20 22:21:41.725 | MS1 | 121.4656777117 | 31.1446236761 | 481 | 504990 | -92.88 | 11.49 | 436.77 | 0.06 | 2.91 | 1600 |
| 2024-09-20 22:21:42.691 | MS1 | 121.4656731295 | 31.1446265359 | 481 | 504990 | -92.99 | 9.46 | 507.71 | 0.14 | 2.17 | 1590 |

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
| 3236274 | 4 | 121.4748406489 | 31.1515669397 | 283 | 10 | 2 | 48.2 | TDD | 700 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3257540 | 3 | 121.4730062851 | 31.1476361076 | 272 | 3 | 9 | 36.1 | TDD | 161 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3258127 | 2 | 121.4732528125 | 31.1552656813 | 272 | 8 | 4 | 29.3 | TDD | 481 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3264528 | 1 | 121.4698438150 | 31.1493938815 | 100 | 6 | 2 | 40.2 | TDD | 704 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.380 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.395 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.506 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.506 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.226 | NREventA3 | measId:2;ServCellPCI:108;Se... |
| 2024-09-20 22:21:38.466 | NRHandoverAttempt | SourcePCI:108;SourceNR-ARFC... |
| 2024-09-20 22:21:38.507 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.522 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.624 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.624 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264528 | 1 | 5.5102 | 18.1933 | -114.7852 | 18.5497 | 123.4221 | 0.0006 | 0.0125 |
| 2024_09_20 22:00 | 3258127 | 2 | 18.7276 | 19.4665 | -114.6286 | 12.1882 | 164.9039 | 0.0087 | 0.0134 |
| 2024_09_20 22:00 | 3257540 | 3 | 15.5289 | 19.5971 | -114.9915 | 18.8114 | 157.4277 | 0.0191 | 0.0118 |
| 2024_09_20 22:00 | 3236274 | 4 | 12.0918 | 6.2792 | -114.1430 | 12.8837 | 132.0361 | 0.0027 | 0.0044 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416186_5FEB051F | 504990 | 481 | -86.6 | 504990 | 704 | -84.9 | 504990 | 700 | -100.1 | 504990 | 161 |
| MR_1774416186_FBC7065D | 504990 | 481 | -84.9 | 504990 | 704 | -87.3 | 504990 | 700 | -101.2 | 504990 | 161 |
| MR_1774416186_3EC0E40E | 504990 | 481 | -86.2 | 504990 | 704 | -86.3 | 504990 | 700 | -98.2 | 504990 | 161 |
| MR_1774416186_308F3D96 | 504990 | 481 | -85.3 | 504990 | 704 | -85.2 | 504990 | 700 | -99.0 | 504990 | 161 |
| MR_1774416186_5808AC4E | 504990 | 481 | -86.9 | 504990 | 704 | -86.3 | 504990 | 700 | -99.2 | 504990 | 161 |

> *... 2개 열 생략 (전체 14열)*

---
