# Track A 문제 분석 — train[1880]~train[1889]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1880] ~ train[1889] (10개)

## 목차

1. [문제 1880: `f532624d-245...`](#1880) — single-answer, 정답: C15
2. [문제 1881: `d30b3cde-94f...`](#1881) — single-answer, 정답: C22
3. [문제 1882: `97ebbc89-cfc...`](#1882) — single-answer, 정답: C20
4. [문제 1883: `12e10400-c59...`](#1883) — single-answer, 정답: C11
5. [문제 1884: `7dedf194-38b...`](#1884) — multiple-answer, 정답: C12|C17
6. [문제 1885: `105b7b12-4cb...`](#1885) — single-answer, 정답: C11
7. [문제 1886: `4eca084f-cd0...`](#1886) — single-answer, 정답: C6
8. [문제 1887: `f7edba81-030...`](#1887) — single-answer, 정답: C13
9. [문제 1888: `0b215664-54a...`](#1888) — single-answer, 정답: C2
10. [문제 1889: `6ee4006d-a33...`](#1889) — single-answer, 정답: C13

---

### 문제 1880: `f532624d-245...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f532624d-245a-4f27-ba59-63f84ee77748` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Add neighbor relationship between 3239514_1 and 3241777_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1880] topology](images/train_1880.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3239514_1 by 50 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239514_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241777_3
- `C4`: Increase transmission power for 3239514_1
- `C5`: Decrease A3 Offset threshold for 3239514_1
- `C6`: Press down the tilt angle  of 3241777_3 by 3 degrees
- `C7`: Adjust the azimuth of 3241777_3 by 28 degrees
- `C8`: Decrease transmission power for 3239514_1
- `C9`: Decrease transmission power for 3241777_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241777_3
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Lift the tilt angle of 3239514_1 by 10 degrees
- `C13`: Press down the tilt angle of 3239514_1 by 10 degrees
- `C14`: Add neighbor relationship between 3216610_4 and 3241777_3
- `C15`: Add neighbor relationship between 3239514_1 and 3241777_3 **← 정답**
- `C16`: Lift the tilt angle  of 3241777_3 by 3 degrees
- `C17`: Check test server and transmission issues
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239514_1
- `C19`: Increase A3 Offset threshold for 3241777_3
- `C20`: Increase A3 Offset threshold for 3239514_1
- `C21`: Increase transmission power for 3241777_3
- `C22`: Decrease A3 Offset threshold for 3241777_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.708 | MS1 | 121.4656727192 | 31.1446253694 | 17 | 504990 | -84.04 | 13.01 | 479.66 | 0.06 | 2.67 | 1566 |
| 2024-09-20 22:21:32.944 | MS1 | 121.4656708153 | 31.1446361582 | 17 | 504990 | -82.78 | 14.83 | 444.61 | 0.11 | 2.85 | 1565 |
| 2024-09-20 22:21:33.383 | MS1 | 121.4656731021 | 31.1446201340 | 17 | 504990 | -75.11 | 15.65 | 588.37 | 0.09 | 2.15 | 1562 |
| 2024-09-20 22:21:34.338 | MS1 | 121.4656652371 | 31.1446351031 | 17 | 504990 | -93.67 | -2.96 | 50.66 | 0.07 | 1.45 | 1574 |
| 2024-09-20 22:21:35.401 | MS1 | 121.4656723231 | 31.1446270227 | 17 | 504990 | -85.30 | -3.78 | 51.80 | 0.06 | 1.50 | 1578 |
| 2024-09-20 22:21:36.369 | MS1 | 121.4656652810 | 31.1446191784 | 17 | 504990 | -88.29 | -2.78 | 36.38 | 0.14 | 1.46 | 1596 |
| 2024-09-20 22:21:37.731 | MS1 | 121.4656588598 | 31.1446281178 | 17 | 504990 | -86.68 | -1.76 | 40.80 | 0.13 | 1.06 | 1593 |
| 2024-09-20 22:21:38.665 | MS1 | 121.4656693052 | 31.1446350849 | 17 | 504990 | -83.93 | 16.39 | 428.18 | 0.18 | 1.04 | 1573 |
| 2024-09-20 22:21:39.475 | MS1 | 121.4656587009 | 31.1446248802 | 17 | 504990 | -82.17 | 16.25 | 527.68 | 0.11 | 1.12 | 1588 |
| 2024-09-20 22:21:40.543 | MS1 | 121.4656610454 | 31.1446361389 | 17 | 504990 | -83.31 | 16.63 | 503.98 | 0.19 | 2.12 | 1583 |
| 2024-09-20 22:21:41.813 | MS1 | 121.4656647092 | 31.1446260925 | 17 | 504990 | -82.27 | 17.27 | 541.56 | 0.20 | 2.86 | 1587 |
| 2024-09-20 22:21:42.255 | MS1 | 121.4656585957 | 31.1446319582 | 17 | 504990 | -75.67 | 12.84 | 388.71 | 0.08 | 2.29 | 1597 |

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
| 3216610 | 4 | 121.4737980452 | 31.1523756859 | 310 | 15 | 1 | 19.4 | TDD | 285 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3239514 | 1 | 121.4706706709 | 31.1456994606 | 31 | 10 | 7 | 40.4 | TDD | 17 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3241041 | 2 | 121.4702300624 | 31.1468571424 | 273 | 0 | 1 | 35.7 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3241777 | 3 | 121.4714241919 | 31.1506334343 | 247 | 1 | 12 | 30.4 | TDD | 995 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.325 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.349 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.459 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.459 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.188 | NREventA3 | measId:2;ServCellPCI:435;Se... |
| 2024-09-20 22:21:36.188 | NREventA3 | measId:2;ServCellPCI:435;Se... |
| 2024-09-20 22:21:37.188 | NREventA3 | measId:2;ServCellPCI:435;Se... |
| 2024-09-20 22:21:39.688 | NRRRCReestablishAttempt | PCI:435 |
| 2024-09-20 22:21:39.707 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.722 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.868 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.868 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239514 | 1 | 16.8016 | 11.0979 | -115.8446 | 7.3086 | 131.6799 | 0.0161 | 0.1078 |
| 2024_09_20 22:00 | 3241041 | 2 | 19.1639 | 15.1615 | -114.1562 | 11.4226 | 108.2054 | 0.0180 | 0.0039 |
| 2024_09_20 22:00 | 3241777 | 3 | 15.8846 | 17.5204 | -114.4601 | 19.1439 | 191.1160 | 0.0154 | 0.0122 |
| 2024_09_20 22:00 | 3216610 | 4 | 9.0004 | 5.9080 | -114.8871 | 15.1718 | 178.9099 | 0.0120 | 0.0165 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412523_108F5984 | 504990 | 995 | -89.7 | 504990 | 17 | -93.9 | 504990 | 285 | -90.7 | 504990 | 129 |
| MR_1774412523_26EA4443 | 504990 | 17 | -93.4 | 504990 | 995 | -90.1 | 504990 | 285 | -91.4 | 504990 | 129 |
| MR_1774412523_8C5381D7 | 504990 | 17 | -91.9 | 504990 | 995 | -90.0 | 504990 | 285 | -89.1 | 504990 | 129 |
| MR_1774412523_99401BED | 504990 | 995 | -89.6 | 504990 | 17 | -94.8 | 504990 | 285 | -91.2 | 504990 | 129 |
| MR_1774412523_B78F57A4 | 504990 | 17 | -94.7 | 504990 | 995 | -88.1 | 504990 | 285 | -89.7 | 504990 | 129 |
| MR_1774412523_76479188 | 504990 | 995 | -91.0 | 504990 | 17 | -93.9 | 504990 | 285 | -90.1 | 504990 | 129 |
| MR_1774412523_F252CB00 | 504990 | 995 | -90.3 | 504990 | 17 | -91.7 | 504990 | 285 | -92.2 | 504990 | 129 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1881: `d30b3cde-94f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d30b3cde-94fa-4d00-abee-ac231353f275` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease A3 Offset threshold for 3240696_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1881] topology](images/train_1881.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Check test server and transmission issues
- `C3`: Press down the tilt angle of 3240696_3 by 10 degrees
- `C4`: Increase A3 Offset threshold for 3240696_3
- `C5`: Adjust the azimuth of 3276652_1 by 50 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240696_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276652_1
- `C8`: Add neighbor relationship between 3240696_3 and 3276652_1
- `C9`: Decrease transmission power for 3276652_1
- `C10`: Increase A3 Offset threshold for 3276652_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276652_1
- `C12`: Decrease transmission power for 3240696_3
- `C13`: Lift the tilt angle  of 3276652_1 by 5 degrees
- `C14`: Adjust the azimuth of 3240696_3 by 50 degrees
- `C15`: Increase transmission power for 3276652_1
- `C16`: Increase transmission power for 3240696_3
- `C17`: Press down the tilt angle  of 3276652_1 by 5 degrees
- `C18`: Add neighbor relationship between 3220939_2 and 3276652_1
- `C19`: Lift the tilt angle of 3240696_3 by 10 degrees
- `C20`: Decrease A3 Offset threshold for 3276652_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240696_3
- `C22`: Decrease A3 Offset threshold for 3240696_3 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.373 | MS1 | 121.4656674515 | 31.1446378737 | 564 | 504990 | -82.84 | 14.22 | 393.23 | 0.15 | 2.07 | 1560 |
| 2024-09-20 22:21:32.644 | MS1 | 121.4656742279 | 31.1446379896 | 564 | 504990 | -79.61 | 16.55 | 438.90 | 0.19 | 2.28 | 1579 |
| 2024-09-20 22:21:33.802 | MS1 | 121.4656756419 | 31.1446338142 | 564 | 504990 | -79.12 | 16.85 | 344.26 | 0.09 | 2.24 | 1589 |
| 2024-09-20 22:21:34.562 | MS1 | 121.4656590527 | 31.1446221591 | 564 | 504990 | -91.88 | -0.00 | 64.30 | 0.13 | 1.15 | 1586 |
| 2024-09-20 22:21:35.569 | MS1 | 121.4656727955 | 31.1446279059 | 564 | 504990 | -84.33 | -0.10 | 57.43 | 0.10 | 1.38 | 1584 |
| 2024-09-20 22:21:36.209 | MS1 | 121.4656586617 | 31.1446252710 | 564 | 504990 | -86.55 | -2.79 | 65.04 | 0.18 | 1.02 | 1575 |
| 2024-09-20 22:21:37.371 | MS1 | 121.4656630998 | 31.1446314738 | 564 | 504990 | -91.21 | -2.60 | 54.18 | 0.07 | 1.00 | 1585 |
| 2024-09-20 22:21:38.842 | MS1 | 121.4656702195 | 31.1446292031 | 564 | 504990 | -89.15 | -0.47 | 60.68 | 0.08 | 1.45 | 1593 |
| 2024-09-20 22:21:39.324 | MS1 | 121.4656755939 | 31.1446334638 | 635 | 504990 | -84.89 | 14.21 | 166.57 | 0.15 | 1.29 | 1569 |
| 2024-09-20 22:21:40.503 | MS1 | 121.4656655738 | 31.1446336100 | 635 | 504990 | -76.06 | 12.48 | 355.54 | 0.07 | 2.72 | 1573 |
| 2024-09-20 22:21:41.930 | MS1 | 121.4656700713 | 31.1446194130 | 635 | 504990 | -75.72 | 16.82 | 381.99 | 0.08 | 2.49 | 1598 |
| 2024-09-20 22:21:42.718 | MS1 | 121.4656624582 | 31.1446321071 | 635 | 504990 | -76.46 | 15.38 | 555.18 | 0.19 | 2.26 | 1574 |

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
| 3210276 | 4 | 121.4647902350 | 31.1447876423 | 108 | 11 | 8 | 36.6 | TDD | 85 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3220939 | 2 | 121.4644431123 | 31.1485723796 | 99 | 13 | 3 | 46.2 | TDD | 867 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3240696 | 3 | 121.4722348024 | 31.1526885473 | 330 | 10 | 8 | 42.8 | TDD | 564 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3276652 | 1 | 121.4743535434 | 31.1548416437 | 111 | 4 | 4 | 34.4 | TDD | 635 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.779 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.801 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.940 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.940 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.623 | NREventA3 | measId:2;ServCellPCI:249;Se... |
| 2024-09-20 22:21:37.863 | NRHandoverAttempt | SourcePCI:249;SourceNR-ARFC... |
| 2024-09-20 22:21:37.909 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.922 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.065 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.065 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276652 | 1 | 17.2244 | 14.8460 | -114.6486 | 9.9289 | 139.9141 | 0.0088 | 0.0102 |
| 2024_09_20 22:00 | 3220939 | 2 | 13.5217 | 13.2628 | -115.5124 | 18.3634 | 103.2505 | 0.0065 | 0.0024 |
| 2024_09_20 22:00 | 3240696 | 3 | 18.9208 | 10.0402 | -115.4490 | 6.6550 | 175.4812 | 0.0136 | 0.1053 |
| 2024_09_20 22:00 | 3210276 | 4 | 12.2031 | 6.6362 | -116.6863 | 10.6666 | 168.6381 | 0.0015 | 0.0037 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415054_F1D17777 | 504990 | 564 | -93.4 | 504990 | 635 | -88.3 | 504990 | 867 | -93.5 | 504990 | 85 |
| MR_1774415054_F0606854 | 504990 | 564 | -90.4 | 504990 | 635 | -85.5 | 504990 | 867 | -92.5 | 504990 | 85 |
| MR_1774415054_107D5117 | 504990 | 564 | -92.0 | 504990 | 635 | -88.2 | 504990 | 867 | -95.9 | 504990 | 85 |
| MR_1774415054_67DD4ECB | 504990 | 564 | -92.8 | 504990 | 635 | -87.9 | 504990 | 867 | -94.3 | 504990 | 85 |
| MR_1774415054_DDB6B8BB | 504990 | 564 | -93.4 | 504990 | 635 | -84.9 | 504990 | 867 | -96.3 | 504990 | 85 |
| MR_1774415054_AF9F9373 | 504990 | 635 | -86.0 | 504990 | 564 | -93.4 | 504990 | 867 | -92.9 | 504990 | 85 |
| MR_1774415054_2D335B28 | 504990 | 564 | -90.6 | 504990 | 635 | -86.4 | 504990 | 867 | -95.9 | 504990 | 85 |
| MR_1774415054_4F6CA1B8 | 504990 | 564 | -92.5 | 504990 | 635 | -88.4 | 504990 | 867 | -94.4 | 504990 | 85 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1882: `97ebbc89-cfc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `97ebbc89-cfc5-4ac8-853c-1bbc38c94a35` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254094_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1882] topology](images/train_1882.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3275092_1 by 1 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275092_1
- `C3`: Decrease A3 Offset threshold for 3275092_1
- `C4`: Add neighbor relationship between 3279645_12 and 3275092_1
- `C5`: Adjust the azimuth of 3254094_4 by 1 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275092_1
- `C7`: Adjust the azimuth of 3275092_1 by 5 degrees
- `C8`: Add neighbor relationship between 3254094_4 and 3275092_1
- `C9`: Lift the tilt angle  of 3275092_1 by 1 degrees
- `C10`: Increase A3 Offset threshold for 3254094_4
- `C11`: Check test server and transmission issues
- `C12`: Decrease transmission power for 3254094_4
- `C13`: Increase A3 Offset threshold for 3275092_1
- `C14`: Increase transmission power for 3254094_4
- `C15`: Decrease transmission power for 3275092_1
- `C16`: Increase transmission power for 3275092_1
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease A3 Offset threshold for 3254094_4
- `C19`: Lift the tilt angle of 3254094_4 by 3 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254094_4 **← 정답**
- `C21`: Press down the tilt angle of 3254094_4 by 3 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254094_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.243 | MS1 | 121.4656680966 | 31.1446351241 | 281 | 504990 | -93.92 | 10.72 | 493.57 | 0.12 | 2.18 | 1579 |
| 2024-09-20 22:21:32.299 | MS1 | 121.4656770657 | 31.1446250589 | 21 | 504990 | -93.40 | 12.29 | 496.89 | 0.20 | 2.81 | 1590 |
| 2024-09-20 22:21:33.714 | MS1 | 121.4656612295 | 31.1446251238 | 765 | 504990 | -94.09 | 9.29 | 403.27 | 0.16 | 2.65 | 1596 |
| 2024-09-20 22:21:34.861 | MS1 | 121.4656691698 | 31.1446342826 | 605 | 152650 | -92.99 | 3.67 | 72.86 | 0.06 | 1.79 | 997 |
| 2024-09-20 22:21:35.877 | MS1 | 121.4656602402 | 31.1446313647 | 316 | 152650 | -87.96 | 3.52 | 83.36 | 0.10 | 1.70 | 964 |
| 2024-09-20 22:21:36.233 | MS1 | 121.4656705432 | 31.1446219319 | 830 | 152650 | -88.86 | 3.94 | 91.57 | 0.02 | 1.98 | 928 |
| 2024-09-20 22:21:37.455 | MS1 | 121.4656707763 | 31.1446329747 | 314 | 152650 | -88.05 | 4.84 | 80.00 | 0.00 | 1.72 | 942 |
| 2024-09-20 22:21:38.594 | MS1 | 121.4656658405 | 31.1446337674 | 605 | 152650 | -96.68 | 3.20 | 60.48 | 0.12 | 1.95 | 995 |
| 2024-09-20 22:21:39.247 | MS1 | 121.4656683966 | 31.1446333629 | 316 | 152650 | -87.39 | 4.24 | 41.94 | 0.03 | 1.79 | 941 |
| 2024-09-20 22:21:40.420 | MS1 | 121.4656761217 | 31.1446238352 | 830 | 152650 | -92.57 | 4.81 | 75.17 | 0.07 | 2.15 | 1598 |
| 2024-09-20 22:21:41.284 | MS1 | 121.4656649223 | 31.1446182348 | 314 | 152650 | -93.80 | 6.15 | 102.46 | 0.19 | 2.72 | 1577 |
| 2024-09-20 22:21:42.431 | MS1 | 121.4656699041 | 31.1446219277 | 605 | 152650 | -96.47 | 7.37 | 56.54 | 0.00 | 2.37 | 1595 |

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
| 3214232 | 13 | 121.4742450690 | 31.1456053044 | 182 | 2 | 3 | 19.1 | FDD | 604 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3229405 | 8 | 121.4721858635 | 31.1496312608 | 180 | 6 | 1 | 11.1 | FDD | 10 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3240499 | 7 | 121.4672958499 | 31.1461685901 | 291 | 8 | 9 | 7.7 | FDD | 229 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3249956 | 6 | 121.4661354528 | 31.1484791119 | 5 | 10 | 11 | 18.4 | TDD | 765 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3254094 | 4 | 121.4727639468 | 31.1539618214 | 212 | 2 | 5 | 17.5 | TDD | 281 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3263317 | 3 | 121.4759223872 | 31.1510250765 | 15 | 15 | 11 | 27.7 | TDD | 21 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3264135 | 10 | 121.4743070877 | 31.1484338622 | 290 | 11 | 0 | 10.7 | FDD | 316 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3268068 | 5 | 121.4657779813 | 31.1460260111 | 193 | 12 | 6 | 19.6 | TDD | 795 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3268136 | 2 | 121.4679391162 | 31.1535712891 | 60 | 5 | 12 | 4.8 | TDD | 19 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3275092 | 1 | 121.4653567029 | 31.1516092497 | 173 | 0 | 12 | 11.0 | TDD | 65 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3275720 | 11 | 121.4641166956 | 31.1451377373 | 266 | 4 | 4 | 26.6 | FDD | 605 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3279645 | 12 | 121.4689666037 | 31.1545828066 | 259 | 14 | 3 | 27.9 | FDD | 830 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3279863 | 9 | 121.4751899074 | 31.1470699014 | 267 | 5 | 4 | 24.2 | FDD | 314 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |

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
| 2024-09-20 22:21:31.343 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.360 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.475 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.475 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.181 | NREventA2 | measId:1;ServCellPCI:363;Se... |
| 2024-09-20 22:21:35.283 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.574 | NREventA5 | measId:3;ServCellPCI:363;Se... |
| 2024-09-20 22:21:35.639 | NRHandoverAttempt | SourcePCI:363;SourceNR-ARFC... |
| 2024-09-20 22:21:35.688 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.698 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.812 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.812 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275092 | 1 | 11.9752 | 16.4828 | -115.8489 | 17.8617 | 135.7422 | 0.0077 | 0.0052 |
| 2024_09_20 22:00 | 3268136 | 2 | 17.8317 | 18.6156 | -116.9771 | 8.9340 | 166.9247 | 0.0076 | 0.0105 |
| 2024_09_20 22:00 | 3263317 | 3 | 10.4505 | 11.8748 | -115.1166 | 19.5419 | 186.5320 | 0.0179 | 0.0055 |
| 2024_09_20 22:00 | 3254094 | 4 | 10.7086 | 9.2834 | -117.4768 | 12.0916 | 165.8200 | 0.0010 | 0.0171 |
| 2024_09_20 22:00 | 3268068 | 5 | 5.6505 | 18.8605 | -117.6829 | 18.4719 | 192.1368 | 0.0092 | 0.0003 |
| 2024_09_20 22:00 | 3249956 | 6 | 13.1558 | 7.7731 | -117.1875 | 5.3025 | 130.6437 | 0.0133 | 0.0087 |
| 2024_09_20 22:00 | 3240499 | 7 | 19.5337 | 15.4156 | -114.0658 | 4.8497 | 23.1409 | 0.0135 | 0.0029 |
| 2024_09_20 22:00 | 3229405 | 8 | 12.4981 | 9.5369 | -116.4130 | 3.3045 | 48.2270 | 0.0152 | 0.0056 |
| 2024_09_20 22:00 | 3279863 | 9 | 9.5065 | 11.2136 | -116.4068 | 4.4173 | 52.9613 | 0.0119 | 0.0021 |
| 2024_09_20 22:00 | 3264135 | 10 | 10.2269 | 13.9851 | -115.4683 | 4.1765 | 48.4361 | 0.0024 | 0.0193 |
| 2024_09_20 22:00 | 3275720 | 11 | 12.1539 | 14.9399 | -114.4003 | 3.1986 | 30.9686 | 0.0156 | 0.0172 |
| 2024_09_20 22:00 | 3279645 | 12 | 17.3701 | 6.7615 | -114.2229 | 4.4205 | 21.5671 | 0.0115 | 0.0045 |
| 2024_09_20 22:00 | 3214232 | 13 | 17.7264 | 8.9300 | -115.3715 | 3.5986 | 56.6118 | 0.0096 | 0.0158 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415171_9D2A1091 | 504990 | 765 | -95.8 | 504990 | 65 | -92.2 | 504990 | 795 | -97.4 | 504990 | 19 |
| MR_1774415171_EECCCB3F | 152650 | 605 | -93.0 | 152650 | 10 | -97.5 | 152650 | 604 | -103.6 | 152650 | 229 |
| MR_1774415171_EF14FA12 | 152650 | 605 | -94.9 | 152650 | 10 | -96.8 | 152650 | 604 | -103.3 | 152650 | 229 |
| MR_1774415171_94441546 | 504990 | 765 | -95.0 | 504990 | 65 | -92.6 | 504990 | 795 | -98.7 | 504990 | 19 |
| MR_1774415171_CF4C087A | 152650 | 605 | -91.0 | 152650 | 10 | -99.1 | 152650 | 604 | -102.3 | 152650 | 229 |
| MR_1774415171_DE793D70 | 152650 | 605 | -92.7 | 152650 | 10 | -100.1 | 152650 | 604 | -103.0 | 152650 | 229 |
| MR_1774415171_DC3917A6 | 152650 | 605 | -93.1 | 152650 | 10 | -96.8 | 152650 | 604 | -102.2 | 152650 | 229 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1883: `12e10400-c59...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `12e10400-c593-4f80-8ca9-3c63b6e83a98` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Lift the tilt angle  of 3253978_2 by 9 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1883] topology](images/train_1883.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3229326_3
- `C2`: Increase transmission power for 3229326_3
- `C3`: Decrease A3 Offset threshold for 3212562_4
- `C4`: Decrease transmission power for 3212562_4
- `C5`: Increase transmission power for 3212562_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212562_4
- `C7`: Press down the tilt angle of 3212562_4 by 3 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229326_3
- `C9`: Decrease A3 Offset threshold for 3229326_3
- `C10`: Adjust the azimuth of 3212562_4 by 12 degrees
- `C11`: Lift the tilt angle  of 3253978_2 by 9 degrees **← 정답**
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229326_3
- `C13`: Press down the tilt angle  of 3253978_2 by 9 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase A3 Offset threshold for 3212562_4
- `C16`: Decrease transmission power for 3229326_3
- `C17`: Lift the tilt angle of 3212562_4 by 3 degrees
- `C18`: Add neighbor relationship between 3212562_4 and 3229326_3
- `C19`: Add neighbor relationship between 3253978_2 and 3229326_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212562_4
- `C21`: Adjust the azimuth of 3253978_2 by 29 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.848 | MS1 | 121.4656777935 | 31.1446261770 | 68 | 504990 | -89.11 | 12.56 | 400.46 | 0.18 | 2.34 | 1586 |
| 2024-09-20 22:21:32.166 | MS1 | 121.4656753920 | 31.1446295401 | 68 | 504990 | -90.49 | 12.38 | 360.22 | 0.08 | 2.93 | 1571 |
| 2024-09-20 22:21:33.702 | MS1 | 121.4656592463 | 31.1446337742 | 68 | 504990 | -91.44 | 14.36 | 357.97 | 0.13 | 2.10 | 1586 |
| 2024-09-20 22:21:34.655 | MS1 | 121.4656693628 | 31.1446292537 | 68 | 504990 | -90.49 | 14.41 | 45.85 | 0.14 | 2.92 | 1562 |
| 2024-09-20 22:21:35.455 | MS1 | 121.4656739795 | 31.1446196297 | 68 | 504990 | -86.30 | 14.91 | 88.99 | 0.07 | 2.66 | 1584 |
| 2024-09-20 22:21:36.599 | MS1 | 121.4656633917 | 31.1446206916 | 68 | 504990 | -85.51 | 12.65 | 49.70 | 0.18 | 2.68 | 1564 |
| 2024-09-20 22:21:37.251 | MS1 | 121.4656661542 | 31.1446322839 | 68 | 504990 | -90.67 | 11.36 | 74.92 | 0.14 | 2.04 | 1577 |
| 2024-09-20 22:21:38.870 | MS1 | 121.4656592663 | 31.1446210388 | 68 | 504990 | -91.88 | 8.88 | 57.23 | 0.10 | 2.45 | 1571 |
| 2024-09-20 22:21:39.312 | MS1 | 121.4656748849 | 31.1446299870 | 68 | 504990 | -90.67 | 9.88 | 89.66 | 0.14 | 2.20 | 1566 |
| 2024-09-20 22:21:40.796 | MS1 | 121.4656680618 | 31.1446270599 | 68 | 504990 | -91.29 | 8.88 | 317.57 | 0.00 | 2.17 | 1589 |
| 2024-09-20 22:21:41.696 | MS1 | 121.4656766304 | 31.1446256053 | 68 | 504990 | -91.18 | 8.74 | 504.35 | 0.14 | 2.91 | 1598 |
| 2024-09-20 22:21:42.221 | MS1 | 121.4656756099 | 31.1446191581 | 68 | 504990 | -93.09 | 11.78 | 460.39 | 0.01 | 2.28 | 1594 |

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
| 3210255 | 1 | 121.4735481793 | 31.1472250275 | 185 | 5 | 12 | 19.5 | TDD | 305 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3212562 | 4 | 121.4678697509 | 31.1504667477 | 186 | 1 | 4 | 21.2 | TDD | 68 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3229326 | 3 | 121.4759085395 | 31.1522342842 | 200 | 7 | 0 | 47.5 | TDD | 884 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3253978 | 2 | 121.4694591572 | 31.1487721218 | 1 | 1 | 0 | 27.6 | TDD | 751 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.261 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.279 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.384 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.384 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.065 | NREventA3 | measId:2;ServCellPCI:166;Se... |
| 2024-09-20 22:21:38.305 | NRHandoverAttempt | SourcePCI:166;SourceNR-ARFC... |
| 2024-09-20 22:21:38.347 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.361 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.502 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.502 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210255 | 1 | 7.0499 | 10.9599 | -117.5922 | 17.2093 | 123.5329 | 0.0154 | 0.0053 |
| 2024_09_20 22:00 | 3253978 | 2 | 12.7255 | 16.4541 | -114.2669 | 7.0134 | 182.8248 | 0.0049 | 0.0052 |
| 2024_09_20 22:00 | 3229326 | 3 | 16.9221 | 13.1549 | -114.4450 | 6.9264 | 136.0705 | 0.0024 | 0.0194 |
| 2024_09_20 22:00 | 3212562 | 4 | 83.2547 | 93.2549 | -117.2591 | 7.5010 | 172.7461 | 0.0147 | 0.0131 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415646_829888D2 | 504990 | 68 | -90.8 | 504990 | 884 | -88.9 | 504990 | 751 | -100.0 | 504990 | 305 |
| MR_1774415646_B34E5675 | 504990 | 68 | -90.0 | 504990 | 884 | -90.6 | 504990 | 751 | -100.7 | 504990 | 305 |
| MR_1774415646_5507BC30 | 504990 | 68 | -92.4 | 504990 | 884 | -88.9 | 504990 | 751 | -97.1 | 504990 | 305 |
| MR_1774415646_3576529A | 504990 | 68 | -90.3 | 504990 | 884 | -92.0 | 504990 | 751 | -96.9 | 504990 | 305 |
| MR_1774415646_49475A9A | 504990 | 68 | -89.4 | 504990 | 884 | -92.4 | 504990 | 751 | -97.7 | 504990 | 305 |
| MR_1774415646_7F8E2AF6 | 504990 | 68 | -91.8 | 504990 | 884 | -88.7 | 504990 | 751 | -98.7 | 504990 | 305 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1884: `7dedf194-38b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7dedf194-38b6-4fd1-b755-f73f2b11830d` |
| Tag | **multiple-answer** |
| 정답 | **C12|C17** |
| C12 의미 | Press down the tilt angle  of 3229172_1 by 2 degrees |
| C17 의미 | Decrease transmission power for 3229172_1 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1884] topology](images/train_1884.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3245527_3 and 3229172_1
- `C2`: Decrease A3 Offset threshold for 3229172_1
- `C3`: Increase A3 Offset threshold for 3229172_1
- `C4`: Add neighbor relationship between 3261279_2 and 3229172_1
- `C5`: Lift the tilt angle of 3261279_2 by 4 degrees
- `C6`: Press down the tilt angle of 3261279_2 by 4 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229172_1
- `C8`: Decrease transmission power for 3261279_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229172_1
- `C10`: Increase transmission power for 3261279_2
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Press down the tilt angle  of 3229172_1 by 2 degrees **← 정답**
- `C13`: Check test server and transmission issues
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261279_2
- `C15`: Adjust the azimuth of 3229172_1 by 14 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261279_2
- `C17`: Decrease transmission power for 3229172_1 **← 정답**
- `C18`: Adjust the azimuth of 3261279_2 by 19 degrees
- `C19`: Decrease A3 Offset threshold for 3261279_2
- `C20`: Increase A3 Offset threshold for 3261279_2
- `C21`: Lift the tilt angle  of 3229172_1 by 2 degrees
- `C22`: Increase transmission power for 3229172_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.888 | MS1 | 121.4656752388 | 31.1446356198 | 785 | 504990 | -83.89 | 12.24 | 515.72 | 0.15 | 2.47 | 1574 |
| 2024-09-20 22:21:32.286 | MS1 | 121.4656746071 | 31.1446285405 | 785 | 504990 | -83.41 | 14.37 | 560.87 | 0.14 | 2.08 | 1581 |
| 2024-09-20 22:21:33.797 | MS1 | 121.4656594104 | 31.1446280402 | 785 | 504990 | -80.86 | 14.05 | 538.18 | 0.09 | 2.36 | 1563 |
| 2024-09-20 22:21:34.979 | MS1 | 121.4656770273 | 31.1446335386 | 785 | 504990 | -94.38 | 0.41 | 71.83 | 0.06 | 1.44 | 1583 |
| 2024-09-20 22:21:35.234 | MS1 | 121.4656624123 | 31.1446291403 | 785 | 504990 | -88.02 | 0.06 | 47.38 | 0.15 | 1.01 | 1578 |
| 2024-09-20 22:21:36.108 | MS1 | 121.4656586134 | 31.1446244273 | 785 | 504990 | -92.57 | 0.96 | 72.96 | 0.17 | 1.04 | 1593 |
| 2024-09-20 22:21:37.943 | MS1 | 121.4656657592 | 31.1446293864 | 785 | 504990 | -89.85 | 3.16 | 63.55 | 0.11 | 1.06 | 1571 |
| 2024-09-20 22:21:38.828 | MS1 | 121.4656688640 | 31.1446187020 | 785 | 504990 | -86.62 | 1.83 | 48.67 | 0.17 | 1.07 | 1571 |
| 2024-09-20 22:21:39.591 | MS1 | 121.4656700653 | 31.1446210417 | 785 | 504990 | -86.39 | 3.36 | 80.47 | 0.16 | 1.15 | 1597 |
| 2024-09-20 22:21:40.334 | MS1 | 121.4656611471 | 31.1446345337 | 785 | 504990 | -81.76 | 14.09 | 425.82 | 0.14 | 2.42 | 1586 |
| 2024-09-20 22:21:41.123 | MS1 | 121.4656751906 | 31.1446256505 | 785 | 504990 | -77.58 | 15.32 | 566.65 | 0.03 | 2.90 | 1590 |
| 2024-09-20 22:21:42.165 | MS1 | 121.4656649603 | 31.1446269771 | 785 | 504990 | -81.36 | 14.47 | 555.69 | 0.13 | 2.25 | 1587 |

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
| 3225647 | 4 | 121.4740067627 | 31.1530432977 | 232 | 11 | 2 | 30.3 | TDD | 751 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3229172 | 1 | 121.4716499957 | 31.1485806248 | 246 | 0 | 7 | 27.9 | TDD | 38 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3245527 | 3 | 121.4721004776 | 31.1549859558 | 228 | 0 | 10 | 33.2 | TDD | 822 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3261279 | 2 | 121.4667951527 | 31.1530441924 | 206 | 2 | 4 | 40.9 | TDD | 785 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.994 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.016 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.126 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.126 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229172 | 1 | 18.9020 | 19.3259 | -115.3452 | 10.5489 | 191.8646 | 0.0143 | 0.0172 |
| 2024_09_20 22:00 | 3261279 | 2 | 13.8443 | 19.3499 | -109.0692 | 5.4562 | 127.3729 | 0.0013 | 0.0134 |
| 2024_09_20 22:00 | 3245527 | 3 | 8.1630 | 12.4444 | -116.2017 | 7.5316 | 103.8543 | 0.0041 | 0.0055 |
| 2024_09_20 22:00 | 3225647 | 4 | 9.4423 | 8.6636 | -114.6849 | 18.4139 | 145.5396 | 0.0186 | 0.0156 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413711_B134BEE9 | 504990 | 785 | -93.7 | 504990 | 38 | -91.0 | 504990 | 822 | -92.0 | 504990 | 751 |
| MR_1774413711_D1CA17B0 | 504990 | 38 | -94.7 | 504990 | 785 | -91.8 | 504990 | 822 | -91.7 | 504990 | 751 |
| MR_1774413711_66A83E95 | 504990 | 785 | -92.5 | 504990 | 38 | -90.9 | 504990 | 822 | -90.2 | 504990 | 751 |
| MR_1774413711_E635ADC5 | 504990 | 38 | -95.7 | 504990 | 785 | -91.2 | 504990 | 822 | -89.7 | 504990 | 751 |
| MR_1774413711_BBB77197 | 504990 | 38 | -93.7 | 504990 | 785 | -91.6 | 504990 | 822 | -89.4 | 504990 | 751 |
| MR_1774413711_C13F2AFD | 504990 | 785 | -94.1 | 504990 | 38 | -90.4 | 504990 | 822 | -92.3 | 504990 | 751 |
| MR_1774413711_793520CF | 504990 | 785 | -94.7 | 504990 | 38 | -89.4 | 504990 | 822 | -91.4 | 504990 | 751 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1885: `105b7b12-4cb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `105b7b12-4cb9-4acd-a56c-12dd8ebfbd51` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220139_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1885] topology](images/train_1885.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3220139_1
- `C2`: Decrease A3 Offset threshold for 3249216_3
- `C3`: Press down the tilt angle  of 3249216_3 by 1 degrees
- `C4`: Increase transmission power for 3220139_1
- `C5`: Increase transmission power for 3249216_3
- `C6`: Press down the tilt angle of 3220139_1 by 1 degrees
- `C7`: Adjust the azimuth of 3249216_3 by 32 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase A3 Offset threshold for 3220139_1
- `C10`: Lift the tilt angle  of 3249216_3 by 1 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220139_1 **← 정답**
- `C12`: Add neighbor relationship between 3220139_1 and 3249216_3
- `C13`: Add neighbor relationship between 3261850_9 and 3249216_3
- `C14`: Decrease A3 Offset threshold for 3220139_1
- `C15`: Increase A3 Offset threshold for 3249216_3
- `C16`: Lift the tilt angle of 3220139_1 by 1 degrees
- `C17`: Adjust the azimuth of 3220139_1 by 21 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249216_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249216_3
- `C20`: Check test server and transmission issues
- `C21`: Decrease transmission power for 3249216_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220139_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.840 | MS1 | 121.4656747315 | 31.1446376705 | 71 | 504990 | -95.77 | 9.60 | 357.42 | 0.14 | 2.80 | 1578 |
| 2024-09-20 22:21:32.983 | MS1 | 121.4656634770 | 31.1446230459 | 790 | 504990 | -95.17 | 12.37 | 416.91 | 0.05 | 2.74 | 1576 |
| 2024-09-20 22:21:33.402 | MS1 | 121.4656666006 | 31.1446245250 | 377 | 504990 | -93.18 | 12.36 | 425.65 | 0.16 | 2.76 | 1563 |
| 2024-09-20 22:21:34.384 | MS1 | 121.4656588862 | 31.1446245974 | 674 | 152650 | -92.99 | 2.80 | 65.44 | 0.18 | 1.50 | 985 |
| 2024-09-20 22:21:35.147 | MS1 | 121.4656749683 | 31.1446299588 | 347 | 152650 | -94.65 | 4.05 | 65.06 | 0.08 | 1.83 | 936 |
| 2024-09-20 22:21:36.634 | MS1 | 121.4656747296 | 31.1446282367 | 941 | 152650 | -90.21 | 2.74 | 96.68 | 0.15 | 1.64 | 902 |
| 2024-09-20 22:21:37.831 | MS1 | 121.4656692165 | 31.1446214757 | 945 | 152650 | -93.58 | 6.82 | 68.01 | 0.11 | 1.66 | 908 |
| 2024-09-20 22:21:38.830 | MS1 | 121.4656730347 | 31.1446197035 | 674 | 152650 | -96.57 | 2.68 | 73.20 | 0.19 | 1.72 | 972 |
| 2024-09-20 22:21:39.236 | MS1 | 121.4656699193 | 31.1446363712 | 347 | 152650 | -90.28 | 5.76 | 81.36 | 0.10 | 1.64 | 990 |
| 2024-09-20 22:21:40.994 | MS1 | 121.4656775620 | 31.1446356708 | 941 | 152650 | -89.65 | 4.83 | 89.63 | 0.15 | 2.65 | 1588 |
| 2024-09-20 22:21:41.572 | MS1 | 121.4656667127 | 31.1446258282 | 945 | 152650 | -93.41 | 4.87 | 76.82 | 0.20 | 2.21 | 1571 |
| 2024-09-20 22:21:42.201 | MS1 | 121.4656656545 | 31.1446290066 | 674 | 152650 | -95.60 | 7.78 | 89.25 | 0.15 | 2.85 | 1581 |

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
| 3216528 | 11 | 121.4674646452 | 31.1478929212 | 250 | 7 | 2 | 5.4 | FDD | 347 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3220139 | 1 | 121.4664043463 | 31.1538329038 | 163 | 1 | 10 | 2.2 | TDD | 71 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3224742 | 5 | 121.4677026197 | 31.1455433010 | 320 | 0 | 10 | 19.1 | TDD | 694 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3229913 | 13 | 121.4744088606 | 31.1484418794 | 211 | 11 | 6 | 28.3 | FDD | 831 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3234789 | 4 | 121.4665872107 | 31.1526038474 | 166 | 14 | 0 | 26.7 | TDD | 790 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3246349 | 7 | 121.4680636487 | 31.1546504579 | 269 | 9 | 12 | 9.3 | FDD | 674 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3249216 | 3 | 121.4745821409 | 31.1488534686 | 209 | 1 | 9 | 8.0 | TDD | 850 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3254934 | 12 | 121.4733115789 | 31.1456773209 | 174 | 3 | 1 | 23.4 | FDD | 988 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3261737 | 6 | 121.4743432956 | 31.1467409597 | 297 | 11 | 11 | 14.0 | TDD | 377 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3261850 | 9 | 121.4709196062 | 31.1550701893 | 32 | 14 | 8 | 6.7 | FDD | 941 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3267599 | 10 | 121.4729164499 | 31.1552515036 | 46 | 0 | 5 | 16.4 | FDD | 945 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3276082 | 2 | 121.4676994333 | 31.1450759898 | 125 | 14 | 4 | 27.5 | TDD | 689 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3279911 | 8 | 121.4738588364 | 31.1553468594 | 110 | 14 | 0 | 15.9 | FDD | 546 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |

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
| 2024-09-20 22:21:31.647 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.672 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.788 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.788 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.496 | NREventA2 | measId:1;ServCellPCI:375;Se... |
| 2024-09-20 22:21:35.627 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.900 | NREventA5 | measId:3;ServCellPCI:375;Se... |
| 2024-09-20 22:21:35.949 | NRHandoverAttempt | SourcePCI:375;SourceNR-ARFC... |
| 2024-09-20 22:21:35.976 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.988 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:36.106 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.106 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220139 | 1 | 12.3396 | 10.0885 | -114.6716 | 15.1345 | 181.7814 | 0.0019 | 0.0199 |
| 2024_09_20 22:00 | 3276082 | 2 | 17.5662 | 12.0522 | -117.2864 | 10.6927 | 120.3052 | 0.0178 | 0.0057 |
| 2024_09_20 22:00 | 3249216 | 3 | 5.6989 | 14.4608 | -117.1727 | 12.9724 | 127.1367 | 0.0027 | 0.0031 |
| 2024_09_20 22:00 | 3234789 | 4 | 18.5974 | 11.6895 | -117.7392 | 14.7339 | 160.3852 | 0.0073 | 0.0063 |
| 2024_09_20 22:00 | 3224742 | 5 | 12.2938 | 17.9976 | -117.4107 | 18.2154 | 110.8777 | 0.0108 | 0.0100 |
| 2024_09_20 22:00 | 3261737 | 6 | 9.9449 | 7.9508 | -115.6557 | 9.2528 | 170.1119 | 0.0186 | 0.0100 |
| 2024_09_20 22:00 | 3246349 | 7 | 19.7807 | 16.8590 | -116.3421 | 4.1038 | 34.6911 | 0.0078 | 0.0090 |
| 2024_09_20 22:00 | 3279911 | 8 | 15.1297 | 9.6137 | -116.4150 | 3.0912 | 30.5956 | 0.0116 | 0.0030 |
| 2024_09_20 22:00 | 3261850 | 9 | 15.4359 | 18.1996 | -114.1764 | 4.4975 | 52.4534 | 0.0079 | 0.0183 |
| 2024_09_20 22:00 | 3267599 | 10 | 11.0443 | 7.9253 | -114.1619 | 3.3983 | 31.6927 | 0.0128 | 0.0110 |
| 2024_09_20 22:00 | 3216528 | 11 | 16.6072 | 10.6268 | -116.8591 | 3.0254 | 39.3548 | 0.0125 | 0.0077 |
| 2024_09_20 22:00 | 3254934 | 12 | 17.2332 | 11.5037 | -116.9064 | 3.1252 | 59.4955 | 0.0160 | 0.0153 |
| 2024_09_20 22:00 | 3229913 | 13 | 5.7128 | 14.2907 | -114.1153 | 3.9857 | 34.0077 | 0.0011 | 0.0059 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412852_BF435D53 | 504990 | 377 | -94.2 | 504990 | 850 | -91.8 | 504990 | 689 | -94.6 | 504990 | 694 |
| MR_1774412852_F9968B71 | 504990 | 377 | -94.7 | 504990 | 850 | -93.4 | 504990 | 689 | -93.0 | 504990 | 694 |
| MR_1774412852_3D808406 | 504990 | 377 | -93.3 | 504990 | 850 | -94.4 | 504990 | 689 | -94.8 | 504990 | 694 |
| MR_1774412852_A4AC69E3 | 152650 | 674 | -93.7 | 152650 | 831 | -100.1 | 152650 | 546 | -100.4 | 152650 | 988 |
| MR_1774412852_59A7D8AD | 152650 | 674 | -92.0 | 152650 | 831 | -98.1 | 152650 | 546 | -98.6 | 152650 | 988 |
| MR_1774412852_D9F04517 | 152650 | 674 | -91.4 | 152650 | 831 | -96.9 | 152650 | 546 | -99.1 | 152650 | 988 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1886: `4eca084f-cd0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4eca084f-cd07-436d-ba82-79ea70084082` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Lift the tilt angle  of 3226100_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1886] topology](images/train_1886.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3253509_2
- `C2`: Decrease transmission power for 3253509_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245368_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253509_2
- `C5`: Adjust the azimuth of 3226100_3 by 11 degrees
- `C6`: Lift the tilt angle  of 3226100_3 by 10 degrees **← 정답**
- `C7`: Adjust the azimuth of 3245368_4 by 48 degrees
- `C8`: Decrease transmission power for 3245368_4
- `C9`: Press down the tilt angle of 3245368_4 by 4 degrees
- `C10`: Increase A3 Offset threshold for 3253509_2
- `C11`: Lift the tilt angle of 3245368_4 by 4 degrees
- `C12`: Press down the tilt angle  of 3226100_3 by 10 degrees
- `C13`: Check test server and transmission issues
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245368_4
- `C15`: Increase transmission power for 3245368_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253509_2
- `C17`: Decrease A3 Offset threshold for 3253509_2
- `C18`: Add neighbor relationship between 3226100_3 and 3253509_2
- `C19`: Add neighbor relationship between 3245368_4 and 3253509_2
- `C20`: Decrease A3 Offset threshold for 3245368_4
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Increase A3 Offset threshold for 3245368_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.378 | MS1 | 121.4656768427 | 31.1446239686 | 911 | 504990 | -87.59 | 17.42 | 548.08 | 0.12 | 2.42 | 1563 |
| 2024-09-20 22:21:32.837 | MS1 | 121.4656595020 | 31.1446332034 | 911 | 504990 | -91.12 | 15.66 | 387.42 | 0.18 | 2.52 | 1563 |
| 2024-09-20 22:21:33.403 | MS1 | 121.4656590231 | 31.1446219642 | 911 | 504990 | -88.42 | 17.98 | 520.76 | 0.05 | 2.77 | 1577 |
| 2024-09-20 22:21:34.894 | MS1 | 121.4656678122 | 31.1446336358 | 911 | 504990 | -86.89 | 12.96 | 77.88 | 0.14 | 2.20 | 1587 |
| 2024-09-20 22:21:35.340 | MS1 | 121.4656734107 | 31.1446312500 | 911 | 504990 | -86.16 | 12.99 | 57.11 | 0.01 | 2.29 | 1563 |
| 2024-09-20 22:21:36.832 | MS1 | 121.4656712785 | 31.1446257363 | 911 | 504990 | -85.00 | 15.58 | 87.66 | 0.17 | 2.45 | 1581 |
| 2024-09-20 22:21:37.149 | MS1 | 121.4656706344 | 31.1446304364 | 911 | 504990 | -91.21 | 10.63 | 61.74 | 0.13 | 2.11 | 1560 |
| 2024-09-20 22:21:38.211 | MS1 | 121.4656777608 | 31.1446241694 | 911 | 504990 | -91.79 | 8.55 | 74.44 | 0.04 | 2.06 | 1576 |
| 2024-09-20 22:21:39.958 | MS1 | 121.4656654879 | 31.1446366225 | 911 | 504990 | -89.76 | 11.31 | 88.10 | 0.10 | 2.31 | 1561 |
| 2024-09-20 22:21:40.704 | MS1 | 121.4656588434 | 31.1446365057 | 911 | 504990 | -91.47 | 10.21 | 424.71 | 0.05 | 2.41 | 1566 |
| 2024-09-20 22:21:41.834 | MS1 | 121.4656705062 | 31.1446243956 | 911 | 504990 | -91.55 | 8.09 | 557.23 | 0.12 | 2.15 | 1577 |
| 2024-09-20 22:21:42.600 | MS1 | 121.4656740275 | 31.1446263607 | 911 | 504990 | -91.65 | 12.10 | 579.21 | 0.04 | 2.57 | 1567 |

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
| 3226100 | 3 | 121.4730434276 | 31.1462126279 | 327 | 12 | 3 | 42.3 | TDD | 803 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3238033 | 1 | 121.4662822992 | 31.1489985025 | 220 | 1 | 12 | 35.2 | TDD | 432 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3245368 | 4 | 121.4683756090 | 31.1539337715 | 242 | 1 | 11 | 47.8 | TDD | 911 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3253509 | 2 | 121.4679840299 | 31.1473235842 | 205 | 13 | 10 | 28.9 | TDD | 345 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.570 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.720 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.720 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.451 | NREventA3 | measId:2;ServCellPCI:171;Se... |
| 2024-09-20 22:21:38.691 | NRHandoverAttempt | SourcePCI:171;SourceNR-ARFC... |
| 2024-09-20 22:21:38.723 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.734 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.875 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.875 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238033 | 1 | 8.3722 | 16.7841 | -114.4678 | 19.4370 | 112.4912 | 0.0169 | 0.0021 |
| 2024_09_20 22:00 | 3253509 | 2 | 15.9385 | 13.7134 | -117.2475 | 17.6682 | 117.2372 | 0.0040 | 0.0191 |
| 2024_09_20 22:00 | 3226100 | 3 | 14.5124 | 9.9775 | -115.5755 | 18.6060 | 111.2871 | 0.0094 | 0.0103 |
| 2024_09_20 22:00 | 3245368 | 4 | 91.3440 | 90.8600 | -116.3168 | 11.1023 | 108.2500 | 0.0066 | 0.0017 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412550_B2A1B31D | 504990 | 911 | -85.7 | 504990 | 345 | -95.9 | 504990 | 803 | -102.4 | 504990 | 432 |
| MR_1774412550_10724B0D | 504990 | 911 | -87.8 | 504990 | 345 | -95.0 | 504990 | 803 | -101.6 | 504990 | 432 |
| MR_1774412550_746280E5 | 504990 | 911 | -85.9 | 504990 | 345 | -95.3 | 504990 | 803 | -102.6 | 504990 | 432 |
| MR_1774412550_71A58ABE | 504990 | 911 | -88.2 | 504990 | 345 | -96.4 | 504990 | 803 | -102.7 | 504990 | 432 |
| MR_1774412550_19130EF9 | 504990 | 911 | -86.6 | 504990 | 345 | -96.8 | 504990 | 803 | -102.6 | 504990 | 432 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1887: `f7edba81-030...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f7edba81-030c-4fe8-9ba4-d7927e46962f` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1887] topology](images/train_1887.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228648_3
- `C2`: Decrease A3 Offset threshold for 3262180_4
- `C3`: Press down the tilt angle of 3228648_3 by 8 degrees
- `C4`: Decrease A3 Offset threshold for 3228648_3
- `C5`: Increase transmission power for 3262180_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262180_4
- `C7`: Adjust the azimuth of 3262180_4 by 32 degrees
- `C8`: Add neighbor relationship between 3238255_1 and 3262180_4
- `C9`: Decrease transmission power for 3262180_4
- `C10`: Add neighbor relationship between 3228648_3 and 3262180_4
- `C11`: Decrease transmission power for 3228648_3
- `C12`: Increase transmission power for 3228648_3
- `C13`: Check test server and transmission issues **← 정답**
- `C14`: Increase A3 Offset threshold for 3228648_3
- `C15`: Adjust the azimuth of 3228648_3 by 50 degrees
- `C16`: Press down the tilt angle  of 3262180_4 by 10 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228648_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262180_4
- `C19`: Lift the tilt angle  of 3262180_4 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3262180_4
- `C21`: Lift the tilt angle of 3228648_3 by 8 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.999 | MS1 | 121.4656633957 | 31.1446273570 | 933 | 504990 | -86.78 | 16.25 | 436.37 | 0.05 | 2.16 | 1565 |
| 2024-09-20 22:21:32.107 | MS1 | 121.4656656069 | 31.1446340026 | 933 | 504990 | -85.45 | 16.63 | 452.61 | 0.20 | 2.36 | 1579 |
| 2024-09-20 22:21:33.434 | MS1 | 121.4656661080 | 31.1446180151 | 933 | 504990 | -86.53 | 13.94 | 410.20 | 0.11 | 2.92 | 1568 |
| 2024-09-20 22:21:34.570 | MS1 | 121.4656773798 | 31.1446243469 | 933 | 504990 | -86.29 | 13.22 | 82.67 | 0.12 | 2.51 | 398 |
| 2024-09-20 22:21:35.355 | MS1 | 121.4656678019 | 31.1446293015 | 933 | 504990 | -91.62 | 13.41 | 71.06 | 0.05 | 2.32 | 486 |
| 2024-09-20 22:21:36.422 | MS1 | 121.4656700017 | 31.1446350932 | 933 | 504990 | -91.13 | 12.73 | 71.47 | 0.01 | 2.58 | 345 |
| 2024-09-20 22:21:37.102 | MS1 | 121.4656703152 | 31.1446219352 | 933 | 504990 | -92.67 | 12.57 | 86.97 | 0.16 | 2.21 | 473 |
| 2024-09-20 22:21:38.219 | MS1 | 121.4656639435 | 31.1446359129 | 933 | 504990 | -92.95 | 12.30 | 81.75 | 0.16 | 2.03 | 462 |
| 2024-09-20 22:21:39.503 | MS1 | 121.4656754422 | 31.1446244796 | 933 | 504990 | -90.67 | 7.86 | 69.18 | 0.17 | 2.19 | 340 |
| 2024-09-20 22:21:40.967 | MS1 | 121.4656732559 | 31.1446354531 | 933 | 504990 | -90.05 | 10.31 | 427.97 | 0.02 | 2.53 | 1576 |
| 2024-09-20 22:21:41.182 | MS1 | 121.4656649451 | 31.1446356504 | 933 | 504990 | -89.29 | 8.92 | 476.47 | 0.16 | 2.45 | 1588 |
| 2024-09-20 22:21:42.282 | MS1 | 121.4656662396 | 31.1446348876 | 933 | 504990 | -92.30 | 9.88 | 349.98 | 0.05 | 2.17 | 1563 |

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
| 3228648 | 3 | 121.4755995720 | 31.1555061644 | 270 | 7 | 2 | 24.2 | TDD | 933 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3238255 | 1 | 121.4679658882 | 31.1503650991 | 142 | 9 | 2 | 38.3 | TDD | 864 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3262180 | 4 | 121.4690985280 | 31.1497537024 | 178 | 14 | 3 | 49.3 | TDD | 483 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3278650 | 2 | 121.4664885802 | 31.1462060713 | 89 | 7 | 10 | 15.1 | TDD | 771 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.135 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.160 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.266 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.266 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.002 | NREventA3 | measId:2;ServCellPCI:284;Se... |
| 2024-09-20 22:21:38.242 | NRHandoverAttempt | SourcePCI:284;SourceNR-ARFC... |
| 2024-09-20 22:21:38.286 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.297 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.432 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.432 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238255 | 1 | 16.4237 | 18.7025 | -116.1380 | 16.7202 | 191.1701 | 0.0053 | 0.0164 |
| 2024_09_20 22:00 | 3278650 | 2 | 12.6715 | 15.9387 | -114.6567 | 18.3461 | 143.0058 | 0.0076 | 0.0156 |
| 2024_09_20 22:00 | 3228648 | 3 | 11.2490 | 6.3602 | -117.7161 | 15.4210 | 195.5967 | 0.0023 | 0.0076 |
| 2024_09_20 22:00 | 3262180 | 4 | 8.1177 | 14.3533 | -115.4668 | 5.4366 | 120.1499 | 0.0107 | 0.0128 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415847_27A7A467 | 504990 | 933 | -84.5 | 504990 | 483 | -91.2 | 504990 | 864 | -95.2 | 504990 | 771 |
| MR_1774415847_0F6A6E82 | 504990 | 933 | -85.9 | 504990 | 483 | -91.2 | 504990 | 864 | -96.3 | 504990 | 771 |
| MR_1774415847_2133FFBA | 504990 | 933 | -88.1 | 504990 | 483 | -93.3 | 504990 | 864 | -96.5 | 504990 | 771 |
| MR_1774415847_39B4FA8A | 504990 | 933 | -88.1 | 504990 | 483 | -92.5 | 504990 | 864 | -96.5 | 504990 | 771 |
| MR_1774415847_8501E605 | 504990 | 933 | -87.1 | 504990 | 483 | -92.7 | 504990 | 864 | -96.1 | 504990 | 771 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1888: `0b215664-54a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0b215664-54a6-434a-a522-8ab083e47313` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Decrease A3 Offset threshold for 3252486_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1888] topology](images/train_1888.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3236640_1
- `C2`: Decrease A3 Offset threshold for 3252486_2 **← 정답**
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236640_1
- `C4`: Decrease A3 Offset threshold for 3236640_1
- `C5`: Adjust the azimuth of 3252486_2 by 50 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252486_2
- `C7`: Press down the tilt angle of 3252486_2 by 10 degrees
- `C8`: Press down the tilt angle  of 3236640_1 by 3 degrees
- `C9`: Decrease transmission power for 3252486_2
- `C10`: Lift the tilt angle of 3252486_2 by 10 degrees
- `C11`: Lift the tilt angle  of 3236640_1 by 3 degrees
- `C12`: Increase A3 Offset threshold for 3252486_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236640_1
- `C14`: Add neighbor relationship between 3252486_2 and 3236640_1
- `C15`: Increase transmission power for 3236640_1
- `C16`: Adjust the azimuth of 3236640_1 by 50 degrees
- `C17`: Increase transmission power for 3252486_2
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Increase A3 Offset threshold for 3236640_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252486_2
- `C21`: Check test server and transmission issues
- `C22`: Add neighbor relationship between 3240478_4 and 3236640_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.457 | MS1 | 121.4656703883 | 31.1446339113 | 563 | 504990 | -82.89 | 15.97 | 469.81 | 0.03 | 2.92 | 1581 |
| 2024-09-20 22:21:32.571 | MS1 | 121.4656729580 | 31.1446377288 | 563 | 504990 | -76.55 | 14.63 | 449.52 | 0.13 | 2.59 | 1560 |
| 2024-09-20 22:21:33.436 | MS1 | 121.4656731968 | 31.1446323757 | 563 | 504990 | -76.00 | 13.70 | 345.48 | 0.18 | 2.51 | 1569 |
| 2024-09-20 22:21:34.836 | MS1 | 121.4656777872 | 31.1446285209 | 563 | 504990 | -92.58 | -1.23 | 61.29 | 0.07 | 1.27 | 1587 |
| 2024-09-20 22:21:35.232 | MS1 | 121.4656599428 | 31.1446369951 | 563 | 504990 | -91.89 | -0.32 | 36.10 | 0.06 | 1.44 | 1587 |
| 2024-09-20 22:21:36.386 | MS1 | 121.4656696538 | 31.1446365050 | 563 | 504990 | -88.82 | -3.16 | 54.62 | 0.06 | 1.26 | 1576 |
| 2024-09-20 22:21:37.531 | MS1 | 121.4656589708 | 31.1446288265 | 563 | 504990 | -88.14 | -3.66 | 59.15 | 0.03 | 1.28 | 1576 |
| 2024-09-20 22:21:38.707 | MS1 | 121.4656642234 | 31.1446293683 | 563 | 504990 | -89.18 | -2.52 | 82.60 | 0.04 | 1.35 | 1565 |
| 2024-09-20 22:21:39.288 | MS1 | 121.4656587791 | 31.1446325283 | 640 | 504990 | -78.92 | 12.59 | 184.08 | 0.01 | 1.36 | 1591 |
| 2024-09-20 22:21:40.247 | MS1 | 121.4656653067 | 31.1446220994 | 640 | 504990 | -84.32 | 14.82 | 453.80 | 0.06 | 2.84 | 1599 |
| 2024-09-20 22:21:41.318 | MS1 | 121.4656603117 | 31.1446182464 | 640 | 504990 | -78.39 | 15.93 | 340.87 | 0.05 | 2.38 | 1600 |
| 2024-09-20 22:21:42.908 | MS1 | 121.4656662527 | 31.1446259906 | 640 | 504990 | -79.65 | 13.23 | 597.39 | 0.12 | 2.84 | 1586 |

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
| 3236640 | 1 | 121.4726649487 | 31.1442163986 | 40 | 1 | 6 | 26.0 | TDD | 640 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3240478 | 4 | 121.4641199328 | 31.1468032307 | 242 | 12 | 12 | 39.2 | TDD | 888 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3252266 | 3 | 121.4748757838 | 31.1452270700 | 93 | 5 | 11 | 37.8 | TDD | 668 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3252486 | 2 | 121.4759938422 | 31.1515495764 | 93 | 12 | 4 | 15.2 | TDD | 563 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.371 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.387 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.494 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.494 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.250 | NREventA3 | measId:2;ServCellPCI:605;Se... |
| 2024-09-20 22:21:38.490 | NRHandoverAttempt | SourcePCI:605;SourceNR-ARFC... |
| 2024-09-20 22:21:38.534 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.548 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.678 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.678 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236640 | 1 | 9.2913 | 5.4433 | -117.0906 | 15.7566 | 139.7646 | 0.0119 | 0.0182 |
| 2024_09_20 22:00 | 3252486 | 2 | 7.2703 | 18.4073 | -114.4922 | 15.7824 | 187.1483 | 0.0096 | 0.1038 |
| 2024_09_20 22:00 | 3252266 | 3 | 12.5831 | 18.6893 | -116.4014 | 13.3305 | 131.9007 | 0.0120 | 0.0141 |
| 2024_09_20 22:00 | 3240478 | 4 | 14.4003 | 16.5699 | -115.8758 | 12.9670 | 106.3293 | 0.0172 | 0.0087 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413586_887877CF | 504990 | 640 | -89.1 | 504990 | 563 | -92.6 | 504990 | 888 | -95.7 | 504990 | 668 |
| MR_1774413586_86D1865D | 504990 | 640 | -87.6 | 504990 | 563 | -90.9 | 504990 | 888 | -96.4 | 504990 | 668 |
| MR_1774413586_5695F6EE | 504990 | 640 | -87.4 | 504990 | 563 | -90.9 | 504990 | 888 | -95.8 | 504990 | 668 |
| MR_1774413586_786EF6E4 | 504990 | 563 | -92.8 | 504990 | 640 | -88.0 | 504990 | 888 | -96.2 | 504990 | 668 |
| MR_1774413586_60586354 | 504990 | 563 | -92.2 | 504990 | 640 | -87.8 | 504990 | 888 | -94.8 | 504990 | 668 |
| MR_1774413586_10B46887 | 504990 | 640 | -89.7 | 504990 | 563 | -92.6 | 504990 | 888 | -94.2 | 504990 | 668 |
| MR_1774413586_7D534ED8 | 504990 | 640 | -90.3 | 504990 | 563 | -90.7 | 504990 | 888 | -97.6 | 504990 | 668 |
| MR_1774413586_9D05B40F | 504990 | 563 | -93.7 | 504990 | 640 | -89.0 | 504990 | 888 | -95.1 | 504990 | 668 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1889: `6ee4006d-a33...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6ee4006d-a336-49be-b97d-a59fd813b5ab` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Add neighbor relationship between 3213431_3 and 3220321_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1889] topology](images/train_1889.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3220321_2
- `C2`: Press down the tilt angle  of 3220321_2 by 4 degrees
- `C3`: Check test server and transmission issues
- `C4`: Decrease transmission power for 3220321_2
- `C5`: Increase transmission power for 3213431_3
- `C6`: Add neighbor relationship between 3215747_4 and 3220321_2
- `C7`: Decrease A3 Offset threshold for 3220321_2
- `C8`: Lift the tilt angle  of 3220321_2 by 4 degrees
- `C9`: Increase A3 Offset threshold for 3220321_2
- `C10`: Lift the tilt angle of 3213431_3 by 10 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213431_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213431_3
- `C13`: Add neighbor relationship between 3213431_3 and 3220321_2 **← 정답**
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease A3 Offset threshold for 3213431_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220321_2
- `C17`: Increase A3 Offset threshold for 3213431_3
- `C18`: Decrease transmission power for 3213431_3
- `C19`: Adjust the azimuth of 3220321_2 by 32 degrees
- `C20`: Adjust the azimuth of 3213431_3 by 50 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220321_2
- `C22`: Press down the tilt angle of 3213431_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.958 | MS1 | 121.4656583933 | 31.1446373669 | 823 | 504990 | -84.23 | 13.43 | 475.01 | 0.02 | 2.84 | 1593 |
| 2024-09-20 22:21:32.429 | MS1 | 121.4656729609 | 31.1446352809 | 823 | 504990 | -81.01 | 14.82 | 405.02 | 0.10 | 2.98 | 1589 |
| 2024-09-20 22:21:33.347 | MS1 | 121.4656642105 | 31.1446222781 | 823 | 504990 | -80.75 | 12.90 | 433.41 | 0.16 | 2.03 | 1581 |
| 2024-09-20 22:21:34.140 | MS1 | 121.4656710417 | 31.1446284551 | 823 | 504990 | -88.71 | -3.37 | 71.69 | 0.17 | 1.04 | 1589 |
| 2024-09-20 22:21:35.667 | MS1 | 121.4656590398 | 31.1446254080 | 823 | 504990 | -87.47 | -2.62 | 34.63 | 0.10 | 1.12 | 1589 |
| 2024-09-20 22:21:36.584 | MS1 | 121.4656640133 | 31.1446369755 | 823 | 504990 | -93.36 | -0.20 | 61.50 | 0.12 | 1.06 | 1576 |
| 2024-09-20 22:21:37.257 | MS1 | 121.4656730736 | 31.1446209482 | 823 | 504990 | -91.79 | -0.07 | 60.06 | 0.14 | 1.05 | 1592 |
| 2024-09-20 22:21:38.923 | MS1 | 121.4656686261 | 31.1446293323 | 823 | 504990 | -79.81 | 16.90 | 598.44 | 0.11 | 1.23 | 1591 |
| 2024-09-20 22:21:39.467 | MS1 | 121.4656677618 | 31.1446355692 | 823 | 504990 | -81.58 | 16.74 | 591.13 | 0.14 | 1.41 | 1591 |
| 2024-09-20 22:21:40.167 | MS1 | 121.4656751730 | 31.1446290339 | 823 | 504990 | -78.53 | 12.62 | 441.22 | 0.03 | 2.74 | 1581 |
| 2024-09-20 22:21:41.659 | MS1 | 121.4656666609 | 31.1446364777 | 823 | 504990 | -82.18 | 15.98 | 554.78 | 0.12 | 2.90 | 1586 |
| 2024-09-20 22:21:42.968 | MS1 | 121.4656686108 | 31.1446357797 | 823 | 504990 | -82.57 | 12.81 | 507.39 | 0.07 | 2.03 | 1591 |

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
| 3213431 | 3 | 121.4679225697 | 31.1477942486 | 161 | 5 | 9 | 46.4 | TDD | 823 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3213892 | 1 | 121.4698233681 | 31.1553602760 | 237 | 11 | 4 | 22.6 | TDD | 930 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3215747 | 4 | 121.4650904777 | 31.1455614342 | 188 | 13 | 7 | 34.4 | TDD | 71 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3220321 | 2 | 121.4708387656 | 31.1442851798 | 306 | 2 | 9 | 20.8 | TDD | 603 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.485 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.501 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.608 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.608 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.354 | NREventA3 | measId:2;ServCellPCI:165;Se... |
| 2024-09-20 22:21:36.354 | NREventA3 | measId:2;ServCellPCI:165;Se... |
| 2024-09-20 22:21:37.354 | NREventA3 | measId:2;ServCellPCI:165;Se... |
| 2024-09-20 22:21:39.854 | NRRRCReestablishAttempt | PCI:165 |
| 2024-09-20 22:21:39.866 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.877 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:40.026 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.026 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213892 | 1 | 14.0572 | 5.8545 | -114.3099 | 16.6335 | 179.9466 | 0.0199 | 0.0133 |
| 2024_09_20 22:00 | 3220321 | 2 | 19.9988 | 10.9683 | -116.8440 | 15.8530 | 83.0733 | 0.0184 | 0.0111 |
| 2024_09_20 22:00 | 3213431 | 3 | 8.8296 | 15.3844 | -114.4557 | 10.5579 | 141.4264 | 0.0116 | 0.1035 |
| 2024_09_20 22:00 | 3215747 | 4 | 6.1402 | 14.1494 | -114.3663 | 17.5602 | 188.4130 | 0.0034 | 0.0075 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415318_C9AF7DF3 | 504990 | 823 | -89.7 | 504990 | 603 | -86.1 | 504990 | 71 | -85.3 | 504990 | 930 |
| MR_1774415318_3077E828 | 504990 | 603 | -82.6 | 504990 | 823 | -88.4 | 504990 | 71 | -83.6 | 504990 | 930 |
| MR_1774415318_92EB17BA | 504990 | 603 | -85.0 | 504990 | 823 | -88.2 | 504990 | 71 | -83.6 | 504990 | 930 |
| MR_1774415318_1298DBD5 | 504990 | 823 | -87.7 | 504990 | 603 | -84.1 | 504990 | 71 | -83.1 | 504990 | 930 |
| MR_1774415318_A12F0A2C | 504990 | 603 | -83.1 | 504990 | 823 | -88.9 | 504990 | 71 | -83.0 | 504990 | 930 |
| MR_1774415318_D39287D0 | 504990 | 823 | -89.4 | 504990 | 603 | -82.7 | 504990 | 71 | -85.8 | 504990 | 930 |

> *... 2개 열 생략 (전체 14열)*

---
