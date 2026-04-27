# Track A 문제 분석 — train[350]~train[359]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[350] ~ train[359] (10개)

## 목차

1. [문제 350: `fa40100c-c18...`](#350) — single-answer, 정답: C20
2. [문제 351: `1d03b971-95b...`](#351) — single-answer, 정답: C11
3. [문제 352: `5c9d1eba-6ea...`](#352) — single-answer, 정답: C20
4. [문제 353: `a37e4edf-0a9...`](#353) — single-answer, 정답: C12
5. [문제 354: `3b980ed9-eef...`](#354) — single-answer, 정답: C14
6. [문제 355: `4efbe83e-495...`](#355) — single-answer, 정답: C3
7. [문제 356: `2322d4b4-173...`](#356) — single-answer, 정답: C15
8. [문제 357: `b7234b65-d53...`](#357) — single-answer, 정답: C22
9. [문제 358: `0e6b6e18-3e5...`](#358) — single-answer, 정답: C5
10. [문제 359: `6f201387-3d5...`](#359) — single-answer, 정답: C5

---

### 문제 350: `fa40100c-c18...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fa40100c-c186-40c9-81b3-d84d5d81ef2d` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Lift the tilt angle  of 3277898_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[350] topology](images/train_0350.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3275966_4
- `C2`: Decrease A3 Offset threshold for 3225706_1
- `C3`: Add neighbor relationship between 3277898_3 and 3225706_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225706_1
- `C5`: Press down the tilt angle of 3275966_4 by 4 degrees
- `C6`: Increase A3 Offset threshold for 3225706_1
- `C7`: Increase transmission power for 3225706_1
- `C8`: Increase transmission power for 3275966_4
- `C9`: Add neighbor relationship between 3275966_4 and 3225706_1
- `C10`: Lift the tilt angle of 3275966_4 by 4 degrees
- `C11`: Adjust the azimuth of 3277898_3 by 50 degrees
- `C12`: Adjust the azimuth of 3275966_4 by 11 degrees
- `C13`: Press down the tilt angle  of 3277898_3 by 10 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225706_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275966_4
- `C17`: Check test server and transmission issues
- `C18`: Decrease transmission power for 3225706_1
- `C19`: Increase A3 Offset threshold for 3275966_4
- `C20`: Lift the tilt angle  of 3277898_3 by 10 degrees **← 정답**
- `C21`: Decrease transmission power for 3275966_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275966_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.870 | MS1 | 121.4656637822 | 31.1446250268 | 286 | 504990 | -89.18 | 17.83 | 495.24 | 0.06 | 2.98 | 1566 |
| 2024-09-20 22:21:32.413 | MS1 | 121.4656731691 | 31.1446339737 | 286 | 504990 | -86.04 | 15.81 | 444.16 | 0.15 | 2.64 | 1579 |
| 2024-09-20 22:21:33.235 | MS1 | 121.4656672052 | 31.1446285274 | 286 | 504990 | -91.05 | 12.06 | 439.75 | 0.06 | 2.76 | 1580 |
| 2024-09-20 22:21:34.286 | MS1 | 121.4656606064 | 31.1446260504 | 286 | 504990 | -85.65 | 16.84 | 85.30 | 0.03 | 2.81 | 1562 |
| 2024-09-20 22:21:35.752 | MS1 | 121.4656731459 | 31.1446248744 | 286 | 504990 | -90.92 | 17.25 | 92.44 | 0.09 | 2.60 | 1594 |
| 2024-09-20 22:21:36.835 | MS1 | 121.4656629035 | 31.1446325092 | 286 | 504990 | -88.50 | 16.95 | 86.22 | 0.01 | 2.45 | 1572 |
| 2024-09-20 22:21:37.647 | MS1 | 121.4656687290 | 31.1446315536 | 286 | 504990 | -90.30 | 8.03 | 61.79 | 0.11 | 2.79 | 1582 |
| 2024-09-20 22:21:38.357 | MS1 | 121.4656694346 | 31.1446341900 | 286 | 504990 | -92.87 | 7.02 | 100.27 | 0.03 | 2.51 | 1580 |
| 2024-09-20 22:21:39.608 | MS1 | 121.4656693751 | 31.1446316417 | 286 | 504990 | -92.72 | 8.96 | 52.90 | 0.15 | 2.35 | 1582 |
| 2024-09-20 22:21:40.913 | MS1 | 121.4656613392 | 31.1446224737 | 286 | 504990 | -92.91 | 8.37 | 462.54 | 0.06 | 2.11 | 1589 |
| 2024-09-20 22:21:41.775 | MS1 | 121.4656644872 | 31.1446372147 | 286 | 504990 | -93.62 | 12.07 | 421.15 | 0.16 | 2.52 | 1590 |
| 2024-09-20 22:21:42.132 | MS1 | 121.4656671521 | 31.1446338396 | 286 | 504990 | -92.87 | 8.86 | 322.66 | 0.05 | 2.12 | 1587 |

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
| 3225706 | 1 | 121.4700168029 | 31.1549403342 | 358 | 12 | 10 | 42.2 | TDD | 457 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3270525 | 2 | 121.4709322528 | 31.1493642770 | 1 | 4 | 1 | 30.4 | TDD | 681 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3275966 | 4 | 121.4666522472 | 31.1486847786 | 203 | 0 | 1 | 30.7 | TDD | 286 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3277898 | 3 | 121.4751652187 | 31.1462910540 | 34 | 11 | 9 | 48.4 | TDD | 956 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.060 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.081 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.194 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.194 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.914 | NREventA3 | measId:2;ServCellPCI:376;Se... |
| 2024-09-20 22:21:38.154 | NRHandoverAttempt | SourcePCI:376;SourceNR-ARFC... |
| 2024-09-20 22:21:38.184 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.198 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.328 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.328 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225706 | 1 | 18.7331 | 18.5320 | -117.8472 | 16.1726 | 189.4374 | 0.0189 | 0.0004 |
| 2024_09_20 22:00 | 3270525 | 2 | 10.4682 | 16.8372 | -117.7453 | 19.2907 | 179.1950 | 0.0182 | 0.0150 |
| 2024_09_20 22:00 | 3277898 | 3 | 9.8968 | 10.3332 | -116.4769 | 11.1867 | 154.5119 | 0.0136 | 0.0071 |
| 2024_09_20 22:00 | 3275966 | 4 | 83.9844 | 92.0370 | -117.8809 | 9.0677 | 133.8457 | 0.0181 | 0.0157 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416676_1FFC9800 | 504990 | 286 | -84.2 | 504990 | 457 | -89.5 | 504990 | 956 | -97.9 | 504990 | 681 |
| MR_1774416676_6B96698E | 504990 | 286 | -86.0 | 504990 | 457 | -88.9 | 504990 | 956 | -95.4 | 504990 | 681 |
| MR_1774416676_1D8E17F9 | 504990 | 286 | -84.2 | 504990 | 457 | -90.8 | 504990 | 956 | -96.7 | 504990 | 681 |
| MR_1774416676_27BAD667 | 504990 | 286 | -85.3 | 504990 | 457 | -89.5 | 504990 | 956 | -97.8 | 504990 | 681 |
| MR_1774416676_93F3EF0B | 504990 | 286 | -87.0 | 504990 | 457 | -90.4 | 504990 | 956 | -96.7 | 504990 | 681 |
| MR_1774416676_DD94A41E | 504990 | 286 | -87.4 | 504990 | 457 | -87.9 | 504990 | 956 | -97.7 | 504990 | 681 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 351: `1d03b971-95b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1d03b971-95b5-4c20-a3a1-98e9b5722635` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[351] topology](images/train_0351.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3247992_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247992_3
- `C3`: Add neighbor relationship between 3272408_4 and 3247992_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272408_4
- `C5`: Decrease A3 Offset threshold for 3247992_3
- `C6`: Increase A3 Offset threshold for 3272408_4
- `C7`: Lift the tilt angle of 3272408_4 by 9 degrees
- `C8`: Decrease transmission power for 3272408_4
- `C9`: Increase transmission power for 3247992_3
- `C10`: Press down the tilt angle  of 3247992_3 by 3 degrees
- `C11`: Insufficient data; more data is needed for judgment. **← 정답**
- `C12`: Adjust the azimuth of 3247992_3 by 45 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247992_3
- `C14`: Lift the tilt angle  of 3247992_3 by 3 degrees
- `C15`: Press down the tilt angle of 3272408_4 by 9 degrees
- `C16`: Adjust the azimuth of 3272408_4 by 50 degrees
- `C17`: Check test server and transmission issues
- `C18`: Decrease A3 Offset threshold for 3272408_4
- `C19`: Add neighbor relationship between 3224395_1 and 3247992_3
- `C20`: Increase transmission power for 3272408_4
- `C21`: Decrease transmission power for 3247992_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272408_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.556 | MS1 | 121.4656603174 | 31.1446342566 | 679 | 504990 | -87.43 | 16.09 | 449.85 | 0.03 | 2.02 | 1564 |
| 2024-09-20 22:21:32.966 | MS1 | 121.4656604996 | 31.1446320260 | 679 | 504990 | -86.06 | 15.07 | 350.48 | 0.15 | 2.69 | 1585 |
| 2024-09-20 22:21:33.686 | MS1 | 121.4656594928 | 31.1446226939 | 679 | 504990 | -86.00 | 17.61 | 395.98 | 0.20 | 2.90 | 1584 |
| 2024-09-20 22:21:34.659 | MS1 | 121.4656764746 | 31.1446354832 | 679 | 504990 | -89.06 | 13.41 | 99.77 | 0.05 | 2.83 | 1566 |
| 2024-09-20 22:21:35.656 | MS1 | 121.4656637687 | 31.1446262970 | 679 | 504990 | -91.53 | 14.84 | 80.43 | 0.17 | 2.51 | 1588 |
| 2024-09-20 22:21:36.117 | MS1 | 121.4656599131 | 31.1446265987 | 679 | 504990 | -91.23 | 13.25 | 65.55 | 0.10 | 2.13 | 1589 |
| 2024-09-20 22:21:37.647 | MS1 | 121.4656747953 | 31.1446234143 | 679 | 504990 | -89.97 | 12.64 | 79.40 | 0.18 | 2.73 | 1563 |
| 2024-09-20 22:21:38.620 | MS1 | 121.4656641616 | 31.1446356818 | 679 | 504990 | -91.45 | 9.23 | 66.08 | 0.10 | 2.74 | 1573 |
| 2024-09-20 22:21:39.402 | MS1 | 121.4656628331 | 31.1446368539 | 679 | 504990 | -93.45 | 8.73 | 70.70 | 0.11 | 2.24 | 1577 |
| 2024-09-20 22:21:40.174 | MS1 | 121.4656669930 | 31.1446337838 | 679 | 504990 | -91.07 | 7.15 | 533.30 | 0.16 | 2.35 | 1587 |
| 2024-09-20 22:21:41.815 | MS1 | 121.4656708822 | 31.1446362910 | 679 | 504990 | -93.53 | 9.63 | 398.15 | 0.18 | 2.95 | 1567 |
| 2024-09-20 22:21:42.331 | MS1 | 121.4656749415 | 31.1446379648 | 679 | 504990 | -89.85 | 11.19 | 469.83 | 0.01 | 2.09 | 1593 |

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
| 3224395 | 1 | 121.4653568879 | 31.1491527888 | 140 | 9 | 12 | 20.6 | TDD | 793 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3247992 | 3 | 121.4659579532 | 31.1487752416 | 229 | 0 | 12 | 27.3 | TDD | 156 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3267462 | 2 | 121.4675472873 | 31.1495582923 | 35 | 4 | 5 | 45.5 | TDD | 665 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3272408 | 4 | 121.4739432665 | 31.1450262178 | 81 | 5 | 11 | 49.0 | TDD | 679 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.918 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.938 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.078 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.078 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.795 | NREventA3 | measId:2;ServCellPCI:961;Se... |
| 2024-09-20 22:21:38.035 | NRHandoverAttempt | SourcePCI:961;SourceNR-ARFC... |
| 2024-09-20 22:21:38.080 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.093 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.243 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.243 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3224395 | 1 | 84.4514 | 78.7239 | -115.1092 | 9.5809 | 191.9949 | 0.0027 | 0.0149 |
| 2024_09_19 22:00 | 3267462 | 2 | 81.1202 | 75.5964 | -115.2339 | 9.7921 | 182.9754 | 0.0035 | 0.0085 |
| 2024_09_19 22:00 | 3247992 | 3 | 76.4532 | 77.7646 | -115.4107 | 17.3190 | 146.5447 | 0.0088 | 0.0120 |
| 2024_09_19 22:00 | 3272408 | 4 | 76.4311 | 79.1982 | -116.2768 | 7.7325 | 193.3602 | 0.0024 | 0.0108 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412630_8FDADDAD | 504990 | 679 | -88.4 | 504990 | 156 | -94.8 | 504990 | 793 | -97.0 | 504990 | 665 |
| MR_1774412630_802C0AE8 | 504990 | 679 | -87.7 | 504990 | 156 | -93.8 | 504990 | 793 | -96.1 | 504990 | 665 |
| MR_1774412630_E87B39B5 | 504990 | 679 | -88.9 | 504990 | 156 | -93.0 | 504990 | 793 | -98.9 | 504990 | 665 |
| MR_1774412630_C74A7F56 | 504990 | 679 | -87.1 | 504990 | 156 | -91.2 | 504990 | 793 | -97.0 | 504990 | 665 |
| MR_1774412630_9E24B2B3 | 504990 | 679 | -89.6 | 504990 | 156 | -91.8 | 504990 | 793 | -97.8 | 504990 | 665 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 352: `5c9d1eba-6ea...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5c9d1eba-6ea3-4da8-8d3f-46652073388e` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[352] topology](images/train_0352.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3273008_4 by 3 degrees
- `C2`: Press down the tilt angle of 3214326_2 by 9 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273008_4
- `C4`: Increase transmission power for 3214326_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214326_2
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Add neighbor relationship between 3230544_1 and 3273008_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273008_4
- `C9`: Decrease transmission power for 3273008_4
- `C10`: Decrease transmission power for 3214326_2
- `C11`: Increase A3 Offset threshold for 3214326_2
- `C12`: Lift the tilt angle of 3214326_2 by 9 degrees
- `C13`: Lift the tilt angle  of 3273008_4 by 3 degrees
- `C14`: Adjust the azimuth of 3273008_4 by 9 degrees
- `C15`: Increase transmission power for 3273008_4
- `C16`: Add neighbor relationship between 3214326_2 and 3273008_4
- `C17`: Adjust the azimuth of 3214326_2 by 50 degrees
- `C18`: Decrease A3 Offset threshold for 3214326_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214326_2
- `C20`: Check test server and transmission issues **← 정답**
- `C21`: Increase A3 Offset threshold for 3273008_4
- `C22`: Decrease A3 Offset threshold for 3273008_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.606 | MS1 | 121.4656657340 | 31.1446303350 | 386 | 504990 | -85.49 | 12.99 | 375.03 | 0.06 | 2.82 | 1561 |
| 2024-09-20 22:21:32.500 | MS1 | 121.4656647454 | 31.1446333172 | 386 | 504990 | -87.91 | 12.78 | 497.84 | 0.16 | 2.99 | 1574 |
| 2024-09-20 22:21:33.860 | MS1 | 121.4656633208 | 31.1446255376 | 386 | 504990 | -89.64 | 13.58 | 473.52 | 0.05 | 2.90 | 1564 |
| 2024-09-20 22:21:34.181 | MS1 | 121.4656621845 | 31.1446234573 | 386 | 504990 | -89.02 | 15.81 | 84.51 | 0.07 | 2.91 | 466 |
| 2024-09-20 22:21:35.857 | MS1 | 121.4656769689 | 31.1446229003 | 386 | 504990 | -85.88 | 15.34 | 69.79 | 0.04 | 2.30 | 311 |
| 2024-09-20 22:21:36.580 | MS1 | 121.4656597330 | 31.1446252313 | 386 | 504990 | -90.93 | 13.99 | 56.74 | 0.08 | 2.66 | 375 |
| 2024-09-20 22:21:37.361 | MS1 | 121.4656764444 | 31.1446354162 | 386 | 504990 | -92.12 | 10.49 | 54.53 | 0.19 | 2.26 | 333 |
| 2024-09-20 22:21:38.899 | MS1 | 121.4656689876 | 31.1446297946 | 386 | 504990 | -89.60 | 11.63 | 47.01 | 0.12 | 2.25 | 302 |
| 2024-09-20 22:21:39.537 | MS1 | 121.4656583329 | 31.1446234298 | 386 | 504990 | -90.51 | 7.90 | 81.36 | 0.04 | 2.40 | 428 |
| 2024-09-20 22:21:40.167 | MS1 | 121.4656618087 | 31.1446375694 | 386 | 504990 | -90.10 | 11.85 | 526.88 | 0.18 | 2.19 | 1565 |
| 2024-09-20 22:21:41.350 | MS1 | 121.4656651938 | 31.1446286344 | 386 | 504990 | -93.36 | 12.61 | 479.22 | 0.00 | 2.04 | 1596 |
| 2024-09-20 22:21:42.758 | MS1 | 121.4656701195 | 31.1446294584 | 386 | 504990 | -90.82 | 10.06 | 584.28 | 0.05 | 2.94 | 1591 |

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
| 3214326 | 2 | 121.4687112625 | 31.1488050527 | 350 | 7 | 6 | 19.1 | TDD | 386 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3230544 | 1 | 121.4742945758 | 31.1487371029 | 233 | 15 | 8 | 21.1 | TDD | 705 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3232090 | 3 | 121.4672863293 | 31.1536204377 | 146 | 14 | 7 | 45.2 | TDD | 948 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3273008 | 4 | 121.4671578907 | 31.1535998335 | 179 | 1 | 4 | 39.1 | TDD | 663 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.258 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.276 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.387 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.387 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.146 | NREventA3 | measId:2;ServCellPCI:979;Se... |
| 2024-09-20 22:21:38.386 | NRHandoverAttempt | SourcePCI:979;SourceNR-ARFC... |
| 2024-09-20 22:21:38.425 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.440 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.586 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.586 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230544 | 1 | 10.2767 | 17.3613 | -117.7784 | 9.7354 | 133.3586 | 0.0017 | 0.0100 |
| 2024_09_20 22:00 | 3214326 | 2 | 6.4456 | 7.7876 | -116.7070 | 7.3214 | 80.2809 | 0.0089 | 0.0135 |
| 2024_09_20 22:00 | 3232090 | 3 | 10.9678 | 19.7392 | -116.7470 | 19.0299 | 106.8272 | 0.0040 | 0.0028 |
| 2024_09_20 22:00 | 3273008 | 4 | 16.2906 | 15.5317 | -116.9083 | 10.2382 | 120.0385 | 0.0195 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416298_0632E035 | 504990 | 386 | -88.9 | 504990 | 663 | -88.5 | 504990 | 705 | -98.5 | 504990 | 948 |
| MR_1774416298_01E39DA9 | 504990 | 386 | -91.0 | 504990 | 663 | -90.9 | 504990 | 705 | -99.8 | 504990 | 948 |
| MR_1774416298_C7815AB9 | 504990 | 386 | -90.5 | 504990 | 663 | -88.4 | 504990 | 705 | -99.0 | 504990 | 948 |
| MR_1774416298_949908C6 | 504990 | 386 | -87.2 | 504990 | 663 | -90.9 | 504990 | 705 | -101.7 | 504990 | 948 |
| MR_1774416298_FA81F14C | 504990 | 386 | -90.4 | 504990 | 663 | -91.8 | 504990 | 705 | -101.4 | 504990 | 948 |
| MR_1774416298_78476805 | 504990 | 386 | -89.3 | 504990 | 663 | -90.5 | 504990 | 705 | -101.0 | 504990 | 948 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 353: `a37e4edf-0a9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a37e4edf-0a92-4d3c-a145-37b711c7d8c3` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3261823_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[353] topology](images/train_0353.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248478_2
- `C2`: Press down the tilt angle  of 3248478_2 by 10 degrees
- `C3`: Check test server and transmission issues
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261823_4
- `C5`: Increase A3 Offset threshold for 3261823_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease A3 Offset threshold for 3248478_2
- `C8`: Adjust the azimuth of 3248478_2 by 50 degrees
- `C9`: Increase A3 Offset threshold for 3248478_2
- `C10`: Press down the tilt angle of 3261823_4 by 2 degrees
- `C11`: Increase transmission power for 3248478_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261823_4 **← 정답**
- `C13`: Add neighbor relationship between 3261823_4 and 3248478_2
- `C14`: Adjust the azimuth of 3261823_4 by 8 degrees
- `C15`: Decrease transmission power for 3261823_4
- `C16`: Add neighbor relationship between 3230653_1 and 3248478_2
- `C17`: Increase transmission power for 3261823_4
- `C18`: Lift the tilt angle of 3261823_4 by 2 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248478_2
- `C20`: Lift the tilt angle  of 3248478_2 by 10 degrees
- `C21`: Decrease transmission power for 3248478_2
- `C22`: Decrease A3 Offset threshold for 3261823_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.559 | MS1 | 121.4656590540 | 31.1446358449 | 260 | 504990 | -86.68 | 14.85 | 317.09 | 0.06 | 2.63 | 1581 |
| 2024-09-20 22:21:32.594 | MS1 | 121.4656690989 | 31.1446287665 | 260 | 504990 | -88.21 | 13.91 | 426.31 | 0.11 | 2.45 | 1561 |
| 2024-09-20 22:21:33.612 | MS1 | 121.4656751365 | 31.1446242798 | 260 | 504990 | -88.60 | 16.42 | 391.96 | 0.15 | 2.13 | 1570 |
| 2024-09-20 22:21:34.706 | MS1 | 121.4656668971 | 31.1446352249 | 260 | 504990 | -90.97 | 15.18 | 96.25 | 0.66 | 2.80 | 666 |
| 2024-09-20 22:21:35.200 | MS1 | 121.4656752520 | 31.1446251502 | 260 | 504990 | -87.51 | 13.32 | 99.45 | 0.70 | 2.84 | 683 |
| 2024-09-20 22:21:36.934 | MS1 | 121.4656681593 | 31.1446348522 | 260 | 504990 | -88.98 | 14.24 | 53.34 | 0.59 | 2.63 | 551 |
| 2024-09-20 22:21:37.588 | MS1 | 121.4656705994 | 31.1446249110 | 260 | 504990 | -93.05 | 12.08 | 92.56 | 0.54 | 2.20 | 504 |
| 2024-09-20 22:21:38.204 | MS1 | 121.4656709275 | 31.1446225607 | 260 | 504990 | -89.34 | 10.13 | 62.77 | 0.68 | 2.26 | 628 |
| 2024-09-20 22:21:39.771 | MS1 | 121.4656742880 | 31.1446328710 | 260 | 504990 | -90.19 | 11.69 | 63.88 | 0.52 | 2.64 | 561 |
| 2024-09-20 22:21:40.616 | MS1 | 121.4656687145 | 31.1446310686 | 260 | 504990 | -91.51 | 12.13 | 477.79 | 0.07 | 2.77 | 1581 |
| 2024-09-20 22:21:41.423 | MS1 | 121.4656757686 | 31.1446334795 | 260 | 504990 | -90.22 | 10.25 | 395.97 | 0.17 | 2.97 | 1568 |
| 2024-09-20 22:21:42.707 | MS1 | 121.4656678545 | 31.1446289690 | 260 | 504990 | -93.54 | 8.01 | 566.62 | 0.06 | 2.50 | 1594 |

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
| 3230653 | 1 | 121.4711102118 | 31.1496816797 | 130 | 6 | 8 | 21.9 | TDD | 112 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3248478 | 2 | 121.4694520646 | 31.1550780147 | 352 | 11 | 4 | 22.0 | TDD | 993 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3261823 | 4 | 121.4746855991 | 31.1552774957 | 224 | 1 | 12 | 37.2 | TDD | 260 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3268903 | 3 | 121.4748951505 | 31.1447452017 | 320 | 10 | 1 | 47.5 | TDD | 850 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.449 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.470 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.587 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.587 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.251 | NREventA3 | measId:2;ServCellPCI:8;Serv... |
| 2024-09-20 22:21:38.491 | NRHandoverAttempt | SourcePCI:8;SourceNR-ARFCN:... |
| 2024-09-20 22:21:38.536 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.549 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.686 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.686 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230653 | 1 | 19.3882 | 14.2685 | -114.3063 | 6.9189 | 111.2072 | 0.0183 | 0.0049 |
| 2024_09_20 22:00 | 3248478 | 2 | 11.3670 | 5.1822 | -114.7860 | 14.1908 | 126.0764 | 0.0151 | 0.0001 |
| 2024_09_20 22:00 | 3268903 | 3 | 12.5705 | 12.2516 | -116.0937 | 11.0619 | 160.4483 | 0.0028 | 0.0109 |
| 2024_09_20 22:00 | 3261823 | 4 | 13.5803 | 17.6014 | -117.2562 | 6.6724 | 171.9099 | 0.0118 | 0.0135 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416243_ED8B21DE | 504990 | 260 | -92.0 | 504990 | 993 | -92.9 | 504990 | 112 | -103.0 | 504990 | 850 |
| MR_1774416243_030F13E2 | 504990 | 260 | -91.7 | 504990 | 993 | -94.4 | 504990 | 112 | -105.1 | 504990 | 850 |
| MR_1774416243_41C2C2E4 | 504990 | 260 | -92.9 | 504990 | 993 | -94.5 | 504990 | 112 | -103.8 | 504990 | 850 |
| MR_1774416243_F90E0BC3 | 504990 | 260 | -92.8 | 504990 | 993 | -93.8 | 504990 | 112 | -105.0 | 504990 | 850 |
| MR_1774416243_99F1589E | 504990 | 260 | -90.9 | 504990 | 993 | -94.7 | 504990 | 112 | -105.6 | 504990 | 850 |
| MR_1774416243_FA576B8E | 504990 | 260 | -89.3 | 504990 | 993 | -95.9 | 504990 | 112 | -103.5 | 504990 | 850 |
| MR_1774416243_D3C32F91 | 504990 | 260 | -90.0 | 504990 | 993 | -92.3 | 504990 | 112 | -106.3 | 504990 | 850 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 354: `3b980ed9-eef...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3b980ed9-eefa-4723-9d5f-ba8cde85869b` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261453_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[354] topology](images/train_0354.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3217808_5
- `C2`: Decrease transmission power for 3261453_2
- `C3`: Press down the tilt angle of 3261453_2 by 4 degrees
- `C4`: Increase A3 Offset threshold for 3261453_2
- `C5`: Add neighbor relationship between 3261453_2 and 3217808_5
- `C6`: Press down the tilt angle  of 3217808_5 by 4 degrees
- `C7`: Decrease A3 Offset threshold for 3217808_5
- `C8`: Increase transmission power for 3217808_5
- `C9`: Adjust the azimuth of 3261453_2 by 22 degrees
- `C10`: Increase transmission power for 3261453_2
- `C11`: Increase A3 Offset threshold for 3217808_5
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Lift the tilt angle of 3261453_2 by 4 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261453_2 **← 정답**
- `C15`: Lift the tilt angle  of 3217808_5 by 4 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261453_2
- `C17`: Adjust the azimuth of 3217808_5 by 12 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217808_5
- `C19`: Add neighbor relationship between 3262837_8 and 3217808_5
- `C20`: Check test server and transmission issues
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217808_5
- `C22`: Decrease A3 Offset threshold for 3261453_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.767 | MS1 | 121.4656656517 | 31.1446184707 | 940 | 504990 | -94.05 | 9.24 | 362.72 | 0.17 | 2.48 | 1561 |
| 2024-09-20 22:21:32.590 | MS1 | 121.4656776824 | 31.1446336507 | 83 | 504990 | -93.87 | 12.79 | 492.94 | 0.06 | 2.10 | 1585 |
| 2024-09-20 22:21:33.814 | MS1 | 121.4656720092 | 31.1446238922 | 269 | 504990 | -94.20 | 9.39 | 352.05 | 0.06 | 2.79 | 1597 |
| 2024-09-20 22:21:34.465 | MS1 | 121.4656689318 | 31.1446342114 | 814 | 152650 | -90.80 | 5.49 | 95.77 | 0.15 | 1.55 | 953 |
| 2024-09-20 22:21:35.321 | MS1 | 121.4656755290 | 31.1446231278 | 754 | 152650 | -94.20 | 3.07 | 90.85 | 0.03 | 1.96 | 949 |
| 2024-09-20 22:21:36.655 | MS1 | 121.4656594631 | 31.1446336153 | 331 | 152650 | -94.82 | 2.54 | 81.26 | 0.05 | 1.98 | 925 |
| 2024-09-20 22:21:37.108 | MS1 | 121.4656768926 | 31.1446272001 | 912 | 152650 | -87.84 | 7.18 | 67.78 | 0.15 | 1.56 | 960 |
| 2024-09-20 22:21:38.430 | MS1 | 121.4656712154 | 31.1446330139 | 814 | 152650 | -91.65 | 6.14 | 46.63 | 0.16 | 1.55 | 987 |
| 2024-09-20 22:21:39.505 | MS1 | 121.4656643275 | 31.1446367925 | 754 | 152650 | -93.92 | 5.17 | 68.94 | 0.19 | 1.74 | 986 |
| 2024-09-20 22:21:40.111 | MS1 | 121.4656618735 | 31.1446339600 | 331 | 152650 | -91.87 | 5.23 | 67.28 | 0.11 | 2.93 | 1565 |
| 2024-09-20 22:21:41.315 | MS1 | 121.4656704839 | 31.1446187164 | 912 | 152650 | -87.67 | 5.50 | 79.01 | 0.12 | 2.58 | 1598 |
| 2024-09-20 22:21:42.355 | MS1 | 121.4656699797 | 31.1446295316 | 814 | 152650 | -92.70 | 7.51 | 82.67 | 0.01 | 2.40 | 1564 |

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
| 3211729 | 11 | 121.4654766737 | 31.1518598501 | 161 | 10 | 3 | 9.1 | FDD | 912 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3214246 | 1 | 121.4738702411 | 31.1535602185 | 335 | 10 | 6 | 14.8 | TDD | 518 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3215514 | 10 | 121.4710958213 | 31.1474411068 | 10 | 5 | 12 | 12.4 | FDD | 814 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3217808 | 5 | 121.4750925173 | 31.1532139443 | 235 | 4 | 10 | 7.6 | TDD | 564 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3221832 | 12 | 121.4698816740 | 31.1457915115 | 190 | 10 | 9 | 23.1 | FDD | 754 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3223518 | 3 | 121.4687660582 | 31.1452797941 | 121 | 10 | 9 | 5.8 | TDD | 269 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3229858 | 6 | 121.4646126769 | 31.1466519643 | 246 | 11 | 3 | 21.7 | TDD | 407 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3255918 | 7 | 121.4659990684 | 31.1556950255 | 251 | 14 | 4 | 28.0 | FDD | 608 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3261453 | 2 | 121.4721099601 | 31.1492309378 | 252 | 2 | 7 | 26.4 | TDD | 940 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3262837 | 8 | 121.4705465865 | 31.1517193568 | 184 | 2 | 0 | 17.7 | FDD | 331 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3267569 | 9 | 121.4646881711 | 31.1520555885 | 178 | 14 | 0 | 21.8 | FDD | 301 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3269880 | 13 | 121.4709722217 | 31.1528507350 | 292 | 11 | 2 | 20.0 | FDD | 218 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3277177 | 4 | 121.4695590053 | 31.1460415815 | 116 | 9 | 11 | 2.2 | TDD | 83 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.347 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.366 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.485 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.485 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.221 | NREventA2 | measId:1;ServCellPCI:823;Se... |
| 2024-09-20 22:21:35.370 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.639 | NREventA5 | measId:3;ServCellPCI:823;Se... |
| 2024-09-20 22:21:35.683 | NRHandoverAttempt | SourcePCI:823;SourceNR-ARFC... |
| 2024-09-20 22:21:35.720 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.732 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.835 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.835 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214246 | 1 | 6.7095 | 17.4936 | -115.8803 | 7.6904 | 178.6444 | 0.0074 | 0.0063 |
| 2024_09_20 22:00 | 3261453 | 2 | 9.7761 | 19.2266 | -116.0449 | 9.2748 | 123.9651 | 0.0066 | 0.0167 |
| 2024_09_20 22:00 | 3223518 | 3 | 12.9179 | 10.8016 | -116.1303 | 13.2861 | 104.6079 | 0.0035 | 0.0012 |
| 2024_09_20 22:00 | 3277177 | 4 | 12.8156 | 10.7038 | -114.5181 | 15.2219 | 112.1109 | 0.0063 | 0.0085 |
| 2024_09_20 22:00 | 3217808 | 5 | 9.8187 | 17.6117 | -116.7212 | 15.7286 | 147.0993 | 0.0178 | 0.0189 |
| 2024_09_20 22:00 | 3229858 | 6 | 10.8533 | 19.0352 | -114.2475 | 11.7098 | 83.8976 | 0.0120 | 0.0058 |
| 2024_09_20 22:00 | 3255918 | 7 | 7.5864 | 16.7003 | -116.2780 | 4.6398 | 30.2600 | 0.0094 | 0.0015 |
| 2024_09_20 22:00 | 3262837 | 8 | 12.5515 | 11.0921 | -116.4754 | 4.2796 | 29.4740 | 0.0021 | 0.0175 |
| 2024_09_20 22:00 | 3267569 | 9 | 13.9895 | 19.7701 | -116.6439 | 3.1424 | 24.7872 | 0.0079 | 0.0044 |
| 2024_09_20 22:00 | 3215514 | 10 | 18.7057 | 6.9972 | -115.4745 | 3.6192 | 28.9245 | 0.0062 | 0.0186 |
| 2024_09_20 22:00 | 3211729 | 11 | 19.2529 | 18.2885 | -116.3544 | 3.2843 | 27.6807 | 0.0058 | 0.0108 |
| 2024_09_20 22:00 | 3221832 | 12 | 16.9412 | 6.3066 | -115.2537 | 3.3109 | 58.0633 | 0.0065 | 0.0198 |
| 2024_09_20 22:00 | 3269880 | 13 | 9.2793 | 19.2442 | -115.2496 | 3.3236 | 54.2542 | 0.0104 | 0.0150 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414452_5EA643DA | 504990 | 269 | -93.6 | 504990 | 564 | -96.9 | 504990 | 407 | -98.4 | 504990 | 518 |
| MR_1774414452_16E33D3A | 152650 | 814 | -91.6 | 152650 | 301 | -96.0 | 152650 | 218 | -100.1 | 152650 | 608 |
| MR_1774414452_7F08E5EE | 504990 | 269 | -95.4 | 504990 | 564 | -97.0 | 504990 | 407 | -99.9 | 504990 | 518 |
| MR_1774414452_815678C0 | 504990 | 269 | -96.2 | 504990 | 564 | -97.5 | 504990 | 407 | -100.5 | 504990 | 518 |
| MR_1774414452_4E8FEC85 | 152650 | 814 | -89.8 | 152650 | 301 | -94.4 | 152650 | 218 | -102.2 | 152650 | 608 |
| MR_1774414452_54770962 | 152650 | 814 | -92.8 | 152650 | 301 | -96.3 | 152650 | 218 | -101.4 | 152650 | 608 |
| MR_1774414452_56B69A75 | 152650 | 814 | -91.5 | 152650 | 301 | -96.7 | 152650 | 218 | -102.7 | 152650 | 608 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 355: `4efbe83e-495...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4efbe83e-495c-460a-aa1e-c02d814369c4` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Add neighbor relationship between 3275917_1 and 3236135_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[355] topology](images/train_0355.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3236135_2 by 9 degrees
- `C2`: Decrease A3 Offset threshold for 3236135_2
- `C3`: Add neighbor relationship between 3275917_1 and 3236135_2 **← 정답**
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275917_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275917_1
- `C6`: Check test server and transmission issues
- `C7`: Increase transmission power for 3275917_1
- `C8`: Lift the tilt angle  of 3236135_2 by 3 degrees
- `C9`: Increase transmission power for 3236135_2
- `C10`: Increase A3 Offset threshold for 3275917_1
- `C11`: Lift the tilt angle of 3275917_1 by 10 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236135_2
- `C13`: Press down the tilt angle  of 3236135_2 by 3 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Press down the tilt angle of 3275917_1 by 10 degrees
- `C16`: Adjust the azimuth of 3275917_1 by 50 degrees
- `C17`: Increase A3 Offset threshold for 3236135_2
- `C18`: Decrease transmission power for 3275917_1
- `C19`: Add neighbor relationship between 3259422_3 and 3236135_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236135_2
- `C21`: Decrease A3 Offset threshold for 3275917_1
- `C22`: Decrease transmission power for 3236135_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.846 | MS1 | 121.4656652033 | 31.1446303154 | 537 | 504990 | -78.01 | 14.47 | 565.38 | 0.08 | 2.28 | 1594 |
| 2024-09-20 22:21:32.659 | MS1 | 121.4656749521 | 31.1446236535 | 537 | 504990 | -77.51 | 13.46 | 553.15 | 0.16 | 2.62 | 1580 |
| 2024-09-20 22:21:33.639 | MS1 | 121.4656691791 | 31.1446185408 | 537 | 504990 | -84.26 | 14.75 | 329.79 | 0.09 | 2.37 | 1565 |
| 2024-09-20 22:21:34.752 | MS1 | 121.4656698930 | 31.1446201288 | 537 | 504990 | -91.84 | -1.33 | 42.16 | 0.04 | 1.01 | 1575 |
| 2024-09-20 22:21:35.863 | MS1 | 121.4656604600 | 31.1446209508 | 537 | 504990 | -86.69 | -0.53 | 59.36 | 0.18 | 1.18 | 1593 |
| 2024-09-20 22:21:36.870 | MS1 | 121.4656610911 | 31.1446329007 | 537 | 504990 | -93.10 | -2.08 | 26.37 | 0.07 | 1.18 | 1594 |
| 2024-09-20 22:21:37.437 | MS1 | 121.4656765555 | 31.1446374827 | 537 | 504990 | -91.63 | -2.58 | 63.40 | 0.01 | 1.43 | 1569 |
| 2024-09-20 22:21:38.559 | MS1 | 121.4656690161 | 31.1446297823 | 537 | 504990 | -82.16 | 13.65 | 578.61 | 0.07 | 1.43 | 1584 |
| 2024-09-20 22:21:39.779 | MS1 | 121.4656667701 | 31.1446200116 | 537 | 504990 | -83.64 | 15.95 | 527.77 | 0.04 | 1.41 | 1583 |
| 2024-09-20 22:21:40.531 | MS1 | 121.4656766405 | 31.1446285825 | 537 | 504990 | -78.45 | 16.08 | 581.96 | 0.02 | 2.82 | 1575 |
| 2024-09-20 22:21:41.381 | MS1 | 121.4656582104 | 31.1446365749 | 537 | 504990 | -76.56 | 15.22 | 363.39 | 0.03 | 2.87 | 1560 |
| 2024-09-20 22:21:42.396 | MS1 | 121.4656580347 | 31.1446205289 | 537 | 504990 | -82.37 | 12.98 | 337.67 | 0.03 | 2.76 | 1569 |

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
| 3236135 | 2 | 121.4656451313 | 31.1511375060 | 189 | 1 | 6 | 21.6 | TDD | 347 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3259422 | 3 | 121.4744324085 | 31.1526945604 | 190 | 14 | 9 | 22.5 | TDD | 228 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3261827 | 4 | 121.4748542208 | 31.1505542198 | 128 | 7 | 4 | 28.9 | TDD | 61 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3275917 | 1 | 121.4703644590 | 31.1461064896 | 146 | 11 | 7 | 27.7 | TDD | 537 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.589 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.610 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.713 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.713 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.439 | NREventA3 | measId:2;ServCellPCI:391;Se... |
| 2024-09-20 22:21:36.439 | NREventA3 | measId:2;ServCellPCI:391;Se... |
| 2024-09-20 22:21:37.439 | NREventA3 | measId:2;ServCellPCI:391;Se... |
| 2024-09-20 22:21:39.939 | NRRRCReestablishAttempt | PCI:391 |
| 2024-09-20 22:21:39.953 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.967 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:40.103 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.103 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275917 | 1 | 15.0571 | 5.4719 | -115.7542 | 14.3379 | 129.0857 | 0.0001 | 0.1959 |
| 2024_09_20 22:00 | 3236135 | 2 | 12.5731 | 16.8954 | -115.8818 | 10.3741 | 169.6838 | 0.0023 | 0.0125 |
| 2024_09_20 22:00 | 3259422 | 3 | 12.1639 | 15.6797 | -115.6042 | 12.0379 | 106.4878 | 0.0170 | 0.0188 |
| 2024_09_20 22:00 | 3261827 | 4 | 9.0158 | 9.7305 | -114.2352 | 17.5983 | 93.4739 | 0.0024 | 0.0182 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417195_96E2DCB1 | 504990 | 347 | -87.9 | 504990 | 537 | -92.3 | 504990 | 228 | -92.3 | 504990 | 61 |
| MR_1774417195_8AA4000A | 504990 | 537 | -90.2 | 504990 | 347 | -84.9 | 504990 | 228 | -91.0 | 504990 | 61 |
| MR_1774417195_7437A1D1 | 504990 | 537 | -91.7 | 504990 | 347 | -86.9 | 504990 | 228 | -91.2 | 504990 | 61 |
| MR_1774417195_7C39E83B | 504990 | 537 | -93.5 | 504990 | 347 | -85.6 | 504990 | 228 | -90.6 | 504990 | 61 |
| MR_1774417195_B8D79702 | 504990 | 347 | -85.4 | 504990 | 537 | -90.9 | 504990 | 228 | -91.3 | 504990 | 61 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 356: `2322d4b4-173...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2322d4b4-173f-41e5-a25c-dd7e98f7026b` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[356] topology](images/train_0356.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219558_4
- `C2`: Add neighbor relationship between 3231251_1 and 3219558_4
- `C3`: Press down the tilt angle  of 3219558_4 by 10 degrees
- `C4`: Decrease A3 Offset threshold for 3219558_4
- `C5`: Adjust the azimuth of 3219558_4 by 35 degrees
- `C6`: Decrease transmission power for 3231251_1
- `C7`: Lift the tilt angle  of 3219558_4 by 10 degrees
- `C8`: Increase transmission power for 3231251_1
- `C9`: Press down the tilt angle of 3231251_1 by 8 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231251_1
- `C11`: Decrease transmission power for 3219558_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219558_4
- `C13`: Increase transmission power for 3219558_4
- `C14`: Decrease A3 Offset threshold for 3231251_1
- `C15`: Insufficient data; more data is needed for judgment. **← 정답**
- `C16`: Adjust the azimuth of 3231251_1 by 50 degrees
- `C17`: Check test server and transmission issues
- `C18`: Increase A3 Offset threshold for 3219558_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231251_1
- `C20`: Add neighbor relationship between 3279227_3 and 3219558_4
- `C21`: Increase A3 Offset threshold for 3231251_1
- `C22`: Lift the tilt angle of 3231251_1 by 8 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.180 | MS1 | 121.4656737356 | 31.1446311255 | 440 | 504990 | -89.04 | 15.89 | 457.35 | 0.07 | 2.73 | 1575 |
| 2024-09-20 22:21:32.171 | MS1 | 121.4656750228 | 31.1446261270 | 440 | 504990 | -89.61 | 14.32 | 402.77 | 0.01 | 2.67 | 1585 |
| 2024-09-20 22:21:33.475 | MS1 | 121.4656620088 | 31.1446363973 | 440 | 504990 | -89.65 | 15.84 | 602.51 | 0.15 | 2.69 | 1560 |
| 2024-09-20 22:21:34.482 | MS1 | 121.4656617943 | 31.1446369653 | 440 | 504990 | -87.96 | 15.76 | 48.34 | 0.05 | 2.91 | 1569 |
| 2024-09-20 22:21:35.841 | MS1 | 121.4656693496 | 31.1446209052 | 440 | 504990 | -90.08 | 15.45 | 52.59 | 0.01 | 2.61 | 1594 |
| 2024-09-20 22:21:36.870 | MS1 | 121.4656744904 | 31.1446180665 | 440 | 504990 | -91.91 | 17.96 | 54.94 | 0.09 | 2.03 | 1589 |
| 2024-09-20 22:21:37.376 | MS1 | 121.4656695614 | 31.1446322995 | 440 | 504990 | -90.36 | 7.90 | 88.56 | 0.17 | 2.75 | 1585 |
| 2024-09-20 22:21:38.782 | MS1 | 121.4656716835 | 31.1446271903 | 440 | 504990 | -92.95 | 7.86 | 75.72 | 0.14 | 2.13 | 1600 |
| 2024-09-20 22:21:39.502 | MS1 | 121.4656674434 | 31.1446282473 | 440 | 504990 | -90.65 | 12.09 | 67.81 | 0.19 | 2.09 | 1562 |
| 2024-09-20 22:21:40.502 | MS1 | 121.4656683481 | 31.1446246711 | 440 | 504990 | -89.59 | 12.44 | 363.30 | 0.12 | 2.71 | 1598 |
| 2024-09-20 22:21:41.770 | MS1 | 121.4656707709 | 31.1446298364 | 440 | 504990 | -93.23 | 11.64 | 413.87 | 0.04 | 2.60 | 1594 |
| 2024-09-20 22:21:42.235 | MS1 | 121.4656724929 | 31.1446314551 | 440 | 504990 | -90.27 | 7.88 | 315.23 | 0.08 | 2.14 | 1569 |

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
| 3219558 | 4 | 121.4727826336 | 31.1526145981 | 182 | 14 | 8 | 16.1 | TDD | 102 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3231251 | 1 | 121.4684073410 | 31.1509900138 | 259 | 5 | 0 | 45.1 | TDD | 440 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3242384 | 2 | 121.4750532097 | 31.1535669155 | 339 | 8 | 6 | 47.4 | TDD | 792 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3279227 | 3 | 121.4727634173 | 31.1498005887 | 15 | 14 | 8 | 17.8 | TDD | 563 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.482 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.600 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.600 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.295 | NREventA3 | measId:2;ServCellPCI:709;Se... |
| 2024-09-20 22:21:38.535 | NRHandoverAttempt | SourcePCI:709;SourceNR-ARFC... |
| 2024-09-20 22:21:38.567 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.582 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.721 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.721 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3231251 | 1 | 90.8127 | 90.5073 | -117.1612 | 9.5054 | 114.1605 | 0.0080 | 0.0001 |
| 2024_09_19 22:00 | 3242384 | 2 | 84.3493 | 84.1017 | -116.9997 | 18.4580 | 185.5132 | 0.0152 | 0.0000 |
| 2024_09_19 22:00 | 3279227 | 3 | 94.2788 | 88.7318 | -115.8425 | 9.8385 | 158.6318 | 0.0053 | 0.0108 |
| 2024_09_19 22:00 | 3219558 | 4 | 77.3424 | 87.8563 | -115.0835 | 7.2159 | 128.2554 | 0.0001 | 0.0082 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416851_CD815B9C | 504990 | 440 | -89.6 | 504990 | 102 | -97.8 | 504990 | 563 | -100.4 | 504990 | 792 |
| MR_1774416851_F2F30A01 | 504990 | 440 | -89.2 | 504990 | 102 | -98.1 | 504990 | 563 | -99.2 | 504990 | 792 |
| MR_1774416851_08718787 | 504990 | 440 | -87.5 | 504990 | 102 | -96.2 | 504990 | 563 | -99.5 | 504990 | 792 |
| MR_1774416851_E8914A92 | 504990 | 440 | -88.6 | 504990 | 102 | -94.7 | 504990 | 563 | -101.8 | 504990 | 792 |
| MR_1774416851_E565E258 | 504990 | 440 | -86.6 | 504990 | 102 | -94.5 | 504990 | 563 | -101.3 | 504990 | 792 |
| MR_1774416851_1FA94524 | 504990 | 440 | -87.6 | 504990 | 102 | -97.3 | 504990 | 563 | -100.8 | 504990 | 792 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 357: `b7234b65-d53...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b7234b65-d533-443f-93d7-76f6f47a2f23` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[357] topology](images/train_0357.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Add neighbor relationship between 3274668_1 and 3265363_4
- `C3`: Press down the tilt angle  of 3265363_4 by 5 degrees
- `C4`: Increase A3 Offset threshold for 3265363_4
- `C5`: Decrease A3 Offset threshold for 3256915_3
- `C6`: Add neighbor relationship between 3256915_3 and 3265363_4
- `C7`: Increase transmission power for 3265363_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256915_3
- `C9`: Decrease transmission power for 3256915_3
- `C10`: Lift the tilt angle  of 3265363_4 by 5 degrees
- `C11`: Lift the tilt angle of 3256915_3 by 9 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256915_3
- `C13`: Decrease transmission power for 3265363_4
- `C14`: Adjust the azimuth of 3256915_3 by 50 degrees
- `C15`: Press down the tilt angle of 3256915_3 by 9 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265363_4
- `C17`: Increase transmission power for 3256915_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265363_4
- `C19`: Adjust the azimuth of 3265363_4 by 50 degrees
- `C20`: Increase A3 Offset threshold for 3256915_3
- `C21`: Decrease A3 Offset threshold for 3265363_4
- `C22`: Insufficient data; more data is needed for judgment. **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.870 | MS1 | 121.4656646129 | 31.1446199584 | 970 | 504990 | -91.44 | 16.49 | 401.63 | 0.19 | 2.01 | 1564 |
| 2024-09-20 22:21:32.974 | MS1 | 121.4656753288 | 31.1446286223 | 970 | 504990 | -85.11 | 14.22 | 549.05 | 0.17 | 2.46 | 1565 |
| 2024-09-20 22:21:33.322 | MS1 | 121.4656590263 | 31.1446232441 | 970 | 504990 | -88.22 | 17.29 | 561.46 | 0.08 | 2.12 | 1596 |
| 2024-09-20 22:21:34.671 | MS1 | 121.4656726266 | 31.1446181151 | 970 | 504990 | -87.29 | 14.56 | 77.79 | 0.05 | 2.43 | 1570 |
| 2024-09-20 22:21:35.138 | MS1 | 121.4656775113 | 31.1446295153 | 970 | 504990 | -85.14 | 16.27 | 67.25 | 0.14 | 2.08 | 1593 |
| 2024-09-20 22:21:36.629 | MS1 | 121.4656753086 | 31.1446377468 | 970 | 504990 | -91.20 | 12.29 | 93.01 | 0.04 | 2.07 | 1568 |
| 2024-09-20 22:21:37.888 | MS1 | 121.4656678956 | 31.1446273381 | 970 | 504990 | -91.42 | 7.49 | 62.93 | 0.04 | 2.15 | 1565 |
| 2024-09-20 22:21:38.196 | MS1 | 121.4656655804 | 31.1446311196 | 970 | 504990 | -92.16 | 10.04 | 76.48 | 0.11 | 2.46 | 1597 |
| 2024-09-20 22:21:39.198 | MS1 | 121.4656752875 | 31.1446208000 | 970 | 504990 | -92.09 | 10.60 | 65.97 | 0.19 | 2.12 | 1574 |
| 2024-09-20 22:21:40.164 | MS1 | 121.4656650156 | 31.1446374838 | 970 | 504990 | -92.74 | 9.25 | 448.79 | 0.05 | 2.92 | 1597 |
| 2024-09-20 22:21:41.916 | MS1 | 121.4656638958 | 31.1446280464 | 970 | 504990 | -90.14 | 8.08 | 572.39 | 0.18 | 2.56 | 1595 |
| 2024-09-20 22:21:42.800 | MS1 | 121.4656609222 | 31.1446295605 | 970 | 504990 | -90.65 | 11.57 | 598.77 | 0.15 | 2.10 | 1574 |

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
| 3213189 | 2 | 121.4678359495 | 31.1451969307 | 103 | 1 | 9 | 20.7 | TDD | 953 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3256915 | 3 | 121.4756695532 | 31.1549360063 | 298 | 8 | 3 | 31.0 | TDD | 970 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3265363 | 4 | 121.4737898632 | 31.1470916635 | 128 | 2 | 9 | 43.2 | TDD | 915 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3274668 | 1 | 121.4649914202 | 31.1483109607 | 11 | 3 | 1 | 21.4 | TDD | 48 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.566 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.588 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.733 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.733 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.462 | NREventA3 | measId:2;ServCellPCI:400;Se... |
| 2024-09-20 22:21:38.702 | NRHandoverAttempt | SourcePCI:400;SourceNR-ARFC... |
| 2024-09-20 22:21:38.750 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.763 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.870 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.870 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3274668 | 1 | 83.4973 | 89.5485 | -117.1419 | 12.7539 | 169.6258 | 0.0176 | 0.0081 |
| 2024_09_19 22:00 | 3213189 | 2 | 78.9392 | 84.8894 | -115.0227 | 15.4985 | 151.7246 | 0.0123 | 0.0181 |
| 2024_09_19 22:00 | 3256915 | 3 | 79.8411 | 80.6811 | -116.6539 | 17.8506 | 174.9876 | 0.0162 | 0.0050 |
| 2024_09_19 22:00 | 3265363 | 4 | 90.5079 | 91.8913 | -116.7287 | 17.8312 | 139.6374 | 0.0058 | 0.0047 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414642_A9D1F44A | 504990 | 970 | -86.1 | 504990 | 915 | -90.5 | 504990 | 48 | -99.6 | 504990 | 953 |
| MR_1774414642_FDA771B8 | 504990 | 970 | -89.2 | 504990 | 915 | -88.6 | 504990 | 48 | -102.6 | 504990 | 953 |
| MR_1774414642_5BE8680C | 504990 | 970 | -87.4 | 504990 | 915 | -90.3 | 504990 | 48 | -101.4 | 504990 | 953 |
| MR_1774414642_D69BCE23 | 504990 | 970 | -87.3 | 504990 | 915 | -91.7 | 504990 | 48 | -102.9 | 504990 | 953 |
| MR_1774414642_1E2AC929 | 504990 | 970 | -86.4 | 504990 | 915 | -91.8 | 504990 | 48 | -101.7 | 504990 | 953 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 358: `0e6b6e18-3e5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0e6b6e18-3e59-45d6-8466-80f0e66457fa` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234463_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[358] topology](images/train_0358.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3211331_6
- `C2`: Decrease A3 Offset threshold for 3234463_4
- `C3`: Increase A3 Offset threshold for 3234463_4
- `C4`: Check test server and transmission issues
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234463_4 **← 정답**
- `C6`: Press down the tilt angle of 3234463_4 by 3 degrees
- `C7`: Increase transmission power for 3211331_6
- `C8`: Lift the tilt angle of 3234463_4 by 3 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211331_6
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease A3 Offset threshold for 3211331_6
- `C12`: Press down the tilt angle  of 3211331_6 by 3 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211331_6
- `C14`: Decrease transmission power for 3234463_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234463_4
- `C16`: Lift the tilt angle  of 3211331_6 by 3 degrees
- `C17`: Increase transmission power for 3234463_4
- `C18`: Add neighbor relationship between 3254884_9 and 3211331_6
- `C19`: Decrease transmission power for 3211331_6
- `C20`: Adjust the azimuth of 3234463_4 by 27 degrees
- `C21`: Add neighbor relationship between 3234463_4 and 3211331_6
- `C22`: Adjust the azimuth of 3211331_6 by 38 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.987 | MS1 | 121.4656688254 | 31.1446340337 | 209 | 504990 | -93.15 | 10.99 | 431.97 | 0.19 | 2.30 | 1574 |
| 2024-09-20 22:21:32.393 | MS1 | 121.4656727761 | 31.1446194270 | 325 | 504990 | -93.16 | 13.05 | 462.32 | 0.02 | 2.28 | 1560 |
| 2024-09-20 22:21:33.684 | MS1 | 121.4656706903 | 31.1446260466 | 212 | 504990 | -95.59 | 11.45 | 395.77 | 0.16 | 2.68 | 1582 |
| 2024-09-20 22:21:34.793 | MS1 | 121.4656604310 | 31.1446255088 | 544 | 152650 | -91.59 | 5.94 | 57.35 | 0.13 | 1.51 | 986 |
| 2024-09-20 22:21:35.599 | MS1 | 121.4656661828 | 31.1446323351 | 590 | 152650 | -96.55 | 2.55 | 82.47 | 0.04 | 1.90 | 906 |
| 2024-09-20 22:21:36.723 | MS1 | 121.4656636995 | 31.1446305447 | 841 | 152650 | -90.26 | 4.21 | 50.14 | 0.10 | 1.92 | 993 |
| 2024-09-20 22:21:37.894 | MS1 | 121.4656724453 | 31.1446344179 | 955 | 152650 | -87.39 | 7.41 | 74.84 | 0.16 | 1.86 | 980 |
| 2024-09-20 22:21:38.132 | MS1 | 121.4656612000 | 31.1446255504 | 544 | 152650 | -88.26 | 3.52 | 106.90 | 0.06 | 1.74 | 932 |
| 2024-09-20 22:21:39.774 | MS1 | 121.4656679923 | 31.1446255648 | 590 | 152650 | -91.22 | 5.53 | 74.15 | 0.11 | 1.65 | 961 |
| 2024-09-20 22:21:40.988 | MS1 | 121.4656736179 | 31.1446188125 | 841 | 152650 | -89.69 | 3.45 | 64.45 | 0.19 | 2.02 | 1587 |
| 2024-09-20 22:21:41.300 | MS1 | 121.4656702035 | 31.1446223371 | 955 | 152650 | -91.29 | 2.58 | 58.50 | 0.06 | 2.78 | 1588 |
| 2024-09-20 22:21:42.228 | MS1 | 121.4656624421 | 31.1446183250 | 544 | 152650 | -87.59 | 6.05 | 53.26 | 0.12 | 2.61 | 1575 |

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
| 3210029 | 10 | 121.4757048982 | 31.1490931369 | 193 | 15 | 5 | 9.8 | FDD | 590 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3211331 | 6 | 121.4713717858 | 31.1470633199 | 282 | 3 | 3 | 2.7 | TDD | 952 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3213762 | 1 | 121.4717216250 | 31.1524979867 | 224 | 5 | 8 | 20.4 | TDD | 325 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3228070 | 13 | 121.4723615432 | 31.1559063907 | 152 | 1 | 5 | 21.3 | FDD | 955 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3232412 | 7 | 121.4715337346 | 31.1441890064 | 248 | 14 | 11 | 2.2 | FDD | 544 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3232977 | 12 | 121.4757654571 | 31.1440621625 | 117 | 14 | 12 | 14.7 | FDD | 850 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3234463 | 4 | 121.4698128466 | 31.1479756719 | 254 | 1 | 2 | 19.8 | TDD | 209 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3240022 | 5 | 121.4711033201 | 31.1537160489 | 186 | 11 | 3 | 18.2 | TDD | 212 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3253499 | 11 | 121.4747626202 | 31.1559898078 | 174 | 13 | 1 | 21.4 | FDD | 14 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3254884 | 9 | 121.4703695072 | 31.1522230479 | 279 | 5 | 8 | 19.6 | FDD | 841 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3264745 | 8 | 121.4644962721 | 31.1447423003 | 30 | 9 | 9 | 0.1 | FDD | 322 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3273862 | 2 | 121.4724339695 | 31.1526643319 | 297 | 14 | 1 | 26.9 | TDD | 1004 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3277955 | 3 | 121.4649616555 | 31.1514609466 | 275 | 11 | 4 | 10.6 | TDD | 588 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.118 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.134 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.235 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.235 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.956 | NREventA2 | measId:1;ServCellPCI:334;Se... |
| 2024-09-20 22:21:35.072 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.275 | NREventA5 | measId:3;ServCellPCI:334;Se... |
| 2024-09-20 22:21:35.338 | NRHandoverAttempt | SourcePCI:334;SourceNR-ARFC... |
| 2024-09-20 22:21:35.365 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.379 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.483 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.483 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213762 | 1 | 14.1310 | 5.2573 | -116.5783 | 15.9222 | 164.3249 | 0.0178 | 0.0011 |
| 2024_09_20 22:00 | 3273862 | 2 | 10.2603 | 15.3694 | -117.5730 | 15.8494 | 101.5836 | 0.0108 | 0.0042 |
| 2024_09_20 22:00 | 3277955 | 3 | 18.4221 | 9.6825 | -114.3556 | 15.9724 | 138.7534 | 0.0117 | 0.0195 |
| 2024_09_20 22:00 | 3234463 | 4 | 15.5976 | 16.2089 | -114.9800 | 10.1330 | 106.1921 | 0.0156 | 0.0101 |
| 2024_09_20 22:00 | 3240022 | 5 | 8.5758 | 11.4108 | -115.6461 | 8.8614 | 156.3261 | 0.0072 | 0.0189 |
| 2024_09_20 22:00 | 3211331 | 6 | 19.9012 | 19.8046 | -114.2779 | 7.6352 | 99.7603 | 0.0031 | 0.0111 |
| 2024_09_20 22:00 | 3232412 | 7 | 11.1025 | 13.7741 | -117.7411 | 3.3859 | 29.4354 | 0.0077 | 0.0001 |
| 2024_09_20 22:00 | 3264745 | 8 | 11.9031 | 10.4034 | -117.8563 | 4.7264 | 51.6979 | 0.0111 | 0.0061 |
| 2024_09_20 22:00 | 3254884 | 9 | 18.0117 | 6.2120 | -117.8405 | 4.3889 | 22.4250 | 0.0170 | 0.0161 |
| 2024_09_20 22:00 | 3210029 | 10 | 19.9029 | 7.6586 | -115.1461 | 4.1219 | 33.9265 | 0.0071 | 0.0135 |
| 2024_09_20 22:00 | 3253499 | 11 | 6.7942 | 17.5497 | -116.2365 | 4.2374 | 31.9697 | 0.0110 | 0.0048 |
| 2024_09_20 22:00 | 3232977 | 12 | 7.0041 | 8.4098 | -115.4316 | 4.2477 | 53.3216 | 0.0009 | 0.0070 |
| 2024_09_20 22:00 | 3228070 | 13 | 16.3188 | 5.0691 | -117.7195 | 4.3064 | 21.9555 | 0.0058 | 0.0075 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415617_B2C32E01 | 152650 | 544 | -91.1 | 152650 | 14 | -98.3 | 152650 | 850 | -101.3 | 152650 | 322 |
| MR_1774415617_2D8E7E63 | 504990 | 212 | -96.4 | 504990 | 952 | -95.7 | 504990 | 1004 | -95.7 | 504990 | 588 |
| MR_1774415617_F7FA6F9E | 504990 | 212 | -95.1 | 504990 | 952 | -93.1 | 504990 | 1004 | -95.8 | 504990 | 588 |
| MR_1774415617_28410BE3 | 152650 | 544 | -92.4 | 152650 | 14 | -98.6 | 152650 | 850 | -99.3 | 152650 | 322 |
| MR_1774415617_2903542B | 504990 | 212 | -93.8 | 504990 | 952 | -95.5 | 504990 | 1004 | -97.8 | 504990 | 588 |
| MR_1774415617_3CE81DDD | 152650 | 544 | -90.5 | 152650 | 14 | -95.5 | 152650 | 850 | -100.1 | 152650 | 322 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 359: `6f201387-3d5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6f201387-3d5f-4dce-be69-0cdefd1d5cba` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Decrease A3 Offset threshold for 3227367_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[359] topology](images/train_0359.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3227367_1
- `C2`: Increase A3 Offset threshold for 3250036_4
- `C3`: Add neighbor relationship between 3256039_2 and 3250036_4
- `C4`: Lift the tilt angle  of 3250036_4 by 5 degrees
- `C5`: Decrease A3 Offset threshold for 3227367_1 **← 정답**
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227367_1
- `C7`: Decrease transmission power for 3250036_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250036_4
- `C9`: Lift the tilt angle of 3227367_1 by 8 degrees
- `C10`: Increase transmission power for 3250036_4
- `C11`: Adjust the azimuth of 3227367_1 by 50 degrees
- `C12`: Decrease transmission power for 3227367_1
- `C13`: Increase transmission power for 3227367_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Press down the tilt angle  of 3250036_4 by 5 degrees
- `C16`: Press down the tilt angle of 3227367_1 by 8 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227367_1
- `C18`: Add neighbor relationship between 3227367_1 and 3250036_4
- `C19`: Decrease A3 Offset threshold for 3250036_4
- `C20`: Adjust the azimuth of 3250036_4 by 21 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250036_4
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.679 | MS1 | 121.4656606628 | 31.1446240248 | 172 | 504990 | -81.22 | 14.13 | 348.70 | 0.08 | 2.16 | 1564 |
| 2024-09-20 22:21:32.831 | MS1 | 121.4656582077 | 31.1446311278 | 172 | 504990 | -80.62 | 17.50 | 362.90 | 0.12 | 2.08 | 1584 |
| 2024-09-20 22:21:33.733 | MS1 | 121.4656629125 | 31.1446314653 | 172 | 504990 | -75.19 | 14.76 | 355.46 | 0.10 | 2.97 | 1573 |
| 2024-09-20 22:21:34.144 | MS1 | 121.4656634747 | 31.1446333509 | 172 | 504990 | -87.74 | -0.83 | 41.75 | 0.10 | 1.33 | 1591 |
| 2024-09-20 22:21:35.740 | MS1 | 121.4656774913 | 31.1446370408 | 172 | 504990 | -89.89 | -0.72 | 37.27 | 0.07 | 1.17 | 1573 |
| 2024-09-20 22:21:36.590 | MS1 | 121.4656624444 | 31.1446324559 | 172 | 504990 | -85.93 | -2.70 | 62.91 | 0.20 | 1.42 | 1584 |
| 2024-09-20 22:21:37.761 | MS1 | 121.4656697150 | 31.1446353740 | 172 | 504990 | -84.31 | -1.38 | 66.36 | 0.03 | 1.15 | 1582 |
| 2024-09-20 22:21:38.274 | MS1 | 121.4656590028 | 31.1446213042 | 172 | 504990 | -88.36 | -1.23 | 61.50 | 0.02 | 1.11 | 1567 |
| 2024-09-20 22:21:39.902 | MS1 | 121.4656602112 | 31.1446262844 | 431 | 504990 | -80.12 | 16.57 | 185.83 | 0.19 | 1.26 | 1576 |
| 2024-09-20 22:21:40.262 | MS1 | 121.4656620841 | 31.1446224587 | 431 | 504990 | -83.78 | 17.91 | 506.17 | 0.05 | 2.15 | 1567 |
| 2024-09-20 22:21:41.684 | MS1 | 121.4656666462 | 31.1446368823 | 431 | 504990 | -76.04 | 12.23 | 594.29 | 0.16 | 2.50 | 1563 |
| 2024-09-20 22:21:42.664 | MS1 | 121.4656656574 | 31.1446218423 | 431 | 504990 | -78.05 | 16.39 | 358.65 | 0.18 | 2.67 | 1594 |

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
| 3227367 | 1 | 121.4694288160 | 31.1452767505 | 319 | 1 | 5 | 46.0 | TDD | 172 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3250036 | 4 | 121.4680028579 | 31.1555625482 | 169 | 3 | 0 | 42.4 | TDD | 431 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3255486 | 3 | 121.4703388218 | 31.1459739634 | 194 | 14 | 0 | 32.5 | TDD | 638 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3256039 | 2 | 121.4751265568 | 31.1465193469 | 35 | 14 | 8 | 27.4 | TDD | 700 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.375 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.397 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.504 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.504 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.254 | NREventA3 | measId:2;ServCellPCI:521;Se... |
| 2024-09-20 22:21:38.494 | NRHandoverAttempt | SourcePCI:521;SourceNR-ARFC... |
| 2024-09-20 22:21:38.543 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.553 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.691 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.691 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227367 | 1 | 9.3860 | 18.9211 | -116.5765 | 13.3503 | 173.3100 | 0.0032 | 0.1686 |
| 2024_09_20 22:00 | 3256039 | 2 | 11.1695 | 8.5643 | -117.9857 | 10.1347 | 186.6296 | 0.0162 | 0.0089 |
| 2024_09_20 22:00 | 3255486 | 3 | 14.8678 | 8.1939 | -116.7143 | 19.2760 | 119.9178 | 0.0168 | 0.0105 |
| 2024_09_20 22:00 | 3250036 | 4 | 6.8364 | 19.9177 | -115.3491 | 12.6977 | 81.2648 | 0.0103 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412757_D91E8CD8 | 504990 | 172 | -89.2 | 504990 | 431 | -80.8 | 504990 | 700 | -82.4 | 504990 | 638 |
| MR_1774412757_01C87A4C | 504990 | 172 | -89.6 | 504990 | 431 | -83.5 | 504990 | 700 | -81.5 | 504990 | 638 |
| MR_1774412757_0144A8C0 | 504990 | 172 | -88.0 | 504990 | 431 | -83.2 | 504990 | 700 | -84.0 | 504990 | 638 |
| MR_1774412757_D8141CB2 | 504990 | 172 | -85.8 | 504990 | 431 | -80.7 | 504990 | 700 | -83.1 | 504990 | 638 |
| MR_1774412757_9AF95656 | 504990 | 431 | -82.9 | 504990 | 172 | -87.9 | 504990 | 700 | -81.3 | 504990 | 638 |
| MR_1774412757_18971E56 | 504990 | 172 | -85.8 | 504990 | 431 | -81.9 | 504990 | 700 | -83.2 | 504990 | 638 |
| MR_1774412757_49593946 | 504990 | 172 | -87.2 | 504990 | 431 | -80.6 | 504990 | 700 | -81.2 | 504990 | 638 |

> *... 2개 열 생략 (전체 14열)*

---
