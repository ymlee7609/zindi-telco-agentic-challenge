# Track A 문제 분석 — train[950]~train[959]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[950] ~ train[959] (10개)

## 목차

1. [문제 950: `a3f64df0-b5f...`](#950) — multiple-answer, 정답: C2|C10|C13|C20
2. [문제 951: `3578800d-093...`](#951) — multiple-answer, 정답: C10|C14
3. [문제 952: `6d83fb82-45e...`](#952) — single-answer, 정답: C19
4. [문제 953: `13c6f4d8-c34...`](#953) — multiple-answer, 정답: C9|C13
5. [문제 954: `e066ed55-f4c...`](#954) — single-answer, 정답: C3
6. [문제 955: `6f713b24-3a2...`](#955) — single-answer, 정답: C4
7. [문제 956: `9bd9dc4a-953...`](#956) — single-answer, 정답: C13
8. [문제 957: `dd536777-43b...`](#957) — single-answer, 정답: C15
9. [문제 958: `d2bf2681-c1c...`](#958) — single-answer, 정답: C2
10. [문제 959: `a6fb5ee1-728...`](#959) — single-answer, 정답: C3

---

### 문제 950: `a3f64df0-b5f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a3f64df0-b5f0-4c29-bfb3-faf91461a69f` |
| Tag | **multiple-answer** |
| 정답 | **C2|C10|C13|C20** |
| C2 의미 | Decrease transmission power for 3211011_2 |
| C10 의미 | Press down the tilt angle  of 3211011_2 by 4 degrees |
| C13 의미 | Increase A3 Offset threshold for 3249948_5 |
| C20 의미 | Increase A3 Offset threshold for 3211011_2 |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[950] topology](images/train_0950.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249948_5
- `C2`: Decrease transmission power for 3211011_2 **← 정답**
- `C3`: Decrease transmission power for 3249948_5
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Add neighbor relationship between 3279142_3 and 3211011_2
- `C6`: Adjust the azimuth of 3211011_2 by 0 degrees
- `C7`: Decrease A3 Offset threshold for 3211011_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211011_2
- `C9`: Press down the tilt angle of 3249948_5 by 6 degrees
- `C10`: Press down the tilt angle  of 3211011_2 by 4 degrees **← 정답**
- `C11`: Increase transmission power for 3249948_5
- `C12`: Adjust the azimuth of 3249948_5 by 42 degrees
- `C13`: Increase A3 Offset threshold for 3249948_5 **← 정답**
- `C14`: Lift the tilt angle  of 3211011_2 by 4 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211011_2
- `C16`: Lift the tilt angle of 3249948_5 by 6 degrees
- `C17`: Add neighbor relationship between 3249948_5 and 3211011_2
- `C18`: Decrease A3 Offset threshold for 3249948_5
- `C19`: Check test server and transmission issues
- `C20`: Increase A3 Offset threshold for 3211011_2 **← 정답**
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249948_5
- `C22`: Increase transmission power for 3211011_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.499 | MS1 | 121.4656681154 | 31.1446285454 | 443 | 504990 | -82.13 | 14.15 | 522.94 | 0.14 | 2.08 | 1568 |
| 2024-09-20 22:21:32.956 | MS1 | 121.4656772603 | 31.1446355854 | 443 | 504990 | -82.96 | 12.42 | 552.64 | 0.16 | 2.59 | 1571 |
| 2024-09-20 22:21:33.501 | MS1 | 121.4656585898 | 31.1446197990 | 443 | 504990 | -77.39 | 16.81 | 504.84 | 0.01 | 2.88 | 1568 |
| 2024-09-20 22:21:34.580 | MS1 | 121.4656759381 | 31.1446235794 | 817 | 504990 | -82.75 | 2.25 | 27.19 | 0.08 | 1.20 | 1564 |
| 2024-09-20 22:21:35.344 | MS1 | 121.4656585192 | 31.1446308873 | 817 | 504990 | -84.66 | 3.84 | 48.73 | 0.17 | 1.19 | 1564 |
| 2024-09-20 22:21:36.177 | MS1 | 121.4656677333 | 31.1446303060 | 443 | 504990 | -84.46 | 1.88 | 64.49 | 0.11 | 1.18 | 1599 |
| 2024-09-20 22:21:37.181 | MS1 | 121.4656718280 | 31.1446324913 | 443 | 504990 | -81.98 | 2.49 | 59.62 | 0.07 | 1.46 | 1598 |
| 2024-09-20 22:21:38.943 | MS1 | 121.4656747234 | 31.1446341440 | 817 | 504990 | -84.52 | 3.83 | 65.28 | 0.08 | 1.09 | 1584 |
| 2024-09-20 22:21:39.152 | MS1 | 121.4656589702 | 31.1446325416 | 817 | 504990 | -85.77 | 4.70 | 64.18 | 0.16 | 1.12 | 1562 |
| 2024-09-20 22:21:40.776 | MS1 | 121.4656743149 | 31.1446353237 | 817 | 504990 | -78.75 | 17.73 | 541.05 | 0.16 | 2.71 | 1600 |
| 2024-09-20 22:21:41.553 | MS1 | 121.4656704451 | 31.1446257109 | 817 | 504990 | -79.81 | 12.45 | 517.12 | 0.14 | 2.43 | 1581 |
| 2024-09-20 22:21:42.800 | MS1 | 121.4656778705 | 31.1446284765 | 817 | 504990 | -83.35 | 13.32 | 301.73 | 0.05 | 2.19 | 1579 |

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
| 3211011 | 2 | 121.4712969666 | 31.1477379255 | 237 | 0 | 12 | 43.0 | TDD | 808 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3224906 | 4 | 121.4750026616 | 31.1527586405 | 233 | 5 | 7 | 37.1 | TDD | 817 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3245130 | 1 | 121.4663478817 | 31.1488245752 | 237 | 12 | 12 | 48.0 | TDD | 550 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3249948 | 5 | 121.4725655990 | 31.1447161037 | 311 | 4 | 0 | 19.7 | TDD | 443 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3279142 | 3 | 121.4694472907 | 31.1520538695 | 255 | 5 | 9 | 33.0 | TDD | 522 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.103 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.122 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.252 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.252 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.911 | NREventA3 | measId:2;ServCellPCI:86;Ser... |
| 2024-09-20 22:21:34.151 | NRHandoverAttempt | SourcePCI:86;SourceNR-ARFCN... |
| 2024-09-20 22:21:34.188 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.201 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:34.329 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.329 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.911 | NREventA3 | measId:2;ServCellPCI:561;Se... |
| 2024-09-20 22:21:36.151 | NRHandoverAttempt | SourcePCI:561;SourceNR-ARFC... |
| 2024-09-20 22:21:36.199 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.214 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.348 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.348 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.911 | NREventA3 | measId:2;ServCellPCI:86;Ser... |
| 2024-09-20 22:21:38.151 | NRHandoverAttempt | SourcePCI:86;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.192 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.205 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.317 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.317 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245130 | 1 | 7.6083 | 12.1332 | -114.1461 | 16.5234 | 138.5187 | 0.0156 | 0.0157 |
| 2024_09_20 22:00 | 3211011 | 2 | 18.7139 | 16.7529 | -117.1942 | 6.8312 | 158.2052 | 0.0163 | 0.0056 |
| 2024_09_20 22:00 | 3279142 | 3 | 13.0404 | 18.7061 | -116.4421 | 15.6999 | 166.1786 | 0.0090 | 0.0143 |
| 2024_09_20 22:00 | 3224906 | 4 | 19.2117 | 15.6049 | -115.3840 | 6.0127 | 155.6205 | 0.0177 | 0.0028 |
| 2024_09_20 22:00 | 3249948 | 5 | 14.1640 | 10.6605 | -114.2126 | 15.4724 | 122.5817 | 0.0067 | 0.0175 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416397_7ACDADCC | 504990 | 817 | -82.9 | 504990 | 443 | -79.2 | 504990 | 808 | -80.9 | 504990 | 522 |
| MR_1774416397_B1A1F128 | 504990 | 817 | -83.4 | 504990 | 443 | -80.0 | 504990 | 808 | -82.1 | 504990 | 522 |
| MR_1774416397_FB846B97 | 504990 | 443 | -84.2 | 504990 | 817 | -77.5 | 504990 | 808 | -82.6 | 504990 | 522 |
| MR_1774416397_4B6060BE | 504990 | 443 | -83.6 | 504990 | 817 | -79.4 | 504990 | 808 | -79.7 | 504990 | 522 |
| MR_1774416397_C6C73FB7 | 504990 | 443 | -84.1 | 504990 | 817 | -80.4 | 504990 | 808 | -79.5 | 504990 | 522 |
| MR_1774416397_9A952A00 | 504990 | 443 | -83.1 | 504990 | 817 | -77.1 | 504990 | 808 | -79.3 | 504990 | 522 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 951: `3578800d-093...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3578800d-0937-4b15-9dac-8577424e98d3` |
| Tag | **multiple-answer** |
| 정답 | **C10|C14** |
| C10 의미 | Press down the tilt angle  of 3244576_3 by 5 degrees |
| C14 의미 | Decrease transmission power for 3244576_3 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[951] topology](images/train_0951.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3263500_1 and 3244576_3
- `C2`: Increase A3 Offset threshold for 3214247_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244576_3
- `C4`: Decrease A3 Offset threshold for 3244576_3
- `C5`: Increase transmission power for 3244576_3
- `C6`: Adjust the azimuth of 3244576_3 by 6 degrees
- `C7`: Lift the tilt angle  of 3244576_3 by 5 degrees
- `C8`: Adjust the azimuth of 3214247_2 by 33 degrees
- `C9`: Increase A3 Offset threshold for 3244576_3
- `C10`: Press down the tilt angle  of 3244576_3 by 5 degrees **← 정답**
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214247_2
- `C12`: Increase transmission power for 3214247_2
- `C13`: Add neighbor relationship between 3214247_2 and 3244576_3
- `C14`: Decrease transmission power for 3244576_3 **← 정답**
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214247_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244576_3
- `C17`: Decrease transmission power for 3214247_2
- `C18`: Decrease A3 Offset threshold for 3214247_2
- `C19`: Press down the tilt angle of 3214247_2 by 6 degrees
- `C20`: Check test server and transmission issues
- `C21`: Lift the tilt angle of 3214247_2 by 6 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.832 | MS1 | 121.4656733370 | 31.1446216359 | 651 | 504990 | -81.39 | 12.08 | 519.26 | 0.17 | 2.74 | 1584 |
| 2024-09-20 22:21:32.688 | MS1 | 121.4656720588 | 31.1446239543 | 651 | 504990 | -82.00 | 15.97 | 568.06 | 0.18 | 2.57 | 1563 |
| 2024-09-20 22:21:33.101 | MS1 | 121.4656604980 | 31.1446370111 | 651 | 504990 | -76.49 | 16.20 | 437.18 | 0.05 | 2.43 | 1598 |
| 2024-09-20 22:21:34.558 | MS1 | 121.4656765340 | 31.1446366125 | 651 | 504990 | -87.09 | 0.53 | 76.53 | 0.14 | 1.21 | 1563 |
| 2024-09-20 22:21:35.587 | MS1 | 121.4656775061 | 31.1446250813 | 651 | 504990 | -88.35 | 0.25 | 36.84 | 0.14 | 1.05 | 1590 |
| 2024-09-20 22:21:36.690 | MS1 | 121.4656656235 | 31.1446286458 | 651 | 504990 | -91.61 | 0.94 | 47.00 | 0.17 | 1.42 | 1574 |
| 2024-09-20 22:21:37.821 | MS1 | 121.4656695086 | 31.1446284279 | 651 | 504990 | -87.68 | 1.76 | 72.47 | 0.19 | 1.08 | 1571 |
| 2024-09-20 22:21:38.178 | MS1 | 121.4656652173 | 31.1446213900 | 651 | 504990 | -94.52 | 2.38 | 51.20 | 0.19 | 1.11 | 1586 |
| 2024-09-20 22:21:39.690 | MS1 | 121.4656629635 | 31.1446217846 | 651 | 504990 | -89.70 | 1.04 | 40.15 | 0.12 | 1.35 | 1560 |
| 2024-09-20 22:21:40.944 | MS1 | 121.4656607446 | 31.1446267011 | 651 | 504990 | -79.19 | 14.81 | 457.35 | 0.14 | 2.27 | 1589 |
| 2024-09-20 22:21:41.918 | MS1 | 121.4656706262 | 31.1446185858 | 651 | 504990 | -83.53 | 14.39 | 408.48 | 0.11 | 2.59 | 1579 |
| 2024-09-20 22:21:42.708 | MS1 | 121.4656598354 | 31.1446248238 | 651 | 504990 | -81.23 | 14.09 | 476.84 | 0.15 | 2.20 | 1581 |

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
| 3214247 | 2 | 121.4737419750 | 31.1517916508 | 191 | 3 | 11 | 49.6 | TDD | 651 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3223699 | 4 | 121.4694414566 | 31.1509953032 | 42 | 3 | 4 | 30.8 | TDD | 377 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3244576 | 3 | 121.4647168648 | 31.1495511237 | 165 | 3 | 10 | 17.7 | TDD | 782 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3263500 | 1 | 121.4688091775 | 31.1534960289 | 215 | 15 | 4 | 26.7 | TDD | 457 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.635 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.650 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.797 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.797 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263500 | 1 | 13.5776 | 5.7966 | -114.5993 | 8.8223 | 182.1704 | 0.0156 | 0.0058 |
| 2024_09_20 22:00 | 3214247 | 2 | 8.5392 | 17.8835 | -108.1118 | 18.9852 | 157.2976 | 0.0100 | 0.0022 |
| 2024_09_20 22:00 | 3244576 | 3 | 11.2032 | 9.6687 | -114.6835 | 9.8155 | 169.9810 | 0.0187 | 0.0074 |
| 2024_09_20 22:00 | 3223699 | 4 | 10.5084 | 7.6310 | -114.3392 | 16.2421 | 119.0192 | 0.0185 | 0.0012 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415272_99A4C256 | 504990 | 651 | -87.8 | 504990 | 782 | -82.7 | 504990 | 457 | -88.2 | 504990 | 377 |
| MR_1774415272_86480DE0 | 504990 | 651 | -86.7 | 504990 | 782 | -84.5 | 504990 | 457 | -86.9 | 504990 | 377 |
| MR_1774415272_5A8B9DB7 | 504990 | 651 | -87.7 | 504990 | 782 | -84.6 | 504990 | 457 | -87.2 | 504990 | 377 |
| MR_1774415272_75839AE6 | 504990 | 651 | -86.9 | 504990 | 782 | -84.2 | 504990 | 457 | -87.7 | 504990 | 377 |
| MR_1774415272_CB64CC2D | 504990 | 651 | -86.3 | 504990 | 782 | -84.9 | 504990 | 457 | -86.1 | 504990 | 377 |
| MR_1774415272_9EACB8E5 | 504990 | 782 | -86.5 | 504990 | 651 | -85.8 | 504990 | 457 | -87.9 | 504990 | 377 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 952: `6d83fb82-45e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6d83fb82-45ea-4503-be3c-1c64feeb26ba` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Lift the tilt angle  of 3265810_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[952] topology](images/train_0952.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3259506_3
- `C2`: Check test server and transmission issues
- `C3`: Adjust the azimuth of 3265810_2 by 49 degrees
- `C4`: Press down the tilt angle  of 3265810_2 by 10 degrees
- `C5`: Increase A3 Offset threshold for 3210777_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259506_3
- `C7`: Adjust the azimuth of 3210777_1 by 37 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease transmission power for 3210777_1
- `C10`: Add neighbor relationship between 3265810_2 and 3259506_3
- `C11`: Press down the tilt angle of 3210777_1 by 6 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210777_1
- `C13`: Increase transmission power for 3210777_1
- `C14`: Add neighbor relationship between 3210777_1 and 3259506_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210777_1
- `C16`: Lift the tilt angle of 3210777_1 by 6 degrees
- `C17`: Decrease A3 Offset threshold for 3210777_1
- `C18`: Increase A3 Offset threshold for 3259506_3
- `C19`: Lift the tilt angle  of 3265810_2 by 10 degrees **← 정답**
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259506_3
- `C21`: Decrease transmission power for 3259506_3
- `C22`: Increase transmission power for 3259506_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.435 | MS1 | 121.4656723927 | 31.1446238872 | 9 | 504990 | -90.95 | 16.06 | 471.82 | 0.03 | 2.76 | 1600 |
| 2024-09-20 22:21:32.729 | MS1 | 121.4656756504 | 31.1446271693 | 9 | 504990 | -86.68 | 14.61 | 516.57 | 0.03 | 2.88 | 1580 |
| 2024-09-20 22:21:33.415 | MS1 | 121.4656650160 | 31.1446268817 | 9 | 504990 | -89.60 | 17.59 | 445.55 | 0.06 | 2.53 | 1563 |
| 2024-09-20 22:21:34.928 | MS1 | 121.4656694754 | 31.1446244651 | 9 | 504990 | -91.98 | 12.87 | 66.03 | 0.05 | 2.43 | 1598 |
| 2024-09-20 22:21:35.704 | MS1 | 121.4656713456 | 31.1446207478 | 9 | 504990 | -88.63 | 12.10 | 61.40 | 0.16 | 2.25 | 1570 |
| 2024-09-20 22:21:36.935 | MS1 | 121.4656765701 | 31.1446371013 | 9 | 504990 | -90.52 | 14.76 | 69.83 | 0.04 | 2.68 | 1581 |
| 2024-09-20 22:21:37.184 | MS1 | 121.4656647932 | 31.1446363562 | 9 | 504990 | -92.47 | 9.32 | 84.15 | 0.02 | 2.38 | 1591 |
| 2024-09-20 22:21:38.346 | MS1 | 121.4656700070 | 31.1446288377 | 9 | 504990 | -91.90 | 12.20 | 78.77 | 0.06 | 2.91 | 1586 |
| 2024-09-20 22:21:39.562 | MS1 | 121.4656652548 | 31.1446258487 | 9 | 504990 | -93.71 | 10.29 | 59.23 | 0.03 | 2.39 | 1584 |
| 2024-09-20 22:21:40.458 | MS1 | 121.4656635371 | 31.1446260112 | 9 | 504990 | -93.60 | 10.58 | 426.07 | 0.09 | 2.60 | 1568 |
| 2024-09-20 22:21:41.767 | MS1 | 121.4656666109 | 31.1446223621 | 9 | 504990 | -91.74 | 11.89 | 384.24 | 0.11 | 2.53 | 1589 |
| 2024-09-20 22:21:42.629 | MS1 | 121.4656733213 | 31.1446298352 | 9 | 504990 | -90.45 | 11.75 | 511.86 | 0.09 | 2.22 | 1569 |

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
| 3210777 | 1 | 121.4727879147 | 31.1477609660 | 280 | 3 | 10 | 33.4 | TDD | 9 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3258852 | 4 | 121.4722731580 | 31.1528847403 | 107 | 0 | 12 | 16.1 | TDD | 437 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3259506 | 3 | 121.4729028497 | 31.1519729316 | 269 | 12 | 10 | 37.4 | TDD | 707 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3265810 | 2 | 121.4696101639 | 31.1456385572 | 54 | 1 | 5 | 46.0 | TDD | 266 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.493 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.508 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.614 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.614 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.369 | NREventA3 | measId:2;ServCellPCI:430;Se... |
| 2024-09-20 22:21:38.609 | NRHandoverAttempt | SourcePCI:430;SourceNR-ARFC... |
| 2024-09-20 22:21:38.659 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.673 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.794 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.794 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210777 | 1 | 81.5999 | 86.6150 | -116.7144 | 7.9416 | 199.1820 | 0.0076 | 0.0113 |
| 2024_09_20 22:00 | 3265810 | 2 | 19.7262 | 12.0636 | -116.8152 | 17.5110 | 90.2135 | 0.0170 | 0.0007 |
| 2024_09_20 22:00 | 3259506 | 3 | 9.3000 | 17.7990 | -114.2996 | 8.1518 | 178.1759 | 0.0190 | 0.0135 |
| 2024_09_20 22:00 | 3258852 | 4 | 17.9317 | 15.7098 | -115.2588 | 15.2375 | 163.4206 | 0.0188 | 0.0158 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416969_F7C5DED8 | 504990 | 9 | -91.5 | 504990 | 707 | -93.9 | 504990 | 266 | -106.5 | 504990 | 437 |
| MR_1774416969_B67F5133 | 504990 | 9 | -90.4 | 504990 | 707 | -92.4 | 504990 | 266 | -105.2 | 504990 | 437 |
| MR_1774416969_A4D92C29 | 504990 | 9 | -90.2 | 504990 | 707 | -94.3 | 504990 | 266 | -104.9 | 504990 | 437 |
| MR_1774416969_D94E138F | 504990 | 9 | -92.6 | 504990 | 707 | -94.7 | 504990 | 266 | -104.7 | 504990 | 437 |
| MR_1774416969_6B720768 | 504990 | 9 | -93.1 | 504990 | 707 | -93.1 | 504990 | 266 | -104.2 | 504990 | 437 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 953: `13c6f4d8-c34...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `13c6f4d8-c34f-4a99-89b6-b781e05f8246` |
| Tag | **multiple-answer** |
| 정답 | **C9|C13** |
| C9 의미 | Press down the tilt angle  of 3228865_1 by 4 degrees |
| C13 의미 | Decrease transmission power for 3228865_1 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[953] topology](images/train_0953.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3228865_1 by 1 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231982_3
- `C3`: Decrease A3 Offset threshold for 3228865_1
- `C4`: Check test server and transmission issues
- `C5`: Press down the tilt angle of 3231982_3 by 6 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228865_1
- `C7`: Add neighbor relationship between 3243979_2 and 3228865_1
- `C8`: Lift the tilt angle  of 3228865_1 by 4 degrees
- `C9`: Press down the tilt angle  of 3228865_1 by 4 degrees **← 정답**
- `C10`: Increase A3 Offset threshold for 3228865_1
- `C11`: Increase transmission power for 3228865_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228865_1
- `C13`: Decrease transmission power for 3228865_1 **← 정답**
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Add neighbor relationship between 3231982_3 and 3228865_1
- `C16`: Decrease A3 Offset threshold for 3231982_3
- `C17`: Adjust the azimuth of 3231982_3 by 48 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231982_3
- `C19`: Decrease transmission power for 3231982_3
- `C20`: Increase transmission power for 3231982_3
- `C21`: Lift the tilt angle of 3231982_3 by 6 degrees
- `C22`: Increase A3 Offset threshold for 3231982_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.996 | MS1 | 121.4656724855 | 31.1446238007 | 114 | 504990 | -83.35 | 16.15 | 497.77 | 0.12 | 2.28 | 1571 |
| 2024-09-20 22:21:32.955 | MS1 | 121.4656709281 | 31.1446182098 | 114 | 504990 | -83.50 | 15.95 | 469.31 | 0.03 | 2.63 | 1597 |
| 2024-09-20 22:21:33.296 | MS1 | 121.4656645365 | 31.1446342229 | 114 | 504990 | -75.32 | 12.47 | 316.66 | 0.11 | 2.81 | 1577 |
| 2024-09-20 22:21:34.936 | MS1 | 121.4656699983 | 31.1446241208 | 114 | 504990 | -93.87 | 2.74 | 33.86 | 0.10 | 1.47 | 1560 |
| 2024-09-20 22:21:35.638 | MS1 | 121.4656712103 | 31.1446318478 | 114 | 504990 | -87.15 | 0.33 | 72.48 | 0.16 | 1.01 | 1582 |
| 2024-09-20 22:21:36.919 | MS1 | 121.4656669139 | 31.1446279511 | 114 | 504990 | -91.10 | 3.65 | 74.50 | 0.12 | 1.50 | 1571 |
| 2024-09-20 22:21:37.244 | MS1 | 121.4656763696 | 31.1446375883 | 114 | 504990 | -90.81 | 0.03 | 57.74 | 0.11 | 1.26 | 1585 |
| 2024-09-20 22:21:38.217 | MS1 | 121.4656704447 | 31.1446283605 | 114 | 504990 | -85.23 | 3.62 | 87.56 | 0.20 | 1.37 | 1566 |
| 2024-09-20 22:21:39.565 | MS1 | 121.4656694173 | 31.1446286733 | 114 | 504990 | -94.58 | 1.43 | 71.70 | 0.01 | 1.35 | 1582 |
| 2024-09-20 22:21:40.447 | MS1 | 121.4656682138 | 31.1446337398 | 114 | 504990 | -84.85 | 14.98 | 364.35 | 0.05 | 2.53 | 1581 |
| 2024-09-20 22:21:41.491 | MS1 | 121.4656610342 | 31.1446348234 | 114 | 504990 | -79.29 | 16.85 | 557.68 | 0.15 | 2.21 | 1573 |
| 2024-09-20 22:21:42.255 | MS1 | 121.4656743943 | 31.1446321022 | 114 | 504990 | -80.27 | 16.02 | 401.82 | 0.19 | 2.89 | 1568 |

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
| 3228865 | 1 | 121.4714007834 | 31.1509769342 | 219 | 2 | 7 | 27.1 | TDD | 984 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3231982 | 3 | 121.4724147402 | 31.1529573224 | 167 | 4 | 0 | 38.9 | TDD | 114 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3243979 | 2 | 121.4740624270 | 31.1520667924 | 22 | 12 | 3 | 30.0 | TDD | 569 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3268196 | 4 | 121.4743888247 | 31.1469322069 | 9 | 4 | 2 | 39.7 | TDD | 415 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.006 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.027 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.134 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.134 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228865 | 1 | 10.4598 | 7.5938 | -114.8039 | 11.7615 | 157.9283 | 0.0075 | 0.0135 |
| 2024_09_20 22:00 | 3243979 | 2 | 11.3677 | 5.7758 | -115.4595 | 10.2447 | 116.8442 | 0.0010 | 0.0056 |
| 2024_09_20 22:00 | 3231982 | 3 | 18.8492 | 12.7466 | -109.4611 | 16.8709 | 180.0489 | 0.0105 | 0.0199 |
| 2024_09_20 22:00 | 3268196 | 4 | 12.5778 | 9.7093 | -117.4106 | 11.6775 | 121.9963 | 0.0138 | 0.0021 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413394_E4805690 | 504990 | 114 | -92.0 | 504990 | 984 | -90.9 | 504990 | 569 | -92.8 | 504990 | 415 |
| MR_1774413394_BB22D390 | 504990 | 114 | -93.8 | 504990 | 984 | -90.3 | 504990 | 569 | -95.3 | 504990 | 415 |
| MR_1774413394_47691815 | 504990 | 114 | -93.1 | 504990 | 984 | -90.4 | 504990 | 569 | -92.1 | 504990 | 415 |
| MR_1774413394_31891DB1 | 504990 | 114 | -92.3 | 504990 | 984 | -93.4 | 504990 | 569 | -94.1 | 504990 | 415 |
| MR_1774413394_C01E15AF | 504990 | 114 | -95.5 | 504990 | 984 | -93.7 | 504990 | 569 | -95.3 | 504990 | 415 |
| MR_1774413394_85A5BFC6 | 504990 | 114 | -93.5 | 504990 | 984 | -92.2 | 504990 | 569 | -95.9 | 504990 | 415 |
| MR_1774413394_9D737C78 | 504990 | 984 | -95.4 | 504990 | 114 | -94.0 | 504990 | 569 | -92.5 | 504990 | 415 |
| MR_1774413394_14653208 | 504990 | 114 | -93.1 | 504990 | 984 | -92.3 | 504990 | 569 | -93.8 | 504990 | 415 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 954: `e066ed55-f4c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e066ed55-f4cc-4898-b7f8-913f5ce75c5f` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Lift the tilt angle  of 3250366_1 by 6 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[954] topology](images/train_0954.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3267223_3 by 4 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231505_2
- `C3`: Lift the tilt angle  of 3250366_1 by 6 degrees **← 정답**
- `C4`: Adjust the azimuth of 3250366_1 by 7 degrees
- `C5`: Lift the tilt angle of 3267223_3 by 4 degrees
- `C6`: Decrease transmission power for 3231505_2
- `C7`: Add neighbor relationship between 3267223_3 and 3231505_2
- `C8`: Add neighbor relationship between 3250366_1 and 3231505_2
- `C9`: Check test server and transmission issues
- `C10`: Increase transmission power for 3231505_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231505_2
- `C12`: Press down the tilt angle  of 3250366_1 by 6 degrees
- `C13`: Decrease A3 Offset threshold for 3267223_3
- `C14`: Decrease A3 Offset threshold for 3231505_2
- `C15`: Increase A3 Offset threshold for 3231505_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267223_3
- `C17`: Decrease transmission power for 3267223_3
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267223_3
- `C20`: Increase A3 Offset threshold for 3267223_3
- `C21`: Increase transmission power for 3267223_3
- `C22`: Adjust the azimuth of 3267223_3 by 22 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.497 | MS1 | 121.4656733541 | 31.1446296909 | 755 | 504990 | -86.32 | 15.24 | 402.13 | 0.03 | 2.80 | 1589 |
| 2024-09-20 22:21:32.387 | MS1 | 121.4656707501 | 31.1446248028 | 755 | 504990 | -90.69 | 14.87 | 339.86 | 0.05 | 2.92 | 1577 |
| 2024-09-20 22:21:33.212 | MS1 | 121.4656713709 | 31.1446194939 | 755 | 504990 | -88.54 | 17.50 | 402.94 | 0.18 | 2.15 | 1566 |
| 2024-09-20 22:21:34.124 | MS1 | 121.4656598681 | 31.1446364626 | 755 | 504990 | -90.52 | 13.85 | 86.24 | 0.16 | 2.85 | 1561 |
| 2024-09-20 22:21:35.755 | MS1 | 121.4656705371 | 31.1446346823 | 755 | 504990 | -86.52 | 16.25 | 98.16 | 0.05 | 2.83 | 1598 |
| 2024-09-20 22:21:36.931 | MS1 | 121.4656719763 | 31.1446292939 | 755 | 504990 | -86.37 | 13.50 | 86.12 | 0.08 | 2.08 | 1565 |
| 2024-09-20 22:21:37.699 | MS1 | 121.4656644028 | 31.1446333893 | 755 | 504990 | -92.14 | 9.87 | 81.70 | 0.07 | 2.21 | 1574 |
| 2024-09-20 22:21:38.839 | MS1 | 121.4656675033 | 31.1446223434 | 755 | 504990 | -90.36 | 11.05 | 50.97 | 0.16 | 2.79 | 1569 |
| 2024-09-20 22:21:39.635 | MS1 | 121.4656665350 | 31.1446326399 | 755 | 504990 | -89.21 | 7.99 | 97.85 | 0.18 | 2.99 | 1590 |
| 2024-09-20 22:21:40.642 | MS1 | 121.4656643281 | 31.1446221944 | 755 | 504990 | -92.72 | 11.15 | 313.28 | 0.02 | 2.31 | 1590 |
| 2024-09-20 22:21:41.164 | MS1 | 121.4656716647 | 31.1446364341 | 755 | 504990 | -92.13 | 7.18 | 404.48 | 0.01 | 3.00 | 1571 |
| 2024-09-20 22:21:42.272 | MS1 | 121.4656606615 | 31.1446343211 | 755 | 504990 | -91.51 | 8.82 | 454.87 | 0.15 | 2.52 | 1567 |

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
| 3231505 | 2 | 121.4642531857 | 31.1553010710 | 181 | 4 | 10 | 49.8 | TDD | 614 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3250366 | 1 | 121.4644931180 | 31.1540632553 | 19 | 1 | 6 | 25.0 | TDD | 361 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3256114 | 4 | 121.4715024809 | 31.1523130248 | 355 | 3 | 11 | 32.0 | TDD | 150 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3267223 | 3 | 121.4724498875 | 31.1518405658 | 241 | 2 | 3 | 41.5 | TDD | 755 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.285 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.302 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.405 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.405 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.152 | NREventA3 | measId:2;ServCellPCI:365;Se... |
| 2024-09-20 22:21:38.392 | NRHandoverAttempt | SourcePCI:365;SourceNR-ARFC... |
| 2024-09-20 22:21:38.437 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.452 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.572 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.572 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250366 | 1 | 15.5887 | 18.6966 | -116.7622 | 5.5650 | 126.6191 | 0.0177 | 0.0179 |
| 2024_09_20 22:00 | 3231505 | 2 | 6.4963 | 17.2009 | -116.3708 | 9.1886 | 148.3200 | 0.0187 | 0.0017 |
| 2024_09_20 22:00 | 3267223 | 3 | 82.7339 | 92.4904 | -117.5774 | 13.1301 | 129.2303 | 0.0067 | 0.0045 |
| 2024_09_20 22:00 | 3256114 | 4 | 18.8490 | 17.3495 | -116.4374 | 7.3527 | 103.1410 | 0.0129 | 0.0073 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415452_E067E4C8 | 504990 | 755 | -88.6 | 504990 | 614 | -99.2 | 504990 | 361 | -102.4 | 504990 | 150 |
| MR_1774415452_E90E411F | 504990 | 755 | -92.0 | 504990 | 614 | -100.8 | 504990 | 361 | -103.8 | 504990 | 150 |
| MR_1774415452_9126F6A8 | 504990 | 755 | -88.9 | 504990 | 614 | -99.5 | 504990 | 361 | -102.0 | 504990 | 150 |
| MR_1774415452_DB0B8E1A | 504990 | 755 | -91.5 | 504990 | 614 | -98.5 | 504990 | 361 | -104.5 | 504990 | 150 |
| MR_1774415452_6C8B6384 | 504990 | 755 | -89.0 | 504990 | 614 | -102.2 | 504990 | 361 | -102.4 | 504990 | 150 |
| MR_1774415452_03702EEF | 504990 | 755 | -92.3 | 504990 | 614 | -101.8 | 504990 | 361 | -102.4 | 504990 | 150 |
| MR_1774415452_BEC5D517 | 504990 | 755 | -90.2 | 504990 | 614 | -102.0 | 504990 | 361 | -104.3 | 504990 | 150 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 955: `6f713b24-3a2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6f713b24-3a2b-4769-b0e9-229b7b58e48d` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242670_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[955] topology](images/train_0955.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3242670_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264143_1
- `C3`: Lift the tilt angle of 3242670_3 by 5 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242670_3 **← 정답**
- `C5`: Check test server and transmission issues
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242670_3
- `C7`: Adjust the azimuth of 3242670_3 by 14 degrees
- `C8`: Add neighbor relationship between 3247492_7 and 3264143_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264143_1
- `C10`: Adjust the azimuth of 3264143_1 by 21 degrees
- `C11`: Increase transmission power for 3242670_3
- `C12`: Increase A3 Offset threshold for 3264143_1
- `C13`: Decrease A3 Offset threshold for 3242670_3
- `C14`: Increase transmission power for 3264143_1
- `C15`: Lift the tilt angle  of 3264143_1 by 1 degrees
- `C16`: Decrease transmission power for 3264143_1
- `C17`: Add neighbor relationship between 3242670_3 and 3264143_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Press down the tilt angle  of 3264143_1 by 1 degrees
- `C20`: Press down the tilt angle of 3242670_3 by 5 degrees
- `C21`: Decrease transmission power for 3242670_3
- `C22`: Decrease A3 Offset threshold for 3264143_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.685 | MS1 | 121.4656721662 | 31.1446206691 | 298 | 504990 | -95.60 | 13.15 | 367.91 | 0.02 | 2.27 | 1593 |
| 2024-09-20 22:21:32.532 | MS1 | 121.4656686136 | 31.1446267226 | 112 | 504990 | -95.87 | 9.40 | 523.89 | 0.20 | 2.36 | 1592 |
| 2024-09-20 22:21:33.315 | MS1 | 121.4656774108 | 31.1446348667 | 560 | 504990 | -95.90 | 9.77 | 452.31 | 0.09 | 2.58 | 1570 |
| 2024-09-20 22:21:34.991 | MS1 | 121.4656712682 | 31.1446236069 | 116 | 152650 | -90.53 | 4.71 | 83.23 | 0.19 | 1.56 | 982 |
| 2024-09-20 22:21:35.224 | MS1 | 121.4656599500 | 31.1446219920 | 303 | 152650 | -95.69 | 7.32 | 62.52 | 0.15 | 1.67 | 974 |
| 2024-09-20 22:21:36.422 | MS1 | 121.4656615743 | 31.1446319909 | 228 | 152650 | -93.13 | 5.73 | 101.43 | 0.05 | 1.84 | 987 |
| 2024-09-20 22:21:37.728 | MS1 | 121.4656601574 | 31.1446195347 | 950 | 152650 | -91.10 | 5.44 | 78.00 | 0.06 | 1.90 | 987 |
| 2024-09-20 22:21:38.655 | MS1 | 121.4656614312 | 31.1446204986 | 116 | 152650 | -91.20 | 3.69 | 55.09 | 0.05 | 1.88 | 968 |
| 2024-09-20 22:21:39.667 | MS1 | 121.4656728070 | 31.1446184700 | 303 | 152650 | -87.52 | 2.48 | 51.22 | 0.17 | 1.92 | 982 |
| 2024-09-20 22:21:40.111 | MS1 | 121.4656764079 | 31.1446316740 | 228 | 152650 | -95.16 | 2.24 | 43.88 | 0.12 | 2.44 | 1586 |
| 2024-09-20 22:21:41.209 | MS1 | 121.4656771986 | 31.1446236047 | 950 | 152650 | -88.35 | 6.61 | 82.09 | 0.04 | 2.07 | 1577 |
| 2024-09-20 22:21:42.552 | MS1 | 121.4656720691 | 31.1446346454 | 116 | 152650 | -92.24 | 2.77 | 87.34 | 0.05 | 2.67 | 1584 |

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
| 3217649 | 8 | 121.4743007371 | 31.1455930488 | 299 | 15 | 7 | 9.1 | FDD | 779 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3223140 | 9 | 121.4745367110 | 31.1492152377 | 46 | 11 | 12 | 12.4 | FDD | 303 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3237405 | 2 | 121.4698386983 | 31.1503192244 | 95 | 14 | 11 | 25.0 | TDD | 40 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3242670 | 3 | 121.4722220741 | 31.1556319761 | 221 | 4 | 3 | 19.7 | TDD | 298 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3247492 | 7 | 121.4713101525 | 31.1518991891 | 235 | 6 | 0 | 9.5 | FDD | 228 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3248672 | 5 | 121.4747730064 | 31.1485451315 | 103 | 3 | 9 | 6.1 | TDD | 592 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3248940 | 12 | 121.4706669005 | 31.1509981276 | 197 | 6 | 10 | 18.2 | FDD | 950 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3253296 | 11 | 121.4721105620 | 31.1518723429 | 86 | 3 | 11 | 17.9 | FDD | 116 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3254676 | 10 | 121.4682869568 | 31.1440200536 | 121 | 11 | 4 | 25.7 | FDD | 17 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3259652 | 4 | 121.4662763486 | 31.1477045065 | 40 | 11 | 1 | 21.0 | TDD | 112 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3260356 | 6 | 121.4712102339 | 31.1483756942 | 181 | 10 | 10 | 7.9 | TDD | 560 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3264143 | 1 | 121.4678355245 | 31.1481617282 | 229 | 0 | 6 | 11.4 | TDD | 899 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3264803 | 13 | 121.4669027460 | 31.1527626045 | 320 | 14 | 5 | 29.2 | FDD | 441 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |

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
| 2024-09-20 22:21:31.391 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.407 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.528 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.528 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.273 | NREventA2 | measId:1;ServCellPCI:678;Se... |
| 2024-09-20 22:21:35.400 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.652 | NREventA5 | measId:3;ServCellPCI:678;Se... |
| 2024-09-20 22:21:35.700 | NRHandoverAttempt | SourcePCI:678;SourceNR-ARFC... |
| 2024-09-20 22:21:35.733 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.744 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.883 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.883 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264143 | 1 | 13.4962 | 9.8040 | -115.2557 | 9.7594 | 179.6129 | 0.0020 | 0.0126 |
| 2024_09_20 22:00 | 3237405 | 2 | 13.4639 | 10.8219 | -115.7443 | 6.7593 | 84.4110 | 0.0051 | 0.0063 |
| 2024_09_20 22:00 | 3242670 | 3 | 14.5070 | 18.9818 | -114.3899 | 5.7021 | 97.4934 | 0.0004 | 0.0004 |
| 2024_09_20 22:00 | 3259652 | 4 | 16.7444 | 17.6571 | -116.6858 | 17.2786 | 162.5020 | 0.0099 | 0.0093 |
| 2024_09_20 22:00 | 3248672 | 5 | 12.0366 | 7.7393 | -114.3852 | 15.3949 | 181.2611 | 0.0138 | 0.0004 |
| 2024_09_20 22:00 | 3260356 | 6 | 15.2191 | 8.7315 | -115.8114 | 14.2540 | 191.4354 | 0.0144 | 0.0012 |
| 2024_09_20 22:00 | 3247492 | 7 | 8.0112 | 13.3969 | -116.3186 | 4.6789 | 25.0808 | 0.0021 | 0.0199 |
| 2024_09_20 22:00 | 3217649 | 8 | 15.2295 | 12.4210 | -115.6474 | 3.0289 | 26.3906 | 0.0048 | 0.0191 |
| 2024_09_20 22:00 | 3223140 | 9 | 17.9678 | 15.1500 | -114.3988 | 4.5360 | 42.8567 | 0.0157 | 0.0149 |
| 2024_09_20 22:00 | 3254676 | 10 | 11.9224 | 8.1477 | -117.1326 | 3.7987 | 33.4046 | 0.0153 | 0.0101 |
| 2024_09_20 22:00 | 3253296 | 11 | 14.1776 | 7.6620 | -117.0251 | 3.9824 | 21.5140 | 0.0087 | 0.0148 |
| 2024_09_20 22:00 | 3248940 | 12 | 16.6548 | 14.2280 | -116.3498 | 4.5167 | 53.6387 | 0.0142 | 0.0151 |
| 2024_09_20 22:00 | 3264803 | 13 | 14.3970 | 9.6394 | -116.2956 | 4.8112 | 27.6765 | 0.0117 | 0.0004 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413911_A4D82864 | 152650 | 116 | -91.4 | 152650 | 441 | -94.4 | 152650 | 17 | -97.7 | 152650 | 779 |
| MR_1774413911_FE0DD321 | 504990 | 560 | -97.4 | 504990 | 899 | -95.0 | 504990 | 592 | -104.7 | 504990 | 40 |
| MR_1774413911_B82A45B7 | 504990 | 560 | -94.3 | 504990 | 899 | -92.2 | 504990 | 592 | -102.2 | 504990 | 40 |
| MR_1774413911_CE9695C6 | 152650 | 116 | -90.0 | 152650 | 441 | -94.4 | 152650 | 17 | -98.9 | 152650 | 779 |
| MR_1774413911_EB1284C7 | 504990 | 560 | -95.3 | 504990 | 899 | -94.4 | 504990 | 592 | -102.3 | 504990 | 40 |
| MR_1774413911_5E113EF9 | 152650 | 116 | -89.8 | 152650 | 441 | -95.3 | 152650 | 17 | -98.3 | 152650 | 779 |
| MR_1774413911_83A5C092 | 152650 | 116 | -88.8 | 152650 | 441 | -94.2 | 152650 | 17 | -98.4 | 152650 | 779 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 956: `9bd9dc4a-953...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9bd9dc4a-9530-4894-9f21-8f1118b857b4` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease A3 Offset threshold for 3213214_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[956] topology](images/train_0956.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3213214_3
- `C2`: Press down the tilt angle  of 3229959_1 by 7 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213214_3
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Check test server and transmission issues
- `C6`: Lift the tilt angle of 3213214_3 by 5 degrees
- `C7`: Press down the tilt angle of 3213214_3 by 5 degrees
- `C8`: Increase A3 Offset threshold for 3229959_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213214_3
- `C10`: Add neighbor relationship between 3213214_3 and 3229959_1
- `C11`: Add neighbor relationship between 3278581_2 and 3229959_1
- `C12`: Decrease transmission power for 3229959_1
- `C13`: Decrease A3 Offset threshold for 3213214_3 **← 정답**
- `C14`: Increase transmission power for 3229959_1
- `C15`: Decrease A3 Offset threshold for 3229959_1
- `C16`: Decrease transmission power for 3213214_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229959_1
- `C18`: Adjust the azimuth of 3229959_1 by 50 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229959_1
- `C20`: Lift the tilt angle  of 3229959_1 by 7 degrees
- `C21`: Adjust the azimuth of 3213214_3 by 48 degrees
- `C22`: Increase transmission power for 3213214_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.447 | MS1 | 121.4656762019 | 31.1446187563 | 293 | 504990 | -75.92 | 12.62 | 488.71 | 0.15 | 2.17 | 1562 |
| 2024-09-20 22:21:32.154 | MS1 | 121.4656756154 | 31.1446365172 | 293 | 504990 | -75.08 | 14.53 | 483.07 | 0.05 | 2.58 | 1563 |
| 2024-09-20 22:21:33.504 | MS1 | 121.4656742084 | 31.1446246651 | 293 | 504990 | -80.87 | 17.53 | 335.52 | 0.07 | 2.67 | 1597 |
| 2024-09-20 22:21:34.992 | MS1 | 121.4656671797 | 31.1446274501 | 293 | 504990 | -84.11 | -3.17 | 44.43 | 0.00 | 1.02 | 1563 |
| 2024-09-20 22:21:35.154 | MS1 | 121.4656661621 | 31.1446328098 | 293 | 504990 | -85.23 | -0.37 | 42.16 | 0.07 | 1.26 | 1571 |
| 2024-09-20 22:21:36.757 | MS1 | 121.4656610196 | 31.1446339623 | 293 | 504990 | -91.67 | -0.42 | 55.27 | 0.10 | 1.43 | 1579 |
| 2024-09-20 22:21:37.856 | MS1 | 121.4656690759 | 31.1446267253 | 293 | 504990 | -92.97 | -3.94 | 40.68 | 0.06 | 1.25 | 1585 |
| 2024-09-20 22:21:38.975 | MS1 | 121.4656639907 | 31.1446376632 | 293 | 504990 | -84.96 | -2.12 | 37.31 | 0.11 | 1.30 | 1595 |
| 2024-09-20 22:21:39.302 | MS1 | 121.4656612077 | 31.1446345558 | 905 | 504990 | -77.26 | 15.79 | 256.19 | 0.10 | 1.10 | 1564 |
| 2024-09-20 22:21:40.530 | MS1 | 121.4656745663 | 31.1446348903 | 905 | 504990 | -83.05 | 14.13 | 383.19 | 0.16 | 2.01 | 1561 |
| 2024-09-20 22:21:41.663 | MS1 | 121.4656764460 | 31.1446254334 | 905 | 504990 | -83.57 | 12.04 | 330.17 | 0.11 | 2.87 | 1574 |
| 2024-09-20 22:21:42.549 | MS1 | 121.4656758979 | 31.1446307255 | 905 | 504990 | -80.91 | 13.11 | 461.44 | 0.07 | 2.35 | 1574 |

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
| 3213214 | 3 | 121.4728806831 | 31.1482797003 | 287 | 2 | 5 | 46.2 | TDD | 293 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3215560 | 4 | 121.4652739747 | 31.1449862239 | 115 | 14 | 0 | 27.3 | TDD | 941 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3229959 | 1 | 121.4675525627 | 31.1538549893 | 286 | 5 | 7 | 37.5 | TDD | 905 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3278581 | 2 | 121.4685513658 | 31.1546794517 | 256 | 13 | 3 | 34.1 | TDD | 330 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.760 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.861 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.861 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.626 | NREventA3 | measId:2;ServCellPCI:378;Se... |
| 2024-09-20 22:21:37.866 | NRHandoverAttempt | SourcePCI:378;SourceNR-ARFC... |
| 2024-09-20 22:21:37.903 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.914 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.016 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.016 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229959 | 1 | 14.6594 | 16.4422 | -117.2199 | 9.0258 | 108.1842 | 0.0087 | 0.0051 |
| 2024_09_20 22:00 | 3278581 | 2 | 13.6246 | 13.7139 | -116.3194 | 12.8260 | 149.2730 | 0.0080 | 0.0068 |
| 2024_09_20 22:00 | 3213214 | 3 | 5.9382 | 13.1301 | -114.6234 | 7.0676 | 195.9200 | 0.0166 | 0.1945 |
| 2024_09_20 22:00 | 3215560 | 4 | 5.7794 | 12.6382 | -114.7607 | 14.2040 | 109.7645 | 0.0071 | 0.0184 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412738_319668AC | 504990 | 293 | -82.8 | 504990 | 905 | -80.7 | 504990 | 330 | -90.4 | 504990 | 941 |
| MR_1774412738_2FBAD804 | 504990 | 905 | -77.8 | 504990 | 293 | -83.2 | 504990 | 330 | -89.3 | 504990 | 941 |
| MR_1774412738_88C510F5 | 504990 | 905 | -77.7 | 504990 | 293 | -82.4 | 504990 | 330 | -89.7 | 504990 | 941 |
| MR_1774412738_14EF29C7 | 504990 | 293 | -83.5 | 504990 | 905 | -80.0 | 504990 | 330 | -89.4 | 504990 | 941 |
| MR_1774412738_129CC8A7 | 504990 | 293 | -83.3 | 504990 | 905 | -80.6 | 504990 | 330 | -88.2 | 504990 | 941 |
| MR_1774412738_32AF26B7 | 504990 | 293 | -84.8 | 504990 | 905 | -79.0 | 504990 | 330 | -88.8 | 504990 | 941 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 957: `dd536777-43b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dd536777-43b7-453c-b6b2-cb20ef72c7a3` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[957] topology](images/train_0957.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3269060_1
- `C2`: Adjust the azimuth of 3215141_2 by 50 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215141_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215141_2
- `C5`: Increase transmission power for 3269060_1
- `C6`: Increase A3 Offset threshold for 3269060_1
- `C7`: Press down the tilt angle  of 3269060_1 by 10 degrees
- `C8`: Lift the tilt angle of 3215141_2 by 10 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269060_1
- `C10`: Increase transmission power for 3215141_2
- `C11`: Adjust the azimuth of 3269060_1 by 45 degrees
- `C12`: Press down the tilt angle of 3215141_2 by 10 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269060_1
- `C14`: Increase A3 Offset threshold for 3215141_2
- `C15`: Insufficient data; more data is needed for judgment. **← 정답**
- `C16`: Check test server and transmission issues
- `C17`: Decrease A3 Offset threshold for 3215141_2
- `C18`: Decrease transmission power for 3269060_1
- `C19`: Add neighbor relationship between 3215141_2 and 3269060_1
- `C20`: Lift the tilt angle  of 3269060_1 by 10 degrees
- `C21`: Decrease transmission power for 3215141_2
- `C22`: Add neighbor relationship between 3237072_4 and 3269060_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.101 | MS1 | 121.4656625975 | 31.1446337750 | 803 | 504990 | -87.03 | 16.99 | 516.94 | 0.02 | 2.09 | 1568 |
| 2024-09-20 22:21:32.968 | MS1 | 121.4656772267 | 31.1446302754 | 803 | 504990 | -89.32 | 17.67 | 321.75 | 0.03 | 2.53 | 1585 |
| 2024-09-20 22:21:33.738 | MS1 | 121.4656738396 | 31.1446208677 | 803 | 504990 | -85.03 | 13.98 | 559.46 | 0.07 | 2.55 | 1598 |
| 2024-09-20 22:21:34.226 | MS1 | 121.4656607395 | 31.1446195499 | 803 | 504990 | -87.59 | 14.69 | 96.95 | 0.04 | 2.91 | 1593 |
| 2024-09-20 22:21:35.954 | MS1 | 121.4656657079 | 31.1446244513 | 803 | 504990 | -90.60 | 13.27 | 56.97 | 0.04 | 2.44 | 1593 |
| 2024-09-20 22:21:36.826 | MS1 | 121.4656719748 | 31.1446200391 | 803 | 504990 | -91.89 | 14.24 | 91.64 | 0.07 | 2.76 | 1564 |
| 2024-09-20 22:21:37.899 | MS1 | 121.4656739389 | 31.1446250555 | 803 | 504990 | -90.54 | 7.90 | 60.07 | 0.10 | 2.15 | 1594 |
| 2024-09-20 22:21:38.783 | MS1 | 121.4656672597 | 31.1446342463 | 803 | 504990 | -89.25 | 9.77 | 77.35 | 0.17 | 2.78 | 1583 |
| 2024-09-20 22:21:39.598 | MS1 | 121.4656643066 | 31.1446234191 | 803 | 504990 | -92.98 | 7.19 | 63.02 | 0.15 | 2.96 | 1580 |
| 2024-09-20 22:21:40.758 | MS1 | 121.4656740053 | 31.1446261508 | 803 | 504990 | -89.31 | 7.54 | 410.37 | 0.12 | 2.95 | 1595 |
| 2024-09-20 22:21:41.219 | MS1 | 121.4656695267 | 31.1446190469 | 803 | 504990 | -92.73 | 8.41 | 338.62 | 0.12 | 2.70 | 1571 |
| 2024-09-20 22:21:42.525 | MS1 | 121.4656725931 | 31.1446193329 | 803 | 504990 | -93.60 | 7.05 | 381.54 | 0.16 | 2.56 | 1565 |

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
| 3215141 | 2 | 121.4653598050 | 31.1441627017 | 306 | 4 | 11 | 25.9 | TDD | 803 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3237072 | 4 | 121.4754816850 | 31.1508581453 | 76 | 3 | 12 | 26.1 | TDD | 17 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3247792 | 3 | 121.4672232594 | 31.1517395300 | 221 | 7 | 8 | 25.0 | TDD | 814 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3269060 | 1 | 121.4677883857 | 31.1454723474 | 290 | 9 | 9 | 32.7 | TDD | 89 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.612 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.637 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.763 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.763 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.456 | NREventA3 | measId:2;ServCellPCI:349;Se... |
| 2024-09-20 22:21:38.696 | NRHandoverAttempt | SourcePCI:349;SourceNR-ARFC... |
| 2024-09-20 22:21:38.734 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.747 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.860 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.860 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3269060 | 1 | 82.7190 | 84.0960 | -115.2003 | 9.3206 | 121.9027 | 0.0138 | 0.0017 |
| 2024_09_19 22:00 | 3215141 | 2 | 93.5508 | 93.6986 | -115.6386 | 5.5260 | 85.1579 | 0.0134 | 0.0174 |
| 2024_09_19 22:00 | 3247792 | 3 | 81.6841 | 81.2721 | -114.2194 | 16.0484 | 129.2012 | 0.0186 | 0.0154 |
| 2024_09_19 22:00 | 3237072 | 4 | 90.5665 | 88.2398 | -114.8082 | 8.4897 | 127.2705 | 0.0170 | 0.0142 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413608_5523873C | 504990 | 803 | -85.8 | 504990 | 89 | -89.9 | 504990 | 17 | -96.2 | 504990 | 814 |
| MR_1774413608_E18D5E4A | 504990 | 803 | -86.2 | 504990 | 89 | -92.5 | 504990 | 17 | -95.5 | 504990 | 814 |
| MR_1774413608_1A6F6119 | 504990 | 803 | -86.4 | 504990 | 89 | -92.5 | 504990 | 17 | -93.0 | 504990 | 814 |
| MR_1774413608_D3E3AA3E | 504990 | 803 | -89.3 | 504990 | 89 | -92.0 | 504990 | 17 | -94.4 | 504990 | 814 |
| MR_1774413608_9C2B6DB6 | 504990 | 803 | -85.6 | 504990 | 89 | -91.8 | 504990 | 17 | -92.9 | 504990 | 814 |
| MR_1774413608_C339EAEE | 504990 | 803 | -87.9 | 504990 | 89 | -90.0 | 504990 | 17 | -96.2 | 504990 | 814 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 958: `d2bf2681-c1c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d2bf2681-c1c2-4102-be30-5971059fabf3` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3269941_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[958] topology](images/train_0958.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3269941_2 by 6 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269941_2 **← 정답**
- `C3`: Check test server and transmission issues
- `C4`: Decrease A3 Offset threshold for 3225552_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225552_3
- `C6`: Increase A3 Offset threshold for 3225552_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269941_2
- `C8`: Add neighbor relationship between 3237662_1 and 3225552_3
- `C9`: Press down the tilt angle  of 3225552_3 by 10 degrees
- `C10`: Press down the tilt angle of 3269941_2 by 6 degrees
- `C11`: Adjust the azimuth of 3225552_3 by 50 degrees
- `C12`: Decrease A3 Offset threshold for 3269941_2
- `C13`: Decrease transmission power for 3225552_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225552_3
- `C15`: Adjust the azimuth of 3269941_2 by 46 degrees
- `C16`: Increase transmission power for 3225552_3
- `C17`: Increase transmission power for 3269941_2
- `C18`: Increase A3 Offset threshold for 3269941_2
- `C19`: Add neighbor relationship between 3269941_2 and 3225552_3
- `C20`: Decrease transmission power for 3269941_2
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Lift the tilt angle  of 3225552_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.457 | MS1 | 121.4656733752 | 31.1446197235 | 445 | 504990 | -86.52 | 14.98 | 510.90 | 0.03 | 2.69 | 1583 |
| 2024-09-20 22:21:32.393 | MS1 | 121.4656611847 | 31.1446201378 | 445 | 504990 | -90.59 | 15.43 | 411.37 | 0.13 | 2.44 | 1571 |
| 2024-09-20 22:21:33.710 | MS1 | 121.4656580178 | 31.1446238889 | 445 | 504990 | -90.47 | 15.16 | 411.93 | 0.04 | 2.19 | 1594 |
| 2024-09-20 22:21:34.163 | MS1 | 121.4656626964 | 31.1446285037 | 445 | 504990 | -88.96 | 12.84 | 84.93 | 0.61 | 2.60 | 626 |
| 2024-09-20 22:21:35.551 | MS1 | 121.4656737196 | 31.1446257049 | 445 | 504990 | -85.37 | 16.43 | 70.32 | 0.58 | 2.96 | 660 |
| 2024-09-20 22:21:36.651 | MS1 | 121.4656657783 | 31.1446346632 | 445 | 504990 | -86.38 | 12.28 | 86.11 | 0.53 | 2.48 | 579 |
| 2024-09-20 22:21:37.452 | MS1 | 121.4656594964 | 31.1446270149 | 445 | 504990 | -93.94 | 12.78 | 101.77 | 0.57 | 2.49 | 544 |
| 2024-09-20 22:21:38.637 | MS1 | 121.4656709863 | 31.1446361420 | 445 | 504990 | -91.75 | 9.15 | 84.91 | 0.65 | 2.44 | 572 |
| 2024-09-20 22:21:39.901 | MS1 | 121.4656731156 | 31.1446213088 | 445 | 504990 | -90.21 | 10.79 | 88.94 | 0.64 | 2.59 | 647 |
| 2024-09-20 22:21:40.694 | MS1 | 121.4656677902 | 31.1446262477 | 445 | 504990 | -92.84 | 11.83 | 533.79 | 0.12 | 2.57 | 1576 |
| 2024-09-20 22:21:41.728 | MS1 | 121.4656687093 | 31.1446286345 | 445 | 504990 | -89.93 | 8.95 | 304.30 | 0.13 | 2.93 | 1595 |
| 2024-09-20 22:21:42.540 | MS1 | 121.4656747644 | 31.1446327152 | 445 | 504990 | -92.85 | 8.17 | 549.99 | 0.19 | 2.23 | 1600 |

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
| 3225552 | 3 | 121.4706198943 | 31.1491901518 | 50 | 10 | 10 | 15.7 | TDD | 838 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3237662 | 1 | 121.4748570605 | 31.1450921499 | 143 | 3 | 5 | 24.4 | TDD | 464 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3269941 | 2 | 121.4693871435 | 31.1452788979 | 212 | 1 | 8 | 30.2 | TDD | 445 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3271326 | 4 | 121.4752507837 | 31.1497510078 | 288 | 8 | 8 | 27.7 | TDD | 472 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.541 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.565 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.685 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.685 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.363 | NREventA3 | measId:2;ServCellPCI:573;Se... |
| 2024-09-20 22:21:38.603 | NRHandoverAttempt | SourcePCI:573;SourceNR-ARFC... |
| 2024-09-20 22:21:38.639 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.651 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.791 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.791 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237662 | 1 | 16.2353 | 9.5117 | -114.5216 | 12.6978 | 113.3591 | 0.0057 | 0.0016 |
| 2024_09_20 22:00 | 3269941 | 2 | 7.1559 | 8.2249 | -114.4307 | 12.9509 | 162.4455 | 0.0103 | 0.0041 |
| 2024_09_20 22:00 | 3225552 | 3 | 15.3930 | 11.6909 | -115.4408 | 12.5165 | 143.7341 | 0.0046 | 0.0096 |
| 2024_09_20 22:00 | 3271326 | 4 | 9.8320 | 7.2196 | -117.3779 | 6.3539 | 81.7173 | 0.0188 | 0.0094 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413200_A71AF8F5 | 504990 | 445 | -87.8 | 504990 | 838 | -90.6 | 504990 | 464 | -100.0 | 504990 | 472 |
| MR_1774413200_A0BC63B7 | 504990 | 445 | -89.4 | 504990 | 838 | -93.1 | 504990 | 464 | -98.9 | 504990 | 472 |
| MR_1774413200_5036C049 | 504990 | 445 | -88.4 | 504990 | 838 | -91.9 | 504990 | 464 | -99.1 | 504990 | 472 |
| MR_1774413200_FAC6AC78 | 504990 | 445 | -89.7 | 504990 | 838 | -92.1 | 504990 | 464 | -98.9 | 504990 | 472 |
| MR_1774413200_3DFFC2C6 | 504990 | 445 | -90.0 | 504990 | 838 | -92.8 | 504990 | 464 | -98.8 | 504990 | 472 |
| MR_1774413200_6930BC92 | 504990 | 445 | -88.3 | 504990 | 838 | -90.4 | 504990 | 464 | -99.7 | 504990 | 472 |
| MR_1774413200_418CEAE0 | 504990 | 445 | -90.8 | 504990 | 838 | -90.8 | 504990 | 464 | -100.7 | 504990 | 472 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 959: `a6fb5ee1-728...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a6fb5ee1-728a-4cbb-987d-ec564ebb0572` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[959] topology](images/train_0959.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217904_2
- `C2`: Press down the tilt angle of 3217904_2 by 10 degrees
- `C3`: Check test server and transmission issues **← 정답**
- `C4`: Increase transmission power for 3274080_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274080_1
- `C6`: Increase A3 Offset threshold for 3217904_2
- `C7`: Adjust the azimuth of 3217904_2 by 40 degrees
- `C8`: Add neighbor relationship between 3217904_2 and 3274080_1
- `C9`: Lift the tilt angle of 3217904_2 by 10 degrees
- `C10`: Decrease A3 Offset threshold for 3274080_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Lift the tilt angle  of 3274080_1 by 10 degrees
- `C13`: Increase transmission power for 3217904_2
- `C14`: Decrease A3 Offset threshold for 3217904_2
- `C15`: Press down the tilt angle  of 3274080_1 by 10 degrees
- `C16`: Decrease transmission power for 3217904_2
- `C17`: Increase A3 Offset threshold for 3274080_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217904_2
- `C19`: Add neighbor relationship between 3211823_3 and 3274080_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274080_1
- `C21`: Decrease transmission power for 3274080_1
- `C22`: Adjust the azimuth of 3274080_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.415 | MS1 | 121.4656664562 | 31.1446327017 | 99 | 504990 | -85.59 | 15.88 | 519.17 | 0.00 | 2.18 | 1574 |
| 2024-09-20 22:21:32.120 | MS1 | 121.4656758893 | 31.1446283956 | 99 | 504990 | -91.64 | 14.27 | 353.94 | 0.13 | 2.56 | 1578 |
| 2024-09-20 22:21:33.484 | MS1 | 121.4656711868 | 31.1446224432 | 99 | 504990 | -91.08 | 17.23 | 300.51 | 0.12 | 2.57 | 1598 |
| 2024-09-20 22:21:34.552 | MS1 | 121.4656604196 | 31.1446366656 | 99 | 504990 | -85.97 | 12.55 | 61.81 | 0.10 | 2.64 | 353 |
| 2024-09-20 22:21:35.584 | MS1 | 121.4656629412 | 31.1446280199 | 99 | 504990 | -85.72 | 15.74 | 84.53 | 0.04 | 2.54 | 421 |
| 2024-09-20 22:21:36.672 | MS1 | 121.4656669354 | 31.1446366286 | 99 | 504990 | -87.42 | 17.18 | 86.77 | 0.06 | 2.97 | 388 |
| 2024-09-20 22:21:37.212 | MS1 | 121.4656606602 | 31.1446217553 | 99 | 504990 | -90.65 | 8.50 | 96.47 | 0.05 | 2.50 | 422 |
| 2024-09-20 22:21:38.467 | MS1 | 121.4656580473 | 31.1446300888 | 99 | 504990 | -89.64 | 12.74 | 59.76 | 0.18 | 2.55 | 303 |
| 2024-09-20 22:21:39.499 | MS1 | 121.4656725466 | 31.1446212592 | 99 | 504990 | -90.22 | 7.24 | 81.34 | 0.10 | 2.94 | 339 |
| 2024-09-20 22:21:40.979 | MS1 | 121.4656668216 | 31.1446282074 | 99 | 504990 | -91.28 | 10.14 | 522.14 | 0.05 | 2.97 | 1569 |
| 2024-09-20 22:21:41.226 | MS1 | 121.4656689875 | 31.1446372235 | 99 | 504990 | -90.51 | 11.12 | 337.76 | 0.04 | 2.78 | 1595 |
| 2024-09-20 22:21:42.424 | MS1 | 121.4656656217 | 31.1446335507 | 99 | 504990 | -92.35 | 9.94 | 577.12 | 0.15 | 2.41 | 1577 |

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
| 3211823 | 3 | 121.4685290931 | 31.1472016597 | 65 | 11 | 5 | 29.1 | TDD | 965 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3212624 | 4 | 121.4642100127 | 31.1496623662 | 143 | 1 | 11 | 48.9 | TDD | 424 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3217904 | 2 | 121.4641753355 | 31.1550372252 | 213 | 10 | 4 | 30.6 | TDD | 99 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3274080 | 1 | 121.4672475519 | 31.1544496957 | 135 | 15 | 12 | 26.8 | TDD | 61 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.057 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.078 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.193 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.193 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.893 | NREventA3 | measId:2;ServCellPCI:57;Ser... |
| 2024-09-20 22:21:38.133 | NRHandoverAttempt | SourcePCI:57;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.183 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.198 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.325 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.325 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274080 | 1 | 12.8964 | 19.8765 | -117.4428 | 12.7757 | 109.7476 | 0.0034 | 0.0039 |
| 2024_09_20 22:00 | 3217904 | 2 | 14.8225 | 16.6066 | -117.3739 | 5.1202 | 96.6334 | 0.0150 | 0.0096 |
| 2024_09_20 22:00 | 3211823 | 3 | 18.2442 | 15.6282 | -114.6529 | 10.1385 | 92.4072 | 0.0074 | 0.0089 |
| 2024_09_20 22:00 | 3212624 | 4 | 10.6807 | 9.1558 | -114.8313 | 12.7742 | 129.6416 | 0.0063 | 0.0086 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413428_BAF21ED8 | 504990 | 99 | -87.2 | 504990 | 61 | -87.8 | 504990 | 965 | -91.5 | 504990 | 424 |
| MR_1774413428_86F05020 | 504990 | 99 | -84.9 | 504990 | 61 | -91.3 | 504990 | 965 | -93.8 | 504990 | 424 |
| MR_1774413428_EC2ECC45 | 504990 | 99 | -84.3 | 504990 | 61 | -88.7 | 504990 | 965 | -94.2 | 504990 | 424 |
| MR_1774413428_380D000E | 504990 | 99 | -86.0 | 504990 | 61 | -90.5 | 504990 | 965 | -91.5 | 504990 | 424 |
| MR_1774413428_93E268D8 | 504990 | 99 | -85.0 | 504990 | 61 | -89.5 | 504990 | 965 | -91.2 | 504990 | 424 |
| MR_1774413428_FD39EEEC | 504990 | 99 | -85.5 | 504990 | 61 | -87.6 | 504990 | 965 | -92.4 | 504990 | 424 |
| MR_1774413428_CA138316 | 504990 | 99 | -85.3 | 504990 | 61 | -90.0 | 504990 | 965 | -92.0 | 504990 | 424 |
| MR_1774413428_1581A1FB | 504990 | 99 | -84.3 | 504990 | 61 | -88.5 | 504990 | 965 | -93.5 | 504990 | 424 |

> *... 2개 열 생략 (전체 14열)*

---
