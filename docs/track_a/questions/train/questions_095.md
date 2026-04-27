# Track A 문제 분석 — train[940]~train[949]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[940] ~ train[949] (10개)

## 목차

1. [문제 940: `ef9a77e0-69f...`](#940) — single-answer, 정답: C2
2. [문제 941: `de34cc20-f33...`](#941) — single-answer, 정답: C16
3. [문제 942: `309471e6-2d3...`](#942) — single-answer, 정답: C1
4. [문제 943: `77b6c36e-10f...`](#943) — single-answer, 정답: C14
5. [문제 944: `6a4a1114-9a1...`](#944) — single-answer, 정답: C22
6. [문제 945: `6292dcb9-09e...`](#945) — single-answer, 정답: C18
7. [문제 946: `ff16b76c-ca8...`](#946) — single-answer, 정답: C19
8. [문제 947: `6bd8ca1a-2f0...`](#947) — single-answer, 정답: C15
9. [문제 948: `4daa2d69-70c...`](#948) — single-answer, 정답: C19
10. [문제 949: `af7f8d8e-2dc...`](#949) — single-answer, 정답: C4

---

### 문제 940: `ef9a77e0-69f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ef9a77e0-69f7-459b-ad98-cd61bae498fd` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Decrease A3 Offset threshold for 3215363_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[940] topology](images/train_0940.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3215363_1 and 3226010_3
- `C2`: Decrease A3 Offset threshold for 3215363_1 **← 정답**
- `C3`: Adjust the azimuth of 3215363_1 by 50 degrees
- `C4`: Decrease transmission power for 3215363_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226010_3
- `C6`: Lift the tilt angle of 3215363_1 by 2 degrees
- `C7`: Increase transmission power for 3215363_1
- `C8`: Press down the tilt angle of 3215363_1 by 2 degrees
- `C9`: Press down the tilt angle  of 3226010_3 by 10 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215363_1
- `C11`: Check test server and transmission issues
- `C12`: Increase transmission power for 3226010_3
- `C13`: Decrease transmission power for 3226010_3
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Lift the tilt angle  of 3226010_3 by 10 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215363_1
- `C17`: Increase A3 Offset threshold for 3215363_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226010_3
- `C19`: Add neighbor relationship between 3238847_2 and 3226010_3
- `C20`: Decrease A3 Offset threshold for 3226010_3
- `C21`: Adjust the azimuth of 3226010_3 by 50 degrees
- `C22`: Increase A3 Offset threshold for 3226010_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.486 | MS1 | 121.4656656289 | 31.1446332032 | 408 | 504990 | -80.26 | 15.06 | 410.85 | 0.19 | 2.68 | 1563 |
| 2024-09-20 22:21:32.454 | MS1 | 121.4656775232 | 31.1446254415 | 408 | 504990 | -84.76 | 17.13 | 529.98 | 0.11 | 2.27 | 1578 |
| 2024-09-20 22:21:33.553 | MS1 | 121.4656639607 | 31.1446330601 | 408 | 504990 | -84.22 | 13.12 | 447.84 | 0.07 | 2.32 | 1581 |
| 2024-09-20 22:21:34.920 | MS1 | 121.4656621370 | 31.1446334619 | 408 | 504990 | -87.72 | -1.88 | 38.70 | 0.06 | 1.28 | 1569 |
| 2024-09-20 22:21:35.855 | MS1 | 121.4656772460 | 31.1446305910 | 408 | 504990 | -88.32 | -3.77 | 47.98 | 0.15 | 1.12 | 1580 |
| 2024-09-20 22:21:36.111 | MS1 | 121.4656670387 | 31.1446355183 | 408 | 504990 | -89.63 | -1.42 | 40.22 | 0.19 | 1.00 | 1575 |
| 2024-09-20 22:21:37.798 | MS1 | 121.4656691355 | 31.1446180955 | 408 | 504990 | -87.48 | -2.46 | 46.58 | 0.07 | 1.47 | 1600 |
| 2024-09-20 22:21:38.197 | MS1 | 121.4656636983 | 31.1446377846 | 408 | 504990 | -90.84 | -1.29 | 71.43 | 0.06 | 1.45 | 1584 |
| 2024-09-20 22:21:39.553 | MS1 | 121.4656744778 | 31.1446271397 | 403 | 504990 | -84.30 | 16.82 | 176.09 | 0.09 | 1.27 | 1564 |
| 2024-09-20 22:21:40.122 | MS1 | 121.4656637225 | 31.1446195305 | 403 | 504990 | -83.48 | 15.09 | 522.30 | 0.11 | 2.85 | 1592 |
| 2024-09-20 22:21:41.955 | MS1 | 121.4656639546 | 31.1446354632 | 403 | 504990 | -80.54 | 16.85 | 568.34 | 0.18 | 2.02 | 1593 |
| 2024-09-20 22:21:42.464 | MS1 | 121.4656759228 | 31.1446306551 | 403 | 504990 | -76.98 | 12.31 | 520.15 | 0.13 | 2.65 | 1600 |

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
| 3215363 | 1 | 121.4746103160 | 31.1521715299 | 32 | 0 | 3 | 39.5 | TDD | 408 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3226010 | 3 | 121.4714009561 | 31.1550150937 | 138 | 10 | 7 | 41.0 | TDD | 403 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3238847 | 2 | 121.4736932319 | 31.1559635969 | 56 | 9 | 6 | 49.6 | TDD | 937 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3243848 | 4 | 121.4718756733 | 31.1463651961 | 102 | 11 | 11 | 38.0 | TDD | 660 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.551 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.566 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.715 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.715 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.440 | NREventA3 | measId:2;ServCellPCI:708;Se... |
| 2024-09-20 22:21:38.680 | NRHandoverAttempt | SourcePCI:708;SourceNR-ARFC... |
| 2024-09-20 22:21:38.727 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.740 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.850 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.850 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215363 | 1 | 10.3762 | 6.0403 | -114.8798 | 10.8197 | 88.8577 | 0.0026 | 0.1043 |
| 2024_09_20 22:00 | 3238847 | 2 | 11.6163 | 18.1022 | -115.2380 | 8.9434 | 91.8414 | 0.0056 | 0.0016 |
| 2024_09_20 22:00 | 3226010 | 3 | 16.8892 | 16.8578 | -116.7769 | 15.4863 | 159.7343 | 0.0065 | 0.0088 |
| 2024_09_20 22:00 | 3243848 | 4 | 12.0474 | 11.9912 | -114.4047 | 5.9171 | 131.3865 | 0.0102 | 0.0151 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413876_B42F8CF6 | 504990 | 408 | -89.3 | 504990 | 403 | -84.7 | 504990 | 937 | -89.7 | 504990 | 660 |
| MR_1774413876_3B6446F5 | 504990 | 403 | -82.7 | 504990 | 408 | -88.0 | 504990 | 937 | -90.0 | 504990 | 660 |
| MR_1774413876_34DF7564 | 504990 | 403 | -82.8 | 504990 | 408 | -87.2 | 504990 | 937 | -88.6 | 504990 | 660 |
| MR_1774413876_9EAD87AD | 504990 | 408 | -88.2 | 504990 | 403 | -81.3 | 504990 | 937 | -87.6 | 504990 | 660 |
| MR_1774413876_FAFD85A0 | 504990 | 403 | -81.0 | 504990 | 408 | -87.4 | 504990 | 937 | -87.7 | 504990 | 660 |
| MR_1774413876_5E072BD4 | 504990 | 408 | -86.0 | 504990 | 403 | -84.6 | 504990 | 937 | -89.7 | 504990 | 660 |
| MR_1774413876_6D6649A1 | 504990 | 408 | -89.1 | 504990 | 403 | -81.1 | 504990 | 937 | -87.7 | 504990 | 660 |
| MR_1774413876_633E6A6B | 504990 | 403 | -83.2 | 504990 | 408 | -89.4 | 504990 | 937 | -87.3 | 504990 | 660 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 941: `de34cc20-f33...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `de34cc20-f334-4cbc-961b-dbf110360611` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265176_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[941] topology](images/train_0941.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3265176_6 by 27 degrees
- `C2`: Decrease transmission power for 3277420_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265176_6
- `C4`: Increase transmission power for 3265176_6
- `C5`: Add neighbor relationship between 3234053_10 and 3277420_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277420_3
- `C7`: Increase A3 Offset threshold for 3277420_3
- `C8`: Press down the tilt angle of 3265176_6 by 0 degrees
- `C9`: Decrease A3 Offset threshold for 3277420_3
- `C10`: Lift the tilt angle  of 3277420_3 by 5 degrees
- `C11`: Adjust the azimuth of 3277420_3 by 41 degrees
- `C12`: Increase transmission power for 3277420_3
- `C13`: Decrease transmission power for 3265176_6
- `C14`: Decrease A3 Offset threshold for 3265176_6
- `C15`: Lift the tilt angle of 3265176_6 by 0 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265176_6 **← 정답**
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Press down the tilt angle  of 3277420_3 by 5 degrees
- `C19`: Add neighbor relationship between 3265176_6 and 3277420_3
- `C20`: Increase A3 Offset threshold for 3265176_6
- `C21`: Check test server and transmission issues
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277420_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.172 | MS1 | 121.4656602596 | 31.1446231693 | 409 | 504990 | -93.36 | 9.92 | 331.84 | 0.01 | 2.35 | 1592 |
| 2024-09-20 22:21:32.344 | MS1 | 121.4656729830 | 31.1446207303 | 77 | 504990 | -94.04 | 9.96 | 544.77 | 0.12 | 2.39 | 1569 |
| 2024-09-20 22:21:33.984 | MS1 | 121.4656717854 | 31.1446315627 | 565 | 504990 | -93.18 | 12.55 | 337.16 | 0.19 | 2.90 | 1565 |
| 2024-09-20 22:21:34.318 | MS1 | 121.4656728583 | 31.1446379961 | 865 | 152650 | -93.14 | 7.18 | 85.94 | 0.19 | 1.62 | 988 |
| 2024-09-20 22:21:35.143 | MS1 | 121.4656756536 | 31.1446249753 | 516 | 152650 | -89.34 | 2.80 | 94.49 | 0.12 | 1.97 | 925 |
| 2024-09-20 22:21:36.409 | MS1 | 121.4656745536 | 31.1446302195 | 836 | 152650 | -96.98 | 2.51 | 74.21 | 0.06 | 1.91 | 930 |
| 2024-09-20 22:21:37.471 | MS1 | 121.4656639613 | 31.1446373007 | 945 | 152650 | -87.12 | 3.37 | 53.21 | 0.06 | 1.79 | 918 |
| 2024-09-20 22:21:38.269 | MS1 | 121.4656621813 | 31.1446375878 | 865 | 152650 | -88.59 | 5.29 | 59.13 | 0.01 | 1.66 | 971 |
| 2024-09-20 22:21:39.900 | MS1 | 121.4656714610 | 31.1446230937 | 516 | 152650 | -92.86 | 5.53 | 63.56 | 0.11 | 1.60 | 906 |
| 2024-09-20 22:21:40.231 | MS1 | 121.4656762210 | 31.1446240807 | 836 | 152650 | -87.15 | 2.97 | 73.55 | 0.18 | 2.34 | 1593 |
| 2024-09-20 22:21:41.404 | MS1 | 121.4656650152 | 31.1446256841 | 945 | 152650 | -95.79 | 3.75 | 53.38 | 0.18 | 2.46 | 1594 |
| 2024-09-20 22:21:42.681 | MS1 | 121.4656704686 | 31.1446260878 | 865 | 152650 | -91.28 | 6.78 | 70.86 | 0.18 | 2.39 | 1586 |

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
| 3210443 | 12 | 121.4696661992 | 31.1440838627 | 141 | 13 | 11 | 13.1 | FDD | 945 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3215587 | 7 | 121.4713560884 | 31.1518401380 | 145 | 2 | 10 | 7.1 | FDD | 865 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3218321 | 9 | 121.4734460746 | 31.1481658548 | 306 | 13 | 9 | 2.3 | FDD | 516 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3226615 | 11 | 121.4657503195 | 31.1505273613 | 29 | 10 | 8 | 28.8 | FDD | 646 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3234053 | 10 | 121.4707429630 | 31.1457465246 | 57 | 9 | 12 | 29.1 | FDD | 836 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3234269 | 5 | 121.4642039907 | 31.1546458810 | 131 | 12 | 8 | 29.4 | TDD | 565 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3248538 | 8 | 121.4664305147 | 31.1532056170 | 44 | 3 | 7 | 10.6 | FDD | 226 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3249336 | 13 | 121.4683305492 | 31.1483747436 | 144 | 11 | 1 | 27.1 | FDD | 986 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3256076 | 1 | 121.4720428466 | 31.1475545942 | 259 | 13 | 4 | 28.3 | TDD | 259 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3264181 | 4 | 121.4701373300 | 31.1476608154 | 59 | 10 | 10 | 16.8 | TDD | 242 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3265176 | 6 | 121.4643656978 | 31.1520736803 | 145 | 0 | 7 | 4.5 | TDD | 409 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3273288 | 2 | 121.4643613354 | 31.1515376459 | 6 | 12 | 8 | 26.5 | TDD | 77 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3277420 | 3 | 121.4734669951 | 31.1558589296 | 170 | 4 | 0 | 27.3 | TDD | 722 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.961 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.984 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.104 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.104 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.794 | NREventA2 | measId:1;ServCellPCI:992;Se... |
| 2024-09-20 22:21:34.938 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.167 | NREventA5 | measId:3;ServCellPCI:992;Se... |
| 2024-09-20 22:21:35.224 | NRHandoverAttempt | SourcePCI:992;SourceNR-ARFC... |
| 2024-09-20 22:21:35.247 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.258 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.359 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.359 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256076 | 1 | 7.8838 | 5.8438 | -114.2751 | 13.5189 | 174.4721 | 0.0048 | 0.0175 |
| 2024_09_20 22:00 | 3273288 | 2 | 13.7932 | 18.3573 | -114.7789 | 17.0032 | 99.5807 | 0.0180 | 0.0197 |
| 2024_09_20 22:00 | 3277420 | 3 | 14.4531 | 16.3666 | -117.7143 | 6.8535 | 110.3546 | 0.0061 | 0.0114 |
| 2024_09_20 22:00 | 3264181 | 4 | 19.7209 | 15.5936 | -115.1100 | 19.3794 | 93.9674 | 0.0039 | 0.0199 |
| 2024_09_20 22:00 | 3234269 | 5 | 18.7092 | 7.2497 | -114.5643 | 7.1206 | 151.4131 | 0.0058 | 0.0083 |
| 2024_09_20 22:00 | 3265176 | 6 | 12.8918 | 7.5665 | -117.8614 | 7.3977 | 80.4342 | 0.0091 | 0.0066 |
| 2024_09_20 22:00 | 3215587 | 7 | 9.0975 | 19.9567 | -116.4547 | 4.8496 | 37.2248 | 0.0193 | 0.0185 |
| 2024_09_20 22:00 | 3248538 | 8 | 5.2111 | 15.1387 | -116.6512 | 4.0323 | 53.7565 | 0.0180 | 0.0143 |
| 2024_09_20 22:00 | 3218321 | 9 | 5.6995 | 6.0051 | -115.5696 | 4.8747 | 49.4044 | 0.0133 | 0.0008 |
| 2024_09_20 22:00 | 3234053 | 10 | 7.4070 | 14.0541 | -114.0303 | 3.1653 | 59.7942 | 0.0021 | 0.0048 |
| 2024_09_20 22:00 | 3226615 | 11 | 16.7464 | 10.9294 | -114.5129 | 4.6746 | 26.0306 | 0.0180 | 0.0108 |
| 2024_09_20 22:00 | 3210443 | 12 | 16.0839 | 17.6419 | -116.2988 | 4.9353 | 37.3558 | 0.0141 | 0.0055 |
| 2024_09_20 22:00 | 3249336 | 13 | 13.6879 | 18.5942 | -114.8285 | 4.8838 | 32.9783 | 0.0158 | 0.0072 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414255_A290F600 | 152650 | 865 | -93.6 | 152650 | 646 | -101.4 | 152650 | 226 | -103.7 | 152650 | 986 |
| MR_1774414255_7DBC1819 | 152650 | 865 | -94.3 | 152650 | 646 | -100.1 | 152650 | 226 | -101.9 | 152650 | 986 |
| MR_1774414255_8E3B8CBA | 152650 | 865 | -95.1 | 152650 | 646 | -98.5 | 152650 | 226 | -103.6 | 152650 | 986 |
| MR_1774414255_49C3E7A7 | 152650 | 865 | -93.3 | 152650 | 646 | -98.8 | 152650 | 226 | -101.5 | 152650 | 986 |
| MR_1774414255_295EE786 | 152650 | 865 | -92.4 | 152650 | 646 | -98.5 | 152650 | 226 | -103.8 | 152650 | 986 |
| MR_1774414255_C4BC390D | 152650 | 865 | -94.6 | 152650 | 646 | -98.8 | 152650 | 226 | -104.8 | 152650 | 986 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 942: `309471e6-2d3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `309471e6-2d3b-4b57-92f9-7c656d81e214` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Lift the tilt angle  of 3256847_1 by 6 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[942] topology](images/train_0942.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3256847_1 by 6 degrees **← 정답**
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215433_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216034_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Add neighbor relationship between 3256847_1 and 3216034_2
- `C6`: Adjust the azimuth of 3256847_1 by 14 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215433_4
- `C8`: Increase A3 Offset threshold for 3215433_4
- `C9`: Decrease transmission power for 3215433_4
- `C10`: Decrease transmission power for 3216034_2
- `C11`: Adjust the azimuth of 3215433_4 by 6 degrees
- `C12`: Decrease A3 Offset threshold for 3215433_4
- `C13`: Press down the tilt angle of 3215433_4 by 5 degrees
- `C14`: Increase A3 Offset threshold for 3216034_2
- `C15`: Press down the tilt angle  of 3256847_1 by 6 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216034_2
- `C17`: Decrease A3 Offset threshold for 3216034_2
- `C18`: Check test server and transmission issues
- `C19`: Add neighbor relationship between 3215433_4 and 3216034_2
- `C20`: Lift the tilt angle of 3215433_4 by 5 degrees
- `C21`: Increase transmission power for 3216034_2
- `C22`: Increase transmission power for 3215433_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.227 | MS1 | 121.4656727428 | 31.1446180590 | 327 | 504990 | -89.46 | 14.44 | 545.06 | 0.15 | 2.74 | 1565 |
| 2024-09-20 22:21:32.682 | MS1 | 121.4656669499 | 31.1446367695 | 327 | 504990 | -91.27 | 16.47 | 526.40 | 0.14 | 2.60 | 1573 |
| 2024-09-20 22:21:33.949 | MS1 | 121.4656698254 | 31.1446218565 | 327 | 504990 | -85.99 | 17.49 | 530.26 | 0.02 | 2.39 | 1577 |
| 2024-09-20 22:21:34.161 | MS1 | 121.4656699519 | 31.1446368890 | 327 | 504990 | -89.82 | 17.54 | 93.54 | 0.14 | 2.72 | 1587 |
| 2024-09-20 22:21:35.620 | MS1 | 121.4656777407 | 31.1446218054 | 327 | 504990 | -91.29 | 13.21 | 72.30 | 0.18 | 2.29 | 1567 |
| 2024-09-20 22:21:36.895 | MS1 | 121.4656648625 | 31.1446263975 | 327 | 504990 | -86.08 | 14.71 | 97.60 | 0.01 | 2.88 | 1580 |
| 2024-09-20 22:21:37.684 | MS1 | 121.4656700854 | 31.1446288834 | 327 | 504990 | -91.14 | 11.97 | 93.35 | 0.10 | 2.45 | 1571 |
| 2024-09-20 22:21:38.195 | MS1 | 121.4656614840 | 31.1446223365 | 327 | 504990 | -91.79 | 7.45 | 100.41 | 0.18 | 2.42 | 1587 |
| 2024-09-20 22:21:39.795 | MS1 | 121.4656589253 | 31.1446248200 | 327 | 504990 | -91.73 | 10.07 | 71.02 | 0.18 | 2.21 | 1585 |
| 2024-09-20 22:21:40.403 | MS1 | 121.4656684758 | 31.1446257122 | 327 | 504990 | -91.55 | 8.57 | 514.35 | 0.19 | 2.82 | 1595 |
| 2024-09-20 22:21:41.426 | MS1 | 121.4656675510 | 31.1446344779 | 327 | 504990 | -90.31 | 7.22 | 332.60 | 0.08 | 2.19 | 1600 |
| 2024-09-20 22:21:42.215 | MS1 | 121.4656711249 | 31.1446287829 | 327 | 504990 | -91.04 | 11.04 | 342.98 | 0.14 | 2.05 | 1580 |

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
| 3215433 | 4 | 121.4690521355 | 31.1533499112 | 204 | 3 | 9 | 35.4 | TDD | 327 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3216034 | 2 | 121.4735819683 | 31.1444534582 | 257 | 4 | 2 | 23.1 | TDD | 958 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3240523 | 3 | 121.4756646770 | 31.1538482041 | 103 | 9 | 9 | 26.6 | TDD | 14 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3256847 | 1 | 121.4662419130 | 31.1447974720 | 40 | 2 | 3 | 26.6 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.169 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.192 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.323 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.323 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.983 | NREventA3 | measId:2;ServCellPCI:330;Se... |
| 2024-09-20 22:21:38.223 | NRHandoverAttempt | SourcePCI:330;SourceNR-ARFC... |
| 2024-09-20 22:21:38.259 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.274 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.401 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.401 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256847 | 1 | 5.0234 | 16.3758 | -117.5112 | 8.8376 | 160.8632 | 0.0066 | 0.0026 |
| 2024_09_20 22:00 | 3216034 | 2 | 9.1859 | 17.9131 | -116.9124 | 19.7776 | 111.2001 | 0.0178 | 0.0140 |
| 2024_09_20 22:00 | 3240523 | 3 | 11.4841 | 12.7391 | -115.4397 | 17.3008 | 199.2109 | 0.0033 | 0.0074 |
| 2024_09_20 22:00 | 3215433 | 4 | 90.6440 | 90.6129 | -117.0584 | 6.9795 | 195.1247 | 0.0151 | 0.0101 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413768_3DD012CA | 504990 | 327 | -88.0 | 504990 | 958 | -89.9 | 504990 | 129 | -101.0 | 504990 | 14 |
| MR_1774413768_8602F78F | 504990 | 327 | -90.9 | 504990 | 958 | -89.2 | 504990 | 129 | -100.3 | 504990 | 14 |
| MR_1774413768_C563AD63 | 504990 | 327 | -89.2 | 504990 | 958 | -92.2 | 504990 | 129 | -101.9 | 504990 | 14 |
| MR_1774413768_2F235A9D | 504990 | 327 | -90.7 | 504990 | 958 | -90.1 | 504990 | 129 | -100.9 | 504990 | 14 |
| MR_1774413768_86547540 | 504990 | 327 | -90.3 | 504990 | 958 | -91.9 | 504990 | 129 | -100.5 | 504990 | 14 |
| MR_1774413768_CB1E63EB | 504990 | 327 | -89.2 | 504990 | 958 | -89.8 | 504990 | 129 | -101.3 | 504990 | 14 |
| MR_1774413768_CCD1FFD3 | 504990 | 327 | -90.7 | 504990 | 958 | -89.2 | 504990 | 129 | -101.8 | 504990 | 14 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 943: `77b6c36e-10f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `77b6c36e-10f1-45b2-9090-bba68c693290` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263491_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[943] topology](images/train_0943.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3263491_5
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263491_5
- `C3`: Add neighbor relationship between 3263491_5 and 3231659_2
- `C4`: Decrease A3 Offset threshold for 3231659_2
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase A3 Offset threshold for 3231659_2
- `C7`: Increase transmission power for 3231659_2
- `C8`: Check test server and transmission issues
- `C9`: Decrease transmission power for 3231659_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231659_2
- `C11`: Decrease transmission power for 3263491_5
- `C12`: Lift the tilt angle of 3263491_5 by 4 degrees
- `C13`: Add neighbor relationship between 3278295_13 and 3231659_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263491_5 **← 정답**
- `C15`: Decrease A3 Offset threshold for 3263491_5
- `C16`: Adjust the azimuth of 3263491_5 by 18 degrees
- `C17`: Adjust the azimuth of 3231659_2 by 21 degrees
- `C18`: Press down the tilt angle of 3263491_5 by 4 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231659_2
- `C20`: Lift the tilt angle  of 3231659_2 by 4 degrees
- `C21`: Press down the tilt angle  of 3231659_2 by 4 degrees
- `C22`: Increase transmission power for 3263491_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.921 | MS1 | 121.4656733070 | 31.1446338412 | 597 | 504990 | -95.81 | 10.84 | 319.63 | 0.06 | 2.23 | 1596 |
| 2024-09-20 22:21:32.669 | MS1 | 121.4656754322 | 31.1446366089 | 484 | 504990 | -94.62 | 11.17 | 552.58 | 0.17 | 2.93 | 1573 |
| 2024-09-20 22:21:33.763 | MS1 | 121.4656617607 | 31.1446191369 | 979 | 504990 | -94.52 | 11.30 | 374.04 | 0.04 | 2.02 | 1598 |
| 2024-09-20 22:21:34.386 | MS1 | 121.4656675390 | 31.1446204826 | 56 | 152650 | -92.77 | 2.32 | 74.41 | 0.06 | 1.98 | 938 |
| 2024-09-20 22:21:35.386 | MS1 | 121.4656592453 | 31.1446341383 | 141 | 152650 | -90.65 | 3.01 | 88.45 | 0.11 | 1.64 | 964 |
| 2024-09-20 22:21:36.574 | MS1 | 121.4656777282 | 31.1446273108 | 474 | 152650 | -91.59 | 4.87 | 75.30 | 0.05 | 1.93 | 958 |
| 2024-09-20 22:21:37.552 | MS1 | 121.4656638205 | 31.1446196559 | 441 | 152650 | -95.54 | 2.59 | 63.62 | 0.02 | 1.90 | 923 |
| 2024-09-20 22:21:38.446 | MS1 | 121.4656754717 | 31.1446250486 | 56 | 152650 | -92.15 | 7.00 | 68.54 | 0.18 | 1.89 | 981 |
| 2024-09-20 22:21:39.601 | MS1 | 121.4656762970 | 31.1446225417 | 141 | 152650 | -88.67 | 5.22 | 87.42 | 0.11 | 1.64 | 972 |
| 2024-09-20 22:21:40.383 | MS1 | 121.4656762184 | 31.1446223073 | 474 | 152650 | -89.77 | 7.70 | 96.59 | 0.02 | 2.59 | 1593 |
| 2024-09-20 22:21:41.817 | MS1 | 121.4656770429 | 31.1446182301 | 441 | 152650 | -95.39 | 4.00 | 52.09 | 0.13 | 2.99 | 1597 |
| 2024-09-20 22:21:42.333 | MS1 | 121.4656628771 | 31.1446315535 | 56 | 152650 | -93.39 | 3.06 | 55.48 | 0.19 | 2.82 | 1568 |

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
| 3222724 | 1 | 121.4689336821 | 31.1541220937 | 6 | 7 | 3 | 0.8 | TDD | 484 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3231659 | 2 | 121.4738279023 | 31.1508055187 | 249 | 4 | 3 | 6.3 | TDD | 840 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3238408 | 12 | 121.4675096494 | 31.1542668862 | 70 | 0 | 0 | 21.2 | FDD | 441 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3242057 | 8 | 121.4737033993 | 31.1505295821 | 122 | 4 | 11 | 3.3 | FDD | 141 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3246017 | 10 | 121.4741787115 | 31.1464839726 | 274 | 11 | 9 | 10.4 | FDD | 461 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3247031 | 11 | 121.4740628977 | 31.1510965872 | 269 | 14 | 10 | 1.3 | FDD | 56 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3255257 | 6 | 121.4715624230 | 31.1455062299 | 31 | 10 | 12 | 14.1 | TDD | 477 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3260534 | 3 | 121.4740143608 | 31.1500060697 | 74 | 3 | 8 | 19.6 | TDD | 458 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3263491 | 5 | 121.4676541820 | 31.1470911685 | 232 | 1 | 2 | 14.8 | TDD | 597 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3265723 | 4 | 121.4661118997 | 31.1446249101 | 257 | 0 | 0 | 28.4 | TDD | 979 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3267059 | 9 | 121.4668127687 | 31.1452049189 | 140 | 3 | 2 | 13.6 | FDD | 378 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3274860 | 7 | 121.4664900689 | 31.1445349144 | 204 | 10 | 11 | 28.8 | FDD | 704 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3278295 | 13 | 121.4643601700 | 31.1506914254 | 207 | 12 | 8 | 5.4 | FDD | 474 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |

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
| 2024-09-20 22:21:31.002 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.023 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.133 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.133 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.899 | NREventA2 | measId:1;ServCellPCI:289;Se... |
| 2024-09-20 22:21:35.048 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.327 | NREventA5 | measId:3;ServCellPCI:289;Se... |
| 2024-09-20 22:21:35.372 | NRHandoverAttempt | SourcePCI:289;SourceNR-ARFC... |
| 2024-09-20 22:21:35.392 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.403 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.524 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.524 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222724 | 1 | 6.5292 | 9.2478 | -117.0071 | 5.8073 | 122.6387 | 0.0150 | 0.0172 |
| 2024_09_20 22:00 | 3231659 | 2 | 5.0219 | 18.9177 | -117.6114 | 7.3576 | 132.8234 | 0.0037 | 0.0057 |
| 2024_09_20 22:00 | 3260534 | 3 | 9.3553 | 6.2815 | -114.5343 | 8.5898 | 120.8938 | 0.0070 | 0.0196 |
| 2024_09_20 22:00 | 3265723 | 4 | 14.2590 | 19.8343 | -115.6939 | 15.3911 | 140.4072 | 0.0011 | 0.0154 |
| 2024_09_20 22:00 | 3263491 | 5 | 17.5296 | 6.8174 | -115.2785 | 12.5106 | 97.8138 | 0.0175 | 0.0002 |
| 2024_09_20 22:00 | 3255257 | 6 | 16.2066 | 8.5269 | -117.6196 | 6.8053 | 168.3892 | 0.0109 | 0.0154 |
| 2024_09_20 22:00 | 3274860 | 7 | 10.4140 | 14.7834 | -114.4009 | 4.8280 | 35.2059 | 0.0052 | 0.0070 |
| 2024_09_20 22:00 | 3242057 | 8 | 5.5159 | 13.2626 | -117.3243 | 4.8402 | 27.6963 | 0.0039 | 0.0021 |
| 2024_09_20 22:00 | 3267059 | 9 | 9.1977 | 7.5029 | -117.8953 | 3.1744 | 31.1767 | 0.0161 | 0.0160 |
| 2024_09_20 22:00 | 3246017 | 10 | 15.3573 | 12.2629 | -116.3630 | 3.3087 | 55.5448 | 0.0086 | 0.0189 |
| 2024_09_20 22:00 | 3247031 | 11 | 10.7245 | 17.4188 | -115.7759 | 3.0362 | 23.8358 | 0.0168 | 0.0077 |
| 2024_09_20 22:00 | 3238408 | 12 | 10.1157 | 14.3360 | -116.7216 | 4.8074 | 24.7875 | 0.0041 | 0.0139 |
| 2024_09_20 22:00 | 3278295 | 13 | 10.2558 | 11.0505 | -115.0401 | 3.2941 | 35.1306 | 0.0057 | 0.0109 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412352_AE6C4925 | 152650 | 56 | -91.1 | 152650 | 378 | -95.1 | 152650 | 704 | -100.6 | 152650 | 461 |
| MR_1774412352_DDF1A847 | 504990 | 979 | -92.6 | 504990 | 840 | -92.0 | 504990 | 477 | -92.6 | 504990 | 458 |
| MR_1774412352_CF1443E5 | 152650 | 56 | -92.8 | 152650 | 378 | -93.0 | 152650 | 704 | -101.1 | 152650 | 461 |
| MR_1774412352_006FFF1B | 504990 | 979 | -94.5 | 504990 | 840 | -92.1 | 504990 | 477 | -94.1 | 504990 | 458 |
| MR_1774412352_DAC068FC | 504990 | 979 | -96.2 | 504990 | 840 | -89.5 | 504990 | 477 | -92.6 | 504990 | 458 |
| MR_1774412352_47E24ABF | 504990 | 979 | -93.6 | 504990 | 840 | -90.5 | 504990 | 477 | -93.8 | 504990 | 458 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 944: `6a4a1114-9a1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6a4a1114-9a10-4506-bbbe-57849d2bfcef` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[944] topology](images/train_0944.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3279999_3
- `C2`: Adjust the azimuth of 3279999_3 by 50 degrees
- `C3`: Decrease transmission power for 3213880_4
- `C4`: Increase A3 Offset threshold for 3279999_3
- `C5`: Lift the tilt angle of 3279999_3 by 10 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213880_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279999_3
- `C8`: Add neighbor relationship between 3279999_3 and 3213880_4
- `C9`: Adjust the azimuth of 3213880_4 by 50 degrees
- `C10`: Lift the tilt angle  of 3213880_4 by 10 degrees
- `C11`: Press down the tilt angle of 3279999_3 by 10 degrees
- `C12`: Decrease A3 Offset threshold for 3279999_3
- `C13`: Add neighbor relationship between 3256410_1 and 3213880_4
- `C14`: Decrease A3 Offset threshold for 3213880_4
- `C15`: Press down the tilt angle  of 3213880_4 by 10 degrees
- `C16`: Increase A3 Offset threshold for 3213880_4
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279999_3
- `C19`: Increase transmission power for 3213880_4
- `C20`: Increase transmission power for 3279999_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213880_4
- `C22`: Check test server and transmission issues **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.500 | MS1 | 121.4656585971 | 31.1446323012 | 517 | 504990 | -88.81 | 12.54 | 391.98 | 0.13 | 2.81 | 1565 |
| 2024-09-20 22:21:32.614 | MS1 | 121.4656743400 | 31.1446352354 | 517 | 504990 | -89.99 | 14.20 | 491.62 | 0.20 | 2.99 | 1584 |
| 2024-09-20 22:21:33.180 | MS1 | 121.4656713583 | 31.1446334599 | 517 | 504990 | -86.67 | 14.30 | 527.65 | 0.14 | 2.80 | 1594 |
| 2024-09-20 22:21:34.759 | MS1 | 121.4656719910 | 31.1446309570 | 517 | 504990 | -86.65 | 16.86 | 67.18 | 0.18 | 2.96 | 355 |
| 2024-09-20 22:21:35.640 | MS1 | 121.4656612505 | 31.1446306929 | 517 | 504990 | -87.05 | 12.93 | 54.35 | 0.05 | 2.45 | 366 |
| 2024-09-20 22:21:36.277 | MS1 | 121.4656592266 | 31.1446240372 | 517 | 504990 | -86.95 | 13.48 | 82.10 | 0.18 | 2.11 | 480 |
| 2024-09-20 22:21:37.929 | MS1 | 121.4656646539 | 31.1446223379 | 517 | 504990 | -91.58 | 12.80 | 80.08 | 0.01 | 2.51 | 315 |
| 2024-09-20 22:21:38.218 | MS1 | 121.4656609431 | 31.1446323849 | 517 | 504990 | -92.70 | 9.88 | 76.69 | 0.00 | 2.48 | 355 |
| 2024-09-20 22:21:39.802 | MS1 | 121.4656588961 | 31.1446378819 | 517 | 504990 | -90.42 | 10.88 | 89.72 | 0.20 | 2.32 | 471 |
| 2024-09-20 22:21:40.758 | MS1 | 121.4656690771 | 31.1446233920 | 517 | 504990 | -90.44 | 8.21 | 428.75 | 0.08 | 2.76 | 1568 |
| 2024-09-20 22:21:41.419 | MS1 | 121.4656745714 | 31.1446331165 | 517 | 504990 | -92.79 | 7.43 | 457.99 | 0.15 | 2.79 | 1582 |
| 2024-09-20 22:21:42.471 | MS1 | 121.4656775108 | 31.1446237480 | 517 | 504990 | -92.98 | 8.44 | 326.46 | 0.15 | 2.38 | 1588 |

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
| 3213880 | 4 | 121.4704936387 | 31.1475241740 | 304 | 11 | 4 | 16.9 | TDD | 639 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3256410 | 1 | 121.4652185141 | 31.1446890611 | 297 | 1 | 6 | 25.1 | TDD | 225 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3269707 | 2 | 121.4705845109 | 31.1500249429 | 244 | 14 | 9 | 28.9 | TDD | 466 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3279999 | 3 | 121.4675394345 | 31.1449992268 | 106 | 15 | 2 | 19.4 | TDD | 517 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.428 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.444 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.573 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.573 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.270 | NREventA3 | measId:2;ServCellPCI:510;Se... |
| 2024-09-20 22:21:38.510 | NRHandoverAttempt | SourcePCI:510;SourceNR-ARFC... |
| 2024-09-20 22:21:38.557 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.571 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.687 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.687 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256410 | 1 | 13.8365 | 16.7854 | -115.5419 | 6.0340 | 113.6103 | 0.0118 | 0.0141 |
| 2024_09_20 22:00 | 3269707 | 2 | 19.3535 | 12.0014 | -117.8497 | 16.3113 | 137.6470 | 0.0015 | 0.0084 |
| 2024_09_20 22:00 | 3279999 | 3 | 17.3920 | 17.9722 | -117.2514 | 18.9462 | 180.4879 | 0.0045 | 0.0006 |
| 2024_09_20 22:00 | 3213880 | 4 | 13.3093 | 9.8261 | -114.9169 | 12.7954 | 187.7962 | 0.0152 | 0.0188 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417023_789436D3 | 504990 | 517 | -87.2 | 504990 | 639 | -93.4 | 504990 | 225 | -99.7 | 504990 | 466 |
| MR_1774417023_839BB3A0 | 504990 | 517 | -87.0 | 504990 | 639 | -90.1 | 504990 | 225 | -100.9 | 504990 | 466 |
| MR_1774417023_FB1C122D | 504990 | 517 | -86.9 | 504990 | 639 | -91.3 | 504990 | 225 | -98.4 | 504990 | 466 |
| MR_1774417023_52358E4B | 504990 | 517 | -87.3 | 504990 | 639 | -91.5 | 504990 | 225 | -98.2 | 504990 | 466 |
| MR_1774417023_E0A251AE | 504990 | 517 | -87.4 | 504990 | 639 | -89.8 | 504990 | 225 | -101.5 | 504990 | 466 |
| MR_1774417023_8F64DE5B | 504990 | 517 | -87.1 | 504990 | 639 | -91.2 | 504990 | 225 | -98.5 | 504990 | 466 |
| MR_1774417023_235DC433 | 504990 | 517 | -85.7 | 504990 | 639 | -89.6 | 504990 | 225 | -100.6 | 504990 | 466 |
| MR_1774417023_D496E0F8 | 504990 | 517 | -85.6 | 504990 | 639 | -92.5 | 504990 | 225 | -100.7 | 504990 | 466 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 945: `6292dcb9-09e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6292dcb9-09e0-4f4a-b231-fa5eb9ed8417` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Decrease A3 Offset threshold for 3222161_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[945] topology](images/train_0945.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3222161_4 and 3213417_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213417_1
- `C3`: Increase A3 Offset threshold for 3213417_1
- `C4`: Adjust the azimuth of 3213417_1 by 28 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222161_4
- `C6`: Increase transmission power for 3213417_1
- `C7`: Press down the tilt angle of 3222161_4 by 10 degrees
- `C8`: Press down the tilt angle  of 3213417_1 by 1 degrees
- `C9`: Check test server and transmission issues
- `C10`: Add neighbor relationship between 3262797_2 and 3213417_1
- `C11`: Adjust the azimuth of 3222161_4 by 9 degrees
- `C12`: Decrease A3 Offset threshold for 3213417_1
- `C13`: Lift the tilt angle of 3222161_4 by 10 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222161_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213417_1
- `C17`: Decrease transmission power for 3213417_1
- `C18`: Decrease A3 Offset threshold for 3222161_4 **← 정답**
- `C19`: Increase transmission power for 3222161_4
- `C20`: Lift the tilt angle  of 3213417_1 by 1 degrees
- `C21`: Decrease transmission power for 3222161_4
- `C22`: Increase A3 Offset threshold for 3222161_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.614 | MS1 | 121.4656757237 | 31.1446286012 | 246 | 504990 | -84.90 | 14.91 | 528.67 | 0.10 | 2.11 | 1562 |
| 2024-09-20 22:21:32.625 | MS1 | 121.4656740424 | 31.1446365686 | 246 | 504990 | -76.25 | 16.95 | 343.62 | 0.07 | 2.84 | 1586 |
| 2024-09-20 22:21:33.966 | MS1 | 121.4656760123 | 31.1446330779 | 246 | 504990 | -75.34 | 15.98 | 380.45 | 0.04 | 2.13 | 1588 |
| 2024-09-20 22:21:34.786 | MS1 | 121.4656683768 | 31.1446283739 | 246 | 504990 | -87.76 | -0.74 | 36.83 | 0.12 | 1.17 | 1581 |
| 2024-09-20 22:21:35.568 | MS1 | 121.4656611040 | 31.1446289793 | 246 | 504990 | -83.30 | -0.98 | 67.54 | 0.10 | 1.16 | 1578 |
| 2024-09-20 22:21:36.777 | MS1 | 121.4656640723 | 31.1446291976 | 246 | 504990 | -83.14 | -1.48 | 63.47 | 0.11 | 1.08 | 1576 |
| 2024-09-20 22:21:37.887 | MS1 | 121.4656591025 | 31.1446303922 | 246 | 504990 | -88.48 | -2.92 | 58.33 | 0.16 | 1.14 | 1583 |
| 2024-09-20 22:21:38.695 | MS1 | 121.4656581218 | 31.1446319129 | 246 | 504990 | -90.67 | -1.10 | 63.49 | 0.08 | 1.29 | 1578 |
| 2024-09-20 22:21:39.372 | MS1 | 121.4656713989 | 31.1446217778 | 994 | 504990 | -84.68 | 12.15 | 189.82 | 0.14 | 1.32 | 1576 |
| 2024-09-20 22:21:40.264 | MS1 | 121.4656684945 | 31.1446279141 | 994 | 504990 | -84.52 | 15.12 | 419.07 | 0.02 | 2.80 | 1568 |
| 2024-09-20 22:21:41.806 | MS1 | 121.4656602026 | 31.1446195998 | 994 | 504990 | -78.04 | 15.87 | 500.57 | 0.00 | 2.04 | 1600 |
| 2024-09-20 22:21:42.988 | MS1 | 121.4656770979 | 31.1446340209 | 994 | 504990 | -83.13 | 16.74 | 586.34 | 0.19 | 2.66 | 1569 |

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
| 3210148 | 3 | 121.4699718446 | 31.1506377059 | 199 | 1 | 4 | 22.1 | TDD | 630 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3213417 | 1 | 121.4695671649 | 31.1515490150 | 234 | 0 | 3 | 20.2 | TDD | 994 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3222161 | 4 | 121.4661835987 | 31.1489773319 | 177 | 11 | 8 | 17.7 | TDD | 246 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3262797 | 2 | 121.4716615374 | 31.1544798172 | 256 | 10 | 9 | 48.0 | TDD | 964 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.400 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.418 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.558 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.558 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.261 | NREventA3 | measId:2;ServCellPCI:919;Se... |
| 2024-09-20 22:21:38.501 | NRHandoverAttempt | SourcePCI:919;SourceNR-ARFC... |
| 2024-09-20 22:21:38.538 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.550 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.653 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.653 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213417 | 1 | 16.8226 | 6.6686 | -115.1314 | 16.3294 | 123.8534 | 0.0179 | 0.0179 |
| 2024_09_20 22:00 | 3262797 | 2 | 17.3807 | 12.0034 | -116.1581 | 6.1598 | 142.5097 | 0.0123 | 0.0034 |
| 2024_09_20 22:00 | 3210148 | 3 | 15.4062 | 19.7484 | -114.3453 | 9.1304 | 127.1151 | 0.0041 | 0.0043 |
| 2024_09_20 22:00 | 3222161 | 4 | 17.2988 | 11.7518 | -115.2323 | 8.9952 | 115.2402 | 0.0057 | 0.1132 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412689_C64F174F | 504990 | 246 | -86.5 | 504990 | 994 | -84.8 | 504990 | 964 | -92.6 | 504990 | 630 |
| MR_1774412689_3EE55AA2 | 504990 | 246 | -87.8 | 504990 | 994 | -81.1 | 504990 | 964 | -92.3 | 504990 | 630 |
| MR_1774412689_236C6470 | 504990 | 246 | -87.3 | 504990 | 994 | -83.6 | 504990 | 964 | -91.8 | 504990 | 630 |
| MR_1774412689_DD014EC6 | 504990 | 246 | -86.3 | 504990 | 994 | -80.9 | 504990 | 964 | -88.8 | 504990 | 630 |
| MR_1774412689_A669913D | 504990 | 246 | -88.1 | 504990 | 994 | -81.1 | 504990 | 964 | -90.3 | 504990 | 630 |
| MR_1774412689_A7695678 | 504990 | 994 | -82.6 | 504990 | 246 | -86.3 | 504990 | 964 | -91.4 | 504990 | 630 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 946: `ff16b76c-ca8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ff16b76c-ca80-473c-83f2-7110718a433e` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3260826_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[946] topology](images/train_0946.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3260826_1 by 4 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248439_4
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease A3 Offset threshold for 3260826_1
- `C5`: Adjust the azimuth of 3248439_4 by 50 degrees
- `C6`: Increase A3 Offset threshold for 3248439_4
- `C7`: Press down the tilt angle of 3260826_1 by 4 degrees
- `C8`: Press down the tilt angle  of 3248439_4 by 10 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248439_4
- `C10`: Increase transmission power for 3248439_4
- `C11`: Check test server and transmission issues
- `C12`: Add neighbor relationship between 3260826_1 and 3248439_4
- `C13`: Increase transmission power for 3260826_1
- `C14`: Add neighbor relationship between 3266364_3 and 3248439_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260826_1
- `C16`: Decrease A3 Offset threshold for 3248439_4
- `C17`: Decrease transmission power for 3260826_1
- `C18`: Lift the tilt angle  of 3248439_4 by 10 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260826_1 **← 정답**
- `C20`: Adjust the azimuth of 3260826_1 by 37 degrees
- `C21`: Increase A3 Offset threshold for 3260826_1
- `C22`: Decrease transmission power for 3248439_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.672 | MS1 | 121.4656733152 | 31.1446298799 | 968 | 504990 | -91.54 | 15.22 | 452.91 | 0.13 | 2.19 | 1562 |
| 2024-09-20 22:21:32.993 | MS1 | 121.4656700767 | 31.1446339351 | 968 | 504990 | -88.40 | 14.78 | 481.16 | 0.11 | 2.24 | 1586 |
| 2024-09-20 22:21:33.178 | MS1 | 121.4656641546 | 31.1446216404 | 968 | 504990 | -85.42 | 16.13 | 436.02 | 0.08 | 2.84 | 1573 |
| 2024-09-20 22:21:34.326 | MS1 | 121.4656736750 | 31.1446213069 | 968 | 504990 | -85.12 | 17.83 | 68.01 | 0.66 | 2.22 | 543 |
| 2024-09-20 22:21:35.720 | MS1 | 121.4656763018 | 31.1446337634 | 968 | 504990 | -90.33 | 14.10 | 86.41 | 0.56 | 2.82 | 625 |
| 2024-09-20 22:21:36.174 | MS1 | 121.4656720992 | 31.1446225803 | 968 | 504990 | -91.96 | 17.96 | 103.15 | 0.54 | 2.11 | 574 |
| 2024-09-20 22:21:37.563 | MS1 | 121.4656765105 | 31.1446348183 | 968 | 504990 | -91.94 | 9.89 | 72.54 | 0.62 | 2.08 | 608 |
| 2024-09-20 22:21:38.461 | MS1 | 121.4656744499 | 31.1446192570 | 968 | 504990 | -92.58 | 8.35 | 92.80 | 0.64 | 2.28 | 645 |
| 2024-09-20 22:21:39.945 | MS1 | 121.4656679108 | 31.1446374170 | 968 | 504990 | -90.23 | 8.39 | 62.11 | 0.59 | 2.69 | 677 |
| 2024-09-20 22:21:40.223 | MS1 | 121.4656706888 | 31.1446291680 | 968 | 504990 | -89.83 | 8.68 | 456.44 | 0.11 | 2.10 | 1600 |
| 2024-09-20 22:21:41.125 | MS1 | 121.4656745001 | 31.1446316829 | 968 | 504990 | -90.50 | 12.91 | 399.08 | 0.06 | 2.35 | 1571 |
| 2024-09-20 22:21:42.254 | MS1 | 121.4656595282 | 31.1446323463 | 968 | 504990 | -90.67 | 12.38 | 581.30 | 0.13 | 2.21 | 1587 |

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
| 3226940 | 2 | 121.4656917198 | 31.1515683943 | 172 | 7 | 5 | 39.4 | TDD | 1003 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3248439 | 4 | 121.4646186795 | 31.1475113383 | 84 | 13 | 8 | 36.6 | TDD | 742 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3260826 | 1 | 121.4750347021 | 31.1445569817 | 308 | 3 | 12 | 16.8 | TDD | 968 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3266364 | 3 | 121.4715563603 | 31.1533126075 | 336 | 2 | 2 | 40.7 | TDD | 837 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.064 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.085 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.210 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.210 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.913 | NREventA3 | measId:2;ServCellPCI:525;Se... |
| 2024-09-20 22:21:38.153 | NRHandoverAttempt | SourcePCI:525;SourceNR-ARFC... |
| 2024-09-20 22:21:38.198 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.209 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.326 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.326 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260826 | 1 | 5.6438 | 16.1788 | -114.2634 | 7.9603 | 187.4781 | 0.0072 | 0.0014 |
| 2024_09_20 22:00 | 3226940 | 2 | 19.9532 | 13.6725 | -114.6806 | 11.5779 | 190.0592 | 0.0012 | 0.0038 |
| 2024_09_20 22:00 | 3266364 | 3 | 8.6526 | 7.0322 | -115.3376 | 13.2320 | 145.8119 | 0.0132 | 0.0094 |
| 2024_09_20 22:00 | 3248439 | 4 | 14.0532 | 8.3476 | -115.7500 | 19.6876 | 177.1054 | 0.0081 | 0.0148 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414308_BC52276A | 504990 | 968 | -84.5 | 504990 | 742 | -91.2 | 504990 | 837 | -94.1 | 504990 | 1003 |
| MR_1774414308_28F6B091 | 504990 | 968 | -86.0 | 504990 | 742 | -90.2 | 504990 | 837 | -94.6 | 504990 | 1003 |
| MR_1774414308_F1E8F67B | 504990 | 968 | -86.0 | 504990 | 742 | -90.8 | 504990 | 837 | -92.1 | 504990 | 1003 |
| MR_1774414308_CAE5D5EA | 504990 | 968 | -84.3 | 504990 | 742 | -88.3 | 504990 | 837 | -92.8 | 504990 | 1003 |
| MR_1774414308_DE046235 | 504990 | 968 | -86.5 | 504990 | 742 | -89.0 | 504990 | 837 | -92.2 | 504990 | 1003 |
| MR_1774414308_7D0A0FC5 | 504990 | 968 | -84.8 | 504990 | 742 | -91.1 | 504990 | 837 | -94.3 | 504990 | 1003 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 947: `6bd8ca1a-2f0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6bd8ca1a-2f06-48fa-93bb-6e62153ad2de` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3268060_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[947] topology](images/train_0947.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278405_2
- `C2`: Press down the tilt angle of 3268060_1 by 3 degrees
- `C3`: Lift the tilt angle of 3268060_1 by 3 degrees
- `C4`: Increase A3 Offset threshold for 3278405_2
- `C5`: Adjust the azimuth of 3278405_2 by 50 degrees
- `C6`: Press down the tilt angle  of 3278405_2 by 9 degrees
- `C7`: Add neighbor relationship between 3251669_4 and 3278405_2
- `C8`: Increase A3 Offset threshold for 3268060_1
- `C9`: Decrease A3 Offset threshold for 3278405_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278405_2
- `C12`: Check test server and transmission issues
- `C13`: Decrease A3 Offset threshold for 3268060_1
- `C14`: Adjust the azimuth of 3268060_1 by 34 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268060_1 **← 정답**
- `C16`: Add neighbor relationship between 3268060_1 and 3278405_2
- `C17`: Decrease transmission power for 3278405_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268060_1
- `C19`: Increase transmission power for 3268060_1
- `C20`: Decrease transmission power for 3268060_1
- `C21`: Increase transmission power for 3278405_2
- `C22`: Lift the tilt angle  of 3278405_2 by 9 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.520 | MS1 | 121.4656712875 | 31.1446182122 | 441 | 504990 | -89.08 | 14.94 | 512.58 | 0.19 | 2.51 | 1579 |
| 2024-09-20 22:21:32.460 | MS1 | 121.4656693883 | 31.1446377328 | 441 | 504990 | -88.85 | 13.82 | 582.28 | 0.05 | 2.44 | 1582 |
| 2024-09-20 22:21:33.738 | MS1 | 121.4656621540 | 31.1446251057 | 441 | 504990 | -88.51 | 16.61 | 428.28 | 0.04 | 2.38 | 1600 |
| 2024-09-20 22:21:34.450 | MS1 | 121.4656645653 | 31.1446368592 | 441 | 504990 | -88.76 | 13.98 | 82.09 | 0.56 | 2.78 | 637 |
| 2024-09-20 22:21:35.766 | MS1 | 121.4656730289 | 31.1446319451 | 441 | 504990 | -90.20 | 13.41 | 75.99 | 0.50 | 2.37 | 534 |
| 2024-09-20 22:21:36.672 | MS1 | 121.4656646350 | 31.1446309443 | 441 | 504990 | -85.72 | 12.22 | 105.44 | 0.56 | 2.78 | 685 |
| 2024-09-20 22:21:37.691 | MS1 | 121.4656773563 | 31.1446319246 | 441 | 504990 | -89.43 | 11.87 | 76.62 | 0.54 | 2.83 | 556 |
| 2024-09-20 22:21:38.441 | MS1 | 121.4656628746 | 31.1446316904 | 441 | 504990 | -90.97 | 11.02 | 95.66 | 0.59 | 2.32 | 626 |
| 2024-09-20 22:21:39.250 | MS1 | 121.4656592311 | 31.1446211156 | 441 | 504990 | -93.21 | 7.75 | 89.10 | 0.53 | 2.77 | 669 |
| 2024-09-20 22:21:40.582 | MS1 | 121.4656713279 | 31.1446371105 | 441 | 504990 | -91.75 | 7.00 | 578.39 | 0.12 | 2.63 | 1562 |
| 2024-09-20 22:21:41.356 | MS1 | 121.4656709321 | 31.1446193624 | 441 | 504990 | -91.60 | 7.20 | 592.18 | 0.05 | 2.89 | 1577 |
| 2024-09-20 22:21:42.768 | MS1 | 121.4656738421 | 31.1446225773 | 441 | 504990 | -90.00 | 12.37 | 317.30 | 0.01 | 2.43 | 1563 |

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
| 3220073 | 3 | 121.4649580773 | 31.1537864393 | 269 | 4 | 8 | 33.3 | TDD | 621 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3251669 | 4 | 121.4693330229 | 31.1553692557 | 67 | 13 | 1 | 25.0 | TDD | 319 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3268060 | 1 | 121.4752086614 | 31.1529974112 | 190 | 1 | 2 | 47.9 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3278405 | 2 | 121.4643305128 | 31.1483655643 | 4 | 5 | 1 | 30.2 | TDD | 362 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.503 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.521 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.665 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.665 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.390 | NREventA3 | measId:2;ServCellPCI:780;Se... |
| 2024-09-20 22:21:38.630 | NRHandoverAttempt | SourcePCI:780;SourceNR-ARFC... |
| 2024-09-20 22:21:38.664 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.678 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.782 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.782 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268060 | 1 | 19.3322 | 6.2585 | -117.9842 | 18.1652 | 80.0918 | 0.0108 | 0.0041 |
| 2024_09_20 22:00 | 3278405 | 2 | 9.7540 | 7.9905 | -117.4104 | 9.5987 | 141.7690 | 0.0109 | 0.0115 |
| 2024_09_20 22:00 | 3220073 | 3 | 18.0086 | 19.8900 | -114.0747 | 12.9476 | 99.2015 | 0.0158 | 0.0132 |
| 2024_09_20 22:00 | 3251669 | 4 | 5.3661 | 8.5117 | -116.3294 | 6.0802 | 162.8888 | 0.0018 | 0.0178 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414859_6B871349 | 504990 | 441 | -87.8 | 504990 | 362 | -91.0 | 504990 | 319 | -97.5 | 504990 | 621 |
| MR_1774414859_2CC077B7 | 504990 | 441 | -86.8 | 504990 | 362 | -90.6 | 504990 | 319 | -98.4 | 504990 | 621 |
| MR_1774414859_BE018150 | 504990 | 441 | -90.4 | 504990 | 362 | -90.9 | 504990 | 319 | -97.5 | 504990 | 621 |
| MR_1774414859_289F895C | 504990 | 441 | -90.6 | 504990 | 362 | -87.9 | 504990 | 319 | -95.3 | 504990 | 621 |
| MR_1774414859_0E6A50F4 | 504990 | 441 | -87.9 | 504990 | 362 | -87.8 | 504990 | 319 | -98.5 | 504990 | 621 |
| MR_1774414859_A8C51439 | 504990 | 441 | -90.4 | 504990 | 362 | -87.7 | 504990 | 319 | -97.4 | 504990 | 621 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 948: `4daa2d69-70c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4daa2d69-70c0-44b7-a438-348d668dba93` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249990_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[948] topology](images/train_0948.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3249990_1 by 23 degrees
- `C2`: Decrease A3 Offset threshold for 3263373_6
- `C3`: Press down the tilt angle of 3249990_1 by 6 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Adjust the azimuth of 3263373_6 by 41 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249990_1
- `C7`: Increase transmission power for 3249990_1
- `C8`: Lift the tilt angle  of 3263373_6 by 6 degrees
- `C9`: Decrease A3 Offset threshold for 3249990_1
- `C10`: Increase A3 Offset threshold for 3249990_1
- `C11`: Press down the tilt angle  of 3263373_6 by 6 degrees
- `C12`: Lift the tilt angle of 3249990_1 by 6 degrees
- `C13`: Increase A3 Offset threshold for 3263373_6
- `C14`: Add neighbor relationship between 3249990_1 and 3263373_6
- `C15`: Decrease transmission power for 3263373_6
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263373_6
- `C17`: Check test server and transmission issues
- `C18`: Decrease transmission power for 3249990_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249990_1 **← 정답**
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263373_6
- `C21`: Increase transmission power for 3263373_6
- `C22`: Add neighbor relationship between 3245617_13 and 3263373_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.904 | MS1 | 121.4656742786 | 31.1446356879 | 36 | 504990 | -95.24 | 9.81 | 358.52 | 0.00 | 2.45 | 1564 |
| 2024-09-20 22:21:32.508 | MS1 | 121.4656655015 | 31.1446374729 | 874 | 504990 | -95.89 | 11.25 | 595.20 | 0.19 | 2.01 | 1591 |
| 2024-09-20 22:21:33.447 | MS1 | 121.4656717403 | 31.1446299271 | 861 | 504990 | -95.32 | 11.22 | 511.89 | 0.19 | 2.70 | 1597 |
| 2024-09-20 22:21:34.883 | MS1 | 121.4656636219 | 31.1446273231 | 241 | 152650 | -88.10 | 2.69 | 68.30 | 0.06 | 1.57 | 973 |
| 2024-09-20 22:21:35.112 | MS1 | 121.4656741773 | 31.1446371401 | 931 | 152650 | -88.42 | 2.36 | 97.34 | 0.07 | 1.79 | 941 |
| 2024-09-20 22:21:36.106 | MS1 | 121.4656741259 | 31.1446284796 | 703 | 152650 | -90.84 | 6.41 | 56.86 | 0.16 | 1.62 | 958 |
| 2024-09-20 22:21:37.968 | MS1 | 121.4656729868 | 31.1446260890 | 332 | 152650 | -89.23 | 4.60 | 67.42 | 0.15 | 1.79 | 934 |
| 2024-09-20 22:21:38.619 | MS1 | 121.4656678967 | 31.1446360849 | 241 | 152650 | -88.43 | 7.74 | 86.87 | 0.06 | 1.68 | 940 |
| 2024-09-20 22:21:39.508 | MS1 | 121.4656592023 | 31.1446348907 | 931 | 152650 | -91.92 | 2.08 | 60.08 | 0.09 | 1.85 | 973 |
| 2024-09-20 22:21:40.718 | MS1 | 121.4656635742 | 31.1446181572 | 703 | 152650 | -89.60 | 3.51 | 87.33 | 0.09 | 2.12 | 1570 |
| 2024-09-20 22:21:41.260 | MS1 | 121.4656737845 | 31.1446192394 | 332 | 152650 | -90.61 | 3.57 | 83.39 | 0.16 | 2.33 | 1595 |
| 2024-09-20 22:21:42.798 | MS1 | 121.4656676412 | 31.1446297132 | 241 | 152650 | -89.11 | 2.96 | 67.09 | 0.18 | 2.15 | 1590 |

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
| 3210965 | 9 | 121.4757426784 | 31.1495481304 | 196 | 7 | 3 | 17.4 | FDD | 332 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3218628 | 8 | 121.4688666827 | 31.1449803008 | 151 | 9 | 4 | 24.1 | FDD | 520 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3224245 | 11 | 121.4676200396 | 31.1553414659 | 128 | 9 | 11 | 12.3 | FDD | 241 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3230538 | 2 | 121.4663529946 | 31.1493563948 | 328 | 10 | 6 | 4.0 | TDD | 614 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3239961 | 5 | 121.4683069398 | 31.1508879691 | 327 | 11 | 1 | 7.6 | TDD | 861 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3245617 | 13 | 121.4680391510 | 31.1509539187 | 1 | 8 | 1 | 3.0 | FDD | 703 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3246416 | 3 | 121.4746610490 | 31.1467776922 | 224 | 0 | 0 | 16.2 | TDD | 8 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3248205 | 12 | 121.4759737008 | 31.1482447414 | 214 | 6 | 4 | 6.0 | FDD | 824 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3249990 | 1 | 121.4742699975 | 31.1555041013 | 237 | 5 | 2 | 20.2 | TDD | 36 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3254610 | 4 | 121.4695961187 | 31.1535353711 | 192 | 1 | 8 | 4.6 | TDD | 874 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3262877 | 10 | 121.4671258939 | 31.1486694666 | 128 | 14 | 2 | 2.2 | FDD | 365 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3263373 | 6 | 121.4647586346 | 31.1523151322 | 215 | 5 | 12 | 8.5 | TDD | 125 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3275863 | 7 | 121.4710048878 | 31.1441678763 | 320 | 3 | 4 | 7.5 | FDD | 931 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |

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
| 2024-09-20 22:21:30.977 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.127 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.127 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.832 | NREventA2 | measId:1;ServCellPCI:308;Se... |
| 2024-09-20 22:21:34.940 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.207 | NREventA5 | measId:3;ServCellPCI:308;Se... |
| 2024-09-20 22:21:35.268 | NRHandoverAttempt | SourcePCI:308;SourceNR-ARFC... |
| 2024-09-20 22:21:35.297 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.311 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.427 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.427 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249990 | 1 | 18.1044 | 10.4738 | -115.9397 | 9.7878 | 176.9308 | 0.0113 | 0.0110 |
| 2024_09_20 22:00 | 3230538 | 2 | 13.9197 | 6.8405 | -115.9890 | 19.7223 | 174.3510 | 0.0180 | 0.0131 |
| 2024_09_20 22:00 | 3246416 | 3 | 14.5886 | 7.5184 | -114.5040 | 12.9965 | 178.8020 | 0.0058 | 0.0080 |
| 2024_09_20 22:00 | 3254610 | 4 | 5.9076 | 12.8821 | -116.4349 | 17.7056 | 145.7313 | 0.0044 | 0.0108 |
| 2024_09_20 22:00 | 3239961 | 5 | 16.7536 | 17.4689 | -117.9999 | 18.9378 | 178.3276 | 0.0151 | 0.0086 |
| 2024_09_20 22:00 | 3263373 | 6 | 19.6025 | 17.4403 | -115.1520 | 18.9109 | 90.1460 | 0.0035 | 0.0011 |
| 2024_09_20 22:00 | 3275863 | 7 | 10.6958 | 15.0700 | -115.2829 | 3.8456 | 31.6101 | 0.0085 | 0.0082 |
| 2024_09_20 22:00 | 3218628 | 8 | 10.0263 | 5.5387 | -114.0074 | 4.2077 | 49.7229 | 0.0020 | 0.0039 |
| 2024_09_20 22:00 | 3210965 | 9 | 16.0269 | 19.2980 | -116.8480 | 4.8728 | 26.1109 | 0.0159 | 0.0095 |
| 2024_09_20 22:00 | 3262877 | 10 | 9.1551 | 10.9429 | -117.6329 | 3.3280 | 37.0339 | 0.0181 | 0.0050 |
| 2024_09_20 22:00 | 3224245 | 11 | 7.8480 | 5.1913 | -114.3897 | 4.1745 | 50.8071 | 0.0172 | 0.0174 |
| 2024_09_20 22:00 | 3248205 | 12 | 9.0360 | 5.0506 | -115.7782 | 3.1241 | 44.0189 | 0.0175 | 0.0026 |
| 2024_09_20 22:00 | 3245617 | 13 | 7.1053 | 10.8109 | -116.7020 | 3.9764 | 38.4862 | 0.0031 | 0.0056 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416792_6FBEDED1 | 504990 | 861 | -96.7 | 504990 | 125 | -96.7 | 504990 | 8 | -101.4 | 504990 | 614 |
| MR_1774416792_CAADD1D2 | 504990 | 861 | -94.8 | 504990 | 125 | -95.5 | 504990 | 8 | -102.0 | 504990 | 614 |
| MR_1774416792_9761E365 | 152650 | 241 | -89.6 | 152650 | 520 | -93.5 | 152650 | 824 | -99.0 | 152650 | 365 |
| MR_1774416792_BF9B2539 | 504990 | 861 | -96.1 | 504990 | 125 | -94.2 | 504990 | 8 | -99.8 | 504990 | 614 |
| MR_1774416792_EBA53525 | 152650 | 241 | -88.6 | 152650 | 520 | -93.4 | 152650 | 824 | -99.5 | 152650 | 365 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 949: `af7f8d8e-2dc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `af7f8d8e-2dc7-40de-b093-577be6b5d359` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Decrease A3 Offset threshold for 3231533_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[949] topology](images/train_0949.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3249542_4 by 8 degrees
- `C2`: Decrease transmission power for 3249542_4
- `C3`: Press down the tilt angle of 3231533_1 by 7 degrees
- `C4`: Decrease A3 Offset threshold for 3231533_1 **← 정답**
- `C5`: Decrease transmission power for 3231533_1
- `C6`: Increase A3 Offset threshold for 3249542_4
- `C7`: Add neighbor relationship between 3237724_3 and 3249542_4
- `C8`: Increase transmission power for 3231533_1
- `C9`: Check test server and transmission issues
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231533_1
- `C11`: Increase transmission power for 3249542_4
- `C12`: Press down the tilt angle  of 3249542_4 by 8 degrees
- `C13`: Increase A3 Offset threshold for 3231533_1
- `C14`: Decrease A3 Offset threshold for 3249542_4
- `C15`: Add neighbor relationship between 3231533_1 and 3249542_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231533_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249542_4
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249542_4
- `C20`: Adjust the azimuth of 3249542_4 by 50 degrees
- `C21`: Adjust the azimuth of 3231533_1 by 50 degrees
- `C22`: Lift the tilt angle of 3231533_1 by 7 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.702 | MS1 | 121.4656624225 | 31.1446296086 | 232 | 504990 | -77.24 | 17.60 | 408.43 | 0.17 | 2.72 | 1596 |
| 2024-09-20 22:21:32.934 | MS1 | 121.4656652635 | 31.1446308731 | 232 | 504990 | -82.72 | 16.59 | 587.56 | 0.08 | 2.29 | 1562 |
| 2024-09-20 22:21:33.104 | MS1 | 121.4656672045 | 31.1446296202 | 232 | 504990 | -83.89 | 16.66 | 582.07 | 0.09 | 2.18 | 1577 |
| 2024-09-20 22:21:34.729 | MS1 | 121.4656721997 | 31.1446266952 | 232 | 504990 | -89.92 | -3.06 | 52.40 | 0.00 | 1.26 | 1591 |
| 2024-09-20 22:21:35.158 | MS1 | 121.4656710140 | 31.1446363208 | 232 | 504990 | -87.00 | -2.80 | 76.49 | 0.18 | 1.44 | 1561 |
| 2024-09-20 22:21:36.477 | MS1 | 121.4656642133 | 31.1446350505 | 232 | 504990 | -92.91 | -1.99 | 28.61 | 0.05 | 1.49 | 1576 |
| 2024-09-20 22:21:37.695 | MS1 | 121.4656730803 | 31.1446230996 | 232 | 504990 | -88.48 | -2.24 | 34.53 | 0.09 | 1.37 | 1590 |
| 2024-09-20 22:21:38.274 | MS1 | 121.4656656812 | 31.1446334865 | 232 | 504990 | -90.47 | -3.26 | 51.24 | 0.14 | 1.29 | 1588 |
| 2024-09-20 22:21:39.397 | MS1 | 121.4656723083 | 31.1446269348 | 254 | 504990 | -79.63 | 12.03 | 220.41 | 0.01 | 1.03 | 1592 |
| 2024-09-20 22:21:40.765 | MS1 | 121.4656582015 | 31.1446344151 | 254 | 504990 | -78.83 | 16.95 | 423.29 | 0.06 | 2.22 | 1582 |
| 2024-09-20 22:21:41.813 | MS1 | 121.4656773823 | 31.1446259127 | 254 | 504990 | -76.87 | 15.11 | 364.42 | 0.08 | 2.71 | 1584 |
| 2024-09-20 22:21:42.612 | MS1 | 121.4656743089 | 31.1446212102 | 254 | 504990 | -76.95 | 14.85 | 321.37 | 0.20 | 2.83 | 1586 |

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
| 3231533 | 1 | 121.4703206974 | 31.1529136584 | 38 | 6 | 9 | 19.5 | TDD | 232 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3237724 | 3 | 121.4691265846 | 31.1483864143 | 104 | 4 | 2 | 44.9 | TDD | 274 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3249542 | 4 | 121.4740789781 | 31.1502896448 | 1 | 5 | 6 | 47.8 | TDD | 254 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3255491 | 2 | 121.4687137960 | 31.1441095783 | 68 | 14 | 8 | 37.2 | TDD | 361 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.119 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.134 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.252 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.252 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.955 | NREventA3 | measId:2;ServCellPCI:868;Se... |
| 2024-09-20 22:21:38.195 | NRHandoverAttempt | SourcePCI:868;SourceNR-ARFC... |
| 2024-09-20 22:21:38.243 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.254 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.370 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.370 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231533 | 1 | 11.4336 | 10.7902 | -115.9541 | 7.4129 | 87.1215 | 0.0002 | 0.1018 |
| 2024_09_20 22:00 | 3255491 | 2 | 17.7414 | 7.4439 | -117.6589 | 11.3549 | 102.6105 | 0.0101 | 0.0060 |
| 2024_09_20 22:00 | 3237724 | 3 | 15.5416 | 15.6939 | -116.6675 | 19.1373 | 101.2680 | 0.0037 | 0.0033 |
| 2024_09_20 22:00 | 3249542 | 4 | 10.5759 | 15.4099 | -116.1465 | 18.5957 | 193.0812 | 0.0163 | 0.0029 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414673_683801E2 | 504990 | 254 | -82.9 | 504990 | 232 | -90.0 | 504990 | 274 | -87.5 | 504990 | 361 |
| MR_1774414673_215C4907 | 504990 | 254 | -84.6 | 504990 | 232 | -90.6 | 504990 | 274 | -85.7 | 504990 | 361 |
| MR_1774414673_C2A326F6 | 504990 | 254 | -83.4 | 504990 | 232 | -91.7 | 504990 | 274 | -86.0 | 504990 | 361 |
| MR_1774414673_83842D2F | 504990 | 232 | -91.6 | 504990 | 254 | -84.4 | 504990 | 274 | -87.0 | 504990 | 361 |
| MR_1774414673_E3167CDC | 504990 | 254 | -85.6 | 504990 | 232 | -89.0 | 504990 | 274 | -86.0 | 504990 | 361 |
| MR_1774414673_D2A41315 | 504990 | 232 | -91.7 | 504990 | 254 | -83.4 | 504990 | 274 | -86.6 | 504990 | 361 |
| MR_1774414673_83D70225 | 504990 | 254 | -83.4 | 504990 | 232 | -89.6 | 504990 | 274 | -86.1 | 504990 | 361 |
| MR_1774414673_289D9B91 | 504990 | 254 | -83.4 | 504990 | 232 | -89.6 | 504990 | 274 | -86.5 | 504990 | 361 |

> *... 2개 열 생략 (전체 14열)*

---
