# Track A 문제 분석 — test[90]~test[99]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[90] ~ test[99] (10개)

## 목차

1. [문제 90: `1a103abd-72c...`](#90) — single-answer
2. [문제 91: `c78acddb-e53...`](#91) — single-answer
3. [문제 92: `0aa7797b-556...`](#92) — single-answer
4. [문제 93: `e666e92e-aec...`](#93) — single-answer
5. [문제 94: `47894def-46c...`](#94) — multiple-answer
6. [문제 95: `990a6082-86d...`](#95) — single-answer
7. [문제 96: `02637243-f59...`](#96) — multiple-answer
8. [문제 97: `6101be3f-9fa...`](#97) — single-answer
9. [문제 98: `fb4d6986-5f5...`](#98) — single-answer
10. [문제 99: `5538b826-d1b...`](#99) — single-answer

---

### 문제 90: `1a103abd-72c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1a103abd-72cf-4f63-8a7d-c687da867d42` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[90] topology](images/test_0090.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3236929_12 and 3215804_3
- `C2`: Press down the tilt angle of 3249972_2 by 0 degrees
- `C3`: Press down the tilt angle  of 3215804_3 by 4 degrees
- `C4`: Check test server and transmission issues
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249972_2
- `C6`: Lift the tilt angle of 3249972_2 by 0 degrees
- `C7`: Increase transmission power for 3249972_2
- `C8`: Increase A3 Offset threshold for 3215804_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249972_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Adjust the azimuth of 3215804_3 by 33 degrees
- `C12`: Increase transmission power for 3215804_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215804_3
- `C14`: Decrease transmission power for 3215804_3
- `C15`: Decrease A3 Offset threshold for 3215804_3
- `C16`: Lift the tilt angle  of 3215804_3 by 4 degrees
- `C17`: Adjust the azimuth of 3249972_2 by 33 degrees
- `C18`: Add neighbor relationship between 3249972_2 and 3215804_3
- `C19`: Decrease transmission power for 3249972_2
- `C20`: Decrease A3 Offset threshold for 3249972_2
- `C21`: Increase A3 Offset threshold for 3249972_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215804_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.720 | MS1 | 121.4656602841 | 31.1446353587 | 291 | 504990 | -94.64 | 11.74 | 531.11 | 0.11 | 2.30 | 1597 |
| 2024-09-20 22:21:32.344 | MS1 | 121.4656752375 | 31.1446320785 | 514 | 504990 | -95.58 | 10.93 | 317.99 | 0.14 | 2.33 | 1581 |
| 2024-09-20 22:21:33.823 | MS1 | 121.4656589790 | 31.1446196120 | 728 | 504990 | -93.90 | 12.84 | 597.71 | 0.16 | 2.80 | 1573 |
| 2024-09-20 22:21:34.419 | MS1 | 121.4656729783 | 31.1446272517 | 978 | 152650 | -94.96 | 7.28 | 56.94 | 0.15 | 1.68 | 952 |
| 2024-09-20 22:21:35.846 | MS1 | 121.4656616151 | 31.1446180048 | 62 | 152650 | -90.42 | 5.67 | 71.21 | 0.13 | 1.55 | 970 |
| 2024-09-20 22:21:36.964 | MS1 | 121.4656764475 | 31.1446301407 | 348 | 152650 | -89.84 | 2.19 | 49.34 | 0.05 | 1.73 | 916 |
| 2024-09-20 22:21:37.998 | MS1 | 121.4656622080 | 31.1446264737 | 474 | 152650 | -93.52 | 2.98 | 53.98 | 0.16 | 1.74 | 964 |
| 2024-09-20 22:21:38.201 | MS1 | 121.4656719476 | 31.1446221528 | 978 | 152650 | -95.23 | 7.36 | 71.59 | 0.16 | 1.55 | 952 |
| 2024-09-20 22:21:39.659 | MS1 | 121.4656749213 | 31.1446341123 | 62 | 152650 | -88.79 | 7.67 | 78.19 | 0.20 | 1.57 | 922 |
| 2024-09-20 22:21:40.957 | MS1 | 121.4656727335 | 31.1446297234 | 348 | 152650 | -95.34 | 3.62 | 53.27 | 0.01 | 2.52 | 1594 |
| 2024-09-20 22:21:41.165 | MS1 | 121.4656654483 | 31.1446365182 | 474 | 152650 | -94.62 | 3.38 | 89.14 | 0.18 | 2.06 | 1563 |
| 2024-09-20 22:21:42.579 | MS1 | 121.4656669738 | 31.1446296283 | 978 | 152650 | -93.49 | 6.28 | 62.41 | 0.02 | 2.19 | 1563 |

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
| 3215804 | 3 | 121.4729275295 | 31.1440780192 | 308 | 3 | 0 | 10.9 | TDD | 420 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3218201 | 13 | 121.4755000561 | 31.1532452590 | 47 | 4 | 1 | 18.2 | FDD | 62 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3222437 | 5 | 121.4684255580 | 31.1533989685 | 115 | 4 | 2 | 25.5 | TDD | 617 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3226331 | 11 | 121.4719079379 | 31.1523571457 | 53 | 14 | 2 | 16.8 | FDD | 474 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3235203 | 7 | 121.4753210686 | 31.1493832225 | 103 | 7 | 7 | 24.1 | FDD | 999 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3236929 | 12 | 121.4724610546 | 31.1494251121 | 7 | 15 | 3 | 17.7 | FDD | 348 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3246905 | 10 | 121.4738678623 | 31.1452408993 | 304 | 4 | 12 | 11.6 | FDD | 978 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3249972 | 2 | 121.4712079660 | 31.1558214908 | 236 | 0 | 5 | 9.8 | TDD | 291 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3255540 | 4 | 121.4671852714 | 31.1445930275 | 342 | 9 | 5 | 4.5 | TDD | 354 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3259119 | 6 | 121.4710308309 | 31.1470522001 | 102 | 4 | 10 | 7.9 | TDD | 728 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3259343 | 8 | 121.4675888957 | 31.1474506214 | 0 | 1 | 5 | 20.1 | FDD | 872 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3268882 | 1 | 121.4757930816 | 31.1454712840 | 118 | 0 | 6 | 27.1 | TDD | 514 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3272780 | 9 | 121.4682572852 | 31.1545902119 | 274 | 14 | 2 | 13.8 | FDD | 556 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |

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
| 2024-09-20 22:21:31.504 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.522 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.660 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.660 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.396 | NREventA2 | measId:1;ServCellPCI:769;Se... |
| 2024-09-20 22:21:35.509 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.724 | NREventA5 | measId:3;ServCellPCI:769;Se... |
| 2024-09-20 22:21:35.790 | NRHandoverAttempt | SourcePCI:769;SourceNR-ARFC... |
| 2024-09-20 22:21:35.822 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.834 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.940 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.940 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268882 | 1 | 6.4359 | 12.9266 | -116.4698 | 8.0239 | 156.0611 | 0.0182 | 0.0030 |
| 2024_09_20 22:00 | 3249972 | 2 | 15.7747 | 14.6599 | -117.1564 | 11.2582 | 174.0725 | 0.0149 | 0.0133 |
| 2024_09_20 22:00 | 3215804 | 3 | 15.9827 | 9.2366 | -116.8276 | 17.4257 | 149.4302 | 0.0174 | 0.0116 |
| 2024_09_20 22:00 | 3255540 | 4 | 15.1180 | 11.4005 | -115.9109 | 17.4393 | 103.6286 | 0.0184 | 0.0193 |
| 2024_09_20 22:00 | 3222437 | 5 | 7.4511 | 11.4557 | -117.8646 | 15.0116 | 103.2282 | 0.0185 | 0.0009 |
| 2024_09_20 22:00 | 3259119 | 6 | 9.0590 | 14.7000 | -116.7269 | 19.5064 | 86.4377 | 0.0052 | 0.0161 |
| 2024_09_20 22:00 | 3235203 | 7 | 8.0828 | 13.3458 | -114.2767 | 3.8885 | 46.6048 | 0.0067 | 0.0158 |
| 2024_09_20 22:00 | 3259343 | 8 | 8.6325 | 11.2938 | -117.6894 | 4.4821 | 25.8360 | 0.0195 | 0.0136 |
| 2024_09_20 22:00 | 3272780 | 9 | 7.0950 | 10.9819 | -115.9601 | 4.2127 | 42.0382 | 0.0080 | 0.0176 |
| 2024_09_20 22:00 | 3246905 | 10 | 15.1212 | 11.0240 | -114.9391 | 4.3343 | 36.4547 | 0.0004 | 0.0103 |
| 2024_09_20 22:00 | 3226331 | 11 | 16.5660 | 18.3933 | -115.0578 | 4.6758 | 45.8052 | 0.0117 | 0.0194 |
| 2024_09_20 22:00 | 3236929 | 12 | 13.8498 | 17.5932 | -116.4302 | 4.4418 | 23.6015 | 0.0114 | 0.0011 |
| 2024_09_20 22:00 | 3218201 | 13 | 6.2625 | 18.4386 | -114.3059 | 3.6251 | 54.7375 | 0.0002 | 0.0180 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416885_EDC180A7 | 152650 | 978 | -93.1 | 152650 | 556 | -103.6 | 152650 | 872 | -102.4 | 152650 | 999 |
| MR_1774416885_5A33F76F | 152650 | 978 | -94.8 | 152650 | 556 | -103.2 | 152650 | 872 | -102.6 | 152650 | 999 |
| MR_1774416885_E204EFF1 | 152650 | 978 | -96.2 | 152650 | 556 | -103.5 | 152650 | 872 | -100.9 | 152650 | 999 |
| MR_1774416885_CEBAFB46 | 504990 | 728 | -93.6 | 504990 | 420 | -93.3 | 504990 | 617 | -99.3 | 504990 | 354 |
| MR_1774416885_38E500FD | 504990 | 728 | -95.6 | 504990 | 420 | -96.5 | 504990 | 617 | -100.1 | 504990 | 354 |
| MR_1774416885_67E7A706 | 504990 | 728 | -95.0 | 504990 | 420 | -96.2 | 504990 | 617 | -98.6 | 504990 | 354 |
| MR_1774416885_E8937731 | 152650 | 978 | -93.5 | 152650 | 556 | -101.2 | 152650 | 872 | -102.8 | 152650 | 999 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 91: `c78acddb-e53...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c78acddb-e535-4f9e-bb8e-0007851ef632` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[91] topology](images/test_0091.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3222376_1
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222376_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222376_1
- `C5`: Decrease transmission power for 3245994_2
- `C6`: Lift the tilt angle  of 3245994_2 by 10 degrees
- `C7`: Check test server and transmission issues
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245994_2
- `C9`: Increase transmission power for 3245994_2
- `C10`: Press down the tilt angle of 3222376_1 by 10 degrees
- `C11`: Press down the tilt angle  of 3245994_2 by 10 degrees
- `C12`: Lift the tilt angle of 3222376_1 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3222376_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245994_2
- `C15`: Adjust the azimuth of 3222376_1 by 21 degrees
- `C16`: Decrease transmission power for 3222376_1
- `C17`: Adjust the azimuth of 3245994_2 by 50 degrees
- `C18`: Add neighbor relationship between 3212165_4 and 3245994_2
- `C19`: Add neighbor relationship between 3222376_1 and 3245994_2
- `C20`: Increase transmission power for 3222376_1
- `C21`: Increase A3 Offset threshold for 3245994_2
- `C22`: Decrease A3 Offset threshold for 3245994_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.830 | MS1 | 121.4656777084 | 31.1446182900 | 664 | 504990 | -91.47 | 12.29 | 526.80 | 0.09 | 2.31 | 1590 |
| 2024-09-20 22:21:32.506 | MS1 | 121.4656599474 | 31.1446272565 | 664 | 504990 | -88.56 | 17.47 | 599.23 | 0.11 | 2.04 | 1564 |
| 2024-09-20 22:21:33.834 | MS1 | 121.4656655899 | 31.1446298833 | 664 | 504990 | -87.84 | 13.22 | 334.47 | 0.10 | 2.36 | 1568 |
| 2024-09-20 22:21:34.729 | MS1 | 121.4656771112 | 31.1446358731 | 664 | 504990 | -89.43 | 12.40 | 83.20 | 0.15 | 2.12 | 1573 |
| 2024-09-20 22:21:35.398 | MS1 | 121.4656674796 | 31.1446302662 | 664 | 504990 | -86.55 | 15.90 | 77.84 | 0.04 | 2.36 | 1573 |
| 2024-09-20 22:21:36.690 | MS1 | 121.4656595026 | 31.1446297279 | 664 | 504990 | -91.25 | 15.54 | 51.56 | 0.06 | 2.96 | 1587 |
| 2024-09-20 22:21:37.598 | MS1 | 121.4656710599 | 31.1446245471 | 664 | 504990 | -89.91 | 10.45 | 75.86 | 0.08 | 2.55 | 1599 |
| 2024-09-20 22:21:38.194 | MS1 | 121.4656755844 | 31.1446277866 | 664 | 504990 | -90.84 | 9.32 | 89.59 | 0.07 | 2.16 | 1584 |
| 2024-09-20 22:21:39.752 | MS1 | 121.4656590480 | 31.1446259931 | 664 | 504990 | -89.98 | 12.70 | 100.28 | 0.18 | 2.66 | 1589 |
| 2024-09-20 22:21:40.749 | MS1 | 121.4656655821 | 31.1446369401 | 664 | 504990 | -93.19 | 10.88 | 493.38 | 0.15 | 2.76 | 1587 |
| 2024-09-20 22:21:41.855 | MS1 | 121.4656753812 | 31.1446355176 | 664 | 504990 | -92.50 | 7.84 | 548.92 | 0.07 | 2.61 | 1582 |
| 2024-09-20 22:21:42.882 | MS1 | 121.4656696866 | 31.1446184136 | 664 | 504990 | -92.58 | 12.31 | 509.60 | 0.12 | 2.01 | 1584 |

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
| 3212165 | 4 | 121.4694155497 | 31.1449568949 | 164 | 11 | 2 | 34.4 | TDD | 717 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3222376 | 1 | 121.4671918235 | 31.1462630662 | 240 | 13 | 12 | 18.3 | TDD | 664 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3245994 | 2 | 121.4656991390 | 31.1539158134 | 335 | 11 | 0 | 32.0 | TDD | 353 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3255944 | 3 | 121.4744893807 | 31.1441312458 | 76 | 7 | 4 | 39.3 | TDD | 937 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.764 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.780 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:30.909 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.909 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.607 | NREventA3 | measId:2;ServCellPCI:389;Se... |
| 2024-09-20 22:21:37.847 | NRHandoverAttempt | SourcePCI:389;SourceNR-ARFC... |
| 2024-09-20 22:21:37.885 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.898 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.011 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.011 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3222376 | 1 | 92.5418 | 86.1865 | -117.1539 | 18.9981 | 167.2931 | 0.0189 | 0.0024 |
| 2024_09_19 22:00 | 3245994 | 2 | 78.0773 | 94.8002 | -116.5327 | 11.4617 | 112.2395 | 0.0014 | 0.0045 |
| 2024_09_19 22:00 | 3255944 | 3 | 88.7420 | 75.3339 | -114.8531 | 9.7648 | 178.5636 | 0.0069 | 0.0112 |
| 2024_09_19 22:00 | 3212165 | 4 | 89.7781 | 78.6487 | -117.1674 | 11.9746 | 194.9680 | 0.0119 | 0.0105 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417107_CFFCE125 | 504990 | 664 | -88.3 | 504990 | 353 | -93.7 | 504990 | 717 | -99.4 | 504990 | 937 |
| MR_1774417107_1C07721D | 504990 | 664 | -89.7 | 504990 | 353 | -94.1 | 504990 | 717 | -99.2 | 504990 | 937 |
| MR_1774417107_A972EB6F | 504990 | 664 | -89.1 | 504990 | 353 | -96.7 | 504990 | 717 | -99.9 | 504990 | 937 |
| MR_1774417107_82A28385 | 504990 | 664 | -91.2 | 504990 | 353 | -96.4 | 504990 | 717 | -99.5 | 504990 | 937 |
| MR_1774417107_298DCCC9 | 504990 | 664 | -89.2 | 504990 | 353 | -94.3 | 504990 | 717 | -98.2 | 504990 | 937 |
| MR_1774417107_71677D2B | 504990 | 664 | -89.2 | 504990 | 353 | -93.8 | 504990 | 717 | -99.9 | 504990 | 937 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 92: `0aa7797b-556...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0aa7797b-5562-4bf0-ad77-fb2c80be057e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[92] topology](images/test_0092.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3257729_2 by 10 degrees
- `C2`: Lift the tilt angle of 3211755_3 by 5 degrees
- `C3`: Increase transmission power for 3215555_1
- `C4`: Increase transmission power for 3211755_3
- `C5`: Adjust the azimuth of 3257729_2 by 50 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211755_3
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Adjust the azimuth of 3211755_3 by 30 degrees
- `C9`: Check test server and transmission issues
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215555_1
- `C11`: Increase A3 Offset threshold for 3211755_3
- `C12`: Press down the tilt angle of 3211755_3 by 5 degrees
- `C13`: Decrease A3 Offset threshold for 3211755_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215555_1
- `C15`: Lift the tilt angle  of 3257729_2 by 10 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211755_3
- `C17`: Increase A3 Offset threshold for 3215555_1
- `C18`: Decrease transmission power for 3215555_1
- `C19`: Add neighbor relationship between 3257729_2 and 3215555_1
- `C20`: Decrease transmission power for 3211755_3
- `C21`: Decrease A3 Offset threshold for 3215555_1
- `C22`: Add neighbor relationship between 3211755_3 and 3215555_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.526 | MS1 | 121.4656692650 | 31.1446285694 | 948 | 504990 | -90.72 | 13.36 | 548.74 | 0.18 | 2.59 | 1580 |
| 2024-09-20 22:21:32.926 | MS1 | 121.4656760611 | 31.1446248980 | 948 | 504990 | -86.98 | 16.04 | 577.83 | 0.10 | 2.43 | 1575 |
| 2024-09-20 22:21:33.587 | MS1 | 121.4656655674 | 31.1446262615 | 948 | 504990 | -89.82 | 15.13 | 588.76 | 0.16 | 2.90 | 1562 |
| 2024-09-20 22:21:34.931 | MS1 | 121.4656724676 | 31.1446304694 | 948 | 504990 | -87.85 | 14.58 | 60.17 | 0.06 | 2.08 | 1586 |
| 2024-09-20 22:21:35.381 | MS1 | 121.4656708397 | 31.1446269704 | 948 | 504990 | -89.43 | 16.40 | 79.25 | 0.04 | 2.86 | 1561 |
| 2024-09-20 22:21:36.394 | MS1 | 121.4656580593 | 31.1446215491 | 948 | 504990 | -87.76 | 13.66 | 97.20 | 0.19 | 2.42 | 1568 |
| 2024-09-20 22:21:37.343 | MS1 | 121.4656607118 | 31.1446350061 | 948 | 504990 | -92.31 | 8.66 | 71.69 | 0.20 | 2.24 | 1593 |
| 2024-09-20 22:21:38.433 | MS1 | 121.4656593321 | 31.1446370615 | 948 | 504990 | -92.74 | 11.93 | 97.35 | 0.10 | 2.11 | 1573 |
| 2024-09-20 22:21:39.795 | MS1 | 121.4656775795 | 31.1446180700 | 948 | 504990 | -90.46 | 7.72 | 67.33 | 0.06 | 2.67 | 1562 |
| 2024-09-20 22:21:40.565 | MS1 | 121.4656604816 | 31.1446336293 | 948 | 504990 | -92.96 | 11.41 | 382.75 | 0.03 | 2.82 | 1596 |
| 2024-09-20 22:21:41.913 | MS1 | 121.4656779102 | 31.1446214534 | 948 | 504990 | -91.59 | 9.89 | 541.24 | 0.04 | 2.77 | 1562 |
| 2024-09-20 22:21:42.661 | MS1 | 121.4656758394 | 31.1446368790 | 948 | 504990 | -91.48 | 7.62 | 451.37 | 0.12 | 2.14 | 1579 |

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
| 3211755 | 3 | 121.4699688423 | 31.1468335631 | 209 | 2 | 11 | 25.2 | TDD | 948 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3215555 | 1 | 121.4662828327 | 31.1559018239 | 31 | 12 | 12 | 37.8 | TDD | 577 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3221508 | 4 | 121.4728277268 | 31.1486275855 | 255 | 12 | 10 | 35.9 | TDD | 478 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3257729 | 2 | 121.4678644059 | 31.1468090248 | 20 | 2 | 1 | 45.8 | TDD | 435 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.768 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.790 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.937 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.937 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.664 | NREventA3 | measId:2;ServCellPCI:196;Se... |
| 2024-09-20 22:21:37.904 | NRHandoverAttempt | SourcePCI:196;SourceNR-ARFC... |
| 2024-09-20 22:21:37.945 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.956 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.091 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.091 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215555 | 1 | 16.2238 | 17.8856 | -116.6278 | 10.6701 | 168.2767 | 0.0140 | 0.0099 |
| 2024_09_20 22:00 | 3257729 | 2 | 11.5430 | 10.5447 | -117.9620 | 15.3353 | 92.7921 | 0.0065 | 0.0173 |
| 2024_09_20 22:00 | 3211755 | 3 | 80.4472 | 90.8050 | -115.4625 | 8.7976 | 122.6478 | 0.0083 | 0.0011 |
| 2024_09_20 22:00 | 3221508 | 4 | 15.8443 | 16.4849 | -116.6234 | 16.3848 | 146.6145 | 0.0091 | 0.0177 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417190_178FFDFC | 504990 | 948 | -88.9 | 504990 | 577 | -89.4 | 504990 | 435 | -100.1 | 504990 | 478 |
| MR_1774417190_97FE2442 | 504990 | 948 | -87.8 | 504990 | 577 | -90.8 | 504990 | 435 | -100.9 | 504990 | 478 |
| MR_1774417190_5CBAB102 | 504990 | 948 | -89.0 | 504990 | 577 | -92.3 | 504990 | 435 | -98.8 | 504990 | 478 |
| MR_1774417190_2307EC7D | 504990 | 948 | -87.4 | 504990 | 577 | -89.8 | 504990 | 435 | -98.9 | 504990 | 478 |
| MR_1774417190_5D0379F3 | 504990 | 948 | -86.7 | 504990 | 577 | -92.8 | 504990 | 435 | -100.7 | 504990 | 478 |
| MR_1774417190_5BA4AA98 | 504990 | 948 | -89.1 | 504990 | 577 | -92.7 | 504990 | 435 | -100.4 | 504990 | 478 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 93: `e666e92e-aec...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e666e92e-aec5-453a-945c-ec6dacf8d958` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[93] topology](images/test_0093.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3240476_4
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Press down the tilt angle  of 3230633_3 by 5 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252776_1
- `C5`: Add neighbor relationship between 3230633_3 and 3240476_4
- `C6`: Decrease A3 Offset threshold for 3252776_1
- `C7`: Add neighbor relationship between 3252776_1 and 3240476_4
- `C8`: Press down the tilt angle of 3252776_1 by 4 degrees
- `C9`: Increase A3 Offset threshold for 3252776_1
- `C10`: Increase transmission power for 3252776_1
- `C11`: Lift the tilt angle of 3252776_1 by 4 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240476_4
- `C13`: Decrease transmission power for 3252776_1
- `C14`: Adjust the azimuth of 3252776_1 by 46 degrees
- `C15`: Check test server and transmission issues
- `C16`: Increase transmission power for 3240476_4
- `C17`: Lift the tilt angle  of 3230633_3 by 5 degrees
- `C18`: Adjust the azimuth of 3230633_3 by 50 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252776_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240476_4
- `C21`: Decrease transmission power for 3240476_4
- `C22`: Increase A3 Offset threshold for 3240476_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.529 | MS1 | 121.4656589236 | 31.1446200887 | 512 | 504990 | -88.93 | 12.52 | 361.75 | 0.04 | 2.80 | 1586 |
| 2024-09-20 22:21:32.378 | MS1 | 121.4656756567 | 31.1446261418 | 512 | 504990 | -91.05 | 13.76 | 350.14 | 0.15 | 2.35 | 1581 |
| 2024-09-20 22:21:33.141 | MS1 | 121.4656601423 | 31.1446312372 | 512 | 504990 | -90.68 | 13.89 | 384.74 | 0.15 | 2.27 | 1580 |
| 2024-09-20 22:21:34.275 | MS1 | 121.4656769698 | 31.1446209477 | 512 | 504990 | -86.20 | 14.50 | 89.50 | 0.13 | 2.37 | 1594 |
| 2024-09-20 22:21:35.564 | MS1 | 121.4656639459 | 31.1446307681 | 512 | 504990 | -85.21 | 12.69 | 71.22 | 0.18 | 2.56 | 1576 |
| 2024-09-20 22:21:36.933 | MS1 | 121.4656709920 | 31.1446300958 | 512 | 504990 | -91.53 | 15.94 | 65.05 | 0.16 | 2.17 | 1586 |
| 2024-09-20 22:21:37.261 | MS1 | 121.4656722361 | 31.1446333332 | 512 | 504990 | -89.78 | 11.50 | 64.50 | 0.06 | 2.22 | 1587 |
| 2024-09-20 22:21:38.442 | MS1 | 121.4656654525 | 31.1446252926 | 512 | 504990 | -89.17 | 10.51 | 63.20 | 0.19 | 2.39 | 1585 |
| 2024-09-20 22:21:39.605 | MS1 | 121.4656635555 | 31.1446245103 | 512 | 504990 | -93.20 | 11.61 | 98.45 | 0.09 | 2.38 | 1565 |
| 2024-09-20 22:21:40.668 | MS1 | 121.4656748767 | 31.1446287109 | 512 | 504990 | -89.92 | 9.73 | 556.55 | 0.19 | 2.93 | 1576 |
| 2024-09-20 22:21:41.710 | MS1 | 121.4656766491 | 31.1446273764 | 512 | 504990 | -92.03 | 8.98 | 407.99 | 0.15 | 2.39 | 1566 |
| 2024-09-20 22:21:42.585 | MS1 | 121.4656777060 | 31.1446354761 | 512 | 504990 | -89.06 | 11.37 | 340.14 | 0.14 | 2.07 | 1578 |

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
| 3230633 | 3 | 121.4670903041 | 31.1462842370 | 131 | 3 | 2 | 42.8 | TDD | 94 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3240476 | 4 | 121.4741552727 | 31.1548013670 | 159 | 3 | 11 | 45.7 | TDD | 944 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3252776 | 1 | 121.4684209126 | 31.1525042093 | 243 | 1 | 7 | 46.0 | TDD | 512 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3266803 | 2 | 121.4703477551 | 31.1497585392 | 160 | 9 | 7 | 43.6 | TDD | 982 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.905 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.929 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.046 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.046 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.713 | NREventA3 | measId:2;ServCellPCI:33;Ser... |
| 2024-09-20 22:21:37.953 | NRHandoverAttempt | SourcePCI:33;SourceNR-ARFCN... |
| 2024-09-20 22:21:37.987 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.997 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.100 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.100 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252776 | 1 | 89.0958 | 81.6789 | -117.6085 | 18.9626 | 104.5360 | 0.0069 | 0.0127 |
| 2024_09_20 22:00 | 3266803 | 2 | 6.5613 | 9.8176 | -116.1610 | 9.0948 | 162.5173 | 0.0112 | 0.0088 |
| 2024_09_20 22:00 | 3230633 | 3 | 9.6333 | 7.3020 | -116.5278 | 10.1662 | 197.0782 | 0.0082 | 0.0143 |
| 2024_09_20 22:00 | 3240476 | 4 | 12.6120 | 19.5085 | -114.0368 | 10.5978 | 83.0933 | 0.0029 | 0.0052 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415450_5A36780E | 504990 | 512 | -85.7 | 504990 | 944 | -90.4 | 504990 | 94 | -94.5 | 504990 | 982 |
| MR_1774415450_9E1FB223 | 504990 | 512 | -85.4 | 504990 | 944 | -89.9 | 504990 | 94 | -96.9 | 504990 | 982 |
| MR_1774415450_F63E522F | 504990 | 512 | -88.0 | 504990 | 944 | -91.8 | 504990 | 94 | -97.3 | 504990 | 982 |
| MR_1774415450_49FDFC88 | 504990 | 512 | -86.8 | 504990 | 944 | -91.5 | 504990 | 94 | -97.0 | 504990 | 982 |
| MR_1774415450_8F8FD8FE | 504990 | 512 | -88.1 | 504990 | 944 | -88.0 | 504990 | 94 | -96.5 | 504990 | 982 |
| MR_1774415450_61BB5031 | 504990 | 512 | -86.4 | 504990 | 944 | -87.9 | 504990 | 94 | -93.9 | 504990 | 982 |
| MR_1774415450_2B57BE81 | 504990 | 512 | -85.5 | 504990 | 944 | -89.9 | 504990 | 94 | -97.4 | 504990 | 982 |
| MR_1774415450_455B2084 | 504990 | 512 | -88.2 | 504990 | 944 | -90.3 | 504990 | 94 | -95.9 | 504990 | 982 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 94: `47894def-46c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `47894def-46ca-4cb8-b222-30b355e27389` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[94] topology](images/test_0094.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3248963_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248963_1
- `C3`: Increase A3 Offset threshold for 3255828_2
- `C4`: Adjust the azimuth of 3248963_1 by 25 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255828_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255828_2
- `C7`: Decrease A3 Offset threshold for 3255828_2
- `C8`: Decrease transmission power for 3255828_2
- `C9`: Add neighbor relationship between 3271890_4 and 3248963_1
- `C10`: Lift the tilt angle of 3255828_2 by 2 degrees
- `C11`: Decrease transmission power for 3248963_1
- `C12`: Increase transmission power for 3255828_2
- `C13`: Press down the tilt angle  of 3248963_1 by 2 degrees
- `C14`: Check test server and transmission issues
- `C15`: Lift the tilt angle  of 3248963_1 by 2 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase A3 Offset threshold for 3248963_1
- `C18`: Increase transmission power for 3248963_1
- `C19`: Add neighbor relationship between 3255828_2 and 3248963_1
- `C20`: Press down the tilt angle of 3255828_2 by 2 degrees
- `C21`: Adjust the azimuth of 3255828_2 by 25 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248963_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.434 | MS1 | 121.4656720063 | 31.1446263442 | 295 | 504990 | -80.65 | 13.16 | 388.17 | 0.05 | 2.43 | 1577 |
| 2024-09-20 22:21:32.636 | MS1 | 121.4656738811 | 31.1446355164 | 295 | 504990 | -78.99 | 12.56 | 395.50 | 0.18 | 2.76 | 1597 |
| 2024-09-20 22:21:33.464 | MS1 | 121.4656677746 | 31.1446345503 | 295 | 504990 | -77.34 | 16.77 | 330.33 | 0.17 | 2.50 | 1590 |
| 2024-09-20 22:21:34.470 | MS1 | 121.4656618232 | 31.1446304443 | 630 | 504990 | -85.42 | 2.15 | 44.70 | 0.18 | 1.19 | 1572 |
| 2024-09-20 22:21:35.438 | MS1 | 121.4656778558 | 31.1446289559 | 630 | 504990 | -81.50 | 2.58 | 71.57 | 0.11 | 1.33 | 1560 |
| 2024-09-20 22:21:36.348 | MS1 | 121.4656690884 | 31.1446294239 | 295 | 504990 | -88.85 | 2.54 | 36.58 | 0.09 | 1.20 | 1587 |
| 2024-09-20 22:21:37.410 | MS1 | 121.4656648644 | 31.1446275347 | 295 | 504990 | -89.09 | 3.98 | 43.82 | 0.13 | 1.33 | 1575 |
| 2024-09-20 22:21:38.220 | MS1 | 121.4656627234 | 31.1446260415 | 630 | 504990 | -87.92 | 2.83 | 54.06 | 0.12 | 1.38 | 1571 |
| 2024-09-20 22:21:39.475 | MS1 | 121.4656606330 | 31.1446319945 | 630 | 504990 | -87.65 | 4.31 | 50.10 | 0.16 | 1.12 | 1569 |
| 2024-09-20 22:21:40.104 | MS1 | 121.4656616668 | 31.1446316452 | 630 | 504990 | -82.27 | 14.73 | 506.44 | 0.02 | 2.64 | 1590 |
| 2024-09-20 22:21:41.939 | MS1 | 121.4656719886 | 31.1446242342 | 630 | 504990 | -75.35 | 12.35 | 488.05 | 0.12 | 2.26 | 1597 |
| 2024-09-20 22:21:42.497 | MS1 | 121.4656628111 | 31.1446281473 | 630 | 504990 | -78.94 | 13.64 | 602.31 | 0.02 | 2.39 | 1599 |

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
| 3218361 | 3 | 121.4681350333 | 31.1489147960 | 121 | 9 | 3 | 16.4 | TDD | 630 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3248963 | 1 | 121.4747116773 | 31.1448559961 | 243 | 0 | 1 | 29.5 | TDD | 548 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3255828 | 2 | 121.4701427978 | 31.1520185841 | 182 | 1 | 4 | 20.8 | TDD | 295 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3271890 | 4 | 121.4709683104 | 31.1514034012 | 151 | 15 | 5 | 29.7 | TDD | 54 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3274345 | 5 | 121.4655758762 | 31.1458039224 | 93 | 9 | 10 | 25.0 | TDD | 799 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.096 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.116 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.256 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.256 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.917 | NREventA3 | measId:2;ServCellPCI:152;Se... |
| 2024-09-20 22:21:34.157 | NRHandoverAttempt | SourcePCI:152;SourceNR-ARFC... |
| 2024-09-20 22:21:34.195 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.205 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:34.335 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.335 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.917 | NREventA3 | measId:2;ServCellPCI:691;Se... |
| 2024-09-20 22:21:36.157 | NRHandoverAttempt | SourcePCI:691;SourceNR-ARFC... |
| 2024-09-20 22:21:36.203 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.217 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.318 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.318 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.917 | NREventA3 | measId:2;ServCellPCI:152;Se... |
| 2024-09-20 22:21:38.157 | NRHandoverAttempt | SourcePCI:152;SourceNR-ARFC... |
| 2024-09-20 22:21:38.200 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.211 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.359 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.359 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248963 | 1 | 6.2103 | 17.3992 | -115.2659 | 7.2414 | 86.8493 | 0.0115 | 0.0135 |
| 2024_09_20 22:00 | 3255828 | 2 | 17.0004 | 5.9669 | -117.3086 | 6.2743 | 169.8853 | 0.0158 | 0.0096 |
| 2024_09_20 22:00 | 3218361 | 3 | 8.9058 | 13.2932 | -116.4613 | 14.6636 | 167.8889 | 0.0134 | 0.0045 |
| 2024_09_20 22:00 | 3271890 | 4 | 19.2168 | 18.4943 | -115.9777 | 9.9188 | 109.5116 | 0.0147 | 0.0057 |
| 2024_09_20 22:00 | 3274345 | 5 | 11.5680 | 19.4952 | -117.8502 | 11.3544 | 170.2934 | 0.0152 | 0.0041 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415227_33C0D883 | 504990 | 295 | -85.8 | 504990 | 630 | -87.8 | 504990 | 548 | -87.4 | 504990 | 54 |
| MR_1774415227_5D4216AE | 504990 | 295 | -86.7 | 504990 | 630 | -84.8 | 504990 | 548 | -89.6 | 504990 | 54 |
| MR_1774415227_361F11C8 | 504990 | 630 | -84.9 | 504990 | 295 | -84.1 | 504990 | 548 | -88.8 | 504990 | 54 |
| MR_1774415227_82682175 | 504990 | 630 | -86.4 | 504990 | 295 | -85.0 | 504990 | 548 | -86.7 | 504990 | 54 |
| MR_1774415227_483C7E89 | 504990 | 295 | -87.4 | 504990 | 630 | -84.4 | 504990 | 548 | -86.2 | 504990 | 54 |
| MR_1774415227_0CFF63AC | 504990 | 630 | -84.5 | 504990 | 295 | -85.1 | 504990 | 548 | -86.7 | 504990 | 54 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 95: `990a6082-86d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `990a6082-86dc-45f4-b79f-7b84ed13faad` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[95] topology](images/test_0095.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3246009_1 and 3243863_3
- `C2`: Decrease transmission power for 3263472_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243863_3
- `C4`: Decrease A3 Offset threshold for 3243863_3
- `C5`: Increase A3 Offset threshold for 3263472_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243863_3
- `C7`: Adjust the azimuth of 3243863_3 by 50 degrees
- `C8`: Check test server and transmission issues
- `C9`: Increase transmission power for 3263472_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263472_2
- `C11`: Add neighbor relationship between 3263472_2 and 3243863_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263472_2
- `C13`: Decrease transmission power for 3243863_3
- `C14`: Decrease A3 Offset threshold for 3263472_2
- `C15`: Press down the tilt angle  of 3243863_3 by 10 degrees
- `C16`: Increase transmission power for 3243863_3
- `C17`: Lift the tilt angle  of 3243863_3 by 10 degrees
- `C18`: Lift the tilt angle of 3263472_2 by 3 degrees
- `C19`: Increase A3 Offset threshold for 3243863_3
- `C20`: Press down the tilt angle of 3263472_2 by 3 degrees
- `C21`: Adjust the azimuth of 3263472_2 by 24 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.491 | MS1 | 121.4656648561 | 31.1446349849 | 604 | 504990 | -88.32 | 12.51 | 397.01 | 0.19 | 2.82 | 1570 |
| 2024-09-20 22:21:32.215 | MS1 | 121.4656595559 | 31.1446189460 | 604 | 504990 | -90.58 | 17.08 | 337.59 | 0.18 | 2.44 | 1589 |
| 2024-09-20 22:21:33.440 | MS1 | 121.4656601990 | 31.1446379042 | 604 | 504990 | -90.91 | 16.75 | 360.64 | 0.15 | 2.18 | 1562 |
| 2024-09-20 22:21:34.268 | MS1 | 121.4656669139 | 31.1446355453 | 604 | 504990 | -87.26 | 14.47 | 89.65 | 0.69 | 2.30 | 578 |
| 2024-09-20 22:21:35.444 | MS1 | 121.4656698887 | 31.1446199110 | 604 | 504990 | -87.31 | 16.00 | 73.19 | 0.67 | 2.54 | 545 |
| 2024-09-20 22:21:36.793 | MS1 | 121.4656638920 | 31.1446279027 | 604 | 504990 | -87.15 | 12.60 | 66.64 | 0.66 | 2.00 | 543 |
| 2024-09-20 22:21:37.750 | MS1 | 121.4656674350 | 31.1446294219 | 604 | 504990 | -92.76 | 12.81 | 97.67 | 0.67 | 2.85 | 678 |
| 2024-09-20 22:21:38.456 | MS1 | 121.4656770516 | 31.1446362443 | 604 | 504990 | -92.18 | 7.29 | 60.15 | 0.50 | 2.14 | 589 |
| 2024-09-20 22:21:39.440 | MS1 | 121.4656584237 | 31.1446277032 | 604 | 504990 | -89.70 | 9.45 | 72.86 | 0.64 | 2.37 | 523 |
| 2024-09-20 22:21:40.157 | MS1 | 121.4656586400 | 31.1446293776 | 604 | 504990 | -93.85 | 11.89 | 307.13 | 0.07 | 2.26 | 1575 |
| 2024-09-20 22:21:41.549 | MS1 | 121.4656771557 | 31.1446299137 | 604 | 504990 | -93.00 | 12.98 | 512.79 | 0.03 | 2.77 | 1583 |
| 2024-09-20 22:21:42.714 | MS1 | 121.4656656957 | 31.1446296853 | 604 | 504990 | -91.42 | 7.66 | 429.19 | 0.15 | 2.79 | 1566 |

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
| 3243863 | 3 | 121.4642662356 | 31.1452682306 | 324 | 14 | 3 | 49.1 | TDD | 133 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3246009 | 1 | 121.4697982099 | 31.1443892491 | 281 | 4 | 12 | 37.3 | TDD | 39 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3262087 | 4 | 121.4692421855 | 31.1492407149 | 75 | 8 | 7 | 35.6 | TDD | 383 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3263472 | 2 | 121.4648213168 | 31.1529229407 | 199 | 1 | 9 | 30.5 | TDD | 604 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.309 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.331 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.438 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.438 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.112 | NREventA3 | measId:2;ServCellPCI:936;Se... |
| 2024-09-20 22:21:38.352 | NRHandoverAttempt | SourcePCI:936;SourceNR-ARFC... |
| 2024-09-20 22:21:38.396 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.407 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.536 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.536 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246009 | 1 | 8.2937 | 8.3162 | -116.8377 | 14.5043 | 100.4809 | 0.0141 | 0.0040 |
| 2024_09_20 22:00 | 3263472 | 2 | 17.5428 | 7.8972 | -116.5460 | 10.7473 | 187.9467 | 0.0061 | 0.0069 |
| 2024_09_20 22:00 | 3243863 | 3 | 6.8130 | 7.4319 | -117.9830 | 13.0890 | 87.0014 | 0.0079 | 0.0039 |
| 2024_09_20 22:00 | 3262087 | 4 | 9.3138 | 8.3357 | -115.0054 | 19.4616 | 136.9881 | 0.0115 | 0.0075 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416624_ED542EA4 | 504990 | 604 | -87.4 | 504990 | 133 | -91.2 | 504990 | 39 | -93.7 | 504990 | 383 |
| MR_1774416624_0D2C6E10 | 504990 | 604 | -89.2 | 504990 | 133 | -93.1 | 504990 | 39 | -93.3 | 504990 | 383 |
| MR_1774416624_00573544 | 504990 | 604 | -89.0 | 504990 | 133 | -90.7 | 504990 | 39 | -92.5 | 504990 | 383 |
| MR_1774416624_96DC8A2F | 504990 | 604 | -87.0 | 504990 | 133 | -91.5 | 504990 | 39 | -94.0 | 504990 | 383 |
| MR_1774416624_E1D833BD | 504990 | 604 | -88.5 | 504990 | 133 | -91.5 | 504990 | 39 | -93.0 | 504990 | 383 |
| MR_1774416624_89104717 | 504990 | 604 | -86.2 | 504990 | 133 | -93.0 | 504990 | 39 | -95.1 | 504990 | 383 |
| MR_1774416624_4A7F2159 | 504990 | 604 | -85.4 | 504990 | 133 | -90.0 | 504990 | 39 | -95.8 | 504990 | 383 |
| MR_1774416624_58ABA8E9 | 504990 | 604 | -89.2 | 504990 | 133 | -89.5 | 504990 | 39 | -93.9 | 504990 | 383 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 96: `02637243-f59...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `02637243-f59b-4c2e-9d86-9d16df5fa305` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[96] topology](images/test_0096.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3244132_1 by 3 degrees
- `C2`: Decrease A3 Offset threshold for 3277663_2
- `C3`: Increase A3 Offset threshold for 3244132_1
- `C4`: Add neighbor relationship between 3267997_4 and 3244132_1
- `C5`: Adjust the azimuth of 3277663_2 by 15 degrees
- `C6`: Adjust the azimuth of 3244132_1 by 22 degrees
- `C7`: Increase transmission power for 3244132_1
- `C8`: Decrease transmission power for 3277663_2
- `C9`: Check test server and transmission issues
- `C10`: Decrease A3 Offset threshold for 3244132_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244132_1
- `C13`: Decrease transmission power for 3244132_1
- `C14`: Lift the tilt angle of 3277663_2 by 3 degrees
- `C15`: Press down the tilt angle  of 3244132_1 by 3 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277663_2
- `C17`: Increase A3 Offset threshold for 3277663_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277663_2
- `C19`: Increase transmission power for 3277663_2
- `C20`: Add neighbor relationship between 3277663_2 and 3244132_1
- `C21`: Press down the tilt angle of 3277663_2 by 3 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244132_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.900 | MS1 | 121.4656705148 | 31.1446222784 | 753 | 504990 | -83.52 | 14.41 | 506.18 | 0.04 | 2.31 | 1598 |
| 2024-09-20 22:21:32.843 | MS1 | 121.4656592138 | 31.1446213428 | 753 | 504990 | -84.54 | 16.02 | 424.03 | 0.09 | 2.40 | 1571 |
| 2024-09-20 22:21:33.399 | MS1 | 121.4656772177 | 31.1446300860 | 753 | 504990 | -76.71 | 12.66 | 520.31 | 0.08 | 2.67 | 1591 |
| 2024-09-20 22:21:34.577 | MS1 | 121.4656721685 | 31.1446234635 | 753 | 504990 | -86.40 | 1.22 | 52.63 | 0.04 | 1.18 | 1595 |
| 2024-09-20 22:21:35.927 | MS1 | 121.4656750181 | 31.1446325766 | 753 | 504990 | -94.58 | 1.05 | 62.92 | 0.03 | 1.26 | 1587 |
| 2024-09-20 22:21:36.166 | MS1 | 121.4656675279 | 31.1446320410 | 753 | 504990 | -86.34 | 1.65 | 86.05 | 0.09 | 1.27 | 1567 |
| 2024-09-20 22:21:37.496 | MS1 | 121.4656662581 | 31.1446334183 | 753 | 504990 | -92.46 | 2.10 | 83.38 | 0.10 | 1.18 | 1600 |
| 2024-09-20 22:21:38.111 | MS1 | 121.4656716353 | 31.1446353751 | 753 | 504990 | -90.62 | 3.01 | 90.12 | 0.19 | 1.15 | 1569 |
| 2024-09-20 22:21:39.959 | MS1 | 121.4656708861 | 31.1446301889 | 753 | 504990 | -89.45 | 0.63 | 36.18 | 0.11 | 1.37 | 1571 |
| 2024-09-20 22:21:40.416 | MS1 | 121.4656727508 | 31.1446353567 | 753 | 504990 | -81.12 | 13.53 | 607.65 | 0.08 | 2.77 | 1584 |
| 2024-09-20 22:21:41.445 | MS1 | 121.4656632990 | 31.1446212346 | 753 | 504990 | -79.09 | 16.89 | 391.04 | 0.07 | 2.28 | 1582 |
| 2024-09-20 22:21:42.913 | MS1 | 121.4656728066 | 31.1446287139 | 753 | 504990 | -81.31 | 15.35 | 543.85 | 0.18 | 2.35 | 1571 |

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
| 3216946 | 3 | 121.4751328642 | 31.1478942114 | 48 | 7 | 3 | 42.5 | TDD | 506 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3244132 | 1 | 121.4719673836 | 31.1542633668 | 231 | 1 | 12 | 49.6 | TDD | 469 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3267997 | 4 | 121.4739772688 | 31.1474847642 | 100 | 8 | 6 | 26.7 | TDD | 813 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3277663 | 2 | 121.4685598444 | 31.1543181280 | 209 | 1 | 9 | 39.0 | TDD | 753 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.189 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.211 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.315 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.315 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244132 | 1 | 12.2386 | 5.5181 | -115.1601 | 12.6207 | 115.0982 | 0.0056 | 0.0158 |
| 2024_09_20 22:00 | 3277663 | 2 | 19.1607 | 10.8913 | -108.4919 | 5.8267 | 113.8571 | 0.0014 | 0.0067 |
| 2024_09_20 22:00 | 3216946 | 3 | 13.5241 | 8.6863 | -115.0608 | 16.5257 | 190.4940 | 0.0032 | 0.0150 |
| 2024_09_20 22:00 | 3267997 | 4 | 13.7964 | 8.8109 | -117.2735 | 9.9136 | 125.3620 | 0.0147 | 0.0025 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413194_AAFA57AB | 504990 | 469 | -85.8 | 504990 | 753 | -83.5 | 504990 | 813 | -85.9 | 504990 | 506 |
| MR_1774413194_C94DE512 | 504990 | 469 | -85.2 | 504990 | 753 | -82.7 | 504990 | 813 | -88.1 | 504990 | 506 |
| MR_1774413194_45F11F38 | 504990 | 753 | -85.4 | 504990 | 469 | -85.0 | 504990 | 813 | -86.7 | 504990 | 506 |
| MR_1774413194_9CBF44C5 | 504990 | 469 | -84.4 | 504990 | 753 | -83.6 | 504990 | 813 | -88.0 | 504990 | 506 |
| MR_1774413194_8FEBA82F | 504990 | 753 | -86.2 | 504990 | 469 | -84.5 | 504990 | 813 | -85.6 | 504990 | 506 |
| MR_1774413194_D0982EF6 | 504990 | 753 | -85.2 | 504990 | 469 | -85.7 | 504990 | 813 | -86.1 | 504990 | 506 |
| MR_1774413194_A5188CA6 | 504990 | 753 | -85.9 | 504990 | 469 | -84.7 | 504990 | 813 | -87.4 | 504990 | 506 |
| MR_1774413194_D9413386 | 504990 | 469 | -84.5 | 504990 | 753 | -84.0 | 504990 | 813 | -86.1 | 504990 | 506 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 97: `6101be3f-9fa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6101be3f-9fa1-4827-a946-4f0947448bab` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[97] topology](images/test_0097.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3216263_4
- `C2`: Press down the tilt angle of 3216263_4 by 3 degrees
- `C3`: Check test server and transmission issues
- `C4`: Lift the tilt angle of 3216263_4 by 3 degrees
- `C5`: Lift the tilt angle  of 3252829_1 by 10 degrees
- `C6`: Increase A3 Offset threshold for 3219391_2
- `C7`: Increase transmission power for 3216263_4
- `C8`: Decrease transmission power for 3216263_4
- `C9`: Adjust the azimuth of 3252829_1 by 50 degrees
- `C10`: Add neighbor relationship between 3252829_1 and 3219391_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219391_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Increase A3 Offset threshold for 3216263_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219391_2
- `C15`: Increase transmission power for 3219391_2
- `C16`: Decrease A3 Offset threshold for 3219391_2
- `C17`: Press down the tilt angle  of 3252829_1 by 10 degrees
- `C18`: Adjust the azimuth of 3216263_4 by 46 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216263_4
- `C20`: Add neighbor relationship between 3216263_4 and 3219391_2
- `C21`: Decrease transmission power for 3219391_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216263_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.976 | MS1 | 121.4656581895 | 31.1446294777 | 586 | 504990 | -90.71 | 15.62 | 314.53 | 0.06 | 2.46 | 1590 |
| 2024-09-20 22:21:32.881 | MS1 | 121.4656688828 | 31.1446275913 | 586 | 504990 | -89.20 | 16.26 | 536.75 | 0.18 | 2.01 | 1563 |
| 2024-09-20 22:21:33.583 | MS1 | 121.4656683868 | 31.1446219326 | 586 | 504990 | -88.02 | 14.02 | 507.15 | 0.08 | 2.46 | 1575 |
| 2024-09-20 22:21:34.823 | MS1 | 121.4656674434 | 31.1446366472 | 586 | 504990 | -85.18 | 16.57 | 68.08 | 0.13 | 2.34 | 1595 |
| 2024-09-20 22:21:35.412 | MS1 | 121.4656610557 | 31.1446210529 | 586 | 504990 | -86.13 | 17.56 | 76.74 | 0.08 | 2.11 | 1562 |
| 2024-09-20 22:21:36.574 | MS1 | 121.4656615825 | 31.1446236163 | 586 | 504990 | -86.43 | 16.92 | 83.41 | 0.07 | 2.55 | 1561 |
| 2024-09-20 22:21:37.747 | MS1 | 121.4656640529 | 31.1446203063 | 586 | 504990 | -90.63 | 11.79 | 79.80 | 0.09 | 2.39 | 1572 |
| 2024-09-20 22:21:38.427 | MS1 | 121.4656735561 | 31.1446191313 | 586 | 504990 | -91.90 | 9.30 | 81.77 | 0.04 | 2.20 | 1588 |
| 2024-09-20 22:21:39.265 | MS1 | 121.4656670550 | 31.1446355616 | 586 | 504990 | -89.09 | 12.07 | 86.89 | 0.06 | 2.39 | 1562 |
| 2024-09-20 22:21:40.405 | MS1 | 121.4656640138 | 31.1446239526 | 586 | 504990 | -92.95 | 10.90 | 429.98 | 0.17 | 2.35 | 1582 |
| 2024-09-20 22:21:41.983 | MS1 | 121.4656713047 | 31.1446348899 | 586 | 504990 | -89.85 | 11.44 | 420.40 | 0.05 | 2.99 | 1563 |
| 2024-09-20 22:21:42.894 | MS1 | 121.4656772697 | 31.1446355089 | 586 | 504990 | -93.96 | 8.01 | 406.16 | 0.09 | 2.50 | 1574 |

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
| 3214972 | 3 | 121.4728307351 | 31.1553415800 | 298 | 8 | 10 | 34.6 | TDD | 67 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3216263 | 4 | 121.4663046632 | 31.1531070987 | 230 | 1 | 5 | 36.9 | TDD | 586 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3219391 | 2 | 121.4741010917 | 31.1452778790 | 116 | 13 | 2 | 19.1 | TDD | 946 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3252829 | 1 | 121.4748477956 | 31.1481971447 | 325 | 9 | 7 | 33.5 | TDD | 456 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.573 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.597 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.709 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.709 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.448 | NREventA3 | measId:2;ServCellPCI:810;Se... |
| 2024-09-20 22:21:38.688 | NRHandoverAttempt | SourcePCI:810;SourceNR-ARFC... |
| 2024-09-20 22:21:38.719 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.732 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.854 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.854 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252829 | 1 | 6.7410 | 8.4866 | -114.8499 | 16.4339 | 188.7328 | 0.0055 | 0.0188 |
| 2024_09_20 22:00 | 3219391 | 2 | 6.2079 | 13.0854 | -114.1830 | 16.6751 | 90.1528 | 0.0184 | 0.0181 |
| 2024_09_20 22:00 | 3214972 | 3 | 17.6707 | 18.1769 | -117.3846 | 8.0738 | 121.9969 | 0.0039 | 0.0021 |
| 2024_09_20 22:00 | 3216263 | 4 | 94.2474 | 86.6530 | -117.8434 | 7.5247 | 119.7358 | 0.0091 | 0.0017 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414469_9CF5C2FA | 504990 | 586 | -86.1 | 504990 | 946 | -88.4 | 504990 | 456 | -100.3 | 504990 | 67 |
| MR_1774414469_5C38D9EC | 504990 | 586 | -86.7 | 504990 | 946 | -89.7 | 504990 | 456 | -98.3 | 504990 | 67 |
| MR_1774414469_F1C92654 | 504990 | 586 | -85.6 | 504990 | 946 | -90.0 | 504990 | 456 | -96.7 | 504990 | 67 |
| MR_1774414469_83288136 | 504990 | 586 | -83.9 | 504990 | 946 | -91.4 | 504990 | 456 | -98.7 | 504990 | 67 |
| MR_1774414469_7714A625 | 504990 | 586 | -83.3 | 504990 | 946 | -88.2 | 504990 | 456 | -97.4 | 504990 | 67 |
| MR_1774414469_D9EBDE14 | 504990 | 586 | -84.5 | 504990 | 946 | -90.5 | 504990 | 456 | -100.4 | 504990 | 67 |
| MR_1774414469_372CF7D2 | 504990 | 586 | -83.3 | 504990 | 946 | -90.4 | 504990 | 456 | -98.5 | 504990 | 67 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 98: `fb4d6986-5f5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fb4d6986-5f5b-4ff4-8642-08d5ec531524` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[98] topology](images/test_0098.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219354_3
- `C2`: Decrease transmission power for 3221258_1
- `C3`: Increase A3 Offset threshold for 3221258_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219354_3
- `C5`: Decrease A3 Offset threshold for 3221258_1
- `C6`: Adjust the azimuth of 3219354_3 by 49 degrees
- `C7`: Lift the tilt angle  of 3221258_1 by 10 degrees
- `C8`: Press down the tilt angle  of 3221258_1 by 10 degrees
- `C9`: Decrease A3 Offset threshold for 3219354_3
- `C10`: Increase transmission power for 3219354_3
- `C11`: Lift the tilt angle of 3219354_3 by 5 degrees
- `C12`: Adjust the azimuth of 3221258_1 by 50 degrees
- `C13`: Check test server and transmission issues
- `C14`: Add neighbor relationship between 3219354_3 and 3221258_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221258_1
- `C16`: Increase transmission power for 3221258_1
- `C17`: Decrease transmission power for 3219354_3
- `C18`: Add neighbor relationship between 3266517_2 and 3221258_1
- `C19`: Press down the tilt angle of 3219354_3 by 5 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221258_1
- `C21`: Increase A3 Offset threshold for 3219354_3
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.458 | MS1 | 121.4656637110 | 31.1446226969 | 124 | 504990 | -89.79 | 13.19 | 563.78 | 0.01 | 2.88 | 1575 |
| 2024-09-20 22:21:32.364 | MS1 | 121.4656750677 | 31.1446189270 | 124 | 504990 | -91.17 | 15.43 | 495.66 | 0.20 | 2.82 | 1566 |
| 2024-09-20 22:21:33.390 | MS1 | 121.4656746749 | 31.1446283951 | 124 | 504990 | -88.39 | 12.96 | 481.97 | 0.01 | 2.99 | 1560 |
| 2024-09-20 22:21:34.521 | MS1 | 121.4656756237 | 31.1446219792 | 124 | 504990 | -90.20 | 17.55 | 75.97 | 0.58 | 2.82 | 643 |
| 2024-09-20 22:21:35.960 | MS1 | 121.4656659913 | 31.1446281541 | 124 | 504990 | -89.66 | 13.58 | 40.96 | 0.52 | 2.42 | 634 |
| 2024-09-20 22:21:36.361 | MS1 | 121.4656684464 | 31.1446349811 | 124 | 504990 | -90.34 | 13.40 | 61.88 | 0.58 | 2.39 | 679 |
| 2024-09-20 22:21:37.584 | MS1 | 121.4656779856 | 31.1446195469 | 124 | 504990 | -93.45 | 9.11 | 84.62 | 0.52 | 2.21 | 659 |
| 2024-09-20 22:21:38.714 | MS1 | 121.4656603630 | 31.1446311422 | 124 | 504990 | -89.03 | 8.52 | 65.88 | 0.66 | 2.64 | 576 |
| 2024-09-20 22:21:39.533 | MS1 | 121.4656618519 | 31.1446190628 | 124 | 504990 | -91.24 | 7.54 | 99.41 | 0.66 | 2.12 | 535 |
| 2024-09-20 22:21:40.870 | MS1 | 121.4656707489 | 31.1446296045 | 124 | 504990 | -90.40 | 10.73 | 356.61 | 0.13 | 2.24 | 1587 |
| 2024-09-20 22:21:41.683 | MS1 | 121.4656746277 | 31.1446233117 | 124 | 504990 | -89.69 | 12.27 | 335.29 | 0.15 | 2.20 | 1599 |
| 2024-09-20 22:21:42.247 | MS1 | 121.4656659345 | 31.1446245650 | 124 | 504990 | -93.49 | 10.96 | 472.42 | 0.03 | 2.12 | 1576 |

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
| 3219354 | 3 | 121.4711918148 | 31.1451476388 | 313 | 0 | 7 | 48.8 | TDD | 124 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3221258 | 1 | 121.4689352393 | 31.1475464236 | 137 | 7 | 10 | 42.6 | TDD | 776 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3242479 | 4 | 121.4730636974 | 31.1496410556 | 24 | 12 | 11 | 44.2 | TDD | 333 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3266517 | 2 | 121.4703325743 | 31.1541704144 | 21 | 6 | 11 | 19.6 | TDD | 953 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.196 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.220 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.333 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.333 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.058 | NREventA3 | measId:2;ServCellPCI:340;Se... |
| 2024-09-20 22:21:38.298 | NRHandoverAttempt | SourcePCI:340;SourceNR-ARFC... |
| 2024-09-20 22:21:38.336 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.348 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.477 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.477 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221258 | 1 | 8.4836 | 6.7376 | -117.8329 | 16.7079 | 134.2726 | 0.0042 | 0.0065 |
| 2024_09_20 22:00 | 3266517 | 2 | 17.2643 | 13.6528 | -116.8034 | 13.7997 | 100.2231 | 0.0170 | 0.0052 |
| 2024_09_20 22:00 | 3219354 | 3 | 16.6340 | 13.6742 | -115.6572 | 9.8113 | 86.0376 | 0.0099 | 0.0155 |
| 2024_09_20 22:00 | 3242479 | 4 | 17.2210 | 12.3265 | -114.9719 | 5.4423 | 88.8198 | 0.0099 | 0.0056 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415483_8FE368BD | 504990 | 124 | -91.6 | 504990 | 776 | -94.9 | 504990 | 953 | -99.9 | 504990 | 333 |
| MR_1774415483_A0C5E090 | 504990 | 124 | -91.3 | 504990 | 776 | -93.1 | 504990 | 953 | -98.1 | 504990 | 333 |
| MR_1774415483_4F829608 | 504990 | 124 | -89.0 | 504990 | 776 | -92.6 | 504990 | 953 | -97.7 | 504990 | 333 |
| MR_1774415483_7A85A983 | 504990 | 124 | -91.4 | 504990 | 776 | -94.7 | 504990 | 953 | -99.6 | 504990 | 333 |
| MR_1774415483_9D6AC933 | 504990 | 124 | -90.1 | 504990 | 776 | -95.3 | 504990 | 953 | -97.7 | 504990 | 333 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 99: `5538b826-d1b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5538b826-d1b3-49a8-b40e-b157e0ad453f` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[99] topology](images/test_0099.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215629_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252265_3
- `C4`: Press down the tilt angle of 3215629_2 by 5 degrees
- `C5`: Press down the tilt angle  of 3252265_3 by 2 degrees
- `C6`: Increase A3 Offset threshold for 3252265_3
- `C7`: Add neighbor relationship between 3215629_2 and 3252265_3
- `C8`: Lift the tilt angle  of 3252265_3 by 2 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252265_3
- `C10`: Decrease A3 Offset threshold for 3215629_2
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease transmission power for 3252265_3
- `C13`: Adjust the azimuth of 3215629_2 by 50 degrees
- `C14`: Adjust the azimuth of 3252265_3 by 7 degrees
- `C15`: Add neighbor relationship between 3273659_9 and 3252265_3
- `C16`: Increase A3 Offset threshold for 3215629_2
- `C17`: Increase transmission power for 3215629_2
- `C18`: Increase transmission power for 3252265_3
- `C19`: Decrease A3 Offset threshold for 3252265_3
- `C20`: Decrease transmission power for 3215629_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215629_2
- `C22`: Lift the tilt angle of 3215629_2 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.317 | MS1 | 121.4656690465 | 31.1446263763 | 360 | 504990 | -93.25 | 11.60 | 431.06 | 0.07 | 2.20 | 1588 |
| 2024-09-20 22:21:32.379 | MS1 | 121.4656650395 | 31.1446310775 | 749 | 504990 | -95.07 | 11.33 | 502.64 | 0.19 | 2.89 | 1567 |
| 2024-09-20 22:21:33.155 | MS1 | 121.4656631402 | 31.1446300371 | 99 | 504990 | -94.11 | 13.05 | 368.65 | 0.06 | 2.87 | 1567 |
| 2024-09-20 22:21:34.146 | MS1 | 121.4656694810 | 31.1446331226 | 367 | 152650 | -88.07 | 6.65 | 86.53 | 0.20 | 1.63 | 910 |
| 2024-09-20 22:21:35.604 | MS1 | 121.4656590800 | 31.1446368778 | 124 | 152650 | -94.48 | 7.42 | 98.87 | 0.01 | 1.57 | 982 |
| 2024-09-20 22:21:36.753 | MS1 | 121.4656684134 | 31.1446188290 | 199 | 152650 | -88.56 | 3.89 | 100.38 | 0.03 | 1.85 | 958 |
| 2024-09-20 22:21:37.469 | MS1 | 121.4656731788 | 31.1446238863 | 646 | 152650 | -87.80 | 4.63 | 58.24 | 0.18 | 1.62 | 951 |
| 2024-09-20 22:21:38.119 | MS1 | 121.4656640521 | 31.1446268356 | 367 | 152650 | -93.55 | 2.25 | 86.52 | 0.08 | 1.76 | 948 |
| 2024-09-20 22:21:39.953 | MS1 | 121.4656640200 | 31.1446358665 | 124 | 152650 | -93.00 | 3.39 | 75.13 | 0.05 | 1.56 | 991 |
| 2024-09-20 22:21:40.454 | MS1 | 121.4656688112 | 31.1446241064 | 199 | 152650 | -94.06 | 4.99 | 80.34 | 0.04 | 2.33 | 1583 |
| 2024-09-20 22:21:41.395 | MS1 | 121.4656749615 | 31.1446325293 | 646 | 152650 | -89.74 | 4.51 | 53.12 | 0.15 | 2.14 | 1560 |
| 2024-09-20 22:21:42.575 | MS1 | 121.4656628850 | 31.1446199806 | 367 | 152650 | -93.40 | 7.30 | 77.95 | 0.16 | 2.23 | 1572 |

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
| 3215629 | 2 | 121.4738695175 | 31.1500363172 | 282 | 3 | 11 | 28.9 | TDD | 360 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3219320 | 1 | 121.4747619634 | 31.1502386726 | 243 | 2 | 10 | 5.3 | TDD | 99 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3230591 | 6 | 121.4671117159 | 31.1442675968 | 326 | 11 | 11 | 2.7 | TDD | 728 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3232961 | 10 | 121.4667098765 | 31.1507576894 | 218 | 8 | 6 | 25.0 | FDD | 426 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3238586 | 13 | 121.4727984981 | 31.1542233495 | 217 | 8 | 8 | 17.2 | FDD | 124 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3240433 | 8 | 121.4709600846 | 31.1500996318 | 135 | 12 | 0 | 21.3 | FDD | 646 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3242538 | 5 | 121.4687203301 | 31.1496423560 | 184 | 8 | 1 | 5.4 | TDD | 79 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3249323 | 4 | 121.4697026721 | 31.1452403365 | 50 | 2 | 3 | 6.9 | TDD | 749 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3252265 | 3 | 121.4722870893 | 31.1549006987 | 216 | 2 | 0 | 0.3 | TDD | 523 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3263030 | 12 | 121.4751092804 | 31.1452254195 | 160 | 3 | 12 | 27.1 | FDD | 19 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3263330 | 11 | 121.4687999708 | 31.1558003035 | 213 | 4 | 4 | 17.5 | FDD | 367 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3264602 | 7 | 121.4666143966 | 31.1469419185 | 326 | 5 | 5 | 4.0 | FDD | 704 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3273659 | 9 | 121.4708346369 | 31.1547733832 | 182 | 1 | 7 | 1.8 | FDD | 199 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |

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
| 2024-09-20 22:21:31.206 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.225 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.372 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.372 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.088 | NREventA2 | measId:1;ServCellPCI:522;Se... |
| 2024-09-20 22:21:35.197 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.481 | NREventA5 | measId:3;ServCellPCI:522;Se... |
| 2024-09-20 22:21:35.512 | NRHandoverAttempt | SourcePCI:522;SourceNR-ARFC... |
| 2024-09-20 22:21:35.543 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.554 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.682 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.682 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219320 | 1 | 8.3232 | 9.9317 | -115.2530 | 11.6975 | 117.0862 | 0.0149 | 0.0197 |
| 2024_09_20 22:00 | 3215629 | 2 | 10.0879 | 13.9256 | -115.0357 | 6.2438 | 152.0408 | 0.0022 | 0.0020 |
| 2024_09_20 22:00 | 3252265 | 3 | 9.3317 | 13.8429 | -117.5074 | 19.0310 | 119.4267 | 0.0033 | 0.0033 |
| 2024_09_20 22:00 | 3249323 | 4 | 11.4027 | 10.7684 | -115.3086 | 14.4316 | 198.7912 | 0.0108 | 0.0040 |
| 2024_09_20 22:00 | 3242538 | 5 | 8.0237 | 14.1347 | -115.5160 | 15.4447 | 84.8354 | 0.0122 | 0.0183 |
| 2024_09_20 22:00 | 3230591 | 6 | 8.9489 | 14.0471 | -114.6026 | 17.4086 | 103.6999 | 0.0121 | 0.0076 |
| 2024_09_20 22:00 | 3264602 | 7 | 14.9221 | 5.0983 | -117.1308 | 3.4319 | 54.5236 | 0.0013 | 0.0067 |
| 2024_09_20 22:00 | 3240433 | 8 | 15.3794 | 16.9879 | -115.3988 | 4.9195 | 25.4236 | 0.0170 | 0.0146 |
| 2024_09_20 22:00 | 3273659 | 9 | 16.2042 | 6.9224 | -115.4407 | 4.4299 | 25.2266 | 0.0060 | 0.0122 |
| 2024_09_20 22:00 | 3232961 | 10 | 7.1010 | 5.0605 | -114.0434 | 4.1622 | 55.9048 | 0.0022 | 0.0036 |
| 2024_09_20 22:00 | 3263330 | 11 | 8.9886 | 18.5421 | -117.5565 | 3.6109 | 53.5265 | 0.0020 | 0.0040 |
| 2024_09_20 22:00 | 3263030 | 12 | 8.5766 | 10.4896 | -114.6944 | 4.1750 | 38.4749 | 0.0090 | 0.0038 |
| 2024_09_20 22:00 | 3238586 | 13 | 19.5765 | 12.9667 | -114.8893 | 4.6062 | 21.9668 | 0.0124 | 0.0068 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416944_C976536C | 152650 | 367 | -88.4 | 152650 | 426 | -95.3 | 152650 | 704 | -93.9 | 152650 | 19 |
| MR_1774416944_4BDC2F4F | 504990 | 99 | -95.8 | 504990 | 523 | -93.4 | 504990 | 79 | -97.8 | 504990 | 728 |
| MR_1774416944_D02B158E | 152650 | 367 | -88.2 | 152650 | 426 | -95.0 | 152650 | 704 | -95.3 | 152650 | 19 |
| MR_1774416944_CE04B3C3 | 504990 | 99 | -95.2 | 504990 | 523 | -94.0 | 504990 | 79 | -98.8 | 504990 | 728 |
| MR_1774416944_602BD359 | 152650 | 367 | -89.7 | 152650 | 426 | -93.4 | 152650 | 704 | -94.9 | 152650 | 19 |
| MR_1774416944_6E5D6C0C | 152650 | 367 | -89.8 | 152650 | 426 | -95.8 | 152650 | 704 | -92.4 | 152650 | 19 |

> *... 2개 열 생략 (전체 14열)*

---
