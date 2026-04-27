# Track A 문제 분석 — train[670]~train[679]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[670] ~ train[679] (10개)

## 목차

1. [문제 670: `b759c0d3-80d...`](#670) — multiple-answer, 정답: C2|C9
2. [문제 671: `2df4ce31-47b...`](#671) — single-answer, 정답: C12
3. [문제 672: `526a5f67-fec...`](#672) — single-answer, 정답: C5
4. [문제 673: `bdc05637-d69...`](#673) — single-answer, 정답: C3
5. [문제 674: `d303f985-a0b...`](#674) — single-answer, 정답: C1
6. [문제 675: `b821388a-cf3...`](#675) — single-answer, 정답: C4
7. [문제 676: `65b3ac33-e0c...`](#676) — multiple-answer, 정답: C8|C15
8. [문제 677: `ae455e86-83d...`](#677) — single-answer, 정답: C20
9. [문제 678: `fd8868b0-895...`](#678) — single-answer, 정답: C14
10. [문제 679: `228bf361-6da...`](#679) — single-answer, 정답: C22

---

### 문제 670: `b759c0d3-80d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b759c0d3-80d6-4e2a-86a1-cabb211f6e6b` |
| Tag | **multiple-answer** |
| 정답 | **C2|C9** |
| C2 의미 | Increase transmission power for 3212132_2 |
| C9 의미 | Adjust the azimuth of 3212132_2 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[670] topology](images/train_0670.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase transmission power for 3212132_2 **← 정답**
- `C3`: Press down the tilt angle of 3212132_2 by 2 degrees
- `C4`: Decrease A3 Offset threshold for 3212132_2
- `C5`: Increase A3 Offset threshold for 3212132_2
- `C6`: Increase transmission power for 3236794_4
- `C7`: Lift the tilt angle  of 3236794_4 by 6 degrees
- `C8`: Add neighbor relationship between 3212132_2 and 3236794_4
- `C9`: Adjust the azimuth of 3212132_2 by 50 degrees **← 정답**
- `C10`: Lift the tilt angle of 3212132_2 by 2 degrees
- `C11`: Decrease A3 Offset threshold for 3236794_4
- `C12`: Add neighbor relationship between 3239825_3 and 3236794_4
- `C13`: Increase A3 Offset threshold for 3236794_4
- `C14`: Decrease transmission power for 3236794_4
- `C15`: Adjust the azimuth of 3236794_4 by 43 degrees
- `C16`: Decrease transmission power for 3212132_2
- `C17`: Check test server and transmission issues
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212132_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236794_4
- `C20`: Press down the tilt angle  of 3236794_4 by 6 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212132_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236794_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.809 | MS1 | 121.4656756588 | 31.1446314313 | 378 | 504990 | -90.07 | 16.14 | 465.54 | 0.10 | 2.74 | 1592 |
| 2024-09-20 22:21:32.765 | MS1 | 121.4656665213 | 31.1446353245 | 378 | 504990 | -86.92 | 15.45 | 368.62 | 0.10 | 2.39 | 1586 |
| 2024-09-20 22:21:33.980 | MS1 | 121.4656646862 | 31.1446236978 | 378 | 504990 | -85.27 | 16.96 | 463.36 | 0.00 | 2.23 | 1570 |
| 2024-09-20 22:21:34.836 | MS1 | 121.4656629871 | 31.1446321343 | 378 | 504990 | -108.07 | -0.46 | 47.04 | 0.01 | 1.45 | 1574 |
| 2024-09-20 22:21:35.492 | MS1 | 121.4656656181 | 31.1446197841 | 378 | 504990 | -105.17 | 1.02 | 61.53 | 0.05 | 1.46 | 1569 |
| 2024-09-20 22:21:36.724 | MS1 | 121.4656629554 | 31.1446307238 | 378 | 504990 | -102.14 | 0.59 | 29.41 | 0.15 | 1.04 | 1584 |
| 2024-09-20 22:21:37.865 | MS1 | 121.4656646995 | 31.1446305436 | 378 | 504990 | -102.36 | -1.54 | 75.56 | 0.14 | 1.05 | 1575 |
| 2024-09-20 22:21:38.827 | MS1 | 121.4656616780 | 31.1446187263 | 378 | 504990 | -106.58 | -0.42 | 64.93 | 0.09 | 1.08 | 1578 |
| 2024-09-20 22:21:39.355 | MS1 | 121.4656645445 | 31.1446323775 | 378 | 504990 | -109.15 | 1.27 | 20.70 | 0.11 | 1.22 | 1598 |
| 2024-09-20 22:21:40.112 | MS1 | 121.4656744316 | 31.1446355978 | 378 | 504990 | -92.98 | 15.13 | 438.41 | 0.12 | 2.40 | 1595 |
| 2024-09-20 22:21:41.595 | MS1 | 121.4656766515 | 31.1446243096 | 378 | 504990 | -92.50 | 16.37 | 290.85 | 0.01 | 2.69 | 1577 |
| 2024-09-20 22:21:42.562 | MS1 | 121.4656648301 | 31.1446217591 | 378 | 504990 | -92.01 | 17.61 | 560.37 | 0.03 | 2.87 | 1560 |

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
| 3212132 | 2 | 121.4678836579 | 31.1545899520 | 138 | 1 | 4 | 15.7 | TDD | 378 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3217362 | 1 | 121.4661850962 | 31.1487697419 | 62 | 13 | 12 | 43.9 | TDD | 865 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3236794 | 4 | 121.4694505326 | 31.1446594502 | 227 | 2 | 1 | 22.8 | TDD | 874 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3239825 | 3 | 121.4698989009 | 31.1478515043 | 81 | 2 | 4 | 21.2 | TDD | 621 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.228 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.228 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.398 | NREventA2 | measId:1;ServCellPCI:610;Se... |
| 2024-09-20 22:21:34.513 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217362 | 1 | 6.5817 | 11.8404 | -114.3296 | 18.3539 | 98.3269 | 0.0035 | 0.0005 |
| 2024_09_20 22:00 | 3212132 | 2 | 15.8168 | 6.2511 | -117.8695 | 9.0442 | 99.1814 | 0.1769 | 0.0015 |
| 2024_09_20 22:00 | 3239825 | 3 | 9.7030 | 14.3357 | -116.4127 | 18.2222 | 138.3867 | 0.0194 | 0.0099 |
| 2024_09_20 22:00 | 3236794 | 4 | 15.2347 | 19.1605 | -117.1976 | 13.4934 | 151.5573 | 0.0116 | 0.0074 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414660_BF4101F2 | 504990 | 378 | -108.6 | 504990 | 874 | -110.3 | 504990 | 621 | -116.5 | 504990 | 865 |
| MR_1774414660_B96E51FD | 504990 | 378 | -107.3 | 504990 | 874 | -112.9 | 504990 | 621 | -117.2 | 504990 | 865 |
| MR_1774414660_F7460FB3 | 504990 | 378 | -108.2 | 504990 | 874 | -113.2 | 504990 | 621 | -116.0 | 504990 | 865 |
| MR_1774414660_32ADDE5E | 504990 | 378 | -109.8 | 504990 | 874 | -110.4 | 504990 | 621 | -118.8 | 504990 | 865 |
| MR_1774414660_54740F91 | 504990 | 378 | -108.0 | 504990 | 874 | -110.5 | 504990 | 621 | -115.2 | 504990 | 865 |
| MR_1774414660_C8AFAECF | 504990 | 378 | -106.4 | 504990 | 874 | -109.7 | 504990 | 621 | -118.1 | 504990 | 865 |
| MR_1774414660_0D82CEF2 | 504990 | 378 | -106.4 | 504990 | 874 | -110.1 | 504990 | 621 | -116.7 | 504990 | 865 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 671: `2df4ce31-47b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2df4ce31-47be-4940-85fe-70d33ad39cee` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274599_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[671] topology](images/train_0671.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3274599_5
- `C2`: Increase A3 Offset threshold for 3276818_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276818_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276818_2
- `C5`: Press down the tilt angle  of 3276818_2 by 4 degrees
- `C6`: Lift the tilt angle  of 3276818_2 by 4 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274599_5
- `C8`: Increase transmission power for 3274599_5
- `C9`: Increase transmission power for 3276818_2
- `C10`: Decrease transmission power for 3276818_2
- `C11`: Increase A3 Offset threshold for 3274599_5
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274599_5 **← 정답**
- `C13`: Decrease A3 Offset threshold for 3274599_5
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Adjust the azimuth of 3274599_5 by 18 degrees
- `C16`: Lift the tilt angle of 3274599_5 by 6 degrees
- `C17`: Press down the tilt angle of 3274599_5 by 6 degrees
- `C18`: Add neighbor relationship between 3268297_10 and 3276818_2
- `C19`: Add neighbor relationship between 3274599_5 and 3276818_2
- `C20`: Adjust the azimuth of 3276818_2 by 43 degrees
- `C21`: Check test server and transmission issues
- `C22`: Decrease A3 Offset threshold for 3276818_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.604 | MS1 | 121.4656713317 | 31.1446305397 | 466 | 504990 | -94.12 | 12.70 | 548.05 | 0.04 | 2.34 | 1564 |
| 2024-09-20 22:21:32.542 | MS1 | 121.4656673200 | 31.1446212273 | 388 | 504990 | -93.12 | 10.82 | 501.41 | 0.15 | 2.07 | 1596 |
| 2024-09-20 22:21:33.102 | MS1 | 121.4656730081 | 31.1446302237 | 889 | 504990 | -93.83 | 9.04 | 508.58 | 0.00 | 2.49 | 1587 |
| 2024-09-20 22:21:34.171 | MS1 | 121.4656747785 | 31.1446347250 | 313 | 152650 | -87.45 | 2.39 | 67.43 | 0.11 | 1.64 | 992 |
| 2024-09-20 22:21:35.456 | MS1 | 121.4656725542 | 31.1446314662 | 844 | 152650 | -88.12 | 2.48 | 54.61 | 0.07 | 1.95 | 924 |
| 2024-09-20 22:21:36.363 | MS1 | 121.4656658287 | 31.1446269378 | 979 | 152650 | -93.69 | 2.05 | 93.80 | 0.07 | 1.64 | 977 |
| 2024-09-20 22:21:37.930 | MS1 | 121.4656750625 | 31.1446227381 | 440 | 152650 | -93.53 | 5.94 | 83.58 | 0.10 | 1.71 | 1000 |
| 2024-09-20 22:21:38.538 | MS1 | 121.4656581569 | 31.1446314801 | 313 | 152650 | -95.97 | 6.33 | 68.96 | 0.19 | 1.94 | 919 |
| 2024-09-20 22:21:39.808 | MS1 | 121.4656583192 | 31.1446360889 | 844 | 152650 | -88.18 | 2.49 | 91.97 | 0.09 | 1.92 | 926 |
| 2024-09-20 22:21:40.249 | MS1 | 121.4656672203 | 31.1446233709 | 979 | 152650 | -92.38 | 3.85 | 87.01 | 0.12 | 2.68 | 1569 |
| 2024-09-20 22:21:41.923 | MS1 | 121.4656713484 | 31.1446226574 | 440 | 152650 | -92.37 | 2.58 | 82.76 | 0.17 | 2.74 | 1590 |
| 2024-09-20 22:21:42.448 | MS1 | 121.4656768357 | 31.1446368420 | 313 | 152650 | -89.54 | 2.94 | 78.91 | 0.06 | 2.80 | 1582 |

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
| 3210669 | 12 | 121.4755189445 | 31.1493723739 | 85 | 7 | 8 | 8.6 | FDD | 313 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3217709 | 8 | 121.4705553967 | 31.1519523554 | 137 | 6 | 12 | 24.3 | FDD | 1002 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3222235 | 13 | 121.4696721721 | 31.1529279523 | 281 | 3 | 11 | 29.2 | FDD | 223 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3232517 | 3 | 121.4689365193 | 31.1498019754 | 128 | 1 | 7 | 21.2 | TDD | 388 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3248981 | 4 | 121.4749812583 | 31.1558836163 | 194 | 13 | 10 | 15.7 | TDD | 937 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3258714 | 9 | 121.4670712484 | 31.1465182159 | 3 | 5 | 2 | 17.9 | FDD | 844 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3268297 | 10 | 121.4667129003 | 31.1476931901 | 220 | 10 | 0 | 3.8 | FDD | 979 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3269665 | 6 | 121.4739793226 | 31.1486434445 | 309 | 4 | 12 | 18.2 | TDD | 889 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3270150 | 7 | 121.4720848929 | 31.1515859133 | 150 | 3 | 9 | 15.7 | FDD | 360 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3271010 | 1 | 121.4680590246 | 31.1544584088 | 187 | 15 | 11 | 25.9 | TDD | 898 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3272487 | 11 | 121.4704042252 | 31.1483581652 | 44 | 8 | 3 | 17.0 | FDD | 440 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3274599 | 5 | 121.4744748460 | 31.1484908214 | 225 | 4 | 7 | 25.5 | TDD | 466 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3276818 | 2 | 121.4704041697 | 31.1515654331 | 167 | 3 | 7 | 15.4 | TDD | 291 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.239 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.260 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.361 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.361 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.068 | NREventA2 | measId:1;ServCellPCI:30;Ser... |
| 2024-09-20 22:21:35.201 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.474 | NREventA5 | measId:3;ServCellPCI:30;Ser... |
| 2024-09-20 22:21:35.509 | NRHandoverAttempt | SourcePCI:30;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.548 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.560 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.662 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.662 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271010 | 1 | 19.3416 | 10.6338 | -114.8325 | 6.3933 | 160.1614 | 0.0173 | 0.0038 |
| 2024_09_20 22:00 | 3276818 | 2 | 17.1462 | 5.5715 | -115.0325 | 19.0842 | 163.4681 | 0.0115 | 0.0190 |
| 2024_09_20 22:00 | 3232517 | 3 | 17.0104 | 18.6790 | -114.6890 | 12.7869 | 86.6337 | 0.0027 | 0.0047 |
| 2024_09_20 22:00 | 3248981 | 4 | 10.7089 | 6.7179 | -115.6357 | 15.3313 | 187.4069 | 0.0135 | 0.0058 |
| 2024_09_20 22:00 | 3274599 | 5 | 10.2960 | 11.3971 | -116.4354 | 7.1233 | 171.1626 | 0.0195 | 0.0070 |
| 2024_09_20 22:00 | 3269665 | 6 | 12.2068 | 13.0354 | -115.0838 | 16.0600 | 140.3237 | 0.0174 | 0.0160 |
| 2024_09_20 22:00 | 3270150 | 7 | 7.7122 | 7.9460 | -117.0722 | 4.4131 | 33.0480 | 0.0089 | 0.0165 |
| 2024_09_20 22:00 | 3217709 | 8 | 5.9710 | 12.2182 | -114.9812 | 3.9717 | 21.1221 | 0.0179 | 0.0088 |
| 2024_09_20 22:00 | 3258714 | 9 | 17.5497 | 13.5930 | -116.7222 | 3.5861 | 55.2477 | 0.0173 | 0.0160 |
| 2024_09_20 22:00 | 3268297 | 10 | 18.7023 | 8.7401 | -117.2530 | 3.6024 | 56.1725 | 0.0069 | 0.0054 |
| 2024_09_20 22:00 | 3272487 | 11 | 11.7037 | 7.8859 | -115.9510 | 3.6140 | 45.1184 | 0.0134 | 0.0182 |
| 2024_09_20 22:00 | 3210669 | 12 | 7.8704 | 15.7431 | -114.1915 | 4.1116 | 47.8625 | 0.0107 | 0.0175 |
| 2024_09_20 22:00 | 3222235 | 13 | 8.8593 | 12.9308 | -117.4931 | 3.5369 | 44.2596 | 0.0097 | 0.0090 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417102_22BCCC77 | 152650 | 313 | -87.1 | 152650 | 1002 | -90.4 | 152650 | 360 | -93.7 | 152650 | 223 |
| MR_1774417102_8B4F92CF | 504990 | 889 | -93.3 | 504990 | 291 | -90.5 | 504990 | 898 | -94.0 | 504990 | 937 |
| MR_1774417102_75250A24 | 504990 | 889 | -93.9 | 504990 | 291 | -90.6 | 504990 | 898 | -94.3 | 504990 | 937 |
| MR_1774417102_AE47F815 | 152650 | 313 | -88.4 | 152650 | 1002 | -91.9 | 152650 | 360 | -94.2 | 152650 | 223 |
| MR_1774417102_721C6F4E | 152650 | 313 | -86.3 | 152650 | 1002 | -89.2 | 152650 | 360 | -94.3 | 152650 | 223 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 672: `526a5f67-fec...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `526a5f67-fecd-4b2b-ab08-1f55b4c5af71` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[672] topology](images/train_0672.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3240815_3
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase A3 Offset threshold for 3277752_2
- `C4`: Adjust the azimuth of 3240815_3 by 27 degrees
- `C5`: Check test server and transmission issues **← 정답**
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277752_2
- `C7`: Decrease A3 Offset threshold for 3277752_2
- `C8`: Decrease A3 Offset threshold for 3240815_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277752_2
- `C10`: Adjust the azimuth of 3277752_2 by 50 degrees
- `C11`: Add neighbor relationship between 3277752_2 and 3240815_3
- `C12`: Decrease transmission power for 3277752_2
- `C13`: Decrease transmission power for 3240815_3
- `C14`: Lift the tilt angle of 3277752_2 by 6 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240815_3
- `C16`: Increase transmission power for 3277752_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240815_3
- `C18`: Add neighbor relationship between 3232352_4 and 3240815_3
- `C19`: Increase A3 Offset threshold for 3240815_3
- `C20`: Press down the tilt angle of 3277752_2 by 6 degrees
- `C21`: Lift the tilt angle  of 3240815_3 by 10 degrees
- `C22`: Press down the tilt angle  of 3240815_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.504 | MS1 | 121.4656609980 | 31.1446309466 | 67 | 504990 | -86.26 | 15.59 | 323.56 | 0.11 | 2.14 | 1591 |
| 2024-09-20 22:21:32.572 | MS1 | 121.4656647292 | 31.1446287773 | 67 | 504990 | -90.94 | 16.58 | 402.15 | 0.17 | 2.43 | 1598 |
| 2024-09-20 22:21:33.724 | MS1 | 121.4656666542 | 31.1446254345 | 67 | 504990 | -88.09 | 17.65 | 505.87 | 0.15 | 3.00 | 1591 |
| 2024-09-20 22:21:34.183 | MS1 | 121.4656664186 | 31.1446270412 | 67 | 504990 | -85.62 | 14.14 | 62.54 | 0.18 | 2.74 | 386 |
| 2024-09-20 22:21:35.776 | MS1 | 121.4656650941 | 31.1446300732 | 67 | 504990 | -90.95 | 12.36 | 78.07 | 0.15 | 2.19 | 430 |
| 2024-09-20 22:21:36.385 | MS1 | 121.4656689190 | 31.1446322815 | 67 | 504990 | -89.32 | 15.89 | 61.09 | 0.08 | 2.54 | 440 |
| 2024-09-20 22:21:37.489 | MS1 | 121.4656668138 | 31.1446196833 | 67 | 504990 | -89.49 | 10.66 | 48.27 | 0.14 | 2.14 | 416 |
| 2024-09-20 22:21:38.601 | MS1 | 121.4656607196 | 31.1446261332 | 67 | 504990 | -90.36 | 7.96 | 78.57 | 0.01 | 2.53 | 339 |
| 2024-09-20 22:21:39.643 | MS1 | 121.4656746541 | 31.1446303738 | 67 | 504990 | -91.01 | 7.49 | 88.90 | 0.06 | 2.72 | 385 |
| 2024-09-20 22:21:40.806 | MS1 | 121.4656757015 | 31.1446278193 | 67 | 504990 | -93.02 | 9.44 | 331.94 | 0.09 | 2.14 | 1599 |
| 2024-09-20 22:21:41.795 | MS1 | 121.4656616189 | 31.1446311942 | 67 | 504990 | -89.32 | 9.80 | 311.85 | 0.03 | 2.07 | 1585 |
| 2024-09-20 22:21:42.771 | MS1 | 121.4656648380 | 31.1446205770 | 67 | 504990 | -89.83 | 9.84 | 334.79 | 0.20 | 2.54 | 1587 |

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
| 3232352 | 4 | 121.4670267909 | 31.1483759625 | 51 | 4 | 2 | 17.0 | TDD | 54 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3240815 | 3 | 121.4733779209 | 31.1467926927 | 225 | 13 | 11 | 26.9 | TDD | 322 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3246049 | 1 | 121.4718183638 | 31.1492614444 | 231 | 2 | 1 | 28.7 | TDD | 266 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3277752 | 2 | 121.4754131730 | 31.1484574257 | 124 | 4 | 5 | 30.0 | TDD | 67 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.565 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.590 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.701 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.701 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.410 | NREventA3 | measId:2;ServCellPCI:651;Se... |
| 2024-09-20 22:21:38.650 | NRHandoverAttempt | SourcePCI:651;SourceNR-ARFC... |
| 2024-09-20 22:21:38.681 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.692 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.805 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.805 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246049 | 1 | 11.0574 | 10.3891 | -115.5037 | 14.9281 | 141.3305 | 0.0033 | 0.0076 |
| 2024_09_20 22:00 | 3277752 | 2 | 18.6598 | 8.2526 | -115.0160 | 13.4294 | 150.4227 | 0.0048 | 0.0112 |
| 2024_09_20 22:00 | 3240815 | 3 | 10.1389 | 5.6391 | -117.4195 | 5.6078 | 115.9374 | 0.0189 | 0.0036 |
| 2024_09_20 22:00 | 3232352 | 4 | 13.2442 | 5.2282 | -115.7119 | 6.5822 | 174.7278 | 0.0132 | 0.0189 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415828_81BCDA08 | 504990 | 67 | -84.2 | 504990 | 322 | -87.1 | 504990 | 54 | -98.0 | 504990 | 266 |
| MR_1774415828_6C9039D9 | 504990 | 67 | -86.6 | 504990 | 322 | -85.7 | 504990 | 54 | -99.4 | 504990 | 266 |
| MR_1774415828_2A541ADB | 504990 | 67 | -85.5 | 504990 | 322 | -87.3 | 504990 | 54 | -97.1 | 504990 | 266 |
| MR_1774415828_19D933A5 | 504990 | 67 | -84.9 | 504990 | 322 | -85.2 | 504990 | 54 | -99.5 | 504990 | 266 |
| MR_1774415828_16022F8B | 504990 | 67 | -84.3 | 504990 | 322 | -85.6 | 504990 | 54 | -99.5 | 504990 | 266 |
| MR_1774415828_779A0C17 | 504990 | 67 | -84.7 | 504990 | 322 | -85.9 | 504990 | 54 | -97.1 | 504990 | 266 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 673: `bdc05637-d69...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bdc05637-d690-46b0-b3a6-804281f3b012` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235667_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[673] topology](images/train_0673.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3210490_2 by 4 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235667_6 **← 정답**
- `C4`: Decrease A3 Offset threshold for 3235667_6
- `C5`: Decrease transmission power for 3210490_2
- `C6`: Increase transmission power for 3210490_2
- `C7`: Adjust the azimuth of 3210490_2 by 34 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235667_6
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210490_2
- `C10`: Increase transmission power for 3235667_6
- `C11`: Add neighbor relationship between 3241503_8 and 3210490_2
- `C12`: Decrease A3 Offset threshold for 3210490_2
- `C13`: Increase A3 Offset threshold for 3210490_2
- `C14`: Adjust the azimuth of 3235667_6 by 32 degrees
- `C15`: Increase A3 Offset threshold for 3235667_6
- `C16`: Press down the tilt angle  of 3210490_2 by 4 degrees
- `C17`: Lift the tilt angle of 3235667_6 by 6 degrees
- `C18`: Add neighbor relationship between 3235667_6 and 3210490_2
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle of 3235667_6 by 6 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210490_2
- `C22`: Decrease transmission power for 3235667_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.446 | MS1 | 121.4656603337 | 31.1446238797 | 659 | 504990 | -93.96 | 14.68 | 300.90 | 0.02 | 2.97 | 1590 |
| 2024-09-20 22:21:32.677 | MS1 | 121.4656768098 | 31.1446199193 | 882 | 504990 | -94.35 | 10.31 | 397.29 | 0.07 | 2.94 | 1574 |
| 2024-09-20 22:21:33.334 | MS1 | 121.4656725947 | 31.1446292848 | 845 | 504990 | -94.99 | 13.42 | 561.09 | 0.04 | 2.36 | 1580 |
| 2024-09-20 22:21:34.410 | MS1 | 121.4656646183 | 31.1446194233 | 209 | 152650 | -92.27 | 7.96 | 61.05 | 0.14 | 1.96 | 990 |
| 2024-09-20 22:21:35.899 | MS1 | 121.4656730340 | 31.1446249811 | 894 | 152650 | -96.99 | 5.56 | 58.61 | 0.12 | 1.98 | 946 |
| 2024-09-20 22:21:36.847 | MS1 | 121.4656707238 | 31.1446266918 | 300 | 152650 | -88.21 | 7.13 | 79.60 | 0.18 | 1.53 | 922 |
| 2024-09-20 22:21:37.200 | MS1 | 121.4656711425 | 31.1446247416 | 941 | 152650 | -91.45 | 5.78 | 74.81 | 0.19 | 1.87 | 945 |
| 2024-09-20 22:21:38.878 | MS1 | 121.4656631947 | 31.1446299760 | 209 | 152650 | -94.76 | 7.12 | 87.49 | 0.13 | 1.94 | 980 |
| 2024-09-20 22:21:39.973 | MS1 | 121.4656727420 | 31.1446376675 | 894 | 152650 | -96.23 | 4.27 | 103.72 | 0.14 | 1.71 | 902 |
| 2024-09-20 22:21:40.392 | MS1 | 121.4656662354 | 31.1446377827 | 300 | 152650 | -92.04 | 6.56 | 58.30 | 0.16 | 2.78 | 1568 |
| 2024-09-20 22:21:41.399 | MS1 | 121.4656620174 | 31.1446287467 | 941 | 152650 | -92.65 | 7.41 | 44.42 | 0.09 | 2.15 | 1572 |
| 2024-09-20 22:21:42.276 | MS1 | 121.4656627929 | 31.1446185048 | 209 | 152650 | -91.33 | 3.42 | 95.56 | 0.06 | 2.12 | 1582 |

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
| 3210490 | 2 | 121.4698356049 | 31.1481674746 | 259 | 4 | 11 | 2.3 | TDD | 746 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3224946 | 5 | 121.4710570261 | 31.1491126571 | 22 | 15 | 0 | 8.1 | TDD | 882 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3226958 | 4 | 121.4719452577 | 31.1495304862 | 268 | 0 | 11 | 6.8 | TDD | 750 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3235667 | 6 | 121.4759904032 | 31.1553878683 | 251 | 5 | 11 | 24.3 | TDD | 659 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3237057 | 12 | 121.4680658644 | 31.1485097260 | 43 | 15 | 4 | 25.7 | FDD | 791 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3239896 | 10 | 121.4732830389 | 31.1472627217 | 219 | 0 | 11 | 4.2 | FDD | 208 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3241503 | 8 | 121.4674508114 | 31.1493129738 | 350 | 0 | 0 | 3.5 | FDD | 300 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3260779 | 1 | 121.4647763443 | 31.1511062317 | 20 | 2 | 0 | 1.1 | TDD | 420 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3262522 | 3 | 121.4645533452 | 31.1550705752 | 208 | 12 | 4 | 15.9 | TDD | 845 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3263767 | 11 | 121.4690334167 | 31.1536705596 | 272 | 15 | 0 | 6.1 | FDD | 209 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3264366 | 7 | 121.4697304250 | 31.1492857985 | 40 | 11 | 12 | 0.4 | FDD | 834 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3268986 | 13 | 121.4755560478 | 31.1495828754 | 202 | 14 | 12 | 11.2 | FDD | 894 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3275369 | 9 | 121.4723007822 | 31.1475350616 | 1 | 13 | 5 | 14.0 | FDD | 941 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |

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
| 2024-09-20 22:21:31.522 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.542 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.684 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.684 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.355 | NREventA2 | measId:1;ServCellPCI:836;Se... |
| 2024-09-20 22:21:35.503 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.782 | NREventA5 | measId:3;ServCellPCI:836;Se... |
| 2024-09-20 22:21:35.824 | NRHandoverAttempt | SourcePCI:836;SourceNR-ARFC... |
| 2024-09-20 22:21:35.872 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.887 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.031 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.031 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260779 | 1 | 10.3101 | 5.6449 | -117.3286 | 5.4146 | 133.4955 | 0.0016 | 0.0084 |
| 2024_09_20 22:00 | 3210490 | 2 | 11.7417 | 19.6450 | -115.2055 | 15.3864 | 175.7786 | 0.0172 | 0.0049 |
| 2024_09_20 22:00 | 3262522 | 3 | 16.1934 | 12.8108 | -114.8163 | 17.3324 | 149.6604 | 0.0049 | 0.0171 |
| 2024_09_20 22:00 | 3226958 | 4 | 19.1695 | 11.5437 | -115.5614 | 7.3533 | 82.1989 | 0.0082 | 0.0021 |
| 2024_09_20 22:00 | 3224946 | 5 | 19.2870 | 9.7037 | -115.2718 | 10.4496 | 137.1628 | 0.0110 | 0.0097 |
| 2024_09_20 22:00 | 3235667 | 6 | 12.1279 | 12.9589 | -115.5838 | 12.1490 | 100.0466 | 0.0135 | 0.0200 |
| 2024_09_20 22:00 | 3264366 | 7 | 16.6638 | 16.8277 | -114.0163 | 3.8907 | 40.7358 | 0.0121 | 0.0115 |
| 2024_09_20 22:00 | 3241503 | 8 | 14.7101 | 19.3636 | -115.7699 | 4.8376 | 35.3800 | 0.0060 | 0.0034 |
| 2024_09_20 22:00 | 3275369 | 9 | 8.8379 | 14.2373 | -116.3614 | 3.4951 | 43.2464 | 0.0136 | 0.0085 |
| 2024_09_20 22:00 | 3239896 | 10 | 7.6567 | 13.3471 | -115.2817 | 3.8291 | 22.7136 | 0.0161 | 0.0091 |
| 2024_09_20 22:00 | 3263767 | 11 | 13.7334 | 9.0031 | -115.6084 | 4.2723 | 42.4219 | 0.0135 | 0.0176 |
| 2024_09_20 22:00 | 3237057 | 12 | 12.6166 | 10.8714 | -114.3584 | 4.1649 | 20.0732 | 0.0023 | 0.0108 |
| 2024_09_20 22:00 | 3268986 | 13 | 19.5789 | 16.7626 | -116.6545 | 3.1527 | 24.5400 | 0.0014 | 0.0114 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414882_69FFBBB8 | 152650 | 209 | -93.5 | 152650 | 208 | -96.7 | 152650 | 791 | -103.0 | 152650 | 834 |
| MR_1774414882_159BFE9A | 152650 | 209 | -92.2 | 152650 | 208 | -97.6 | 152650 | 791 | -99.9 | 152650 | 834 |
| MR_1774414882_DE9B0CA2 | 504990 | 845 | -94.4 | 504990 | 746 | -93.0 | 504990 | 420 | -99.9 | 504990 | 750 |
| MR_1774414882_B954847F | 504990 | 845 | -93.1 | 504990 | 746 | -92.4 | 504990 | 420 | -99.8 | 504990 | 750 |
| MR_1774414882_5630AA56 | 504990 | 845 | -93.4 | 504990 | 746 | -94.8 | 504990 | 420 | -100.5 | 504990 | 750 |
| MR_1774414882_00B785D2 | 152650 | 209 | -93.8 | 152650 | 208 | -96.7 | 152650 | 791 | -101.2 | 152650 | 834 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 674: `d303f985-a0b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d303f985-a0b0-4548-af51-49dff94703d5` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[674] topology](images/train_0674.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues **← 정답**
- `C2`: Lift the tilt angle of 3236097_2 by 10 degrees
- `C3`: Press down the tilt angle  of 3239946_1 by 9 degrees
- `C4`: Add neighbor relationship between 3228687_4 and 3239946_1
- `C5`: Decrease transmission power for 3239946_1
- `C6`: Increase A3 Offset threshold for 3236097_2
- `C7`: Decrease transmission power for 3236097_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239946_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236097_2
- `C10`: Increase A3 Offset threshold for 3239946_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239946_1
- `C12`: Add neighbor relationship between 3236097_2 and 3239946_1
- `C13`: Increase transmission power for 3236097_2
- `C14`: Lift the tilt angle  of 3239946_1 by 9 degrees
- `C15`: Adjust the azimuth of 3236097_2 by 50 degrees
- `C16`: Adjust the azimuth of 3239946_1 by 50 degrees
- `C17`: Decrease A3 Offset threshold for 3239946_1
- `C18`: Increase transmission power for 3239946_1
- `C19`: Press down the tilt angle of 3236097_2 by 10 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236097_2
- `C21`: Decrease A3 Offset threshold for 3236097_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.713 | MS1 | 121.4656759219 | 31.1446298254 | 789 | 504990 | -88.59 | 13.22 | 500.68 | 0.05 | 2.43 | 1598 |
| 2024-09-20 22:21:32.716 | MS1 | 121.4656745213 | 31.1446291095 | 789 | 504990 | -91.47 | 12.95 | 338.60 | 0.12 | 2.37 | 1592 |
| 2024-09-20 22:21:33.561 | MS1 | 121.4656597909 | 31.1446328297 | 789 | 504990 | -86.89 | 13.24 | 511.61 | 0.09 | 2.05 | 1563 |
| 2024-09-20 22:21:34.303 | MS1 | 121.4656644064 | 31.1446210221 | 789 | 504990 | -86.67 | 16.37 | 64.36 | 0.02 | 2.74 | 406 |
| 2024-09-20 22:21:35.814 | MS1 | 121.4656687873 | 31.1446294598 | 789 | 504990 | -90.36 | 16.13 | 69.84 | 0.08 | 2.18 | 433 |
| 2024-09-20 22:21:36.330 | MS1 | 121.4656734017 | 31.1446241242 | 789 | 504990 | -89.98 | 14.60 | 87.83 | 0.00 | 2.52 | 485 |
| 2024-09-20 22:21:37.556 | MS1 | 121.4656597193 | 31.1446293692 | 789 | 504990 | -92.28 | 7.42 | 53.50 | 0.16 | 2.91 | 320 |
| 2024-09-20 22:21:38.574 | MS1 | 121.4656647652 | 31.1446343761 | 789 | 504990 | -90.12 | 11.57 | 56.10 | 0.07 | 2.16 | 397 |
| 2024-09-20 22:21:39.206 | MS1 | 121.4656733981 | 31.1446379160 | 789 | 504990 | -91.02 | 7.48 | 86.33 | 0.09 | 2.97 | 328 |
| 2024-09-20 22:21:40.611 | MS1 | 121.4656615770 | 31.1446224782 | 789 | 504990 | -91.26 | 8.18 | 507.07 | 0.17 | 2.31 | 1593 |
| 2024-09-20 22:21:41.133 | MS1 | 121.4656625420 | 31.1446224082 | 789 | 504990 | -93.83 | 12.41 | 537.48 | 0.12 | 2.66 | 1578 |
| 2024-09-20 22:21:42.242 | MS1 | 121.4656586432 | 31.1446187071 | 789 | 504990 | -93.52 | 9.75 | 588.81 | 0.16 | 2.31 | 1597 |

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
| 3218420 | 3 | 121.4707923618 | 31.1553918637 | 29 | 6 | 6 | 45.6 | TDD | 494 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3228687 | 4 | 121.4715223321 | 31.1528633332 | 146 | 1 | 11 | 36.1 | TDD | 855 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3236097 | 2 | 121.4744217887 | 31.1476801362 | 89 | 15 | 11 | 20.7 | TDD | 789 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3239946 | 1 | 121.4752389785 | 31.1459606181 | 77 | 7 | 5 | 26.5 | TDD | 640 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.073 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.073 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.792 | NREventA3 | measId:2;ServCellPCI:606;Se... |
| 2024-09-20 22:21:38.032 | NRHandoverAttempt | SourcePCI:606;SourceNR-ARFC... |
| 2024-09-20 22:21:38.082 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.092 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.241 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.241 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239946 | 1 | 19.8073 | 12.8186 | -117.5552 | 12.5972 | 126.0638 | 0.0177 | 0.0075 |
| 2024_09_20 22:00 | 3236097 | 2 | 13.2702 | 11.6653 | -115.5282 | 14.8572 | 96.6564 | 0.0093 | 0.0040 |
| 2024_09_20 22:00 | 3218420 | 3 | 13.3844 | 7.2222 | -115.2456 | 10.2061 | 180.7175 | 0.0175 | 0.0062 |
| 2024_09_20 22:00 | 3228687 | 4 | 7.5652 | 10.6276 | -117.4320 | 16.3181 | 130.8471 | 0.0105 | 0.0186 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413718_783DFA02 | 504990 | 789 | -85.5 | 504990 | 640 | -92.0 | 504990 | 855 | -98.8 | 504990 | 494 |
| MR_1774413718_6AF14D95 | 504990 | 789 | -85.9 | 504990 | 640 | -92.0 | 504990 | 855 | -97.8 | 504990 | 494 |
| MR_1774413718_1052C7E2 | 504990 | 789 | -85.6 | 504990 | 640 | -93.6 | 504990 | 855 | -100.7 | 504990 | 494 |
| MR_1774413718_E0929000 | 504990 | 789 | -85.8 | 504990 | 640 | -91.9 | 504990 | 855 | -99.9 | 504990 | 494 |
| MR_1774413718_2BB3CBDC | 504990 | 789 | -87.4 | 504990 | 640 | -93.4 | 504990 | 855 | -98.5 | 504990 | 494 |
| MR_1774413718_CC058173 | 504990 | 789 | -86.8 | 504990 | 640 | -93.3 | 504990 | 855 | -97.3 | 504990 | 494 |
| MR_1774413718_3666A3A6 | 504990 | 789 | -85.6 | 504990 | 640 | -93.6 | 504990 | 855 | -100.4 | 504990 | 494 |
| MR_1774413718_AF374411 | 504990 | 789 | -85.2 | 504990 | 640 | -91.5 | 504990 | 855 | -97.6 | 504990 | 494 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 675: `b821388a-cf3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b821388a-cf33-4220-8530-a937877fa2c6` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Decrease A3 Offset threshold for 3250764_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[675] topology](images/train_0675.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250764_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263486_4
- `C3`: Lift the tilt angle of 3250764_1 by 1 degrees
- `C4`: Decrease A3 Offset threshold for 3250764_1 **← 정답**
- `C5`: Increase A3 Offset threshold for 3250764_1
- `C6`: Check test server and transmission issues
- `C7`: Decrease transmission power for 3263486_4
- `C8`: Decrease transmission power for 3250764_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263486_4
- `C10`: Add neighbor relationship between 3212761_2 and 3263486_4
- `C11`: Press down the tilt angle of 3250764_1 by 1 degrees
- `C12`: Increase transmission power for 3263486_4
- `C13`: Decrease A3 Offset threshold for 3263486_4
- `C14`: Press down the tilt angle  of 3263486_4 by 10 degrees
- `C15`: Increase A3 Offset threshold for 3263486_4
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Add neighbor relationship between 3250764_1 and 3263486_4
- `C18`: Adjust the azimuth of 3250764_1 by 50 degrees
- `C19`: Lift the tilt angle  of 3263486_4 by 10 degrees
- `C20`: Increase transmission power for 3250764_1
- `C21`: Adjust the azimuth of 3263486_4 by 45 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250764_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.375 | MS1 | 121.4656693466 | 31.1446247286 | 960 | 504990 | -81.72 | 13.48 | 518.76 | 0.08 | 2.13 | 1599 |
| 2024-09-20 22:21:32.303 | MS1 | 121.4656668680 | 31.1446330857 | 960 | 504990 | -78.71 | 15.90 | 518.51 | 0.01 | 2.38 | 1586 |
| 2024-09-20 22:21:33.471 | MS1 | 121.4656610194 | 31.1446360746 | 960 | 504990 | -79.82 | 16.42 | 307.82 | 0.01 | 2.92 | 1568 |
| 2024-09-20 22:21:34.855 | MS1 | 121.4656606715 | 31.1446304198 | 960 | 504990 | -83.75 | -0.79 | 71.40 | 0.08 | 1.21 | 1573 |
| 2024-09-20 22:21:35.732 | MS1 | 121.4656735781 | 31.1446244826 | 960 | 504990 | -91.54 | -1.64 | 66.93 | 0.00 | 1.37 | 1592 |
| 2024-09-20 22:21:36.260 | MS1 | 121.4656703709 | 31.1446284818 | 960 | 504990 | -87.03 | -0.49 | 52.42 | 0.17 | 1.01 | 1600 |
| 2024-09-20 22:21:37.447 | MS1 | 121.4656670103 | 31.1446243816 | 960 | 504990 | -87.99 | -1.74 | 45.02 | 0.12 | 1.20 | 1560 |
| 2024-09-20 22:21:38.812 | MS1 | 121.4656626803 | 31.1446255905 | 960 | 504990 | -92.38 | -1.38 | 45.71 | 0.03 | 1.44 | 1590 |
| 2024-09-20 22:21:39.709 | MS1 | 121.4656607902 | 31.1446195472 | 766 | 504990 | -81.19 | 16.77 | 254.27 | 0.13 | 1.35 | 1593 |
| 2024-09-20 22:21:40.883 | MS1 | 121.4656625241 | 31.1446317483 | 766 | 504990 | -77.68 | 15.53 | 356.97 | 0.04 | 2.45 | 1593 |
| 2024-09-20 22:21:41.222 | MS1 | 121.4656593891 | 31.1446368008 | 766 | 504990 | -78.46 | 16.04 | 409.72 | 0.18 | 2.09 | 1598 |
| 2024-09-20 22:21:42.954 | MS1 | 121.4656707440 | 31.1446233218 | 766 | 504990 | -78.50 | 14.34 | 543.70 | 0.09 | 2.80 | 1570 |

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
| 3212761 | 2 | 121.4713761784 | 31.1534191382 | 81 | 3 | 1 | 31.9 | TDD | 721 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3250764 | 1 | 121.4728245964 | 31.1518025349 | 89 | 0 | 3 | 22.2 | TDD | 960 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3263486 | 4 | 121.4671792969 | 31.1533977020 | 143 | 13 | 3 | 31.7 | TDD | 766 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3264110 | 3 | 121.4694259757 | 31.1535446953 | 11 | 0 | 1 | 43.1 | TDD | 131 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.739 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.762 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.863 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.863 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.614 | NREventA3 | measId:2;ServCellPCI:225;Se... |
| 2024-09-20 22:21:37.854 | NRHandoverAttempt | SourcePCI:225;SourceNR-ARFC... |
| 2024-09-20 22:21:37.898 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.909 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.015 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.015 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250764 | 1 | 10.1736 | 9.1964 | -114.7893 | 8.3287 | 180.8229 | 0.0092 | 0.1045 |
| 2024_09_20 22:00 | 3212761 | 2 | 15.2853 | 5.3917 | -116.5965 | 13.2804 | 182.0965 | 0.0174 | 0.0151 |
| 2024_09_20 22:00 | 3264110 | 3 | 7.9153 | 17.6116 | -116.3070 | 5.7574 | 100.6567 | 0.0013 | 0.0138 |
| 2024_09_20 22:00 | 3263486 | 4 | 19.3519 | 13.5949 | -117.1524 | 15.6069 | 124.7079 | 0.0132 | 0.0018 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416990_0C57F0B7 | 504990 | 960 | -82.8 | 504990 | 766 | -77.2 | 504990 | 721 | -86.0 | 504990 | 131 |
| MR_1774416990_3228058C | 504990 | 960 | -83.6 | 504990 | 766 | -78.0 | 504990 | 721 | -85.3 | 504990 | 131 |
| MR_1774416990_CA9FC975 | 504990 | 960 | -81.8 | 504990 | 766 | -79.6 | 504990 | 721 | -86.0 | 504990 | 131 |
| MR_1774416990_38C6DB60 | 504990 | 960 | -85.0 | 504990 | 766 | -79.2 | 504990 | 721 | -85.4 | 504990 | 131 |
| MR_1774416990_B03B32D1 | 504990 | 766 | -77.8 | 504990 | 960 | -85.4 | 504990 | 721 | -84.5 | 504990 | 131 |
| MR_1774416990_8CCECB0F | 504990 | 960 | -82.1 | 504990 | 766 | -78.8 | 504990 | 721 | -85.8 | 504990 | 131 |
| MR_1774416990_2917D4F1 | 504990 | 766 | -78.0 | 504990 | 960 | -84.7 | 504990 | 721 | -84.3 | 504990 | 131 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 676: `65b3ac33-e0c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `65b3ac33-e0c1-41ab-a4d0-b8350e552ebc` |
| Tag | **multiple-answer** |
| 정답 | **C8|C15** |
| C8 의미 | Adjust the azimuth of 3263035_2 by 50 degrees |
| C15 의미 | Increase transmission power for 3263035_2 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[676] topology](images/train_0676.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3249871_4
- `C2`: Check test server and transmission issues
- `C3`: Add neighbor relationship between 3238618_1 and 3249871_4
- `C4`: Increase A3 Offset threshold for 3263035_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263035_2
- `C6`: Press down the tilt angle of 3263035_2 by 10 degrees
- `C7`: Lift the tilt angle of 3263035_2 by 10 degrees
- `C8`: Adjust the azimuth of 3263035_2 by 50 degrees **← 정답**
- `C9`: Adjust the azimuth of 3249871_4 by 48 degrees
- `C10`: Lift the tilt angle  of 3249871_4 by 2 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249871_4
- `C12`: Increase A3 Offset threshold for 3249871_4
- `C13`: Decrease transmission power for 3263035_2
- `C14`: Decrease transmission power for 3249871_4
- `C15`: Increase transmission power for 3263035_2 **← 정답**
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249871_4
- `C17`: Add neighbor relationship between 3263035_2 and 3249871_4
- `C18`: Decrease A3 Offset threshold for 3249871_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263035_2
- `C20`: Press down the tilt angle  of 3249871_4 by 2 degrees
- `C21`: Decrease A3 Offset threshold for 3263035_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.392 | MS1 | 121.4656622270 | 31.1446210447 | 530 | 504990 | -87.11 | 16.69 | 429.85 | 0.16 | 2.93 | 1578 |
| 2024-09-20 22:21:32.716 | MS1 | 121.4656610922 | 31.1446223325 | 530 | 504990 | -86.11 | 16.88 | 441.86 | 0.18 | 2.50 | 1574 |
| 2024-09-20 22:21:33.325 | MS1 | 121.4656731391 | 31.1446239259 | 530 | 504990 | -86.59 | 13.07 | 510.36 | 0.13 | 2.51 | 1589 |
| 2024-09-20 22:21:34.711 | MS1 | 121.4656777634 | 31.1446358442 | 530 | 504990 | -103.12 | -0.06 | 78.44 | 0.15 | 1.05 | 1580 |
| 2024-09-20 22:21:35.429 | MS1 | 121.4656640542 | 31.1446212024 | 530 | 504990 | -101.61 | -0.20 | 36.58 | 0.15 | 1.45 | 1600 |
| 2024-09-20 22:21:36.214 | MS1 | 121.4656589908 | 31.1446307829 | 530 | 504990 | -108.28 | -1.35 | 88.53 | 0.17 | 1.36 | 1595 |
| 2024-09-20 22:21:37.508 | MS1 | 121.4656700017 | 31.1446357246 | 530 | 504990 | -101.57 | 0.94 | 81.44 | 0.14 | 1.32 | 1582 |
| 2024-09-20 22:21:38.493 | MS1 | 121.4656766450 | 31.1446277245 | 530 | 504990 | -107.46 | 1.85 | 21.44 | 0.01 | 1.42 | 1575 |
| 2024-09-20 22:21:39.291 | MS1 | 121.4656624337 | 31.1446223401 | 530 | 504990 | -109.43 | -0.02 | 43.51 | 0.16 | 1.21 | 1580 |
| 2024-09-20 22:21:40.769 | MS1 | 121.4656586367 | 31.1446336133 | 530 | 504990 | -91.75 | 17.12 | 415.13 | 0.17 | 2.00 | 1573 |
| 2024-09-20 22:21:41.312 | MS1 | 121.4656722034 | 31.1446278480 | 530 | 504990 | -90.70 | 16.80 | 315.38 | 0.08 | 2.98 | 1581 |
| 2024-09-20 22:21:42.621 | MS1 | 121.4656661283 | 31.1446256719 | 530 | 504990 | -86.34 | 13.80 | 513.93 | 0.07 | 2.75 | 1588 |

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
| 3238618 | 1 | 121.4647311736 | 31.1489781239 | 302 | 11 | 0 | 50.0 | TDD | 848 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3246844 | 3 | 121.4663495879 | 31.1483586082 | 32 | 5 | 0 | 32.4 | TDD | 396 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3249871 | 4 | 121.4758975965 | 31.1454844859 | 312 | 1 | 0 | 16.8 | TDD | 967 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3263035 | 2 | 121.4695885907 | 31.1532193052 | 123 | 11 | 9 | 22.8 | TDD | 530 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.134 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.154 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.260 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.260 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.528 | NREventA2 | measId:1;ServCellPCI:558;Se... |
| 2024-09-20 22:21:34.648 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238618 | 1 | 19.9689 | 11.0558 | -117.7379 | 19.3232 | 141.3982 | 0.0093 | 0.0189 |
| 2024_09_20 22:00 | 3263035 | 2 | 19.1188 | 12.5116 | -117.7869 | 14.7107 | 178.3580 | 0.1706 | 0.0027 |
| 2024_09_20 22:00 | 3246844 | 3 | 8.4501 | 13.3957 | -114.5083 | 10.5614 | 96.6739 | 0.0191 | 0.0186 |
| 2024_09_20 22:00 | 3249871 | 4 | 17.4744 | 6.5318 | -114.0733 | 7.4255 | 88.3772 | 0.0161 | 0.0021 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416172_0EED2AA5 | 504990 | 530 | -104.3 | 504990 | 967 | -107.1 | 504990 | 848 | -112.9 | 504990 | 396 |
| MR_1774416172_0233D604 | 504990 | 530 | -104.6 | 504990 | 967 | -104.7 | 504990 | 848 | -111.1 | 504990 | 396 |
| MR_1774416172_16BF8C1A | 504990 | 530 | -104.7 | 504990 | 967 | -106.2 | 504990 | 848 | -112.8 | 504990 | 396 |
| MR_1774416172_FAAEA585 | 504990 | 530 | -102.2 | 504990 | 967 | -108.1 | 504990 | 848 | -110.7 | 504990 | 396 |
| MR_1774416172_6B7C6F28 | 504990 | 530 | -102.3 | 504990 | 967 | -106.8 | 504990 | 848 | -110.7 | 504990 | 396 |
| MR_1774416172_59EB7B12 | 504990 | 530 | -101.4 | 504990 | 967 | -106.2 | 504990 | 848 | -112.9 | 504990 | 396 |
| MR_1774416172_E015CC39 | 504990 | 530 | -102.1 | 504990 | 967 | -106.3 | 504990 | 848 | -113.3 | 504990 | 396 |
| MR_1774416172_16F6557E | 504990 | 530 | -104.1 | 504990 | 967 | -107.5 | 504990 | 848 | -113.8 | 504990 | 396 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 677: `ae455e86-83d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ae455e86-83da-4714-a167-107d38d03833` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264067_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[677] topology](images/train_0677.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Add neighbor relationship between 3264067_5 and 3259418_1
- `C3`: Increase A3 Offset threshold for 3264067_5
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259418_1
- `C5`: Add neighbor relationship between 3264346_8 and 3259418_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264067_5
- `C7`: Lift the tilt angle  of 3259418_1 by 2 degrees
- `C8`: Adjust the azimuth of 3264067_5 by 22 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Press down the tilt angle of 3264067_5 by 4 degrees
- `C11`: Increase transmission power for 3259418_1
- `C12`: Decrease A3 Offset threshold for 3264067_5
- `C13`: Lift the tilt angle of 3264067_5 by 4 degrees
- `C14`: Decrease transmission power for 3259418_1
- `C15`: Adjust the azimuth of 3259418_1 by 34 degrees
- `C16`: Decrease transmission power for 3264067_5
- `C17`: Decrease A3 Offset threshold for 3259418_1
- `C18`: Press down the tilt angle  of 3259418_1 by 2 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259418_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264067_5 **← 정답**
- `C21`: Increase A3 Offset threshold for 3259418_1
- `C22`: Increase transmission power for 3264067_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.996 | MS1 | 121.4656614261 | 31.1446362961 | 316 | 504990 | -94.68 | 14.89 | 371.51 | 0.05 | 2.98 | 1596 |
| 2024-09-20 22:21:32.423 | MS1 | 121.4656714221 | 31.1446248592 | 253 | 504990 | -94.56 | 14.67 | 541.39 | 0.05 | 2.44 | 1593 |
| 2024-09-20 22:21:33.212 | MS1 | 121.4656709248 | 31.1446341281 | 891 | 504990 | -95.60 | 11.85 | 475.82 | 0.08 | 2.42 | 1577 |
| 2024-09-20 22:21:34.856 | MS1 | 121.4656768700 | 31.1446253029 | 71 | 152650 | -95.65 | 7.39 | 79.24 | 0.10 | 1.78 | 919 |
| 2024-09-20 22:21:35.330 | MS1 | 121.4656652626 | 31.1446360324 | 483 | 152650 | -93.78 | 2.63 | 108.02 | 0.02 | 1.57 | 978 |
| 2024-09-20 22:21:36.746 | MS1 | 121.4656626559 | 31.1446270274 | 422 | 152650 | -92.08 | 6.86 | 95.86 | 0.04 | 1.83 | 940 |
| 2024-09-20 22:21:37.482 | MS1 | 121.4656626395 | 31.1446199071 | 180 | 152650 | -95.41 | 4.55 | 92.27 | 0.19 | 1.80 | 937 |
| 2024-09-20 22:21:38.861 | MS1 | 121.4656738376 | 31.1446346107 | 71 | 152650 | -94.59 | 3.70 | 95.14 | 0.00 | 1.60 | 995 |
| 2024-09-20 22:21:39.992 | MS1 | 121.4656700778 | 31.1446200230 | 483 | 152650 | -90.13 | 7.19 | 78.00 | 0.17 | 1.62 | 909 |
| 2024-09-20 22:21:40.336 | MS1 | 121.4656737198 | 31.1446311368 | 422 | 152650 | -92.17 | 5.78 | 75.05 | 0.08 | 2.34 | 1588 |
| 2024-09-20 22:21:41.887 | MS1 | 121.4656673912 | 31.1446249335 | 180 | 152650 | -90.11 | 3.74 | 71.98 | 0.09 | 2.92 | 1597 |
| 2024-09-20 22:21:42.272 | MS1 | 121.4656695113 | 31.1446338162 | 71 | 152650 | -88.34 | 5.02 | 92.06 | 0.18 | 2.54 | 1565 |

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
| 3212184 | 7 | 121.4724056313 | 31.1496110041 | 34 | 14 | 9 | 12.8 | FDD | 483 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3223088 | 3 | 121.4705641258 | 31.1554668277 | 290 | 0 | 7 | 1.5 | TDD | 826 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3231835 | 11 | 121.4732944362 | 31.1509740446 | 188 | 2 | 0 | 13.4 | FDD | 180 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3237370 | 12 | 121.4727629659 | 31.1550428158 | 81 | 10 | 1 | 20.0 | FDD | 759 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3238647 | 13 | 121.4753133731 | 31.1491338344 | 153 | 2 | 4 | 22.8 | FDD | 57 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3242664 | 9 | 121.4759274604 | 31.1501316904 | 200 | 11 | 2 | 10.5 | FDD | 71 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3253278 | 10 | 121.4755961884 | 31.1548989809 | 350 | 11 | 9 | 15.9 | FDD | 45 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3259418 | 1 | 121.4711375694 | 31.1443699456 | 239 | 2 | 8 | 1.8 | TDD | 143 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3262747 | 2 | 121.4708768315 | 31.1452026077 | 161 | 9 | 1 | 9.4 | TDD | 657 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3264067 | 5 | 121.4738809002 | 31.1460096877 | 281 | 2 | 3 | 27.6 | TDD | 316 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3264346 | 8 | 121.4644470046 | 31.1551957088 | 51 | 0 | 5 | 0.7 | FDD | 422 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3266488 | 4 | 121.4676620421 | 31.1542733742 | 208 | 8 | 8 | 5.1 | TDD | 891 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3268941 | 6 | 121.4671274572 | 31.1465909548 | 277 | 0 | 5 | 0.9 | TDD | 253 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.131 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.155 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.284 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.284 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.023 | NREventA2 | measId:1;ServCellPCI:10;Ser... |
| 2024-09-20 22:21:35.143 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.399 | NREventA5 | measId:3;ServCellPCI:10;Ser... |
| 2024-09-20 22:21:35.454 | NRHandoverAttempt | SourcePCI:10;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.486 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.498 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.636 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.636 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259418 | 1 | 19.7062 | 15.0674 | -116.0947 | 7.9179 | 161.7246 | 0.0112 | 0.0196 |
| 2024_09_20 22:00 | 3262747 | 2 | 9.3530 | 10.1381 | -115.7926 | 9.2507 | 89.5500 | 0.0100 | 0.0083 |
| 2024_09_20 22:00 | 3223088 | 3 | 11.9266 | 18.2511 | -117.6022 | 13.5518 | 100.4191 | 0.0020 | 0.0092 |
| 2024_09_20 22:00 | 3266488 | 4 | 9.7777 | 16.0200 | -117.3397 | 6.8888 | 99.3399 | 0.0069 | 0.0177 |
| 2024_09_20 22:00 | 3264067 | 5 | 18.9066 | 8.4340 | -117.6306 | 18.8407 | 112.8691 | 0.0158 | 0.0001 |
| 2024_09_20 22:00 | 3268941 | 6 | 10.9480 | 19.7507 | -115.3557 | 14.1388 | 141.2597 | 0.0033 | 0.0174 |
| 2024_09_20 22:00 | 3212184 | 7 | 8.4041 | 9.1535 | -114.6730 | 3.3463 | 53.0528 | 0.0167 | 0.0070 |
| 2024_09_20 22:00 | 3264346 | 8 | 10.8619 | 14.8903 | -114.6808 | 4.7307 | 52.7316 | 0.0073 | 0.0087 |
| 2024_09_20 22:00 | 3242664 | 9 | 12.6459 | 5.5918 | -116.8681 | 4.7940 | 22.3820 | 0.0196 | 0.0077 |
| 2024_09_20 22:00 | 3253278 | 10 | 15.1851 | 7.0818 | -116.9789 | 4.9423 | 36.4991 | 0.0130 | 0.0049 |
| 2024_09_20 22:00 | 3231835 | 11 | 7.0766 | 18.8297 | -114.3372 | 4.3167 | 45.9239 | 0.0008 | 0.0150 |
| 2024_09_20 22:00 | 3237370 | 12 | 13.1023 | 7.9893 | -117.7300 | 4.9476 | 28.0916 | 0.0036 | 0.0042 |
| 2024_09_20 22:00 | 3238647 | 13 | 8.7300 | 12.1997 | -114.8879 | 3.1171 | 21.7691 | 0.0178 | 0.0199 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416669_3E9449A8 | 152650 | 71 | -94.0 | 152650 | 45 | -98.1 | 152650 | 759 | -101.5 | 152650 | 57 |
| MR_1774416669_0BBBF844 | 152650 | 71 | -96.4 | 152650 | 45 | -98.5 | 152650 | 759 | -102.5 | 152650 | 57 |
| MR_1774416669_2C7E3681 | 152650 | 71 | -93.8 | 152650 | 45 | -99.4 | 152650 | 759 | -103.6 | 152650 | 57 |
| MR_1774416669_BB161923 | 504990 | 891 | -97.3 | 504990 | 143 | -96.2 | 504990 | 826 | -104.4 | 504990 | 657 |
| MR_1774416669_580F7A6E | 504990 | 891 | -94.7 | 504990 | 143 | -97.8 | 504990 | 826 | -102.4 | 504990 | 657 |
| MR_1774416669_37D8B0F0 | 152650 | 71 | -97.0 | 152650 | 45 | -100.9 | 152650 | 759 | -101.1 | 152650 | 57 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 678: `fd8868b0-895...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fd8868b0-8954-4dca-a846-de48171140ad` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Lift the tilt angle  of 3247411_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[678] topology](images/train_0678.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217662_4
- `C3`: Decrease transmission power for 3218733_2
- `C4`: Adjust the azimuth of 3217662_4 by 12 degrees
- `C5`: Decrease A3 Offset threshold for 3218733_2
- `C6`: Increase transmission power for 3218733_2
- `C7`: Increase transmission power for 3217662_4
- `C8`: Decrease A3 Offset threshold for 3217662_4
- `C9`: Check test server and transmission issues
- `C10`: Press down the tilt angle of 3217662_4 by 3 degrees
- `C11`: Increase A3 Offset threshold for 3218733_2
- `C12`: Lift the tilt angle of 3217662_4 by 3 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217662_4
- `C14`: Lift the tilt angle  of 3247411_1 by 10 degrees **← 정답**
- `C15`: Decrease transmission power for 3217662_4
- `C16`: Add neighbor relationship between 3217662_4 and 3218733_2
- `C17`: Increase A3 Offset threshold for 3217662_4
- `C18`: Add neighbor relationship between 3247411_1 and 3218733_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218733_2
- `C20`: Adjust the azimuth of 3247411_1 by 50 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218733_2
- `C22`: Press down the tilt angle  of 3247411_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.397 | MS1 | 121.4656680513 | 31.1446336070 | 831 | 504990 | -90.74 | 16.09 | 367.96 | 0.01 | 2.73 | 1568 |
| 2024-09-20 22:21:32.795 | MS1 | 121.4656583150 | 31.1446374409 | 831 | 504990 | -88.98 | 15.52 | 525.72 | 0.11 | 2.94 | 1590 |
| 2024-09-20 22:21:33.932 | MS1 | 121.4656640853 | 31.1446222812 | 831 | 504990 | -85.77 | 17.53 | 432.83 | 0.20 | 2.17 | 1586 |
| 2024-09-20 22:21:34.887 | MS1 | 121.4656655766 | 31.1446330595 | 831 | 504990 | -85.15 | 14.95 | 72.14 | 0.18 | 2.16 | 1567 |
| 2024-09-20 22:21:35.574 | MS1 | 121.4656732956 | 31.1446353668 | 831 | 504990 | -91.93 | 17.45 | 88.49 | 0.02 | 2.44 | 1572 |
| 2024-09-20 22:21:36.242 | MS1 | 121.4656695068 | 31.1446314076 | 831 | 504990 | -85.97 | 15.64 | 91.66 | 0.18 | 2.98 | 1569 |
| 2024-09-20 22:21:37.373 | MS1 | 121.4656710845 | 31.1446260564 | 831 | 504990 | -92.28 | 8.15 | 60.04 | 0.09 | 2.05 | 1571 |
| 2024-09-20 22:21:38.402 | MS1 | 121.4656715127 | 31.1446357727 | 831 | 504990 | -90.81 | 7.39 | 88.60 | 0.03 | 2.55 | 1594 |
| 2024-09-20 22:21:39.107 | MS1 | 121.4656666665 | 31.1446242339 | 831 | 504990 | -92.30 | 11.63 | 94.05 | 0.04 | 2.02 | 1583 |
| 2024-09-20 22:21:40.352 | MS1 | 121.4656589488 | 31.1446216661 | 831 | 504990 | -91.80 | 11.07 | 486.47 | 0.19 | 2.16 | 1597 |
| 2024-09-20 22:21:41.349 | MS1 | 121.4656685586 | 31.1446263297 | 831 | 504990 | -92.50 | 8.28 | 355.12 | 0.13 | 2.78 | 1560 |
| 2024-09-20 22:21:42.660 | MS1 | 121.4656606168 | 31.1446197127 | 831 | 504990 | -90.93 | 7.14 | 441.97 | 0.06 | 2.57 | 1564 |

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
| 3217662 | 4 | 121.4641299815 | 31.1503566139 | 179 | 0 | 9 | 30.1 | TDD | 831 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3218733 | 2 | 121.4708119874 | 31.1537486304 | 280 | 8 | 2 | 39.4 | TDD | 356 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3247411 | 1 | 121.4690501573 | 31.1522150168 | 45 | 14 | 5 | 24.3 | TDD | 633 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3273289 | 3 | 121.4702044384 | 31.1457510632 | 139 | 1 | 7 | 38.6 | TDD | 796 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.874 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.890 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.018 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.018 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.724 | NREventA3 | measId:2;ServCellPCI:708;Se... |
| 2024-09-20 22:21:37.964 | NRHandoverAttempt | SourcePCI:708;SourceNR-ARFC... |
| 2024-09-20 22:21:38.001 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.015 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.128 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.128 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247411 | 1 | 13.7816 | 13.5795 | -114.5509 | 8.9356 | 136.9219 | 0.0121 | 0.0008 |
| 2024_09_20 22:00 | 3218733 | 2 | 12.8873 | 19.0575 | -116.8123 | 8.7694 | 165.7898 | 0.0110 | 0.0197 |
| 2024_09_20 22:00 | 3273289 | 3 | 5.8929 | 17.5325 | -117.6007 | 15.2141 | 129.6560 | 0.0105 | 0.0010 |
| 2024_09_20 22:00 | 3217662 | 4 | 94.3960 | 91.3572 | -114.8445 | 8.3777 | 199.4291 | 0.0158 | 0.0038 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416008_BBD397E4 | 504990 | 831 | -85.9 | 504990 | 356 | -95.2 | 504990 | 633 | -97.2 | 504990 | 796 |
| MR_1774416008_5A5AF14A | 504990 | 831 | -84.5 | 504990 | 356 | -92.5 | 504990 | 633 | -97.3 | 504990 | 796 |
| MR_1774416008_AB80CE73 | 504990 | 831 | -84.4 | 504990 | 356 | -95.7 | 504990 | 633 | -96.3 | 504990 | 796 |
| MR_1774416008_AFADBBFF | 504990 | 831 | -83.6 | 504990 | 356 | -95.3 | 504990 | 633 | -94.7 | 504990 | 796 |
| MR_1774416008_AA3319ED | 504990 | 831 | -85.0 | 504990 | 356 | -92.9 | 504990 | 633 | -97.5 | 504990 | 796 |
| MR_1774416008_1ABFEB78 | 504990 | 831 | -87.1 | 504990 | 356 | -93.7 | 504990 | 633 | -96.4 | 504990 | 796 |
| MR_1774416008_A49030B7 | 504990 | 831 | -86.3 | 504990 | 356 | -93.0 | 504990 | 633 | -95.4 | 504990 | 796 |
| MR_1774416008_B6522294 | 504990 | 831 | -86.2 | 504990 | 356 | -94.1 | 504990 | 633 | -97.3 | 504990 | 796 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 679: `228bf361-6da...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `228bf361-6dac-45d0-a4cc-e9b1e78a9615` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Lift the tilt angle  of 3253931_1 by 4 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[679] topology](images/train_0679.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3275187_3
- `C2`: Lift the tilt angle of 3214681_2 by 3 degrees
- `C3`: Decrease A3 Offset threshold for 3214681_2
- `C4`: Add neighbor relationship between 3253931_1 and 3275187_3
- `C5`: Check test server and transmission issues
- `C6`: Adjust the azimuth of 3253931_1 by 18 degrees
- `C7`: Add neighbor relationship between 3214681_2 and 3275187_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214681_2
- `C9`: Decrease A3 Offset threshold for 3275187_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275187_3
- `C11`: Increase A3 Offset threshold for 3214681_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease transmission power for 3214681_2
- `C14`: Press down the tilt angle  of 3253931_1 by 4 degrees
- `C15`: Adjust the azimuth of 3214681_2 by 16 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214681_2
- `C17`: Press down the tilt angle of 3214681_2 by 3 degrees
- `C18`: Decrease transmission power for 3275187_3
- `C19`: Increase A3 Offset threshold for 3275187_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275187_3
- `C21`: Increase transmission power for 3214681_2
- `C22`: Lift the tilt angle  of 3253931_1 by 4 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.740 | MS1 | 121.4656775313 | 31.1446285030 | 332 | 504990 | -91.38 | 15.24 | 562.96 | 0.03 | 2.99 | 1593 |
| 2024-09-20 22:21:32.300 | MS1 | 121.4656651735 | 31.1446331723 | 332 | 504990 | -85.27 | 13.34 | 596.96 | 0.07 | 2.45 | 1586 |
| 2024-09-20 22:21:33.947 | MS1 | 121.4656639214 | 31.1446330204 | 332 | 504990 | -85.73 | 15.30 | 565.91 | 0.18 | 2.44 | 1590 |
| 2024-09-20 22:21:34.708 | MS1 | 121.4656653210 | 31.1446202773 | 332 | 504990 | -90.89 | 15.93 | 55.42 | 0.16 | 2.55 | 1566 |
| 2024-09-20 22:21:35.129 | MS1 | 121.4656718881 | 31.1446368132 | 332 | 504990 | -91.81 | 13.06 | 98.41 | 0.14 | 2.19 | 1588 |
| 2024-09-20 22:21:36.882 | MS1 | 121.4656605066 | 31.1446212237 | 332 | 504990 | -89.08 | 14.21 | 68.01 | 0.03 | 2.86 | 1594 |
| 2024-09-20 22:21:37.292 | MS1 | 121.4656732965 | 31.1446278139 | 332 | 504990 | -92.58 | 10.54 | 88.46 | 0.04 | 2.81 | 1576 |
| 2024-09-20 22:21:38.669 | MS1 | 121.4656714142 | 31.1446324141 | 332 | 504990 | -93.25 | 11.39 | 97.07 | 0.11 | 2.74 | 1587 |
| 2024-09-20 22:21:39.276 | MS1 | 121.4656719209 | 31.1446196061 | 332 | 504990 | -90.10 | 10.87 | 75.90 | 0.17 | 2.66 | 1569 |
| 2024-09-20 22:21:40.464 | MS1 | 121.4656664374 | 31.1446248477 | 332 | 504990 | -90.89 | 12.62 | 397.54 | 0.05 | 2.50 | 1572 |
| 2024-09-20 22:21:41.265 | MS1 | 121.4656662522 | 31.1446216962 | 332 | 504990 | -89.52 | 8.52 | 448.07 | 0.18 | 2.16 | 1562 |
| 2024-09-20 22:21:42.111 | MS1 | 121.4656641886 | 31.1446192460 | 332 | 504990 | -90.49 | 9.96 | 436.96 | 0.03 | 2.35 | 1594 |

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
| 3214681 | 2 | 121.4714019653 | 31.1449067052 | 251 | 0 | 9 | 28.2 | TDD | 332 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3250184 | 4 | 121.4670567140 | 31.1550848995 | 181 | 4 | 10 | 28.0 | TDD | 670 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3253931 | 1 | 121.4667090062 | 31.1458776642 | 58 | 2 | 3 | 25.4 | TDD | 366 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3275187 | 3 | 121.4735089384 | 31.1554298852 | 230 | 2 | 3 | 37.7 | TDD | 269 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.331 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.355 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.497 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.497 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.141 | NREventA3 | measId:2;ServCellPCI:408;Se... |
| 2024-09-20 22:21:38.381 | NRHandoverAttempt | SourcePCI:408;SourceNR-ARFC... |
| 2024-09-20 22:21:38.415 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.429 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.541 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.541 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253931 | 1 | 10.2813 | 11.5387 | -115.4041 | 16.8278 | 140.9283 | 0.0078 | 0.0176 |
| 2024_09_20 22:00 | 3214681 | 2 | 91.0348 | 94.2284 | -117.3105 | 8.0681 | 95.9478 | 0.0186 | 0.0122 |
| 2024_09_20 22:00 | 3275187 | 3 | 19.5797 | 11.9972 | -114.4250 | 16.7049 | 122.1773 | 0.0048 | 0.0128 |
| 2024_09_20 22:00 | 3250184 | 4 | 18.4970 | 10.0934 | -114.8578 | 15.5383 | 181.4772 | 0.0002 | 0.0173 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412012_C38BC0E1 | 504990 | 332 | -89.8 | 504990 | 269 | -93.9 | 504990 | 366 | -103.2 | 504990 | 670 |
| MR_1774412012_E4D7D84B | 504990 | 332 | -92.2 | 504990 | 269 | -95.2 | 504990 | 366 | -103.0 | 504990 | 670 |
| MR_1774412012_9EDCED14 | 504990 | 332 | -91.3 | 504990 | 269 | -94.4 | 504990 | 366 | -103.3 | 504990 | 670 |
| MR_1774412012_36DAFA9A | 504990 | 332 | -90.0 | 504990 | 269 | -92.7 | 504990 | 366 | -103.8 | 504990 | 670 |
| MR_1774412012_AF561C17 | 504990 | 332 | -90.2 | 504990 | 269 | -93.9 | 504990 | 366 | -103.9 | 504990 | 670 |
| MR_1774412012_2B79A53A | 504990 | 332 | -90.7 | 504990 | 269 | -93.0 | 504990 | 366 | -101.9 | 504990 | 670 |
| MR_1774412012_04DE3C99 | 504990 | 332 | -92.3 | 504990 | 269 | -94.5 | 504990 | 366 | -101.0 | 504990 | 670 |
| MR_1774412012_10219BA4 | 504990 | 332 | -91.4 | 504990 | 269 | -94.0 | 504990 | 366 | -102.7 | 504990 | 670 |

> *... 2개 열 생략 (전체 14열)*

---
