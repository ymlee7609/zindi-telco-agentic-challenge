# Track A 문제 분석 — train[770]~train[779]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[770] ~ train[779] (10개)

## 목차

1. [문제 770: `8e1fa289-09b...`](#770) — single-answer, 정답: C10
2. [문제 771: `87dc9527-7e2...`](#771) — single-answer, 정답: C20
3. [문제 772: `30f0f286-1c3...`](#772) — multiple-answer, 정답: C8|C19
4. [문제 773: `a071a1ff-80e...`](#773) — single-answer, 정답: C5
5. [문제 774: `1eeb57f1-1fa...`](#774) — single-answer, 정답: C17
6. [문제 775: `27edea6d-90d...`](#775) — multiple-answer, 정답: C1|C4
7. [문제 776: `90772778-1f4...`](#776) — single-answer, 정답: C15
8. [문제 777: `e9852b17-f8f...`](#777) — single-answer, 정답: C8
9. [문제 778: `6d1c9ec5-52d...`](#778) — single-answer, 정답: C2
10. [문제 779: `49490005-464...`](#779) — single-answer, 정답: C15

---

### 문제 770: `8e1fa289-09b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8e1fa289-09b0-4697-97bf-6804eb3c74cb` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[770] topology](images/train_0770.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Increase transmission power for 3223313_1
- `C3`: Decrease A3 Offset threshold for 3237377_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223313_1
- `C5`: Adjust the azimuth of 3223313_1 by 50 degrees
- `C6`: Lift the tilt angle  of 3237377_4 by 9 degrees
- `C7`: Decrease A3 Offset threshold for 3223313_1
- `C8`: Add neighbor relationship between 3223313_1 and 3237377_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223313_1
- `C10`: Insufficient data; more data is needed for judgment. **← 정답**
- `C11`: Increase transmission power for 3237377_4
- `C12`: Lift the tilt angle of 3223313_1 by 10 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237377_4
- `C14`: Decrease transmission power for 3237377_4
- `C15`: Increase A3 Offset threshold for 3223313_1
- `C16`: Press down the tilt angle  of 3237377_4 by 9 degrees
- `C17`: Press down the tilt angle of 3223313_1 by 10 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237377_4
- `C19`: Add neighbor relationship between 3272415_2 and 3237377_4
- `C20`: Adjust the azimuth of 3237377_4 by 50 degrees
- `C21`: Increase A3 Offset threshold for 3237377_4
- `C22`: Decrease transmission power for 3223313_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.171 | MS1 | 121.4656642200 | 31.1446220898 | 574 | 504990 | -89.63 | 15.72 | 425.03 | 0.01 | 2.91 | 1572 |
| 2024-09-20 22:21:32.295 | MS1 | 121.4656646645 | 31.1446235288 | 574 | 504990 | -91.10 | 13.35 | 548.57 | 0.07 | 2.40 | 1580 |
| 2024-09-20 22:21:33.793 | MS1 | 121.4656676269 | 31.1446236048 | 574 | 504990 | -91.09 | 16.06 | 536.03 | 0.10 | 2.39 | 1591 |
| 2024-09-20 22:21:34.866 | MS1 | 121.4656646004 | 31.1446296855 | 574 | 504990 | -85.15 | 15.66 | 54.76 | 0.03 | 2.29 | 1583 |
| 2024-09-20 22:21:35.140 | MS1 | 121.4656719057 | 31.1446331366 | 574 | 504990 | -85.18 | 14.95 | 73.88 | 0.14 | 2.65 | 1565 |
| 2024-09-20 22:21:36.633 | MS1 | 121.4656743744 | 31.1446339998 | 574 | 504990 | -90.81 | 17.05 | 73.86 | 0.07 | 2.22 | 1592 |
| 2024-09-20 22:21:37.646 | MS1 | 121.4656654416 | 31.1446287123 | 574 | 504990 | -90.74 | 12.42 | 64.54 | 0.12 | 2.43 | 1570 |
| 2024-09-20 22:21:38.741 | MS1 | 121.4656670779 | 31.1446337621 | 574 | 504990 | -91.94 | 7.49 | 84.05 | 0.05 | 2.53 | 1589 |
| 2024-09-20 22:21:39.817 | MS1 | 121.4656704828 | 31.1446236523 | 574 | 504990 | -93.08 | 7.09 | 67.28 | 0.10 | 2.73 | 1571 |
| 2024-09-20 22:21:40.703 | MS1 | 121.4656693591 | 31.1446352033 | 574 | 504990 | -92.91 | 9.33 | 312.13 | 0.10 | 2.90 | 1572 |
| 2024-09-20 22:21:41.242 | MS1 | 121.4656693879 | 31.1446324348 | 574 | 504990 | -89.83 | 12.65 | 331.37 | 0.04 | 2.81 | 1587 |
| 2024-09-20 22:21:42.231 | MS1 | 121.4656710747 | 31.1446333173 | 574 | 504990 | -93.09 | 9.97 | 393.96 | 0.15 | 2.25 | 1561 |

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
| 3223313 | 1 | 121.4669036016 | 31.1454012265 | 317 | 11 | 10 | 35.8 | TDD | 574 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3237377 | 4 | 121.4684015673 | 31.1529718030 | 25 | 7 | 0 | 31.8 | TDD | 846 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3255955 | 3 | 121.4708358931 | 31.1490743465 | 142 | 12 | 6 | 42.0 | TDD | 788 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3272415 | 2 | 121.4655409178 | 31.1487974899 | 221 | 5 | 11 | 44.3 | TDD | 650 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.886 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.907 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.057 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.057 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.730 | NREventA3 | measId:2;ServCellPCI:278;Se... |
| 2024-09-20 22:21:37.970 | NRHandoverAttempt | SourcePCI:278;SourceNR-ARFC... |
| 2024-09-20 22:21:38.016 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.031 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.163 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.163 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3223313 | 1 | 83.2902 | 86.8808 | -115.3555 | 8.1376 | 98.4449 | 0.0117 | 0.0171 |
| 2024_09_19 22:00 | 3272415 | 2 | 84.2824 | 84.9330 | -117.2330 | 14.8672 | 148.7482 | 0.0034 | 0.0046 |
| 2024_09_19 22:00 | 3255955 | 3 | 75.3075 | 80.7810 | -114.3568 | 5.4191 | 113.2993 | 0.0179 | 0.0187 |
| 2024_09_19 22:00 | 3237377 | 4 | 84.7414 | 77.7162 | -114.8739 | 15.4104 | 154.0780 | 0.0140 | 0.0193 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413571_5A4FFB49 | 504990 | 574 | -87.0 | 504990 | 846 | -91.0 | 504990 | 650 | -91.8 | 504990 | 788 |
| MR_1774413571_3B23F041 | 504990 | 574 | -86.1 | 504990 | 846 | -90.7 | 504990 | 650 | -94.0 | 504990 | 788 |
| MR_1774413571_BC4F2549 | 504990 | 574 | -86.0 | 504990 | 846 | -90.3 | 504990 | 650 | -93.6 | 504990 | 788 |
| MR_1774413571_14772729 | 504990 | 574 | -84.9 | 504990 | 846 | -89.9 | 504990 | 650 | -91.3 | 504990 | 788 |
| MR_1774413571_AD1BA748 | 504990 | 574 | -85.8 | 504990 | 846 | -91.3 | 504990 | 650 | -95.0 | 504990 | 788 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 771: `87dc9527-7e2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `87dc9527-7e2b-41e3-83cb-47fc0f0bb033` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[771] topology](images/train_0771.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3222323_2
- `C2`: Increase A3 Offset threshold for 3265264_3
- `C3`: Press down the tilt angle  of 3222323_2 by 10 degrees
- `C4`: Adjust the azimuth of 3265264_3 by 50 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222323_2
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Lift the tilt angle  of 3222323_2 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222323_2
- `C9`: Add neighbor relationship between 3265264_3 and 3222323_2
- `C10`: Increase A3 Offset threshold for 3222323_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265264_3
- `C12`: Adjust the azimuth of 3222323_2 by 48 degrees
- `C13`: Decrease A3 Offset threshold for 3222323_2
- `C14`: Lift the tilt angle of 3265264_3 by 6 degrees
- `C15`: Decrease A3 Offset threshold for 3265264_3
- `C16`: Press down the tilt angle of 3265264_3 by 6 degrees
- `C17`: Add neighbor relationship between 3272295_1 and 3222323_2
- `C18`: Decrease transmission power for 3222323_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265264_3
- `C20`: Check test server and transmission issues **← 정답**
- `C21`: Decrease transmission power for 3265264_3
- `C22`: Increase transmission power for 3265264_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.737 | MS1 | 121.4656779546 | 31.1446271406 | 4 | 504990 | -85.64 | 12.52 | 547.31 | 0.20 | 2.02 | 1561 |
| 2024-09-20 22:21:32.444 | MS1 | 121.4656695679 | 31.1446184276 | 4 | 504990 | -91.64 | 16.48 | 535.31 | 0.06 | 2.84 | 1595 |
| 2024-09-20 22:21:33.111 | MS1 | 121.4656685592 | 31.1446372162 | 4 | 504990 | -88.29 | 17.95 | 586.49 | 0.06 | 2.95 | 1593 |
| 2024-09-20 22:21:34.827 | MS1 | 121.4656691873 | 31.1446281773 | 4 | 504990 | -85.08 | 12.44 | 76.27 | 0.03 | 2.14 | 429 |
| 2024-09-20 22:21:35.146 | MS1 | 121.4656672357 | 31.1446352513 | 4 | 504990 | -90.15 | 13.50 | 68.60 | 0.14 | 2.11 | 308 |
| 2024-09-20 22:21:36.924 | MS1 | 121.4656728380 | 31.1446378029 | 4 | 504990 | -87.62 | 13.58 | 51.72 | 0.16 | 2.18 | 392 |
| 2024-09-20 22:21:37.274 | MS1 | 121.4656701444 | 31.1446247664 | 4 | 504990 | -91.56 | 9.17 | 101.07 | 0.09 | 2.79 | 380 |
| 2024-09-20 22:21:38.670 | MS1 | 121.4656668440 | 31.1446266089 | 4 | 504990 | -93.49 | 12.55 | 67.17 | 0.10 | 2.31 | 339 |
| 2024-09-20 22:21:39.705 | MS1 | 121.4656775617 | 31.1446312302 | 4 | 504990 | -91.87 | 7.60 | 55.44 | 0.06 | 2.06 | 388 |
| 2024-09-20 22:21:40.827 | MS1 | 121.4656773617 | 31.1446295225 | 4 | 504990 | -92.79 | 8.05 | 389.83 | 0.07 | 2.52 | 1582 |
| 2024-09-20 22:21:41.966 | MS1 | 121.4656662229 | 31.1446338737 | 4 | 504990 | -92.28 | 9.06 | 549.56 | 0.18 | 2.27 | 1577 |
| 2024-09-20 22:21:42.898 | MS1 | 121.4656695228 | 31.1446200191 | 4 | 504990 | -89.76 | 12.56 | 507.74 | 0.18 | 2.59 | 1573 |

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
| 3215746 | 4 | 121.4751187131 | 31.1518121404 | 174 | 2 | 9 | 27.1 | TDD | 279 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3222323 | 2 | 121.4757801850 | 31.1501663578 | 285 | 14 | 7 | 24.5 | TDD | 220 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3265264 | 3 | 121.4701240310 | 31.1441365269 | 35 | 2 | 6 | 32.3 | TDD | 4 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3272295 | 1 | 121.4692842845 | 31.1454707092 | 335 | 13 | 6 | 31.3 | TDD | 344 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.595 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.614 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.762 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.762 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.477 | NREventA3 | measId:2;ServCellPCI:433;Se... |
| 2024-09-20 22:21:38.717 | NRHandoverAttempt | SourcePCI:433;SourceNR-ARFC... |
| 2024-09-20 22:21:38.758 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.770 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.904 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.904 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272295 | 1 | 8.9849 | 10.0427 | -117.9925 | 18.1196 | 166.5432 | 0.0101 | 0.0022 |
| 2024_09_20 22:00 | 3222323 | 2 | 15.1250 | 5.5802 | -117.1662 | 17.2905 | 94.5196 | 0.0108 | 0.0039 |
| 2024_09_20 22:00 | 3265264 | 3 | 5.0722 | 6.4775 | -116.9555 | 5.6280 | 159.2189 | 0.0052 | 0.0156 |
| 2024_09_20 22:00 | 3215746 | 4 | 13.0867 | 9.8997 | -114.0344 | 9.5838 | 169.0720 | 0.0131 | 0.0195 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413501_19C84B8D | 504990 | 4 | -83.3 | 504990 | 220 | -90.9 | 504990 | 344 | -101.1 | 504990 | 279 |
| MR_1774413501_EF8AEFA4 | 504990 | 4 | -83.1 | 504990 | 220 | -91.6 | 504990 | 344 | -100.0 | 504990 | 279 |
| MR_1774413501_D216181B | 504990 | 4 | -85.9 | 504990 | 220 | -89.8 | 504990 | 344 | -100.8 | 504990 | 279 |
| MR_1774413501_7BB13335 | 504990 | 4 | -84.5 | 504990 | 220 | -91.4 | 504990 | 344 | -99.4 | 504990 | 279 |
| MR_1774413501_B46704F8 | 504990 | 4 | -86.6 | 504990 | 220 | -92.5 | 504990 | 344 | -100.5 | 504990 | 279 |
| MR_1774413501_54A36A59 | 504990 | 4 | -84.7 | 504990 | 220 | -89.8 | 504990 | 344 | -100.8 | 504990 | 279 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 772: `30f0f286-1c3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `30f0f286-1c31-4892-bd43-483fc8b4d8d2` |
| Tag | **multiple-answer** |
| 정답 | **C8|C19** |
| C8 의미 | Adjust the azimuth of 3262506_2 by 17 degrees |
| C19 의미 | Increase transmission power for 3262506_2 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[772] topology](images/train_0772.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3231727_4 by 5 degrees
- `C2`: Increase A3 Offset threshold for 3231727_4
- `C3`: Decrease transmission power for 3231727_4
- `C4`: Lift the tilt angle of 3262506_2 by 10 degrees
- `C5`: Add neighbor relationship between 3274125_3 and 3231727_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231727_4
- `C7`: Adjust the azimuth of 3231727_4 by 25 degrees
- `C8`: Adjust the azimuth of 3262506_2 by 17 degrees **← 정답**
- `C9`: Check test server and transmission issues
- `C10`: Press down the tilt angle of 3262506_2 by 10 degrees
- `C11`: Decrease A3 Offset threshold for 3262506_2
- `C12`: Decrease transmission power for 3262506_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262506_2
- `C14`: Press down the tilt angle  of 3231727_4 by 5 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231727_4
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase transmission power for 3231727_4
- `C18`: Increase A3 Offset threshold for 3262506_2
- `C19`: Increase transmission power for 3262506_2 **← 정답**
- `C20`: Add neighbor relationship between 3262506_2 and 3231727_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262506_2
- `C22`: Decrease A3 Offset threshold for 3231727_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.785 | MS1 | 121.4656654092 | 31.1446361146 | 563 | 504990 | -86.33 | 12.32 | 311.22 | 0.14 | 2.92 | 1589 |
| 2024-09-20 22:21:32.512 | MS1 | 121.4656692184 | 31.1446275462 | 563 | 504990 | -92.91 | 13.53 | 412.01 | 0.18 | 2.58 | 1569 |
| 2024-09-20 22:21:33.869 | MS1 | 121.4656614759 | 31.1446312645 | 563 | 504990 | -88.91 | 14.29 | 483.16 | 0.13 | 2.13 | 1587 |
| 2024-09-20 22:21:34.239 | MS1 | 121.4656609960 | 31.1446279825 | 563 | 504990 | -107.51 | 0.02 | 71.79 | 0.12 | 1.04 | 1580 |
| 2024-09-20 22:21:35.941 | MS1 | 121.4656655062 | 31.1446205470 | 563 | 504990 | -108.54 | 0.50 | 73.83 | 0.01 | 1.32 | 1570 |
| 2024-09-20 22:21:36.283 | MS1 | 121.4656749992 | 31.1446329128 | 563 | 504990 | -106.06 | -1.72 | 50.96 | 0.15 | 1.32 | 1566 |
| 2024-09-20 22:21:37.129 | MS1 | 121.4656724940 | 31.1446190432 | 563 | 504990 | -101.12 | 1.29 | 73.22 | 0.07 | 1.49 | 1589 |
| 2024-09-20 22:21:38.109 | MS1 | 121.4656675993 | 31.1446347944 | 563 | 504990 | -100.36 | 1.00 | 30.37 | 0.08 | 1.45 | 1599 |
| 2024-09-20 22:21:39.441 | MS1 | 121.4656591591 | 31.1446375564 | 563 | 504990 | -100.98 | 1.44 | 56.58 | 0.07 | 1.14 | 1600 |
| 2024-09-20 22:21:40.499 | MS1 | 121.4656586046 | 31.1446254380 | 563 | 504990 | -91.97 | 12.70 | 592.45 | 0.04 | 2.00 | 1593 |
| 2024-09-20 22:21:41.268 | MS1 | 121.4656623211 | 31.1446297317 | 563 | 504990 | -85.20 | 12.44 | 411.54 | 0.01 | 2.41 | 1600 |
| 2024-09-20 22:21:42.434 | MS1 | 121.4656771932 | 31.1446274723 | 563 | 504990 | -90.90 | 12.03 | 400.85 | 0.07 | 2.20 | 1563 |

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
| 3231727 | 4 | 121.4641208786 | 31.1544836526 | 147 | 4 | 0 | 19.4 | TDD | 723 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3238553 | 1 | 121.4680939944 | 31.1489898030 | 45 | 8 | 1 | 41.1 | TDD | 72 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3262506 | 2 | 121.4702080793 | 31.1466100092 | 260 | 8 | 5 | 24.3 | TDD | 563 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3274125 | 3 | 121.4680943599 | 31.1528557888 | 127 | 4 | 4 | 41.0 | TDD | 69 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.125 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.146 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.294 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.294 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.524 | NREventA2 | measId:1;ServCellPCI:716;Se... |
| 2024-09-20 22:21:34.646 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238553 | 1 | 9.4445 | 10.5600 | -117.2993 | 19.3466 | 133.0411 | 0.0080 | 0.0068 |
| 2024_09_20 22:00 | 3262506 | 2 | 6.4441 | 16.8374 | -117.0939 | 12.3129 | 138.6236 | 0.1029 | 0.0132 |
| 2024_09_20 22:00 | 3274125 | 3 | 13.2101 | 16.8241 | -114.7566 | 13.4765 | 169.8791 | 0.0016 | 0.0039 |
| 2024_09_20 22:00 | 3231727 | 4 | 15.1805 | 13.3088 | -115.5377 | 11.0077 | 155.5979 | 0.0176 | 0.0054 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414397_5C5181D0 | 504990 | 563 | -109.0 | 504990 | 723 | -108.7 | 504990 | 69 | -119.1 | 504990 | 72 |
| MR_1774414397_C493ADEB | 504990 | 563 | -107.4 | 504990 | 723 | -109.0 | 504990 | 69 | -117.3 | 504990 | 72 |
| MR_1774414397_7F77BCC1 | 504990 | 563 | -109.2 | 504990 | 723 | -110.6 | 504990 | 69 | -116.9 | 504990 | 72 |
| MR_1774414397_B4A3B266 | 504990 | 563 | -108.2 | 504990 | 723 | -110.0 | 504990 | 69 | -118.5 | 504990 | 72 |
| MR_1774414397_8DD6404B | 504990 | 563 | -105.8 | 504990 | 723 | -111.3 | 504990 | 69 | -117.8 | 504990 | 72 |
| MR_1774414397_14BD5DB8 | 504990 | 563 | -105.7 | 504990 | 723 | -112.0 | 504990 | 69 | -119.1 | 504990 | 72 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 773: `a071a1ff-80e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a071a1ff-80eb-4623-b4fd-522af3fe0f96` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Add neighbor relationship between 3253864_1 and 3254475_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[773] topology](images/train_0773.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254475_4
- `C2`: Increase transmission power for 3253864_1
- `C3`: Check test server and transmission issues
- `C4`: Press down the tilt angle  of 3254475_4 by 5 degrees
- `C5`: Add neighbor relationship between 3253864_1 and 3254475_4 **← 정답**
- `C6`: Lift the tilt angle of 3253864_1 by 10 degrees
- `C7`: Decrease transmission power for 3254475_4
- `C8`: Adjust the azimuth of 3253864_1 by 37 degrees
- `C9`: Increase A3 Offset threshold for 3253864_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253864_1
- `C11`: Adjust the azimuth of 3254475_4 by 23 degrees
- `C12`: Decrease A3 Offset threshold for 3253864_1
- `C13`: Increase A3 Offset threshold for 3254475_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254475_4
- `C15`: Add neighbor relationship between 3272573_3 and 3254475_4
- `C16`: Lift the tilt angle  of 3254475_4 by 5 degrees
- `C17`: Press down the tilt angle of 3253864_1 by 10 degrees
- `C18`: Increase transmission power for 3254475_4
- `C19`: Decrease A3 Offset threshold for 3254475_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253864_1
- `C21`: Decrease transmission power for 3253864_1
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.943 | MS1 | 121.4656695958 | 31.1446342546 | 992 | 504990 | -83.59 | 13.44 | 316.68 | 0.16 | 2.88 | 1582 |
| 2024-09-20 22:21:32.226 | MS1 | 121.4656580424 | 31.1446243782 | 992 | 504990 | -75.71 | 17.04 | 522.28 | 0.15 | 2.60 | 1565 |
| 2024-09-20 22:21:33.148 | MS1 | 121.4656739418 | 31.1446220911 | 992 | 504990 | -78.60 | 14.01 | 521.32 | 0.04 | 3.00 | 1586 |
| 2024-09-20 22:21:34.230 | MS1 | 121.4656691587 | 31.1446278410 | 992 | 504990 | -94.60 | -3.59 | 55.33 | 0.08 | 1.43 | 1579 |
| 2024-09-20 22:21:35.983 | MS1 | 121.4656725790 | 31.1446206669 | 992 | 504990 | -89.80 | -3.00 | 57.45 | 0.13 | 1.10 | 1591 |
| 2024-09-20 22:21:36.603 | MS1 | 121.4656608333 | 31.1446182573 | 992 | 504990 | -94.16 | -3.35 | 39.24 | 0.08 | 1.35 | 1594 |
| 2024-09-20 22:21:37.118 | MS1 | 121.4656600166 | 31.1446300398 | 992 | 504990 | -88.97 | -0.95 | 56.29 | 0.13 | 1.44 | 1587 |
| 2024-09-20 22:21:38.401 | MS1 | 121.4656678563 | 31.1446318161 | 992 | 504990 | -77.49 | 16.85 | 563.93 | 0.11 | 1.31 | 1574 |
| 2024-09-20 22:21:39.414 | MS1 | 121.4656772221 | 31.1446360195 | 992 | 504990 | -84.07 | 17.09 | 315.48 | 0.16 | 1.44 | 1584 |
| 2024-09-20 22:21:40.992 | MS1 | 121.4656719729 | 31.1446324012 | 992 | 504990 | -81.71 | 13.02 | 533.18 | 0.20 | 2.49 | 1584 |
| 2024-09-20 22:21:41.447 | MS1 | 121.4656756559 | 31.1446329438 | 992 | 504990 | -80.58 | 13.83 | 532.65 | 0.09 | 2.90 | 1569 |
| 2024-09-20 22:21:42.275 | MS1 | 121.4656699508 | 31.1446258880 | 992 | 504990 | -77.22 | 15.24 | 362.08 | 0.14 | 2.90 | 1571 |

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
| 3253864 | 1 | 121.4662925585 | 31.1534201546 | 147 | 9 | 10 | 28.1 | TDD | 992 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3254475 | 4 | 121.4701572960 | 31.1454443075 | 235 | 2 | 12 | 21.1 | TDD | 397 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3255620 | 2 | 121.4663880081 | 31.1536263379 | 326 | 8 | 11 | 27.6 | TDD | 918 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3272573 | 3 | 121.4717950157 | 31.1477863639 | 39 | 13 | 5 | 24.6 | TDD | 525 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.498 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.523 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.637 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.637 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.388 | NREventA3 | measId:2;ServCellPCI:625;Se... |
| 2024-09-20 22:21:36.388 | NREventA3 | measId:2;ServCellPCI:625;Se... |
| 2024-09-20 22:21:37.388 | NREventA3 | measId:2;ServCellPCI:625;Se... |
| 2024-09-20 22:21:39.888 | NRRRCReestablishAttempt | PCI:625 |
| 2024-09-20 22:21:39.904 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.918 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:40.060 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.060 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253864 | 1 | 15.2065 | 5.3465 | -116.2725 | 11.0205 | 92.8101 | 0.0011 | 0.1058 |
| 2024_09_20 22:00 | 3255620 | 2 | 14.7307 | 9.7408 | -116.0453 | 12.9000 | 119.0375 | 0.0043 | 0.0129 |
| 2024_09_20 22:00 | 3272573 | 3 | 18.9313 | 5.6129 | -116.6399 | 7.2036 | 111.9175 | 0.0040 | 0.0170 |
| 2024_09_20 22:00 | 3254475 | 4 | 6.6799 | 14.9391 | -114.5859 | 8.6925 | 98.8835 | 0.0196 | 0.0124 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413924_F8790679 | 504990 | 992 | -94.3 | 504990 | 397 | -90.0 | 504990 | 525 | -100.6 | 504990 | 918 |
| MR_1774413924_FDBA8DAD | 504990 | 992 | -95.9 | 504990 | 397 | -91.0 | 504990 | 525 | -99.0 | 504990 | 918 |
| MR_1774413924_35D4A357 | 504990 | 992 | -93.1 | 504990 | 397 | -87.7 | 504990 | 525 | -99.1 | 504990 | 918 |
| MR_1774413924_FA8F0840 | 504990 | 992 | -95.5 | 504990 | 397 | -88.7 | 504990 | 525 | -99.0 | 504990 | 918 |
| MR_1774413924_CB4C9C74 | 504990 | 397 | -88.9 | 504990 | 992 | -95.3 | 504990 | 525 | -98.4 | 504990 | 918 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 774: `1eeb57f1-1fa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1eeb57f1-1fa1-467f-beb5-f0c68248f8e5` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[774] topology](images/train_0774.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3245074_2 and 3227086_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222830_3
- `C3`: Increase transmission power for 3222830_3
- `C4`: Increase A3 Offset threshold for 3222830_3
- `C5`: Lift the tilt angle  of 3227086_4 by 3 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227086_4
- `C7`: Decrease A3 Offset threshold for 3227086_4
- `C8`: Decrease transmission power for 3222830_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227086_4
- `C10`: Add neighbor relationship between 3222830_3 and 3227086_4
- `C11`: Increase A3 Offset threshold for 3227086_4
- `C12`: Adjust the azimuth of 3227086_4 by 0 degrees
- `C13`: Press down the tilt angle of 3222830_3 by 6 degrees
- `C14`: Increase transmission power for 3227086_4
- `C15`: Lift the tilt angle of 3222830_3 by 6 degrees
- `C16`: Adjust the azimuth of 3222830_3 by 50 degrees
- `C17`: Insufficient data; more data is needed for judgment. **← 정답**
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222830_3
- `C19`: Decrease A3 Offset threshold for 3222830_3
- `C20`: Press down the tilt angle  of 3227086_4 by 3 degrees
- `C21`: Check test server and transmission issues
- `C22`: Decrease transmission power for 3227086_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.558 | MS1 | 121.4656610167 | 31.1446349891 | 342 | 504990 | -88.49 | 14.73 | 461.98 | 0.00 | 2.92 | 1595 |
| 2024-09-20 22:21:32.441 | MS1 | 121.4656594745 | 31.1446328163 | 342 | 504990 | -86.37 | 16.31 | 403.29 | 0.13 | 2.10 | 1595 |
| 2024-09-20 22:21:33.541 | MS1 | 121.4656731221 | 31.1446230566 | 342 | 504990 | -86.77 | 17.90 | 508.23 | 0.16 | 2.92 | 1573 |
| 2024-09-20 22:21:34.607 | MS1 | 121.4656607674 | 31.1446248609 | 342 | 504990 | -87.55 | 17.99 | 67.21 | 0.00 | 2.57 | 1587 |
| 2024-09-20 22:21:35.495 | MS1 | 121.4656738754 | 31.1446373059 | 342 | 504990 | -89.58 | 14.82 | 53.66 | 0.11 | 2.62 | 1583 |
| 2024-09-20 22:21:36.929 | MS1 | 121.4656595543 | 31.1446207117 | 342 | 504990 | -86.41 | 13.27 | 76.12 | 0.08 | 2.75 | 1590 |
| 2024-09-20 22:21:37.206 | MS1 | 121.4656648427 | 31.1446235708 | 342 | 504990 | -89.05 | 10.43 | 63.74 | 0.20 | 2.99 | 1570 |
| 2024-09-20 22:21:38.614 | MS1 | 121.4656771756 | 31.1446272748 | 342 | 504990 | -89.97 | 12.39 | 61.96 | 0.08 | 2.76 | 1571 |
| 2024-09-20 22:21:39.325 | MS1 | 121.4656591261 | 31.1446261063 | 342 | 504990 | -90.30 | 8.99 | 59.35 | 0.05 | 2.11 | 1561 |
| 2024-09-20 22:21:40.779 | MS1 | 121.4656679477 | 31.1446364207 | 342 | 504990 | -89.34 | 11.47 | 373.95 | 0.02 | 2.01 | 1563 |
| 2024-09-20 22:21:41.359 | MS1 | 121.4656611843 | 31.1446309353 | 342 | 504990 | -90.12 | 10.54 | 560.59 | 0.14 | 2.98 | 1563 |
| 2024-09-20 22:21:42.649 | MS1 | 121.4656705337 | 31.1446285480 | 342 | 504990 | -90.97 | 7.08 | 577.44 | 0.16 | 2.55 | 1587 |

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
| 3222830 | 3 | 121.4658359606 | 31.1527003696 | 345 | 5 | 5 | 17.8 | TDD | 342 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3223854 | 1 | 121.4734478725 | 31.1491175280 | 181 | 1 | 12 | 46.8 | TDD | 81 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3227086 | 4 | 121.4741216672 | 31.1492795038 | 237 | 2 | 1 | 18.7 | TDD | 7 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3245074 | 2 | 121.4741865386 | 31.1500132682 | 189 | 3 | 12 | 28.0 | TDD | 419 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.489 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.509 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.632 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.632 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.359 | NREventA3 | measId:2;ServCellPCI:180;Se... |
| 2024-09-20 22:21:38.599 | NRHandoverAttempt | SourcePCI:180;SourceNR-ARFC... |
| 2024-09-20 22:21:38.636 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.646 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.760 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.760 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3223854 | 1 | 82.2026 | 85.1458 | -116.9398 | 13.1807 | 124.9011 | 0.0075 | 0.0144 |
| 2024_09_19 22:00 | 3245074 | 2 | 79.6594 | 86.9545 | -114.7863 | 10.9334 | 196.2369 | 0.0060 | 0.0172 |
| 2024_09_19 22:00 | 3222830 | 3 | 91.7975 | 76.4036 | -116.9375 | 10.2392 | 126.3090 | 0.0154 | 0.0132 |
| 2024_09_19 22:00 | 3227086 | 4 | 83.4390 | 91.4946 | -114.7134 | 9.1065 | 157.8266 | 0.0117 | 0.0001 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412546_4231AA33 | 504990 | 342 | -89.1 | 504990 | 7 | -89.0 | 504990 | 419 | -99.3 | 504990 | 81 |
| MR_1774412546_7F3C28DC | 504990 | 342 | -86.2 | 504990 | 7 | -89.7 | 504990 | 419 | -97.8 | 504990 | 81 |
| MR_1774412546_987E90F2 | 504990 | 342 | -85.6 | 504990 | 7 | -88.9 | 504990 | 419 | -99.0 | 504990 | 81 |
| MR_1774412546_E47AC248 | 504990 | 342 | -87.9 | 504990 | 7 | -89.9 | 504990 | 419 | -100.2 | 504990 | 81 |
| MR_1774412546_F8778B81 | 504990 | 342 | -88.1 | 504990 | 7 | -90.1 | 504990 | 419 | -100.6 | 504990 | 81 |
| MR_1774412546_B802B267 | 504990 | 342 | -88.7 | 504990 | 7 | -88.5 | 504990 | 419 | -99.9 | 504990 | 81 |
| MR_1774412546_A48E4C41 | 504990 | 342 | -86.2 | 504990 | 7 | -89.1 | 504990 | 419 | -99.9 | 504990 | 81 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 775: `27edea6d-90d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `27edea6d-90d1-4019-9aa7-3f81be0a0005` |
| Tag | **multiple-answer** |
| 정답 | **C1|C4** |
| C1 의미 | Increase transmission power for 3278034_2 |
| C4 의미 | Adjust the azimuth of 3278034_2 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[775] topology](images/train_0775.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3278034_2 **← 정답**
- `C2`: Press down the tilt angle  of 3274625_1 by 2 degrees
- `C3`: Lift the tilt angle  of 3274625_1 by 2 degrees
- `C4`: Adjust the azimuth of 3278034_2 by 50 degrees **← 정답**
- `C5`: Adjust the azimuth of 3274625_1 by 43 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274625_1
- `C7`: Increase A3 Offset threshold for 3274625_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase transmission power for 3274625_1
- `C10`: Check test server and transmission issues
- `C11`: Increase A3 Offset threshold for 3278034_2
- `C12`: Add neighbor relationship between 3278034_2 and 3274625_1
- `C13`: Press down the tilt angle of 3278034_2 by 4 degrees
- `C14`: Decrease transmission power for 3278034_2
- `C15`: Decrease A3 Offset threshold for 3274625_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278034_2
- `C17`: Decrease transmission power for 3274625_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278034_2
- `C19`: Lift the tilt angle of 3278034_2 by 4 degrees
- `C20`: Decrease A3 Offset threshold for 3278034_2
- `C21`: Add neighbor relationship between 3228614_3 and 3274625_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274625_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.187 | MS1 | 121.4656729249 | 31.1446259293 | 668 | 504990 | -87.09 | 14.56 | 498.33 | 0.16 | 2.64 | 1589 |
| 2024-09-20 22:21:32.225 | MS1 | 121.4656687864 | 31.1446292353 | 668 | 504990 | -87.28 | 15.68 | 480.70 | 0.10 | 2.87 | 1578 |
| 2024-09-20 22:21:33.860 | MS1 | 121.4656598772 | 31.1446228210 | 668 | 504990 | -85.36 | 14.33 | 295.90 | 0.13 | 2.11 | 1578 |
| 2024-09-20 22:21:34.228 | MS1 | 121.4656772803 | 31.1446224981 | 668 | 504990 | -106.34 | -1.39 | 55.71 | 0.04 | 1.18 | 1594 |
| 2024-09-20 22:21:35.517 | MS1 | 121.4656778556 | 31.1446352051 | 668 | 504990 | -104.20 | -1.68 | 68.14 | 0.08 | 1.24 | 1563 |
| 2024-09-20 22:21:36.664 | MS1 | 121.4656643733 | 31.1446189540 | 668 | 504990 | -105.21 | 0.56 | 59.66 | 0.10 | 1.25 | 1571 |
| 2024-09-20 22:21:37.634 | MS1 | 121.4656583426 | 31.1446268426 | 668 | 504990 | -107.42 | 0.08 | 70.02 | 0.16 | 1.12 | 1599 |
| 2024-09-20 22:21:38.338 | MS1 | 121.4656655640 | 31.1446337195 | 668 | 504990 | -102.48 | -1.47 | 35.32 | 0.14 | 1.03 | 1567 |
| 2024-09-20 22:21:39.103 | MS1 | 121.4656622948 | 31.1446367627 | 668 | 504990 | -105.54 | 1.27 | 57.83 | 0.18 | 1.10 | 1576 |
| 2024-09-20 22:21:40.245 | MS1 | 121.4656609512 | 31.1446316028 | 668 | 504990 | -85.95 | 16.00 | 511.21 | 0.12 | 2.71 | 1586 |
| 2024-09-20 22:21:41.111 | MS1 | 121.4656640596 | 31.1446267604 | 668 | 504990 | -91.12 | 15.00 | 510.09 | 0.06 | 2.43 | 1579 |
| 2024-09-20 22:21:42.476 | MS1 | 121.4656619398 | 31.1446272931 | 668 | 504990 | -92.65 | 15.61 | 516.68 | 0.18 | 2.91 | 1565 |

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
| 3228614 | 3 | 121.4737126005 | 31.1552098987 | 192 | 7 | 5 | 42.8 | TDD | 741 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3262711 | 4 | 121.4743214838 | 31.1479439459 | 75 | 5 | 9 | 45.2 | TDD | 518 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3274625 | 1 | 121.4756663653 | 31.1526298795 | 184 | 1 | 12 | 32.1 | TDD | 848 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3278034 | 2 | 121.4647407916 | 31.1487632055 | 111 | 1 | 6 | 25.5 | TDD | 668 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.324 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.339 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.459 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.459 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.675 | NREventA2 | measId:1;ServCellPCI:238;Se... |
| 2024-09-20 22:21:34.820 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274625 | 1 | 16.2830 | 9.9258 | -116.0201 | 9.1113 | 168.6874 | 0.0034 | 0.0045 |
| 2024_09_20 22:00 | 3278034 | 2 | 7.5351 | 12.8294 | -115.9565 | 12.5456 | 172.2543 | 0.1089 | 0.0165 |
| 2024_09_20 22:00 | 3228614 | 3 | 17.1771 | 6.1597 | -116.5423 | 18.7674 | 186.9382 | 0.0119 | 0.0192 |
| 2024_09_20 22:00 | 3262711 | 4 | 19.6255 | 18.7431 | -116.3391 | 9.4083 | 162.3934 | 0.0090 | 0.0042 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413318_CE14AFD9 | 504990 | 668 | -106.4 | 504990 | 848 | -112.1 | 504990 | 741 | -118.3 | 504990 | 518 |
| MR_1774413318_0B50E296 | 504990 | 668 | -107.1 | 504990 | 848 | -110.0 | 504990 | 741 | -115.8 | 504990 | 518 |
| MR_1774413318_F237F562 | 504990 | 668 | -107.8 | 504990 | 848 | -111.2 | 504990 | 741 | -118.5 | 504990 | 518 |
| MR_1774413318_824588BA | 504990 | 668 | -105.9 | 504990 | 848 | -109.4 | 504990 | 741 | -118.0 | 504990 | 518 |
| MR_1774413318_459923FD | 504990 | 668 | -104.6 | 504990 | 848 | -109.1 | 504990 | 741 | -118.1 | 504990 | 518 |
| MR_1774413318_FD62B184 | 504990 | 668 | -105.3 | 504990 | 848 | -109.4 | 504990 | 741 | -118.3 | 504990 | 518 |
| MR_1774413318_9A7FBA88 | 504990 | 668 | -106.7 | 504990 | 848 | -110.3 | 504990 | 741 | -115.7 | 504990 | 518 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 776: `90772778-1f4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `90772778-1f49-448e-bf1f-0f402c8f3888` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[776] topology](images/train_0776.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3257880_3
- `C2`: Press down the tilt angle  of 3220246_4 by 10 degrees
- `C3`: Increase A3 Offset threshold for 3257880_3
- `C4`: Increase A3 Offset threshold for 3220246_4
- `C5`: Add neighbor relationship between 3215148_1 and 3220246_4
- `C6`: Adjust the azimuth of 3257880_3 by 24 degrees
- `C7`: Lift the tilt angle  of 3220246_4 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3257880_3
- `C9`: Decrease transmission power for 3220246_4
- `C10`: Adjust the azimuth of 3220246_4 by 50 degrees
- `C11`: Decrease A3 Offset threshold for 3220246_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257880_3
- `C13`: Press down the tilt angle of 3257880_3 by 6 degrees
- `C14`: Add neighbor relationship between 3257880_3 and 3220246_4
- `C15`: Insufficient data; more data is needed for judgment. **← 정답**
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220246_4
- `C17`: Lift the tilt angle of 3257880_3 by 6 degrees
- `C18`: Decrease transmission power for 3257880_3
- `C19`: Increase transmission power for 3220246_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257880_3
- `C21`: Check test server and transmission issues
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220246_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.554 | MS1 | 121.4656779276 | 31.1446361835 | 973 | 504990 | -88.69 | 16.75 | 343.97 | 0.01 | 2.08 | 1593 |
| 2024-09-20 22:21:32.837 | MS1 | 121.4656763549 | 31.1446313042 | 973 | 504990 | -88.57 | 12.61 | 376.21 | 0.09 | 2.03 | 1561 |
| 2024-09-20 22:21:33.136 | MS1 | 121.4656624961 | 31.1446277404 | 973 | 504990 | -90.90 | 17.42 | 546.49 | 0.06 | 2.77 | 1583 |
| 2024-09-20 22:21:34.969 | MS1 | 121.4656715375 | 31.1446326118 | 973 | 504990 | -87.71 | 16.27 | 86.45 | 0.13 | 2.79 | 1571 |
| 2024-09-20 22:21:35.251 | MS1 | 121.4656642586 | 31.1446200666 | 973 | 504990 | -86.58 | 13.53 | 72.30 | 0.03 | 2.88 | 1586 |
| 2024-09-20 22:21:36.263 | MS1 | 121.4656698628 | 31.1446259534 | 973 | 504990 | -85.33 | 12.17 | 64.73 | 0.12 | 2.19 | 1583 |
| 2024-09-20 22:21:37.238 | MS1 | 121.4656772723 | 31.1446364780 | 973 | 504990 | -89.85 | 8.06 | 61.87 | 0.10 | 2.31 | 1594 |
| 2024-09-20 22:21:38.133 | MS1 | 121.4656684498 | 31.1446309486 | 973 | 504990 | -92.00 | 8.98 | 72.65 | 0.14 | 2.84 | 1589 |
| 2024-09-20 22:21:39.279 | MS1 | 121.4656631520 | 31.1446193709 | 973 | 504990 | -91.11 | 11.67 | 94.15 | 0.11 | 2.97 | 1591 |
| 2024-09-20 22:21:40.544 | MS1 | 121.4656592402 | 31.1446229565 | 973 | 504990 | -89.19 | 11.44 | 476.08 | 0.09 | 2.35 | 1570 |
| 2024-09-20 22:21:41.140 | MS1 | 121.4656745995 | 31.1446228153 | 973 | 504990 | -90.62 | 7.88 | 589.84 | 0.01 | 2.13 | 1591 |
| 2024-09-20 22:21:42.376 | MS1 | 121.4656732467 | 31.1446239871 | 973 | 504990 | -92.93 | 10.44 | 487.54 | 0.13 | 2.87 | 1561 |

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
| 3215148 | 1 | 121.4672463194 | 31.1535659500 | 157 | 8 | 9 | 34.4 | TDD | 992 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3219439 | 2 | 121.4679755683 | 31.1520628778 | 320 | 7 | 10 | 48.1 | TDD | 699 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3220246 | 4 | 121.4676626566 | 31.1486238442 | 9 | 7 | 6 | 24.1 | TDD | 7 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3257880 | 3 | 121.4703673890 | 31.1515477863 | 186 | 3 | 3 | 46.1 | TDD | 973 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.923 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.939 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.065 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.065 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.809 | NREventA3 | measId:2;ServCellPCI:113;Se... |
| 2024-09-20 22:21:38.049 | NRHandoverAttempt | SourcePCI:113;SourceNR-ARFC... |
| 2024-09-20 22:21:38.099 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.114 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.253 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.253 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3215148 | 1 | 79.9216 | 84.0895 | -117.0581 | 8.4670 | 184.3326 | 0.0156 | 0.0144 |
| 2024_09_19 22:00 | 3219439 | 2 | 81.0050 | 77.7234 | -117.8324 | 9.3113 | 165.2963 | 0.0172 | 0.0169 |
| 2024_09_19 22:00 | 3257880 | 3 | 92.7767 | 94.9689 | -114.3477 | 18.9009 | 131.9618 | 0.0088 | 0.0007 |
| 2024_09_19 22:00 | 3220246 | 4 | 82.3982 | 82.9713 | -117.5433 | 14.8081 | 188.2747 | 0.0147 | 0.0005 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413013_D3C1F7C2 | 504990 | 973 | -87.9 | 504990 | 7 | -90.4 | 504990 | 992 | -93.4 | 504990 | 699 |
| MR_1774413013_2E0B8600 | 504990 | 973 | -85.7 | 504990 | 7 | -88.4 | 504990 | 992 | -95.5 | 504990 | 699 |
| MR_1774413013_9EC386C1 | 504990 | 973 | -87.9 | 504990 | 7 | -88.3 | 504990 | 992 | -95.5 | 504990 | 699 |
| MR_1774413013_77F9ADA4 | 504990 | 973 | -89.5 | 504990 | 7 | -88.7 | 504990 | 992 | -94.8 | 504990 | 699 |
| MR_1774413013_AC538598 | 504990 | 973 | -86.5 | 504990 | 7 | -92.1 | 504990 | 992 | -95.7 | 504990 | 699 |
| MR_1774413013_CB09A4D4 | 504990 | 973 | -86.8 | 504990 | 7 | -88.8 | 504990 | 992 | -94.6 | 504990 | 699 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 777: `e9852b17-f8f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e9852b17-f8f8-44d8-ba85-f5485afc2fc7` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Lift the tilt angle  of 3254245_4 by 9 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[777] topology](images/train_0777.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3250643_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262727_1
- `C3`: Check test server and transmission issues
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250643_2
- `C5`: Decrease A3 Offset threshold for 3262727_1
- `C6`: Add neighbor relationship between 3254245_4 and 3250643_2
- `C7`: Press down the tilt angle of 3262727_1 by 2 degrees
- `C8`: Lift the tilt angle  of 3254245_4 by 9 degrees **← 정답**
- `C9`: Press down the tilt angle  of 3254245_4 by 9 degrees
- `C10`: Increase A3 Offset threshold for 3250643_2
- `C11`: Adjust the azimuth of 3262727_1 by 35 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250643_2
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Increase transmission power for 3262727_1
- `C15`: Decrease A3 Offset threshold for 3250643_2
- `C16`: Decrease transmission power for 3262727_1
- `C17`: Increase A3 Offset threshold for 3262727_1
- `C18`: Adjust the azimuth of 3254245_4 by 50 degrees
- `C19`: Decrease transmission power for 3250643_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262727_1
- `C21`: Add neighbor relationship between 3262727_1 and 3250643_2
- `C22`: Lift the tilt angle of 3262727_1 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.134 | MS1 | 121.4656604485 | 31.1446208563 | 898 | 504990 | -86.75 | 17.70 | 565.98 | 0.11 | 2.49 | 1563 |
| 2024-09-20 22:21:32.905 | MS1 | 121.4656701072 | 31.1446341079 | 898 | 504990 | -90.57 | 12.21 | 407.82 | 0.00 | 2.06 | 1564 |
| 2024-09-20 22:21:33.141 | MS1 | 121.4656678804 | 31.1446292580 | 898 | 504990 | -86.75 | 16.26 | 303.04 | 0.04 | 2.82 | 1584 |
| 2024-09-20 22:21:34.431 | MS1 | 121.4656701140 | 31.1446200758 | 898 | 504990 | -89.99 | 13.30 | 73.73 | 0.15 | 2.46 | 1591 |
| 2024-09-20 22:21:35.358 | MS1 | 121.4656752346 | 31.1446359025 | 898 | 504990 | -87.27 | 17.22 | 67.34 | 0.02 | 2.46 | 1599 |
| 2024-09-20 22:21:36.636 | MS1 | 121.4656613905 | 31.1446334117 | 898 | 504990 | -87.59 | 15.54 | 85.36 | 0.13 | 2.84 | 1577 |
| 2024-09-20 22:21:37.817 | MS1 | 121.4656582029 | 31.1446182518 | 898 | 504990 | -91.91 | 7.48 | 67.97 | 0.04 | 2.99 | 1599 |
| 2024-09-20 22:21:38.538 | MS1 | 121.4656647777 | 31.1446325047 | 898 | 504990 | -93.58 | 9.45 | 83.79 | 0.11 | 2.58 | 1560 |
| 2024-09-20 22:21:39.809 | MS1 | 121.4656708012 | 31.1446262001 | 898 | 504990 | -93.57 | 10.13 | 56.48 | 0.17 | 2.54 | 1572 |
| 2024-09-20 22:21:40.481 | MS1 | 121.4656776649 | 31.1446286339 | 898 | 504990 | -90.88 | 7.84 | 353.48 | 0.00 | 2.09 | 1586 |
| 2024-09-20 22:21:41.512 | MS1 | 121.4656640325 | 31.1446220941 | 898 | 504990 | -89.16 | 11.07 | 417.79 | 0.06 | 2.14 | 1572 |
| 2024-09-20 22:21:42.555 | MS1 | 121.4656668701 | 31.1446277847 | 898 | 504990 | -92.27 | 7.47 | 432.45 | 0.12 | 2.60 | 1560 |

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
| 3221869 | 3 | 121.4715296171 | 31.1527409446 | 58 | 8 | 3 | 31.9 | TDD | 60 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3250643 | 2 | 121.4644142964 | 31.1525870188 | 72 | 7 | 5 | 37.7 | TDD | 291 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3254245 | 4 | 121.4725069650 | 31.1450647269 | 57 | 15 | 12 | 36.9 | TDD | 79 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3262727 | 1 | 121.4671479495 | 31.1522254239 | 154 | 0 | 4 | 24.1 | TDD | 898 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.946 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.971 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.103 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.103 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.797 | NREventA3 | measId:2;ServCellPCI:598;Se... |
| 2024-09-20 22:21:38.037 | NRHandoverAttempt | SourcePCI:598;SourceNR-ARFC... |
| 2024-09-20 22:21:38.074 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.085 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.214 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.214 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262727 | 1 | 75.4829 | 79.0631 | -114.6349 | 12.1871 | 183.1535 | 0.0083 | 0.0183 |
| 2024_09_20 22:00 | 3250643 | 2 | 11.5212 | 19.5909 | -114.5918 | 18.9857 | 126.1347 | 0.0174 | 0.0163 |
| 2024_09_20 22:00 | 3221869 | 3 | 15.1426 | 8.7701 | -114.9609 | 13.8004 | 121.7951 | 0.0197 | 0.0152 |
| 2024_09_20 22:00 | 3254245 | 4 | 6.8314 | 14.9550 | -114.5952 | 8.1769 | 181.2792 | 0.0134 | 0.0002 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415832_34E02DF7 | 504990 | 898 | -89.9 | 504990 | 291 | -95.6 | 504990 | 79 | -97.0 | 504990 | 60 |
| MR_1774415832_CD90FCC5 | 504990 | 898 | -88.1 | 504990 | 291 | -96.2 | 504990 | 79 | -95.9 | 504990 | 60 |
| MR_1774415832_A2398BD7 | 504990 | 898 | -88.6 | 504990 | 291 | -94.3 | 504990 | 79 | -97.1 | 504990 | 60 |
| MR_1774415832_67A6BAF8 | 504990 | 898 | -89.2 | 504990 | 291 | -96.7 | 504990 | 79 | -96.7 | 504990 | 60 |
| MR_1774415832_7BD9BB1C | 504990 | 898 | -88.1 | 504990 | 291 | -95.8 | 504990 | 79 | -98.1 | 504990 | 60 |
| MR_1774415832_25FAC99A | 504990 | 898 | -90.0 | 504990 | 291 | -95.5 | 504990 | 79 | -98.1 | 504990 | 60 |
| MR_1774415832_00B0C011 | 504990 | 898 | -90.5 | 504990 | 291 | -95.8 | 504990 | 79 | -97.2 | 504990 | 60 |
| MR_1774415832_67C421C6 | 504990 | 898 | -90.3 | 504990 | 291 | -96.1 | 504990 | 79 | -98.0 | 504990 | 60 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 778: `6d1c9ec5-52d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6d1c9ec5-52db-447a-ab3f-6ae0d5b2fd42` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Lift the tilt angle  of 3246576_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[778] topology](images/train_0778.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3215426_3
- `C2`: Lift the tilt angle  of 3246576_2 by 10 degrees **← 정답**
- `C3`: Add neighbor relationship between 3246576_2 and 3215426_3
- `C4`: Decrease transmission power for 3255460_1
- `C5`: Decrease A3 Offset threshold for 3215426_3
- `C6`: Increase transmission power for 3255460_1
- `C7`: Check test server and transmission issues
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255460_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255460_1
- `C10`: Decrease A3 Offset threshold for 3255460_1
- `C11`: Increase A3 Offset threshold for 3255460_1
- `C12`: Press down the tilt angle of 3255460_1 by 4 degrees
- `C13`: Press down the tilt angle  of 3246576_2 by 10 degrees
- `C14`: Increase transmission power for 3215426_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215426_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215426_3
- `C17`: Adjust the azimuth of 3246576_2 by 50 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Add neighbor relationship between 3255460_1 and 3215426_3
- `C20`: Lift the tilt angle of 3255460_1 by 4 degrees
- `C21`: Adjust the azimuth of 3255460_1 by 13 degrees
- `C22`: Decrease transmission power for 3215426_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.730 | MS1 | 121.4656731881 | 31.1446375101 | 401 | 504990 | -91.13 | 17.52 | 550.78 | 0.04 | 2.02 | 1568 |
| 2024-09-20 22:21:32.191 | MS1 | 121.4656695730 | 31.1446330471 | 401 | 504990 | -89.03 | 14.87 | 565.08 | 0.13 | 2.53 | 1600 |
| 2024-09-20 22:21:33.808 | MS1 | 121.4656726776 | 31.1446322239 | 401 | 504990 | -91.43 | 15.05 | 504.02 | 0.09 | 2.66 | 1579 |
| 2024-09-20 22:21:34.731 | MS1 | 121.4656588981 | 31.1446181207 | 401 | 504990 | -86.52 | 12.49 | 64.70 | 0.16 | 2.35 | 1600 |
| 2024-09-20 22:21:35.352 | MS1 | 121.4656759551 | 31.1446208880 | 401 | 504990 | -91.57 | 14.14 | 77.79 | 0.12 | 2.77 | 1581 |
| 2024-09-20 22:21:36.181 | MS1 | 121.4656649726 | 31.1446352042 | 401 | 504990 | -87.11 | 13.07 | 62.34 | 0.14 | 2.05 | 1568 |
| 2024-09-20 22:21:37.820 | MS1 | 121.4656666713 | 31.1446239720 | 401 | 504990 | -89.06 | 11.19 | 57.63 | 0.17 | 2.47 | 1579 |
| 2024-09-20 22:21:38.145 | MS1 | 121.4656713038 | 31.1446226880 | 401 | 504990 | -92.86 | 11.03 | 50.56 | 0.18 | 2.09 | 1579 |
| 2024-09-20 22:21:39.631 | MS1 | 121.4656771217 | 31.1446331628 | 401 | 504990 | -93.05 | 9.51 | 81.85 | 0.07 | 2.11 | 1586 |
| 2024-09-20 22:21:40.361 | MS1 | 121.4656671087 | 31.1446334815 | 401 | 504990 | -92.61 | 11.54 | 581.85 | 0.11 | 2.77 | 1567 |
| 2024-09-20 22:21:41.176 | MS1 | 121.4656671208 | 31.1446326250 | 401 | 504990 | -93.76 | 8.54 | 419.36 | 0.01 | 2.10 | 1564 |
| 2024-09-20 22:21:42.760 | MS1 | 121.4656700172 | 31.1446364179 | 401 | 504990 | -93.77 | 9.42 | 389.20 | 0.16 | 2.51 | 1597 |

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
| 3215426 | 3 | 121.4698031817 | 31.1457783669 | 145 | 13 | 3 | 33.1 | TDD | 111 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3228083 | 4 | 121.4660438904 | 31.1528979341 | 203 | 0 | 12 | 42.0 | TDD | 839 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3246576 | 2 | 121.4737446143 | 31.1558961566 | 74 | 0 | 8 | 48.5 | TDD | 930 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3255460 | 1 | 121.4739358329 | 31.1493308837 | 249 | 2 | 1 | 28.0 | TDD | 401 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.104 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.126 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.247 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.247 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.982 | NREventA3 | measId:2;ServCellPCI:926;Se... |
| 2024-09-20 22:21:38.222 | NRHandoverAttempt | SourcePCI:926;SourceNR-ARFC... |
| 2024-09-20 22:21:38.264 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.279 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.383 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.383 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255460 | 1 | 84.7840 | 94.3290 | -114.3323 | 12.5783 | 139.7005 | 0.0176 | 0.0133 |
| 2024_09_20 22:00 | 3246576 | 2 | 11.8382 | 12.0333 | -114.4658 | 11.9047 | 143.3653 | 0.0022 | 0.0057 |
| 2024_09_20 22:00 | 3215426 | 3 | 14.0614 | 18.8171 | -114.0336 | 15.7222 | 152.1135 | 0.0111 | 0.0142 |
| 2024_09_20 22:00 | 3228083 | 4 | 5.1692 | 11.2007 | -116.2725 | 13.6580 | 122.3845 | 0.0054 | 0.0167 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415401_C7214177 | 504990 | 401 | -86.6 | 504990 | 111 | -88.2 | 504990 | 930 | -93.4 | 504990 | 839 |
| MR_1774415401_62A2FD84 | 504990 | 401 | -87.4 | 504990 | 111 | -90.2 | 504990 | 930 | -94.9 | 504990 | 839 |
| MR_1774415401_192E0CF6 | 504990 | 401 | -87.0 | 504990 | 111 | -89.1 | 504990 | 930 | -94.0 | 504990 | 839 |
| MR_1774415401_C7FF7B53 | 504990 | 401 | -86.3 | 504990 | 111 | -90.5 | 504990 | 930 | -93.8 | 504990 | 839 |
| MR_1774415401_948DF119 | 504990 | 401 | -86.1 | 504990 | 111 | -89.4 | 504990 | 930 | -94.9 | 504990 | 839 |
| MR_1774415401_54D7CF25 | 504990 | 401 | -87.7 | 504990 | 111 | -89.4 | 504990 | 930 | -95.5 | 504990 | 839 |
| MR_1774415401_9DD06159 | 504990 | 401 | -86.2 | 504990 | 111 | -88.7 | 504990 | 930 | -95.2 | 504990 | 839 |
| MR_1774415401_8E3C005A | 504990 | 401 | -88.4 | 504990 | 111 | -89.5 | 504990 | 930 | -93.5 | 504990 | 839 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 779: `49490005-464...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `49490005-4648-4135-ace8-f07d2b280858` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[779] topology](images/train_0779.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3276273_3 by 10 degrees
- `C2`: Add neighbor relationship between 3220378_1 and 3257025_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276273_3
- `C4`: Decrease A3 Offset threshold for 3257025_4
- `C5`: Increase transmission power for 3276273_3
- `C6`: Decrease transmission power for 3257025_4
- `C7`: Increase A3 Offset threshold for 3257025_4
- `C8`: Lift the tilt angle  of 3257025_4 by 7 degrees
- `C9`: Increase A3 Offset threshold for 3276273_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257025_4
- `C11`: Press down the tilt angle of 3276273_3 by 10 degrees
- `C12`: Decrease transmission power for 3276273_3
- `C13`: Adjust the azimuth of 3276273_3 by 14 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276273_3
- `C15`: Insufficient data; more data is needed for judgment. **← 정답**
- `C16`: Decrease A3 Offset threshold for 3276273_3
- `C17`: Add neighbor relationship between 3276273_3 and 3257025_4
- `C18`: Press down the tilt angle  of 3257025_4 by 7 degrees
- `C19`: Check test server and transmission issues
- `C20`: Adjust the azimuth of 3257025_4 by 17 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257025_4
- `C22`: Increase transmission power for 3257025_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.272 | MS1 | 121.4656642917 | 31.1446211431 | 78 | 504990 | -88.27 | 15.20 | 470.26 | 0.17 | 2.71 | 1597 |
| 2024-09-20 22:21:32.391 | MS1 | 121.4656754475 | 31.1446278458 | 78 | 504990 | -86.15 | 12.41 | 516.38 | 0.04 | 2.20 | 1571 |
| 2024-09-20 22:21:33.400 | MS1 | 121.4656713346 | 31.1446284278 | 78 | 504990 | -87.14 | 17.91 | 502.06 | 0.04 | 2.90 | 1565 |
| 2024-09-20 22:21:34.126 | MS1 | 121.4656742052 | 31.1446333016 | 78 | 504990 | -87.29 | 16.65 | 76.79 | 0.11 | 2.05 | 1560 |
| 2024-09-20 22:21:35.116 | MS1 | 121.4656634981 | 31.1446204445 | 78 | 504990 | -90.98 | 15.34 | 80.93 | 0.07 | 2.35 | 1591 |
| 2024-09-20 22:21:36.986 | MS1 | 121.4656668466 | 31.1446363746 | 78 | 504990 | -88.44 | 13.92 | 60.61 | 0.10 | 2.20 | 1570 |
| 2024-09-20 22:21:37.975 | MS1 | 121.4656739382 | 31.1446213621 | 78 | 504990 | -93.47 | 9.22 | 98.69 | 0.05 | 2.24 | 1569 |
| 2024-09-20 22:21:38.637 | MS1 | 121.4656593272 | 31.1446376771 | 78 | 504990 | -92.04 | 7.69 | 73.75 | 0.01 | 2.67 | 1561 |
| 2024-09-20 22:21:39.626 | MS1 | 121.4656761659 | 31.1446282351 | 78 | 504990 | -90.07 | 11.11 | 99.01 | 0.10 | 2.13 | 1567 |
| 2024-09-20 22:21:40.196 | MS1 | 121.4656713178 | 31.1446285613 | 78 | 504990 | -91.40 | 10.07 | 557.34 | 0.07 | 2.95 | 1572 |
| 2024-09-20 22:21:41.440 | MS1 | 121.4656712085 | 31.1446377413 | 78 | 504990 | -91.28 | 12.19 | 385.95 | 0.02 | 2.84 | 1570 |
| 2024-09-20 22:21:42.733 | MS1 | 121.4656726420 | 31.1446223592 | 78 | 504990 | -89.62 | 10.62 | 386.60 | 0.13 | 2.62 | 1577 |

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
| 3213908 | 2 | 121.4666654306 | 31.1522083966 | 299 | 0 | 6 | 36.4 | TDD | 924 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3220378 | 1 | 121.4692594098 | 31.1518248787 | 227 | 14 | 7 | 27.5 | TDD | 218 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3257025 | 4 | 121.4750738084 | 31.1512444548 | 248 | 5 | 1 | 36.5 | TDD | 270 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3276273 | 3 | 121.4683445258 | 31.1448975793 | 277 | 10 | 7 | 41.7 | TDD | 78 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.831 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.980 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.980 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.685 | NREventA3 | measId:2;ServCellPCI:95;Ser... |
| 2024-09-20 22:21:37.925 | NRHandoverAttempt | SourcePCI:95;SourceNR-ARFCN... |
| 2024-09-20 22:21:37.958 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.971 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.121 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.121 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3220378 | 1 | 93.2338 | 92.3896 | -114.4566 | 15.2999 | 150.1932 | 0.0045 | 0.0129 |
| 2024_09_19 22:00 | 3213908 | 2 | 83.5934 | 84.3768 | -114.4913 | 16.0824 | 138.9234 | 0.0090 | 0.0084 |
| 2024_09_19 22:00 | 3276273 | 3 | 75.3168 | 91.2739 | -114.8741 | 14.7862 | 110.2096 | 0.0053 | 0.0180 |
| 2024_09_19 22:00 | 3257025 | 4 | 86.4655 | 83.2539 | -115.7472 | 14.0267 | 138.0086 | 0.0038 | 0.0035 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413781_E7DEC045 | 504990 | 78 | -87.6 | 504990 | 270 | -95.6 | 504990 | 218 | -97.0 | 504990 | 924 |
| MR_1774413781_89CDD275 | 504990 | 78 | -85.6 | 504990 | 270 | -95.1 | 504990 | 218 | -98.9 | 504990 | 924 |
| MR_1774413781_38FD2882 | 504990 | 78 | -87.5 | 504990 | 270 | -95.5 | 504990 | 218 | -96.3 | 504990 | 924 |
| MR_1774413781_E1C16DDC | 504990 | 78 | -87.1 | 504990 | 270 | -95.6 | 504990 | 218 | -99.2 | 504990 | 924 |
| MR_1774413781_0AD56F70 | 504990 | 78 | -86.7 | 504990 | 270 | -97.4 | 504990 | 218 | -96.1 | 504990 | 924 |
| MR_1774413781_E094737C | 504990 | 78 | -87.9 | 504990 | 270 | -95.8 | 504990 | 218 | -97.1 | 504990 | 924 |
| MR_1774413781_9F61765B | 504990 | 78 | -88.4 | 504990 | 270 | -96.3 | 504990 | 218 | -96.1 | 504990 | 924 |

> *... 2개 열 생략 (전체 14열)*

---
