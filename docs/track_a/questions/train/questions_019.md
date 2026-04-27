# Track A 문제 분석 — train[180]~train[189]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[180] ~ train[189] (10개)

## 목차

1. [문제 180: `9a6e2413-cb8...`](#180) — single-answer, 정답: C5
2. [문제 181: `dba6d8a1-145...`](#181) — single-answer, 정답: C20
3. [문제 182: `4d319ef8-dea...`](#182) — multiple-answer, 정답: C11|C15
4. [문제 183: `71d68f86-081...`](#183) — single-answer, 정답: C10
5. [문제 184: `686d00df-ca9...`](#184) — single-answer, 정답: C14
6. [문제 185: `0ee6cb83-91b...`](#185) — single-answer, 정답: C12
7. [문제 186: `c237bcf3-34d...`](#186) — single-answer, 정답: C20
8. [문제 187: `23c70be7-a8c...`](#187) — single-answer, 정답: C15
9. [문제 188: `a5ee85a0-fd2...`](#188) — single-answer, 정답: C13
10. [문제 189: `20c666b1-f59...`](#189) — single-answer, 정답: C9

---

### 문제 180: `9a6e2413-cb8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9a6e2413-cb84-40ee-8412-e5f7ce1ab8ea` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[180] topology](images/train_0180.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3245435_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245435_2
- `C3`: Decrease A3 Offset threshold for 3245435_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240376_4
- `C5`: Check test server and transmission issues **← 정답**
- `C6`: Decrease A3 Offset threshold for 3240376_4
- `C7`: Lift the tilt angle of 3240376_4 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240376_4
- `C9`: Increase transmission power for 3240376_4
- `C10`: Adjust the azimuth of 3245435_2 by 12 degrees
- `C11`: Lift the tilt angle  of 3245435_2 by 10 degrees
- `C12`: Increase A3 Offset threshold for 3245435_2
- `C13`: Increase transmission power for 3245435_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245435_2
- `C15`: Add neighbor relationship between 3278177_1 and 3245435_2
- `C16`: Press down the tilt angle  of 3245435_2 by 10 degrees
- `C17`: Adjust the azimuth of 3240376_4 by 50 degrees
- `C18`: Press down the tilt angle of 3240376_4 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3240376_4
- `C20`: Add neighbor relationship between 3240376_4 and 3245435_2
- `C21`: Decrease transmission power for 3240376_4
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.670 | MS1 | 121.4656621275 | 31.1446352546 | 221 | 504990 | -90.05 | 17.50 | 411.35 | 0.07 | 2.42 | 1576 |
| 2024-09-20 22:21:32.821 | MS1 | 121.4656770361 | 31.1446362302 | 221 | 504990 | -89.07 | 15.05 | 509.57 | 0.05 | 2.81 | 1598 |
| 2024-09-20 22:21:33.660 | MS1 | 121.4656736816 | 31.1446261382 | 221 | 504990 | -89.87 | 12.47 | 550.05 | 0.11 | 2.18 | 1570 |
| 2024-09-20 22:21:34.949 | MS1 | 121.4656711234 | 31.1446326069 | 221 | 504990 | -87.00 | 13.12 | 77.01 | 0.12 | 2.04 | 371 |
| 2024-09-20 22:21:35.347 | MS1 | 121.4656718819 | 31.1446335939 | 221 | 504990 | -90.31 | 14.06 | 94.32 | 0.16 | 2.27 | 364 |
| 2024-09-20 22:21:36.423 | MS1 | 121.4656686172 | 31.1446206924 | 221 | 504990 | -85.88 | 13.04 | 56.19 | 0.06 | 2.12 | 412 |
| 2024-09-20 22:21:37.377 | MS1 | 121.4656759917 | 31.1446234442 | 221 | 504990 | -89.76 | 9.74 | 89.99 | 0.07 | 2.66 | 391 |
| 2024-09-20 22:21:38.375 | MS1 | 121.4656672989 | 31.1446213809 | 221 | 504990 | -89.75 | 10.39 | 49.36 | 0.01 | 2.13 | 333 |
| 2024-09-20 22:21:39.833 | MS1 | 121.4656644447 | 31.1446331595 | 221 | 504990 | -92.57 | 8.40 | 75.35 | 0.13 | 2.96 | 378 |
| 2024-09-20 22:21:40.935 | MS1 | 121.4656690651 | 31.1446211648 | 221 | 504990 | -90.37 | 7.33 | 606.20 | 0.05 | 2.54 | 1564 |
| 2024-09-20 22:21:41.561 | MS1 | 121.4656677923 | 31.1446311426 | 221 | 504990 | -91.95 | 7.70 | 432.34 | 0.14 | 2.02 | 1578 |
| 2024-09-20 22:21:42.407 | MS1 | 121.4656645184 | 31.1446215715 | 221 | 504990 | -91.43 | 12.84 | 589.92 | 0.18 | 2.89 | 1562 |

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
| 3240376 | 4 | 121.4697834241 | 31.1547685948 | 127 | 14 | 5 | 42.8 | TDD | 221 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3240668 | 3 | 121.4735192610 | 31.1506224826 | 156 | 8 | 3 | 24.5 | TDD | 908 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3245435 | 2 | 121.4649430073 | 31.1455056600 | 157 | 7 | 8 | 43.6 | TDD | 644 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3278177 | 1 | 121.4671988644 | 31.1509596654 | 27 | 0 | 10 | 28.5 | TDD | 136 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.677 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.695 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.807 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.807 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.493 | NREventA3 | measId:2;ServCellPCI:637;Se... |
| 2024-09-20 22:21:38.733 | NRHandoverAttempt | SourcePCI:637;SourceNR-ARFC... |
| 2024-09-20 22:21:38.767 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.777 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.905 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.905 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278177 | 1 | 17.3062 | 11.0808 | -114.3486 | 16.6859 | 94.4072 | 0.0099 | 0.0186 |
| 2024_09_20 22:00 | 3245435 | 2 | 15.4410 | 17.4457 | -116.6561 | 15.1903 | 139.6667 | 0.0022 | 0.0041 |
| 2024_09_20 22:00 | 3240668 | 3 | 9.8174 | 11.1294 | -115.0202 | 6.3816 | 110.2825 | 0.0105 | 0.0119 |
| 2024_09_20 22:00 | 3240376 | 4 | 19.0220 | 17.9388 | -117.9292 | 12.8699 | 138.6155 | 0.0100 | 0.0113 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412835_FC97E0A4 | 504990 | 221 | -86.9 | 504990 | 644 | -87.2 | 504990 | 136 | -99.5 | 504990 | 908 |
| MR_1774412835_60813235 | 504990 | 221 | -86.0 | 504990 | 644 | -90.0 | 504990 | 136 | -100.4 | 504990 | 908 |
| MR_1774412835_172B04CF | 504990 | 221 | -87.5 | 504990 | 644 | -90.1 | 504990 | 136 | -98.3 | 504990 | 908 |
| MR_1774412835_B784609C | 504990 | 221 | -87.1 | 504990 | 644 | -88.4 | 504990 | 136 | -97.3 | 504990 | 908 |
| MR_1774412835_F78EAB96 | 504990 | 221 | -87.7 | 504990 | 644 | -89.5 | 504990 | 136 | -96.7 | 504990 | 908 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 181: `dba6d8a1-145...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dba6d8a1-145d-4a3d-a930-5fea498a584f` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[181] topology](images/train_0181.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253111_2
- `C2`: Increase A3 Offset threshold for 3253111_2
- `C3`: Lift the tilt angle  of 3217090_1 by 10 degrees
- `C4`: Decrease transmission power for 3217090_1
- `C5`: Press down the tilt angle  of 3217090_1 by 10 degrees
- `C6`: Increase transmission power for 3217090_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217090_1
- `C8`: Add neighbor relationship between 3253111_2 and 3217090_1
- `C9`: Decrease A3 Offset threshold for 3217090_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253111_2
- `C11`: Increase transmission power for 3253111_2
- `C12`: Lift the tilt angle of 3253111_2 by 6 degrees
- `C13`: Decrease A3 Offset threshold for 3253111_2
- `C14`: Add neighbor relationship between 3264917_4 and 3217090_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217090_1
- `C16`: Increase A3 Offset threshold for 3217090_1
- `C17`: Adjust the azimuth of 3253111_2 by 50 degrees
- `C18`: Press down the tilt angle of 3253111_2 by 6 degrees
- `C19`: Adjust the azimuth of 3217090_1 by 7 degrees
- `C20`: Insufficient data; more data is needed for judgment. **← 정답**
- `C21`: Decrease transmission power for 3253111_2
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.229 | MS1 | 121.4656662293 | 31.1446316235 | 891 | 504990 | -90.82 | 17.65 | 532.18 | 0.06 | 2.49 | 1566 |
| 2024-09-20 22:21:32.750 | MS1 | 121.4656714126 | 31.1446308346 | 891 | 504990 | -87.71 | 12.58 | 564.65 | 0.01 | 2.43 | 1598 |
| 2024-09-20 22:21:33.428 | MS1 | 121.4656729594 | 31.1446375795 | 891 | 504990 | -88.91 | 17.99 | 550.92 | 0.14 | 2.25 | 1580 |
| 2024-09-20 22:21:34.558 | MS1 | 121.4656646944 | 31.1446327090 | 891 | 504990 | -87.46 | 12.28 | 48.92 | 0.19 | 2.67 | 1595 |
| 2024-09-20 22:21:35.699 | MS1 | 121.4656674205 | 31.1446323134 | 891 | 504990 | -85.22 | 14.72 | 75.87 | 0.15 | 2.93 | 1578 |
| 2024-09-20 22:21:36.157 | MS1 | 121.4656652831 | 31.1446272040 | 891 | 504990 | -91.98 | 17.27 | 86.33 | 0.10 | 2.40 | 1578 |
| 2024-09-20 22:21:37.109 | MS1 | 121.4656726057 | 31.1446306150 | 891 | 504990 | -92.11 | 9.50 | 48.53 | 0.06 | 2.27 | 1596 |
| 2024-09-20 22:21:38.151 | MS1 | 121.4656647716 | 31.1446196986 | 891 | 504990 | -91.51 | 8.27 | 99.96 | 0.12 | 2.81 | 1574 |
| 2024-09-20 22:21:39.995 | MS1 | 121.4656628215 | 31.1446314536 | 891 | 504990 | -91.86 | 8.96 | 96.23 | 0.17 | 2.21 | 1574 |
| 2024-09-20 22:21:40.981 | MS1 | 121.4656639810 | 31.1446332152 | 891 | 504990 | -92.72 | 8.38 | 309.76 | 0.04 | 2.53 | 1572 |
| 2024-09-20 22:21:41.307 | MS1 | 121.4656645983 | 31.1446372867 | 891 | 504990 | -89.10 | 7.54 | 371.94 | 0.02 | 2.30 | 1567 |
| 2024-09-20 22:21:42.609 | MS1 | 121.4656633430 | 31.1446198851 | 891 | 504990 | -89.76 | 12.76 | 591.43 | 0.11 | 2.50 | 1588 |

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
| 3217090 | 1 | 121.4647564912 | 31.1487865602 | 176 | 15 | 7 | 24.4 | TDD | 931 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3220446 | 3 | 121.4663112550 | 31.1501422654 | 23 | 14 | 0 | 36.7 | TDD | 677 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3253111 | 2 | 121.4742751055 | 31.1472312256 | 49 | 4 | 12 | 36.7 | TDD | 891 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3264917 | 4 | 121.4645108669 | 31.1473236287 | 10 | 1 | 5 | 23.0 | TDD | 399 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.145 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.163 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.269 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.269 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.015 | NREventA3 | measId:2;ServCellPCI:404;Se... |
| 2024-09-20 22:21:38.255 | NRHandoverAttempt | SourcePCI:404;SourceNR-ARFC... |
| 2024-09-20 22:21:38.295 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.308 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.450 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.450 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3217090 | 1 | 79.5061 | 81.7047 | -115.4729 | 15.2740 | 134.8930 | 0.0059 | 0.0120 |
| 2024_09_19 22:00 | 3253111 | 2 | 76.0185 | 93.1255 | -114.8953 | 9.0330 | 143.9645 | 0.0037 | 0.0045 |
| 2024_09_19 22:00 | 3220446 | 3 | 83.2328 | 88.0753 | -114.5183 | 16.2287 | 196.2056 | 0.0163 | 0.0112 |
| 2024_09_19 22:00 | 3264917 | 4 | 87.1901 | 89.1961 | -117.8955 | 11.5732 | 196.3880 | 0.0005 | 0.0031 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415799_917F1C37 | 504990 | 891 | -86.8 | 504990 | 931 | -95.1 | 504990 | 399 | -101.6 | 504990 | 677 |
| MR_1774415799_34209FCD | 504990 | 891 | -88.3 | 504990 | 931 | -98.4 | 504990 | 399 | -101.1 | 504990 | 677 |
| MR_1774415799_C7553C20 | 504990 | 891 | -87.8 | 504990 | 931 | -96.5 | 504990 | 399 | -101.6 | 504990 | 677 |
| MR_1774415799_37D4F5EA | 504990 | 891 | -87.7 | 504990 | 931 | -98.7 | 504990 | 399 | -103.4 | 504990 | 677 |
| MR_1774415799_74B94D4F | 504990 | 891 | -85.9 | 504990 | 931 | -98.4 | 504990 | 399 | -103.0 | 504990 | 677 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 182: `4d319ef8-dea...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4d319ef8-dea9-49e2-97a5-8f71e7362789` |
| Tag | **multiple-answer** |
| 정답 | **C11|C15** |
| C11 의미 | Adjust the azimuth of 3244693_4 by 50 degrees |
| C15 의미 | Increase transmission power for 3244693_4 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[182] topology](images/train_0182.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277468_1
- `C2`: Increase A3 Offset threshold for 3277468_1
- `C3`: Increase transmission power for 3277468_1
- `C4`: Decrease transmission power for 3244693_4
- `C5`: Increase A3 Offset threshold for 3244693_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease A3 Offset threshold for 3277468_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244693_4
- `C9`: Press down the tilt angle of 3244693_4 by 10 degrees
- `C10`: Decrease transmission power for 3277468_1
- `C11`: Adjust the azimuth of 3244693_4 by 50 degrees **← 정답**
- `C12`: Check test server and transmission issues
- `C13`: Adjust the azimuth of 3277468_1 by 15 degrees
- `C14`: Lift the tilt angle  of 3277468_1 by 4 degrees
- `C15`: Increase transmission power for 3244693_4 **← 정답**
- `C16`: Add neighbor relationship between 3274552_3 and 3277468_1
- `C17`: Lift the tilt angle of 3244693_4 by 10 degrees
- `C18`: Add neighbor relationship between 3244693_4 and 3277468_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244693_4
- `C20`: Decrease A3 Offset threshold for 3244693_4
- `C21`: Press down the tilt angle  of 3277468_1 by 4 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277468_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.331 | MS1 | 121.4656609573 | 31.1446273494 | 430 | 504990 | -89.67 | 14.10 | 340.79 | 0.08 | 2.59 | 1581 |
| 2024-09-20 22:21:32.468 | MS1 | 121.4656677128 | 31.1446250704 | 430 | 504990 | -93.52 | 12.56 | 427.51 | 0.16 | 2.97 | 1568 |
| 2024-09-20 22:21:33.483 | MS1 | 121.4656756377 | 31.1446354776 | 430 | 504990 | -93.47 | 16.59 | 318.46 | 0.20 | 2.83 | 1560 |
| 2024-09-20 22:21:34.707 | MS1 | 121.4656641772 | 31.1446211501 | 430 | 504990 | -108.10 | -1.18 | 36.41 | 0.16 | 1.14 | 1593 |
| 2024-09-20 22:21:35.698 | MS1 | 121.4656616100 | 31.1446237470 | 430 | 504990 | -102.46 | -1.22 | 26.21 | 0.04 | 1.10 | 1570 |
| 2024-09-20 22:21:36.386 | MS1 | 121.4656715667 | 31.1446243442 | 430 | 504990 | -107.84 | -1.14 | 22.68 | 0.04 | 1.29 | 1590 |
| 2024-09-20 22:21:37.937 | MS1 | 121.4656719509 | 31.1446209704 | 430 | 504990 | -105.08 | -0.88 | 69.00 | 0.20 | 1.24 | 1569 |
| 2024-09-20 22:21:38.555 | MS1 | 121.4656639214 | 31.1446271172 | 430 | 504990 | -102.40 | 1.67 | 62.43 | 0.07 | 1.19 | 1574 |
| 2024-09-20 22:21:39.272 | MS1 | 121.4656642828 | 31.1446307461 | 430 | 504990 | -109.15 | 1.25 | 44.18 | 0.11 | 1.46 | 1587 |
| 2024-09-20 22:21:40.623 | MS1 | 121.4656767378 | 31.1446248853 | 430 | 504990 | -91.92 | 15.18 | 352.09 | 0.02 | 2.68 | 1572 |
| 2024-09-20 22:21:41.451 | MS1 | 121.4656643851 | 31.1446196077 | 430 | 504990 | -85.56 | 12.01 | 327.93 | 0.01 | 2.79 | 1591 |
| 2024-09-20 22:21:42.266 | MS1 | 121.4656698156 | 31.1446261214 | 430 | 504990 | -86.48 | 17.50 | 436.24 | 0.12 | 2.66 | 1567 |

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
| 3244693 | 4 | 121.4672066557 | 31.1484704225 | 131 | 12 | 9 | 19.6 | TDD | 430 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3262507 | 2 | 121.4698763026 | 31.1441611113 | 10 | 13 | 4 | 43.6 | TDD | 76 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3274552 | 3 | 121.4741796625 | 31.1470658760 | 179 | 5 | 7 | 22.6 | TDD | 693 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3277468 | 1 | 121.4731274892 | 31.1485379438 | 253 | 2 | 4 | 26.2 | TDD | 994 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.793 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.818 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.949 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.949 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.119 | NREventA2 | measId:1;ServCellPCI:553;Se... |
| 2024-09-20 22:21:34.221 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277468 | 1 | 5.7944 | 15.4588 | -116.1586 | 12.5806 | 158.1009 | 0.0151 | 0.0052 |
| 2024_09_20 22:00 | 3262507 | 2 | 6.7570 | 13.3001 | -115.1242 | 14.5283 | 85.5425 | 0.0039 | 0.0106 |
| 2024_09_20 22:00 | 3274552 | 3 | 12.8586 | 18.9887 | -115.9669 | 14.6873 | 161.3985 | 0.0018 | 0.0019 |
| 2024_09_20 22:00 | 3244693 | 4 | 7.5960 | 16.5883 | -115.8145 | 15.7227 | 121.4114 | 0.1172 | 0.0180 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416553_9086E26A | 504990 | 430 | -108.8 | 504990 | 994 | -112.5 | 504990 | 693 | -117.6 | 504990 | 76 |
| MR_1774416553_EC56CB9B | 504990 | 430 | -109.0 | 504990 | 994 | -110.8 | 504990 | 693 | -115.8 | 504990 | 76 |
| MR_1774416553_3771E7E7 | 504990 | 430 | -107.2 | 504990 | 994 | -110.8 | 504990 | 693 | -116.0 | 504990 | 76 |
| MR_1774416553_424683C1 | 504990 | 430 | -108.0 | 504990 | 994 | -110.5 | 504990 | 693 | -117.5 | 504990 | 76 |
| MR_1774416553_094D8D97 | 504990 | 430 | -107.9 | 504990 | 994 | -111.7 | 504990 | 693 | -114.7 | 504990 | 76 |
| MR_1774416553_B671B769 | 504990 | 430 | -107.7 | 504990 | 994 | -112.3 | 504990 | 693 | -115.8 | 504990 | 76 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 183: `71d68f86-081...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `71d68f86-0815-4c3d-9403-8830533a32a0` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease A3 Offset threshold for 3258148_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[183] topology](images/train_0183.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3258148_2 by 23 degrees
- `C2`: Decrease transmission power for 3258148_2
- `C3`: Decrease transmission power for 3210448_1
- `C4`: Increase transmission power for 3210448_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210448_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258148_2
- `C7`: Add neighbor relationship between 3255339_3 and 3210448_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210448_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease A3 Offset threshold for 3258148_2 **← 정답**
- `C11`: Press down the tilt angle  of 3210448_1 by 10 degrees
- `C12`: Press down the tilt angle of 3258148_2 by 10 degrees
- `C13`: Increase A3 Offset threshold for 3210448_1
- `C14`: Check test server and transmission issues
- `C15`: Add neighbor relationship between 3258148_2 and 3210448_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258148_2
- `C17`: Lift the tilt angle of 3258148_2 by 10 degrees
- `C18`: Increase transmission power for 3258148_2
- `C19`: Increase A3 Offset threshold for 3258148_2
- `C20`: Decrease A3 Offset threshold for 3210448_1
- `C21`: Lift the tilt angle  of 3210448_1 by 10 degrees
- `C22`: Adjust the azimuth of 3210448_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.449 | MS1 | 121.4656646390 | 31.1446264239 | 396 | 504990 | -77.96 | 15.04 | 496.64 | 0.01 | 2.51 | 1599 |
| 2024-09-20 22:21:32.418 | MS1 | 121.4656614269 | 31.1446221245 | 396 | 504990 | -83.01 | 16.27 | 552.34 | 0.00 | 2.16 | 1595 |
| 2024-09-20 22:21:33.274 | MS1 | 121.4656582258 | 31.1446261046 | 396 | 504990 | -78.21 | 17.55 | 377.12 | 0.00 | 2.67 | 1600 |
| 2024-09-20 22:21:34.246 | MS1 | 121.4656757910 | 31.1446366496 | 396 | 504990 | -87.42 | -2.11 | 71.53 | 0.06 | 1.17 | 1566 |
| 2024-09-20 22:21:35.229 | MS1 | 121.4656755976 | 31.1446308392 | 396 | 504990 | -85.58 | -3.48 | 43.35 | 0.10 | 1.37 | 1583 |
| 2024-09-20 22:21:36.490 | MS1 | 121.4656590201 | 31.1446347255 | 396 | 504990 | -90.16 | -0.63 | 52.46 | 0.10 | 1.41 | 1576 |
| 2024-09-20 22:21:37.382 | MS1 | 121.4656766837 | 31.1446282611 | 396 | 504990 | -91.73 | -1.82 | 49.32 | 0.13 | 1.48 | 1579 |
| 2024-09-20 22:21:38.327 | MS1 | 121.4656600001 | 31.1446322309 | 396 | 504990 | -86.64 | -1.55 | 48.24 | 0.17 | 1.43 | 1563 |
| 2024-09-20 22:21:39.396 | MS1 | 121.4656764049 | 31.1446307802 | 850 | 504990 | -75.08 | 15.44 | 286.81 | 0.15 | 1.43 | 1577 |
| 2024-09-20 22:21:40.726 | MS1 | 121.4656681193 | 31.1446369330 | 850 | 504990 | -81.97 | 12.21 | 555.81 | 0.16 | 2.73 | 1584 |
| 2024-09-20 22:21:41.531 | MS1 | 121.4656714654 | 31.1446187953 | 850 | 504990 | -79.82 | 16.93 | 439.40 | 0.16 | 2.64 | 1570 |
| 2024-09-20 22:21:42.905 | MS1 | 121.4656644897 | 31.1446336779 | 850 | 504990 | -82.94 | 14.13 | 394.29 | 0.19 | 2.28 | 1580 |

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
| 3210448 | 1 | 121.4658823400 | 31.1457538995 | 126 | 13 | 3 | 29.6 | TDD | 850 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3215677 | 4 | 121.4674622973 | 31.1505016459 | 183 | 6 | 9 | 40.3 | TDD | 39 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3255339 | 3 | 121.4652352273 | 31.1553928962 | 200 | 12 | 12 | 25.9 | TDD | 718 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3258148 | 2 | 121.4677724522 | 31.1477522126 | 187 | 10 | 9 | 40.1 | TDD | 396 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.492 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.607 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.607 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.372 | NREventA3 | measId:2;ServCellPCI:757;Se... |
| 2024-09-20 22:21:38.612 | NRHandoverAttempt | SourcePCI:757;SourceNR-ARFC... |
| 2024-09-20 22:21:38.653 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.665 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.791 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.791 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210448 | 1 | 12.5562 | 19.0933 | -114.6781 | 17.8577 | 82.1477 | 0.0180 | 0.0096 |
| 2024_09_20 22:00 | 3258148 | 2 | 14.5297 | 12.9349 | -115.2845 | 7.4433 | 142.7405 | 0.0113 | 0.1961 |
| 2024_09_20 22:00 | 3255339 | 3 | 19.1538 | 13.9330 | -117.0369 | 9.6072 | 197.1204 | 0.0171 | 0.0011 |
| 2024_09_20 22:00 | 3215677 | 4 | 14.6977 | 10.3707 | -116.7810 | 19.7045 | 85.0910 | 0.0053 | 0.0048 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414203_887502BD | 504990 | 850 | -83.9 | 504990 | 396 | -87.3 | 504990 | 718 | -82.4 | 504990 | 39 |
| MR_1774414203_BE1C6B7F | 504990 | 396 | -87.6 | 504990 | 850 | -83.7 | 504990 | 718 | -83.5 | 504990 | 39 |
| MR_1774414203_60F4F3C7 | 504990 | 396 | -88.2 | 504990 | 850 | -82.0 | 504990 | 718 | -83.6 | 504990 | 39 |
| MR_1774414203_EDE12D56 | 504990 | 396 | -88.2 | 504990 | 850 | -80.5 | 504990 | 718 | -83.6 | 504990 | 39 |
| MR_1774414203_E175324C | 504990 | 850 | -83.3 | 504990 | 396 | -88.5 | 504990 | 718 | -80.4 | 504990 | 39 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 184: `686d00df-ca9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `686d00df-ca9a-480c-bed9-01f5a0c9911b` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Lift the tilt angle  of 3241172_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[184] topology](images/train_0184.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3232575_1 by 4 degrees
- `C2`: Press down the tilt angle  of 3241172_2 by 10 degrees
- `C3`: Increase transmission power for 3232575_1
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232575_1
- `C6`: Adjust the azimuth of 3232575_1 by 12 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276760_3
- `C8`: Decrease A3 Offset threshold for 3232575_1
- `C9`: Check test server and transmission issues
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232575_1
- `C11`: Add neighbor relationship between 3232575_1 and 3276760_3
- `C12`: Decrease transmission power for 3232575_1
- `C13`: Decrease transmission power for 3276760_3
- `C14`: Lift the tilt angle  of 3241172_2 by 10 degrees **← 정답**
- `C15`: Increase A3 Offset threshold for 3276760_3
- `C16`: Decrease A3 Offset threshold for 3276760_3
- `C17`: Press down the tilt angle of 3232575_1 by 4 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276760_3
- `C19`: Adjust the azimuth of 3241172_2 by 50 degrees
- `C20`: Increase A3 Offset threshold for 3232575_1
- `C21`: Add neighbor relationship between 3241172_2 and 3276760_3
- `C22`: Increase transmission power for 3276760_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.120 | MS1 | 121.4656767051 | 31.1446330286 | 697 | 504990 | -88.27 | 17.19 | 538.40 | 0.09 | 2.85 | 1586 |
| 2024-09-20 22:21:32.971 | MS1 | 121.4656613189 | 31.1446279162 | 697 | 504990 | -86.58 | 14.39 | 433.24 | 0.10 | 2.76 | 1571 |
| 2024-09-20 22:21:33.349 | MS1 | 121.4656653450 | 31.1446351318 | 697 | 504990 | -86.53 | 13.55 | 358.53 | 0.06 | 2.71 | 1596 |
| 2024-09-20 22:21:34.431 | MS1 | 121.4656654682 | 31.1446377116 | 697 | 504990 | -85.35 | 14.50 | 68.47 | 0.20 | 2.49 | 1567 |
| 2024-09-20 22:21:35.208 | MS1 | 121.4656759193 | 31.1446304773 | 697 | 504990 | -88.95 | 12.67 | 43.72 | 0.04 | 2.01 | 1563 |
| 2024-09-20 22:21:36.411 | MS1 | 121.4656611364 | 31.1446237685 | 697 | 504990 | -87.99 | 14.41 | 70.23 | 0.09 | 2.22 | 1585 |
| 2024-09-20 22:21:37.244 | MS1 | 121.4656730688 | 31.1446318026 | 697 | 504990 | -89.93 | 10.86 | 70.76 | 0.04 | 2.31 | 1578 |
| 2024-09-20 22:21:38.208 | MS1 | 121.4656641171 | 31.1446310852 | 697 | 504990 | -91.91 | 11.58 | 91.67 | 0.13 | 2.13 | 1593 |
| 2024-09-20 22:21:39.601 | MS1 | 121.4656775141 | 31.1446331725 | 697 | 504990 | -92.85 | 12.41 | 47.76 | 0.06 | 2.64 | 1584 |
| 2024-09-20 22:21:40.936 | MS1 | 121.4656616418 | 31.1446256285 | 697 | 504990 | -89.25 | 9.39 | 515.56 | 0.10 | 2.24 | 1595 |
| 2024-09-20 22:21:41.889 | MS1 | 121.4656625411 | 31.1446252631 | 697 | 504990 | -89.97 | 10.12 | 405.29 | 0.05 | 2.53 | 1587 |
| 2024-09-20 22:21:42.543 | MS1 | 121.4656771165 | 31.1446351350 | 697 | 504990 | -90.25 | 8.12 | 592.69 | 0.12 | 2.61 | 1583 |

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
| 3232575 | 1 | 121.4751017440 | 31.1481920333 | 234 | 3 | 5 | 25.2 | TDD | 697 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3241172 | 2 | 121.4744725461 | 31.1554145821 | 52 | 4 | 4 | 18.4 | TDD | 244 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3242986 | 4 | 121.4731247674 | 31.1540692391 | 64 | 9 | 9 | 38.3 | TDD | 316 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3276760 | 3 | 121.4645166308 | 31.1502905988 | 3 | 10 | 1 | 49.4 | TDD | 333 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.192 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.217 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.346 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.346 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.053 | NREventA3 | measId:2;ServCellPCI:988;Se... |
| 2024-09-20 22:21:38.293 | NRHandoverAttempt | SourcePCI:988;SourceNR-ARFC... |
| 2024-09-20 22:21:38.334 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.349 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.466 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.466 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232575 | 1 | 79.7836 | 94.4604 | -117.8968 | 12.2929 | 157.6182 | 0.0108 | 0.0191 |
| 2024_09_20 22:00 | 3241172 | 2 | 13.8297 | 7.6650 | -116.1965 | 10.8808 | 182.0896 | 0.0045 | 0.0164 |
| 2024_09_20 22:00 | 3276760 | 3 | 11.7119 | 7.7888 | -114.2338 | 15.2974 | 194.3324 | 0.0113 | 0.0028 |
| 2024_09_20 22:00 | 3242986 | 4 | 7.4257 | 19.2073 | -114.5535 | 8.0868 | 170.8736 | 0.0078 | 0.0156 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412096_02B858FE | 504990 | 697 | -86.9 | 504990 | 333 | -90.9 | 504990 | 244 | -94.1 | 504990 | 316 |
| MR_1774412096_89ED1050 | 504990 | 697 | -85.4 | 504990 | 333 | -90.1 | 504990 | 244 | -94.9 | 504990 | 316 |
| MR_1774412096_A1E6A1A9 | 504990 | 697 | -83.6 | 504990 | 333 | -89.2 | 504990 | 244 | -91.9 | 504990 | 316 |
| MR_1774412096_017EF65A | 504990 | 697 | -85.4 | 504990 | 333 | -90.5 | 504990 | 244 | -92.0 | 504990 | 316 |
| MR_1774412096_8FF057D2 | 504990 | 697 | -84.1 | 504990 | 333 | -91.8 | 504990 | 244 | -93.7 | 504990 | 316 |
| MR_1774412096_55ACC751 | 504990 | 697 | -85.4 | 504990 | 333 | -89.5 | 504990 | 244 | -92.4 | 504990 | 316 |
| MR_1774412096_9B7BEF65 | 504990 | 697 | -85.5 | 504990 | 333 | -91.7 | 504990 | 244 | -94.4 | 504990 | 316 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 185: `0ee6cb83-91b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0ee6cb83-91b2-4d57-9b08-4b28e52a9c65` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[185] topology](images/train_0185.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3210182_2 by 8 degrees
- `C2`: Decrease transmission power for 3210182_2
- `C3`: Increase A3 Offset threshold for 3213276_1
- `C4`: Increase transmission power for 3210182_2
- `C5`: Increase A3 Offset threshold for 3210182_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210182_2
- `C7`: Add neighbor relationship between 3210182_2 and 3213276_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210182_2
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Increase transmission power for 3213276_1
- `C11`: Lift the tilt angle of 3210182_2 by 8 degrees
- `C12`: Check test server and transmission issues **← 정답**
- `C13`: Lift the tilt angle  of 3213276_1 by 10 degrees
- `C14`: Decrease A3 Offset threshold for 3210182_2
- `C15`: Press down the tilt angle  of 3213276_1 by 10 degrees
- `C16`: Adjust the azimuth of 3213276_1 by 50 degrees
- `C17`: Decrease A3 Offset threshold for 3213276_1
- `C18`: Add neighbor relationship between 3278736_3 and 3213276_1
- `C19`: Adjust the azimuth of 3210182_2 by 50 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213276_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213276_1
- `C22`: Decrease transmission power for 3213276_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.285 | MS1 | 121.4656595968 | 31.1446269634 | 98 | 504990 | -86.90 | 16.92 | 561.82 | 0.06 | 2.27 | 1576 |
| 2024-09-20 22:21:32.845 | MS1 | 121.4656634943 | 31.1446291234 | 98 | 504990 | -90.97 | 14.35 | 387.48 | 0.04 | 2.74 | 1573 |
| 2024-09-20 22:21:33.997 | MS1 | 121.4656614257 | 31.1446223858 | 98 | 504990 | -90.69 | 14.89 | 577.48 | 0.13 | 2.05 | 1589 |
| 2024-09-20 22:21:34.983 | MS1 | 121.4656635269 | 31.1446254357 | 98 | 504990 | -87.34 | 15.59 | 46.04 | 0.10 | 2.62 | 376 |
| 2024-09-20 22:21:35.615 | MS1 | 121.4656593972 | 31.1446192466 | 98 | 504990 | -88.25 | 14.72 | 86.31 | 0.16 | 2.19 | 440 |
| 2024-09-20 22:21:36.675 | MS1 | 121.4656703792 | 31.1446364277 | 98 | 504990 | -87.86 | 12.69 | 65.80 | 0.18 | 2.33 | 481 |
| 2024-09-20 22:21:37.621 | MS1 | 121.4656731402 | 31.1446216557 | 98 | 504990 | -90.49 | 10.15 | 58.61 | 0.13 | 2.55 | 389 |
| 2024-09-20 22:21:38.574 | MS1 | 121.4656677936 | 31.1446203314 | 98 | 504990 | -92.62 | 11.06 | 67.82 | 0.09 | 2.61 | 335 |
| 2024-09-20 22:21:39.561 | MS1 | 121.4656615026 | 31.1446321987 | 98 | 504990 | -93.41 | 9.92 | 66.61 | 0.09 | 2.40 | 422 |
| 2024-09-20 22:21:40.728 | MS1 | 121.4656711899 | 31.1446246067 | 98 | 504990 | -89.51 | 8.01 | 574.88 | 0.17 | 2.56 | 1596 |
| 2024-09-20 22:21:41.483 | MS1 | 121.4656594343 | 31.1446248966 | 98 | 504990 | -92.51 | 11.57 | 469.65 | 0.07 | 2.98 | 1573 |
| 2024-09-20 22:21:42.415 | MS1 | 121.4656775301 | 31.1446198626 | 98 | 504990 | -90.97 | 12.52 | 365.61 | 0.09 | 2.59 | 1589 |

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
| 3210182 | 2 | 121.4737155054 | 31.1498485620 | 76 | 7 | 10 | 20.1 | TDD | 98 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3213276 | 1 | 121.4691618647 | 31.1549357233 | 64 | 15 | 12 | 33.6 | TDD | 416 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3220946 | 4 | 121.4687545431 | 31.1441562358 | 221 | 7 | 10 | 43.4 | TDD | 725 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3278736 | 3 | 121.4732124949 | 31.1507033880 | 58 | 2 | 5 | 28.6 | TDD | 68 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.153 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.177 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.302 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.302 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.964 | NREventA3 | measId:2;ServCellPCI:191;Se... |
| 2024-09-20 22:21:38.204 | NRHandoverAttempt | SourcePCI:191;SourceNR-ARFC... |
| 2024-09-20 22:21:38.241 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.256 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.370 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.370 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213276 | 1 | 5.5681 | 18.5612 | -116.0746 | 5.6966 | 119.6029 | 0.0073 | 0.0150 |
| 2024_09_20 22:00 | 3210182 | 2 | 7.1913 | 15.0840 | -115.6161 | 7.5981 | 95.5214 | 0.0045 | 0.0046 |
| 2024_09_20 22:00 | 3278736 | 3 | 6.4822 | 17.2408 | -114.9315 | 15.8112 | 105.7610 | 0.0132 | 0.0018 |
| 2024_09_20 22:00 | 3220946 | 4 | 16.7993 | 19.6167 | -116.9542 | 15.7602 | 181.4314 | 0.0188 | 0.0159 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412907_F7AA9472 | 504990 | 98 | -86.0 | 504990 | 416 | -93.2 | 504990 | 68 | -99.9 | 504990 | 725 |
| MR_1774412907_438413BC | 504990 | 98 | -87.8 | 504990 | 416 | -94.5 | 504990 | 68 | -101.6 | 504990 | 725 |
| MR_1774412907_91E5AF0A | 504990 | 98 | -88.7 | 504990 | 416 | -93.5 | 504990 | 68 | -98.0 | 504990 | 725 |
| MR_1774412907_602853F9 | 504990 | 98 | -88.6 | 504990 | 416 | -95.6 | 504990 | 68 | -97.9 | 504990 | 725 |
| MR_1774412907_F7E079F5 | 504990 | 98 | -88.0 | 504990 | 416 | -93.2 | 504990 | 68 | -99.4 | 504990 | 725 |
| MR_1774412907_CACCFB99 | 504990 | 98 | -87.0 | 504990 | 416 | -91.7 | 504990 | 68 | -100.3 | 504990 | 725 |
| MR_1774412907_01C812D0 | 504990 | 98 | -86.5 | 504990 | 416 | -94.1 | 504990 | 68 | -99.4 | 504990 | 725 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 186: `c237bcf3-34d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c237bcf3-34dd-4bc8-a2dc-b727eb0d8395` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Lift the tilt angle  of 3233734_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[186] topology](images/train_0186.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3246592_2 by 4 degrees
- `C2`: Decrease A3 Offset threshold for 3246592_2
- `C3`: Adjust the azimuth of 3233734_3 by 50 degrees
- `C4`: Decrease A3 Offset threshold for 3265460_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265460_4
- `C6`: Press down the tilt angle  of 3233734_3 by 10 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246592_2
- `C8`: Add neighbor relationship between 3233734_3 and 3265460_4
- `C9`: Increase transmission power for 3265460_4
- `C10`: Increase A3 Offset threshold for 3265460_4
- `C11`: Decrease transmission power for 3265460_4
- `C12`: Decrease transmission power for 3246592_2
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246592_2
- `C15`: Add neighbor relationship between 3246592_2 and 3265460_4
- `C16`: Increase transmission power for 3246592_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265460_4
- `C18`: Lift the tilt angle of 3246592_2 by 4 degrees
- `C19`: Increase A3 Offset threshold for 3246592_2
- `C20`: Lift the tilt angle  of 3233734_3 by 10 degrees **← 정답**
- `C21`: Adjust the azimuth of 3246592_2 by 18 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.738 | MS1 | 121.4656687100 | 31.1446234280 | 203 | 504990 | -88.72 | 15.07 | 454.84 | 0.13 | 2.89 | 1578 |
| 2024-09-20 22:21:32.637 | MS1 | 121.4656715261 | 31.1446357746 | 203 | 504990 | -90.52 | 13.33 | 411.32 | 0.16 | 2.81 | 1582 |
| 2024-09-20 22:21:33.891 | MS1 | 121.4656739153 | 31.1446313497 | 203 | 504990 | -88.81 | 16.13 | 504.53 | 0.05 | 2.56 | 1600 |
| 2024-09-20 22:21:34.894 | MS1 | 121.4656661666 | 31.1446315295 | 203 | 504990 | -86.11 | 15.11 | 83.61 | 0.11 | 2.39 | 1587 |
| 2024-09-20 22:21:35.973 | MS1 | 121.4656687257 | 31.1446320125 | 203 | 504990 | -91.68 | 17.43 | 58.32 | 0.14 | 2.74 | 1599 |
| 2024-09-20 22:21:36.192 | MS1 | 121.4656752537 | 31.1446227446 | 203 | 504990 | -87.01 | 14.04 | 73.39 | 0.06 | 2.21 | 1569 |
| 2024-09-20 22:21:37.205 | MS1 | 121.4656604962 | 31.1446198855 | 203 | 504990 | -91.56 | 8.85 | 62.74 | 0.11 | 2.05 | 1561 |
| 2024-09-20 22:21:38.386 | MS1 | 121.4656611392 | 31.1446377006 | 203 | 504990 | -91.35 | 10.25 | 65.15 | 0.20 | 2.37 | 1573 |
| 2024-09-20 22:21:39.333 | MS1 | 121.4656587748 | 31.1446370102 | 203 | 504990 | -90.17 | 11.34 | 67.65 | 0.20 | 2.21 | 1566 |
| 2024-09-20 22:21:40.515 | MS1 | 121.4656723863 | 31.1446271217 | 203 | 504990 | -91.58 | 10.45 | 385.93 | 0.15 | 2.84 | 1586 |
| 2024-09-20 22:21:41.989 | MS1 | 121.4656605668 | 31.1446287726 | 203 | 504990 | -93.24 | 9.29 | 333.06 | 0.08 | 2.30 | 1564 |
| 2024-09-20 22:21:42.339 | MS1 | 121.4656650120 | 31.1446370604 | 203 | 504990 | -91.69 | 10.25 | 449.05 | 0.14 | 2.68 | 1594 |

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
| 3233734 | 3 | 121.4719619685 | 31.1546763140 | 29 | 9 | 12 | 43.7 | TDD | 190 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3246592 | 2 | 121.4756518116 | 31.1524548531 | 210 | 3 | 12 | 20.5 | TDD | 203 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3257345 | 1 | 121.4742272916 | 31.1527068331 | 325 | 10 | 11 | 26.9 | TDD | 186 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3265460 | 4 | 121.4668990340 | 31.1520073622 | 40 | 11 | 12 | 46.3 | TDD | 335 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.572 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.589 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.726 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.726 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.472 | NREventA3 | measId:2;ServCellPCI:333;Se... |
| 2024-09-20 22:21:38.712 | NRHandoverAttempt | SourcePCI:333;SourceNR-ARFC... |
| 2024-09-20 22:21:38.754 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.768 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.874 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.874 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257345 | 1 | 8.2934 | 14.6719 | -115.8441 | 8.1816 | 88.9237 | 0.0189 | 0.0185 |
| 2024_09_20 22:00 | 3246592 | 2 | 77.8080 | 79.6151 | -116.9368 | 14.0041 | 156.6109 | 0.0027 | 0.0022 |
| 2024_09_20 22:00 | 3233734 | 3 | 8.5056 | 15.8854 | -117.1984 | 7.8993 | 130.6248 | 0.0082 | 0.0189 |
| 2024_09_20 22:00 | 3265460 | 4 | 7.8757 | 13.4287 | -114.8815 | 9.6823 | 128.6028 | 0.0096 | 0.0155 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414977_2596EA41 | 504990 | 203 | -88.0 | 504990 | 335 | -85.6 | 504990 | 190 | -100.2 | 504990 | 186 |
| MR_1774414977_C2D00989 | 504990 | 203 | -85.8 | 504990 | 335 | -86.1 | 504990 | 190 | -98.1 | 504990 | 186 |
| MR_1774414977_13743F5D | 504990 | 203 | -87.6 | 504990 | 335 | -86.4 | 504990 | 190 | -97.5 | 504990 | 186 |
| MR_1774414977_91E6339F | 504990 | 203 | -87.9 | 504990 | 335 | -85.4 | 504990 | 190 | -98.4 | 504990 | 186 |
| MR_1774414977_05167761 | 504990 | 203 | -85.9 | 504990 | 335 | -88.7 | 504990 | 190 | -100.7 | 504990 | 186 |
| MR_1774414977_0C0C362E | 504990 | 203 | -84.6 | 504990 | 335 | -87.7 | 504990 | 190 | -100.5 | 504990 | 186 |
| MR_1774414977_ADD56007 | 504990 | 203 | -84.7 | 504990 | 335 | -88.8 | 504990 | 190 | -98.5 | 504990 | 186 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 187: `23c70be7-a8c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `23c70be7-a8cf-4457-b894-96487763f4a3` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229129_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[187] topology](images/train_0187.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3229129_3 by 3 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277638_4
- `C3`: Increase transmission power for 3229129_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229129_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277638_4
- `C6`: Lift the tilt angle  of 3277638_4 by 3 degrees
- `C7`: Adjust the azimuth of 3277638_4 by 43 degrees
- `C8`: Decrease A3 Offset threshold for 3277638_4
- `C9`: Decrease transmission power for 3229129_3
- `C10`: Decrease transmission power for 3277638_4
- `C11`: Check test server and transmission issues
- `C12`: Adjust the azimuth of 3229129_3 by 1 degrees
- `C13`: Add neighbor relationship between 3270251_10 and 3277638_4
- `C14`: Add neighbor relationship between 3229129_3 and 3277638_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229129_3 **← 정답**
- `C16`: Increase A3 Offset threshold for 3277638_4
- `C17`: Increase transmission power for 3277638_4
- `C18`: Press down the tilt angle  of 3277638_4 by 3 degrees
- `C19`: Decrease A3 Offset threshold for 3229129_3
- `C20`: Increase A3 Offset threshold for 3229129_3
- `C21`: Press down the tilt angle of 3229129_3 by 3 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.535 | MS1 | 121.4656662442 | 31.1446316441 | 991 | 504990 | -95.24 | 11.46 | 555.93 | 0.16 | 2.88 | 1567 |
| 2024-09-20 22:21:32.224 | MS1 | 121.4656713563 | 31.1446323766 | 285 | 504990 | -95.04 | 12.88 | 342.52 | 0.09 | 2.77 | 1587 |
| 2024-09-20 22:21:33.918 | MS1 | 121.4656777154 | 31.1446287914 | 532 | 504990 | -93.82 | 9.81 | 584.08 | 0.14 | 2.72 | 1580 |
| 2024-09-20 22:21:34.216 | MS1 | 121.4656581338 | 31.1446349673 | 275 | 152650 | -88.06 | 7.63 | 95.32 | 0.18 | 1.85 | 976 |
| 2024-09-20 22:21:35.393 | MS1 | 121.4656700059 | 31.1446365400 | 52 | 152650 | -88.68 | 6.57 | 75.50 | 0.04 | 1.55 | 944 |
| 2024-09-20 22:21:36.803 | MS1 | 121.4656733545 | 31.1446298235 | 147 | 152650 | -89.41 | 2.30 | 75.51 | 0.16 | 1.59 | 967 |
| 2024-09-20 22:21:37.256 | MS1 | 121.4656668318 | 31.1446188888 | 979 | 152650 | -93.82 | 5.51 | 75.29 | 0.08 | 1.76 | 998 |
| 2024-09-20 22:21:38.735 | MS1 | 121.4656715999 | 31.1446180359 | 275 | 152650 | -90.46 | 5.01 | 85.01 | 0.10 | 1.80 | 911 |
| 2024-09-20 22:21:39.895 | MS1 | 121.4656730572 | 31.1446232540 | 52 | 152650 | -94.02 | 6.48 | 82.72 | 0.17 | 1.65 | 947 |
| 2024-09-20 22:21:40.434 | MS1 | 121.4656624008 | 31.1446267285 | 147 | 152650 | -89.91 | 3.80 | 86.05 | 0.09 | 2.35 | 1595 |
| 2024-09-20 22:21:41.463 | MS1 | 121.4656617787 | 31.1446288865 | 979 | 152650 | -89.39 | 6.16 | 93.58 | 0.16 | 2.72 | 1568 |
| 2024-09-20 22:21:42.133 | MS1 | 121.4656586859 | 31.1446289981 | 275 | 152650 | -93.85 | 4.79 | 63.80 | 0.13 | 2.25 | 1587 |

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
| 3215376 | 2 | 121.4706734746 | 31.1445789986 | 185 | 5 | 4 | 3.2 | TDD | 532 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3222937 | 7 | 121.4706244449 | 31.1509962049 | 335 | 4 | 8 | 11.3 | FDD | 15 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3229047 | 6 | 121.4674720266 | 31.1549474542 | 323 | 6 | 1 | 19.1 | TDD | 415 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3229129 | 3 | 121.4692973594 | 31.1500288097 | 209 | 2 | 8 | 6.1 | TDD | 991 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3232333 | 8 | 121.4650787940 | 31.1453630703 | 342 | 12 | 11 | 16.3 | FDD | 275 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3245343 | 5 | 121.4675079922 | 31.1442925170 | 313 | 6 | 6 | 11.6 | TDD | 285 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3255567 | 1 | 121.4684288045 | 31.1540323920 | 138 | 8 | 10 | 8.8 | TDD | 384 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3256314 | 13 | 121.4662217850 | 31.1525965797 | 16 | 12 | 4 | 10.9 | FDD | 637 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3270251 | 10 | 121.4727102686 | 31.1465841372 | 40 | 1 | 12 | 9.3 | FDD | 147 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3271302 | 12 | 121.4754241008 | 31.1470143782 | 311 | 4 | 8 | 29.7 | FDD | 217 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3273641 | 11 | 121.4687373116 | 31.1461007139 | 124 | 11 | 2 | 23.7 | FDD | 979 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3277386 | 9 | 121.4709578740 | 31.1499199352 | 9 | 10 | 10 | 10.1 | FDD | 52 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3277638 | 4 | 121.4752827238 | 31.1514179576 | 188 | 2 | 3 | 27.2 | TDD | 476 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.622 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.637 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.767 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.767 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.482 | NREventA2 | measId:1;ServCellPCI:298;Se... |
| 2024-09-20 22:21:35.606 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.821 | NREventA5 | measId:3;ServCellPCI:298;Se... |
| 2024-09-20 22:21:35.855 | NRHandoverAttempt | SourcePCI:298;SourceNR-ARFC... |
| 2024-09-20 22:21:35.897 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.912 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.062 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.062 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255567 | 1 | 10.2814 | 14.4987 | -117.4978 | 16.8070 | 155.7900 | 0.0059 | 0.0063 |
| 2024_09_20 22:00 | 3215376 | 2 | 18.1046 | 5.1749 | -115.6512 | 8.4141 | 145.6855 | 0.0144 | 0.0086 |
| 2024_09_20 22:00 | 3229129 | 3 | 17.2699 | 7.0490 | -115.3322 | 15.8145 | 162.7615 | 0.0055 | 0.0023 |
| 2024_09_20 22:00 | 3277638 | 4 | 6.7581 | 11.2083 | -116.5961 | 7.1182 | 91.6049 | 0.0158 | 0.0078 |
| 2024_09_20 22:00 | 3245343 | 5 | 10.6707 | 13.5874 | -115.5377 | 7.9763 | 152.6631 | 0.0024 | 0.0055 |
| 2024_09_20 22:00 | 3229047 | 6 | 19.8994 | 7.4012 | -114.4582 | 18.3319 | 195.9615 | 0.0173 | 0.0098 |
| 2024_09_20 22:00 | 3222937 | 7 | 7.4944 | 12.2848 | -115.9054 | 4.4699 | 32.6172 | 0.0069 | 0.0091 |
| 2024_09_20 22:00 | 3232333 | 8 | 10.8297 | 7.1569 | -114.4554 | 4.9874 | 37.5710 | 0.0091 | 0.0114 |
| 2024_09_20 22:00 | 3277386 | 9 | 6.0409 | 8.4515 | -115.0753 | 4.8594 | 46.9039 | 0.0013 | 0.0024 |
| 2024_09_20 22:00 | 3270251 | 10 | 16.1249 | 10.0227 | -115.7592 | 3.0226 | 51.0260 | 0.0147 | 0.0064 |
| 2024_09_20 22:00 | 3273641 | 11 | 13.0076 | 15.7096 | -116.9205 | 3.5177 | 43.8483 | 0.0112 | 0.0171 |
| 2024_09_20 22:00 | 3271302 | 12 | 10.8632 | 18.4438 | -114.1305 | 4.0110 | 22.3395 | 0.0047 | 0.0152 |
| 2024_09_20 22:00 | 3256314 | 13 | 7.9257 | 6.8528 | -116.4952 | 4.2945 | 56.0741 | 0.0153 | 0.0149 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413546_8E648784 | 504990 | 532 | -93.3 | 504990 | 476 | -90.9 | 504990 | 415 | -91.1 | 504990 | 384 |
| MR_1774413546_D59132B3 | 504990 | 532 | -94.5 | 504990 | 476 | -90.7 | 504990 | 415 | -93.3 | 504990 | 384 |
| MR_1774413546_EE7597FE | 504990 | 532 | -95.2 | 504990 | 476 | -91.8 | 504990 | 415 | -94.2 | 504990 | 384 |
| MR_1774413546_BDDC80D2 | 152650 | 275 | -89.8 | 152650 | 217 | -93.8 | 152650 | 15 | -96.9 | 152650 | 637 |
| MR_1774413546_12D2DC42 | 504990 | 532 | -95.8 | 504990 | 476 | -91.3 | 504990 | 415 | -91.2 | 504990 | 384 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 188: `a5ee85a0-fd2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a5ee85a0-fd21-469b-8f49-8f8d81f27c42` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249038_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[188] topology](images/train_0188.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3276331_8 and 3253106_5
- `C2`: Adjust the azimuth of 3253106_5 by 29 degrees
- `C3`: Check test server and transmission issues
- `C4`: Adjust the azimuth of 3249038_4 by 11 degrees
- `C5`: Press down the tilt angle of 3249038_4 by 3 degrees
- `C6`: Lift the tilt angle  of 3253106_5 by 3 degrees
- `C7`: Increase transmission power for 3253106_5
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253106_5
- `C9`: Increase A3 Offset threshold for 3249038_4
- `C10`: Add neighbor relationship between 3249038_4 and 3253106_5
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease transmission power for 3249038_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249038_4 **← 정답**
- `C14`: Increase A3 Offset threshold for 3253106_5
- `C15`: Increase transmission power for 3249038_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249038_4
- `C17`: Decrease A3 Offset threshold for 3253106_5
- `C18`: Press down the tilt angle  of 3253106_5 by 3 degrees
- `C19`: Decrease A3 Offset threshold for 3249038_4
- `C20`: Lift the tilt angle of 3249038_4 by 3 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253106_5
- `C22`: Decrease transmission power for 3253106_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.318 | MS1 | 121.4656611913 | 31.1446277128 | 201 | 504990 | -93.82 | 11.97 | 458.86 | 0.11 | 2.70 | 1598 |
| 2024-09-20 22:21:32.664 | MS1 | 121.4656716250 | 31.1446204043 | 865 | 504990 | -95.56 | 10.23 | 532.65 | 0.02 | 2.55 | 1580 |
| 2024-09-20 22:21:33.534 | MS1 | 121.4656736413 | 31.1446207718 | 965 | 504990 | -93.02 | 9.60 | 499.43 | 0.15 | 2.82 | 1566 |
| 2024-09-20 22:21:34.386 | MS1 | 121.4656590107 | 31.1446345522 | 363 | 152650 | -94.59 | 6.30 | 69.92 | 0.12 | 1.94 | 985 |
| 2024-09-20 22:21:35.716 | MS1 | 121.4656586253 | 31.1446361002 | 356 | 152650 | -87.09 | 3.77 | 87.81 | 0.04 | 1.66 | 985 |
| 2024-09-20 22:21:36.519 | MS1 | 121.4656719966 | 31.1446241395 | 578 | 152650 | -89.78 | 5.55 | 72.50 | 0.19 | 1.52 | 929 |
| 2024-09-20 22:21:37.637 | MS1 | 121.4656688811 | 31.1446339612 | 120 | 152650 | -92.43 | 6.61 | 102.99 | 0.08 | 1.73 | 909 |
| 2024-09-20 22:21:38.836 | MS1 | 121.4656711381 | 31.1446333254 | 363 | 152650 | -94.80 | 7.07 | 65.37 | 0.03 | 1.61 | 908 |
| 2024-09-20 22:21:39.655 | MS1 | 121.4656755353 | 31.1446335873 | 356 | 152650 | -87.43 | 7.18 | 44.92 | 0.00 | 1.67 | 987 |
| 2024-09-20 22:21:40.281 | MS1 | 121.4656660838 | 31.1446289260 | 578 | 152650 | -87.41 | 5.58 | 59.83 | 0.10 | 2.33 | 1571 |
| 2024-09-20 22:21:41.340 | MS1 | 121.4656687848 | 31.1446354042 | 120 | 152650 | -90.09 | 7.16 | 92.05 | 0.06 | 2.29 | 1579 |
| 2024-09-20 22:21:42.427 | MS1 | 121.4656744025 | 31.1446365741 | 363 | 152650 | -88.89 | 4.93 | 83.31 | 0.02 | 2.38 | 1597 |

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
| 3212388 | 6 | 121.4719782529 | 31.1454140270 | 237 | 14 | 9 | 9.7 | TDD | 221 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3249038 | 4 | 121.4754582945 | 31.1506055467 | 224 | 3 | 12 | 0.2 | TDD | 201 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3249901 | 1 | 121.4684269929 | 31.1473323484 | 160 | 12 | 5 | 17.6 | TDD | 865 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3252727 | 12 | 121.4643402698 | 31.1523217215 | 262 | 5 | 11 | 13.1 | FDD | 363 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3253016 | 10 | 121.4735314549 | 31.1555339369 | 313 | 6 | 7 | 19.1 | FDD | 551 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3253106 | 5 | 121.4669036346 | 31.1528466976 | 216 | 2 | 5 | 19.0 | TDD | 273 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3254553 | 9 | 121.4664801504 | 31.1464970366 | 359 | 5 | 4 | 15.5 | FDD | 356 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3261619 | 3 | 121.4706543993 | 31.1526192482 | 126 | 1 | 4 | 24.9 | TDD | 421 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3261850 | 11 | 121.4683052953 | 31.1443132146 | 126 | 1 | 4 | 24.5 | FDD | 935 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3263664 | 2 | 121.4753473100 | 31.1545307942 | 108 | 13 | 1 | 19.8 | TDD | 965 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3265063 | 7 | 121.4680713896 | 31.1502444074 | 259 | 11 | 1 | 25.1 | FDD | 674 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3268729 | 13 | 121.4675337543 | 31.1528292648 | 353 | 11 | 9 | 29.6 | FDD | 120 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3276331 | 8 | 121.4728897733 | 31.1552885569 | 0 | 0 | 10 | 3.8 | FDD | 578 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |

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
| 2024-09-20 22:21:31.464 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.482 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.630 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.630 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.363 | NREventA2 | measId:1;ServCellPCI:601;Se... |
| 2024-09-20 22:21:35.480 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.760 | NREventA5 | measId:3;ServCellPCI:601;Se... |
| 2024-09-20 22:21:35.818 | NRHandoverAttempt | SourcePCI:601;SourceNR-ARFC... |
| 2024-09-20 22:21:35.867 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.878 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.004 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.004 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249901 | 1 | 18.2567 | 5.0437 | -116.8489 | 9.3301 | 163.1711 | 0.0120 | 0.0192 |
| 2024_09_20 22:00 | 3263664 | 2 | 10.6710 | 6.8733 | -117.1267 | 9.1248 | 194.1615 | 0.0169 | 0.0082 |
| 2024_09_20 22:00 | 3261619 | 3 | 18.5179 | 19.5082 | -116.1167 | 14.4964 | 174.0523 | 0.0134 | 0.0026 |
| 2024_09_20 22:00 | 3249038 | 4 | 10.6995 | 18.4646 | -114.1501 | 13.6489 | 108.9260 | 0.0026 | 0.0093 |
| 2024_09_20 22:00 | 3253106 | 5 | 16.3190 | 15.5987 | -117.8089 | 17.9315 | 129.6313 | 0.0159 | 0.0073 |
| 2024_09_20 22:00 | 3212388 | 6 | 11.0929 | 8.0537 | -114.0115 | 14.4090 | 175.6572 | 0.0010 | 0.0043 |
| 2024_09_20 22:00 | 3265063 | 7 | 17.7813 | 16.2283 | -116.5557 | 3.5039 | 47.4574 | 0.0063 | 0.0147 |
| 2024_09_20 22:00 | 3276331 | 8 | 14.3535 | 18.5947 | -115.0963 | 4.2477 | 30.9029 | 0.0085 | 0.0117 |
| 2024_09_20 22:00 | 3254553 | 9 | 15.9324 | 12.0188 | -115.7431 | 4.2119 | 52.1924 | 0.0041 | 0.0118 |
| 2024_09_20 22:00 | 3253016 | 10 | 12.3237 | 17.6951 | -116.6976 | 4.1398 | 39.1810 | 0.0084 | 0.0180 |
| 2024_09_20 22:00 | 3261850 | 11 | 7.6768 | 15.5894 | -117.7788 | 4.9258 | 23.3747 | 0.0185 | 0.0012 |
| 2024_09_20 22:00 | 3252727 | 12 | 6.5513 | 11.7837 | -116.7912 | 3.3483 | 56.0592 | 0.0002 | 0.0177 |
| 2024_09_20 22:00 | 3268729 | 13 | 17.4547 | 11.4120 | -116.0451 | 3.3170 | 37.9445 | 0.0196 | 0.0009 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412815_515E3BE3 | 504990 | 965 | -93.9 | 504990 | 273 | -95.7 | 504990 | 221 | -96.3 | 504990 | 421 |
| MR_1774412815_88028D77 | 504990 | 965 | -92.5 | 504990 | 273 | -93.1 | 504990 | 221 | -94.0 | 504990 | 421 |
| MR_1774412815_5477FE4B | 152650 | 363 | -95.9 | 152650 | 674 | -98.8 | 152650 | 551 | -102.9 | 152650 | 935 |
| MR_1774412815_D0E4F212 | 152650 | 363 | -92.9 | 152650 | 674 | -101.0 | 152650 | 551 | -101.0 | 152650 | 935 |
| MR_1774412815_B5A06233 | 504990 | 965 | -94.0 | 504990 | 273 | -95.7 | 504990 | 221 | -93.8 | 504990 | 421 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 189: `20c666b1-f59...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `20c666b1-f595-4083-881c-72d5cacbf7ee` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease A3 Offset threshold for 3257758_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[189] topology](images/train_0189.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3210524_2 by 50 degrees
- `C2`: Add neighbor relationship between 3244631_3 and 3210524_2
- `C3`: Add neighbor relationship between 3257758_1 and 3210524_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257758_1
- `C5`: Decrease A3 Offset threshold for 3210524_2
- `C6`: Lift the tilt angle  of 3210524_2 by 10 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210524_2
- `C8`: Decrease transmission power for 3210524_2
- `C9`: Decrease A3 Offset threshold for 3257758_1 **← 정답**
- `C10`: Adjust the azimuth of 3257758_1 by 50 degrees
- `C11`: Increase transmission power for 3257758_1
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Increase A3 Offset threshold for 3257758_1
- `C14`: Check test server and transmission issues
- `C15`: Press down the tilt angle  of 3210524_2 by 10 degrees
- `C16`: Increase A3 Offset threshold for 3210524_2
- `C17`: Increase transmission power for 3210524_2
- `C18`: Decrease transmission power for 3257758_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210524_2
- `C20`: Press down the tilt angle of 3257758_1 by 5 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257758_1
- `C22`: Lift the tilt angle of 3257758_1 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.817 | MS1 | 121.4656704116 | 31.1446263672 | 689 | 504990 | -77.71 | 16.36 | 428.32 | 0.01 | 2.56 | 1593 |
| 2024-09-20 22:21:32.545 | MS1 | 121.4656777892 | 31.1446293128 | 689 | 504990 | -83.87 | 16.77 | 449.32 | 0.20 | 2.73 | 1576 |
| 2024-09-20 22:21:33.362 | MS1 | 121.4656621795 | 31.1446298732 | 689 | 504990 | -79.75 | 15.38 | 469.52 | 0.16 | 2.21 | 1574 |
| 2024-09-20 22:21:34.139 | MS1 | 121.4656709126 | 31.1446339757 | 689 | 504990 | -89.84 | -0.20 | 73.66 | 0.12 | 1.28 | 1560 |
| 2024-09-20 22:21:35.336 | MS1 | 121.4656724075 | 31.1446283706 | 689 | 504990 | -87.86 | -0.52 | 68.29 | 0.15 | 1.09 | 1587 |
| 2024-09-20 22:21:36.807 | MS1 | 121.4656675385 | 31.1446269808 | 689 | 504990 | -86.58 | -3.77 | 41.94 | 0.19 | 1.15 | 1560 |
| 2024-09-20 22:21:37.479 | MS1 | 121.4656724317 | 31.1446357835 | 689 | 504990 | -85.78 | -1.17 | 75.45 | 0.06 | 1.01 | 1589 |
| 2024-09-20 22:21:38.695 | MS1 | 121.4656608800 | 31.1446275194 | 689 | 504990 | -88.17 | -0.71 | 47.95 | 0.06 | 1.32 | 1579 |
| 2024-09-20 22:21:39.515 | MS1 | 121.4656583509 | 31.1446367382 | 658 | 504990 | -76.76 | 16.54 | 308.20 | 0.12 | 1.07 | 1570 |
| 2024-09-20 22:21:40.707 | MS1 | 121.4656742488 | 31.1446209694 | 658 | 504990 | -79.49 | 13.07 | 546.06 | 0.13 | 2.60 | 1586 |
| 2024-09-20 22:21:41.724 | MS1 | 121.4656707341 | 31.1446363586 | 658 | 504990 | -84.83 | 17.47 | 353.17 | 0.14 | 2.88 | 1591 |
| 2024-09-20 22:21:42.881 | MS1 | 121.4656654469 | 31.1446250210 | 658 | 504990 | -82.46 | 14.81 | 595.20 | 0.09 | 2.51 | 1591 |

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
| 3210524 | 2 | 121.4725541451 | 31.1454939554 | 350 | 14 | 8 | 43.6 | TDD | 658 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3211136 | 4 | 121.4697318199 | 31.1443101902 | 241 | 1 | 0 | 48.3 | TDD | 837 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3244631 | 3 | 121.4682129857 | 31.1446761780 | 33 | 11 | 6 | 25.4 | TDD | 19 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3257758 | 1 | 121.4643477368 | 31.1489475117 | 292 | 0 | 10 | 42.5 | TDD | 689 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.158 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.173 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.306 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.306 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.969 | NREventA3 | measId:2;ServCellPCI:400;Se... |
| 2024-09-20 22:21:38.209 | NRHandoverAttempt | SourcePCI:400;SourceNR-ARFC... |
| 2024-09-20 22:21:38.251 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.261 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.381 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.381 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257758 | 1 | 10.4695 | 10.1393 | -114.6760 | 10.6563 | 167.7226 | 0.0061 | 0.1474 |
| 2024_09_20 22:00 | 3210524 | 2 | 15.7636 | 17.4655 | -117.2705 | 10.4154 | 100.5436 | 0.0160 | 0.0128 |
| 2024_09_20 22:00 | 3244631 | 3 | 6.1388 | 14.5023 | -117.5302 | 14.1832 | 114.9987 | 0.0084 | 0.0199 |
| 2024_09_20 22:00 | 3211136 | 4 | 7.3859 | 9.4681 | -117.5118 | 6.7064 | 98.4977 | 0.0090 | 0.0059 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414278_2EFB0F2E | 504990 | 658 | -83.7 | 504990 | 689 | -88.8 | 504990 | 19 | -87.0 | 504990 | 837 |
| MR_1774414278_A8A70AD4 | 504990 | 689 | -89.7 | 504990 | 658 | -82.3 | 504990 | 19 | -89.2 | 504990 | 837 |
| MR_1774414278_9861EC29 | 504990 | 658 | -84.5 | 504990 | 689 | -91.7 | 504990 | 19 | -87.0 | 504990 | 837 |
| MR_1774414278_C72B0374 | 504990 | 689 | -88.0 | 504990 | 658 | -82.5 | 504990 | 19 | -90.0 | 504990 | 837 |
| MR_1774414278_CA51FAF6 | 504990 | 658 | -82.4 | 504990 | 689 | -89.3 | 504990 | 19 | -86.9 | 504990 | 837 |
| MR_1774414278_1ACBC784 | 504990 | 658 | -85.1 | 504990 | 689 | -89.8 | 504990 | 19 | -86.7 | 504990 | 837 |
| MR_1774414278_649A1F57 | 504990 | 658 | -83.6 | 504990 | 689 | -90.7 | 504990 | 19 | -90.3 | 504990 | 837 |

> *... 2개 열 생략 (전체 14열)*

---
