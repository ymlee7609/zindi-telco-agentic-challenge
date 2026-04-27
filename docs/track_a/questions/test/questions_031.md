# Track A 문제 분석 — test[300]~test[309]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[300] ~ test[309] (10개)

## 목차

1. [문제 300: `5d799708-2e5...`](#300) — single-answer
2. [문제 301: `5c3a5ebb-f30...`](#301) — single-answer
3. [문제 302: `06970f12-357...`](#302) — single-answer
4. [문제 303: `622ea6f9-d09...`](#303) — single-answer
5. [문제 304: `8a2feb2d-90f...`](#304) — multiple-answer
6. [문제 305: `56a98aea-02e...`](#305) — single-answer
7. [문제 306: `f7ab4aa3-211...`](#306) — single-answer
8. [문제 307: `fa34c7c0-30a...`](#307) — single-answer
9. [문제 308: `b2c2f51c-d86...`](#308) — single-answer
10. [문제 309: `36f53307-797...`](#309) — single-answer

---

### 문제 300: `5d799708-2e5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5d799708-2e57-459c-8adc-b73167593e25` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[300] topology](images/test_0300.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3248696_5
- `C2`: Lift the tilt angle  of 3272207_4 by 1 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272207_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272207_4
- `C5`: Lift the tilt angle of 3248696_5 by 3 degrees
- `C6`: Adjust the azimuth of 3272207_4 by 48 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248696_5
- `C8`: Increase A3 Offset threshold for 3248696_5
- `C9`: Increase transmission power for 3272207_4
- `C10`: Check test server and transmission issues
- `C11`: Decrease transmission power for 3272207_4
- `C12`: Add neighbor relationship between 3248696_5 and 3272207_4
- `C13`: Adjust the azimuth of 3248696_5 by 24 degrees
- `C14`: Add neighbor relationship between 3273731_13 and 3272207_4
- `C15`: Increase transmission power for 3248696_5
- `C16`: Press down the tilt angle of 3248696_5 by 3 degrees
- `C17`: Decrease A3 Offset threshold for 3248696_5
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Increase A3 Offset threshold for 3272207_4
- `C20`: Press down the tilt angle  of 3272207_4 by 1 degrees
- `C21`: Decrease A3 Offset threshold for 3272207_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248696_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.283 | MS1 | 121.4656624914 | 31.1446289148 | 121 | 504990 | -94.79 | 10.31 | 575.73 | 0.14 | 2.16 | 1561 |
| 2024-09-20 22:21:32.605 | MS1 | 121.4656592407 | 31.1446309029 | 175 | 504990 | -94.63 | 14.66 | 376.08 | 0.11 | 2.40 | 1577 |
| 2024-09-20 22:21:33.795 | MS1 | 121.4656696284 | 31.1446238411 | 552 | 504990 | -95.31 | 11.01 | 432.13 | 0.05 | 2.39 | 1585 |
| 2024-09-20 22:21:34.757 | MS1 | 121.4656629349 | 31.1446328584 | 634 | 152650 | -92.81 | 2.24 | 97.58 | 0.11 | 1.50 | 979 |
| 2024-09-20 22:21:35.313 | MS1 | 121.4656590646 | 31.1446254696 | 965 | 152650 | -94.11 | 2.24 | 74.10 | 0.14 | 1.52 | 996 |
| 2024-09-20 22:21:36.837 | MS1 | 121.4656634750 | 31.1446244270 | 508 | 152650 | -87.27 | 7.72 | 67.80 | 0.08 | 1.88 | 994 |
| 2024-09-20 22:21:37.611 | MS1 | 121.4656727212 | 31.1446339848 | 300 | 152650 | -96.11 | 4.66 | 89.12 | 0.04 | 1.77 | 976 |
| 2024-09-20 22:21:38.571 | MS1 | 121.4656676239 | 31.1446270269 | 634 | 152650 | -93.16 | 3.20 | 86.47 | 0.16 | 1.51 | 910 |
| 2024-09-20 22:21:39.858 | MS1 | 121.4656668220 | 31.1446194344 | 965 | 152650 | -94.95 | 6.69 | 52.78 | 0.20 | 1.53 | 933 |
| 2024-09-20 22:21:40.289 | MS1 | 121.4656633265 | 31.1446184187 | 508 | 152650 | -91.55 | 5.48 | 60.69 | 0.17 | 2.05 | 1573 |
| 2024-09-20 22:21:41.270 | MS1 | 121.4656741426 | 31.1446205971 | 300 | 152650 | -90.00 | 3.32 | 75.24 | 0.03 | 2.78 | 1573 |
| 2024-09-20 22:21:42.513 | MS1 | 121.4656761773 | 31.1446209922 | 634 | 152650 | -93.88 | 7.20 | 92.44 | 0.10 | 2.60 | 1582 |

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
| 3213446 | 6 | 121.4689321258 | 31.1533487996 | 183 | 9 | 0 | 3.1 | TDD | 506 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3218071 | 8 | 121.4678669028 | 31.1451818186 | 179 | 11 | 7 | 13.7 | FDD | 875 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3225426 | 10 | 121.4728018441 | 31.1514596348 | 316 | 3 | 4 | 12.0 | FDD | 211 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3231418 | 3 | 121.4752529892 | 31.1474323783 | 199 | 8 | 10 | 11.0 | TDD | 175 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3237021 | 11 | 121.4701760701 | 31.1467724030 | 286 | 0 | 4 | 27.8 | FDD | 408 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3243958 | 2 | 121.4729973224 | 31.1462827077 | 76 | 7 | 4 | 12.3 | TDD | 552 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3248696 | 5 | 121.4734771948 | 31.1526785467 | 196 | 2 | 2 | 28.0 | TDD | 121 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3251729 | 9 | 121.4708366154 | 31.1467852118 | 40 | 5 | 1 | 13.6 | FDD | 300 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3265966 | 1 | 121.4749557812 | 31.1559362467 | 158 | 14 | 8 | 9.7 | TDD | 483 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3272207 | 4 | 121.4670671494 | 31.1516642042 | 142 | 1 | 6 | 0.4 | TDD | 727 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3273731 | 13 | 121.4710819900 | 31.1476416285 | 221 | 0 | 10 | 28.6 | FDD | 508 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3275125 | 7 | 121.4649333490 | 31.1543814950 | 123 | 12 | 7 | 12.4 | FDD | 965 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3276524 | 12 | 121.4719379638 | 31.1494742286 | 208 | 11 | 11 | 4.2 | FDD | 634 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |

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
| 2024-09-20 22:21:31.682 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.697 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.839 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.839 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.490 | NREventA2 | measId:1;ServCellPCI:452;Se... |
| 2024-09-20 22:21:35.625 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.838 | NREventA5 | measId:3;ServCellPCI:452;Se... |
| 2024-09-20 22:21:35.894 | NRHandoverAttempt | SourcePCI:452;SourceNR-ARFC... |
| 2024-09-20 22:21:35.939 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.950 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.097 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.097 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265966 | 1 | 8.6882 | 10.2562 | -117.4225 | 12.0086 | 114.3233 | 0.0188 | 0.0000 |
| 2024_09_20 22:00 | 3243958 | 2 | 14.9995 | 9.5456 | -117.6118 | 6.0726 | 96.2583 | 0.0185 | 0.0069 |
| 2024_09_20 22:00 | 3231418 | 3 | 16.8173 | 17.2834 | -115.9416 | 18.4782 | 164.9741 | 0.0014 | 0.0029 |
| 2024_09_20 22:00 | 3272207 | 4 | 9.2228 | 7.6501 | -117.3182 | 13.9238 | 127.7971 | 0.0102 | 0.0021 |
| 2024_09_20 22:00 | 3248696 | 5 | 5.0178 | 16.8496 | -116.5265 | 15.7998 | 167.4184 | 0.0104 | 0.0121 |
| 2024_09_20 22:00 | 3213446 | 6 | 9.3473 | 12.9671 | -115.8715 | 19.4330 | 125.0075 | 0.0123 | 0.0147 |
| 2024_09_20 22:00 | 3275125 | 7 | 17.5129 | 12.6437 | -117.2908 | 3.8193 | 53.1151 | 0.0051 | 0.0063 |
| 2024_09_20 22:00 | 3218071 | 8 | 13.1418 | 17.2723 | -117.4423 | 3.7610 | 57.0276 | 0.0021 | 0.0078 |
| 2024_09_20 22:00 | 3251729 | 9 | 19.7662 | 5.4185 | -116.2242 | 4.4892 | 40.6959 | 0.0143 | 0.0159 |
| 2024_09_20 22:00 | 3225426 | 10 | 14.9695 | 5.9346 | -114.8301 | 3.5728 | 42.2055 | 0.0020 | 0.0170 |
| 2024_09_20 22:00 | 3237021 | 11 | 8.7123 | 18.1007 | -117.1921 | 3.6867 | 24.5294 | 0.0182 | 0.0137 |
| 2024_09_20 22:00 | 3276524 | 12 | 16.5580 | 14.1069 | -115.1559 | 3.5690 | 42.4920 | 0.0088 | 0.0122 |
| 2024_09_20 22:00 | 3273731 | 13 | 11.5554 | 16.6130 | -116.0589 | 4.7831 | 56.7642 | 0.0112 | 0.0048 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413741_9E4B611C | 504990 | 552 | -93.8 | 504990 | 727 | -99.5 | 504990 | 506 | -100.8 | 504990 | 483 |
| MR_1774413741_BF2FA7CC | 504990 | 552 | -96.1 | 504990 | 727 | -99.8 | 504990 | 506 | -100.6 | 504990 | 483 |
| MR_1774413741_D7507562 | 504990 | 552 | -94.0 | 504990 | 727 | -97.3 | 504990 | 506 | -100.9 | 504990 | 483 |
| MR_1774413741_02EBBA6D | 152650 | 634 | -93.8 | 152650 | 875 | -98.2 | 152650 | 211 | -100.9 | 152650 | 408 |
| MR_1774413741_6B8F0037 | 504990 | 552 | -94.5 | 504990 | 727 | -97.2 | 504990 | 506 | -101.6 | 504990 | 483 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 301: `5c3a5ebb-f30...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5c3a5ebb-f305-4168-8e5d-8e4898573b82` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[301] topology](images/test_0301.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3247247_3 by 10 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242391_2
- `C3`: Increase A3 Offset threshold for 3242391_2
- `C4`: Adjust the azimuth of 3247247_3 by 50 degrees
- `C5`: Adjust the azimuth of 3242391_2 by 9 degrees
- `C6`: Decrease A3 Offset threshold for 3247247_3
- `C7`: Lift the tilt angle  of 3242391_2 by 10 degrees
- `C8`: Check test server and transmission issues
- `C9`: Increase A3 Offset threshold for 3247247_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242391_2
- `C11`: Decrease transmission power for 3242391_2
- `C12`: Lift the tilt angle of 3247247_3 by 10 degrees
- `C13`: Add neighbor relationship between 3217393_4 and 3242391_2
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247247_3
- `C16`: Increase transmission power for 3247247_3
- `C17`: Decrease transmission power for 3247247_3
- `C18`: Increase transmission power for 3242391_2
- `C19`: Add neighbor relationship between 3247247_3 and 3242391_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247247_3
- `C21`: Press down the tilt angle  of 3242391_2 by 10 degrees
- `C22`: Decrease A3 Offset threshold for 3242391_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.590 | MS1 | 121.4656719607 | 31.1446195522 | 125 | 504990 | -89.81 | 17.58 | 591.98 | 0.01 | 2.69 | 1573 |
| 2024-09-20 22:21:32.505 | MS1 | 121.4656600483 | 31.1446361950 | 125 | 504990 | -90.48 | 16.14 | 315.83 | 0.15 | 2.81 | 1582 |
| 2024-09-20 22:21:33.755 | MS1 | 121.4656746887 | 31.1446270156 | 125 | 504990 | -90.85 | 12.31 | 479.25 | 0.18 | 2.92 | 1597 |
| 2024-09-20 22:21:34.263 | MS1 | 121.4656722002 | 31.1446190780 | 125 | 504990 | -87.66 | 13.02 | 60.47 | 0.01 | 3.00 | 357 |
| 2024-09-20 22:21:35.583 | MS1 | 121.4656619512 | 31.1446285947 | 125 | 504990 | -89.11 | 14.67 | 82.08 | 0.15 | 2.83 | 483 |
| 2024-09-20 22:21:36.270 | MS1 | 121.4656637816 | 31.1446305212 | 125 | 504990 | -86.18 | 12.45 | 56.51 | 0.19 | 2.29 | 490 |
| 2024-09-20 22:21:37.342 | MS1 | 121.4656733546 | 31.1446231350 | 125 | 504990 | -89.31 | 8.89 | 87.34 | 0.01 | 2.22 | 484 |
| 2024-09-20 22:21:38.684 | MS1 | 121.4656699686 | 31.1446204846 | 125 | 504990 | -91.29 | 7.07 | 66.05 | 0.04 | 2.87 | 417 |
| 2024-09-20 22:21:39.376 | MS1 | 121.4656714140 | 31.1446296372 | 125 | 504990 | -91.81 | 9.91 | 63.80 | 0.18 | 2.91 | 460 |
| 2024-09-20 22:21:40.506 | MS1 | 121.4656754155 | 31.1446302560 | 125 | 504990 | -91.38 | 12.06 | 551.79 | 0.02 | 2.52 | 1565 |
| 2024-09-20 22:21:41.924 | MS1 | 121.4656703854 | 31.1446198609 | 125 | 504990 | -93.84 | 7.34 | 532.75 | 0.19 | 2.52 | 1587 |
| 2024-09-20 22:21:42.537 | MS1 | 121.4656593642 | 31.1446358971 | 125 | 504990 | -90.58 | 8.06 | 408.90 | 0.00 | 2.11 | 1570 |

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
| 3217393 | 4 | 121.4688786431 | 31.1457229724 | 328 | 5 | 0 | 48.6 | TDD | 887 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3242391 | 2 | 121.4674432494 | 31.1459727051 | 238 | 10 | 1 | 35.3 | TDD | 74 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3242927 | 1 | 121.4720043760 | 31.1534892847 | 310 | 4 | 9 | 36.2 | TDD | 608 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3247247 | 3 | 121.4684564743 | 31.1530517021 | 315 | 14 | 9 | 45.2 | TDD | 125 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.337 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.358 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.490 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.490 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.139 | NREventA3 | measId:2;ServCellPCI:240;Se... |
| 2024-09-20 22:21:38.379 | NRHandoverAttempt | SourcePCI:240;SourceNR-ARFC... |
| 2024-09-20 22:21:38.415 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.425 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.540 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.540 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242927 | 1 | 19.0257 | 13.4033 | -117.7221 | 18.4767 | 149.5212 | 0.0176 | 0.0163 |
| 2024_09_20 22:00 | 3242391 | 2 | 19.0208 | 19.5582 | -115.7402 | 5.5832 | 169.5501 | 0.0135 | 0.0123 |
| 2024_09_20 22:00 | 3247247 | 3 | 12.5971 | 10.7674 | -115.1466 | 9.1745 | 140.7667 | 0.0038 | 0.0084 |
| 2024_09_20 22:00 | 3217393 | 4 | 7.2458 | 15.5884 | -116.4950 | 5.0628 | 104.3169 | 0.0167 | 0.0121 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415992_6DA2F1CE | 504990 | 125 | -86.8 | 504990 | 74 | -91.6 | 504990 | 887 | -95.1 | 504990 | 608 |
| MR_1774415992_E69F72D9 | 504990 | 125 | -88.1 | 504990 | 74 | -89.9 | 504990 | 887 | -92.1 | 504990 | 608 |
| MR_1774415992_B9BA75EA | 504990 | 125 | -89.4 | 504990 | 74 | -92.9 | 504990 | 887 | -95.0 | 504990 | 608 |
| MR_1774415992_634A6222 | 504990 | 125 | -86.0 | 504990 | 74 | -90.1 | 504990 | 887 | -93.6 | 504990 | 608 |
| MR_1774415992_B19F9368 | 504990 | 125 | -88.7 | 504990 | 74 | -89.6 | 504990 | 887 | -92.3 | 504990 | 608 |
| MR_1774415992_BEFE5766 | 504990 | 125 | -87.7 | 504990 | 74 | -91.2 | 504990 | 887 | -92.4 | 504990 | 608 |
| MR_1774415992_CBA1EB19 | 504990 | 125 | -86.5 | 504990 | 74 | -89.8 | 504990 | 887 | -95.7 | 504990 | 608 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 302: `06970f12-357...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `06970f12-3576-4112-9e5f-96a5cd838f5e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[302] topology](images/test_0302.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270726_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270726_1
- `C3`: Decrease transmission power for 3270726_1
- `C4`: Decrease transmission power for 3235366_2
- `C5`: Increase transmission power for 3235366_2
- `C6`: Increase A3 Offset threshold for 3270726_1
- `C7`: Increase A3 Offset threshold for 3235366_2
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Lift the tilt angle of 3270726_1 by 4 degrees
- `C10`: Decrease A3 Offset threshold for 3235366_2
- `C11`: Add neighbor relationship between 3270726_1 and 3235366_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235366_2
- `C13`: Decrease A3 Offset threshold for 3270726_1
- `C14`: Press down the tilt angle of 3270726_1 by 4 degrees
- `C15`: Check test server and transmission issues
- `C16`: Press down the tilt angle  of 3228762_3 by 4 degrees
- `C17`: Increase transmission power for 3270726_1
- `C18`: Adjust the azimuth of 3270726_1 by 21 degrees
- `C19`: Adjust the azimuth of 3228762_3 by 50 degrees
- `C20`: Lift the tilt angle  of 3228762_3 by 4 degrees
- `C21`: Add neighbor relationship between 3228762_3 and 3235366_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235366_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.401 | MS1 | 121.4656761510 | 31.1446315574 | 176 | 504990 | -89.74 | 14.49 | 562.63 | 0.07 | 2.53 | 1595 |
| 2024-09-20 22:21:32.298 | MS1 | 121.4656694239 | 31.1446185601 | 176 | 504990 | -85.65 | 12.59 | 382.35 | 0.03 | 2.05 | 1577 |
| 2024-09-20 22:21:33.194 | MS1 | 121.4656768289 | 31.1446368922 | 176 | 504990 | -91.70 | 16.77 | 388.26 | 0.04 | 2.18 | 1575 |
| 2024-09-20 22:21:34.361 | MS1 | 121.4656717713 | 31.1446229379 | 176 | 504990 | -91.02 | 13.49 | 46.73 | 0.18 | 2.94 | 1567 |
| 2024-09-20 22:21:35.677 | MS1 | 121.4656604824 | 31.1446203680 | 176 | 504990 | -89.63 | 16.96 | 92.88 | 0.11 | 2.43 | 1575 |
| 2024-09-20 22:21:36.239 | MS1 | 121.4656652858 | 31.1446308255 | 176 | 504990 | -85.58 | 12.87 | 54.43 | 0.18 | 2.69 | 1578 |
| 2024-09-20 22:21:37.294 | MS1 | 121.4656622665 | 31.1446344366 | 176 | 504990 | -89.64 | 12.24 | 72.29 | 0.19 | 2.86 | 1599 |
| 2024-09-20 22:21:38.353 | MS1 | 121.4656707306 | 31.1446206449 | 176 | 504990 | -93.69 | 11.44 | 84.46 | 0.13 | 2.77 | 1586 |
| 2024-09-20 22:21:39.173 | MS1 | 121.4656770571 | 31.1446311093 | 176 | 504990 | -89.90 | 8.23 | 81.14 | 0.12 | 2.81 | 1586 |
| 2024-09-20 22:21:40.805 | MS1 | 121.4656622774 | 31.1446182312 | 176 | 504990 | -90.83 | 9.64 | 407.86 | 0.06 | 2.65 | 1591 |
| 2024-09-20 22:21:41.645 | MS1 | 121.4656736825 | 31.1446194289 | 176 | 504990 | -90.84 | 8.36 | 580.25 | 0.14 | 2.71 | 1566 |
| 2024-09-20 22:21:42.443 | MS1 | 121.4656740015 | 31.1446344156 | 176 | 504990 | -91.94 | 8.55 | 575.71 | 0.04 | 2.96 | 1581 |

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
| 3214239 | 4 | 121.4659133757 | 31.1550323819 | 245 | 12 | 6 | 28.8 | TDD | 688 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3228762 | 3 | 121.4692745061 | 31.1504614834 | 46 | 3 | 7 | 20.2 | TDD | 392 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3235366 | 2 | 121.4724446170 | 31.1531447258 | 268 | 3 | 7 | 20.9 | TDD | 449 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3270726 | 1 | 121.4739924529 | 31.1472451359 | 229 | 1 | 12 | 41.7 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.113 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.131 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.260 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.260 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.949 | NREventA3 | measId:2;ServCellPCI:342;Se... |
| 2024-09-20 22:21:38.189 | NRHandoverAttempt | SourcePCI:342;SourceNR-ARFC... |
| 2024-09-20 22:21:38.237 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.247 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.355 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.355 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270726 | 1 | 88.4054 | 77.3923 | -117.3015 | 6.7404 | 166.8911 | 0.0016 | 0.0142 |
| 2024_09_20 22:00 | 3235366 | 2 | 17.0024 | 19.8724 | -116.3638 | 14.5385 | 143.8811 | 0.0153 | 0.0140 |
| 2024_09_20 22:00 | 3228762 | 3 | 19.8659 | 19.3059 | -115.0881 | 9.9945 | 179.1564 | 0.0180 | 0.0022 |
| 2024_09_20 22:00 | 3214239 | 4 | 7.8640 | 11.5459 | -117.2183 | 17.4972 | 114.3624 | 0.0189 | 0.0029 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417192_CEF45287 | 504990 | 176 | -89.5 | 504990 | 449 | -95.9 | 504990 | 392 | -98.3 | 504990 | 688 |
| MR_1774417192_EF70C874 | 504990 | 176 | -91.8 | 504990 | 449 | -95.6 | 504990 | 392 | -98.7 | 504990 | 688 |
| MR_1774417192_F0053C04 | 504990 | 176 | -92.0 | 504990 | 449 | -95.2 | 504990 | 392 | -98.1 | 504990 | 688 |
| MR_1774417192_50D79D9F | 504990 | 176 | -90.0 | 504990 | 449 | -95.0 | 504990 | 392 | -99.3 | 504990 | 688 |
| MR_1774417192_A319F122 | 504990 | 176 | -89.4 | 504990 | 449 | -95.8 | 504990 | 392 | -98.9 | 504990 | 688 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 303: `622ea6f9-d09...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `622ea6f9-d095-438b-b5d9-b98c7c948da3` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[303] topology](images/test_0303.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase A3 Offset threshold for 3262907_1
- `C3`: Adjust the azimuth of 3262907_1 by 50 degrees
- `C4`: Decrease transmission power for 3217049_2
- `C5`: Increase transmission power for 3217049_2
- `C6`: Decrease A3 Offset threshold for 3217049_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217049_2
- `C8`: Add neighbor relationship between 3270456_4 and 3262907_1
- `C9`: Adjust the azimuth of 3217049_2 by 50 degrees
- `C10`: Lift the tilt angle of 3217049_2 by 6 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262907_1
- `C12`: Decrease A3 Offset threshold for 3262907_1
- `C13`: Add neighbor relationship between 3217049_2 and 3262907_1
- `C14`: Increase A3 Offset threshold for 3217049_2
- `C15`: Increase transmission power for 3262907_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262907_1
- `C17`: Press down the tilt angle  of 3262907_1 by 8 degrees
- `C18`: Press down the tilt angle of 3217049_2 by 6 degrees
- `C19`: Decrease transmission power for 3262907_1
- `C20`: Lift the tilt angle  of 3262907_1 by 8 degrees
- `C21`: Check test server and transmission issues
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217049_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.449 | MS1 | 121.4656656880 | 31.1446236558 | 355 | 504990 | -80.47 | 17.83 | 503.96 | 0.00 | 2.48 | 1575 |
| 2024-09-20 22:21:32.320 | MS1 | 121.4656732008 | 31.1446375698 | 355 | 504990 | -78.35 | 12.90 | 498.30 | 0.10 | 2.09 | 1583 |
| 2024-09-20 22:21:33.632 | MS1 | 121.4656746442 | 31.1446200209 | 355 | 504990 | -84.21 | 17.49 | 321.40 | 0.10 | 2.57 | 1600 |
| 2024-09-20 22:21:34.413 | MS1 | 121.4656757881 | 31.1446181160 | 355 | 504990 | -83.90 | -3.49 | 57.66 | 0.01 | 1.03 | 1586 |
| 2024-09-20 22:21:35.543 | MS1 | 121.4656690452 | 31.1446379715 | 355 | 504990 | -83.05 | -1.95 | 47.13 | 0.16 | 1.07 | 1584 |
| 2024-09-20 22:21:36.858 | MS1 | 121.4656724057 | 31.1446328202 | 355 | 504990 | -83.81 | -0.12 | 43.64 | 0.01 | 1.37 | 1569 |
| 2024-09-20 22:21:37.134 | MS1 | 121.4656724401 | 31.1446319955 | 355 | 504990 | -85.17 | -1.68 | 64.45 | 0.10 | 1.06 | 1579 |
| 2024-09-20 22:21:38.798 | MS1 | 121.4656601717 | 31.1446320086 | 355 | 504990 | -84.72 | -2.42 | 75.77 | 0.00 | 1.44 | 1574 |
| 2024-09-20 22:21:39.717 | MS1 | 121.4656619838 | 31.1446298968 | 98 | 504990 | -84.32 | 13.06 | 253.84 | 0.16 | 1.24 | 1576 |
| 2024-09-20 22:21:40.121 | MS1 | 121.4656582094 | 31.1446181925 | 98 | 504990 | -79.48 | 16.38 | 465.35 | 0.19 | 2.95 | 1570 |
| 2024-09-20 22:21:41.631 | MS1 | 121.4656675481 | 31.1446374612 | 98 | 504990 | -84.50 | 13.07 | 417.43 | 0.12 | 2.65 | 1590 |
| 2024-09-20 22:21:42.514 | MS1 | 121.4656607447 | 31.1446265140 | 98 | 504990 | -81.11 | 15.40 | 499.85 | 0.05 | 2.97 | 1600 |

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
| 3217049 | 2 | 121.4647054603 | 31.1558447794 | 304 | 5 | 3 | 27.1 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3251041 | 3 | 121.4646136147 | 31.1522770258 | 136 | 3 | 1 | 28.9 | TDD | 155 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3262907 | 1 | 121.4752185245 | 31.1475437026 | 115 | 6 | 4 | 40.0 | TDD | 98 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3270456 | 4 | 121.4676949973 | 31.1496186862 | 200 | 6 | 9 | 47.3 | TDD | 14 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.072 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.095 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.225 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.225 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.916 | NREventA3 | measId:2;ServCellPCI:483;Se... |
| 2024-09-20 22:21:38.156 | NRHandoverAttempt | SourcePCI:483;SourceNR-ARFC... |
| 2024-09-20 22:21:38.195 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.207 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.311 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.311 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262907 | 1 | 19.4898 | 5.9850 | -115.9325 | 5.8120 | 133.8947 | 0.0153 | 0.0141 |
| 2024_09_20 22:00 | 3217049 | 2 | 18.7119 | 5.7795 | -116.7035 | 12.3336 | 108.3319 | 0.0041 | 0.1252 |
| 2024_09_20 22:00 | 3251041 | 3 | 5.8990 | 16.1725 | -114.6812 | 16.6601 | 162.2343 | 0.0011 | 0.0135 |
| 2024_09_20 22:00 | 3270456 | 4 | 7.1341 | 9.0352 | -115.7599 | 17.0630 | 173.8037 | 0.0142 | 0.0063 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413430_D88E9D40 | 504990 | 98 | -79.1 | 504990 | 355 | -82.1 | 504990 | 14 | -84.1 | 504990 | 155 |
| MR_1774413430_AAB5C9DD | 504990 | 355 | -82.3 | 504990 | 98 | -77.8 | 504990 | 14 | -85.7 | 504990 | 155 |
| MR_1774413430_E4C1A6E8 | 504990 | 355 | -82.2 | 504990 | 98 | -79.4 | 504990 | 14 | -84.0 | 504990 | 155 |
| MR_1774413430_D4057756 | 504990 | 355 | -82.6 | 504990 | 98 | -78.4 | 504990 | 14 | -83.0 | 504990 | 155 |
| MR_1774413430_CC638A4F | 504990 | 355 | -82.5 | 504990 | 98 | -76.2 | 504990 | 14 | -86.5 | 504990 | 155 |
| MR_1774413430_40FBF971 | 504990 | 98 | -79.0 | 504990 | 355 | -84.0 | 504990 | 14 | -86.3 | 504990 | 155 |
| MR_1774413430_8CBE7C21 | 504990 | 98 | -78.9 | 504990 | 355 | -85.8 | 504990 | 14 | -83.8 | 504990 | 155 |
| MR_1774413430_2F1A1F86 | 504990 | 355 | -85.8 | 504990 | 98 | -79.5 | 504990 | 14 | -83.1 | 504990 | 155 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 304: `8a2feb2d-90f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8a2feb2d-90fa-4231-89f8-00742b5137e6` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[304] topology](images/test_0304.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3232395_3 by 5 degrees
- `C2`: Add neighbor relationship between 3235837_1 and 3232395_3
- `C3`: Press down the tilt angle of 3266511_4 by 7 degrees
- `C4`: Decrease transmission power for 3232395_3
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase transmission power for 3266511_4
- `C7`: Adjust the azimuth of 3266511_4 by 50 degrees
- `C8`: Decrease A3 Offset threshold for 3266511_4
- `C9`: Add neighbor relationship between 3266511_4 and 3232395_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232395_3
- `C11`: Decrease transmission power for 3266511_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232395_3
- `C13`: Increase A3 Offset threshold for 3232395_3
- `C14`: Adjust the azimuth of 3232395_3 by 30 degrees
- `C15`: Increase transmission power for 3232395_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266511_4
- `C17`: Decrease A3 Offset threshold for 3232395_3
- `C18`: Increase A3 Offset threshold for 3266511_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266511_4
- `C20`: Lift the tilt angle of 3266511_4 by 7 degrees
- `C21`: Lift the tilt angle  of 3232395_3 by 5 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.724 | MS1 | 121.4656770262 | 31.1446202556 | 54 | 504990 | -91.79 | 17.80 | 559.93 | 0.09 | 2.75 | 1594 |
| 2024-09-20 22:21:32.334 | MS1 | 121.4656664939 | 31.1446370762 | 54 | 504990 | -90.81 | 13.72 | 560.17 | 0.03 | 2.11 | 1600 |
| 2024-09-20 22:21:33.403 | MS1 | 121.4656727847 | 31.1446239150 | 54 | 504990 | -85.23 | 14.43 | 391.15 | 0.19 | 2.21 | 1589 |
| 2024-09-20 22:21:34.342 | MS1 | 121.4656702203 | 31.1446221412 | 54 | 504990 | -102.05 | -0.81 | 44.53 | 0.04 | 1.40 | 1598 |
| 2024-09-20 22:21:35.762 | MS1 | 121.4656608562 | 31.1446193616 | 54 | 504990 | -100.46 | 1.23 | 67.89 | 0.17 | 1.05 | 1576 |
| 2024-09-20 22:21:36.773 | MS1 | 121.4656717861 | 31.1446347649 | 54 | 504990 | -104.89 | -0.79 | 47.51 | 0.15 | 1.41 | 1560 |
| 2024-09-20 22:21:37.350 | MS1 | 121.4656721983 | 31.1446340533 | 54 | 504990 | -105.57 | 1.32 | 76.79 | 0.17 | 1.41 | 1587 |
| 2024-09-20 22:21:38.589 | MS1 | 121.4656734473 | 31.1446366656 | 54 | 504990 | -105.72 | 0.28 | 44.97 | 0.01 | 1.31 | 1566 |
| 2024-09-20 22:21:39.161 | MS1 | 121.4656731725 | 31.1446369221 | 54 | 504990 | -108.88 | -0.68 | 83.75 | 0.15 | 1.10 | 1569 |
| 2024-09-20 22:21:40.391 | MS1 | 121.4656590776 | 31.1446190672 | 54 | 504990 | -92.10 | 15.15 | 354.95 | 0.16 | 2.04 | 1599 |
| 2024-09-20 22:21:41.650 | MS1 | 121.4656659726 | 31.1446307832 | 54 | 504990 | -92.21 | 14.87 | 363.04 | 0.19 | 2.51 | 1570 |
| 2024-09-20 22:21:42.330 | MS1 | 121.4656732336 | 31.1446235936 | 54 | 504990 | -87.11 | 12.97 | 479.14 | 0.09 | 2.61 | 1565 |

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
| 3232395 | 3 | 121.4750984211 | 31.1445467318 | 241 | 2 | 7 | 42.8 | TDD | 381 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3235837 | 1 | 121.4654765179 | 31.1457386158 | 150 | 2 | 11 | 44.4 | TDD | 904 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3250740 | 2 | 121.4757460509 | 31.1519476874 | 269 | 6 | 0 | 20.0 | TDD | 131 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3266511 | 4 | 121.4656846885 | 31.1521275309 | 118 | 6 | 3 | 20.0 | TDD | 54 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.478 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.502 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.630 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.630 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.818 | NREventA2 | measId:1;ServCellPCI:946;Se... |
| 2024-09-20 22:21:34.928 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235837 | 1 | 18.4527 | 17.8008 | -117.3770 | 9.7380 | 198.0944 | 0.0184 | 0.0084 |
| 2024_09_20 22:00 | 3250740 | 2 | 6.7575 | 10.0793 | -116.8138 | 6.0450 | 147.0952 | 0.0051 | 0.0085 |
| 2024_09_20 22:00 | 3232395 | 3 | 12.2506 | 11.3307 | -117.4710 | 14.8567 | 188.2913 | 0.0196 | 0.0045 |
| 2024_09_20 22:00 | 3266511 | 4 | 7.5123 | 9.6602 | -114.1448 | 6.4668 | 110.0126 | 0.1693 | 0.0082 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414578_C104935D | 504990 | 54 | -101.6 | 504990 | 381 | -107.1 | 504990 | 904 | -111.7 | 504990 | 131 |
| MR_1774414578_5D39930C | 504990 | 54 | -103.0 | 504990 | 381 | -105.9 | 504990 | 904 | -110.6 | 504990 | 131 |
| MR_1774414578_15F6934D | 504990 | 54 | -100.1 | 504990 | 381 | -106.2 | 504990 | 904 | -110.9 | 504990 | 131 |
| MR_1774414578_B17F2E32 | 504990 | 54 | -102.9 | 504990 | 381 | -108.1 | 504990 | 904 | -109.5 | 504990 | 131 |
| MR_1774414578_BF870ED7 | 504990 | 54 | -101.7 | 504990 | 381 | -106.7 | 504990 | 904 | -109.3 | 504990 | 131 |
| MR_1774414578_D9DBA0F2 | 504990 | 54 | -101.8 | 504990 | 381 | -104.5 | 504990 | 904 | -110.2 | 504990 | 131 |
| MR_1774414578_29DE3B50 | 504990 | 54 | -103.7 | 504990 | 381 | -104.5 | 504990 | 904 | -111.7 | 504990 | 131 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 305: `56a98aea-02e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `56a98aea-02e0-4a30-9315-715c1e8bd1f3` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[305] topology](images/test_0305.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3253475_3
- `C2`: Lift the tilt angle of 3253475_3 by 8 degrees
- `C3`: Press down the tilt angle of 3253475_3 by 8 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223962_2
- `C5`: Increase A3 Offset threshold for 3253475_3
- `C6`: Decrease A3 Offset threshold for 3253475_3
- `C7`: Lift the tilt angle  of 3223962_2 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3223962_2
- `C9`: Adjust the azimuth of 3253475_3 by 50 degrees
- `C10`: Increase A3 Offset threshold for 3223962_2
- `C11`: Press down the tilt angle  of 3223962_2 by 10 degrees
- `C12`: Decrease transmission power for 3223962_2
- `C13`: Increase transmission power for 3253475_3
- `C14`: Adjust the azimuth of 3223962_2 by 50 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223962_2
- `C16`: Check test server and transmission issues
- `C17`: Increase transmission power for 3223962_2
- `C18`: Add neighbor relationship between 3270245_4 and 3223962_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253475_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253475_3
- `C21`: Add neighbor relationship between 3253475_3 and 3223962_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.845 | MS1 | 121.4656596960 | 31.1446280689 | 547 | 504990 | -78.41 | 12.02 | 585.91 | 0.17 | 2.18 | 1562 |
| 2024-09-20 22:21:32.991 | MS1 | 121.4656708913 | 31.1446187287 | 547 | 504990 | -79.19 | 14.74 | 351.70 | 0.02 | 2.96 | 1575 |
| 2024-09-20 22:21:33.710 | MS1 | 121.4656628472 | 31.1446193163 | 547 | 504990 | -82.34 | 17.54 | 335.56 | 0.01 | 2.24 | 1598 |
| 2024-09-20 22:21:34.612 | MS1 | 121.4656646951 | 31.1446257774 | 547 | 504990 | -89.00 | -3.41 | 47.35 | 0.05 | 1.04 | 1600 |
| 2024-09-20 22:21:35.814 | MS1 | 121.4656680037 | 31.1446268219 | 547 | 504990 | -87.23 | -1.89 | 62.97 | 0.07 | 1.30 | 1585 |
| 2024-09-20 22:21:36.660 | MS1 | 121.4656657634 | 31.1446200420 | 547 | 504990 | -88.55 | -1.88 | 30.90 | 0.15 | 1.16 | 1578 |
| 2024-09-20 22:21:37.946 | MS1 | 121.4656642561 | 31.1446239380 | 547 | 504990 | -87.75 | -1.90 | 71.11 | 0.18 | 1.32 | 1593 |
| 2024-09-20 22:21:38.297 | MS1 | 121.4656721657 | 31.1446263730 | 547 | 504990 | -92.59 | -1.78 | 66.09 | 0.09 | 1.41 | 1575 |
| 2024-09-20 22:21:39.737 | MS1 | 121.4656745683 | 31.1446203583 | 234 | 504990 | -80.19 | 16.08 | 180.53 | 0.15 | 1.15 | 1592 |
| 2024-09-20 22:21:40.755 | MS1 | 121.4656770025 | 31.1446267031 | 234 | 504990 | -84.30 | 17.38 | 475.99 | 0.18 | 2.74 | 1569 |
| 2024-09-20 22:21:41.893 | MS1 | 121.4656688085 | 31.1446226574 | 234 | 504990 | -76.52 | 14.64 | 477.83 | 0.09 | 2.93 | 1569 |
| 2024-09-20 22:21:42.382 | MS1 | 121.4656683527 | 31.1446309633 | 234 | 504990 | -83.86 | 13.07 | 362.98 | 0.03 | 2.84 | 1564 |

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
| 3223962 | 2 | 121.4646925721 | 31.1476295666 | 7 | 9 | 3 | 40.4 | TDD | 234 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3253475 | 3 | 121.4669222307 | 31.1503358577 | 243 | 6 | 7 | 21.2 | TDD | 547 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3263152 | 1 | 121.4758616872 | 31.1498658032 | 195 | 14 | 5 | 35.7 | TDD | 513 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3270245 | 4 | 121.4713390255 | 31.1549234781 | 48 | 14 | 1 | 24.2 | TDD | 117 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.773 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.796 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.896 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.896 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.628 | NREventA3 | measId:2;ServCellPCI:9;Serv... |
| 2024-09-20 22:21:37.868 | NRHandoverAttempt | SourcePCI:9;SourceNR-ARFCN:... |
| 2024-09-20 22:21:37.913 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.925 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.038 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.038 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263152 | 1 | 13.4232 | 16.4208 | -116.1878 | 12.2628 | 117.5056 | 0.0155 | 0.0179 |
| 2024_09_20 22:00 | 3223962 | 2 | 9.5514 | 7.6786 | -115.5432 | 16.2344 | 85.0883 | 0.0117 | 0.0170 |
| 2024_09_20 22:00 | 3253475 | 3 | 6.7814 | 17.6797 | -116.4969 | 7.2254 | 149.9735 | 0.0031 | 0.1105 |
| 2024_09_20 22:00 | 3270245 | 4 | 10.2275 | 15.4854 | -117.0143 | 15.4816 | 143.8833 | 0.0171 | 0.0106 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416982_8AD8F22E | 504990 | 234 | -82.6 | 504990 | 547 | -87.8 | 504990 | 117 | -91.3 | 504990 | 513 |
| MR_1774416982_A249F956 | 504990 | 547 | -90.6 | 504990 | 234 | -83.6 | 504990 | 117 | -91.2 | 504990 | 513 |
| MR_1774416982_5B68BAE4 | 504990 | 547 | -89.6 | 504990 | 234 | -83.0 | 504990 | 117 | -91.2 | 504990 | 513 |
| MR_1774416982_96E32129 | 504990 | 234 | -83.7 | 504990 | 547 | -89.7 | 504990 | 117 | -89.0 | 504990 | 513 |
| MR_1774416982_56D6BBB2 | 504990 | 234 | -84.1 | 504990 | 547 | -88.2 | 504990 | 117 | -89.9 | 504990 | 513 |
| MR_1774416982_3F77EFFC | 504990 | 547 | -89.9 | 504990 | 234 | -85.0 | 504990 | 117 | -89.9 | 504990 | 513 |
| MR_1774416982_4ED64AF6 | 504990 | 547 | -87.5 | 504990 | 234 | -85.0 | 504990 | 117 | -91.3 | 504990 | 513 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 306: `f7ab4aa3-211...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f7ab4aa3-2110-4765-ada3-6e2dfcd9ebd0` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[306] topology](images/test_0306.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3279122_1 by 2 degrees
- `C2`: Adjust the azimuth of 3279122_1 by 14 degrees
- `C3`: Adjust the azimuth of 3253708_3 by 50 degrees
- `C4`: Check test server and transmission issues
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279122_1
- `C6`: Decrease A3 Offset threshold for 3279122_1
- `C7`: Decrease A3 Offset threshold for 3253708_3
- `C8`: Press down the tilt angle  of 3253708_3 by 7 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Increase A3 Offset threshold for 3253708_3
- `C11`: Add neighbor relationship between 3279122_1 and 3253708_3
- `C12`: Decrease transmission power for 3279122_1
- `C13`: Increase A3 Offset threshold for 3279122_1
- `C14`: Increase transmission power for 3253708_3
- `C15`: Decrease transmission power for 3253708_3
- `C16`: Add neighbor relationship between 3257108_4 and 3253708_3
- `C17`: Press down the tilt angle of 3279122_1 by 2 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253708_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253708_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279122_1
- `C21`: Lift the tilt angle  of 3253708_3 by 7 degrees
- `C22`: Increase transmission power for 3279122_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.424 | MS1 | 121.4656580479 | 31.1446347968 | 216 | 504990 | -90.70 | 16.19 | 405.77 | 0.06 | 2.59 | 1577 |
| 2024-09-20 22:21:32.456 | MS1 | 121.4656775042 | 31.1446228569 | 216 | 504990 | -86.51 | 14.74 | 598.44 | 0.06 | 2.16 | 1597 |
| 2024-09-20 22:21:33.845 | MS1 | 121.4656770290 | 31.1446318094 | 216 | 504990 | -88.06 | 13.20 | 525.56 | 0.20 | 2.41 | 1596 |
| 2024-09-20 22:21:34.474 | MS1 | 121.4656648791 | 31.1446205257 | 216 | 504990 | -87.52 | 16.28 | 61.76 | 0.51 | 2.19 | 655 |
| 2024-09-20 22:21:35.900 | MS1 | 121.4656662828 | 31.1446377624 | 216 | 504990 | -86.79 | 17.55 | 56.23 | 0.51 | 2.32 | 518 |
| 2024-09-20 22:21:36.450 | MS1 | 121.4656600572 | 31.1446242836 | 216 | 504990 | -86.50 | 13.53 | 55.27 | 0.63 | 2.01 | 644 |
| 2024-09-20 22:21:37.910 | MS1 | 121.4656755016 | 31.1446221331 | 216 | 504990 | -93.59 | 7.11 | 60.95 | 0.57 | 2.49 | 636 |
| 2024-09-20 22:21:38.836 | MS1 | 121.4656772980 | 31.1446337544 | 216 | 504990 | -93.43 | 9.42 | 54.23 | 0.57 | 2.04 | 547 |
| 2024-09-20 22:21:39.954 | MS1 | 121.4656693334 | 31.1446314409 | 216 | 504990 | -90.55 | 7.44 | 62.51 | 0.56 | 2.30 | 510 |
| 2024-09-20 22:21:40.436 | MS1 | 121.4656605282 | 31.1446338589 | 216 | 504990 | -92.64 | 7.60 | 508.54 | 0.17 | 2.42 | 1563 |
| 2024-09-20 22:21:41.332 | MS1 | 121.4656773377 | 31.1446361525 | 216 | 504990 | -91.93 | 11.32 | 398.92 | 0.18 | 2.55 | 1594 |
| 2024-09-20 22:21:42.959 | MS1 | 121.4656584066 | 31.1446368662 | 216 | 504990 | -89.25 | 8.74 | 408.17 | 0.16 | 2.11 | 1569 |

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
| 3244212 | 2 | 121.4657066273 | 31.1532859437 | 271 | 14 | 11 | 34.1 | TDD | 361 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3253708 | 3 | 121.4745222827 | 31.1515249177 | 64 | 6 | 6 | 22.2 | TDD | 408 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3257108 | 4 | 121.4650683322 | 31.1558276183 | 268 | 5 | 11 | 20.7 | TDD | 438 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3279122 | 1 | 121.4754615324 | 31.1468952036 | 241 | 1 | 3 | 21.5 | TDD | 216 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.594 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.618 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.760 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.760 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.484 | NREventA3 | measId:2;ServCellPCI:105;Se... |
| 2024-09-20 22:21:38.724 | NRHandoverAttempt | SourcePCI:105;SourceNR-ARFC... |
| 2024-09-20 22:21:38.754 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.765 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.865 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.865 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279122 | 1 | 5.9013 | 14.2225 | -116.3620 | 8.9743 | 155.7954 | 0.0004 | 0.0139 |
| 2024_09_20 22:00 | 3244212 | 2 | 18.1673 | 15.2479 | -114.1270 | 10.0671 | 127.6497 | 0.0010 | 0.0026 |
| 2024_09_20 22:00 | 3253708 | 3 | 13.2920 | 13.5769 | -117.8718 | 5.7543 | 95.4185 | 0.0008 | 0.0100 |
| 2024_09_20 22:00 | 3257108 | 4 | 11.1874 | 14.7936 | -117.4413 | 13.5489 | 177.9737 | 0.0158 | 0.0018 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415763_5E7CB627 | 504990 | 216 | -87.0 | 504990 | 408 | -90.3 | 504990 | 438 | -98.0 | 504990 | 361 |
| MR_1774415763_FC639983 | 504990 | 216 | -88.9 | 504990 | 408 | -87.9 | 504990 | 438 | -97.3 | 504990 | 361 |
| MR_1774415763_523D1301 | 504990 | 216 | -89.3 | 504990 | 408 | -88.4 | 504990 | 438 | -98.1 | 504990 | 361 |
| MR_1774415763_0070BC96 | 504990 | 216 | -86.9 | 504990 | 408 | -86.7 | 504990 | 438 | -96.0 | 504990 | 361 |
| MR_1774415763_99ACEB14 | 504990 | 216 | -86.5 | 504990 | 408 | -89.6 | 504990 | 438 | -96.9 | 504990 | 361 |
| MR_1774415763_ED18E35A | 504990 | 216 | -89.2 | 504990 | 408 | -89.5 | 504990 | 438 | -97.2 | 504990 | 361 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 307: `fa34c7c0-30a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fa34c7c0-30a0-4bfc-bc66-8dc4e48d0381` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[307] topology](images/test_0307.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3271950_1 by 50 degrees
- `C2`: Increase A3 Offset threshold for 3271950_1
- `C3`: Add neighbor relationship between 3271950_1 and 3234923_4
- `C4`: Decrease transmission power for 3271950_1
- `C5`: Decrease transmission power for 3234923_4
- `C6`: Press down the tilt angle of 3271950_1 by 10 degrees
- `C7`: Increase A3 Offset threshold for 3234923_4
- `C8`: Adjust the azimuth of 3234923_4 by 14 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271950_1
- `C10`: Decrease A3 Offset threshold for 3234923_4
- `C11`: Decrease A3 Offset threshold for 3271950_1
- `C12`: Press down the tilt angle  of 3234923_4 by 10 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234923_4
- `C14`: Lift the tilt angle of 3271950_1 by 10 degrees
- `C15`: Increase transmission power for 3271950_1
- `C16`: Lift the tilt angle  of 3234923_4 by 10 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271950_1
- `C18`: Add neighbor relationship between 3238173_3 and 3234923_4
- `C19`: Check test server and transmission issues
- `C20`: Increase transmission power for 3234923_4
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234923_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.764 | MS1 | 121.4656583338 | 31.1446220393 | 248 | 504990 | -87.60 | 16.26 | 363.41 | 0.05 | 2.72 | 1594 |
| 2024-09-20 22:21:32.779 | MS1 | 121.4656604425 | 31.1446293609 | 248 | 504990 | -90.87 | 14.28 | 366.44 | 0.14 | 2.01 | 1578 |
| 2024-09-20 22:21:33.676 | MS1 | 121.4656774393 | 31.1446229420 | 248 | 504990 | -88.91 | 17.25 | 467.68 | 0.01 | 2.34 | 1578 |
| 2024-09-20 22:21:34.314 | MS1 | 121.4656610408 | 31.1446342689 | 248 | 504990 | -88.72 | 17.47 | 70.21 | 0.11 | 2.02 | 1600 |
| 2024-09-20 22:21:35.782 | MS1 | 121.4656719384 | 31.1446286217 | 248 | 504990 | -89.13 | 13.56 | 85.34 | 0.04 | 2.73 | 1594 |
| 2024-09-20 22:21:36.126 | MS1 | 121.4656633319 | 31.1446361203 | 248 | 504990 | -88.22 | 13.85 | 46.61 | 0.12 | 2.07 | 1577 |
| 2024-09-20 22:21:37.983 | MS1 | 121.4656588022 | 31.1446302214 | 248 | 504990 | -93.21 | 10.90 | 61.50 | 0.14 | 2.63 | 1598 |
| 2024-09-20 22:21:38.413 | MS1 | 121.4656609667 | 31.1446328541 | 248 | 504990 | -89.29 | 10.62 | 84.78 | 0.16 | 2.43 | 1567 |
| 2024-09-20 22:21:39.143 | MS1 | 121.4656653070 | 31.1446264384 | 248 | 504990 | -92.38 | 8.46 | 69.18 | 0.00 | 2.44 | 1598 |
| 2024-09-20 22:21:40.905 | MS1 | 121.4656739096 | 31.1446216770 | 248 | 504990 | -94.00 | 12.35 | 436.45 | 0.02 | 2.87 | 1570 |
| 2024-09-20 22:21:41.272 | MS1 | 121.4656592089 | 31.1446360397 | 248 | 504990 | -93.27 | 7.31 | 363.46 | 0.11 | 2.34 | 1580 |
| 2024-09-20 22:21:42.556 | MS1 | 121.4656614273 | 31.1446241617 | 248 | 504990 | -89.58 | 7.05 | 350.21 | 0.11 | 2.77 | 1577 |

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
| 3217968 | 2 | 121.4685256939 | 31.1482747185 | 99 | 2 | 0 | 34.0 | TDD | 761 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3234923 | 4 | 121.4697175351 | 31.1543564459 | 186 | 11 | 6 | 45.2 | TDD | 5 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3238173 | 3 | 121.4731287854 | 31.1512174359 | 125 | 4 | 8 | 47.7 | TDD | 202 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3271950 | 1 | 121.4695311761 | 31.1465389606 | 292 | 14 | 4 | 22.6 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.201 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.226 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.337 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.337 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.022 | NREventA3 | measId:2;ServCellPCI:200;Se... |
| 2024-09-20 22:21:38.262 | NRHandoverAttempt | SourcePCI:200;SourceNR-ARFC... |
| 2024-09-20 22:21:38.311 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.321 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.427 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.427 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3271950 | 1 | 94.6712 | 77.9057 | -117.3387 | 19.2896 | 126.8647 | 0.0056 | 0.0094 |
| 2024_09_19 22:00 | 3217968 | 2 | 77.6305 | 92.9081 | -114.3935 | 9.7000 | 170.2972 | 0.0114 | 0.0142 |
| 2024_09_19 22:00 | 3238173 | 3 | 86.8176 | 93.8934 | -117.1408 | 14.9746 | 193.3096 | 0.0183 | 0.0143 |
| 2024_09_19 22:00 | 3234923 | 4 | 83.5278 | 80.8255 | -114.8735 | 9.6045 | 162.7559 | 0.0090 | 0.0017 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414294_1599AEE7 | 504990 | 248 | -89.3 | 504990 | 5 | -94.1 | 504990 | 202 | -99.1 | 504990 | 761 |
| MR_1774414294_25A235AA | 504990 | 248 | -89.9 | 504990 | 5 | -92.4 | 504990 | 202 | -99.4 | 504990 | 761 |
| MR_1774414294_5992F57E | 504990 | 248 | -89.2 | 504990 | 5 | -92.2 | 504990 | 202 | -97.9 | 504990 | 761 |
| MR_1774414294_4142C28D | 504990 | 248 | -90.2 | 504990 | 5 | -91.1 | 504990 | 202 | -99.8 | 504990 | 761 |
| MR_1774414294_3DF24327 | 504990 | 248 | -90.7 | 504990 | 5 | -93.2 | 504990 | 202 | -99.8 | 504990 | 761 |
| MR_1774414294_F8D95D98 | 504990 | 248 | -88.9 | 504990 | 5 | -91.0 | 504990 | 202 | -99.4 | 504990 | 761 |
| MR_1774414294_0045B063 | 504990 | 248 | -89.8 | 504990 | 5 | -94.3 | 504990 | 202 | -99.2 | 504990 | 761 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 308: `b2c2f51c-d86...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b2c2f51c-d86d-4105-b995-7e697de1f02f` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[308] topology](images/test_0308.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3211551_2
- `C2`: Check test server and transmission issues
- `C3`: Decrease A3 Offset threshold for 3246956_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211551_2
- `C5`: Add neighbor relationship between 3246646_4 and 3211551_2
- `C6`: Adjust the azimuth of 3211551_2 by 49 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246956_3
- `C8`: Increase A3 Offset threshold for 3246956_3
- `C9`: Decrease transmission power for 3211551_2
- `C10`: Press down the tilt angle  of 3211551_2 by 10 degrees
- `C11`: Decrease transmission power for 3246956_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246956_3
- `C13`: Add neighbor relationship between 3246956_3 and 3211551_2
- `C14`: Lift the tilt angle of 3246956_3 by 10 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211551_2
- `C16`: Press down the tilt angle of 3246956_3 by 10 degrees
- `C17`: Decrease A3 Offset threshold for 3211551_2
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Lift the tilt angle  of 3211551_2 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3211551_2
- `C21`: Increase transmission power for 3246956_3
- `C22`: Adjust the azimuth of 3246956_3 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.750 | MS1 | 121.4656624897 | 31.1446240506 | 829 | 504990 | -85.39 | 15.60 | 587.55 | 0.02 | 2.80 | 1582 |
| 2024-09-20 22:21:32.247 | MS1 | 121.4656761470 | 31.1446287701 | 829 | 504990 | -86.08 | 13.99 | 486.03 | 0.18 | 2.08 | 1580 |
| 2024-09-20 22:21:33.702 | MS1 | 121.4656742030 | 31.1446253035 | 829 | 504990 | -88.88 | 16.29 | 344.79 | 0.15 | 2.85 | 1575 |
| 2024-09-20 22:21:34.659 | MS1 | 121.4656706184 | 31.1446375459 | 829 | 504990 | -88.00 | 12.41 | 100.89 | 0.03 | 2.55 | 429 |
| 2024-09-20 22:21:35.467 | MS1 | 121.4656614851 | 31.1446220507 | 829 | 504990 | -86.52 | 12.45 | 83.93 | 0.14 | 2.39 | 457 |
| 2024-09-20 22:21:36.826 | MS1 | 121.4656765866 | 31.1446274243 | 829 | 504990 | -85.93 | 12.76 | 58.51 | 0.02 | 2.57 | 331 |
| 2024-09-20 22:21:37.738 | MS1 | 121.4656690673 | 31.1446237540 | 829 | 504990 | -89.02 | 12.51 | 75.01 | 0.05 | 2.33 | 423 |
| 2024-09-20 22:21:38.431 | MS1 | 121.4656664882 | 31.1446216347 | 829 | 504990 | -89.25 | 12.29 | 102.64 | 0.01 | 2.79 | 383 |
| 2024-09-20 22:21:39.611 | MS1 | 121.4656628510 | 31.1446310318 | 829 | 504990 | -92.11 | 10.35 | 105.79 | 0.14 | 2.22 | 380 |
| 2024-09-20 22:21:40.670 | MS1 | 121.4656580639 | 31.1446188371 | 829 | 504990 | -93.13 | 9.00 | 360.40 | 0.08 | 2.07 | 1573 |
| 2024-09-20 22:21:41.511 | MS1 | 121.4656712144 | 31.1446185903 | 829 | 504990 | -91.49 | 7.06 | 594.15 | 0.07 | 2.55 | 1564 |
| 2024-09-20 22:21:42.661 | MS1 | 121.4656684017 | 31.1446210553 | 829 | 504990 | -92.10 | 11.43 | 356.94 | 0.18 | 2.38 | 1579 |

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
| 3211551 | 2 | 121.4650783418 | 31.1486255262 | 124 | 7 | 1 | 21.2 | TDD | 226 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3246646 | 4 | 121.4709077086 | 31.1543858258 | 15 | 10 | 2 | 33.1 | TDD | 879 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3246956 | 3 | 121.4735344276 | 31.1538767495 | 37 | 12 | 10 | 15.4 | TDD | 829 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3276824 | 1 | 121.4710294892 | 31.1532731550 | 338 | 15 | 5 | 25.3 | TDD | 185 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.287 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.304 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.434 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.434 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.173 | NREventA3 | measId:2;ServCellPCI:918;Se... |
| 2024-09-20 22:21:38.413 | NRHandoverAttempt | SourcePCI:918;SourceNR-ARFC... |
| 2024-09-20 22:21:38.458 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.473 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.603 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.603 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276824 | 1 | 8.6680 | 19.0173 | -114.0518 | 11.6947 | 191.0514 | 0.0100 | 0.0054 |
| 2024_09_20 22:00 | 3211551 | 2 | 13.3098 | 19.8325 | -117.9833 | 15.5991 | 107.9781 | 0.0005 | 0.0043 |
| 2024_09_20 22:00 | 3246956 | 3 | 6.3151 | 17.9869 | -115.9002 | 16.1754 | 147.9251 | 0.0177 | 0.0147 |
| 2024_09_20 22:00 | 3246646 | 4 | 12.4543 | 16.8551 | -114.2386 | 14.1184 | 138.0331 | 0.0022 | 0.0137 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417020_6D38422D | 504990 | 829 | -86.7 | 504990 | 226 | -88.7 | 504990 | 879 | -95.1 | 504990 | 185 |
| MR_1774417020_30EA0B63 | 504990 | 829 | -88.4 | 504990 | 226 | -90.9 | 504990 | 879 | -98.7 | 504990 | 185 |
| MR_1774417020_E591C944 | 504990 | 829 | -88.4 | 504990 | 226 | -91.7 | 504990 | 879 | -98.2 | 504990 | 185 |
| MR_1774417020_FCBFAFE0 | 504990 | 829 | -85.7 | 504990 | 226 | -88.8 | 504990 | 879 | -96.3 | 504990 | 185 |
| MR_1774417020_E7A51B66 | 504990 | 829 | -88.3 | 504990 | 226 | -89.0 | 504990 | 879 | -95.0 | 504990 | 185 |
| MR_1774417020_29DA5824 | 504990 | 829 | -87.7 | 504990 | 226 | -89.3 | 504990 | 879 | -98.2 | 504990 | 185 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 309: `36f53307-797...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `36f53307-797a-418f-8328-63e72b87a206` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[309] topology](images/test_0309.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240182_2
- `C2`: Increase transmission power for 3266632_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266632_1
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Increase transmission power for 3240182_2
- `C6`: Decrease transmission power for 3266632_1
- `C7`: Add neighbor relationship between 3266632_1 and 3240182_2
- `C8`: Lift the tilt angle of 3266632_1 by 10 degrees
- `C9`: Adjust the azimuth of 3240182_2 by 50 degrees
- `C10`: Check test server and transmission issues
- `C11`: Adjust the azimuth of 3266632_1 by 50 degrees
- `C12`: Increase A3 Offset threshold for 3266632_1
- `C13`: Decrease A3 Offset threshold for 3266632_1
- `C14`: Press down the tilt angle  of 3240182_2 by 10 degrees
- `C15`: Decrease transmission power for 3240182_2
- `C16`: Decrease A3 Offset threshold for 3240182_2
- `C17`: Add neighbor relationship between 3264785_4 and 3240182_2
- `C18`: Press down the tilt angle of 3266632_1 by 10 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266632_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240182_2
- `C21`: Increase A3 Offset threshold for 3240182_2
- `C22`: Lift the tilt angle  of 3240182_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.567 | MS1 | 121.4656746175 | 31.1446346392 | 184 | 504990 | -91.59 | 15.18 | 317.18 | 0.10 | 2.57 | 1566 |
| 2024-09-20 22:21:32.215 | MS1 | 121.4656618204 | 31.1446339857 | 184 | 504990 | -90.79 | 17.18 | 553.38 | 0.19 | 2.38 | 1564 |
| 2024-09-20 22:21:33.152 | MS1 | 121.4656660602 | 31.1446366858 | 184 | 504990 | -89.22 | 15.48 | 370.19 | 0.19 | 2.25 | 1591 |
| 2024-09-20 22:21:34.815 | MS1 | 121.4656704742 | 31.1446276224 | 184 | 504990 | -85.01 | 12.09 | 60.91 | 0.01 | 2.10 | 326 |
| 2024-09-20 22:21:35.946 | MS1 | 121.4656686605 | 31.1446255351 | 184 | 504990 | -89.76 | 16.56 | 83.78 | 0.16 | 2.53 | 306 |
| 2024-09-20 22:21:36.259 | MS1 | 121.4656645845 | 31.1446262035 | 184 | 504990 | -89.17 | 13.53 | 88.07 | 0.09 | 2.07 | 320 |
| 2024-09-20 22:21:37.816 | MS1 | 121.4656696195 | 31.1446306814 | 184 | 504990 | -90.39 | 8.82 | 84.46 | 0.14 | 2.90 | 379 |
| 2024-09-20 22:21:38.338 | MS1 | 121.4656683654 | 31.1446268308 | 184 | 504990 | -91.91 | 8.95 | 66.27 | 0.11 | 2.79 | 349 |
| 2024-09-20 22:21:39.804 | MS1 | 121.4656603964 | 31.1446252571 | 184 | 504990 | -91.64 | 7.36 | 94.81 | 0.14 | 2.46 | 494 |
| 2024-09-20 22:21:40.379 | MS1 | 121.4656611732 | 31.1446230955 | 184 | 504990 | -93.34 | 7.90 | 379.19 | 0.16 | 2.36 | 1572 |
| 2024-09-20 22:21:41.847 | MS1 | 121.4656764508 | 31.1446330485 | 184 | 504990 | -90.47 | 7.74 | 379.00 | 0.18 | 2.22 | 1561 |
| 2024-09-20 22:21:42.399 | MS1 | 121.4656709577 | 31.1446304993 | 184 | 504990 | -91.61 | 7.79 | 560.68 | 0.01 | 2.53 | 1584 |

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
| 3240182 | 2 | 121.4664979386 | 31.1542020352 | 108 | 10 | 8 | 45.8 | TDD | 986 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3260872 | 3 | 121.4728891822 | 31.1443494060 | 26 | 5 | 10 | 44.4 | TDD | 531 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3264785 | 4 | 121.4671310104 | 31.1535450631 | 252 | 3 | 0 | 36.7 | TDD | 814 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3266632 | 1 | 121.4717103172 | 31.1447156997 | 47 | 12 | 1 | 42.6 | TDD | 184 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.359 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.375 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.509 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.509 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.240 | NREventA3 | measId:2;ServCellPCI:860;Se... |
| 2024-09-20 22:21:38.480 | NRHandoverAttempt | SourcePCI:860;SourceNR-ARFC... |
| 2024-09-20 22:21:38.517 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.528 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.643 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.643 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266632 | 1 | 7.5032 | 12.3772 | -115.3775 | 16.9058 | 92.9773 | 0.0108 | 0.0177 |
| 2024_09_20 22:00 | 3240182 | 2 | 9.4004 | 13.0721 | -117.7422 | 18.7311 | 191.1154 | 0.0162 | 0.0167 |
| 2024_09_20 22:00 | 3260872 | 3 | 5.0409 | 11.1060 | -117.7330 | 8.3147 | 103.3182 | 0.0028 | 0.0014 |
| 2024_09_20 22:00 | 3264785 | 4 | 16.8396 | 11.0211 | -114.5754 | 17.4170 | 113.9157 | 0.0109 | 0.0042 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415891_CA2F85ED | 504990 | 184 | -83.4 | 504990 | 986 | -89.3 | 504990 | 814 | -90.7 | 504990 | 531 |
| MR_1774415891_ABA19CB9 | 504990 | 184 | -85.1 | 504990 | 986 | -92.1 | 504990 | 814 | -90.6 | 504990 | 531 |
| MR_1774415891_A56DFC1B | 504990 | 184 | -83.6 | 504990 | 986 | -91.6 | 504990 | 814 | -92.0 | 504990 | 531 |
| MR_1774415891_047B6858 | 504990 | 184 | -86.5 | 504990 | 986 | -91.7 | 504990 | 814 | -91.5 | 504990 | 531 |
| MR_1774415891_F50F2DB8 | 504990 | 184 | -84.2 | 504990 | 986 | -91.6 | 504990 | 814 | -92.7 | 504990 | 531 |
| MR_1774415891_D486EEE9 | 504990 | 184 | -83.3 | 504990 | 986 | -89.7 | 504990 | 814 | -90.7 | 504990 | 531 |
| MR_1774415891_9384DB6C | 504990 | 184 | -84.1 | 504990 | 986 | -90.9 | 504990 | 814 | -91.4 | 504990 | 531 |

> *... 2개 열 생략 (전체 14열)*

---
