# Track A 문제 분석 — test[390]~test[399]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[390] ~ test[399] (10개)

## 목차

1. [문제 390: `191a0f74-d6c...`](#390) — single-answer
2. [문제 391: `e49b192e-13d...`](#391) — single-answer
3. [문제 392: `8b11cbf8-f18...`](#392) — single-answer
4. [문제 393: `e9c9b2cd-239...`](#393) — single-answer
5. [문제 394: `9805b484-d8f...`](#394) — single-answer
6. [문제 395: `7f6cffd4-024...`](#395) — single-answer
7. [문제 396: `8677dcd5-2d8...`](#396) — single-answer
8. [문제 397: `625fad59-551...`](#397) — multiple-answer
9. [문제 398: `e129be25-f19...`](#398) — multiple-answer
10. [문제 399: `f9c5a2e6-858...`](#399) — single-answer

---

### 문제 390: `191a0f74-d6c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `191a0f74-d6c1-4a5e-af10-aa3685e80415` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[390] topology](images/test_0390.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease A3 Offset threshold for 3211344_2
- `C3`: Press down the tilt angle  of 3211344_2 by 1 degrees
- `C4`: Increase A3 Offset threshold for 3238735_3
- `C5`: Increase A3 Offset threshold for 3211344_2
- `C6`: Decrease transmission power for 3211344_2
- `C7`: Adjust the azimuth of 3238735_3 by 26 degrees
- `C8`: Press down the tilt angle of 3238735_3 by 5 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211344_2
- `C10`: Lift the tilt angle of 3238735_3 by 5 degrees
- `C11`: Decrease A3 Offset threshold for 3238735_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238735_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211344_2
- `C14`: Add neighbor relationship between 3275795_4 and 3211344_2
- `C15`: Decrease transmission power for 3238735_3
- `C16`: Increase transmission power for 3238735_3
- `C17`: Lift the tilt angle  of 3211344_2 by 1 degrees
- `C18`: Increase transmission power for 3211344_2
- `C19`: Adjust the azimuth of 3211344_2 by 50 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238735_3
- `C21`: Add neighbor relationship between 3238735_3 and 3211344_2
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.265 | MS1 | 121.4656683848 | 31.1446319359 | 780 | 504990 | -90.31 | 12.60 | 496.45 | 0.18 | 2.28 | 1588 |
| 2024-09-20 22:21:32.434 | MS1 | 121.4656713869 | 31.1446345595 | 780 | 504990 | -91.73 | 16.96 | 306.33 | 0.15 | 2.13 | 1578 |
| 2024-09-20 22:21:33.883 | MS1 | 121.4656746327 | 31.1446199585 | 780 | 504990 | -87.27 | 14.74 | 519.52 | 0.10 | 2.82 | 1560 |
| 2024-09-20 22:21:34.665 | MS1 | 121.4656586524 | 31.1446251988 | 780 | 504990 | -88.80 | 12.76 | 98.60 | 0.63 | 2.71 | 605 |
| 2024-09-20 22:21:35.506 | MS1 | 121.4656722314 | 31.1446270977 | 780 | 504990 | -88.42 | 16.22 | 48.84 | 0.57 | 2.70 | 562 |
| 2024-09-20 22:21:36.789 | MS1 | 121.4656589190 | 31.1446349226 | 780 | 504990 | -91.28 | 14.55 | 57.96 | 0.57 | 2.42 | 548 |
| 2024-09-20 22:21:37.463 | MS1 | 121.4656675463 | 31.1446321170 | 780 | 504990 | -92.04 | 12.73 | 81.85 | 0.61 | 2.99 | 558 |
| 2024-09-20 22:21:38.678 | MS1 | 121.4656769551 | 31.1446346383 | 780 | 504990 | -90.21 | 11.38 | 73.73 | 0.50 | 2.94 | 591 |
| 2024-09-20 22:21:39.132 | MS1 | 121.4656675520 | 31.1446235837 | 780 | 504990 | -89.80 | 7.97 | 57.02 | 0.50 | 2.87 | 613 |
| 2024-09-20 22:21:40.289 | MS1 | 121.4656723498 | 31.1446331686 | 780 | 504990 | -91.40 | 9.45 | 501.40 | 0.10 | 2.76 | 1575 |
| 2024-09-20 22:21:41.999 | MS1 | 121.4656641209 | 31.1446227949 | 780 | 504990 | -90.61 | 10.66 | 393.44 | 0.01 | 2.02 | 1578 |
| 2024-09-20 22:21:42.725 | MS1 | 121.4656671078 | 31.1446284853 | 780 | 504990 | -93.77 | 12.81 | 387.47 | 0.08 | 2.17 | 1570 |

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
| 3211344 | 2 | 121.4716301187 | 31.1558702014 | 50 | 0 | 5 | 29.2 | TDD | 57 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3212881 | 1 | 121.4640354854 | 31.1462330644 | 75 | 3 | 2 | 30.0 | TDD | 888 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3238735 | 3 | 121.4733895927 | 31.1554117254 | 237 | 4 | 2 | 21.8 | TDD | 780 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3275795 | 4 | 121.4704683977 | 31.1450453515 | 29 | 4 | 5 | 38.8 | TDD | 887 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.578 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.601 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.749 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.749 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.414 | NREventA3 | measId:2;ServCellPCI:240;Se... |
| 2024-09-20 22:21:38.654 | NRHandoverAttempt | SourcePCI:240;SourceNR-ARFC... |
| 2024-09-20 22:21:38.685 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.696 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.845 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.845 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212881 | 1 | 19.2634 | 7.7132 | -115.4611 | 19.9684 | 126.8532 | 0.0041 | 0.0126 |
| 2024_09_20 22:00 | 3211344 | 2 | 6.4720 | 19.5984 | -114.9486 | 17.6431 | 190.2850 | 0.0128 | 0.0193 |
| 2024_09_20 22:00 | 3238735 | 3 | 10.8082 | 18.8631 | -114.9480 | 19.7332 | 190.6217 | 0.0084 | 0.0119 |
| 2024_09_20 22:00 | 3275795 | 4 | 12.8869 | 14.3613 | -117.4305 | 12.1461 | 111.5850 | 0.0148 | 0.0123 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415827_AA5D3FFD | 504990 | 780 | -88.8 | 504990 | 57 | -92.2 | 504990 | 887 | -98.6 | 504990 | 888 |
| MR_1774415827_6980D987 | 504990 | 780 | -88.1 | 504990 | 57 | -93.0 | 504990 | 887 | -98.6 | 504990 | 888 |
| MR_1774415827_F0C3B16A | 504990 | 780 | -89.8 | 504990 | 57 | -92.6 | 504990 | 887 | -95.4 | 504990 | 888 |
| MR_1774415827_CD7E89FF | 504990 | 780 | -87.2 | 504990 | 57 | -92.2 | 504990 | 887 | -95.8 | 504990 | 888 |
| MR_1774415827_9B8956AB | 504990 | 780 | -90.4 | 504990 | 57 | -91.9 | 504990 | 887 | -98.9 | 504990 | 888 |
| MR_1774415827_C436A047 | 504990 | 780 | -87.8 | 504990 | 57 | -93.5 | 504990 | 887 | -96.6 | 504990 | 888 |
| MR_1774415827_A3E356FC | 504990 | 780 | -90.2 | 504990 | 57 | -89.9 | 504990 | 887 | -96.3 | 504990 | 888 |
| MR_1774415827_DAE58872 | 504990 | 780 | -88.3 | 504990 | 57 | -91.0 | 504990 | 887 | -96.7 | 504990 | 888 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 391: `e49b192e-13d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e49b192e-13df-4220-865c-cdfd37054473` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[391] topology](images/test_0391.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3261112_3
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262684_5
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262684_5
- `C5`: Check test server and transmission issues
- `C6`: Decrease transmission power for 3262684_5
- `C7`: Increase A3 Offset threshold for 3261112_3
- `C8`: Lift the tilt angle  of 3262684_5 by 1 degrees
- `C9`: Increase A3 Offset threshold for 3262684_5
- `C10`: Decrease A3 Offset threshold for 3261112_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261112_3
- `C12`: Adjust the azimuth of 3261112_3 by 44 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261112_3
- `C14`: Lift the tilt angle of 3261112_3 by 1 degrees
- `C15`: Decrease transmission power for 3261112_3
- `C16`: Add neighbor relationship between 3261112_3 and 3262684_5
- `C17`: Adjust the azimuth of 3262684_5 by 26 degrees
- `C18`: Increase transmission power for 3262684_5
- `C19`: Press down the tilt angle of 3261112_3 by 1 degrees
- `C20`: Decrease A3 Offset threshold for 3262684_5
- `C21`: Press down the tilt angle  of 3262684_5 by 1 degrees
- `C22`: Add neighbor relationship between 3229176_8 and 3262684_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.402 | MS1 | 121.4656706020 | 31.1446283016 | 5 | 504990 | -94.02 | 12.60 | 530.18 | 0.08 | 2.34 | 1586 |
| 2024-09-20 22:21:32.978 | MS1 | 121.4656713137 | 31.1446337320 | 612 | 504990 | -94.40 | 14.95 | 312.63 | 0.08 | 2.23 | 1591 |
| 2024-09-20 22:21:33.850 | MS1 | 121.4656621152 | 31.1446340157 | 666 | 504990 | -95.88 | 10.00 | 446.55 | 0.18 | 2.04 | 1593 |
| 2024-09-20 22:21:34.481 | MS1 | 121.4656622244 | 31.1446193355 | 736 | 152650 | -93.97 | 2.51 | 79.42 | 0.01 | 1.84 | 917 |
| 2024-09-20 22:21:35.447 | MS1 | 121.4656771735 | 31.1446348504 | 22 | 152650 | -94.68 | 4.75 | 58.31 | 0.20 | 1.99 | 1000 |
| 2024-09-20 22:21:36.909 | MS1 | 121.4656681956 | 31.1446215112 | 193 | 152650 | -89.31 | 7.09 | 67.29 | 0.18 | 1.56 | 900 |
| 2024-09-20 22:21:37.739 | MS1 | 121.4656641453 | 31.1446217267 | 346 | 152650 | -96.83 | 5.30 | 58.47 | 0.11 | 1.51 | 956 |
| 2024-09-20 22:21:38.480 | MS1 | 121.4656616972 | 31.1446183515 | 736 | 152650 | -87.13 | 4.47 | 70.29 | 0.04 | 1.73 | 956 |
| 2024-09-20 22:21:39.563 | MS1 | 121.4656740471 | 31.1446209636 | 22 | 152650 | -87.58 | 5.68 | 89.68 | 0.03 | 1.63 | 921 |
| 2024-09-20 22:21:40.503 | MS1 | 121.4656777178 | 31.1446311636 | 193 | 152650 | -96.63 | 5.21 | 91.26 | 0.14 | 2.59 | 1597 |
| 2024-09-20 22:21:41.567 | MS1 | 121.4656712470 | 31.1446252207 | 346 | 152650 | -90.32 | 5.15 | 80.92 | 0.14 | 2.63 | 1576 |
| 2024-09-20 22:21:42.720 | MS1 | 121.4656679374 | 31.1446366539 | 736 | 152650 | -89.34 | 2.85 | 65.19 | 0.14 | 2.80 | 1579 |

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
| 3210074 | 1 | 121.4702305582 | 31.1488149541 | 159 | 9 | 12 | 23.2 | TDD | 644 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3221666 | 12 | 121.4696627171 | 31.1522777433 | 179 | 10 | 7 | 19.5 | FDD | 729 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3226577 | 2 | 121.4686041605 | 31.1492269329 | 67 | 12 | 10 | 0.3 | TDD | 612 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3227382 | 6 | 121.4717330149 | 31.1480610336 | 161 | 4 | 11 | 11.8 | TDD | 666 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3229176 | 8 | 121.4703039282 | 31.1491489773 | 124 | 5 | 6 | 8.8 | FDD | 193 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3230719 | 11 | 121.4708288047 | 31.1541131397 | 55 | 12 | 5 | 1.1 | FDD | 22 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3236104 | 13 | 121.4710421223 | 31.1450141280 | 124 | 2 | 12 | 16.0 | FDD | 346 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3236632 | 4 | 121.4744330465 | 31.1497080562 | 92 | 6 | 3 | 16.1 | TDD | 912 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3244236 | 10 | 121.4671904452 | 31.1534444064 | 357 | 4 | 12 | 15.4 | FDD | 523 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3245828 | 9 | 121.4756559672 | 31.1507044986 | 129 | 3 | 9 | 8.8 | FDD | 683 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3261112 | 3 | 121.4725678791 | 31.1448642477 | 224 | 0 | 4 | 17.1 | TDD | 5 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3262684 | 5 | 121.4733225510 | 31.1452216762 | 239 | 1 | 4 | 2.5 | TDD | 179 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3272929 | 7 | 121.4645451597 | 31.1450602803 | 172 | 4 | 12 | 28.7 | FDD | 736 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |

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
| 2024-09-20 22:21:31.257 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.278 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.393 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.393 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.069 | NREventA2 | measId:1;ServCellPCI:302;Se... |
| 2024-09-20 22:21:35.173 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.375 | NREventA5 | measId:3;ServCellPCI:302;Se... |
| 2024-09-20 22:21:35.435 | NRHandoverAttempt | SourcePCI:302;SourceNR-ARFC... |
| 2024-09-20 22:21:35.466 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.481 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.581 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.581 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210074 | 1 | 5.5743 | 10.0218 | -117.5536 | 11.1854 | 86.3244 | 0.0050 | 0.0102 |
| 2024_09_20 22:00 | 3226577 | 2 | 13.4499 | 11.4394 | -117.1743 | 14.1800 | 117.6313 | 0.0014 | 0.0009 |
| 2024_09_20 22:00 | 3261112 | 3 | 16.4208 | 19.6189 | -116.9793 | 16.3082 | 151.0945 | 0.0098 | 0.0177 |
| 2024_09_20 22:00 | 3236632 | 4 | 14.9082 | 10.4293 | -114.8341 | 16.3862 | 178.9049 | 0.0097 | 0.0091 |
| 2024_09_20 22:00 | 3262684 | 5 | 15.6838 | 10.9190 | -117.1019 | 8.2945 | 140.1023 | 0.0177 | 0.0146 |
| 2024_09_20 22:00 | 3227382 | 6 | 13.9712 | 17.1744 | -114.1816 | 15.4756 | 193.3682 | 0.0151 | 0.0176 |
| 2024_09_20 22:00 | 3272929 | 7 | 6.3965 | 10.3941 | -116.0485 | 3.3430 | 34.8567 | 0.0070 | 0.0192 |
| 2024_09_20 22:00 | 3229176 | 8 | 19.6488 | 16.5086 | -116.5429 | 3.8910 | 56.6267 | 0.0199 | 0.0148 |
| 2024_09_20 22:00 | 3245828 | 9 | 15.8833 | 17.2652 | -117.8028 | 3.9566 | 28.1613 | 0.0196 | 0.0153 |
| 2024_09_20 22:00 | 3244236 | 10 | 17.4658 | 13.1526 | -115.7947 | 3.6180 | 26.9961 | 0.0122 | 0.0010 |
| 2024_09_20 22:00 | 3230719 | 11 | 17.4003 | 5.5969 | -115.7969 | 4.6604 | 34.9444 | 0.0175 | 0.0151 |
| 2024_09_20 22:00 | 3221666 | 12 | 7.4792 | 9.3775 | -114.1246 | 4.2229 | 59.9752 | 0.0181 | 0.0156 |
| 2024_09_20 22:00 | 3236104 | 13 | 15.1503 | 13.7343 | -115.0429 | 3.7976 | 27.1233 | 0.0183 | 0.0171 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415406_602C6BF7 | 504990 | 666 | -96.7 | 504990 | 179 | -94.8 | 504990 | 644 | -99.7 | 504990 | 912 |
| MR_1774415406_6C66BC06 | 152650 | 736 | -94.4 | 152650 | 683 | -100.4 | 152650 | 523 | -107.1 | 152650 | 729 |
| MR_1774415406_13E7B5B0 | 152650 | 736 | -92.6 | 152650 | 683 | -101.7 | 152650 | 523 | -105.0 | 152650 | 729 |
| MR_1774415406_2F8FAED3 | 504990 | 666 | -94.2 | 504990 | 179 | -92.6 | 504990 | 644 | -98.1 | 504990 | 912 |
| MR_1774415406_5344B750 | 504990 | 666 | -97.2 | 504990 | 179 | -94.3 | 504990 | 644 | -101.4 | 504990 | 912 |
| MR_1774415406_98D8C5BE | 152650 | 736 | -93.9 | 152650 | 683 | -99.3 | 152650 | 523 | -107.0 | 152650 | 729 |
| MR_1774415406_9F13ABCC | 152650 | 736 | -94.1 | 152650 | 683 | -101.7 | 152650 | 523 | -104.0 | 152650 | 729 |
| MR_1774415406_12AFF126 | 504990 | 666 | -94.7 | 504990 | 179 | -95.2 | 504990 | 644 | -99.9 | 504990 | 912 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 392: `8b11cbf8-f18...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8b11cbf8-f180-4c39-9caa-1935ee50c931` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[392] topology](images/test_0392.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3236076_1 by 4 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease transmission power for 3236076_1
- `C4`: Increase A3 Offset threshold for 3236076_1
- `C5`: Adjust the azimuth of 3236076_1 by 28 degrees
- `C6`: Decrease A3 Offset threshold for 3236076_1
- `C7`: Increase transmission power for 3276203_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276203_2
- `C9`: Add neighbor relationship between 3270639_4 and 3276203_2
- `C10`: Increase transmission power for 3236076_1
- `C11`: Lift the tilt angle  of 3270639_4 by 4 degrees
- `C12`: Decrease A3 Offset threshold for 3276203_2
- `C13`: Add neighbor relationship between 3236076_1 and 3276203_2
- `C14`: Press down the tilt angle  of 3270639_4 by 4 degrees
- `C15`: Decrease transmission power for 3276203_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236076_1
- `C17`: Increase A3 Offset threshold for 3276203_2
- `C18`: Check test server and transmission issues
- `C19`: Adjust the azimuth of 3270639_4 by 50 degrees
- `C20`: Lift the tilt angle of 3236076_1 by 4 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276203_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236076_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.389 | MS1 | 121.4656685255 | 31.1446335308 | 728 | 504990 | -85.06 | 14.97 | 332.98 | 0.19 | 2.36 | 1571 |
| 2024-09-20 22:21:32.930 | MS1 | 121.4656610739 | 31.1446280720 | 728 | 504990 | -86.80 | 14.31 | 375.18 | 0.18 | 2.26 | 1580 |
| 2024-09-20 22:21:33.957 | MS1 | 121.4656605165 | 31.1446271143 | 728 | 504990 | -90.57 | 15.77 | 347.52 | 0.10 | 2.12 | 1589 |
| 2024-09-20 22:21:34.924 | MS1 | 121.4656623858 | 31.1446226163 | 728 | 504990 | -87.28 | 17.86 | 67.41 | 0.10 | 2.13 | 1574 |
| 2024-09-20 22:21:35.857 | MS1 | 121.4656619544 | 31.1446293283 | 728 | 504990 | -89.21 | 13.35 | 78.32 | 0.02 | 2.66 | 1562 |
| 2024-09-20 22:21:36.963 | MS1 | 121.4656640069 | 31.1446326929 | 728 | 504990 | -87.39 | 15.11 | 64.85 | 0.06 | 2.28 | 1584 |
| 2024-09-20 22:21:37.878 | MS1 | 121.4656674439 | 31.1446323655 | 728 | 504990 | -89.64 | 10.37 | 44.88 | 0.20 | 2.18 | 1562 |
| 2024-09-20 22:21:38.200 | MS1 | 121.4656642182 | 31.1446227349 | 728 | 504990 | -91.72 | 8.61 | 100.31 | 0.11 | 2.51 | 1576 |
| 2024-09-20 22:21:39.395 | MS1 | 121.4656776379 | 31.1446274046 | 728 | 504990 | -91.24 | 10.17 | 91.10 | 0.18 | 2.82 | 1575 |
| 2024-09-20 22:21:40.919 | MS1 | 121.4656653677 | 31.1446350136 | 728 | 504990 | -92.60 | 7.07 | 320.06 | 0.12 | 2.16 | 1595 |
| 2024-09-20 22:21:41.924 | MS1 | 121.4656703405 | 31.1446333889 | 728 | 504990 | -90.20 | 9.42 | 412.04 | 0.07 | 2.36 | 1581 |
| 2024-09-20 22:21:42.881 | MS1 | 121.4656778144 | 31.1446269777 | 728 | 504990 | -89.29 | 8.37 | 309.27 | 0.00 | 2.24 | 1569 |

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
| 3236076 | 1 | 121.4696056258 | 31.1506294820 | 181 | 2 | 2 | 29.7 | TDD | 728 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3270639 | 4 | 121.4675658201 | 31.1497288411 | 350 | 0 | 10 | 28.8 | TDD | 968 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3276012 | 3 | 121.4678960832 | 31.1558114813 | 292 | 15 | 11 | 48.7 | TDD | 84 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3276203 | 2 | 121.4672032988 | 31.1497407585 | 285 | 0 | 8 | 41.6 | TDD | 51 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.956 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.973 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.098 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.098 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.758 | NREventA3 | measId:2;ServCellPCI:23;Ser... |
| 2024-09-20 22:21:37.998 | NRHandoverAttempt | SourcePCI:23;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.028 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.043 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.150 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.150 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236076 | 1 | 76.3366 | 85.1665 | -117.3975 | 8.5025 | 122.5137 | 0.0170 | 0.0167 |
| 2024_09_20 22:00 | 3276203 | 2 | 6.8627 | 13.4911 | -117.1793 | 5.0793 | 121.1768 | 0.0156 | 0.0039 |
| 2024_09_20 22:00 | 3276012 | 3 | 8.0479 | 10.7066 | -114.8727 | 10.6903 | 194.7152 | 0.0111 | 0.0090 |
| 2024_09_20 22:00 | 3270639 | 4 | 18.9062 | 12.0574 | -114.9669 | 17.6572 | 143.4014 | 0.0100 | 0.0182 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416020_1F54DC79 | 504990 | 728 | -86.3 | 504990 | 51 | -98.5 | 504990 | 968 | -99.6 | 504990 | 84 |
| MR_1774416020_BD27794A | 504990 | 728 | -86.7 | 504990 | 51 | -97.4 | 504990 | 968 | -102.4 | 504990 | 84 |
| MR_1774416020_FEAB0A25 | 504990 | 728 | -85.7 | 504990 | 51 | -95.8 | 504990 | 968 | -100.2 | 504990 | 84 |
| MR_1774416020_3EA0B553 | 504990 | 728 | -87.1 | 504990 | 51 | -95.6 | 504990 | 968 | -101.0 | 504990 | 84 |
| MR_1774416020_E7CF6D40 | 504990 | 728 | -85.4 | 504990 | 51 | -95.7 | 504990 | 968 | -102.9 | 504990 | 84 |
| MR_1774416020_C9D97790 | 504990 | 728 | -87.6 | 504990 | 51 | -98.8 | 504990 | 968 | -100.5 | 504990 | 84 |
| MR_1774416020_54C207A4 | 504990 | 728 | -85.9 | 504990 | 51 | -95.3 | 504990 | 968 | -99.7 | 504990 | 84 |
| MR_1774416020_9FF6FE37 | 504990 | 728 | -87.6 | 504990 | 51 | -95.7 | 504990 | 968 | -101.3 | 504990 | 84 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 393: `e9c9b2cd-239...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e9c9b2cd-239f-45e3-b69a-9309b25d12f8` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[393] topology](images/test_0393.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3276329_4
- `C2`: Check test server and transmission issues
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277136_2
- `C4`: Increase A3 Offset threshold for 3277136_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276329_4
- `C6`: Press down the tilt angle of 3276329_4 by 10 degrees
- `C7`: Increase transmission power for 3276329_4
- `C8`: Press down the tilt angle  of 3277136_2 by 10 degrees
- `C9`: Decrease A3 Offset threshold for 3276329_4
- `C10`: Lift the tilt angle  of 3277136_2 by 10 degrees
- `C11`: Increase A3 Offset threshold for 3276329_4
- `C12`: Adjust the azimuth of 3276329_4 by 50 degrees
- `C13`: Lift the tilt angle of 3276329_4 by 10 degrees
- `C14`: Increase transmission power for 3277136_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276329_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277136_2
- `C17`: Adjust the azimuth of 3277136_2 by 33 degrees
- `C18`: Add neighbor relationship between 3276329_4 and 3277136_2
- `C19`: Add neighbor relationship between 3221543_1 and 3277136_2
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease A3 Offset threshold for 3277136_2
- `C22`: Decrease transmission power for 3277136_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.816 | MS1 | 121.4656706726 | 31.1446319664 | 727 | 504990 | -87.61 | 12.03 | 384.47 | 0.10 | 2.19 | 1570 |
| 2024-09-20 22:21:32.334 | MS1 | 121.4656645915 | 31.1446285029 | 727 | 504990 | -87.44 | 17.84 | 311.98 | 0.10 | 2.07 | 1570 |
| 2024-09-20 22:21:33.799 | MS1 | 121.4656748400 | 31.1446310055 | 727 | 504990 | -85.11 | 15.57 | 550.14 | 0.20 | 2.13 | 1565 |
| 2024-09-20 22:21:34.872 | MS1 | 121.4656640231 | 31.1446315656 | 727 | 504990 | -91.63 | 17.08 | 92.28 | 0.02 | 2.44 | 371 |
| 2024-09-20 22:21:35.192 | MS1 | 121.4656637165 | 31.1446189213 | 727 | 504990 | -91.81 | 17.31 | 67.10 | 0.14 | 2.53 | 399 |
| 2024-09-20 22:21:36.732 | MS1 | 121.4656754750 | 31.1446208525 | 727 | 504990 | -91.20 | 15.44 | 99.93 | 0.09 | 2.08 | 418 |
| 2024-09-20 22:21:37.499 | MS1 | 121.4656694105 | 31.1446256178 | 727 | 504990 | -92.00 | 10.62 | 56.52 | 0.14 | 2.17 | 379 |
| 2024-09-20 22:21:38.281 | MS1 | 121.4656672062 | 31.1446362997 | 727 | 504990 | -90.30 | 7.05 | 82.06 | 0.19 | 2.30 | 369 |
| 2024-09-20 22:21:39.127 | MS1 | 121.4656612143 | 31.1446231174 | 727 | 504990 | -89.65 | 10.95 | 56.82 | 0.04 | 2.35 | 388 |
| 2024-09-20 22:21:40.615 | MS1 | 121.4656706517 | 31.1446334106 | 727 | 504990 | -90.35 | 12.82 | 427.03 | 0.20 | 2.03 | 1589 |
| 2024-09-20 22:21:41.507 | MS1 | 121.4656643369 | 31.1446261311 | 727 | 504990 | -90.32 | 9.86 | 345.06 | 0.14 | 2.29 | 1582 |
| 2024-09-20 22:21:42.321 | MS1 | 121.4656645916 | 31.1446309853 | 727 | 504990 | -93.21 | 12.55 | 395.06 | 0.13 | 2.24 | 1579 |

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
| 3213705 | 3 | 121.4731242214 | 31.1495306004 | 251 | 9 | 7 | 35.8 | TDD | 480 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3221543 | 1 | 121.4671369683 | 31.1449456916 | 202 | 11 | 5 | 41.7 | TDD | 496 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3276329 | 4 | 121.4641583887 | 31.1457984003 | 192 | 13 | 5 | 41.0 | TDD | 727 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3277136 | 2 | 121.4680128354 | 31.1551506162 | 158 | 13 | 2 | 46.9 | TDD | 977 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.585 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.609 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.739 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.739 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.411 | NREventA3 | measId:2;ServCellPCI:268;Se... |
| 2024-09-20 22:21:38.651 | NRHandoverAttempt | SourcePCI:268;SourceNR-ARFC... |
| 2024-09-20 22:21:38.693 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.707 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.837 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.837 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221543 | 1 | 6.7367 | 19.2350 | -115.8004 | 13.7258 | 142.0367 | 0.0128 | 0.0111 |
| 2024_09_20 22:00 | 3277136 | 2 | 12.8000 | 5.3325 | -114.2214 | 12.1555 | 80.1957 | 0.0004 | 0.0076 |
| 2024_09_20 22:00 | 3213705 | 3 | 13.1697 | 14.1864 | -117.0397 | 13.3144 | 165.8632 | 0.0120 | 0.0097 |
| 2024_09_20 22:00 | 3276329 | 4 | 11.9643 | 14.4949 | -116.6704 | 9.8547 | 177.5140 | 0.0137 | 0.0101 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413791_0FC21A48 | 504990 | 727 | -92.9 | 504990 | 977 | -97.1 | 504990 | 496 | -102.7 | 504990 | 480 |
| MR_1774413791_5E7F6BFF | 504990 | 727 | -90.5 | 504990 | 977 | -99.2 | 504990 | 496 | -105.0 | 504990 | 480 |
| MR_1774413791_314AC83E | 504990 | 727 | -90.2 | 504990 | 977 | -97.1 | 504990 | 496 | -103.6 | 504990 | 480 |
| MR_1774413791_ED0A5BFC | 504990 | 727 | -93.1 | 504990 | 977 | -96.0 | 504990 | 496 | -103.7 | 504990 | 480 |
| MR_1774413791_B2877B47 | 504990 | 727 | -89.6 | 504990 | 977 | -98.1 | 504990 | 496 | -104.0 | 504990 | 480 |
| MR_1774413791_8CD44222 | 504990 | 727 | -90.6 | 504990 | 977 | -98.0 | 504990 | 496 | -105.4 | 504990 | 480 |
| MR_1774413791_15B208AA | 504990 | 727 | -90.4 | 504990 | 977 | -95.9 | 504990 | 496 | -105.0 | 504990 | 480 |
| MR_1774413791_5D556B97 | 504990 | 727 | -92.1 | 504990 | 977 | -98.7 | 504990 | 496 | -105.3 | 504990 | 480 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 394: `9805b484-d8f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9805b484-d8fc-4e12-9aec-074849e9fe0e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[394] topology](images/test_0394.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218258_1
- `C2`: Increase A3 Offset threshold for 3218258_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218258_1
- `C4`: Press down the tilt angle  of 3267921_2 by 10 degrees
- `C5`: Decrease transmission power for 3218258_1
- `C6`: Check test server and transmission issues
- `C7`: Press down the tilt angle of 3218258_1 by 10 degrees
- `C8`: Increase transmission power for 3267921_2
- `C9`: Decrease transmission power for 3267921_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267921_2
- `C12`: Adjust the azimuth of 3267921_2 by 50 degrees
- `C13`: Add neighbor relationship between 3268834_3 and 3267921_2
- `C14`: Adjust the azimuth of 3218258_1 by 50 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267921_2
- `C16`: Increase A3 Offset threshold for 3267921_2
- `C17`: Lift the tilt angle of 3218258_1 by 10 degrees
- `C18`: Lift the tilt angle  of 3267921_2 by 10 degrees
- `C19`: Increase transmission power for 3218258_1
- `C20`: Decrease A3 Offset threshold for 3267921_2
- `C21`: Add neighbor relationship between 3218258_1 and 3267921_2
- `C22`: Decrease A3 Offset threshold for 3218258_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.664 | MS1 | 121.4656633473 | 31.1446246916 | 745 | 504990 | -83.79 | 14.80 | 408.22 | 0.13 | 2.91 | 1585 |
| 2024-09-20 22:21:32.889 | MS1 | 121.4656714371 | 31.1446289654 | 745 | 504990 | -77.37 | 16.79 | 317.62 | 0.16 | 2.75 | 1566 |
| 2024-09-20 22:21:33.501 | MS1 | 121.4656758718 | 31.1446335198 | 745 | 504990 | -80.91 | 16.50 | 474.18 | 0.00 | 2.14 | 1599 |
| 2024-09-20 22:21:34.753 | MS1 | 121.4656746381 | 31.1446298020 | 745 | 504990 | -87.88 | -3.20 | 72.04 | 0.18 | 1.44 | 1593 |
| 2024-09-20 22:21:35.660 | MS1 | 121.4656739367 | 31.1446251396 | 745 | 504990 | -86.57 | -1.48 | 56.64 | 0.02 | 1.03 | 1570 |
| 2024-09-20 22:21:36.383 | MS1 | 121.4656729569 | 31.1446223664 | 745 | 504990 | -90.48 | -0.02 | 47.86 | 0.02 | 1.11 | 1580 |
| 2024-09-20 22:21:37.552 | MS1 | 121.4656632646 | 31.1446308206 | 745 | 504990 | -84.28 | -1.18 | 66.50 | 0.10 | 1.19 | 1595 |
| 2024-09-20 22:21:38.181 | MS1 | 121.4656628185 | 31.1446309772 | 745 | 504990 | -84.18 | -2.12 | 75.74 | 0.10 | 1.41 | 1565 |
| 2024-09-20 22:21:39.707 | MS1 | 121.4656704716 | 31.1446270732 | 435 | 504990 | -82.62 | 13.64 | 178.39 | 0.12 | 1.34 | 1585 |
| 2024-09-20 22:21:40.496 | MS1 | 121.4656699415 | 31.1446320545 | 435 | 504990 | -82.31 | 12.14 | 400.75 | 0.04 | 2.67 | 1565 |
| 2024-09-20 22:21:41.212 | MS1 | 121.4656751723 | 31.1446254407 | 435 | 504990 | -80.32 | 12.77 | 475.80 | 0.14 | 2.74 | 1563 |
| 2024-09-20 22:21:42.484 | MS1 | 121.4656720713 | 31.1446187866 | 435 | 504990 | -84.93 | 16.39 | 372.71 | 0.15 | 2.09 | 1595 |

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
| 3218258 | 1 | 121.4716063760 | 31.1507828207 | 39 | 12 | 0 | 31.4 | TDD | 745 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3267921 | 2 | 121.4675650219 | 31.1490566280 | 69 | 7 | 2 | 37.3 | TDD | 435 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3268834 | 3 | 121.4746287103 | 31.1525617221 | 33 | 0 | 7 | 23.4 | TDD | 219 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3273519 | 4 | 121.4685594003 | 31.1539597213 | 268 | 14 | 9 | 40.0 | TDD | 739 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.442 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.467 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.582 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.582 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.264 | NREventA3 | measId:2;ServCellPCI:57;Ser... |
| 2024-09-20 22:21:38.504 | NRHandoverAttempt | SourcePCI:57;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.537 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.552 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.655 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.655 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218258 | 1 | 19.9483 | 16.0134 | -114.4226 | 14.8035 | 152.6357 | 0.0156 | 0.1390 |
| 2024_09_20 22:00 | 3267921 | 2 | 10.1292 | 15.9348 | -116.2642 | 5.8381 | 124.0590 | 0.0008 | 0.0195 |
| 2024_09_20 22:00 | 3268834 | 3 | 18.7645 | 17.4903 | -116.9209 | 11.4500 | 164.0649 | 0.0084 | 0.0126 |
| 2024_09_20 22:00 | 3273519 | 4 | 16.5401 | 9.8076 | -117.9974 | 10.2374 | 143.4668 | 0.0083 | 0.0155 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416772_B01E195C | 504990 | 745 | -88.4 | 504990 | 435 | -84.3 | 504990 | 219 | -82.6 | 504990 | 739 |
| MR_1774416772_87933C58 | 504990 | 435 | -81.2 | 504990 | 745 | -86.3 | 504990 | 219 | -83.6 | 504990 | 739 |
| MR_1774416772_641CEC11 | 504990 | 745 | -86.7 | 504990 | 435 | -84.2 | 504990 | 219 | -83.8 | 504990 | 739 |
| MR_1774416772_6E9141AF | 504990 | 435 | -84.2 | 504990 | 745 | -87.1 | 504990 | 219 | -84.8 | 504990 | 739 |
| MR_1774416772_308A756D | 504990 | 745 | -87.9 | 504990 | 435 | -83.3 | 504990 | 219 | -83.0 | 504990 | 739 |
| MR_1774416772_11798848 | 504990 | 745 | -89.6 | 504990 | 435 | -81.0 | 504990 | 219 | -84.9 | 504990 | 739 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 395: `7f6cffd4-024...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7f6cffd4-024e-4d9e-a863-2389400b369e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[395] topology](images/test_0395.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Lift the tilt angle of 3219975_3 by 8 degrees
- `C3`: Adjust the azimuth of 3219975_3 by 50 degrees
- `C4`: Check test server and transmission issues
- `C5`: Increase A3 Offset threshold for 3218755_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218755_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218755_4
- `C8`: Increase transmission power for 3219975_3
- `C9`: Lift the tilt angle  of 3218755_4 by 2 degrees
- `C10`: Increase transmission power for 3218755_4
- `C11`: Decrease A3 Offset threshold for 3219975_3
- `C12`: Decrease transmission power for 3219975_3
- `C13`: Press down the tilt angle of 3219975_3 by 8 degrees
- `C14`: Decrease A3 Offset threshold for 3218755_4
- `C15`: Adjust the azimuth of 3218755_4 by 50 degrees
- `C16`: Decrease transmission power for 3218755_4
- `C17`: Increase A3 Offset threshold for 3219975_3
- `C18`: Press down the tilt angle  of 3218755_4 by 2 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219975_3
- `C20`: Add neighbor relationship between 3252012_1 and 3218755_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219975_3
- `C22`: Add neighbor relationship between 3219975_3 and 3218755_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.244 | MS1 | 121.4656622961 | 31.1446344601 | 493 | 504990 | -80.53 | 15.62 | 383.28 | 0.14 | 2.51 | 1595 |
| 2024-09-20 22:21:32.637 | MS1 | 121.4656779119 | 31.1446195045 | 493 | 504990 | -83.80 | 15.46 | 519.91 | 0.11 | 2.24 | 1593 |
| 2024-09-20 22:21:33.846 | MS1 | 121.4656606632 | 31.1446352918 | 493 | 504990 | -77.84 | 16.67 | 586.54 | 0.05 | 2.73 | 1595 |
| 2024-09-20 22:21:34.230 | MS1 | 121.4656736146 | 31.1446376285 | 493 | 504990 | -91.96 | -0.38 | 41.30 | 0.16 | 1.33 | 1579 |
| 2024-09-20 22:21:35.194 | MS1 | 121.4656756574 | 31.1446199907 | 493 | 504990 | -84.12 | -0.11 | 55.91 | 0.11 | 1.29 | 1582 |
| 2024-09-20 22:21:36.649 | MS1 | 121.4656602003 | 31.1446359256 | 493 | 504990 | -83.02 | -1.48 | 69.13 | 0.01 | 1.47 | 1599 |
| 2024-09-20 22:21:37.335 | MS1 | 121.4656649849 | 31.1446355431 | 493 | 504990 | -86.14 | -0.04 | 45.80 | 0.03 | 1.30 | 1590 |
| 2024-09-20 22:21:38.853 | MS1 | 121.4656685836 | 31.1446345630 | 493 | 504990 | -88.74 | -2.03 | 58.32 | 0.05 | 1.20 | 1585 |
| 2024-09-20 22:21:39.631 | MS1 | 121.4656645755 | 31.1446292528 | 750 | 504990 | -77.66 | 13.46 | 194.80 | 0.09 | 1.17 | 1587 |
| 2024-09-20 22:21:40.560 | MS1 | 121.4656726821 | 31.1446225258 | 750 | 504990 | -80.48 | 17.42 | 470.21 | 0.02 | 2.21 | 1598 |
| 2024-09-20 22:21:41.407 | MS1 | 121.4656749713 | 31.1446293598 | 750 | 504990 | -80.56 | 13.65 | 383.11 | 0.14 | 2.72 | 1589 |
| 2024-09-20 22:21:42.923 | MS1 | 121.4656641581 | 31.1446286317 | 750 | 504990 | -75.25 | 17.19 | 342.63 | 0.13 | 2.92 | 1589 |

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
| 3218755 | 4 | 121.4708955448 | 31.1537963791 | 335 | 1 | 5 | 16.4 | TDD | 750 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3219975 | 3 | 121.4713333656 | 31.1546089840 | 324 | 6 | 0 | 39.9 | TDD | 493 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3223978 | 2 | 121.4693783266 | 31.1474752102 | 34 | 12 | 11 | 44.3 | TDD | 218 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3252012 | 1 | 121.4669690586 | 31.1444361947 | 222 | 9 | 11 | 26.0 | TDD | 824 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.047 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.064 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.206 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.206 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.863 | NREventA3 | measId:2;ServCellPCI:736;Se... |
| 2024-09-20 22:21:38.103 | NRHandoverAttempt | SourcePCI:736;SourceNR-ARFC... |
| 2024-09-20 22:21:38.133 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.145 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.282 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.282 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252012 | 1 | 14.6903 | 12.8700 | -117.5179 | 17.7178 | 94.9562 | 0.0047 | 0.0091 |
| 2024_09_20 22:00 | 3223978 | 2 | 6.1304 | 8.2402 | -116.3827 | 13.2021 | 165.4568 | 0.0022 | 0.0068 |
| 2024_09_20 22:00 | 3219975 | 3 | 12.4554 | 16.7022 | -117.2164 | 9.0955 | 179.1326 | 0.0159 | 0.1480 |
| 2024_09_20 22:00 | 3218755 | 4 | 6.7090 | 14.3147 | -116.7495 | 12.8162 | 151.3458 | 0.0136 | 0.0187 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417127_BD8312F1 | 504990 | 750 | -87.9 | 504990 | 493 | -92.5 | 504990 | 824 | -87.2 | 504990 | 218 |
| MR_1774417127_7567A7EB | 504990 | 750 | -87.9 | 504990 | 493 | -90.8 | 504990 | 824 | -90.0 | 504990 | 218 |
| MR_1774417127_171E00F4 | 504990 | 493 | -90.1 | 504990 | 750 | -84.8 | 504990 | 824 | -88.9 | 504990 | 218 |
| MR_1774417127_35D1F213 | 504990 | 493 | -91.6 | 504990 | 750 | -86.2 | 504990 | 824 | -88.0 | 504990 | 218 |
| MR_1774417127_13E5FFCF | 504990 | 750 | -84.8 | 504990 | 493 | -92.2 | 504990 | 824 | -90.4 | 504990 | 218 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 396: `8677dcd5-2d8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8677dcd5-2d84-463d-84c4-bce004387d51` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[396] topology](images/test_0396.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3267676_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211317_1
- `C3`: Press down the tilt angle  of 3211317_1 by 7 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Increase A3 Offset threshold for 3211317_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267676_2
- `C7`: Lift the tilt angle  of 3211317_1 by 7 degrees
- `C8`: Add neighbor relationship between 3267676_2 and 3211317_1
- `C9`: Decrease A3 Offset threshold for 3267676_2
- `C10`: Adjust the azimuth of 3211317_1 by 50 degrees
- `C11`: Decrease transmission power for 3211317_1
- `C12`: Increase transmission power for 3211317_1
- `C13`: Press down the tilt angle of 3267676_2 by 1 degrees
- `C14`: Increase A3 Offset threshold for 3267676_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211317_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267676_2
- `C17`: Decrease A3 Offset threshold for 3211317_1
- `C18`: Adjust the azimuth of 3267676_2 by 25 degrees
- `C19`: Decrease transmission power for 3267676_2
- `C20`: Add neighbor relationship between 3221516_4 and 3211317_1
- `C21`: Lift the tilt angle of 3267676_2 by 1 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.690 | MS1 | 121.4656747318 | 31.1446221816 | 522 | 504990 | -90.97 | 15.29 | 296.15 | 0.13 | 2.97 | 1569 |
| 2024-09-20 22:21:32.955 | MS1 | 121.4656610618 | 31.1446378337 | 522 | 504990 | -87.55 | 17.08 | 557.66 | 0.09 | 2.42 | 1575 |
| 2024-09-20 22:21:33.893 | MS1 | 121.4656679584 | 31.1446287068 | 522 | 504990 | -91.29 | 17.93 | 508.58 | 0.03 | 2.63 | 1591 |
| 2024-09-20 22:21:34.233 | MS1 | 121.4656613106 | 31.1446378080 | 522 | 504990 | -87.92 | 13.32 | 95.61 | 0.66 | 2.79 | 585 |
| 2024-09-20 22:21:35.434 | MS1 | 121.4656762547 | 31.1446244309 | 522 | 504990 | -90.53 | 12.58 | 83.32 | 0.63 | 2.32 | 619 |
| 2024-09-20 22:21:36.740 | MS1 | 121.4656677754 | 31.1446357165 | 522 | 504990 | -86.42 | 16.09 | 71.55 | 0.65 | 2.76 | 544 |
| 2024-09-20 22:21:37.164 | MS1 | 121.4656636968 | 31.1446286669 | 522 | 504990 | -91.76 | 12.78 | 44.63 | 0.57 | 2.95 | 619 |
| 2024-09-20 22:21:38.258 | MS1 | 121.4656627481 | 31.1446203643 | 522 | 504990 | -93.44 | 10.32 | 62.24 | 0.55 | 2.01 | 575 |
| 2024-09-20 22:21:39.803 | MS1 | 121.4656769148 | 31.1446208277 | 522 | 504990 | -90.35 | 7.52 | 47.93 | 0.70 | 2.27 | 679 |
| 2024-09-20 22:21:40.683 | MS1 | 121.4656587166 | 31.1446350254 | 522 | 504990 | -90.81 | 12.01 | 364.49 | 0.01 | 2.56 | 1576 |
| 2024-09-20 22:21:41.503 | MS1 | 121.4656678371 | 31.1446333479 | 522 | 504990 | -93.31 | 9.86 | 311.62 | 0.17 | 2.42 | 1598 |
| 2024-09-20 22:21:42.199 | MS1 | 121.4656671582 | 31.1446302940 | 522 | 504990 | -89.61 | 8.21 | 581.99 | 0.13 | 2.00 | 1595 |

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
| 3211317 | 1 | 121.4730297945 | 31.1513919585 | 31 | 5 | 7 | 31.2 | TDD | 904 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3221516 | 4 | 121.4697224829 | 31.1501776795 | 47 | 14 | 8 | 28.0 | TDD | 959 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3236300 | 3 | 121.4700318359 | 31.1512955570 | 294 | 9 | 1 | 21.5 | TDD | 74 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3267676 | 2 | 121.4736857106 | 31.1539453514 | 241 | 0 | 2 | 29.2 | TDD | 522 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.823 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.846 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.985 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.985 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.659 | NREventA3 | measId:2;ServCellPCI:766;Se... |
| 2024-09-20 22:21:37.899 | NRHandoverAttempt | SourcePCI:766;SourceNR-ARFC... |
| 2024-09-20 22:21:37.943 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.955 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.066 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.066 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211317 | 1 | 12.1050 | 6.2537 | -114.8594 | 13.7666 | 85.0961 | 0.0014 | 0.0146 |
| 2024_09_20 22:00 | 3267676 | 2 | 14.8006 | 19.5947 | -114.4150 | 17.7169 | 173.5370 | 0.0186 | 0.0103 |
| 2024_09_20 22:00 | 3236300 | 3 | 5.6982 | 5.8039 | -116.2717 | 18.8837 | 98.1295 | 0.0093 | 0.0025 |
| 2024_09_20 22:00 | 3221516 | 4 | 14.6229 | 13.0864 | -117.9459 | 10.5789 | 94.3214 | 0.0190 | 0.0190 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412935_AE533D8E | 504990 | 522 | -88.0 | 504990 | 904 | -93.9 | 504990 | 959 | -99.7 | 504990 | 74 |
| MR_1774412935_70235D29 | 504990 | 522 | -86.6 | 504990 | 904 | -92.7 | 504990 | 959 | -100.3 | 504990 | 74 |
| MR_1774412935_23C46874 | 504990 | 522 | -87.5 | 504990 | 904 | -94.9 | 504990 | 959 | -101.8 | 504990 | 74 |
| MR_1774412935_0493064C | 504990 | 522 | -87.9 | 504990 | 904 | -96.2 | 504990 | 959 | -98.8 | 504990 | 74 |
| MR_1774412935_5B8566AD | 504990 | 522 | -86.1 | 504990 | 904 | -95.2 | 504990 | 959 | -101.3 | 504990 | 74 |
| MR_1774412935_8C0A31BB | 504990 | 522 | -86.3 | 504990 | 904 | -92.5 | 504990 | 959 | -98.1 | 504990 | 74 |
| MR_1774412935_2D1A38FC | 504990 | 522 | -87.2 | 504990 | 904 | -95.7 | 504990 | 959 | -99.1 | 504990 | 74 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 397: `625fad59-551...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `625fad59-5511-4898-a533-b7d6c419d505` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[397] topology](images/test_0397.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3279805_2 and 3272995_1
- `C2`: Press down the tilt angle  of 3272995_1 by 4 degrees
- `C3`: Decrease transmission power for 3279805_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Lift the tilt angle  of 3272995_1 by 4 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272995_1
- `C7`: Decrease transmission power for 3272995_1
- `C8`: Increase transmission power for 3279805_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279805_2
- `C10`: Increase transmission power for 3272995_1
- `C11`: Lift the tilt angle of 3279805_2 by 10 degrees
- `C12`: Add neighbor relationship between 3249927_3 and 3272995_1
- `C13`: Increase A3 Offset threshold for 3272995_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279805_2
- `C15`: Adjust the azimuth of 3279805_2 by 50 degrees
- `C16`: Decrease A3 Offset threshold for 3272995_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272995_1
- `C18`: Check test server and transmission issues
- `C19`: Press down the tilt angle of 3279805_2 by 10 degrees
- `C20`: Adjust the azimuth of 3272995_1 by 42 degrees
- `C21`: Decrease A3 Offset threshold for 3279805_2
- `C22`: Increase A3 Offset threshold for 3279805_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.320 | MS1 | 121.4656686172 | 31.1446285388 | 916 | 504990 | -89.95 | 15.34 | 516.24 | 0.03 | 2.50 | 1594 |
| 2024-09-20 22:21:32.256 | MS1 | 121.4656665314 | 31.1446203669 | 916 | 504990 | -94.25 | 16.92 | 569.39 | 0.19 | 2.52 | 1582 |
| 2024-09-20 22:21:33.417 | MS1 | 121.4656741245 | 31.1446246232 | 916 | 504990 | -89.83 | 16.17 | 577.04 | 0.06 | 2.55 | 1597 |
| 2024-09-20 22:21:34.747 | MS1 | 121.4656768622 | 31.1446329169 | 916 | 504990 | -104.53 | 0.51 | 33.16 | 0.11 | 1.48 | 1576 |
| 2024-09-20 22:21:35.751 | MS1 | 121.4656733038 | 31.1446271631 | 916 | 504990 | -107.46 | -0.98 | 29.98 | 0.17 | 1.07 | 1598 |
| 2024-09-20 22:21:36.632 | MS1 | 121.4656693388 | 31.1446222301 | 916 | 504990 | -101.55 | 1.82 | 53.60 | 0.16 | 1.25 | 1566 |
| 2024-09-20 22:21:37.442 | MS1 | 121.4656768764 | 31.1446320192 | 916 | 504990 | -107.58 | -0.34 | 62.13 | 0.17 | 1.05 | 1576 |
| 2024-09-20 22:21:38.728 | MS1 | 121.4656700590 | 31.1446351519 | 916 | 504990 | -106.67 | 1.48 | 41.96 | 0.13 | 1.22 | 1573 |
| 2024-09-20 22:21:39.676 | MS1 | 121.4656708648 | 31.1446269175 | 916 | 504990 | -108.73 | -0.06 | 25.92 | 0.13 | 1.10 | 1579 |
| 2024-09-20 22:21:40.239 | MS1 | 121.4656595130 | 31.1446245025 | 916 | 504990 | -92.77 | 12.04 | 335.44 | 0.08 | 2.69 | 1582 |
| 2024-09-20 22:21:41.421 | MS1 | 121.4656765834 | 31.1446196741 | 916 | 504990 | -86.39 | 13.30 | 488.76 | 0.06 | 2.96 | 1568 |
| 2024-09-20 22:21:42.597 | MS1 | 121.4656583649 | 31.1446337865 | 916 | 504990 | -92.36 | 14.78 | 362.39 | 0.13 | 2.51 | 1581 |

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
| 3219155 | 4 | 121.4691183318 | 31.1548825474 | 152 | 10 | 1 | 46.4 | TDD | 63 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3249927 | 3 | 121.4712480650 | 31.1483250712 | 132 | 5 | 11 | 23.3 | TDD | 755 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3272995 | 1 | 121.4646956862 | 31.1558904150 | 218 | 3 | 2 | 20.2 | TDD | 635 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3279805 | 2 | 121.4717633312 | 31.1440890393 | 226 | 14 | 4 | 43.3 | TDD | 916 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.015 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.039 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.173 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.173 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.405 | NREventA2 | measId:1;ServCellPCI:985;Se... |
| 2024-09-20 22:21:34.509 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272995 | 1 | 15.8976 | 7.0790 | -117.5555 | 10.1187 | 132.1560 | 0.0191 | 0.0169 |
| 2024_09_20 22:00 | 3279805 | 2 | 19.6929 | 17.8320 | -117.4598 | 11.7791 | 140.5413 | 0.1728 | 0.0010 |
| 2024_09_20 22:00 | 3249927 | 3 | 16.9360 | 19.3522 | -115.3568 | 15.9625 | 178.7067 | 0.0107 | 0.0054 |
| 2024_09_20 22:00 | 3219155 | 4 | 15.0785 | 11.3317 | -114.0775 | 17.7921 | 170.1641 | 0.0037 | 0.0194 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416815_3EB23B6E | 504990 | 916 | -106.0 | 504990 | 635 | -107.9 | 504990 | 755 | -114.8 | 504990 | 63 |
| MR_1774416815_A5A8F492 | 504990 | 916 | -105.9 | 504990 | 635 | -109.4 | 504990 | 755 | -114.6 | 504990 | 63 |
| MR_1774416815_A7341B2F | 504990 | 916 | -106.1 | 504990 | 635 | -107.7 | 504990 | 755 | -115.4 | 504990 | 63 |
| MR_1774416815_E9A107EC | 504990 | 916 | -103.3 | 504990 | 635 | -107.8 | 504990 | 755 | -114.0 | 504990 | 63 |
| MR_1774416815_7E651232 | 504990 | 916 | -104.5 | 504990 | 635 | -108.8 | 504990 | 755 | -115.7 | 504990 | 63 |
| MR_1774416815_4E81B8A1 | 504990 | 916 | -105.7 | 504990 | 635 | -109.7 | 504990 | 755 | -116.7 | 504990 | 63 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 398: `e129be25-f19...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e129be25-f19a-499c-9b8b-45173972486d` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[398] topology](images/test_0398.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3243958_4
- `C2`: Increase A3 Offset threshold for 3276659_1
- `C3`: Press down the tilt angle  of 3243958_4 by 3 degrees
- `C4`: Increase A3 Offset threshold for 3243958_4
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243958_4
- `C7`: Decrease transmission power for 3243958_4
- `C8`: Press down the tilt angle of 3276659_1 by 10 degrees
- `C9`: Increase transmission power for 3243958_4
- `C10`: Lift the tilt angle  of 3243958_4 by 3 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276659_1
- `C12`: Decrease transmission power for 3276659_1
- `C13`: Add neighbor relationship between 3217346_3 and 3243958_4
- `C14`: Adjust the azimuth of 3243958_4 by 1 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276659_1
- `C16`: Check test server and transmission issues
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243958_4
- `C18`: Increase transmission power for 3276659_1
- `C19`: Decrease A3 Offset threshold for 3276659_1
- `C20`: Adjust the azimuth of 3276659_1 by 21 degrees
- `C21`: Add neighbor relationship between 3276659_1 and 3243958_4
- `C22`: Lift the tilt angle of 3276659_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.863 | MS1 | 121.4656665841 | 31.1446358808 | 176 | 504990 | -88.40 | 15.27 | 592.49 | 0.09 | 2.40 | 1562 |
| 2024-09-20 22:21:32.542 | MS1 | 121.4656596156 | 31.1446335187 | 176 | 504990 | -92.01 | 14.92 | 321.16 | 0.02 | 2.72 | 1585 |
| 2024-09-20 22:21:33.963 | MS1 | 121.4656621201 | 31.1446311889 | 176 | 504990 | -90.77 | 14.68 | 492.87 | 0.08 | 2.40 | 1598 |
| 2024-09-20 22:21:34.662 | MS1 | 121.4656771769 | 31.1446196173 | 176 | 504990 | -103.63 | 0.02 | 61.36 | 0.14 | 1.17 | 1600 |
| 2024-09-20 22:21:35.476 | MS1 | 121.4656770817 | 31.1446365022 | 176 | 504990 | -103.52 | -0.89 | 70.31 | 0.18 | 1.27 | 1594 |
| 2024-09-20 22:21:36.278 | MS1 | 121.4656752855 | 31.1446282544 | 176 | 504990 | -103.42 | -0.63 | 68.97 | 0.02 | 1.12 | 1569 |
| 2024-09-20 22:21:37.708 | MS1 | 121.4656751928 | 31.1446352166 | 176 | 504990 | -102.32 | 1.41 | 56.77 | 0.12 | 1.30 | 1567 |
| 2024-09-20 22:21:38.850 | MS1 | 121.4656585654 | 31.1446198667 | 176 | 504990 | -107.86 | 0.93 | 48.43 | 0.07 | 1.43 | 1588 |
| 2024-09-20 22:21:39.918 | MS1 | 121.4656580441 | 31.1446183153 | 176 | 504990 | -104.83 | 0.58 | 70.60 | 0.03 | 1.42 | 1568 |
| 2024-09-20 22:21:40.581 | MS1 | 121.4656736087 | 31.1446363422 | 176 | 504990 | -87.21 | 16.55 | 467.48 | 0.18 | 2.45 | 1570 |
| 2024-09-20 22:21:41.192 | MS1 | 121.4656654946 | 31.1446301343 | 176 | 504990 | -86.69 | 13.15 | 550.49 | 0.11 | 2.38 | 1584 |
| 2024-09-20 22:21:42.816 | MS1 | 121.4656629357 | 31.1446300724 | 176 | 504990 | -87.28 | 12.44 | 553.67 | 0.06 | 2.61 | 1585 |

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
| 3217346 | 3 | 121.4657124764 | 31.1513834586 | 2 | 0 | 9 | 24.1 | TDD | 838 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3243958 | 4 | 121.4751072317 | 31.1545799727 | 220 | 1 | 8 | 43.7 | TDD | 766 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3254293 | 2 | 121.4755478203 | 31.1467887119 | 211 | 3 | 8 | 39.3 | TDD | 573 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3276659 | 1 | 121.4696581636 | 31.1441812748 | 256 | 15 | 8 | 34.8 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.967 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.984 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.111 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.111 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.300 | NREventA2 | measId:1;ServCellPCI:844;Se... |
| 2024-09-20 22:21:34.424 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276659 | 1 | 17.1409 | 15.7531 | -114.3508 | 18.1099 | 102.2041 | 0.1523 | 0.0106 |
| 2024_09_20 22:00 | 3254293 | 2 | 10.2650 | 19.7635 | -117.4609 | 13.6731 | 102.2691 | 0.0094 | 0.0088 |
| 2024_09_20 22:00 | 3217346 | 3 | 8.8698 | 6.1010 | -116.7283 | 8.3178 | 98.7154 | 0.0060 | 0.0115 |
| 2024_09_20 22:00 | 3243958 | 4 | 8.1062 | 12.9043 | -116.5197 | 16.7940 | 165.5632 | 0.0009 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415883_1AAE0497 | 504990 | 176 | -102.4 | 504990 | 766 | -109.6 | 504990 | 838 | -114.5 | 504990 | 573 |
| MR_1774415883_7288A657 | 504990 | 176 | -102.6 | 504990 | 766 | -109.0 | 504990 | 838 | -112.2 | 504990 | 573 |
| MR_1774415883_61130991 | 504990 | 176 | -104.6 | 504990 | 766 | -107.8 | 504990 | 838 | -115.6 | 504990 | 573 |
| MR_1774415883_8955EF57 | 504990 | 176 | -103.2 | 504990 | 766 | -110.1 | 504990 | 838 | -113.2 | 504990 | 573 |
| MR_1774415883_997B07D4 | 504990 | 176 | -101.7 | 504990 | 766 | -107.0 | 504990 | 838 | -111.8 | 504990 | 573 |
| MR_1774415883_AE8A9667 | 504990 | 176 | -102.6 | 504990 | 766 | -107.5 | 504990 | 838 | -114.4 | 504990 | 573 |
| MR_1774415883_E5082D47 | 504990 | 176 | -103.0 | 504990 | 766 | -108.1 | 504990 | 838 | -114.3 | 504990 | 573 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 399: `f9c5a2e6-858...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f9c5a2e6-8582-4665-8195-f29d1d6f44cc` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[399] topology](images/test_0399.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3237312_2 by 48 degrees
- `C2`: Increase A3 Offset threshold for 3237312_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237312_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Lift the tilt angle of 3237312_2 by 10 degrees
- `C6`: Decrease A3 Offset threshold for 3237312_2
- `C7`: Decrease transmission power for 3237312_2
- `C8`: Decrease A3 Offset threshold for 3215099_1
- `C9`: Adjust the azimuth of 3215099_1 by 25 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215099_1
- `C11`: Increase transmission power for 3237312_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215099_1
- `C13`: Add neighbor relationship between 3237312_2 and 3215099_1
- `C14`: Press down the tilt angle of 3237312_2 by 10 degrees
- `C15`: Lift the tilt angle  of 3215099_1 by 2 degrees
- `C16`: Decrease transmission power for 3215099_1
- `C17`: Add neighbor relationship between 3241067_3 and 3215099_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237312_2
- `C19`: Increase transmission power for 3215099_1
- `C20`: Press down the tilt angle  of 3215099_1 by 2 degrees
- `C21`: Check test server and transmission issues
- `C22`: Increase A3 Offset threshold for 3215099_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.307 | MS1 | 121.4656717146 | 31.1446355212 | 245 | 504990 | -77.96 | 17.09 | 527.37 | 0.17 | 2.53 | 1598 |
| 2024-09-20 22:21:32.558 | MS1 | 121.4656699234 | 31.1446331611 | 245 | 504990 | -75.83 | 17.55 | 355.06 | 0.20 | 2.52 | 1577 |
| 2024-09-20 22:21:33.172 | MS1 | 121.4656589683 | 31.1446218110 | 245 | 504990 | -75.20 | 12.71 | 355.80 | 0.14 | 2.91 | 1584 |
| 2024-09-20 22:21:34.937 | MS1 | 121.4656633360 | 31.1446185330 | 245 | 504990 | -90.76 | -3.61 | 38.75 | 0.17 | 1.12 | 1597 |
| 2024-09-20 22:21:35.217 | MS1 | 121.4656637864 | 31.1446217353 | 245 | 504990 | -92.26 | -0.60 | 49.20 | 0.11 | 1.06 | 1573 |
| 2024-09-20 22:21:36.868 | MS1 | 121.4656663295 | 31.1446215207 | 245 | 504990 | -94.07 | -3.59 | 47.92 | 0.11 | 1.36 | 1595 |
| 2024-09-20 22:21:37.675 | MS1 | 121.4656595601 | 31.1446193277 | 245 | 504990 | -87.99 | -3.31 | 61.17 | 0.08 | 1.38 | 1564 |
| 2024-09-20 22:21:38.190 | MS1 | 121.4656749145 | 31.1446184248 | 245 | 504990 | -78.58 | 12.79 | 536.45 | 0.05 | 1.10 | 1572 |
| 2024-09-20 22:21:39.608 | MS1 | 121.4656675009 | 31.1446193848 | 245 | 504990 | -84.14 | 12.79 | 515.23 | 0.10 | 1.35 | 1578 |
| 2024-09-20 22:21:40.273 | MS1 | 121.4656748561 | 31.1446265386 | 245 | 504990 | -84.88 | 17.42 | 444.62 | 0.06 | 2.70 | 1579 |
| 2024-09-20 22:21:41.890 | MS1 | 121.4656662974 | 31.1446250247 | 245 | 504990 | -82.46 | 13.71 | 567.91 | 0.05 | 2.35 | 1568 |
| 2024-09-20 22:21:42.410 | MS1 | 121.4656638437 | 31.1446359874 | 245 | 504990 | -82.19 | 16.37 | 551.81 | 0.14 | 2.14 | 1577 |

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
| 3215099 | 1 | 121.4741128057 | 31.1512638674 | 252 | 1 | 10 | 28.4 | TDD | 672 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3237312 | 2 | 121.4690868629 | 31.1471903207 | 181 | 9 | 12 | 26.3 | TDD | 245 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3241067 | 3 | 121.4659779274 | 31.1490340835 | 193 | 11 | 9 | 22.0 | TDD | 51 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3258849 | 4 | 121.4680491242 | 31.1475015998 | 26 | 4 | 6 | 47.8 | TDD | 757 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.154 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.178 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.323 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.323 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.987 | NREventA3 | measId:2;ServCellPCI:185;Se... |
| 2024-09-20 22:21:35.987 | NREventA3 | measId:2;ServCellPCI:185;Se... |
| 2024-09-20 22:21:36.987 | NREventA3 | measId:2;ServCellPCI:185;Se... |
| 2024-09-20 22:21:39.487 | NRRRCReestablishAttempt | PCI:185 |
| 2024-09-20 22:21:39.504 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.514 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.656 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.656 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215099 | 1 | 16.8740 | 8.2692 | -114.1587 | 18.9635 | 168.9934 | 0.0100 | 0.0012 |
| 2024_09_20 22:00 | 3237312 | 2 | 19.4376 | 5.7560 | -116.8081 | 18.5093 | 158.8846 | 0.0073 | 0.1521 |
| 2024_09_20 22:00 | 3241067 | 3 | 16.8795 | 17.6970 | -114.0043 | 10.7408 | 117.4776 | 0.0149 | 0.0106 |
| 2024_09_20 22:00 | 3258849 | 4 | 19.5192 | 12.6505 | -117.5229 | 8.0074 | 131.6620 | 0.0157 | 0.0068 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416456_E1B19911 | 504990 | 245 | -91.5 | 504990 | 672 | -87.1 | 504990 | 51 | -93.9 | 504990 | 757 |
| MR_1774416456_BA58BF62 | 504990 | 672 | -84.4 | 504990 | 245 | -89.3 | 504990 | 51 | -93.4 | 504990 | 757 |
| MR_1774416456_79E339B6 | 504990 | 245 | -92.4 | 504990 | 672 | -86.1 | 504990 | 51 | -95.9 | 504990 | 757 |
| MR_1774416456_71EBE0F1 | 504990 | 245 | -92.3 | 504990 | 672 | -86.0 | 504990 | 51 | -94.7 | 504990 | 757 |
| MR_1774416456_CF092B8E | 504990 | 245 | -90.8 | 504990 | 672 | -84.9 | 504990 | 51 | -96.6 | 504990 | 757 |

> *... 2개 열 생략 (전체 14열)*

---
