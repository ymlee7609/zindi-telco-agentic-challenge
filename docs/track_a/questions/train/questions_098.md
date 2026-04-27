# Track A 문제 분석 — train[970]~train[979]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[970] ~ train[979] (10개)

## 목차

1. [문제 970: `41dfef82-548...`](#970) — single-answer, 정답: C12
2. [문제 971: `aae84ab3-056...`](#971) — single-answer, 정답: C17
3. [문제 972: `6d9c1168-13e...`](#972) — single-answer, 정답: C8
4. [문제 973: `b7716e63-9f8...`](#973) — single-answer, 정답: C21
5. [문제 974: `b4a9b36c-24b...`](#974) — single-answer, 정답: C1
6. [문제 975: `2f32eacc-e54...`](#975) — single-answer, 정답: C21
7. [문제 976: `74530cda-7e2...`](#976) — single-answer, 정답: C8
8. [문제 977: `9f4ffcca-c81...`](#977) — single-answer, 정답: C3
9. [문제 978: `8c98631d-49d...`](#978) — single-answer, 정답: C3
10. [문제 979: `acceaf16-ea3...`](#979) — single-answer, 정답: C7

---

### 문제 970: `41dfef82-548...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `41dfef82-5487-450a-a836-512f46227913` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[970] topology](images/train_0970.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258964_1
- `C2`: Adjust the azimuth of 3258964_1 by 50 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258964_1
- `C4`: Decrease A3 Offset threshold for 3258964_1
- `C5`: Decrease transmission power for 3258964_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248135_3
- `C7`: Press down the tilt angle of 3248135_3 by 1 degrees
- `C8`: Increase A3 Offset threshold for 3248135_3
- `C9`: Add neighbor relationship between 3270898_2 and 3258964_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248135_3
- `C11`: Decrease A3 Offset threshold for 3248135_3
- `C12`: Insufficient data; more data is needed for judgment. **← 정답**
- `C13`: Press down the tilt angle  of 3258964_1 by 3 degrees
- `C14`: Lift the tilt angle  of 3258964_1 by 3 degrees
- `C15`: Add neighbor relationship between 3248135_3 and 3258964_1
- `C16`: Decrease transmission power for 3248135_3
- `C17`: Lift the tilt angle of 3248135_3 by 1 degrees
- `C18`: Adjust the azimuth of 3248135_3 by 50 degrees
- `C19`: Increase A3 Offset threshold for 3258964_1
- `C20`: Increase transmission power for 3258964_1
- `C21`: Check test server and transmission issues
- `C22`: Increase transmission power for 3248135_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.635 | MS1 | 121.4656676513 | 31.1446373750 | 726 | 504990 | -85.12 | 13.55 | 377.61 | 0.18 | 2.53 | 1567 |
| 2024-09-20 22:21:32.373 | MS1 | 121.4656703524 | 31.1446311989 | 726 | 504990 | -90.84 | 15.63 | 566.46 | 0.18 | 2.62 | 1585 |
| 2024-09-20 22:21:33.658 | MS1 | 121.4656706742 | 31.1446287257 | 726 | 504990 | -91.65 | 12.29 | 572.42 | 0.03 | 2.46 | 1562 |
| 2024-09-20 22:21:34.449 | MS1 | 121.4656772199 | 31.1446245670 | 726 | 504990 | -86.70 | 14.95 | 66.82 | 0.16 | 2.98 | 1590 |
| 2024-09-20 22:21:35.690 | MS1 | 121.4656633205 | 31.1446297394 | 726 | 504990 | -86.02 | 16.58 | 94.09 | 0.01 | 2.65 | 1575 |
| 2024-09-20 22:21:36.540 | MS1 | 121.4656728138 | 31.1446192115 | 726 | 504990 | -88.88 | 15.65 | 84.27 | 0.17 | 2.35 | 1573 |
| 2024-09-20 22:21:37.878 | MS1 | 121.4656760764 | 31.1446372998 | 726 | 504990 | -90.94 | 8.79 | 65.11 | 0.14 | 2.08 | 1568 |
| 2024-09-20 22:21:38.875 | MS1 | 121.4656709979 | 31.1446227814 | 726 | 504990 | -90.88 | 9.26 | 53.08 | 0.07 | 2.54 | 1570 |
| 2024-09-20 22:21:39.993 | MS1 | 121.4656595899 | 31.1446218166 | 726 | 504990 | -89.54 | 8.18 | 95.70 | 0.17 | 2.49 | 1593 |
| 2024-09-20 22:21:40.374 | MS1 | 121.4656746688 | 31.1446246131 | 726 | 504990 | -90.08 | 11.65 | 510.09 | 0.00 | 2.92 | 1588 |
| 2024-09-20 22:21:41.651 | MS1 | 121.4656676960 | 31.1446325695 | 726 | 504990 | -91.29 | 10.22 | 462.94 | 0.16 | 2.18 | 1599 |
| 2024-09-20 22:21:42.214 | MS1 | 121.4656674956 | 31.1446319922 | 726 | 504990 | -92.81 | 10.85 | 537.75 | 0.17 | 2.94 | 1597 |

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
| 3239253 | 4 | 121.4715149267 | 31.1531380832 | 97 | 15 | 12 | 22.8 | TDD | 545 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3248135 | 3 | 121.4666022015 | 31.1549861057 | 52 | 0 | 7 | 21.7 | TDD | 726 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3258964 | 1 | 121.4725571771 | 31.1513081726 | 346 | 1 | 0 | 33.2 | TDD | 385 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3270898 | 2 | 121.4731573268 | 31.1490131838 | 252 | 2 | 0 | 22.9 | TDD | 531 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.973 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.988 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.111 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.111 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.823 | NREventA3 | measId:2;ServCellPCI:543;Se... |
| 2024-09-20 22:21:38.063 | NRHandoverAttempt | SourcePCI:543;SourceNR-ARFC... |
| 2024-09-20 22:21:38.106 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.120 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.220 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.220 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3258964 | 1 | 94.1793 | 92.8907 | -115.4324 | 15.9682 | 168.1878 | 0.0115 | 0.0189 |
| 2024_09_19 22:00 | 3270898 | 2 | 93.5098 | 82.3944 | -114.3108 | 6.3068 | 92.4227 | 0.0078 | 0.0130 |
| 2024_09_19 22:00 | 3248135 | 3 | 92.9943 | 93.6671 | -117.4842 | 5.5029 | 164.9395 | 0.0182 | 0.0092 |
| 2024_09_19 22:00 | 3239253 | 4 | 94.0220 | 86.0343 | -115.0874 | 6.0925 | 154.7590 | 0.0060 | 0.0105 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416051_0B606FF0 | 504990 | 726 | -87.1 | 504990 | 385 | -86.7 | 504990 | 531 | -93.9 | 504990 | 545 |
| MR_1774416051_06293581 | 504990 | 726 | -87.6 | 504990 | 385 | -88.2 | 504990 | 531 | -94.0 | 504990 | 545 |
| MR_1774416051_3BBD54E3 | 504990 | 726 | -85.8 | 504990 | 385 | -86.7 | 504990 | 531 | -93.3 | 504990 | 545 |
| MR_1774416051_D3759218 | 504990 | 726 | -86.6 | 504990 | 385 | -88.0 | 504990 | 531 | -93.6 | 504990 | 545 |
| MR_1774416051_CF4DA565 | 504990 | 726 | -87.1 | 504990 | 385 | -87.2 | 504990 | 531 | -93.0 | 504990 | 545 |
| MR_1774416051_410F791A | 504990 | 726 | -85.8 | 504990 | 385 | -86.9 | 504990 | 531 | -95.6 | 504990 | 545 |
| MR_1774416051_A67C24E4 | 504990 | 726 | -88.1 | 504990 | 385 | -88.0 | 504990 | 531 | -92.5 | 504990 | 545 |
| MR_1774416051_CFCA0BAD | 504990 | 726 | -87.5 | 504990 | 385 | -87.5 | 504990 | 531 | -94.7 | 504990 | 545 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 971: `aae84ab3-056...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `aae84ab3-0565-4e98-be26-efacae118304` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Lift the tilt angle  of 3224300_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[971] topology](images/train_0971.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271504_1
- `C2`: Adjust the azimuth of 3224300_3 by 21 degrees
- `C3`: Decrease A3 Offset threshold for 3271504_1
- `C4`: Increase transmission power for 3273531_4
- `C5`: Adjust the azimuth of 3271504_1 by 21 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273531_4
- `C7`: Increase A3 Offset threshold for 3273531_4
- `C8`: Press down the tilt angle  of 3224300_3 by 10 degrees
- `C9`: Decrease A3 Offset threshold for 3273531_4
- `C10`: Lift the tilt angle of 3271504_1 by 5 degrees
- `C11`: Decrease transmission power for 3271504_1
- `C12`: Increase A3 Offset threshold for 3271504_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271504_1
- `C14`: Decrease transmission power for 3273531_4
- `C15`: Add neighbor relationship between 3224300_3 and 3273531_4
- `C16`: Check test server and transmission issues
- `C17`: Lift the tilt angle  of 3224300_3 by 10 degrees **← 정답**
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273531_4
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Press down the tilt angle of 3271504_1 by 5 degrees
- `C21`: Add neighbor relationship between 3271504_1 and 3273531_4
- `C22`: Increase transmission power for 3271504_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.512 | MS1 | 121.4656660047 | 31.1446237728 | 803 | 504990 | -88.27 | 17.28 | 395.72 | 0.08 | 2.80 | 1561 |
| 2024-09-20 22:21:32.949 | MS1 | 121.4656661060 | 31.1446367666 | 803 | 504990 | -85.27 | 16.39 | 450.47 | 0.04 | 2.51 | 1579 |
| 2024-09-20 22:21:33.369 | MS1 | 121.4656670237 | 31.1446333519 | 803 | 504990 | -85.85 | 16.38 | 374.95 | 0.11 | 2.04 | 1579 |
| 2024-09-20 22:21:34.980 | MS1 | 121.4656651577 | 31.1446231364 | 803 | 504990 | -91.96 | 17.02 | 63.66 | 0.19 | 2.08 | 1588 |
| 2024-09-20 22:21:35.679 | MS1 | 121.4656596570 | 31.1446349604 | 803 | 504990 | -91.53 | 15.72 | 47.69 | 0.11 | 2.35 | 1561 |
| 2024-09-20 22:21:36.235 | MS1 | 121.4656613759 | 31.1446277354 | 803 | 504990 | -90.32 | 13.54 | 63.99 | 0.04 | 2.17 | 1593 |
| 2024-09-20 22:21:37.799 | MS1 | 121.4656622320 | 31.1446273133 | 803 | 504990 | -89.89 | 7.84 | 91.21 | 0.06 | 3.00 | 1567 |
| 2024-09-20 22:21:38.888 | MS1 | 121.4656726191 | 31.1446317834 | 803 | 504990 | -89.84 | 10.11 | 50.73 | 0.05 | 2.63 | 1597 |
| 2024-09-20 22:21:39.846 | MS1 | 121.4656731278 | 31.1446336299 | 803 | 504990 | -92.80 | 7.77 | 55.09 | 0.05 | 2.59 | 1596 |
| 2024-09-20 22:21:40.369 | MS1 | 121.4656735526 | 31.1446240249 | 803 | 504990 | -90.87 | 9.09 | 549.31 | 0.01 | 2.65 | 1579 |
| 2024-09-20 22:21:41.908 | MS1 | 121.4656694028 | 31.1446250568 | 803 | 504990 | -90.48 | 8.95 | 505.76 | 0.02 | 2.09 | 1573 |
| 2024-09-20 22:21:42.341 | MS1 | 121.4656597428 | 31.1446273300 | 803 | 504990 | -89.85 | 10.18 | 470.26 | 0.02 | 2.16 | 1599 |

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
| 3224300 | 3 | 121.4665102440 | 31.1444315751 | 66 | 9 | 7 | 32.2 | TDD | 549 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3267054 | 2 | 121.4693129886 | 31.1498273353 | 170 | 6 | 10 | 41.6 | TDD | 163 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3271504 | 1 | 121.4724615331 | 31.1470485404 | 226 | 3 | 8 | 27.6 | TDD | 803 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3273531 | 4 | 121.4684839138 | 31.1531817871 | 175 | 9 | 12 | 32.3 | TDD | 862 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.787 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.809 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.947 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.947 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.677 | NREventA3 | measId:2;ServCellPCI:997;Se... |
| 2024-09-20 22:21:37.917 | NRHandoverAttempt | SourcePCI:997;SourceNR-ARFC... |
| 2024-09-20 22:21:37.967 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.978 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.090 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.090 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271504 | 1 | 83.8794 | 86.5076 | -117.8243 | 10.5292 | 94.9107 | 0.0167 | 0.0072 |
| 2024_09_20 22:00 | 3267054 | 2 | 15.2662 | 15.4819 | -117.6633 | 6.1762 | 188.4598 | 0.0138 | 0.0063 |
| 2024_09_20 22:00 | 3224300 | 3 | 12.0142 | 5.1954 | -114.3788 | 15.1516 | 85.0921 | 0.0115 | 0.0160 |
| 2024_09_20 22:00 | 3273531 | 4 | 11.9277 | 13.5394 | -115.7413 | 10.5671 | 129.1759 | 0.0122 | 0.0035 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413664_0B123692 | 504990 | 803 | -92.2 | 504990 | 862 | -94.2 | 504990 | 549 | -98.8 | 504990 | 163 |
| MR_1774413664_B2BF2254 | 504990 | 803 | -90.8 | 504990 | 862 | -97.3 | 504990 | 549 | -98.7 | 504990 | 163 |
| MR_1774413664_395ADD99 | 504990 | 803 | -92.8 | 504990 | 862 | -95.5 | 504990 | 549 | -99.8 | 504990 | 163 |
| MR_1774413664_D89C011D | 504990 | 803 | -90.6 | 504990 | 862 | -95.9 | 504990 | 549 | -99.7 | 504990 | 163 |
| MR_1774413664_02EA788E | 504990 | 803 | -90.1 | 504990 | 862 | -94.4 | 504990 | 549 | -96.3 | 504990 | 163 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 972: `6d9c1168-13e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6d9c1168-13ec-4666-bbea-b57c7e90d5b4` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease A3 Offset threshold for 3249194_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[972] topology](images/train_0972.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3211667_4
- `C2`: Press down the tilt angle  of 3211667_4 by 10 degrees
- `C3`: Adjust the azimuth of 3211667_4 by 50 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Add neighbor relationship between 3249194_1 and 3211667_4
- `C6`: Increase A3 Offset threshold for 3211667_4
- `C7`: Lift the tilt angle  of 3211667_4 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3249194_1 **← 정답**
- `C9`: Decrease transmission power for 3211667_4
- `C10`: Add neighbor relationship between 3273936_2 and 3211667_4
- `C11`: Check test server and transmission issues
- `C12`: Increase transmission power for 3249194_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249194_1
- `C14`: Press down the tilt angle of 3249194_1 by 4 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211667_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211667_4
- `C17`: Decrease transmission power for 3249194_1
- `C18`: Increase transmission power for 3211667_4
- `C19`: Adjust the azimuth of 3249194_1 by 50 degrees
- `C20`: Increase A3 Offset threshold for 3249194_1
- `C21`: Lift the tilt angle of 3249194_1 by 4 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249194_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.519 | MS1 | 121.4656599154 | 31.1446241194 | 40 | 504990 | -80.19 | 17.04 | 507.74 | 0.20 | 2.16 | 1587 |
| 2024-09-20 22:21:32.400 | MS1 | 121.4656720521 | 31.1446321349 | 40 | 504990 | -82.33 | 15.54 | 509.84 | 0.08 | 2.89 | 1596 |
| 2024-09-20 22:21:33.161 | MS1 | 121.4656580036 | 31.1446367926 | 40 | 504990 | -79.38 | 12.54 | 422.43 | 0.15 | 2.27 | 1572 |
| 2024-09-20 22:21:34.809 | MS1 | 121.4656625777 | 31.1446352937 | 40 | 504990 | -86.67 | -1.17 | 80.90 | 0.12 | 1.24 | 1578 |
| 2024-09-20 22:21:35.531 | MS1 | 121.4656749201 | 31.1446269681 | 40 | 504990 | -91.23 | -3.90 | 40.31 | 0.05 | 1.39 | 1583 |
| 2024-09-20 22:21:36.956 | MS1 | 121.4656710997 | 31.1446203773 | 40 | 504990 | -89.75 | -2.43 | 42.50 | 0.06 | 1.02 | 1598 |
| 2024-09-20 22:21:37.369 | MS1 | 121.4656623991 | 31.1446251692 | 40 | 504990 | -84.44 | -0.73 | 42.25 | 0.02 | 1.43 | 1596 |
| 2024-09-20 22:21:38.800 | MS1 | 121.4656733580 | 31.1446239561 | 40 | 504990 | -87.33 | -0.21 | 67.14 | 0.07 | 1.35 | 1581 |
| 2024-09-20 22:21:39.865 | MS1 | 121.4656713198 | 31.1446373605 | 831 | 504990 | -81.72 | 15.01 | 254.48 | 0.19 | 1.42 | 1581 |
| 2024-09-20 22:21:40.612 | MS1 | 121.4656634959 | 31.1446295472 | 831 | 504990 | -78.56 | 13.32 | 535.24 | 0.07 | 2.15 | 1588 |
| 2024-09-20 22:21:41.616 | MS1 | 121.4656752852 | 31.1446285074 | 831 | 504990 | -83.91 | 16.16 | 351.30 | 0.01 | 2.41 | 1583 |
| 2024-09-20 22:21:42.204 | MS1 | 121.4656776810 | 31.1446256896 | 831 | 504990 | -76.64 | 12.24 | 543.93 | 0.00 | 2.45 | 1564 |

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
| 3210395 | 3 | 121.4667465530 | 31.1505366869 | 163 | 11 | 2 | 27.4 | TDD | 186 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3211667 | 4 | 121.4730483999 | 31.1476900212 | 339 | 13 | 2 | 47.8 | TDD | 831 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3249194 | 1 | 121.4758182653 | 31.1460098905 | 50 | 2 | 2 | 30.5 | TDD | 40 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3273936 | 2 | 121.4726675858 | 31.1474254405 | 63 | 8 | 1 | 25.0 | TDD | 625 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.335 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.357 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.496 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.496 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.165 | NREventA3 | measId:2;ServCellPCI:423;Se... |
| 2024-09-20 22:21:38.405 | NRHandoverAttempt | SourcePCI:423;SourceNR-ARFC... |
| 2024-09-20 22:21:38.452 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.467 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.595 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.595 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249194 | 1 | 15.2520 | 12.5604 | -117.5023 | 19.7019 | 124.2821 | 0.0103 | 0.1276 |
| 2024_09_20 22:00 | 3273936 | 2 | 16.5394 | 8.7286 | -114.5908 | 6.9145 | 109.8943 | 0.0144 | 0.0075 |
| 2024_09_20 22:00 | 3210395 | 3 | 16.8846 | 12.0663 | -116.3086 | 9.3947 | 128.4080 | 0.0118 | 0.0017 |
| 2024_09_20 22:00 | 3211667 | 4 | 9.0363 | 12.3339 | -117.7630 | 12.6156 | 119.2515 | 0.0028 | 0.0113 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416966_5DC79DE4 | 504990 | 40 | -86.4 | 504990 | 831 | -81.1 | 504990 | 625 | -82.5 | 504990 | 186 |
| MR_1774416966_76804C6A | 504990 | 40 | -86.1 | 504990 | 831 | -82.7 | 504990 | 625 | -82.9 | 504990 | 186 |
| MR_1774416966_7F5D1CF8 | 504990 | 831 | -79.4 | 504990 | 40 | -88.3 | 504990 | 625 | -85.3 | 504990 | 186 |
| MR_1774416966_B9E97935 | 504990 | 40 | -85.2 | 504990 | 831 | -80.6 | 504990 | 625 | -82.4 | 504990 | 186 |
| MR_1774416966_36177573 | 504990 | 831 | -79.6 | 504990 | 40 | -87.2 | 504990 | 625 | -86.2 | 504990 | 186 |
| MR_1774416966_6B711C85 | 504990 | 831 | -80.5 | 504990 | 40 | -85.4 | 504990 | 625 | -83.8 | 504990 | 186 |
| MR_1774416966_E13C7AAC | 504990 | 831 | -80.2 | 504990 | 40 | -86.8 | 504990 | 625 | -82.5 | 504990 | 186 |
| MR_1774416966_F3783867 | 504990 | 40 | -87.6 | 504990 | 831 | -82.7 | 504990 | 625 | -83.7 | 504990 | 186 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 973: `b7716e63-9f8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b7716e63-9f81-4dd6-a430-9b6d9e51fbc0` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Add neighbor relationship between 3275286_1 and 3221429_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[973] topology](images/train_0973.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3221429_2
- `C2`: Press down the tilt angle of 3275286_1 by 10 degrees
- `C3`: Lift the tilt angle of 3275286_1 by 10 degrees
- `C4`: Lift the tilt angle  of 3221429_2 by 6 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221429_2
- `C6`: Adjust the azimuth of 3221429_2 by 40 degrees
- `C7`: Adjust the azimuth of 3275286_1 by 50 degrees
- `C8`: Increase transmission power for 3275286_1
- `C9`: Press down the tilt angle  of 3221429_2 by 6 degrees
- `C10`: Decrease transmission power for 3275286_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease A3 Offset threshold for 3221429_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275286_1
- `C14`: Increase A3 Offset threshold for 3275286_1
- `C15`: Add neighbor relationship between 3257566_4 and 3221429_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221429_2
- `C17`: Decrease A3 Offset threshold for 3275286_1
- `C18`: Increase A3 Offset threshold for 3221429_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275286_1
- `C20`: Check test server and transmission issues
- `C21`: Add neighbor relationship between 3275286_1 and 3221429_2 **← 정답**
- `C22`: Increase transmission power for 3221429_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.933 | MS1 | 121.4656644328 | 31.1446298889 | 248 | 504990 | -81.65 | 14.53 | 531.44 | 0.01 | 2.23 | 1590 |
| 2024-09-20 22:21:32.533 | MS1 | 121.4656694973 | 31.1446251743 | 248 | 504990 | -78.90 | 14.51 | 492.54 | 0.15 | 2.37 | 1585 |
| 2024-09-20 22:21:33.164 | MS1 | 121.4656777892 | 31.1446216976 | 248 | 504990 | -81.08 | 16.58 | 594.85 | 0.04 | 2.36 | 1591 |
| 2024-09-20 22:21:34.204 | MS1 | 121.4656691627 | 31.1446339578 | 248 | 504990 | -91.03 | -3.16 | 58.81 | 0.14 | 1.47 | 1583 |
| 2024-09-20 22:21:35.495 | MS1 | 121.4656737285 | 31.1446224840 | 248 | 504990 | -92.62 | -3.30 | 73.38 | 0.17 | 1.08 | 1589 |
| 2024-09-20 22:21:36.354 | MS1 | 121.4656734489 | 31.1446265205 | 248 | 504990 | -86.05 | -3.56 | 47.86 | 0.16 | 1.36 | 1568 |
| 2024-09-20 22:21:37.243 | MS1 | 121.4656585458 | 31.1446255968 | 248 | 504990 | -89.83 | -0.35 | 43.85 | 0.10 | 1.11 | 1597 |
| 2024-09-20 22:21:38.538 | MS1 | 121.4656777431 | 31.1446341803 | 248 | 504990 | -78.39 | 14.22 | 542.47 | 0.17 | 1.23 | 1569 |
| 2024-09-20 22:21:39.956 | MS1 | 121.4656761538 | 31.1446233156 | 248 | 504990 | -79.82 | 15.31 | 317.70 | 0.03 | 1.38 | 1589 |
| 2024-09-20 22:21:40.814 | MS1 | 121.4656677818 | 31.1446277872 | 248 | 504990 | -83.25 | 17.45 | 504.82 | 0.09 | 2.41 | 1580 |
| 2024-09-20 22:21:41.743 | MS1 | 121.4656617066 | 31.1446268464 | 248 | 504990 | -83.73 | 17.92 | 547.25 | 0.05 | 2.14 | 1589 |
| 2024-09-20 22:21:42.340 | MS1 | 121.4656728343 | 31.1446262635 | 248 | 504990 | -77.00 | 13.51 | 481.41 | 0.07 | 2.24 | 1572 |

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
| 3221429 | 2 | 121.4663484246 | 31.1511998624 | 225 | 4 | 3 | 22.1 | TDD | 498 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3257566 | 4 | 121.4736416107 | 31.1523560614 | 357 | 8 | 9 | 25.0 | TDD | 98 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3270518 | 3 | 121.4651843119 | 31.1501483232 | 105 | 2 | 3 | 22.3 | TDD | 896 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3275286 | 1 | 121.4650440202 | 31.1516457719 | 87 | 11 | 0 | 31.1 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.044 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.066 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.215 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.215 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.919 | NREventA3 | measId:2;ServCellPCI:177;Se... |
| 2024-09-20 22:21:35.919 | NREventA3 | measId:2;ServCellPCI:177;Se... |
| 2024-09-20 22:21:36.919 | NREventA3 | measId:2;ServCellPCI:177;Se... |
| 2024-09-20 22:21:39.419 | NRRRCReestablishAttempt | PCI:177 |
| 2024-09-20 22:21:39.432 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.447 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.577 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.577 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275286 | 1 | 6.9762 | 8.0404 | -117.6790 | 5.3942 | 191.5554 | 0.0179 | 0.1920 |
| 2024_09_20 22:00 | 3221429 | 2 | 10.1047 | 13.6620 | -114.2325 | 10.5583 | 146.9146 | 0.0048 | 0.0078 |
| 2024_09_20 22:00 | 3270518 | 3 | 13.0474 | 15.2099 | -117.1282 | 10.5111 | 198.5105 | 0.0188 | 0.0057 |
| 2024_09_20 22:00 | 3257566 | 4 | 12.1620 | 18.8487 | -115.0130 | 19.0945 | 103.4597 | 0.0090 | 0.0119 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417083_52939524 | 504990 | 498 | -84.3 | 504990 | 248 | -90.0 | 504990 | 98 | -87.9 | 504990 | 896 |
| MR_1774417083_FF75FD51 | 504990 | 248 | -89.1 | 504990 | 498 | -87.8 | 504990 | 98 | -89.4 | 504990 | 896 |
| MR_1774417083_DD8B61E1 | 504990 | 498 | -86.1 | 504990 | 248 | -92.4 | 504990 | 98 | -88.7 | 504990 | 896 |
| MR_1774417083_490451B4 | 504990 | 498 | -85.8 | 504990 | 248 | -91.8 | 504990 | 98 | -88.4 | 504990 | 896 |
| MR_1774417083_426E309B | 504990 | 248 | -92.8 | 504990 | 498 | -85.3 | 504990 | 98 | -88.6 | 504990 | 896 |
| MR_1774417083_344F147F | 504990 | 248 | -90.0 | 504990 | 498 | -88.1 | 504990 | 98 | -89.3 | 504990 | 896 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 974: `b4a9b36c-24b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b4a9b36c-24b4-474d-a612-4e5b07dfadf7` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[974] topology](images/train_0974.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment. **← 정답**
- `C2`: Increase transmission power for 3273898_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273898_3
- `C4`: Lift the tilt angle  of 3217505_2 by 10 degrees
- `C5`: Press down the tilt angle of 3273898_3 by 10 degrees
- `C6`: Decrease transmission power for 3273898_3
- `C7`: Decrease A3 Offset threshold for 3217505_2
- `C8`: Decrease transmission power for 3217505_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217505_2
- `C10`: Press down the tilt angle  of 3217505_2 by 10 degrees
- `C11`: Adjust the azimuth of 3273898_3 by 37 degrees
- `C12`: Adjust the azimuth of 3217505_2 by 50 degrees
- `C13`: Check test server and transmission issues
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273898_3
- `C15`: Decrease A3 Offset threshold for 3273898_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217505_2
- `C17`: Lift the tilt angle of 3273898_3 by 10 degrees
- `C18`: Increase A3 Offset threshold for 3217505_2
- `C19`: Increase A3 Offset threshold for 3273898_3
- `C20`: Add neighbor relationship between 3273898_3 and 3217505_2
- `C21`: Add neighbor relationship between 3242950_4 and 3217505_2
- `C22`: Increase transmission power for 3217505_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.892 | MS1 | 121.4656772531 | 31.1446271999 | 589 | 504990 | -91.61 | 17.93 | 302.11 | 0.17 | 2.72 | 1570 |
| 2024-09-20 22:21:32.283 | MS1 | 121.4656725899 | 31.1446307286 | 589 | 504990 | -91.32 | 16.10 | 331.66 | 0.17 | 2.78 | 1574 |
| 2024-09-20 22:21:33.737 | MS1 | 121.4656592754 | 31.1446214111 | 589 | 504990 | -90.03 | 17.37 | 309.40 | 0.11 | 2.01 | 1571 |
| 2024-09-20 22:21:34.402 | MS1 | 121.4656773736 | 31.1446213750 | 589 | 504990 | -89.28 | 16.68 | 67.15 | 0.13 | 2.32 | 1569 |
| 2024-09-20 22:21:35.801 | MS1 | 121.4656598117 | 31.1446316385 | 589 | 504990 | -90.49 | 17.91 | 73.83 | 0.11 | 2.97 | 1598 |
| 2024-09-20 22:21:36.610 | MS1 | 121.4656647615 | 31.1446331951 | 589 | 504990 | -86.25 | 17.58 | 83.29 | 0.19 | 2.17 | 1589 |
| 2024-09-20 22:21:37.649 | MS1 | 121.4656669536 | 31.1446278882 | 589 | 504990 | -92.48 | 9.85 | 90.05 | 0.16 | 2.32 | 1590 |
| 2024-09-20 22:21:38.932 | MS1 | 121.4656586806 | 31.1446334897 | 589 | 504990 | -90.41 | 8.40 | 101.32 | 0.17 | 2.02 | 1577 |
| 2024-09-20 22:21:39.235 | MS1 | 121.4656731748 | 31.1446336775 | 589 | 504990 | -93.25 | 8.09 | 68.98 | 0.18 | 2.36 | 1576 |
| 2024-09-20 22:21:40.121 | MS1 | 121.4656704075 | 31.1446353418 | 589 | 504990 | -91.76 | 9.99 | 547.85 | 0.16 | 2.40 | 1575 |
| 2024-09-20 22:21:41.288 | MS1 | 121.4656616154 | 31.1446318970 | 589 | 504990 | -90.93 | 11.61 | 449.46 | 0.04 | 2.96 | 1594 |
| 2024-09-20 22:21:42.394 | MS1 | 121.4656604893 | 31.1446351677 | 589 | 504990 | -93.79 | 8.47 | 591.33 | 0.13 | 2.94 | 1598 |

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
| 3217505 | 2 | 121.4657811886 | 31.1523234912 | 122 | 14 | 7 | 29.4 | TDD | 636 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3240490 | 1 | 121.4731585767 | 31.1485613960 | 8 | 8 | 6 | 26.8 | TDD | 800 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3242950 | 4 | 121.4734759703 | 31.1472736574 | 107 | 15 | 1 | 44.1 | TDD | 991 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3273898 | 3 | 121.4713147243 | 31.1442995817 | 237 | 14 | 12 | 49.9 | TDD | 589 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.890 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.908 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.033 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.033 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.714 | NREventA3 | measId:2;ServCellPCI:700;Se... |
| 2024-09-20 22:21:37.954 | NRHandoverAttempt | SourcePCI:700;SourceNR-ARFC... |
| 2024-09-20 22:21:37.994 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.009 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.127 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.127 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3240490 | 1 | 76.2490 | 92.9298 | -114.3727 | 15.9085 | 103.7751 | 0.0087 | 0.0052 |
| 2024_09_19 22:00 | 3217505 | 2 | 91.4639 | 79.4393 | -114.1793 | 10.2545 | 171.6931 | 0.0137 | 0.0110 |
| 2024_09_19 22:00 | 3273898 | 3 | 81.2940 | 82.9583 | -115.8095 | 12.2478 | 120.7748 | 0.0191 | 0.0185 |
| 2024_09_19 22:00 | 3242950 | 4 | 84.1723 | 86.2409 | -116.1310 | 11.5875 | 167.1573 | 0.0137 | 0.0141 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417062_F00E0E96 | 504990 | 589 | -89.2 | 504990 | 636 | -90.4 | 504990 | 991 | -103.2 | 504990 | 800 |
| MR_1774417062_63CDDED0 | 504990 | 589 | -88.9 | 504990 | 636 | -92.8 | 504990 | 991 | -102.0 | 504990 | 800 |
| MR_1774417062_40CAA1BE | 504990 | 589 | -87.9 | 504990 | 636 | -91.4 | 504990 | 991 | -100.0 | 504990 | 800 |
| MR_1774417062_F872DA81 | 504990 | 589 | -91.2 | 504990 | 636 | -91.4 | 504990 | 991 | -101.8 | 504990 | 800 |
| MR_1774417062_741D3AA6 | 504990 | 589 | -90.4 | 504990 | 636 | -92.7 | 504990 | 991 | -100.1 | 504990 | 800 |
| MR_1774417062_DFE56087 | 504990 | 589 | -88.4 | 504990 | 636 | -93.1 | 504990 | 991 | -103.6 | 504990 | 800 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 975: `2f32eacc-e54...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2f32eacc-e547-4b67-a2f2-6135e2d62a6f` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[975] topology](images/train_0975.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3244817_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244817_2
- `C3`: Add neighbor relationship between 3253934_1 and 3244817_2
- `C4`: Lift the tilt angle of 3222181_3 by 10 degrees
- `C5`: Add neighbor relationship between 3222181_3 and 3244817_2
- `C6`: Increase transmission power for 3222181_3
- `C7`: Increase A3 Offset threshold for 3222181_3
- `C8`: Press down the tilt angle  of 3244817_2 by 5 degrees
- `C9`: Adjust the azimuth of 3222181_3 by 50 degrees
- `C10`: Check test server and transmission issues
- `C11`: Decrease A3 Offset threshold for 3244817_2
- `C12`: Increase transmission power for 3244817_2
- `C13`: Press down the tilt angle of 3222181_3 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222181_3
- `C15`: Adjust the azimuth of 3244817_2 by 40 degrees
- `C16`: Decrease transmission power for 3222181_3
- `C17`: Lift the tilt angle  of 3244817_2 by 5 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244817_2
- `C19`: Decrease A3 Offset threshold for 3222181_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222181_3
- `C21`: Insufficient data; more data is needed for judgment. **← 정답**
- `C22`: Decrease transmission power for 3244817_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.853 | MS1 | 121.4656641658 | 31.1446206325 | 605 | 504990 | -86.79 | 15.40 | 314.77 | 0.08 | 2.05 | 1598 |
| 2024-09-20 22:21:32.758 | MS1 | 121.4656581196 | 31.1446288457 | 605 | 504990 | -85.38 | 12.86 | 492.83 | 0.02 | 2.44 | 1589 |
| 2024-09-20 22:21:33.361 | MS1 | 121.4656706494 | 31.1446212827 | 605 | 504990 | -86.47 | 15.16 | 563.20 | 0.02 | 2.79 | 1564 |
| 2024-09-20 22:21:34.404 | MS1 | 121.4656705464 | 31.1446222167 | 605 | 504990 | -90.48 | 12.18 | 50.41 | 0.14 | 2.26 | 1570 |
| 2024-09-20 22:21:35.338 | MS1 | 121.4656609757 | 31.1446259805 | 605 | 504990 | -85.57 | 13.25 | 63.10 | 0.10 | 2.08 | 1593 |
| 2024-09-20 22:21:36.308 | MS1 | 121.4656610416 | 31.1446330460 | 605 | 504990 | -88.42 | 14.76 | 58.72 | 0.03 | 2.56 | 1579 |
| 2024-09-20 22:21:37.417 | MS1 | 121.4656589632 | 31.1446252048 | 605 | 504990 | -91.97 | 11.46 | 55.75 | 0.01 | 2.58 | 1572 |
| 2024-09-20 22:21:38.408 | MS1 | 121.4656653581 | 31.1446209176 | 605 | 504990 | -93.15 | 9.69 | 52.81 | 0.06 | 2.83 | 1578 |
| 2024-09-20 22:21:39.712 | MS1 | 121.4656587740 | 31.1446235700 | 605 | 504990 | -91.28 | 10.56 | 55.11 | 0.04 | 2.78 | 1565 |
| 2024-09-20 22:21:40.554 | MS1 | 121.4656618041 | 31.1446223426 | 605 | 504990 | -91.51 | 11.47 | 548.52 | 0.09 | 2.72 | 1573 |
| 2024-09-20 22:21:41.967 | MS1 | 121.4656677089 | 31.1446244683 | 605 | 504990 | -90.31 | 7.10 | 553.80 | 0.03 | 2.25 | 1572 |
| 2024-09-20 22:21:42.495 | MS1 | 121.4656646577 | 31.1446330843 | 605 | 504990 | -93.41 | 10.91 | 464.82 | 0.02 | 2.90 | 1600 |

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
| 3222181 | 3 | 121.4643561946 | 31.1465998955 | 301 | 10 | 2 | 21.2 | TDD | 605 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3236096 | 4 | 121.4686240367 | 31.1490562551 | 171 | 2 | 3 | 46.7 | TDD | 526 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3244817 | 2 | 121.4683918023 | 31.1553808507 | 152 | 4 | 11 | 26.2 | TDD | 812 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3253934 | 1 | 121.4654798342 | 31.1556545559 | 39 | 0 | 8 | 48.0 | TDD | 915 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.569 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.694 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.694 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.448 | NREventA3 | measId:2;ServCellPCI:726;Se... |
| 2024-09-20 22:21:38.688 | NRHandoverAttempt | SourcePCI:726;SourceNR-ARFC... |
| 2024-09-20 22:21:38.731 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.746 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.876 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.876 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3253934 | 1 | 94.7649 | 81.9138 | -115.5150 | 14.9759 | 105.4145 | 0.0112 | 0.0173 |
| 2024_09_19 22:00 | 3244817 | 2 | 89.0054 | 94.9930 | -116.7075 | 6.2933 | 183.1631 | 0.0152 | 0.0129 |
| 2024_09_19 22:00 | 3222181 | 3 | 94.6717 | 83.7240 | -116.5587 | 18.8625 | 108.9175 | 0.0026 | 0.0035 |
| 2024_09_19 22:00 | 3236096 | 4 | 89.1425 | 90.7386 | -115.2859 | 15.3363 | 133.6492 | 0.0075 | 0.0162 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413465_268C182A | 504990 | 605 | -89.1 | 504990 | 812 | -91.9 | 504990 | 915 | -104.5 | 504990 | 526 |
| MR_1774413465_5619DA2C | 504990 | 605 | -88.6 | 504990 | 812 | -92.3 | 504990 | 915 | -104.5 | 504990 | 526 |
| MR_1774413465_55175655 | 504990 | 605 | -88.9 | 504990 | 812 | -90.5 | 504990 | 915 | -105.2 | 504990 | 526 |
| MR_1774413465_9200FC43 | 504990 | 605 | -92.1 | 504990 | 812 | -90.3 | 504990 | 915 | -105.4 | 504990 | 526 |
| MR_1774413465_BCCA67DA | 504990 | 605 | -92.0 | 504990 | 812 | -91.9 | 504990 | 915 | -105.0 | 504990 | 526 |
| MR_1774413465_006DDD77 | 504990 | 605 | -89.0 | 504990 | 812 | -90.1 | 504990 | 915 | -104.2 | 504990 | 526 |
| MR_1774413465_398E544A | 504990 | 605 | -90.4 | 504990 | 812 | -91.6 | 504990 | 915 | -105.5 | 504990 | 526 |
| MR_1774413465_FBEF714A | 504990 | 605 | -91.6 | 504990 | 812 | -89.7 | 504990 | 915 | -106.7 | 504990 | 526 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 976: `74530cda-7e2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `74530cda-7e23-48c4-9d48-7710982af299` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease A3 Offset threshold for 3276610_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[976] topology](images/train_0976.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3240746_2 by 10 degrees
- `C2`: Adjust the azimuth of 3276610_1 by 50 degrees
- `C3`: Increase transmission power for 3240746_2
- `C4`: Increase transmission power for 3276610_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276610_1
- `C6`: Decrease transmission power for 3240746_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276610_1
- `C8`: Decrease A3 Offset threshold for 3276610_1 **← 정답**
- `C9`: Lift the tilt angle of 3276610_1 by 10 degrees
- `C10`: Decrease A3 Offset threshold for 3240746_2
- `C11`: Check test server and transmission issues
- `C12`: Increase A3 Offset threshold for 3240746_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240746_2
- `C14`: Increase A3 Offset threshold for 3276610_1
- `C15`: Add neighbor relationship between 3277530_4 and 3240746_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240746_2
- `C17`: Adjust the azimuth of 3240746_2 by 50 degrees
- `C18`: Press down the tilt angle of 3276610_1 by 10 degrees
- `C19`: Add neighbor relationship between 3276610_1 and 3240746_2
- `C20`: Decrease transmission power for 3276610_1
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Lift the tilt angle  of 3240746_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.958 | MS1 | 121.4656744100 | 31.1446288306 | 785 | 504990 | -75.57 | 13.63 | 543.02 | 0.06 | 2.55 | 1572 |
| 2024-09-20 22:21:32.961 | MS1 | 121.4656697558 | 31.1446185374 | 785 | 504990 | -84.96 | 12.95 | 581.77 | 0.02 | 2.78 | 1574 |
| 2024-09-20 22:21:33.343 | MS1 | 121.4656651888 | 31.1446250952 | 785 | 504990 | -81.50 | 13.59 | 371.79 | 0.17 | 2.43 | 1563 |
| 2024-09-20 22:21:34.908 | MS1 | 121.4656634042 | 31.1446344207 | 785 | 504990 | -87.66 | -2.19 | 61.69 | 0.03 | 1.34 | 1574 |
| 2024-09-20 22:21:35.955 | MS1 | 121.4656667939 | 31.1446377642 | 785 | 504990 | -87.99 | -3.52 | 60.89 | 0.16 | 1.23 | 1577 |
| 2024-09-20 22:21:36.830 | MS1 | 121.4656772042 | 31.1446244212 | 785 | 504990 | -84.94 | -2.27 | 55.15 | 0.07 | 1.47 | 1561 |
| 2024-09-20 22:21:37.153 | MS1 | 121.4656754228 | 31.1446265995 | 785 | 504990 | -90.15 | -0.39 | 64.02 | 0.02 | 1.06 | 1576 |
| 2024-09-20 22:21:38.251 | MS1 | 121.4656602057 | 31.1446310609 | 785 | 504990 | -88.06 | -3.39 | 26.50 | 0.01 | 1.15 | 1593 |
| 2024-09-20 22:21:39.677 | MS1 | 121.4656651579 | 31.1446283029 | 283 | 504990 | -83.24 | 17.80 | 194.25 | 0.03 | 1.06 | 1577 |
| 2024-09-20 22:21:40.260 | MS1 | 121.4656634168 | 31.1446320301 | 283 | 504990 | -75.85 | 17.85 | 366.48 | 0.01 | 2.96 | 1567 |
| 2024-09-20 22:21:41.443 | MS1 | 121.4656681610 | 31.1446297191 | 283 | 504990 | -81.03 | 15.52 | 590.27 | 0.10 | 2.21 | 1582 |
| 2024-09-20 22:21:42.650 | MS1 | 121.4656746161 | 31.1446275749 | 283 | 504990 | -83.89 | 13.20 | 358.60 | 0.06 | 2.63 | 1565 |

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
| 3237520 | 3 | 121.4739134002 | 31.1550448516 | 331 | 14 | 2 | 29.1 | TDD | 188 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3240746 | 2 | 121.4708877959 | 31.1516808511 | 274 | 11 | 1 | 40.0 | TDD | 283 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3276610 | 1 | 121.4669909791 | 31.1484269628 | 310 | 4 | 8 | 44.7 | TDD | 785 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3277530 | 4 | 121.4724302535 | 31.1533533965 | 172 | 15 | 4 | 26.9 | TDD | 135 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.952 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.973 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.086 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.086 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.768 | NREventA3 | measId:2;ServCellPCI:375;Se... |
| 2024-09-20 22:21:38.008 | NRHandoverAttempt | SourcePCI:375;SourceNR-ARFC... |
| 2024-09-20 22:21:38.048 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.063 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.193 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.193 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276610 | 1 | 12.7927 | 6.4873 | -116.2485 | 13.8998 | 184.1754 | 0.0062 | 0.1088 |
| 2024_09_20 22:00 | 3240746 | 2 | 9.6097 | 16.7958 | -115.6627 | 17.2727 | 123.9490 | 0.0117 | 0.0103 |
| 2024_09_20 22:00 | 3237520 | 3 | 7.8978 | 10.6989 | -114.7703 | 19.2406 | 188.7642 | 0.0170 | 0.0041 |
| 2024_09_20 22:00 | 3277530 | 4 | 16.0903 | 8.1707 | -114.0812 | 12.4424 | 137.6173 | 0.0087 | 0.0009 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416436_D62A083A | 504990 | 785 | -87.7 | 504990 | 283 | -81.0 | 504990 | 135 | -85.4 | 504990 | 188 |
| MR_1774416436_CBC92F72 | 504990 | 283 | -82.6 | 504990 | 785 | -86.9 | 504990 | 135 | -85.5 | 504990 | 188 |
| MR_1774416436_B0BBAC8A | 504990 | 283 | -81.8 | 504990 | 785 | -88.7 | 504990 | 135 | -87.8 | 504990 | 188 |
| MR_1774416436_428C26AA | 504990 | 785 | -86.4 | 504990 | 283 | -80.8 | 504990 | 135 | -88.1 | 504990 | 188 |
| MR_1774416436_1AE4FCBD | 504990 | 785 | -88.7 | 504990 | 283 | -82.2 | 504990 | 135 | -88.9 | 504990 | 188 |
| MR_1774416436_88E7CD22 | 504990 | 283 | -81.1 | 504990 | 785 | -88.9 | 504990 | 135 | -88.9 | 504990 | 188 |
| MR_1774416436_D5BE8DAE | 504990 | 283 | -82.1 | 504990 | 785 | -86.8 | 504990 | 135 | -86.1 | 504990 | 188 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 977: `9f4ffcca-c81...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9f4ffcca-c810-40b9-a95c-7f48134f90b1` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3242158_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[977] topology](images/train_0977.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3263622_3
- `C2`: Adjust the azimuth of 3263622_3 by 50 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242158_2 **← 정답**
- `C4`: Press down the tilt angle  of 3263622_3 by 10 degrees
- `C5`: Increase transmission power for 3242158_2
- `C6`: Decrease transmission power for 3263622_3
- `C7`: Check test server and transmission issues
- `C8`: Add neighbor relationship between 3247890_4 and 3263622_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263622_3
- `C10`: Lift the tilt angle of 3242158_2 by 5 degrees
- `C11`: Adjust the azimuth of 3242158_2 by 0 degrees
- `C12`: Lift the tilt angle  of 3263622_3 by 10 degrees
- `C13`: Increase A3 Offset threshold for 3263622_3
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease transmission power for 3242158_2
- `C16`: Press down the tilt angle of 3242158_2 by 5 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242158_2
- `C18`: Increase transmission power for 3263622_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263622_3
- `C20`: Add neighbor relationship between 3242158_2 and 3263622_3
- `C21`: Decrease A3 Offset threshold for 3242158_2
- `C22`: Increase A3 Offset threshold for 3242158_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.835 | MS1 | 121.4656701792 | 31.1446272982 | 651 | 504990 | -87.87 | 13.05 | 375.78 | 0.04 | 2.67 | 1587 |
| 2024-09-20 22:21:32.969 | MS1 | 121.4656640125 | 31.1446262391 | 651 | 504990 | -88.76 | 13.82 | 395.93 | 0.00 | 2.91 | 1586 |
| 2024-09-20 22:21:33.810 | MS1 | 121.4656611160 | 31.1446344536 | 651 | 504990 | -85.71 | 17.54 | 316.89 | 0.02 | 2.84 | 1561 |
| 2024-09-20 22:21:34.551 | MS1 | 121.4656605442 | 31.1446278878 | 651 | 504990 | -88.35 | 17.45 | 86.90 | 0.62 | 2.67 | 642 |
| 2024-09-20 22:21:35.601 | MS1 | 121.4656772267 | 31.1446327145 | 651 | 504990 | -86.18 | 15.96 | 72.27 | 0.70 | 2.91 | 505 |
| 2024-09-20 22:21:36.693 | MS1 | 121.4656672135 | 31.1446228874 | 651 | 504990 | -86.27 | 12.78 | 61.51 | 0.51 | 2.87 | 530 |
| 2024-09-20 22:21:37.306 | MS1 | 121.4656654589 | 31.1446296052 | 651 | 504990 | -89.62 | 9.41 | 73.03 | 0.60 | 2.59 | 615 |
| 2024-09-20 22:21:38.794 | MS1 | 121.4656587427 | 31.1446194598 | 651 | 504990 | -91.28 | 10.84 | 102.56 | 0.65 | 2.55 | 660 |
| 2024-09-20 22:21:39.484 | MS1 | 121.4656668839 | 31.1446351004 | 651 | 504990 | -89.36 | 12.93 | 75.11 | 0.61 | 2.51 | 618 |
| 2024-09-20 22:21:40.693 | MS1 | 121.4656715950 | 31.1446197139 | 651 | 504990 | -93.92 | 12.30 | 517.91 | 0.07 | 2.51 | 1565 |
| 2024-09-20 22:21:41.161 | MS1 | 121.4656739081 | 31.1446180040 | 651 | 504990 | -89.20 | 8.27 | 539.16 | 0.19 | 2.10 | 1567 |
| 2024-09-20 22:21:42.632 | MS1 | 121.4656763804 | 31.1446368159 | 651 | 504990 | -92.21 | 7.37 | 476.68 | 0.02 | 2.76 | 1565 |

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
| 3234867 | 1 | 121.4677783585 | 31.1454433069 | 111 | 5 | 11 | 38.9 | TDD | 32 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3242158 | 2 | 121.4713742663 | 31.1521542671 | 213 | 3 | 10 | 38.9 | TDD | 651 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3247890 | 4 | 121.4722604329 | 31.1501417834 | 338 | 11 | 1 | 49.5 | TDD | 502 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3263622 | 3 | 121.4735132708 | 31.1503506196 | 20 | 12 | 10 | 48.2 | TDD | 1005 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.307 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.324 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.443 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.443 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.205 | NREventA3 | measId:2;ServCellPCI:435;Se... |
| 2024-09-20 22:21:38.445 | NRHandoverAttempt | SourcePCI:435;SourceNR-ARFC... |
| 2024-09-20 22:21:38.482 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.495 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.613 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.613 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234867 | 1 | 17.4212 | 8.4448 | -116.1669 | 12.5430 | 155.3324 | 0.0022 | 0.0108 |
| 2024_09_20 22:00 | 3242158 | 2 | 9.3642 | 11.8527 | -117.5677 | 16.5748 | 183.3095 | 0.0139 | 0.0085 |
| 2024_09_20 22:00 | 3263622 | 3 | 6.9890 | 16.1413 | -117.2461 | 6.2955 | 184.8079 | 0.0122 | 0.0022 |
| 2024_09_20 22:00 | 3247890 | 4 | 10.5865 | 6.4197 | -114.6314 | 9.6701 | 157.5198 | 0.0122 | 0.0103 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414406_1AFA136B | 504990 | 651 | -89.8 | 504990 | 1005 | -92.0 | 504990 | 502 | -97.9 | 504990 | 32 |
| MR_1774414406_35C7D18C | 504990 | 651 | -89.4 | 504990 | 1005 | -91.4 | 504990 | 502 | -98.0 | 504990 | 32 |
| MR_1774414406_18656F67 | 504990 | 651 | -88.7 | 504990 | 1005 | -91.4 | 504990 | 502 | -98.1 | 504990 | 32 |
| MR_1774414406_4A8F8C83 | 504990 | 651 | -87.5 | 504990 | 1005 | -90.4 | 504990 | 502 | -98.2 | 504990 | 32 |
| MR_1774414406_8D496066 | 504990 | 651 | -89.4 | 504990 | 1005 | -89.8 | 504990 | 502 | -96.1 | 504990 | 32 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 978: `8c98631d-49d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8c98631d-49da-4c7f-b5a0-3e0debe13f37` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Add neighbor relationship between 3217138_4 and 3212289_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[978] topology](images/train_0978.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3217138_4 by 10 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Add neighbor relationship between 3217138_4 and 3212289_3 **← 정답**
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212289_3
- `C5`: Add neighbor relationship between 3275537_2 and 3212289_3
- `C6`: Increase A3 Offset threshold for 3212289_3
- `C7`: Decrease A3 Offset threshold for 3217138_4
- `C8`: Lift the tilt angle of 3217138_4 by 10 degrees
- `C9`: Adjust the azimuth of 3217138_4 by 50 degrees
- `C10`: Increase A3 Offset threshold for 3217138_4
- `C11`: Decrease transmission power for 3217138_4
- `C12`: Check test server and transmission issues
- `C13`: Decrease transmission power for 3212289_3
- `C14`: Decrease A3 Offset threshold for 3212289_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212289_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217138_4
- `C17`: Press down the tilt angle  of 3212289_3 by 6 degrees
- `C18`: Adjust the azimuth of 3212289_3 by 34 degrees
- `C19`: Lift the tilt angle  of 3212289_3 by 6 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217138_4
- `C21`: Increase transmission power for 3212289_3
- `C22`: Increase transmission power for 3217138_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.884 | MS1 | 121.4656746100 | 31.1446317952 | 46 | 504990 | -83.64 | 16.25 | 344.00 | 0.18 | 2.06 | 1563 |
| 2024-09-20 22:21:32.597 | MS1 | 121.4656712465 | 31.1446229391 | 46 | 504990 | -76.02 | 15.30 | 479.14 | 0.04 | 2.92 | 1584 |
| 2024-09-20 22:21:33.127 | MS1 | 121.4656711287 | 31.1446289134 | 46 | 504990 | -81.89 | 12.12 | 499.41 | 0.06 | 2.94 | 1587 |
| 2024-09-20 22:21:34.843 | MS1 | 121.4656647955 | 31.1446242294 | 46 | 504990 | -90.30 | -1.23 | 66.81 | 0.13 | 1.35 | 1576 |
| 2024-09-20 22:21:35.736 | MS1 | 121.4656580174 | 31.1446361934 | 46 | 504990 | -94.58 | -1.74 | 38.37 | 0.17 | 1.28 | 1578 |
| 2024-09-20 22:21:36.879 | MS1 | 121.4656686256 | 31.1446280312 | 46 | 504990 | -86.27 | -0.51 | 49.25 | 0.18 | 1.50 | 1596 |
| 2024-09-20 22:21:37.109 | MS1 | 121.4656595203 | 31.1446232610 | 46 | 504990 | -88.02 | -1.98 | 43.09 | 0.18 | 1.32 | 1586 |
| 2024-09-20 22:21:38.275 | MS1 | 121.4656736201 | 31.1446206645 | 46 | 504990 | -80.35 | 13.23 | 357.73 | 0.05 | 1.25 | 1572 |
| 2024-09-20 22:21:39.521 | MS1 | 121.4656779052 | 31.1446186760 | 46 | 504990 | -83.83 | 13.08 | 304.78 | 0.16 | 1.49 | 1568 |
| 2024-09-20 22:21:40.393 | MS1 | 121.4656695387 | 31.1446288669 | 46 | 504990 | -77.44 | 17.04 | 435.89 | 0.13 | 2.59 | 1593 |
| 2024-09-20 22:21:41.383 | MS1 | 121.4656607438 | 31.1446295083 | 46 | 504990 | -75.07 | 13.24 | 458.55 | 0.20 | 2.35 | 1599 |
| 2024-09-20 22:21:42.690 | MS1 | 121.4656764198 | 31.1446240948 | 46 | 504990 | -79.87 | 12.03 | 558.81 | 0.08 | 2.29 | 1575 |

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
| 3212289 | 3 | 121.4734253781 | 31.1527969864 | 253 | 5 | 6 | 15.2 | TDD | 45 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3217138 | 4 | 121.4667943082 | 31.1500034387 | 12 | 9 | 12 | 42.8 | TDD | 46 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3238306 | 1 | 121.4643561261 | 31.1462869839 | 13 | 3 | 9 | 34.0 | TDD | 416 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3275537 | 2 | 121.4695932387 | 31.1443299905 | 350 | 11 | 12 | 42.5 | TDD | 745 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.926 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.947 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.089 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.089 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.810 | NREventA3 | measId:2;ServCellPCI:781;Se... |
| 2024-09-20 22:21:35.810 | NREventA3 | measId:2;ServCellPCI:781;Se... |
| 2024-09-20 22:21:36.810 | NREventA3 | measId:2;ServCellPCI:781;Se... |
| 2024-09-20 22:21:39.310 | NRRRCReestablishAttempt | PCI:781 |
| 2024-09-20 22:21:39.328 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.338 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.476 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.476 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238306 | 1 | 19.5218 | 12.4324 | -117.7293 | 19.2721 | 185.4691 | 0.0059 | 0.0172 |
| 2024_09_20 22:00 | 3275537 | 2 | 9.6311 | 6.3616 | -115.8165 | 8.9815 | 111.6198 | 0.0072 | 0.0126 |
| 2024_09_20 22:00 | 3212289 | 3 | 11.3514 | 8.6351 | -117.7751 | 6.8191 | 91.4716 | 0.0024 | 0.0022 |
| 2024_09_20 22:00 | 3217138 | 4 | 18.0886 | 8.0480 | -114.4142 | 17.5357 | 171.7892 | 0.0142 | 0.1686 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412022_766291DD | 504990 | 46 | -92.1 | 504990 | 45 | -84.4 | 504990 | 745 | -88.3 | 504990 | 416 |
| MR_1774412022_BC3A2D03 | 504990 | 46 | -91.1 | 504990 | 45 | -85.9 | 504990 | 745 | -88.1 | 504990 | 416 |
| MR_1774412022_DF5814C7 | 504990 | 46 | -89.8 | 504990 | 45 | -87.0 | 504990 | 745 | -88.0 | 504990 | 416 |
| MR_1774412022_E87C8FB9 | 504990 | 46 | -91.3 | 504990 | 45 | -83.2 | 504990 | 745 | -88.0 | 504990 | 416 |
| MR_1774412022_5D701D4C | 504990 | 45 | -84.0 | 504990 | 46 | -92.1 | 504990 | 745 | -90.1 | 504990 | 416 |
| MR_1774412022_7BEB8756 | 504990 | 46 | -88.3 | 504990 | 45 | -85.2 | 504990 | 745 | -88.9 | 504990 | 416 |
| MR_1774412022_3F18D4B8 | 504990 | 46 | -88.6 | 504990 | 45 | -86.0 | 504990 | 745 | -88.4 | 504990 | 416 |
| MR_1774412022_FA32688A | 504990 | 46 | -89.3 | 504990 | 45 | -86.0 | 504990 | 745 | -89.6 | 504990 | 416 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 979: `acceaf16-ea3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `acceaf16-ea35-4e6a-a304-57a1340a97f5` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[979] topology](images/train_0979.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219524_3
- `C2`: Lift the tilt angle  of 3219524_3 by 5 degrees
- `C3`: Decrease A3 Offset threshold for 3250956_4
- `C4`: Decrease transmission power for 3219524_3
- `C5`: Increase A3 Offset threshold for 3219524_3
- `C6`: Lift the tilt angle of 3250956_4 by 4 degrees
- `C7`: Check test server and transmission issues **← 정답**
- `C8`: Add neighbor relationship between 3256428_2 and 3219524_3
- `C9`: Press down the tilt angle  of 3219524_3 by 5 degrees
- `C10`: Adjust the azimuth of 3219524_3 by 50 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219524_3
- `C13`: Decrease transmission power for 3250956_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250956_4
- `C15`: Decrease A3 Offset threshold for 3219524_3
- `C16`: Increase transmission power for 3250956_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250956_4
- `C18`: Add neighbor relationship between 3250956_4 and 3219524_3
- `C19`: Increase A3 Offset threshold for 3250956_4
- `C20`: Increase transmission power for 3219524_3
- `C21`: Adjust the azimuth of 3250956_4 by 50 degrees
- `C22`: Press down the tilt angle of 3250956_4 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.767 | MS1 | 121.4656595620 | 31.1446201360 | 111 | 504990 | -85.43 | 17.47 | 506.39 | 0.04 | 2.84 | 1575 |
| 2024-09-20 22:21:32.257 | MS1 | 121.4656580974 | 31.1446244591 | 111 | 504990 | -85.29 | 13.33 | 492.58 | 0.18 | 2.86 | 1572 |
| 2024-09-20 22:21:33.980 | MS1 | 121.4656712294 | 31.1446336110 | 111 | 504990 | -89.37 | 15.43 | 431.95 | 0.13 | 2.35 | 1560 |
| 2024-09-20 22:21:34.472 | MS1 | 121.4656691442 | 31.1446245297 | 111 | 504990 | -85.76 | 14.47 | 86.42 | 0.12 | 2.26 | 349 |
| 2024-09-20 22:21:35.737 | MS1 | 121.4656589895 | 31.1446246509 | 111 | 504990 | -89.67 | 17.57 | 51.95 | 0.09 | 2.64 | 467 |
| 2024-09-20 22:21:36.819 | MS1 | 121.4656598395 | 31.1446261123 | 111 | 504990 | -88.61 | 17.07 | 60.70 | 0.13 | 2.41 | 324 |
| 2024-09-20 22:21:37.429 | MS1 | 121.4656754095 | 31.1446336941 | 111 | 504990 | -92.54 | 8.25 | 91.75 | 0.17 | 2.01 | 328 |
| 2024-09-20 22:21:38.190 | MS1 | 121.4656776413 | 31.1446304201 | 111 | 504990 | -90.98 | 8.68 | 95.46 | 0.19 | 2.63 | 314 |
| 2024-09-20 22:21:39.973 | MS1 | 121.4656706232 | 31.1446200093 | 111 | 504990 | -93.74 | 10.75 | 96.87 | 0.18 | 2.03 | 426 |
| 2024-09-20 22:21:40.515 | MS1 | 121.4656689793 | 31.1446202115 | 111 | 504990 | -91.85 | 9.45 | 358.83 | 0.00 | 2.26 | 1597 |
| 2024-09-20 22:21:41.324 | MS1 | 121.4656719509 | 31.1446343311 | 111 | 504990 | -92.50 | 8.44 | 403.27 | 0.17 | 2.77 | 1590 |
| 2024-09-20 22:21:42.812 | MS1 | 121.4656721101 | 31.1446180680 | 111 | 504990 | -92.72 | 7.53 | 350.86 | 0.02 | 2.20 | 1595 |

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
| 3219524 | 3 | 121.4701729860 | 31.1550293338 | 285 | 3 | 8 | 45.4 | TDD | 756 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3240389 | 1 | 121.4698052784 | 31.1458497663 | 197 | 14 | 10 | 37.7 | TDD | 208 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3250956 | 4 | 121.4680598408 | 31.1473972185 | 111 | 1 | 10 | 23.0 | TDD | 111 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3256428 | 2 | 121.4741017209 | 31.1457566327 | 348 | 1 | 7 | 43.7 | TDD | 675 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.742 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.762 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.872 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.872 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.631 | NREventA3 | measId:2;ServCellPCI:243;Se... |
| 2024-09-20 22:21:37.871 | NRHandoverAttempt | SourcePCI:243;SourceNR-ARFC... |
| 2024-09-20 22:21:37.909 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.920 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.029 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.029 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240389 | 1 | 5.9198 | 19.8119 | -115.6772 | 14.5753 | 185.2003 | 0.0020 | 0.0046 |
| 2024_09_20 22:00 | 3256428 | 2 | 15.3237 | 18.4630 | -115.6299 | 13.9667 | 86.0421 | 0.0119 | 0.0180 |
| 2024_09_20 22:00 | 3219524 | 3 | 12.4650 | 14.9620 | -115.9399 | 10.0470 | 121.0298 | 0.0184 | 0.0032 |
| 2024_09_20 22:00 | 3250956 | 4 | 11.3799 | 11.1328 | -116.6540 | 12.4437 | 159.3873 | 0.0144 | 0.0141 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414930_E3703F7C | 504990 | 111 | -85.7 | 504990 | 756 | -89.2 | 504990 | 675 | -93.3 | 504990 | 208 |
| MR_1774414930_2B357DA2 | 504990 | 111 | -83.8 | 504990 | 756 | -89.3 | 504990 | 675 | -95.3 | 504990 | 208 |
| MR_1774414930_48F4EB17 | 504990 | 111 | -86.6 | 504990 | 756 | -90.6 | 504990 | 675 | -94.4 | 504990 | 208 |
| MR_1774414930_1B2A30B5 | 504990 | 111 | -85.5 | 504990 | 756 | -88.7 | 504990 | 675 | -92.7 | 504990 | 208 |
| MR_1774414930_8B4952F8 | 504990 | 111 | -85.0 | 504990 | 756 | -88.9 | 504990 | 675 | -92.8 | 504990 | 208 |
| MR_1774414930_602F23BB | 504990 | 111 | -86.5 | 504990 | 756 | -89.5 | 504990 | 675 | -94.6 | 504990 | 208 |
| MR_1774414930_2EF319B0 | 504990 | 111 | -85.5 | 504990 | 756 | -88.8 | 504990 | 675 | -92.7 | 504990 | 208 |
| MR_1774414930_AADA56B3 | 504990 | 111 | -83.9 | 504990 | 756 | -90.9 | 504990 | 675 | -95.4 | 504990 | 208 |

> *... 2개 열 생략 (전체 14열)*

---
