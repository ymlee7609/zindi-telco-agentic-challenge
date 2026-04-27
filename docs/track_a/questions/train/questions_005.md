# Track A 문제 분석 — train[40]~train[49]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[40] ~ train[49] (10개)

## 목차

1. [문제 40: `49795cc9-710...`](#40) — single-answer, 정답: C4
2. [문제 41: `80fa2595-33c...`](#41) — single-answer, 정답: C21
3. [문제 42: `2f94c2a1-35c...`](#42) — single-answer, 정답: C1
4. [문제 43: `630be894-99a...`](#43) — single-answer, 정답: C9
5. [문제 44: `24a7bab5-2c9...`](#44) — multiple-answer, 정답: C1|C17
6. [문제 45: `9e882927-278...`](#45) — single-answer, 정답: C11
7. [문제 46: `01c2d671-d5c...`](#46) — single-answer, 정답: C7
8. [문제 47: `8f3fa224-5f4...`](#47) — single-answer, 정답: C10
9. [문제 48: `c4dadddd-cc1...`](#48) — single-answer, 정답: C1
10. [문제 49: `807626fb-09c...`](#49) — single-answer, 정답: C7

---

### 문제 40: `49795cc9-710...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `49795cc9-7106-4b8f-81c1-90edd227555e` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[40] topology](images/train_0040.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3237699_2 by 50 degrees
- `C2`: Press down the tilt angle  of 3212247_3 by 9 degrees
- `C3`: Add neighbor relationship between 3237699_2 and 3212247_3
- `C4`: Check test server and transmission issues **← 정답**
- `C5`: Adjust the azimuth of 3212247_3 by 26 degrees
- `C6`: Increase A3 Offset threshold for 3237699_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212247_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237699_2
- `C9`: Decrease A3 Offset threshold for 3237699_2
- `C10`: Decrease transmission power for 3212247_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237699_2
- `C12`: Decrease transmission power for 3237699_2
- `C13`: Increase transmission power for 3237699_2
- `C14`: Lift the tilt angle  of 3212247_3 by 9 degrees
- `C15`: Increase transmission power for 3212247_3
- `C16`: Decrease A3 Offset threshold for 3212247_3
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase A3 Offset threshold for 3212247_3
- `C19`: Lift the tilt angle of 3237699_2 by 9 degrees
- `C20`: Add neighbor relationship between 3229081_1 and 3212247_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212247_3
- `C22`: Press down the tilt angle of 3237699_2 by 9 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.911 | MS1 | 121.4656726721 | 31.1446367790 | 153 | 504990 | -87.39 | 13.13 | 377.84 | 0.19 | 2.07 | 1575 |
| 2024-09-20 22:21:32.123 | MS1 | 121.4656675498 | 31.1446182658 | 153 | 504990 | -87.62 | 13.61 | 389.44 | 0.06 | 2.56 | 1588 |
| 2024-09-20 22:21:33.972 | MS1 | 121.4656642288 | 31.1446223817 | 153 | 504990 | -87.01 | 14.39 | 321.35 | 0.18 | 2.45 | 1578 |
| 2024-09-20 22:21:34.339 | MS1 | 121.4656587927 | 31.1446317699 | 153 | 504990 | -85.98 | 14.02 | 42.62 | 0.05 | 2.80 | 311 |
| 2024-09-20 22:21:35.123 | MS1 | 121.4656777154 | 31.1446337042 | 153 | 504990 | -87.66 | 14.78 | 69.14 | 0.14 | 2.40 | 301 |
| 2024-09-20 22:21:36.314 | MS1 | 121.4656642882 | 31.1446315319 | 153 | 504990 | -91.75 | 12.97 | 69.22 | 0.13 | 2.06 | 372 |
| 2024-09-20 22:21:37.291 | MS1 | 121.4656690944 | 31.1446341595 | 153 | 504990 | -91.07 | 7.81 | 68.73 | 0.17 | 2.02 | 475 |
| 2024-09-20 22:21:38.136 | MS1 | 121.4656656452 | 31.1446333924 | 153 | 504990 | -92.27 | 9.53 | 47.09 | 0.17 | 2.62 | 491 |
| 2024-09-20 22:21:39.352 | MS1 | 121.4656748734 | 31.1446213628 | 153 | 504990 | -90.80 | 12.04 | 68.45 | 0.10 | 2.49 | 417 |
| 2024-09-20 22:21:40.751 | MS1 | 121.4656650855 | 31.1446323547 | 153 | 504990 | -89.95 | 12.72 | 490.46 | 0.17 | 2.55 | 1573 |
| 2024-09-20 22:21:41.208 | MS1 | 121.4656668917 | 31.1446225527 | 153 | 504990 | -91.17 | 9.29 | 359.29 | 0.19 | 2.83 | 1590 |
| 2024-09-20 22:21:42.483 | MS1 | 121.4656753224 | 31.1446312781 | 153 | 504990 | -89.03 | 10.79 | 389.24 | 0.10 | 2.27 | 1575 |

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
| 3212247 | 3 | 121.4661848974 | 31.1501494935 | 159 | 6 | 6 | 27.5 | TDD | 995 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3229081 | 1 | 121.4688392679 | 31.1511548282 | 183 | 11 | 4 | 25.6 | TDD | 872 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3229205 | 4 | 121.4716382600 | 31.1486846874 | 162 | 10 | 11 | 49.5 | TDD | 782 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3237699 | 2 | 121.4728665729 | 31.1517107126 | 66 | 7 | 4 | 30.3 | TDD | 153 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.969 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.984 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.088 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.088 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.839 | NREventA3 | measId:2;ServCellPCI:176;Se... |
| 2024-09-20 22:21:38.079 | NRHandoverAttempt | SourcePCI:176;SourceNR-ARFC... |
| 2024-09-20 22:21:38.127 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.137 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.258 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.258 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229081 | 1 | 13.3300 | 7.9548 | -117.0878 | 16.8737 | 176.1829 | 0.0052 | 0.0002 |
| 2024_09_20 22:00 | 3237699 | 2 | 7.2295 | 14.1679 | -116.8767 | 18.8123 | 111.1633 | 0.0109 | 0.0155 |
| 2024_09_20 22:00 | 3212247 | 3 | 17.2260 | 17.3929 | -116.1137 | 15.0633 | 107.4412 | 0.0123 | 0.0041 |
| 2024_09_20 22:00 | 3229205 | 4 | 9.1777 | 12.7628 | -114.0784 | 9.5150 | 113.5511 | 0.0033 | 0.0025 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416602_A85C6979 | 504990 | 153 | -84.5 | 504990 | 995 | -94.2 | 504990 | 872 | -97.9 | 504990 | 782 |
| MR_1774416602_44DAC263 | 504990 | 153 | -87.3 | 504990 | 995 | -93.1 | 504990 | 872 | -97.5 | 504990 | 782 |
| MR_1774416602_84575749 | 504990 | 153 | -87.0 | 504990 | 995 | -95.6 | 504990 | 872 | -96.2 | 504990 | 782 |
| MR_1774416602_FBB9043F | 504990 | 153 | -85.1 | 504990 | 995 | -94.3 | 504990 | 872 | -96.2 | 504990 | 782 |
| MR_1774416602_D9609497 | 504990 | 153 | -84.3 | 504990 | 995 | -95.0 | 504990 | 872 | -97.5 | 504990 | 782 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 41: `80fa2595-33c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `80fa2595-33c3-46ed-85f9-2ae7174def52` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3274398_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[41] topology](images/train_0041.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3274398_2
- `C2`: Add neighbor relationship between 3219072_1 and 3223290_4
- `C3`: Decrease transmission power for 3223290_4
- `C4`: Press down the tilt angle of 3274398_2 by 3 degrees
- `C5`: Add neighbor relationship between 3274398_2 and 3223290_4
- `C6`: Lift the tilt angle  of 3223290_4 by 8 degrees
- `C7`: Increase transmission power for 3223290_4
- `C8`: Lift the tilt angle of 3274398_2 by 3 degrees
- `C9`: Increase A3 Offset threshold for 3223290_4
- `C10`: Adjust the azimuth of 3223290_4 by 50 degrees
- `C11`: Press down the tilt angle  of 3223290_4 by 8 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223290_4
- `C13`: Check test server and transmission issues
- `C14`: Decrease transmission power for 3274398_2
- `C15`: Decrease A3 Offset threshold for 3223290_4
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase A3 Offset threshold for 3274398_2
- `C18`: Adjust the azimuth of 3274398_2 by 28 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223290_4
- `C20`: Decrease A3 Offset threshold for 3274398_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274398_2 **← 정답**
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274398_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.956 | MS1 | 121.4656657764 | 31.1446283717 | 929 | 504990 | -91.50 | 12.29 | 361.16 | 0.16 | 2.35 | 1568 |
| 2024-09-20 22:21:32.994 | MS1 | 121.4656756401 | 31.1446344916 | 929 | 504990 | -87.10 | 15.74 | 347.29 | 0.04 | 2.27 | 1565 |
| 2024-09-20 22:21:33.346 | MS1 | 121.4656587223 | 31.1446292462 | 929 | 504990 | -87.54 | 16.25 | 425.29 | 0.08 | 2.22 | 1567 |
| 2024-09-20 22:21:34.772 | MS1 | 121.4656611450 | 31.1446217873 | 929 | 504990 | -90.51 | 16.95 | 64.60 | 0.66 | 2.47 | 550 |
| 2024-09-20 22:21:35.673 | MS1 | 121.4656642664 | 31.1446241592 | 929 | 504990 | -86.95 | 14.90 | 53.08 | 0.53 | 2.35 | 511 |
| 2024-09-20 22:21:36.170 | MS1 | 121.4656656381 | 31.1446207190 | 929 | 504990 | -87.85 | 17.41 | 58.10 | 0.67 | 2.95 | 669 |
| 2024-09-20 22:21:37.402 | MS1 | 121.4656747191 | 31.1446182627 | 929 | 504990 | -92.91 | 7.12 | 68.01 | 0.62 | 2.29 | 537 |
| 2024-09-20 22:21:38.339 | MS1 | 121.4656692472 | 31.1446251670 | 929 | 504990 | -89.01 | 10.50 | 64.19 | 0.69 | 2.70 | 673 |
| 2024-09-20 22:21:39.842 | MS1 | 121.4656739934 | 31.1446186627 | 929 | 504990 | -89.72 | 12.81 | 103.32 | 0.63 | 2.49 | 545 |
| 2024-09-20 22:21:40.845 | MS1 | 121.4656688454 | 31.1446368777 | 929 | 504990 | -92.09 | 11.72 | 440.93 | 0.12 | 2.22 | 1566 |
| 2024-09-20 22:21:41.499 | MS1 | 121.4656746836 | 31.1446234960 | 929 | 504990 | -93.46 | 11.14 | 423.40 | 0.00 | 2.66 | 1599 |
| 2024-09-20 22:21:42.414 | MS1 | 121.4656682070 | 31.1446337354 | 929 | 504990 | -93.86 | 10.92 | 479.24 | 0.02 | 2.31 | 1597 |

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
| 3219072 | 1 | 121.4745219247 | 31.1476478250 | 191 | 3 | 3 | 49.3 | TDD | 944 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3223290 | 4 | 121.4651749712 | 31.1554179026 | 75 | 7 | 10 | 31.0 | TDD | 407 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3268793 | 3 | 121.4672427155 | 31.1454725918 | 219 | 15 | 4 | 19.9 | TDD | 715 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3274398 | 2 | 121.4705598786 | 31.1494331373 | 193 | 0 | 10 | 31.8 | TDD | 929 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.951 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.973 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.078 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.078 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.831 | NREventA3 | measId:2;ServCellPCI:271;Se... |
| 2024-09-20 22:21:38.071 | NRHandoverAttempt | SourcePCI:271;SourceNR-ARFC... |
| 2024-09-20 22:21:38.117 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.130 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.231 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.231 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219072 | 1 | 19.1810 | 16.7131 | -115.6785 | 6.4063 | 105.3724 | 0.0152 | 0.0147 |
| 2024_09_20 22:00 | 3274398 | 2 | 9.5283 | 9.9696 | -116.4468 | 14.9248 | 185.9911 | 0.0145 | 0.0046 |
| 2024_09_20 22:00 | 3268793 | 3 | 10.0551 | 5.0076 | -114.3005 | 11.6377 | 84.1917 | 0.0068 | 0.0052 |
| 2024_09_20 22:00 | 3223290 | 4 | 8.7186 | 11.0507 | -116.8301 | 9.0847 | 111.6200 | 0.0037 | 0.0093 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415160_AEE2AE8F | 504990 | 929 | -91.2 | 504990 | 407 | -98.6 | 504990 | 944 | -99.6 | 504990 | 715 |
| MR_1774415160_478868F2 | 504990 | 929 | -89.2 | 504990 | 407 | -98.6 | 504990 | 944 | -100.1 | 504990 | 715 |
| MR_1774415160_1C4F2348 | 504990 | 929 | -88.6 | 504990 | 407 | -101.1 | 504990 | 944 | -98.7 | 504990 | 715 |
| MR_1774415160_0A6AA5AA | 504990 | 929 | -91.5 | 504990 | 407 | -98.6 | 504990 | 944 | -99.9 | 504990 | 715 |
| MR_1774415160_5E27D1D7 | 504990 | 929 | -88.5 | 504990 | 407 | -100.4 | 504990 | 944 | -100.5 | 504990 | 715 |
| MR_1774415160_5D217C45 | 504990 | 929 | -91.3 | 504990 | 407 | -98.8 | 504990 | 944 | -100.2 | 504990 | 715 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 42: `2f94c2a1-35c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2f94c2a1-35cb-47e1-b58e-d1bc591f9003` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Add neighbor relationship between 3265543_1 and 3276948_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[42] topology](images/train_0042.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3265543_1 and 3276948_4 **← 정답**
- `C2`: Press down the tilt angle of 3265543_1 by 10 degrees
- `C3`: Lift the tilt angle  of 3276948_4 by 4 degrees
- `C4`: Increase transmission power for 3265543_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Check test server and transmission issues
- `C7`: Press down the tilt angle  of 3276948_4 by 4 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265543_1
- `C9`: Add neighbor relationship between 3253658_3 and 3276948_4
- `C10`: Increase A3 Offset threshold for 3276948_4
- `C11`: Increase A3 Offset threshold for 3265543_1
- `C12`: Increase transmission power for 3276948_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276948_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265543_1
- `C15`: Lift the tilt angle of 3265543_1 by 10 degrees
- `C16`: Decrease A3 Offset threshold for 3265543_1
- `C17`: Decrease A3 Offset threshold for 3276948_4
- `C18`: Adjust the azimuth of 3265543_1 by 50 degrees
- `C19`: Adjust the azimuth of 3276948_4 by 34 degrees
- `C20`: Decrease transmission power for 3265543_1
- `C21`: Decrease transmission power for 3276948_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276948_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.153 | MS1 | 121.4656629581 | 31.1446235218 | 896 | 504990 | -81.99 | 12.63 | 596.96 | 0.03 | 2.54 | 1591 |
| 2024-09-20 22:21:32.317 | MS1 | 121.4656672681 | 31.1446233980 | 896 | 504990 | -78.73 | 14.79 | 546.97 | 0.15 | 2.47 | 1581 |
| 2024-09-20 22:21:33.409 | MS1 | 121.4656694191 | 31.1446323024 | 896 | 504990 | -77.14 | 14.71 | 445.09 | 0.12 | 2.10 | 1561 |
| 2024-09-20 22:21:34.899 | MS1 | 121.4656714797 | 31.1446197116 | 896 | 504990 | -91.22 | -3.34 | 33.97 | 0.04 | 1.39 | 1577 |
| 2024-09-20 22:21:35.641 | MS1 | 121.4656659268 | 31.1446290063 | 896 | 504990 | -85.81 | -0.23 | 49.77 | 0.09 | 1.48 | 1564 |
| 2024-09-20 22:21:36.382 | MS1 | 121.4656715891 | 31.1446290437 | 896 | 504990 | -85.02 | -1.07 | 65.44 | 0.15 | 1.10 | 1574 |
| 2024-09-20 22:21:37.808 | MS1 | 121.4656581411 | 31.1446352712 | 896 | 504990 | -86.42 | -2.96 | 32.66 | 0.03 | 1.50 | 1596 |
| 2024-09-20 22:21:38.639 | MS1 | 121.4656589969 | 31.1446250988 | 896 | 504990 | -78.86 | 12.11 | 601.27 | 0.01 | 1.14 | 1567 |
| 2024-09-20 22:21:39.139 | MS1 | 121.4656766410 | 31.1446315763 | 896 | 504990 | -80.24 | 15.59 | 383.91 | 0.01 | 1.23 | 1590 |
| 2024-09-20 22:21:40.541 | MS1 | 121.4656640191 | 31.1446374017 | 896 | 504990 | -81.83 | 13.77 | 309.27 | 0.10 | 2.95 | 1575 |
| 2024-09-20 22:21:41.725 | MS1 | 121.4656593170 | 31.1446313485 | 896 | 504990 | -84.49 | 12.34 | 335.03 | 0.14 | 2.36 | 1578 |
| 2024-09-20 22:21:42.354 | MS1 | 121.4656597076 | 31.1446291164 | 896 | 504990 | -78.27 | 16.62 | 385.14 | 0.05 | 2.62 | 1579 |

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
| 3253658 | 3 | 121.4649491757 | 31.1538592024 | 148 | 3 | 10 | 40.7 | TDD | 354 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3253900 | 2 | 121.4726121648 | 31.1474449614 | 359 | 2 | 5 | 30.9 | TDD | 449 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3265543 | 1 | 121.4707858313 | 31.1504923195 | 122 | 13 | 2 | 45.7 | TDD | 896 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3276948 | 4 | 121.4666715708 | 31.1502419877 | 223 | 3 | 9 | 16.5 | TDD | 205 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.567 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.679 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.679 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.380 | NREventA3 | measId:2;ServCellPCI:315;Se... |
| 2024-09-20 22:21:36.380 | NREventA3 | measId:2;ServCellPCI:315;Se... |
| 2024-09-20 22:21:37.380 | NREventA3 | measId:2;ServCellPCI:315;Se... |
| 2024-09-20 22:21:39.880 | NRRRCReestablishAttempt | PCI:315 |
| 2024-09-20 22:21:39.897 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.912 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:40.038 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.038 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265543 | 1 | 11.6022 | 9.4312 | -115.8144 | 18.5398 | 104.4067 | 0.0006 | 0.1176 |
| 2024_09_20 22:00 | 3253900 | 2 | 7.1083 | 14.3344 | -117.9726 | 9.1688 | 140.9522 | 0.0123 | 0.0021 |
| 2024_09_20 22:00 | 3253658 | 3 | 5.4683 | 12.7075 | -115.7423 | 11.6903 | 164.7840 | 0.0016 | 0.0108 |
| 2024_09_20 22:00 | 3276948 | 4 | 17.9014 | 18.1174 | -114.9269 | 11.7098 | 129.9622 | 0.0055 | 0.0101 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412663_1E2DA4D8 | 504990 | 896 | -90.0 | 504990 | 205 | -85.5 | 504990 | 354 | -92.8 | 504990 | 449 |
| MR_1774412663_A0E91964 | 504990 | 896 | -89.4 | 504990 | 205 | -86.2 | 504990 | 354 | -90.6 | 504990 | 449 |
| MR_1774412663_92F42C5F | 504990 | 896 | -92.5 | 504990 | 205 | -86.7 | 504990 | 354 | -90.7 | 504990 | 449 |
| MR_1774412663_2EE6670C | 504990 | 896 | -91.0 | 504990 | 205 | -85.6 | 504990 | 354 | -90.8 | 504990 | 449 |
| MR_1774412663_DDDE3153 | 504990 | 896 | -89.4 | 504990 | 205 | -86.1 | 504990 | 354 | -93.2 | 504990 | 449 |
| MR_1774412663_ECE977CA | 504990 | 205 | -85.2 | 504990 | 896 | -90.5 | 504990 | 354 | -90.1 | 504990 | 449 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 43: `630be894-99a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `630be894-99a3-46fb-a9bb-875f09496ef7` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Lift the tilt angle  of 3225895_2 by 6 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[43] topology](images/train_0043.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3251808_3
- `C2`: Decrease A3 Offset threshold for 3232470_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251808_3
- `C4`: Adjust the azimuth of 3225895_2 by 50 degrees
- `C5`: Add neighbor relationship between 3232470_4 and 3251808_3
- `C6`: Increase transmission power for 3251808_3
- `C7`: Increase A3 Offset threshold for 3251808_3
- `C8`: Press down the tilt angle of 3232470_4 by 3 degrees
- `C9`: Lift the tilt angle  of 3225895_2 by 6 degrees **← 정답**
- `C10`: Lift the tilt angle of 3232470_4 by 3 degrees
- `C11`: Add neighbor relationship between 3225895_2 and 3251808_3
- `C12`: Decrease transmission power for 3251808_3
- `C13`: Decrease transmission power for 3232470_4
- `C14`: Increase A3 Offset threshold for 3232470_4
- `C15`: Adjust the azimuth of 3232470_4 by 9 degrees
- `C16`: Increase transmission power for 3232470_4
- `C17`: Check test server and transmission issues
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232470_4
- `C19`: Press down the tilt angle  of 3225895_2 by 6 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232470_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251808_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.852 | MS1 | 121.4656663039 | 31.1446328703 | 566 | 504990 | -86.44 | 13.62 | 408.24 | 0.18 | 2.39 | 1573 |
| 2024-09-20 22:21:32.675 | MS1 | 121.4656639715 | 31.1446263685 | 566 | 504990 | -85.09 | 16.57 | 509.35 | 0.11 | 2.79 | 1568 |
| 2024-09-20 22:21:33.908 | MS1 | 121.4656585158 | 31.1446322195 | 566 | 504990 | -90.11 | 17.53 | 447.38 | 0.15 | 2.87 | 1562 |
| 2024-09-20 22:21:34.866 | MS1 | 121.4656610090 | 31.1446332642 | 566 | 504990 | -87.46 | 14.52 | 99.70 | 0.04 | 2.53 | 1596 |
| 2024-09-20 22:21:35.490 | MS1 | 121.4656767073 | 31.1446357158 | 566 | 504990 | -85.88 | 15.05 | 56.30 | 0.12 | 2.80 | 1588 |
| 2024-09-20 22:21:36.867 | MS1 | 121.4656700729 | 31.1446232231 | 566 | 504990 | -86.70 | 17.34 | 80.06 | 0.14 | 3.00 | 1571 |
| 2024-09-20 22:21:37.204 | MS1 | 121.4656637548 | 31.1446214802 | 566 | 504990 | -89.03 | 9.61 | 53.11 | 0.08 | 2.64 | 1589 |
| 2024-09-20 22:21:38.817 | MS1 | 121.4656680866 | 31.1446206409 | 566 | 504990 | -90.85 | 11.51 | 100.33 | 0.04 | 2.32 | 1591 |
| 2024-09-20 22:21:39.972 | MS1 | 121.4656616286 | 31.1446284443 | 566 | 504990 | -92.15 | 9.96 | 65.64 | 0.03 | 2.87 | 1576 |
| 2024-09-20 22:21:40.432 | MS1 | 121.4656695077 | 31.1446323526 | 566 | 504990 | -92.68 | 9.54 | 557.99 | 0.04 | 2.57 | 1576 |
| 2024-09-20 22:21:41.237 | MS1 | 121.4656626433 | 31.1446210125 | 566 | 504990 | -93.39 | 11.79 | 414.00 | 0.10 | 2.86 | 1587 |
| 2024-09-20 22:21:42.945 | MS1 | 121.4656593579 | 31.1446352153 | 566 | 504990 | -89.65 | 11.39 | 541.98 | 0.19 | 2.82 | 1583 |

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
| 3225895 | 2 | 121.4673555876 | 31.1440259483 | 83 | 2 | 10 | 49.5 | TDD | 403 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3232470 | 4 | 121.4731434066 | 31.1536159089 | 206 | 1 | 9 | 33.8 | TDD | 566 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3247910 | 1 | 121.4740080333 | 31.1512846318 | 16 | 2 | 1 | 46.3 | TDD | 442 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3251808 | 3 | 121.4751880108 | 31.1507490730 | 91 | 4 | 5 | 45.9 | TDD | 141 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.602 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.602 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.306 | NREventA3 | measId:2;ServCellPCI:65;Ser... |
| 2024-09-20 22:21:38.546 | NRHandoverAttempt | SourcePCI:65;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.582 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.594 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.697 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.697 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247910 | 1 | 19.4519 | 5.1106 | -117.0091 | 13.3252 | 160.4897 | 0.0080 | 0.0008 |
| 2024_09_20 22:00 | 3225895 | 2 | 8.2375 | 11.6730 | -117.6879 | 10.2519 | 92.2272 | 0.0066 | 0.0065 |
| 2024_09_20 22:00 | 3251808 | 3 | 12.0312 | 18.3582 | -117.2003 | 13.0608 | 80.2927 | 0.0016 | 0.0088 |
| 2024_09_20 22:00 | 3232470 | 4 | 81.0397 | 84.0849 | -116.2149 | 10.7757 | 193.8538 | 0.0105 | 0.0062 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413667_84A1AE55 | 504990 | 566 | -86.7 | 504990 | 141 | -88.4 | 504990 | 403 | -99.1 | 504990 | 442 |
| MR_1774413667_67F43A0A | 504990 | 566 | -86.4 | 504990 | 141 | -91.2 | 504990 | 403 | -98.0 | 504990 | 442 |
| MR_1774413667_9ACFDB31 | 504990 | 566 | -88.3 | 504990 | 141 | -90.1 | 504990 | 403 | -99.2 | 504990 | 442 |
| MR_1774413667_DAC70E33 | 504990 | 566 | -89.3 | 504990 | 141 | -88.9 | 504990 | 403 | -100.2 | 504990 | 442 |
| MR_1774413667_7E8890E1 | 504990 | 566 | -89.4 | 504990 | 141 | -89.8 | 504990 | 403 | -101.5 | 504990 | 442 |
| MR_1774413667_5AA24B0B | 504990 | 566 | -86.9 | 504990 | 141 | -88.5 | 504990 | 403 | -98.1 | 504990 | 442 |
| MR_1774413667_081B2B9F | 504990 | 566 | -88.6 | 504990 | 141 | -91.6 | 504990 | 403 | -98.9 | 504990 | 442 |
| MR_1774413667_B7956146 | 504990 | 566 | -88.2 | 504990 | 141 | -88.9 | 504990 | 403 | -101.7 | 504990 | 442 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 44: `24a7bab5-2c9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `24a7bab5-2c9f-4aa7-9773-1be52b3a0b58` |
| Tag | **multiple-answer** |
| 정답 | **C1|C17** |
| C1 의미 | Adjust the azimuth of 3274618_4 by 50 degrees |
| C17 의미 | Increase transmission power for 3274618_4 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[44] topology](images/train_0044.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3274618_4 by 50 degrees **← 정답**
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248115_2
- `C3`: Increase A3 Offset threshold for 3248115_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248115_2
- `C5`: Decrease transmission power for 3248115_2
- `C6`: Check test server and transmission issues
- `C7`: Add neighbor relationship between 3253348_3 and 3248115_2
- `C8`: Press down the tilt angle of 3274618_4 by 8 degrees
- `C9`: Add neighbor relationship between 3274618_4 and 3248115_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274618_4
- `C11`: Lift the tilt angle of 3274618_4 by 8 degrees
- `C12`: Adjust the azimuth of 3248115_2 by 36 degrees
- `C13`: Decrease A3 Offset threshold for 3274618_4
- `C14`: Press down the tilt angle  of 3248115_2 by 5 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274618_4
- `C16`: Increase transmission power for 3248115_2
- `C17`: Increase transmission power for 3274618_4 **← 정답**
- `C18`: Increase A3 Offset threshold for 3274618_4
- `C19`: Lift the tilt angle  of 3248115_2 by 5 degrees
- `C20`: Decrease transmission power for 3274618_4
- `C21`: Decrease A3 Offset threshold for 3248115_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.703 | MS1 | 121.4656711760 | 31.1446353852 | 606 | 504990 | -90.51 | 15.07 | 459.47 | 0.02 | 2.05 | 1560 |
| 2024-09-20 22:21:32.612 | MS1 | 121.4656666188 | 31.1446283117 | 606 | 504990 | -92.52 | 15.58 | 345.74 | 0.06 | 2.96 | 1576 |
| 2024-09-20 22:21:33.262 | MS1 | 121.4656667317 | 31.1446228838 | 606 | 504990 | -86.56 | 14.71 | 466.03 | 0.18 | 2.96 | 1578 |
| 2024-09-20 22:21:34.434 | MS1 | 121.4656724080 | 31.1446343118 | 606 | 504990 | -107.94 | -1.94 | 73.25 | 0.07 | 1.50 | 1599 |
| 2024-09-20 22:21:35.965 | MS1 | 121.4656732452 | 31.1446246478 | 606 | 504990 | -100.78 | 1.30 | 28.32 | 0.05 | 1.28 | 1570 |
| 2024-09-20 22:21:36.486 | MS1 | 121.4656644413 | 31.1446335151 | 606 | 504990 | -105.15 | 0.65 | 62.13 | 0.13 | 1.16 | 1569 |
| 2024-09-20 22:21:37.682 | MS1 | 121.4656650379 | 31.1446308988 | 606 | 504990 | -103.30 | 1.42 | 69.95 | 0.14 | 1.08 | 1595 |
| 2024-09-20 22:21:38.612 | MS1 | 121.4656604053 | 31.1446346204 | 606 | 504990 | -106.16 | -0.57 | 56.48 | 0.20 | 1.03 | 1590 |
| 2024-09-20 22:21:39.595 | MS1 | 121.4656711624 | 31.1446223530 | 606 | 504990 | -109.81 | -1.28 | 55.23 | 0.05 | 1.41 | 1598 |
| 2024-09-20 22:21:40.657 | MS1 | 121.4656613556 | 31.1446295993 | 606 | 504990 | -85.15 | 14.61 | 473.84 | 0.16 | 2.14 | 1562 |
| 2024-09-20 22:21:41.616 | MS1 | 121.4656620553 | 31.1446198800 | 606 | 504990 | -85.76 | 16.43 | 511.35 | 0.01 | 2.37 | 1581 |
| 2024-09-20 22:21:42.848 | MS1 | 121.4656748297 | 31.1446250623 | 606 | 504990 | -85.82 | 15.90 | 569.03 | 0.05 | 2.40 | 1568 |

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
| 3248115 | 2 | 121.4641896817 | 31.1545261835 | 137 | 4 | 10 | 25.2 | TDD | 739 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3253348 | 3 | 121.4640066604 | 31.1447124388 | 255 | 10 | 9 | 26.4 | TDD | 846 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3261132 | 1 | 121.4725348594 | 31.1495584208 | 164 | 1 | 6 | 27.0 | TDD | 497 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3274618 | 4 | 121.4743600862 | 31.1471546400 | 325 | 5 | 5 | 49.7 | TDD | 606 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.991 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.010 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.140 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.140 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.314 | NREventA2 | measId:1;ServCellPCI:51;Ser... |
| 2024-09-20 22:21:34.460 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261132 | 1 | 15.6947 | 18.3186 | -115.2370 | 19.1639 | 137.3771 | 0.0089 | 0.0036 |
| 2024_09_20 22:00 | 3248115 | 2 | 6.0342 | 9.5355 | -117.7777 | 18.6165 | 121.9696 | 0.0074 | 0.0021 |
| 2024_09_20 22:00 | 3253348 | 3 | 16.6709 | 9.1233 | -116.8935 | 16.0643 | 129.7401 | 0.0140 | 0.0133 |
| 2024_09_20 22:00 | 3274618 | 4 | 15.3549 | 11.8107 | -117.5960 | 19.0070 | 131.0186 | 0.1614 | 0.0069 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415061_A159F303 | 504990 | 606 | -106.3 | 504990 | 739 | -113.8 | 504990 | 846 | -122.3 | 504990 | 497 |
| MR_1774415061_D666BD65 | 504990 | 606 | -108.6 | 504990 | 739 | -114.6 | 504990 | 846 | -122.4 | 504990 | 497 |
| MR_1774415061_92F34754 | 504990 | 606 | -109.2 | 504990 | 739 | -114.2 | 504990 | 846 | -122.4 | 504990 | 497 |
| MR_1774415061_0E12DCC8 | 504990 | 606 | -108.9 | 504990 | 739 | -114.5 | 504990 | 846 | -122.5 | 504990 | 497 |
| MR_1774415061_C57558C1 | 504990 | 606 | -106.9 | 504990 | 739 | -116.7 | 504990 | 846 | -121.9 | 504990 | 497 |
| MR_1774415061_B2387B51 | 504990 | 606 | -108.3 | 504990 | 739 | -115.6 | 504990 | 846 | -120.3 | 504990 | 497 |
| MR_1774415061_9E5E7E0E | 504990 | 606 | -109.0 | 504990 | 739 | -115.8 | 504990 | 846 | -122.0 | 504990 | 497 |
| MR_1774415061_88EA4F5C | 504990 | 606 | -109.2 | 504990 | 739 | -113.7 | 504990 | 846 | -121.0 | 504990 | 497 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 45: `9e882927-278...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9e882927-2781-4eb4-8bd9-2de9a6f555d5` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Lift the tilt angle  of 3278288_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[45] topology](images/train_0045.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242978_3
- `C2`: Decrease transmission power for 3242978_3
- `C3`: Increase transmission power for 3245901_4
- `C4`: Check test server and transmission issues
- `C5`: Increase A3 Offset threshold for 3245901_4
- `C6`: Press down the tilt angle of 3242978_3 by 6 degrees
- `C7`: Adjust the azimuth of 3242978_3 by 26 degrees
- `C8`: Decrease A3 Offset threshold for 3245901_4
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease A3 Offset threshold for 3242978_3
- `C11`: Lift the tilt angle  of 3278288_1 by 10 degrees **← 정답**
- `C12`: Increase transmission power for 3242978_3
- `C13`: Add neighbor relationship between 3242978_3 and 3245901_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242978_3
- `C15`: Lift the tilt angle of 3242978_3 by 6 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245901_4
- `C17`: Add neighbor relationship between 3278288_1 and 3245901_4
- `C18`: Decrease transmission power for 3245901_4
- `C19`: Adjust the azimuth of 3278288_1 by 50 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245901_4
- `C21`: Press down the tilt angle  of 3278288_1 by 10 degrees
- `C22`: Increase A3 Offset threshold for 3242978_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.171 | MS1 | 121.4656634863 | 31.1446227028 | 950 | 504990 | -89.10 | 13.53 | 568.37 | 0.03 | 2.59 | 1586 |
| 2024-09-20 22:21:32.476 | MS1 | 121.4656660750 | 31.1446240905 | 950 | 504990 | -89.72 | 16.90 | 485.45 | 0.12 | 2.85 | 1582 |
| 2024-09-20 22:21:33.646 | MS1 | 121.4656640023 | 31.1446307831 | 950 | 504990 | -85.92 | 17.09 | 484.39 | 0.14 | 2.41 | 1570 |
| 2024-09-20 22:21:34.202 | MS1 | 121.4656687686 | 31.1446218214 | 950 | 504990 | -91.70 | 14.57 | 82.43 | 0.20 | 2.29 | 1572 |
| 2024-09-20 22:21:35.677 | MS1 | 121.4656758408 | 31.1446259209 | 950 | 504990 | -86.67 | 14.38 | 51.50 | 0.08 | 2.36 | 1579 |
| 2024-09-20 22:21:36.939 | MS1 | 121.4656747731 | 31.1446326458 | 950 | 504990 | -90.50 | 12.83 | 98.02 | 0.01 | 2.53 | 1574 |
| 2024-09-20 22:21:37.573 | MS1 | 121.4656730891 | 31.1446330005 | 950 | 504990 | -92.68 | 12.86 | 85.50 | 0.19 | 2.52 | 1571 |
| 2024-09-20 22:21:38.121 | MS1 | 121.4656612178 | 31.1446322701 | 950 | 504990 | -90.28 | 11.91 | 105.59 | 0.02 | 2.95 | 1572 |
| 2024-09-20 22:21:39.863 | MS1 | 121.4656704424 | 31.1446226843 | 950 | 504990 | -89.26 | 12.97 | 68.00 | 0.09 | 2.87 | 1572 |
| 2024-09-20 22:21:40.409 | MS1 | 121.4656660162 | 31.1446375162 | 950 | 504990 | -89.43 | 7.93 | 382.70 | 0.03 | 2.33 | 1563 |
| 2024-09-20 22:21:41.367 | MS1 | 121.4656721857 | 31.1446205179 | 950 | 504990 | -89.33 | 11.40 | 484.99 | 0.11 | 2.77 | 1562 |
| 2024-09-20 22:21:42.840 | MS1 | 121.4656760212 | 31.1446228364 | 950 | 504990 | -91.20 | 10.00 | 396.19 | 0.11 | 2.54 | 1567 |

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
| 3242978 | 3 | 121.4642840354 | 31.1488332061 | 190 | 2 | 5 | 32.8 | TDD | 950 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3245901 | 4 | 121.4699742044 | 31.1472325240 | 3 | 5 | 0 | 46.5 | TDD | 271 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3255811 | 2 | 121.4652235823 | 31.1518267252 | 125 | 14 | 7 | 33.1 | TDD | 252 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3278288 | 1 | 121.4757961430 | 31.1552707427 | 47 | 9 | 1 | 25.7 | TDD | 418 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.120 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.141 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.269 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.269 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.982 | NREventA3 | measId:2;ServCellPCI:5;Serv... |
| 2024-09-20 22:21:38.222 | NRHandoverAttempt | SourcePCI:5;SourceNR-ARFCN:... |
| 2024-09-20 22:21:38.266 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.280 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.385 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.385 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278288 | 1 | 11.2614 | 7.6139 | -114.8431 | 7.7968 | 96.2029 | 0.0180 | 0.0045 |
| 2024_09_20 22:00 | 3255811 | 2 | 12.2155 | 10.2512 | -115.4157 | 13.3436 | 193.0999 | 0.0015 | 0.0111 |
| 2024_09_20 22:00 | 3242978 | 3 | 93.4413 | 91.1686 | -114.5967 | 5.7923 | 166.6621 | 0.0115 | 0.0140 |
| 2024_09_20 22:00 | 3245901 | 4 | 17.8744 | 14.2685 | -116.8079 | 19.8449 | 162.8615 | 0.0014 | 0.0074 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413655_A9736C99 | 504990 | 950 | -92.1 | 504990 | 271 | -97.6 | 504990 | 418 | -105.1 | 504990 | 252 |
| MR_1774413655_D5136A7D | 504990 | 950 | -90.1 | 504990 | 271 | -96.8 | 504990 | 418 | -103.2 | 504990 | 252 |
| MR_1774413655_FE27A903 | 504990 | 950 | -90.0 | 504990 | 271 | -96.7 | 504990 | 418 | -105.0 | 504990 | 252 |
| MR_1774413655_E8F33A4E | 504990 | 950 | -93.6 | 504990 | 271 | -96.5 | 504990 | 418 | -105.8 | 504990 | 252 |
| MR_1774413655_F56F3BBC | 504990 | 950 | -91.3 | 504990 | 271 | -97.4 | 504990 | 418 | -104.6 | 504990 | 252 |
| MR_1774413655_4B96DCAB | 504990 | 950 | -89.9 | 504990 | 271 | -97.3 | 504990 | 418 | -105.1 | 504990 | 252 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 46: `01c2d671-d5c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `01c2d671-d5c6-40a1-9373-7d4ad0ee550d` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease A3 Offset threshold for 3273806_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[46] topology](images/train_0046.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3273806_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223528_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273806_3
- `C5`: Add neighbor relationship between 3273806_3 and 3223528_1
- `C6`: Lift the tilt angle of 3273806_3 by 10 degrees
- `C7`: Decrease A3 Offset threshold for 3273806_3 **← 정답**
- `C8`: Decrease transmission power for 3223528_1
- `C9`: Increase A3 Offset threshold for 3223528_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223528_1
- `C11`: Increase transmission power for 3273806_3
- `C12`: Lift the tilt angle  of 3223528_1 by 7 degrees
- `C13`: Check test server and transmission issues
- `C14`: Add neighbor relationship between 3235087_2 and 3223528_1
- `C15`: Increase transmission power for 3223528_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273806_3
- `C17`: Press down the tilt angle of 3273806_3 by 10 degrees
- `C18`: Adjust the azimuth of 3223528_1 by 50 degrees
- `C19`: Press down the tilt angle  of 3223528_1 by 7 degrees
- `C20`: Increase A3 Offset threshold for 3273806_3
- `C21`: Decrease A3 Offset threshold for 3223528_1
- `C22`: Adjust the azimuth of 3273806_3 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.300 | MS1 | 121.4656611530 | 31.1446204927 | 814 | 504990 | -82.68 | 15.73 | 370.87 | 0.07 | 2.65 | 1564 |
| 2024-09-20 22:21:32.259 | MS1 | 121.4656776455 | 31.1446318491 | 814 | 504990 | -76.22 | 13.91 | 384.50 | 0.06 | 2.90 | 1579 |
| 2024-09-20 22:21:33.807 | MS1 | 121.4656777248 | 31.1446234728 | 814 | 504990 | -84.17 | 13.14 | 489.55 | 0.08 | 2.31 | 1587 |
| 2024-09-20 22:21:34.366 | MS1 | 121.4656772644 | 31.1446353170 | 814 | 504990 | -84.32 | -0.35 | 42.88 | 0.14 | 1.06 | 1582 |
| 2024-09-20 22:21:35.561 | MS1 | 121.4656767878 | 31.1446365589 | 814 | 504990 | -90.63 | -2.44 | 45.21 | 0.06 | 1.36 | 1598 |
| 2024-09-20 22:21:36.737 | MS1 | 121.4656690199 | 31.1446255342 | 814 | 504990 | -89.27 | -0.17 | 52.26 | 0.10 | 1.41 | 1567 |
| 2024-09-20 22:21:37.527 | MS1 | 121.4656694665 | 31.1446313250 | 814 | 504990 | -87.29 | -0.68 | 57.42 | 0.17 | 1.31 | 1570 |
| 2024-09-20 22:21:38.251 | MS1 | 121.4656735703 | 31.1446317485 | 814 | 504990 | -88.66 | -1.92 | 47.14 | 0.15 | 1.42 | 1577 |
| 2024-09-20 22:21:39.777 | MS1 | 121.4656656081 | 31.1446313375 | 473 | 504990 | -84.82 | 16.68 | 164.76 | 0.07 | 1.26 | 1594 |
| 2024-09-20 22:21:40.449 | MS1 | 121.4656622477 | 31.1446340233 | 473 | 504990 | -79.27 | 16.57 | 358.36 | 0.20 | 2.05 | 1566 |
| 2024-09-20 22:21:41.254 | MS1 | 121.4656723766 | 31.1446223420 | 473 | 504990 | -80.03 | 14.41 | 403.57 | 0.03 | 2.31 | 1570 |
| 2024-09-20 22:21:42.875 | MS1 | 121.4656625403 | 31.1446192442 | 473 | 504990 | -82.84 | 16.77 | 520.98 | 0.11 | 2.50 | 1571 |

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
| 3223528 | 1 | 121.4707357353 | 31.1468479360 | 14 | 4 | 2 | 28.3 | TDD | 473 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3235087 | 2 | 121.4681303104 | 31.1528721134 | 43 | 5 | 3 | 20.4 | TDD | 852 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3258368 | 4 | 121.4641713156 | 31.1532831246 | 20 | 1 | 0 | 21.7 | TDD | 529 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3273806 | 3 | 121.4709992374 | 31.1488130907 | 24 | 15 | 3 | 45.1 | TDD | 814 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.927 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.949 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.076 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.076 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.728 | NREventA3 | measId:2;ServCellPCI:416;Se... |
| 2024-09-20 22:21:37.968 | NRHandoverAttempt | SourcePCI:416;SourceNR-ARFC... |
| 2024-09-20 22:21:38.015 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.029 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.170 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.170 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223528 | 1 | 10.5439 | 7.9759 | -115.1696 | 7.0064 | 178.7079 | 0.0086 | 0.0128 |
| 2024_09_20 22:00 | 3235087 | 2 | 5.6347 | 7.9331 | -117.2422 | 10.2390 | 115.5741 | 0.0187 | 0.0169 |
| 2024_09_20 22:00 | 3273806 | 3 | 10.8084 | 16.5896 | -115.2678 | 17.3558 | 154.2207 | 0.0171 | 0.1202 |
| 2024_09_20 22:00 | 3258368 | 4 | 12.6805 | 6.7198 | -117.4316 | 7.5389 | 167.1818 | 0.0090 | 0.0136 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412080_F309C419 | 504990 | 473 | -76.8 | 504990 | 814 | -85.8 | 504990 | 852 | -81.2 | 504990 | 529 |
| MR_1774412080_5E8A942C | 504990 | 814 | -83.5 | 504990 | 473 | -77.0 | 504990 | 852 | -79.1 | 504990 | 529 |
| MR_1774412080_90F0E783 | 504990 | 814 | -83.5 | 504990 | 473 | -77.0 | 504990 | 852 | -79.0 | 504990 | 529 |
| MR_1774412080_D27BE6FC | 504990 | 814 | -86.1 | 504990 | 473 | -78.9 | 504990 | 852 | -78.5 | 504990 | 529 |
| MR_1774412080_FCEA9F29 | 504990 | 473 | -76.6 | 504990 | 814 | -86.0 | 504990 | 852 | -80.6 | 504990 | 529 |
| MR_1774412080_A123817C | 504990 | 814 | -86.3 | 504990 | 473 | -80.2 | 504990 | 852 | -78.0 | 504990 | 529 |
| MR_1774412080_947D3C4E | 504990 | 814 | -84.4 | 504990 | 473 | -78.0 | 504990 | 852 | -79.6 | 504990 | 529 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 47: `8f3fa224-5f4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8f3fa224-5f4c-4c72-938b-a20d84ec60f4` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Add neighbor relationship between 3229881_2 and 3266662_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[47] topology](images/train_0047.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3229881_2
- `C2`: Decrease transmission power for 3229881_2
- `C3`: Press down the tilt angle  of 3266662_3 by 3 degrees
- `C4`: Lift the tilt angle of 3229881_2 by 7 degrees
- `C5`: Increase transmission power for 3266662_3
- `C6`: Increase A3 Offset threshold for 3266662_3
- `C7`: Press down the tilt angle of 3229881_2 by 7 degrees
- `C8`: Adjust the azimuth of 3266662_3 by 45 degrees
- `C9`: Decrease transmission power for 3266662_3
- `C10`: Add neighbor relationship between 3229881_2 and 3266662_3 **← 정답**
- `C11`: Adjust the azimuth of 3229881_2 by 1 degrees
- `C12`: Decrease A3 Offset threshold for 3229881_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266662_3
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease A3 Offset threshold for 3266662_3
- `C16`: Add neighbor relationship between 3239824_4 and 3266662_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266662_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229881_2
- `C19`: Check test server and transmission issues
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229881_2
- `C21`: Increase A3 Offset threshold for 3229881_2
- `C22`: Lift the tilt angle  of 3266662_3 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.167 | MS1 | 121.4656619453 | 31.1446219490 | 785 | 504990 | -83.33 | 15.61 | 524.04 | 0.01 | 2.05 | 1578 |
| 2024-09-20 22:21:32.200 | MS1 | 121.4656683200 | 31.1446316279 | 785 | 504990 | -75.13 | 15.39 | 332.74 | 0.12 | 2.95 | 1570 |
| 2024-09-20 22:21:33.578 | MS1 | 121.4656764238 | 31.1446232325 | 785 | 504990 | -81.97 | 12.91 | 543.86 | 0.08 | 2.65 | 1569 |
| 2024-09-20 22:21:34.198 | MS1 | 121.4656681492 | 31.1446356921 | 785 | 504990 | -90.19 | -2.47 | 28.70 | 0.16 | 1.07 | 1592 |
| 2024-09-20 22:21:35.930 | MS1 | 121.4656669031 | 31.1446309920 | 785 | 504990 | -86.65 | -1.57 | 49.10 | 0.06 | 1.40 | 1597 |
| 2024-09-20 22:21:36.518 | MS1 | 121.4656766217 | 31.1446296278 | 785 | 504990 | -93.41 | -3.57 | 50.70 | 0.09 | 1.48 | 1561 |
| 2024-09-20 22:21:37.582 | MS1 | 121.4656625776 | 31.1446244385 | 785 | 504990 | -91.24 | -2.74 | 28.20 | 0.20 | 1.46 | 1600 |
| 2024-09-20 22:21:38.869 | MS1 | 121.4656704478 | 31.1446258788 | 785 | 504990 | -79.59 | 14.51 | 302.09 | 0.09 | 1.18 | 1598 |
| 2024-09-20 22:21:39.306 | MS1 | 121.4656670287 | 31.1446352969 | 785 | 504990 | -75.59 | 17.01 | 378.53 | 0.18 | 1.48 | 1599 |
| 2024-09-20 22:21:40.950 | MS1 | 121.4656764282 | 31.1446185029 | 785 | 504990 | -84.86 | 13.47 | 483.53 | 0.06 | 2.18 | 1591 |
| 2024-09-20 22:21:41.636 | MS1 | 121.4656724545 | 31.1446237844 | 785 | 504990 | -79.67 | 17.41 | 451.39 | 0.07 | 2.60 | 1599 |
| 2024-09-20 22:21:42.964 | MS1 | 121.4656689049 | 31.1446324356 | 785 | 504990 | -76.47 | 17.03 | 333.58 | 0.00 | 2.29 | 1598 |

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
| 3218551 | 1 | 121.4748962043 | 31.1551206595 | 17 | 15 | 8 | 41.5 | TDD | 528 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3229881 | 2 | 121.4713163957 | 31.1499598215 | 223 | 4 | 6 | 45.3 | TDD | 785 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3239824 | 4 | 121.4729880880 | 31.1514376350 | 14 | 9 | 12 | 43.5 | TDD | 63 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3266662 | 3 | 121.4732332805 | 31.1540371929 | 170 | 1 | 10 | 49.1 | TDD | 269 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.415 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.430 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.574 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.574 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.281 | NREventA3 | measId:2;ServCellPCI:613;Se... |
| 2024-09-20 22:21:36.281 | NREventA3 | measId:2;ServCellPCI:613;Se... |
| 2024-09-20 22:21:37.281 | NREventA3 | measId:2;ServCellPCI:613;Se... |
| 2024-09-20 22:21:39.781 | NRRRCReestablishAttempt | PCI:613 |
| 2024-09-20 22:21:39.797 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.810 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.943 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.943 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218551 | 1 | 11.4045 | 15.8090 | -117.5411 | 18.5695 | 129.8152 | 0.0149 | 0.0157 |
| 2024_09_20 22:00 | 3229881 | 2 | 13.1114 | 14.6107 | -116.3590 | 10.8501 | 188.6537 | 0.0189 | 0.1621 |
| 2024_09_20 22:00 | 3266662 | 3 | 7.8290 | 17.0429 | -117.1486 | 16.1938 | 147.7857 | 0.0047 | 0.0086 |
| 2024_09_20 22:00 | 3239824 | 4 | 17.4349 | 5.0001 | -115.7214 | 17.6774 | 143.8843 | 0.0021 | 0.0102 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412930_3E9E68C8 | 504990 | 785 | -90.1 | 504990 | 269 | -82.7 | 504990 | 63 | -86.2 | 504990 | 528 |
| MR_1774412930_800ED2CB | 504990 | 269 | -86.2 | 504990 | 785 | -91.1 | 504990 | 63 | -89.1 | 504990 | 528 |
| MR_1774412930_94D9A1EE | 504990 | 785 | -89.2 | 504990 | 269 | -83.6 | 504990 | 63 | -86.9 | 504990 | 528 |
| MR_1774412930_437C8484 | 504990 | 785 | -91.0 | 504990 | 269 | -85.1 | 504990 | 63 | -89.2 | 504990 | 528 |
| MR_1774412930_A56C8033 | 504990 | 269 | -84.4 | 504990 | 785 | -90.9 | 504990 | 63 | -86.7 | 504990 | 528 |
| MR_1774412930_351FB2AF | 504990 | 785 | -92.0 | 504990 | 269 | -86.1 | 504990 | 63 | -85.7 | 504990 | 528 |
| MR_1774412930_851E2B17 | 504990 | 785 | -89.0 | 504990 | 269 | -85.0 | 504990 | 63 | -88.0 | 504990 | 528 |
| MR_1774412930_6C23E3C7 | 504990 | 269 | -85.6 | 504990 | 785 | -90.5 | 504990 | 63 | -89.3 | 504990 | 528 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 48: `c4dadddd-cc1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c4dadddd-cc1d-464c-8465-fbb199efe461` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[48] topology](images/train_0048.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues **← 정답**
- `C2`: Increase A3 Offset threshold for 3210182_1
- `C3`: Lift the tilt angle of 3263801_2 by 5 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210182_1
- `C5`: Increase transmission power for 3263801_2
- `C6`: Increase A3 Offset threshold for 3263801_2
- `C7`: Add neighbor relationship between 3263801_2 and 3210182_1
- `C8`: Decrease transmission power for 3263801_2
- `C9`: Lift the tilt angle  of 3210182_1 by 4 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263801_2
- `C11`: Adjust the azimuth of 3263801_2 by 50 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210182_1
- `C13`: Press down the tilt angle  of 3210182_1 by 4 degrees
- `C14`: Decrease A3 Offset threshold for 3210182_1
- `C15`: Decrease A3 Offset threshold for 3263801_2
- `C16`: Adjust the azimuth of 3210182_1 by 4 degrees
- `C17`: Add neighbor relationship between 3267286_3 and 3210182_1
- `C18`: Increase transmission power for 3210182_1
- `C19`: Press down the tilt angle of 3263801_2 by 5 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease transmission power for 3210182_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263801_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.431 | MS1 | 121.4656619900 | 31.1446273197 | 875 | 504990 | -90.39 | 14.17 | 382.09 | 0.15 | 2.56 | 1575 |
| 2024-09-20 22:21:32.940 | MS1 | 121.4656755331 | 31.1446251059 | 875 | 504990 | -90.48 | 17.94 | 390.00 | 0.08 | 2.51 | 1582 |
| 2024-09-20 22:21:33.972 | MS1 | 121.4656645151 | 31.1446252871 | 875 | 504990 | -88.33 | 16.30 | 363.10 | 0.00 | 2.63 | 1591 |
| 2024-09-20 22:21:34.999 | MS1 | 121.4656749081 | 31.1446244385 | 875 | 504990 | -85.92 | 12.17 | 87.12 | 0.18 | 2.44 | 499 |
| 2024-09-20 22:21:35.458 | MS1 | 121.4656751177 | 31.1446180162 | 875 | 504990 | -89.80 | 16.53 | 77.89 | 0.16 | 2.59 | 319 |
| 2024-09-20 22:21:36.672 | MS1 | 121.4656587337 | 31.1446338821 | 875 | 504990 | -86.48 | 12.51 | 89.73 | 0.18 | 2.91 | 424 |
| 2024-09-20 22:21:37.950 | MS1 | 121.4656644982 | 31.1446355435 | 875 | 504990 | -89.41 | 8.15 | 78.31 | 0.11 | 2.20 | 372 |
| 2024-09-20 22:21:38.104 | MS1 | 121.4656691582 | 31.1446310098 | 875 | 504990 | -89.80 | 11.20 | 92.88 | 0.04 | 2.24 | 480 |
| 2024-09-20 22:21:39.106 | MS1 | 121.4656712385 | 31.1446316167 | 875 | 504990 | -90.30 | 9.22 | 105.69 | 0.11 | 2.00 | 465 |
| 2024-09-20 22:21:40.804 | MS1 | 121.4656685864 | 31.1446354406 | 875 | 504990 | -91.36 | 8.19 | 559.97 | 0.00 | 2.25 | 1564 |
| 2024-09-20 22:21:41.827 | MS1 | 121.4656690302 | 31.1446189196 | 875 | 504990 | -89.72 | 7.83 | 377.50 | 0.05 | 2.30 | 1593 |
| 2024-09-20 22:21:42.563 | MS1 | 121.4656760032 | 31.1446373853 | 875 | 504990 | -92.93 | 8.63 | 344.07 | 0.20 | 2.21 | 1591 |

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
| 3210182 | 1 | 121.4747320939 | 31.1446121523 | 274 | 2 | 5 | 23.3 | TDD | 374 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3241777 | 4 | 121.4671520030 | 31.1522076972 | 188 | 14 | 5 | 45.4 | TDD | 70 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3263801 | 2 | 121.4758835716 | 31.1444624911 | 205 | 2 | 12 | 45.4 | TDD | 875 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3267286 | 3 | 121.4750666856 | 31.1543158770 | 290 | 14 | 6 | 40.1 | TDD | 788 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.555 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.570 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.700 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.700 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.430 | NREventA3 | measId:2;ServCellPCI:53;Ser... |
| 2024-09-20 22:21:38.670 | NRHandoverAttempt | SourcePCI:53;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.711 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.721 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.826 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.826 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210182 | 1 | 13.8495 | 10.0396 | -116.6556 | 8.4301 | 157.6110 | 0.0049 | 0.0049 |
| 2024_09_20 22:00 | 3263801 | 2 | 5.3554 | 9.7073 | -115.7977 | 7.1747 | 89.4438 | 0.0104 | 0.0059 |
| 2024_09_20 22:00 | 3267286 | 3 | 19.1623 | 18.1273 | -114.9778 | 19.3436 | 102.3193 | 0.0054 | 0.0047 |
| 2024_09_20 22:00 | 3241777 | 4 | 15.0195 | 17.0781 | -115.3150 | 15.1175 | 164.2417 | 0.0198 | 0.0106 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417195_08E37223 | 504990 | 875 | -87.6 | 504990 | 374 | -91.1 | 504990 | 788 | -99.0 | 504990 | 70 |
| MR_1774417195_297B90CC | 504990 | 875 | -87.6 | 504990 | 374 | -90.6 | 504990 | 788 | -100.5 | 504990 | 70 |
| MR_1774417195_50143458 | 504990 | 875 | -85.6 | 504990 | 374 | -88.5 | 504990 | 788 | -99.6 | 504990 | 70 |
| MR_1774417195_214BE8F1 | 504990 | 875 | -85.4 | 504990 | 374 | -88.3 | 504990 | 788 | -101.1 | 504990 | 70 |
| MR_1774417195_AA883D9D | 504990 | 875 | -84.4 | 504990 | 374 | -90.6 | 504990 | 788 | -100.7 | 504990 | 70 |
| MR_1774417195_EA5D6F23 | 504990 | 875 | -87.1 | 504990 | 374 | -88.1 | 504990 | 788 | -99.4 | 504990 | 70 |
| MR_1774417195_14AF610D | 504990 | 875 | -84.4 | 504990 | 374 | -90.5 | 504990 | 788 | -99.4 | 504990 | 70 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 49: `807626fb-09c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `807626fb-09ca-4955-8fd6-955797f6312b` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease A3 Offset threshold for 3213755_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[49] topology](images/train_0049.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213755_1
- `C2`: Press down the tilt angle  of 3239674_3 by 7 degrees
- `C3`: Press down the tilt angle of 3213755_1 by 8 degrees
- `C4`: Lift the tilt angle  of 3239674_3 by 7 degrees
- `C5`: Decrease A3 Offset threshold for 3239674_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239674_3
- `C7`: Decrease A3 Offset threshold for 3213755_1 **← 정답**
- `C8`: Increase transmission power for 3213755_1
- `C9`: Decrease transmission power for 3213755_1
- `C10`: Increase transmission power for 3239674_3
- `C11`: Increase A3 Offset threshold for 3239674_3
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Lift the tilt angle of 3213755_1 by 8 degrees
- `C14`: Add neighbor relationship between 3213755_1 and 3239674_3
- `C15`: Decrease transmission power for 3239674_3
- `C16`: Increase A3 Offset threshold for 3213755_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213755_1
- `C18`: Add neighbor relationship between 3270001_2 and 3239674_3
- `C19`: Check test server and transmission issues
- `C20`: Adjust the azimuth of 3239674_3 by 50 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239674_3
- `C22`: Adjust the azimuth of 3213755_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.687 | MS1 | 121.4656624122 | 31.1446211706 | 192 | 504990 | -83.17 | 16.15 | 339.80 | 0.19 | 2.31 | 1573 |
| 2024-09-20 22:21:32.544 | MS1 | 121.4656669490 | 31.1446360361 | 192 | 504990 | -80.81 | 12.01 | 314.91 | 0.12 | 2.45 | 1574 |
| 2024-09-20 22:21:33.164 | MS1 | 121.4656765819 | 31.1446346740 | 192 | 504990 | -80.35 | 14.04 | 531.53 | 0.09 | 2.72 | 1578 |
| 2024-09-20 22:21:34.903 | MS1 | 121.4656754357 | 31.1446239634 | 192 | 504990 | -92.24 | -1.57 | 62.13 | 0.10 | 1.38 | 1591 |
| 2024-09-20 22:21:35.639 | MS1 | 121.4656729596 | 31.1446336791 | 192 | 504990 | -83.21 | -0.30 | 80.66 | 0.05 | 1.29 | 1589 |
| 2024-09-20 22:21:36.943 | MS1 | 121.4656719225 | 31.1446344133 | 192 | 504990 | -89.45 | -2.03 | 28.49 | 0.20 | 1.29 | 1588 |
| 2024-09-20 22:21:37.540 | MS1 | 121.4656758759 | 31.1446342335 | 192 | 504990 | -84.12 | -0.28 | 26.95 | 0.13 | 1.24 | 1571 |
| 2024-09-20 22:21:38.541 | MS1 | 121.4656754927 | 31.1446191323 | 192 | 504990 | -89.54 | -2.09 | 58.30 | 0.20 | 1.28 | 1593 |
| 2024-09-20 22:21:39.869 | MS1 | 121.4656601399 | 31.1446235689 | 533 | 504990 | -82.23 | 13.21 | 250.26 | 0.15 | 1.43 | 1580 |
| 2024-09-20 22:21:40.451 | MS1 | 121.4656647215 | 31.1446346075 | 533 | 504990 | -78.37 | 15.75 | 563.84 | 0.08 | 2.51 | 1585 |
| 2024-09-20 22:21:41.471 | MS1 | 121.4656723351 | 31.1446202947 | 533 | 504990 | -76.48 | 16.55 | 310.05 | 0.13 | 2.42 | 1585 |
| 2024-09-20 22:21:42.782 | MS1 | 121.4656693930 | 31.1446284755 | 533 | 504990 | -83.60 | 17.46 | 472.80 | 0.05 | 2.33 | 1585 |

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
| 3213755 | 1 | 121.4723084112 | 31.1558732457 | 217 | 6 | 6 | 49.1 | TDD | 192 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3239674 | 3 | 121.4702856898 | 31.1452745128 | 74 | 2 | 11 | 38.2 | TDD | 533 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3270001 | 2 | 121.4756428920 | 31.1514061161 | 254 | 5 | 12 | 38.6 | TDD | 586 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3277932 | 4 | 121.4669659185 | 31.1440458318 | 254 | 9 | 10 | 16.7 | TDD | 157 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.948 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.964 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.075 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.075 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.802 | NREventA3 | measId:2;ServCellPCI:784;Se... |
| 2024-09-20 22:21:38.042 | NRHandoverAttempt | SourcePCI:784;SourceNR-ARFC... |
| 2024-09-20 22:21:38.079 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.094 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.202 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.202 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213755 | 1 | 6.9181 | 10.5256 | -117.8407 | 17.7811 | 92.9551 | 0.0077 | 0.1818 |
| 2024_09_20 22:00 | 3270001 | 2 | 19.7798 | 15.9030 | -115.4226 | 19.4769 | 136.3117 | 0.0082 | 0.0057 |
| 2024_09_20 22:00 | 3239674 | 3 | 8.7886 | 17.3481 | -116.8993 | 16.8147 | 184.5655 | 0.0177 | 0.0057 |
| 2024_09_20 22:00 | 3277932 | 4 | 7.7429 | 18.9590 | -115.1026 | 16.9681 | 129.4017 | 0.0007 | 0.0183 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415894_6695CFA9 | 504990 | 192 | -90.8 | 504990 | 533 | -84.7 | 504990 | 586 | -85.9 | 504990 | 157 |
| MR_1774415894_7AF00722 | 504990 | 192 | -90.8 | 504990 | 533 | -84.5 | 504990 | 586 | -86.1 | 504990 | 157 |
| MR_1774415894_369A343A | 504990 | 192 | -91.7 | 504990 | 533 | -84.9 | 504990 | 586 | -86.9 | 504990 | 157 |
| MR_1774415894_B96CBD46 | 504990 | 192 | -94.1 | 504990 | 533 | -83.9 | 504990 | 586 | -85.0 | 504990 | 157 |
| MR_1774415894_F5E656C5 | 504990 | 533 | -84.0 | 504990 | 192 | -90.7 | 504990 | 586 | -86.9 | 504990 | 157 |
| MR_1774415894_95CB8C7A | 504990 | 533 | -86.3 | 504990 | 192 | -94.1 | 504990 | 586 | -85.1 | 504990 | 157 |

> *... 2개 열 생략 (전체 14열)*

---
