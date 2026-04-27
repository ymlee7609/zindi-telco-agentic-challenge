# Track A 문제 분석 — train[390]~train[399]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[390] ~ train[399] (10개)

## 목차

1. [문제 390: `7a7542d1-270...`](#390) — single-answer, 정답: C2
2. [문제 391: `76995b58-f55...`](#391) — single-answer, 정답: C14
3. [문제 392: `d88e05d0-cd6...`](#392) — single-answer, 정답: C13
4. [문제 393: `b81f94af-2e0...`](#393) — single-answer, 정답: C13
5. [문제 394: `6afd4ec2-59a...`](#394) — single-answer, 정답: C12
6. [문제 395: `76da2a11-864...`](#395) — multiple-answer, 정답: C1|C3|C13|C21
7. [문제 396: `293d164d-d8e...`](#396) — single-answer, 정답: C5
8. [문제 397: `5f17d02d-d9d...`](#397) — single-answer, 정답: C11
9. [문제 398: `e32e080a-d3d...`](#398) — single-answer, 정답: C9
10. [문제 399: `ee1a96e3-30c...`](#399) — single-answer, 정답: C6

---

### 문제 390: `7a7542d1-270...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7a7542d1-2707-4ed1-add8-554ce4c1d903` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3272877_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[390] topology](images/train_0390.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3272877_4 by 45 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272877_4 **← 정답**
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248381_1
- `C4`: Lift the tilt angle  of 3248381_1 by 10 degrees
- `C5`: Add neighbor relationship between 3229340_2 and 3248381_1
- `C6`: Increase transmission power for 3272877_4
- `C7`: Adjust the azimuth of 3248381_1 by 50 degrees
- `C8`: Press down the tilt angle of 3272877_4 by 1 degrees
- `C9`: Increase transmission power for 3248381_1
- `C10`: Decrease transmission power for 3272877_4
- `C11`: Check test server and transmission issues
- `C12`: Increase A3 Offset threshold for 3272877_4
- `C13`: Increase A3 Offset threshold for 3248381_1
- `C14`: Lift the tilt angle of 3272877_4 by 1 degrees
- `C15`: Decrease A3 Offset threshold for 3272877_4
- `C16`: Decrease transmission power for 3248381_1
- `C17`: Add neighbor relationship between 3272877_4 and 3248381_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248381_1
- `C19`: Decrease A3 Offset threshold for 3248381_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272877_4
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Press down the tilt angle  of 3248381_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.984 | MS1 | 121.4656734683 | 31.1446285974 | 158 | 504990 | -86.26 | 15.53 | 340.03 | 0.13 | 2.43 | 1593 |
| 2024-09-20 22:21:32.903 | MS1 | 121.4656590255 | 31.1446238929 | 158 | 504990 | -86.55 | 15.67 | 599.58 | 0.12 | 2.41 | 1573 |
| 2024-09-20 22:21:33.133 | MS1 | 121.4656718156 | 31.1446260803 | 158 | 504990 | -87.03 | 14.95 | 515.72 | 0.08 | 2.80 | 1567 |
| 2024-09-20 22:21:34.622 | MS1 | 121.4656655700 | 31.1446282571 | 158 | 504990 | -85.12 | 12.55 | 79.06 | 0.64 | 2.99 | 559 |
| 2024-09-20 22:21:35.971 | MS1 | 121.4656658752 | 31.1446364374 | 158 | 504990 | -86.67 | 12.20 | 108.93 | 0.70 | 2.78 | 556 |
| 2024-09-20 22:21:36.499 | MS1 | 121.4656686735 | 31.1446204478 | 158 | 504990 | -91.91 | 16.43 | 65.73 | 0.51 | 2.23 | 676 |
| 2024-09-20 22:21:37.706 | MS1 | 121.4656763614 | 31.1446331026 | 158 | 504990 | -90.87 | 12.82 | 79.18 | 0.61 | 2.77 | 578 |
| 2024-09-20 22:21:38.378 | MS1 | 121.4656700624 | 31.1446325547 | 158 | 504990 | -90.58 | 7.60 | 65.33 | 0.51 | 2.26 | 525 |
| 2024-09-20 22:21:39.278 | MS1 | 121.4656718221 | 31.1446299623 | 158 | 504990 | -90.36 | 10.72 | 80.65 | 0.52 | 2.35 | 678 |
| 2024-09-20 22:21:40.782 | MS1 | 121.4656666590 | 31.1446199642 | 158 | 504990 | -90.28 | 8.21 | 441.29 | 0.15 | 2.10 | 1580 |
| 2024-09-20 22:21:41.370 | MS1 | 121.4656655055 | 31.1446295779 | 158 | 504990 | -89.52 | 7.89 | 584.40 | 0.05 | 2.97 | 1562 |
| 2024-09-20 22:21:42.355 | MS1 | 121.4656611238 | 31.1446334717 | 158 | 504990 | -91.88 | 12.41 | 528.19 | 0.03 | 2.94 | 1583 |

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
| 3229340 | 2 | 121.4652717145 | 31.1457917076 | 319 | 3 | 10 | 30.3 | TDD | 892 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3233166 | 3 | 121.4715203367 | 31.1492379334 | 288 | 11 | 9 | 16.7 | TDD | 748 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3248381 | 1 | 121.4715850719 | 31.1461819524 | 25 | 8 | 4 | 28.1 | TDD | 625 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3272877 | 4 | 121.4665192566 | 31.1539158913 | 229 | 0 | 11 | 21.5 | TDD | 158 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.226 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.245 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.358 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.358 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.033 | NREventA3 | measId:2;ServCellPCI:338;Se... |
| 2024-09-20 22:21:38.273 | NRHandoverAttempt | SourcePCI:338;SourceNR-ARFC... |
| 2024-09-20 22:21:38.313 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.326 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.460 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.460 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248381 | 1 | 18.5283 | 5.1224 | -115.5475 | 13.6069 | 192.9038 | 0.0157 | 0.0098 |
| 2024_09_20 22:00 | 3229340 | 2 | 16.8566 | 15.0909 | -114.7275 | 7.4401 | 196.3637 | 0.0001 | 0.0177 |
| 2024_09_20 22:00 | 3233166 | 3 | 11.0805 | 5.0605 | -116.7473 | 18.6466 | 112.4602 | 0.0122 | 0.0149 |
| 2024_09_20 22:00 | 3272877 | 4 | 14.0791 | 13.8131 | -115.6075 | 17.7245 | 85.3283 | 0.0166 | 0.0172 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414243_49EAEEA5 | 504990 | 158 | -86.0 | 504990 | 625 | -89.9 | 504990 | 892 | -93.0 | 504990 | 748 |
| MR_1774414243_0ADC6CB2 | 504990 | 158 | -84.2 | 504990 | 625 | -92.3 | 504990 | 892 | -95.9 | 504990 | 748 |
| MR_1774414243_6A5A55AA | 504990 | 158 | -86.8 | 504990 | 625 | -92.0 | 504990 | 892 | -96.6 | 504990 | 748 |
| MR_1774414243_CD851643 | 504990 | 158 | -83.3 | 504990 | 625 | -89.7 | 504990 | 892 | -95.7 | 504990 | 748 |
| MR_1774414243_4C39C63B | 504990 | 158 | -84.6 | 504990 | 625 | -92.8 | 504990 | 892 | -92.9 | 504990 | 748 |
| MR_1774414243_7FBD4C72 | 504990 | 158 | -84.3 | 504990 | 625 | -92.7 | 504990 | 892 | -95.2 | 504990 | 748 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 391: `76995b58-f55...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `76995b58-f55c-4d6d-af9b-beea1d1cf950` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3222945_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[391] topology](images/train_0391.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3222945_4 and 3276332_2
- `C2`: Decrease transmission power for 3222945_4
- `C3`: Decrease A3 Offset threshold for 3222945_4
- `C4`: Increase A3 Offset threshold for 3276332_2
- `C5`: Press down the tilt angle of 3222945_4 by 2 degrees
- `C6`: Increase transmission power for 3276332_2
- `C7`: Lift the tilt angle of 3222945_4 by 2 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276332_2
- `C9`: Adjust the azimuth of 3276332_2 by 50 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease transmission power for 3276332_2
- `C12`: Increase transmission power for 3222945_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222945_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222945_4 **← 정답**
- `C15`: Check test server and transmission issues
- `C16`: Press down the tilt angle  of 3276332_2 by 10 degrees
- `C17`: Increase A3 Offset threshold for 3222945_4
- `C18`: Decrease A3 Offset threshold for 3276332_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276332_2
- `C20`: Add neighbor relationship between 3210095_3 and 3276332_2
- `C21`: Adjust the azimuth of 3222945_4 by 13 degrees
- `C22`: Lift the tilt angle  of 3276332_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.198 | MS1 | 121.4656732283 | 31.1446355817 | 615 | 504990 | -89.40 | 15.76 | 359.53 | 0.11 | 2.96 | 1599 |
| 2024-09-20 22:21:32.443 | MS1 | 121.4656768815 | 31.1446237399 | 615 | 504990 | -89.31 | 15.13 | 554.49 | 0.06 | 2.19 | 1596 |
| 2024-09-20 22:21:33.191 | MS1 | 121.4656726984 | 31.1446346808 | 615 | 504990 | -86.02 | 13.46 | 591.18 | 0.05 | 2.50 | 1562 |
| 2024-09-20 22:21:34.311 | MS1 | 121.4656626369 | 31.1446327976 | 615 | 504990 | -85.10 | 16.94 | 97.60 | 0.65 | 2.92 | 588 |
| 2024-09-20 22:21:35.664 | MS1 | 121.4656775742 | 31.1446188175 | 615 | 504990 | -90.36 | 14.73 | 45.87 | 0.50 | 2.61 | 618 |
| 2024-09-20 22:21:36.718 | MS1 | 121.4656774985 | 31.1446311499 | 615 | 504990 | -91.68 | 16.22 | 79.34 | 0.67 | 2.98 | 532 |
| 2024-09-20 22:21:37.748 | MS1 | 121.4656732282 | 31.1446241696 | 615 | 504990 | -91.50 | 9.55 | 76.13 | 0.54 | 2.31 | 658 |
| 2024-09-20 22:21:38.431 | MS1 | 121.4656696354 | 31.1446268556 | 615 | 504990 | -93.27 | 10.10 | 69.56 | 0.61 | 2.94 | 663 |
| 2024-09-20 22:21:39.306 | MS1 | 121.4656761091 | 31.1446299612 | 615 | 504990 | -93.54 | 12.73 | 63.84 | 0.59 | 2.90 | 549 |
| 2024-09-20 22:21:40.521 | MS1 | 121.4656702866 | 31.1446289744 | 615 | 504990 | -89.77 | 11.66 | 519.25 | 0.15 | 2.55 | 1600 |
| 2024-09-20 22:21:41.462 | MS1 | 121.4656752552 | 31.1446298716 | 615 | 504990 | -89.68 | 12.40 | 532.99 | 0.01 | 2.95 | 1589 |
| 2024-09-20 22:21:42.318 | MS1 | 121.4656588849 | 31.1446313209 | 615 | 504990 | -91.81 | 12.79 | 593.56 | 0.12 | 2.08 | 1594 |

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
| 3210095 | 3 | 121.4758067246 | 31.1459250443 | 333 | 4 | 7 | 26.3 | TDD | 122 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3216326 | 1 | 121.4677780535 | 31.1529562276 | 148 | 13 | 5 | 29.1 | TDD | 210 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3222945 | 4 | 121.4750392146 | 31.1454075813 | 277 | 0 | 5 | 28.8 | TDD | 615 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3276332 | 2 | 121.4640177292 | 31.1447814003 | 359 | 2 | 11 | 48.3 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.868 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.893 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.037 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.037 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.713 | NREventA3 | measId:2;ServCellPCI:583;Se... |
| 2024-09-20 22:21:37.953 | NRHandoverAttempt | SourcePCI:583;SourceNR-ARFC... |
| 2024-09-20 22:21:37.989 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.003 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.120 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.120 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216326 | 1 | 18.9766 | 16.2129 | -114.0574 | 11.4390 | 84.3878 | 0.0190 | 0.0008 |
| 2024_09_20 22:00 | 3276332 | 2 | 10.6550 | 13.3503 | -114.0869 | 5.1327 | 101.1173 | 0.0151 | 0.0025 |
| 2024_09_20 22:00 | 3210095 | 3 | 11.1820 | 19.0882 | -114.5328 | 5.3357 | 172.5387 | 0.0019 | 0.0020 |
| 2024_09_20 22:00 | 3222945 | 4 | 8.5165 | 17.4314 | -117.7519 | 5.4622 | 90.0785 | 0.0108 | 0.0056 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412842_FAFC5600 | 504990 | 615 | -85.8 | 504990 | 309 | -84.8 | 504990 | 122 | -97.3 | 504990 | 210 |
| MR_1774412842_A97C8E97 | 504990 | 615 | -83.6 | 504990 | 309 | -83.3 | 504990 | 122 | -97.2 | 504990 | 210 |
| MR_1774412842_B53B8910 | 504990 | 615 | -85.7 | 504990 | 309 | -85.6 | 504990 | 122 | -97.1 | 504990 | 210 |
| MR_1774412842_39BF50C9 | 504990 | 615 | -85.0 | 504990 | 309 | -83.2 | 504990 | 122 | -97.8 | 504990 | 210 |
| MR_1774412842_FE756A57 | 504990 | 615 | -83.6 | 504990 | 309 | -84.4 | 504990 | 122 | -98.4 | 504990 | 210 |
| MR_1774412842_942A19A6 | 504990 | 615 | -84.1 | 504990 | 309 | -86.6 | 504990 | 122 | -98.9 | 504990 | 210 |
| MR_1774412842_37820E12 | 504990 | 615 | -83.2 | 504990 | 309 | -83.3 | 504990 | 122 | -98.5 | 504990 | 210 |
| MR_1774412842_D8EBD1C5 | 504990 | 615 | -85.1 | 504990 | 309 | -85.6 | 504990 | 122 | -97.4 | 504990 | 210 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 392: `d88e05d0-cd6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d88e05d0-cd64-4d26-a791-221857168744` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Add neighbor relationship between 3250083_4 and 3266253_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[392] topology](images/train_0392.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3266253_1
- `C2`: Increase transmission power for 3250083_4
- `C3`: Adjust the azimuth of 3250083_4 by 50 degrees
- `C4`: Adjust the azimuth of 3266253_1 by 12 degrees
- `C5`: Add neighbor relationship between 3232519_2 and 3266253_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266253_1
- `C7`: Lift the tilt angle  of 3266253_1 by 3 degrees
- `C8`: Lift the tilt angle of 3250083_4 by 7 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266253_1
- `C10`: Increase transmission power for 3266253_1
- `C11`: Increase A3 Offset threshold for 3250083_4
- `C12`: Increase A3 Offset threshold for 3266253_1
- `C13`: Add neighbor relationship between 3250083_4 and 3266253_1 **← 정답**
- `C14`: Check test server and transmission issues
- `C15`: Decrease A3 Offset threshold for 3250083_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250083_4
- `C17`: Press down the tilt angle of 3250083_4 by 7 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250083_4
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease transmission power for 3250083_4
- `C21`: Decrease A3 Offset threshold for 3266253_1
- `C22`: Press down the tilt angle  of 3266253_1 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.573 | MS1 | 121.4656725633 | 31.1446358596 | 559 | 504990 | -81.67 | 17.79 | 413.91 | 0.14 | 3.00 | 1599 |
| 2024-09-20 22:21:32.107 | MS1 | 121.4656625795 | 31.1446203003 | 559 | 504990 | -80.31 | 12.19 | 432.70 | 0.07 | 2.11 | 1591 |
| 2024-09-20 22:21:33.307 | MS1 | 121.4656616518 | 31.1446258710 | 559 | 504990 | -80.80 | 13.43 | 430.37 | 0.12 | 2.03 | 1563 |
| 2024-09-20 22:21:34.249 | MS1 | 121.4656727765 | 31.1446195504 | 559 | 504990 | -87.66 | -0.03 | 53.29 | 0.18 | 1.19 | 1588 |
| 2024-09-20 22:21:35.518 | MS1 | 121.4656622806 | 31.1446234100 | 559 | 504990 | -86.38 | -1.44 | 77.80 | 0.06 | 1.44 | 1563 |
| 2024-09-20 22:21:36.732 | MS1 | 121.4656610752 | 31.1446234369 | 559 | 504990 | -86.16 | -1.12 | 41.69 | 0.04 | 1.01 | 1564 |
| 2024-09-20 22:21:37.348 | MS1 | 121.4656695532 | 31.1446352627 | 559 | 504990 | -85.85 | -3.74 | 42.15 | 0.17 | 1.04 | 1560 |
| 2024-09-20 22:21:38.326 | MS1 | 121.4656700237 | 31.1446307752 | 559 | 504990 | -79.91 | 12.49 | 367.48 | 0.17 | 1.16 | 1575 |
| 2024-09-20 22:21:39.894 | MS1 | 121.4656672386 | 31.1446337742 | 559 | 504990 | -75.87 | 17.68 | 373.60 | 0.17 | 1.08 | 1581 |
| 2024-09-20 22:21:40.324 | MS1 | 121.4656702507 | 31.1446276611 | 559 | 504990 | -80.65 | 15.50 | 353.61 | 0.07 | 2.96 | 1589 |
| 2024-09-20 22:21:41.282 | MS1 | 121.4656657262 | 31.1446222015 | 559 | 504990 | -82.63 | 13.01 | 346.17 | 0.04 | 2.17 | 1576 |
| 2024-09-20 22:21:42.927 | MS1 | 121.4656737527 | 31.1446292661 | 559 | 504990 | -75.91 | 15.14 | 378.41 | 0.10 | 2.29 | 1560 |

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
| 3232519 | 2 | 121.4668396005 | 31.1518246197 | 317 | 2 | 8 | 37.5 | TDD | 593 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3250083 | 4 | 121.4736899527 | 31.1487824675 | 348 | 4 | 7 | 44.5 | TDD | 559 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3253376 | 3 | 121.4709286979 | 31.1514384160 | 183 | 5 | 10 | 38.6 | TDD | 797 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3266253 | 1 | 121.4724004049 | 31.1478037979 | 253 | 2 | 10 | 15.0 | TDD | 720 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.600 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.624 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.729 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.729 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.430 | NREventA3 | measId:2;ServCellPCI:23;Ser... |
| 2024-09-20 22:21:36.430 | NREventA3 | measId:2;ServCellPCI:23;Ser... |
| 2024-09-20 22:21:37.430 | NREventA3 | measId:2;ServCellPCI:23;Ser... |
| 2024-09-20 22:21:39.930 | NRRRCReestablishAttempt | PCI:23 |
| 2024-09-20 22:21:39.948 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.962 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:40.090 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.090 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266253 | 1 | 13.3309 | 19.5079 | -115.6804 | 17.5732 | 186.8971 | 0.0033 | 0.0048 |
| 2024_09_20 22:00 | 3232519 | 2 | 11.4219 | 14.8888 | -114.2548 | 6.8208 | 108.1459 | 0.0149 | 0.0174 |
| 2024_09_20 22:00 | 3253376 | 3 | 6.9024 | 19.5183 | -116.5423 | 8.0784 | 181.2125 | 0.0002 | 0.0139 |
| 2024_09_20 22:00 | 3250083 | 4 | 8.6090 | 15.9765 | -117.9554 | 15.7357 | 92.9709 | 0.0142 | 0.1524 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415425_2BCDAB57 | 504990 | 720 | -80.7 | 504990 | 559 | -87.0 | 504990 | 593 | -91.1 | 504990 | 797 |
| MR_1774415425_6D553C47 | 504990 | 559 | -89.3 | 504990 | 720 | -83.4 | 504990 | 593 | -90.5 | 504990 | 797 |
| MR_1774415425_D823E0B5 | 504990 | 559 | -87.6 | 504990 | 720 | -83.2 | 504990 | 593 | -90.2 | 504990 | 797 |
| MR_1774415425_EED6861C | 504990 | 720 | -81.3 | 504990 | 559 | -89.0 | 504990 | 593 | -91.6 | 504990 | 797 |
| MR_1774415425_D099DFFC | 504990 | 559 | -89.1 | 504990 | 720 | -81.0 | 504990 | 593 | -89.3 | 504990 | 797 |
| MR_1774415425_BC72C3EC | 504990 | 720 | -83.5 | 504990 | 559 | -87.7 | 504990 | 593 | -89.5 | 504990 | 797 |
| MR_1774415425_5AF52875 | 504990 | 720 | -81.4 | 504990 | 559 | -88.2 | 504990 | 593 | -92.8 | 504990 | 797 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 393: `b81f94af-2e0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b81f94af-2e0d-4edc-83f7-fc492204d482` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[393] topology](images/train_0393.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3214733_4
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Press down the tilt angle  of 3214733_4 by 10 degrees
- `C4`: Add neighbor relationship between 3241815_1 and 3214733_4
- `C5`: Adjust the azimuth of 3214733_4 by 50 degrees
- `C6`: Press down the tilt angle of 3241815_1 by 7 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241815_1
- `C8`: Increase transmission power for 3241815_1
- `C9`: Increase A3 Offset threshold for 3241815_1
- `C10`: Add neighbor relationship between 3245571_2 and 3214733_4
- `C11`: Increase transmission power for 3214733_4
- `C12`: Adjust the azimuth of 3241815_1 by 50 degrees
- `C13`: Check test server and transmission issues **← 정답**
- `C14`: Increase A3 Offset threshold for 3214733_4
- `C15`: Decrease transmission power for 3241815_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214733_4
- `C17`: Lift the tilt angle  of 3214733_4 by 10 degrees
- `C18`: Lift the tilt angle of 3241815_1 by 7 degrees
- `C19`: Decrease A3 Offset threshold for 3214733_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214733_4
- `C21`: Decrease A3 Offset threshold for 3241815_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241815_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.286 | MS1 | 121.4656606947 | 31.1446200918 | 856 | 504990 | -86.97 | 16.36 | 304.03 | 0.05 | 2.66 | 1598 |
| 2024-09-20 22:21:32.892 | MS1 | 121.4656706220 | 31.1446201272 | 856 | 504990 | -87.37 | 15.29 | 586.58 | 0.18 | 2.77 | 1577 |
| 2024-09-20 22:21:33.439 | MS1 | 121.4656721000 | 31.1446362696 | 856 | 504990 | -87.18 | 17.66 | 543.04 | 0.18 | 2.77 | 1583 |
| 2024-09-20 22:21:34.150 | MS1 | 121.4656631976 | 31.1446327180 | 856 | 504990 | -86.22 | 12.87 | 71.32 | 0.17 | 2.86 | 364 |
| 2024-09-20 22:21:35.147 | MS1 | 121.4656620860 | 31.1446335534 | 856 | 504990 | -87.95 | 17.85 | 66.09 | 0.06 | 2.77 | 361 |
| 2024-09-20 22:21:36.206 | MS1 | 121.4656612787 | 31.1446263038 | 856 | 504990 | -87.79 | 13.20 | 68.69 | 0.09 | 2.45 | 411 |
| 2024-09-20 22:21:37.699 | MS1 | 121.4656581428 | 31.1446192556 | 856 | 504990 | -92.27 | 11.75 | 65.10 | 0.19 | 2.80 | 342 |
| 2024-09-20 22:21:38.960 | MS1 | 121.4656663338 | 31.1446366368 | 856 | 504990 | -90.80 | 8.69 | 70.40 | 0.11 | 2.34 | 325 |
| 2024-09-20 22:21:39.897 | MS1 | 121.4656627763 | 31.1446357974 | 856 | 504990 | -93.38 | 12.61 | 60.87 | 0.08 | 2.86 | 380 |
| 2024-09-20 22:21:40.864 | MS1 | 121.4656692343 | 31.1446323866 | 856 | 504990 | -91.86 | 9.88 | 425.85 | 0.00 | 2.58 | 1591 |
| 2024-09-20 22:21:41.489 | MS1 | 121.4656702281 | 31.1446205401 | 856 | 504990 | -91.41 | 9.32 | 500.47 | 0.01 | 2.01 | 1585 |
| 2024-09-20 22:21:42.338 | MS1 | 121.4656726668 | 31.1446368703 | 856 | 504990 | -90.18 | 12.89 | 391.98 | 0.14 | 2.69 | 1581 |

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
| 3214733 | 4 | 121.4647278759 | 31.1458302612 | 226 | 0 | 4 | 39.5 | TDD | 884 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3231457 | 3 | 121.4648245420 | 31.1543911925 | 45 | 1 | 2 | 39.9 | TDD | 48 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3241815 | 1 | 121.4704809782 | 31.1539519083 | 26 | 5 | 9 | 31.8 | TDD | 856 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3245571 | 2 | 121.4728546780 | 31.1440683441 | 14 | 1 | 0 | 40.7 | TDD | 434 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.184 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.327 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.327 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.011 | NREventA3 | measId:2;ServCellPCI:754;Se... |
| 2024-09-20 22:21:38.251 | NRHandoverAttempt | SourcePCI:754;SourceNR-ARFC... |
| 2024-09-20 22:21:38.301 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.312 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.423 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.423 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241815 | 1 | 6.1363 | 11.3911 | -114.5572 | 10.7229 | 163.1022 | 0.0090 | 0.0150 |
| 2024_09_20 22:00 | 3245571 | 2 | 12.9082 | 6.0363 | -116.3934 | 16.4747 | 142.5281 | 0.0142 | 0.0042 |
| 2024_09_20 22:00 | 3231457 | 3 | 19.6542 | 10.3970 | -116.7271 | 12.7255 | 173.0518 | 0.0034 | 0.0176 |
| 2024_09_20 22:00 | 3214733 | 4 | 8.5021 | 10.0773 | -115.2306 | 15.5653 | 149.9161 | 0.0101 | 0.0010 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414629_E96228DA | 504990 | 856 | -86.4 | 504990 | 884 | -95.0 | 504990 | 434 | -100.2 | 504990 | 48 |
| MR_1774414629_B2CE9CFC | 504990 | 856 | -87.1 | 504990 | 884 | -93.8 | 504990 | 434 | -98.8 | 504990 | 48 |
| MR_1774414629_CC43CE1B | 504990 | 856 | -84.3 | 504990 | 884 | -95.8 | 504990 | 434 | -99.6 | 504990 | 48 |
| MR_1774414629_CC252174 | 504990 | 856 | -85.2 | 504990 | 884 | -94.4 | 504990 | 434 | -101.3 | 504990 | 48 |
| MR_1774414629_E7EDC30B | 504990 | 856 | -85.7 | 504990 | 884 | -92.6 | 504990 | 434 | -99.1 | 504990 | 48 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 394: `6afd4ec2-59a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6afd4ec2-59a2-49af-b791-86852a44a43f` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[394] topology](images/train_0394.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3233106_1
- `C2`: Increase transmission power for 3269622_4
- `C3`: Increase A3 Offset threshold for 3269622_4
- `C4`: Adjust the azimuth of 3233106_1 by 50 degrees
- `C5`: Check test server and transmission issues
- `C6`: Lift the tilt angle of 3269622_4 by 5 degrees
- `C7`: Add neighbor relationship between 3232789_2 and 3233106_1
- `C8`: Adjust the azimuth of 3269622_4 by 18 degrees
- `C9`: Lift the tilt angle  of 3233106_1 by 10 degrees
- `C10`: Decrease A3 Offset threshold for 3269622_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233106_1
- `C12`: Insufficient data; more data is needed for judgment. **← 정답**
- `C13`: Increase transmission power for 3233106_1
- `C14`: Decrease transmission power for 3233106_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233106_1
- `C16`: Decrease transmission power for 3269622_4
- `C17`: Press down the tilt angle of 3269622_4 by 5 degrees
- `C18`: Press down the tilt angle  of 3233106_1 by 10 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269622_4
- `C20`: Decrease A3 Offset threshold for 3233106_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269622_4
- `C22`: Add neighbor relationship between 3269622_4 and 3233106_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.433 | MS1 | 121.4656591881 | 31.1446359955 | 854 | 504990 | -87.23 | 15.07 | 546.58 | 0.11 | 2.15 | 1582 |
| 2024-09-20 22:21:32.693 | MS1 | 121.4656640532 | 31.1446306129 | 854 | 504990 | -88.13 | 12.81 | 467.11 | 0.07 | 2.52 | 1590 |
| 2024-09-20 22:21:33.345 | MS1 | 121.4656713241 | 31.1446375025 | 854 | 504990 | -85.49 | 13.96 | 443.56 | 0.17 | 2.75 | 1560 |
| 2024-09-20 22:21:34.438 | MS1 | 121.4656742954 | 31.1446232459 | 854 | 504990 | -86.54 | 17.47 | 60.03 | 0.06 | 2.93 | 1593 |
| 2024-09-20 22:21:35.819 | MS1 | 121.4656735334 | 31.1446375302 | 854 | 504990 | -85.26 | 17.24 | 104.87 | 0.17 | 2.52 | 1576 |
| 2024-09-20 22:21:36.277 | MS1 | 121.4656730301 | 31.1446183959 | 854 | 504990 | -85.16 | 12.57 | 60.68 | 0.07 | 2.26 | 1599 |
| 2024-09-20 22:21:37.715 | MS1 | 121.4656743882 | 31.1446338116 | 854 | 504990 | -90.18 | 11.41 | 58.61 | 0.07 | 2.66 | 1597 |
| 2024-09-20 22:21:38.838 | MS1 | 121.4656700326 | 31.1446346706 | 854 | 504990 | -91.72 | 7.53 | 63.52 | 0.04 | 2.91 | 1570 |
| 2024-09-20 22:21:39.248 | MS1 | 121.4656625902 | 31.1446242136 | 854 | 504990 | -91.92 | 7.54 | 62.61 | 0.02 | 2.61 | 1591 |
| 2024-09-20 22:21:40.908 | MS1 | 121.4656629533 | 31.1446241159 | 854 | 504990 | -93.17 | 7.50 | 300.08 | 0.10 | 2.73 | 1564 |
| 2024-09-20 22:21:41.368 | MS1 | 121.4656639528 | 31.1446192761 | 854 | 504990 | -93.85 | 7.89 | 581.32 | 0.14 | 2.63 | 1576 |
| 2024-09-20 22:21:42.610 | MS1 | 121.4656697641 | 31.1446196258 | 854 | 504990 | -91.82 | 12.30 | 551.09 | 0.20 | 2.96 | 1560 |

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
| 3232789 | 2 | 121.4756294842 | 31.1472249037 | 163 | 15 | 1 | 42.4 | TDD | 51 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3233106 | 1 | 121.4749903762 | 31.1547579970 | 347 | 10 | 4 | 29.0 | TDD | 752 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3259681 | 3 | 121.4672932920 | 31.1509418442 | 293 | 5 | 1 | 15.0 | TDD | 107 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3269622 | 4 | 121.4649706566 | 31.1520762922 | 157 | 3 | 4 | 29.1 | TDD | 854 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.543 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.649 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.649 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.354 | NREventA3 | measId:2;ServCellPCI:488;Se... |
| 2024-09-20 22:21:38.594 | NRHandoverAttempt | SourcePCI:488;SourceNR-ARFC... |
| 2024-09-20 22:21:38.625 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.636 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.766 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.766 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3233106 | 1 | 82.1873 | 83.3833 | -117.7622 | 14.9876 | 165.8814 | 0.0013 | 0.0075 |
| 2024_09_19 22:00 | 3232789 | 2 | 78.4299 | 87.5898 | -117.6341 | 15.7792 | 108.3339 | 0.0014 | 0.0173 |
| 2024_09_19 22:00 | 3259681 | 3 | 81.7608 | 90.6542 | -115.9048 | 15.9272 | 101.6461 | 0.0185 | 0.0018 |
| 2024_09_19 22:00 | 3269622 | 4 | 92.7102 | 89.2762 | -114.2594 | 8.2167 | 85.9941 | 0.0180 | 0.0108 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413300_019E9AA9 | 504990 | 854 | -87.3 | 504990 | 752 | -90.8 | 504990 | 51 | -96.3 | 504990 | 107 |
| MR_1774413300_E73118B6 | 504990 | 854 | -85.0 | 504990 | 752 | -93.0 | 504990 | 51 | -94.7 | 504990 | 107 |
| MR_1774413300_49BFE932 | 504990 | 854 | -88.3 | 504990 | 752 | -92.1 | 504990 | 51 | -96.3 | 504990 | 107 |
| MR_1774413300_522B5B13 | 504990 | 854 | -87.8 | 504990 | 752 | -93.9 | 504990 | 51 | -94.3 | 504990 | 107 |
| MR_1774413300_FBF62EC1 | 504990 | 854 | -88.5 | 504990 | 752 | -91.4 | 504990 | 51 | -95.8 | 504990 | 107 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 395: `76da2a11-864...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `76da2a11-8643-40d3-8369-928e46cf3f45` |
| Tag | **multiple-answer** |
| 정답 | **C1|C3|C13|C21** |
| C1 의미 | Increase A3 Offset threshold for 3215365_5 |
| C3 의미 | Increase A3 Offset threshold for 3240927_1 |
| C13 의미 | Press down the tilt angle  of 3240927_1 by 4 degrees |
| C21 의미 | Decrease transmission power for 3240927_1 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[395] topology](images/train_0395.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3215365_5 **← 정답**
- `C2`: Increase transmission power for 3215365_5
- `C3`: Increase A3 Offset threshold for 3240927_1 **← 정답**
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240927_1
- `C5`: Check test server and transmission issues
- `C6`: Lift the tilt angle  of 3240927_1 by 4 degrees
- `C7`: Adjust the azimuth of 3215365_5 by 8 degrees
- `C8`: Add neighbor relationship between 3224545_2 and 3240927_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240927_1
- `C10`: Decrease A3 Offset threshold for 3215365_5
- `C11`: Press down the tilt angle of 3215365_5 by 1 degrees
- `C12`: Add neighbor relationship between 3215365_5 and 3240927_1
- `C13`: Press down the tilt angle  of 3240927_1 by 4 degrees **← 정답**
- `C14`: Adjust the azimuth of 3240927_1 by 15 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215365_5
- `C16`: Decrease transmission power for 3215365_5
- `C17`: Increase transmission power for 3240927_1
- `C18`: Lift the tilt angle of 3215365_5 by 1 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease A3 Offset threshold for 3240927_1
- `C21`: Decrease transmission power for 3240927_1 **← 정답**
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215365_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.296 | MS1 | 121.4656580742 | 31.1446182047 | 351 | 504990 | -84.71 | 12.51 | 548.87 | 0.02 | 2.56 | 1591 |
| 2024-09-20 22:21:32.650 | MS1 | 121.4656729502 | 31.1446233802 | 351 | 504990 | -79.93 | 14.21 | 491.79 | 0.03 | 2.21 | 1587 |
| 2024-09-20 22:21:33.988 | MS1 | 121.4656722687 | 31.1446370054 | 351 | 504990 | -77.04 | 12.10 | 390.64 | 0.15 | 2.68 | 1565 |
| 2024-09-20 22:21:34.459 | MS1 | 121.4656680765 | 31.1446228173 | 809 | 504990 | -82.31 | 4.35 | 66.63 | 0.16 | 1.23 | 1589 |
| 2024-09-20 22:21:35.473 | MS1 | 121.4656714808 | 31.1446281346 | 809 | 504990 | -84.83 | 3.27 | 73.42 | 0.08 | 1.33 | 1600 |
| 2024-09-20 22:21:36.903 | MS1 | 121.4656680958 | 31.1446300252 | 351 | 504990 | -88.61 | 1.06 | 55.55 | 0.09 | 1.21 | 1569 |
| 2024-09-20 22:21:37.554 | MS1 | 121.4656588864 | 31.1446363305 | 351 | 504990 | -87.35 | 4.21 | 71.62 | 0.12 | 1.08 | 1593 |
| 2024-09-20 22:21:38.404 | MS1 | 121.4656621411 | 31.1446322241 | 809 | 504990 | -85.03 | 4.14 | 36.42 | 0.17 | 1.48 | 1592 |
| 2024-09-20 22:21:39.116 | MS1 | 121.4656748608 | 31.1446190630 | 809 | 504990 | -88.18 | 1.06 | 56.54 | 0.03 | 1.29 | 1566 |
| 2024-09-20 22:21:40.308 | MS1 | 121.4656675179 | 31.1446181333 | 809 | 504990 | -81.43 | 14.42 | 498.85 | 0.13 | 2.54 | 1583 |
| 2024-09-20 22:21:41.160 | MS1 | 121.4656708593 | 31.1446253070 | 809 | 504990 | -78.66 | 16.85 | 575.56 | 0.14 | 2.55 | 1574 |
| 2024-09-20 22:21:42.494 | MS1 | 121.4656775177 | 31.1446187466 | 809 | 504990 | -81.79 | 16.47 | 339.35 | 0.18 | 2.70 | 1583 |

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
| 3210896 | 4 | 121.4710548693 | 31.1483219020 | 24 | 8 | 11 | 40.2 | TDD | 796 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3215365 | 5 | 121.4757770144 | 31.1555329127 | 226 | 0 | 6 | 19.0 | TDD | 351 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3224545 | 2 | 121.4694099706 | 31.1502595459 | 112 | 2 | 2 | 22.3 | TDD | 805 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3240927 | 1 | 121.4668619897 | 31.1521685672 | 173 | 1 | 2 | 47.5 | TDD | 611 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3265057 | 3 | 121.4697380911 | 31.1482472090 | 232 | 14 | 2 | 43.5 | TDD | 809 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.544 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.559 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.684 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.684 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.360 | NREventA3 | measId:2;ServCellPCI:744;Se... |
| 2024-09-20 22:21:34.600 | NRHandoverAttempt | SourcePCI:744;SourceNR-ARFC... |
| 2024-09-20 22:21:34.645 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.656 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:34.790 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.790 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.360 | NREventA3 | measId:2;ServCellPCI:534;Se... |
| 2024-09-20 22:21:36.600 | NRHandoverAttempt | SourcePCI:534;SourceNR-ARFC... |
| 2024-09-20 22:21:36.633 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.646 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.794 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.794 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.360 | NREventA3 | measId:2;ServCellPCI:744;Se... |
| 2024-09-20 22:21:38.600 | NRHandoverAttempt | SourcePCI:744;SourceNR-ARFC... |
| 2024-09-20 22:21:38.633 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.644 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.780 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.780 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240927 | 1 | 8.5485 | 11.1108 | -115.2407 | 6.6502 | 138.8168 | 0.0001 | 0.0051 |
| 2024_09_20 22:00 | 3224545 | 2 | 10.4148 | 8.9692 | -116.6232 | 19.3728 | 129.3346 | 0.0132 | 0.0031 |
| 2024_09_20 22:00 | 3265057 | 3 | 7.0834 | 13.8615 | -117.7801 | 7.2921 | 186.9045 | 0.0024 | 0.0073 |
| 2024_09_20 22:00 | 3210896 | 4 | 14.0303 | 6.0115 | -117.0278 | 19.4360 | 135.8284 | 0.0181 | 0.0036 |
| 2024_09_20 22:00 | 3215365 | 5 | 7.6279 | 9.2852 | -116.2773 | 8.0969 | 127.7010 | 0.0062 | 0.0062 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414019_4D8DE4FA | 504990 | 809 | -81.0 | 504990 | 351 | -83.7 | 504990 | 611 | -83.5 | 504990 | 805 |
| MR_1774414019_5FD214D1 | 504990 | 809 | -81.1 | 504990 | 351 | -80.9 | 504990 | 611 | -82.9 | 504990 | 805 |
| MR_1774414019_59FFE4A4 | 504990 | 809 | -82.7 | 504990 | 351 | -82.8 | 504990 | 611 | -82.2 | 504990 | 805 |
| MR_1774414019_1863C214 | 504990 | 809 | -81.9 | 504990 | 351 | -81.1 | 504990 | 611 | -83.4 | 504990 | 805 |
| MR_1774414019_69DD934D | 504990 | 809 | -81.6 | 504990 | 351 | -82.2 | 504990 | 611 | -84.4 | 504990 | 805 |
| MR_1774414019_CD5C21EF | 504990 | 809 | -82.2 | 504990 | 351 | -84.0 | 504990 | 611 | -82.9 | 504990 | 805 |
| MR_1774414019_A8181264 | 504990 | 351 | -82.1 | 504990 | 809 | -82.9 | 504990 | 611 | -84.9 | 504990 | 805 |
| MR_1774414019_3BAD3256 | 504990 | 351 | -84.1 | 504990 | 809 | -84.0 | 504990 | 611 | -84.3 | 504990 | 805 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 396: `293d164d-d8e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `293d164d-d8e7-4829-b23a-982b914bd0cc` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3212011_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[396] topology](images/train_0396.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3212011_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224177_2
- `C3`: Press down the tilt angle  of 3224177_2 by 10 degrees
- `C4`: Decrease A3 Offset threshold for 3212011_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212011_4 **← 정답**
- `C6`: Increase A3 Offset threshold for 3212011_4
- `C7`: Increase transmission power for 3224177_2
- `C8`: Decrease transmission power for 3212011_4
- `C9`: Check test server and transmission issues
- `C10`: Press down the tilt angle of 3212011_4 by 3 degrees
- `C11`: Lift the tilt angle  of 3224177_2 by 10 degrees
- `C12`: Adjust the azimuth of 3224177_2 by 50 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224177_2
- `C14`: Add neighbor relationship between 3236716_3 and 3224177_2
- `C15`: Add neighbor relationship between 3212011_4 and 3224177_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease transmission power for 3224177_2
- `C18`: Increase A3 Offset threshold for 3224177_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212011_4
- `C20`: Decrease A3 Offset threshold for 3224177_2
- `C21`: Lift the tilt angle of 3212011_4 by 3 degrees
- `C22`: Adjust the azimuth of 3212011_4 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.844 | MS1 | 121.4656699377 | 31.1446234942 | 127 | 504990 | -87.90 | 14.16 | 589.32 | 0.03 | 2.09 | 1599 |
| 2024-09-20 22:21:32.339 | MS1 | 121.4656620839 | 31.1446364991 | 127 | 504990 | -91.80 | 13.58 | 376.12 | 0.16 | 2.26 | 1596 |
| 2024-09-20 22:21:33.191 | MS1 | 121.4656701063 | 31.1446335479 | 127 | 504990 | -88.09 | 17.82 | 435.81 | 0.07 | 2.89 | 1591 |
| 2024-09-20 22:21:34.599 | MS1 | 121.4656621270 | 31.1446186721 | 127 | 504990 | -86.22 | 13.11 | 64.07 | 0.68 | 2.71 | 502 |
| 2024-09-20 22:21:35.383 | MS1 | 121.4656606091 | 31.1446195529 | 127 | 504990 | -91.53 | 12.51 | 55.04 | 0.68 | 2.49 | 529 |
| 2024-09-20 22:21:36.141 | MS1 | 121.4656769340 | 31.1446306076 | 127 | 504990 | -86.34 | 16.06 | 84.27 | 0.68 | 2.45 | 682 |
| 2024-09-20 22:21:37.228 | MS1 | 121.4656635725 | 31.1446180205 | 127 | 504990 | -90.40 | 9.38 | 64.83 | 0.60 | 2.20 | 615 |
| 2024-09-20 22:21:38.401 | MS1 | 121.4656589080 | 31.1446203450 | 127 | 504990 | -89.91 | 11.07 | 90.79 | 0.62 | 2.84 | 506 |
| 2024-09-20 22:21:39.261 | MS1 | 121.4656743342 | 31.1446196568 | 127 | 504990 | -91.29 | 10.63 | 67.25 | 0.50 | 2.82 | 628 |
| 2024-09-20 22:21:40.831 | MS1 | 121.4656776387 | 31.1446196175 | 127 | 504990 | -90.15 | 8.86 | 348.14 | 0.17 | 2.52 | 1585 |
| 2024-09-20 22:21:41.347 | MS1 | 121.4656743752 | 31.1446355158 | 127 | 504990 | -91.72 | 9.94 | 502.64 | 0.03 | 2.19 | 1580 |
| 2024-09-20 22:21:42.253 | MS1 | 121.4656673301 | 31.1446341645 | 127 | 504990 | -92.05 | 11.48 | 565.78 | 0.12 | 2.41 | 1567 |

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
| 3212011 | 4 | 121.4725214921 | 31.1537369066 | 219 | 2 | 10 | 18.4 | TDD | 127 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3224177 | 2 | 121.4654336080 | 31.1440482201 | 182 | 9 | 0 | 41.4 | TDD | 605 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3236716 | 3 | 121.4647254106 | 31.1450345910 | 138 | 13 | 8 | 24.6 | TDD | 566 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3275159 | 1 | 121.4727271887 | 31.1502247116 | 273 | 13 | 7 | 28.9 | TDD | 537 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.790 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.812 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.943 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.943 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.657 | NREventA3 | measId:2;ServCellPCI:275;Se... |
| 2024-09-20 22:21:37.897 | NRHandoverAttempt | SourcePCI:275;SourceNR-ARFC... |
| 2024-09-20 22:21:37.927 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.942 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.082 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.082 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275159 | 1 | 12.4471 | 19.8998 | -116.7734 | 6.0639 | 186.0630 | 0.0005 | 0.0056 |
| 2024_09_20 22:00 | 3224177 | 2 | 10.3718 | 18.1424 | -117.7080 | 6.9804 | 186.9697 | 0.0159 | 0.0012 |
| 2024_09_20 22:00 | 3236716 | 3 | 17.1431 | 13.4742 | -116.7272 | 19.0096 | 109.2427 | 0.0170 | 0.0038 |
| 2024_09_20 22:00 | 3212011 | 4 | 16.8095 | 18.9317 | -115.9355 | 8.9163 | 198.3544 | 0.0188 | 0.0109 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413224_D66A29E5 | 504990 | 127 | -85.3 | 504990 | 605 | -90.5 | 504990 | 566 | -99.2 | 504990 | 537 |
| MR_1774413224_B03651EE | 504990 | 127 | -87.7 | 504990 | 605 | -90.6 | 504990 | 566 | -100.0 | 504990 | 537 |
| MR_1774413224_165FC8D2 | 504990 | 127 | -86.1 | 504990 | 605 | -90.6 | 504990 | 566 | -96.9 | 504990 | 537 |
| MR_1774413224_94AE5941 | 504990 | 127 | -86.7 | 504990 | 605 | -91.6 | 504990 | 566 | -99.4 | 504990 | 537 |
| MR_1774413224_16BDD77F | 504990 | 127 | -86.7 | 504990 | 605 | -91.3 | 504990 | 566 | -96.8 | 504990 | 537 |
| MR_1774413224_A47FE25A | 504990 | 127 | -87.2 | 504990 | 605 | -89.1 | 504990 | 566 | -97.3 | 504990 | 537 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 397: `5f17d02d-d9d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5f17d02d-d9d9-44a3-bc0c-3e67c47f0d08` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3265544_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[397] topology](images/train_0397.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3250692_3
- `C2`: Increase A3 Offset threshold for 3250692_3
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250692_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265544_1
- `C6`: Decrease transmission power for 3265544_1
- `C7`: Lift the tilt angle  of 3250692_3 by 10 degrees
- `C8`: Decrease transmission power for 3250692_3
- `C9`: Increase A3 Offset threshold for 3265544_1
- `C10`: Adjust the azimuth of 3250692_3 by 50 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265544_1 **← 정답**
- `C12`: Press down the tilt angle  of 3250692_3 by 10 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250692_3
- `C14`: Press down the tilt angle of 3265544_1 by 5 degrees
- `C15`: Increase transmission power for 3265544_1
- `C16`: Decrease A3 Offset threshold for 3250692_3
- `C17`: Add neighbor relationship between 3278322_4 and 3250692_3
- `C18`: Check test server and transmission issues
- `C19`: Adjust the azimuth of 3265544_1 by 18 degrees
- `C20`: Add neighbor relationship between 3265544_1 and 3250692_3
- `C21`: Decrease A3 Offset threshold for 3265544_1
- `C22`: Lift the tilt angle of 3265544_1 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.107 | MS1 | 121.4656768603 | 31.1446256816 | 760 | 504990 | -87.44 | 16.71 | 537.67 | 0.17 | 2.64 | 1569 |
| 2024-09-20 22:21:32.187 | MS1 | 121.4656611840 | 31.1446356766 | 760 | 504990 | -90.28 | 17.83 | 325.30 | 0.07 | 2.42 | 1592 |
| 2024-09-20 22:21:33.514 | MS1 | 121.4656774352 | 31.1446325080 | 760 | 504990 | -87.31 | 14.40 | 463.99 | 0.08 | 2.49 | 1570 |
| 2024-09-20 22:21:34.616 | MS1 | 121.4656638373 | 31.1446269683 | 760 | 504990 | -91.29 | 16.46 | 89.88 | 0.61 | 2.47 | 572 |
| 2024-09-20 22:21:35.194 | MS1 | 121.4656768588 | 31.1446236776 | 760 | 504990 | -86.38 | 14.86 | 67.61 | 0.63 | 2.69 | 592 |
| 2024-09-20 22:21:36.924 | MS1 | 121.4656723125 | 31.1446270786 | 760 | 504990 | -87.41 | 12.99 | 92.87 | 0.63 | 2.79 | 520 |
| 2024-09-20 22:21:37.119 | MS1 | 121.4656731136 | 31.1446181572 | 760 | 504990 | -90.66 | 11.71 | 95.20 | 0.70 | 2.08 | 564 |
| 2024-09-20 22:21:38.762 | MS1 | 121.4656615623 | 31.1446308008 | 760 | 504990 | -89.35 | 11.86 | 86.81 | 0.64 | 2.62 | 623 |
| 2024-09-20 22:21:39.959 | MS1 | 121.4656580460 | 31.1446193068 | 760 | 504990 | -89.57 | 10.48 | 79.33 | 0.65 | 2.10 | 613 |
| 2024-09-20 22:21:40.596 | MS1 | 121.4656778033 | 31.1446183943 | 760 | 504990 | -93.49 | 11.98 | 423.87 | 0.09 | 2.88 | 1562 |
| 2024-09-20 22:21:41.830 | MS1 | 121.4656701206 | 31.1446258608 | 760 | 504990 | -89.31 | 10.39 | 342.85 | 0.14 | 2.79 | 1589 |
| 2024-09-20 22:21:42.115 | MS1 | 121.4656774822 | 31.1446193532 | 760 | 504990 | -90.85 | 11.98 | 546.45 | 0.09 | 2.55 | 1576 |

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
| 3250692 | 3 | 121.4652208230 | 31.1512585280 | 59 | 9 | 10 | 27.2 | TDD | 591 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3265544 | 1 | 121.4726985531 | 31.1547828645 | 193 | 4 | 4 | 20.1 | TDD | 760 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3267374 | 2 | 121.4737569973 | 31.1496883248 | 162 | 8 | 12 | 47.6 | TDD | 664 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3278322 | 4 | 121.4736650578 | 31.1520367568 | 303 | 5 | 2 | 40.2 | TDD | 189 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.141 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.157 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.294 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.294 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.970 | NREventA3 | measId:2;ServCellPCI:696;Se... |
| 2024-09-20 22:21:38.210 | NRHandoverAttempt | SourcePCI:696;SourceNR-ARFC... |
| 2024-09-20 22:21:38.241 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.254 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.384 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.384 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265544 | 1 | 10.4722 | 10.2043 | -116.8655 | 10.0935 | 159.3402 | 0.0095 | 0.0092 |
| 2024_09_20 22:00 | 3267374 | 2 | 8.1463 | 15.2393 | -116.3678 | 8.4715 | 148.0077 | 0.0111 | 0.0055 |
| 2024_09_20 22:00 | 3250692 | 3 | 18.4747 | 5.8776 | -117.1848 | 14.5779 | 164.6626 | 0.0165 | 0.0107 |
| 2024_09_20 22:00 | 3278322 | 4 | 16.9994 | 6.9111 | -116.4365 | 16.2099 | 94.9614 | 0.0135 | 0.0055 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413707_1875A814 | 504990 | 760 | -93.0 | 504990 | 591 | -98.1 | 504990 | 189 | -104.5 | 504990 | 664 |
| MR_1774413707_868EA40F | 504990 | 760 | -92.0 | 504990 | 591 | -98.2 | 504990 | 189 | -104.7 | 504990 | 664 |
| MR_1774413707_327D0891 | 504990 | 760 | -92.1 | 504990 | 591 | -99.8 | 504990 | 189 | -103.9 | 504990 | 664 |
| MR_1774413707_19790372 | 504990 | 760 | -92.6 | 504990 | 591 | -99.1 | 504990 | 189 | -102.2 | 504990 | 664 |
| MR_1774413707_72B71B45 | 504990 | 760 | -93.2 | 504990 | 591 | -98.6 | 504990 | 189 | -102.9 | 504990 | 664 |
| MR_1774413707_C35A46BE | 504990 | 760 | -92.9 | 504990 | 591 | -100.3 | 504990 | 189 | -103.4 | 504990 | 664 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 398: `e32e080a-d3d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e32e080a-d3dc-4176-ade8-ef0f5364516c` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[398] topology](images/train_0398.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3247020_3 by 10 degrees
- `C2`: Decrease transmission power for 3227720_4
- `C3`: Adjust the azimuth of 3227720_4 by 14 degrees
- `C4`: Lift the tilt angle  of 3247020_3 by 10 degrees
- `C5`: Check test server and transmission issues
- `C6`: Adjust the azimuth of 3247020_3 by 50 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247020_3
- `C8`: Add neighbor relationship between 3227720_4 and 3247020_3
- `C9`: Insufficient data; more data is needed for judgment. **← 정답**
- `C10`: Decrease A3 Offset threshold for 3247020_3
- `C11`: Increase A3 Offset threshold for 3227720_4
- `C12`: Increase transmission power for 3247020_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227720_4
- `C14`: Increase transmission power for 3227720_4
- `C15`: Decrease A3 Offset threshold for 3227720_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247020_3
- `C17`: Press down the tilt angle of 3227720_4 by 8 degrees
- `C18`: Decrease transmission power for 3247020_3
- `C19`: Lift the tilt angle of 3227720_4 by 8 degrees
- `C20`: Add neighbor relationship between 3219223_2 and 3247020_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227720_4
- `C22`: Increase A3 Offset threshold for 3247020_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.727 | MS1 | 121.4656655892 | 31.1446240878 | 114 | 504990 | -89.73 | 15.01 | 425.26 | 0.13 | 2.20 | 1571 |
| 2024-09-20 22:21:32.526 | MS1 | 121.4656653262 | 31.1446245934 | 114 | 504990 | -90.05 | 12.20 | 357.04 | 0.12 | 2.16 | 1562 |
| 2024-09-20 22:21:33.568 | MS1 | 121.4656597712 | 31.1446336200 | 114 | 504990 | -89.10 | 12.32 | 506.58 | 0.04 | 2.07 | 1590 |
| 2024-09-20 22:21:34.608 | MS1 | 121.4656762899 | 31.1446232951 | 114 | 504990 | -91.26 | 17.78 | 93.84 | 0.13 | 2.82 | 1584 |
| 2024-09-20 22:21:35.646 | MS1 | 121.4656603451 | 31.1446284562 | 114 | 504990 | -90.02 | 14.07 | 56.35 | 0.16 | 2.22 | 1595 |
| 2024-09-20 22:21:36.794 | MS1 | 121.4656721063 | 31.1446339718 | 114 | 504990 | -86.94 | 17.00 | 93.42 | 0.09 | 2.61 | 1598 |
| 2024-09-20 22:21:37.860 | MS1 | 121.4656729134 | 31.1446321134 | 114 | 504990 | -92.94 | 7.57 | 100.13 | 0.09 | 2.72 | 1567 |
| 2024-09-20 22:21:38.446 | MS1 | 121.4656659162 | 31.1446191677 | 114 | 504990 | -93.10 | 10.66 | 78.89 | 0.09 | 2.08 | 1560 |
| 2024-09-20 22:21:39.745 | MS1 | 121.4656585796 | 31.1446225830 | 114 | 504990 | -91.37 | 10.07 | 81.47 | 0.12 | 2.95 | 1561 |
| 2024-09-20 22:21:40.528 | MS1 | 121.4656607360 | 31.1446251287 | 114 | 504990 | -91.10 | 10.76 | 466.14 | 0.17 | 2.53 | 1594 |
| 2024-09-20 22:21:41.481 | MS1 | 121.4656751186 | 31.1446312219 | 114 | 504990 | -93.48 | 12.17 | 491.84 | 0.05 | 2.72 | 1570 |
| 2024-09-20 22:21:42.151 | MS1 | 121.4656734941 | 31.1446236956 | 114 | 504990 | -93.75 | 9.03 | 567.82 | 0.01 | 2.63 | 1561 |

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
| 3219223 | 2 | 121.4700766420 | 31.1529528331 | 116 | 6 | 0 | 30.1 | TDD | 978 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3227720 | 4 | 121.4678455568 | 31.1493742684 | 216 | 4 | 1 | 35.0 | TDD | 114 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3247020 | 3 | 121.4640072756 | 31.1547381963 | 255 | 9 | 1 | 31.0 | TDD | 683 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3253144 | 1 | 121.4759381159 | 31.1555652776 | 305 | 12 | 8 | 49.5 | TDD | 568 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.984 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.999 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.111 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.111 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.826 | NREventA3 | measId:2;ServCellPCI:982;Se... |
| 2024-09-20 22:21:38.066 | NRHandoverAttempt | SourcePCI:982;SourceNR-ARFC... |
| 2024-09-20 22:21:38.113 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.128 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.255 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.255 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3253144 | 1 | 87.0589 | 81.6790 | -115.2672 | 5.9285 | 158.2711 | 0.0068 | 0.0024 |
| 2024_09_19 22:00 | 3219223 | 2 | 87.0567 | 78.5952 | -115.8289 | 19.6529 | 146.3591 | 0.0013 | 0.0134 |
| 2024_09_19 22:00 | 3247020 | 3 | 80.8654 | 83.1733 | -117.5595 | 8.6336 | 179.0473 | 0.0111 | 0.0065 |
| 2024_09_19 22:00 | 3227720 | 4 | 80.2499 | 81.0758 | -117.3603 | 8.2356 | 90.1022 | 0.0130 | 0.0118 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412655_3C17321C | 504990 | 114 | -92.9 | 504990 | 683 | -93.2 | 504990 | 978 | -105.5 | 504990 | 568 |
| MR_1774412655_3CFFDE8C | 504990 | 114 | -92.7 | 504990 | 683 | -92.1 | 504990 | 978 | -105.5 | 504990 | 568 |
| MR_1774412655_2A609761 | 504990 | 114 | -92.1 | 504990 | 683 | -91.4 | 504990 | 978 | -107.9 | 504990 | 568 |
| MR_1774412655_AC4D0372 | 504990 | 114 | -92.9 | 504990 | 683 | -92.0 | 504990 | 978 | -104.3 | 504990 | 568 |
| MR_1774412655_387D48B1 | 504990 | 114 | -90.4 | 504990 | 683 | -90.8 | 504990 | 978 | -105.6 | 504990 | 568 |
| MR_1774412655_055686DA | 504990 | 114 | -89.6 | 504990 | 683 | -93.3 | 504990 | 978 | -106.4 | 504990 | 568 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 399: `ee1a96e3-30c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ee1a96e3-30c7-4a3b-b2af-e33e6cda5f24` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3228682_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[399] topology](images/train_0399.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3228682_1
- `C2`: Increase transmission power for 3265280_4
- `C3`: Check test server and transmission issues
- `C4`: Lift the tilt angle of 3228682_1 by 2 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265280_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228682_1 **← 정답**
- `C7`: Add neighbor relationship between 3278583_2 and 3265280_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265280_4
- `C9`: Decrease transmission power for 3265280_4
- `C10`: Adjust the azimuth of 3265280_4 by 50 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase A3 Offset threshold for 3228682_1
- `C13`: Adjust the azimuth of 3228682_1 by 38 degrees
- `C14`: Press down the tilt angle of 3228682_1 by 2 degrees
- `C15`: Add neighbor relationship between 3228682_1 and 3265280_4
- `C16`: Press down the tilt angle  of 3265280_4 by 10 degrees
- `C17`: Decrease A3 Offset threshold for 3265280_4
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228682_1
- `C19`: Lift the tilt angle  of 3265280_4 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3265280_4
- `C21`: Decrease transmission power for 3228682_1
- `C22`: Decrease A3 Offset threshold for 3228682_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.746 | MS1 | 121.4656776211 | 31.1446357442 | 761 | 504990 | -86.54 | 16.36 | 335.57 | 0.13 | 2.70 | 1596 |
| 2024-09-20 22:21:32.251 | MS1 | 121.4656586451 | 31.1446305967 | 761 | 504990 | -91.67 | 13.66 | 518.06 | 0.02 | 2.26 | 1563 |
| 2024-09-20 22:21:33.921 | MS1 | 121.4656616666 | 31.1446312390 | 761 | 504990 | -91.88 | 13.51 | 496.89 | 0.01 | 2.10 | 1567 |
| 2024-09-20 22:21:34.720 | MS1 | 121.4656600753 | 31.1446269254 | 761 | 504990 | -86.97 | 14.96 | 88.67 | 0.56 | 2.63 | 665 |
| 2024-09-20 22:21:35.654 | MS1 | 121.4656712251 | 31.1446359932 | 761 | 504990 | -88.50 | 17.11 | 66.58 | 0.68 | 2.89 | 517 |
| 2024-09-20 22:21:36.558 | MS1 | 121.4656748124 | 31.1446333226 | 761 | 504990 | -86.66 | 14.65 | 65.79 | 0.55 | 2.84 | 567 |
| 2024-09-20 22:21:37.175 | MS1 | 121.4656698893 | 31.1446365584 | 761 | 504990 | -92.93 | 7.74 | 62.29 | 0.60 | 2.24 | 615 |
| 2024-09-20 22:21:38.863 | MS1 | 121.4656597029 | 31.1446198570 | 761 | 504990 | -90.56 | 12.22 | 60.24 | 0.66 | 2.57 | 615 |
| 2024-09-20 22:21:39.672 | MS1 | 121.4656658614 | 31.1446320923 | 761 | 504990 | -91.48 | 12.20 | 75.07 | 0.52 | 2.55 | 549 |
| 2024-09-20 22:21:40.997 | MS1 | 121.4656589229 | 31.1446355673 | 761 | 504990 | -93.67 | 8.56 | 531.53 | 0.11 | 2.53 | 1592 |
| 2024-09-20 22:21:41.610 | MS1 | 121.4656677172 | 31.1446295835 | 761 | 504990 | -92.16 | 7.18 | 496.87 | 0.01 | 2.89 | 1575 |
| 2024-09-20 22:21:42.765 | MS1 | 121.4656676870 | 31.1446357032 | 761 | 504990 | -90.56 | 10.70 | 403.42 | 0.03 | 2.16 | 1589 |

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
| 3228682 | 1 | 121.4756602872 | 31.1544803209 | 183 | 1 | 9 | 19.7 | TDD | 761 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3249225 | 3 | 121.4720128217 | 31.1475205202 | 254 | 6 | 2 | 24.1 | TDD | 358 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3265280 | 4 | 121.4715066297 | 31.1480862437 | 322 | 12 | 8 | 23.1 | TDD | 598 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3278583 | 2 | 121.4713938146 | 31.1520388651 | 108 | 3 | 10 | 49.0 | TDD | 637 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.982 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.003 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.129 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.129 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.861 | NREventA3 | measId:2;ServCellPCI:352;Se... |
| 2024-09-20 22:21:38.101 | NRHandoverAttempt | SourcePCI:352;SourceNR-ARFC... |
| 2024-09-20 22:21:38.151 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.162 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.288 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.288 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228682 | 1 | 12.9563 | 13.3244 | -115.4330 | 7.8591 | 99.9875 | 0.0132 | 0.0192 |
| 2024_09_20 22:00 | 3278583 | 2 | 12.3491 | 17.1700 | -114.8147 | 8.4476 | 163.1728 | 0.0139 | 0.0159 |
| 2024_09_20 22:00 | 3249225 | 3 | 16.4234 | 11.7938 | -117.9078 | 12.9622 | 151.2545 | 0.0012 | 0.0050 |
| 2024_09_20 22:00 | 3265280 | 4 | 10.7962 | 13.6972 | -114.2750 | 9.2160 | 147.7068 | 0.0107 | 0.0115 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412114_F9CB0365 | 504990 | 761 | -87.3 | 504990 | 598 | -96.1 | 504990 | 637 | -97.6 | 504990 | 358 |
| MR_1774412114_D2A541BF | 504990 | 761 | -86.3 | 504990 | 598 | -96.6 | 504990 | 637 | -95.3 | 504990 | 358 |
| MR_1774412114_5A1C4E36 | 504990 | 761 | -85.2 | 504990 | 598 | -94.0 | 504990 | 637 | -98.3 | 504990 | 358 |
| MR_1774412114_E14DC0C3 | 504990 | 761 | -86.9 | 504990 | 598 | -93.1 | 504990 | 637 | -97.0 | 504990 | 358 |
| MR_1774412114_B7C70329 | 504990 | 761 | -86.1 | 504990 | 598 | -95.4 | 504990 | 637 | -97.8 | 504990 | 358 |
| MR_1774412114_24F80DEB | 504990 | 761 | -88.8 | 504990 | 598 | -93.2 | 504990 | 637 | -97.2 | 504990 | 358 |
| MR_1774412114_0B730C52 | 504990 | 761 | -88.8 | 504990 | 598 | -95.3 | 504990 | 637 | -98.1 | 504990 | 358 |

> *... 2개 열 생략 (전체 14열)*

---
