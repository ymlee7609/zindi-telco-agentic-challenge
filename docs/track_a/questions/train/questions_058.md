# Track A 문제 분석 — train[570]~train[579]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[570] ~ train[579] (10개)

## 목차

1. [문제 570: `ea864a2a-e00...`](#570) — single-answer, 정답: C9
2. [문제 571: `bf76e556-b0f...`](#571) — single-answer, 정답: C9
3. [문제 572: `1dd34985-92b...`](#572) — single-answer, 정답: C9
4. [문제 573: `408bc32e-c7d...`](#573) — multiple-answer, 정답: C1|C8
5. [문제 574: `d655fe62-9cf...`](#574) — single-answer, 정답: C7
6. [문제 575: `b3cbf190-ca0...`](#575) — single-answer, 정답: C5
7. [문제 576: `e1b838c8-0ed...`](#576) — single-answer, 정답: C19
8. [문제 577: `33ec70a1-1bf...`](#577) — single-answer, 정답: C22
9. [문제 578: `6ecacd1b-e58...`](#578) — single-answer, 정답: C12
10. [문제 579: `42a45488-8ae...`](#579) — single-answer, 정답: C10

---

### 문제 570: `ea864a2a-e00...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ea864a2a-e00b-4a4d-9f5b-69ed993e94ea` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[570] topology](images/train_0570.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3232538_2
- `C2`: Increase transmission power for 3268628_4
- `C3`: Add neighbor relationship between 3270663_3 and 3232538_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232538_2
- `C5`: Press down the tilt angle of 3268628_4 by 10 degrees
- `C6`: Press down the tilt angle  of 3232538_2 by 10 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268628_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232538_2
- `C9`: Insufficient data; more data is needed for judgment. **← 정답**
- `C10`: Lift the tilt angle  of 3232538_2 by 10 degrees
- `C11`: Lift the tilt angle of 3268628_4 by 10 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268628_4
- `C13`: Add neighbor relationship between 3268628_4 and 3232538_2
- `C14`: Adjust the azimuth of 3268628_4 by 14 degrees
- `C15`: Decrease transmission power for 3232538_2
- `C16`: Check test server and transmission issues
- `C17`: Decrease transmission power for 3268628_4
- `C18`: Increase A3 Offset threshold for 3268628_4
- `C19`: Decrease A3 Offset threshold for 3268628_4
- `C20`: Decrease A3 Offset threshold for 3232538_2
- `C21`: Increase A3 Offset threshold for 3232538_2
- `C22`: Adjust the azimuth of 3232538_2 by 25 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.168 | MS1 | 121.4656632646 | 31.1446183842 | 831 | 504990 | -90.61 | 15.03 | 406.34 | 0.08 | 2.97 | 1565 |
| 2024-09-20 22:21:32.501 | MS1 | 121.4656680683 | 31.1446202744 | 831 | 504990 | -86.69 | 14.99 | 361.49 | 0.17 | 2.40 | 1561 |
| 2024-09-20 22:21:33.650 | MS1 | 121.4656653567 | 31.1446253817 | 831 | 504990 | -90.00 | 17.64 | 363.49 | 0.08 | 2.18 | 1595 |
| 2024-09-20 22:21:34.419 | MS1 | 121.4656585572 | 31.1446206176 | 831 | 504990 | -86.45 | 12.44 | 104.61 | 0.17 | 2.41 | 1596 |
| 2024-09-20 22:21:35.176 | MS1 | 121.4656612722 | 31.1446267258 | 831 | 504990 | -86.50 | 17.40 | 82.78 | 0.20 | 2.34 | 1598 |
| 2024-09-20 22:21:36.607 | MS1 | 121.4656593832 | 31.1446217272 | 831 | 504990 | -91.85 | 16.16 | 67.82 | 0.12 | 2.90 | 1575 |
| 2024-09-20 22:21:37.111 | MS1 | 121.4656654440 | 31.1446202886 | 831 | 504990 | -90.58 | 8.72 | 100.09 | 0.02 | 2.22 | 1580 |
| 2024-09-20 22:21:38.332 | MS1 | 121.4656636487 | 31.1446358135 | 831 | 504990 | -93.03 | 7.83 | 56.94 | 0.08 | 2.13 | 1587 |
| 2024-09-20 22:21:39.115 | MS1 | 121.4656602494 | 31.1446206301 | 831 | 504990 | -91.31 | 7.65 | 89.36 | 0.15 | 2.17 | 1580 |
| 2024-09-20 22:21:40.377 | MS1 | 121.4656773735 | 31.1446186721 | 831 | 504990 | -89.44 | 8.67 | 548.39 | 0.02 | 2.71 | 1586 |
| 2024-09-20 22:21:41.923 | MS1 | 121.4656658299 | 31.1446374700 | 831 | 504990 | -91.45 | 8.37 | 433.19 | 0.12 | 2.93 | 1589 |
| 2024-09-20 22:21:42.558 | MS1 | 121.4656694219 | 31.1446355149 | 831 | 504990 | -91.88 | 8.80 | 552.81 | 0.19 | 2.74 | 1579 |

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
| 3210180 | 1 | 121.4641240862 | 31.1449431797 | 258 | 14 | 1 | 19.8 | TDD | 449 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3232538 | 2 | 121.4655328915 | 31.1482884206 | 153 | 14 | 12 | 19.1 | TDD | 891 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3268628 | 4 | 121.4687823218 | 31.1450827588 | 274 | 11 | 7 | 15.5 | TDD | 831 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3270663 | 3 | 121.4641630223 | 31.1487206088 | 347 | 2 | 1 | 33.4 | TDD | 54 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.010 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.027 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.166 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.166 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.815 | NREventA3 | measId:2;ServCellPCI:149;Se... |
| 2024-09-20 22:21:38.055 | NRHandoverAttempt | SourcePCI:149;SourceNR-ARFC... |
| 2024-09-20 22:21:38.085 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.097 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.229 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.229 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3210180 | 1 | 88.1633 | 80.2267 | -116.0093 | 18.5525 | 194.3100 | 0.0147 | 0.0038 |
| 2024_09_19 22:00 | 3232538 | 2 | 90.7438 | 83.8531 | -117.8825 | 16.8845 | 98.2184 | 0.0117 | 0.0128 |
| 2024_09_19 22:00 | 3270663 | 3 | 90.5564 | 79.9566 | -115.1065 | 14.6998 | 141.1469 | 0.0175 | 0.0120 |
| 2024_09_19 22:00 | 3268628 | 4 | 77.2922 | 80.9080 | -117.6301 | 7.7917 | 175.5993 | 0.0112 | 0.0190 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412309_804D1442 | 504990 | 831 | -87.1 | 504990 | 891 | -96.5 | 504990 | 54 | -97.6 | 504990 | 449 |
| MR_1774412309_1A1C6D44 | 504990 | 831 | -85.6 | 504990 | 891 | -94.2 | 504990 | 54 | -96.4 | 504990 | 449 |
| MR_1774412309_A571C2B7 | 504990 | 831 | -86.3 | 504990 | 891 | -96.1 | 504990 | 54 | -99.3 | 504990 | 449 |
| MR_1774412309_04FF33BB | 504990 | 831 | -85.0 | 504990 | 891 | -95.8 | 504990 | 54 | -96.9 | 504990 | 449 |
| MR_1774412309_56DE04B0 | 504990 | 831 | -86.4 | 504990 | 891 | -97.3 | 504990 | 54 | -98.3 | 504990 | 449 |
| MR_1774412309_97D6A59E | 504990 | 831 | -87.2 | 504990 | 891 | -97.1 | 504990 | 54 | -98.1 | 504990 | 449 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 571: `bf76e556-b0f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bf76e556-b0f3-4d63-970d-728bbf68cdb1` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3252948_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[571] topology](images/train_0571.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3252948_2 by 4 degrees
- `C2`: Adjust the azimuth of 3272779_4 by 50 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272779_4
- `C4`: Decrease transmission power for 3252948_2
- `C5`: Lift the tilt angle of 3252948_2 by 4 degrees
- `C6`: Increase A3 Offset threshold for 3252948_2
- `C7`: Decrease transmission power for 3272779_4
- `C8`: Increase transmission power for 3252948_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252948_2 **← 정답**
- `C10`: Check test server and transmission issues
- `C11`: Add neighbor relationship between 3267846_3 and 3272779_4
- `C12`: Decrease A3 Offset threshold for 3252948_2
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Add neighbor relationship between 3252948_2 and 3272779_4
- `C15`: Press down the tilt angle  of 3272779_4 by 10 degrees
- `C16`: Increase transmission power for 3272779_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272779_4
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252948_2
- `C19`: Increase A3 Offset threshold for 3272779_4
- `C20`: Decrease A3 Offset threshold for 3272779_4
- `C21`: Adjust the azimuth of 3252948_2 by 2 degrees
- `C22`: Lift the tilt angle  of 3272779_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.663 | MS1 | 121.4656586399 | 31.1446285736 | 139 | 504990 | -87.46 | 13.65 | 404.89 | 0.10 | 2.47 | 1570 |
| 2024-09-20 22:21:32.812 | MS1 | 121.4656616922 | 31.1446252679 | 139 | 504990 | -89.97 | 14.81 | 412.32 | 0.18 | 2.80 | 1567 |
| 2024-09-20 22:21:33.133 | MS1 | 121.4656777496 | 31.1446265355 | 139 | 504990 | -88.93 | 17.92 | 374.50 | 0.09 | 2.10 | 1568 |
| 2024-09-20 22:21:34.782 | MS1 | 121.4656677872 | 31.1446374099 | 139 | 504990 | -89.88 | 14.95 | 74.00 | 0.68 | 2.09 | 664 |
| 2024-09-20 22:21:35.933 | MS1 | 121.4656611741 | 31.1446337822 | 139 | 504990 | -87.81 | 16.23 | 53.89 | 0.56 | 2.12 | 501 |
| 2024-09-20 22:21:36.825 | MS1 | 121.4656761547 | 31.1446248984 | 139 | 504990 | -88.43 | 13.42 | 55.87 | 0.66 | 2.92 | 549 |
| 2024-09-20 22:21:37.392 | MS1 | 121.4656739882 | 31.1446326076 | 139 | 504990 | -90.75 | 8.19 | 68.01 | 0.62 | 2.53 | 675 |
| 2024-09-20 22:21:38.357 | MS1 | 121.4656605674 | 31.1446372969 | 139 | 504990 | -91.82 | 11.73 | 72.41 | 0.65 | 2.49 | 641 |
| 2024-09-20 22:21:39.838 | MS1 | 121.4656736919 | 31.1446217574 | 139 | 504990 | -91.20 | 9.00 | 68.79 | 0.69 | 2.02 | 578 |
| 2024-09-20 22:21:40.285 | MS1 | 121.4656746987 | 31.1446300458 | 139 | 504990 | -92.20 | 8.84 | 517.41 | 0.13 | 2.26 | 1590 |
| 2024-09-20 22:21:41.190 | MS1 | 121.4656676080 | 31.1446244252 | 139 | 504990 | -89.94 | 12.21 | 603.80 | 0.11 | 2.07 | 1592 |
| 2024-09-20 22:21:42.395 | MS1 | 121.4656741255 | 31.1446331020 | 139 | 504990 | -91.87 | 12.81 | 318.88 | 0.02 | 2.02 | 1594 |

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
| 3240066 | 1 | 121.4642927804 | 31.1512565562 | 60 | 3 | 2 | 18.1 | TDD | 969 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3252948 | 2 | 121.4731381880 | 31.1447147170 | 267 | 1 | 3 | 35.1 | TDD | 139 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3267846 | 3 | 121.4732668068 | 31.1455130711 | 173 | 6 | 6 | 36.5 | TDD | 294 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3272779 | 4 | 121.4643957191 | 31.1526113753 | 309 | 13 | 4 | 38.5 | TDD | 798 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.176 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.197 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.319 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.319 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.049 | NREventA3 | measId:2;ServCellPCI:304;Se... |
| 2024-09-20 22:21:38.289 | NRHandoverAttempt | SourcePCI:304;SourceNR-ARFC... |
| 2024-09-20 22:21:38.329 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.344 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.479 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.479 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240066 | 1 | 10.3384 | 6.5469 | -114.4974 | 8.9303 | 143.7738 | 0.0190 | 0.0186 |
| 2024_09_20 22:00 | 3252948 | 2 | 16.5090 | 18.9242 | -116.2100 | 11.7919 | 102.4081 | 0.0086 | 0.0195 |
| 2024_09_20 22:00 | 3267846 | 3 | 9.9600 | 13.4704 | -117.6385 | 8.1541 | 175.7205 | 0.0037 | 0.0124 |
| 2024_09_20 22:00 | 3272779 | 4 | 17.4909 | 15.3537 | -115.1857 | 6.4291 | 95.6232 | 0.0170 | 0.0150 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417178_BB446D5F | 504990 | 139 | -91.1 | 504990 | 798 | -90.1 | 504990 | 294 | -98.0 | 504990 | 969 |
| MR_1774417178_0B736969 | 504990 | 139 | -91.5 | 504990 | 798 | -89.3 | 504990 | 294 | -96.4 | 504990 | 969 |
| MR_1774417178_4159E00A | 504990 | 139 | -88.3 | 504990 | 798 | -89.7 | 504990 | 294 | -99.7 | 504990 | 969 |
| MR_1774417178_F2FAC4A0 | 504990 | 139 | -91.6 | 504990 | 798 | -91.4 | 504990 | 294 | -99.8 | 504990 | 969 |
| MR_1774417178_E6C25B3A | 504990 | 139 | -91.0 | 504990 | 798 | -89.6 | 504990 | 294 | -98.2 | 504990 | 969 |
| MR_1774417178_881AF7F3 | 504990 | 139 | -91.9 | 504990 | 798 | -89.9 | 504990 | 294 | -97.2 | 504990 | 969 |
| MR_1774417178_6345AEF0 | 504990 | 139 | -88.9 | 504990 | 798 | -89.8 | 504990 | 294 | -98.2 | 504990 | 969 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 572: `1dd34985-92b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1dd34985-92bc-4f41-a30a-fcc4b5fffcf1` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Lift the tilt angle  of 3250088_3 by 9 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[572] topology](images/train_0572.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3250088_3 and 3274669_1
- `C2`: Increase transmission power for 3246911_2
- `C3`: Adjust the azimuth of 3250088_3 by 50 degrees
- `C4`: Decrease transmission power for 3274669_1
- `C5`: Lift the tilt angle of 3246911_2 by 1 degrees
- `C6`: Increase A3 Offset threshold for 3246911_2
- `C7`: Decrease A3 Offset threshold for 3274669_1
- `C8`: Increase A3 Offset threshold for 3274669_1
- `C9`: Lift the tilt angle  of 3250088_3 by 9 degrees **← 정답**
- `C10`: Press down the tilt angle  of 3250088_3 by 9 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246911_2
- `C12`: Add neighbor relationship between 3246911_2 and 3274669_1
- `C13`: Adjust the azimuth of 3246911_2 by 35 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246911_2
- `C15`: Increase transmission power for 3274669_1
- `C16`: Press down the tilt angle of 3246911_2 by 1 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Check test server and transmission issues
- `C19`: Decrease A3 Offset threshold for 3246911_2
- `C20`: Decrease transmission power for 3246911_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274669_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274669_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.560 | MS1 | 121.4656756161 | 31.1446254763 | 654 | 504990 | -88.17 | 12.87 | 550.33 | 0.13 | 2.52 | 1566 |
| 2024-09-20 22:21:32.814 | MS1 | 121.4656726484 | 31.1446185876 | 654 | 504990 | -90.02 | 12.35 | 397.70 | 0.15 | 2.88 | 1594 |
| 2024-09-20 22:21:33.802 | MS1 | 121.4656698826 | 31.1446270851 | 654 | 504990 | -90.19 | 12.17 | 462.44 | 0.18 | 2.84 | 1589 |
| 2024-09-20 22:21:34.408 | MS1 | 121.4656765342 | 31.1446280530 | 654 | 504990 | -86.27 | 12.89 | 83.87 | 0.06 | 2.45 | 1587 |
| 2024-09-20 22:21:35.206 | MS1 | 121.4656713648 | 31.1446248891 | 654 | 504990 | -90.39 | 12.45 | 60.17 | 0.13 | 2.08 | 1567 |
| 2024-09-20 22:21:36.438 | MS1 | 121.4656722755 | 31.1446327155 | 654 | 504990 | -88.76 | 17.23 | 86.31 | 0.03 | 2.53 | 1583 |
| 2024-09-20 22:21:37.263 | MS1 | 121.4656758568 | 31.1446270355 | 654 | 504990 | -89.99 | 7.50 | 106.57 | 0.07 | 2.25 | 1591 |
| 2024-09-20 22:21:38.627 | MS1 | 121.4656652337 | 31.1446273614 | 654 | 504990 | -91.63 | 7.09 | 56.31 | 0.13 | 2.58 | 1596 |
| 2024-09-20 22:21:39.719 | MS1 | 121.4656590495 | 31.1446372766 | 654 | 504990 | -93.62 | 11.45 | 82.08 | 0.05 | 2.19 | 1595 |
| 2024-09-20 22:21:40.131 | MS1 | 121.4656756476 | 31.1446369578 | 654 | 504990 | -92.46 | 8.14 | 336.03 | 0.08 | 2.57 | 1586 |
| 2024-09-20 22:21:41.145 | MS1 | 121.4656640741 | 31.1446315650 | 654 | 504990 | -93.32 | 7.66 | 580.54 | 0.01 | 2.92 | 1591 |
| 2024-09-20 22:21:42.454 | MS1 | 121.4656750173 | 31.1446300506 | 654 | 504990 | -92.41 | 12.31 | 579.37 | 0.07 | 2.76 | 1588 |

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
| 3246911 | 2 | 121.4710231999 | 31.1543140991 | 170 | 0 | 5 | 27.9 | TDD | 654 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3250088 | 3 | 121.4661182626 | 31.1548368593 | 6 | 10 | 9 | 17.3 | TDD | 349 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3261992 | 4 | 121.4735920920 | 31.1523488760 | 317 | 14 | 2 | 19.3 | TDD | 934 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3274669 | 1 | 121.4716376497 | 31.1452710470 | 195 | 6 | 3 | 26.6 | TDD | 752 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.193 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.209 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.330 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.330 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.089 | NREventA3 | measId:2;ServCellPCI:761;Se... |
| 2024-09-20 22:21:38.329 | NRHandoverAttempt | SourcePCI:761;SourceNR-ARFC... |
| 2024-09-20 22:21:38.369 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.384 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.516 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.516 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274669 | 1 | 19.6902 | 14.9947 | -115.4702 | 15.7032 | 110.6283 | 0.0194 | 0.0002 |
| 2024_09_20 22:00 | 3246911 | 2 | 89.8083 | 77.3533 | -116.4874 | 13.8695 | 199.6013 | 0.0071 | 0.0012 |
| 2024_09_20 22:00 | 3250088 | 3 | 18.8052 | 5.5106 | -116.3063 | 9.8686 | 188.7856 | 0.0123 | 0.0148 |
| 2024_09_20 22:00 | 3261992 | 4 | 8.0392 | 12.8782 | -115.3143 | 5.7077 | 122.5793 | 0.0069 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416596_F985A5EE | 504990 | 654 | -84.4 | 504990 | 752 | -96.1 | 504990 | 349 | -98.7 | 504990 | 934 |
| MR_1774416596_4D5043E1 | 504990 | 654 | -85.1 | 504990 | 752 | -96.5 | 504990 | 349 | -96.8 | 504990 | 934 |
| MR_1774416596_3A137359 | 504990 | 654 | -87.4 | 504990 | 752 | -96.8 | 504990 | 349 | -97.5 | 504990 | 934 |
| MR_1774416596_BE8AD21E | 504990 | 654 | -84.7 | 504990 | 752 | -94.4 | 504990 | 349 | -99.3 | 504990 | 934 |
| MR_1774416596_C5130B29 | 504990 | 654 | -85.1 | 504990 | 752 | -95.8 | 504990 | 349 | -98.7 | 504990 | 934 |
| MR_1774416596_AB6B097E | 504990 | 654 | -88.2 | 504990 | 752 | -94.9 | 504990 | 349 | -98.3 | 504990 | 934 |
| MR_1774416596_43D5BE50 | 504990 | 654 | -86.8 | 504990 | 752 | -96.3 | 504990 | 349 | -96.6 | 504990 | 934 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 573: `408bc32e-c7d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `408bc32e-c7dc-4d5e-af4d-1db987775e34` |
| Tag | **multiple-answer** |
| 정답 | **C1|C8** |
| C1 의미 | Decrease transmission power for 3249358_2 |
| C8 의미 | Press down the tilt angle  of 3249358_2 by 6 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[573] topology](images/train_0573.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3249358_2 **← 정답**
- `C2`: Add neighbor relationship between 3259819_3 and 3249358_2
- `C3`: Add neighbor relationship between 3234413_1 and 3249358_2
- `C4`: Decrease A3 Offset threshold for 3249358_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259819_3
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease A3 Offset threshold for 3259819_3
- `C8`: Press down the tilt angle  of 3249358_2 by 6 degrees **← 정답**
- `C9`: Press down the tilt angle of 3259819_3 by 4 degrees
- `C10`: Lift the tilt angle  of 3249358_2 by 6 degrees
- `C11`: Adjust the azimuth of 3249358_2 by 21 degrees
- `C12`: Increase A3 Offset threshold for 3259819_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249358_2
- `C14`: Increase transmission power for 3249358_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259819_3
- `C16`: Check test server and transmission issues
- `C17`: Lift the tilt angle of 3259819_3 by 4 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249358_2
- `C19`: Increase A3 Offset threshold for 3249358_2
- `C20`: Increase transmission power for 3259819_3
- `C21`: Adjust the azimuth of 3259819_3 by 4 degrees
- `C22`: Decrease transmission power for 3259819_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.756 | MS1 | 121.4656677700 | 31.1446216663 | 739 | 504990 | -80.01 | 13.08 | 461.66 | 0.03 | 2.57 | 1562 |
| 2024-09-20 22:21:32.383 | MS1 | 121.4656666457 | 31.1446298045 | 739 | 504990 | -84.68 | 13.34 | 330.24 | 0.05 | 2.92 | 1600 |
| 2024-09-20 22:21:33.708 | MS1 | 121.4656622018 | 31.1446218567 | 739 | 504990 | -77.84 | 17.44 | 566.72 | 0.06 | 2.16 | 1594 |
| 2024-09-20 22:21:34.887 | MS1 | 121.4656602464 | 31.1446262975 | 739 | 504990 | -91.70 | 2.52 | 84.41 | 0.06 | 1.01 | 1594 |
| 2024-09-20 22:21:35.393 | MS1 | 121.4656710896 | 31.1446272437 | 739 | 504990 | -92.69 | 2.44 | 79.99 | 0.14 | 1.06 | 1564 |
| 2024-09-20 22:21:36.440 | MS1 | 121.4656694300 | 31.1446191569 | 739 | 504990 | -88.97 | 0.34 | 61.07 | 0.19 | 1.10 | 1566 |
| 2024-09-20 22:21:37.923 | MS1 | 121.4656775863 | 31.1446284032 | 739 | 504990 | -93.62 | 3.77 | 81.84 | 0.15 | 1.19 | 1562 |
| 2024-09-20 22:21:38.294 | MS1 | 121.4656752662 | 31.1446187808 | 739 | 504990 | -89.87 | 1.18 | 82.88 | 0.10 | 1.17 | 1583 |
| 2024-09-20 22:21:39.337 | MS1 | 121.4656634341 | 31.1446364124 | 739 | 504990 | -86.08 | 2.39 | 86.88 | 0.19 | 1.32 | 1566 |
| 2024-09-20 22:21:40.730 | MS1 | 121.4656678478 | 31.1446216051 | 739 | 504990 | -77.81 | 16.99 | 550.24 | 0.01 | 2.43 | 1568 |
| 2024-09-20 22:21:41.234 | MS1 | 121.4656686869 | 31.1446334965 | 739 | 504990 | -75.91 | 13.10 | 569.83 | 0.16 | 2.21 | 1588 |
| 2024-09-20 22:21:42.694 | MS1 | 121.4656650884 | 31.1446289279 | 739 | 504990 | -83.08 | 17.93 | 601.68 | 0.08 | 2.55 | 1598 |

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
| 3234413 | 1 | 121.4681338121 | 31.1450837629 | 323 | 15 | 6 | 16.2 | TDD | 497 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3249358 | 2 | 121.4688092343 | 31.1548326223 | 174 | 4 | 3 | 37.5 | TDD | 994 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3259819 | 3 | 121.4686939588 | 31.1483405131 | 211 | 0 | 1 | 36.1 | TDD | 739 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3268291 | 4 | 121.4651512522 | 31.1455152335 | 38 | 9 | 12 | 41.0 | TDD | 21 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.376 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.399 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.523 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.523 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234413 | 1 | 8.7994 | 17.7855 | -117.6495 | 11.3304 | 127.9563 | 0.0155 | 0.0036 |
| 2024_09_20 22:00 | 3249358 | 2 | 5.4678 | 17.8019 | -116.6617 | 18.4138 | 198.5493 | 0.0132 | 0.0194 |
| 2024_09_20 22:00 | 3259819 | 3 | 5.8156 | 18.7706 | -108.5417 | 14.3306 | 101.5496 | 0.0057 | 0.0020 |
| 2024_09_20 22:00 | 3268291 | 4 | 13.8913 | 7.9935 | -115.4768 | 11.8065 | 192.8796 | 0.0184 | 0.0073 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412788_C5F6D0FA | 504990 | 994 | -93.6 | 504990 | 739 | -91.9 | 504990 | 497 | -93.1 | 504990 | 21 |
| MR_1774412788_123B108C | 504990 | 994 | -90.1 | 504990 | 739 | -92.0 | 504990 | 497 | -92.7 | 504990 | 21 |
| MR_1774412788_249844D4 | 504990 | 994 | -91.8 | 504990 | 739 | -92.2 | 504990 | 497 | -92.6 | 504990 | 21 |
| MR_1774412788_589BBE21 | 504990 | 739 | -91.1 | 504990 | 994 | -91.5 | 504990 | 497 | -93.7 | 504990 | 21 |
| MR_1774412788_8C1CDBB2 | 504990 | 994 | -92.5 | 504990 | 739 | -90.9 | 504990 | 497 | -93.8 | 504990 | 21 |
| MR_1774412788_F852CD7C | 504990 | 994 | -91.1 | 504990 | 739 | -94.5 | 504990 | 497 | -94.4 | 504990 | 21 |
| MR_1774412788_A0668BC5 | 504990 | 739 | -92.0 | 504990 | 994 | -93.0 | 504990 | 497 | -91.4 | 504990 | 21 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 574: `d655fe62-9cf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d655fe62-9cf8-480d-a70d-a6a795cf3952` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Lift the tilt angle  of 3226501_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[574] topology](images/train_0574.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3226501_4 by 10 degrees
- `C2`: Adjust the azimuth of 3272741_1 by 16 degrees
- `C3`: Decrease A3 Offset threshold for 3272741_1
- `C4`: Increase A3 Offset threshold for 3216016_2
- `C5`: Add neighbor relationship between 3226501_4 and 3216016_2
- `C6`: Increase transmission power for 3216016_2
- `C7`: Lift the tilt angle  of 3226501_4 by 10 degrees **← 정답**
- `C8`: Decrease transmission power for 3216016_2
- `C9`: Increase transmission power for 3272741_1
- `C10`: Decrease A3 Offset threshold for 3216016_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272741_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216016_2
- `C13`: Decrease transmission power for 3272741_1
- `C14`: Check test server and transmission issues
- `C15`: Adjust the azimuth of 3226501_4 by 50 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272741_1
- `C18`: Lift the tilt angle of 3272741_1 by 5 degrees
- `C19`: Add neighbor relationship between 3272741_1 and 3216016_2
- `C20`: Increase A3 Offset threshold for 3272741_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216016_2
- `C22`: Press down the tilt angle of 3272741_1 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.620 | MS1 | 121.4656595425 | 31.1446284193 | 617 | 504990 | -86.20 | 12.79 | 314.48 | 0.13 | 2.73 | 1596 |
| 2024-09-20 22:21:32.427 | MS1 | 121.4656604655 | 31.1446196908 | 617 | 504990 | -85.35 | 13.70 | 422.15 | 0.06 | 2.40 | 1597 |
| 2024-09-20 22:21:33.811 | MS1 | 121.4656694968 | 31.1446364408 | 617 | 504990 | -90.95 | 14.53 | 503.39 | 0.19 | 2.35 | 1566 |
| 2024-09-20 22:21:34.694 | MS1 | 121.4656696231 | 31.1446303723 | 617 | 504990 | -91.03 | 17.94 | 44.41 | 0.13 | 2.11 | 1570 |
| 2024-09-20 22:21:35.129 | MS1 | 121.4656640101 | 31.1446360533 | 617 | 504990 | -87.09 | 16.24 | 45.61 | 0.17 | 2.36 | 1576 |
| 2024-09-20 22:21:36.357 | MS1 | 121.4656686416 | 31.1446221636 | 617 | 504990 | -90.20 | 17.94 | 86.50 | 0.12 | 2.53 | 1570 |
| 2024-09-20 22:21:37.878 | MS1 | 121.4656718160 | 31.1446364312 | 617 | 504990 | -90.53 | 11.36 | 101.35 | 0.00 | 2.91 | 1579 |
| 2024-09-20 22:21:38.683 | MS1 | 121.4656616755 | 31.1446366739 | 617 | 504990 | -89.99 | 8.30 | 42.93 | 0.10 | 2.26 | 1581 |
| 2024-09-20 22:21:39.304 | MS1 | 121.4656656568 | 31.1446259950 | 617 | 504990 | -93.00 | 7.33 | 89.14 | 0.04 | 2.74 | 1571 |
| 2024-09-20 22:21:40.200 | MS1 | 121.4656735816 | 31.1446330388 | 617 | 504990 | -90.15 | 10.52 | 582.16 | 0.05 | 2.37 | 1591 |
| 2024-09-20 22:21:41.235 | MS1 | 121.4656644261 | 31.1446377196 | 617 | 504990 | -93.85 | 8.24 | 419.42 | 0.11 | 2.60 | 1570 |
| 2024-09-20 22:21:42.357 | MS1 | 121.4656731515 | 31.1446319417 | 617 | 504990 | -89.63 | 9.43 | 506.41 | 0.15 | 2.53 | 1584 |

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
| 3216016 | 2 | 121.4754088444 | 31.1503573417 | 156 | 11 | 5 | 35.3 | TDD | 882 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3226501 | 4 | 121.4687921319 | 31.1493538704 | 335 | 14 | 6 | 25.2 | TDD | 527 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3235718 | 3 | 121.4750426307 | 31.1483364774 | 314 | 4 | 12 | 16.5 | TDD | 868 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3272741 | 1 | 121.4660861703 | 31.1533899275 | 166 | 3 | 0 | 40.5 | TDD | 617 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.393 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.416 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.516 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.516 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.258 | NREventA3 | measId:2;ServCellPCI:93;Ser... |
| 2024-09-20 22:21:38.498 | NRHandoverAttempt | SourcePCI:93;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.548 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.560 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.697 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.697 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272741 | 1 | 85.2505 | 81.5077 | -116.7370 | 19.1268 | 173.2000 | 0.0187 | 0.0122 |
| 2024_09_20 22:00 | 3216016 | 2 | 17.8318 | 16.4808 | -117.0377 | 16.9465 | 86.9840 | 0.0097 | 0.0153 |
| 2024_09_20 22:00 | 3235718 | 3 | 5.1940 | 7.2466 | -114.9475 | 15.1568 | 139.8900 | 0.0092 | 0.0165 |
| 2024_09_20 22:00 | 3226501 | 4 | 14.9142 | 6.0131 | -114.3772 | 7.2513 | 139.7119 | 0.0053 | 0.0165 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415894_D3220C48 | 504990 | 617 | -89.4 | 504990 | 882 | -100.0 | 504990 | 527 | -103.0 | 504990 | 868 |
| MR_1774415894_C7397C47 | 504990 | 617 | -91.0 | 504990 | 882 | -99.2 | 504990 | 527 | -105.1 | 504990 | 868 |
| MR_1774415894_33FA686B | 504990 | 617 | -89.8 | 504990 | 882 | -102.7 | 504990 | 527 | -102.3 | 504990 | 868 |
| MR_1774415894_F5C4E1AE | 504990 | 617 | -90.7 | 504990 | 882 | -99.3 | 504990 | 527 | -104.2 | 504990 | 868 |
| MR_1774415894_94CEBA43 | 504990 | 617 | -89.6 | 504990 | 882 | -99.0 | 504990 | 527 | -103.6 | 504990 | 868 |
| MR_1774415894_705DACCD | 504990 | 617 | -92.5 | 504990 | 882 | -100.6 | 504990 | 527 | -102.7 | 504990 | 868 |
| MR_1774415894_C1FBFC51 | 504990 | 617 | -92.6 | 504990 | 882 | -102.6 | 504990 | 527 | -103.2 | 504990 | 868 |
| MR_1774415894_C330A908 | 504990 | 617 | -92.6 | 504990 | 882 | -101.2 | 504990 | 527 | -101.6 | 504990 | 868 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 575: `b3cbf190-ca0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b3cbf190-ca0b-477a-927c-1bf5cf6ac990` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[575] topology](images/train_0575.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3264089_4
- `C2`: Adjust the azimuth of 3247965_2 by 10 degrees
- `C3`: Decrease A3 Offset threshold for 3247965_2
- `C4`: Adjust the azimuth of 3264089_4 by 50 degrees
- `C5`: Insufficient data; more data is needed for judgment. **← 정답**
- `C6`: Add neighbor relationship between 3264089_4 and 3247965_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264089_4
- `C8`: Decrease transmission power for 3247965_2
- `C9`: Increase transmission power for 3247965_2
- `C10`: Increase A3 Offset threshold for 3247965_2
- `C11`: Press down the tilt angle of 3264089_4 by 5 degrees
- `C12`: Increase transmission power for 3264089_4
- `C13`: Lift the tilt angle of 3264089_4 by 5 degrees
- `C14`: Decrease transmission power for 3264089_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264089_4
- `C16`: Check test server and transmission issues
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247965_2
- `C18`: Press down the tilt angle  of 3247965_2 by 5 degrees
- `C19`: Increase A3 Offset threshold for 3264089_4
- `C20`: Lift the tilt angle  of 3247965_2 by 5 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247965_2
- `C22`: Add neighbor relationship between 3216044_1 and 3247965_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.577 | MS1 | 121.4656704742 | 31.1446186289 | 630 | 504990 | -91.57 | 16.92 | 350.65 | 0.18 | 2.66 | 1585 |
| 2024-09-20 22:21:32.955 | MS1 | 121.4656593811 | 31.1446261063 | 630 | 504990 | -86.13 | 13.37 | 588.27 | 0.12 | 2.23 | 1575 |
| 2024-09-20 22:21:33.229 | MS1 | 121.4656708305 | 31.1446353013 | 630 | 504990 | -88.74 | 12.84 | 395.75 | 0.14 | 2.21 | 1570 |
| 2024-09-20 22:21:34.854 | MS1 | 121.4656705876 | 31.1446302195 | 630 | 504990 | -88.84 | 17.92 | 86.51 | 0.09 | 2.91 | 1584 |
| 2024-09-20 22:21:35.308 | MS1 | 121.4656696327 | 31.1446290139 | 630 | 504990 | -87.40 | 17.33 | 80.60 | 0.13 | 2.50 | 1595 |
| 2024-09-20 22:21:36.116 | MS1 | 121.4656585529 | 31.1446322188 | 630 | 504990 | -89.86 | 14.27 | 89.53 | 0.19 | 2.98 | 1572 |
| 2024-09-20 22:21:37.321 | MS1 | 121.4656625834 | 31.1446272216 | 630 | 504990 | -90.05 | 11.52 | 87.29 | 0.16 | 2.83 | 1593 |
| 2024-09-20 22:21:38.947 | MS1 | 121.4656599055 | 31.1446258617 | 630 | 504990 | -93.67 | 10.84 | 64.68 | 0.06 | 2.50 | 1564 |
| 2024-09-20 22:21:39.626 | MS1 | 121.4656610761 | 31.1446353611 | 630 | 504990 | -91.57 | 11.97 | 62.56 | 0.11 | 2.39 | 1564 |
| 2024-09-20 22:21:40.341 | MS1 | 121.4656713201 | 31.1446372520 | 630 | 504990 | -92.96 | 9.20 | 473.33 | 0.05 | 2.22 | 1595 |
| 2024-09-20 22:21:41.893 | MS1 | 121.4656600738 | 31.1446244982 | 630 | 504990 | -93.28 | 7.08 | 365.76 | 0.05 | 2.13 | 1591 |
| 2024-09-20 22:21:42.902 | MS1 | 121.4656597460 | 31.1446242149 | 630 | 504990 | -90.29 | 9.71 | 471.79 | 0.11 | 2.97 | 1600 |

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
| 3216044 | 1 | 121.4687682866 | 31.1494259541 | 31 | 5 | 8 | 49.6 | TDD | 192 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3217069 | 3 | 121.4646388614 | 31.1458119307 | 90 | 13 | 12 | 23.7 | TDD | 651 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3247965 | 2 | 121.4669061963 | 31.1474829230 | 191 | 0 | 8 | 32.0 | TDD | 745 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3264089 | 4 | 121.4663137288 | 31.1485122707 | 93 | 3 | 9 | 18.8 | TDD | 630 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.352 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.367 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.500 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.500 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.170 | NREventA3 | measId:2;ServCellPCI:787;Se... |
| 2024-09-20 22:21:38.410 | NRHandoverAttempt | SourcePCI:787;SourceNR-ARFC... |
| 2024-09-20 22:21:38.446 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.457 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.569 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.569 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3216044 | 1 | 80.5833 | 77.7821 | -117.0596 | 11.4295 | 194.5961 | 0.0169 | 0.0009 |
| 2024_09_19 22:00 | 3247965 | 2 | 78.1460 | 93.3375 | -117.2393 | 9.1047 | 150.6687 | 0.0019 | 0.0016 |
| 2024_09_19 22:00 | 3217069 | 3 | 91.7076 | 75.1484 | -117.9484 | 7.9400 | 158.2416 | 0.0008 | 0.0145 |
| 2024_09_19 22:00 | 3264089 | 4 | 88.5066 | 87.2156 | -116.2824 | 13.3982 | 190.1384 | 0.0052 | 0.0111 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416048_C53CAD9A | 504990 | 630 | -89.2 | 504990 | 745 | -98.2 | 504990 | 192 | -97.2 | 504990 | 651 |
| MR_1774416048_C6536BBC | 504990 | 630 | -90.5 | 504990 | 745 | -99.2 | 504990 | 192 | -100.6 | 504990 | 651 |
| MR_1774416048_29FEEFD6 | 504990 | 630 | -87.3 | 504990 | 745 | -98.3 | 504990 | 192 | -100.8 | 504990 | 651 |
| MR_1774416048_5FADE6D3 | 504990 | 630 | -89.4 | 504990 | 745 | -99.9 | 504990 | 192 | -98.3 | 504990 | 651 |
| MR_1774416048_99EF4B09 | 504990 | 630 | -89.7 | 504990 | 745 | -97.6 | 504990 | 192 | -99.6 | 504990 | 651 |
| MR_1774416048_86144FF1 | 504990 | 630 | -90.7 | 504990 | 745 | -99.6 | 504990 | 192 | -97.4 | 504990 | 651 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 576: `e1b838c8-0ed...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e1b838c8-0ed6-460e-9874-1fbfb75ba2a8` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[576] topology](images/train_0576.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277669_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277669_4
- `C3`: Decrease A3 Offset threshold for 3277669_4
- `C4`: Increase A3 Offset threshold for 3277669_4
- `C5`: Press down the tilt angle of 3277367_2 by 7 degrees
- `C6`: Decrease transmission power for 3277669_4
- `C7`: Lift the tilt angle  of 3277669_4 by 10 degrees
- `C8`: Increase transmission power for 3277367_2
- `C9`: Decrease transmission power for 3277367_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277367_2
- `C11`: Decrease A3 Offset threshold for 3277367_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Adjust the azimuth of 3277367_2 by 8 degrees
- `C14`: Press down the tilt angle  of 3277669_4 by 10 degrees
- `C15`: Increase A3 Offset threshold for 3277367_2
- `C16`: Add neighbor relationship between 3244561_3 and 3277669_4
- `C17`: Add neighbor relationship between 3277367_2 and 3277669_4
- `C18`: Adjust the azimuth of 3277669_4 by 50 degrees
- `C19`: Check test server and transmission issues **← 정답**
- `C20`: Lift the tilt angle of 3277367_2 by 7 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277367_2
- `C22`: Increase transmission power for 3277669_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.662 | MS1 | 121.4656734607 | 31.1446335983 | 638 | 504990 | -89.48 | 17.24 | 373.21 | 0.13 | 2.41 | 1592 |
| 2024-09-20 22:21:32.110 | MS1 | 121.4656593953 | 31.1446234364 | 638 | 504990 | -85.73 | 16.47 | 349.60 | 0.04 | 2.12 | 1599 |
| 2024-09-20 22:21:33.601 | MS1 | 121.4656667207 | 31.1446306575 | 638 | 504990 | -85.53 | 16.94 | 357.65 | 0.18 | 2.13 | 1563 |
| 2024-09-20 22:21:34.559 | MS1 | 121.4656679510 | 31.1446309613 | 638 | 504990 | -85.60 | 16.91 | 89.53 | 0.10 | 2.47 | 303 |
| 2024-09-20 22:21:35.710 | MS1 | 121.4656771800 | 31.1446244452 | 638 | 504990 | -86.79 | 16.00 | 87.17 | 0.10 | 2.82 | 323 |
| 2024-09-20 22:21:36.338 | MS1 | 121.4656771926 | 31.1446226209 | 638 | 504990 | -86.09 | 15.39 | 99.14 | 0.01 | 2.75 | 402 |
| 2024-09-20 22:21:37.135 | MS1 | 121.4656635203 | 31.1446288439 | 638 | 504990 | -91.33 | 12.32 | 59.02 | 0.03 | 2.31 | 471 |
| 2024-09-20 22:21:38.202 | MS1 | 121.4656737010 | 31.1446225960 | 638 | 504990 | -93.40 | 11.51 | 63.92 | 0.06 | 2.29 | 365 |
| 2024-09-20 22:21:39.730 | MS1 | 121.4656754420 | 31.1446183104 | 638 | 504990 | -93.94 | 9.33 | 104.50 | 0.10 | 2.29 | 488 |
| 2024-09-20 22:21:40.687 | MS1 | 121.4656596585 | 31.1446274008 | 638 | 504990 | -89.27 | 10.59 | 433.89 | 0.02 | 2.09 | 1591 |
| 2024-09-20 22:21:41.778 | MS1 | 121.4656694958 | 31.1446249160 | 638 | 504990 | -91.08 | 8.86 | 509.56 | 0.08 | 2.65 | 1576 |
| 2024-09-20 22:21:42.434 | MS1 | 121.4656692995 | 31.1446262568 | 638 | 504990 | -92.76 | 10.69 | 439.08 | 0.04 | 2.40 | 1569 |

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
| 3239244 | 1 | 121.4710304533 | 31.1527469781 | 300 | 3 | 5 | 29.5 | TDD | 674 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3244561 | 3 | 121.4726543880 | 31.1512032300 | 173 | 13 | 12 | 36.5 | TDD | 718 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3277367 | 2 | 121.4757338096 | 31.1473264862 | 245 | 5 | 6 | 33.5 | TDD | 638 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3277669 | 4 | 121.4670704061 | 31.1443850772 | 41 | 7 | 5 | 19.4 | TDD | 870 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.207 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.227 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.363 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.363 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.033 | NREventA3 | measId:2;ServCellPCI:910;Se... |
| 2024-09-20 22:21:38.273 | NRHandoverAttempt | SourcePCI:910;SourceNR-ARFC... |
| 2024-09-20 22:21:38.305 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.318 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.462 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.462 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239244 | 1 | 8.9714 | 18.5500 | -114.4777 | 8.8468 | 169.8731 | 0.0164 | 0.0157 |
| 2024_09_20 22:00 | 3277367 | 2 | 8.0277 | 19.3152 | -116.2632 | 18.4060 | 125.7969 | 0.0139 | 0.0043 |
| 2024_09_20 22:00 | 3244561 | 3 | 7.1118 | 19.0716 | -116.5705 | 9.1525 | 156.8143 | 0.0168 | 0.0107 |
| 2024_09_20 22:00 | 3277669 | 4 | 12.1748 | 6.0947 | -117.3033 | 18.8606 | 197.9929 | 0.0020 | 0.0022 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416830_2F7FA3BB | 504990 | 638 | -85.7 | 504990 | 870 | -89.1 | 504990 | 718 | -90.5 | 504990 | 674 |
| MR_1774416830_07067DD9 | 504990 | 638 | -86.8 | 504990 | 870 | -92.4 | 504990 | 718 | -91.4 | 504990 | 674 |
| MR_1774416830_5003E74D | 504990 | 638 | -84.4 | 504990 | 870 | -90.4 | 504990 | 718 | -91.4 | 504990 | 674 |
| MR_1774416830_407CC9FD | 504990 | 638 | -86.8 | 504990 | 870 | -92.4 | 504990 | 718 | -91.3 | 504990 | 674 |
| MR_1774416830_157CF220 | 504990 | 638 | -86.7 | 504990 | 870 | -90.7 | 504990 | 718 | -92.7 | 504990 | 674 |
| MR_1774416830_8AB10354 | 504990 | 638 | -85.7 | 504990 | 870 | -91.4 | 504990 | 718 | -94.4 | 504990 | 674 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 577: `33ec70a1-1bf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `33ec70a1-1bfa-4376-be8d-a0a1c7813b23` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3257805_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[577] topology](images/train_0577.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3257805_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228991_4
- `C3`: Decrease A3 Offset threshold for 3228991_4
- `C4`: Decrease transmission power for 3228991_4
- `C5`: Lift the tilt angle  of 3228991_4 by 10 degrees
- `C6`: Increase transmission power for 3257805_2
- `C7`: Decrease transmission power for 3257805_2
- `C8`: Press down the tilt angle of 3257805_2 by 6 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228991_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257805_2
- `C11`: Adjust the azimuth of 3228991_4 by 2 degrees
- `C12`: Adjust the azimuth of 3257805_2 by 12 degrees
- `C13`: Press down the tilt angle  of 3228991_4 by 10 degrees
- `C14`: Lift the tilt angle of 3257805_2 by 6 degrees
- `C15`: Increase transmission power for 3228991_4
- `C16`: Check test server and transmission issues
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Add neighbor relationship between 3249574_3 and 3228991_4
- `C19`: Increase A3 Offset threshold for 3257805_2
- `C20`: Add neighbor relationship between 3257805_2 and 3228991_4
- `C21`: Increase A3 Offset threshold for 3228991_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257805_2 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.783 | MS1 | 121.4656718121 | 31.1446185525 | 838 | 504990 | -88.94 | 17.84 | 542.66 | 0.07 | 2.53 | 1588 |
| 2024-09-20 22:21:32.521 | MS1 | 121.4656664945 | 31.1446306203 | 838 | 504990 | -90.94 | 14.02 | 401.69 | 0.02 | 2.41 | 1585 |
| 2024-09-20 22:21:33.184 | MS1 | 121.4656686535 | 31.1446341295 | 838 | 504990 | -89.50 | 12.66 | 496.03 | 0.12 | 2.39 | 1600 |
| 2024-09-20 22:21:34.684 | MS1 | 121.4656663192 | 31.1446284702 | 838 | 504990 | -85.37 | 16.87 | 67.42 | 0.58 | 2.84 | 632 |
| 2024-09-20 22:21:35.682 | MS1 | 121.4656646406 | 31.1446294207 | 838 | 504990 | -88.27 | 12.14 | 71.12 | 0.59 | 2.91 | 666 |
| 2024-09-20 22:21:36.255 | MS1 | 121.4656750999 | 31.1446260919 | 838 | 504990 | -88.96 | 16.12 | 55.03 | 0.64 | 2.53 | 569 |
| 2024-09-20 22:21:37.730 | MS1 | 121.4656723852 | 31.1446229307 | 838 | 504990 | -90.37 | 12.61 | 85.32 | 0.51 | 2.30 | 520 |
| 2024-09-20 22:21:38.371 | MS1 | 121.4656704244 | 31.1446238915 | 838 | 504990 | -91.97 | 10.23 | 59.53 | 0.69 | 2.75 | 641 |
| 2024-09-20 22:21:39.392 | MS1 | 121.4656685047 | 31.1446188718 | 838 | 504990 | -93.17 | 10.48 | 78.16 | 0.58 | 2.92 | 693 |
| 2024-09-20 22:21:40.169 | MS1 | 121.4656668389 | 31.1446253560 | 838 | 504990 | -92.01 | 8.86 | 487.60 | 0.06 | 2.97 | 1589 |
| 2024-09-20 22:21:41.891 | MS1 | 121.4656699706 | 31.1446335592 | 838 | 504990 | -92.24 | 12.28 | 301.56 | 0.15 | 2.63 | 1585 |
| 2024-09-20 22:21:42.428 | MS1 | 121.4656595360 | 31.1446228416 | 838 | 504990 | -92.34 | 9.35 | 353.46 | 0.15 | 2.87 | 1583 |

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
| 3228991 | 4 | 121.4676510432 | 31.1444828133 | 273 | 13 | 6 | 48.7 | TDD | 190 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3249574 | 3 | 121.4711847925 | 31.1454385213 | 121 | 6 | 12 | 23.3 | TDD | 170 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3257805 | 2 | 121.4713048250 | 31.1551609318 | 217 | 5 | 1 | 19.4 | TDD | 838 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3266866 | 1 | 121.4751801793 | 31.1440195792 | 357 | 2 | 7 | 40.4 | TDD | 944 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.115 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.138 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.242 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.242 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.925 | NREventA3 | measId:2;ServCellPCI:811;Se... |
| 2024-09-20 22:21:38.165 | NRHandoverAttempt | SourcePCI:811;SourceNR-ARFC... |
| 2024-09-20 22:21:38.209 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.220 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.321 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.321 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266866 | 1 | 19.1192 | 17.1739 | -115.3703 | 14.6969 | 110.5468 | 0.0082 | 0.0015 |
| 2024_09_20 22:00 | 3257805 | 2 | 6.5014 | 11.5798 | -117.1169 | 8.4919 | 94.3953 | 0.0150 | 0.0103 |
| 2024_09_20 22:00 | 3249574 | 3 | 8.9582 | 15.2377 | -114.3493 | 10.9491 | 192.5219 | 0.0031 | 0.0063 |
| 2024_09_20 22:00 | 3228991 | 4 | 6.5641 | 17.9310 | -115.4454 | 16.4845 | 197.0453 | 0.0166 | 0.0096 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414734_5866DAC0 | 504990 | 838 | -84.7 | 504990 | 190 | -92.3 | 504990 | 170 | -93.6 | 504990 | 944 |
| MR_1774414734_211D2919 | 504990 | 838 | -87.3 | 504990 | 190 | -91.6 | 504990 | 170 | -93.1 | 504990 | 944 |
| MR_1774414734_01738C41 | 504990 | 838 | -84.0 | 504990 | 190 | -91.4 | 504990 | 170 | -94.6 | 504990 | 944 |
| MR_1774414734_B2FF394E | 504990 | 838 | -86.8 | 504990 | 190 | -90.9 | 504990 | 170 | -93.0 | 504990 | 944 |
| MR_1774414734_2AB602F9 | 504990 | 838 | -86.1 | 504990 | 190 | -91.4 | 504990 | 170 | -92.6 | 504990 | 944 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 578: `6ecacd1b-e58...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6ecacd1b-e58f-499d-b3b1-d86cb8b828d4` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Lift the tilt angle  of 3277301_2 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[578] topology](images/train_0578.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214081_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267450_4
- `C3`: Press down the tilt angle  of 3277301_2 by 7 degrees
- `C4`: Increase A3 Offset threshold for 3214081_1
- `C5`: Add neighbor relationship between 3267450_4 and 3214081_1
- `C6`: Decrease A3 Offset threshold for 3267450_4
- `C7`: Lift the tilt angle of 3267450_4 by 5 degrees
- `C8`: Decrease A3 Offset threshold for 3214081_1
- `C9`: Adjust the azimuth of 3277301_2 by 50 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267450_4
- `C11`: Decrease transmission power for 3267450_4
- `C12`: Lift the tilt angle  of 3277301_2 by 7 degrees **← 정답**
- `C13`: Increase transmission power for 3267450_4
- `C14`: Adjust the azimuth of 3267450_4 by 28 degrees
- `C15`: Decrease transmission power for 3214081_1
- `C16`: Press down the tilt angle of 3267450_4 by 5 degrees
- `C17`: Check test server and transmission issues
- `C18`: Add neighbor relationship between 3277301_2 and 3214081_1
- `C19`: Increase A3 Offset threshold for 3267450_4
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase transmission power for 3214081_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214081_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.203 | MS1 | 121.4656769892 | 31.1446198515 | 405 | 504990 | -85.46 | 14.44 | 351.39 | 0.04 | 2.91 | 1578 |
| 2024-09-20 22:21:32.718 | MS1 | 121.4656598262 | 31.1446250788 | 405 | 504990 | -91.65 | 15.40 | 521.82 | 0.13 | 2.05 | 1576 |
| 2024-09-20 22:21:33.375 | MS1 | 121.4656772575 | 31.1446305515 | 405 | 504990 | -85.51 | 15.01 | 336.53 | 0.14 | 2.17 | 1591 |
| 2024-09-20 22:21:34.723 | MS1 | 121.4656654285 | 31.1446235933 | 405 | 504990 | -85.42 | 13.54 | 89.41 | 0.05 | 2.68 | 1600 |
| 2024-09-20 22:21:35.219 | MS1 | 121.4656642438 | 31.1446324220 | 405 | 504990 | -88.84 | 15.37 | 74.69 | 0.03 | 2.18 | 1587 |
| 2024-09-20 22:21:36.246 | MS1 | 121.4656740278 | 31.1446189317 | 405 | 504990 | -92.00 | 15.84 | 84.39 | 0.09 | 2.42 | 1586 |
| 2024-09-20 22:21:37.939 | MS1 | 121.4656686179 | 31.1446361458 | 405 | 504990 | -89.24 | 8.42 | 57.95 | 0.12 | 2.12 | 1577 |
| 2024-09-20 22:21:38.891 | MS1 | 121.4656662788 | 31.1446375924 | 405 | 504990 | -89.34 | 12.31 | 92.96 | 0.16 | 2.17 | 1599 |
| 2024-09-20 22:21:39.960 | MS1 | 121.4656651336 | 31.1446364968 | 405 | 504990 | -89.88 | 10.04 | 83.09 | 0.07 | 2.58 | 1578 |
| 2024-09-20 22:21:40.793 | MS1 | 121.4656642940 | 31.1446220567 | 405 | 504990 | -90.74 | 8.33 | 433.28 | 0.01 | 2.42 | 1596 |
| 2024-09-20 22:21:41.182 | MS1 | 121.4656647608 | 31.1446231192 | 405 | 504990 | -93.79 | 9.35 | 318.57 | 0.03 | 2.18 | 1594 |
| 2024-09-20 22:21:42.842 | MS1 | 121.4656755006 | 31.1446212334 | 405 | 504990 | -92.79 | 9.94 | 375.57 | 0.01 | 2.39 | 1589 |

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
| 3214081 | 1 | 121.4691431710 | 31.1518668218 | 74 | 4 | 12 | 40.1 | TDD | 938 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3228506 | 3 | 121.4693647249 | 31.1503242619 | 168 | 13 | 10 | 37.0 | TDD | 724 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3267450 | 4 | 121.4649715986 | 31.1513894665 | 203 | 3 | 0 | 29.8 | TDD | 405 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3277301 | 2 | 121.4751627767 | 31.1547126132 | 98 | 2 | 0 | 34.9 | TDD | 2 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.025 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.041 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.167 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.167 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.840 | NREventA3 | measId:2;ServCellPCI:204;Se... |
| 2024-09-20 22:21:38.080 | NRHandoverAttempt | SourcePCI:204;SourceNR-ARFC... |
| 2024-09-20 22:21:38.120 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.134 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.244 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.244 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214081 | 1 | 15.3534 | 8.9668 | -115.8045 | 12.1481 | 195.2200 | 0.0019 | 0.0122 |
| 2024_09_20 22:00 | 3277301 | 2 | 11.4502 | 8.3875 | -115.4326 | 7.2493 | 85.7004 | 0.0015 | 0.0032 |
| 2024_09_20 22:00 | 3228506 | 3 | 19.1149 | 10.4008 | -117.2969 | 18.7114 | 133.3762 | 0.0027 | 0.0042 |
| 2024_09_20 22:00 | 3267450 | 4 | 86.7758 | 75.7762 | -116.7797 | 17.1451 | 111.3388 | 0.0085 | 0.0063 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415233_7671A872 | 504990 | 405 | -85.0 | 504990 | 938 | -88.8 | 504990 | 2 | -98.6 | 504990 | 724 |
| MR_1774415233_C7F93875 | 504990 | 405 | -83.4 | 504990 | 938 | -87.4 | 504990 | 2 | -98.7 | 504990 | 724 |
| MR_1774415233_2F6D4FFE | 504990 | 405 | -85.7 | 504990 | 938 | -89.3 | 504990 | 2 | -97.7 | 504990 | 724 |
| MR_1774415233_4E2C9E07 | 504990 | 405 | -84.0 | 504990 | 938 | -88.5 | 504990 | 2 | -99.3 | 504990 | 724 |
| MR_1774415233_6B47C98A | 504990 | 405 | -86.3 | 504990 | 938 | -88.0 | 504990 | 2 | -96.8 | 504990 | 724 |
| MR_1774415233_621CEC3C | 504990 | 405 | -83.8 | 504990 | 938 | -88.3 | 504990 | 2 | -97.9 | 504990 | 724 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 579: `42a45488-8ae...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `42a45488-8ae0-45b6-a46b-742efac3eeb3` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3220812_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[579] topology](images/train_0579.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase transmission power for 3220812_2
- `C3`: Increase transmission power for 3212082_3
- `C4`: Press down the tilt angle  of 3212082_3 by 10 degrees
- `C5`: Check test server and transmission issues
- `C6`: Lift the tilt angle  of 3212082_3 by 10 degrees
- `C7`: Decrease transmission power for 3212082_3
- `C8`: Add neighbor relationship between 3220812_2 and 3212082_3
- `C9`: Increase A3 Offset threshold for 3212082_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220812_2 **← 정답**
- `C11`: Decrease A3 Offset threshold for 3220812_2
- `C12`: Adjust the azimuth of 3220812_2 by 32 degrees
- `C13`: Add neighbor relationship between 3236820_1 and 3212082_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212082_3
- `C15`: Press down the tilt angle of 3220812_2 by 5 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212082_3
- `C17`: Lift the tilt angle of 3220812_2 by 5 degrees
- `C18`: Decrease transmission power for 3220812_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220812_2
- `C20`: Adjust the azimuth of 3212082_3 by 50 degrees
- `C21`: Decrease A3 Offset threshold for 3212082_3
- `C22`: Increase A3 Offset threshold for 3220812_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.533 | MS1 | 121.4656777627 | 31.1446239201 | 169 | 504990 | -91.79 | 15.23 | 462.46 | 0.17 | 2.08 | 1574 |
| 2024-09-20 22:21:32.876 | MS1 | 121.4656630590 | 31.1446335474 | 169 | 504990 | -86.39 | 17.37 | 353.73 | 0.01 | 2.24 | 1563 |
| 2024-09-20 22:21:33.393 | MS1 | 121.4656754476 | 31.1446249253 | 169 | 504990 | -88.23 | 15.49 | 566.21 | 0.16 | 2.66 | 1571 |
| 2024-09-20 22:21:34.103 | MS1 | 121.4656736231 | 31.1446316131 | 169 | 504990 | -88.93 | 16.72 | 80.55 | 0.51 | 2.24 | 645 |
| 2024-09-20 22:21:35.422 | MS1 | 121.4656771668 | 31.1446369325 | 169 | 504990 | -90.92 | 17.08 | 55.38 | 0.66 | 2.98 | 610 |
| 2024-09-20 22:21:36.358 | MS1 | 121.4656715008 | 31.1446377984 | 169 | 504990 | -91.63 | 14.05 | 51.10 | 0.64 | 2.24 | 563 |
| 2024-09-20 22:21:37.841 | MS1 | 121.4656680760 | 31.1446214688 | 169 | 504990 | -93.45 | 11.53 | 61.66 | 0.64 | 2.10 | 637 |
| 2024-09-20 22:21:38.923 | MS1 | 121.4656620210 | 31.1446337740 | 169 | 504990 | -89.01 | 11.51 | 60.86 | 0.61 | 2.34 | 549 |
| 2024-09-20 22:21:39.198 | MS1 | 121.4656603663 | 31.1446258568 | 169 | 504990 | -89.06 | 12.16 | 73.19 | 0.67 | 2.96 | 676 |
| 2024-09-20 22:21:40.103 | MS1 | 121.4656722123 | 31.1446287436 | 169 | 504990 | -91.88 | 9.88 | 570.41 | 0.16 | 2.14 | 1576 |
| 2024-09-20 22:21:41.186 | MS1 | 121.4656663732 | 31.1446311367 | 169 | 504990 | -91.19 | 12.03 | 373.97 | 0.03 | 2.52 | 1563 |
| 2024-09-20 22:21:42.219 | MS1 | 121.4656612634 | 31.1446258960 | 169 | 504990 | -91.65 | 9.39 | 418.98 | 0.19 | 2.51 | 1592 |

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
| 3212082 | 3 | 121.4750068908 | 31.1555080166 | 157 | 11 | 11 | 24.3 | TDD | 507 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3220812 | 2 | 121.4738138733 | 31.1443763428 | 240 | 4 | 1 | 16.0 | TDD | 169 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3236820 | 1 | 121.4707149276 | 31.1449533166 | 63 | 1 | 10 | 27.0 | TDD | 928 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3263386 | 4 | 121.4747478509 | 31.1476395183 | 24 | 9 | 8 | 32.2 | TDD | 411 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.913 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.928 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.030 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.030 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.800 | NREventA3 | measId:2;ServCellPCI:987;Se... |
| 2024-09-20 22:21:38.040 | NRHandoverAttempt | SourcePCI:987;SourceNR-ARFC... |
| 2024-09-20 22:21:38.090 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.104 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.230 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.230 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236820 | 1 | 7.7019 | 14.1312 | -116.9651 | 10.1149 | 149.8660 | 0.0013 | 0.0198 |
| 2024_09_20 22:00 | 3220812 | 2 | 17.2605 | 13.7680 | -114.1395 | 17.5231 | 145.0390 | 0.0015 | 0.0113 |
| 2024_09_20 22:00 | 3212082 | 3 | 14.1425 | 5.2563 | -116.6562 | 9.0327 | 132.7437 | 0.0157 | 0.0096 |
| 2024_09_20 22:00 | 3263386 | 4 | 13.2516 | 9.8723 | -117.9559 | 14.6176 | 100.5415 | 0.0069 | 0.0026 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415139_BF5C7191 | 504990 | 169 | -90.1 | 504990 | 507 | -88.2 | 504990 | 928 | -100.9 | 504990 | 411 |
| MR_1774415139_875889F9 | 504990 | 169 | -90.0 | 504990 | 507 | -88.8 | 504990 | 928 | -101.3 | 504990 | 411 |
| MR_1774415139_17E3E34B | 504990 | 169 | -90.3 | 504990 | 507 | -90.9 | 504990 | 928 | -100.9 | 504990 | 411 |
| MR_1774415139_A56E39F6 | 504990 | 169 | -87.0 | 504990 | 507 | -88.3 | 504990 | 928 | -100.1 | 504990 | 411 |
| MR_1774415139_AA92C8BF | 504990 | 169 | -89.9 | 504990 | 507 | -89.0 | 504990 | 928 | -100.3 | 504990 | 411 |
| MR_1774415139_2046FD6C | 504990 | 169 | -89.6 | 504990 | 507 | -90.2 | 504990 | 928 | -99.9 | 504990 | 411 |

> *... 2개 열 생략 (전체 14열)*

---
