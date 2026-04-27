# Track A 문제 분석 — test[400]~test[409]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[400] ~ test[409] (10개)

## 목차

1. [문제 400: `17157c64-352...`](#400) — single-answer
2. [문제 401: `85cc4eba-d23...`](#401) — single-answer
3. [문제 402: `58a6d4cf-667...`](#402) — single-answer
4. [문제 403: `3035b75d-210...`](#403) — single-answer
5. [문제 404: `87094513-963...`](#404) — single-answer
6. [문제 405: `dfb16541-9e4...`](#405) — single-answer
7. [문제 406: `8c8f264a-075...`](#406) — single-answer
8. [문제 407: `78bd577f-2c2...`](#407) — multiple-answer
9. [문제 408: `85bc95aa-f02...`](#408) — single-answer
10. [문제 409: `55e4900f-dc8...`](#409) — single-answer

---

### 문제 400: `17157c64-352...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `17157c64-352a-484c-8519-2cec4231c5fa` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[400] topology](images/test_0400.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3227919_4
- `C2`: Increase A3 Offset threshold for 3216064_1
- `C3`: Decrease transmission power for 3227919_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216064_1
- `C5`: Decrease transmission power for 3216064_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227919_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216064_1
- `C8`: Adjust the azimuth of 3227919_4 by 30 degrees
- `C9`: Decrease A3 Offset threshold for 3216064_1
- `C10`: Add neighbor relationship between 3272637_2 and 3227919_4
- `C11`: Add neighbor relationship between 3216064_1 and 3227919_4
- `C12`: Adjust the azimuth of 3216064_1 by 48 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227919_4
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Lift the tilt angle  of 3227919_4 by 6 degrees
- `C16`: Press down the tilt angle of 3216064_1 by 10 degrees
- `C17`: Lift the tilt angle of 3216064_1 by 10 degrees
- `C18`: Decrease A3 Offset threshold for 3227919_4
- `C19`: Increase A3 Offset threshold for 3227919_4
- `C20`: Increase transmission power for 3216064_1
- `C21`: Press down the tilt angle  of 3227919_4 by 6 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.400 | MS1 | 121.4656671972 | 31.1446332983 | 425 | 504990 | -80.13 | 12.19 | 338.10 | 0.05 | 2.70 | 1590 |
| 2024-09-20 22:21:32.879 | MS1 | 121.4656738930 | 31.1446296417 | 425 | 504990 | -83.40 | 13.95 | 449.83 | 0.15 | 2.42 | 1595 |
| 2024-09-20 22:21:33.853 | MS1 | 121.4656654083 | 31.1446211344 | 425 | 504990 | -78.41 | 12.63 | 530.30 | 0.08 | 2.18 | 1566 |
| 2024-09-20 22:21:34.980 | MS1 | 121.4656629346 | 31.1446335615 | 425 | 504990 | -90.15 | -0.51 | 74.91 | 0.01 | 1.42 | 1579 |
| 2024-09-20 22:21:35.782 | MS1 | 121.4656678894 | 31.1446324432 | 425 | 504990 | -94.03 | -2.72 | 76.80 | 0.20 | 1.17 | 1598 |
| 2024-09-20 22:21:36.926 | MS1 | 121.4656716582 | 31.1446242466 | 425 | 504990 | -87.20 | -0.45 | 74.77 | 0.11 | 1.47 | 1563 |
| 2024-09-20 22:21:37.880 | MS1 | 121.4656628896 | 31.1446187250 | 425 | 504990 | -86.32 | -1.08 | 35.98 | 0.16 | 1.06 | 1562 |
| 2024-09-20 22:21:38.790 | MS1 | 121.4656588761 | 31.1446221999 | 425 | 504990 | -82.34 | 17.14 | 424.47 | 0.10 | 1.04 | 1578 |
| 2024-09-20 22:21:39.123 | MS1 | 121.4656695009 | 31.1446326368 | 425 | 504990 | -76.73 | 15.32 | 446.88 | 0.12 | 1.29 | 1598 |
| 2024-09-20 22:21:40.524 | MS1 | 121.4656772969 | 31.1446185856 | 425 | 504990 | -76.04 | 14.90 | 519.10 | 0.09 | 2.95 | 1585 |
| 2024-09-20 22:21:41.616 | MS1 | 121.4656648415 | 31.1446311201 | 425 | 504990 | -77.23 | 12.75 | 396.72 | 0.10 | 2.67 | 1598 |
| 2024-09-20 22:21:42.523 | MS1 | 121.4656739097 | 31.1446248164 | 425 | 504990 | -82.37 | 13.89 | 437.37 | 0.06 | 2.72 | 1596 |

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
| 3216064 | 1 | 121.4754517570 | 31.1530028567 | 273 | 12 | 6 | 47.6 | TDD | 425 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3224772 | 3 | 121.4751188990 | 31.1489937012 | 151 | 5 | 0 | 34.5 | TDD | 148 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3227919 | 4 | 121.4717436159 | 31.1529929277 | 182 | 4 | 0 | 35.9 | TDD | 606 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3272637 | 2 | 121.4699528596 | 31.1538404941 | 98 | 0 | 1 | 30.1 | TDD | 43 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.957 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.982 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.100 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.100 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.780 | NREventA3 | measId:2;ServCellPCI:317;Se... |
| 2024-09-20 22:21:35.780 | NREventA3 | measId:2;ServCellPCI:317;Se... |
| 2024-09-20 22:21:36.780 | NREventA3 | measId:2;ServCellPCI:317;Se... |
| 2024-09-20 22:21:39.280 | NRRRCReestablishAttempt | PCI:317 |
| 2024-09-20 22:21:39.299 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.314 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.443 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.443 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216064 | 1 | 8.4798 | 15.8213 | -116.5556 | 19.9491 | 197.8581 | 0.0197 | 0.1471 |
| 2024_09_20 22:00 | 3272637 | 2 | 5.5830 | 7.1961 | -117.7713 | 15.7417 | 191.6404 | 0.0039 | 0.0003 |
| 2024_09_20 22:00 | 3224772 | 3 | 13.7595 | 11.0697 | -114.7177 | 14.9255 | 123.0144 | 0.0186 | 0.0150 |
| 2024_09_20 22:00 | 3227919 | 4 | 18.3885 | 17.4899 | -114.2226 | 16.6916 | 105.0992 | 0.0073 | 0.0184 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414934_1B796747 | 504990 | 606 | -83.5 | 504990 | 425 | -90.2 | 504990 | 43 | -92.9 | 504990 | 148 |
| MR_1774414934_EC101041 | 504990 | 425 | -89.6 | 504990 | 606 | -85.4 | 504990 | 43 | -89.5 | 504990 | 148 |
| MR_1774414934_1C6064D6 | 504990 | 425 | -92.1 | 504990 | 606 | -85.8 | 504990 | 43 | -89.7 | 504990 | 148 |
| MR_1774414934_64C292FC | 504990 | 425 | -89.0 | 504990 | 606 | -84.9 | 504990 | 43 | -93.1 | 504990 | 148 |
| MR_1774414934_B0EAD3AE | 504990 | 606 | -85.8 | 504990 | 425 | -91.1 | 504990 | 43 | -92.4 | 504990 | 148 |
| MR_1774414934_B76884EA | 504990 | 425 | -89.6 | 504990 | 606 | -83.9 | 504990 | 43 | -93.1 | 504990 | 148 |
| MR_1774414934_CF431C38 | 504990 | 606 | -82.6 | 504990 | 425 | -89.7 | 504990 | 43 | -90.9 | 504990 | 148 |
| MR_1774414934_F7667BEA | 504990 | 606 | -85.0 | 504990 | 425 | -88.2 | 504990 | 43 | -90.0 | 504990 | 148 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 401: `85cc4eba-d23...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `85cc4eba-d238-4ef1-89df-e1e083c33f8d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[401] topology](images/test_0401.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3213149_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213149_3
- `C3`: Add neighbor relationship between 3215402_2 and 3213149_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215402_2
- `C5`: Decrease transmission power for 3213149_3
- `C6`: Lift the tilt angle of 3215402_2 by 10 degrees
- `C7`: Add neighbor relationship between 3266728_4 and 3213149_3
- `C8`: Increase transmission power for 3215402_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215402_2
- `C10`: Increase A3 Offset threshold for 3213149_3
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Adjust the azimuth of 3213149_3 by 34 degrees
- `C13`: Decrease A3 Offset threshold for 3215402_2
- `C14`: Lift the tilt angle  of 3213149_3 by 4 degrees
- `C15`: Check test server and transmission issues
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213149_3
- `C17`: Decrease transmission power for 3215402_2
- `C18`: Increase transmission power for 3213149_3
- `C19`: Press down the tilt angle of 3215402_2 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3215402_2
- `C21`: Adjust the azimuth of 3215402_2 by 50 degrees
- `C22`: Press down the tilt angle  of 3213149_3 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.284 | MS1 | 121.4656642446 | 31.1446365042 | 155 | 504990 | -77.36 | 15.85 | 534.41 | 0.12 | 2.97 | 1575 |
| 2024-09-20 22:21:32.314 | MS1 | 121.4656768706 | 31.1446257580 | 155 | 504990 | -79.00 | 12.98 | 528.90 | 0.05 | 2.81 | 1596 |
| 2024-09-20 22:21:33.646 | MS1 | 121.4656681283 | 31.1446325561 | 155 | 504990 | -76.26 | 14.98 | 523.18 | 0.14 | 2.81 | 1573 |
| 2024-09-20 22:21:34.326 | MS1 | 121.4656715105 | 31.1446344526 | 155 | 504990 | -88.58 | -2.61 | 68.99 | 0.09 | 1.19 | 1567 |
| 2024-09-20 22:21:35.407 | MS1 | 121.4656709892 | 31.1446180044 | 155 | 504990 | -87.59 | -0.55 | 52.15 | 0.20 | 1.14 | 1583 |
| 2024-09-20 22:21:36.657 | MS1 | 121.4656590593 | 31.1446286006 | 155 | 504990 | -92.02 | -1.75 | 43.92 | 0.15 | 1.21 | 1598 |
| 2024-09-20 22:21:37.625 | MS1 | 121.4656590281 | 31.1446227783 | 155 | 504990 | -85.88 | -2.53 | 76.55 | 0.10 | 1.10 | 1592 |
| 2024-09-20 22:21:38.620 | MS1 | 121.4656729732 | 31.1446279457 | 155 | 504990 | -81.94 | 16.25 | 543.98 | 0.13 | 1.03 | 1571 |
| 2024-09-20 22:21:39.806 | MS1 | 121.4656606152 | 31.1446295446 | 155 | 504990 | -82.93 | 12.05 | 576.53 | 0.07 | 1.47 | 1562 |
| 2024-09-20 22:21:40.545 | MS1 | 121.4656658855 | 31.1446371444 | 155 | 504990 | -80.95 | 13.01 | 303.64 | 0.15 | 2.35 | 1579 |
| 2024-09-20 22:21:41.681 | MS1 | 121.4656620163 | 31.1446295173 | 155 | 504990 | -78.85 | 15.55 | 465.40 | 0.08 | 2.34 | 1560 |
| 2024-09-20 22:21:42.452 | MS1 | 121.4656774254 | 31.1446342367 | 155 | 504990 | -82.94 | 17.79 | 506.24 | 0.07 | 2.89 | 1593 |

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
| 3213149 | 3 | 121.4739341773 | 31.1520820955 | 190 | 2 | 4 | 41.8 | TDD | 847 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3215402 | 2 | 121.4641376749 | 31.1517003455 | 76 | 11 | 8 | 38.5 | TDD | 155 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3266728 | 4 | 121.4703296925 | 31.1483406468 | 307 | 4 | 3 | 43.6 | TDD | 231 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3273186 | 1 | 121.4725741422 | 31.1554409431 | 221 | 13 | 3 | 18.3 | TDD | 978 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.800 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.822 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.957 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.957 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.640 | NREventA3 | measId:2;ServCellPCI:558;Se... |
| 2024-09-20 22:21:35.640 | NREventA3 | measId:2;ServCellPCI:558;Se... |
| 2024-09-20 22:21:36.640 | NREventA3 | measId:2;ServCellPCI:558;Se... |
| 2024-09-20 22:21:39.140 | NRRRCReestablishAttempt | PCI:558 |
| 2024-09-20 22:21:39.157 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.170 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.318 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.318 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273186 | 1 | 14.6144 | 13.2222 | -114.8070 | 19.5098 | 122.8475 | 0.0115 | 0.0049 |
| 2024_09_20 22:00 | 3215402 | 2 | 11.8999 | 10.2952 | -117.9379 | 6.1709 | 104.7508 | 0.0010 | 0.1446 |
| 2024_09_20 22:00 | 3213149 | 3 | 12.1990 | 6.0017 | -116.6141 | 11.6998 | 110.0299 | 0.0179 | 0.0113 |
| 2024_09_20 22:00 | 3266728 | 4 | 17.8838 | 17.9121 | -116.2959 | 12.3842 | 114.4557 | 0.0045 | 0.0033 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412848_94D83C0C | 504990 | 155 | -87.0 | 504990 | 847 | -83.2 | 504990 | 231 | -86.8 | 504990 | 978 |
| MR_1774412848_0F3341E0 | 504990 | 847 | -83.3 | 504990 | 155 | -88.1 | 504990 | 231 | -88.6 | 504990 | 978 |
| MR_1774412848_CC92F109 | 504990 | 155 | -86.8 | 504990 | 847 | -82.0 | 504990 | 231 | -87.7 | 504990 | 978 |
| MR_1774412848_1BAAAAD1 | 504990 | 155 | -89.9 | 504990 | 847 | -82.0 | 504990 | 231 | -89.4 | 504990 | 978 |
| MR_1774412848_60C2EA1E | 504990 | 155 | -88.9 | 504990 | 847 | -83.3 | 504990 | 231 | -88.6 | 504990 | 978 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 402: `58a6d4cf-667...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `58a6d4cf-6671-4bb6-977d-348ff6fad618` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[402] topology](images/test_0402.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Press down the tilt angle  of 3245731_2 by 10 degrees
- `C3`: Check test server and transmission issues
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245731_2
- `C5`: Press down the tilt angle of 3228014_4 by 4 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228014_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245731_2
- `C8`: Decrease A3 Offset threshold for 3245731_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228014_4
- `C10`: Add neighbor relationship between 3228014_4 and 3245731_2
- `C11`: Increase transmission power for 3228014_4
- `C12`: Lift the tilt angle of 3228014_4 by 4 degrees
- `C13`: Adjust the azimuth of 3245731_2 by 50 degrees
- `C14`: Add neighbor relationship between 3236633_3 and 3245731_2
- `C15`: Decrease transmission power for 3228014_4
- `C16`: Lift the tilt angle  of 3245731_2 by 10 degrees
- `C17`: Adjust the azimuth of 3228014_4 by 17 degrees
- `C18`: Increase transmission power for 3245731_2
- `C19`: Increase A3 Offset threshold for 3228014_4
- `C20`: Decrease transmission power for 3245731_2
- `C21`: Increase A3 Offset threshold for 3245731_2
- `C22`: Decrease A3 Offset threshold for 3228014_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.626 | MS1 | 121.4656740343 | 31.1446366941 | 943 | 504990 | -86.82 | 12.84 | 470.44 | 0.17 | 2.23 | 1566 |
| 2024-09-20 22:21:32.957 | MS1 | 121.4656689146 | 31.1446196702 | 943 | 504990 | -90.49 | 15.87 | 428.35 | 0.02 | 2.14 | 1575 |
| 2024-09-20 22:21:33.425 | MS1 | 121.4656622625 | 31.1446264526 | 943 | 504990 | -85.98 | 14.33 | 339.10 | 0.11 | 2.03 | 1583 |
| 2024-09-20 22:21:34.323 | MS1 | 121.4656622086 | 31.1446345749 | 943 | 504990 | -90.43 | 17.56 | 66.48 | 0.50 | 2.89 | 690 |
| 2024-09-20 22:21:35.934 | MS1 | 121.4656700274 | 31.1446363421 | 943 | 504990 | -88.09 | 17.53 | 88.42 | 0.62 | 2.29 | 596 |
| 2024-09-20 22:21:36.416 | MS1 | 121.4656700152 | 31.1446224165 | 943 | 504990 | -90.80 | 12.80 | 92.37 | 0.53 | 2.02 | 578 |
| 2024-09-20 22:21:37.806 | MS1 | 121.4656619216 | 31.1446237647 | 943 | 504990 | -89.84 | 11.19 | 76.65 | 0.55 | 2.10 | 566 |
| 2024-09-20 22:21:38.600 | MS1 | 121.4656702526 | 31.1446293633 | 943 | 504990 | -92.18 | 9.73 | 76.93 | 0.57 | 2.71 | 656 |
| 2024-09-20 22:21:39.719 | MS1 | 121.4656723474 | 31.1446295920 | 943 | 504990 | -93.04 | 9.19 | 63.39 | 0.59 | 2.78 | 556 |
| 2024-09-20 22:21:40.335 | MS1 | 121.4656648486 | 31.1446241774 | 943 | 504990 | -89.70 | 8.02 | 416.48 | 0.04 | 2.68 | 1575 |
| 2024-09-20 22:21:41.201 | MS1 | 121.4656678286 | 31.1446321423 | 943 | 504990 | -89.03 | 11.62 | 384.24 | 0.06 | 2.09 | 1560 |
| 2024-09-20 22:21:42.421 | MS1 | 121.4656748708 | 31.1446190442 | 943 | 504990 | -93.08 | 12.53 | 314.30 | 0.18 | 2.67 | 1571 |

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
| 3228014 | 4 | 121.4681615655 | 31.1533688434 | 211 | 2 | 4 | 39.1 | TDD | 943 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3236633 | 3 | 121.4672470630 | 31.1537552813 | 334 | 12 | 9 | 34.5 | TDD | 964 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3245731 | 2 | 121.4641321965 | 31.1493942012 | 65 | 15 | 8 | 39.2 | TDD | 380 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3272556 | 1 | 121.4652833583 | 31.1477428734 | 284 | 1 | 6 | 21.8 | TDD | 256 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.076 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.100 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.250 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.250 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.926 | NREventA3 | measId:2;ServCellPCI:187;Se... |
| 2024-09-20 22:21:38.166 | NRHandoverAttempt | SourcePCI:187;SourceNR-ARFC... |
| 2024-09-20 22:21:38.201 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.214 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.364 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.364 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272556 | 1 | 7.7540 | 11.9883 | -116.7094 | 9.3287 | 112.3752 | 0.0020 | 0.0014 |
| 2024_09_20 22:00 | 3245731 | 2 | 13.3595 | 11.8073 | -117.1916 | 7.1187 | 185.1325 | 0.0008 | 0.0050 |
| 2024_09_20 22:00 | 3236633 | 3 | 13.3847 | 12.1942 | -114.3177 | 19.0335 | 125.3783 | 0.0185 | 0.0172 |
| 2024_09_20 22:00 | 3228014 | 4 | 15.7946 | 15.1224 | -114.8581 | 16.6714 | 83.5135 | 0.0108 | 0.0043 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414790_D2903524 | 504990 | 943 | -92.3 | 504990 | 380 | -94.8 | 504990 | 964 | -98.9 | 504990 | 256 |
| MR_1774414790_95BE93CE | 504990 | 943 | -92.4 | 504990 | 380 | -96.5 | 504990 | 964 | -98.2 | 504990 | 256 |
| MR_1774414790_7C9CBCAF | 504990 | 943 | -91.9 | 504990 | 380 | -94.6 | 504990 | 964 | -97.6 | 504990 | 256 |
| MR_1774414790_A85B1196 | 504990 | 943 | -89.6 | 504990 | 380 | -94.6 | 504990 | 964 | -100.7 | 504990 | 256 |
| MR_1774414790_7AB164CF | 504990 | 943 | -91.7 | 504990 | 380 | -93.0 | 504990 | 964 | -100.6 | 504990 | 256 |
| MR_1774414790_B8C78109 | 504990 | 943 | -90.5 | 504990 | 380 | -94.8 | 504990 | 964 | -97.6 | 504990 | 256 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 403: `3035b75d-210...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3035b75d-2106-4199-ba95-2a8cb01ac0d4` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[403] topology](images/test_0403.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3265539_1 and 3262725_2
- `C2`: Increase transmission power for 3265539_1
- `C3`: Lift the tilt angle  of 3262725_2 by 7 degrees
- `C4`: Press down the tilt angle of 3265539_1 by 10 degrees
- `C5`: Increase A3 Offset threshold for 3262725_2
- `C6`: Add neighbor relationship between 3240273_3 and 3262725_2
- `C7`: Decrease transmission power for 3262725_2
- `C8`: Adjust the azimuth of 3262725_2 by 44 degrees
- `C9`: Press down the tilt angle  of 3262725_2 by 7 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262725_2
- `C11`: Check test server and transmission issues
- `C12`: Adjust the azimuth of 3265539_1 by 50 degrees
- `C13`: Decrease A3 Offset threshold for 3265539_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262725_2
- `C15`: Decrease transmission power for 3265539_1
- `C16`: Lift the tilt angle of 3265539_1 by 10 degrees
- `C17`: Increase A3 Offset threshold for 3265539_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265539_1
- `C19`: Decrease A3 Offset threshold for 3262725_2
- `C20`: Increase transmission power for 3262725_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265539_1
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.170 | MS1 | 121.4656692825 | 31.1446347366 | 233 | 504990 | -91.95 | 15.38 | 293.75 | 0.13 | 2.20 | 1578 |
| 2024-09-20 22:21:32.823 | MS1 | 121.4656626822 | 31.1446291132 | 233 | 504990 | -88.94 | 12.50 | 515.25 | 0.04 | 2.09 | 1572 |
| 2024-09-20 22:21:33.874 | MS1 | 121.4656701635 | 31.1446286952 | 233 | 504990 | -86.95 | 13.94 | 309.32 | 0.05 | 2.09 | 1564 |
| 2024-09-20 22:21:34.890 | MS1 | 121.4656770035 | 31.1446311348 | 233 | 504990 | -89.72 | 13.70 | 93.71 | 0.02 | 2.00 | 1563 |
| 2024-09-20 22:21:35.326 | MS1 | 121.4656688641 | 31.1446359874 | 233 | 504990 | -91.65 | 15.52 | 87.13 | 0.13 | 2.51 | 1597 |
| 2024-09-20 22:21:36.663 | MS1 | 121.4656757500 | 31.1446379730 | 233 | 504990 | -85.61 | 17.40 | 90.04 | 0.07 | 2.20 | 1567 |
| 2024-09-20 22:21:37.157 | MS1 | 121.4656634022 | 31.1446184237 | 233 | 504990 | -92.20 | 9.29 | 96.35 | 0.07 | 2.93 | 1591 |
| 2024-09-20 22:21:38.854 | MS1 | 121.4656776021 | 31.1446186040 | 233 | 504990 | -91.72 | 12.13 | 62.30 | 0.11 | 2.90 | 1581 |
| 2024-09-20 22:21:39.582 | MS1 | 121.4656664683 | 31.1446351364 | 233 | 504990 | -89.42 | 8.35 | 83.00 | 0.07 | 2.97 | 1596 |
| 2024-09-20 22:21:40.126 | MS1 | 121.4656744248 | 31.1446266980 | 233 | 504990 | -89.88 | 8.52 | 507.56 | 0.04 | 2.85 | 1580 |
| 2024-09-20 22:21:41.105 | MS1 | 121.4656653836 | 31.1446287104 | 233 | 504990 | -90.93 | 8.36 | 530.00 | 0.03 | 2.74 | 1585 |
| 2024-09-20 22:21:42.342 | MS1 | 121.4656641789 | 31.1446231918 | 233 | 504990 | -91.98 | 7.58 | 372.92 | 0.17 | 2.28 | 1562 |

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
| 3218202 | 4 | 121.4656543521 | 31.1512106820 | 284 | 14 | 11 | 40.7 | TDD | 70 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3240273 | 3 | 121.4648469620 | 31.1473539296 | 324 | 9 | 0 | 42.7 | TDD | 828 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3262725 | 2 | 121.4682907272 | 31.1547718360 | 148 | 6 | 4 | 23.0 | TDD | 266 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3265539 | 1 | 121.4721160916 | 31.1441464552 | 95 | 12 | 7 | 39.0 | TDD | 233 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.531 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.556 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.680 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.680 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.338 | NREventA3 | measId:2;ServCellPCI:30;Ser... |
| 2024-09-20 22:21:38.578 | NRHandoverAttempt | SourcePCI:30;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.616 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.631 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.734 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.734 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3265539 | 1 | 85.1776 | 91.0832 | -117.0556 | 5.0241 | 117.6533 | 0.0072 | 0.0147 |
| 2024_09_19 22:00 | 3262725 | 2 | 79.4544 | 80.4005 | -117.9200 | 15.3381 | 115.6456 | 0.0049 | 0.0035 |
| 2024_09_19 22:00 | 3240273 | 3 | 79.0965 | 87.9873 | -115.6654 | 16.1569 | 88.8009 | 0.0097 | 0.0071 |
| 2024_09_19 22:00 | 3218202 | 4 | 75.4114 | 93.3457 | -117.9661 | 19.7673 | 130.0053 | 0.0105 | 0.0135 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416600_E48FBFE1 | 504990 | 233 | -88.0 | 504990 | 266 | -93.1 | 504990 | 828 | -101.3 | 504990 | 70 |
| MR_1774416600_3935BBAC | 504990 | 233 | -88.3 | 504990 | 266 | -95.2 | 504990 | 828 | -102.4 | 504990 | 70 |
| MR_1774416600_47091DF5 | 504990 | 233 | -89.5 | 504990 | 266 | -91.9 | 504990 | 828 | -100.7 | 504990 | 70 |
| MR_1774416600_F00EC6CD | 504990 | 233 | -87.8 | 504990 | 266 | -95.4 | 504990 | 828 | -102.4 | 504990 | 70 |
| MR_1774416600_2B7B77DA | 504990 | 233 | -88.1 | 504990 | 266 | -94.4 | 504990 | 828 | -99.4 | 504990 | 70 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 404: `87094513-963...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `87094513-9633-4ec4-b845-4d89b738bcac` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[404] topology](images/test_0404.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3274650_3 by 10 degrees
- `C2`: Increase transmission power for 3225249_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225249_4
- `C4`: Decrease transmission power for 3210883_2
- `C5`: Lift the tilt angle of 3210883_2 by 3 degrees
- `C6`: Adjust the azimuth of 3274650_3 by 50 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225249_4
- `C8`: Decrease transmission power for 3225249_4
- `C9`: Press down the tilt angle of 3210883_2 by 3 degrees
- `C10`: Check test server and transmission issues
- `C11`: Adjust the azimuth of 3210883_2 by 27 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210883_2
- `C13`: Decrease A3 Offset threshold for 3225249_4
- `C14`: Add neighbor relationship between 3274650_3 and 3225249_4
- `C15`: Increase transmission power for 3210883_2
- `C16`: Increase A3 Offset threshold for 3225249_4
- `C17`: Increase A3 Offset threshold for 3210883_2
- `C18`: Decrease A3 Offset threshold for 3210883_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210883_2
- `C20`: Add neighbor relationship between 3210883_2 and 3225249_4
- `C21`: Press down the tilt angle  of 3274650_3 by 10 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.650 | MS1 | 121.4656777714 | 31.1446337218 | 802 | 504990 | -91.08 | 16.20 | 430.18 | 0.14 | 2.84 | 1590 |
| 2024-09-20 22:21:32.999 | MS1 | 121.4656623932 | 31.1446286432 | 802 | 504990 | -91.96 | 17.78 | 515.55 | 0.17 | 2.15 | 1582 |
| 2024-09-20 22:21:33.858 | MS1 | 121.4656628963 | 31.1446341851 | 802 | 504990 | -89.78 | 14.84 | 420.35 | 0.19 | 2.01 | 1587 |
| 2024-09-20 22:21:34.195 | MS1 | 121.4656604392 | 31.1446277292 | 802 | 504990 | -91.34 | 15.97 | 104.59 | 0.02 | 2.75 | 1598 |
| 2024-09-20 22:21:35.498 | MS1 | 121.4656711319 | 31.1446239250 | 802 | 504990 | -91.80 | 15.21 | 69.56 | 0.13 | 2.02 | 1580 |
| 2024-09-20 22:21:36.664 | MS1 | 121.4656761941 | 31.1446236575 | 802 | 504990 | -86.69 | 16.57 | 94.83 | 0.10 | 2.40 | 1569 |
| 2024-09-20 22:21:37.941 | MS1 | 121.4656733269 | 31.1446306093 | 802 | 504990 | -90.54 | 12.46 | 76.60 | 0.20 | 2.53 | 1560 |
| 2024-09-20 22:21:38.829 | MS1 | 121.4656773002 | 31.1446293981 | 802 | 504990 | -89.81 | 11.56 | 58.39 | 0.14 | 2.18 | 1567 |
| 2024-09-20 22:21:39.445 | MS1 | 121.4656763831 | 31.1446192997 | 802 | 504990 | -90.61 | 9.50 | 75.23 | 0.05 | 2.66 | 1561 |
| 2024-09-20 22:21:40.346 | MS1 | 121.4656724999 | 31.1446325196 | 802 | 504990 | -89.61 | 11.78 | 461.96 | 0.13 | 2.57 | 1595 |
| 2024-09-20 22:21:41.185 | MS1 | 121.4656775784 | 31.1446190397 | 802 | 504990 | -92.05 | 10.44 | 480.34 | 0.02 | 2.75 | 1564 |
| 2024-09-20 22:21:42.825 | MS1 | 121.4656768942 | 31.1446189329 | 802 | 504990 | -90.38 | 12.95 | 409.61 | 0.04 | 2.70 | 1562 |

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
| 3210883 | 2 | 121.4712963097 | 31.1469161374 | 272 | 1 | 7 | 15.9 | TDD | 802 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3225249 | 4 | 121.4728838843 | 31.1539103470 | 341 | 9 | 7 | 19.2 | TDD | 683 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3228302 | 1 | 121.4759080790 | 31.1544715838 | 38 | 4 | 10 | 21.6 | TDD | 945 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3274650 | 3 | 121.4724980386 | 31.1555241715 | 106 | 10 | 2 | 48.0 | TDD | 291 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.888 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.904 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.036 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.036 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.695 | NREventA3 | measId:2;ServCellPCI:458;Se... |
| 2024-09-20 22:21:37.935 | NRHandoverAttempt | SourcePCI:458;SourceNR-ARFC... |
| 2024-09-20 22:21:37.979 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.991 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.124 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.124 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228302 | 1 | 15.2539 | 8.2937 | -115.8130 | 13.2920 | 134.0569 | 0.0130 | 0.0027 |
| 2024_09_20 22:00 | 3210883 | 2 | 88.1328 | 87.0657 | -117.2630 | 9.4982 | 182.6468 | 0.0048 | 0.0199 |
| 2024_09_20 22:00 | 3274650 | 3 | 18.1183 | 17.9297 | -116.7168 | 5.8824 | 128.4600 | 0.0112 | 0.0072 |
| 2024_09_20 22:00 | 3225249 | 4 | 8.5388 | 6.6354 | -117.4243 | 10.0768 | 124.5080 | 0.0103 | 0.0061 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412301_4B3D9956 | 504990 | 802 | -90.7 | 504990 | 683 | -101.8 | 504990 | 291 | -103.3 | 504990 | 945 |
| MR_1774412301_1FA6CEE5 | 504990 | 802 | -89.8 | 504990 | 683 | -100.8 | 504990 | 291 | -104.4 | 504990 | 945 |
| MR_1774412301_7DE2086A | 504990 | 802 | -90.6 | 504990 | 683 | -100.8 | 504990 | 291 | -101.9 | 504990 | 945 |
| MR_1774412301_02E8C767 | 504990 | 802 | -91.0 | 504990 | 683 | -100.8 | 504990 | 291 | -103.4 | 504990 | 945 |
| MR_1774412301_087FD282 | 504990 | 802 | -91.6 | 504990 | 683 | -102.3 | 504990 | 291 | -102.2 | 504990 | 945 |
| MR_1774412301_1B249B4E | 504990 | 802 | -91.4 | 504990 | 683 | -102.9 | 504990 | 291 | -103.8 | 504990 | 945 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 405: `dfb16541-9e4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dfb16541-9e49-4d32-a51c-9576ed10a2a2` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[405] topology](images/test_0405.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3216343_4 by 2 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211543_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211543_3
- `C4`: Increase transmission power for 3211543_3
- `C5`: Check test server and transmission issues
- `C6`: Lift the tilt angle  of 3211543_3 by 4 degrees
- `C7`: Decrease transmission power for 3216343_4
- `C8`: Decrease A3 Offset threshold for 3216343_4
- `C9`: Increase A3 Offset threshold for 3211543_3
- `C10`: Decrease A3 Offset threshold for 3211543_3
- `C11`: Increase A3 Offset threshold for 3216343_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216343_4
- `C13`: Add neighbor relationship between 3274747_13 and 3211543_3
- `C14`: Increase transmission power for 3216343_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216343_4
- `C16`: Lift the tilt angle of 3216343_4 by 2 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Press down the tilt angle  of 3211543_3 by 4 degrees
- `C19`: Adjust the azimuth of 3216343_4 by 31 degrees
- `C20`: Add neighbor relationship between 3216343_4 and 3211543_3
- `C21`: Adjust the azimuth of 3211543_3 by 37 degrees
- `C22`: Decrease transmission power for 3211543_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.678 | MS1 | 121.4656626638 | 31.1446195699 | 56 | 504990 | -95.66 | 13.18 | 563.06 | 0.07 | 2.36 | 1594 |
| 2024-09-20 22:21:32.417 | MS1 | 121.4656675672 | 31.1446254386 | 551 | 504990 | -93.65 | 9.96 | 361.56 | 0.01 | 2.60 | 1594 |
| 2024-09-20 22:21:33.175 | MS1 | 121.4656622157 | 31.1446284962 | 379 | 504990 | -94.58 | 13.54 | 450.94 | 0.03 | 2.68 | 1587 |
| 2024-09-20 22:21:34.801 | MS1 | 121.4656638845 | 31.1446361610 | 188 | 152650 | -91.48 | 4.69 | 47.78 | 0.04 | 1.52 | 928 |
| 2024-09-20 22:21:35.847 | MS1 | 121.4656737304 | 31.1446241052 | 621 | 152650 | -92.53 | 2.48 | 58.25 | 0.07 | 1.73 | 923 |
| 2024-09-20 22:21:36.136 | MS1 | 121.4656620626 | 31.1446231964 | 125 | 152650 | -92.25 | 4.11 | 75.62 | 0.15 | 1.97 | 922 |
| 2024-09-20 22:21:37.703 | MS1 | 121.4656690300 | 31.1446373709 | 241 | 152650 | -88.75 | 6.40 | 85.67 | 0.15 | 1.76 | 901 |
| 2024-09-20 22:21:38.939 | MS1 | 121.4656723526 | 31.1446339777 | 188 | 152650 | -94.77 | 4.61 | 91.30 | 0.04 | 1.66 | 979 |
| 2024-09-20 22:21:39.226 | MS1 | 121.4656737734 | 31.1446243708 | 621 | 152650 | -94.76 | 3.79 | 79.02 | 0.04 | 1.92 | 996 |
| 2024-09-20 22:21:40.312 | MS1 | 121.4656730788 | 31.1446242602 | 125 | 152650 | -88.57 | 7.77 | 96.58 | 0.09 | 2.48 | 1584 |
| 2024-09-20 22:21:41.934 | MS1 | 121.4656592299 | 31.1446197525 | 241 | 152650 | -92.31 | 4.67 | 73.98 | 0.02 | 2.72 | 1561 |
| 2024-09-20 22:21:42.743 | MS1 | 121.4656626635 | 31.1446345540 | 188 | 152650 | -90.93 | 7.05 | 73.58 | 0.11 | 2.64 | 1597 |

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
| 3211543 | 3 | 121.4690987395 | 31.1490633203 | 251 | 3 | 6 | 7.8 | TDD | 118 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3215685 | 9 | 121.4744377388 | 31.1440180921 | 28 | 13 | 9 | 1.2 | FDD | 28 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3216190 | 7 | 121.4651893290 | 31.1500639166 | 2 | 6 | 2 | 14.1 | FDD | 621 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3216343 | 4 | 121.4674864934 | 31.1447938390 | 295 | 0 | 7 | 6.5 | TDD | 56 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3218365 | 6 | 121.4690641266 | 31.1454402583 | 212 | 13 | 6 | 11.5 | TDD | 379 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3223345 | 10 | 121.4690245424 | 31.1482658323 | 352 | 7 | 5 | 13.8 | FDD | 241 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3231405 | 2 | 121.4697463874 | 31.1489665937 | 167 | 12 | 12 | 9.0 | TDD | 301 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3254700 | 1 | 121.4657723299 | 31.1553077812 | 210 | 2 | 0 | 18.5 | TDD | 551 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3259221 | 11 | 121.4656146976 | 31.1515043108 | 311 | 10 | 0 | 12.7 | FDD | 282 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3265978 | 12 | 121.4737218177 | 31.1543124460 | 178 | 7 | 5 | 8.6 | FDD | 188 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3274747 | 13 | 121.4708402771 | 31.1460745132 | 200 | 12 | 6 | 22.5 | FDD | 125 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3275558 | 5 | 121.4723774846 | 31.1456273910 | 61 | 2 | 5 | 18.2 | TDD | 730 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3277552 | 8 | 121.4643458421 | 31.1533827281 | 115 | 15 | 10 | 2.6 | FDD | 366 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |

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
| 2024-09-20 22:21:30.806 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.821 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.950 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.950 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.659 | NREventA2 | measId:1;ServCellPCI:980;Se... |
| 2024-09-20 22:21:34.765 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:34.982 | NREventA5 | measId:3;ServCellPCI:980;Se... |
| 2024-09-20 22:21:35.024 | NRHandoverAttempt | SourcePCI:980;SourceNR-ARFC... |
| 2024-09-20 22:21:35.053 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.066 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.216 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.216 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254700 | 1 | 15.3502 | 10.7796 | -116.4820 | 6.2232 | 178.2642 | 0.0014 | 0.0175 |
| 2024_09_20 22:00 | 3231405 | 2 | 19.4245 | 19.1806 | -116.2390 | 14.5679 | 199.0169 | 0.0022 | 0.0121 |
| 2024_09_20 22:00 | 3211543 | 3 | 5.7212 | 8.1647 | -115.8984 | 8.7236 | 186.6362 | 0.0136 | 0.0199 |
| 2024_09_20 22:00 | 3216343 | 4 | 15.9917 | 10.4144 | -115.6445 | 7.3684 | 86.0137 | 0.0115 | 0.0056 |
| 2024_09_20 22:00 | 3275558 | 5 | 6.4158 | 19.4317 | -114.8802 | 7.0555 | 132.8879 | 0.0121 | 0.0019 |
| 2024_09_20 22:00 | 3218365 | 6 | 6.7732 | 7.7606 | -117.0536 | 17.6357 | 147.8844 | 0.0009 | 0.0116 |
| 2024_09_20 22:00 | 3216190 | 7 | 5.7316 | 14.4081 | -115.6487 | 4.2792 | 28.8277 | 0.0053 | 0.0150 |
| 2024_09_20 22:00 | 3277552 | 8 | 17.2679 | 19.0203 | -115.3908 | 4.4562 | 41.7581 | 0.0064 | 0.0141 |
| 2024_09_20 22:00 | 3215685 | 9 | 11.1672 | 10.0797 | -117.2788 | 3.3734 | 21.8308 | 0.0150 | 0.0091 |
| 2024_09_20 22:00 | 3223345 | 10 | 16.8500 | 15.4222 | -115.2265 | 4.1697 | 56.3312 | 0.0015 | 0.0133 |
| 2024_09_20 22:00 | 3259221 | 11 | 10.2573 | 19.2801 | -117.0175 | 4.5739 | 25.5066 | 0.0065 | 0.0171 |
| 2024_09_20 22:00 | 3265978 | 12 | 10.2424 | 13.4496 | -117.4958 | 4.3026 | 42.4121 | 0.0160 | 0.0195 |
| 2024_09_20 22:00 | 3274747 | 13 | 5.2469 | 16.6584 | -115.2705 | 3.0311 | 48.1773 | 0.0024 | 0.0096 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413172_7B189C55 | 152650 | 188 | -91.8 | 152650 | 366 | -91.7 | 152650 | 282 | -100.3 | 152650 | 28 |
| MR_1774413172_E8C5A338 | 152650 | 188 | -92.4 | 152650 | 366 | -93.7 | 152650 | 282 | -100.1 | 152650 | 28 |
| MR_1774413172_9CB3B7E3 | 152650 | 188 | -89.5 | 152650 | 366 | -92.5 | 152650 | 282 | -102.3 | 152650 | 28 |
| MR_1774413172_201AB041 | 152650 | 188 | -89.6 | 152650 | 366 | -94.2 | 152650 | 282 | -99.8 | 152650 | 28 |
| MR_1774413172_6718381A | 152650 | 188 | -89.9 | 152650 | 366 | -92.9 | 152650 | 282 | -102.2 | 152650 | 28 |
| MR_1774413172_0E04AE1A | 152650 | 188 | -92.2 | 152650 | 366 | -95.5 | 152650 | 282 | -99.4 | 152650 | 28 |
| MR_1774413172_2C2EFC3E | 504990 | 379 | -96.4 | 504990 | 118 | -95.4 | 504990 | 730 | -99.9 | 504990 | 301 |
| MR_1774413172_4179980E | 152650 | 188 | -93.4 | 152650 | 366 | -94.2 | 152650 | 282 | -100.7 | 152650 | 28 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 406: `8c8f264a-075...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8c8f264a-0758-4746-9938-848ad317586e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[406] topology](images/test_0406.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3251215_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251215_2
- `C3`: Decrease transmission power for 3251215_2
- `C4`: Decrease A3 Offset threshold for 3251215_2
- `C5`: Adjust the azimuth of 3268519_3 by 50 degrees
- `C6`: Lift the tilt angle  of 3251215_2 by 7 degrees
- `C7`: Check test server and transmission issues
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268519_3
- `C9`: Press down the tilt angle of 3268519_3 by 10 degrees
- `C10`: Increase A3 Offset threshold for 3251215_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251215_2
- `C12`: Add neighbor relationship between 3279921_4 and 3251215_2
- `C13`: Lift the tilt angle of 3268519_3 by 10 degrees
- `C14`: Decrease A3 Offset threshold for 3268519_3
- `C15`: Increase A3 Offset threshold for 3268519_3
- `C16`: Decrease transmission power for 3268519_3
- `C17`: Adjust the azimuth of 3251215_2 by 50 degrees
- `C18`: Add neighbor relationship between 3268519_3 and 3251215_2
- `C19`: Increase transmission power for 3268519_3
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268519_3
- `C22`: Press down the tilt angle  of 3251215_2 by 7 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.103 | MS1 | 121.4656583573 | 31.1446195303 | 850 | 504990 | -87.14 | 15.17 | 510.25 | 0.11 | 2.74 | 1570 |
| 2024-09-20 22:21:32.998 | MS1 | 121.4656760559 | 31.1446345521 | 850 | 504990 | -87.57 | 15.56 | 455.01 | 0.06 | 2.88 | 1584 |
| 2024-09-20 22:21:33.897 | MS1 | 121.4656638128 | 31.1446350019 | 850 | 504990 | -85.25 | 14.83 | 339.41 | 0.04 | 2.78 | 1569 |
| 2024-09-20 22:21:34.475 | MS1 | 121.4656733396 | 31.1446273832 | 850 | 504990 | -89.85 | 17.38 | 81.76 | 0.14 | 2.10 | 430 |
| 2024-09-20 22:21:35.949 | MS1 | 121.4656748276 | 31.1446273853 | 850 | 504990 | -90.33 | 16.19 | 90.90 | 0.07 | 2.34 | 416 |
| 2024-09-20 22:21:36.406 | MS1 | 121.4656766420 | 31.1446359208 | 850 | 504990 | -89.70 | 14.65 | 56.58 | 0.05 | 2.69 | 397 |
| 2024-09-20 22:21:37.590 | MS1 | 121.4656765768 | 31.1446280383 | 850 | 504990 | -93.25 | 9.65 | 97.23 | 0.09 | 2.25 | 342 |
| 2024-09-20 22:21:38.938 | MS1 | 121.4656643197 | 31.1446250555 | 850 | 504990 | -89.03 | 10.86 | 76.23 | 0.04 | 2.43 | 448 |
| 2024-09-20 22:21:39.636 | MS1 | 121.4656631295 | 31.1446187752 | 850 | 504990 | -90.18 | 11.46 | 72.96 | 0.14 | 2.20 | 478 |
| 2024-09-20 22:21:40.892 | MS1 | 121.4656663649 | 31.1446347821 | 850 | 504990 | -93.77 | 12.19 | 471.48 | 0.02 | 2.01 | 1588 |
| 2024-09-20 22:21:41.739 | MS1 | 121.4656737833 | 31.1446222208 | 850 | 504990 | -91.30 | 7.61 | 512.58 | 0.08 | 2.36 | 1569 |
| 2024-09-20 22:21:42.299 | MS1 | 121.4656594046 | 31.1446293161 | 850 | 504990 | -90.67 | 7.34 | 356.86 | 0.06 | 2.50 | 1595 |

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
| 3226130 | 1 | 121.4700762799 | 31.1477790181 | 273 | 0 | 1 | 33.2 | TDD | 640 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3251215 | 2 | 121.4736152343 | 31.1529567386 | 35 | 5 | 2 | 32.2 | TDD | 209 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3268519 | 3 | 121.4727267264 | 31.1450872489 | 336 | 15 | 8 | 32.3 | TDD | 850 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3279921 | 4 | 121.4743961455 | 31.1557904617 | 213 | 2 | 7 | 39.3 | TDD | 263 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.151 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.171 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.288 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.288 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.049 | NREventA3 | measId:2;ServCellPCI:589;Se... |
| 2024-09-20 22:21:38.289 | NRHandoverAttempt | SourcePCI:589;SourceNR-ARFC... |
| 2024-09-20 22:21:38.332 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.345 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.450 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.450 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226130 | 1 | 15.0818 | 7.0525 | -114.9293 | 6.3037 | 115.0458 | 0.0141 | 0.0109 |
| 2024_09_20 22:00 | 3251215 | 2 | 10.6746 | 16.2726 | -116.3792 | 10.2938 | 185.5367 | 0.0174 | 0.0030 |
| 2024_09_20 22:00 | 3268519 | 3 | 11.7604 | 11.6875 | -117.6407 | 7.2937 | 130.2809 | 0.0105 | 0.0063 |
| 2024_09_20 22:00 | 3279921 | 4 | 11.9809 | 15.7781 | -116.0662 | 5.5130 | 96.5688 | 0.0110 | 0.0065 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414287_B8AFF771 | 504990 | 850 | -88.9 | 504990 | 209 | -92.6 | 504990 | 263 | -95.2 | 504990 | 640 |
| MR_1774414287_94A574C9 | 504990 | 850 | -91.4 | 504990 | 209 | -94.5 | 504990 | 263 | -95.2 | 504990 | 640 |
| MR_1774414287_BE90A42B | 504990 | 850 | -89.5 | 504990 | 209 | -93.8 | 504990 | 263 | -95.9 | 504990 | 640 |
| MR_1774414287_48999939 | 504990 | 850 | -89.4 | 504990 | 209 | -94.6 | 504990 | 263 | -97.4 | 504990 | 640 |
| MR_1774414287_CD68618E | 504990 | 850 | -90.7 | 504990 | 209 | -95.0 | 504990 | 263 | -96.1 | 504990 | 640 |
| MR_1774414287_80D220FF | 504990 | 850 | -89.5 | 504990 | 209 | -95.6 | 504990 | 263 | -96.6 | 504990 | 640 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 407: `78bd577f-2c2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `78bd577f-2c2b-48e5-91ab-ca6d74bd4c04` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[407] topology](images/test_0407.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3223436_3
- `C2`: Adjust the azimuth of 3223436_3 by 16 degrees
- `C3`: Add neighbor relationship between 3235923_4 and 3223436_3
- `C4`: Increase A3 Offset threshold for 3223436_3
- `C5`: Increase transmission power for 3256963_2
- `C6`: Lift the tilt angle of 3256963_2 by 2 degrees
- `C7`: Add neighbor relationship between 3256963_2 and 3223436_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256963_2
- `C9`: Decrease transmission power for 3256963_2
- `C10`: Increase A3 Offset threshold for 3256963_2
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Check test server and transmission issues
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223436_3
- `C14`: Press down the tilt angle of 3256963_2 by 2 degrees
- `C15`: Decrease A3 Offset threshold for 3223436_3
- `C16`: Lift the tilt angle  of 3223436_3 by 5 degrees
- `C17`: Adjust the azimuth of 3256963_2 by 28 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223436_3
- `C19`: Press down the tilt angle  of 3223436_3 by 5 degrees
- `C20`: Decrease transmission power for 3223436_3
- `C21`: Decrease A3 Offset threshold for 3256963_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256963_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.452 | MS1 | 121.4656641892 | 31.1446358960 | 394 | 504990 | -78.83 | 14.17 | 540.91 | 0.14 | 2.89 | 1569 |
| 2024-09-20 22:21:32.201 | MS1 | 121.4656714920 | 31.1446240721 | 394 | 504990 | -76.29 | 14.49 | 316.40 | 0.08 | 2.27 | 1580 |
| 2024-09-20 22:21:33.495 | MS1 | 121.4656753020 | 31.1446370663 | 394 | 504990 | -76.49 | 12.50 | 504.88 | 0.06 | 2.96 | 1584 |
| 2024-09-20 22:21:34.465 | MS1 | 121.4656653457 | 31.1446269841 | 857 | 504990 | -83.11 | 3.00 | 46.58 | 0.12 | 1.45 | 1561 |
| 2024-09-20 22:21:35.422 | MS1 | 121.4656761936 | 31.1446347510 | 857 | 504990 | -85.47 | 4.69 | 58.96 | 0.20 | 1.26 | 1598 |
| 2024-09-20 22:21:36.581 | MS1 | 121.4656648011 | 31.1446321253 | 394 | 504990 | -83.75 | 3.33 | 68.31 | 0.06 | 1.08 | 1579 |
| 2024-09-20 22:21:37.735 | MS1 | 121.4656762641 | 31.1446226724 | 394 | 504990 | -87.86 | 3.18 | 60.51 | 0.00 | 1.29 | 1576 |
| 2024-09-20 22:21:38.795 | MS1 | 121.4656771561 | 31.1446185954 | 857 | 504990 | -85.39 | 2.50 | 55.33 | 0.01 | 1.03 | 1583 |
| 2024-09-20 22:21:39.560 | MS1 | 121.4656677130 | 31.1446374379 | 857 | 504990 | -84.47 | 1.49 | 55.41 | 0.08 | 1.21 | 1568 |
| 2024-09-20 22:21:40.569 | MS1 | 121.4656701083 | 31.1446233062 | 857 | 504990 | -76.44 | 16.18 | 546.97 | 0.00 | 2.37 | 1563 |
| 2024-09-20 22:21:41.989 | MS1 | 121.4656746617 | 31.1446309907 | 857 | 504990 | -78.29 | 12.48 | 550.51 | 0.07 | 2.66 | 1575 |
| 2024-09-20 22:21:42.704 | MS1 | 121.4656712442 | 31.1446322405 | 857 | 504990 | -84.50 | 16.31 | 518.94 | 0.08 | 2.65 | 1590 |

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
| 3214713 | 1 | 121.4718965068 | 31.1523354304 | 330 | 1 | 3 | 19.9 | TDD | 9 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3223436 | 3 | 121.4726005217 | 31.1543193983 | 195 | 3 | 12 | 39.3 | TDD | 330 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3235923 | 4 | 121.4662479047 | 31.1506421414 | 19 | 11 | 9 | 24.0 | TDD | 496 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3256963 | 2 | 121.4652313621 | 31.1526565649 | 205 | 0 | 4 | 35.2 | TDD | 394 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3264384 | 5 | 121.4715329183 | 31.1471078219 | 75 | 10 | 10 | 32.0 | TDD | 857 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.305 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.425 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.425 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.159 | NREventA3 | measId:2;ServCellPCI:410;Se... |
| 2024-09-20 22:21:34.399 | NRHandoverAttempt | SourcePCI:410;SourceNR-ARFC... |
| 2024-09-20 22:21:34.433 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.444 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:34.593 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.593 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.159 | NREventA3 | measId:2;ServCellPCI:1;Serv... |
| 2024-09-20 22:21:36.399 | NRHandoverAttempt | SourcePCI:1;SourceNR-ARFCN:... |
| 2024-09-20 22:21:36.439 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.449 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:36.550 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.550 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.159 | NREventA3 | measId:2;ServCellPCI:410;Se... |
| 2024-09-20 22:21:38.399 | NRHandoverAttempt | SourcePCI:410;SourceNR-ARFC... |
| 2024-09-20 22:21:38.440 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.451 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.553 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.553 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214713 | 1 | 16.7015 | 13.7025 | -114.4279 | 16.8165 | 131.1397 | 0.0155 | 0.0097 |
| 2024_09_20 22:00 | 3256963 | 2 | 18.8122 | 18.1024 | -114.6615 | 8.0834 | 118.3084 | 0.0179 | 0.0039 |
| 2024_09_20 22:00 | 3223436 | 3 | 6.7334 | 10.1685 | -117.2637 | 9.4971 | 161.5304 | 0.0200 | 0.0154 |
| 2024_09_20 22:00 | 3235923 | 4 | 10.2542 | 11.4647 | -114.8192 | 19.7578 | 94.6217 | 0.0112 | 0.0155 |
| 2024_09_20 22:00 | 3264384 | 5 | 8.6578 | 13.8191 | -117.8306 | 16.9716 | 187.4732 | 0.0164 | 0.0127 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414346_88AFBF6D | 504990 | 394 | -84.8 | 504990 | 857 | -79.1 | 504990 | 330 | -83.0 | 504990 | 496 |
| MR_1774414346_AFDA9AEE | 504990 | 857 | -84.9 | 504990 | 394 | -81.8 | 504990 | 330 | -83.0 | 504990 | 496 |
| MR_1774414346_1925388B | 504990 | 857 | -84.2 | 504990 | 394 | -80.8 | 504990 | 330 | -79.6 | 504990 | 496 |
| MR_1774414346_E2C2CFFE | 504990 | 857 | -83.6 | 504990 | 394 | -81.7 | 504990 | 330 | -80.2 | 504990 | 496 |
| MR_1774414346_CC245E6E | 504990 | 857 | -83.7 | 504990 | 394 | -81.8 | 504990 | 330 | -83.3 | 504990 | 496 |
| MR_1774414346_58A9988A | 504990 | 857 | -84.6 | 504990 | 394 | -81.4 | 504990 | 330 | -80.5 | 504990 | 496 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 408: `85bc95aa-f02...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `85bc95aa-f021-4620-b8f1-005aed19bc15` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[408] topology](images/test_0408.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3257202_6
- `C2`: Increase A3 Offset threshold for 3257202_6
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257202_6
- `C4`: Adjust the azimuth of 3248083_5 by 26 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease A3 Offset threshold for 3248083_5
- `C7`: Lift the tilt angle  of 3257202_6 by 5 degrees
- `C8`: Decrease transmission power for 3257202_6
- `C9`: Increase transmission power for 3257202_6
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248083_5
- `C11`: Add neighbor relationship between 3216697_7 and 3257202_6
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257202_6
- `C13`: Add neighbor relationship between 3248083_5 and 3257202_6
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248083_5
- `C15`: Lift the tilt angle of 3248083_5 by 4 degrees
- `C16`: Press down the tilt angle of 3248083_5 by 4 degrees
- `C17`: Increase transmission power for 3248083_5
- `C18`: Decrease transmission power for 3248083_5
- `C19`: Adjust the azimuth of 3257202_6 by 36 degrees
- `C20`: Check test server and transmission issues
- `C21`: Press down the tilt angle  of 3257202_6 by 5 degrees
- `C22`: Increase A3 Offset threshold for 3248083_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.970 | MS1 | 121.4656600262 | 31.1446201671 | 316 | 504990 | -95.35 | 12.95 | 470.15 | 0.18 | 2.23 | 1587 |
| 2024-09-20 22:21:32.484 | MS1 | 121.4656595941 | 31.1446239847 | 698 | 504990 | -94.39 | 11.39 | 419.39 | 0.08 | 2.13 | 1576 |
| 2024-09-20 22:21:33.843 | MS1 | 121.4656713777 | 31.1446336770 | 454 | 504990 | -94.65 | 13.04 | 546.17 | 0.05 | 2.35 | 1571 |
| 2024-09-20 22:21:34.913 | MS1 | 121.4656712352 | 31.1446218651 | 212 | 152650 | -91.73 | 2.20 | 86.18 | 0.18 | 1.67 | 937 |
| 2024-09-20 22:21:35.366 | MS1 | 121.4656734933 | 31.1446223586 | 738 | 152650 | -93.61 | 5.74 | 80.99 | 0.03 | 1.79 | 935 |
| 2024-09-20 22:21:36.505 | MS1 | 121.4656691057 | 31.1446210999 | 480 | 152650 | -87.01 | 3.42 | 89.54 | 0.13 | 1.95 | 901 |
| 2024-09-20 22:21:37.423 | MS1 | 121.4656609064 | 31.1446330577 | 757 | 152650 | -94.69 | 5.89 | 74.35 | 0.08 | 1.74 | 993 |
| 2024-09-20 22:21:38.309 | MS1 | 121.4656688859 | 31.1446335097 | 212 | 152650 | -89.51 | 2.94 | 95.04 | 0.13 | 1.67 | 990 |
| 2024-09-20 22:21:39.420 | MS1 | 121.4656671906 | 31.1446223552 | 738 | 152650 | -89.38 | 4.48 | 50.42 | 0.02 | 1.68 | 996 |
| 2024-09-20 22:21:40.159 | MS1 | 121.4656757985 | 31.1446181792 | 480 | 152650 | -90.89 | 2.74 | 90.12 | 0.05 | 2.43 | 1599 |
| 2024-09-20 22:21:41.843 | MS1 | 121.4656733696 | 31.1446312401 | 757 | 152650 | -95.51 | 5.03 | 79.56 | 0.05 | 2.88 | 1574 |
| 2024-09-20 22:21:42.195 | MS1 | 121.4656585474 | 31.1446259818 | 212 | 152650 | -91.52 | 5.99 | 56.34 | 0.17 | 2.02 | 1589 |

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
| 3216697 | 7 | 121.4720214484 | 31.1507801850 | 113 | 1 | 8 | 10.0 | FDD | 480 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3221140 | 4 | 121.4712728746 | 31.1498823215 | 16 | 8 | 12 | 6.9 | TDD | 698 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3230066 | 13 | 121.4669589549 | 31.1490080026 | 316 | 7 | 5 | 8.8 | FDD | 823 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3236056 | 2 | 121.4641078368 | 31.1442184464 | 96 | 13 | 4 | 26.0 | TDD | 617 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3236724 | 12 | 121.4644501379 | 31.1471568641 | 86 | 13 | 12 | 8.0 | FDD | 564 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3238527 | 11 | 121.4724750138 | 31.1491528858 | 237 | 2 | 12 | 10.7 | FDD | 757 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3248083 | 5 | 121.4716546403 | 31.1503833515 | 248 | 3 | 8 | 9.1 | TDD | 316 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3250731 | 8 | 121.4643964188 | 31.1487908967 | 63 | 10 | 1 | 19.2 | FDD | 738 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3257142 | 9 | 121.4670848394 | 31.1446725544 | 35 | 14 | 4 | 18.1 | FDD | 722 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3257202 | 6 | 121.4669754378 | 31.1485279744 | 160 | 2 | 11 | 20.6 | TDD | 862 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3259650 | 1 | 121.4739967822 | 31.1482276081 | 10 | 0 | 3 | 23.4 | TDD | 454 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3265365 | 10 | 121.4688805482 | 31.1545870716 | 277 | 7 | 10 | 8.7 | FDD | 212 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3273101 | 3 | 121.4713829772 | 31.1553260928 | 331 | 4 | 1 | 12.1 | TDD | 953 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.138 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.258 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.258 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.002 | NREventA2 | measId:1;ServCellPCI:355;Se... |
| 2024-09-20 22:21:35.148 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.386 | NREventA5 | measId:3;ServCellPCI:355;Se... |
| 2024-09-20 22:21:35.464 | NRHandoverAttempt | SourcePCI:355;SourceNR-ARFC... |
| 2024-09-20 22:21:35.513 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.527 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.652 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.652 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259650 | 1 | 10.1984 | 8.9171 | -114.5633 | 8.5476 | 137.7142 | 0.0144 | 0.0162 |
| 2024_09_20 22:00 | 3236056 | 2 | 10.4891 | 10.4686 | -115.3282 | 15.3258 | 131.2785 | 0.0008 | 0.0163 |
| 2024_09_20 22:00 | 3273101 | 3 | 11.3853 | 6.0439 | -117.9383 | 9.2687 | 183.0443 | 0.0013 | 0.0106 |
| 2024_09_20 22:00 | 3221140 | 4 | 8.2032 | 7.9845 | -115.0836 | 11.3038 | 179.7632 | 0.0142 | 0.0197 |
| 2024_09_20 22:00 | 3248083 | 5 | 17.2506 | 18.0158 | -114.1487 | 19.0088 | 189.7464 | 0.0171 | 0.0131 |
| 2024_09_20 22:00 | 3257202 | 6 | 9.0291 | 13.5037 | -115.2430 | 6.5134 | 92.5822 | 0.0135 | 0.0181 |
| 2024_09_20 22:00 | 3216697 | 7 | 11.1516 | 7.3461 | -115.1057 | 4.4051 | 26.7479 | 0.0158 | 0.0038 |
| 2024_09_20 22:00 | 3250731 | 8 | 19.2153 | 14.8173 | -114.2709 | 3.7901 | 45.8581 | 0.0192 | 0.0156 |
| 2024_09_20 22:00 | 3257142 | 9 | 13.6765 | 13.1963 | -115.4436 | 3.9677 | 34.9728 | 0.0133 | 0.0138 |
| 2024_09_20 22:00 | 3265365 | 10 | 12.5423 | 12.0439 | -114.4513 | 4.8008 | 58.4735 | 0.0113 | 0.0021 |
| 2024_09_20 22:00 | 3238527 | 11 | 10.9531 | 6.7682 | -114.1195 | 4.7968 | 59.5570 | 0.0030 | 0.0058 |
| 2024_09_20 22:00 | 3236724 | 12 | 14.5202 | 5.2171 | -117.7279 | 3.9673 | 42.6818 | 0.0180 | 0.0132 |
| 2024_09_20 22:00 | 3230066 | 13 | 11.6368 | 19.7140 | -114.1499 | 4.2877 | 23.4641 | 0.0035 | 0.0076 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412508_DBF020E3 | 152650 | 212 | -93.5 | 152650 | 722 | -100.5 | 152650 | 564 | -98.4 | 152650 | 823 |
| MR_1774412508_7EEC44F8 | 504990 | 454 | -94.6 | 504990 | 862 | -91.5 | 504990 | 953 | -95.1 | 504990 | 617 |
| MR_1774412508_BDDA17DF | 504990 | 454 | -94.7 | 504990 | 862 | -91.4 | 504990 | 953 | -96.0 | 504990 | 617 |
| MR_1774412508_19D43E1F | 152650 | 212 | -92.3 | 152650 | 722 | -101.3 | 152650 | 564 | -99.4 | 152650 | 823 |
| MR_1774412508_0564384E | 152650 | 212 | -93.7 | 152650 | 722 | -99.6 | 152650 | 564 | -101.1 | 152650 | 823 |
| MR_1774412508_FE413236 | 152650 | 212 | -90.3 | 152650 | 722 | -101.5 | 152650 | 564 | -97.9 | 152650 | 823 |
| MR_1774412508_96FF9D87 | 152650 | 212 | -90.7 | 152650 | 722 | -98.6 | 152650 | 564 | -101.2 | 152650 | 823 |
| MR_1774412508_0EA803E1 | 504990 | 454 | -96.5 | 504990 | 862 | -90.9 | 504990 | 953 | -92.9 | 504990 | 617 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 409: `55e4900f-dc8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `55e4900f-dc88-420d-9428-d84fc9229deb` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[409] topology](images/test_0409.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3244317_2 and 3251732_1
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Check test server and transmission issues
- `C4`: Decrease A3 Offset threshold for 3251732_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244317_2
- `C6`: Decrease transmission power for 3244317_2
- `C7`: Increase transmission power for 3251732_1
- `C8`: Decrease transmission power for 3251732_1
- `C9`: Increase A3 Offset threshold for 3251732_1
- `C10`: Press down the tilt angle  of 3251732_1 by 5 degrees
- `C11`: Lift the tilt angle of 3244317_2 by 9 degrees
- `C12`: Adjust the azimuth of 3244317_2 by 50 degrees
- `C13`: Increase A3 Offset threshold for 3244317_2
- `C14`: Decrease A3 Offset threshold for 3244317_2
- `C15`: Press down the tilt angle of 3244317_2 by 9 degrees
- `C16`: Lift the tilt angle  of 3251732_1 by 5 degrees
- `C17`: Add neighbor relationship between 3261298_4 and 3251732_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251732_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251732_1
- `C20`: Adjust the azimuth of 3251732_1 by 48 degrees
- `C21`: Increase transmission power for 3244317_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244317_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.368 | MS1 | 121.4656642168 | 31.1446190385 | 545 | 504990 | -85.66 | 15.29 | 453.11 | 0.17 | 2.70 | 1564 |
| 2024-09-20 22:21:32.319 | MS1 | 121.4656689660 | 31.1446294312 | 545 | 504990 | -85.55 | 15.19 | 558.87 | 0.05 | 2.47 | 1590 |
| 2024-09-20 22:21:33.622 | MS1 | 121.4656688729 | 31.1446362156 | 545 | 504990 | -89.54 | 15.53 | 407.55 | 0.05 | 2.33 | 1597 |
| 2024-09-20 22:21:34.915 | MS1 | 121.4656581765 | 31.1446249052 | 545 | 504990 | -89.33 | 16.34 | 66.10 | 0.18 | 2.99 | 499 |
| 2024-09-20 22:21:35.920 | MS1 | 121.4656706104 | 31.1446285277 | 545 | 504990 | -85.63 | 16.24 | 102.47 | 0.00 | 2.44 | 453 |
| 2024-09-20 22:21:36.912 | MS1 | 121.4656677871 | 31.1446268640 | 545 | 504990 | -87.12 | 14.94 | 59.74 | 0.04 | 2.81 | 365 |
| 2024-09-20 22:21:37.832 | MS1 | 121.4656766300 | 31.1446185466 | 545 | 504990 | -90.70 | 7.26 | 97.14 | 0.05 | 2.31 | 300 |
| 2024-09-20 22:21:38.572 | MS1 | 121.4656742268 | 31.1446312080 | 545 | 504990 | -91.36 | 11.42 | 67.31 | 0.05 | 2.70 | 430 |
| 2024-09-20 22:21:39.944 | MS1 | 121.4656601295 | 31.1446253734 | 545 | 504990 | -91.52 | 10.11 | 58.99 | 0.03 | 2.53 | 382 |
| 2024-09-20 22:21:40.134 | MS1 | 121.4656729725 | 31.1446266894 | 545 | 504990 | -89.48 | 9.10 | 590.54 | 0.08 | 2.54 | 1584 |
| 2024-09-20 22:21:41.455 | MS1 | 121.4656640920 | 31.1446317725 | 545 | 504990 | -91.76 | 8.79 | 414.56 | 0.20 | 2.58 | 1593 |
| 2024-09-20 22:21:42.669 | MS1 | 121.4656675569 | 31.1446221569 | 545 | 504990 | -91.16 | 12.72 | 495.05 | 0.13 | 2.23 | 1585 |

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
| 3244317 | 2 | 121.4659011196 | 31.1499413332 | 292 | 5 | 5 | 43.3 | TDD | 545 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3251732 | 1 | 121.4650238223 | 31.1508963618 | 223 | 2 | 1 | 35.0 | TDD | 784 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3254112 | 3 | 121.4700299259 | 31.1542291076 | 54 | 9 | 0 | 23.7 | TDD | 883 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3261298 | 4 | 121.4678182370 | 31.1535873893 | 177 | 4 | 7 | 18.4 | TDD | 257 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.051 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.066 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.181 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.181 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.864 | NREventA3 | measId:2;ServCellPCI:977;Se... |
| 2024-09-20 22:21:38.104 | NRHandoverAttempt | SourcePCI:977;SourceNR-ARFC... |
| 2024-09-20 22:21:38.134 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.144 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.244 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.244 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251732 | 1 | 12.0085 | 9.9688 | -114.4822 | 8.0584 | 90.4510 | 0.0147 | 0.0082 |
| 2024_09_20 22:00 | 3244317 | 2 | 12.5465 | 17.7660 | -117.4068 | 16.2517 | 153.0493 | 0.0157 | 0.0175 |
| 2024_09_20 22:00 | 3254112 | 3 | 17.9756 | 8.8715 | -115.4775 | 12.2695 | 120.0090 | 0.0087 | 0.0023 |
| 2024_09_20 22:00 | 3261298 | 4 | 11.4723 | 16.5815 | -115.0179 | 8.3492 | 173.0641 | 0.0088 | 0.0047 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416548_49461FAE | 504990 | 545 | -89.6 | 504990 | 784 | -95.5 | 504990 | 257 | -96.4 | 504990 | 883 |
| MR_1774416548_E5806F58 | 504990 | 545 | -89.4 | 504990 | 784 | -94.5 | 504990 | 257 | -98.5 | 504990 | 883 |
| MR_1774416548_8E624FAC | 504990 | 545 | -91.0 | 504990 | 784 | -96.9 | 504990 | 257 | -98.1 | 504990 | 883 |
| MR_1774416548_B4D75C4C | 504990 | 545 | -89.4 | 504990 | 784 | -95.0 | 504990 | 257 | -98.4 | 504990 | 883 |
| MR_1774416548_763F9ADB | 504990 | 545 | -87.4 | 504990 | 784 | -94.9 | 504990 | 257 | -97.2 | 504990 | 883 |
| MR_1774416548_2A744705 | 504990 | 545 | -90.5 | 504990 | 784 | -93.8 | 504990 | 257 | -98.1 | 504990 | 883 |
| MR_1774416548_C3436A56 | 504990 | 545 | -89.4 | 504990 | 784 | -94.3 | 504990 | 257 | -96.3 | 504990 | 883 |
| MR_1774416548_5AD8CA32 | 504990 | 545 | -89.7 | 504990 | 784 | -96.2 | 504990 | 257 | -98.9 | 504990 | 883 |

> *... 2개 열 생략 (전체 14열)*

---
