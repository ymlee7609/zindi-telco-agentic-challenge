# Track A 문제 분석 — train[1370]~train[1379]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1370] ~ train[1379] (10개)

## 목차

1. [문제 1370: `c04f86da-745...`](#1370) — single-answer, 정답: C19
2. [문제 1371: `d2028366-210...`](#1371) — single-answer, 정답: C22
3. [문제 1372: `e7d8bb45-c4c...`](#1372) — single-answer, 정답: C3
4. [문제 1373: `abdcb0e4-a5c...`](#1373) — multiple-answer, 정답: C6|C9|C10|C19
5. [문제 1374: `8f4c1113-11c...`](#1374) — multiple-answer, 정답: C3|C19
6. [문제 1375: `873b8a92-8da...`](#1375) — single-answer, 정답: C3
7. [문제 1376: `36645cba-465...`](#1376) — multiple-answer, 정답: C11|C19
8. [문제 1377: `3bdd3480-662...`](#1377) — multiple-answer, 정답: C13|C21
9. [문제 1378: `e250f489-837...`](#1378) — single-answer, 정답: C6
10. [문제 1379: `7bc02551-e84...`](#1379) — single-answer, 정답: C21

---

### 문제 1370: `c04f86da-745...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c04f86da-7454-4bf1-a923-53fddf05b741` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Lift the tilt angle  of 3263021_1 by 8 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1370] topology](images/train_1370.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3263021_1 by 8 degrees
- `C2`: Add neighbor relationship between 3275179_2 and 3249323_4
- `C3`: Lift the tilt angle of 3275179_2 by 1 degrees
- `C4`: Adjust the azimuth of 3263021_1 by 46 degrees
- `C5`: Decrease A3 Offset threshold for 3249323_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Adjust the azimuth of 3275179_2 by 4 degrees
- `C8`: Increase transmission power for 3275179_2
- `C9`: Press down the tilt angle of 3275179_2 by 1 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275179_2
- `C11`: Decrease transmission power for 3275179_2
- `C12`: Increase A3 Offset threshold for 3275179_2
- `C13`: Increase A3 Offset threshold for 3249323_4
- `C14`: Decrease A3 Offset threshold for 3275179_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249323_4
- `C16`: Add neighbor relationship between 3263021_1 and 3249323_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275179_2
- `C18`: Decrease transmission power for 3249323_4
- `C19`: Lift the tilt angle  of 3263021_1 by 8 degrees **← 정답**
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249323_4
- `C21`: Check test server and transmission issues
- `C22`: Increase transmission power for 3249323_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.609 | MS1 | 121.4656690279 | 31.1446225604 | 356 | 504990 | -90.54 | 12.94 | 494.42 | 0.10 | 2.31 | 1599 |
| 2024-09-20 22:21:32.163 | MS1 | 121.4656688419 | 31.1446188348 | 356 | 504990 | -88.03 | 14.93 | 310.76 | 0.04 | 2.59 | 1599 |
| 2024-09-20 22:21:33.251 | MS1 | 121.4656721829 | 31.1446355952 | 356 | 504990 | -88.29 | 12.21 | 485.67 | 0.11 | 2.04 | 1597 |
| 2024-09-20 22:21:34.841 | MS1 | 121.4656721785 | 31.1446292159 | 356 | 504990 | -88.71 | 17.65 | 69.56 | 0.06 | 2.59 | 1583 |
| 2024-09-20 22:21:35.945 | MS1 | 121.4656584369 | 31.1446324890 | 356 | 504990 | -86.82 | 12.97 | 84.99 | 0.08 | 2.07 | 1562 |
| 2024-09-20 22:21:36.396 | MS1 | 121.4656677654 | 31.1446278164 | 356 | 504990 | -85.86 | 13.50 | 90.90 | 0.17 | 2.70 | 1568 |
| 2024-09-20 22:21:37.966 | MS1 | 121.4656582757 | 31.1446222289 | 356 | 504990 | -91.27 | 10.68 | 95.16 | 0.09 | 2.67 | 1573 |
| 2024-09-20 22:21:38.815 | MS1 | 121.4656644583 | 31.1446206683 | 356 | 504990 | -92.11 | 9.05 | 97.80 | 0.14 | 2.16 | 1580 |
| 2024-09-20 22:21:39.326 | MS1 | 121.4656720960 | 31.1446280077 | 356 | 504990 | -90.72 | 11.70 | 56.15 | 0.02 | 2.78 | 1562 |
| 2024-09-20 22:21:40.202 | MS1 | 121.4656594066 | 31.1446239576 | 356 | 504990 | -92.39 | 8.31 | 343.17 | 0.05 | 2.77 | 1568 |
| 2024-09-20 22:21:41.757 | MS1 | 121.4656586356 | 31.1446215563 | 356 | 504990 | -89.73 | 9.35 | 416.88 | 0.13 | 2.66 | 1570 |
| 2024-09-20 22:21:42.740 | MS1 | 121.4656625804 | 31.1446205653 | 356 | 504990 | -92.46 | 10.92 | 453.80 | 0.16 | 2.42 | 1578 |

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
| 3249323 | 4 | 121.4674046573 | 31.1494001233 | 243 | 4 | 1 | 35.6 | TDD | 52 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3258592 | 3 | 121.4752832122 | 31.1468670138 | 331 | 7 | 3 | 43.3 | TDD | 908 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3263021 | 1 | 121.4651718721 | 31.1471906411 | 313 | 3 | 9 | 25.4 | TDD | 304 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3275179 | 2 | 121.4754448406 | 31.1521674372 | 224 | 0 | 7 | 17.2 | TDD | 356 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.366 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.387 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.505 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.505 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.266 | NREventA3 | measId:2;ServCellPCI:782;Se... |
| 2024-09-20 22:21:38.506 | NRHandoverAttempt | SourcePCI:782;SourceNR-ARFC... |
| 2024-09-20 22:21:38.554 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.565 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.711 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.711 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263021 | 1 | 13.3539 | 7.5841 | -116.4854 | 12.5029 | 151.1786 | 0.0176 | 0.0197 |
| 2024_09_20 22:00 | 3275179 | 2 | 79.8961 | 87.3760 | -115.7436 | 5.7881 | 198.3396 | 0.0141 | 0.0018 |
| 2024_09_20 22:00 | 3258592 | 3 | 8.8733 | 10.2961 | -115.8069 | 9.1676 | 128.1378 | 0.0131 | 0.0009 |
| 2024_09_20 22:00 | 3249323 | 4 | 18.6607 | 7.1853 | -115.9072 | 10.4525 | 123.0419 | 0.0014 | 0.0010 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415760_1F99405F | 504990 | 356 | -87.4 | 504990 | 52 | -95.8 | 504990 | 304 | -95.9 | 504990 | 908 |
| MR_1774415760_45AC742F | 504990 | 356 | -88.8 | 504990 | 52 | -95.2 | 504990 | 304 | -96.3 | 504990 | 908 |
| MR_1774415760_08CC3F8D | 504990 | 356 | -89.5 | 504990 | 52 | -95.3 | 504990 | 304 | -98.5 | 504990 | 908 |
| MR_1774415760_975A7900 | 504990 | 356 | -89.4 | 504990 | 52 | -95.4 | 504990 | 304 | -95.8 | 504990 | 908 |
| MR_1774415760_5B8FB917 | 504990 | 356 | -89.8 | 504990 | 52 | -98.3 | 504990 | 304 | -99.1 | 504990 | 908 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1371: `d2028366-210...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d2028366-2104-4566-bad4-54c607f19183` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Lift the tilt angle  of 3262912_3 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1371] topology](images/train_1371.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Add neighbor relationship between 3268521_2 and 3252509_1
- `C3`: Decrease A3 Offset threshold for 3268521_2
- `C4`: Lift the tilt angle of 3268521_2 by 6 degrees
- `C5`: Adjust the azimuth of 3268521_2 by 5 degrees
- `C6`: Adjust the azimuth of 3262912_3 by 50 degrees
- `C7`: Increase A3 Offset threshold for 3252509_1
- `C8`: Check test server and transmission issues
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252509_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268521_2
- `C11`: Add neighbor relationship between 3262912_3 and 3252509_1
- `C12`: Press down the tilt angle of 3268521_2 by 6 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268521_2
- `C14`: Increase transmission power for 3252509_1
- `C15`: Decrease transmission power for 3268521_2
- `C16`: Decrease A3 Offset threshold for 3252509_1
- `C17`: Increase A3 Offset threshold for 3268521_2
- `C18`: Decrease transmission power for 3252509_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252509_1
- `C20`: Increase transmission power for 3268521_2
- `C21`: Press down the tilt angle  of 3262912_3 by 7 degrees
- `C22`: Lift the tilt angle  of 3262912_3 by 7 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.231 | MS1 | 121.4656689091 | 31.1446362608 | 61 | 504990 | -90.06 | 14.95 | 361.57 | 0.19 | 2.44 | 1574 |
| 2024-09-20 22:21:32.426 | MS1 | 121.4656619551 | 31.1446217678 | 61 | 504990 | -90.64 | 13.68 | 398.19 | 0.10 | 2.66 | 1583 |
| 2024-09-20 22:21:33.372 | MS1 | 121.4656708778 | 31.1446216578 | 61 | 504990 | -89.69 | 14.76 | 344.41 | 0.13 | 2.46 | 1561 |
| 2024-09-20 22:21:34.626 | MS1 | 121.4656757380 | 31.1446289155 | 61 | 504990 | -90.95 | 15.47 | 105.58 | 0.12 | 2.57 | 1599 |
| 2024-09-20 22:21:35.229 | MS1 | 121.4656779405 | 31.1446282018 | 61 | 504990 | -91.12 | 17.00 | 53.99 | 0.03 | 2.60 | 1588 |
| 2024-09-20 22:21:36.194 | MS1 | 121.4656760150 | 31.1446297732 | 61 | 504990 | -87.98 | 16.61 | 88.07 | 0.08 | 2.39 | 1562 |
| 2024-09-20 22:21:37.973 | MS1 | 121.4656629829 | 31.1446194115 | 61 | 504990 | -91.92 | 11.25 | 61.95 | 0.01 | 2.75 | 1572 |
| 2024-09-20 22:21:38.197 | MS1 | 121.4656666930 | 31.1446273641 | 61 | 504990 | -89.95 | 7.47 | 101.36 | 0.18 | 2.47 | 1569 |
| 2024-09-20 22:21:39.456 | MS1 | 121.4656730588 | 31.1446352882 | 61 | 504990 | -93.73 | 10.11 | 78.57 | 0.18 | 2.97 | 1597 |
| 2024-09-20 22:21:40.926 | MS1 | 121.4656635056 | 31.1446296216 | 61 | 504990 | -93.41 | 8.64 | 415.81 | 0.06 | 2.87 | 1589 |
| 2024-09-20 22:21:41.867 | MS1 | 121.4656717075 | 31.1446360452 | 61 | 504990 | -90.87 | 11.54 | 429.81 | 0.15 | 2.98 | 1585 |
| 2024-09-20 22:21:42.361 | MS1 | 121.4656684961 | 31.1446265396 | 61 | 504990 | -92.26 | 10.79 | 476.09 | 0.05 | 2.03 | 1571 |

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
| 3210246 | 4 | 121.4663607189 | 31.1444012268 | 260 | 8 | 8 | 41.3 | TDD | 327 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3252509 | 1 | 121.4648723514 | 31.1546710802 | 321 | 5 | 12 | 47.7 | TDD | 720 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3262912 | 3 | 121.4713648089 | 31.1484340434 | 358 | 5 | 9 | 35.7 | TDD | 989 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3268521 | 2 | 121.4669024965 | 31.1555648929 | 180 | 4 | 1 | 40.5 | TDD | 61 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.079 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.102 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.220 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.220 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.913 | NREventA3 | measId:2;ServCellPCI:758;Se... |
| 2024-09-20 22:21:38.153 | NRHandoverAttempt | SourcePCI:758;SourceNR-ARFC... |
| 2024-09-20 22:21:38.202 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.216 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.339 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.339 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252509 | 1 | 11.5952 | 10.6268 | -116.2920 | 14.2333 | 143.9103 | 0.0151 | 0.0101 |
| 2024_09_20 22:00 | 3268521 | 2 | 91.6245 | 90.4396 | -115.1640 | 5.6022 | 199.0395 | 0.0145 | 0.0061 |
| 2024_09_20 22:00 | 3262912 | 3 | 7.3515 | 19.0850 | -114.3432 | 14.1445 | 149.4789 | 0.0072 | 0.0093 |
| 2024_09_20 22:00 | 3210246 | 4 | 12.4163 | 10.7299 | -117.6847 | 7.0018 | 108.2679 | 0.0078 | 0.0071 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414665_7F4845F7 | 504990 | 61 | -89.8 | 504990 | 720 | -90.2 | 504990 | 989 | -104.5 | 504990 | 327 |
| MR_1774414665_8BAD5C73 | 504990 | 61 | -92.9 | 504990 | 720 | -91.7 | 504990 | 989 | -103.1 | 504990 | 327 |
| MR_1774414665_3E7BC52C | 504990 | 61 | -91.1 | 504990 | 720 | -92.3 | 504990 | 989 | -101.2 | 504990 | 327 |
| MR_1774414665_ED419168 | 504990 | 61 | -89.7 | 504990 | 720 | -92.9 | 504990 | 989 | -103.2 | 504990 | 327 |
| MR_1774414665_B1109B9D | 504990 | 61 | -92.6 | 504990 | 720 | -90.0 | 504990 | 989 | -101.7 | 504990 | 327 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1372: `e7d8bb45-c4c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e7d8bb45-c4cf-433e-9317-595fd487aea2` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Lift the tilt angle  of 3214368_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1372] topology](images/train_1372.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3259051_1 by 3 degrees
- `C2`: Press down the tilt angle  of 3214368_4 by 10 degrees
- `C3`: Lift the tilt angle  of 3214368_4 by 10 degrees **← 정답**
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259051_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Adjust the azimuth of 3214368_4 by 34 degrees
- `C7`: Increase A3 Offset threshold for 3264921_3
- `C8`: Increase transmission power for 3259051_1
- `C9`: Add neighbor relationship between 3214368_4 and 3264921_3
- `C10`: Decrease transmission power for 3264921_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259051_1
- `C12`: Increase transmission power for 3264921_3
- `C13`: Check test server and transmission issues
- `C14`: Decrease A3 Offset threshold for 3264921_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264921_3
- `C16`: Decrease A3 Offset threshold for 3259051_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264921_3
- `C18`: Adjust the azimuth of 3259051_1 by 41 degrees
- `C19`: Lift the tilt angle of 3259051_1 by 3 degrees
- `C20`: Decrease transmission power for 3259051_1
- `C21`: Add neighbor relationship between 3259051_1 and 3264921_3
- `C22`: Increase A3 Offset threshold for 3259051_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.852 | MS1 | 121.4656621525 | 31.1446366538 | 617 | 504990 | -87.84 | 17.71 | 369.89 | 0.14 | 2.13 | 1582 |
| 2024-09-20 22:21:32.421 | MS1 | 121.4656771539 | 31.1446190132 | 617 | 504990 | -88.81 | 17.65 | 387.18 | 0.10 | 2.78 | 1569 |
| 2024-09-20 22:21:33.821 | MS1 | 121.4656587485 | 31.1446289702 | 617 | 504990 | -85.32 | 14.20 | 473.41 | 0.06 | 2.54 | 1570 |
| 2024-09-20 22:21:34.600 | MS1 | 121.4656707908 | 31.1446217011 | 617 | 504990 | -87.31 | 16.67 | 82.23 | 0.02 | 2.03 | 1565 |
| 2024-09-20 22:21:35.389 | MS1 | 121.4656582256 | 31.1446325324 | 617 | 504990 | -91.01 | 17.30 | 65.70 | 0.00 | 2.28 | 1585 |
| 2024-09-20 22:21:36.595 | MS1 | 121.4656750563 | 31.1446307033 | 617 | 504990 | -88.62 | 14.15 | 95.84 | 0.00 | 2.21 | 1565 |
| 2024-09-20 22:21:37.640 | MS1 | 121.4656618952 | 31.1446273786 | 617 | 504990 | -93.57 | 12.36 | 66.81 | 0.08 | 2.39 | 1583 |
| 2024-09-20 22:21:38.321 | MS1 | 121.4656594835 | 31.1446188957 | 617 | 504990 | -89.80 | 8.07 | 87.77 | 0.06 | 2.87 | 1573 |
| 2024-09-20 22:21:39.408 | MS1 | 121.4656765641 | 31.1446238057 | 617 | 504990 | -91.23 | 7.41 | 70.74 | 0.09 | 2.25 | 1574 |
| 2024-09-20 22:21:40.776 | MS1 | 121.4656688467 | 31.1446308163 | 617 | 504990 | -91.61 | 8.40 | 411.98 | 0.11 | 2.35 | 1574 |
| 2024-09-20 22:21:41.754 | MS1 | 121.4656727779 | 31.1446379119 | 617 | 504990 | -90.40 | 12.94 | 412.50 | 0.10 | 2.24 | 1561 |
| 2024-09-20 22:21:42.356 | MS1 | 121.4656628617 | 31.1446284613 | 617 | 504990 | -91.94 | 10.36 | 363.12 | 0.16 | 2.28 | 1596 |

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
| 3214368 | 4 | 121.4642149328 | 31.1477721107 | 335 | 11 | 12 | 19.1 | TDD | 375 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3259051 | 1 | 121.4747211324 | 31.1532005928 | 181 | 1 | 10 | 47.4 | TDD | 617 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3264921 | 3 | 121.4654310931 | 31.1473310294 | 142 | 11 | 6 | 45.1 | TDD | 519 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3268386 | 2 | 121.4699812493 | 31.1443815287 | 32 | 11 | 3 | 48.9 | TDD | 546 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.190 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.206 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.334 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.334 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.070 | NREventA3 | measId:2;ServCellPCI:613;Se... |
| 2024-09-20 22:21:38.310 | NRHandoverAttempt | SourcePCI:613;SourceNR-ARFC... |
| 2024-09-20 22:21:38.344 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.359 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.509 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.509 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259051 | 1 | 84.9757 | 77.6031 | -117.7357 | 8.1533 | 81.2253 | 0.0147 | 0.0001 |
| 2024_09_20 22:00 | 3268386 | 2 | 11.6023 | 7.3391 | -115.8005 | 12.4819 | 196.4944 | 0.0182 | 0.0163 |
| 2024_09_20 22:00 | 3264921 | 3 | 12.4751 | 15.1284 | -116.1117 | 6.4581 | 195.2418 | 0.0059 | 0.0032 |
| 2024_09_20 22:00 | 3214368 | 4 | 8.3582 | 6.0881 | -115.0267 | 11.8549 | 100.5972 | 0.0105 | 0.0076 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414988_9CB9A800 | 504990 | 617 | -87.4 | 504990 | 519 | -88.1 | 504990 | 375 | -101.7 | 504990 | 546 |
| MR_1774414988_DFE853AB | 504990 | 617 | -86.8 | 504990 | 519 | -86.1 | 504990 | 375 | -100.7 | 504990 | 546 |
| MR_1774414988_876C7A24 | 504990 | 617 | -86.1 | 504990 | 519 | -88.7 | 504990 | 375 | -100.3 | 504990 | 546 |
| MR_1774414988_AB75E35B | 504990 | 617 | -87.4 | 504990 | 519 | -87.6 | 504990 | 375 | -102.4 | 504990 | 546 |
| MR_1774414988_649C9E2A | 504990 | 617 | -86.2 | 504990 | 519 | -88.9 | 504990 | 375 | -102.2 | 504990 | 546 |
| MR_1774414988_C34F1AA7 | 504990 | 617 | -87.9 | 504990 | 519 | -88.2 | 504990 | 375 | -100.5 | 504990 | 546 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1373: `abdcb0e4-a5c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `abdcb0e4-a5cc-4fef-ba4f-d5c52958f247` |
| Tag | **multiple-answer** |
| 정답 | **C6|C9|C10|C19** |
| C6 의미 | Press down the tilt angle  of 3238125_4 by 5 degrees |
| C9 의미 | Increase A3 Offset threshold for 3252989_2 |
| C10 의미 | Increase A3 Offset threshold for 3238125_4 |
| C19 의미 | Decrease transmission power for 3238125_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1373] topology](images/train_1373.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3252989_2
- `C2`: Press down the tilt angle of 3252989_2 by 3 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252989_2
- `C4`: Decrease A3 Offset threshold for 3238125_4
- `C5`: Check test server and transmission issues
- `C6`: Press down the tilt angle  of 3238125_4 by 5 degrees **← 정답**
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252989_2
- `C8`: Adjust the azimuth of 3252989_2 by 50 degrees
- `C9`: Increase A3 Offset threshold for 3252989_2 **← 정답**
- `C10`: Increase A3 Offset threshold for 3238125_4 **← 정답**
- `C11`: Lift the tilt angle  of 3238125_4 by 5 degrees
- `C12`: Increase transmission power for 3238125_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238125_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238125_4
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Lift the tilt angle of 3252989_2 by 3 degrees
- `C17`: Decrease A3 Offset threshold for 3252989_2
- `C18`: Add neighbor relationship between 3233014_1 and 3238125_4
- `C19`: Decrease transmission power for 3238125_4 **← 정답**
- `C20`: Add neighbor relationship between 3252989_2 and 3238125_4
- `C21`: Adjust the azimuth of 3238125_4 by 7 degrees
- `C22`: Decrease transmission power for 3252989_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.626 | MS1 | 121.4656694203 | 31.1446221415 | 261 | 504990 | -78.03 | 16.89 | 454.19 | 0.14 | 2.49 | 1587 |
| 2024-09-20 22:21:32.309 | MS1 | 121.4656684930 | 31.1446256291 | 261 | 504990 | -78.54 | 17.10 | 299.50 | 0.07 | 2.23 | 1594 |
| 2024-09-20 22:21:33.319 | MS1 | 121.4656778005 | 31.1446324297 | 261 | 504990 | -75.51 | 14.11 | 422.98 | 0.02 | 2.87 | 1574 |
| 2024-09-20 22:21:34.853 | MS1 | 121.4656700591 | 31.1446276206 | 727 | 504990 | -82.10 | 1.55 | 65.81 | 0.09 | 1.09 | 1577 |
| 2024-09-20 22:21:35.131 | MS1 | 121.4656745311 | 31.1446312329 | 727 | 504990 | -81.54 | 3.88 | 74.40 | 0.16 | 1.20 | 1594 |
| 2024-09-20 22:21:36.530 | MS1 | 121.4656775282 | 31.1446253010 | 261 | 504990 | -84.38 | 2.61 | 37.56 | 0.19 | 1.45 | 1592 |
| 2024-09-20 22:21:37.267 | MS1 | 121.4656606770 | 31.1446367838 | 261 | 504990 | -80.45 | 4.18 | 46.29 | 0.09 | 1.16 | 1578 |
| 2024-09-20 22:21:38.135 | MS1 | 121.4656623917 | 31.1446298868 | 727 | 504990 | -85.13 | 1.49 | 47.37 | 0.02 | 1.40 | 1600 |
| 2024-09-20 22:21:39.742 | MS1 | 121.4656618095 | 31.1446284400 | 727 | 504990 | -88.02 | 4.91 | 47.47 | 0.08 | 1.41 | 1573 |
| 2024-09-20 22:21:40.399 | MS1 | 121.4656721095 | 31.1446378201 | 727 | 504990 | -77.22 | 16.08 | 405.35 | 0.01 | 2.31 | 1578 |
| 2024-09-20 22:21:41.307 | MS1 | 121.4656722702 | 31.1446265658 | 727 | 504990 | -84.90 | 17.09 | 521.51 | 0.08 | 2.59 | 1569 |
| 2024-09-20 22:21:42.362 | MS1 | 121.4656753840 | 31.1446261364 | 727 | 504990 | -81.60 | 16.54 | 315.95 | 0.15 | 2.49 | 1600 |

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
| 3216166 | 3 | 121.4754456366 | 31.1486225684 | 134 | 10 | 0 | 22.9 | TDD | 677 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3233014 | 1 | 121.4743847748 | 31.1463030773 | 105 | 5 | 11 | 28.6 | TDD | 803 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3238125 | 4 | 121.4679550501 | 31.1509305670 | 204 | 4 | 10 | 16.5 | TDD | 1007 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3240482 | 5 | 121.4675567648 | 31.1478882697 | 332 | 6 | 1 | 29.4 | TDD | 727 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3252989 | 2 | 121.4675997443 | 31.1505382026 | 146 | 2 | 6 | 16.9 | TDD | 261 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.552 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.571 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.681 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.681 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.408 | NREventA3 | measId:2;ServCellPCI:149;Se... |
| 2024-09-20 22:21:34.648 | NRHandoverAttempt | SourcePCI:149;SourceNR-ARFC... |
| 2024-09-20 22:21:34.688 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.703 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.837 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.837 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.408 | NREventA3 | measId:2;ServCellPCI:247;Se... |
| 2024-09-20 22:21:36.648 | NRHandoverAttempt | SourcePCI:247;SourceNR-ARFC... |
| 2024-09-20 22:21:36.688 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.698 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:36.828 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.828 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.408 | NREventA3 | measId:2;ServCellPCI:149;Se... |
| 2024-09-20 22:21:38.648 | NRHandoverAttempt | SourcePCI:149;SourceNR-ARFC... |
| 2024-09-20 22:21:38.682 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.692 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.799 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.799 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233014 | 1 | 7.2433 | 16.9624 | -114.2054 | 12.8100 | 162.2595 | 0.0171 | 0.0028 |
| 2024_09_20 22:00 | 3252989 | 2 | 18.5789 | 5.4440 | -114.9644 | 18.6343 | 165.8826 | 0.0093 | 0.0080 |
| 2024_09_20 22:00 | 3216166 | 3 | 17.6650 | 5.0301 | -117.6708 | 7.9073 | 193.4831 | 0.0104 | 0.0038 |
| 2024_09_20 22:00 | 3238125 | 4 | 12.5471 | 14.4994 | -117.6869 | 8.4714 | 191.3274 | 0.0080 | 0.0037 |
| 2024_09_20 22:00 | 3240482 | 5 | 5.5552 | 15.9167 | -116.8926 | 19.6703 | 161.0201 | 0.0158 | 0.0157 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413528_54AB5723 | 504990 | 727 | -82.2 | 504990 | 261 | -82.0 | 504990 | 1007 | -82.7 | 504990 | 803 |
| MR_1774413528_C587AEFB | 504990 | 261 | -84.0 | 504990 | 727 | -79.9 | 504990 | 1007 | -81.2 | 504990 | 803 |
| MR_1774413528_DB811EE6 | 504990 | 261 | -82.2 | 504990 | 727 | -82.6 | 504990 | 1007 | -83.0 | 504990 | 803 |
| MR_1774413528_DF4047CD | 504990 | 261 | -82.7 | 504990 | 727 | -81.7 | 504990 | 1007 | -81.3 | 504990 | 803 |
| MR_1774413528_F9C80FEF | 504990 | 727 | -80.4 | 504990 | 261 | -80.1 | 504990 | 1007 | -81.1 | 504990 | 803 |
| MR_1774413528_0713BD52 | 504990 | 727 | -81.3 | 504990 | 261 | -82.4 | 504990 | 1007 | -80.0 | 504990 | 803 |
| MR_1774413528_E359EC66 | 504990 | 727 | -82.7 | 504990 | 261 | -81.4 | 504990 | 1007 | -82.9 | 504990 | 803 |
| MR_1774413528_B25D094F | 504990 | 261 | -82.6 | 504990 | 727 | -83.3 | 504990 | 1007 | -80.9 | 504990 | 803 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1374: `8f4c1113-11c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8f4c1113-11c0-4e54-b2fd-0fdd61220ac7` |
| Tag | **multiple-answer** |
| 정답 | **C3|C19** |
| C3 의미 | Press down the tilt angle  of 3246635_1 by 2 degrees |
| C19 의미 | Decrease transmission power for 3246635_1 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1374] topology](images/train_1374.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3262685_3
- `C2`: Adjust the azimuth of 3246635_1 by 7 degrees
- `C3`: Press down the tilt angle  of 3246635_1 by 2 degrees **← 정답**
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246635_1
- `C5`: Add neighbor relationship between 3242259_4 and 3246635_1
- `C6`: Check test server and transmission issues
- `C7`: Lift the tilt angle of 3262685_3 by 6 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262685_3
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Increase transmission power for 3262685_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262685_3
- `C12`: Press down the tilt angle of 3262685_3 by 6 degrees
- `C13`: Decrease transmission power for 3262685_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246635_1
- `C15`: Lift the tilt angle  of 3246635_1 by 2 degrees
- `C16`: Increase transmission power for 3246635_1
- `C17`: Increase A3 Offset threshold for 3246635_1
- `C18`: Adjust the azimuth of 3262685_3 by 7 degrees
- `C19`: Decrease transmission power for 3246635_1 **← 정답**
- `C20`: Add neighbor relationship between 3262685_3 and 3246635_1
- `C21`: Increase A3 Offset threshold for 3262685_3
- `C22`: Decrease A3 Offset threshold for 3246635_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.876 | MS1 | 121.4656763470 | 31.1446190261 | 522 | 504990 | -83.06 | 17.10 | 506.10 | 0.05 | 2.41 | 1591 |
| 2024-09-20 22:21:32.722 | MS1 | 121.4656619498 | 31.1446186515 | 522 | 504990 | -84.06 | 15.11 | 433.00 | 0.15 | 2.06 | 1600 |
| 2024-09-20 22:21:33.760 | MS1 | 121.4656657957 | 31.1446215084 | 522 | 504990 | -81.57 | 12.01 | 566.95 | 0.10 | 2.90 | 1584 |
| 2024-09-20 22:21:34.714 | MS1 | 121.4656620036 | 31.1446373351 | 522 | 504990 | -87.78 | 0.65 | 68.15 | 0.20 | 1.00 | 1560 |
| 2024-09-20 22:21:35.556 | MS1 | 121.4656693819 | 31.1446319182 | 522 | 504990 | -93.28 | 4.00 | 94.94 | 0.03 | 1.28 | 1592 |
| 2024-09-20 22:21:36.705 | MS1 | 121.4656729619 | 31.1446242109 | 522 | 504990 | -86.35 | 3.81 | 80.99 | 0.15 | 1.21 | 1597 |
| 2024-09-20 22:21:37.660 | MS1 | 121.4656617839 | 31.1446325982 | 522 | 504990 | -91.64 | 0.84 | 73.96 | 0.14 | 1.14 | 1589 |
| 2024-09-20 22:21:38.882 | MS1 | 121.4656618772 | 31.1446268314 | 522 | 504990 | -85.31 | 1.24 | 68.75 | 0.10 | 1.49 | 1578 |
| 2024-09-20 22:21:39.704 | MS1 | 121.4656593532 | 31.1446343132 | 522 | 504990 | -94.94 | 2.21 | 44.90 | 0.11 | 1.50 | 1594 |
| 2024-09-20 22:21:40.126 | MS1 | 121.4656660805 | 31.1446203209 | 522 | 504990 | -77.87 | 14.85 | 372.04 | 0.08 | 2.82 | 1582 |
| 2024-09-20 22:21:41.612 | MS1 | 121.4656589170 | 31.1446354877 | 522 | 504990 | -79.21 | 17.29 | 546.03 | 0.13 | 2.68 | 1593 |
| 2024-09-20 22:21:42.670 | MS1 | 121.4656699103 | 31.1446256407 | 522 | 504990 | -83.36 | 12.45 | 453.93 | 0.07 | 2.98 | 1573 |

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
| 3242259 | 4 | 121.4725975207 | 31.1508613502 | 343 | 4 | 11 | 32.2 | TDD | 282 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3246635 | 1 | 121.4752847549 | 31.1476746521 | 257 | 0 | 11 | 35.5 | TDD | 768 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3258248 | 2 | 121.4742551049 | 31.1540125976 | 349 | 8 | 11 | 37.9 | TDD | 201 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3262685 | 3 | 121.4727868068 | 31.1480629733 | 248 | 4 | 9 | 20.5 | TDD | 522 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.216 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.237 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.358 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.358 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246635 | 1 | 16.2326 | 17.7589 | -115.8722 | 13.7985 | 146.5581 | 0.0085 | 0.0112 |
| 2024_09_20 22:00 | 3258248 | 2 | 9.9450 | 6.5763 | -115.2933 | 12.8505 | 123.0272 | 0.0159 | 0.0048 |
| 2024_09_20 22:00 | 3262685 | 3 | 18.3902 | 7.7491 | -108.3230 | 15.1195 | 140.2249 | 0.0161 | 0.0172 |
| 2024_09_20 22:00 | 3242259 | 4 | 18.7023 | 19.6600 | -115.1553 | 14.5936 | 197.3210 | 0.0116 | 0.0122 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414718_9DD440E8 | 504990 | 768 | -86.2 | 504990 | 522 | -88.0 | 504990 | 282 | -89.7 | 504990 | 201 |
| MR_1774414718_E3962ECE | 504990 | 768 | -86.9 | 504990 | 522 | -87.8 | 504990 | 282 | -90.4 | 504990 | 201 |
| MR_1774414718_6A0A6F82 | 504990 | 522 | -88.3 | 504990 | 768 | -89.1 | 504990 | 282 | -89.4 | 504990 | 201 |
| MR_1774414718_70B96B47 | 504990 | 522 | -89.4 | 504990 | 768 | -91.0 | 504990 | 282 | -90.8 | 504990 | 201 |
| MR_1774414718_7C46FD4E | 504990 | 522 | -89.5 | 504990 | 768 | -90.2 | 504990 | 282 | -89.4 | 504990 | 201 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1375: `873b8a92-8da...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `873b8a92-8da0-4a25-b72b-5b05ea4c4219` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease A3 Offset threshold for 3235996_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1375] topology](images/train_1375.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235996_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235996_3
- `C3`: Decrease A3 Offset threshold for 3235996_3 **← 정답**
- `C4`: Increase A3 Offset threshold for 3235996_3
- `C5`: Press down the tilt angle  of 3225571_1 by 10 degrees
- `C6`: Increase A3 Offset threshold for 3225571_1
- `C7`: Lift the tilt angle  of 3225571_1 by 10 degrees
- `C8`: Decrease transmission power for 3225571_1
- `C9`: Lift the tilt angle of 3235996_3 by 3 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Adjust the azimuth of 3235996_3 by 31 degrees
- `C12`: Decrease A3 Offset threshold for 3225571_1
- `C13`: Decrease transmission power for 3235996_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225571_1
- `C15`: Increase transmission power for 3225571_1
- `C16`: Adjust the azimuth of 3225571_1 by 50 degrees
- `C17`: Add neighbor relationship between 3235996_3 and 3225571_1
- `C18`: Add neighbor relationship between 3256755_2 and 3225571_1
- `C19`: Increase transmission power for 3235996_3
- `C20`: Check test server and transmission issues
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225571_1
- `C22`: Press down the tilt angle of 3235996_3 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.384 | MS1 | 121.4656682548 | 31.1446341140 | 260 | 504990 | -81.39 | 12.94 | 491.79 | 0.01 | 2.77 | 1591 |
| 2024-09-20 22:21:32.260 | MS1 | 121.4656613034 | 31.1446347137 | 260 | 504990 | -83.08 | 14.82 | 353.91 | 0.02 | 2.72 | 1580 |
| 2024-09-20 22:21:33.889 | MS1 | 121.4656610867 | 31.1446183807 | 260 | 504990 | -79.50 | 13.96 | 497.30 | 0.11 | 2.98 | 1594 |
| 2024-09-20 22:21:34.724 | MS1 | 121.4656675956 | 31.1446230993 | 260 | 504990 | -85.29 | -2.53 | 55.63 | 0.03 | 1.23 | 1594 |
| 2024-09-20 22:21:35.520 | MS1 | 121.4656730266 | 31.1446182922 | 260 | 504990 | -91.39 | -3.06 | 55.91 | 0.03 | 1.07 | 1599 |
| 2024-09-20 22:21:36.576 | MS1 | 121.4656685416 | 31.1446370922 | 260 | 504990 | -88.00 | -1.62 | 37.46 | 0.15 | 1.38 | 1584 |
| 2024-09-20 22:21:37.772 | MS1 | 121.4656646724 | 31.1446324946 | 260 | 504990 | -90.68 | -1.12 | 30.07 | 0.06 | 1.28 | 1593 |
| 2024-09-20 22:21:38.452 | MS1 | 121.4656696956 | 31.1446201681 | 260 | 504990 | -83.99 | -1.83 | 61.24 | 0.12 | 1.45 | 1600 |
| 2024-09-20 22:21:39.854 | MS1 | 121.4656596444 | 31.1446366854 | 409 | 504990 | -79.98 | 17.00 | 157.31 | 0.16 | 1.04 | 1560 |
| 2024-09-20 22:21:40.125 | MS1 | 121.4656624560 | 31.1446373834 | 409 | 504990 | -83.08 | 16.20 | 445.09 | 0.17 | 2.24 | 1577 |
| 2024-09-20 22:21:41.508 | MS1 | 121.4656602807 | 31.1446247937 | 409 | 504990 | -75.28 | 17.89 | 300.20 | 0.09 | 2.95 | 1569 |
| 2024-09-20 22:21:42.184 | MS1 | 121.4656581411 | 31.1446240676 | 409 | 504990 | -81.07 | 13.34 | 302.92 | 0.04 | 2.66 | 1599 |

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
| 3225571 | 1 | 121.4648570480 | 31.1547775335 | 75 | 10 | 4 | 39.2 | TDD | 409 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3231256 | 4 | 121.4713028611 | 31.1501478391 | 60 | 2 | 7 | 38.3 | TDD | 63 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3235996 | 3 | 121.4747167188 | 31.1552222273 | 247 | 1 | 3 | 42.8 | TDD | 260 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3256755 | 2 | 121.4722749819 | 31.1486476672 | 78 | 10 | 9 | 25.3 | TDD | 890 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.863 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.881 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.999 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.999 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.704 | NREventA3 | measId:2;ServCellPCI:600;Se... |
| 2024-09-20 22:21:37.944 | NRHandoverAttempt | SourcePCI:600;SourceNR-ARFC... |
| 2024-09-20 22:21:37.980 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.991 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.105 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.105 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225571 | 1 | 11.0326 | 18.3877 | -116.1632 | 12.7148 | 178.9304 | 0.0152 | 0.0107 |
| 2024_09_20 22:00 | 3256755 | 2 | 7.6568 | 7.0779 | -117.0125 | 7.4666 | 98.2512 | 0.0003 | 0.0111 |
| 2024_09_20 22:00 | 3235996 | 3 | 15.9345 | 7.4267 | -116.6592 | 10.3311 | 140.2109 | 0.0003 | 0.1383 |
| 2024_09_20 22:00 | 3231256 | 4 | 18.5342 | 18.2821 | -116.0573 | 18.7254 | 81.6237 | 0.0130 | 0.0163 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415209_174F41F4 | 504990 | 409 | -78.4 | 504990 | 260 | -86.6 | 504990 | 890 | -82.7 | 504990 | 63 |
| MR_1774415209_0418F222 | 504990 | 260 | -84.4 | 504990 | 409 | -80.3 | 504990 | 890 | -80.6 | 504990 | 63 |
| MR_1774415209_FFE10FCD | 504990 | 260 | -86.7 | 504990 | 409 | -79.6 | 504990 | 890 | -80.7 | 504990 | 63 |
| MR_1774415209_BD64FB10 | 504990 | 409 | -78.8 | 504990 | 260 | -87.3 | 504990 | 890 | -80.3 | 504990 | 63 |
| MR_1774415209_2B02258B | 504990 | 409 | -80.6 | 504990 | 260 | -86.6 | 504990 | 890 | -79.6 | 504990 | 63 |
| MR_1774415209_19E0F2B5 | 504990 | 260 | -87.1 | 504990 | 409 | -80.6 | 504990 | 890 | -82.5 | 504990 | 63 |
| MR_1774415209_10D8B19A | 504990 | 260 | -86.3 | 504990 | 409 | -79.0 | 504990 | 890 | -83.4 | 504990 | 63 |
| MR_1774415209_F3D8A709 | 504990 | 409 | -77.9 | 504990 | 260 | -85.1 | 504990 | 890 | -80.8 | 504990 | 63 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1376: `36645cba-465...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `36645cba-4655-4a40-be43-218a51290edc` |
| Tag | **multiple-answer** |
| 정답 | **C11|C19** |
| C11 의미 | Increase transmission power for 3235936_1 |
| C19 의미 | Adjust the azimuth of 3235936_1 by 26 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1376] topology](images/train_1376.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3225618_3
- `C2`: Decrease A3 Offset threshold for 3235936_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Lift the tilt angle  of 3225618_3 by 5 degrees
- `C5`: Increase A3 Offset threshold for 3235936_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235936_1
- `C7`: Add neighbor relationship between 3235936_1 and 3225618_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225618_3
- `C9`: Press down the tilt angle  of 3225618_3 by 5 degrees
- `C10`: Lift the tilt angle of 3235936_1 by 10 degrees
- `C11`: Increase transmission power for 3235936_1 **← 정답**
- `C12`: Decrease A3 Offset threshold for 3225618_3
- `C13`: Increase transmission power for 3225618_3
- `C14`: Check test server and transmission issues
- `C15`: Add neighbor relationship between 3244958_2 and 3225618_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235936_1
- `C17`: Decrease transmission power for 3225618_3
- `C18`: Press down the tilt angle of 3235936_1 by 10 degrees
- `C19`: Adjust the azimuth of 3235936_1 by 26 degrees **← 정답**
- `C20`: Decrease transmission power for 3235936_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225618_3
- `C22`: Adjust the azimuth of 3225618_3 by 13 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.604 | MS1 | 121.4656755765 | 31.1446229573 | 208 | 504990 | -86.73 | 16.39 | 567.57 | 0.14 | 2.17 | 1581 |
| 2024-09-20 22:21:32.896 | MS1 | 121.4656607425 | 31.1446221090 | 208 | 504990 | -87.62 | 15.44 | 426.09 | 0.15 | 2.41 | 1566 |
| 2024-09-20 22:21:33.537 | MS1 | 121.4656612384 | 31.1446293685 | 208 | 504990 | -87.78 | 16.08 | 324.94 | 0.08 | 2.91 | 1563 |
| 2024-09-20 22:21:34.944 | MS1 | 121.4656608352 | 31.1446367309 | 208 | 504990 | -104.36 | 0.27 | 26.37 | 0.01 | 1.39 | 1586 |
| 2024-09-20 22:21:35.290 | MS1 | 121.4656723584 | 31.1446223934 | 208 | 504990 | -103.82 | 0.56 | 56.10 | 0.17 | 1.29 | 1574 |
| 2024-09-20 22:21:36.963 | MS1 | 121.4656710852 | 31.1446371733 | 208 | 504990 | -102.83 | -0.38 | 31.27 | 0.17 | 1.47 | 1585 |
| 2024-09-20 22:21:37.969 | MS1 | 121.4656649992 | 31.1446205185 | 208 | 504990 | -102.93 | 1.26 | 77.60 | 0.02 | 1.37 | 1600 |
| 2024-09-20 22:21:38.574 | MS1 | 121.4656777696 | 31.1446350319 | 208 | 504990 | -104.67 | -0.19 | 54.44 | 0.03 | 1.24 | 1584 |
| 2024-09-20 22:21:39.131 | MS1 | 121.4656705187 | 31.1446344012 | 208 | 504990 | -102.40 | 0.42 | 26.73 | 0.03 | 1.44 | 1576 |
| 2024-09-20 22:21:40.496 | MS1 | 121.4656615178 | 31.1446276789 | 208 | 504990 | -85.39 | 17.45 | 534.98 | 0.16 | 2.51 | 1570 |
| 2024-09-20 22:21:41.357 | MS1 | 121.4656632780 | 31.1446213528 | 208 | 504990 | -94.19 | 16.89 | 357.79 | 0.02 | 2.31 | 1595 |
| 2024-09-20 22:21:42.629 | MS1 | 121.4656676499 | 31.1446284127 | 208 | 504990 | -94.34 | 13.86 | 376.00 | 0.10 | 2.58 | 1564 |

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
| 3212221 | 4 | 121.4743229069 | 31.1536271137 | 219 | 0 | 12 | 38.2 | TDD | 557 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3225618 | 3 | 121.4691955916 | 31.1557222834 | 182 | 3 | 9 | 34.2 | TDD | 877 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3235936 | 1 | 121.4693593134 | 31.1464274905 | 267 | 10 | 5 | 25.1 | TDD | 208 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3244958 | 2 | 121.4757698296 | 31.1521090348 | 316 | 12 | 10 | 22.1 | TDD | 794 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.557 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.581 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.713 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.713 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.879 | NREventA2 | measId:1;ServCellPCI:54;Ser... |
| 2024-09-20 22:21:34.990 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235936 | 1 | 5.0851 | 5.6939 | -116.3583 | 11.5541 | 175.0892 | 0.1446 | 0.0043 |
| 2024_09_20 22:00 | 3244958 | 2 | 9.0476 | 11.8266 | -117.9786 | 14.6391 | 184.4495 | 0.0183 | 0.0038 |
| 2024_09_20 22:00 | 3225618 | 3 | 12.4449 | 10.8335 | -114.9433 | 5.4027 | 126.6730 | 0.0015 | 0.0178 |
| 2024_09_20 22:00 | 3212221 | 4 | 17.2562 | 10.9134 | -116.4857 | 13.3085 | 146.6814 | 0.0166 | 0.0007 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414462_5ED5D70F | 504990 | 208 | -106.3 | 504990 | 877 | -111.7 | 504990 | 794 | -114.5 | 504990 | 557 |
| MR_1774414462_AB11952C | 504990 | 208 | -105.0 | 504990 | 877 | -112.7 | 504990 | 794 | -117.2 | 504990 | 557 |
| MR_1774414462_899F5C2B | 504990 | 208 | -103.6 | 504990 | 877 | -112.0 | 504990 | 794 | -117.1 | 504990 | 557 |
| MR_1774414462_54B5A453 | 504990 | 208 | -105.1 | 504990 | 877 | -112.6 | 504990 | 794 | -117.3 | 504990 | 557 |
| MR_1774414462_259C53BD | 504990 | 208 | -103.9 | 504990 | 877 | -112.2 | 504990 | 794 | -115.3 | 504990 | 557 |
| MR_1774414462_BC93D6FE | 504990 | 208 | -102.6 | 504990 | 877 | -112.4 | 504990 | 794 | -114.6 | 504990 | 557 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1377: `3bdd3480-662...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3bdd3480-6622-4e66-88d6-952b18118488` |
| Tag | **multiple-answer** |
| 정답 | **C13|C21** |
| C13 의미 | Decrease transmission power for 3240223_1 |
| C21 의미 | Press down the tilt angle  of 3240223_1 by 6 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1377] topology](images/train_1377.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3241552_4 by 2 degrees
- `C2`: Adjust the azimuth of 3241552_4 by 1 degrees
- `C3`: Lift the tilt angle of 3241552_4 by 2 degrees
- `C4`: Adjust the azimuth of 3240223_1 by 4 degrees
- `C5`: Decrease A3 Offset threshold for 3240223_1
- `C6`: Check test server and transmission issues
- `C7`: Decrease A3 Offset threshold for 3241552_4
- `C8`: Lift the tilt angle  of 3240223_1 by 6 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240223_1
- `C10`: Increase A3 Offset threshold for 3241552_4
- `C11`: Increase A3 Offset threshold for 3240223_1
- `C12`: Increase transmission power for 3240223_1
- `C13`: Decrease transmission power for 3240223_1 **← 정답**
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase transmission power for 3241552_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241552_4
- `C17`: Decrease transmission power for 3241552_4
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240223_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241552_4
- `C20`: Add neighbor relationship between 3241552_4 and 3240223_1
- `C21`: Press down the tilt angle  of 3240223_1 by 6 degrees **← 정답**
- `C22`: Add neighbor relationship between 3242557_2 and 3240223_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.104 | MS1 | 121.4656742756 | 31.1446186137 | 911 | 504990 | -78.44 | 16.70 | 409.04 | 0.09 | 2.74 | 1575 |
| 2024-09-20 22:21:32.887 | MS1 | 121.4656586083 | 31.1446199709 | 911 | 504990 | -76.56 | 13.78 | 341.85 | 0.18 | 2.62 | 1600 |
| 2024-09-20 22:21:33.432 | MS1 | 121.4656602431 | 31.1446189706 | 911 | 504990 | -79.34 | 14.79 | 579.11 | 0.09 | 2.42 | 1600 |
| 2024-09-20 22:21:34.344 | MS1 | 121.4656746534 | 31.1446312212 | 911 | 504990 | -91.37 | 0.27 | 46.80 | 0.03 | 1.16 | 1576 |
| 2024-09-20 22:21:35.117 | MS1 | 121.4656688110 | 31.1446203206 | 911 | 504990 | -89.02 | 3.95 | 52.76 | 0.19 | 1.34 | 1564 |
| 2024-09-20 22:21:36.468 | MS1 | 121.4656649605 | 31.1446355942 | 911 | 504990 | -89.83 | 0.90 | 54.84 | 0.14 | 1.31 | 1591 |
| 2024-09-20 22:21:37.489 | MS1 | 121.4656676291 | 31.1446341875 | 911 | 504990 | -93.44 | 0.73 | 80.82 | 0.17 | 1.41 | 1584 |
| 2024-09-20 22:21:38.115 | MS1 | 121.4656687915 | 31.1446214990 | 911 | 504990 | -93.87 | 3.52 | 40.36 | 0.03 | 1.49 | 1571 |
| 2024-09-20 22:21:39.598 | MS1 | 121.4656688254 | 31.1446289866 | 911 | 504990 | -86.01 | 1.59 | 46.78 | 0.09 | 1.17 | 1598 |
| 2024-09-20 22:21:40.772 | MS1 | 121.4656646459 | 31.1446301564 | 911 | 504990 | -76.50 | 15.52 | 419.06 | 0.04 | 2.19 | 1589 |
| 2024-09-20 22:21:41.309 | MS1 | 121.4656711691 | 31.1446254954 | 911 | 504990 | -81.88 | 14.97 | 384.72 | 0.06 | 3.00 | 1585 |
| 2024-09-20 22:21:42.482 | MS1 | 121.4656701212 | 31.1446344824 | 911 | 504990 | -82.81 | 15.13 | 521.20 | 0.12 | 2.91 | 1576 |

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
| 3224224 | 3 | 121.4710549822 | 31.1530440961 | 58 | 11 | 2 | 42.9 | TDD | 366 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3240223 | 1 | 121.4721288487 | 31.1486130080 | 238 | 4 | 10 | 20.0 | TDD | 624 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3241552 | 4 | 121.4718177800 | 31.1494486071 | 226 | 1 | 5 | 19.9 | TDD | 911 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3242557 | 2 | 121.4700503844 | 31.1559295873 | 268 | 9 | 8 | 16.0 | TDD | 969 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.577 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.593 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.732 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.732 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240223 | 1 | 8.4863 | 16.9635 | -115.3908 | 19.3980 | 145.8680 | 0.0113 | 0.0165 |
| 2024_09_20 22:00 | 3242557 | 2 | 19.8175 | 19.8640 | -117.2265 | 13.0665 | 142.9943 | 0.0095 | 0.0143 |
| 2024_09_20 22:00 | 3224224 | 3 | 14.1252 | 11.6051 | -116.2668 | 15.8892 | 133.4023 | 0.0166 | 0.0010 |
| 2024_09_20 22:00 | 3241552 | 4 | 19.4222 | 13.5173 | -109.0719 | 11.0554 | 198.6031 | 0.0198 | 0.0034 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414406_3054C44B | 504990 | 911 | -90.8 | 504990 | 624 | -88.7 | 504990 | 969 | -92.7 | 504990 | 366 |
| MR_1774414406_25971A63 | 504990 | 911 | -91.0 | 504990 | 624 | -91.4 | 504990 | 969 | -93.6 | 504990 | 366 |
| MR_1774414406_E9856267 | 504990 | 911 | -89.7 | 504990 | 624 | -91.1 | 504990 | 969 | -94.9 | 504990 | 366 |
| MR_1774414406_191E250D | 504990 | 624 | -92.3 | 504990 | 911 | -87.9 | 504990 | 969 | -93.5 | 504990 | 366 |
| MR_1774414406_79A4B6A2 | 504990 | 624 | -92.4 | 504990 | 911 | -90.4 | 504990 | 969 | -93.1 | 504990 | 366 |
| MR_1774414406_326F00F3 | 504990 | 624 | -90.0 | 504990 | 911 | -89.0 | 504990 | 969 | -94.4 | 504990 | 366 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1378: `e250f489-837...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e250f489-8370-4322-97f0-94d54dc22023` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245898_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1378] topology](images/train_1378.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3245898_3
- `C2`: Increase A3 Offset threshold for 3279940_1
- `C3`: Add neighbor relationship between 3245898_3 and 3279940_1
- `C4`: Increase transmission power for 3245898_3
- `C5`: Adjust the azimuth of 3279940_1 by 36 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245898_3 **← 정답**
- `C7`: Press down the tilt angle of 3245898_3 by 1 degrees
- `C8`: Lift the tilt angle of 3245898_3 by 1 degrees
- `C9`: Add neighbor relationship between 3261213_10 and 3279940_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279940_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279940_1
- `C12`: Check test server and transmission issues
- `C13`: Increase transmission power for 3279940_1
- `C14`: Decrease A3 Offset threshold for 3245898_3
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease transmission power for 3245898_3
- `C17`: Press down the tilt angle  of 3279940_1 by 1 degrees
- `C18`: Lift the tilt angle  of 3279940_1 by 1 degrees
- `C19`: Adjust the azimuth of 3245898_3 by 9 degrees
- `C20`: Decrease transmission power for 3279940_1
- `C21`: Decrease A3 Offset threshold for 3279940_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245898_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.526 | MS1 | 121.4656753962 | 31.1446234087 | 4 | 504990 | -94.70 | 12.17 | 515.27 | 0.02 | 2.18 | 1561 |
| 2024-09-20 22:21:32.358 | MS1 | 121.4656726045 | 31.1446288212 | 280 | 504990 | -93.39 | 11.25 | 439.79 | 0.15 | 2.27 | 1584 |
| 2024-09-20 22:21:33.924 | MS1 | 121.4656598137 | 31.1446303239 | 625 | 504990 | -93.85 | 13.62 | 441.68 | 0.00 | 2.79 | 1596 |
| 2024-09-20 22:21:34.586 | MS1 | 121.4656647596 | 31.1446201973 | 197 | 152650 | -87.20 | 7.77 | 77.41 | 0.16 | 1.96 | 977 |
| 2024-09-20 22:21:35.994 | MS1 | 121.4656709561 | 31.1446268697 | 624 | 152650 | -89.65 | 3.78 | 93.50 | 0.12 | 1.63 | 940 |
| 2024-09-20 22:21:36.624 | MS1 | 121.4656645371 | 31.1446276532 | 809 | 152650 | -91.26 | 3.81 | 101.15 | 0.01 | 1.56 | 963 |
| 2024-09-20 22:21:37.952 | MS1 | 121.4656727863 | 31.1446362402 | 1004 | 152650 | -87.32 | 2.28 | 79.08 | 0.05 | 1.56 | 904 |
| 2024-09-20 22:21:38.699 | MS1 | 121.4656629756 | 31.1446359911 | 197 | 152650 | -89.88 | 2.58 | 70.38 | 0.02 | 1.57 | 941 |
| 2024-09-20 22:21:39.147 | MS1 | 121.4656591756 | 31.1446309452 | 624 | 152650 | -95.13 | 5.79 | 97.79 | 0.19 | 1.69 | 916 |
| 2024-09-20 22:21:40.862 | MS1 | 121.4656750707 | 31.1446338811 | 809 | 152650 | -93.82 | 6.84 | 58.11 | 0.15 | 2.95 | 1580 |
| 2024-09-20 22:21:41.491 | MS1 | 121.4656756465 | 31.1446337550 | 1004 | 152650 | -92.08 | 5.32 | 78.02 | 0.05 | 2.02 | 1582 |
| 2024-09-20 22:21:42.206 | MS1 | 121.4656770940 | 31.1446197839 | 197 | 152650 | -96.04 | 3.56 | 68.67 | 0.03 | 2.10 | 1560 |

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
| 3214208 | 11 | 121.4741001051 | 31.1516761404 | 68 | 10 | 5 | 10.9 | FDD | 1004 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3225691 | 5 | 121.4685429494 | 31.1528314524 | 240 | 10 | 9 | 10.3 | TDD | 625 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3228211 | 2 | 121.4675034130 | 31.1441614294 | 272 | 7 | 5 | 13.1 | TDD | 321 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3232752 | 4 | 121.4700554345 | 31.1500348464 | 6 | 4 | 5 | 2.4 | TDD | 524 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3232853 | 7 | 121.4666968181 | 31.1492349328 | 9 | 6 | 7 | 5.3 | FDD | 962 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3233189 | 8 | 121.4751779428 | 31.1497324248 | 83 | 4 | 5 | 3.6 | FDD | 197 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3238684 | 12 | 121.4683814440 | 31.1549442431 | 244 | 0 | 0 | 3.5 | FDD | 624 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3245898 | 3 | 121.4719432313 | 31.1533166130 | 203 | 1 | 6 | 7.0 | TDD | 4 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3247307 | 9 | 121.4758099122 | 31.1545796799 | 93 | 2 | 4 | 11.8 | FDD | 805 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3251013 | 13 | 121.4688350130 | 31.1508377586 | 242 | 3 | 3 | 17.0 | FDD | 180 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3253208 | 6 | 121.4645228775 | 31.1535027381 | 199 | 8 | 7 | 7.3 | TDD | 280 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3261213 | 10 | 121.4643889713 | 31.1492164482 | 93 | 4 | 5 | 18.9 | FDD | 809 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3279940 | 1 | 121.4683009884 | 31.1475282988 | 182 | 1 | 0 | 0.4 | TDD | 33 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.117 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.140 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.285 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.285 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.964 | NREventA2 | measId:1;ServCellPCI:796;Se... |
| 2024-09-20 22:21:35.086 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.354 | NREventA5 | measId:3;ServCellPCI:796;Se... |
| 2024-09-20 22:21:35.415 | NRHandoverAttempt | SourcePCI:796;SourceNR-ARFC... |
| 2024-09-20 22:21:35.456 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.469 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.617 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.617 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279940 | 1 | 11.3931 | 16.1781 | -117.1629 | 9.9615 | 138.2037 | 0.0052 | 0.0047 |
| 2024_09_20 22:00 | 3228211 | 2 | 16.0087 | 18.4904 | -116.4656 | 11.7807 | 154.0116 | 0.0032 | 0.0164 |
| 2024_09_20 22:00 | 3245898 | 3 | 14.4365 | 17.5189 | -117.0373 | 19.1469 | 185.1174 | 0.0066 | 0.0146 |
| 2024_09_20 22:00 | 3232752 | 4 | 19.7220 | 5.9487 | -115.1203 | 15.9749 | 184.5268 | 0.0077 | 0.0073 |
| 2024_09_20 22:00 | 3225691 | 5 | 9.6323 | 19.6565 | -115.0303 | 12.5592 | 154.8632 | 0.0097 | 0.0166 |
| 2024_09_20 22:00 | 3253208 | 6 | 11.5012 | 9.6427 | -117.9180 | 5.7565 | 144.0488 | 0.0149 | 0.0165 |
| 2024_09_20 22:00 | 3232853 | 7 | 11.7911 | 8.3477 | -117.2399 | 4.5672 | 59.8905 | 0.0121 | 0.0127 |
| 2024_09_20 22:00 | 3233189 | 8 | 9.7223 | 7.8011 | -116.9905 | 3.4084 | 23.0546 | 0.0074 | 0.0133 |
| 2024_09_20 22:00 | 3247307 | 9 | 8.6489 | 13.7926 | -114.6930 | 3.9321 | 30.7440 | 0.0081 | 0.0129 |
| 2024_09_20 22:00 | 3261213 | 10 | 16.6744 | 5.7843 | -114.3902 | 3.3096 | 52.9969 | 0.0182 | 0.0182 |
| 2024_09_20 22:00 | 3214208 | 11 | 11.9651 | 6.2294 | -115.5999 | 4.1041 | 39.0959 | 0.0119 | 0.0187 |
| 2024_09_20 22:00 | 3238684 | 12 | 10.0943 | 6.1489 | -116.7554 | 3.6600 | 27.6305 | 0.0121 | 0.0041 |
| 2024_09_20 22:00 | 3251013 | 13 | 16.8208 | 11.4357 | -115.0537 | 3.8121 | 25.3344 | 0.0176 | 0.0177 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413212_4AF04C3D | 504990 | 625 | -94.0 | 504990 | 33 | -94.7 | 504990 | 524 | -96.5 | 504990 | 321 |
| MR_1774413212_57FB8EE3 | 504990 | 625 | -91.9 | 504990 | 33 | -92.8 | 504990 | 524 | -96.3 | 504990 | 321 |
| MR_1774413212_D7E7C600 | 152650 | 197 | -88.7 | 152650 | 962 | -93.5 | 152650 | 805 | -93.1 | 152650 | 180 |
| MR_1774413212_D8F428C2 | 504990 | 625 | -95.4 | 504990 | 33 | -92.9 | 504990 | 524 | -94.8 | 504990 | 321 |
| MR_1774413212_9709CA86 | 152650 | 197 | -87.2 | 152650 | 962 | -93.6 | 152650 | 805 | -95.3 | 152650 | 180 |
| MR_1774413212_66D2F646 | 504990 | 625 | -94.6 | 504990 | 33 | -94.0 | 504990 | 524 | -97.3 | 504990 | 321 |
| MR_1774413212_80228003 | 152650 | 197 | -85.7 | 152650 | 962 | -92.1 | 152650 | 805 | -96.5 | 152650 | 180 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1379: `7bc02551-e84...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7bc02551-e848-4a3d-91c2-aacc7a413514` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease A3 Offset threshold for 3277640_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1379] topology](images/train_1379.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3277640_3 by 4 degrees
- `C2`: Adjust the azimuth of 3277640_3 by 50 degrees
- `C3`: Press down the tilt angle  of 3259607_4 by 10 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259607_4
- `C5`: Adjust the azimuth of 3259607_4 by 50 degrees
- `C6`: Check test server and transmission issues
- `C7`: Decrease transmission power for 3259607_4
- `C8`: Increase A3 Offset threshold for 3259607_4
- `C9`: Lift the tilt angle  of 3259607_4 by 10 degrees
- `C10`: Add neighbor relationship between 3261184_1 and 3259607_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277640_3
- `C12`: Increase transmission power for 3259607_4
- `C13`: Increase transmission power for 3277640_3
- `C14`: Increase A3 Offset threshold for 3277640_3
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Add neighbor relationship between 3277640_3 and 3259607_4
- `C17`: Decrease transmission power for 3277640_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259607_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277640_3
- `C20`: Press down the tilt angle of 3277640_3 by 4 degrees
- `C21`: Decrease A3 Offset threshold for 3277640_3 **← 정답**
- `C22`: Decrease A3 Offset threshold for 3259607_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.243 | MS1 | 121.4656759693 | 31.1446213726 | 325 | 504990 | -83.93 | 16.17 | 355.90 | 0.07 | 2.73 | 1570 |
| 2024-09-20 22:21:32.428 | MS1 | 121.4656675456 | 31.1446354010 | 325 | 504990 | -84.44 | 14.87 | 374.55 | 0.02 | 2.78 | 1595 |
| 2024-09-20 22:21:33.128 | MS1 | 121.4656712049 | 31.1446365049 | 325 | 504990 | -83.82 | 12.54 | 548.82 | 0.18 | 2.96 | 1592 |
| 2024-09-20 22:21:34.727 | MS1 | 121.4656755677 | 31.1446360581 | 325 | 504990 | -87.43 | -1.55 | 73.43 | 0.19 | 1.15 | 1599 |
| 2024-09-20 22:21:35.472 | MS1 | 121.4656601386 | 31.1446195842 | 325 | 504990 | -87.15 | -3.43 | 59.37 | 0.02 | 1.48 | 1573 |
| 2024-09-20 22:21:36.266 | MS1 | 121.4656618489 | 31.1446266825 | 325 | 504990 | -88.29 | -2.43 | 38.18 | 0.08 | 1.47 | 1576 |
| 2024-09-20 22:21:37.811 | MS1 | 121.4656630598 | 31.1446289898 | 325 | 504990 | -83.91 | -0.39 | 45.13 | 0.16 | 1.05 | 1581 |
| 2024-09-20 22:21:38.201 | MS1 | 121.4656745421 | 31.1446341138 | 325 | 504990 | -92.14 | -0.34 | 69.95 | 0.01 | 1.49 | 1598 |
| 2024-09-20 22:21:39.756 | MS1 | 121.4656739945 | 31.1446337339 | 559 | 504990 | -83.34 | 14.03 | 265.04 | 0.04 | 1.32 | 1595 |
| 2024-09-20 22:21:40.372 | MS1 | 121.4656691290 | 31.1446345671 | 559 | 504990 | -82.44 | 12.93 | 577.94 | 0.18 | 2.64 | 1589 |
| 2024-09-20 22:21:41.527 | MS1 | 121.4656582395 | 31.1446330838 | 559 | 504990 | -76.17 | 17.50 | 329.87 | 0.06 | 2.10 | 1593 |
| 2024-09-20 22:21:42.807 | MS1 | 121.4656695946 | 31.1446200776 | 559 | 504990 | -81.30 | 14.44 | 586.71 | 0.19 | 2.07 | 1574 |

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
| 3259607 | 4 | 121.4640306440 | 31.1462544367 | 338 | 9 | 8 | 21.8 | TDD | 559 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3261184 | 1 | 121.4752824527 | 31.1492138362 | 63 | 5 | 3 | 28.7 | TDD | 840 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3277558 | 2 | 121.4663953523 | 31.1553834480 | 99 | 5 | 10 | 26.7 | TDD | 10 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3277640 | 3 | 121.4732922237 | 31.1446643843 | 340 | 1 | 0 | 34.4 | TDD | 325 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.775 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.790 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.935 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.935 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.610 | NREventA3 | measId:2;ServCellPCI:325;Se... |
| 2024-09-20 22:21:37.850 | NRHandoverAttempt | SourcePCI:325;SourceNR-ARFC... |
| 2024-09-20 22:21:37.897 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.909 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.010 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.010 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261184 | 1 | 7.9189 | 5.7414 | -117.0837 | 11.9166 | 98.3650 | 0.0163 | 0.0023 |
| 2024_09_20 22:00 | 3277558 | 2 | 19.7822 | 13.8555 | -116.5158 | 16.2427 | 113.4877 | 0.0150 | 0.0041 |
| 2024_09_20 22:00 | 3277640 | 3 | 19.5081 | 11.7805 | -116.9641 | 16.0887 | 97.5662 | 0.0190 | 0.1776 |
| 2024_09_20 22:00 | 3259607 | 4 | 5.2532 | 13.3894 | -115.8038 | 12.8080 | 184.5419 | 0.0121 | 0.0055 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414514_6835DA1D | 504990 | 325 | -88.9 | 504990 | 559 | -81.4 | 504990 | 840 | -90.6 | 504990 | 10 |
| MR_1774414514_D95F5E14 | 504990 | 559 | -82.0 | 504990 | 325 | -86.4 | 504990 | 840 | -90.7 | 504990 | 10 |
| MR_1774414514_57505B34 | 504990 | 559 | -82.6 | 504990 | 325 | -87.3 | 504990 | 840 | -90.2 | 504990 | 10 |
| MR_1774414514_2E45FC18 | 504990 | 559 | -82.1 | 504990 | 325 | -88.2 | 504990 | 840 | -92.9 | 504990 | 10 |
| MR_1774414514_9E9CAD9D | 504990 | 559 | -82.7 | 504990 | 325 | -88.6 | 504990 | 840 | -91.8 | 504990 | 10 |
| MR_1774414514_7051281A | 504990 | 559 | -81.0 | 504990 | 325 | -86.7 | 504990 | 840 | -91.8 | 504990 | 10 |
| MR_1774414514_69664829 | 504990 | 325 | -85.9 | 504990 | 559 | -83.3 | 504990 | 840 | -90.4 | 504990 | 10 |

> *... 2개 열 생략 (전체 14열)*

---
