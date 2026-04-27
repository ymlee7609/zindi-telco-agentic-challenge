# Track A 문제 분석 — test[250]~test[259]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[250] ~ test[259] (10개)

## 목차

1. [문제 250: `8d67eaa2-f2f...`](#250) — single-answer
2. [문제 251: `b9bf3cb0-e9c...`](#251) — single-answer
3. [문제 252: `1cc4104f-716...`](#252) — single-answer
4. [문제 253: `a4de052b-38b...`](#253) — multiple-answer
5. [문제 254: `7c24794f-c14...`](#254) — multiple-answer
6. [문제 255: `7e07891d-13e...`](#255) — single-answer
7. [문제 256: `5d9078b0-e1b...`](#256) — single-answer
8. [문제 257: `ed30b351-98d...`](#257) — single-answer
9. [문제 258: `f5d30f47-7a8...`](#258) — single-answer
10. [문제 259: `8a3f83cc-e68...`](#259) — single-answer

---

### 문제 250: `8d67eaa2-f2f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8d67eaa2-f2fd-46b4-b751-bd9b7a9f83e3` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[250] topology](images/test_0250.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3222479_3
- `C2`: Add neighbor relationship between 3222479_3 and 3236278_2
- `C3`: Decrease A3 Offset threshold for 3236278_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222479_3
- `C5`: Increase A3 Offset threshold for 3222479_3
- `C6`: Decrease transmission power for 3236278_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Add neighbor relationship between 3260968_1 and 3236278_2
- `C9`: Increase transmission power for 3222479_3
- `C10`: Lift the tilt angle  of 3260968_1 by 10 degrees
- `C11`: Adjust the azimuth of 3260968_1 by 42 degrees
- `C12`: Lift the tilt angle of 3222479_3 by 5 degrees
- `C13`: Increase transmission power for 3236278_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236278_2
- `C15`: Press down the tilt angle of 3222479_3 by 5 degrees
- `C16`: Check test server and transmission issues
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236278_2
- `C18`: Press down the tilt angle  of 3260968_1 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3236278_2
- `C20`: Decrease A3 Offset threshold for 3222479_3
- `C21`: Adjust the azimuth of 3222479_3 by 24 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222479_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.532 | MS1 | 121.4656716347 | 31.1446225883 | 372 | 504990 | -89.26 | 16.04 | 520.32 | 0.05 | 2.39 | 1599 |
| 2024-09-20 22:21:32.538 | MS1 | 121.4656729986 | 31.1446309919 | 372 | 504990 | -89.91 | 12.03 | 419.39 | 0.12 | 2.75 | 1595 |
| 2024-09-20 22:21:33.959 | MS1 | 121.4656625777 | 31.1446327097 | 372 | 504990 | -85.91 | 17.64 | 363.93 | 0.06 | 2.66 | 1582 |
| 2024-09-20 22:21:34.811 | MS1 | 121.4656727948 | 31.1446210345 | 372 | 504990 | -90.72 | 12.23 | 77.70 | 0.08 | 2.54 | 1592 |
| 2024-09-20 22:21:35.389 | MS1 | 121.4656664457 | 31.1446294077 | 372 | 504990 | -91.78 | 17.36 | 75.31 | 0.11 | 2.92 | 1574 |
| 2024-09-20 22:21:36.532 | MS1 | 121.4656694590 | 31.1446196257 | 372 | 504990 | -88.38 | 17.78 | 95.22 | 0.16 | 2.07 | 1576 |
| 2024-09-20 22:21:37.508 | MS1 | 121.4656748144 | 31.1446271031 | 372 | 504990 | -91.37 | 9.68 | 92.90 | 0.20 | 2.86 | 1563 |
| 2024-09-20 22:21:38.214 | MS1 | 121.4656745210 | 31.1446319077 | 372 | 504990 | -93.69 | 8.74 | 80.41 | 0.14 | 2.98 | 1578 |
| 2024-09-20 22:21:39.809 | MS1 | 121.4656641945 | 31.1446271011 | 372 | 504990 | -91.75 | 11.88 | 86.85 | 0.02 | 2.18 | 1582 |
| 2024-09-20 22:21:40.442 | MS1 | 121.4656595908 | 31.1446359416 | 372 | 504990 | -89.71 | 9.27 | 576.94 | 0.04 | 2.28 | 1564 |
| 2024-09-20 22:21:41.156 | MS1 | 121.4656716669 | 31.1446180752 | 372 | 504990 | -92.76 | 12.72 | 399.20 | 0.09 | 2.54 | 1587 |
| 2024-09-20 22:21:42.649 | MS1 | 121.4656731113 | 31.1446205399 | 372 | 504990 | -89.04 | 11.83 | 320.96 | 0.18 | 2.25 | 1583 |

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
| 3221053 | 4 | 121.4643579778 | 31.1501640652 | 311 | 4 | 9 | 48.1 | TDD | 477 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3222479 | 3 | 121.4664242451 | 31.1537446678 | 160 | 2 | 1 | 44.8 | TDD | 372 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3236278 | 2 | 121.4647456167 | 31.1479615584 | 125 | 7 | 11 | 19.3 | TDD | 123 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3260968 | 1 | 121.4661799822 | 31.1453449343 | 326 | 11 | 1 | 28.8 | TDD | 928 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.211 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.231 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.376 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.376 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.086 | NREventA3 | measId:2;ServCellPCI:864;Se... |
| 2024-09-20 22:21:38.326 | NRHandoverAttempt | SourcePCI:864;SourceNR-ARFC... |
| 2024-09-20 22:21:38.358 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.368 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.487 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.487 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260968 | 1 | 14.6113 | 8.4895 | -117.2165 | 11.4335 | 115.1547 | 0.0120 | 0.0100 |
| 2024_09_20 22:00 | 3236278 | 2 | 8.6230 | 16.6420 | -114.7012 | 14.8606 | 111.1372 | 0.0094 | 0.0196 |
| 2024_09_20 22:00 | 3222479 | 3 | 81.7591 | 89.4367 | -114.6198 | 17.8912 | 113.3442 | 0.0176 | 0.0117 |
| 2024_09_20 22:00 | 3221053 | 4 | 17.3345 | 12.3267 | -116.9000 | 6.7359 | 128.4435 | 0.0107 | 0.0129 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416811_5894DAAC | 504990 | 372 | -89.8 | 504990 | 123 | -96.6 | 504990 | 928 | -103.2 | 504990 | 477 |
| MR_1774416811_DE970BA9 | 504990 | 372 | -92.2 | 504990 | 123 | -99.5 | 504990 | 928 | -103.7 | 504990 | 477 |
| MR_1774416811_E6D782E0 | 504990 | 372 | -90.5 | 504990 | 123 | -99.9 | 504990 | 928 | -101.7 | 504990 | 477 |
| MR_1774416811_4A10D4B5 | 504990 | 372 | -89.5 | 504990 | 123 | -99.7 | 504990 | 928 | -103.1 | 504990 | 477 |
| MR_1774416811_A18958DF | 504990 | 372 | -91.2 | 504990 | 123 | -99.7 | 504990 | 928 | -104.1 | 504990 | 477 |
| MR_1774416811_80F6D4FF | 504990 | 372 | -91.7 | 504990 | 123 | -96.6 | 504990 | 928 | -101.7 | 504990 | 477 |
| MR_1774416811_D5B041ED | 504990 | 372 | -92.2 | 504990 | 123 | -97.3 | 504990 | 928 | -103.3 | 504990 | 477 |
| MR_1774416811_9AEE4E5D | 504990 | 372 | -90.7 | 504990 | 123 | -97.5 | 504990 | 928 | -102.5 | 504990 | 477 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 251: `b9bf3cb0-e9c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b9bf3cb0-e9c8-451b-8709-2b7d53ac9ae2` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[251] topology](images/test_0251.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Add neighbor relationship between 3213687_4 and 3216135_2
- `C3`: Adjust the azimuth of 3216135_2 by 50 degrees
- `C4`: Lift the tilt angle  of 3216135_2 by 10 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216135_2
- `C7`: Add neighbor relationship between 3260022_3 and 3216135_2
- `C8`: Decrease A3 Offset threshold for 3216135_2
- `C9`: Increase A3 Offset threshold for 3216135_2
- `C10`: Press down the tilt angle of 3260022_3 by 10 degrees
- `C11`: Decrease transmission power for 3260022_3
- `C12`: Increase A3 Offset threshold for 3260022_3
- `C13`: Press down the tilt angle  of 3216135_2 by 10 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260022_3
- `C15`: Lift the tilt angle of 3260022_3 by 10 degrees
- `C16`: Increase transmission power for 3260022_3
- `C17`: Increase transmission power for 3216135_2
- `C18`: Adjust the azimuth of 3260022_3 by 6 degrees
- `C19`: Decrease transmission power for 3216135_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216135_2
- `C21`: Decrease A3 Offset threshold for 3260022_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260022_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.371 | MS1 | 121.4656693831 | 31.1446363394 | 837 | 504990 | -76.14 | 14.26 | 480.21 | 0.02 | 2.46 | 1586 |
| 2024-09-20 22:21:32.965 | MS1 | 121.4656594693 | 31.1446358140 | 837 | 504990 | -75.69 | 16.31 | 605.46 | 0.07 | 2.50 | 1572 |
| 2024-09-20 22:21:33.940 | MS1 | 121.4656641728 | 31.1446262146 | 837 | 504990 | -76.76 | 14.49 | 322.98 | 0.05 | 2.83 | 1599 |
| 2024-09-20 22:21:34.660 | MS1 | 121.4656603101 | 31.1446355098 | 837 | 504990 | -92.89 | -3.37 | 61.51 | 0.18 | 1.45 | 1582 |
| 2024-09-20 22:21:35.256 | MS1 | 121.4656630262 | 31.1446351580 | 837 | 504990 | -85.79 | -2.73 | 32.53 | 0.01 | 1.49 | 1569 |
| 2024-09-20 22:21:36.111 | MS1 | 121.4656765346 | 31.1446310040 | 837 | 504990 | -87.47 | -0.37 | 37.09 | 0.13 | 1.47 | 1576 |
| 2024-09-20 22:21:37.264 | MS1 | 121.4656769419 | 31.1446247386 | 837 | 504990 | -92.54 | -1.16 | 56.50 | 0.07 | 1.12 | 1564 |
| 2024-09-20 22:21:38.932 | MS1 | 121.4656715776 | 31.1446280597 | 837 | 504990 | -84.45 | -2.39 | 68.20 | 0.10 | 1.31 | 1570 |
| 2024-09-20 22:21:39.600 | MS1 | 121.4656678816 | 31.1446379496 | 803 | 504990 | -77.40 | 16.80 | 176.64 | 0.17 | 1.17 | 1564 |
| 2024-09-20 22:21:40.932 | MS1 | 121.4656725225 | 31.1446229300 | 803 | 504990 | -82.46 | 16.27 | 502.52 | 0.01 | 2.40 | 1564 |
| 2024-09-20 22:21:41.219 | MS1 | 121.4656754457 | 31.1446378671 | 803 | 504990 | -76.37 | 14.26 | 394.34 | 0.17 | 2.43 | 1594 |
| 2024-09-20 22:21:42.616 | MS1 | 121.4656719550 | 31.1446321981 | 803 | 504990 | -76.10 | 14.09 | 531.22 | 0.00 | 2.79 | 1598 |

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
| 3213687 | 4 | 121.4685633925 | 31.1510749333 | 201 | 3 | 8 | 23.7 | TDD | 351 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3216135 | 2 | 121.4699745427 | 31.1507761095 | 8 | 11 | 10 | 45.5 | TDD | 803 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3260022 | 3 | 121.4746000992 | 31.1543860833 | 224 | 13 | 8 | 15.2 | TDD | 837 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3261910 | 1 | 121.4751148535 | 31.1467796816 | 42 | 1 | 3 | 37.9 | TDD | 705 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.111 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.127 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.232 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.232 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.005 | NREventA3 | measId:2;ServCellPCI:912;Se... |
| 2024-09-20 22:21:38.245 | NRHandoverAttempt | SourcePCI:912;SourceNR-ARFC... |
| 2024-09-20 22:21:38.288 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.303 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.404 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.404 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261910 | 1 | 19.9748 | 17.8517 | -116.8868 | 12.3791 | 146.2104 | 0.0132 | 0.0182 |
| 2024_09_20 22:00 | 3216135 | 2 | 10.3634 | 15.6131 | -116.2077 | 10.5633 | 93.1877 | 0.0051 | 0.0091 |
| 2024_09_20 22:00 | 3260022 | 3 | 19.1043 | 13.1919 | -115.9409 | 17.6565 | 104.7579 | 0.0079 | 0.1621 |
| 2024_09_20 22:00 | 3213687 | 4 | 11.9204 | 5.8875 | -117.5636 | 7.6198 | 167.5542 | 0.0149 | 0.0040 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414372_C3DC3E60 | 504990 | 837 | -91.2 | 504990 | 803 | -86.1 | 504990 | 351 | -96.9 | 504990 | 705 |
| MR_1774414372_8ECC06C3 | 504990 | 803 | -88.9 | 504990 | 837 | -91.2 | 504990 | 351 | -95.4 | 504990 | 705 |
| MR_1774414372_17F885DC | 504990 | 803 | -86.3 | 504990 | 837 | -91.7 | 504990 | 351 | -98.5 | 504990 | 705 |
| MR_1774414372_74CB845F | 504990 | 803 | -87.8 | 504990 | 837 | -94.9 | 504990 | 351 | -97.8 | 504990 | 705 |
| MR_1774414372_1DB4911C | 504990 | 803 | -86.3 | 504990 | 837 | -92.2 | 504990 | 351 | -96.5 | 504990 | 705 |
| MR_1774414372_3E7E7F24 | 504990 | 803 | -86.9 | 504990 | 837 | -91.0 | 504990 | 351 | -98.6 | 504990 | 705 |
| MR_1774414372_54ACBCCD | 504990 | 837 | -94.6 | 504990 | 803 | -86.6 | 504990 | 351 | -98.8 | 504990 | 705 |
| MR_1774414372_A9A66177 | 504990 | 803 | -86.2 | 504990 | 837 | -93.5 | 504990 | 351 | -96.1 | 504990 | 705 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 252: `1cc4104f-716...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1cc4104f-7166-4d4e-a061-6af23e5e1062` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[252] topology](images/test_0252.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase transmission power for 3269654_2
- `C3`: Check test server and transmission issues
- `C4`: Lift the tilt angle of 3252097_1 by 2 degrees
- `C5`: Adjust the azimuth of 3269654_2 by 50 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269654_2
- `C7`: Adjust the azimuth of 3252097_1 by 26 degrees
- `C8`: Add neighbor relationship between 3223879_3 and 3269654_2
- `C9`: Press down the tilt angle  of 3269654_2 by 10 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269654_2
- `C11`: Increase transmission power for 3252097_1
- `C12`: Decrease transmission power for 3269654_2
- `C13`: Decrease A3 Offset threshold for 3269654_2
- `C14`: Increase A3 Offset threshold for 3269654_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252097_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252097_1
- `C17`: Lift the tilt angle  of 3269654_2 by 10 degrees
- `C18`: Decrease A3 Offset threshold for 3252097_1
- `C19`: Press down the tilt angle of 3252097_1 by 2 degrees
- `C20`: Increase A3 Offset threshold for 3252097_1
- `C21`: Decrease transmission power for 3252097_1
- `C22`: Add neighbor relationship between 3252097_1 and 3269654_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.476 | MS1 | 121.4656743884 | 31.1446345560 | 602 | 504990 | -85.12 | 16.98 | 525.21 | 0.16 | 2.72 | 1573 |
| 2024-09-20 22:21:32.131 | MS1 | 121.4656659016 | 31.1446321533 | 602 | 504990 | -91.50 | 12.88 | 360.61 | 0.08 | 2.90 | 1599 |
| 2024-09-20 22:21:33.300 | MS1 | 121.4656675311 | 31.1446226105 | 602 | 504990 | -86.63 | 15.95 | 447.63 | 0.08 | 2.85 | 1600 |
| 2024-09-20 22:21:34.220 | MS1 | 121.4656718091 | 31.1446339548 | 602 | 504990 | -91.61 | 17.16 | 73.47 | 0.59 | 2.49 | 691 |
| 2024-09-20 22:21:35.336 | MS1 | 121.4656594919 | 31.1446281399 | 602 | 504990 | -89.81 | 14.67 | 72.52 | 0.65 | 2.36 | 580 |
| 2024-09-20 22:21:36.783 | MS1 | 121.4656760799 | 31.1446266717 | 602 | 504990 | -87.83 | 12.65 | 78.28 | 0.55 | 2.32 | 643 |
| 2024-09-20 22:21:37.660 | MS1 | 121.4656727047 | 31.1446335880 | 602 | 504990 | -91.07 | 12.93 | 66.82 | 0.62 | 2.82 | 505 |
| 2024-09-20 22:21:38.589 | MS1 | 121.4656599948 | 31.1446344828 | 602 | 504990 | -92.57 | 9.16 | 67.65 | 0.70 | 2.34 | 664 |
| 2024-09-20 22:21:39.863 | MS1 | 121.4656711865 | 31.1446303878 | 602 | 504990 | -90.08 | 10.06 | 93.63 | 0.58 | 2.47 | 556 |
| 2024-09-20 22:21:40.246 | MS1 | 121.4656770217 | 31.1446234025 | 602 | 504990 | -90.81 | 11.50 | 556.21 | 0.18 | 2.56 | 1589 |
| 2024-09-20 22:21:41.614 | MS1 | 121.4656586336 | 31.1446238034 | 602 | 504990 | -91.78 | 11.48 | 486.63 | 0.05 | 2.77 | 1582 |
| 2024-09-20 22:21:42.929 | MS1 | 121.4656716533 | 31.1446302955 | 602 | 504990 | -89.31 | 7.07 | 545.30 | 0.08 | 2.59 | 1570 |

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
| 3223879 | 3 | 121.4678771232 | 31.1495978921 | 241 | 3 | 7 | 20.9 | TDD | 764 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3252097 | 1 | 121.4749251685 | 31.1466058543 | 282 | 0 | 3 | 28.9 | TDD | 602 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3264102 | 4 | 121.4754657617 | 31.1486121143 | 46 | 14 | 11 | 43.5 | TDD | 685 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3269654 | 2 | 121.4689916665 | 31.1445959574 | 53 | 10 | 6 | 39.2 | TDD | 435 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.250 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.272 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.393 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.393 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.065 | NREventA3 | measId:2;ServCellPCI:122;Se... |
| 2024-09-20 22:21:38.305 | NRHandoverAttempt | SourcePCI:122;SourceNR-ARFC... |
| 2024-09-20 22:21:38.343 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.354 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.476 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.476 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252097 | 1 | 11.9921 | 5.5524 | -115.2640 | 14.6673 | 94.2625 | 0.0094 | 0.0109 |
| 2024_09_20 22:00 | 3269654 | 2 | 15.4548 | 16.9592 | -116.5609 | 7.9279 | 129.1923 | 0.0022 | 0.0002 |
| 2024_09_20 22:00 | 3223879 | 3 | 10.0698 | 13.7389 | -116.5544 | 5.4943 | 160.9249 | 0.0096 | 0.0100 |
| 2024_09_20 22:00 | 3264102 | 4 | 14.9538 | 9.1645 | -114.2645 | 9.2301 | 123.0942 | 0.0145 | 0.0076 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413868_099F245E | 504990 | 602 | -91.1 | 504990 | 435 | -92.9 | 504990 | 764 | -99.6 | 504990 | 685 |
| MR_1774413868_E9BAC685 | 504990 | 602 | -91.1 | 504990 | 435 | -91.0 | 504990 | 764 | -99.6 | 504990 | 685 |
| MR_1774413868_3706073E | 504990 | 602 | -90.3 | 504990 | 435 | -92.1 | 504990 | 764 | -99.5 | 504990 | 685 |
| MR_1774413868_327ABDDC | 504990 | 602 | -92.4 | 504990 | 435 | -92.4 | 504990 | 764 | -97.0 | 504990 | 685 |
| MR_1774413868_088AA3D2 | 504990 | 602 | -90.5 | 504990 | 435 | -91.7 | 504990 | 764 | -99.0 | 504990 | 685 |
| MR_1774413868_F3A1B724 | 504990 | 602 | -90.0 | 504990 | 435 | -92.8 | 504990 | 764 | -99.8 | 504990 | 685 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 253: `a4de052b-38b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a4de052b-38b7-4924-a84a-ba4dcb736fcc` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[253] topology](images/test_0253.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3254333_2 and 3238145_3
- `C2`: Add neighbor relationship between 3268057_4 and 3238145_3
- `C3`: Lift the tilt angle  of 3238145_3 by 5 degrees
- `C4`: Adjust the azimuth of 3238145_3 by 12 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease A3 Offset threshold for 3268057_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238145_3
- `C8`: Adjust the azimuth of 3268057_4 by 31 degrees
- `C9`: Press down the tilt angle of 3268057_4 by 4 degrees
- `C10`: Increase A3 Offset threshold for 3238145_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238145_3
- `C12`: Lift the tilt angle of 3268057_4 by 4 degrees
- `C13`: Check test server and transmission issues
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268057_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268057_4
- `C16`: Press down the tilt angle  of 3238145_3 by 5 degrees
- `C17`: Increase A3 Offset threshold for 3268057_4
- `C18`: Increase transmission power for 3268057_4
- `C19`: Decrease transmission power for 3268057_4
- `C20`: Decrease A3 Offset threshold for 3238145_3
- `C21`: Increase transmission power for 3238145_3
- `C22`: Decrease transmission power for 3238145_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.776 | MS1 | 121.4656768487 | 31.1446216903 | 631 | 504990 | -78.91 | 16.59 | 440.71 | 0.11 | 2.65 | 1572 |
| 2024-09-20 22:21:32.758 | MS1 | 121.4656618583 | 31.1446229616 | 631 | 504990 | -77.14 | 12.54 | 527.78 | 0.12 | 2.81 | 1596 |
| 2024-09-20 22:21:33.157 | MS1 | 121.4656583485 | 31.1446363517 | 631 | 504990 | -75.95 | 16.88 | 372.13 | 0.13 | 2.55 | 1593 |
| 2024-09-20 22:21:34.598 | MS1 | 121.4656744223 | 31.1446292791 | 381 | 504990 | -89.57 | 2.19 | 63.91 | 0.13 | 1.22 | 1591 |
| 2024-09-20 22:21:35.428 | MS1 | 121.4656640845 | 31.1446343281 | 381 | 504990 | -81.07 | 1.42 | 37.91 | 0.19 | 1.08 | 1597 |
| 2024-09-20 22:21:36.799 | MS1 | 121.4656730026 | 31.1446192661 | 631 | 504990 | -84.55 | 1.77 | 65.44 | 0.04 | 1.36 | 1587 |
| 2024-09-20 22:21:37.365 | MS1 | 121.4656708901 | 31.1446365665 | 631 | 504990 | -80.36 | 3.38 | 68.58 | 0.08 | 1.20 | 1575 |
| 2024-09-20 22:21:38.389 | MS1 | 121.4656614824 | 31.1446180225 | 381 | 504990 | -85.10 | 2.19 | 64.13 | 0.18 | 1.06 | 1582 |
| 2024-09-20 22:21:39.298 | MS1 | 121.4656605685 | 31.1446316445 | 381 | 504990 | -82.93 | 2.44 | 41.21 | 0.15 | 1.15 | 1592 |
| 2024-09-20 22:21:40.911 | MS1 | 121.4656690067 | 31.1446273751 | 381 | 504990 | -82.10 | 13.12 | 486.10 | 0.08 | 2.97 | 1590 |
| 2024-09-20 22:21:41.693 | MS1 | 121.4656619000 | 31.1446370193 | 381 | 504990 | -75.07 | 16.96 | 550.66 | 0.10 | 2.91 | 1568 |
| 2024-09-20 22:21:42.655 | MS1 | 121.4656611435 | 31.1446263063 | 381 | 504990 | -81.39 | 15.54 | 350.45 | 0.19 | 2.99 | 1564 |

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
| 3236216 | 5 | 121.4697415854 | 31.1519195789 | 353 | 15 | 2 | 39.5 | TDD | 381 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3238145 | 3 | 121.4675579040 | 31.1492452146 | 211 | 1 | 2 | 41.9 | TDD | 598 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3254333 | 2 | 121.4751738793 | 31.1442245915 | 192 | 9 | 3 | 38.1 | TDD | 277 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3268057 | 4 | 121.4688129981 | 31.1508461606 | 172 | 1 | 11 | 41.3 | TDD | 631 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3271252 | 1 | 121.4677380667 | 31.1455770004 | 153 | 13 | 2 | 45.6 | TDD | 715 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.246 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.270 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.406 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.406 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.053 | NREventA3 | measId:2;ServCellPCI:781;Se... |
| 2024-09-20 22:21:34.293 | NRHandoverAttempt | SourcePCI:781;SourceNR-ARFC... |
| 2024-09-20 22:21:34.327 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.342 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.467 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.467 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.053 | NREventA3 | measId:2;ServCellPCI:727;Se... |
| 2024-09-20 22:21:36.293 | NRHandoverAttempt | SourcePCI:727;SourceNR-ARFC... |
| 2024-09-20 22:21:36.323 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.335 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:36.472 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.472 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.053 | NREventA3 | measId:2;ServCellPCI:781;Se... |
| 2024-09-20 22:21:38.293 | NRHandoverAttempt | SourcePCI:781;SourceNR-ARFC... |
| 2024-09-20 22:21:38.335 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.347 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.480 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.480 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271252 | 1 | 7.3048 | 19.6649 | -114.8526 | 11.8704 | 103.6682 | 0.0023 | 0.0130 |
| 2024_09_20 22:00 | 3254333 | 2 | 13.1552 | 9.1700 | -114.0870 | 6.2248 | 82.8133 | 0.0110 | 0.0126 |
| 2024_09_20 22:00 | 3238145 | 3 | 8.2490 | 10.7831 | -114.8049 | 7.7839 | 185.7310 | 0.0041 | 0.0043 |
| 2024_09_20 22:00 | 3268057 | 4 | 18.0901 | 9.4227 | -115.1157 | 18.3952 | 91.8968 | 0.0114 | 0.0198 |
| 2024_09_20 22:00 | 3236216 | 5 | 16.8905 | 6.4146 | -114.5868 | 10.5638 | 90.1801 | 0.0149 | 0.0120 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414282_3BB3E3C2 | 504990 | 631 | -88.3 | 504990 | 381 | -90.5 | 504990 | 598 | -94.5 | 504990 | 277 |
| MR_1774414282_98E02B90 | 504990 | 631 | -88.4 | 504990 | 381 | -89.2 | 504990 | 598 | -91.4 | 504990 | 277 |
| MR_1774414282_1F75BD5D | 504990 | 381 | -90.1 | 504990 | 631 | -88.3 | 504990 | 598 | -91.0 | 504990 | 277 |
| MR_1774414282_085C5FC2 | 504990 | 381 | -90.1 | 504990 | 631 | -88.0 | 504990 | 598 | -93.9 | 504990 | 277 |
| MR_1774414282_4D73911A | 504990 | 631 | -88.3 | 504990 | 381 | -90.3 | 504990 | 598 | -94.1 | 504990 | 277 |
| MR_1774414282_21B2B50A | 504990 | 381 | -88.7 | 504990 | 631 | -91.4 | 504990 | 598 | -92.4 | 504990 | 277 |
| MR_1774414282_BBE6DFC5 | 504990 | 631 | -88.5 | 504990 | 381 | -88.7 | 504990 | 598 | -92.7 | 504990 | 277 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 254: `7c24794f-c14...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7c24794f-c14b-482b-9351-e3491f77bbb4` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[254] topology](images/test_0254.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3227957_1
- `C2`: Increase transmission power for 3228297_4
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Add neighbor relationship between 3227957_1 and 3228297_4
- `C5`: Press down the tilt angle  of 3228297_4 by 6 degrees
- `C6`: Decrease A3 Offset threshold for 3228297_4
- `C7`: Lift the tilt angle of 3227957_1 by 4 degrees
- `C8`: Increase A3 Offset threshold for 3228297_4
- `C9`: Lift the tilt angle  of 3228297_4 by 6 degrees
- `C10`: Adjust the azimuth of 3227957_1 by 26 degrees
- `C11`: Increase A3 Offset threshold for 3227957_1
- `C12`: Decrease transmission power for 3228297_4
- `C13`: Check test server and transmission issues
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228297_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227957_1
- `C16`: Add neighbor relationship between 3278845_3 and 3228297_4
- `C17`: Press down the tilt angle of 3227957_1 by 4 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227957_1
- `C19`: Increase transmission power for 3227957_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228297_4
- `C21`: Adjust the azimuth of 3228297_4 by 20 degrees
- `C22`: Decrease transmission power for 3227957_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.341 | MS1 | 121.4656607756 | 31.1446217034 | 37 | 504990 | -77.37 | 16.29 | 501.28 | 0.12 | 2.37 | 1592 |
| 2024-09-20 22:21:32.459 | MS1 | 121.4656591547 | 31.1446182072 | 37 | 504990 | -75.22 | 16.23 | 435.26 | 0.01 | 2.39 | 1587 |
| 2024-09-20 22:21:33.349 | MS1 | 121.4656653751 | 31.1446237569 | 37 | 504990 | -75.94 | 14.78 | 563.63 | 0.01 | 2.42 | 1584 |
| 2024-09-20 22:21:34.100 | MS1 | 121.4656710208 | 31.1446185097 | 37 | 504990 | -86.99 | 0.29 | 47.45 | 0.06 | 1.09 | 1565 |
| 2024-09-20 22:21:35.649 | MS1 | 121.4656753534 | 31.1446227146 | 37 | 504990 | -88.75 | 2.66 | 61.13 | 0.01 | 1.47 | 1588 |
| 2024-09-20 22:21:36.562 | MS1 | 121.4656701210 | 31.1446342786 | 37 | 504990 | -85.94 | 1.83 | 40.27 | 0.12 | 1.00 | 1578 |
| 2024-09-20 22:21:37.248 | MS1 | 121.4656625252 | 31.1446376995 | 37 | 504990 | -91.36 | 3.53 | 72.12 | 0.11 | 1.45 | 1591 |
| 2024-09-20 22:21:38.314 | MS1 | 121.4656608174 | 31.1446255141 | 37 | 504990 | -85.94 | 3.93 | 56.15 | 0.08 | 1.17 | 1586 |
| 2024-09-20 22:21:39.503 | MS1 | 121.4656738791 | 31.1446348273 | 37 | 504990 | -93.44 | 0.76 | 64.07 | 0.03 | 1.11 | 1596 |
| 2024-09-20 22:21:40.920 | MS1 | 121.4656660015 | 31.1446259162 | 37 | 504990 | -78.43 | 16.53 | 433.79 | 0.07 | 2.63 | 1574 |
| 2024-09-20 22:21:41.961 | MS1 | 121.4656679035 | 31.1446354988 | 37 | 504990 | -75.39 | 13.85 | 348.10 | 0.08 | 2.97 | 1586 |
| 2024-09-20 22:21:42.303 | MS1 | 121.4656627718 | 31.1446354899 | 37 | 504990 | -78.17 | 16.96 | 501.17 | 0.19 | 2.93 | 1586 |

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
| 3227957 | 1 | 121.4759996176 | 31.1514971460 | 206 | 3 | 8 | 22.3 | TDD | 37 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3228297 | 4 | 121.4703489041 | 31.1482566057 | 208 | 4 | 0 | 16.4 | TDD | 958 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3274495 | 2 | 121.4703597195 | 31.1522600410 | 104 | 7 | 12 | 22.0 | TDD | 132 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3278845 | 3 | 121.4695416417 | 31.1463296314 | 288 | 9 | 1 | 39.4 | TDD | 276 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.959 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.979 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.117 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.117 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227957 | 1 | 10.9979 | 10.5242 | -109.0802 | 16.9651 | 151.6305 | 0.0127 | 0.0031 |
| 2024_09_20 22:00 | 3274495 | 2 | 6.4764 | 6.8449 | -117.5658 | 10.4950 | 184.4594 | 0.0161 | 0.0007 |
| 2024_09_20 22:00 | 3278845 | 3 | 9.7458 | 10.0999 | -114.8532 | 12.0845 | 171.1089 | 0.0150 | 0.0171 |
| 2024_09_20 22:00 | 3228297 | 4 | 10.1533 | 6.7488 | -117.6175 | 19.2804 | 178.3324 | 0.0138 | 0.0102 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414058_8C6DFE5D | 504990 | 958 | -87.6 | 504990 | 37 | -86.1 | 504990 | 276 | -89.5 | 504990 | 132 |
| MR_1774414058_572A761C | 504990 | 958 | -85.2 | 504990 | 37 | -85.4 | 504990 | 276 | -87.1 | 504990 | 132 |
| MR_1774414058_D6E3D554 | 504990 | 37 | -88.0 | 504990 | 958 | -84.2 | 504990 | 276 | -87.8 | 504990 | 132 |
| MR_1774414058_7454AE67 | 504990 | 958 | -86.9 | 504990 | 37 | -84.8 | 504990 | 276 | -88.1 | 504990 | 132 |
| MR_1774414058_3752501D | 504990 | 37 | -87.7 | 504990 | 958 | -86.3 | 504990 | 276 | -88.6 | 504990 | 132 |
| MR_1774414058_C9C42270 | 504990 | 37 | -88.1 | 504990 | 958 | -84.3 | 504990 | 276 | -88.2 | 504990 | 132 |
| MR_1774414058_3BB164CD | 504990 | 37 | -88.5 | 504990 | 958 | -83.5 | 504990 | 276 | -89.3 | 504990 | 132 |
| MR_1774414058_079B0BC4 | 504990 | 958 | -86.8 | 504990 | 37 | -86.3 | 504990 | 276 | -89.2 | 504990 | 132 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 255: `7e07891d-13e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7e07891d-13e5-4ff9-8468-4c927d98c6ba` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[255] topology](images/test_0255.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3250864_3
- `C2`: Adjust the azimuth of 3255991_2 by 50 degrees
- `C3`: Check test server and transmission issues
- `C4`: Add neighbor relationship between 3235775_4 and 3250864_3
- `C5`: Decrease A3 Offset threshold for 3255991_2
- `C6`: Increase transmission power for 3250864_3
- `C7`: Lift the tilt angle of 3255991_2 by 10 degrees
- `C8`: Adjust the azimuth of 3250864_3 by 50 degrees
- `C9`: Press down the tilt angle of 3255991_2 by 10 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250864_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250864_3
- `C12`: Add neighbor relationship between 3255991_2 and 3250864_3
- `C13`: Increase A3 Offset threshold for 3250864_3
- `C14`: Increase A3 Offset threshold for 3255991_2
- `C15`: Decrease transmission power for 3255991_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255991_2
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Lift the tilt angle  of 3250864_3 by 10 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255991_2
- `C20`: Press down the tilt angle  of 3250864_3 by 10 degrees
- `C21`: Decrease transmission power for 3250864_3
- `C22`: Increase transmission power for 3255991_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.396 | MS1 | 121.4656709521 | 31.1446192549 | 562 | 504990 | -86.94 | 17.30 | 508.29 | 0.09 | 2.50 | 1576 |
| 2024-09-20 22:21:32.316 | MS1 | 121.4656619064 | 31.1446324227 | 562 | 504990 | -91.72 | 17.96 | 306.44 | 0.11 | 2.54 | 1591 |
| 2024-09-20 22:21:33.650 | MS1 | 121.4656679043 | 31.1446370689 | 562 | 504990 | -88.62 | 17.97 | 367.81 | 0.13 | 2.26 | 1580 |
| 2024-09-20 22:21:34.543 | MS1 | 121.4656767519 | 31.1446201431 | 562 | 504990 | -91.72 | 14.50 | 77.91 | 0.11 | 2.43 | 1573 |
| 2024-09-20 22:21:35.478 | MS1 | 121.4656705784 | 31.1446218008 | 562 | 504990 | -90.23 | 13.94 | 60.00 | 0.07 | 2.48 | 1592 |
| 2024-09-20 22:21:36.756 | MS1 | 121.4656609472 | 31.1446314602 | 562 | 504990 | -85.29 | 14.54 | 51.08 | 0.08 | 2.32 | 1588 |
| 2024-09-20 22:21:37.154 | MS1 | 121.4656641903 | 31.1446249313 | 562 | 504990 | -92.04 | 9.42 | 91.61 | 0.06 | 2.94 | 1596 |
| 2024-09-20 22:21:38.676 | MS1 | 121.4656764108 | 31.1446265760 | 562 | 504990 | -90.84 | 11.82 | 82.75 | 0.00 | 2.30 | 1579 |
| 2024-09-20 22:21:39.784 | MS1 | 121.4656617014 | 31.1446325678 | 562 | 504990 | -89.96 | 7.80 | 102.15 | 0.07 | 2.26 | 1599 |
| 2024-09-20 22:21:40.168 | MS1 | 121.4656605999 | 31.1446341883 | 562 | 504990 | -91.22 | 7.98 | 400.72 | 0.06 | 2.22 | 1576 |
| 2024-09-20 22:21:41.538 | MS1 | 121.4656665343 | 31.1446305288 | 562 | 504990 | -89.75 | 11.83 | 371.42 | 0.17 | 2.32 | 1579 |
| 2024-09-20 22:21:42.590 | MS1 | 121.4656700794 | 31.1446291848 | 562 | 504990 | -91.48 | 12.16 | 517.02 | 0.19 | 2.04 | 1591 |

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
| 3220719 | 1 | 121.4735720245 | 31.1499054663 | 126 | 5 | 3 | 36.6 | TDD | 969 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3235775 | 4 | 121.4727985536 | 31.1441892958 | 60 | 2 | 3 | 15.1 | TDD | 518 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3250864 | 3 | 121.4751450563 | 31.1548454892 | 354 | 11 | 9 | 47.3 | TDD | 140 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3255991 | 2 | 121.4754650343 | 31.1538606519 | 54 | 14 | 2 | 21.6 | TDD | 562 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.355 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.379 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.479 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.479 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.239 | NREventA3 | measId:2;ServCellPCI:254;Se... |
| 2024-09-20 22:21:38.479 | NRHandoverAttempt | SourcePCI:254;SourceNR-ARFC... |
| 2024-09-20 22:21:38.510 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.522 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.624 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.624 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3220719 | 1 | 76.4640 | 83.8102 | -117.5613 | 15.3652 | 173.1026 | 0.0193 | 0.0192 |
| 2024_09_19 22:00 | 3255991 | 2 | 84.5009 | 76.9089 | -115.1785 | 16.2954 | 87.5759 | 0.0130 | 0.0077 |
| 2024_09_19 22:00 | 3250864 | 3 | 93.9314 | 88.1463 | -115.2558 | 8.3818 | 158.2649 | 0.0195 | 0.0041 |
| 2024_09_19 22:00 | 3235775 | 4 | 90.6906 | 80.9700 | -117.4023 | 9.1842 | 86.0760 | 0.0135 | 0.0183 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415697_4C6CD8E5 | 504990 | 562 | -90.6 | 504990 | 140 | -95.8 | 504990 | 518 | -97.5 | 504990 | 969 |
| MR_1774415697_B790500D | 504990 | 562 | -90.2 | 504990 | 140 | -97.9 | 504990 | 518 | -100.8 | 504990 | 969 |
| MR_1774415697_A1CCAF41 | 504990 | 562 | -90.0 | 504990 | 140 | -95.9 | 504990 | 518 | -100.1 | 504990 | 969 |
| MR_1774415697_0A60A301 | 504990 | 562 | -92.0 | 504990 | 140 | -97.5 | 504990 | 518 | -99.0 | 504990 | 969 |
| MR_1774415697_31B672B2 | 504990 | 562 | -93.5 | 504990 | 140 | -96.3 | 504990 | 518 | -99.7 | 504990 | 969 |
| MR_1774415697_5B8A40B3 | 504990 | 562 | -89.9 | 504990 | 140 | -99.1 | 504990 | 518 | -99.5 | 504990 | 969 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 256: `5d9078b0-e1b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5d9078b0-e1b7-4a2e-9db3-6e3394fa252e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[256] topology](images/test_0256.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease A3 Offset threshold for 3232825_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Add neighbor relationship between 3273757_2 and 3216735_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216735_3
- `C6`: Decrease transmission power for 3216735_3
- `C7`: Adjust the azimuth of 3216735_3 by 15 degrees
- `C8`: Press down the tilt angle  of 3216735_3 by 2 degrees
- `C9`: Press down the tilt angle of 3232825_1 by 5 degrees
- `C10`: Increase transmission power for 3232825_1
- `C11`: Lift the tilt angle of 3232825_1 by 5 degrees
- `C12`: Lift the tilt angle  of 3216735_3 by 2 degrees
- `C13`: Increase A3 Offset threshold for 3216735_3
- `C14`: Add neighbor relationship between 3232825_1 and 3216735_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216735_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232825_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232825_1
- `C18`: Increase A3 Offset threshold for 3232825_1
- `C19`: Decrease A3 Offset threshold for 3216735_3
- `C20`: Increase transmission power for 3216735_3
- `C21`: Decrease transmission power for 3232825_1
- `C22`: Adjust the azimuth of 3232825_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.842 | MS1 | 121.4656590600 | 31.1446283861 | 800 | 504990 | -90.68 | 16.97 | 459.98 | 0.18 | 2.07 | 1577 |
| 2024-09-20 22:21:32.542 | MS1 | 121.4656591670 | 31.1446299566 | 800 | 504990 | -85.22 | 15.99 | 419.19 | 0.15 | 2.44 | 1564 |
| 2024-09-20 22:21:33.949 | MS1 | 121.4656647899 | 31.1446350444 | 800 | 504990 | -90.36 | 13.13 | 594.96 | 0.04 | 2.82 | 1572 |
| 2024-09-20 22:21:34.292 | MS1 | 121.4656715814 | 31.1446208351 | 800 | 504990 | -91.45 | 14.69 | 103.63 | 0.15 | 2.57 | 1573 |
| 2024-09-20 22:21:35.589 | MS1 | 121.4656657073 | 31.1446250090 | 800 | 504990 | -91.57 | 16.45 | 81.49 | 0.01 | 2.59 | 1574 |
| 2024-09-20 22:21:36.171 | MS1 | 121.4656614048 | 31.1446219789 | 800 | 504990 | -91.57 | 16.92 | 90.41 | 0.08 | 2.72 | 1570 |
| 2024-09-20 22:21:37.763 | MS1 | 121.4656749640 | 31.1446256394 | 800 | 504990 | -89.74 | 7.11 | 99.69 | 0.09 | 2.57 | 1589 |
| 2024-09-20 22:21:38.533 | MS1 | 121.4656699759 | 31.1446284454 | 800 | 504990 | -91.51 | 12.04 | 66.31 | 0.06 | 2.38 | 1593 |
| 2024-09-20 22:21:39.303 | MS1 | 121.4656710068 | 31.1446189054 | 800 | 504990 | -89.76 | 9.05 | 95.76 | 0.20 | 2.31 | 1569 |
| 2024-09-20 22:21:40.622 | MS1 | 121.4656602914 | 31.1446275051 | 800 | 504990 | -91.70 | 7.83 | 501.01 | 0.00 | 2.81 | 1588 |
| 2024-09-20 22:21:41.555 | MS1 | 121.4656593481 | 31.1446261228 | 800 | 504990 | -93.12 | 12.22 | 301.23 | 0.13 | 2.56 | 1592 |
| 2024-09-20 22:21:42.773 | MS1 | 121.4656761819 | 31.1446346104 | 800 | 504990 | -91.40 | 12.61 | 517.71 | 0.14 | 2.46 | 1591 |

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
| 3216735 | 3 | 121.4724607508 | 31.1489795425 | 218 | 0 | 1 | 24.4 | TDD | 101 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3232825 | 1 | 121.4718395326 | 31.1455082257 | 192 | 1 | 12 | 38.7 | TDD | 800 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3241038 | 4 | 121.4695240267 | 31.1494019522 | 203 | 5 | 1 | 16.0 | TDD | 693 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3273757 | 2 | 121.4728867593 | 31.1524610020 | 209 | 7 | 3 | 43.0 | TDD | 633 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.818 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.834 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:30.971 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.971 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.683 | NREventA3 | measId:2;ServCellPCI:929;Se... |
| 2024-09-20 22:21:37.923 | NRHandoverAttempt | SourcePCI:929;SourceNR-ARFC... |
| 2024-09-20 22:21:37.959 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.970 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.072 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.072 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3232825 | 1 | 89.2326 | 89.4283 | -117.2703 | 17.7573 | 146.4603 | 0.0030 | 0.0152 |
| 2024_09_19 22:00 | 3273757 | 2 | 83.1539 | 85.3974 | -117.5881 | 13.5975 | 170.1923 | 0.0110 | 0.0121 |
| 2024_09_19 22:00 | 3216735 | 3 | 87.7003 | 91.7684 | -117.8975 | 14.4260 | 165.6605 | 0.0165 | 0.0140 |
| 2024_09_19 22:00 | 3241038 | 4 | 76.3206 | 89.5585 | -117.6498 | 7.4056 | 171.2631 | 0.0173 | 0.0161 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412039_6CD700D4 | 504990 | 800 | -89.7 | 504990 | 101 | -98.7 | 504990 | 633 | -99.1 | 504990 | 693 |
| MR_1774412039_BEE75FE0 | 504990 | 800 | -91.1 | 504990 | 101 | -98.7 | 504990 | 633 | -102.0 | 504990 | 693 |
| MR_1774412039_06784440 | 504990 | 800 | -90.3 | 504990 | 101 | -98.4 | 504990 | 633 | -99.6 | 504990 | 693 |
| MR_1774412039_8BEFF932 | 504990 | 800 | -90.8 | 504990 | 101 | -96.9 | 504990 | 633 | -102.0 | 504990 | 693 |
| MR_1774412039_1C57BE3C | 504990 | 800 | -89.8 | 504990 | 101 | -100.1 | 504990 | 633 | -103.0 | 504990 | 693 |
| MR_1774412039_35A4F4D4 | 504990 | 800 | -89.6 | 504990 | 101 | -99.0 | 504990 | 633 | -101.9 | 504990 | 693 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 257: `ed30b351-98d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ed30b351-98d0-4b98-ab39-d3ee74acd2e1` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[257] topology](images/test_0257.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3222570_1 by 50 degrees
- `C2`: Decrease A3 Offset threshold for 3222570_1
- `C3`: Increase transmission power for 3229357_2
- `C4`: Increase A3 Offset threshold for 3222570_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229357_2
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease A3 Offset threshold for 3229357_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229357_2
- `C9`: Check test server and transmission issues
- `C10`: Decrease transmission power for 3222570_1
- `C11`: Increase transmission power for 3222570_1
- `C12`: Press down the tilt angle  of 3229357_2 by 6 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222570_1
- `C14`: Increase A3 Offset threshold for 3229357_2
- `C15`: Adjust the azimuth of 3229357_2 by 22 degrees
- `C16`: Lift the tilt angle  of 3229357_2 by 6 degrees
- `C17`: Add neighbor relationship between 3217303_4 and 3229357_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222570_1
- `C19`: Add neighbor relationship between 3222570_1 and 3229357_2
- `C20`: Press down the tilt angle of 3222570_1 by 10 degrees
- `C21`: Decrease transmission power for 3229357_2
- `C22`: Lift the tilt angle of 3222570_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.826 | MS1 | 121.4656689754 | 31.1446280909 | 232 | 504990 | -82.85 | 13.73 | 567.97 | 0.02 | 2.49 | 1591 |
| 2024-09-20 22:21:32.912 | MS1 | 121.4656703980 | 31.1446292319 | 232 | 504990 | -83.10 | 15.20 | 477.47 | 0.05 | 2.18 | 1583 |
| 2024-09-20 22:21:33.658 | MS1 | 121.4656741892 | 31.1446254367 | 232 | 504990 | -83.93 | 15.91 | 385.08 | 0.13 | 2.13 | 1562 |
| 2024-09-20 22:21:34.841 | MS1 | 121.4656769439 | 31.1446298915 | 232 | 504990 | -85.69 | -2.37 | 72.71 | 0.03 | 1.21 | 1563 |
| 2024-09-20 22:21:35.466 | MS1 | 121.4656777688 | 31.1446332854 | 232 | 504990 | -87.24 | -3.75 | 48.67 | 0.09 | 1.09 | 1596 |
| 2024-09-20 22:21:36.766 | MS1 | 121.4656618707 | 31.1446308137 | 232 | 504990 | -86.29 | -0.08 | 42.31 | 0.09 | 1.23 | 1572 |
| 2024-09-20 22:21:37.129 | MS1 | 121.4656634751 | 31.1446267693 | 232 | 504990 | -93.15 | -3.76 | 38.35 | 0.20 | 1.10 | 1595 |
| 2024-09-20 22:21:38.790 | MS1 | 121.4656715170 | 31.1446286089 | 232 | 504990 | -80.71 | 17.40 | 387.24 | 0.06 | 1.44 | 1579 |
| 2024-09-20 22:21:39.227 | MS1 | 121.4656738275 | 31.1446217482 | 232 | 504990 | -75.37 | 16.90 | 310.23 | 0.14 | 1.08 | 1567 |
| 2024-09-20 22:21:40.828 | MS1 | 121.4656598149 | 31.1446271447 | 232 | 504990 | -77.20 | 17.64 | 551.27 | 0.07 | 2.33 | 1561 |
| 2024-09-20 22:21:41.178 | MS1 | 121.4656640032 | 31.1446345573 | 232 | 504990 | -75.12 | 17.30 | 586.44 | 0.01 | 2.94 | 1599 |
| 2024-09-20 22:21:42.609 | MS1 | 121.4656682328 | 31.1446287012 | 232 | 504990 | -82.09 | 14.77 | 342.35 | 0.00 | 2.89 | 1564 |

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
| 3217303 | 4 | 121.4652513891 | 31.1523018924 | 109 | 12 | 12 | 29.4 | TDD | 301 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3222570 | 1 | 121.4705668445 | 31.1500139469 | 326 | 15 | 9 | 19.6 | TDD | 232 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3229357 | 2 | 121.4750591807 | 31.1557807523 | 194 | 5 | 3 | 19.1 | TDD | 365 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3273363 | 3 | 121.4701041990 | 31.1483350989 | 267 | 2 | 2 | 48.7 | TDD | 11 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.242 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.261 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.396 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.396 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.062 | NREventA3 | measId:2;ServCellPCI:720;Se... |
| 2024-09-20 22:21:36.062 | NREventA3 | measId:2;ServCellPCI:720;Se... |
| 2024-09-20 22:21:37.062 | NREventA3 | measId:2;ServCellPCI:720;Se... |
| 2024-09-20 22:21:39.562 | NRRRCReestablishAttempt | PCI:720 |
| 2024-09-20 22:21:39.579 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.593 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.728 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.728 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222570 | 1 | 13.2881 | 14.9869 | -117.9547 | 15.3489 | 169.4465 | 0.0107 | 0.1750 |
| 2024_09_20 22:00 | 3229357 | 2 | 15.7758 | 12.6827 | -117.4774 | 13.9791 | 125.1696 | 0.0075 | 0.0193 |
| 2024_09_20 22:00 | 3273363 | 3 | 14.6003 | 12.9813 | -115.7225 | 8.4472 | 179.0324 | 0.0007 | 0.0101 |
| 2024_09_20 22:00 | 3217303 | 4 | 12.2301 | 9.0205 | -115.3145 | 17.0982 | 188.4642 | 0.0106 | 0.0044 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416763_808B06F0 | 504990 | 365 | -78.5 | 504990 | 232 | -86.4 | 504990 | 301 | -87.4 | 504990 | 11 |
| MR_1774416763_D03F612C | 504990 | 365 | -79.7 | 504990 | 232 | -85.6 | 504990 | 301 | -89.4 | 504990 | 11 |
| MR_1774416763_CC6FA6BE | 504990 | 232 | -86.1 | 504990 | 365 | -81.0 | 504990 | 301 | -89.4 | 504990 | 11 |
| MR_1774416763_6A93F8D2 | 504990 | 232 | -85.7 | 504990 | 365 | -80.3 | 504990 | 301 | -87.2 | 504990 | 11 |
| MR_1774416763_0FFCCF96 | 504990 | 232 | -86.4 | 504990 | 365 | -81.7 | 504990 | 301 | -88.7 | 504990 | 11 |
| MR_1774416763_4D7EF13C | 504990 | 365 | -81.3 | 504990 | 232 | -83.9 | 504990 | 301 | -89.6 | 504990 | 11 |
| MR_1774416763_1DE055CB | 504990 | 365 | -80.1 | 504990 | 232 | -84.2 | 504990 | 301 | -86.5 | 504990 | 11 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 258: `f5d30f47-7a8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f5d30f47-7a81-433d-97d2-6207ee3d9c00` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[258] topology](images/test_0258.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239368_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267732_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239368_3
- `C4`: Add neighbor relationship between 3270835_4 and 3239368_3
- `C5`: Adjust the azimuth of 3267732_2 by 47 degrees
- `C6`: Decrease A3 Offset threshold for 3239368_3
- `C7`: Check test server and transmission issues
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267732_2
- `C9`: Lift the tilt angle  of 3239368_3 by 10 degrees
- `C10`: Increase A3 Offset threshold for 3239368_3
- `C11`: Decrease A3 Offset threshold for 3267732_2
- `C12`: Increase transmission power for 3239368_3
- `C13`: Adjust the azimuth of 3239368_3 by 50 degrees
- `C14`: Lift the tilt angle of 3267732_2 by 10 degrees
- `C15`: Press down the tilt angle of 3267732_2 by 10 degrees
- `C16`: Decrease transmission power for 3239368_3
- `C17`: Increase A3 Offset threshold for 3267732_2
- `C18`: Decrease transmission power for 3267732_2
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Press down the tilt angle  of 3239368_3 by 10 degrees
- `C21`: Increase transmission power for 3267732_2
- `C22`: Add neighbor relationship between 3267732_2 and 3239368_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.603 | MS1 | 121.4656584964 | 31.1446195695 | 247 | 504990 | -89.10 | 15.09 | 480.62 | 0.02 | 2.76 | 1588 |
| 2024-09-20 22:21:32.835 | MS1 | 121.4656632597 | 31.1446307961 | 247 | 504990 | -85.65 | 13.31 | 321.84 | 0.06 | 2.67 | 1567 |
| 2024-09-20 22:21:33.620 | MS1 | 121.4656703317 | 31.1446352551 | 247 | 504990 | -86.26 | 17.10 | 527.34 | 0.09 | 2.46 | 1560 |
| 2024-09-20 22:21:34.935 | MS1 | 121.4656624766 | 31.1446327813 | 247 | 504990 | -88.50 | 17.85 | 61.81 | 0.14 | 2.03 | 1561 |
| 2024-09-20 22:21:35.420 | MS1 | 121.4656755727 | 31.1446217106 | 247 | 504990 | -89.69 | 14.47 | 80.55 | 0.16 | 2.62 | 1589 |
| 2024-09-20 22:21:36.258 | MS1 | 121.4656601770 | 31.1446313593 | 247 | 504990 | -88.68 | 16.69 | 68.92 | 0.14 | 2.50 | 1594 |
| 2024-09-20 22:21:37.534 | MS1 | 121.4656723966 | 31.1446370284 | 247 | 504990 | -89.54 | 9.92 | 78.71 | 0.14 | 2.94 | 1575 |
| 2024-09-20 22:21:38.244 | MS1 | 121.4656613767 | 31.1446248656 | 247 | 504990 | -93.28 | 9.29 | 94.25 | 0.12 | 2.54 | 1565 |
| 2024-09-20 22:21:39.125 | MS1 | 121.4656591730 | 31.1446279214 | 247 | 504990 | -92.28 | 12.45 | 85.07 | 0.20 | 2.84 | 1573 |
| 2024-09-20 22:21:40.930 | MS1 | 121.4656717841 | 31.1446255693 | 247 | 504990 | -90.01 | 10.99 | 544.24 | 0.15 | 2.85 | 1593 |
| 2024-09-20 22:21:41.944 | MS1 | 121.4656583467 | 31.1446293356 | 247 | 504990 | -89.28 | 8.70 | 475.53 | 0.10 | 2.70 | 1569 |
| 2024-09-20 22:21:42.319 | MS1 | 121.4656726005 | 31.1446368126 | 247 | 504990 | -90.01 | 12.60 | 527.99 | 0.16 | 2.45 | 1570 |

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
| 3239368 | 3 | 121.4696110233 | 31.1558887498 | 322 | 8 | 4 | 37.6 | TDD | 710 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3251551 | 1 | 121.4640017976 | 31.1540245914 | 346 | 9 | 1 | 29.9 | TDD | 490 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3267732 | 2 | 121.4744479891 | 31.1512469235 | 182 | 15 | 4 | 18.7 | TDD | 247 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3270835 | 4 | 121.4734475217 | 31.1529498751 | 331 | 0 | 12 | 34.8 | TDD | 319 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.367 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.386 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.499 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.499 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.255 | NREventA3 | measId:2;ServCellPCI:969;Se... |
| 2024-09-20 22:21:38.495 | NRHandoverAttempt | SourcePCI:969;SourceNR-ARFC... |
| 2024-09-20 22:21:38.531 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.546 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.673 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.673 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3251551 | 1 | 77.7359 | 92.1039 | -114.8930 | 6.7400 | 114.3058 | 0.0121 | 0.0048 |
| 2024_09_19 22:00 | 3267732 | 2 | 89.5002 | 83.2897 | -114.9225 | 5.7066 | 199.1681 | 0.0112 | 0.0117 |
| 2024_09_19 22:00 | 3239368 | 3 | 80.2618 | 76.6766 | -117.5006 | 10.8703 | 109.5371 | 0.0076 | 0.0083 |
| 2024_09_19 22:00 | 3270835 | 4 | 78.8104 | 81.1147 | -116.3205 | 13.9161 | 197.0646 | 0.0177 | 0.0035 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414695_B573525A | 504990 | 247 | -88.9 | 504990 | 710 | -87.4 | 504990 | 319 | -100.7 | 504990 | 490 |
| MR_1774414695_7CFEBAD6 | 504990 | 247 | -89.2 | 504990 | 710 | -86.5 | 504990 | 319 | -99.7 | 504990 | 490 |
| MR_1774414695_698F55BF | 504990 | 247 | -90.1 | 504990 | 710 | -89.5 | 504990 | 319 | -97.7 | 504990 | 490 |
| MR_1774414695_B2BB46D2 | 504990 | 247 | -87.6 | 504990 | 710 | -87.0 | 504990 | 319 | -98.0 | 504990 | 490 |
| MR_1774414695_0C4D3612 | 504990 | 247 | -90.1 | 504990 | 710 | -87.3 | 504990 | 319 | -98.1 | 504990 | 490 |
| MR_1774414695_43E4CB24 | 504990 | 247 | -87.5 | 504990 | 710 | -87.5 | 504990 | 319 | -97.7 | 504990 | 490 |
| MR_1774414695_2381E13F | 504990 | 247 | -90.5 | 504990 | 710 | -87.0 | 504990 | 319 | -97.8 | 504990 | 490 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 259: `8a3f83cc-e68...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8a3f83cc-e689-4fef-b41c-8d453e51a191` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[259] topology](images/test_0259.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230670_3
- `C2`: Add neighbor relationship between 3257141_1 and 3230670_3
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease A3 Offset threshold for 3230670_3
- `C5`: Check test server and transmission issues
- `C6`: Decrease transmission power for 3257141_1
- `C7`: Adjust the azimuth of 3257141_1 by 49 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257141_1
- `C9`: Lift the tilt angle  of 3230670_3 by 3 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230670_3
- `C11`: Adjust the azimuth of 3230670_3 by 28 degrees
- `C12`: Increase A3 Offset threshold for 3257141_1
- `C13`: Decrease A3 Offset threshold for 3257141_1
- `C14`: Press down the tilt angle of 3257141_1 by 3 degrees
- `C15`: Lift the tilt angle of 3257141_1 by 3 degrees
- `C16`: Press down the tilt angle  of 3230670_3 by 3 degrees
- `C17`: Add neighbor relationship between 3227280_9 and 3230670_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257141_1
- `C19`: Increase transmission power for 3257141_1
- `C20`: Increase transmission power for 3230670_3
- `C21`: Decrease transmission power for 3230670_3
- `C22`: Increase A3 Offset threshold for 3230670_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.546 | MS1 | 121.4656716651 | 31.1446254937 | 451 | 504990 | -93.56 | 11.45 | 409.49 | 0.11 | 2.99 | 1560 |
| 2024-09-20 22:21:32.464 | MS1 | 121.4656669210 | 31.1446193753 | 473 | 504990 | -94.15 | 13.37 | 402.09 | 0.07 | 2.54 | 1595 |
| 2024-09-20 22:21:33.415 | MS1 | 121.4656593236 | 31.1446355225 | 400 | 504990 | -93.97 | 12.10 | 435.75 | 0.17 | 2.23 | 1573 |
| 2024-09-20 22:21:34.469 | MS1 | 121.4656773642 | 31.1446192216 | 1005 | 152650 | -89.81 | 6.93 | 47.57 | 0.03 | 1.67 | 927 |
| 2024-09-20 22:21:35.131 | MS1 | 121.4656582040 | 31.1446376137 | 484 | 152650 | -93.14 | 6.84 | 51.08 | 0.15 | 1.51 | 982 |
| 2024-09-20 22:21:36.257 | MS1 | 121.4656761720 | 31.1446214617 | 453 | 152650 | -87.69 | 5.25 | 95.82 | 0.15 | 1.54 | 955 |
| 2024-09-20 22:21:37.790 | MS1 | 121.4656634058 | 31.1446282869 | 163 | 152650 | -88.77 | 6.36 | 79.05 | 0.02 | 1.56 | 983 |
| 2024-09-20 22:21:38.423 | MS1 | 121.4656637205 | 31.1446307822 | 1005 | 152650 | -95.11 | 4.45 | 53.86 | 0.13 | 1.82 | 951 |
| 2024-09-20 22:21:39.426 | MS1 | 121.4656719913 | 31.1446300932 | 484 | 152650 | -89.84 | 7.06 | 53.12 | 0.18 | 1.61 | 999 |
| 2024-09-20 22:21:40.314 | MS1 | 121.4656607053 | 31.1446248485 | 453 | 152650 | -90.14 | 3.70 | 55.81 | 0.16 | 2.04 | 1575 |
| 2024-09-20 22:21:41.156 | MS1 | 121.4656732294 | 31.1446243184 | 163 | 152650 | -95.79 | 4.49 | 76.28 | 0.18 | 2.97 | 1564 |
| 2024-09-20 22:21:42.519 | MS1 | 121.4656734902 | 31.1446235245 | 1005 | 152650 | -95.34 | 7.42 | 54.47 | 0.09 | 2.26 | 1587 |

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
| 3223713 | 6 | 121.4736319645 | 31.1546825791 | 121 | 10 | 11 | 3.4 | TDD | 473 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3225740 | 5 | 121.4655440354 | 31.1505205477 | 253 | 6 | 8 | 26.8 | TDD | 51 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3227280 | 9 | 121.4682011350 | 31.1513487733 | 163 | 0 | 10 | 21.2 | FDD | 453 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3230670 | 3 | 121.4686902493 | 31.1505027902 | 176 | 2 | 10 | 14.8 | TDD | 846 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3233027 | 13 | 121.4690431387 | 31.1527813736 | 184 | 5 | 2 | 1.4 | FDD | 1005 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3241806 | 11 | 121.4700311900 | 31.1542484043 | 13 | 8 | 9 | 17.2 | FDD | 394 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3243022 | 2 | 121.4732552421 | 31.1450662923 | 204 | 9 | 9 | 25.5 | TDD | 313 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3244843 | 8 | 121.4730308259 | 31.1472038227 | 251 | 11 | 0 | 20.9 | FDD | 484 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3252009 | 10 | 121.4710705041 | 31.1467089938 | 138 | 1 | 4 | 20.0 | FDD | 707 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3257141 | 1 | 121.4661774119 | 31.1512423909 | 233 | 1 | 11 | 21.4 | TDD | 451 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3259354 | 7 | 121.4650142239 | 31.1527166602 | 134 | 5 | 4 | 14.7 | FDD | 163 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3262524 | 4 | 121.4735379581 | 31.1456132125 | 188 | 1 | 11 | 1.9 | TDD | 400 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3272719 | 12 | 121.4732030395 | 31.1555009299 | 261 | 7 | 2 | 23.7 | FDD | 268 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |

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
| 2024-09-20 22:21:31.317 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.336 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.463 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.463 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.129 | NREventA2 | measId:1;ServCellPCI:780;Se... |
| 2024-09-20 22:21:35.259 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.459 | NREventA5 | measId:3;ServCellPCI:780;Se... |
| 2024-09-20 22:21:35.534 | NRHandoverAttempt | SourcePCI:780;SourceNR-ARFC... |
| 2024-09-20 22:21:35.559 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.574 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.678 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.678 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257141 | 1 | 16.1493 | 16.7930 | -117.1104 | 7.2557 | 104.6180 | 0.0077 | 0.0172 |
| 2024_09_20 22:00 | 3243022 | 2 | 17.1395 | 16.2297 | -117.7058 | 19.1312 | 184.4903 | 0.0105 | 0.0092 |
| 2024_09_20 22:00 | 3230670 | 3 | 6.3612 | 13.4468 | -115.6331 | 18.2235 | 110.5537 | 0.0088 | 0.0057 |
| 2024_09_20 22:00 | 3262524 | 4 | 16.8821 | 10.2524 | -117.2470 | 19.1505 | 112.8790 | 0.0045 | 0.0155 |
| 2024_09_20 22:00 | 3225740 | 5 | 18.9064 | 9.9081 | -117.6776 | 10.0060 | 121.3509 | 0.0040 | 0.0148 |
| 2024_09_20 22:00 | 3223713 | 6 | 7.2293 | 12.1990 | -114.4258 | 5.4443 | 101.8887 | 0.0141 | 0.0119 |
| 2024_09_20 22:00 | 3259354 | 7 | 14.6369 | 19.7199 | -117.4596 | 4.5126 | 40.3395 | 0.0147 | 0.0088 |
| 2024_09_20 22:00 | 3244843 | 8 | 9.7401 | 9.2186 | -117.1454 | 4.1400 | 55.7787 | 0.0076 | 0.0059 |
| 2024_09_20 22:00 | 3227280 | 9 | 15.2531 | 15.2418 | -114.5668 | 3.7892 | 50.0004 | 0.0098 | 0.0079 |
| 2024_09_20 22:00 | 3252009 | 10 | 6.4038 | 5.8444 | -115.4397 | 4.3836 | 37.2115 | 0.0135 | 0.0138 |
| 2024_09_20 22:00 | 3241806 | 11 | 19.1320 | 12.6237 | -117.8311 | 4.0729 | 39.6378 | 0.0175 | 0.0044 |
| 2024_09_20 22:00 | 3272719 | 12 | 17.4930 | 14.8688 | -114.0097 | 3.7385 | 51.7392 | 0.0148 | 0.0078 |
| 2024_09_20 22:00 | 3233027 | 13 | 19.4896 | 10.2443 | -116.7538 | 4.6181 | 21.2028 | 0.0017 | 0.0098 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413650_0C051AB4 | 152650 | 1005 | -90.3 | 152650 | 394 | -96.8 | 152650 | 707 | -103.2 | 152650 | 268 |
| MR_1774413650_9BC98F76 | 504990 | 400 | -92.9 | 504990 | 846 | -92.4 | 504990 | 51 | -94.1 | 504990 | 313 |
| MR_1774413650_900EF36A | 152650 | 1005 | -90.2 | 152650 | 394 | -96.4 | 152650 | 707 | -101.7 | 152650 | 268 |
| MR_1774413650_FE42285F | 504990 | 400 | -92.9 | 504990 | 846 | -92.1 | 504990 | 51 | -94.3 | 504990 | 313 |
| MR_1774413650_2C3B55EC | 152650 | 1005 | -91.8 | 152650 | 394 | -96.2 | 152650 | 707 | -102.2 | 152650 | 268 |

> *... 2개 열 생략 (전체 14열)*

---
