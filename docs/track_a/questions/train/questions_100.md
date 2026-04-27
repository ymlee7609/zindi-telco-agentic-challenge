# Track A 문제 분석 — train[990]~train[999]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[990] ~ train[999] (10개)

## 목차

1. [문제 990: `332a4d3a-3f2...`](#990) — single-answer, 정답: C14
2. [문제 991: `95160fa1-388...`](#991) — single-answer, 정답: C22
3. [문제 992: `1c1f381a-05e...`](#992) — single-answer, 정답: C18
4. [문제 993: `3b332364-435...`](#993) — single-answer, 정답: C22
5. [문제 994: `9239c5b5-f71...`](#994) — single-answer, 정답: C3
6. [문제 995: `f29e7638-744...`](#995) — single-answer, 정답: C3
7. [문제 996: `21319f7e-06f...`](#996) — single-answer, 정답: C17
8. [문제 997: `3c49e63d-4f5...`](#997) — single-answer, 정답: C16
9. [문제 998: `488740df-e20...`](#998) — single-answer, 정답: C12
10. [문제 999: `9efd162a-d5a...`](#999) — single-answer, 정답: C5

---

### 문제 990: `332a4d3a-3f2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `332a4d3a-3f24-44e8-a628-f1f06bb6e9d9` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[990] topology](images/train_0990.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3234783_4
- `C2`: Adjust the azimuth of 3261379_3 by 50 degrees
- `C3`: Lift the tilt angle of 3261379_3 by 5 degrees
- `C4`: Increase transmission power for 3261379_3
- `C5`: Check test server and transmission issues
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261379_3
- `C7`: Adjust the azimuth of 3234783_4 by 50 degrees
- `C8`: Increase A3 Offset threshold for 3234783_4
- `C9`: Decrease A3 Offset threshold for 3261379_3
- `C10`: Decrease transmission power for 3261379_3
- `C11`: Press down the tilt angle of 3261379_3 by 5 degrees
- `C12`: Add neighbor relationship between 3262680_2 and 3234783_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234783_4
- `C14`: Insufficient data; more data is needed for judgment. **← 정답**
- `C15`: Add neighbor relationship between 3261379_3 and 3234783_4
- `C16`: Press down the tilt angle  of 3234783_4 by 10 degrees
- `C17`: Increase A3 Offset threshold for 3261379_3
- `C18`: Decrease A3 Offset threshold for 3234783_4
- `C19`: Lift the tilt angle  of 3234783_4 by 10 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234783_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261379_3
- `C22`: Decrease transmission power for 3234783_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.766 | MS1 | 121.4656716471 | 31.1446192784 | 172 | 504990 | -91.90 | 12.93 | 406.82 | 0.08 | 2.69 | 1571 |
| 2024-09-20 22:21:32.662 | MS1 | 121.4656594710 | 31.1446321760 | 172 | 504990 | -87.36 | 13.02 | 583.03 | 0.02 | 2.15 | 1563 |
| 2024-09-20 22:21:33.274 | MS1 | 121.4656707793 | 31.1446279496 | 172 | 504990 | -91.36 | 12.88 | 443.58 | 0.10 | 2.60 | 1567 |
| 2024-09-20 22:21:34.989 | MS1 | 121.4656661149 | 31.1446286778 | 172 | 504990 | -91.42 | 14.27 | 61.93 | 0.17 | 2.85 | 1581 |
| 2024-09-20 22:21:35.335 | MS1 | 121.4656629864 | 31.1446366463 | 172 | 504990 | -86.99 | 15.75 | 70.73 | 0.01 | 2.59 | 1567 |
| 2024-09-20 22:21:36.323 | MS1 | 121.4656607611 | 31.1446296399 | 172 | 504990 | -88.41 | 14.60 | 69.06 | 0.06 | 2.90 | 1564 |
| 2024-09-20 22:21:37.218 | MS1 | 121.4656696462 | 31.1446235422 | 172 | 504990 | -89.58 | 7.80 | 48.81 | 0.17 | 2.26 | 1576 |
| 2024-09-20 22:21:38.383 | MS1 | 121.4656729020 | 31.1446187395 | 172 | 504990 | -92.22 | 11.98 | 65.12 | 0.15 | 2.91 | 1579 |
| 2024-09-20 22:21:39.741 | MS1 | 121.4656580534 | 31.1446363342 | 172 | 504990 | -92.17 | 7.70 | 47.92 | 0.04 | 2.13 | 1561 |
| 2024-09-20 22:21:40.903 | MS1 | 121.4656674851 | 31.1446250977 | 172 | 504990 | -89.66 | 11.84 | 497.14 | 0.16 | 2.42 | 1599 |
| 2024-09-20 22:21:41.928 | MS1 | 121.4656625458 | 31.1446273187 | 172 | 504990 | -91.18 | 9.44 | 499.39 | 0.19 | 2.33 | 1589 |
| 2024-09-20 22:21:42.692 | MS1 | 121.4656611277 | 31.1446330091 | 172 | 504990 | -92.60 | 11.41 | 329.84 | 0.16 | 2.30 | 1585 |

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
| 3234783 | 4 | 121.4654527792 | 31.1510035430 | 67 | 8 | 0 | 31.5 | TDD | 412 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3255530 | 1 | 121.4670166778 | 31.1532543640 | 191 | 7 | 3 | 39.9 | TDD | 148 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3261379 | 3 | 121.4707325952 | 31.1464797262 | 157 | 0 | 9 | 41.7 | TDD | 172 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3262680 | 2 | 121.4725541912 | 31.1469500937 | 343 | 7 | 3 | 15.5 | TDD | 682 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.610 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.631 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.764 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.764 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.456 | NREventA3 | measId:2;ServCellPCI:920;Se... |
| 2024-09-20 22:21:38.696 | NRHandoverAttempt | SourcePCI:920;SourceNR-ARFC... |
| 2024-09-20 22:21:38.738 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.750 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.873 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.873 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3255530 | 1 | 85.4906 | 94.8912 | -114.1420 | 18.2303 | 103.8006 | 0.0091 | 0.0005 |
| 2024_09_19 22:00 | 3262680 | 2 | 85.0807 | 81.9808 | -114.5990 | 18.7106 | 199.0735 | 0.0017 | 0.0070 |
| 2024_09_19 22:00 | 3261379 | 3 | 88.5383 | 94.3067 | -114.2557 | 17.7919 | 133.5281 | 0.0054 | 0.0030 |
| 2024_09_19 22:00 | 3234783 | 4 | 89.0667 | 77.2371 | -115.5776 | 6.2228 | 195.0984 | 0.0178 | 0.0172 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412037_D2614E3B | 504990 | 172 | -90.3 | 504990 | 412 | -95.8 | 504990 | 682 | -101.0 | 504990 | 148 |
| MR_1774412037_78F1EDC9 | 504990 | 172 | -91.4 | 504990 | 412 | -95.6 | 504990 | 682 | -101.3 | 504990 | 148 |
| MR_1774412037_3F63BF3D | 504990 | 172 | -92.6 | 504990 | 412 | -95.3 | 504990 | 682 | -98.8 | 504990 | 148 |
| MR_1774412037_12649F63 | 504990 | 172 | -89.5 | 504990 | 412 | -96.7 | 504990 | 682 | -99.5 | 504990 | 148 |
| MR_1774412037_994C597B | 504990 | 172 | -91.2 | 504990 | 412 | -94.7 | 504990 | 682 | -101.3 | 504990 | 148 |
| MR_1774412037_46487E4C | 504990 | 172 | -90.8 | 504990 | 412 | -94.3 | 504990 | 682 | -98.3 | 504990 | 148 |
| MR_1774412037_A718B3E5 | 504990 | 172 | -90.7 | 504990 | 412 | -94.1 | 504990 | 682 | -100.1 | 504990 | 148 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 991: `95160fa1-388...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `95160fa1-3881-4923-b196-e311937ea87d` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Add neighbor relationship between 3279327_2 and 3228005_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[991] topology](images/train_0991.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3228005_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228005_3
- `C3`: Press down the tilt angle  of 3228005_3 by 6 degrees
- `C4`: Adjust the azimuth of 3228005_3 by 34 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase transmission power for 3228005_3
- `C7`: Check test server and transmission issues
- `C8`: Decrease A3 Offset threshold for 3279327_2
- `C9`: Add neighbor relationship between 3220255_1 and 3228005_3
- `C10`: Increase A3 Offset threshold for 3279327_2
- `C11`: Press down the tilt angle of 3279327_2 by 10 degrees
- `C12`: Lift the tilt angle of 3279327_2 by 10 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279327_2
- `C14`: Adjust the azimuth of 3279327_2 by 50 degrees
- `C15`: Decrease transmission power for 3279327_2
- `C16`: Increase A3 Offset threshold for 3228005_3
- `C17`: Decrease transmission power for 3228005_3
- `C18`: Lift the tilt angle  of 3228005_3 by 6 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279327_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228005_3
- `C21`: Increase transmission power for 3279327_2
- `C22`: Add neighbor relationship between 3279327_2 and 3228005_3 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.503 | MS1 | 121.4656722695 | 31.1446274900 | 650 | 504990 | -83.78 | 15.60 | 322.91 | 0.14 | 2.68 | 1594 |
| 2024-09-20 22:21:32.354 | MS1 | 121.4656761081 | 31.1446190852 | 650 | 504990 | -80.95 | 17.45 | 430.33 | 0.00 | 2.47 | 1570 |
| 2024-09-20 22:21:33.471 | MS1 | 121.4656767946 | 31.1446344905 | 650 | 504990 | -82.93 | 14.06 | 425.22 | 0.19 | 2.60 | 1591 |
| 2024-09-20 22:21:34.659 | MS1 | 121.4656615591 | 31.1446368406 | 650 | 504990 | -92.57 | -0.67 | 54.54 | 0.14 | 1.40 | 1591 |
| 2024-09-20 22:21:35.993 | MS1 | 121.4656776216 | 31.1446200810 | 650 | 504990 | -87.59 | -0.83 | 50.26 | 0.17 | 1.33 | 1577 |
| 2024-09-20 22:21:36.519 | MS1 | 121.4656660812 | 31.1446218592 | 650 | 504990 | -88.79 | -2.31 | 52.77 | 0.09 | 1.36 | 1566 |
| 2024-09-20 22:21:37.576 | MS1 | 121.4656635255 | 31.1446306450 | 650 | 504990 | -85.02 | -2.84 | 68.82 | 0.12 | 1.30 | 1564 |
| 2024-09-20 22:21:38.540 | MS1 | 121.4656768599 | 31.1446312876 | 650 | 504990 | -81.37 | 13.90 | 319.25 | 0.04 | 1.21 | 1585 |
| 2024-09-20 22:21:39.766 | MS1 | 121.4656625105 | 31.1446252123 | 650 | 504990 | -76.00 | 16.94 | 305.16 | 0.05 | 1.02 | 1594 |
| 2024-09-20 22:21:40.821 | MS1 | 121.4656589226 | 31.1446181834 | 650 | 504990 | -78.52 | 12.51 | 558.64 | 0.17 | 2.79 | 1581 |
| 2024-09-20 22:21:41.757 | MS1 | 121.4656675671 | 31.1446277653 | 650 | 504990 | -76.23 | 15.99 | 419.93 | 0.12 | 2.80 | 1589 |
| 2024-09-20 22:21:42.367 | MS1 | 121.4656590206 | 31.1446276936 | 650 | 504990 | -83.24 | 12.01 | 459.20 | 0.05 | 2.30 | 1586 |

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
| 3220255 | 1 | 121.4689241084 | 31.1458478812 | 223 | 3 | 9 | 25.2 | TDD | 376 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3228005 | 3 | 121.4640349641 | 31.1509115565 | 133 | 3 | 2 | 35.9 | TDD | 693 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3232074 | 4 | 121.4679170242 | 31.1472076467 | 137 | 1 | 5 | 39.9 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3279327 | 2 | 121.4738958028 | 31.1488859663 | 21 | 12 | 10 | 24.7 | TDD | 650 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.812 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.835 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.976 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.976 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.709 | NREventA3 | measId:2;ServCellPCI:539;Se... |
| 2024-09-20 22:21:35.709 | NREventA3 | measId:2;ServCellPCI:539;Se... |
| 2024-09-20 22:21:36.709 | NREventA3 | measId:2;ServCellPCI:539;Se... |
| 2024-09-20 22:21:39.209 | NRRRCReestablishAttempt | PCI:539 |
| 2024-09-20 22:21:39.227 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.237 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.373 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.373 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220255 | 1 | 11.7453 | 13.7829 | -115.7182 | 18.0158 | 100.1960 | 0.0067 | 0.0175 |
| 2024_09_20 22:00 | 3279327 | 2 | 10.9732 | 14.0469 | -116.3331 | 9.9870 | 142.7229 | 0.0139 | 0.1786 |
| 2024_09_20 22:00 | 3228005 | 3 | 8.4447 | 11.5506 | -117.3909 | 7.4031 | 197.9603 | 0.0165 | 0.0098 |
| 2024_09_20 22:00 | 3232074 | 4 | 17.9013 | 10.7776 | -116.5155 | 17.3804 | 185.0693 | 0.0089 | 0.0120 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414022_F4EEB307 | 504990 | 650 | -92.9 | 504990 | 693 | -88.5 | 504990 | 376 | -87.1 | 504990 | 382 |
| MR_1774414022_A5FA9589 | 504990 | 693 | -88.8 | 504990 | 650 | -92.1 | 504990 | 376 | -89.7 | 504990 | 382 |
| MR_1774414022_2D5F1919 | 504990 | 693 | -85.4 | 504990 | 650 | -94.0 | 504990 | 376 | -87.6 | 504990 | 382 |
| MR_1774414022_C3FA395B | 504990 | 693 | -86.9 | 504990 | 650 | -92.1 | 504990 | 376 | -89.6 | 504990 | 382 |
| MR_1774414022_2E028F75 | 504990 | 693 | -88.4 | 504990 | 650 | -91.1 | 504990 | 376 | -89.6 | 504990 | 382 |
| MR_1774414022_B74ADF72 | 504990 | 650 | -91.9 | 504990 | 693 | -85.5 | 504990 | 376 | -88.5 | 504990 | 382 |
| MR_1774414022_88B7AAEB | 504990 | 650 | -90.9 | 504990 | 693 | -87.9 | 504990 | 376 | -87.8 | 504990 | 382 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 992: `1c1f381a-05e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1c1f381a-05eb-48d7-a89c-8432c6407ccd` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3259335_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[992] topology](images/train_0992.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3259335_1 by 5 degrees
- `C2`: Add neighbor relationship between 3259335_1 and 3218242_2
- `C3`: Increase A3 Offset threshold for 3218242_2
- `C4`: Lift the tilt angle of 3259335_1 by 5 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease A3 Offset threshold for 3259335_1
- `C7`: Increase transmission power for 3218242_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259335_1
- `C9`: Increase transmission power for 3259335_1
- `C10`: Decrease A3 Offset threshold for 3218242_2
- `C11`: Adjust the azimuth of 3218242_2 by 50 degrees
- `C12`: Adjust the azimuth of 3259335_1 by 40 degrees
- `C13`: Decrease transmission power for 3259335_1
- `C14`: Add neighbor relationship between 3279591_3 and 3218242_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218242_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218242_2
- `C17`: Press down the tilt angle  of 3218242_2 by 10 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259335_1 **← 정답**
- `C19`: Decrease transmission power for 3218242_2
- `C20`: Increase A3 Offset threshold for 3259335_1
- `C21`: Lift the tilt angle  of 3218242_2 by 10 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.885 | MS1 | 121.4656682403 | 31.1446292253 | 257 | 504990 | -86.49 | 17.08 | 314.77 | 0.06 | 2.14 | 1591 |
| 2024-09-20 22:21:32.568 | MS1 | 121.4656747986 | 31.1446357942 | 257 | 504990 | -87.71 | 13.26 | 570.48 | 0.08 | 2.04 | 1585 |
| 2024-09-20 22:21:33.341 | MS1 | 121.4656620645 | 31.1446205492 | 257 | 504990 | -86.09 | 12.85 | 309.94 | 0.11 | 2.11 | 1565 |
| 2024-09-20 22:21:34.829 | MS1 | 121.4656626883 | 31.1446352169 | 257 | 504990 | -91.64 | 13.32 | 90.47 | 0.62 | 2.04 | 664 |
| 2024-09-20 22:21:35.597 | MS1 | 121.4656677256 | 31.1446376682 | 257 | 504990 | -85.96 | 13.49 | 59.35 | 0.51 | 2.04 | 651 |
| 2024-09-20 22:21:36.294 | MS1 | 121.4656674711 | 31.1446201268 | 257 | 504990 | -87.49 | 13.04 | 90.83 | 0.66 | 2.60 | 653 |
| 2024-09-20 22:21:37.602 | MS1 | 121.4656661759 | 31.1446356602 | 257 | 504990 | -92.48 | 8.38 | 65.67 | 0.53 | 2.94 | 635 |
| 2024-09-20 22:21:38.155 | MS1 | 121.4656673973 | 31.1446225457 | 257 | 504990 | -93.53 | 8.53 | 106.27 | 0.55 | 2.78 | 606 |
| 2024-09-20 22:21:39.990 | MS1 | 121.4656708787 | 31.1446324474 | 257 | 504990 | -89.10 | 9.33 | 92.98 | 0.59 | 2.50 | 572 |
| 2024-09-20 22:21:40.904 | MS1 | 121.4656687573 | 31.1446180830 | 257 | 504990 | -92.19 | 7.67 | 536.95 | 0.02 | 2.71 | 1560 |
| 2024-09-20 22:21:41.567 | MS1 | 121.4656656035 | 31.1446290017 | 257 | 504990 | -91.06 | 8.35 | 417.01 | 0.02 | 2.53 | 1569 |
| 2024-09-20 22:21:42.759 | MS1 | 121.4656610884 | 31.1446221218 | 257 | 504990 | -89.59 | 8.72 | 537.59 | 0.16 | 2.88 | 1571 |

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
| 3218242 | 2 | 121.4709708257 | 31.1529147102 | 287 | 15 | 5 | 24.3 | TDD | 60 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3256979 | 4 | 121.4739353570 | 31.1532011795 | 308 | 0 | 4 | 19.0 | TDD | 238 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3259335 | 1 | 121.4673913027 | 31.1522755330 | 151 | 3 | 8 | 31.5 | TDD | 257 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3279591 | 3 | 121.4745531681 | 31.1508021221 | 184 | 3 | 12 | 34.8 | TDD | 70 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.556 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.679 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.679 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.399 | NREventA3 | measId:2;ServCellPCI:368;Se... |
| 2024-09-20 22:21:38.639 | NRHandoverAttempt | SourcePCI:368;SourceNR-ARFC... |
| 2024-09-20 22:21:38.676 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.691 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.805 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.805 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259335 | 1 | 17.6954 | 11.4492 | -117.0462 | 13.2973 | 185.3636 | 0.0055 | 0.0043 |
| 2024_09_20 22:00 | 3218242 | 2 | 13.8980 | 5.7716 | -117.2657 | 19.4480 | 180.8125 | 0.0045 | 0.0065 |
| 2024_09_20 22:00 | 3279591 | 3 | 7.3770 | 10.6997 | -117.2053 | 8.6000 | 86.8519 | 0.0179 | 0.0040 |
| 2024_09_20 22:00 | 3256979 | 4 | 10.2316 | 14.3179 | -117.8315 | 5.1102 | 179.7465 | 0.0022 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413160_51F17154 | 504990 | 257 | -89.7 | 504990 | 60 | -99.6 | 504990 | 70 | -98.3 | 504990 | 238 |
| MR_1774413160_7D6C2C9F | 504990 | 257 | -91.8 | 504990 | 60 | -97.3 | 504990 | 70 | -98.2 | 504990 | 238 |
| MR_1774413160_0F022706 | 504990 | 257 | -92.5 | 504990 | 60 | -98.7 | 504990 | 70 | -99.0 | 504990 | 238 |
| MR_1774413160_2CC7BED4 | 504990 | 257 | -90.5 | 504990 | 60 | -99.5 | 504990 | 70 | -99.4 | 504990 | 238 |
| MR_1774413160_9624BC15 | 504990 | 257 | -93.3 | 504990 | 60 | -99.8 | 504990 | 70 | -97.7 | 504990 | 238 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 993: `3b332364-435...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3b332364-4353-426c-ba2f-09fb64e752a1` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Add neighbor relationship between 3255499_2 and 3233164_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[993] topology](images/train_0993.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3255499_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255499_2
- `C3`: Decrease A3 Offset threshold for 3255499_2
- `C4`: Press down the tilt angle  of 3233164_3 by 3 degrees
- `C5`: Press down the tilt angle of 3255499_2 by 10 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase transmission power for 3255499_2
- `C8`: Adjust the azimuth of 3255499_2 by 50 degrees
- `C9`: Decrease transmission power for 3255499_2
- `C10`: Increase transmission power for 3233164_3
- `C11`: Adjust the azimuth of 3233164_3 by 27 degrees
- `C12`: Increase A3 Offset threshold for 3233164_3
- `C13`: Decrease A3 Offset threshold for 3233164_3
- `C14`: Decrease transmission power for 3233164_3
- `C15`: Lift the tilt angle of 3255499_2 by 10 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233164_3
- `C17`: Lift the tilt angle  of 3233164_3 by 3 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233164_3
- `C19`: Add neighbor relationship between 3219631_1 and 3233164_3
- `C20`: Check test server and transmission issues
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255499_2
- `C22`: Add neighbor relationship between 3255499_2 and 3233164_3 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.120 | MS1 | 121.4656615476 | 31.1446186882 | 676 | 504990 | -76.83 | 16.01 | 552.90 | 0.19 | 2.72 | 1578 |
| 2024-09-20 22:21:32.298 | MS1 | 121.4656673269 | 31.1446304706 | 676 | 504990 | -82.41 | 17.70 | 357.80 | 0.12 | 2.07 | 1573 |
| 2024-09-20 22:21:33.830 | MS1 | 121.4656745182 | 31.1446360683 | 676 | 504990 | -76.89 | 17.15 | 447.75 | 0.20 | 2.69 | 1565 |
| 2024-09-20 22:21:34.640 | MS1 | 121.4656624617 | 31.1446228205 | 676 | 504990 | -93.49 | -0.95 | 49.93 | 0.16 | 1.15 | 1572 |
| 2024-09-20 22:21:35.992 | MS1 | 121.4656722405 | 31.1446200607 | 676 | 504990 | -94.67 | -3.65 | 35.17 | 0.06 | 1.07 | 1583 |
| 2024-09-20 22:21:36.409 | MS1 | 121.4656726329 | 31.1446320052 | 676 | 504990 | -85.76 | -1.83 | 41.75 | 0.04 | 1.12 | 1582 |
| 2024-09-20 22:21:37.422 | MS1 | 121.4656674694 | 31.1446311558 | 676 | 504990 | -87.36 | -2.97 | 57.06 | 0.06 | 1.01 | 1585 |
| 2024-09-20 22:21:38.850 | MS1 | 121.4656678903 | 31.1446367787 | 676 | 504990 | -80.68 | 15.90 | 462.94 | 0.03 | 1.06 | 1597 |
| 2024-09-20 22:21:39.868 | MS1 | 121.4656749552 | 31.1446213988 | 676 | 504990 | -76.52 | 16.15 | 570.45 | 0.04 | 1.19 | 1567 |
| 2024-09-20 22:21:40.228 | MS1 | 121.4656694283 | 31.1446205557 | 676 | 504990 | -75.42 | 13.09 | 506.85 | 0.01 | 2.61 | 1579 |
| 2024-09-20 22:21:41.159 | MS1 | 121.4656582080 | 31.1446189520 | 676 | 504990 | -79.11 | 13.12 | 369.57 | 0.10 | 2.68 | 1579 |
| 2024-09-20 22:21:42.473 | MS1 | 121.4656645993 | 31.1446261597 | 676 | 504990 | -81.61 | 13.62 | 407.28 | 0.10 | 2.22 | 1588 |

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
| 3219631 | 1 | 121.4684066143 | 31.1496228534 | 222 | 9 | 9 | 39.0 | TDD | 913 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3228590 | 4 | 121.4688748762 | 31.1525364267 | 58 | 3 | 2 | 25.3 | TDD | 445 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3233164 | 3 | 121.4663222974 | 31.1522592377 | 157 | 0 | 6 | 37.9 | TDD | 317 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3255499 | 2 | 121.4648333508 | 31.1534043627 | 232 | 10 | 12 | 40.5 | TDD | 676 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.759 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.777 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.910 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.910 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.633 | NREventA3 | measId:2;ServCellPCI:284;Se... |
| 2024-09-20 22:21:35.633 | NREventA3 | measId:2;ServCellPCI:284;Se... |
| 2024-09-20 22:21:36.633 | NREventA3 | measId:2;ServCellPCI:284;Se... |
| 2024-09-20 22:21:39.133 | NRRRCReestablishAttempt | PCI:284 |
| 2024-09-20 22:21:39.150 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.165 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.292 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.292 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219631 | 1 | 10.2340 | 15.9602 | -115.8302 | 9.1467 | 196.0837 | 0.0110 | 0.0035 |
| 2024_09_20 22:00 | 3255499 | 2 | 10.1527 | 16.5934 | -114.3538 | 15.0041 | 189.8733 | 0.0164 | 0.1777 |
| 2024_09_20 22:00 | 3233164 | 3 | 14.5810 | 10.2903 | -114.6613 | 15.9639 | 147.1714 | 0.0051 | 0.0001 |
| 2024_09_20 22:00 | 3228590 | 4 | 10.4426 | 8.7403 | -115.9508 | 12.3879 | 147.4652 | 0.0060 | 0.0070 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414294_D99C6880 | 504990 | 676 | -92.5 | 504990 | 317 | -87.3 | 504990 | 913 | -94.7 | 504990 | 445 |
| MR_1774414294_4813270A | 504990 | 676 | -93.5 | 504990 | 317 | -87.1 | 504990 | 913 | -96.2 | 504990 | 445 |
| MR_1774414294_508760CA | 504990 | 317 | -87.7 | 504990 | 676 | -95.0 | 504990 | 913 | -96.3 | 504990 | 445 |
| MR_1774414294_944ECEB0 | 504990 | 676 | -93.6 | 504990 | 317 | -89.2 | 504990 | 913 | -96.0 | 504990 | 445 |
| MR_1774414294_E16CF598 | 504990 | 317 | -87.7 | 504990 | 676 | -93.1 | 504990 | 913 | -93.6 | 504990 | 445 |
| MR_1774414294_58418A76 | 504990 | 676 | -91.6 | 504990 | 317 | -89.3 | 504990 | 913 | -94.7 | 504990 | 445 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 994: `9239c5b5-f71...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9239c5b5-f71b-4912-afdd-9106f27281ca` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275034_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[994] topology](images/train_0994.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275034_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275034_2 **← 정답**
- `C4`: Lift the tilt angle  of 3240229_3 by 6 degrees
- `C5`: Increase transmission power for 3240229_3
- `C6`: Decrease A3 Offset threshold for 3240229_3
- `C7`: Decrease A3 Offset threshold for 3275034_2
- `C8`: Decrease transmission power for 3275034_2
- `C9`: Increase transmission power for 3275034_2
- `C10`: Press down the tilt angle  of 3240229_3 by 6 degrees
- `C11`: Decrease transmission power for 3240229_3
- `C12`: Adjust the azimuth of 3275034_2 by 19 degrees
- `C13`: Increase A3 Offset threshold for 3240229_3
- `C14`: Check test server and transmission issues
- `C15`: Adjust the azimuth of 3240229_3 by 37 degrees
- `C16`: Press down the tilt angle of 3275034_2 by 4 degrees
- `C17`: Lift the tilt angle of 3275034_2 by 4 degrees
- `C18`: Increase A3 Offset threshold for 3275034_2
- `C19`: Add neighbor relationship between 3275034_2 and 3240229_3
- `C20`: Add neighbor relationship between 3274095_12 and 3240229_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240229_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240229_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.754 | MS1 | 121.4656660290 | 31.1446332425 | 963 | 504990 | -94.24 | 14.23 | 513.45 | 0.19 | 2.49 | 1581 |
| 2024-09-20 22:21:32.543 | MS1 | 121.4656746197 | 31.1446271579 | 539 | 504990 | -94.14 | 10.40 | 513.99 | 0.06 | 2.33 | 1562 |
| 2024-09-20 22:21:33.172 | MS1 | 121.4656584029 | 31.1446219298 | 738 | 504990 | -95.64 | 12.97 | 437.81 | 0.09 | 2.04 | 1561 |
| 2024-09-20 22:21:34.453 | MS1 | 121.4656587256 | 31.1446186616 | 727 | 152650 | -92.42 | 5.42 | 54.34 | 0.10 | 1.56 | 956 |
| 2024-09-20 22:21:35.157 | MS1 | 121.4656658408 | 31.1446236987 | 320 | 152650 | -88.31 | 4.77 | 89.87 | 0.12 | 1.69 | 919 |
| 2024-09-20 22:21:36.482 | MS1 | 121.4656620865 | 31.1446274641 | 150 | 152650 | -91.19 | 2.79 | 96.88 | 0.11 | 1.68 | 929 |
| 2024-09-20 22:21:37.162 | MS1 | 121.4656667071 | 31.1446218320 | 2 | 152650 | -93.61 | 5.59 | 70.13 | 0.09 | 1.76 | 912 |
| 2024-09-20 22:21:38.977 | MS1 | 121.4656594957 | 31.1446373980 | 727 | 152650 | -90.78 | 3.66 | 105.35 | 0.02 | 1.91 | 981 |
| 2024-09-20 22:21:39.149 | MS1 | 121.4656768933 | 31.1446315237 | 320 | 152650 | -92.48 | 3.09 | 86.13 | 0.07 | 2.00 | 937 |
| 2024-09-20 22:21:40.753 | MS1 | 121.4656767184 | 31.1446212900 | 150 | 152650 | -88.03 | 6.74 | 49.76 | 0.19 | 2.15 | 1598 |
| 2024-09-20 22:21:41.707 | MS1 | 121.4656751793 | 31.1446306420 | 2 | 152650 | -90.97 | 3.77 | 60.22 | 0.19 | 2.20 | 1565 |
| 2024-09-20 22:21:42.418 | MS1 | 121.4656761009 | 31.1446281108 | 727 | 152650 | -89.67 | 7.58 | 86.73 | 0.13 | 2.16 | 1595 |

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
| 3211899 | 13 | 121.4648667806 | 31.1506606340 | 205 | 4 | 5 | 27.7 | FDD | 727 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3213381 | 6 | 121.4734556856 | 31.1507138743 | 55 | 1 | 8 | 25.1 | TDD | 539 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3216601 | 11 | 121.4677928166 | 31.1530859014 | 330 | 10 | 11 | 25.9 | FDD | 622 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3240229 | 3 | 121.4755215550 | 31.1505165179 | 272 | 5 | 4 | 15.5 | TDD | 652 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3244431 | 7 | 121.4744178743 | 31.1515127699 | 170 | 4 | 0 | 5.0 | FDD | 320 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3246987 | 10 | 121.4702556755 | 31.1479860897 | 115 | 11 | 1 | 10.3 | FDD | 621 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3253112 | 5 | 121.4644895018 | 31.1449317591 | 9 | 14 | 2 | 19.5 | TDD | 981 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3256551 | 1 | 121.4675181625 | 31.1519045299 | 59 | 12 | 8 | 6.9 | TDD | 738 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3261335 | 9 | 121.4735224654 | 31.1542596030 | 290 | 8 | 0 | 22.9 | FDD | 613 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3268091 | 4 | 121.4751260560 | 31.1456056239 | 172 | 8 | 2 | 29.7 | TDD | 436 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3274095 | 12 | 121.4649691927 | 31.1482923212 | 10 | 13 | 8 | 16.1 | FDD | 150 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3275034 | 2 | 121.4677617349 | 31.1557138357 | 170 | 3 | 5 | 14.9 | TDD | 963 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3275236 | 8 | 121.4738743202 | 31.1451107790 | 285 | 11 | 12 | 3.1 | FDD | 2 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |

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
| 2024-09-20 22:21:31.195 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.213 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.361 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.361 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.076 | NREventA2 | measId:1;ServCellPCI:698;Se... |
| 2024-09-20 22:21:35.202 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.412 | NREventA5 | measId:3;ServCellPCI:698;Se... |
| 2024-09-20 22:21:35.459 | NRHandoverAttempt | SourcePCI:698;SourceNR-ARFC... |
| 2024-09-20 22:21:35.485 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.497 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.630 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.630 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256551 | 1 | 8.9528 | 10.7356 | -114.9189 | 16.8024 | 168.2222 | 0.0091 | 0.0108 |
| 2024_09_20 22:00 | 3275034 | 2 | 8.1019 | 6.5992 | -115.9486 | 19.4941 | 177.6931 | 0.0062 | 0.0194 |
| 2024_09_20 22:00 | 3240229 | 3 | 17.3714 | 11.1034 | -115.4917 | 8.5058 | 173.3954 | 0.0092 | 0.0012 |
| 2024_09_20 22:00 | 3268091 | 4 | 18.5165 | 17.2298 | -114.2229 | 9.5158 | 104.1082 | 0.0004 | 0.0098 |
| 2024_09_20 22:00 | 3253112 | 5 | 16.4417 | 17.2744 | -115.2131 | 16.0492 | 165.1624 | 0.0133 | 0.0156 |
| 2024_09_20 22:00 | 3213381 | 6 | 19.7760 | 5.7748 | -115.1427 | 18.5659 | 159.3306 | 0.0190 | 0.0149 |
| 2024_09_20 22:00 | 3244431 | 7 | 15.7543 | 19.1929 | -116.9293 | 3.1076 | 45.5947 | 0.0001 | 0.0190 |
| 2024_09_20 22:00 | 3275236 | 8 | 15.7565 | 10.3982 | -117.5306 | 4.8796 | 26.2854 | 0.0023 | 0.0169 |
| 2024_09_20 22:00 | 3261335 | 9 | 6.6250 | 18.2748 | -115.9304 | 3.3244 | 48.9022 | 0.0164 | 0.0190 |
| 2024_09_20 22:00 | 3246987 | 10 | 6.8393 | 11.9226 | -116.1287 | 4.1227 | 59.5074 | 0.0037 | 0.0146 |
| 2024_09_20 22:00 | 3216601 | 11 | 5.3529 | 19.9242 | -115.7718 | 4.8857 | 58.0509 | 0.0040 | 0.0003 |
| 2024_09_20 22:00 | 3274095 | 12 | 7.9012 | 15.3710 | -117.1224 | 3.8193 | 46.4314 | 0.0045 | 0.0107 |
| 2024_09_20 22:00 | 3211899 | 13 | 16.1389 | 6.6781 | -114.0435 | 3.4083 | 47.3315 | 0.0173 | 0.0018 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416843_770E2A4F | 504990 | 738 | -96.9 | 504990 | 652 | -94.7 | 504990 | 436 | -95.4 | 504990 | 981 |
| MR_1774416843_E60BFBAA | 152650 | 727 | -94.0 | 152650 | 622 | -96.0 | 152650 | 621 | -100.5 | 152650 | 613 |
| MR_1774416843_BE448568 | 504990 | 738 | -95.8 | 504990 | 652 | -95.7 | 504990 | 436 | -96.4 | 504990 | 981 |
| MR_1774416843_91326A4F | 152650 | 727 | -91.0 | 152650 | 622 | -98.2 | 152650 | 621 | -99.2 | 152650 | 613 |
| MR_1774416843_2EA27EAF | 152650 | 727 | -91.7 | 152650 | 622 | -96.3 | 152650 | 621 | -100.3 | 152650 | 613 |
| MR_1774416843_3DB9CD15 | 152650 | 727 | -94.0 | 152650 | 622 | -99.4 | 152650 | 621 | -100.3 | 152650 | 613 |
| MR_1774416843_B0F79707 | 504990 | 738 | -97.1 | 504990 | 652 | -97.3 | 504990 | 436 | -98.5 | 504990 | 981 |
| MR_1774416843_CBD641A4 | 504990 | 738 | -97.1 | 504990 | 652 | -95.0 | 504990 | 436 | -98.4 | 504990 | 981 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 995: `f29e7638-744...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f29e7638-7444-4b85-8af3-8d90c9e7098d` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease A3 Offset threshold for 3243222_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[995] topology](images/train_0995.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3274098_2 by 50 degrees
- `C2`: Add neighbor relationship between 3256248_3 and 3274098_2
- `C3`: Decrease A3 Offset threshold for 3243222_1 **← 정답**
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274098_2
- `C5`: Decrease transmission power for 3274098_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243222_1
- `C7`: Increase transmission power for 3243222_1
- `C8`: Add neighbor relationship between 3243222_1 and 3274098_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243222_1
- `C10`: Press down the tilt angle  of 3274098_2 by 5 degrees
- `C11`: Press down the tilt angle of 3243222_1 by 10 degrees
- `C12`: Lift the tilt angle  of 3274098_2 by 5 degrees
- `C13`: Lift the tilt angle of 3243222_1 by 10 degrees
- `C14`: Check test server and transmission issues
- `C15`: Decrease transmission power for 3243222_1
- `C16`: Adjust the azimuth of 3243222_1 by 50 degrees
- `C17`: Increase transmission power for 3274098_2
- `C18`: Increase A3 Offset threshold for 3274098_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274098_2
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease A3 Offset threshold for 3274098_2
- `C22`: Increase A3 Offset threshold for 3243222_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.409 | MS1 | 121.4656641961 | 31.1446351535 | 592 | 504990 | -82.48 | 17.70 | 404.00 | 0.07 | 2.74 | 1598 |
| 2024-09-20 22:21:32.586 | MS1 | 121.4656657954 | 31.1446283374 | 592 | 504990 | -79.27 | 15.77 | 591.81 | 0.03 | 2.01 | 1572 |
| 2024-09-20 22:21:33.853 | MS1 | 121.4656776847 | 31.1446232185 | 592 | 504990 | -76.91 | 14.49 | 402.27 | 0.19 | 2.17 | 1576 |
| 2024-09-20 22:21:34.986 | MS1 | 121.4656649326 | 31.1446274689 | 592 | 504990 | -91.04 | -0.82 | 52.15 | 0.05 | 1.20 | 1569 |
| 2024-09-20 22:21:35.377 | MS1 | 121.4656707252 | 31.1446241909 | 592 | 504990 | -83.42 | -2.17 | 66.33 | 0.02 | 1.08 | 1574 |
| 2024-09-20 22:21:36.446 | MS1 | 121.4656640138 | 31.1446187707 | 592 | 504990 | -90.20 | -3.06 | 59.00 | 0.15 | 1.01 | 1574 |
| 2024-09-20 22:21:37.679 | MS1 | 121.4656631012 | 31.1446285629 | 592 | 504990 | -89.76 | -2.42 | 64.24 | 0.14 | 1.23 | 1569 |
| 2024-09-20 22:21:38.877 | MS1 | 121.4656613543 | 31.1446344664 | 592 | 504990 | -86.90 | -1.42 | 62.89 | 0.03 | 1.15 | 1573 |
| 2024-09-20 22:21:39.986 | MS1 | 121.4656591719 | 31.1446232862 | 50 | 504990 | -79.82 | 14.68 | 163.15 | 0.01 | 1.26 | 1599 |
| 2024-09-20 22:21:40.103 | MS1 | 121.4656656379 | 31.1446247452 | 50 | 504990 | -79.70 | 12.36 | 329.86 | 0.13 | 2.75 | 1587 |
| 2024-09-20 22:21:41.792 | MS1 | 121.4656746285 | 31.1446309625 | 50 | 504990 | -81.04 | 15.02 | 541.92 | 0.17 | 2.88 | 1593 |
| 2024-09-20 22:21:42.172 | MS1 | 121.4656695068 | 31.1446373599 | 50 | 504990 | -84.86 | 15.34 | 312.32 | 0.18 | 2.89 | 1578 |

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
| 3243222 | 1 | 121.4676776009 | 31.1455680397 | 350 | 1 | 6 | 33.4 | TDD | 592 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3254610 | 4 | 121.4747636246 | 31.1520556730 | 62 | 10 | 9 | 29.9 | TDD | 920 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3256248 | 3 | 121.4757197651 | 31.1554298633 | 308 | 4 | 11 | 16.5 | TDD | 4 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3274098 | 2 | 121.4670202770 | 31.1540305841 | 96 | 4 | 11 | 15.8 | TDD | 50 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.588 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.604 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.715 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.715 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.467 | NREventA3 | measId:2;ServCellPCI:704;Se... |
| 2024-09-20 22:21:38.707 | NRHandoverAttempt | SourcePCI:704;SourceNR-ARFC... |
| 2024-09-20 22:21:38.744 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.759 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.861 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.861 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243222 | 1 | 15.6589 | 8.6744 | -117.8563 | 5.4533 | 181.8572 | 0.0152 | 0.1278 |
| 2024_09_20 22:00 | 3274098 | 2 | 6.5131 | 19.4297 | -115.3481 | 17.8599 | 176.1244 | 0.0071 | 0.0134 |
| 2024_09_20 22:00 | 3256248 | 3 | 19.2597 | 10.6436 | -116.9784 | 8.7251 | 144.4556 | 0.0098 | 0.0152 |
| 2024_09_20 22:00 | 3254610 | 4 | 14.3230 | 16.3942 | -116.7970 | 13.1489 | 111.9274 | 0.0090 | 0.0129 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412221_5219B5CB | 504990 | 50 | -86.4 | 504990 | 592 | -89.6 | 504990 | 4 | -88.6 | 504990 | 920 |
| MR_1774412221_7A815937 | 504990 | 592 | -90.8 | 504990 | 50 | -87.7 | 504990 | 4 | -88.6 | 504990 | 920 |
| MR_1774412221_84152AC1 | 504990 | 592 | -89.4 | 504990 | 50 | -86.1 | 504990 | 4 | -89.0 | 504990 | 920 |
| MR_1774412221_00F2E338 | 504990 | 50 | -84.5 | 504990 | 592 | -90.9 | 504990 | 4 | -88.5 | 504990 | 920 |
| MR_1774412221_0E606F0F | 504990 | 592 | -90.9 | 504990 | 50 | -84.7 | 504990 | 4 | -87.1 | 504990 | 920 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 996: `21319f7e-06f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `21319f7e-06f0-40b9-b173-13a7fd9ea066` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[996] topology](images/train_0996.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3268475_1
- `C2`: Increase A3 Offset threshold for 3268767_2
- `C3`: Press down the tilt angle of 3268475_1 by 10 degrees
- `C4`: Decrease transmission power for 3268475_1
- `C5`: Decrease A3 Offset threshold for 3268475_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268475_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268767_2
- `C8`: Check test server and transmission issues
- `C9`: Decrease transmission power for 3268767_2
- `C10`: Adjust the azimuth of 3268767_2 by 23 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268475_1
- `C12`: Increase A3 Offset threshold for 3268475_1
- `C13`: Lift the tilt angle of 3268475_1 by 10 degrees
- `C14`: Add neighbor relationship between 3238813_4 and 3268767_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268767_2
- `C16`: Decrease A3 Offset threshold for 3268767_2
- `C17`: Insufficient data; more data is needed for judgment. **← 정답**
- `C18`: Press down the tilt angle  of 3268767_2 by 9 degrees
- `C19`: Adjust the azimuth of 3268475_1 by 50 degrees
- `C20`: Lift the tilt angle  of 3268767_2 by 9 degrees
- `C21`: Increase transmission power for 3268767_2
- `C22`: Add neighbor relationship between 3268475_1 and 3268767_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.302 | MS1 | 121.4656603594 | 31.1446337802 | 89 | 504990 | -87.18 | 15.84 | 348.83 | 0.19 | 2.31 | 1569 |
| 2024-09-20 22:21:32.382 | MS1 | 121.4656768028 | 31.1446277790 | 89 | 504990 | -87.37 | 16.67 | 528.53 | 0.08 | 2.49 | 1573 |
| 2024-09-20 22:21:33.836 | MS1 | 121.4656727371 | 31.1446342591 | 89 | 504990 | -88.96 | 12.06 | 334.65 | 0.00 | 2.50 | 1589 |
| 2024-09-20 22:21:34.982 | MS1 | 121.4656584781 | 31.1446337536 | 89 | 504990 | -87.13 | 14.75 | 48.02 | 0.11 | 2.28 | 1579 |
| 2024-09-20 22:21:35.723 | MS1 | 121.4656608421 | 31.1446257186 | 89 | 504990 | -88.55 | 17.45 | 64.37 | 0.16 | 2.88 | 1562 |
| 2024-09-20 22:21:36.954 | MS1 | 121.4656743560 | 31.1446206656 | 89 | 504990 | -89.90 | 17.15 | 89.48 | 0.19 | 2.23 | 1562 |
| 2024-09-20 22:21:37.479 | MS1 | 121.4656776762 | 31.1446256861 | 89 | 504990 | -89.12 | 7.96 | 69.78 | 0.06 | 2.44 | 1600 |
| 2024-09-20 22:21:38.216 | MS1 | 121.4656592054 | 31.1446309281 | 89 | 504990 | -90.56 | 11.13 | 64.23 | 0.04 | 2.97 | 1596 |
| 2024-09-20 22:21:39.704 | MS1 | 121.4656681581 | 31.1446252258 | 89 | 504990 | -93.40 | 8.39 | 57.30 | 0.14 | 2.84 | 1600 |
| 2024-09-20 22:21:40.912 | MS1 | 121.4656608267 | 31.1446337028 | 89 | 504990 | -90.00 | 11.75 | 322.56 | 0.15 | 2.54 | 1568 |
| 2024-09-20 22:21:41.474 | MS1 | 121.4656629139 | 31.1446261142 | 89 | 504990 | -93.00 | 10.86 | 318.18 | 0.16 | 2.35 | 1572 |
| 2024-09-20 22:21:42.255 | MS1 | 121.4656680982 | 31.1446375979 | 89 | 504990 | -93.06 | 11.37 | 485.79 | 0.08 | 2.94 | 1600 |

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
| 3238813 | 4 | 121.4642750408 | 31.1524810176 | 275 | 13 | 10 | 18.1 | TDD | 878 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3246020 | 3 | 121.4756428550 | 31.1496117523 | 152 | 2 | 4 | 39.1 | TDD | 261 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3268475 | 1 | 121.4734124042 | 31.1477769743 | 50 | 11 | 10 | 29.9 | TDD | 89 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3268767 | 2 | 121.4746085263 | 31.1525519180 | 201 | 7 | 7 | 45.7 | TDD | 770 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.569 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.586 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.698 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.698 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.451 | NREventA3 | measId:2;ServCellPCI:256;Se... |
| 2024-09-20 22:21:38.691 | NRHandoverAttempt | SourcePCI:256;SourceNR-ARFC... |
| 2024-09-20 22:21:38.728 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.740 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.856 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.856 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3268475 | 1 | 80.5893 | 90.9982 | -117.3006 | 18.7338 | 157.3168 | 0.0126 | 0.0179 |
| 2024_09_19 22:00 | 3268767 | 2 | 86.8971 | 76.9167 | -114.1636 | 19.2338 | 153.6816 | 0.0050 | 0.0184 |
| 2024_09_19 22:00 | 3246020 | 3 | 80.3463 | 77.0468 | -115.5390 | 5.0246 | 127.3543 | 0.0063 | 0.0052 |
| 2024_09_19 22:00 | 3238813 | 4 | 77.0063 | 87.8611 | -115.5371 | 9.8068 | 145.4064 | 0.0017 | 0.0006 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415114_B96EC7CF | 504990 | 89 | -87.3 | 504990 | 770 | -86.6 | 504990 | 878 | -100.3 | 504990 | 261 |
| MR_1774415114_C5EF12F8 | 504990 | 89 | -88.3 | 504990 | 770 | -86.1 | 504990 | 878 | -100.9 | 504990 | 261 |
| MR_1774415114_8ECA4F0B | 504990 | 89 | -88.3 | 504990 | 770 | -88.9 | 504990 | 878 | -99.1 | 504990 | 261 |
| MR_1774415114_4455BABF | 504990 | 89 | -88.8 | 504990 | 770 | -89.9 | 504990 | 878 | -100.9 | 504990 | 261 |
| MR_1774415114_49EB8284 | 504990 | 89 | -85.8 | 504990 | 770 | -86.4 | 504990 | 878 | -98.8 | 504990 | 261 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 997: `3c49e63d-4f5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3c49e63d-4f5a-476f-a148-6cf882bd8493` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3233847_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[997] topology](images/train_0997.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3233847_3
- `C2`: Add neighbor relationship between 3233847_3 and 3252364_1
- `C3`: Decrease A3 Offset threshold for 3252364_1
- `C4`: Decrease transmission power for 3233847_3
- `C5`: Decrease A3 Offset threshold for 3233847_3
- `C6`: Increase A3 Offset threshold for 3252364_1
- `C7`: Adjust the azimuth of 3252364_1 by 50 degrees
- `C8`: Lift the tilt angle  of 3252364_1 by 4 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233847_3
- `C10`: Add neighbor relationship between 3261820_4 and 3252364_1
- `C11`: Press down the tilt angle  of 3252364_1 by 4 degrees
- `C12`: Decrease transmission power for 3252364_1
- `C13`: Increase transmission power for 3252364_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252364_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252364_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233847_3 **← 정답**
- `C17`: Increase transmission power for 3233847_3
- `C18`: Check test server and transmission issues
- `C19`: Press down the tilt angle of 3233847_3 by 5 degrees
- `C20`: Lift the tilt angle of 3233847_3 by 5 degrees
- `C21`: Adjust the azimuth of 3233847_3 by 47 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.502 | MS1 | 121.4656694453 | 31.1446197854 | 629 | 504990 | -89.16 | 13.82 | 472.57 | 0.13 | 2.13 | 1566 |
| 2024-09-20 22:21:32.855 | MS1 | 121.4656604294 | 31.1446328028 | 629 | 504990 | -85.33 | 15.05 | 586.78 | 0.12 | 2.70 | 1562 |
| 2024-09-20 22:21:33.173 | MS1 | 121.4656634857 | 31.1446341707 | 629 | 504990 | -87.10 | 15.91 | 491.67 | 0.01 | 2.48 | 1584 |
| 2024-09-20 22:21:34.835 | MS1 | 121.4656748146 | 31.1446205655 | 629 | 504990 | -88.38 | 17.49 | 57.47 | 0.55 | 2.16 | 688 |
| 2024-09-20 22:21:35.178 | MS1 | 121.4656638403 | 31.1446376472 | 629 | 504990 | -91.31 | 13.56 | 103.61 | 0.69 | 2.61 | 569 |
| 2024-09-20 22:21:36.391 | MS1 | 121.4656651402 | 31.1446183701 | 629 | 504990 | -86.55 | 13.50 | 84.78 | 0.67 | 2.12 | 679 |
| 2024-09-20 22:21:37.111 | MS1 | 121.4656720550 | 31.1446239716 | 629 | 504990 | -93.40 | 12.94 | 64.37 | 0.68 | 2.18 | 665 |
| 2024-09-20 22:21:38.598 | MS1 | 121.4656626727 | 31.1446291053 | 629 | 504990 | -91.05 | 8.07 | 98.17 | 0.69 | 2.47 | 559 |
| 2024-09-20 22:21:39.493 | MS1 | 121.4656650889 | 31.1446231408 | 629 | 504990 | -90.98 | 8.09 | 60.01 | 0.55 | 2.36 | 591 |
| 2024-09-20 22:21:40.714 | MS1 | 121.4656674305 | 31.1446305504 | 629 | 504990 | -91.84 | 8.58 | 524.39 | 0.05 | 2.57 | 1594 |
| 2024-09-20 22:21:41.571 | MS1 | 121.4656694538 | 31.1446260567 | 629 | 504990 | -92.08 | 9.74 | 473.46 | 0.16 | 2.89 | 1591 |
| 2024-09-20 22:21:42.432 | MS1 | 121.4656611888 | 31.1446294959 | 629 | 504990 | -90.03 | 8.08 | 400.43 | 0.05 | 2.71 | 1580 |

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
| 3233847 | 3 | 121.4676524017 | 31.1479524343 | 160 | 0 | 1 | 36.5 | TDD | 629 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3252364 | 1 | 121.4685492611 | 31.1558048314 | 59 | 2 | 1 | 43.5 | TDD | 354 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3261820 | 4 | 121.4734153539 | 31.1465571593 | 221 | 10 | 2 | 43.6 | TDD | 871 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3276344 | 2 | 121.4712505352 | 31.1500997200 | 17 | 1 | 7 | 36.1 | TDD | 27 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.450 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.469 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.581 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.581 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.267 | NREventA3 | measId:2;ServCellPCI:660;Se... |
| 2024-09-20 22:21:38.507 | NRHandoverAttempt | SourcePCI:660;SourceNR-ARFC... |
| 2024-09-20 22:21:38.544 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.558 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.663 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.663 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252364 | 1 | 7.9262 | 18.0257 | -114.1614 | 6.7392 | 108.4473 | 0.0144 | 0.0077 |
| 2024_09_20 22:00 | 3276344 | 2 | 12.2908 | 8.5899 | -117.6047 | 12.8589 | 136.9050 | 0.0081 | 0.0149 |
| 2024_09_20 22:00 | 3233847 | 3 | 17.2478 | 8.6145 | -115.6519 | 14.0406 | 120.5448 | 0.0158 | 0.0162 |
| 2024_09_20 22:00 | 3261820 | 4 | 7.3721 | 18.5561 | -117.5383 | 5.2839 | 160.7307 | 0.0164 | 0.0175 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412560_8ECBCDC2 | 504990 | 629 | -89.8 | 504990 | 354 | -95.2 | 504990 | 871 | -98.6 | 504990 | 27 |
| MR_1774412560_C347AEA7 | 504990 | 629 | -88.8 | 504990 | 354 | -98.0 | 504990 | 871 | -99.2 | 504990 | 27 |
| MR_1774412560_6510307E | 504990 | 629 | -89.6 | 504990 | 354 | -94.8 | 504990 | 871 | -96.8 | 504990 | 27 |
| MR_1774412560_30D93EEB | 504990 | 629 | -89.4 | 504990 | 354 | -96.3 | 504990 | 871 | -97.7 | 504990 | 27 |
| MR_1774412560_725AA46E | 504990 | 629 | -88.6 | 504990 | 354 | -95.3 | 504990 | 871 | -98.9 | 504990 | 27 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 998: `488740df-e20...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `488740df-e209-4f7d-a6e9-e43f2c1a654f` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3269857_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[998] topology](images/train_0998.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3249858_2 by 50 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase transmission power for 3249858_2
- `C4`: Increase transmission power for 3269857_4
- `C5`: Decrease A3 Offset threshold for 3269857_4
- `C6`: Decrease transmission power for 3269857_4
- `C7`: Decrease A3 Offset threshold for 3249858_2
- `C8`: Increase A3 Offset threshold for 3249858_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249858_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249858_2
- `C11`: Press down the tilt angle of 3269857_4 by 3 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269857_4 **← 정답**
- `C13`: Add neighbor relationship between 3228275_1 and 3249858_2
- `C14`: Decrease transmission power for 3249858_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269857_4
- `C16`: Press down the tilt angle  of 3249858_2 by 10 degrees
- `C17`: Adjust the azimuth of 3269857_4 by 49 degrees
- `C18`: Check test server and transmission issues
- `C19`: Lift the tilt angle  of 3249858_2 by 10 degrees
- `C20`: Add neighbor relationship between 3269857_4 and 3249858_2
- `C21`: Lift the tilt angle of 3269857_4 by 3 degrees
- `C22`: Increase A3 Offset threshold for 3269857_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.989 | MS1 | 121.4656607356 | 31.1446222402 | 718 | 504990 | -91.79 | 15.11 | 569.51 | 0.12 | 2.83 | 1564 |
| 2024-09-20 22:21:32.703 | MS1 | 121.4656582516 | 31.1446366044 | 718 | 504990 | -85.20 | 15.56 | 378.28 | 0.11 | 2.41 | 1591 |
| 2024-09-20 22:21:33.262 | MS1 | 121.4656767300 | 31.1446345801 | 718 | 504990 | -91.80 | 16.66 | 319.75 | 0.08 | 2.86 | 1588 |
| 2024-09-20 22:21:34.550 | MS1 | 121.4656588753 | 31.1446330899 | 718 | 504990 | -87.71 | 13.45 | 101.36 | 0.51 | 2.02 | 627 |
| 2024-09-20 22:21:35.435 | MS1 | 121.4656613063 | 31.1446331933 | 718 | 504990 | -88.95 | 14.16 | 94.46 | 0.53 | 2.28 | 506 |
| 2024-09-20 22:21:36.970 | MS1 | 121.4656602584 | 31.1446309099 | 718 | 504990 | -87.94 | 15.69 | 56.07 | 0.65 | 2.48 | 663 |
| 2024-09-20 22:21:37.558 | MS1 | 121.4656645630 | 31.1446200935 | 718 | 504990 | -89.18 | 12.12 | 43.05 | 0.55 | 2.45 | 665 |
| 2024-09-20 22:21:38.818 | MS1 | 121.4656672715 | 31.1446309482 | 718 | 504990 | -90.99 | 12.73 | 85.88 | 0.58 | 2.20 | 622 |
| 2024-09-20 22:21:39.401 | MS1 | 121.4656690363 | 31.1446198323 | 718 | 504990 | -94.00 | 7.62 | 68.25 | 0.69 | 2.48 | 636 |
| 2024-09-20 22:21:40.916 | MS1 | 121.4656629853 | 31.1446273598 | 718 | 504990 | -93.47 | 7.24 | 505.97 | 0.09 | 2.36 | 1578 |
| 2024-09-20 22:21:41.261 | MS1 | 121.4656683893 | 31.1446300315 | 718 | 504990 | -90.05 | 9.26 | 512.02 | 0.01 | 2.90 | 1574 |
| 2024-09-20 22:21:42.811 | MS1 | 121.4656777387 | 31.1446274638 | 718 | 504990 | -90.56 | 10.45 | 509.68 | 0.03 | 2.62 | 1586 |

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
| 3228275 | 1 | 121.4646561887 | 31.1452816009 | 87 | 0 | 3 | 40.9 | TDD | 40 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3249858 | 2 | 121.4676526442 | 31.1516480770 | 17 | 14 | 10 | 46.4 | TDD | 673 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3269857 | 4 | 121.4736721218 | 31.1559322500 | 260 | 1 | 12 | 47.8 | TDD | 718 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3278044 | 3 | 121.4734240106 | 31.1511641956 | 276 | 2 | 9 | 19.0 | TDD | 499 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.524 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.544 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.653 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.653 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.344 | NREventA3 | measId:2;ServCellPCI:558;Se... |
| 2024-09-20 22:21:38.584 | NRHandoverAttempt | SourcePCI:558;SourceNR-ARFC... |
| 2024-09-20 22:21:38.615 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.628 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.766 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.766 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228275 | 1 | 7.8059 | 16.7818 | -116.2941 | 15.0464 | 83.2422 | 0.0098 | 0.0136 |
| 2024_09_20 22:00 | 3249858 | 2 | 17.0196 | 11.9998 | -117.3377 | 15.4491 | 174.7543 | 0.0065 | 0.0177 |
| 2024_09_20 22:00 | 3278044 | 3 | 16.4175 | 13.4748 | -114.8508 | 14.1036 | 96.4028 | 0.0158 | 0.0103 |
| 2024_09_20 22:00 | 3269857 | 4 | 19.0301 | 8.2022 | -117.6320 | 14.8883 | 130.0828 | 0.0017 | 0.0041 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415129_85E7398F | 504990 | 718 | -90.8 | 504990 | 673 | -90.9 | 504990 | 40 | -98.3 | 504990 | 499 |
| MR_1774415129_E85151A8 | 504990 | 718 | -88.9 | 504990 | 673 | -92.3 | 504990 | 40 | -97.8 | 504990 | 499 |
| MR_1774415129_D544785A | 504990 | 718 | -87.7 | 504990 | 673 | -91.0 | 504990 | 40 | -99.4 | 504990 | 499 |
| MR_1774415129_848A5AC6 | 504990 | 718 | -87.0 | 504990 | 673 | -92.1 | 504990 | 40 | -97.4 | 504990 | 499 |
| MR_1774415129_51360812 | 504990 | 718 | -89.7 | 504990 | 673 | -89.6 | 504990 | 40 | -99.5 | 504990 | 499 |
| MR_1774415129_3E302A9B | 504990 | 718 | -87.3 | 504990 | 673 | -92.1 | 504990 | 40 | -98.8 | 504990 | 499 |
| MR_1774415129_CD2BE65D | 504990 | 718 | -90.8 | 504990 | 673 | -92.5 | 504990 | 40 | -98.5 | 504990 | 499 |
| MR_1774415129_45C8E0FF | 504990 | 718 | -89.0 | 504990 | 673 | -93.3 | 504990 | 40 | -98.9 | 504990 | 499 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 999: `9efd162a-d5a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9efd162a-d5a4-4477-9198-0c6437f02833` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[999] topology](images/train_0999.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216638_2
- `C2`: Decrease A3 Offset threshold for 3216638_2
- `C3`: Adjust the azimuth of 3216638_2 by 50 degrees
- `C4`: Press down the tilt angle of 3216638_2 by 2 degrees
- `C5`: Insufficient data; more data is needed for judgment. **← 정답**
- `C6`: Add neighbor relationship between 3275870_1 and 3223196_4
- `C7`: Increase transmission power for 3216638_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223196_4
- `C9`: Check test server and transmission issues
- `C10`: Decrease A3 Offset threshold for 3223196_4
- `C11`: Increase A3 Offset threshold for 3223196_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223196_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216638_2
- `C14`: Decrease transmission power for 3223196_4
- `C15`: Add neighbor relationship between 3216638_2 and 3223196_4
- `C16`: Lift the tilt angle  of 3223196_4 by 3 degrees
- `C17`: Press down the tilt angle  of 3223196_4 by 3 degrees
- `C18`: Lift the tilt angle of 3216638_2 by 2 degrees
- `C19`: Decrease transmission power for 3216638_2
- `C20`: Adjust the azimuth of 3223196_4 by 50 degrees
- `C21`: Increase transmission power for 3223196_4
- `C22`: Increase A3 Offset threshold for 3216638_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.795 | MS1 | 121.4656613619 | 31.1446259761 | 660 | 504990 | -86.72 | 14.74 | 478.99 | 0.08 | 2.82 | 1579 |
| 2024-09-20 22:21:32.349 | MS1 | 121.4656671492 | 31.1446336397 | 660 | 504990 | -85.48 | 17.32 | 514.86 | 0.14 | 2.03 | 1587 |
| 2024-09-20 22:21:33.504 | MS1 | 121.4656746379 | 31.1446264968 | 660 | 504990 | -90.39 | 17.17 | 310.54 | 0.03 | 2.59 | 1564 |
| 2024-09-20 22:21:34.175 | MS1 | 121.4656660625 | 31.1446258250 | 660 | 504990 | -85.17 | 16.68 | 64.27 | 0.17 | 2.53 | 1572 |
| 2024-09-20 22:21:35.245 | MS1 | 121.4656587331 | 31.1446280327 | 660 | 504990 | -85.53 | 14.80 | 66.20 | 0.01 | 2.44 | 1567 |
| 2024-09-20 22:21:36.120 | MS1 | 121.4656636540 | 31.1446251603 | 660 | 504990 | -89.89 | 13.06 | 71.31 | 0.15 | 2.16 | 1576 |
| 2024-09-20 22:21:37.303 | MS1 | 121.4656680477 | 31.1446217524 | 660 | 504990 | -92.26 | 9.73 | 53.52 | 0.07 | 2.90 | 1575 |
| 2024-09-20 22:21:38.821 | MS1 | 121.4656734578 | 31.1446322274 | 660 | 504990 | -91.71 | 11.09 | 46.36 | 0.14 | 2.98 | 1587 |
| 2024-09-20 22:21:39.802 | MS1 | 121.4656599702 | 31.1446305587 | 660 | 504990 | -93.13 | 8.01 | 83.94 | 0.13 | 2.61 | 1584 |
| 2024-09-20 22:21:40.885 | MS1 | 121.4656646232 | 31.1446310585 | 660 | 504990 | -90.83 | 11.11 | 591.02 | 0.12 | 2.05 | 1571 |
| 2024-09-20 22:21:41.428 | MS1 | 121.4656712690 | 31.1446274985 | 660 | 504990 | -89.21 | 7.32 | 378.97 | 0.10 | 2.03 | 1593 |
| 2024-09-20 22:21:42.917 | MS1 | 121.4656647363 | 31.1446189293 | 660 | 504990 | -92.41 | 11.77 | 519.87 | 0.01 | 2.01 | 1570 |

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
| 3211489 | 3 | 121.4662775866 | 31.1450303900 | 92 | 13 | 9 | 23.2 | TDD | 229 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3216638 | 2 | 121.4715298800 | 31.1522617448 | 326 | 0 | 1 | 37.1 | TDD | 660 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3223196 | 4 | 121.4741887480 | 31.1468705214 | 144 | 1 | 4 | 32.0 | TDD | 367 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3275870 | 1 | 121.4694842564 | 31.1456423001 | 100 | 9 | 2 | 33.6 | TDD | 613 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.090 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.107 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.227 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.227 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.904 | NREventA3 | measId:2;ServCellPCI:16;Ser... |
| 2024-09-20 22:21:38.144 | NRHandoverAttempt | SourcePCI:16;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.188 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.201 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.337 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.337 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3275870 | 1 | 77.4016 | 79.7664 | -115.3103 | 12.6653 | 150.5313 | 0.0064 | 0.0108 |
| 2024_09_19 22:00 | 3216638 | 2 | 93.7536 | 85.1275 | -114.3463 | 11.3169 | 190.5667 | 0.0023 | 0.0169 |
| 2024_09_19 22:00 | 3211489 | 3 | 77.8246 | 80.4719 | -114.1551 | 12.3239 | 102.6204 | 0.0135 | 0.0002 |
| 2024_09_19 22:00 | 3223196 | 4 | 91.1824 | 83.3629 | -115.4624 | 17.8795 | 102.8997 | 0.0167 | 0.0106 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415178_7C2C36F9 | 504990 | 660 | -86.1 | 504990 | 367 | -92.8 | 504990 | 613 | -98.6 | 504990 | 229 |
| MR_1774415178_2B8E043C | 504990 | 660 | -86.9 | 504990 | 367 | -91.7 | 504990 | 613 | -97.6 | 504990 | 229 |
| MR_1774415178_F410D7A7 | 504990 | 660 | -84.5 | 504990 | 367 | -90.6 | 504990 | 613 | -98.1 | 504990 | 229 |
| MR_1774415178_9FD8FA77 | 504990 | 660 | -86.9 | 504990 | 367 | -92.7 | 504990 | 613 | -96.5 | 504990 | 229 |
| MR_1774415178_A68C2482 | 504990 | 660 | -87.0 | 504990 | 367 | -91.5 | 504990 | 613 | -95.8 | 504990 | 229 |

> *... 2개 열 생략 (전체 14열)*

---
