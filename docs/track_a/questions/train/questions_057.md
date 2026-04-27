# Track A 문제 분석 — train[560]~train[569]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[560] ~ train[569] (10개)

## 목차

1. [문제 560: `663e8226-9e8...`](#560) — single-answer, 정답: C9
2. [문제 561: `1ef9daf7-750...`](#561) — single-answer, 정답: C16
3. [문제 562: `fc0412cf-fca...`](#562) — single-answer, 정답: C8
4. [문제 563: `8c185e62-cd5...`](#563) — single-answer, 정답: C14
5. [문제 564: `cc96722e-b40...`](#564) — single-answer, 정답: C6
6. [문제 565: `bbe199d3-833...`](#565) — single-answer, 정답: C14
7. [문제 566: `c966fbae-aee...`](#566) — single-answer, 정답: C16
8. [문제 567: `eb72d93a-77e...`](#567) — single-answer, 정답: C3
9. [문제 568: `83609a72-639...`](#568) — single-answer, 정답: C13
10. [문제 569: `0ef23a21-6ed...`](#569) — single-answer, 정답: C4

---

### 문제 560: `663e8226-9e8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `663e8226-9e84-493c-94d2-ad5af73a4125` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Lift the tilt angle  of 3233692_3 by 5 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[560] topology](images/train_0560.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216141_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264296_2
- `C3`: Lift the tilt angle of 3264296_2 by 3 degrees
- `C4`: Add neighbor relationship between 3233692_3 and 3216141_4
- `C5`: Increase transmission power for 3264296_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264296_2
- `C7`: Adjust the azimuth of 3264296_2 by 22 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216141_4
- `C9`: Lift the tilt angle  of 3233692_3 by 5 degrees **← 정답**
- `C10`: Increase A3 Offset threshold for 3216141_4
- `C11`: Add neighbor relationship between 3264296_2 and 3216141_4
- `C12`: Decrease transmission power for 3264296_2
- `C13`: Increase transmission power for 3216141_4
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease A3 Offset threshold for 3264296_2
- `C16`: Decrease A3 Offset threshold for 3216141_4
- `C17`: Press down the tilt angle  of 3233692_3 by 5 degrees
- `C18`: Press down the tilt angle of 3264296_2 by 3 degrees
- `C19`: Decrease transmission power for 3216141_4
- `C20`: Increase A3 Offset threshold for 3264296_2
- `C21`: Adjust the azimuth of 3233692_3 by 50 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.778 | MS1 | 121.4656757381 | 31.1446365091 | 35 | 504990 | -90.80 | 15.35 | 557.18 | 0.04 | 2.66 | 1593 |
| 2024-09-20 22:21:32.347 | MS1 | 121.4656693230 | 31.1446185791 | 35 | 504990 | -90.66 | 14.78 | 426.32 | 0.01 | 2.25 | 1600 |
| 2024-09-20 22:21:33.620 | MS1 | 121.4656593319 | 31.1446215864 | 35 | 504990 | -85.04 | 16.58 | 465.63 | 0.09 | 2.27 | 1586 |
| 2024-09-20 22:21:34.843 | MS1 | 121.4656591392 | 31.1446254140 | 35 | 504990 | -86.73 | 17.36 | 49.54 | 0.10 | 2.98 | 1593 |
| 2024-09-20 22:21:35.568 | MS1 | 121.4656630188 | 31.1446195579 | 35 | 504990 | -88.42 | 15.50 | 69.40 | 0.15 | 2.21 | 1590 |
| 2024-09-20 22:21:36.401 | MS1 | 121.4656731210 | 31.1446345703 | 35 | 504990 | -86.70 | 14.05 | 54.06 | 0.12 | 2.91 | 1573 |
| 2024-09-20 22:21:37.145 | MS1 | 121.4656644226 | 31.1446274635 | 35 | 504990 | -92.30 | 11.04 | 91.31 | 0.02 | 2.96 | 1594 |
| 2024-09-20 22:21:38.224 | MS1 | 121.4656699676 | 31.1446320906 | 35 | 504990 | -92.64 | 11.16 | 90.21 | 0.12 | 2.94 | 1582 |
| 2024-09-20 22:21:39.960 | MS1 | 121.4656668959 | 31.1446265251 | 35 | 504990 | -89.06 | 12.62 | 91.58 | 0.08 | 2.68 | 1575 |
| 2024-09-20 22:21:40.443 | MS1 | 121.4656641812 | 31.1446325019 | 35 | 504990 | -90.87 | 8.95 | 443.59 | 0.14 | 2.44 | 1598 |
| 2024-09-20 22:21:41.400 | MS1 | 121.4656737360 | 31.1446217080 | 35 | 504990 | -92.54 | 12.87 | 403.56 | 0.04 | 2.56 | 1566 |
| 2024-09-20 22:21:42.112 | MS1 | 121.4656628966 | 31.1446351079 | 35 | 504990 | -90.67 | 11.74 | 449.41 | 0.15 | 2.18 | 1571 |

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
| 3216141 | 4 | 121.4736682231 | 31.1477786041 | 190 | 4 | 8 | 16.7 | TDD | 580 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3228906 | 1 | 121.4642914065 | 31.1485258421 | 30 | 6 | 10 | 38.4 | TDD | 25 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3233692 | 3 | 121.4668430353 | 31.1488804754 | 36 | 14 | 3 | 21.5 | TDD | 196 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3264296 | 2 | 121.4681524766 | 31.1491394601 | 227 | 0 | 8 | 32.8 | TDD | 35 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.193 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.209 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.355 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.355 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.052 | NREventA3 | measId:2;ServCellPCI:176;Se... |
| 2024-09-20 22:21:38.292 | NRHandoverAttempt | SourcePCI:176;SourceNR-ARFC... |
| 2024-09-20 22:21:38.337 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.351 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.474 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.474 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228906 | 1 | 8.4298 | 14.7384 | -117.8498 | 17.8546 | 142.5884 | 0.0042 | 0.0190 |
| 2024_09_20 22:00 | 3264296 | 2 | 79.6798 | 83.5179 | -116.8531 | 8.6593 | 81.1328 | 0.0034 | 0.0152 |
| 2024_09_20 22:00 | 3233692 | 3 | 10.2322 | 6.1834 | -117.4101 | 16.8761 | 156.4606 | 0.0152 | 0.0111 |
| 2024_09_20 22:00 | 3216141 | 4 | 15.1882 | 9.9183 | -116.3166 | 13.2957 | 109.4674 | 0.0170 | 0.0107 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412974_6D1D9ED7 | 504990 | 35 | -86.6 | 504990 | 580 | -94.0 | 504990 | 196 | -96.6 | 504990 | 25 |
| MR_1774412974_F9CEAA16 | 504990 | 35 | -86.5 | 504990 | 580 | -94.1 | 504990 | 196 | -94.4 | 504990 | 25 |
| MR_1774412974_669859E1 | 504990 | 35 | -87.8 | 504990 | 580 | -95.0 | 504990 | 196 | -95.9 | 504990 | 25 |
| MR_1774412974_FDAF4778 | 504990 | 35 | -88.1 | 504990 | 580 | -95.1 | 504990 | 196 | -96.5 | 504990 | 25 |
| MR_1774412974_6F6BA69E | 504990 | 35 | -86.5 | 504990 | 580 | -97.1 | 504990 | 196 | -97.9 | 504990 | 25 |
| MR_1774412974_4E072970 | 504990 | 35 | -88.4 | 504990 | 580 | -95.1 | 504990 | 196 | -97.7 | 504990 | 25 |
| MR_1774412974_070486B1 | 504990 | 35 | -85.8 | 504990 | 580 | -93.7 | 504990 | 196 | -96.3 | 504990 | 25 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 561: `1ef9daf7-750...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1ef9daf7-7503-4bfb-8795-03875b9cb56b` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3212749_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[561] topology](images/train_0561.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Add neighbor relationship between 3231999_1 and 3255801_2
- `C3`: Increase transmission power for 3212749_3
- `C4`: Adjust the azimuth of 3212749_3 by 14 degrees
- `C5`: Decrease A3 Offset threshold for 3255801_2
- `C6`: Decrease A3 Offset threshold for 3212749_3
- `C7`: Decrease transmission power for 3212749_3
- `C8`: Press down the tilt angle of 3212749_3 by 4 degrees
- `C9`: Lift the tilt angle of 3212749_3 by 4 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255801_2
- `C11`: Press down the tilt angle  of 3255801_2 by 10 degrees
- `C12`: Increase A3 Offset threshold for 3212749_3
- `C13`: Lift the tilt angle  of 3255801_2 by 10 degrees
- `C14`: Increase A3 Offset threshold for 3255801_2
- `C15`: Decrease transmission power for 3255801_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212749_3 **← 정답**
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212749_3
- `C18`: Add neighbor relationship between 3212749_3 and 3255801_2
- `C19`: Increase transmission power for 3255801_2
- `C20`: Check test server and transmission issues
- `C21`: Adjust the azimuth of 3255801_2 by 50 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255801_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.563 | MS1 | 121.4656672144 | 31.1446226320 | 379 | 504990 | -86.17 | 12.37 | 538.85 | 0.05 | 2.65 | 1581 |
| 2024-09-20 22:21:32.123 | MS1 | 121.4656705423 | 31.1446273569 | 379 | 504990 | -87.22 | 13.99 | 415.23 | 0.17 | 2.43 | 1564 |
| 2024-09-20 22:21:33.131 | MS1 | 121.4656707512 | 31.1446247694 | 379 | 504990 | -85.07 | 17.10 | 494.14 | 0.07 | 2.93 | 1599 |
| 2024-09-20 22:21:34.763 | MS1 | 121.4656755357 | 31.1446223075 | 379 | 504990 | -85.44 | 17.39 | 83.66 | 0.62 | 2.25 | 644 |
| 2024-09-20 22:21:35.623 | MS1 | 121.4656767850 | 31.1446188805 | 379 | 504990 | -91.31 | 13.36 | 59.11 | 0.63 | 2.43 | 688 |
| 2024-09-20 22:21:36.816 | MS1 | 121.4656624154 | 31.1446191037 | 379 | 504990 | -86.73 | 15.68 | 62.61 | 0.64 | 2.59 | 612 |
| 2024-09-20 22:21:37.441 | MS1 | 121.4656724578 | 31.1446297212 | 379 | 504990 | -89.95 | 12.33 | 79.67 | 0.56 | 2.36 | 567 |
| 2024-09-20 22:21:38.219 | MS1 | 121.4656715953 | 31.1446230835 | 379 | 504990 | -90.90 | 10.38 | 61.21 | 0.63 | 2.49 | 518 |
| 2024-09-20 22:21:39.778 | MS1 | 121.4656669380 | 31.1446247158 | 379 | 504990 | -89.57 | 7.93 | 76.55 | 0.59 | 2.29 | 552 |
| 2024-09-20 22:21:40.194 | MS1 | 121.4656591605 | 31.1446318759 | 379 | 504990 | -92.96 | 9.08 | 327.17 | 0.15 | 2.99 | 1568 |
| 2024-09-20 22:21:41.449 | MS1 | 121.4656659389 | 31.1446316894 | 379 | 504990 | -91.85 | 12.48 | 320.80 | 0.08 | 2.12 | 1571 |
| 2024-09-20 22:21:42.396 | MS1 | 121.4656767506 | 31.1446363734 | 379 | 504990 | -91.32 | 11.12 | 344.73 | 0.15 | 2.09 | 1569 |

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
| 3212749 | 3 | 121.4661837148 | 31.1510085969 | 198 | 0 | 2 | 49.5 | TDD | 379 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3231999 | 1 | 121.4691858020 | 31.1501493134 | 345 | 4 | 8 | 41.3 | TDD | 1000 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3255801 | 2 | 121.4678686077 | 31.1499893872 | 28 | 8 | 4 | 33.7 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3264603 | 4 | 121.4698822113 | 31.1518201494 | 56 | 4 | 11 | 40.0 | TDD | 617 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.782 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.798 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:30.922 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.922 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.661 | NREventA3 | measId:2;ServCellPCI:300;Se... |
| 2024-09-20 22:21:37.901 | NRHandoverAttempt | SourcePCI:300;SourceNR-ARFC... |
| 2024-09-20 22:21:37.937 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.952 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.071 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.071 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231999 | 1 | 18.4581 | 9.5745 | -115.0688 | 5.7945 | 143.3702 | 0.0109 | 0.0057 |
| 2024_09_20 22:00 | 3255801 | 2 | 6.9448 | 14.5805 | -114.2631 | 13.3033 | 114.0797 | 0.0125 | 0.0022 |
| 2024_09_20 22:00 | 3212749 | 3 | 17.7214 | 6.8222 | -117.3044 | 8.1543 | 178.1448 | 0.0182 | 0.0085 |
| 2024_09_20 22:00 | 3264603 | 4 | 6.4388 | 11.8482 | -114.2683 | 14.1902 | 132.0103 | 0.0043 | 0.0172 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414364_1333C1E7 | 504990 | 379 | -87.2 | 504990 | 441 | -88.1 | 504990 | 1000 | -93.4 | 504990 | 617 |
| MR_1774414364_270B0AD7 | 504990 | 379 | -84.8 | 504990 | 441 | -88.9 | 504990 | 1000 | -95.0 | 504990 | 617 |
| MR_1774414364_02B5E3F6 | 504990 | 379 | -86.1 | 504990 | 441 | -89.4 | 504990 | 1000 | -96.9 | 504990 | 617 |
| MR_1774414364_60E69FC6 | 504990 | 379 | -84.7 | 504990 | 441 | -89.1 | 504990 | 1000 | -94.7 | 504990 | 617 |
| MR_1774414364_3BF46796 | 504990 | 379 | -87.2 | 504990 | 441 | -88.2 | 504990 | 1000 | -97.1 | 504990 | 617 |
| MR_1774414364_0DA2A292 | 504990 | 379 | -86.5 | 504990 | 441 | -88.3 | 504990 | 1000 | -94.4 | 504990 | 617 |
| MR_1774414364_7CA099A8 | 504990 | 379 | -85.7 | 504990 | 441 | -91.4 | 504990 | 1000 | -93.6 | 504990 | 617 |
| MR_1774414364_50436074 | 504990 | 379 | -85.5 | 504990 | 441 | -91.7 | 504990 | 1000 | -94.0 | 504990 | 617 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 562: `fc0412cf-fca...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fc0412cf-fca4-4a35-888f-004038710b54` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease A3 Offset threshold for 3218907_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[562] topology](images/train_0562.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227544_1
- `C2`: Decrease A3 Offset threshold for 3227544_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227544_1
- `C4`: Increase A3 Offset threshold for 3218907_2
- `C5`: Lift the tilt angle  of 3227544_1 by 10 degrees
- `C6`: Increase A3 Offset threshold for 3227544_1
- `C7`: Lift the tilt angle of 3218907_2 by 3 degrees
- `C8`: Decrease A3 Offset threshold for 3218907_2 **← 정답**
- `C9`: Press down the tilt angle of 3218907_2 by 3 degrees
- `C10`: Decrease transmission power for 3227544_1
- `C11`: Check test server and transmission issues
- `C12`: Press down the tilt angle  of 3227544_1 by 10 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218907_2
- `C14`: Increase transmission power for 3227544_1
- `C15`: Decrease transmission power for 3218907_2
- `C16`: Adjust the azimuth of 3227544_1 by 30 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218907_2
- `C18`: Add neighbor relationship between 3210945_3 and 3227544_1
- `C19`: Adjust the azimuth of 3218907_2 by 50 degrees
- `C20`: Increase transmission power for 3218907_2
- `C21`: Add neighbor relationship between 3218907_2 and 3227544_1
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.114 | MS1 | 121.4656728705 | 31.1446369811 | 1003 | 504990 | -80.74 | 16.75 | 419.01 | 0.03 | 2.55 | 1600 |
| 2024-09-20 22:21:32.140 | MS1 | 121.4656589762 | 31.1446226651 | 1003 | 504990 | -80.91 | 12.47 | 345.07 | 0.08 | 2.20 | 1592 |
| 2024-09-20 22:21:33.342 | MS1 | 121.4656756938 | 31.1446367992 | 1003 | 504990 | -78.16 | 15.97 | 600.30 | 0.02 | 2.84 | 1583 |
| 2024-09-20 22:21:34.571 | MS1 | 121.4656603457 | 31.1446307384 | 1003 | 504990 | -85.53 | -4.00 | 30.53 | 0.01 | 1.36 | 1595 |
| 2024-09-20 22:21:35.820 | MS1 | 121.4656735410 | 31.1446215376 | 1003 | 504990 | -91.74 | -3.96 | 79.93 | 0.02 | 1.19 | 1569 |
| 2024-09-20 22:21:36.376 | MS1 | 121.4656657018 | 31.1446284805 | 1003 | 504990 | -85.07 | -3.04 | 43.43 | 0.01 | 1.27 | 1572 |
| 2024-09-20 22:21:37.494 | MS1 | 121.4656766416 | 31.1446207528 | 1003 | 504990 | -91.90 | -3.85 | 78.85 | 0.14 | 1.50 | 1599 |
| 2024-09-20 22:21:38.938 | MS1 | 121.4656624820 | 31.1446275914 | 1003 | 504990 | -90.50 | -0.89 | 28.25 | 0.09 | 1.22 | 1597 |
| 2024-09-20 22:21:39.625 | MS1 | 121.4656706528 | 31.1446266459 | 992 | 504990 | -80.27 | 13.56 | 163.65 | 0.11 | 1.08 | 1568 |
| 2024-09-20 22:21:40.395 | MS1 | 121.4656730145 | 31.1446372213 | 992 | 504990 | -79.59 | 12.92 | 305.13 | 0.17 | 2.11 | 1585 |
| 2024-09-20 22:21:41.903 | MS1 | 121.4656701853 | 31.1446277523 | 992 | 504990 | -77.27 | 13.52 | 584.09 | 0.12 | 2.09 | 1585 |
| 2024-09-20 22:21:42.408 | MS1 | 121.4656613984 | 31.1446214241 | 992 | 504990 | -77.06 | 12.20 | 542.24 | 0.11 | 2.59 | 1591 |

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
| 3210945 | 3 | 121.4724145130 | 31.1463889603 | 165 | 12 | 2 | 41.3 | TDD | 102 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3218907 | 2 | 121.4649351867 | 31.1484209351 | 347 | 0 | 6 | 21.4 | TDD | 1003 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3227544 | 1 | 121.4643654198 | 31.1509639913 | 140 | 14 | 12 | 25.1 | TDD | 992 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3278569 | 4 | 121.4736207467 | 31.1538222077 | 72 | 1 | 7 | 23.5 | TDD | 199 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.776 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.794 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.920 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.920 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.649 | NREventA3 | measId:2;ServCellPCI:208;Se... |
| 2024-09-20 22:21:37.889 | NRHandoverAttempt | SourcePCI:208;SourceNR-ARFC... |
| 2024-09-20 22:21:37.933 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.948 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.051 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.051 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227544 | 1 | 19.9562 | 14.3024 | -115.7519 | 16.0849 | 101.5077 | 0.0009 | 0.0158 |
| 2024_09_20 22:00 | 3218907 | 2 | 5.6208 | 16.1054 | -116.0476 | 15.3036 | 199.7185 | 0.0143 | 0.1776 |
| 2024_09_20 22:00 | 3210945 | 3 | 18.6858 | 7.0884 | -115.9967 | 16.0894 | 184.9558 | 0.0081 | 0.0159 |
| 2024_09_20 22:00 | 3278569 | 4 | 5.0378 | 6.2948 | -114.4618 | 14.7730 | 182.6358 | 0.0124 | 0.0030 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415803_C72CCA5F | 504990 | 1003 | -87.3 | 504990 | 992 | -80.9 | 504990 | 102 | -89.5 | 504990 | 199 |
| MR_1774415803_547FD859 | 504990 | 1003 | -84.4 | 504990 | 992 | -79.0 | 504990 | 102 | -87.6 | 504990 | 199 |
| MR_1774415803_6890F242 | 504990 | 992 | -79.2 | 504990 | 1003 | -85.5 | 504990 | 102 | -88.0 | 504990 | 199 |
| MR_1774415803_6AF5322E | 504990 | 992 | -82.6 | 504990 | 1003 | -87.5 | 504990 | 102 | -88.6 | 504990 | 199 |
| MR_1774415803_1B83486E | 504990 | 992 | -81.2 | 504990 | 1003 | -84.7 | 504990 | 102 | -86.3 | 504990 | 199 |
| MR_1774415803_7582BE99 | 504990 | 1003 | -84.1 | 504990 | 992 | -82.0 | 504990 | 102 | -89.9 | 504990 | 199 |
| MR_1774415803_388DD78F | 504990 | 992 | -81.6 | 504990 | 1003 | -87.5 | 504990 | 102 | -87.4 | 504990 | 199 |
| MR_1774415803_BE652DCB | 504990 | 1003 | -84.3 | 504990 | 992 | -81.7 | 504990 | 102 | -88.0 | 504990 | 199 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 563: `8c185e62-cd5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8c185e62-cd52-4465-a0ef-0a806e136ea8` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Lift the tilt angle  of 3263769_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[563] topology](images/train_0563.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233523_4
- `C2`: Increase transmission power for 3256221_3
- `C3`: Press down the tilt angle of 3256221_3 by 4 degrees
- `C4`: Increase transmission power for 3233523_4
- `C5`: Press down the tilt angle  of 3263769_1 by 10 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256221_3
- `C8`: Increase A3 Offset threshold for 3256221_3
- `C9`: Check test server and transmission issues
- `C10`: Decrease transmission power for 3233523_4
- `C11`: Adjust the azimuth of 3256221_3 by 40 degrees
- `C12`: Increase A3 Offset threshold for 3233523_4
- `C13`: Add neighbor relationship between 3256221_3 and 3233523_4
- `C14`: Lift the tilt angle  of 3263769_1 by 10 degrees **← 정답**
- `C15`: Decrease transmission power for 3256221_3
- `C16`: Decrease A3 Offset threshold for 3233523_4
- `C17`: Add neighbor relationship between 3263769_1 and 3233523_4
- `C18`: Decrease A3 Offset threshold for 3256221_3
- `C19`: Lift the tilt angle of 3256221_3 by 4 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256221_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233523_4
- `C22`: Adjust the azimuth of 3263769_1 by 40 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.469 | MS1 | 121.4656676057 | 31.1446315809 | 846 | 504990 | -88.09 | 16.81 | 592.50 | 0.18 | 2.51 | 1586 |
| 2024-09-20 22:21:32.665 | MS1 | 121.4656648500 | 31.1446208442 | 846 | 504990 | -87.77 | 17.01 | 496.70 | 0.06 | 2.43 | 1597 |
| 2024-09-20 22:21:33.748 | MS1 | 121.4656613719 | 31.1446275204 | 846 | 504990 | -85.77 | 13.07 | 418.35 | 0.13 | 2.55 | 1575 |
| 2024-09-20 22:21:34.379 | MS1 | 121.4656741327 | 31.1446309043 | 846 | 504990 | -85.43 | 16.27 | 69.38 | 0.14 | 2.48 | 1564 |
| 2024-09-20 22:21:35.475 | MS1 | 121.4656772342 | 31.1446353412 | 846 | 504990 | -88.88 | 15.12 | 58.73 | 0.05 | 2.51 | 1591 |
| 2024-09-20 22:21:36.827 | MS1 | 121.4656742266 | 31.1446361531 | 846 | 504990 | -90.46 | 16.59 | 72.09 | 0.09 | 2.05 | 1568 |
| 2024-09-20 22:21:37.729 | MS1 | 121.4656606227 | 31.1446315973 | 846 | 504990 | -93.75 | 12.17 | 95.46 | 0.07 | 2.10 | 1574 |
| 2024-09-20 22:21:38.686 | MS1 | 121.4656683962 | 31.1446378384 | 846 | 504990 | -90.81 | 7.42 | 63.29 | 0.12 | 2.67 | 1587 |
| 2024-09-20 22:21:39.568 | MS1 | 121.4656729047 | 31.1446186200 | 846 | 504990 | -90.64 | 10.53 | 57.51 | 0.14 | 2.16 | 1574 |
| 2024-09-20 22:21:40.642 | MS1 | 121.4656747365 | 31.1446242308 | 846 | 504990 | -92.98 | 8.09 | 552.74 | 0.07 | 2.97 | 1584 |
| 2024-09-20 22:21:41.362 | MS1 | 121.4656585463 | 31.1446246230 | 846 | 504990 | -93.78 | 7.12 | 307.17 | 0.04 | 2.61 | 1590 |
| 2024-09-20 22:21:42.169 | MS1 | 121.4656767695 | 31.1446366354 | 846 | 504990 | -92.56 | 7.72 | 332.17 | 0.09 | 2.96 | 1560 |

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
| 3223665 | 2 | 121.4653598162 | 31.1451770181 | 162 | 14 | 10 | 30.5 | TDD | 729 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3233523 | 4 | 121.4703001255 | 31.1488027384 | 263 | 8 | 4 | 46.0 | TDD | 247 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3256221 | 3 | 121.4746088981 | 31.1496480114 | 277 | 3 | 3 | 15.2 | TDD | 846 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3263769 | 1 | 121.4745929180 | 31.1470989880 | 103 | 5 | 1 | 33.1 | TDD | 880 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.163 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.181 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.317 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.317 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.963 | NREventA3 | measId:2;ServCellPCI:229;Se... |
| 2024-09-20 22:21:38.203 | NRHandoverAttempt | SourcePCI:229;SourceNR-ARFC... |
| 2024-09-20 22:21:38.237 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.248 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.363 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.363 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263769 | 1 | 11.7922 | 18.1463 | -117.0914 | 13.3624 | 181.1149 | 0.0099 | 0.0042 |
| 2024_09_20 22:00 | 3223665 | 2 | 7.2545 | 17.1256 | -117.2345 | 9.4227 | 142.1990 | 0.0149 | 0.0035 |
| 2024_09_20 22:00 | 3256221 | 3 | 78.4624 | 80.2641 | -116.5092 | 5.4516 | 153.3767 | 0.0087 | 0.0057 |
| 2024_09_20 22:00 | 3233523 | 4 | 7.3306 | 5.6362 | -114.1338 | 9.7763 | 182.6541 | 0.0164 | 0.0090 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412735_B2A450A2 | 504990 | 846 | -84.4 | 504990 | 247 | -89.1 | 504990 | 880 | -95.7 | 504990 | 729 |
| MR_1774412735_8D4E5AB6 | 504990 | 846 | -83.5 | 504990 | 247 | -87.6 | 504990 | 880 | -96.5 | 504990 | 729 |
| MR_1774412735_E39F1F57 | 504990 | 846 | -83.8 | 504990 | 247 | -86.9 | 504990 | 880 | -98.6 | 504990 | 729 |
| MR_1774412735_8DBE8248 | 504990 | 846 | -84.8 | 504990 | 247 | -87.1 | 504990 | 880 | -96.8 | 504990 | 729 |
| MR_1774412735_66591D55 | 504990 | 846 | -85.8 | 504990 | 247 | -88.4 | 504990 | 880 | -99.2 | 504990 | 729 |
| MR_1774412735_EE0F693D | 504990 | 846 | -84.5 | 504990 | 247 | -88.7 | 504990 | 880 | -98.8 | 504990 | 729 |
| MR_1774412735_BB2E429E | 504990 | 846 | -84.5 | 504990 | 247 | -88.7 | 504990 | 880 | -97.4 | 504990 | 729 |
| MR_1774412735_648FDE3B | 504990 | 846 | -85.7 | 504990 | 247 | -86.8 | 504990 | 880 | -96.9 | 504990 | 729 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 564: `cc96722e-b40...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cc96722e-b40a-4e02-adba-889e46eb0278` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease A3 Offset threshold for 3261762_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[564] topology](images/train_0564.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3261762_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261560_3
- `C3`: Lift the tilt angle of 3261762_1 by 10 degrees
- `C4`: Increase A3 Offset threshold for 3261762_1
- `C5`: Add neighbor relationship between 3261762_1 and 3261560_3
- `C6`: Decrease A3 Offset threshold for 3261762_1 **← 정답**
- `C7`: Add neighbor relationship between 3270025_2 and 3261560_3
- `C8`: Lift the tilt angle  of 3261560_3 by 10 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261560_3
- `C10`: Increase transmission power for 3261560_3
- `C11`: Check test server and transmission issues
- `C12`: Adjust the azimuth of 3261762_1 by 50 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261762_1
- `C14`: Decrease transmission power for 3261560_3
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Increase A3 Offset threshold for 3261560_3
- `C17`: Decrease A3 Offset threshold for 3261560_3
- `C18`: Press down the tilt angle of 3261762_1 by 10 degrees
- `C19`: Press down the tilt angle  of 3261560_3 by 10 degrees
- `C20`: Adjust the azimuth of 3261560_3 by 50 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261762_1
- `C22`: Increase transmission power for 3261762_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.302 | MS1 | 121.4656663184 | 31.1446369454 | 999 | 504990 | -84.57 | 12.81 | 310.97 | 0.12 | 2.74 | 1583 |
| 2024-09-20 22:21:32.506 | MS1 | 121.4656611402 | 31.1446266726 | 999 | 504990 | -75.83 | 17.18 | 478.32 | 0.02 | 2.26 | 1570 |
| 2024-09-20 22:21:33.272 | MS1 | 121.4656591285 | 31.1446266393 | 999 | 504990 | -75.42 | 13.50 | 536.06 | 0.04 | 2.03 | 1596 |
| 2024-09-20 22:21:34.421 | MS1 | 121.4656590436 | 31.1446184169 | 999 | 504990 | -87.41 | -1.77 | 62.02 | 0.18 | 1.14 | 1578 |
| 2024-09-20 22:21:35.924 | MS1 | 121.4656677805 | 31.1446215910 | 999 | 504990 | -90.52 | -2.29 | 66.84 | 0.19 | 1.43 | 1581 |
| 2024-09-20 22:21:36.446 | MS1 | 121.4656648233 | 31.1446193781 | 999 | 504990 | -90.27 | -1.18 | 60.69 | 0.17 | 1.26 | 1563 |
| 2024-09-20 22:21:37.283 | MS1 | 121.4656724499 | 31.1446182866 | 999 | 504990 | -90.35 | -0.60 | 46.39 | 0.11 | 1.07 | 1574 |
| 2024-09-20 22:21:38.983 | MS1 | 121.4656757643 | 31.1446264193 | 999 | 504990 | -86.79 | -1.72 | 48.46 | 0.10 | 1.19 | 1565 |
| 2024-09-20 22:21:39.338 | MS1 | 121.4656674901 | 31.1446211175 | 293 | 504990 | -79.64 | 14.84 | 247.76 | 0.05 | 1.19 | 1565 |
| 2024-09-20 22:21:40.875 | MS1 | 121.4656586252 | 31.1446216488 | 293 | 504990 | -77.18 | 14.65 | 607.76 | 0.06 | 2.20 | 1561 |
| 2024-09-20 22:21:41.447 | MS1 | 121.4656758470 | 31.1446199811 | 293 | 504990 | -76.25 | 15.44 | 356.61 | 0.03 | 2.49 | 1576 |
| 2024-09-20 22:21:42.485 | MS1 | 121.4656693858 | 31.1446273171 | 293 | 504990 | -79.34 | 14.96 | 447.49 | 0.16 | 2.66 | 1579 |

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
| 3261560 | 3 | 121.4658020019 | 31.1549830692 | 99 | 11 | 7 | 18.8 | TDD | 293 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3261762 | 1 | 121.4751828333 | 31.1482180902 | 116 | 12 | 2 | 34.3 | TDD | 999 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3270025 | 2 | 121.4705259715 | 31.1520104610 | 8 | 4 | 4 | 44.8 | TDD | 868 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3274334 | 4 | 121.4731225117 | 31.1474514864 | 86 | 10 | 8 | 32.9 | TDD | 183 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.853 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.875 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.976 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.976 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.748 | NREventA3 | measId:2;ServCellPCI:757;Se... |
| 2024-09-20 22:21:37.988 | NRHandoverAttempt | SourcePCI:757;SourceNR-ARFC... |
| 2024-09-20 22:21:38.018 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.033 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.138 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.138 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261762 | 1 | 13.0208 | 8.8427 | -114.4118 | 5.4845 | 156.4805 | 0.0181 | 0.1731 |
| 2024_09_20 22:00 | 3270025 | 2 | 7.8620 | 15.7627 | -114.2929 | 12.0570 | 137.9821 | 0.0122 | 0.0124 |
| 2024_09_20 22:00 | 3261560 | 3 | 16.8229 | 10.0759 | -114.2211 | 11.4343 | 119.3794 | 0.0131 | 0.0126 |
| 2024_09_20 22:00 | 3274334 | 4 | 13.3191 | 5.3222 | -117.6434 | 7.6550 | 87.0087 | 0.0108 | 0.0133 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414857_219FFADC | 504990 | 999 | -87.1 | 504990 | 293 | -83.0 | 504990 | 868 | -83.8 | 504990 | 183 |
| MR_1774414857_AC2D4670 | 504990 | 293 | -82.9 | 504990 | 999 | -89.4 | 504990 | 868 | -82.2 | 504990 | 183 |
| MR_1774414857_3233BAEC | 504990 | 999 | -88.6 | 504990 | 293 | -82.8 | 504990 | 868 | -82.3 | 504990 | 183 |
| MR_1774414857_61AE8ACD | 504990 | 293 | -83.0 | 504990 | 999 | -86.0 | 504990 | 868 | -85.1 | 504990 | 183 |
| MR_1774414857_91012BB0 | 504990 | 999 | -87.3 | 504990 | 293 | -84.8 | 504990 | 868 | -83.4 | 504990 | 183 |
| MR_1774414857_8E8906E2 | 504990 | 293 | -81.9 | 504990 | 999 | -88.9 | 504990 | 868 | -84.0 | 504990 | 183 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 565: `bbe199d3-833...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bbe199d3-8330-4507-9df3-f70f574ae84e` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Lift the tilt angle  of 3215949_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[565] topology](images/train_0565.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3271553_2 by 11 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271553_2
- `C3`: Check test server and transmission issues
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229445_1
- `C5`: Adjust the azimuth of 3215949_3 by 50 degrees
- `C6`: Increase transmission power for 3229445_1
- `C7`: Decrease transmission power for 3271553_2
- `C8`: Add neighbor relationship between 3271553_2 and 3229445_1
- `C9`: Decrease A3 Offset threshold for 3271553_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease transmission power for 3229445_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229445_1
- `C13`: Increase A3 Offset threshold for 3271553_2
- `C14`: Lift the tilt angle  of 3215949_3 by 10 degrees **← 정답**
- `C15`: Increase transmission power for 3271553_2
- `C16`: Increase A3 Offset threshold for 3229445_1
- `C17`: Press down the tilt angle  of 3215949_3 by 10 degrees
- `C18`: Press down the tilt angle of 3271553_2 by 4 degrees
- `C19`: Add neighbor relationship between 3215949_3 and 3229445_1
- `C20`: Decrease A3 Offset threshold for 3229445_1
- `C21`: Lift the tilt angle of 3271553_2 by 4 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271553_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.800 | MS1 | 121.4656695592 | 31.1446307497 | 325 | 504990 | -87.77 | 13.98 | 369.22 | 0.00 | 2.39 | 1600 |
| 2024-09-20 22:21:32.832 | MS1 | 121.4656638903 | 31.1446339202 | 325 | 504990 | -85.51 | 14.09 | 458.30 | 0.18 | 2.66 | 1586 |
| 2024-09-20 22:21:33.355 | MS1 | 121.4656736362 | 31.1446333442 | 325 | 504990 | -90.51 | 14.92 | 591.96 | 0.15 | 2.86 | 1585 |
| 2024-09-20 22:21:34.201 | MS1 | 121.4656596063 | 31.1446373588 | 325 | 504990 | -86.04 | 15.44 | 75.18 | 0.01 | 2.93 | 1573 |
| 2024-09-20 22:21:35.276 | MS1 | 121.4656665467 | 31.1446361361 | 325 | 504990 | -89.54 | 17.79 | 51.39 | 0.11 | 2.02 | 1574 |
| 2024-09-20 22:21:36.451 | MS1 | 121.4656616985 | 31.1446228177 | 325 | 504990 | -85.62 | 12.34 | 59.33 | 0.06 | 2.01 | 1564 |
| 2024-09-20 22:21:37.600 | MS1 | 121.4656726888 | 31.1446247560 | 325 | 504990 | -91.02 | 9.86 | 73.21 | 0.18 | 2.81 | 1571 |
| 2024-09-20 22:21:38.415 | MS1 | 121.4656767531 | 31.1446216568 | 325 | 504990 | -90.81 | 11.76 | 102.82 | 0.19 | 2.77 | 1562 |
| 2024-09-20 22:21:39.755 | MS1 | 121.4656682584 | 31.1446371684 | 325 | 504990 | -89.83 | 10.72 | 79.97 | 0.04 | 2.06 | 1571 |
| 2024-09-20 22:21:40.411 | MS1 | 121.4656779883 | 31.1446347469 | 325 | 504990 | -93.48 | 11.93 | 429.90 | 0.07 | 2.55 | 1593 |
| 2024-09-20 22:21:41.455 | MS1 | 121.4656591791 | 31.1446307366 | 325 | 504990 | -90.73 | 11.48 | 363.14 | 0.00 | 2.62 | 1588 |
| 2024-09-20 22:21:42.470 | MS1 | 121.4656591496 | 31.1446326534 | 325 | 504990 | -89.27 | 12.20 | 479.95 | 0.13 | 2.72 | 1560 |

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
| 3215949 | 3 | 121.4695257896 | 31.1474683119 | 59 | 15 | 12 | 45.4 | TDD | 813 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3229445 | 1 | 121.4743813366 | 31.1555903131 | 96 | 9 | 6 | 40.1 | TDD | 290 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3255319 | 4 | 121.4745477450 | 31.1472084588 | 90 | 5 | 1 | 32.4 | TDD | 398 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3271553 | 2 | 121.4688282277 | 31.1498713336 | 196 | 1 | 4 | 36.2 | TDD | 325 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.519 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.519 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.248 | NREventA3 | measId:2;ServCellPCI:545;Se... |
| 2024-09-20 22:21:38.488 | NRHandoverAttempt | SourcePCI:545;SourceNR-ARFC... |
| 2024-09-20 22:21:38.534 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.548 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.680 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.680 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229445 | 1 | 15.0661 | 7.1284 | -114.6736 | 15.8764 | 153.9538 | 0.0103 | 0.0078 |
| 2024_09_20 22:00 | 3271553 | 2 | 77.7553 | 76.3493 | -115.7408 | 8.5303 | 143.8404 | 0.0056 | 0.0043 |
| 2024_09_20 22:00 | 3215949 | 3 | 8.2233 | 12.0924 | -117.6854 | 17.8686 | 141.4036 | 0.0181 | 0.0006 |
| 2024_09_20 22:00 | 3255319 | 4 | 17.0675 | 7.6637 | -117.4981 | 17.8325 | 115.2460 | 0.0078 | 0.0051 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416786_F17B6B7D | 504990 | 325 | -86.1 | 504990 | 290 | -88.1 | 504990 | 813 | -98.1 | 504990 | 398 |
| MR_1774416786_B8A3091D | 504990 | 325 | -85.9 | 504990 | 290 | -85.6 | 504990 | 813 | -97.5 | 504990 | 398 |
| MR_1774416786_B138CAE2 | 504990 | 325 | -85.4 | 504990 | 290 | -85.5 | 504990 | 813 | -96.7 | 504990 | 398 |
| MR_1774416786_7303DF6E | 504990 | 325 | -87.6 | 504990 | 290 | -87.1 | 504990 | 813 | -98.5 | 504990 | 398 |
| MR_1774416786_14B6A9EB | 504990 | 325 | -86.0 | 504990 | 290 | -88.0 | 504990 | 813 | -98.4 | 504990 | 398 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 566: `c966fbae-aee...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c966fbae-aeee-44c6-ae71-03b336346924` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Add neighbor relationship between 3231412_3 and 3246093_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[566] topology](images/train_0566.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231412_3
- `C2`: Lift the tilt angle of 3231412_3 by 4 degrees
- `C3`: Decrease transmission power for 3231412_3
- `C4`: Add neighbor relationship between 3263408_4 and 3246093_1
- `C5`: Increase transmission power for 3246093_1
- `C6`: Decrease transmission power for 3246093_1
- `C7`: Decrease A3 Offset threshold for 3231412_3
- `C8`: Increase A3 Offset threshold for 3231412_3
- `C9`: Adjust the azimuth of 3246093_1 by 21 degrees
- `C10`: Adjust the azimuth of 3231412_3 by 50 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231412_3
- `C12`: Lift the tilt angle  of 3246093_1 by 4 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246093_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease A3 Offset threshold for 3246093_1
- `C16`: Add neighbor relationship between 3231412_3 and 3246093_1 **← 정답**
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246093_1
- `C18`: Increase A3 Offset threshold for 3246093_1
- `C19`: Increase transmission power for 3231412_3
- `C20`: Press down the tilt angle of 3231412_3 by 4 degrees
- `C21`: Press down the tilt angle  of 3246093_1 by 4 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.348 | MS1 | 121.4656602456 | 31.1446354908 | 605 | 504990 | -78.22 | 12.40 | 539.14 | 0.05 | 2.59 | 1567 |
| 2024-09-20 22:21:32.829 | MS1 | 121.4656737733 | 31.1446323734 | 605 | 504990 | -83.50 | 14.22 | 570.83 | 0.09 | 2.78 | 1600 |
| 2024-09-20 22:21:33.975 | MS1 | 121.4656621900 | 31.1446255822 | 605 | 504990 | -78.91 | 16.55 | 445.85 | 0.20 | 2.62 | 1589 |
| 2024-09-20 22:21:34.667 | MS1 | 121.4656628581 | 31.1446223624 | 605 | 504990 | -88.55 | -1.33 | 63.84 | 0.01 | 1.48 | 1583 |
| 2024-09-20 22:21:35.360 | MS1 | 121.4656598181 | 31.1446201183 | 605 | 504990 | -85.33 | -1.81 | 42.09 | 0.18 | 1.04 | 1560 |
| 2024-09-20 22:21:36.668 | MS1 | 121.4656750275 | 31.1446342305 | 605 | 504990 | -85.20 | -0.23 | 24.95 | 0.18 | 1.19 | 1576 |
| 2024-09-20 22:21:37.967 | MS1 | 121.4656584193 | 31.1446260966 | 605 | 504990 | -90.25 | -3.50 | 72.97 | 0.10 | 1.14 | 1578 |
| 2024-09-20 22:21:38.883 | MS1 | 121.4656720455 | 31.1446375829 | 605 | 504990 | -84.68 | 12.07 | 520.78 | 0.05 | 1.10 | 1583 |
| 2024-09-20 22:21:39.214 | MS1 | 121.4656585542 | 31.1446330125 | 605 | 504990 | -82.68 | 12.20 | 355.62 | 0.12 | 1.03 | 1584 |
| 2024-09-20 22:21:40.923 | MS1 | 121.4656637283 | 31.1446235771 | 605 | 504990 | -75.46 | 14.13 | 584.58 | 0.16 | 2.76 | 1568 |
| 2024-09-20 22:21:41.816 | MS1 | 121.4656632173 | 31.1446215344 | 605 | 504990 | -80.96 | 12.90 | 547.57 | 0.05 | 2.83 | 1585 |
| 2024-09-20 22:21:42.999 | MS1 | 121.4656590336 | 31.1446321831 | 605 | 504990 | -76.85 | 12.45 | 461.52 | 0.15 | 2.73 | 1597 |

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
| 3214685 | 2 | 121.4714412137 | 31.1514455510 | 268 | 11 | 5 | 36.0 | TDD | 76 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3231412 | 3 | 121.4680046719 | 31.1499958522 | 294 | 2 | 6 | 19.2 | TDD | 605 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3246093 | 1 | 121.4734268108 | 31.1553652364 | 233 | 2 | 10 | 45.3 | TDD | 941 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3263408 | 4 | 121.4709281487 | 31.1451613362 | 72 | 7 | 11 | 38.4 | TDD | 588 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.012 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.029 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.129 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.129 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.822 | NREventA3 | measId:2;ServCellPCI:405;Se... |
| 2024-09-20 22:21:35.822 | NREventA3 | measId:2;ServCellPCI:405;Se... |
| 2024-09-20 22:21:36.822 | NREventA3 | measId:2;ServCellPCI:405;Se... |
| 2024-09-20 22:21:39.322 | NRRRCReestablishAttempt | PCI:405 |
| 2024-09-20 22:21:39.342 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.352 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.472 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.472 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246093 | 1 | 17.4728 | 12.4449 | -115.8384 | 16.6891 | 165.3237 | 0.0030 | 0.0124 |
| 2024_09_20 22:00 | 3214685 | 2 | 14.3123 | 5.6912 | -117.8687 | 15.3240 | 81.3659 | 0.0098 | 0.0144 |
| 2024_09_20 22:00 | 3231412 | 3 | 14.2956 | 7.9643 | -115.2681 | 13.5031 | 185.5500 | 0.0019 | 0.1352 |
| 2024_09_20 22:00 | 3263408 | 4 | 10.0146 | 16.1950 | -117.8425 | 16.6142 | 85.9916 | 0.0124 | 0.0055 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416083_10E63652 | 504990 | 941 | -82.3 | 504990 | 605 | -90.5 | 504990 | 588 | -89.4 | 504990 | 76 |
| MR_1774416083_78DCDE5A | 504990 | 605 | -88.0 | 504990 | 941 | -85.0 | 504990 | 588 | -87.6 | 504990 | 76 |
| MR_1774416083_440BE344 | 504990 | 605 | -87.6 | 504990 | 941 | -85.6 | 504990 | 588 | -86.7 | 504990 | 76 |
| MR_1774416083_5A52C6CF | 504990 | 941 | -86.0 | 504990 | 605 | -87.4 | 504990 | 588 | -88.0 | 504990 | 76 |
| MR_1774416083_175EACB6 | 504990 | 941 | -84.7 | 504990 | 605 | -88.2 | 504990 | 588 | -89.9 | 504990 | 76 |
| MR_1774416083_00D100A3 | 504990 | 605 | -89.7 | 504990 | 941 | -85.6 | 504990 | 588 | -88.9 | 504990 | 76 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 567: `eb72d93a-77e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `eb72d93a-77ee-4145-8f99-9bff3f13b1d0` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Add neighbor relationship between 3263383_2 and 3243016_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[567] topology](images/train_0567.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3263383_2 by 50 degrees
- `C2`: Increase A3 Offset threshold for 3243016_3
- `C3`: Add neighbor relationship between 3263383_2 and 3243016_3 **← 정답**
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263383_2
- `C5`: Press down the tilt angle  of 3243016_3 by 3 degrees
- `C6`: Increase A3 Offset threshold for 3263383_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243016_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243016_3
- `C9`: Decrease A3 Offset threshold for 3263383_2
- `C10`: Lift the tilt angle of 3263383_2 by 6 degrees
- `C11`: Lift the tilt angle  of 3243016_3 by 3 degrees
- `C12`: Decrease transmission power for 3243016_3
- `C13`: Increase transmission power for 3263383_2
- `C14`: Decrease transmission power for 3263383_2
- `C15`: Add neighbor relationship between 3230957_4 and 3243016_3
- `C16`: Adjust the azimuth of 3243016_3 by 8 degrees
- `C17`: Check test server and transmission issues
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263383_2
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease A3 Offset threshold for 3243016_3
- `C21`: Increase transmission power for 3243016_3
- `C22`: Press down the tilt angle of 3263383_2 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.937 | MS1 | 121.4656708935 | 31.1446215836 | 724 | 504990 | -77.31 | 12.58 | 335.16 | 0.16 | 2.51 | 1564 |
| 2024-09-20 22:21:32.962 | MS1 | 121.4656616467 | 31.1446334948 | 724 | 504990 | -84.66 | 12.31 | 480.63 | 0.12 | 2.19 | 1568 |
| 2024-09-20 22:21:33.307 | MS1 | 121.4656756023 | 31.1446251832 | 724 | 504990 | -84.77 | 17.87 | 318.58 | 0.17 | 2.07 | 1593 |
| 2024-09-20 22:21:34.174 | MS1 | 121.4656708875 | 31.1446318718 | 724 | 504990 | -94.43 | -2.78 | 67.55 | 0.08 | 1.41 | 1575 |
| 2024-09-20 22:21:35.754 | MS1 | 121.4656713595 | 31.1446201693 | 724 | 504990 | -89.72 | -1.15 | 40.18 | 0.16 | 1.14 | 1593 |
| 2024-09-20 22:21:36.992 | MS1 | 121.4656607679 | 31.1446322759 | 724 | 504990 | -88.29 | -1.00 | 31.33 | 0.14 | 1.24 | 1591 |
| 2024-09-20 22:21:37.949 | MS1 | 121.4656766887 | 31.1446333381 | 724 | 504990 | -91.26 | -2.87 | 66.49 | 0.10 | 1.04 | 1587 |
| 2024-09-20 22:21:38.218 | MS1 | 121.4656651493 | 31.1446218733 | 724 | 504990 | -76.65 | 14.73 | 527.08 | 0.18 | 1.39 | 1578 |
| 2024-09-20 22:21:39.500 | MS1 | 121.4656704915 | 31.1446193644 | 724 | 504990 | -83.89 | 18.00 | 374.23 | 0.18 | 1.21 | 1573 |
| 2024-09-20 22:21:40.617 | MS1 | 121.4656647816 | 31.1446231868 | 724 | 504990 | -75.24 | 13.26 | 485.90 | 0.00 | 2.29 | 1579 |
| 2024-09-20 22:21:41.135 | MS1 | 121.4656724631 | 31.1446358189 | 724 | 504990 | -84.83 | 14.35 | 314.85 | 0.06 | 2.17 | 1599 |
| 2024-09-20 22:21:42.451 | MS1 | 121.4656582110 | 31.1446273459 | 724 | 504990 | -80.54 | 12.55 | 371.43 | 0.15 | 2.53 | 1600 |

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
| 3230957 | 4 | 121.4657650785 | 31.1503698187 | 62 | 2 | 11 | 47.9 | TDD | 386 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3243016 | 3 | 121.4745077446 | 31.1485597268 | 251 | 2 | 3 | 22.3 | TDD | 436 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3245630 | 1 | 121.4647364763 | 31.1446560568 | 332 | 4 | 8 | 36.8 | TDD | 682 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3263383 | 2 | 121.4652652778 | 31.1511483880 | 296 | 4 | 1 | 20.7 | TDD | 724 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.518 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.538 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.660 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.660 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.325 | NREventA3 | measId:2;ServCellPCI:573;Se... |
| 2024-09-20 22:21:36.325 | NREventA3 | measId:2;ServCellPCI:573;Se... |
| 2024-09-20 22:21:37.325 | NREventA3 | measId:2;ServCellPCI:573;Se... |
| 2024-09-20 22:21:39.825 | NRRRCReestablishAttempt | PCI:573 |
| 2024-09-20 22:21:39.835 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.848 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.985 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.985 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245630 | 1 | 11.3865 | 7.1671 | -116.4302 | 10.8958 | 165.8441 | 0.0109 | 0.0005 |
| 2024_09_20 22:00 | 3263383 | 2 | 16.1811 | 13.3684 | -114.3843 | 12.3662 | 125.0712 | 0.0025 | 0.1534 |
| 2024_09_20 22:00 | 3243016 | 3 | 5.1479 | 8.4530 | -114.6335 | 9.2304 | 103.6887 | 0.0162 | 0.0181 |
| 2024_09_20 22:00 | 3230957 | 4 | 15.6007 | 13.3158 | -114.9002 | 12.6890 | 81.9102 | 0.0030 | 0.0059 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413854_37A72EB8 | 504990 | 724 | -95.7 | 504990 | 436 | -88.1 | 504990 | 386 | -93.0 | 504990 | 682 |
| MR_1774413854_06D505BF | 504990 | 724 | -92.6 | 504990 | 436 | -89.6 | 504990 | 386 | -91.4 | 504990 | 682 |
| MR_1774413854_55455BB3 | 504990 | 724 | -92.9 | 504990 | 436 | -91.9 | 504990 | 386 | -92.4 | 504990 | 682 |
| MR_1774413854_0E13BBC4 | 504990 | 724 | -93.0 | 504990 | 436 | -91.3 | 504990 | 386 | -91.8 | 504990 | 682 |
| MR_1774413854_3392A743 | 504990 | 436 | -89.1 | 504990 | 724 | -93.6 | 504990 | 386 | -94.8 | 504990 | 682 |
| MR_1774413854_23FA09AB | 504990 | 436 | -90.5 | 504990 | 724 | -95.9 | 504990 | 386 | -93.8 | 504990 | 682 |
| MR_1774413854_63871D8D | 504990 | 724 | -93.6 | 504990 | 436 | -89.6 | 504990 | 386 | -94.3 | 504990 | 682 |
| MR_1774413854_0EABD563 | 504990 | 724 | -94.8 | 504990 | 436 | -91.7 | 504990 | 386 | -93.9 | 504990 | 682 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 568: `83609a72-639...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `83609a72-6398-4c04-aa40-29184e7b83ef` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[568] topology](images/train_0568.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3268243_2 by 50 degrees
- `C2`: Decrease transmission power for 3265617_4
- `C3`: Decrease transmission power for 3268243_2
- `C4`: Press down the tilt angle of 3265617_4 by 10 degrees
- `C5`: Increase transmission power for 3268243_2
- `C6`: Lift the tilt angle of 3265617_4 by 10 degrees
- `C7`: Lift the tilt angle  of 3268243_2 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3268243_2
- `C9`: Press down the tilt angle  of 3268243_2 by 10 degrees
- `C10`: Add neighbor relationship between 3265617_4 and 3268243_2
- `C11`: Decrease A3 Offset threshold for 3265617_4
- `C12`: Increase transmission power for 3265617_4
- `C13`: Insufficient data; more data is needed for judgment. **← 정답**
- `C14`: Add neighbor relationship between 3261530_1 and 3268243_2
- `C15`: Increase A3 Offset threshold for 3265617_4
- `C16`: Check test server and transmission issues
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268243_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265617_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265617_4
- `C20`: Adjust the azimuth of 3265617_4 by 50 degrees
- `C21`: Increase A3 Offset threshold for 3268243_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268243_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.685 | MS1 | 121.4656719417 | 31.1446223966 | 87 | 504990 | -86.47 | 12.37 | 340.05 | 0.05 | 2.94 | 1588 |
| 2024-09-20 22:21:32.551 | MS1 | 121.4656608027 | 31.1446313083 | 87 | 504990 | -88.23 | 17.28 | 352.03 | 0.18 | 2.42 | 1582 |
| 2024-09-20 22:21:33.718 | MS1 | 121.4656656907 | 31.1446324383 | 87 | 504990 | -87.12 | 17.95 | 539.59 | 0.04 | 2.38 | 1573 |
| 2024-09-20 22:21:34.980 | MS1 | 121.4656709781 | 31.1446338995 | 87 | 504990 | -86.77 | 13.12 | 81.92 | 0.18 | 2.66 | 1599 |
| 2024-09-20 22:21:35.112 | MS1 | 121.4656629318 | 31.1446251358 | 87 | 504990 | -87.91 | 14.11 | 81.81 | 0.12 | 2.75 | 1579 |
| 2024-09-20 22:21:36.455 | MS1 | 121.4656673992 | 31.1446321286 | 87 | 504990 | -89.02 | 13.10 | 45.43 | 0.18 | 2.04 | 1595 |
| 2024-09-20 22:21:37.759 | MS1 | 121.4656593846 | 31.1446333824 | 87 | 504990 | -93.16 | 11.03 | 56.21 | 0.04 | 2.22 | 1588 |
| 2024-09-20 22:21:38.622 | MS1 | 121.4656616310 | 31.1446273193 | 87 | 504990 | -93.82 | 8.69 | 51.45 | 0.17 | 2.98 | 1567 |
| 2024-09-20 22:21:39.171 | MS1 | 121.4656693816 | 31.1446194497 | 87 | 504990 | -91.00 | 12.52 | 53.34 | 0.18 | 2.08 | 1581 |
| 2024-09-20 22:21:40.496 | MS1 | 121.4656644045 | 31.1446379356 | 87 | 504990 | -93.44 | 10.11 | 329.92 | 0.19 | 2.29 | 1593 |
| 2024-09-20 22:21:41.524 | MS1 | 121.4656751895 | 31.1446273069 | 87 | 504990 | -93.03 | 9.11 | 471.68 | 0.10 | 2.04 | 1600 |
| 2024-09-20 22:21:42.822 | MS1 | 121.4656655743 | 31.1446333863 | 87 | 504990 | -93.02 | 11.30 | 338.90 | 0.19 | 2.96 | 1575 |

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
| 3261530 | 1 | 121.4663775062 | 31.1495178370 | 10 | 10 | 6 | 19.6 | TDD | 705 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3265617 | 4 | 121.4741328466 | 31.1498328614 | 114 | 12 | 8 | 46.0 | TDD | 87 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3268243 | 2 | 121.4660266231 | 31.1458734470 | 42 | 7 | 11 | 45.0 | TDD | 812 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3272561 | 3 | 121.4692812420 | 31.1466106854 | 181 | 11 | 7 | 46.1 | TDD | 261 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.456 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.474 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.605 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.605 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.263 | NREventA3 | measId:2;ServCellPCI:110;Se... |
| 2024-09-20 22:21:38.503 | NRHandoverAttempt | SourcePCI:110;SourceNR-ARFC... |
| 2024-09-20 22:21:38.552 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.566 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.682 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.682 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3261530 | 1 | 80.8458 | 84.5807 | -116.4208 | 14.5612 | 189.5265 | 0.0068 | 0.0081 |
| 2024_09_19 22:00 | 3268243 | 2 | 88.2661 | 86.5383 | -115.2877 | 18.4140 | 143.8341 | 0.0122 | 0.0058 |
| 2024_09_19 22:00 | 3272561 | 3 | 84.7631 | 85.5588 | -115.9179 | 8.3112 | 164.6765 | 0.0189 | 0.0005 |
| 2024_09_19 22:00 | 3265617 | 4 | 75.0852 | 81.5396 | -114.7699 | 5.2017 | 135.7280 | 0.0033 | 0.0188 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416156_DAA602E9 | 504990 | 87 | -86.1 | 504990 | 812 | -90.5 | 504990 | 705 | -102.1 | 504990 | 261 |
| MR_1774416156_EB88FB43 | 504990 | 87 | -87.4 | 504990 | 812 | -91.7 | 504990 | 705 | -99.4 | 504990 | 261 |
| MR_1774416156_0877544B | 504990 | 87 | -85.5 | 504990 | 812 | -92.8 | 504990 | 705 | -102.1 | 504990 | 261 |
| MR_1774416156_E5E4F7A6 | 504990 | 87 | -86.5 | 504990 | 812 | -90.9 | 504990 | 705 | -99.0 | 504990 | 261 |
| MR_1774416156_B9117A6C | 504990 | 87 | -85.9 | 504990 | 812 | -93.3 | 504990 | 705 | -101.2 | 504990 | 261 |
| MR_1774416156_BCF99D0D | 504990 | 87 | -88.5 | 504990 | 812 | -91.2 | 504990 | 705 | -101.2 | 504990 | 261 |
| MR_1774416156_22B7505E | 504990 | 87 | -86.3 | 504990 | 812 | -90.5 | 504990 | 705 | -99.6 | 504990 | 261 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 569: `0ef23a21-6ed...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0ef23a21-6ed2-4b94-978a-92d4c322de8d` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[569] topology](images/train_0569.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3216639_1
- `C2`: Decrease transmission power for 3216639_1
- `C3`: Decrease transmission power for 3248725_2
- `C4`: Insufficient data; more data is needed for judgment. **← 정답**
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216639_1
- `C6`: Decrease A3 Offset threshold for 3248725_2
- `C7`: Increase transmission power for 3248725_2
- `C8`: Lift the tilt angle  of 3248725_2 by 10 degrees
- `C9`: Press down the tilt angle of 3216639_1 by 10 degrees
- `C10`: Decrease A3 Offset threshold for 3216639_1
- `C11`: Increase transmission power for 3216639_1
- `C12`: Add neighbor relationship between 3216639_1 and 3248725_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216639_1
- `C14`: Add neighbor relationship between 3223187_4 and 3248725_2
- `C15`: Adjust the azimuth of 3216639_1 by 50 degrees
- `C16`: Adjust the azimuth of 3248725_2 by 50 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248725_2
- `C18`: Press down the tilt angle  of 3248725_2 by 10 degrees
- `C19`: Check test server and transmission issues
- `C20`: Lift the tilt angle of 3216639_1 by 10 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248725_2
- `C22`: Increase A3 Offset threshold for 3248725_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.524 | MS1 | 121.4656771589 | 31.1446234924 | 61 | 504990 | -85.21 | 12.07 | 547.68 | 0.13 | 2.19 | 1584 |
| 2024-09-20 22:21:32.757 | MS1 | 121.4656716752 | 31.1446252722 | 61 | 504990 | -85.69 | 12.16 | 599.51 | 0.10 | 2.75 | 1573 |
| 2024-09-20 22:21:33.481 | MS1 | 121.4656586297 | 31.1446333808 | 61 | 504990 | -86.71 | 16.76 | 394.20 | 0.10 | 2.98 | 1566 |
| 2024-09-20 22:21:34.184 | MS1 | 121.4656678313 | 31.1446351594 | 61 | 504990 | -86.74 | 14.33 | 72.54 | 0.12 | 2.57 | 1598 |
| 2024-09-20 22:21:35.833 | MS1 | 121.4656747610 | 31.1446232725 | 61 | 504990 | -90.90 | 16.78 | 88.32 | 0.18 | 2.38 | 1599 |
| 2024-09-20 22:21:36.782 | MS1 | 121.4656738802 | 31.1446220939 | 61 | 504990 | -88.60 | 17.49 | 48.55 | 0.01 | 2.48 | 1589 |
| 2024-09-20 22:21:37.527 | MS1 | 121.4656742462 | 31.1446235610 | 61 | 504990 | -93.28 | 12.01 | 95.80 | 0.18 | 2.21 | 1575 |
| 2024-09-20 22:21:38.736 | MS1 | 121.4656615117 | 31.1446180579 | 61 | 504990 | -92.11 | 8.35 | 74.70 | 0.08 | 2.21 | 1564 |
| 2024-09-20 22:21:39.507 | MS1 | 121.4656774642 | 31.1446365214 | 61 | 504990 | -91.88 | 11.92 | 68.47 | 0.14 | 2.46 | 1566 |
| 2024-09-20 22:21:40.156 | MS1 | 121.4656764862 | 31.1446327407 | 61 | 504990 | -91.33 | 10.16 | 449.76 | 0.12 | 2.05 | 1560 |
| 2024-09-20 22:21:41.282 | MS1 | 121.4656582899 | 31.1446318073 | 61 | 504990 | -93.39 | 8.31 | 298.31 | 0.19 | 2.49 | 1596 |
| 2024-09-20 22:21:42.185 | MS1 | 121.4656738863 | 31.1446232613 | 61 | 504990 | -91.91 | 10.31 | 466.57 | 0.06 | 2.02 | 1598 |

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
| 3216639 | 1 | 121.4702983469 | 31.1503465429 | 27 | 12 | 10 | 26.1 | TDD | 61 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3223187 | 4 | 121.4670758250 | 31.1451558527 | 267 | 14 | 7 | 33.6 | TDD | 445 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3224195 | 3 | 121.4685999118 | 31.1479879053 | 203 | 1 | 5 | 20.3 | TDD | 509 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3248725 | 2 | 121.4682239101 | 31.1524910791 | 314 | 10 | 9 | 23.5 | TDD | 731 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.385 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.404 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.546 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.546 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.241 | NREventA3 | measId:2;ServCellPCI:486;Se... |
| 2024-09-20 22:21:38.481 | NRHandoverAttempt | SourcePCI:486;SourceNR-ARFC... |
| 2024-09-20 22:21:38.519 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.533 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.641 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.641 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3216639 | 1 | 83.6465 | 75.9800 | -117.9216 | 16.1838 | 157.8646 | 0.0019 | 0.0180 |
| 2024_09_19 22:00 | 3248725 | 2 | 93.2907 | 89.9138 | -117.9520 | 7.3620 | 95.1267 | 0.0077 | 0.0193 |
| 2024_09_19 22:00 | 3224195 | 3 | 91.4515 | 85.6746 | -117.8530 | 12.3576 | 140.1877 | 0.0085 | 0.0200 |
| 2024_09_19 22:00 | 3223187 | 4 | 84.3089 | 76.8414 | -116.4004 | 11.8273 | 167.2568 | 0.0100 | 0.0059 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417174_88D1FB27 | 504990 | 61 | -88.3 | 504990 | 731 | -87.2 | 504990 | 445 | -100.6 | 504990 | 509 |
| MR_1774417174_A0BBA32F | 504990 | 61 | -86.2 | 504990 | 731 | -89.9 | 504990 | 445 | -97.3 | 504990 | 509 |
| MR_1774417174_79C49E17 | 504990 | 61 | -84.9 | 504990 | 731 | -87.9 | 504990 | 445 | -98.1 | 504990 | 509 |
| MR_1774417174_E33FDB96 | 504990 | 61 | -85.2 | 504990 | 731 | -86.9 | 504990 | 445 | -99.7 | 504990 | 509 |
| MR_1774417174_AE9AD68F | 504990 | 61 | -88.4 | 504990 | 731 | -88.7 | 504990 | 445 | -100.5 | 504990 | 509 |
| MR_1774417174_B96582AB | 504990 | 61 | -88.0 | 504990 | 731 | -88.9 | 504990 | 445 | -101.0 | 504990 | 509 |
| MR_1774417174_A89AD266 | 504990 | 61 | -86.7 | 504990 | 731 | -88.5 | 504990 | 445 | -99.9 | 504990 | 509 |

> *... 2개 열 생략 (전체 14열)*

---
