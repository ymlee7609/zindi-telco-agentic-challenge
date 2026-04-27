# Track A 문제 분석 — train[240]~train[249]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[240] ~ train[249] (10개)

## 목차

1. [문제 240: `dfe73feb-0db...`](#240) — single-answer, 정답: C9
2. [문제 241: `bb00003b-ce4...`](#241) — single-answer, 정답: C2
3. [문제 242: `61c97300-f66...`](#242) — single-answer, 정답: C21
4. [문제 243: `ab56ef92-e76...`](#243) — single-answer, 정답: C9
5. [문제 244: `3d0d81cc-1e5...`](#244) — single-answer, 정답: C18
6. [문제 245: `3190425a-613...`](#245) — single-answer, 정답: C9
7. [문제 246: `c3ec6632-bad...`](#246) — single-answer, 정답: C9
8. [문제 247: `01a8d226-7d9...`](#247) — single-answer, 정답: C17
9. [문제 248: `f690b619-9a4...`](#248) — single-answer, 정답: C14
10. [문제 249: `52a9ee89-1d6...`](#249) — single-answer, 정답: C5

---

### 문제 240: `dfe73feb-0db...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dfe73feb-0dba-4866-9693-925400baf492` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease A3 Offset threshold for 3267791_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[240] topology](images/train_0240.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3219814_2 by 4 degrees
- `C2`: Decrease transmission power for 3267791_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267791_1
- `C4`: Add neighbor relationship between 3249546_4 and 3219814_2
- `C5`: Lift the tilt angle of 3267791_1 by 5 degrees
- `C6`: Increase transmission power for 3219814_2
- `C7`: Adjust the azimuth of 3267791_1 by 12 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219814_2
- `C9`: Decrease A3 Offset threshold for 3267791_1 **← 정답**
- `C10`: Increase A3 Offset threshold for 3219814_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267791_1
- `C12`: Adjust the azimuth of 3219814_2 by 50 degrees
- `C13`: Increase A3 Offset threshold for 3267791_1
- `C14`: Add neighbor relationship between 3267791_1 and 3219814_2
- `C15`: Decrease A3 Offset threshold for 3219814_2
- `C16`: Decrease transmission power for 3219814_2
- `C17`: Press down the tilt angle of 3267791_1 by 5 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Check test server and transmission issues
- `C20`: Increase transmission power for 3267791_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219814_2
- `C22`: Lift the tilt angle  of 3219814_2 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.617 | MS1 | 121.4656712267 | 31.1446239255 | 840 | 504990 | -80.60 | 16.04 | 332.42 | 0.09 | 2.17 | 1594 |
| 2024-09-20 22:21:32.659 | MS1 | 121.4656715799 | 31.1446256616 | 840 | 504990 | -84.68 | 13.89 | 341.31 | 0.06 | 2.09 | 1600 |
| 2024-09-20 22:21:33.381 | MS1 | 121.4656678186 | 31.1446216324 | 840 | 504990 | -79.00 | 16.26 | 321.94 | 0.17 | 2.88 | 1598 |
| 2024-09-20 22:21:34.796 | MS1 | 121.4656588808 | 31.1446333146 | 840 | 504990 | -85.18 | -0.38 | 23.85 | 0.16 | 1.21 | 1589 |
| 2024-09-20 22:21:35.768 | MS1 | 121.4656644004 | 31.1446221089 | 840 | 504990 | -87.75 | -0.99 | 69.52 | 0.03 | 1.46 | 1560 |
| 2024-09-20 22:21:36.898 | MS1 | 121.4656643263 | 31.1446355065 | 840 | 504990 | -87.30 | -1.39 | 48.84 | 0.13 | 1.00 | 1599 |
| 2024-09-20 22:21:37.592 | MS1 | 121.4656645345 | 31.1446249342 | 840 | 504990 | -89.55 | -3.06 | 59.51 | 0.10 | 1.49 | 1582 |
| 2024-09-20 22:21:38.609 | MS1 | 121.4656655902 | 31.1446213207 | 840 | 504990 | -83.16 | -1.17 | 65.91 | 0.15 | 1.28 | 1580 |
| 2024-09-20 22:21:39.908 | MS1 | 121.4656708913 | 31.1446183954 | 810 | 504990 | -75.59 | 16.75 | 176.26 | 0.08 | 1.46 | 1595 |
| 2024-09-20 22:21:40.511 | MS1 | 121.4656668584 | 31.1446234454 | 810 | 504990 | -79.38 | 14.87 | 390.57 | 0.05 | 2.82 | 1586 |
| 2024-09-20 22:21:41.734 | MS1 | 121.4656733266 | 31.1446306589 | 810 | 504990 | -77.92 | 15.73 | 540.70 | 0.01 | 2.39 | 1567 |
| 2024-09-20 22:21:42.224 | MS1 | 121.4656585412 | 31.1446325585 | 810 | 504990 | -78.17 | 12.00 | 498.06 | 0.10 | 2.06 | 1587 |

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
| 3219814 | 2 | 121.4698399102 | 31.1530883550 | 100 | 2 | 2 | 29.1 | TDD | 810 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3224055 | 3 | 121.4740034837 | 31.1455935628 | 121 | 4 | 2 | 32.1 | TDD | 660 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3249546 | 4 | 121.4733248747 | 31.1465330115 | 353 | 5 | 6 | 47.9 | TDD | 335 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3267791 | 1 | 121.4715500923 | 31.1498554316 | 212 | 2 | 5 | 40.6 | TDD | 840 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.494 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.513 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.620 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.620 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.352 | NREventA3 | measId:2;ServCellPCI:362;Se... |
| 2024-09-20 22:21:38.592 | NRHandoverAttempt | SourcePCI:362;SourceNR-ARFC... |
| 2024-09-20 22:21:38.627 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.641 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.747 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.747 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267791 | 1 | 15.7979 | 8.8586 | -116.1454 | 7.1562 | 125.4650 | 0.0019 | 0.1883 |
| 2024_09_20 22:00 | 3219814 | 2 | 11.5965 | 6.6917 | -115.2713 | 18.9631 | 139.2914 | 0.0009 | 0.0195 |
| 2024_09_20 22:00 | 3224055 | 3 | 7.8402 | 12.3983 | -115.1808 | 14.3228 | 103.6293 | 0.0137 | 0.0120 |
| 2024_09_20 22:00 | 3249546 | 4 | 6.5057 | 14.3120 | -114.5922 | 15.8798 | 165.4716 | 0.0055 | 0.0194 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415124_6548BE14 | 504990 | 840 | -86.3 | 504990 | 810 | -78.0 | 504990 | 335 | -79.4 | 504990 | 660 |
| MR_1774415124_5870ADF9 | 504990 | 840 | -83.3 | 504990 | 810 | -77.7 | 504990 | 335 | -79.7 | 504990 | 660 |
| MR_1774415124_1F261942 | 504990 | 840 | -85.4 | 504990 | 810 | -79.4 | 504990 | 335 | -80.0 | 504990 | 660 |
| MR_1774415124_0DA24719 | 504990 | 810 | -78.0 | 504990 | 840 | -83.6 | 504990 | 335 | -81.6 | 504990 | 660 |
| MR_1774415124_99607751 | 504990 | 840 | -87.2 | 504990 | 810 | -77.0 | 504990 | 335 | -81.5 | 504990 | 660 |
| MR_1774415124_62200339 | 504990 | 810 | -77.3 | 504990 | 840 | -83.8 | 504990 | 335 | -81.1 | 504990 | 660 |
| MR_1774415124_D3645A34 | 504990 | 810 | -79.0 | 504990 | 840 | -83.5 | 504990 | 335 | -79.6 | 504990 | 660 |
| MR_1774415124_B737D3D8 | 504990 | 810 | -76.6 | 504990 | 840 | -85.6 | 504990 | 335 | -81.2 | 504990 | 660 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 241: `bb00003b-ce4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bb00003b-ce44-4488-b1ee-146d9e23c358` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[241] topology](images/train_0241.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3239837_3
- `C2`: Insufficient data; more data is needed for judgment. **← 정답**
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239837_3
- `C4`: Add neighbor relationship between 3273529_4 and 3239837_3
- `C5`: Decrease transmission power for 3239837_3
- `C6`: Increase transmission power for 3239837_3
- `C7`: Decrease A3 Offset threshold for 3214993_2
- `C8`: Lift the tilt angle  of 3239837_3 by 10 degrees
- `C9`: Lift the tilt angle of 3214993_2 by 3 degrees
- `C10`: Decrease transmission power for 3214993_2
- `C11`: Increase A3 Offset threshold for 3214993_2
- `C12`: Check test server and transmission issues
- `C13`: Decrease A3 Offset threshold for 3239837_3
- `C14`: Add neighbor relationship between 3214993_2 and 3239837_3
- `C15`: Press down the tilt angle of 3214993_2 by 3 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214993_2
- `C17`: Increase transmission power for 3214993_2
- `C18`: Adjust the azimuth of 3239837_3 by 34 degrees
- `C19`: Press down the tilt angle  of 3239837_3 by 10 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214993_2
- `C21`: Adjust the azimuth of 3214993_2 by 50 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239837_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.393 | MS1 | 121.4656662036 | 31.1446356221 | 636 | 504990 | -85.26 | 12.06 | 407.52 | 0.17 | 2.19 | 1577 |
| 2024-09-20 22:21:32.703 | MS1 | 121.4656587880 | 31.1446211110 | 636 | 504990 | -89.93 | 14.53 | 461.82 | 0.09 | 2.48 | 1597 |
| 2024-09-20 22:21:33.325 | MS1 | 121.4656721907 | 31.1446208224 | 636 | 504990 | -88.12 | 17.18 | 498.95 | 0.05 | 2.47 | 1566 |
| 2024-09-20 22:21:34.407 | MS1 | 121.4656677233 | 31.1446291884 | 636 | 504990 | -87.81 | 17.81 | 101.91 | 0.19 | 2.95 | 1565 |
| 2024-09-20 22:21:35.265 | MS1 | 121.4656750927 | 31.1446356686 | 636 | 504990 | -87.97 | 12.18 | 47.43 | 0.14 | 2.15 | 1588 |
| 2024-09-20 22:21:36.194 | MS1 | 121.4656585851 | 31.1446254240 | 636 | 504990 | -91.70 | 15.16 | 51.03 | 0.11 | 2.11 | 1566 |
| 2024-09-20 22:21:37.967 | MS1 | 121.4656586617 | 31.1446379021 | 636 | 504990 | -91.27 | 9.95 | 74.45 | 0.05 | 2.53 | 1599 |
| 2024-09-20 22:21:38.513 | MS1 | 121.4656597335 | 31.1446206892 | 636 | 504990 | -93.64 | 11.24 | 66.75 | 0.17 | 2.33 | 1595 |
| 2024-09-20 22:21:39.968 | MS1 | 121.4656626788 | 31.1446302330 | 636 | 504990 | -92.60 | 9.20 | 54.21 | 0.12 | 2.39 | 1572 |
| 2024-09-20 22:21:40.260 | MS1 | 121.4656604716 | 31.1446312047 | 636 | 504990 | -90.68 | 12.65 | 520.61 | 0.15 | 2.38 | 1592 |
| 2024-09-20 22:21:41.969 | MS1 | 121.4656757239 | 31.1446332714 | 636 | 504990 | -89.64 | 10.71 | 430.12 | 0.09 | 2.99 | 1580 |
| 2024-09-20 22:21:42.338 | MS1 | 121.4656700296 | 31.1446200268 | 636 | 504990 | -91.86 | 8.60 | 422.08 | 0.12 | 2.99 | 1578 |

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
| 3214993 | 2 | 121.4720787061 | 31.1543728534 | 43 | 2 | 8 | 28.5 | TDD | 636 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3239837 | 3 | 121.4751848628 | 31.1474773145 | 217 | 13 | 1 | 26.6 | TDD | 917 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3251722 | 1 | 121.4759039290 | 31.1552006812 | 108 | 5 | 11 | 34.3 | TDD | 898 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3273529 | 4 | 121.4708930630 | 31.1509159265 | 164 | 1 | 5 | 44.1 | TDD | 62 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.877 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.894 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.010 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.010 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.753 | NREventA3 | measId:2;ServCellPCI:29;Ser... |
| 2024-09-20 22:21:37.993 | NRHandoverAttempt | SourcePCI:29;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.028 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.041 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.160 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.160 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3251722 | 1 | 79.9268 | 76.5522 | -117.8127 | 11.1242 | 181.7987 | 0.0164 | 0.0069 |
| 2024_09_19 22:00 | 3214993 | 2 | 90.1219 | 75.4256 | -117.5980 | 9.6751 | 159.7760 | 0.0153 | 0.0095 |
| 2024_09_19 22:00 | 3239837 | 3 | 75.0637 | 92.2721 | -114.1509 | 19.5747 | 99.7473 | 0.0144 | 0.0019 |
| 2024_09_19 22:00 | 3273529 | 4 | 83.4949 | 93.0147 | -114.4346 | 10.4594 | 178.8050 | 0.0022 | 0.0160 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415765_8A4D773C | 504990 | 636 | -88.8 | 504990 | 917 | -89.4 | 504990 | 62 | -100.6 | 504990 | 898 |
| MR_1774415765_64687C26 | 504990 | 636 | -89.9 | 504990 | 917 | -88.3 | 504990 | 62 | -101.1 | 504990 | 898 |
| MR_1774415765_5F9B030F | 504990 | 636 | -88.5 | 504990 | 917 | -88.8 | 504990 | 62 | -99.8 | 504990 | 898 |
| MR_1774415765_7B5C9F9A | 504990 | 636 | -86.6 | 504990 | 917 | -91.2 | 504990 | 62 | -97.2 | 504990 | 898 |
| MR_1774415765_62D813EF | 504990 | 636 | -88.3 | 504990 | 917 | -90.3 | 504990 | 62 | -97.7 | 504990 | 898 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 242: `61c97300-f66...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `61c97300-f66d-4e34-9b22-ad094e25c6b5` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224276_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[242] topology](images/train_0242.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3273411_11 and 3260058_6
- `C2`: Increase transmission power for 3260058_6
- `C3`: Press down the tilt angle of 3224276_1 by 4 degrees
- `C4`: Increase transmission power for 3224276_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224276_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260058_6
- `C7`: Add neighbor relationship between 3224276_1 and 3260058_6
- `C8`: Check test server and transmission issues
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260058_6
- `C10`: Decrease transmission power for 3224276_1
- `C11`: Lift the tilt angle of 3224276_1 by 4 degrees
- `C12`: Decrease transmission power for 3260058_6
- `C13`: Increase A3 Offset threshold for 3260058_6
- `C14`: Decrease A3 Offset threshold for 3224276_1
- `C15`: Adjust the azimuth of 3260058_6 by 25 degrees
- `C16`: Adjust the azimuth of 3224276_1 by 45 degrees
- `C17`: Press down the tilt angle  of 3260058_6 by 2 degrees
- `C18`: Lift the tilt angle  of 3260058_6 by 2 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease A3 Offset threshold for 3260058_6
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224276_1 **← 정답**
- `C22`: Increase A3 Offset threshold for 3224276_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.637 | MS1 | 121.4656604573 | 31.1446216885 | 66 | 504990 | -95.81 | 12.48 | 563.74 | 0.07 | 2.75 | 1581 |
| 2024-09-20 22:21:32.487 | MS1 | 121.4656731488 | 31.1446335336 | 756 | 504990 | -95.12 | 12.04 | 388.30 | 0.18 | 2.11 | 1585 |
| 2024-09-20 22:21:33.586 | MS1 | 121.4656771857 | 31.1446336624 | 820 | 504990 | -95.87 | 9.61 | 442.28 | 0.10 | 2.94 | 1582 |
| 2024-09-20 22:21:34.435 | MS1 | 121.4656590595 | 31.1446246036 | 397 | 152650 | -96.00 | 5.12 | 81.91 | 0.12 | 1.68 | 903 |
| 2024-09-20 22:21:35.392 | MS1 | 121.4656723133 | 31.1446246364 | 457 | 152650 | -94.30 | 5.53 | 94.34 | 0.10 | 1.90 | 900 |
| 2024-09-20 22:21:36.897 | MS1 | 121.4656594253 | 31.1446285091 | 725 | 152650 | -94.67 | 2.87 | 101.99 | 0.03 | 1.91 | 933 |
| 2024-09-20 22:21:37.670 | MS1 | 121.4656759393 | 31.1446282555 | 726 | 152650 | -87.54 | 5.08 | 60.52 | 0.09 | 1.98 | 935 |
| 2024-09-20 22:21:38.242 | MS1 | 121.4656743557 | 31.1446371165 | 397 | 152650 | -91.11 | 3.44 | 84.35 | 0.03 | 1.67 | 955 |
| 2024-09-20 22:21:39.234 | MS1 | 121.4656636841 | 31.1446266997 | 457 | 152650 | -92.39 | 2.82 | 76.01 | 0.09 | 1.82 | 973 |
| 2024-09-20 22:21:40.882 | MS1 | 121.4656608331 | 31.1446290676 | 725 | 152650 | -96.25 | 4.01 | 52.26 | 0.06 | 2.33 | 1579 |
| 2024-09-20 22:21:41.836 | MS1 | 121.4656600981 | 31.1446207384 | 726 | 152650 | -88.06 | 3.08 | 92.62 | 0.01 | 2.81 | 1567 |
| 2024-09-20 22:21:42.107 | MS1 | 121.4656679056 | 31.1446232415 | 397 | 152650 | -94.26 | 3.67 | 79.11 | 0.05 | 2.40 | 1596 |

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
| 3216561 | 5 | 121.4708268860 | 31.1468287488 | 142 | 2 | 8 | 15.9 | TDD | 820 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3224276 | 1 | 121.4646040091 | 31.1475057313 | 118 | 1 | 1 | 17.0 | TDD | 66 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3225693 | 2 | 121.4675915417 | 31.1444029726 | 280 | 15 | 0 | 3.3 | TDD | 773 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3232421 | 10 | 121.4647730225 | 31.1444321650 | 156 | 10 | 0 | 15.0 | FDD | 626 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3237396 | 12 | 121.4759884257 | 31.1473201864 | 20 | 2 | 1 | 28.0 | FDD | 726 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3244793 | 4 | 121.4640323545 | 31.1471714553 | 351 | 11 | 7 | 18.3 | TDD | 756 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3244870 | 13 | 121.4754316159 | 31.1453521876 | 51 | 11 | 11 | 20.1 | FDD | 118 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3252844 | 8 | 121.4711202026 | 31.1498776417 | 86 | 3 | 8 | 16.0 | FDD | 457 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3256302 | 3 | 121.4648669323 | 31.1532402551 | 182 | 6 | 11 | 7.2 | TDD | 744 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3260058 | 6 | 121.4670717434 | 31.1533012242 | 163 | 1 | 0 | 25.2 | TDD | 855 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3265137 | 9 | 121.4704805836 | 31.1458612813 | 187 | 13 | 12 | 17.4 | FDD | 397 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3271276 | 7 | 121.4759213600 | 31.1540789357 | 29 | 5 | 6 | 26.1 | FDD | 64 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3273411 | 11 | 121.4698526794 | 31.1538520212 | 336 | 14 | 12 | 20.3 | FDD | 725 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |

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
| 2024-09-20 22:21:31.406 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.425 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.531 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.531 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.249 | NREventA2 | measId:1;ServCellPCI:800;Se... |
| 2024-09-20 22:21:35.370 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.600 | NREventA5 | measId:3;ServCellPCI:800;Se... |
| 2024-09-20 22:21:35.653 | NRHandoverAttempt | SourcePCI:800;SourceNR-ARFC... |
| 2024-09-20 22:21:35.682 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.696 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.813 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.813 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224276 | 1 | 13.7706 | 15.3231 | -116.0045 | 10.1266 | 129.6891 | 0.0153 | 0.0191 |
| 2024_09_20 22:00 | 3225693 | 2 | 12.5479 | 13.1242 | -117.9728 | 18.4669 | 82.0941 | 0.0178 | 0.0053 |
| 2024_09_20 22:00 | 3256302 | 3 | 14.1510 | 5.3496 | -116.2570 | 7.7344 | 135.8981 | 0.0111 | 0.0142 |
| 2024_09_20 22:00 | 3244793 | 4 | 6.5454 | 6.8376 | -116.6307 | 19.2453 | 130.7383 | 0.0041 | 0.0157 |
| 2024_09_20 22:00 | 3216561 | 5 | 13.9103 | 13.5402 | -115.3754 | 14.5506 | 167.2025 | 0.0180 | 0.0047 |
| 2024_09_20 22:00 | 3260058 | 6 | 7.0340 | 15.2299 | -114.6778 | 10.3856 | 84.4906 | 0.0122 | 0.0066 |
| 2024_09_20 22:00 | 3271276 | 7 | 13.2340 | 11.7370 | -115.9111 | 3.5918 | 50.6438 | 0.0185 | 0.0200 |
| 2024_09_20 22:00 | 3252844 | 8 | 5.4622 | 14.6057 | -117.3207 | 4.2390 | 46.8901 | 0.0118 | 0.0138 |
| 2024_09_20 22:00 | 3265137 | 9 | 9.6494 | 16.9369 | -117.7321 | 3.9378 | 39.5567 | 0.0125 | 0.0033 |
| 2024_09_20 22:00 | 3232421 | 10 | 14.4754 | 14.1674 | -116.6056 | 4.0955 | 48.3371 | 0.0047 | 0.0003 |
| 2024_09_20 22:00 | 3273411 | 11 | 6.6584 | 15.5388 | -116.3900 | 4.6364 | 32.1952 | 0.0084 | 0.0055 |
| 2024_09_20 22:00 | 3237396 | 12 | 12.7028 | 16.2445 | -115.9762 | 4.1806 | 23.7524 | 0.0156 | 0.0033 |
| 2024_09_20 22:00 | 3244870 | 13 | 13.2464 | 5.1461 | -116.3874 | 4.4645 | 35.3138 | 0.0051 | 0.0113 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416578_28D60ADB | 504990 | 820 | -95.3 | 504990 | 855 | -93.1 | 504990 | 744 | -95.7 | 504990 | 773 |
| MR_1774416578_F51E18FA | 152650 | 397 | -96.4 | 152650 | 626 | -102.9 | 152650 | 64 | -106.0 | 152650 | 118 |
| MR_1774416578_95ADE561 | 152650 | 397 | -97.6 | 152650 | 626 | -103.2 | 152650 | 64 | -107.7 | 152650 | 118 |
| MR_1774416578_10950D7F | 504990 | 820 | -96.8 | 504990 | 855 | -93.9 | 504990 | 744 | -94.3 | 504990 | 773 |
| MR_1774416578_ACC2BD40 | 504990 | 820 | -94.3 | 504990 | 855 | -95.9 | 504990 | 744 | -95.9 | 504990 | 773 |
| MR_1774416578_15F41169 | 152650 | 397 | -96.9 | 152650 | 626 | -104.8 | 152650 | 64 | -107.4 | 152650 | 118 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 243: `ab56ef92-e76...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ab56ef92-e767-416c-a438-0c2ad9ae57ba` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[243] topology](images/train_0243.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3210422_1 and 3275393_2
- `C2`: Press down the tilt angle of 3210422_1 by 10 degrees
- `C3`: Press down the tilt angle  of 3275393_2 by 5 degrees
- `C4`: Decrease A3 Offset threshold for 3210422_1
- `C5`: Increase A3 Offset threshold for 3275393_2
- `C6`: Add neighbor relationship between 3258633_3 and 3275393_2
- `C7`: Adjust the azimuth of 3210422_1 by 34 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210422_1
- `C9`: Insufficient data; more data is needed for judgment. **← 정답**
- `C10`: Increase transmission power for 3275393_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275393_2
- `C12`: Lift the tilt angle  of 3275393_2 by 5 degrees
- `C13`: Increase transmission power for 3210422_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210422_1
- `C15`: Increase A3 Offset threshold for 3210422_1
- `C16`: Decrease transmission power for 3275393_2
- `C17`: Decrease A3 Offset threshold for 3275393_2
- `C18`: Decrease transmission power for 3210422_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275393_2
- `C20`: Check test server and transmission issues
- `C21`: Lift the tilt angle of 3210422_1 by 10 degrees
- `C22`: Adjust the azimuth of 3275393_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.635 | MS1 | 121.4656652964 | 31.1446346028 | 681 | 504990 | -87.98 | 12.41 | 340.02 | 0.13 | 2.35 | 1560 |
| 2024-09-20 22:21:32.362 | MS1 | 121.4656603477 | 31.1446367334 | 681 | 504990 | -89.50 | 17.91 | 336.13 | 0.07 | 2.86 | 1567 |
| 2024-09-20 22:21:33.676 | MS1 | 121.4656688403 | 31.1446376853 | 681 | 504990 | -87.23 | 14.22 | 496.56 | 0.03 | 2.21 | 1590 |
| 2024-09-20 22:21:34.999 | MS1 | 121.4656594031 | 31.1446232295 | 681 | 504990 | -91.86 | 14.98 | 75.80 | 0.04 | 2.04 | 1564 |
| 2024-09-20 22:21:35.688 | MS1 | 121.4656580003 | 31.1446259380 | 681 | 504990 | -85.95 | 14.61 | 62.63 | 0.15 | 2.94 | 1572 |
| 2024-09-20 22:21:36.218 | MS1 | 121.4656760238 | 31.1446220375 | 681 | 504990 | -87.81 | 12.25 | 89.24 | 0.12 | 2.54 | 1567 |
| 2024-09-20 22:21:37.830 | MS1 | 121.4656716490 | 31.1446365355 | 681 | 504990 | -92.64 | 9.02 | 65.07 | 0.06 | 2.46 | 1591 |
| 2024-09-20 22:21:38.601 | MS1 | 121.4656711820 | 31.1446288251 | 681 | 504990 | -93.75 | 8.74 | 92.99 | 0.01 | 2.67 | 1590 |
| 2024-09-20 22:21:39.310 | MS1 | 121.4656694176 | 31.1446188869 | 681 | 504990 | -91.05 | 12.00 | 68.43 | 0.14 | 2.78 | 1587 |
| 2024-09-20 22:21:40.899 | MS1 | 121.4656603369 | 31.1446259527 | 681 | 504990 | -93.00 | 12.98 | 481.94 | 0.04 | 2.52 | 1588 |
| 2024-09-20 22:21:41.262 | MS1 | 121.4656736957 | 31.1446338120 | 681 | 504990 | -90.03 | 12.26 | 453.37 | 0.05 | 2.72 | 1594 |
| 2024-09-20 22:21:42.397 | MS1 | 121.4656769325 | 31.1446375043 | 681 | 504990 | -90.52 | 10.88 | 468.81 | 0.03 | 2.83 | 1563 |

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
| 3210422 | 1 | 121.4711504684 | 31.1499879187 | 255 | 13 | 9 | 37.7 | TDD | 681 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3254592 | 4 | 121.4657217994 | 31.1514808926 | 43 | 7 | 8 | 18.9 | TDD | 513 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3258633 | 3 | 121.4705736556 | 31.1459047821 | 295 | 8 | 6 | 35.6 | TDD | 294 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3275393 | 2 | 121.4669221616 | 31.1503671907 | 7 | 3 | 11 | 26.6 | TDD | 694 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.199 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.220 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.350 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.350 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.085 | NREventA3 | measId:2;ServCellPCI:420;Se... |
| 2024-09-20 22:21:38.325 | NRHandoverAttempt | SourcePCI:420;SourceNR-ARFC... |
| 2024-09-20 22:21:38.370 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.383 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.485 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.485 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3210422 | 1 | 83.2235 | 92.3928 | -117.1839 | 12.3878 | 165.8175 | 0.0165 | 0.0190 |
| 2024_09_19 22:00 | 3275393 | 2 | 76.7776 | 90.4904 | -115.3572 | 11.4185 | 179.9213 | 0.0141 | 0.0173 |
| 2024_09_19 22:00 | 3258633 | 3 | 93.4380 | 82.6866 | -114.7898 | 12.5061 | 151.3871 | 0.0008 | 0.0072 |
| 2024_09_19 22:00 | 3254592 | 4 | 92.7161 | 77.7247 | -114.3667 | 11.2530 | 105.9412 | 0.0140 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413360_E9CD6F6E | 504990 | 681 | -90.6 | 504990 | 694 | -96.4 | 504990 | 294 | -106.4 | 504990 | 513 |
| MR_1774413360_7706B6F4 | 504990 | 681 | -92.3 | 504990 | 694 | -98.4 | 504990 | 294 | -104.0 | 504990 | 513 |
| MR_1774413360_E2B0974B | 504990 | 681 | -93.0 | 504990 | 694 | -97.9 | 504990 | 294 | -105.0 | 504990 | 513 |
| MR_1774413360_E6485A2F | 504990 | 681 | -92.0 | 504990 | 694 | -94.6 | 504990 | 294 | -105.8 | 504990 | 513 |
| MR_1774413360_6CC55B2B | 504990 | 681 | -91.0 | 504990 | 694 | -96.2 | 504990 | 294 | -105.6 | 504990 | 513 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 244: `3d0d81cc-1e5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3d0d81cc-1e50-4330-8ad7-9b0459775031` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249693_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[244] topology](images/train_0244.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3252558_10 and 3244498_4
- `C2`: Press down the tilt angle of 3249693_3 by 2 degrees
- `C3`: Increase transmission power for 3249693_3
- `C4`: Adjust the azimuth of 3244498_4 by 29 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244498_4
- `C6`: Increase transmission power for 3244498_4
- `C7`: Lift the tilt angle  of 3244498_4 by 4 degrees
- `C8`: Increase A3 Offset threshold for 3244498_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249693_3
- `C10`: Decrease A3 Offset threshold for 3244498_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244498_4
- `C12`: Adjust the azimuth of 3249693_3 by 1 degrees
- `C13`: Increase A3 Offset threshold for 3249693_3
- `C14`: Add neighbor relationship between 3249693_3 and 3244498_4
- `C15`: Decrease transmission power for 3249693_3
- `C16`: Check test server and transmission issues
- `C17`: Lift the tilt angle of 3249693_3 by 2 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249693_3 **← 정답**
- `C19`: Decrease transmission power for 3244498_4
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease A3 Offset threshold for 3249693_3
- `C22`: Press down the tilt angle  of 3244498_4 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.892 | MS1 | 121.4656595397 | 31.1446205149 | 231 | 504990 | -94.07 | 9.30 | 550.47 | 0.20 | 2.45 | 1564 |
| 2024-09-20 22:21:32.624 | MS1 | 121.4656736127 | 31.1446373474 | 792 | 504990 | -93.95 | 13.54 | 507.42 | 0.13 | 2.27 | 1586 |
| 2024-09-20 22:21:33.477 | MS1 | 121.4656661975 | 31.1446216796 | 743 | 504990 | -93.94 | 14.58 | 588.43 | 0.12 | 2.51 | 1585 |
| 2024-09-20 22:21:34.670 | MS1 | 121.4656776899 | 31.1446340153 | 795 | 152650 | -87.39 | 5.63 | 59.04 | 0.08 | 1.88 | 916 |
| 2024-09-20 22:21:35.194 | MS1 | 121.4656665385 | 31.1446330928 | 430 | 152650 | -89.16 | 7.58 | 86.02 | 0.02 | 1.53 | 983 |
| 2024-09-20 22:21:36.787 | MS1 | 121.4656621855 | 31.1446315488 | 502 | 152650 | -93.36 | 3.00 | 97.62 | 0.08 | 1.90 | 994 |
| 2024-09-20 22:21:37.704 | MS1 | 121.4656609140 | 31.1446222313 | 355 | 152650 | -87.00 | 3.61 | 74.99 | 0.05 | 1.56 | 945 |
| 2024-09-20 22:21:38.416 | MS1 | 121.4656701858 | 31.1446227394 | 795 | 152650 | -90.97 | 6.97 | 91.89 | 0.17 | 1.60 | 953 |
| 2024-09-20 22:21:39.585 | MS1 | 121.4656634730 | 31.1446336811 | 430 | 152650 | -94.40 | 5.12 | 56.55 | 0.18 | 1.92 | 940 |
| 2024-09-20 22:21:40.665 | MS1 | 121.4656695107 | 31.1446317942 | 502 | 152650 | -95.38 | 5.81 | 53.15 | 0.14 | 2.19 | 1573 |
| 2024-09-20 22:21:41.162 | MS1 | 121.4656600944 | 31.1446227042 | 355 | 152650 | -90.57 | 3.08 | 55.02 | 0.15 | 2.04 | 1599 |
| 2024-09-20 22:21:42.641 | MS1 | 121.4656625295 | 31.1446189007 | 795 | 152650 | -95.37 | 5.57 | 90.55 | 0.11 | 2.24 | 1563 |

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
| 3212704 | 8 | 121.4751135377 | 31.1469290347 | 328 | 8 | 2 | 20.9 | FDD | 430 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3213916 | 9 | 121.4700331118 | 31.1541616620 | 325 | 1 | 4 | 14.4 | FDD | 849 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3214034 | 12 | 121.4688008661 | 31.1445652479 | 36 | 15 | 1 | 18.5 | FDD | 795 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3218446 | 7 | 121.4681472529 | 31.1552043091 | 84 | 9 | 6 | 27.0 | FDD | 355 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3221732 | 6 | 121.4740094069 | 31.1518551843 | 239 | 1 | 4 | 15.2 | TDD | 792 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3244498 | 4 | 121.4735396858 | 31.1472155999 | 278 | 2 | 11 | 22.2 | TDD | 747 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3249693 | 3 | 121.4657336533 | 31.1492300626 | 180 | 1 | 4 | 5.5 | TDD | 231 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3252558 | 10 | 121.4702612577 | 31.1460455213 | 48 | 0 | 3 | 17.5 | FDD | 502 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3266092 | 5 | 121.4724859682 | 31.1559330031 | 143 | 12 | 0 | 21.9 | TDD | 949 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3274168 | 2 | 121.4686821354 | 31.1533122272 | 174 | 6 | 6 | 7.5 | TDD | 743 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3278934 | 11 | 121.4730999197 | 31.1559557979 | 62 | 11 | 9 | 10.8 | FDD | 599 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3279316 | 13 | 121.4726638081 | 31.1527108777 | 23 | 0 | 5 | 16.3 | FDD | 925 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3279511 | 1 | 121.4740344511 | 31.1539667456 | 160 | 14 | 0 | 26.3 | TDD | 344 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.301 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.321 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.471 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.471 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.109 | NREventA2 | measId:1;ServCellPCI:352;Se... |
| 2024-09-20 22:21:35.213 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.426 | NREventA5 | measId:3;ServCellPCI:352;Se... |
| 2024-09-20 22:21:35.492 | NRHandoverAttempt | SourcePCI:352;SourceNR-ARFC... |
| 2024-09-20 22:21:35.519 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.531 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.672 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.672 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279511 | 1 | 5.4802 | 7.0063 | -114.4789 | 9.7802 | 108.4336 | 0.0161 | 0.0031 |
| 2024_09_20 22:00 | 3274168 | 2 | 10.3383 | 5.4480 | -115.8334 | 9.9396 | 109.3616 | 0.0049 | 0.0035 |
| 2024_09_20 22:00 | 3249693 | 3 | 18.8839 | 10.7783 | -114.4795 | 15.3587 | 100.6770 | 0.0170 | 0.0188 |
| 2024_09_20 22:00 | 3244498 | 4 | 18.8248 | 12.0162 | -115.8749 | 17.2589 | 133.8363 | 0.0146 | 0.0181 |
| 2024_09_20 22:00 | 3266092 | 5 | 19.3651 | 9.9224 | -115.6871 | 13.9206 | 172.6062 | 0.0081 | 0.0179 |
| 2024_09_20 22:00 | 3221732 | 6 | 19.7677 | 15.9558 | -115.4132 | 11.9103 | 184.0324 | 0.0018 | 0.0082 |
| 2024_09_20 22:00 | 3218446 | 7 | 16.4651 | 19.1526 | -116.7232 | 3.0210 | 58.5390 | 0.0023 | 0.0079 |
| 2024_09_20 22:00 | 3212704 | 8 | 6.9497 | 12.8989 | -116.2370 | 4.5182 | 58.5983 | 0.0009 | 0.0185 |
| 2024_09_20 22:00 | 3213916 | 9 | 14.4886 | 7.9951 | -114.8730 | 4.1712 | 40.0309 | 0.0080 | 0.0128 |
| 2024_09_20 22:00 | 3252558 | 10 | 12.3644 | 14.9323 | -117.6198 | 3.2541 | 22.1381 | 0.0078 | 0.0121 |
| 2024_09_20 22:00 | 3278934 | 11 | 5.5467 | 14.7111 | -114.9172 | 3.8037 | 31.1668 | 0.0111 | 0.0110 |
| 2024_09_20 22:00 | 3214034 | 12 | 11.5138 | 11.5980 | -116.8813 | 3.2135 | 39.8038 | 0.0105 | 0.0070 |
| 2024_09_20 22:00 | 3279316 | 13 | 18.4530 | 12.5276 | -114.3453 | 4.7933 | 45.7776 | 0.0113 | 0.0168 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413340_56CC652A | 152650 | 795 | -88.5 | 152650 | 849 | -94.9 | 152650 | 925 | -95.8 | 152650 | 599 |
| MR_1774413340_4BAFE0D2 | 504990 | 743 | -95.3 | 504990 | 747 | -92.2 | 504990 | 949 | -97.8 | 504990 | 344 |
| MR_1774413340_C090451D | 152650 | 795 | -86.9 | 152650 | 849 | -93.2 | 152650 | 925 | -94.5 | 152650 | 599 |
| MR_1774413340_E159C4D8 | 152650 | 795 | -85.6 | 152650 | 849 | -96.3 | 152650 | 925 | -94.7 | 152650 | 599 |
| MR_1774413340_C0475CAE | 504990 | 743 | -95.7 | 504990 | 747 | -91.4 | 504990 | 949 | -98.5 | 504990 | 344 |
| MR_1774413340_221B05DC | 504990 | 743 | -92.9 | 504990 | 747 | -92.3 | 504990 | 949 | -97.3 | 504990 | 344 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 245: `3190425a-613...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3190425a-6131-4fce-98f5-41e28eebec11` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Lift the tilt angle  of 3243906_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[245] topology](images/train_0245.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3243906_1 by 10 degrees
- `C2`: Lift the tilt angle of 3237987_3 by 2 degrees
- `C3`: Increase A3 Offset threshold for 3237987_3
- `C4`: Adjust the azimuth of 3237987_3 by 26 degrees
- `C5`: Increase transmission power for 3272448_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237987_3
- `C8`: Increase A3 Offset threshold for 3272448_4
- `C9`: Lift the tilt angle  of 3243906_1 by 10 degrees **← 정답**
- `C10`: Check test server and transmission issues
- `C11`: Add neighbor relationship between 3237987_3 and 3272448_4
- `C12`: Decrease transmission power for 3237987_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272448_4
- `C14`: Adjust the azimuth of 3243906_1 by 50 degrees
- `C15`: Add neighbor relationship between 3243906_1 and 3272448_4
- `C16`: Decrease A3 Offset threshold for 3272448_4
- `C17`: Press down the tilt angle of 3237987_3 by 2 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272448_4
- `C19`: Increase transmission power for 3237987_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237987_3
- `C21`: Decrease A3 Offset threshold for 3237987_3
- `C22`: Decrease transmission power for 3272448_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.118 | MS1 | 121.4656686629 | 31.1446240922 | 886 | 504990 | -87.99 | 14.07 | 439.20 | 0.05 | 2.95 | 1567 |
| 2024-09-20 22:21:32.857 | MS1 | 121.4656590345 | 31.1446308041 | 886 | 504990 | -89.46 | 16.51 | 430.38 | 0.04 | 2.53 | 1567 |
| 2024-09-20 22:21:33.403 | MS1 | 121.4656688732 | 31.1446210078 | 886 | 504990 | -87.41 | 15.99 | 469.68 | 0.07 | 2.59 | 1567 |
| 2024-09-20 22:21:34.999 | MS1 | 121.4656700626 | 31.1446349510 | 886 | 504990 | -87.36 | 14.18 | 53.76 | 0.02 | 2.78 | 1583 |
| 2024-09-20 22:21:35.346 | MS1 | 121.4656650851 | 31.1446277700 | 886 | 504990 | -85.13 | 13.19 | 67.77 | 0.04 | 2.25 | 1569 |
| 2024-09-20 22:21:36.343 | MS1 | 121.4656741933 | 31.1446182541 | 886 | 504990 | -86.45 | 13.20 | 73.37 | 0.01 | 2.57 | 1580 |
| 2024-09-20 22:21:37.858 | MS1 | 121.4656679195 | 31.1446261716 | 886 | 504990 | -93.06 | 8.54 | 84.97 | 0.08 | 2.69 | 1560 |
| 2024-09-20 22:21:38.207 | MS1 | 121.4656651349 | 31.1446342926 | 886 | 504990 | -89.85 | 12.84 | 57.75 | 0.09 | 2.55 | 1575 |
| 2024-09-20 22:21:39.908 | MS1 | 121.4656662640 | 31.1446227196 | 886 | 504990 | -92.89 | 8.13 | 71.25 | 0.13 | 2.02 | 1567 |
| 2024-09-20 22:21:40.271 | MS1 | 121.4656678097 | 31.1446191845 | 886 | 504990 | -92.28 | 10.61 | 563.91 | 0.20 | 2.95 | 1584 |
| 2024-09-20 22:21:41.354 | MS1 | 121.4656621885 | 31.1446371652 | 886 | 504990 | -93.05 | 8.07 | 400.11 | 0.16 | 2.49 | 1582 |
| 2024-09-20 22:21:42.618 | MS1 | 121.4656772959 | 31.1446255576 | 886 | 504990 | -93.01 | 10.46 | 483.31 | 0.08 | 2.17 | 1563 |

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
| 3237987 | 3 | 121.4736829829 | 31.1549319431 | 188 | 1 | 7 | 31.6 | TDD | 886 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3243906 | 1 | 121.4648497027 | 31.1515273190 | 285 | 4 | 9 | 49.9 | TDD | 185 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3272448 | 4 | 121.4752946454 | 31.1520582137 | 136 | 15 | 11 | 47.7 | TDD | 31 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3277586 | 2 | 121.4704484629 | 31.1453438704 | 58 | 5 | 10 | 22.3 | TDD | 501 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.254 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.269 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.371 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.371 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.086 | NREventA3 | measId:2;ServCellPCI:78;Ser... |
| 2024-09-20 22:21:38.326 | NRHandoverAttempt | SourcePCI:78;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.357 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.372 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.506 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.506 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243906 | 1 | 14.2819 | 5.2100 | -115.3510 | 9.5918 | 138.2176 | 0.0078 | 0.0166 |
| 2024_09_20 22:00 | 3277586 | 2 | 10.0331 | 16.5860 | -116.6637 | 9.3340 | 188.1322 | 0.0031 | 0.0160 |
| 2024_09_20 22:00 | 3237987 | 3 | 76.8113 | 87.0584 | -117.5415 | 17.1328 | 135.7562 | 0.0133 | 0.0008 |
| 2024_09_20 22:00 | 3272448 | 4 | 13.9318 | 16.1330 | -115.4451 | 7.5642 | 159.7908 | 0.0040 | 0.0143 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416292_94D46B29 | 504990 | 886 | -86.8 | 504990 | 31 | -94.5 | 504990 | 185 | -100.6 | 504990 | 501 |
| MR_1774416292_F00C2D42 | 504990 | 886 | -88.0 | 504990 | 31 | -94.8 | 504990 | 185 | -100.1 | 504990 | 501 |
| MR_1774416292_06517CD4 | 504990 | 886 | -87.6 | 504990 | 31 | -97.3 | 504990 | 185 | -99.7 | 504990 | 501 |
| MR_1774416292_5E3165B5 | 504990 | 886 | -85.4 | 504990 | 31 | -95.4 | 504990 | 185 | -98.7 | 504990 | 501 |
| MR_1774416292_263CBA47 | 504990 | 886 | -88.7 | 504990 | 31 | -95.0 | 504990 | 185 | -100.2 | 504990 | 501 |
| MR_1774416292_83A5F5C2 | 504990 | 886 | -86.2 | 504990 | 31 | -97.0 | 504990 | 185 | -100.9 | 504990 | 501 |
| MR_1774416292_42EE29A7 | 504990 | 886 | -85.9 | 504990 | 31 | -96.8 | 504990 | 185 | -101.7 | 504990 | 501 |
| MR_1774416292_4D89772B | 504990 | 886 | -85.9 | 504990 | 31 | -96.0 | 504990 | 185 | -100.4 | 504990 | 501 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 246: `c3ec6632-bad...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c3ec6632-badc-48de-95b2-4e03e3b4a6a1` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Lift the tilt angle  of 3243286_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[246] topology](images/train_0246.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3243286_3 and 3226882_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226882_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217990_2
- `C4`: Decrease transmission power for 3226882_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226882_1
- `C6`: Decrease A3 Offset threshold for 3226882_1
- `C7`: Increase A3 Offset threshold for 3217990_2
- `C8`: Decrease A3 Offset threshold for 3217990_2
- `C9`: Lift the tilt angle  of 3243286_3 by 10 degrees **← 정답**
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217990_2
- `C11`: Increase A3 Offset threshold for 3226882_1
- `C12`: Increase transmission power for 3217990_2
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease transmission power for 3217990_2
- `C15`: Adjust the azimuth of 3243286_3 by 50 degrees
- `C16`: Lift the tilt angle of 3217990_2 by 5 degrees
- `C17`: Check test server and transmission issues
- `C18`: Adjust the azimuth of 3217990_2 by 5 degrees
- `C19`: Press down the tilt angle  of 3243286_3 by 10 degrees
- `C20`: Increase transmission power for 3226882_1
- `C21`: Add neighbor relationship between 3217990_2 and 3226882_1
- `C22`: Press down the tilt angle of 3217990_2 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.762 | MS1 | 121.4656746811 | 31.1446184018 | 977 | 504990 | -88.61 | 17.45 | 449.63 | 0.16 | 2.69 | 1599 |
| 2024-09-20 22:21:32.380 | MS1 | 121.4656762169 | 31.1446186970 | 977 | 504990 | -87.79 | 15.91 | 363.57 | 0.09 | 2.33 | 1572 |
| 2024-09-20 22:21:33.166 | MS1 | 121.4656592708 | 31.1446340028 | 977 | 504990 | -87.89 | 17.68 | 341.48 | 0.11 | 2.05 | 1570 |
| 2024-09-20 22:21:34.299 | MS1 | 121.4656711355 | 31.1446192436 | 977 | 504990 | -88.79 | 13.99 | 60.03 | 0.08 | 2.25 | 1591 |
| 2024-09-20 22:21:35.683 | MS1 | 121.4656752626 | 31.1446325983 | 977 | 504990 | -91.30 | 17.04 | 101.10 | 0.12 | 2.07 | 1584 |
| 2024-09-20 22:21:36.266 | MS1 | 121.4656739409 | 31.1446193409 | 977 | 504990 | -89.58 | 14.61 | 81.36 | 0.19 | 2.31 | 1563 |
| 2024-09-20 22:21:37.996 | MS1 | 121.4656591458 | 31.1446253514 | 977 | 504990 | -89.91 | 11.44 | 65.72 | 0.09 | 2.11 | 1564 |
| 2024-09-20 22:21:38.685 | MS1 | 121.4656757462 | 31.1446294589 | 977 | 504990 | -92.01 | 12.62 | 60.32 | 0.20 | 2.84 | 1564 |
| 2024-09-20 22:21:39.855 | MS1 | 121.4656620537 | 31.1446304206 | 977 | 504990 | -93.26 | 12.24 | 61.75 | 0.07 | 2.44 | 1593 |
| 2024-09-20 22:21:40.400 | MS1 | 121.4656736171 | 31.1446278020 | 977 | 504990 | -93.58 | 11.59 | 433.27 | 0.01 | 2.24 | 1587 |
| 2024-09-20 22:21:41.951 | MS1 | 121.4656586994 | 31.1446193028 | 977 | 504990 | -89.28 | 9.98 | 486.19 | 0.09 | 2.24 | 1595 |
| 2024-09-20 22:21:42.274 | MS1 | 121.4656722099 | 31.1446319794 | 977 | 504990 | -93.15 | 7.67 | 315.89 | 0.01 | 2.27 | 1585 |

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
| 3217990 | 2 | 121.4745926553 | 31.1461496325 | 254 | 3 | 5 | 28.3 | TDD | 977 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3226882 | 1 | 121.4653769633 | 31.1445744685 | 304 | 6 | 11 | 16.8 | TDD | 560 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3243286 | 3 | 121.4702641443 | 31.1460543846 | 69 | 12 | 9 | 27.4 | TDD | 162 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3244476 | 4 | 121.4730007818 | 31.1555854748 | 310 | 7 | 4 | 26.6 | TDD | 256 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.249 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.270 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.403 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.403 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.085 | NREventA3 | measId:2;ServCellPCI:891;Se... |
| 2024-09-20 22:21:38.325 | NRHandoverAttempt | SourcePCI:891;SourceNR-ARFC... |
| 2024-09-20 22:21:38.355 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.367 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.480 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.480 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226882 | 1 | 6.4890 | 19.4870 | -116.9706 | 13.6942 | 81.3729 | 0.0143 | 0.0016 |
| 2024_09_20 22:00 | 3217990 | 2 | 84.9162 | 86.0225 | -117.9822 | 17.6413 | 189.9137 | 0.0150 | 0.0122 |
| 2024_09_20 22:00 | 3243286 | 3 | 18.6742 | 18.7514 | -115.7125 | 16.8266 | 122.1365 | 0.0130 | 0.0160 |
| 2024_09_20 22:00 | 3244476 | 4 | 5.9893 | 5.2398 | -117.1230 | 5.7823 | 109.1979 | 0.0158 | 0.0079 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416489_C773C2B5 | 504990 | 977 | -86.8 | 504990 | 560 | -93.0 | 504990 | 162 | -95.0 | 504990 | 256 |
| MR_1774416489_4B482369 | 504990 | 977 | -90.7 | 504990 | 560 | -92.7 | 504990 | 162 | -94.5 | 504990 | 256 |
| MR_1774416489_292BA101 | 504990 | 977 | -87.9 | 504990 | 560 | -92.3 | 504990 | 162 | -96.6 | 504990 | 256 |
| MR_1774416489_B97F3933 | 504990 | 977 | -90.4 | 504990 | 560 | -92.1 | 504990 | 162 | -95.9 | 504990 | 256 |
| MR_1774416489_5ABE88A6 | 504990 | 977 | -90.0 | 504990 | 560 | -92.1 | 504990 | 162 | -96.4 | 504990 | 256 |
| MR_1774416489_94B7DB34 | 504990 | 977 | -90.4 | 504990 | 560 | -92.8 | 504990 | 162 | -96.6 | 504990 | 256 |
| MR_1774416489_B01374C4 | 504990 | 977 | -87.4 | 504990 | 560 | -92.7 | 504990 | 162 | -95.3 | 504990 | 256 |
| MR_1774416489_5834A45D | 504990 | 977 | -89.0 | 504990 | 560 | -93.4 | 504990 | 162 | -93.6 | 504990 | 256 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 247: `01a8d226-7d9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `01a8d226-7d95-4f53-aa0f-21cab72f7c95` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Decrease A3 Offset threshold for 3264754_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[247] topology](images/train_0247.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3264754_1 and 3210986_4
- `C2`: Adjust the azimuth of 3264754_1 by 50 degrees
- `C3`: Increase A3 Offset threshold for 3264754_1
- `C4`: Adjust the azimuth of 3210986_4 by 50 degrees
- `C5`: Press down the tilt angle  of 3210986_4 by 10 degrees
- `C6`: Decrease transmission power for 3210986_4
- `C7`: Lift the tilt angle  of 3210986_4 by 10 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264754_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210986_4
- `C10`: Increase transmission power for 3210986_4
- `C11`: Decrease transmission power for 3264754_1
- `C12`: Add neighbor relationship between 3237277_3 and 3210986_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210986_4
- `C14`: Press down the tilt angle of 3264754_1 by 10 degrees
- `C15`: Increase transmission power for 3264754_1
- `C16`: Decrease A3 Offset threshold for 3210986_4
- `C17`: Decrease A3 Offset threshold for 3264754_1 **← 정답**
- `C18`: Check test server and transmission issues
- `C19`: Increase A3 Offset threshold for 3210986_4
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264754_1
- `C22`: Lift the tilt angle of 3264754_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.413 | MS1 | 121.4656631740 | 31.1446220828 | 841 | 504990 | -77.16 | 17.72 | 418.86 | 0.01 | 2.85 | 1588 |
| 2024-09-20 22:21:32.803 | MS1 | 121.4656623615 | 31.1446297365 | 841 | 504990 | -75.61 | 13.37 | 293.36 | 0.15 | 2.69 | 1584 |
| 2024-09-20 22:21:33.893 | MS1 | 121.4656607078 | 31.1446224498 | 841 | 504990 | -76.20 | 17.37 | 471.49 | 0.12 | 2.56 | 1578 |
| 2024-09-20 22:21:34.723 | MS1 | 121.4656700598 | 31.1446221169 | 841 | 504990 | -91.60 | -2.13 | 57.81 | 0.12 | 1.09 | 1582 |
| 2024-09-20 22:21:35.795 | MS1 | 121.4656620642 | 31.1446359908 | 841 | 504990 | -86.29 | -0.78 | 37.59 | 0.11 | 1.22 | 1563 |
| 2024-09-20 22:21:36.779 | MS1 | 121.4656594512 | 31.1446205183 | 841 | 504990 | -90.17 | -0.06 | 57.77 | 0.11 | 1.38 | 1583 |
| 2024-09-20 22:21:37.812 | MS1 | 121.4656596813 | 31.1446369932 | 841 | 504990 | -87.41 | -0.59 | 64.56 | 0.14 | 1.40 | 1580 |
| 2024-09-20 22:21:38.640 | MS1 | 121.4656658539 | 31.1446358363 | 841 | 504990 | -90.78 | -0.45 | 73.88 | 0.13 | 1.41 | 1596 |
| 2024-09-20 22:21:39.306 | MS1 | 121.4656696267 | 31.1446323998 | 390 | 504990 | -81.07 | 17.20 | 274.31 | 0.08 | 1.23 | 1595 |
| 2024-09-20 22:21:40.855 | MS1 | 121.4656589107 | 31.1446255757 | 390 | 504990 | -76.87 | 16.80 | 394.16 | 0.11 | 2.83 | 1589 |
| 2024-09-20 22:21:41.960 | MS1 | 121.4656661296 | 31.1446265316 | 390 | 504990 | -80.16 | 17.17 | 440.31 | 0.17 | 2.22 | 1583 |
| 2024-09-20 22:21:42.329 | MS1 | 121.4656723372 | 31.1446344114 | 390 | 504990 | -83.72 | 16.58 | 561.00 | 0.07 | 2.10 | 1579 |

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
| 3210986 | 4 | 121.4731354809 | 31.1472561550 | 85 | 10 | 7 | 26.2 | TDD | 390 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3237277 | 3 | 121.4660745155 | 31.1528409164 | 210 | 3 | 5 | 49.3 | TDD | 721 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3264754 | 1 | 121.4694511192 | 31.1484923001 | 314 | 11 | 10 | 32.8 | TDD | 841 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3276279 | 2 | 121.4686087055 | 31.1457711384 | 287 | 8 | 8 | 39.8 | TDD | 739 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.845 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.869 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.971 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.971 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.720 | NREventA3 | measId:2;ServCellPCI:623;Se... |
| 2024-09-20 22:21:37.960 | NRHandoverAttempt | SourcePCI:623;SourceNR-ARFC... |
| 2024-09-20 22:21:38.009 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.021 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.160 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.160 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264754 | 1 | 12.6607 | 6.6329 | -117.4819 | 14.6203 | 147.2089 | 0.0036 | 0.1493 |
| 2024_09_20 22:00 | 3276279 | 2 | 16.0977 | 7.1541 | -116.1895 | 16.3579 | 199.4026 | 0.0082 | 0.0194 |
| 2024_09_20 22:00 | 3237277 | 3 | 13.7996 | 8.8965 | -117.9970 | 6.7604 | 116.9358 | 0.0167 | 0.0060 |
| 2024_09_20 22:00 | 3210986 | 4 | 7.4512 | 13.6690 | -114.9247 | 11.1253 | 186.2976 | 0.0199 | 0.0157 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417170_76DB1494 | 504990 | 841 | -92.9 | 504990 | 390 | -85.6 | 504990 | 721 | -88.1 | 504990 | 739 |
| MR_1774417170_EB0A1FE6 | 504990 | 390 | -87.7 | 504990 | 841 | -93.0 | 504990 | 721 | -87.1 | 504990 | 739 |
| MR_1774417170_7DB9E5CA | 504990 | 841 | -93.0 | 504990 | 390 | -88.4 | 504990 | 721 | -88.9 | 504990 | 739 |
| MR_1774417170_747C125E | 504990 | 390 | -86.1 | 504990 | 841 | -91.8 | 504990 | 721 | -88.4 | 504990 | 739 |
| MR_1774417170_057845DF | 504990 | 841 | -93.2 | 504990 | 390 | -84.5 | 504990 | 721 | -88.0 | 504990 | 739 |
| MR_1774417170_90250898 | 504990 | 390 | -87.4 | 504990 | 841 | -93.5 | 504990 | 721 | -90.4 | 504990 | 739 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 248: `f690b619-9a4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f690b619-9a44-4780-b79c-402e1b9c57e8` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Add neighbor relationship between 3235483_3 and 3225567_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[248] topology](images/train_0248.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3235483_3 by 10 degrees
- `C2`: Add neighbor relationship between 3218234_4 and 3225567_1
- `C3`: Increase transmission power for 3225567_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235483_3
- `C5`: Increase transmission power for 3235483_3
- `C6`: Check test server and transmission issues
- `C7`: Decrease transmission power for 3235483_3
- `C8`: Press down the tilt angle  of 3225567_1 by 2 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225567_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235483_3
- `C11`: Decrease A3 Offset threshold for 3225567_1
- `C12`: Adjust the azimuth of 3225567_1 by 6 degrees
- `C13`: Lift the tilt angle of 3235483_3 by 10 degrees
- `C14`: Add neighbor relationship between 3235483_3 and 3225567_1 **← 정답**
- `C15`: Increase A3 Offset threshold for 3225567_1
- `C16`: Adjust the azimuth of 3235483_3 by 2 degrees
- `C17`: Decrease A3 Offset threshold for 3235483_3
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225567_1
- `C20`: Increase A3 Offset threshold for 3235483_3
- `C21`: Lift the tilt angle  of 3225567_1 by 2 degrees
- `C22`: Decrease transmission power for 3225567_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.952 | MS1 | 121.4656684913 | 31.1446267375 | 157 | 504990 | -75.79 | 17.99 | 354.45 | 0.02 | 2.68 | 1576 |
| 2024-09-20 22:21:32.974 | MS1 | 121.4656705231 | 31.1446359764 | 157 | 504990 | -82.14 | 13.40 | 431.39 | 0.05 | 2.46 | 1590 |
| 2024-09-20 22:21:33.575 | MS1 | 121.4656647961 | 31.1446210220 | 157 | 504990 | -82.96 | 15.43 | 554.72 | 0.08 | 2.58 | 1561 |
| 2024-09-20 22:21:34.979 | MS1 | 121.4656766153 | 31.1446286725 | 157 | 504990 | -85.96 | -2.08 | 44.57 | 0.02 | 1.29 | 1561 |
| 2024-09-20 22:21:35.509 | MS1 | 121.4656763177 | 31.1446287022 | 157 | 504990 | -86.81 | -3.11 | 27.18 | 0.17 | 1.04 | 1586 |
| 2024-09-20 22:21:36.153 | MS1 | 121.4656654699 | 31.1446206508 | 157 | 504990 | -92.02 | -1.68 | 60.46 | 0.16 | 1.38 | 1578 |
| 2024-09-20 22:21:37.679 | MS1 | 121.4656721325 | 31.1446251382 | 157 | 504990 | -88.62 | -1.65 | 43.63 | 0.08 | 1.24 | 1594 |
| 2024-09-20 22:21:38.468 | MS1 | 121.4656692291 | 31.1446329584 | 157 | 504990 | -84.43 | 17.35 | 552.48 | 0.20 | 1.09 | 1568 |
| 2024-09-20 22:21:39.625 | MS1 | 121.4656652030 | 31.1446199785 | 157 | 504990 | -79.56 | 15.52 | 588.29 | 0.01 | 1.21 | 1560 |
| 2024-09-20 22:21:40.777 | MS1 | 121.4656652167 | 31.1446330481 | 157 | 504990 | -76.34 | 16.45 | 417.03 | 0.14 | 2.66 | 1563 |
| 2024-09-20 22:21:41.708 | MS1 | 121.4656648732 | 31.1446237505 | 157 | 504990 | -76.26 | 16.97 | 433.12 | 0.06 | 2.00 | 1566 |
| 2024-09-20 22:21:42.251 | MS1 | 121.4656580443 | 31.1446226741 | 157 | 504990 | -84.08 | 12.93 | 362.71 | 0.00 | 2.34 | 1568 |

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
| 3213705 | 2 | 121.4658694496 | 31.1462480836 | 54 | 8 | 7 | 35.9 | TDD | 874 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3218234 | 4 | 121.4676141900 | 31.1523557073 | 0 | 12 | 5 | 16.6 | TDD | 702 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3225567 | 1 | 121.4734318605 | 31.1494955815 | 240 | 1 | 5 | 23.7 | TDD | 350 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3235483 | 3 | 121.4678332279 | 31.1482674517 | 205 | 11 | 11 | 23.4 | TDD | 157 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.128 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.148 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.264 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.264 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.964 | NREventA3 | measId:2;ServCellPCI:951;Se... |
| 2024-09-20 22:21:35.964 | NREventA3 | measId:2;ServCellPCI:951;Se... |
| 2024-09-20 22:21:36.964 | NREventA3 | measId:2;ServCellPCI:951;Se... |
| 2024-09-20 22:21:39.464 | NRRRCReestablishAttempt | PCI:951 |
| 2024-09-20 22:21:39.482 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.497 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.631 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.631 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225567 | 1 | 11.4146 | 12.0364 | -114.7193 | 7.1431 | 97.4316 | 0.0085 | 0.0088 |
| 2024_09_20 22:00 | 3213705 | 2 | 8.9633 | 19.4873 | -116.2346 | 14.7221 | 194.7346 | 0.0151 | 0.0106 |
| 2024_09_20 22:00 | 3235483 | 3 | 19.9101 | 12.7466 | -116.6663 | 11.1098 | 154.7993 | 0.0160 | 0.1777 |
| 2024_09_20 22:00 | 3218234 | 4 | 13.8421 | 15.9841 | -116.0728 | 5.4923 | 93.9064 | 0.0080 | 0.0148 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414332_739AFA32 | 504990 | 350 | -79.6 | 504990 | 157 | -87.5 | 504990 | 702 | -87.6 | 504990 | 874 |
| MR_1774414332_51871509 | 504990 | 157 | -85.2 | 504990 | 350 | -79.5 | 504990 | 702 | -86.5 | 504990 | 874 |
| MR_1774414332_CA77180E | 504990 | 157 | -84.7 | 504990 | 350 | -81.7 | 504990 | 702 | -89.5 | 504990 | 874 |
| MR_1774414332_A7F0A454 | 504990 | 350 | -79.3 | 504990 | 157 | -85.5 | 504990 | 702 | -89.8 | 504990 | 874 |
| MR_1774414332_4BAB6164 | 504990 | 350 | -81.9 | 504990 | 157 | -86.8 | 504990 | 702 | -89.7 | 504990 | 874 |
| MR_1774414332_DE9FDFDE | 504990 | 350 | -82.7 | 504990 | 157 | -86.6 | 504990 | 702 | -87.9 | 504990 | 874 |
| MR_1774414332_08B88A2D | 504990 | 157 | -86.2 | 504990 | 350 | -79.1 | 504990 | 702 | -90.0 | 504990 | 874 |
| MR_1774414332_B310DB38 | 504990 | 350 | -80.6 | 504990 | 157 | -85.0 | 504990 | 702 | -87.7 | 504990 | 874 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 249: `52a9ee89-1d6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `52a9ee89-1d61-4738-803b-7a1e784d1488` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Decrease A3 Offset threshold for 3241287_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[249] topology](images/train_0249.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3217960_3 and 3257104_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241287_2
- `C3`: Add neighbor relationship between 3241287_2 and 3257104_4
- `C4`: Decrease transmission power for 3257104_4
- `C5`: Decrease A3 Offset threshold for 3241287_2 **← 정답**
- `C6`: Increase A3 Offset threshold for 3257104_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257104_4
- `C8`: Increase transmission power for 3241287_2
- `C9`: Increase A3 Offset threshold for 3241287_2
- `C10`: Adjust the azimuth of 3257104_4 by 29 degrees
- `C11`: Lift the tilt angle  of 3257104_4 by 6 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241287_2
- `C13`: Decrease A3 Offset threshold for 3257104_4
- `C14`: Press down the tilt angle  of 3257104_4 by 6 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257104_4
- `C16`: Press down the tilt angle of 3241287_2 by 10 degrees
- `C17`: Decrease transmission power for 3241287_2
- `C18`: Adjust the azimuth of 3241287_2 by 36 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Lift the tilt angle of 3241287_2 by 10 degrees
- `C21`: Increase transmission power for 3257104_4
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.824 | MS1 | 121.4656618876 | 31.1446332788 | 282 | 504990 | -75.01 | 15.77 | 305.82 | 0.14 | 2.77 | 1596 |
| 2024-09-20 22:21:32.955 | MS1 | 121.4656726586 | 31.1446310414 | 282 | 504990 | -76.38 | 15.81 | 326.31 | 0.09 | 2.02 | 1598 |
| 2024-09-20 22:21:33.327 | MS1 | 121.4656657644 | 31.1446195037 | 282 | 504990 | -78.84 | 15.11 | 369.69 | 0.19 | 2.60 | 1577 |
| 2024-09-20 22:21:34.453 | MS1 | 121.4656738330 | 31.1446343002 | 282 | 504990 | -87.28 | -2.77 | 23.75 | 0.09 | 1.44 | 1586 |
| 2024-09-20 22:21:35.107 | MS1 | 121.4656709697 | 31.1446191030 | 282 | 504990 | -91.88 | -3.89 | 54.33 | 0.05 | 1.12 | 1572 |
| 2024-09-20 22:21:36.587 | MS1 | 121.4656586064 | 31.1446277285 | 282 | 504990 | -88.77 | -0.70 | 43.80 | 0.09 | 1.08 | 1560 |
| 2024-09-20 22:21:37.340 | MS1 | 121.4656727073 | 31.1446209234 | 282 | 504990 | -88.50 | -0.78 | 71.92 | 0.15 | 1.27 | 1578 |
| 2024-09-20 22:21:38.293 | MS1 | 121.4656736031 | 31.1446185658 | 282 | 504990 | -87.83 | -0.83 | 69.65 | 0.02 | 1.02 | 1587 |
| 2024-09-20 22:21:39.637 | MS1 | 121.4656745320 | 31.1446339792 | 798 | 504990 | -78.86 | 14.70 | 228.19 | 0.12 | 1.27 | 1596 |
| 2024-09-20 22:21:40.776 | MS1 | 121.4656653652 | 31.1446269401 | 798 | 504990 | -76.45 | 12.79 | 423.78 | 0.19 | 2.25 | 1584 |
| 2024-09-20 22:21:41.814 | MS1 | 121.4656661038 | 31.1446311305 | 798 | 504990 | -78.34 | 12.48 | 386.00 | 0.07 | 2.41 | 1576 |
| 2024-09-20 22:21:42.920 | MS1 | 121.4656757211 | 31.1446305875 | 798 | 504990 | -81.85 | 15.23 | 465.33 | 0.00 | 2.65 | 1588 |

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
| 3217960 | 3 | 121.4665972794 | 31.1452046859 | 143 | 11 | 8 | 33.7 | TDD | 198 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3241287 | 2 | 121.4685461776 | 31.1523805980 | 234 | 9 | 12 | 19.6 | TDD | 282 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3245148 | 1 | 121.4653571507 | 31.1524771565 | 114 | 8 | 8 | 17.3 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3257104 | 4 | 121.4659918723 | 31.1540608879 | 211 | 4 | 7 | 29.0 | TDD | 798 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.801 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.820 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.952 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.952 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.652 | NREventA3 | measId:2;ServCellPCI:456;Se... |
| 2024-09-20 22:21:37.892 | NRHandoverAttempt | SourcePCI:456;SourceNR-ARFC... |
| 2024-09-20 22:21:37.941 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.951 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.065 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.065 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245148 | 1 | 18.1625 | 14.4878 | -117.3485 | 11.7040 | 162.0824 | 0.0027 | 0.0022 |
| 2024_09_20 22:00 | 3241287 | 2 | 12.3660 | 6.2490 | -114.6148 | 5.5279 | 174.9602 | 0.0004 | 0.1676 |
| 2024_09_20 22:00 | 3217960 | 3 | 14.5371 | 19.2398 | -116.8721 | 17.6900 | 146.1780 | 0.0180 | 0.0054 |
| 2024_09_20 22:00 | 3257104 | 4 | 18.6545 | 7.4278 | -114.8361 | 19.5076 | 157.2453 | 0.0091 | 0.0165 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416000_2CF8E2E6 | 504990 | 282 | -88.9 | 504990 | 798 | -84.1 | 504990 | 198 | -90.0 | 504990 | 176 |
| MR_1774416000_6BC9414D | 504990 | 282 | -86.3 | 504990 | 798 | -84.9 | 504990 | 198 | -89.4 | 504990 | 176 |
| MR_1774416000_ED26A0FB | 504990 | 798 | -82.9 | 504990 | 282 | -89.1 | 504990 | 198 | -87.6 | 504990 | 176 |
| MR_1774416000_10372C8C | 504990 | 282 | -88.1 | 504990 | 798 | -82.4 | 504990 | 198 | -88.5 | 504990 | 176 |
| MR_1774416000_0966FB79 | 504990 | 282 | -85.6 | 504990 | 798 | -83.7 | 504990 | 198 | -87.8 | 504990 | 176 |
| MR_1774416000_F18E73F6 | 504990 | 798 | -84.1 | 504990 | 282 | -85.4 | 504990 | 198 | -87.7 | 504990 | 176 |

> *... 2개 열 생략 (전체 14열)*

---
