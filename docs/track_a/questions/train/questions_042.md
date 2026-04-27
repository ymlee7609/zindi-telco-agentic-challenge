# Track A 문제 분석 — train[410]~train[419]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[410] ~ train[419] (10개)

## 목차

1. [문제 410: `e915921f-40e...`](#410) — single-answer, 정답: C15
2. [문제 411: `8e7f4c24-c18...`](#411) — multiple-answer, 정답: C7|C22
3. [문제 412: `63791e7d-063...`](#412) — multiple-answer, 정답: C2|C7|C21|C22
4. [문제 413: `ed67871b-790...`](#413) — single-answer, 정답: C5
5. [문제 414: `2c5f174c-38f...`](#414) — single-answer, 정답: C5
6. [문제 415: `57e38e11-713...`](#415) — single-answer, 정답: C19
7. [문제 416: `58a7f807-062...`](#416) — single-answer, 정답: C9
8. [문제 417: `6d384ff3-ccb...`](#417) — single-answer, 정답: C5
9. [문제 418: `f159a660-768...`](#418) — single-answer, 정답: C14
10. [문제 419: `eccdc0a1-06c...`](#419) — single-answer, 정답: C20

---

### 문제 410: `e915921f-40e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e915921f-40e8-4a18-aad2-f744175f2312` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271970_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[410] topology](images/train_0410.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271970_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243868_6
- `C3`: Check test server and transmission issues
- `C4`: Increase A3 Offset threshold for 3243868_6
- `C5`: Add neighbor relationship between 3221655_11 and 3243868_6
- `C6`: Increase transmission power for 3243868_6
- `C7`: Press down the tilt angle of 3271970_3 by 6 degrees
- `C8`: Decrease transmission power for 3243868_6
- `C9`: Lift the tilt angle of 3271970_3 by 6 degrees
- `C10`: Press down the tilt angle  of 3243868_6 by 0 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243868_6
- `C12`: Decrease A3 Offset threshold for 3243868_6
- `C13`: Adjust the azimuth of 3271970_3 by 8 degrees
- `C14`: Decrease A3 Offset threshold for 3271970_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271970_3 **← 정답**
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase transmission power for 3271970_3
- `C18`: Lift the tilt angle  of 3243868_6 by 0 degrees
- `C19`: Decrease transmission power for 3271970_3
- `C20`: Increase A3 Offset threshold for 3271970_3
- `C21`: Adjust the azimuth of 3243868_6 by 12 degrees
- `C22`: Add neighbor relationship between 3271970_3 and 3243868_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.510 | MS1 | 121.4656660216 | 31.1446252234 | 982 | 504990 | -95.86 | 10.53 | 548.34 | 0.12 | 2.50 | 1562 |
| 2024-09-20 22:21:32.693 | MS1 | 121.4656588621 | 31.1446190716 | 215 | 504990 | -94.52 | 11.47 | 586.99 | 0.19 | 2.35 | 1574 |
| 2024-09-20 22:21:33.417 | MS1 | 121.4656665211 | 31.1446226277 | 386 | 504990 | -93.09 | 10.48 | 537.43 | 0.01 | 2.30 | 1598 |
| 2024-09-20 22:21:34.726 | MS1 | 121.4656689376 | 31.1446306033 | 731 | 152650 | -94.97 | 5.06 | 90.07 | 0.09 | 1.84 | 905 |
| 2024-09-20 22:21:35.497 | MS1 | 121.4656654872 | 31.1446196269 | 275 | 152650 | -93.71 | 5.88 | 76.48 | 0.14 | 1.52 | 945 |
| 2024-09-20 22:21:36.481 | MS1 | 121.4656603620 | 31.1446233441 | 56 | 152650 | -87.87 | 3.84 | 53.64 | 0.15 | 1.57 | 968 |
| 2024-09-20 22:21:37.617 | MS1 | 121.4656762248 | 31.1446365270 | 105 | 152650 | -92.22 | 4.01 | 73.77 | 0.01 | 1.54 | 935 |
| 2024-09-20 22:21:38.797 | MS1 | 121.4656648390 | 31.1446244193 | 731 | 152650 | -89.63 | 6.69 | 55.29 | 0.16 | 1.83 | 983 |
| 2024-09-20 22:21:39.778 | MS1 | 121.4656611504 | 31.1446306499 | 275 | 152650 | -96.88 | 3.71 | 79.15 | 0.14 | 1.62 | 977 |
| 2024-09-20 22:21:40.370 | MS1 | 121.4656703505 | 31.1446341692 | 56 | 152650 | -88.73 | 3.60 | 71.38 | 0.05 | 2.21 | 1584 |
| 2024-09-20 22:21:41.945 | MS1 | 121.4656770595 | 31.1446282606 | 105 | 152650 | -93.41 | 2.13 | 85.56 | 0.04 | 2.05 | 1570 |
| 2024-09-20 22:21:42.123 | MS1 | 121.4656617889 | 31.1446265016 | 731 | 152650 | -87.65 | 5.19 | 86.65 | 0.19 | 2.95 | 1584 |

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
| 3210627 | 4 | 121.4697884089 | 31.1484559483 | 300 | 11 | 12 | 7.7 | TDD | 215 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3221655 | 11 | 121.4720496364 | 31.1454380459 | 242 | 1 | 7 | 5.3 | FDD | 56 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3222526 | 5 | 121.4736379769 | 31.1539343001 | 170 | 9 | 4 | 16.6 | TDD | 952 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3222726 | 10 | 121.4737439606 | 31.1454965793 | 3 | 13 | 7 | 4.2 | FDD | 275 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3239114 | 12 | 121.4664745428 | 31.1507779054 | 89 | 15 | 12 | 18.6 | FDD | 731 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3243868 | 6 | 121.4714948690 | 31.1459541890 | 243 | 0 | 4 | 1.4 | TDD | 699 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3247226 | 8 | 121.4696686816 | 31.1447611135 | 290 | 11 | 0 | 7.4 | FDD | 360 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3257483 | 13 | 121.4677516994 | 31.1458637350 | 241 | 7 | 3 | 21.0 | FDD | 605 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3262578 | 2 | 121.4709534184 | 31.1454684487 | 249 | 11 | 12 | 19.8 | TDD | 211 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3267547 | 9 | 121.4746695260 | 31.1441176067 | 193 | 11 | 8 | 16.3 | FDD | 105 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3268101 | 1 | 121.4654544840 | 31.1500703421 | 276 | 13 | 0 | 16.9 | TDD | 386 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3271970 | 3 | 121.4719735353 | 31.1447227946 | 277 | 4 | 10 | 18.3 | TDD | 982 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3277360 | 7 | 121.4700537856 | 31.1524146062 | 118 | 3 | 0 | 19.7 | FDD | 551 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |

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
| 2024-09-20 22:21:31.277 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.301 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.441 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.441 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.092 | NREventA2 | measId:1;ServCellPCI:691;Se... |
| 2024-09-20 22:21:35.214 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.465 | NREventA5 | measId:3;ServCellPCI:691;Se... |
| 2024-09-20 22:21:35.507 | NRHandoverAttempt | SourcePCI:691;SourceNR-ARFC... |
| 2024-09-20 22:21:35.527 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.539 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.663 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.663 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268101 | 1 | 5.5623 | 14.8901 | -114.4405 | 5.7617 | 162.4026 | 0.0078 | 0.0153 |
| 2024_09_20 22:00 | 3262578 | 2 | 11.1731 | 13.7311 | -114.0322 | 17.0547 | 153.7736 | 0.0099 | 0.0172 |
| 2024_09_20 22:00 | 3271970 | 3 | 19.2409 | 17.1201 | -115.1592 | 9.8030 | 136.5526 | 0.0015 | 0.0184 |
| 2024_09_20 22:00 | 3210627 | 4 | 17.9865 | 18.1373 | -116.6224 | 14.7604 | 147.2133 | 0.0190 | 0.0092 |
| 2024_09_20 22:00 | 3222526 | 5 | 9.1794 | 14.9881 | -114.3790 | 18.4058 | 124.8910 | 0.0153 | 0.0108 |
| 2024_09_20 22:00 | 3243868 | 6 | 15.6206 | 11.1461 | -114.4329 | 17.3383 | 183.5475 | 0.0030 | 0.0121 |
| 2024_09_20 22:00 | 3277360 | 7 | 7.7806 | 16.7895 | -116.9357 | 3.1856 | 31.4130 | 0.0116 | 0.0073 |
| 2024_09_20 22:00 | 3247226 | 8 | 15.2236 | 17.0198 | -115.7790 | 3.7252 | 21.4074 | 0.0110 | 0.0072 |
| 2024_09_20 22:00 | 3267547 | 9 | 17.9884 | 18.3929 | -116.9645 | 4.9792 | 30.7345 | 0.0194 | 0.0116 |
| 2024_09_20 22:00 | 3222726 | 10 | 7.2844 | 11.9123 | -114.4672 | 4.5988 | 49.1543 | 0.0033 | 0.0102 |
| 2024_09_20 22:00 | 3221655 | 11 | 7.5669 | 13.1100 | -117.9122 | 3.0841 | 55.5625 | 0.0001 | 0.0075 |
| 2024_09_20 22:00 | 3239114 | 12 | 9.3055 | 8.0262 | -117.3580 | 3.2064 | 57.5528 | 0.0126 | 0.0013 |
| 2024_09_20 22:00 | 3257483 | 13 | 17.6430 | 7.1730 | -116.0033 | 3.6875 | 28.4467 | 0.0124 | 0.0093 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415647_1642133B | 504990 | 386 | -94.4 | 504990 | 699 | -98.3 | 504990 | 952 | -96.6 | 504990 | 211 |
| MR_1774415647_267A7197 | 152650 | 731 | -93.7 | 152650 | 360 | -100.0 | 152650 | 551 | -106.3 | 152650 | 605 |
| MR_1774415647_1BA61349 | 152650 | 731 | -94.9 | 152650 | 360 | -98.5 | 152650 | 551 | -106.6 | 152650 | 605 |
| MR_1774415647_F8232A9B | 504990 | 386 | -91.9 | 504990 | 699 | -96.2 | 504990 | 952 | -96.7 | 504990 | 211 |
| MR_1774415647_BB082BA4 | 504990 | 386 | -93.1 | 504990 | 699 | -98.4 | 504990 | 952 | -97.0 | 504990 | 211 |
| MR_1774415647_670F22E5 | 152650 | 731 | -95.7 | 152650 | 360 | -99.6 | 152650 | 551 | -105.1 | 152650 | 605 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 411: `8e7f4c24-c18...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8e7f4c24-c188-4463-a267-2cbfde6e5332` |
| Tag | **multiple-answer** |
| 정답 | **C7|C22** |
| C7 의미 | Decrease transmission power for 3235487_1 |
| C22 의미 | Press down the tilt angle  of 3235487_1 by 3 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[411] topology](images/train_0411.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3235487_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225596_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225596_2
- `C4`: Increase transmission power for 3235487_1
- `C5`: Increase transmission power for 3225596_2
- `C6`: Decrease A3 Offset threshold for 3225596_2
- `C7`: Decrease transmission power for 3235487_1 **← 정답**
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235487_1
- `C10`: Press down the tilt angle of 3225596_2 by 4 degrees
- `C11`: Check test server and transmission issues
- `C12`: Decrease transmission power for 3225596_2
- `C13`: Lift the tilt angle  of 3235487_1 by 3 degrees
- `C14`: Adjust the azimuth of 3235487_1 by 19 degrees
- `C15`: Increase A3 Offset threshold for 3225596_2
- `C16`: Add neighbor relationship between 3218855_3 and 3235487_1
- `C17`: Decrease A3 Offset threshold for 3235487_1
- `C18`: Add neighbor relationship between 3225596_2 and 3235487_1
- `C19`: Adjust the azimuth of 3225596_2 by 28 degrees
- `C20`: Lift the tilt angle of 3225596_2 by 4 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235487_1
- `C22`: Press down the tilt angle  of 3235487_1 by 3 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.630 | MS1 | 121.4656626380 | 31.1446191648 | 652 | 504990 | -79.54 | 14.22 | 430.05 | 0.07 | 2.20 | 1590 |
| 2024-09-20 22:21:32.718 | MS1 | 121.4656623101 | 31.1446243775 | 652 | 504990 | -78.82 | 12.84 | 560.34 | 0.06 | 2.89 | 1561 |
| 2024-09-20 22:21:33.720 | MS1 | 121.4656644718 | 31.1446341075 | 652 | 504990 | -78.28 | 17.41 | 348.17 | 0.13 | 2.27 | 1572 |
| 2024-09-20 22:21:34.979 | MS1 | 121.4656621063 | 31.1446343094 | 652 | 504990 | -88.39 | 3.54 | 39.46 | 0.06 | 1.27 | 1594 |
| 2024-09-20 22:21:35.177 | MS1 | 121.4656739080 | 31.1446225342 | 652 | 504990 | -89.77 | 2.85 | 32.64 | 0.13 | 1.22 | 1588 |
| 2024-09-20 22:21:36.197 | MS1 | 121.4656709671 | 31.1446270089 | 652 | 504990 | -90.75 | 0.13 | 75.10 | 0.15 | 1.33 | 1575 |
| 2024-09-20 22:21:37.493 | MS1 | 121.4656778001 | 31.1446365587 | 652 | 504990 | -89.58 | 2.18 | 79.52 | 0.06 | 1.19 | 1565 |
| 2024-09-20 22:21:38.297 | MS1 | 121.4656645828 | 31.1446238077 | 652 | 504990 | -92.44 | 3.62 | 64.32 | 0.08 | 1.25 | 1587 |
| 2024-09-20 22:21:39.302 | MS1 | 121.4656640799 | 31.1446306210 | 652 | 504990 | -94.66 | 1.57 | 75.12 | 0.16 | 1.08 | 1572 |
| 2024-09-20 22:21:40.982 | MS1 | 121.4656694736 | 31.1446265461 | 652 | 504990 | -76.71 | 13.79 | 388.40 | 0.01 | 2.60 | 1598 |
| 2024-09-20 22:21:41.379 | MS1 | 121.4656710098 | 31.1446222683 | 652 | 504990 | -77.43 | 15.61 | 508.57 | 0.17 | 2.46 | 1562 |
| 2024-09-20 22:21:42.581 | MS1 | 121.4656602856 | 31.1446258877 | 652 | 504990 | -80.18 | 12.99 | 368.30 | 0.11 | 2.24 | 1589 |

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
| 3211221 | 4 | 121.4695977914 | 31.1499302209 | 294 | 11 | 12 | 39.7 | TDD | 313 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3218855 | 3 | 121.4716633312 | 31.1520610162 | 138 | 2 | 0 | 19.1 | TDD | 580 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3225596 | 2 | 121.4688256145 | 31.1494182793 | 181 | 2 | 4 | 22.0 | TDD | 652 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3235487 | 1 | 121.4709599540 | 31.1499696473 | 239 | 2 | 11 | 16.3 | TDD | 905 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.543 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.568 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.682 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.682 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235487 | 1 | 14.3343 | 9.6788 | -115.1917 | 5.1013 | 199.6519 | 0.0151 | 0.0175 |
| 2024_09_20 22:00 | 3225596 | 2 | 6.8547 | 16.2890 | -108.2493 | 9.9232 | 84.3011 | 0.0188 | 0.0015 |
| 2024_09_20 22:00 | 3218855 | 3 | 16.1716 | 13.1796 | -117.0126 | 9.2536 | 166.4978 | 0.0100 | 0.0156 |
| 2024_09_20 22:00 | 3211221 | 4 | 10.3858 | 17.4987 | -117.9492 | 9.3377 | 108.3562 | 0.0087 | 0.0139 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414041_817DC34B | 504990 | 652 | -88.8 | 504990 | 905 | -88.3 | 504990 | 580 | -87.7 | 504990 | 313 |
| MR_1774414041_891506D5 | 504990 | 905 | -89.7 | 504990 | 652 | -86.9 | 504990 | 580 | -87.9 | 504990 | 313 |
| MR_1774414041_7EAC4C56 | 504990 | 905 | -90.0 | 504990 | 652 | -87.6 | 504990 | 580 | -87.0 | 504990 | 313 |
| MR_1774414041_98C6C8DB | 504990 | 652 | -89.1 | 504990 | 905 | -86.5 | 504990 | 580 | -85.4 | 504990 | 313 |
| MR_1774414041_F159430D | 504990 | 905 | -88.9 | 504990 | 652 | -85.0 | 504990 | 580 | -87.5 | 504990 | 313 |
| MR_1774414041_DA8787BB | 504990 | 905 | -89.9 | 504990 | 652 | -88.5 | 504990 | 580 | -86.0 | 504990 | 313 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 412: `63791e7d-063...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `63791e7d-0638-4293-8d77-11fa0d01c2c0` |
| Tag | **multiple-answer** |
| 정답 | **C2|C7|C21|C22** |
| C2 의미 | Increase A3 Offset threshold for 3228334_1 |
| C7 의미 | Increase A3 Offset threshold for 3266925_3 |
| C21 의미 | Press down the tilt angle  of 3266925_3 by 6 degrees |
| C22 의미 | Decrease transmission power for 3266925_3 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[412] topology](images/train_0412.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3228334_1 by 6 degrees
- `C2`: Increase A3 Offset threshold for 3228334_1 **← 정답**
- `C3`: Decrease transmission power for 3228334_1
- `C4`: Add neighbor relationship between 3228334_1 and 3266925_3
- `C5`: Check test server and transmission issues
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266925_3
- `C7`: Increase A3 Offset threshold for 3266925_3 **← 정답**
- `C8`: Increase transmission power for 3228334_1
- `C9`: Decrease A3 Offset threshold for 3228334_1
- `C10`: Lift the tilt angle  of 3266925_3 by 6 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228334_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266925_3
- `C14`: Press down the tilt angle of 3228334_1 by 6 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228334_1
- `C16`: Adjust the azimuth of 3266925_3 by 20 degrees
- `C17`: Adjust the azimuth of 3228334_1 by 7 degrees
- `C18`: Increase transmission power for 3266925_3
- `C19`: Add neighbor relationship between 3267817_5 and 3266925_3
- `C20`: Decrease A3 Offset threshold for 3266925_3
- `C21`: Press down the tilt angle  of 3266925_3 by 6 degrees **← 정답**
- `C22`: Decrease transmission power for 3266925_3 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.717 | MS1 | 121.4656587255 | 31.1446230259 | 224 | 504990 | -81.92 | 16.10 | 586.66 | 0.00 | 2.30 | 1560 |
| 2024-09-20 22:21:32.713 | MS1 | 121.4656693124 | 31.1446279225 | 224 | 504990 | -77.24 | 14.38 | 481.24 | 0.06 | 2.03 | 1566 |
| 2024-09-20 22:21:33.704 | MS1 | 121.4656630368 | 31.1446278794 | 224 | 504990 | -76.99 | 15.06 | 469.85 | 0.06 | 2.28 | 1567 |
| 2024-09-20 22:21:34.564 | MS1 | 121.4656763776 | 31.1446337534 | 392 | 504990 | -80.98 | 4.66 | 81.39 | 0.16 | 1.35 | 1563 |
| 2024-09-20 22:21:35.366 | MS1 | 121.4656753413 | 31.1446247901 | 392 | 504990 | -87.48 | 3.97 | 53.52 | 0.10 | 1.43 | 1566 |
| 2024-09-20 22:21:36.610 | MS1 | 121.4656731141 | 31.1446325870 | 224 | 504990 | -82.25 | 4.25 | 68.95 | 0.06 | 1.31 | 1584 |
| 2024-09-20 22:21:37.215 | MS1 | 121.4656584022 | 31.1446183339 | 224 | 504990 | -83.09 | 4.28 | 75.38 | 0.16 | 1.37 | 1565 |
| 2024-09-20 22:21:38.398 | MS1 | 121.4656673506 | 31.1446230680 | 392 | 504990 | -89.70 | 3.53 | 42.89 | 0.15 | 1.34 | 1561 |
| 2024-09-20 22:21:39.735 | MS1 | 121.4656642280 | 31.1446223627 | 392 | 504990 | -84.13 | 3.26 | 69.46 | 0.15 | 1.29 | 1569 |
| 2024-09-20 22:21:40.140 | MS1 | 121.4656741585 | 31.1446324020 | 392 | 504990 | -75.97 | 17.79 | 400.83 | 0.19 | 2.97 | 1596 |
| 2024-09-20 22:21:41.160 | MS1 | 121.4656651731 | 31.1446299167 | 392 | 504990 | -84.08 | 17.78 | 525.80 | 0.14 | 2.46 | 1583 |
| 2024-09-20 22:21:42.351 | MS1 | 121.4656636491 | 31.1446368057 | 392 | 504990 | -81.03 | 12.58 | 361.06 | 0.03 | 2.17 | 1567 |

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
| 3228334 | 1 | 121.4674273755 | 31.1508750404 | 201 | 3 | 9 | 35.2 | TDD | 224 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3255795 | 2 | 121.4672930727 | 31.1555575240 | 230 | 15 | 6 | 18.8 | TDD | 392 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3261631 | 4 | 121.4708620510 | 31.1473335167 | 94 | 4 | 11 | 41.0 | TDD | 504 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3266925 | 3 | 121.4724018945 | 31.1445649253 | 251 | 2 | 10 | 39.9 | TDD | 363 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3267817 | 5 | 121.4660141753 | 31.1511610097 | 266 | 9 | 5 | 48.8 | TDD | 700 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.432 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.455 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.563 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.563 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.291 | NREventA3 | measId:2;ServCellPCI:56;Ser... |
| 2024-09-20 22:21:34.531 | NRHandoverAttempt | SourcePCI:56;SourceNR-ARFCN... |
| 2024-09-20 22:21:34.576 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.591 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.718 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.718 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.291 | NREventA3 | measId:2;ServCellPCI:661;Se... |
| 2024-09-20 22:21:36.531 | NRHandoverAttempt | SourcePCI:661;SourceNR-ARFC... |
| 2024-09-20 22:21:36.566 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.580 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.702 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.702 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.291 | NREventA3 | measId:2;ServCellPCI:56;Ser... |
| 2024-09-20 22:21:38.531 | NRHandoverAttempt | SourcePCI:56;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.578 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.588 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.736 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.736 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228334 | 1 | 19.4643 | 13.5489 | -116.9688 | 18.1738 | 179.1586 | 0.0025 | 0.0162 |
| 2024_09_20 22:00 | 3255795 | 2 | 17.2787 | 5.5542 | -114.6143 | 11.6627 | 173.3412 | 0.0161 | 0.0139 |
| 2024_09_20 22:00 | 3266925 | 3 | 5.6794 | 11.3910 | -116.7330 | 11.3312 | 145.2681 | 0.0151 | 0.0173 |
| 2024_09_20 22:00 | 3261631 | 4 | 8.4776 | 8.3093 | -117.2100 | 19.5381 | 180.2198 | 0.0057 | 0.0064 |
| 2024_09_20 22:00 | 3267817 | 5 | 10.3305 | 8.8132 | -117.6063 | 14.8510 | 156.4241 | 0.0139 | 0.0197 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412230_75D91BC4 | 504990 | 392 | -82.8 | 504990 | 224 | -79.6 | 504990 | 363 | -80.6 | 504990 | 700 |
| MR_1774412230_47E7DE43 | 504990 | 392 | -82.1 | 504990 | 224 | -81.2 | 504990 | 363 | -84.3 | 504990 | 700 |
| MR_1774412230_CDAEF478 | 504990 | 224 | -81.7 | 504990 | 392 | -80.0 | 504990 | 363 | -82.1 | 504990 | 700 |
| MR_1774412230_E1998388 | 504990 | 224 | -80.0 | 504990 | 392 | -80.5 | 504990 | 363 | -82.8 | 504990 | 700 |
| MR_1774412230_75614D02 | 504990 | 392 | -81.9 | 504990 | 224 | -81.0 | 504990 | 363 | -80.7 | 504990 | 700 |
| MR_1774412230_26A35EBF | 504990 | 392 | -80.1 | 504990 | 224 | -78.8 | 504990 | 363 | -81.4 | 504990 | 700 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 413: `ed67871b-790...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ed67871b-7904-4663-bdf6-ce7fd0a17eb8` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Add neighbor relationship between 3273573_2 and 3279852_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[413] topology](images/train_0413.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3279852_1
- `C2`: Increase A3 Offset threshold for 3273573_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279852_1
- `C4`: Increase transmission power for 3279852_1
- `C5`: Add neighbor relationship between 3273573_2 and 3279852_1 **← 정답**
- `C6`: Lift the tilt angle of 3273573_2 by 6 degrees
- `C7`: Lift the tilt angle  of 3279852_1 by 2 degrees
- `C8`: Increase A3 Offset threshold for 3279852_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273573_2
- `C10`: Decrease transmission power for 3279852_1
- `C11`: Press down the tilt angle of 3273573_2 by 6 degrees
- `C12`: Adjust the azimuth of 3273573_2 by 35 degrees
- `C13`: Decrease transmission power for 3273573_2
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase transmission power for 3273573_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273573_2
- `C17`: Decrease A3 Offset threshold for 3273573_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279852_1
- `C19`: Press down the tilt angle  of 3279852_1 by 2 degrees
- `C20`: Add neighbor relationship between 3259611_3 and 3279852_1
- `C21`: Adjust the azimuth of 3279852_1 by 21 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.964 | MS1 | 121.4656733424 | 31.1446291443 | 337 | 504990 | -75.29 | 15.92 | 322.80 | 0.07 | 2.98 | 1570 |
| 2024-09-20 22:21:32.659 | MS1 | 121.4656734471 | 31.1446365770 | 337 | 504990 | -78.63 | 15.87 | 393.59 | 0.14 | 2.76 | 1596 |
| 2024-09-20 22:21:33.650 | MS1 | 121.4656654203 | 31.1446314065 | 337 | 504990 | -76.94 | 12.35 | 383.38 | 0.05 | 2.46 | 1561 |
| 2024-09-20 22:21:34.227 | MS1 | 121.4656703275 | 31.1446322044 | 337 | 504990 | -89.82 | -3.52 | 45.60 | 0.07 | 1.39 | 1592 |
| 2024-09-20 22:21:35.183 | MS1 | 121.4656611455 | 31.1446200094 | 337 | 504990 | -85.93 | -1.87 | 54.97 | 0.01 | 1.37 | 1585 |
| 2024-09-20 22:21:36.244 | MS1 | 121.4656666338 | 31.1446327682 | 337 | 504990 | -87.12 | -2.94 | 55.54 | 0.20 | 1.11 | 1560 |
| 2024-09-20 22:21:37.544 | MS1 | 121.4656589385 | 31.1446268345 | 337 | 504990 | -86.49 | -0.96 | 73.89 | 0.04 | 1.31 | 1594 |
| 2024-09-20 22:21:38.792 | MS1 | 121.4656757808 | 31.1446360387 | 337 | 504990 | -80.82 | 16.35 | 564.54 | 0.05 | 1.35 | 1589 |
| 2024-09-20 22:21:39.643 | MS1 | 121.4656706473 | 31.1446229426 | 337 | 504990 | -84.97 | 12.29 | 454.09 | 0.06 | 1.14 | 1563 |
| 2024-09-20 22:21:40.516 | MS1 | 121.4656669144 | 31.1446314503 | 337 | 504990 | -83.51 | 14.68 | 555.27 | 0.03 | 2.25 | 1571 |
| 2024-09-20 22:21:41.712 | MS1 | 121.4656590399 | 31.1446307545 | 337 | 504990 | -76.63 | 13.11 | 588.93 | 0.10 | 2.82 | 1598 |
| 2024-09-20 22:21:42.382 | MS1 | 121.4656751608 | 31.1446312298 | 337 | 504990 | -76.33 | 13.66 | 390.23 | 0.11 | 2.04 | 1560 |

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
| 3259611 | 3 | 121.4651856431 | 31.1559027101 | 118 | 15 | 8 | 20.4 | TDD | 843 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3273147 | 4 | 121.4677579088 | 31.1450982235 | 289 | 6 | 7 | 26.7 | TDD | 412 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3273573 | 2 | 121.4741118847 | 31.1548925790 | 250 | 5 | 2 | 31.8 | TDD | 337 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3279852 | 1 | 121.4720697911 | 31.1482306388 | 258 | 0 | 4 | 20.6 | TDD | 3 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.153 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.173 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.309 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.309 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.014 | NREventA3 | measId:2;ServCellPCI:370;Se... |
| 2024-09-20 22:21:36.014 | NREventA3 | measId:2;ServCellPCI:370;Se... |
| 2024-09-20 22:21:37.014 | NREventA3 | measId:2;ServCellPCI:370;Se... |
| 2024-09-20 22:21:39.514 | NRRRCReestablishAttempt | PCI:370 |
| 2024-09-20 22:21:39.527 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.537 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.659 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.659 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279852 | 1 | 7.0388 | 16.9550 | -116.4745 | 13.9286 | 84.4325 | 0.0030 | 0.0064 |
| 2024_09_20 22:00 | 3273573 | 2 | 17.9423 | 17.6441 | -115.0993 | 10.5192 | 121.2152 | 0.0029 | 0.1349 |
| 2024_09_20 22:00 | 3259611 | 3 | 16.2851 | 9.9658 | -115.9848 | 18.2872 | 92.4711 | 0.0107 | 0.0166 |
| 2024_09_20 22:00 | 3273147 | 4 | 12.9917 | 19.1544 | -116.6910 | 10.6563 | 131.0037 | 0.0150 | 0.0127 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413352_2AB9F75C | 504990 | 337 | -90.6 | 504990 | 3 | -86.7 | 504990 | 843 | -88.1 | 504990 | 412 |
| MR_1774413352_2572F7DE | 504990 | 337 | -90.0 | 504990 | 3 | -87.1 | 504990 | 843 | -84.5 | 504990 | 412 |
| MR_1774413352_9DC7E961 | 504990 | 3 | -85.1 | 504990 | 337 | -90.6 | 504990 | 843 | -87.1 | 504990 | 412 |
| MR_1774413352_E1B6CF17 | 504990 | 337 | -89.9 | 504990 | 3 | -86.0 | 504990 | 843 | -86.8 | 504990 | 412 |
| MR_1774413352_1A83143C | 504990 | 337 | -89.2 | 504990 | 3 | -85.3 | 504990 | 843 | -85.2 | 504990 | 412 |
| MR_1774413352_C558D1D2 | 504990 | 337 | -90.7 | 504990 | 3 | -85.8 | 504990 | 843 | -85.0 | 504990 | 412 |
| MR_1774413352_5219159D | 504990 | 337 | -87.9 | 504990 | 3 | -86.0 | 504990 | 843 | -88.3 | 504990 | 412 |
| MR_1774413352_D9F090D6 | 504990 | 337 | -91.6 | 504990 | 3 | -84.0 | 504990 | 843 | -87.3 | 504990 | 412 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 414: `2c5f174c-38f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2c5f174c-38f3-444f-8cbb-d73ff227940f` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Lift the tilt angle  of 3232428_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[414] topology](images/train_0414.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3232428_4 by 10 degrees
- `C2`: Add neighbor relationship between 3223387_3 and 3260467_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223387_3
- `C4`: Adjust the azimuth of 3232428_4 by 50 degrees
- `C5`: Lift the tilt angle  of 3232428_4 by 10 degrees **← 정답**
- `C6`: Increase A3 Offset threshold for 3260467_2
- `C7`: Adjust the azimuth of 3223387_3 by 43 degrees
- `C8`: Lift the tilt angle of 3223387_3 by 3 degrees
- `C9`: Press down the tilt angle of 3223387_3 by 3 degrees
- `C10`: Add neighbor relationship between 3232428_4 and 3260467_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223387_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260467_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260467_2
- `C14`: Increase A3 Offset threshold for 3223387_3
- `C15`: Increase transmission power for 3260467_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase transmission power for 3223387_3
- `C18`: Decrease transmission power for 3223387_3
- `C19`: Decrease A3 Offset threshold for 3223387_3
- `C20`: Decrease A3 Offset threshold for 3260467_2
- `C21`: Decrease transmission power for 3260467_2
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.861 | MS1 | 121.4656714912 | 31.1446204300 | 684 | 504990 | -88.72 | 15.51 | 500.36 | 0.00 | 2.97 | 1588 |
| 2024-09-20 22:21:32.557 | MS1 | 121.4656663833 | 31.1446181285 | 684 | 504990 | -88.86 | 15.63 | 303.35 | 0.16 | 2.43 | 1577 |
| 2024-09-20 22:21:33.209 | MS1 | 121.4656643524 | 31.1446363075 | 684 | 504990 | -90.19 | 17.82 | 327.31 | 0.08 | 2.19 | 1583 |
| 2024-09-20 22:21:34.152 | MS1 | 121.4656665701 | 31.1446227804 | 684 | 504990 | -87.83 | 12.54 | 82.94 | 0.07 | 2.79 | 1584 |
| 2024-09-20 22:21:35.519 | MS1 | 121.4656778018 | 31.1446360505 | 684 | 504990 | -88.97 | 14.38 | 52.09 | 0.16 | 2.79 | 1578 |
| 2024-09-20 22:21:36.661 | MS1 | 121.4656662446 | 31.1446229010 | 684 | 504990 | -89.99 | 15.63 | 82.91 | 0.13 | 2.58 | 1579 |
| 2024-09-20 22:21:37.872 | MS1 | 121.4656758379 | 31.1446336853 | 684 | 504990 | -89.54 | 10.69 | 96.63 | 0.03 | 2.93 | 1582 |
| 2024-09-20 22:21:38.980 | MS1 | 121.4656724711 | 31.1446213133 | 684 | 504990 | -91.96 | 8.03 | 62.58 | 0.10 | 2.81 | 1587 |
| 2024-09-20 22:21:39.845 | MS1 | 121.4656606250 | 31.1446224843 | 684 | 504990 | -91.64 | 7.70 | 92.54 | 0.06 | 2.79 | 1580 |
| 2024-09-20 22:21:40.809 | MS1 | 121.4656647076 | 31.1446219003 | 684 | 504990 | -91.07 | 8.64 | 566.68 | 0.03 | 2.16 | 1589 |
| 2024-09-20 22:21:41.211 | MS1 | 121.4656717529 | 31.1446358548 | 684 | 504990 | -92.83 | 12.87 | 483.53 | 0.01 | 2.41 | 1585 |
| 2024-09-20 22:21:42.397 | MS1 | 121.4656601358 | 31.1446219230 | 684 | 504990 | -93.22 | 7.36 | 557.77 | 0.12 | 2.25 | 1598 |

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
| 3211263 | 1 | 121.4732585677 | 31.1506269007 | 197 | 5 | 9 | 43.6 | TDD | 314 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3223387 | 3 | 121.4756834882 | 31.1457007110 | 220 | 1 | 10 | 35.5 | TDD | 684 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3232428 | 4 | 121.4730667716 | 31.1559070581 | 318 | 1 | 12 | 26.5 | TDD | 783 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3260467 | 2 | 121.4688215963 | 31.1491810268 | 65 | 12 | 0 | 16.3 | TDD | 651 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.896 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.914 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.040 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.040 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.726 | NREventA3 | measId:2;ServCellPCI:184;Se... |
| 2024-09-20 22:21:37.966 | NRHandoverAttempt | SourcePCI:184;SourceNR-ARFC... |
| 2024-09-20 22:21:38.016 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.031 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.171 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.171 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211263 | 1 | 9.5640 | 7.5256 | -117.7393 | 14.6517 | 183.9765 | 0.0068 | 0.0122 |
| 2024_09_20 22:00 | 3260467 | 2 | 11.0145 | 12.7844 | -117.6356 | 12.6589 | 124.0040 | 0.0141 | 0.0075 |
| 2024_09_20 22:00 | 3223387 | 3 | 79.5357 | 82.7734 | -114.4285 | 17.7949 | 199.4370 | 0.0073 | 0.0093 |
| 2024_09_20 22:00 | 3232428 | 4 | 15.6007 | 6.0974 | -115.8044 | 15.4125 | 182.4408 | 0.0104 | 0.0077 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415864_EF844651 | 504990 | 684 | -89.0 | 504990 | 651 | -87.8 | 504990 | 783 | -101.1 | 504990 | 314 |
| MR_1774415864_374DA367 | 504990 | 684 | -89.3 | 504990 | 651 | -90.0 | 504990 | 783 | -100.8 | 504990 | 314 |
| MR_1774415864_5570498B | 504990 | 684 | -87.1 | 504990 | 651 | -89.0 | 504990 | 783 | -101.8 | 504990 | 314 |
| MR_1774415864_AC7B6DA0 | 504990 | 684 | -88.4 | 504990 | 651 | -87.6 | 504990 | 783 | -100.4 | 504990 | 314 |
| MR_1774415864_B89F5D19 | 504990 | 684 | -87.0 | 504990 | 651 | -86.8 | 504990 | 783 | -103.2 | 504990 | 314 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 415: `57e38e11-713...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `57e38e11-7136-4193-a474-90e5d50646c3` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[415] topology](images/train_0415.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3244051_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244051_2
- `C3`: Decrease transmission power for 3225788_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225788_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225788_3
- `C6`: Lift the tilt angle  of 3225788_3 by 10 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244051_2
- `C8`: Press down the tilt angle of 3244051_2 by 8 degrees
- `C9`: Adjust the azimuth of 3244051_2 by 50 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease transmission power for 3244051_2
- `C12`: Increase A3 Offset threshold for 3225788_3
- `C13`: Add neighbor relationship between 3244051_2 and 3225788_3
- `C14`: Adjust the azimuth of 3225788_3 by 50 degrees
- `C15`: Decrease A3 Offset threshold for 3244051_2
- `C16`: Increase A3 Offset threshold for 3244051_2
- `C17`: Decrease A3 Offset threshold for 3225788_3
- `C18`: Increase transmission power for 3225788_3
- `C19`: Check test server and transmission issues **← 정답**
- `C20`: Lift the tilt angle of 3244051_2 by 8 degrees
- `C21`: Add neighbor relationship between 3212828_4 and 3225788_3
- `C22`: Press down the tilt angle  of 3225788_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.679 | MS1 | 121.4656585671 | 31.1446336590 | 234 | 504990 | -90.07 | 13.98 | 303.18 | 0.17 | 2.22 | 1580 |
| 2024-09-20 22:21:32.903 | MS1 | 121.4656643424 | 31.1446273828 | 234 | 504990 | -91.04 | 17.23 | 518.37 | 0.04 | 2.53 | 1590 |
| 2024-09-20 22:21:33.440 | MS1 | 121.4656759241 | 31.1446301677 | 234 | 504990 | -88.33 | 16.17 | 438.23 | 0.15 | 2.26 | 1600 |
| 2024-09-20 22:21:34.631 | MS1 | 121.4656754306 | 31.1446317022 | 234 | 504990 | -89.09 | 14.99 | 60.21 | 0.09 | 2.29 | 350 |
| 2024-09-20 22:21:35.521 | MS1 | 121.4656736798 | 31.1446243204 | 234 | 504990 | -86.14 | 16.61 | 60.10 | 0.17 | 2.23 | 445 |
| 2024-09-20 22:21:36.370 | MS1 | 121.4656611328 | 31.1446378859 | 234 | 504990 | -85.50 | 17.99 | 71.76 | 0.14 | 2.33 | 329 |
| 2024-09-20 22:21:37.218 | MS1 | 121.4656719248 | 31.1446312327 | 234 | 504990 | -91.05 | 10.97 | 69.47 | 0.09 | 2.85 | 364 |
| 2024-09-20 22:21:38.706 | MS1 | 121.4656767227 | 31.1446342428 | 234 | 504990 | -92.95 | 7.72 | 88.56 | 0.02 | 2.11 | 306 |
| 2024-09-20 22:21:39.416 | MS1 | 121.4656651896 | 31.1446307839 | 234 | 504990 | -92.78 | 11.90 | 58.90 | 0.13 | 2.25 | 454 |
| 2024-09-20 22:21:40.243 | MS1 | 121.4656662141 | 31.1446214433 | 234 | 504990 | -93.45 | 10.19 | 429.62 | 0.15 | 2.17 | 1574 |
| 2024-09-20 22:21:41.124 | MS1 | 121.4656666121 | 31.1446261047 | 234 | 504990 | -92.54 | 12.07 | 449.39 | 0.12 | 2.37 | 1586 |
| 2024-09-20 22:21:42.870 | MS1 | 121.4656673020 | 31.1446237197 | 234 | 504990 | -89.25 | 12.55 | 489.00 | 0.12 | 2.57 | 1593 |

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
| 3212828 | 4 | 121.4733649951 | 31.1452110314 | 182 | 6 | 9 | 22.0 | TDD | 302 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3212886 | 1 | 121.4728341577 | 31.1557136379 | 75 | 11 | 2 | 25.4 | TDD | 8 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3225788 | 3 | 121.4687587811 | 31.1445000099 | 118 | 10 | 6 | 43.2 | TDD | 979 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3244051 | 2 | 121.4731741714 | 31.1517999243 | 23 | 6 | 3 | 36.9 | TDD | 234 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.029 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.052 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.171 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.171 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.901 | NREventA3 | measId:2;ServCellPCI:998;Se... |
| 2024-09-20 22:21:38.141 | NRHandoverAttempt | SourcePCI:998;SourceNR-ARFC... |
| 2024-09-20 22:21:38.185 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.195 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.345 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.345 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212886 | 1 | 12.9747 | 6.0996 | -115.4361 | 9.8463 | 144.5324 | 0.0100 | 0.0167 |
| 2024_09_20 22:00 | 3244051 | 2 | 18.6717 | 19.2256 | -116.8867 | 9.9271 | 88.0391 | 0.0031 | 0.0195 |
| 2024_09_20 22:00 | 3225788 | 3 | 15.3166 | 12.9751 | -116.0935 | 5.3093 | 144.3876 | 0.0162 | 0.0128 |
| 2024_09_20 22:00 | 3212828 | 4 | 15.9268 | 10.0456 | -117.2018 | 8.6745 | 199.6205 | 0.0095 | 0.0023 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412299_837B5266 | 504990 | 234 | -89.7 | 504990 | 979 | -98.4 | 504990 | 302 | -103.1 | 504990 | 8 |
| MR_1774412299_D56207ED | 504990 | 234 | -87.8 | 504990 | 979 | -98.4 | 504990 | 302 | -102.5 | 504990 | 8 |
| MR_1774412299_D42348D9 | 504990 | 234 | -88.0 | 504990 | 979 | -98.6 | 504990 | 302 | -102.1 | 504990 | 8 |
| MR_1774412299_D49788F7 | 504990 | 234 | -90.9 | 504990 | 979 | -97.2 | 504990 | 302 | -102.4 | 504990 | 8 |
| MR_1774412299_DAAF9970 | 504990 | 234 | -89.2 | 504990 | 979 | -99.3 | 504990 | 302 | -100.8 | 504990 | 8 |
| MR_1774412299_B1EE7F94 | 504990 | 234 | -89.8 | 504990 | 979 | -97.4 | 504990 | 302 | -99.8 | 504990 | 8 |
| MR_1774412299_7AE7FDBF | 504990 | 234 | -89.8 | 504990 | 979 | -96.9 | 504990 | 302 | -100.6 | 504990 | 8 |
| MR_1774412299_1315039D | 504990 | 234 | -90.8 | 504990 | 979 | -98.5 | 504990 | 302 | -101.7 | 504990 | 8 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 416: `58a7f807-062...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `58a7f807-0629-4e53-8098-763b32e4754a` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[416] topology](images/train_0416.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3225021_4 by 50 degrees
- `C2`: Increase transmission power for 3225021_4
- `C3`: Decrease transmission power for 3254902_2
- `C4`: Adjust the azimuth of 3254902_2 by 50 degrees
- `C5`: Decrease A3 Offset threshold for 3225021_4
- `C6`: Lift the tilt angle of 3254902_2 by 10 degrees
- `C7`: Decrease transmission power for 3225021_4
- `C8`: Increase transmission power for 3254902_2
- `C9`: Check test server and transmission issues **← 정답**
- `C10`: Increase A3 Offset threshold for 3225021_4
- `C11`: Increase A3 Offset threshold for 3254902_2
- `C12`: Add neighbor relationship between 3215287_1 and 3225021_4
- `C13`: Press down the tilt angle  of 3225021_4 by 10 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225021_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254902_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Lift the tilt angle  of 3225021_4 by 10 degrees
- `C18`: Decrease A3 Offset threshold for 3254902_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254902_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225021_4
- `C21`: Add neighbor relationship between 3254902_2 and 3225021_4
- `C22`: Press down the tilt angle of 3254902_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.509 | MS1 | 121.4656778822 | 31.1446187539 | 202 | 504990 | -86.03 | 13.96 | 509.60 | 0.15 | 2.10 | 1575 |
| 2024-09-20 22:21:32.974 | MS1 | 121.4656677157 | 31.1446305868 | 202 | 504990 | -87.97 | 14.00 | 591.74 | 0.12 | 2.95 | 1580 |
| 2024-09-20 22:21:33.317 | MS1 | 121.4656674094 | 31.1446310025 | 202 | 504990 | -91.02 | 13.76 | 346.08 | 0.15 | 2.18 | 1560 |
| 2024-09-20 22:21:34.683 | MS1 | 121.4656662040 | 31.1446336047 | 202 | 504990 | -86.18 | 13.37 | 87.09 | 0.01 | 2.55 | 461 |
| 2024-09-20 22:21:35.258 | MS1 | 121.4656635827 | 31.1446309541 | 202 | 504990 | -85.55 | 14.63 | 82.45 | 0.06 | 2.32 | 403 |
| 2024-09-20 22:21:36.716 | MS1 | 121.4656765544 | 31.1446341510 | 202 | 504990 | -89.03 | 14.77 | 64.60 | 0.12 | 2.99 | 355 |
| 2024-09-20 22:21:37.418 | MS1 | 121.4656760197 | 31.1446260632 | 202 | 504990 | -92.47 | 11.76 | 43.54 | 0.08 | 2.17 | 342 |
| 2024-09-20 22:21:38.981 | MS1 | 121.4656772488 | 31.1446241490 | 202 | 504990 | -92.07 | 11.95 | 81.50 | 0.19 | 2.48 | 318 |
| 2024-09-20 22:21:39.652 | MS1 | 121.4656764304 | 31.1446301293 | 202 | 504990 | -92.95 | 12.89 | 53.98 | 0.19 | 2.65 | 338 |
| 2024-09-20 22:21:40.451 | MS1 | 121.4656622791 | 31.1446204067 | 202 | 504990 | -93.38 | 7.53 | 406.17 | 0.05 | 2.95 | 1588 |
| 2024-09-20 22:21:41.318 | MS1 | 121.4656632514 | 31.1446379905 | 202 | 504990 | -92.72 | 11.47 | 582.64 | 0.11 | 2.12 | 1579 |
| 2024-09-20 22:21:42.944 | MS1 | 121.4656708522 | 31.1446208633 | 202 | 504990 | -90.84 | 12.55 | 455.74 | 0.15 | 2.79 | 1582 |

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
| 3215287 | 1 | 121.4705910944 | 31.1473913876 | 310 | 3 | 3 | 31.3 | TDD | 313 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3225021 | 4 | 121.4744866352 | 31.1460058139 | 114 | 15 | 1 | 18.3 | TDD | 511 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3229920 | 3 | 121.4725995438 | 31.1443093457 | 137 | 2 | 3 | 48.8 | TDD | 67 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3254902 | 2 | 121.4754578514 | 31.1456553627 | 204 | 11 | 10 | 18.0 | TDD | 202 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.916 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.934 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.050 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.050 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.737 | NREventA3 | measId:2;ServCellPCI:303;Se... |
| 2024-09-20 22:21:37.977 | NRHandoverAttempt | SourcePCI:303;SourceNR-ARFC... |
| 2024-09-20 22:21:38.016 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.026 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.129 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.129 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215287 | 1 | 18.5272 | 7.9277 | -116.0338 | 6.9849 | 191.0066 | 0.0183 | 0.0126 |
| 2024_09_20 22:00 | 3254902 | 2 | 15.5394 | 8.1885 | -117.9501 | 5.5859 | 198.7366 | 0.0038 | 0.0108 |
| 2024_09_20 22:00 | 3229920 | 3 | 13.1618 | 16.1042 | -115.0147 | 14.8255 | 152.0608 | 0.0191 | 0.0069 |
| 2024_09_20 22:00 | 3225021 | 4 | 17.4948 | 7.0903 | -114.6773 | 8.9722 | 148.5837 | 0.0190 | 0.0169 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417005_84FF1761 | 504990 | 202 | -88.0 | 504990 | 511 | -94.2 | 504990 | 313 | -97.2 | 504990 | 67 |
| MR_1774417005_116D645C | 504990 | 202 | -85.0 | 504990 | 511 | -93.3 | 504990 | 313 | -97.2 | 504990 | 67 |
| MR_1774417005_369086BB | 504990 | 202 | -84.4 | 504990 | 511 | -93.3 | 504990 | 313 | -94.0 | 504990 | 67 |
| MR_1774417005_22F5E5B5 | 504990 | 202 | -86.4 | 504990 | 511 | -92.4 | 504990 | 313 | -95.7 | 504990 | 67 |
| MR_1774417005_BFDDA519 | 504990 | 202 | -85.2 | 504990 | 511 | -91.2 | 504990 | 313 | -96.6 | 504990 | 67 |
| MR_1774417005_FC6C38AC | 504990 | 202 | -85.5 | 504990 | 511 | -91.9 | 504990 | 313 | -97.6 | 504990 | 67 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 417: `6d384ff3-ccb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6d384ff3-ccbc-4c63-bb3d-48369107ac5c` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Add neighbor relationship between 3223825_1 and 3277572_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[417] topology](images/train_0417.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3223825_1
- `C2`: Decrease A3 Offset threshold for 3277572_2
- `C3`: Check test server and transmission issues
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277572_2
- `C5`: Add neighbor relationship between 3223825_1 and 3277572_2 **← 정답**
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223825_1
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223825_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277572_2
- `C10`: Increase A3 Offset threshold for 3223825_1
- `C11`: Adjust the azimuth of 3277572_2 by 26 degrees
- `C12`: Adjust the azimuth of 3223825_1 by 50 degrees
- `C13`: Increase A3 Offset threshold for 3277572_2
- `C14`: Add neighbor relationship between 3272993_4 and 3277572_2
- `C15`: Lift the tilt angle  of 3277572_2 by 2 degrees
- `C16`: Increase transmission power for 3277572_2
- `C17`: Decrease A3 Offset threshold for 3223825_1
- `C18`: Press down the tilt angle of 3223825_1 by 8 degrees
- `C19`: Increase transmission power for 3223825_1
- `C20`: Press down the tilt angle  of 3277572_2 by 2 degrees
- `C21`: Decrease transmission power for 3277572_2
- `C22`: Lift the tilt angle of 3223825_1 by 8 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.424 | MS1 | 121.4656716503 | 31.1446318588 | 25 | 504990 | -75.39 | 16.32 | 320.52 | 0.05 | 2.16 | 1564 |
| 2024-09-20 22:21:32.762 | MS1 | 121.4656611025 | 31.1446355615 | 25 | 504990 | -79.30 | 13.45 | 408.24 | 0.16 | 2.42 | 1574 |
| 2024-09-20 22:21:33.515 | MS1 | 121.4656731741 | 31.1446223325 | 25 | 504990 | -83.75 | 13.73 | 375.83 | 0.04 | 2.17 | 1595 |
| 2024-09-20 22:21:34.685 | MS1 | 121.4656584249 | 31.1446259992 | 25 | 504990 | -92.38 | -0.37 | 78.03 | 0.20 | 1.11 | 1588 |
| 2024-09-20 22:21:35.242 | MS1 | 121.4656732240 | 31.1446349637 | 25 | 504990 | -89.98 | -2.41 | 58.73 | 0.04 | 1.19 | 1562 |
| 2024-09-20 22:21:36.855 | MS1 | 121.4656648565 | 31.1446377548 | 25 | 504990 | -89.92 | -3.91 | 50.82 | 0.07 | 1.15 | 1576 |
| 2024-09-20 22:21:37.260 | MS1 | 121.4656608187 | 31.1446355504 | 25 | 504990 | -88.79 | -1.85 | 42.04 | 0.00 | 1.20 | 1568 |
| 2024-09-20 22:21:38.437 | MS1 | 121.4656705935 | 31.1446251625 | 25 | 504990 | -78.27 | 12.08 | 475.79 | 0.09 | 1.34 | 1579 |
| 2024-09-20 22:21:39.792 | MS1 | 121.4656754272 | 31.1446263949 | 25 | 504990 | -80.64 | 15.54 | 308.77 | 0.20 | 1.16 | 1583 |
| 2024-09-20 22:21:40.866 | MS1 | 121.4656740336 | 31.1446367735 | 25 | 504990 | -75.21 | 17.31 | 506.35 | 0.03 | 2.63 | 1576 |
| 2024-09-20 22:21:41.455 | MS1 | 121.4656678372 | 31.1446336056 | 25 | 504990 | -79.02 | 17.51 | 473.12 | 0.10 | 2.68 | 1600 |
| 2024-09-20 22:21:42.792 | MS1 | 121.4656733691 | 31.1446297064 | 25 | 504990 | -83.03 | 15.06 | 301.65 | 0.10 | 2.70 | 1579 |

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
| 3218404 | 3 | 121.4726327039 | 31.1477000970 | 231 | 6 | 6 | 39.3 | TDD | 202 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3223825 | 1 | 121.4643932359 | 31.1546221856 | 281 | 7 | 10 | 28.5 | TDD | 25 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3272993 | 4 | 121.4727920754 | 31.1446537668 | 312 | 5 | 6 | 28.1 | TDD | 471 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3277572 | 2 | 121.4723575188 | 31.1542279021 | 185 | 1 | 9 | 23.9 | TDD | 938 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.458 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.480 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.614 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.614 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.304 | NREventA3 | measId:2;ServCellPCI:242;Se... |
| 2024-09-20 22:21:36.304 | NREventA3 | measId:2;ServCellPCI:242;Se... |
| 2024-09-20 22:21:37.304 | NREventA3 | measId:2;ServCellPCI:242;Se... |
| 2024-09-20 22:21:39.804 | NRRRCReestablishAttempt | PCI:242 |
| 2024-09-20 22:21:39.819 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.830 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.956 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.956 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223825 | 1 | 17.7037 | 8.3074 | -116.9614 | 16.7768 | 85.8579 | 0.0119 | 0.1148 |
| 2024_09_20 22:00 | 3277572 | 2 | 19.3805 | 5.6334 | -116.0885 | 8.3634 | 133.7403 | 0.0173 | 0.0170 |
| 2024_09_20 22:00 | 3218404 | 3 | 15.1998 | 18.7269 | -116.1233 | 12.6061 | 147.5840 | 0.0047 | 0.0103 |
| 2024_09_20 22:00 | 3272993 | 4 | 16.8702 | 13.3201 | -116.7447 | 14.0865 | 150.9921 | 0.0095 | 0.0050 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415126_C1CC07AB | 504990 | 25 | -92.2 | 504990 | 938 | -85.2 | 504990 | 471 | -92.8 | 504990 | 202 |
| MR_1774415126_68B03259 | 504990 | 25 | -91.7 | 504990 | 938 | -87.7 | 504990 | 471 | -94.1 | 504990 | 202 |
| MR_1774415126_D9BC5399 | 504990 | 25 | -91.0 | 504990 | 938 | -86.4 | 504990 | 471 | -93.3 | 504990 | 202 |
| MR_1774415126_21451964 | 504990 | 25 | -91.7 | 504990 | 938 | -86.5 | 504990 | 471 | -94.5 | 504990 | 202 |
| MR_1774415126_1B8C8698 | 504990 | 938 | -85.2 | 504990 | 25 | -94.3 | 504990 | 471 | -91.5 | 504990 | 202 |
| MR_1774415126_B9F3B62F | 504990 | 25 | -92.0 | 504990 | 938 | -85.1 | 504990 | 471 | -94.3 | 504990 | 202 |
| MR_1774415126_E90C8B14 | 504990 | 938 | -88.3 | 504990 | 25 | -94.0 | 504990 | 471 | -92.1 | 504990 | 202 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 418: `f159a660-768...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f159a660-7683-40a1-872c-295c0239683c` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242707_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[418] topology](images/train_0418.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3242707_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242707_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase transmission power for 3231463_2
- `C5`: Press down the tilt angle  of 3231463_2 by 1 degrees
- `C6`: Adjust the azimuth of 3242707_1 by 40 degrees
- `C7`: Press down the tilt angle of 3242707_1 by 1 degrees
- `C8`: Increase transmission power for 3242707_1
- `C9`: Decrease A3 Offset threshold for 3231463_2
- `C10`: Lift the tilt angle  of 3231463_2 by 1 degrees
- `C11`: Add neighbor relationship between 3242707_1 and 3231463_2
- `C12`: Add neighbor relationship between 3231451_13 and 3231463_2
- `C13`: Increase A3 Offset threshold for 3231463_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242707_1 **← 정답**
- `C15`: Lift the tilt angle of 3242707_1 by 1 degrees
- `C16`: Decrease transmission power for 3242707_1
- `C17`: Decrease transmission power for 3231463_2
- `C18`: Adjust the azimuth of 3231463_2 by 7 degrees
- `C19`: Check test server and transmission issues
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231463_2
- `C21`: Decrease A3 Offset threshold for 3242707_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231463_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.730 | MS1 | 121.4656697684 | 31.1446221349 | 420 | 504990 | -95.86 | 11.53 | 519.96 | 0.08 | 2.32 | 1598 |
| 2024-09-20 22:21:32.146 | MS1 | 121.4656711906 | 31.1446191388 | 562 | 504990 | -93.58 | 10.92 | 482.10 | 0.02 | 2.26 | 1597 |
| 2024-09-20 22:21:33.216 | MS1 | 121.4656595018 | 31.1446315700 | 374 | 504990 | -95.75 | 12.89 | 459.81 | 0.12 | 2.25 | 1578 |
| 2024-09-20 22:21:34.195 | MS1 | 121.4656591330 | 31.1446246717 | 522 | 152650 | -87.95 | 7.06 | 59.97 | 0.02 | 1.84 | 954 |
| 2024-09-20 22:21:35.919 | MS1 | 121.4656711993 | 31.1446186513 | 82 | 152650 | -89.26 | 5.28 | 66.50 | 0.03 | 1.61 | 936 |
| 2024-09-20 22:21:36.324 | MS1 | 121.4656607353 | 31.1446305083 | 606 | 152650 | -87.16 | 2.57 | 65.33 | 0.16 | 1.56 | 965 |
| 2024-09-20 22:21:37.833 | MS1 | 121.4656672115 | 31.1446355102 | 545 | 152650 | -89.86 | 6.08 | 87.67 | 0.11 | 1.93 | 907 |
| 2024-09-20 22:21:38.320 | MS1 | 121.4656602259 | 31.1446232596 | 522 | 152650 | -88.51 | 4.90 | 106.55 | 0.08 | 1.52 | 944 |
| 2024-09-20 22:21:39.930 | MS1 | 121.4656648242 | 31.1446343992 | 82 | 152650 | -95.54 | 7.45 | 52.39 | 0.04 | 1.89 | 986 |
| 2024-09-20 22:21:40.681 | MS1 | 121.4656712725 | 31.1446206811 | 606 | 152650 | -92.36 | 2.35 | 84.87 | 0.20 | 2.78 | 1581 |
| 2024-09-20 22:21:41.818 | MS1 | 121.4656614408 | 31.1446376714 | 545 | 152650 | -92.45 | 2.81 | 69.91 | 0.12 | 2.64 | 1565 |
| 2024-09-20 22:21:42.983 | MS1 | 121.4656616935 | 31.1446233556 | 522 | 152650 | -94.93 | 2.12 | 88.96 | 0.11 | 2.84 | 1573 |

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
| 3223505 | 7 | 121.4692478746 | 31.1489332898 | 160 | 15 | 10 | 20.7 | FDD | 545 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3225425 | 11 | 121.4665723929 | 31.1531169646 | 36 | 12 | 12 | 10.9 | FDD | 522 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3226493 | 10 | 121.4724399345 | 31.1453902720 | 84 | 4 | 9 | 21.9 | FDD | 905 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3227788 | 12 | 121.4646988665 | 31.1529239544 | 68 | 2 | 5 | 0.2 | FDD | 82 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3231451 | 13 | 121.4723059842 | 31.1539231129 | 263 | 12 | 2 | 1.9 | FDD | 606 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3231463 | 2 | 121.4757879846 | 31.1528415188 | 220 | 0 | 6 | 13.4 | TDD | 516 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3234631 | 3 | 121.4644859236 | 31.1527715508 | 70 | 7 | 11 | 5.8 | TDD | 710 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3234938 | 4 | 121.4660360080 | 31.1540411638 | 211 | 6 | 9 | 4.5 | TDD | 13 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3242707 | 1 | 121.4708280575 | 31.1454808763 | 219 | 1 | 7 | 2.7 | TDD | 420 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3248103 | 5 | 121.4675225530 | 31.1553296799 | 149 | 5 | 10 | 3.1 | TDD | 562 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3249538 | 9 | 121.4734172166 | 31.1484583810 | 232 | 8 | 10 | 24.8 | FDD | 807 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3262776 | 6 | 121.4740266752 | 31.1455603715 | 114 | 9 | 8 | 23.9 | TDD | 374 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3271620 | 8 | 121.4679983775 | 31.1485095250 | 274 | 7 | 11 | 29.2 | FDD | 774 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |

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
| 2024-09-20 22:21:31.372 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.389 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.531 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.531 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.269 | NREventA2 | measId:1;ServCellPCI:292;Se... |
| 2024-09-20 22:21:35.399 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.668 | NREventA5 | measId:3;ServCellPCI:292;Se... |
| 2024-09-20 22:21:35.735 | NRHandoverAttempt | SourcePCI:292;SourceNR-ARFC... |
| 2024-09-20 22:21:35.765 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.776 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.893 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.893 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242707 | 1 | 9.9063 | 14.2703 | -116.4521 | 6.0379 | 148.0465 | 0.0105 | 0.0161 |
| 2024_09_20 22:00 | 3231463 | 2 | 9.0709 | 8.5651 | -116.9398 | 12.9909 | 125.8538 | 0.0040 | 0.0128 |
| 2024_09_20 22:00 | 3234631 | 3 | 13.5881 | 17.4192 | -114.8371 | 11.0297 | 160.6219 | 0.0139 | 0.0021 |
| 2024_09_20 22:00 | 3234938 | 4 | 18.7155 | 17.5628 | -114.1409 | 12.6472 | 191.8711 | 0.0027 | 0.0127 |
| 2024_09_20 22:00 | 3248103 | 5 | 14.0607 | 14.1761 | -116.7430 | 16.1914 | 165.0370 | 0.0061 | 0.0194 |
| 2024_09_20 22:00 | 3262776 | 6 | 14.7567 | 19.0219 | -117.3534 | 9.9858 | 147.1743 | 0.0055 | 0.0155 |
| 2024_09_20 22:00 | 3223505 | 7 | 9.0551 | 17.3838 | -116.9923 | 3.3434 | 25.0181 | 0.0098 | 0.0124 |
| 2024_09_20 22:00 | 3271620 | 8 | 16.0345 | 15.2005 | -116.9297 | 4.0970 | 28.6440 | 0.0096 | 0.0007 |
| 2024_09_20 22:00 | 3249538 | 9 | 16.8477 | 6.6090 | -116.8460 | 3.6111 | 47.8614 | 0.0129 | 0.0050 |
| 2024_09_20 22:00 | 3226493 | 10 | 13.7063 | 16.4498 | -115.1067 | 3.2499 | 41.1534 | 0.0187 | 0.0011 |
| 2024_09_20 22:00 | 3225425 | 11 | 15.3929 | 13.4658 | -117.9045 | 3.6764 | 52.2888 | 0.0172 | 0.0041 |
| 2024_09_20 22:00 | 3227788 | 12 | 19.9872 | 10.3888 | -116.4153 | 3.4862 | 46.4498 | 0.0102 | 0.0154 |
| 2024_09_20 22:00 | 3231451 | 13 | 7.9135 | 15.5480 | -116.0026 | 4.5199 | 57.5287 | 0.0016 | 0.0045 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416567_6DDB80FF | 152650 | 522 | -88.2 | 152650 | 807 | -94.6 | 152650 | 774 | -99.2 | 152650 | 905 |
| MR_1774416567_1BA4DEC6 | 504990 | 374 | -94.5 | 504990 | 516 | -94.8 | 504990 | 710 | -104.3 | 504990 | 13 |
| MR_1774416567_EFBD8416 | 152650 | 522 | -88.6 | 152650 | 807 | -94.0 | 152650 | 774 | -99.9 | 152650 | 905 |
| MR_1774416567_F6969CE4 | 152650 | 522 | -88.5 | 152650 | 807 | -91.4 | 152650 | 774 | -96.7 | 152650 | 905 |
| MR_1774416567_D3894FE0 | 504990 | 374 | -97.7 | 504990 | 516 | -95.0 | 504990 | 710 | -102.0 | 504990 | 13 |
| MR_1774416567_0F848061 | 504990 | 374 | -96.5 | 504990 | 516 | -94.1 | 504990 | 710 | -101.2 | 504990 | 13 |
| MR_1774416567_F0C98B24 | 152650 | 522 | -88.3 | 152650 | 807 | -93.4 | 152650 | 774 | -99.1 | 152650 | 905 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 419: `eccdc0a1-06c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `eccdc0a1-06c7-4bae-a283-8fe5803643aa` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[419] topology](images/train_0419.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3245052_1
- `C2`: Adjust the azimuth of 3231615_2 by 0 degrees
- `C3`: Press down the tilt angle of 3231615_2 by 10 degrees
- `C4`: Adjust the azimuth of 3245052_1 by 50 degrees
- `C5`: Lift the tilt angle  of 3245052_1 by 10 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245052_1
- `C7`: Decrease A3 Offset threshold for 3245052_1
- `C8`: Decrease A3 Offset threshold for 3231615_2
- `C9`: Increase transmission power for 3231615_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231615_2
- `C11`: Press down the tilt angle  of 3245052_1 by 10 degrees
- `C12`: Increase A3 Offset threshold for 3245052_1
- `C13`: Check test server and transmission issues
- `C14`: Add neighbor relationship between 3231615_2 and 3245052_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245052_1
- `C16`: Add neighbor relationship between 3230697_4 and 3245052_1
- `C17`: Increase transmission power for 3245052_1
- `C18`: Decrease transmission power for 3231615_2
- `C19`: Increase A3 Offset threshold for 3231615_2
- `C20`: Insufficient data; more data is needed for judgment. **← 정답**
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231615_2
- `C22`: Lift the tilt angle of 3231615_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.352 | MS1 | 121.4656727268 | 31.1446318537 | 468 | 504990 | -89.90 | 16.02 | 350.97 | 0.10 | 2.52 | 1600 |
| 2024-09-20 22:21:32.514 | MS1 | 121.4656726840 | 31.1446215784 | 468 | 504990 | -85.16 | 14.88 | 550.81 | 0.12 | 2.42 | 1563 |
| 2024-09-20 22:21:33.321 | MS1 | 121.4656707361 | 31.1446315043 | 468 | 504990 | -89.72 | 12.09 | 476.06 | 0.07 | 2.99 | 1596 |
| 2024-09-20 22:21:34.209 | MS1 | 121.4656769253 | 31.1446339008 | 468 | 504990 | -89.82 | 13.66 | 80.77 | 0.15 | 2.69 | 1560 |
| 2024-09-20 22:21:35.730 | MS1 | 121.4656702362 | 31.1446298018 | 468 | 504990 | -90.71 | 13.03 | 47.91 | 0.13 | 2.04 | 1583 |
| 2024-09-20 22:21:36.467 | MS1 | 121.4656733518 | 31.1446304282 | 468 | 504990 | -87.82 | 14.63 | 68.20 | 0.14 | 2.46 | 1592 |
| 2024-09-20 22:21:37.154 | MS1 | 121.4656640129 | 31.1446319602 | 468 | 504990 | -90.18 | 9.23 | 71.44 | 0.07 | 2.93 | 1585 |
| 2024-09-20 22:21:38.447 | MS1 | 121.4656641602 | 31.1446235971 | 468 | 504990 | -93.00 | 11.09 | 59.70 | 0.19 | 2.05 | 1576 |
| 2024-09-20 22:21:39.405 | MS1 | 121.4656656455 | 31.1446212747 | 468 | 504990 | -89.37 | 12.08 | 53.89 | 0.07 | 2.57 | 1593 |
| 2024-09-20 22:21:40.119 | MS1 | 121.4656724871 | 31.1446266155 | 468 | 504990 | -92.37 | 12.12 | 468.11 | 0.05 | 2.51 | 1600 |
| 2024-09-20 22:21:41.912 | MS1 | 121.4656622404 | 31.1446326435 | 468 | 504990 | -90.01 | 7.91 | 438.73 | 0.03 | 2.78 | 1585 |
| 2024-09-20 22:21:42.493 | MS1 | 121.4656635727 | 31.1446273703 | 468 | 504990 | -89.80 | 9.70 | 385.73 | 0.20 | 2.69 | 1586 |

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
| 3230697 | 4 | 121.4659361770 | 31.1518118202 | 230 | 5 | 0 | 34.2 | TDD | 327 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3231615 | 2 | 121.4675332026 | 31.1534927181 | 190 | 11 | 3 | 41.8 | TDD | 468 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3245052 | 1 | 121.4698419027 | 31.1481091379 | 59 | 14 | 4 | 48.9 | TDD | 497 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3273340 | 3 | 121.4717088390 | 31.1483419532 | 210 | 6 | 8 | 15.9 | TDD | 973 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.181 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.200 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.339 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.339 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.039 | NREventA3 | measId:2;ServCellPCI:213;Se... |
| 2024-09-20 22:21:38.279 | NRHandoverAttempt | SourcePCI:213;SourceNR-ARFC... |
| 2024-09-20 22:21:38.325 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.336 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.482 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.482 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3245052 | 1 | 85.9353 | 85.5690 | -116.9744 | 6.6048 | 120.7889 | 0.0042 | 0.0030 |
| 2024_09_19 22:00 | 3231615 | 2 | 84.5597 | 78.8523 | -116.9121 | 12.5268 | 188.7188 | 0.0045 | 0.0021 |
| 2024_09_19 22:00 | 3273340 | 3 | 76.0064 | 77.4982 | -116.9496 | 7.4935 | 81.4318 | 0.0101 | 0.0141 |
| 2024_09_19 22:00 | 3230697 | 4 | 91.9451 | 83.1325 | -114.4981 | 15.0113 | 170.2299 | 0.0098 | 0.0074 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415842_B29549DE | 504990 | 468 | -88.9 | 504990 | 497 | -90.9 | 504990 | 327 | -104.7 | 504990 | 973 |
| MR_1774415842_E3935475 | 504990 | 468 | -88.3 | 504990 | 497 | -91.5 | 504990 | 327 | -101.4 | 504990 | 973 |
| MR_1774415842_83A334F0 | 504990 | 468 | -89.0 | 504990 | 497 | -90.9 | 504990 | 327 | -101.9 | 504990 | 973 |
| MR_1774415842_1411D0A2 | 504990 | 468 | -91.7 | 504990 | 497 | -91.6 | 504990 | 327 | -102.4 | 504990 | 973 |
| MR_1774415842_A1DB09E2 | 504990 | 468 | -89.5 | 504990 | 497 | -90.3 | 504990 | 327 | -103.5 | 504990 | 973 |
| MR_1774415842_A56BFAB6 | 504990 | 468 | -91.1 | 504990 | 497 | -90.2 | 504990 | 327 | -103.1 | 504990 | 973 |

> *... 2개 열 생략 (전체 14열)*

---
