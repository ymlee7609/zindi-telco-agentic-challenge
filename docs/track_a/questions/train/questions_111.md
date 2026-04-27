# Track A 문제 분석 — train[1100]~train[1109]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1100] ~ train[1109] (10개)

## 목차

1. [문제 1100: `b30689ce-fdc...`](#1100) — single-answer, 정답: C20
2. [문제 1101: `6bd42704-e9e...`](#1101) — single-answer, 정답: C6
3. [문제 1102: `9464802a-a57...`](#1102) — single-answer, 정답: C22
4. [문제 1103: `d43a2570-4c2...`](#1103) — single-answer, 정답: C4
5. [문제 1104: `ffb19e40-9a2...`](#1104) — single-answer, 정답: C6
6. [문제 1105: `a9bf9e81-ea1...`](#1105) — single-answer, 정답: C11
7. [문제 1106: `dcccaa46-65f...`](#1106) — single-answer, 정답: C12
8. [문제 1107: `ca7c2042-094...`](#1107) — single-answer, 정답: C7
9. [문제 1108: `244ef5cf-4a1...`](#1108) — single-answer, 정답: C4
10. [문제 1109: `40ba7502-3be...`](#1109) — single-answer, 정답: C11

---

### 문제 1100: `b30689ce-fdc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b30689ce-fdcb-4a84-87f3-fc070cb05bcf` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225293_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1100] topology](images/train_1100.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3225293_4 and 3226021_3
- `C2`: Decrease transmission power for 3226021_3
- `C3`: Lift the tilt angle of 3225293_4 by 1 degrees
- `C4`: Increase transmission power for 3225293_4
- `C5`: Press down the tilt angle  of 3226021_3 by 4 degrees
- `C6`: Increase A3 Offset threshold for 3226021_3
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease A3 Offset threshold for 3225293_4
- `C9`: Adjust the azimuth of 3225293_4 by 15 degrees
- `C10`: Decrease transmission power for 3225293_4
- `C11`: Check test server and transmission issues
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225293_4
- `C13`: Press down the tilt angle of 3225293_4 by 1 degrees
- `C14`: Add neighbor relationship between 3264832_7 and 3226021_3
- `C15`: Increase transmission power for 3226021_3
- `C16`: Decrease A3 Offset threshold for 3226021_3
- `C17`: Increase A3 Offset threshold for 3225293_4
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226021_3
- `C19`: Lift the tilt angle  of 3226021_3 by 4 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225293_4 **← 정답**
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226021_3
- `C22`: Adjust the azimuth of 3226021_3 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.875 | MS1 | 121.4656729621 | 31.1446363693 | 49 | 504990 | -95.80 | 10.12 | 331.04 | 0.18 | 2.52 | 1600 |
| 2024-09-20 22:21:32.622 | MS1 | 121.4656583988 | 31.1446324303 | 803 | 504990 | -95.66 | 10.73 | 417.32 | 0.17 | 2.16 | 1566 |
| 2024-09-20 22:21:33.581 | MS1 | 121.4656583884 | 31.1446360546 | 131 | 504990 | -95.54 | 13.39 | 568.80 | 0.18 | 2.85 | 1593 |
| 2024-09-20 22:21:34.386 | MS1 | 121.4656699370 | 31.1446290192 | 631 | 152650 | -92.51 | 7.73 | 69.58 | 0.17 | 1.94 | 924 |
| 2024-09-20 22:21:35.113 | MS1 | 121.4656583366 | 31.1446358775 | 533 | 152650 | -94.17 | 3.46 | 90.57 | 0.09 | 1.87 | 917 |
| 2024-09-20 22:21:36.497 | MS1 | 121.4656612652 | 31.1446305993 | 450 | 152650 | -89.33 | 5.28 | 79.54 | 0.07 | 1.70 | 935 |
| 2024-09-20 22:21:37.305 | MS1 | 121.4656665971 | 31.1446212579 | 51 | 152650 | -87.26 | 3.41 | 62.73 | 0.10 | 1.77 | 954 |
| 2024-09-20 22:21:38.828 | MS1 | 121.4656690441 | 31.1446242040 | 631 | 152650 | -89.42 | 2.17 | 53.75 | 0.15 | 1.71 | 927 |
| 2024-09-20 22:21:39.605 | MS1 | 121.4656767903 | 31.1446260731 | 533 | 152650 | -90.30 | 7.84 | 62.05 | 0.05 | 1.61 | 984 |
| 2024-09-20 22:21:40.401 | MS1 | 121.4656608680 | 31.1446226005 | 450 | 152650 | -90.94 | 2.24 | 82.80 | 0.10 | 2.90 | 1588 |
| 2024-09-20 22:21:41.329 | MS1 | 121.4656773976 | 31.1446287968 | 51 | 152650 | -91.35 | 4.79 | 48.94 | 0.01 | 2.15 | 1563 |
| 2024-09-20 22:21:42.237 | MS1 | 121.4656765993 | 31.1446311885 | 631 | 152650 | -93.24 | 3.43 | 53.88 | 0.20 | 2.46 | 1584 |

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
| 3216910 | 11 | 121.4689863496 | 31.1485623860 | 228 | 5 | 5 | 1.3 | FDD | 51 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3219754 | 12 | 121.4658745638 | 31.1498022978 | 353 | 13 | 5 | 18.2 | FDD | 533 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3222380 | 5 | 121.4660934814 | 31.1521122200 | 277 | 7 | 2 | 16.9 | TDD | 980 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3225293 | 4 | 121.4685695095 | 31.1521979650 | 213 | 0 | 3 | 15.5 | TDD | 49 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3226021 | 3 | 121.4649418093 | 31.1468163096 | 169 | 1 | 1 | 12.2 | TDD | 842 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3233407 | 8 | 121.4706916868 | 31.1530775976 | 206 | 14 | 11 | 8.6 | FDD | 423 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3242220 | 1 | 121.4657412268 | 31.1454298973 | 350 | 0 | 3 | 15.1 | TDD | 803 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3248622 | 6 | 121.4712962973 | 31.1511251180 | 49 | 7 | 9 | 4.9 | TDD | 94 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3257375 | 13 | 121.4720748446 | 31.1555306428 | 164 | 0 | 3 | 2.9 | FDD | 631 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3257923 | 2 | 121.4759408159 | 31.1544800385 | 250 | 3 | 4 | 3.8 | TDD | 131 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3264832 | 7 | 121.4699531829 | 31.1455599967 | 117 | 2 | 3 | 11.4 | FDD | 450 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3265595 | 9 | 121.4702221732 | 31.1558851734 | 271 | 8 | 6 | 4.4 | FDD | 171 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3275869 | 10 | 121.4748145834 | 31.1481887721 | 153 | 2 | 1 | 21.0 | FDD | 594 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |

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
| 2024-09-20 22:21:31.156 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.284 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.284 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.014 | NREventA2 | measId:1;ServCellPCI:738;Se... |
| 2024-09-20 22:21:35.156 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.378 | NREventA5 | measId:3;ServCellPCI:738;Se... |
| 2024-09-20 22:21:35.425 | NRHandoverAttempt | SourcePCI:738;SourceNR-ARFC... |
| 2024-09-20 22:21:35.467 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.477 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.581 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.581 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242220 | 1 | 7.0065 | 19.6819 | -116.0600 | 18.5564 | 107.0453 | 0.0050 | 0.0032 |
| 2024_09_20 22:00 | 3257923 | 2 | 7.9598 | 10.0710 | -115.2675 | 13.3096 | 167.0310 | 0.0021 | 0.0019 |
| 2024_09_20 22:00 | 3226021 | 3 | 9.7597 | 18.5552 | -116.2278 | 8.1759 | 191.5224 | 0.0124 | 0.0103 |
| 2024_09_20 22:00 | 3225293 | 4 | 8.0608 | 9.2051 | -116.1322 | 18.1675 | 142.5154 | 0.0168 | 0.0174 |
| 2024_09_20 22:00 | 3222380 | 5 | 11.7616 | 18.0331 | -117.6476 | 8.9844 | 182.2142 | 0.0084 | 0.0052 |
| 2024_09_20 22:00 | 3248622 | 6 | 19.0326 | 8.0026 | -116.3416 | 15.0357 | 185.1762 | 0.0017 | 0.0148 |
| 2024_09_20 22:00 | 3264832 | 7 | 7.9501 | 12.2452 | -117.2396 | 3.2279 | 46.0464 | 0.0097 | 0.0102 |
| 2024_09_20 22:00 | 3233407 | 8 | 9.1145 | 11.5215 | -117.2585 | 4.0914 | 20.3959 | 0.0078 | 0.0179 |
| 2024_09_20 22:00 | 3265595 | 9 | 14.4036 | 8.5590 | -115.8245 | 4.4087 | 33.7945 | 0.0099 | 0.0144 |
| 2024_09_20 22:00 | 3275869 | 10 | 10.3161 | 18.8887 | -117.5921 | 3.9473 | 50.9587 | 0.0062 | 0.0143 |
| 2024_09_20 22:00 | 3216910 | 11 | 14.7889 | 9.1389 | -115.0777 | 4.2642 | 28.9896 | 0.0063 | 0.0001 |
| 2024_09_20 22:00 | 3219754 | 12 | 15.4623 | 13.4166 | -114.6905 | 4.5239 | 54.9252 | 0.0152 | 0.0013 |
| 2024_09_20 22:00 | 3257375 | 13 | 5.1335 | 16.9499 | -115.6638 | 3.7396 | 59.4516 | 0.0038 | 0.0116 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412792_42B89B15 | 504990 | 131 | -94.0 | 504990 | 842 | -97.9 | 504990 | 94 | -103.8 | 504990 | 980 |
| MR_1774412792_B6A08365 | 504990 | 131 | -95.3 | 504990 | 842 | -100.3 | 504990 | 94 | -102.1 | 504990 | 980 |
| MR_1774412792_BCB58258 | 504990 | 131 | -96.4 | 504990 | 842 | -100.2 | 504990 | 94 | -104.6 | 504990 | 980 |
| MR_1774412792_293532AA | 152650 | 631 | -92.5 | 152650 | 171 | -98.7 | 152650 | 594 | -101.5 | 152650 | 423 |
| MR_1774412792_36D56FAE | 152650 | 631 | -93.2 | 152650 | 171 | -96.4 | 152650 | 594 | -99.8 | 152650 | 423 |
| MR_1774412792_0523EBC1 | 504990 | 131 | -96.3 | 504990 | 842 | -97.7 | 504990 | 94 | -103.3 | 504990 | 980 |
| MR_1774412792_4CF6E26C | 152650 | 631 | -91.3 | 152650 | 171 | -97.3 | 152650 | 594 | -102.8 | 152650 | 423 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1101: `6bd42704-e9e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6bd42704-e9eb-4083-9086-3c94965d8b51` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3267708_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1101] topology](images/train_1101.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3232971_4
- `C2`: Increase transmission power for 3232971_4
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232971_4
- `C5`: Press down the tilt angle  of 3232971_4 by 10 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267708_3 **← 정답**
- `C7`: Check test server and transmission issues
- `C8`: Increase A3 Offset threshold for 3267708_3
- `C9`: Decrease transmission power for 3267708_3
- `C10`: Decrease A3 Offset threshold for 3232971_4
- `C11`: Adjust the azimuth of 3232971_4 by 50 degrees
- `C12`: Increase transmission power for 3267708_3
- `C13`: Lift the tilt angle of 3267708_3 by 4 degrees
- `C14`: Decrease A3 Offset threshold for 3267708_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267708_3
- `C16`: Lift the tilt angle  of 3232971_4 by 10 degrees
- `C17`: Increase A3 Offset threshold for 3232971_4
- `C18`: Add neighbor relationship between 3267708_3 and 3232971_4
- `C19`: Press down the tilt angle of 3267708_3 by 4 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232971_4
- `C21`: Adjust the azimuth of 3267708_3 by 17 degrees
- `C22`: Add neighbor relationship between 3243295_2 and 3232971_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.308 | MS1 | 121.4656658524 | 31.1446237135 | 502 | 504990 | -91.90 | 12.66 | 322.45 | 0.03 | 2.85 | 1572 |
| 2024-09-20 22:21:32.743 | MS1 | 121.4656693061 | 31.1446277459 | 502 | 504990 | -85.96 | 12.85 | 411.44 | 0.08 | 2.78 | 1588 |
| 2024-09-20 22:21:33.777 | MS1 | 121.4656653965 | 31.1446194146 | 502 | 504990 | -90.30 | 14.14 | 420.27 | 0.16 | 2.15 | 1578 |
| 2024-09-20 22:21:34.535 | MS1 | 121.4656580708 | 31.1446194203 | 502 | 504990 | -90.46 | 16.72 | 77.22 | 0.58 | 2.79 | 519 |
| 2024-09-20 22:21:35.237 | MS1 | 121.4656638751 | 31.1446273529 | 502 | 504990 | -85.68 | 15.98 | 79.07 | 0.69 | 2.87 | 604 |
| 2024-09-20 22:21:36.215 | MS1 | 121.4656643429 | 31.1446272024 | 502 | 504990 | -87.93 | 15.80 | 77.44 | 0.64 | 2.80 | 654 |
| 2024-09-20 22:21:37.596 | MS1 | 121.4656771746 | 31.1446235803 | 502 | 504990 | -90.87 | 11.81 | 48.83 | 0.56 | 2.16 | 516 |
| 2024-09-20 22:21:38.167 | MS1 | 121.4656612261 | 31.1446335314 | 502 | 504990 | -89.49 | 7.39 | 59.47 | 0.54 | 2.47 | 578 |
| 2024-09-20 22:21:39.373 | MS1 | 121.4656617460 | 31.1446378715 | 502 | 504990 | -90.42 | 7.86 | 87.60 | 0.67 | 2.43 | 675 |
| 2024-09-20 22:21:40.284 | MS1 | 121.4656598881 | 31.1446189711 | 502 | 504990 | -91.52 | 12.92 | 467.77 | 0.14 | 2.19 | 1568 |
| 2024-09-20 22:21:41.331 | MS1 | 121.4656663556 | 31.1446284001 | 502 | 504990 | -90.54 | 9.16 | 353.38 | 0.04 | 2.95 | 1561 |
| 2024-09-20 22:21:42.623 | MS1 | 121.4656763430 | 31.1446275089 | 502 | 504990 | -92.06 | 7.56 | 332.88 | 0.04 | 2.67 | 1574 |

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
| 3232262 | 1 | 121.4652099917 | 31.1505619704 | 309 | 4 | 0 | 43.6 | TDD | 344 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3232971 | 4 | 121.4648071277 | 31.1528547837 | 10 | 13 | 12 | 40.5 | TDD | 230 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3243295 | 2 | 121.4647019783 | 31.1443706356 | 255 | 2 | 12 | 25.8 | TDD | 906 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3267708 | 3 | 121.4654424995 | 31.1543975056 | 162 | 2 | 12 | 35.2 | TDD | 502 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.094 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.112 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.231 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.231 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.962 | NREventA3 | measId:2;ServCellPCI:212;Se... |
| 2024-09-20 22:21:38.202 | NRHandoverAttempt | SourcePCI:212;SourceNR-ARFC... |
| 2024-09-20 22:21:38.241 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.254 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.356 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.356 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232262 | 1 | 14.2678 | 13.4185 | -114.8000 | 15.5114 | 140.4461 | 0.0177 | 0.0162 |
| 2024_09_20 22:00 | 3243295 | 2 | 17.8656 | 7.4517 | -117.3710 | 13.1688 | 92.8077 | 0.0127 | 0.0122 |
| 2024_09_20 22:00 | 3267708 | 3 | 13.7843 | 16.2409 | -115.1859 | 16.7036 | 195.7387 | 0.0056 | 0.0135 |
| 2024_09_20 22:00 | 3232971 | 4 | 5.1215 | 5.6585 | -114.6139 | 19.0060 | 86.8099 | 0.0057 | 0.0000 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413840_289A14E9 | 504990 | 502 | -89.0 | 504990 | 230 | -94.3 | 504990 | 906 | -100.3 | 504990 | 344 |
| MR_1774413840_942DF38E | 504990 | 502 | -89.9 | 504990 | 230 | -94.8 | 504990 | 906 | -103.0 | 504990 | 344 |
| MR_1774413840_7B4774D3 | 504990 | 502 | -88.5 | 504990 | 230 | -95.0 | 504990 | 906 | -100.3 | 504990 | 344 |
| MR_1774413840_DEA60B26 | 504990 | 502 | -91.3 | 504990 | 230 | -95.3 | 504990 | 906 | -100.7 | 504990 | 344 |
| MR_1774413840_B8EB96C2 | 504990 | 502 | -91.3 | 504990 | 230 | -95.8 | 504990 | 906 | -103.0 | 504990 | 344 |
| MR_1774413840_11E818A7 | 504990 | 502 | -91.3 | 504990 | 230 | -94.8 | 504990 | 906 | -100.9 | 504990 | 344 |
| MR_1774413840_614D9F0A | 504990 | 502 | -90.9 | 504990 | 230 | -95.4 | 504990 | 906 | -101.6 | 504990 | 344 |
| MR_1774413840_CCFC36E0 | 504990 | 502 | -88.9 | 504990 | 230 | -95.7 | 504990 | 906 | -101.3 | 504990 | 344 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1102: `9464802a-a57...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9464802a-a576-4ff6-a6cb-85f2421c6514` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Lift the tilt angle  of 3263276_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1102] topology](images/train_1102.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3263276_4 and 3235855_1
- `C2`: Increase A3 Offset threshold for 3265578_2
- `C3`: Decrease transmission power for 3235855_1
- `C4`: Adjust the azimuth of 3263276_4 by 21 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Check test server and transmission issues
- `C7`: Increase A3 Offset threshold for 3235855_1
- `C8`: Increase transmission power for 3265578_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235855_1
- `C10`: Press down the tilt angle  of 3263276_4 by 10 degrees
- `C11`: Press down the tilt angle of 3265578_2 by 3 degrees
- `C12`: Increase transmission power for 3235855_1
- `C13`: Decrease A3 Offset threshold for 3235855_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235855_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265578_2
- `C16`: Decrease A3 Offset threshold for 3265578_2
- `C17`: Adjust the azimuth of 3265578_2 by 22 degrees
- `C18`: Lift the tilt angle of 3265578_2 by 3 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265578_2
- `C20`: Add neighbor relationship between 3265578_2 and 3235855_1
- `C21`: Decrease transmission power for 3265578_2
- `C22`: Lift the tilt angle  of 3263276_4 by 10 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.701 | MS1 | 121.4656734424 | 31.1446227830 | 169 | 504990 | -87.65 | 16.53 | 308.71 | 0.08 | 2.68 | 1589 |
| 2024-09-20 22:21:32.472 | MS1 | 121.4656620325 | 31.1446213746 | 169 | 504990 | -87.04 | 15.51 | 433.67 | 0.01 | 2.32 | 1587 |
| 2024-09-20 22:21:33.175 | MS1 | 121.4656753638 | 31.1446277410 | 169 | 504990 | -85.13 | 17.34 | 370.18 | 0.09 | 2.36 | 1596 |
| 2024-09-20 22:21:34.797 | MS1 | 121.4656664606 | 31.1446322174 | 169 | 504990 | -87.11 | 12.54 | 63.95 | 0.11 | 2.80 | 1562 |
| 2024-09-20 22:21:35.630 | MS1 | 121.4656682553 | 31.1446336559 | 169 | 504990 | -91.60 | 12.75 | 53.01 | 0.02 | 2.72 | 1586 |
| 2024-09-20 22:21:36.676 | MS1 | 121.4656599154 | 31.1446377853 | 169 | 504990 | -89.94 | 16.78 | 83.21 | 0.08 | 2.02 | 1584 |
| 2024-09-20 22:21:37.624 | MS1 | 121.4656646247 | 31.1446356170 | 169 | 504990 | -89.13 | 9.21 | 53.27 | 0.05 | 2.01 | 1595 |
| 2024-09-20 22:21:38.459 | MS1 | 121.4656653139 | 31.1446371009 | 169 | 504990 | -92.88 | 11.10 | 99.24 | 0.09 | 2.10 | 1598 |
| 2024-09-20 22:21:39.344 | MS1 | 121.4656652528 | 31.1446247813 | 169 | 504990 | -93.75 | 10.90 | 86.48 | 0.14 | 2.09 | 1564 |
| 2024-09-20 22:21:40.176 | MS1 | 121.4656717861 | 31.1446234962 | 169 | 504990 | -92.11 | 9.15 | 351.12 | 0.16 | 2.97 | 1565 |
| 2024-09-20 22:21:41.431 | MS1 | 121.4656682067 | 31.1446365418 | 169 | 504990 | -91.79 | 10.69 | 451.84 | 0.16 | 2.52 | 1599 |
| 2024-09-20 22:21:42.579 | MS1 | 121.4656716660 | 31.1446218154 | 169 | 504990 | -92.24 | 9.46 | 346.28 | 0.13 | 2.79 | 1572 |

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
| 3219441 | 3 | 121.4713726825 | 31.1443394884 | 189 | 1 | 11 | 36.5 | TDD | 363 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3235855 | 1 | 121.4733551472 | 31.1490715039 | 215 | 9 | 2 | 25.8 | TDD | 792 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3263276 | 4 | 121.4664434730 | 31.1470418486 | 17 | 14 | 9 | 36.8 | TDD | 469 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3265578 | 2 | 121.4727369907 | 31.1548437845 | 233 | 1 | 3 | 42.4 | TDD | 169 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.384 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.407 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.544 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.544 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.219 | NREventA3 | measId:2;ServCellPCI:117;Se... |
| 2024-09-20 22:21:38.459 | NRHandoverAttempt | SourcePCI:117;SourceNR-ARFC... |
| 2024-09-20 22:21:38.509 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.523 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.647 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.647 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235855 | 1 | 16.3051 | 18.8994 | -116.8617 | 6.3780 | 154.6507 | 0.0108 | 0.0073 |
| 2024_09_20 22:00 | 3265578 | 2 | 86.1879 | 82.3194 | -116.3012 | 6.0255 | 181.3452 | 0.0061 | 0.0126 |
| 2024_09_20 22:00 | 3219441 | 3 | 8.8849 | 14.7198 | -117.2160 | 7.4467 | 105.2711 | 0.0159 | 0.0093 |
| 2024_09_20 22:00 | 3263276 | 4 | 5.4221 | 15.2560 | -117.7721 | 5.4981 | 153.2179 | 0.0019 | 0.0176 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417204_14C68FAA | 504990 | 169 | -85.2 | 504990 | 792 | -96.3 | 504990 | 469 | -99.7 | 504990 | 363 |
| MR_1774417204_BB7C29B8 | 504990 | 169 | -87.8 | 504990 | 792 | -96.2 | 504990 | 469 | -97.7 | 504990 | 363 |
| MR_1774417204_33E867D6 | 504990 | 169 | -85.5 | 504990 | 792 | -96.8 | 504990 | 469 | -96.6 | 504990 | 363 |
| MR_1774417204_05864389 | 504990 | 169 | -85.6 | 504990 | 792 | -94.9 | 504990 | 469 | -99.5 | 504990 | 363 |
| MR_1774417204_77810900 | 504990 | 169 | -87.5 | 504990 | 792 | -95.2 | 504990 | 469 | -99.2 | 504990 | 363 |
| MR_1774417204_E42A00A8 | 504990 | 169 | -88.1 | 504990 | 792 | -95.2 | 504990 | 469 | -96.0 | 504990 | 363 |
| MR_1774417204_FBB3E9F1 | 504990 | 169 | -88.0 | 504990 | 792 | -93.9 | 504990 | 469 | -99.3 | 504990 | 363 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1103: `d43a2570-4c2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d43a2570-4c22-46df-b613-da3a418e1fb9` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3250537_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1103] topology](images/train_1103.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3250537_2 by 14 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248146_1
- `C3`: Lift the tilt angle of 3250537_2 by 6 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250537_2 **← 정답**
- `C5`: Add neighbor relationship between 3250537_2 and 3248146_1
- `C6`: Decrease transmission power for 3248146_1
- `C7`: Increase A3 Offset threshold for 3250537_2
- `C8`: Decrease transmission power for 3250537_2
- `C9`: Adjust the azimuth of 3248146_1 by 50 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248146_1
- `C11`: Press down the tilt angle  of 3248146_1 by 2 degrees
- `C12`: Lift the tilt angle  of 3248146_1 by 2 degrees
- `C13`: Increase A3 Offset threshold for 3248146_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease A3 Offset threshold for 3250537_2
- `C16`: Decrease A3 Offset threshold for 3248146_1
- `C17`: Check test server and transmission issues
- `C18`: Press down the tilt angle of 3250537_2 by 6 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250537_2
- `C20`: Add neighbor relationship between 3263690_4 and 3248146_1
- `C21`: Increase transmission power for 3248146_1
- `C22`: Increase transmission power for 3250537_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.461 | MS1 | 121.4656678945 | 31.1446364051 | 693 | 504990 | -85.46 | 14.23 | 399.81 | 0.11 | 2.06 | 1571 |
| 2024-09-20 22:21:32.124 | MS1 | 121.4656716897 | 31.1446198061 | 693 | 504990 | -90.38 | 14.29 | 359.63 | 0.15 | 2.95 | 1589 |
| 2024-09-20 22:21:33.459 | MS1 | 121.4656733224 | 31.1446281546 | 693 | 504990 | -88.49 | 15.46 | 452.87 | 0.17 | 2.88 | 1597 |
| 2024-09-20 22:21:34.409 | MS1 | 121.4656775151 | 31.1446331656 | 693 | 504990 | -86.77 | 12.32 | 77.11 | 0.51 | 2.52 | 565 |
| 2024-09-20 22:21:35.787 | MS1 | 121.4656602419 | 31.1446370142 | 693 | 504990 | -90.70 | 15.14 | 82.16 | 0.67 | 2.16 | 598 |
| 2024-09-20 22:21:36.596 | MS1 | 121.4656728096 | 31.1446189575 | 693 | 504990 | -90.93 | 16.48 | 96.31 | 0.54 | 2.72 | 677 |
| 2024-09-20 22:21:37.525 | MS1 | 121.4656733897 | 31.1446319239 | 693 | 504990 | -91.63 | 9.17 | 52.81 | 0.58 | 2.48 | 614 |
| 2024-09-20 22:21:38.696 | MS1 | 121.4656693644 | 31.1446254413 | 693 | 504990 | -92.75 | 12.29 | 78.16 | 0.57 | 2.07 | 674 |
| 2024-09-20 22:21:39.497 | MS1 | 121.4656753081 | 31.1446271995 | 693 | 504990 | -89.62 | 12.22 | 74.75 | 0.59 | 2.40 | 610 |
| 2024-09-20 22:21:40.555 | MS1 | 121.4656615804 | 31.1446315717 | 693 | 504990 | -89.70 | 10.00 | 406.44 | 0.07 | 2.56 | 1577 |
| 2024-09-20 22:21:41.417 | MS1 | 121.4656768810 | 31.1446334990 | 693 | 504990 | -93.70 | 11.50 | 344.31 | 0.07 | 2.62 | 1563 |
| 2024-09-20 22:21:42.209 | MS1 | 121.4656681041 | 31.1446286002 | 693 | 504990 | -92.74 | 8.59 | 348.62 | 0.04 | 2.15 | 1571 |

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
| 3248146 | 1 | 121.4657754161 | 31.1559690444 | 108 | 0 | 12 | 45.6 | TDD | 759 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3250537 | 2 | 121.4707854193 | 31.1468576716 | 257 | 4 | 0 | 15.5 | TDD | 693 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3263690 | 4 | 121.4662452298 | 31.1507171786 | 282 | 10 | 2 | 29.0 | TDD | 815 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3269182 | 3 | 121.4727135441 | 31.1460858728 | 24 | 10 | 11 | 41.9 | TDD | 38 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.245 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.262 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.389 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.389 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.058 | NREventA3 | measId:2;ServCellPCI:433;Se... |
| 2024-09-20 22:21:38.298 | NRHandoverAttempt | SourcePCI:433;SourceNR-ARFC... |
| 2024-09-20 22:21:38.328 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.340 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.473 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.473 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248146 | 1 | 14.3019 | 16.4801 | -115.5169 | 12.5450 | 117.2634 | 0.0188 | 0.0011 |
| 2024_09_20 22:00 | 3250537 | 2 | 19.7415 | 18.6259 | -115.8767 | 13.9562 | 128.3457 | 0.0161 | 0.0031 |
| 2024_09_20 22:00 | 3269182 | 3 | 8.4372 | 18.5046 | -114.6658 | 14.1213 | 150.5743 | 0.0173 | 0.0094 |
| 2024_09_20 22:00 | 3263690 | 4 | 5.6530 | 17.1797 | -117.3967 | 16.8820 | 170.1921 | 0.0200 | 0.0108 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417079_4B1D1D5F | 504990 | 693 | -85.4 | 504990 | 759 | -92.8 | 504990 | 815 | -92.6 | 504990 | 38 |
| MR_1774417079_E15BA478 | 504990 | 693 | -86.4 | 504990 | 759 | -90.9 | 504990 | 815 | -93.8 | 504990 | 38 |
| MR_1774417079_9A8D7274 | 504990 | 693 | -85.9 | 504990 | 759 | -91.0 | 504990 | 815 | -93.8 | 504990 | 38 |
| MR_1774417079_6438CE97 | 504990 | 693 | -85.5 | 504990 | 759 | -92.9 | 504990 | 815 | -93.1 | 504990 | 38 |
| MR_1774417079_331ABE13 | 504990 | 693 | -87.9 | 504990 | 759 | -94.2 | 504990 | 815 | -91.9 | 504990 | 38 |
| MR_1774417079_F5BEE78F | 504990 | 693 | -86.4 | 504990 | 759 | -92.0 | 504990 | 815 | -94.5 | 504990 | 38 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1104: `ffb19e40-9a2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ffb19e40-9a2d-4d92-97eb-f65dfdf72f01` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease A3 Offset threshold for 3236939_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1104] topology](images/train_1104.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3236939_4 by 3 degrees
- `C2`: Increase transmission power for 3219634_1
- `C3`: Lift the tilt angle  of 3219634_1 by 7 degrees
- `C4`: Decrease A3 Offset threshold for 3219634_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236939_4
- `C6`: Decrease A3 Offset threshold for 3236939_4 **← 정답**
- `C7`: Decrease transmission power for 3236939_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219634_1
- `C9`: Adjust the azimuth of 3236939_4 by 42 degrees
- `C10`: Add neighbor relationship between 3236939_4 and 3219634_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236939_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219634_1
- `C14`: Increase transmission power for 3236939_4
- `C15`: Add neighbor relationship between 3211049_2 and 3219634_1
- `C16`: Adjust the azimuth of 3219634_1 by 50 degrees
- `C17`: Check test server and transmission issues
- `C18`: Increase A3 Offset threshold for 3219634_1
- `C19`: Decrease transmission power for 3219634_1
- `C20`: Lift the tilt angle of 3236939_4 by 3 degrees
- `C21`: Increase A3 Offset threshold for 3236939_4
- `C22`: Press down the tilt angle  of 3219634_1 by 7 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.311 | MS1 | 121.4656701832 | 31.1446320596 | 251 | 504990 | -80.82 | 16.56 | 424.39 | 0.03 | 2.90 | 1582 |
| 2024-09-20 22:21:32.536 | MS1 | 121.4656778378 | 31.1446293195 | 251 | 504990 | -76.86 | 17.34 | 478.31 | 0.11 | 2.99 | 1591 |
| 2024-09-20 22:21:33.222 | MS1 | 121.4656617426 | 31.1446312450 | 251 | 504990 | -82.83 | 12.55 | 504.01 | 0.14 | 2.74 | 1578 |
| 2024-09-20 22:21:34.672 | MS1 | 121.4656626344 | 31.1446299504 | 251 | 504990 | -89.17 | -1.09 | 61.52 | 0.19 | 1.31 | 1574 |
| 2024-09-20 22:21:35.922 | MS1 | 121.4656672978 | 31.1446184745 | 251 | 504990 | -84.97 | -0.61 | 67.01 | 0.16 | 1.40 | 1584 |
| 2024-09-20 22:21:36.733 | MS1 | 121.4656585435 | 31.1446350464 | 251 | 504990 | -88.30 | -3.12 | 60.84 | 0.06 | 1.41 | 1577 |
| 2024-09-20 22:21:37.224 | MS1 | 121.4656599048 | 31.1446302849 | 251 | 504990 | -84.63 | -1.55 | 38.09 | 0.05 | 1.18 | 1583 |
| 2024-09-20 22:21:38.167 | MS1 | 121.4656729550 | 31.1446323991 | 251 | 504990 | -89.37 | -3.41 | 53.28 | 0.01 | 1.20 | 1571 |
| 2024-09-20 22:21:39.301 | MS1 | 121.4656613142 | 31.1446226088 | 257 | 504990 | -79.46 | 12.80 | 245.38 | 0.05 | 1.01 | 1599 |
| 2024-09-20 22:21:40.991 | MS1 | 121.4656735240 | 31.1446214502 | 257 | 504990 | -75.80 | 15.81 | 512.30 | 0.16 | 2.98 | 1585 |
| 2024-09-20 22:21:41.955 | MS1 | 121.4656594699 | 31.1446194903 | 257 | 504990 | -81.08 | 13.94 | 359.97 | 0.03 | 2.02 | 1589 |
| 2024-09-20 22:21:42.637 | MS1 | 121.4656666852 | 31.1446286737 | 257 | 504990 | -81.84 | 16.01 | 511.12 | 0.05 | 2.10 | 1576 |

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
| 3211049 | 2 | 121.4731953876 | 31.1517077477 | 65 | 13 | 8 | 38.1 | TDD | 331 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3219634 | 1 | 121.4738889890 | 31.1551391666 | 124 | 6 | 6 | 21.8 | TDD | 257 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3231699 | 3 | 121.4692879491 | 31.1537252268 | 41 | 7 | 9 | 48.4 | TDD | 294 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3236939 | 4 | 121.4754961460 | 31.1471814863 | 211 | 1 | 11 | 41.6 | TDD | 251 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.185 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.202 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.320 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.320 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.013 | NREventA3 | measId:2;ServCellPCI:273;Se... |
| 2024-09-20 22:21:38.253 | NRHandoverAttempt | SourcePCI:273;SourceNR-ARFC... |
| 2024-09-20 22:21:38.299 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.311 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.457 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.457 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219634 | 1 | 11.1599 | 11.2451 | -116.2785 | 6.1006 | 109.6830 | 0.0050 | 0.0126 |
| 2024_09_20 22:00 | 3211049 | 2 | 6.3785 | 11.7281 | -114.6490 | 18.6707 | 185.8907 | 0.0076 | 0.0050 |
| 2024_09_20 22:00 | 3231699 | 3 | 11.2246 | 7.0839 | -117.5001 | 9.8623 | 88.0478 | 0.0030 | 0.0069 |
| 2024_09_20 22:00 | 3236939 | 4 | 7.1644 | 19.2267 | -114.8828 | 17.4121 | 97.8704 | 0.0128 | 0.1055 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416809_9EE31D7C | 504990 | 257 | -84.7 | 504990 | 251 | -90.6 | 504990 | 331 | -88.5 | 504990 | 294 |
| MR_1774416809_23EE4444 | 504990 | 251 | -89.1 | 504990 | 257 | -83.1 | 504990 | 331 | -87.9 | 504990 | 294 |
| MR_1774416809_4FE260E2 | 504990 | 251 | -89.0 | 504990 | 257 | -83.1 | 504990 | 331 | -89.3 | 504990 | 294 |
| MR_1774416809_1F67AD2E | 504990 | 251 | -87.6 | 504990 | 257 | -83.2 | 504990 | 331 | -87.7 | 504990 | 294 |
| MR_1774416809_8F36AEBB | 504990 | 251 | -89.7 | 504990 | 257 | -86.3 | 504990 | 331 | -88.5 | 504990 | 294 |
| MR_1774416809_D65612E9 | 504990 | 251 | -87.8 | 504990 | 257 | -83.4 | 504990 | 331 | -89.5 | 504990 | 294 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1105: `a9bf9e81-ea1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a9bf9e81-ea14-4120-8728-52830deaf6b7` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Add neighbor relationship between 3256494_2 and 3220756_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1105] topology](images/train_1105.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220756_1
- `C2`: Press down the tilt angle  of 3220756_1 by 2 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256494_2
- `C4`: Lift the tilt angle of 3256494_2 by 8 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Add neighbor relationship between 3218704_3 and 3220756_1
- `C7`: Check test server and transmission issues
- `C8`: Decrease A3 Offset threshold for 3256494_2
- `C9`: Increase A3 Offset threshold for 3220756_1
- `C10`: Decrease transmission power for 3220756_1
- `C11`: Add neighbor relationship between 3256494_2 and 3220756_1 **← 정답**
- `C12`: Increase transmission power for 3220756_1
- `C13`: Adjust the azimuth of 3220756_1 by 7 degrees
- `C14`: Increase A3 Offset threshold for 3256494_2
- `C15`: Decrease A3 Offset threshold for 3220756_1
- `C16`: Press down the tilt angle of 3256494_2 by 8 degrees
- `C17`: Adjust the azimuth of 3256494_2 by 50 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220756_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256494_2
- `C20`: Decrease transmission power for 3256494_2
- `C21`: Lift the tilt angle  of 3220756_1 by 2 degrees
- `C22`: Increase transmission power for 3256494_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.730 | MS1 | 121.4656668756 | 31.1446213238 | 989 | 504990 | -83.64 | 14.50 | 529.13 | 0.06 | 2.74 | 1571 |
| 2024-09-20 22:21:32.646 | MS1 | 121.4656706325 | 31.1446197196 | 989 | 504990 | -80.64 | 13.49 | 471.11 | 0.03 | 2.47 | 1592 |
| 2024-09-20 22:21:33.702 | MS1 | 121.4656775434 | 31.1446330541 | 989 | 504990 | -78.78 | 16.65 | 395.73 | 0.11 | 2.97 | 1583 |
| 2024-09-20 22:21:34.369 | MS1 | 121.4656659368 | 31.1446184000 | 989 | 504990 | -94.55 | -1.79 | 55.13 | 0.15 | 1.30 | 1563 |
| 2024-09-20 22:21:35.316 | MS1 | 121.4656758080 | 31.1446184225 | 989 | 504990 | -92.54 | -0.74 | 57.07 | 0.05 | 1.36 | 1586 |
| 2024-09-20 22:21:36.377 | MS1 | 121.4656659142 | 31.1446211030 | 989 | 504990 | -92.66 | -2.69 | 37.97 | 0.17 | 1.43 | 1565 |
| 2024-09-20 22:21:37.883 | MS1 | 121.4656597322 | 31.1446228691 | 989 | 504990 | -85.24 | -3.97 | 65.25 | 0.11 | 1.17 | 1567 |
| 2024-09-20 22:21:38.945 | MS1 | 121.4656747461 | 31.1446339257 | 989 | 504990 | -83.86 | 16.09 | 589.35 | 0.01 | 1.22 | 1568 |
| 2024-09-20 22:21:39.538 | MS1 | 121.4656656751 | 31.1446315774 | 989 | 504990 | -81.76 | 14.89 | 489.63 | 0.19 | 1.49 | 1571 |
| 2024-09-20 22:21:40.914 | MS1 | 121.4656768125 | 31.1446352735 | 989 | 504990 | -78.38 | 17.65 | 528.14 | 0.18 | 2.19 | 1594 |
| 2024-09-20 22:21:41.636 | MS1 | 121.4656683771 | 31.1446271034 | 989 | 504990 | -80.20 | 14.88 | 585.72 | 0.01 | 2.70 | 1577 |
| 2024-09-20 22:21:42.251 | MS1 | 121.4656741271 | 31.1446207850 | 989 | 504990 | -75.72 | 12.51 | 334.44 | 0.08 | 2.19 | 1576 |

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
| 3218704 | 3 | 121.4742518931 | 31.1535251834 | 21 | 5 | 12 | 27.8 | TDD | 626 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3220756 | 1 | 121.4744136075 | 31.1452754335 | 258 | 0 | 12 | 30.7 | TDD | 242 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3226365 | 4 | 121.4709167746 | 31.1515042041 | 57 | 1 | 1 | 18.5 | TDD | 423 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3256494 | 2 | 121.4711916993 | 31.1525471561 | 127 | 7 | 9 | 21.1 | TDD | 989 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.481 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.503 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.606 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.606 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.371 | NREventA3 | measId:2;ServCellPCI:605;Se... |
| 2024-09-20 22:21:36.371 | NREventA3 | measId:2;ServCellPCI:605;Se... |
| 2024-09-20 22:21:37.371 | NREventA3 | measId:2;ServCellPCI:605;Se... |
| 2024-09-20 22:21:39.871 | NRRRCReestablishAttempt | PCI:605 |
| 2024-09-20 22:21:39.884 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.895 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:40.030 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.030 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220756 | 1 | 6.6216 | 5.3278 | -114.5075 | 17.0245 | 169.8220 | 0.0108 | 0.0029 |
| 2024_09_20 22:00 | 3256494 | 2 | 14.7208 | 12.9705 | -116.2295 | 9.3550 | 145.8455 | 0.0033 | 0.1503 |
| 2024_09_20 22:00 | 3218704 | 3 | 12.7162 | 8.9084 | -114.4664 | 6.8596 | 139.8625 | 0.0179 | 0.0188 |
| 2024_09_20 22:00 | 3226365 | 4 | 11.4917 | 15.5714 | -117.6261 | 16.6602 | 175.6819 | 0.0105 | 0.0179 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416934_70C63FD0 | 504990 | 242 | -87.2 | 504990 | 989 | -94.6 | 504990 | 626 | -92.2 | 504990 | 423 |
| MR_1774416934_0E4FE861 | 504990 | 989 | -96.2 | 504990 | 242 | -90.8 | 504990 | 626 | -92.4 | 504990 | 423 |
| MR_1774416934_709C71B4 | 504990 | 989 | -93.7 | 504990 | 242 | -87.1 | 504990 | 626 | -95.6 | 504990 | 423 |
| MR_1774416934_96FC31CE | 504990 | 989 | -93.2 | 504990 | 242 | -88.6 | 504990 | 626 | -95.3 | 504990 | 423 |
| MR_1774416934_5356D39A | 504990 | 989 | -94.4 | 504990 | 242 | -90.2 | 504990 | 626 | -91.9 | 504990 | 423 |
| MR_1774416934_9A5C7335 | 504990 | 242 | -88.7 | 504990 | 989 | -92.8 | 504990 | 626 | -94.8 | 504990 | 423 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1106: `dcccaa46-65f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dcccaa46-65f2-4e16-b6af-66963061a31b` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Lift the tilt angle  of 3240688_2 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1106] topology](images/train_1106.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3243242_1
- `C2`: Add neighbor relationship between 3243242_1 and 3244654_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243242_1
- `C4`: Adjust the azimuth of 3240688_2 by 41 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243242_1
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease transmission power for 3244654_3
- `C8`: Increase transmission power for 3243242_1
- `C9`: Increase A3 Offset threshold for 3243242_1
- `C10`: Check test server and transmission issues
- `C11`: Increase transmission power for 3244654_3
- `C12`: Lift the tilt angle  of 3240688_2 by 7 degrees **← 정답**
- `C13`: Lift the tilt angle of 3243242_1 by 3 degrees
- `C14`: Decrease transmission power for 3243242_1
- `C15`: Press down the tilt angle  of 3240688_2 by 7 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244654_3
- `C17`: Increase A3 Offset threshold for 3244654_3
- `C18`: Press down the tilt angle of 3243242_1 by 3 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244654_3
- `C20`: Adjust the azimuth of 3243242_1 by 11 degrees
- `C21`: Decrease A3 Offset threshold for 3244654_3
- `C22`: Add neighbor relationship between 3240688_2 and 3244654_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.637 | MS1 | 121.4656629158 | 31.1446271087 | 988 | 504990 | -85.33 | 16.72 | 292.25 | 0.18 | 2.59 | 1581 |
| 2024-09-20 22:21:32.844 | MS1 | 121.4656675363 | 31.1446298741 | 988 | 504990 | -89.01 | 17.13 | 520.35 | 0.08 | 2.19 | 1560 |
| 2024-09-20 22:21:33.414 | MS1 | 121.4656763831 | 31.1446303693 | 988 | 504990 | -89.18 | 15.94 | 509.64 | 0.05 | 2.19 | 1560 |
| 2024-09-20 22:21:34.523 | MS1 | 121.4656747427 | 31.1446352178 | 988 | 504990 | -89.75 | 16.07 | 74.97 | 0.09 | 2.04 | 1570 |
| 2024-09-20 22:21:35.451 | MS1 | 121.4656766605 | 31.1446285218 | 988 | 504990 | -91.63 | 15.85 | 99.18 | 0.17 | 2.56 | 1586 |
| 2024-09-20 22:21:36.650 | MS1 | 121.4656683643 | 31.1446307173 | 988 | 504990 | -90.76 | 16.77 | 60.27 | 0.02 | 2.77 | 1600 |
| 2024-09-20 22:21:37.146 | MS1 | 121.4656752959 | 31.1446337197 | 988 | 504990 | -89.75 | 11.49 | 43.89 | 0.15 | 2.33 | 1599 |
| 2024-09-20 22:21:38.717 | MS1 | 121.4656604468 | 31.1446325581 | 988 | 504990 | -90.83 | 12.87 | 86.81 | 0.16 | 2.66 | 1590 |
| 2024-09-20 22:21:39.196 | MS1 | 121.4656611016 | 31.1446302177 | 988 | 504990 | -89.47 | 8.90 | 80.98 | 0.17 | 2.84 | 1584 |
| 2024-09-20 22:21:40.819 | MS1 | 121.4656704612 | 31.1446247756 | 988 | 504990 | -89.28 | 10.82 | 386.62 | 0.17 | 2.64 | 1598 |
| 2024-09-20 22:21:41.517 | MS1 | 121.4656647945 | 31.1446285243 | 988 | 504990 | -90.32 | 11.16 | 319.20 | 0.05 | 2.72 | 1568 |
| 2024-09-20 22:21:42.759 | MS1 | 121.4656657183 | 31.1446236350 | 988 | 504990 | -92.62 | 12.88 | 588.78 | 0.06 | 2.60 | 1565 |

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
| 3218756 | 4 | 121.4749094074 | 31.1522667091 | 28 | 13 | 12 | 25.8 | TDD | 670 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3240688 | 2 | 121.4644901546 | 31.1543593634 | 12 | 2 | 6 | 18.7 | TDD | 644 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3243242 | 1 | 121.4752034369 | 31.1551557522 | 229 | 2 | 10 | 36.7 | TDD | 988 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3244654 | 3 | 121.4754381341 | 31.1494022444 | 199 | 6 | 9 | 16.6 | TDD | 893 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.937 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.961 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.068 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.068 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.823 | NREventA3 | measId:2;ServCellPCI:946;Se... |
| 2024-09-20 22:21:38.063 | NRHandoverAttempt | SourcePCI:946;SourceNR-ARFC... |
| 2024-09-20 22:21:38.112 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.126 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.268 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.268 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243242 | 1 | 93.8428 | 78.3280 | -115.4314 | 5.7486 | 189.9054 | 0.0193 | 0.0152 |
| 2024_09_20 22:00 | 3240688 | 2 | 8.6442 | 17.4440 | -116.4262 | 18.7875 | 90.4843 | 0.0062 | 0.0040 |
| 2024_09_20 22:00 | 3244654 | 3 | 5.7584 | 10.4114 | -116.6247 | 13.6418 | 132.2961 | 0.0028 | 0.0055 |
| 2024_09_20 22:00 | 3218756 | 4 | 18.0717 | 14.1113 | -117.1615 | 15.8614 | 169.1655 | 0.0156 | 0.0034 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414303_4DAF8FAC | 504990 | 988 | -90.9 | 504990 | 893 | -96.7 | 504990 | 644 | -98.5 | 504990 | 670 |
| MR_1774414303_058BC997 | 504990 | 988 | -89.9 | 504990 | 893 | -94.6 | 504990 | 644 | -98.1 | 504990 | 670 |
| MR_1774414303_8ADA86B7 | 504990 | 988 | -88.0 | 504990 | 893 | -96.7 | 504990 | 644 | -100.2 | 504990 | 670 |
| MR_1774414303_73AF500B | 504990 | 988 | -91.4 | 504990 | 893 | -94.2 | 504990 | 644 | -100.0 | 504990 | 670 |
| MR_1774414303_5AF0B220 | 504990 | 988 | -89.7 | 504990 | 893 | -94.8 | 504990 | 644 | -99.3 | 504990 | 670 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1107: `ca7c2042-094...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ca7c2042-0947-4492-a97c-a620068abc7e` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Lift the tilt angle  of 3267338_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1107] topology](images/train_1107.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3221560_1 by 4 degrees
- `C2`: Press down the tilt angle of 3221560_1 by 4 degrees
- `C3`: Increase A3 Offset threshold for 3221560_1
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Add neighbor relationship between 3221560_1 and 3254448_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221560_1
- `C7`: Lift the tilt angle  of 3267338_2 by 10 degrees **← 정답**
- `C8`: Increase transmission power for 3221560_1
- `C9`: Check test server and transmission issues
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221560_1
- `C11`: Decrease A3 Offset threshold for 3254448_4
- `C12`: Press down the tilt angle  of 3267338_2 by 10 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254448_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254448_4
- `C15`: Decrease transmission power for 3254448_4
- `C16`: Decrease A3 Offset threshold for 3221560_1
- `C17`: Decrease transmission power for 3221560_1
- `C18`: Add neighbor relationship between 3267338_2 and 3254448_4
- `C19`: Adjust the azimuth of 3267338_2 by 50 degrees
- `C20`: Adjust the azimuth of 3221560_1 by 36 degrees
- `C21`: Increase A3 Offset threshold for 3254448_4
- `C22`: Increase transmission power for 3254448_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.922 | MS1 | 121.4656752697 | 31.1446283348 | 384 | 504990 | -91.94 | 14.64 | 594.49 | 0.16 | 2.01 | 1561 |
| 2024-09-20 22:21:32.184 | MS1 | 121.4656722903 | 31.1446215562 | 384 | 504990 | -85.82 | 13.06 | 336.30 | 0.15 | 2.70 | 1600 |
| 2024-09-20 22:21:33.176 | MS1 | 121.4656743868 | 31.1446370162 | 384 | 504990 | -89.50 | 17.81 | 569.08 | 0.19 | 2.06 | 1579 |
| 2024-09-20 22:21:34.167 | MS1 | 121.4656743893 | 31.1446207409 | 384 | 504990 | -87.85 | 14.16 | 56.12 | 0.00 | 2.64 | 1585 |
| 2024-09-20 22:21:35.730 | MS1 | 121.4656688993 | 31.1446340509 | 384 | 504990 | -90.37 | 13.98 | 66.39 | 0.04 | 2.83 | 1587 |
| 2024-09-20 22:21:36.100 | MS1 | 121.4656610735 | 31.1446208525 | 384 | 504990 | -88.48 | 13.37 | 80.39 | 0.15 | 2.55 | 1587 |
| 2024-09-20 22:21:37.168 | MS1 | 121.4656641221 | 31.1446274659 | 384 | 504990 | -89.49 | 12.32 | 88.90 | 0.18 | 2.26 | 1570 |
| 2024-09-20 22:21:38.207 | MS1 | 121.4656672587 | 31.1446304669 | 384 | 504990 | -91.86 | 10.93 | 71.75 | 0.11 | 2.58 | 1594 |
| 2024-09-20 22:21:39.277 | MS1 | 121.4656727387 | 31.1446210513 | 384 | 504990 | -91.93 | 11.71 | 99.54 | 0.08 | 2.29 | 1589 |
| 2024-09-20 22:21:40.971 | MS1 | 121.4656735087 | 31.1446199047 | 384 | 504990 | -90.58 | 8.82 | 441.09 | 0.01 | 2.14 | 1574 |
| 2024-09-20 22:21:41.617 | MS1 | 121.4656600374 | 31.1446371746 | 384 | 504990 | -92.34 | 11.19 | 459.89 | 0.08 | 2.85 | 1588 |
| 2024-09-20 22:21:42.335 | MS1 | 121.4656599328 | 31.1446299196 | 384 | 504990 | -93.25 | 8.11 | 582.86 | 0.10 | 2.83 | 1576 |

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
| 3221560 | 1 | 121.4756884923 | 31.1450231433 | 231 | 1 | 10 | 44.2 | TDD | 384 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3231377 | 3 | 121.4676741428 | 31.1549794021 | 262 | 5 | 10 | 27.4 | TDD | 613 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3254448 | 4 | 121.4661764520 | 31.1462292011 | 352 | 7 | 11 | 17.4 | TDD | 575 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3267338 | 2 | 121.4644834675 | 31.1513931771 | 29 | 5 | 7 | 33.9 | TDD | 849 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.234 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.258 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.402 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.402 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.116 | NREventA3 | measId:2;ServCellPCI:541;Se... |
| 2024-09-20 22:21:38.356 | NRHandoverAttempt | SourcePCI:541;SourceNR-ARFC... |
| 2024-09-20 22:21:38.397 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.408 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.555 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.555 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221560 | 1 | 88.2769 | 90.0315 | -117.7879 | 11.1992 | 130.8300 | 0.0062 | 0.0030 |
| 2024_09_20 22:00 | 3267338 | 2 | 17.5857 | 6.3218 | -117.1986 | 16.2799 | 182.6006 | 0.0172 | 0.0085 |
| 2024_09_20 22:00 | 3231377 | 3 | 15.6406 | 10.1920 | -116.7815 | 9.1013 | 84.1041 | 0.0156 | 0.0051 |
| 2024_09_20 22:00 | 3254448 | 4 | 15.2651 | 19.7440 | -115.9828 | 14.5491 | 172.2905 | 0.0091 | 0.0156 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415494_BF579310 | 504990 | 384 | -86.1 | 504990 | 575 | -94.6 | 504990 | 849 | -93.2 | 504990 | 613 |
| MR_1774415494_700A85D7 | 504990 | 384 | -89.8 | 504990 | 575 | -94.0 | 504990 | 849 | -96.0 | 504990 | 613 |
| MR_1774415494_EA49A703 | 504990 | 384 | -87.6 | 504990 | 575 | -93.2 | 504990 | 849 | -95.5 | 504990 | 613 |
| MR_1774415494_F6D0D120 | 504990 | 384 | -89.7 | 504990 | 575 | -92.8 | 504990 | 849 | -96.4 | 504990 | 613 |
| MR_1774415494_A90D07A1 | 504990 | 384 | -89.2 | 504990 | 575 | -93.9 | 504990 | 849 | -93.3 | 504990 | 613 |
| MR_1774415494_EA3F454B | 504990 | 384 | -88.7 | 504990 | 575 | -96.6 | 504990 | 849 | -96.5 | 504990 | 613 |
| MR_1774415494_1B606404 | 504990 | 384 | -89.2 | 504990 | 575 | -95.1 | 504990 | 849 | -94.6 | 504990 | 613 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1108: `244ef5cf-4a1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `244ef5cf-4a1a-4bed-ad89-deaeac15b9d0` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1108] topology](images/train_1108.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3216389_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216389_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216389_1
- `C4`: Insufficient data; more data is needed for judgment. **← 정답**
- `C5`: Adjust the azimuth of 3245592_3 by 25 degrees
- `C6`: Decrease A3 Offset threshold for 3245592_3
- `C7`: Add neighbor relationship between 3214220_4 and 3245592_3
- `C8`: Decrease transmission power for 3245592_3
- `C9`: Check test server and transmission issues
- `C10`: Add neighbor relationship between 3216389_1 and 3245592_3
- `C11`: Increase A3 Offset threshold for 3216389_1
- `C12`: Lift the tilt angle of 3216389_1 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3216389_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245592_3
- `C15`: Decrease transmission power for 3216389_1
- `C16`: Increase A3 Offset threshold for 3245592_3
- `C17`: Lift the tilt angle  of 3245592_3 by 3 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245592_3
- `C19`: Press down the tilt angle of 3216389_1 by 10 degrees
- `C20`: Increase transmission power for 3245592_3
- `C21`: Adjust the azimuth of 3216389_1 by 50 degrees
- `C22`: Press down the tilt angle  of 3245592_3 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.855 | MS1 | 121.4656686653 | 31.1446331742 | 951 | 504990 | -87.73 | 15.83 | 591.37 | 0.04 | 2.43 | 1584 |
| 2024-09-20 22:21:32.466 | MS1 | 121.4656605693 | 31.1446260045 | 951 | 504990 | -91.37 | 14.59 | 385.13 | 0.15 | 2.54 | 1577 |
| 2024-09-20 22:21:33.555 | MS1 | 121.4656620586 | 31.1446379464 | 951 | 504990 | -85.18 | 15.51 | 588.20 | 0.01 | 2.60 | 1565 |
| 2024-09-20 22:21:34.532 | MS1 | 121.4656713812 | 31.1446210668 | 951 | 504990 | -85.26 | 16.14 | 82.96 | 0.17 | 2.73 | 1596 |
| 2024-09-20 22:21:35.297 | MS1 | 121.4656773421 | 31.1446334705 | 951 | 504990 | -88.27 | 14.88 | 72.79 | 0.04 | 2.04 | 1595 |
| 2024-09-20 22:21:36.712 | MS1 | 121.4656735934 | 31.1446230378 | 951 | 504990 | -87.62 | 13.90 | 79.20 | 0.08 | 2.33 | 1575 |
| 2024-09-20 22:21:37.972 | MS1 | 121.4656734842 | 31.1446225114 | 951 | 504990 | -91.44 | 12.47 | 61.71 | 0.12 | 2.37 | 1574 |
| 2024-09-20 22:21:38.820 | MS1 | 121.4656612693 | 31.1446206912 | 951 | 504990 | -90.74 | 8.82 | 77.90 | 0.09 | 2.23 | 1591 |
| 2024-09-20 22:21:39.990 | MS1 | 121.4656727221 | 31.1446303078 | 951 | 504990 | -91.35 | 8.14 | 51.34 | 0.01 | 2.30 | 1566 |
| 2024-09-20 22:21:40.936 | MS1 | 121.4656775994 | 31.1446259608 | 951 | 504990 | -89.36 | 12.65 | 477.02 | 0.00 | 2.66 | 1591 |
| 2024-09-20 22:21:41.818 | MS1 | 121.4656615860 | 31.1446243643 | 951 | 504990 | -91.45 | 9.65 | 444.76 | 0.18 | 2.99 | 1561 |
| 2024-09-20 22:21:42.877 | MS1 | 121.4656612403 | 31.1446290852 | 951 | 504990 | -92.65 | 7.76 | 551.38 | 0.10 | 2.99 | 1583 |

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
| 3210703 | 2 | 121.4668118785 | 31.1441678162 | 340 | 12 | 6 | 46.0 | TDD | 635 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3214220 | 4 | 121.4694369525 | 31.1488413919 | 63 | 6 | 3 | 45.0 | TDD | 887 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3216389 | 1 | 121.4697085470 | 31.1478495390 | 163 | 11 | 8 | 16.2 | TDD | 951 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3245592 | 3 | 121.4640320136 | 31.1533674623 | 146 | 0 | 10 | 49.1 | TDD | 798 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.219 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.237 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.345 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.345 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.061 | NREventA3 | measId:2;ServCellPCI:783;Se... |
| 2024-09-20 22:21:38.301 | NRHandoverAttempt | SourcePCI:783;SourceNR-ARFC... |
| 2024-09-20 22:21:38.332 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.345 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.457 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.457 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3216389 | 1 | 82.8527 | 86.7589 | -117.4492 | 15.4782 | 187.9002 | 0.0018 | 0.0067 |
| 2024_09_19 22:00 | 3210703 | 2 | 94.6408 | 86.9838 | -116.4928 | 5.0508 | 118.8256 | 0.0036 | 0.0185 |
| 2024_09_19 22:00 | 3245592 | 3 | 75.8718 | 76.1722 | -115.1639 | 12.9549 | 197.4119 | 0.0151 | 0.0155 |
| 2024_09_19 22:00 | 3214220 | 4 | 88.7007 | 89.2677 | -115.9711 | 14.8276 | 101.2368 | 0.0073 | 0.0176 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415797_94A1F534 | 504990 | 951 | -84.8 | 504990 | 798 | -84.2 | 504990 | 887 | -90.9 | 504990 | 635 |
| MR_1774415797_4DDAFE68 | 504990 | 951 | -85.9 | 504990 | 798 | -84.5 | 504990 | 887 | -94.1 | 504990 | 635 |
| MR_1774415797_1C9BF0A3 | 504990 | 951 | -85.9 | 504990 | 798 | -86.3 | 504990 | 887 | -93.0 | 504990 | 635 |
| MR_1774415797_578799A9 | 504990 | 951 | -85.3 | 504990 | 798 | -86.4 | 504990 | 887 | -92.9 | 504990 | 635 |
| MR_1774415797_1E50C5C0 | 504990 | 951 | -83.3 | 504990 | 798 | -85.1 | 504990 | 887 | -93.5 | 504990 | 635 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1109: `40ba7502-3be...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `40ba7502-3be9-4a25-a9f9-b3f54b06fcfa` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease A3 Offset threshold for 3212272_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1109] topology](images/train_1109.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212272_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238983_2
- `C3`: Decrease transmission power for 3238983_2
- `C4`: Increase transmission power for 3238983_2
- `C5`: Adjust the azimuth of 3238983_2 by 2 degrees
- `C6`: Adjust the azimuth of 3212272_4 by 50 degrees
- `C7`: Increase transmission power for 3212272_4
- `C8`: Decrease A3 Offset threshold for 3238983_2
- `C9`: Add neighbor relationship between 3237662_3 and 3238983_2
- `C10`: Decrease transmission power for 3212272_4
- `C11`: Decrease A3 Offset threshold for 3212272_4 **← 정답**
- `C12`: Lift the tilt angle of 3212272_4 by 6 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212272_4
- `C14`: Lift the tilt angle  of 3238983_2 by 7 degrees
- `C15`: Add neighbor relationship between 3212272_4 and 3238983_2
- `C16`: Press down the tilt angle  of 3238983_2 by 7 degrees
- `C17`: Press down the tilt angle of 3212272_4 by 6 degrees
- `C18`: Check test server and transmission issues
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238983_2
- `C21`: Increase A3 Offset threshold for 3238983_2
- `C22`: Increase A3 Offset threshold for 3212272_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.182 | MS1 | 121.4656620677 | 31.1446218653 | 676 | 504990 | -82.43 | 13.94 | 571.19 | 0.08 | 2.87 | 1566 |
| 2024-09-20 22:21:32.750 | MS1 | 121.4656719963 | 31.1446374636 | 676 | 504990 | -80.17 | 12.27 | 411.44 | 0.12 | 2.77 | 1584 |
| 2024-09-20 22:21:33.153 | MS1 | 121.4656691610 | 31.1446287910 | 676 | 504990 | -76.80 | 16.18 | 537.67 | 0.03 | 2.46 | 1567 |
| 2024-09-20 22:21:34.347 | MS1 | 121.4656665027 | 31.1446332844 | 676 | 504990 | -91.09 | -3.02 | 41.33 | 0.08 | 1.12 | 1569 |
| 2024-09-20 22:21:35.176 | MS1 | 121.4656642248 | 31.1446336527 | 676 | 504990 | -85.58 | -0.65 | 39.90 | 0.20 | 1.41 | 1574 |
| 2024-09-20 22:21:36.780 | MS1 | 121.4656640459 | 31.1446254847 | 676 | 504990 | -91.89 | -3.77 | 72.89 | 0.09 | 1.18 | 1579 |
| 2024-09-20 22:21:37.660 | MS1 | 121.4656649340 | 31.1446188621 | 676 | 504990 | -91.21 | -1.29 | 37.38 | 0.18 | 1.01 | 1596 |
| 2024-09-20 22:21:38.451 | MS1 | 121.4656750380 | 31.1446340217 | 676 | 504990 | -90.70 | -0.79 | 37.93 | 0.01 | 1.33 | 1576 |
| 2024-09-20 22:21:39.779 | MS1 | 121.4656596452 | 31.1446247018 | 610 | 504990 | -75.92 | 12.22 | 290.77 | 0.08 | 1.18 | 1590 |
| 2024-09-20 22:21:40.338 | MS1 | 121.4656582148 | 31.1446187309 | 610 | 504990 | -80.30 | 15.05 | 375.93 | 0.01 | 2.80 | 1592 |
| 2024-09-20 22:21:41.301 | MS1 | 121.4656606638 | 31.1446342311 | 610 | 504990 | -75.65 | 16.61 | 496.17 | 0.10 | 2.73 | 1568 |
| 2024-09-20 22:21:42.914 | MS1 | 121.4656632217 | 31.1446331890 | 610 | 504990 | -79.45 | 17.28 | 532.00 | 0.07 | 2.51 | 1588 |

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
| 3212272 | 4 | 121.4747678989 | 31.1460061773 | 100 | 3 | 4 | 41.8 | TDD | 676 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3237662 | 3 | 121.4749232810 | 31.1533840244 | 304 | 3 | 7 | 17.0 | TDD | 579 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3238983 | 2 | 121.4693081617 | 31.1442910122 | 278 | 3 | 10 | 26.5 | TDD | 610 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3277785 | 1 | 121.4659168504 | 31.1508851691 | 267 | 12 | 5 | 47.9 | TDD | 936 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.475 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.491 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.641 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.641 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.370 | NREventA3 | measId:2;ServCellPCI:607;Se... |
| 2024-09-20 22:21:38.610 | NRHandoverAttempt | SourcePCI:607;SourceNR-ARFC... |
| 2024-09-20 22:21:38.647 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.658 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.775 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.775 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277785 | 1 | 8.6794 | 16.7374 | -114.8873 | 15.9109 | 91.8744 | 0.0112 | 0.0085 |
| 2024_09_20 22:00 | 3238983 | 2 | 9.5661 | 12.9367 | -117.4554 | 7.9691 | 137.6318 | 0.0097 | 0.0108 |
| 2024_09_20 22:00 | 3237662 | 3 | 18.9132 | 6.4401 | -117.3325 | 15.2438 | 138.7225 | 0.0004 | 0.0048 |
| 2024_09_20 22:00 | 3212272 | 4 | 15.0175 | 9.7474 | -116.0052 | 17.9550 | 161.4893 | 0.0067 | 0.1170 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412081_097D3266 | 504990 | 610 | -86.9 | 504990 | 676 | -92.4 | 504990 | 579 | -91.0 | 504990 | 936 |
| MR_1774412081_7F688EAE | 504990 | 610 | -87.0 | 504990 | 676 | -91.2 | 504990 | 579 | -88.9 | 504990 | 936 |
| MR_1774412081_F3D85C78 | 504990 | 676 | -92.3 | 504990 | 610 | -84.9 | 504990 | 579 | -91.3 | 504990 | 936 |
| MR_1774412081_C175C560 | 504990 | 676 | -91.0 | 504990 | 610 | -88.2 | 504990 | 579 | -90.8 | 504990 | 936 |
| MR_1774412081_1D5BABA3 | 504990 | 610 | -88.6 | 504990 | 676 | -92.4 | 504990 | 579 | -90.8 | 504990 | 936 |
| MR_1774412081_566FBA51 | 504990 | 610 | -84.9 | 504990 | 676 | -92.3 | 504990 | 579 | -91.3 | 504990 | 936 |

> *... 2개 열 생략 (전체 14열)*

---
