# Track A 문제 분석 — train[130]~train[139]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[130] ~ train[139] (10개)

## 목차

1. [문제 130: `381b6c9b-12b...`](#130) — single-answer, 정답: C2
2. [문제 131: `e1f64207-558...`](#131) — single-answer, 정답: C4
3. [문제 132: `14d8e16e-79f...`](#132) — single-answer, 정답: C4
4. [문제 133: `34b6af83-1e7...`](#133) — single-answer, 정답: C10
5. [문제 134: `d590a22a-a3b...`](#134) — single-answer, 정답: C1
6. [문제 135: `4d60edd6-b73...`](#135) — single-answer, 정답: C22
7. [문제 136: `9677f010-52f...`](#136) — multiple-answer, 정답: C10|C18
8. [문제 137: `c099aacc-732...`](#137) — single-answer, 정답: C10
9. [문제 138: `4ad88a7d-acb...`](#138) — multiple-answer, 정답: C3|C10|C12|C15
10. [문제 139: `00a9aa39-51b...`](#139) — single-answer, 정답: C10

---

### 문제 130: `381b6c9b-12b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `381b6c9b-12b5-4a03-9bf7-e57bec4ac21f` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255301_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[130] topology](images/train_0130.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253809_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255301_5 **← 정답**
- `C3`: Increase transmission power for 3255301_5
- `C4`: Lift the tilt angle  of 3253809_1 by 2 degrees
- `C5`: Check test server and transmission issues
- `C6`: Increase transmission power for 3253809_1
- `C7`: Increase A3 Offset threshold for 3255301_5
- `C8`: Add neighbor relationship between 3255301_5 and 3253809_1
- `C9`: Press down the tilt angle of 3255301_5 by 3 degrees
- `C10`: Press down the tilt angle  of 3253809_1 by 2 degrees
- `C11`: Add neighbor relationship between 3279044_13 and 3253809_1
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Adjust the azimuth of 3253809_1 by 7 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253809_1
- `C15`: Lift the tilt angle of 3255301_5 by 3 degrees
- `C16`: Decrease transmission power for 3255301_5
- `C17`: Decrease A3 Offset threshold for 3255301_5
- `C18`: Adjust the azimuth of 3255301_5 by 44 degrees
- `C19`: Decrease transmission power for 3253809_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255301_5
- `C21`: Decrease A3 Offset threshold for 3253809_1
- `C22`: Increase A3 Offset threshold for 3253809_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.821 | MS1 | 121.4656637482 | 31.1446322568 | 347 | 504990 | -94.74 | 14.72 | 493.16 | 0.14 | 2.75 | 1586 |
| 2024-09-20 22:21:32.677 | MS1 | 121.4656767226 | 31.1446269386 | 558 | 504990 | -94.93 | 10.70 | 501.96 | 0.01 | 2.44 | 1563 |
| 2024-09-20 22:21:33.948 | MS1 | 121.4656771195 | 31.1446324168 | 473 | 504990 | -94.06 | 14.45 | 316.41 | 0.11 | 2.25 | 1569 |
| 2024-09-20 22:21:34.517 | MS1 | 121.4656702870 | 31.1446192231 | 690 | 152650 | -88.14 | 4.65 | 49.49 | 0.18 | 1.84 | 904 |
| 2024-09-20 22:21:35.564 | MS1 | 121.4656654698 | 31.1446301354 | 909 | 152650 | -87.89 | 6.26 | 86.81 | 0.01 | 1.60 | 927 |
| 2024-09-20 22:21:36.795 | MS1 | 121.4656715734 | 31.1446233477 | 920 | 152650 | -87.28 | 7.45 | 77.08 | 0.05 | 1.53 | 903 |
| 2024-09-20 22:21:37.274 | MS1 | 121.4656761393 | 31.1446237279 | 681 | 152650 | -88.81 | 5.65 | 66.69 | 0.11 | 1.90 | 990 |
| 2024-09-20 22:21:38.103 | MS1 | 121.4656678982 | 31.1446298356 | 690 | 152650 | -91.96 | 6.16 | 78.54 | 0.05 | 1.60 | 949 |
| 2024-09-20 22:21:39.365 | MS1 | 121.4656689743 | 31.1446230707 | 909 | 152650 | -87.46 | 5.10 | 88.00 | 0.00 | 1.83 | 987 |
| 2024-09-20 22:21:40.729 | MS1 | 121.4656755642 | 31.1446243792 | 920 | 152650 | -89.97 | 7.05 | 69.80 | 0.14 | 2.11 | 1582 |
| 2024-09-20 22:21:41.564 | MS1 | 121.4656645146 | 31.1446232987 | 681 | 152650 | -95.75 | 3.00 | 86.70 | 0.10 | 2.96 | 1598 |
| 2024-09-20 22:21:42.798 | MS1 | 121.4656628520 | 31.1446242970 | 690 | 152650 | -95.59 | 4.78 | 79.55 | 0.14 | 2.74 | 1561 |

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
| 3222875 | 6 | 121.4727070398 | 31.1474776507 | 284 | 10 | 5 | 29.4 | TDD | 605 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3223895 | 10 | 121.4710023392 | 31.1447685059 | 357 | 9 | 11 | 21.2 | FDD | 690 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3226130 | 7 | 121.4699231484 | 31.1518215807 | 150 | 7 | 11 | 19.6 | FDD | 576 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3236288 | 8 | 121.4668330736 | 31.1536231948 | 41 | 14 | 1 | 3.4 | FDD | 681 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3238112 | 11 | 121.4725089665 | 31.1527951062 | 266 | 5 | 6 | 26.1 | FDD | 498 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3239766 | 3 | 121.4733060840 | 31.1554036376 | 39 | 0 | 10 | 23.7 | TDD | 407 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3250674 | 4 | 121.4691443578 | 31.1499311572 | 330 | 10 | 10 | 11.8 | TDD | 473 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3253809 | 1 | 121.4702375064 | 31.1532401274 | 211 | 2 | 2 | 7.2 | TDD | 580 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3255301 | 5 | 121.4730796097 | 31.1470597092 | 293 | 2 | 2 | 15.5 | TDD | 347 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3259898 | 2 | 121.4654678333 | 31.1465168852 | 285 | 6 | 2 | 1.2 | TDD | 558 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3264067 | 12 | 121.4662442288 | 31.1498133919 | 68 | 7 | 3 | 14.1 | FDD | 596 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3273137 | 9 | 121.4672379854 | 31.1514517098 | 150 | 10 | 9 | 17.2 | FDD | 909 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3279044 | 13 | 121.4662336724 | 31.1497051655 | 162 | 8 | 1 | 19.9 | FDD | 920 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |

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
| 2024-09-20 22:21:31.280 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.304 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.429 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.429 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.087 | NREventA2 | measId:1;ServCellPCI:896;Se... |
| 2024-09-20 22:21:35.198 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.494 | NREventA5 | measId:3;ServCellPCI:896;Se... |
| 2024-09-20 22:21:35.544 | NRHandoverAttempt | SourcePCI:896;SourceNR-ARFC... |
| 2024-09-20 22:21:35.569 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.584 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.704 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.704 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253809 | 1 | 15.9100 | 16.5654 | -115.2390 | 5.7824 | 179.4315 | 0.0196 | 0.0174 |
| 2024_09_20 22:00 | 3259898 | 2 | 5.1527 | 17.1045 | -115.7046 | 10.2293 | 159.2545 | 0.0121 | 0.0112 |
| 2024_09_20 22:00 | 3239766 | 3 | 10.9852 | 6.5799 | -114.5800 | 19.6127 | 149.8818 | 0.0027 | 0.0168 |
| 2024_09_20 22:00 | 3250674 | 4 | 19.7787 | 5.1604 | -114.4800 | 5.5859 | 133.6043 | 0.0164 | 0.0058 |
| 2024_09_20 22:00 | 3255301 | 5 | 14.9827 | 7.1112 | -114.9998 | 19.7116 | 194.1496 | 0.0038 | 0.0024 |
| 2024_09_20 22:00 | 3222875 | 6 | 13.1370 | 5.9540 | -116.9886 | 19.0090 | 150.7799 | 0.0003 | 0.0171 |
| 2024_09_20 22:00 | 3226130 | 7 | 6.3779 | 17.2379 | -117.7140 | 3.7249 | 23.8938 | 0.0062 | 0.0026 |
| 2024_09_20 22:00 | 3236288 | 8 | 17.6803 | 9.2743 | -117.9507 | 3.8133 | 33.9429 | 0.0197 | 0.0024 |
| 2024_09_20 22:00 | 3273137 | 9 | 18.0513 | 12.6632 | -115.0193 | 4.9795 | 55.8267 | 0.0147 | 0.0163 |
| 2024_09_20 22:00 | 3223895 | 10 | 17.3753 | 5.5056 | -115.3315 | 3.7616 | 52.9125 | 0.0074 | 0.0027 |
| 2024_09_20 22:00 | 3238112 | 11 | 16.9067 | 12.9634 | -117.6769 | 4.8305 | 26.8547 | 0.0169 | 0.0053 |
| 2024_09_20 22:00 | 3264067 | 12 | 12.9631 | 9.3198 | -115.1978 | 4.5149 | 46.2157 | 0.0117 | 0.0011 |
| 2024_09_20 22:00 | 3279044 | 13 | 13.8130 | 15.5482 | -115.1998 | 3.6452 | 23.9937 | 0.0103 | 0.0105 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417165_10B74F89 | 152650 | 690 | -88.6 | 152650 | 576 | -95.4 | 152650 | 498 | -100.1 | 152650 | 596 |
| MR_1774417165_733F3A72 | 152650 | 690 | -88.7 | 152650 | 576 | -92.7 | 152650 | 498 | -101.1 | 152650 | 596 |
| MR_1774417165_ED2A46C2 | 152650 | 690 | -87.5 | 152650 | 576 | -93.8 | 152650 | 498 | -97.4 | 152650 | 596 |
| MR_1774417165_53C09AF2 | 152650 | 690 | -88.4 | 152650 | 576 | -94.6 | 152650 | 498 | -97.7 | 152650 | 596 |
| MR_1774417165_3E69CE8E | 152650 | 690 | -89.0 | 152650 | 576 | -95.9 | 152650 | 498 | -100.3 | 152650 | 596 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 131: `e1f64207-558...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e1f64207-558d-45ec-ada7-e492d63fbb01` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[131] topology](images/train_0131.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229745_2
- `C2`: Check test server and transmission issues
- `C3`: Increase transmission power for 3239542_3
- `C4`: Insufficient data; more data is needed for judgment. **← 정답**
- `C5`: Add neighbor relationship between 3239542_3 and 3229745_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239542_3
- `C7`: Decrease A3 Offset threshold for 3239542_3
- `C8`: Add neighbor relationship between 3246892_1 and 3229745_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239542_3
- `C10`: Lift the tilt angle  of 3229745_2 by 6 degrees
- `C11`: Increase A3 Offset threshold for 3239542_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229745_2
- `C13`: Press down the tilt angle  of 3229745_2 by 6 degrees
- `C14`: Adjust the azimuth of 3229745_2 by 50 degrees
- `C15`: Decrease transmission power for 3229745_2
- `C16`: Press down the tilt angle of 3239542_3 by 10 degrees
- `C17`: Adjust the azimuth of 3239542_3 by 13 degrees
- `C18`: Decrease transmission power for 3239542_3
- `C19`: Decrease A3 Offset threshold for 3229745_2
- `C20`: Increase A3 Offset threshold for 3229745_2
- `C21`: Increase transmission power for 3229745_2
- `C22`: Lift the tilt angle of 3239542_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.705 | MS1 | 121.4656703862 | 31.1446365406 | 302 | 504990 | -88.39 | 13.28 | 356.39 | 0.09 | 2.04 | 1587 |
| 2024-09-20 22:21:32.629 | MS1 | 121.4656658109 | 31.1446200569 | 302 | 504990 | -85.07 | 16.00 | 468.97 | 0.01 | 2.16 | 1580 |
| 2024-09-20 22:21:33.720 | MS1 | 121.4656684164 | 31.1446184843 | 302 | 504990 | -88.44 | 16.81 | 313.46 | 0.09 | 2.00 | 1570 |
| 2024-09-20 22:21:34.763 | MS1 | 121.4656690821 | 31.1446311967 | 302 | 504990 | -86.45 | 17.32 | 58.71 | 0.11 | 2.54 | 1573 |
| 2024-09-20 22:21:35.284 | MS1 | 121.4656752726 | 31.1446332186 | 302 | 504990 | -87.76 | 13.27 | 98.60 | 0.05 | 2.85 | 1575 |
| 2024-09-20 22:21:36.162 | MS1 | 121.4656770388 | 31.1446307829 | 302 | 504990 | -89.14 | 14.11 | 80.61 | 0.13 | 2.98 | 1567 |
| 2024-09-20 22:21:37.269 | MS1 | 121.4656720462 | 31.1446341202 | 302 | 504990 | -93.68 | 7.09 | 54.29 | 0.18 | 2.37 | 1577 |
| 2024-09-20 22:21:38.636 | MS1 | 121.4656654180 | 31.1446356196 | 302 | 504990 | -91.36 | 9.37 | 69.59 | 0.14 | 2.62 | 1596 |
| 2024-09-20 22:21:39.671 | MS1 | 121.4656672905 | 31.1446363564 | 302 | 504990 | -90.70 | 9.53 | 67.98 | 0.04 | 2.50 | 1579 |
| 2024-09-20 22:21:40.712 | MS1 | 121.4656637680 | 31.1446263205 | 302 | 504990 | -91.79 | 10.18 | 316.34 | 0.13 | 2.94 | 1584 |
| 2024-09-20 22:21:41.895 | MS1 | 121.4656667058 | 31.1446238524 | 302 | 504990 | -91.57 | 8.62 | 581.86 | 0.07 | 2.46 | 1561 |
| 2024-09-20 22:21:42.217 | MS1 | 121.4656665786 | 31.1446292755 | 302 | 504990 | -92.17 | 8.98 | 515.26 | 0.10 | 2.81 | 1590 |

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
| 3229745 | 2 | 121.4669005372 | 31.1479650173 | 283 | 3 | 12 | 22.1 | TDD | 667 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3234084 | 4 | 121.4713197344 | 31.1520155429 | 121 | 9 | 8 | 34.2 | TDD | 168 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3239542 | 3 | 121.4697427621 | 31.1452213936 | 273 | 10 | 4 | 43.2 | TDD | 302 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3246892 | 1 | 121.4674581376 | 31.1448261506 | 311 | 11 | 8 | 41.1 | TDD | 96 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.445 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.465 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.615 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.615 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.318 | NREventA3 | measId:2;ServCellPCI:627;Se... |
| 2024-09-20 22:21:38.558 | NRHandoverAttempt | SourcePCI:627;SourceNR-ARFC... |
| 2024-09-20 22:21:38.603 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.616 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.735 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.735 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3246892 | 1 | 81.9971 | 80.5755 | -115.3361 | 12.8889 | 186.5872 | 0.0058 | 0.0037 |
| 2024_09_19 22:00 | 3229745 | 2 | 81.1460 | 91.4405 | -114.7529 | 6.2142 | 82.9795 | 0.0081 | 0.0172 |
| 2024_09_19 22:00 | 3239542 | 3 | 79.0477 | 83.2661 | -116.7404 | 15.4900 | 131.4096 | 0.0109 | 0.0188 |
| 2024_09_19 22:00 | 3234084 | 4 | 81.8967 | 80.5537 | -115.8093 | 11.5439 | 81.0475 | 0.0170 | 0.0059 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412960_2EFF8642 | 504990 | 302 | -85.7 | 504990 | 667 | -91.9 | 504990 | 96 | -97.4 | 504990 | 168 |
| MR_1774412960_809B69E8 | 504990 | 302 | -85.9 | 504990 | 667 | -93.0 | 504990 | 96 | -97.8 | 504990 | 168 |
| MR_1774412960_999955B6 | 504990 | 302 | -87.4 | 504990 | 667 | -94.2 | 504990 | 96 | -97.6 | 504990 | 168 |
| MR_1774412960_034E2EE4 | 504990 | 302 | -84.6 | 504990 | 667 | -93.9 | 504990 | 96 | -96.7 | 504990 | 168 |
| MR_1774412960_64515581 | 504990 | 302 | -87.0 | 504990 | 667 | -95.5 | 504990 | 96 | -94.4 | 504990 | 168 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 132: `14d8e16e-79f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `14d8e16e-79f5-44ee-9974-45224a3f8b54` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Lift the tilt angle  of 3234509_1 by 6 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[132] topology](images/train_0132.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3215533_2
- `C2`: Increase transmission power for 3264417_3
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Lift the tilt angle  of 3234509_1 by 6 degrees **← 정답**
- `C5`: Decrease transmission power for 3215533_2
- `C6`: Decrease A3 Offset threshold for 3215533_2
- `C7`: Add neighbor relationship between 3215533_2 and 3264417_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215533_2
- `C9`: Check test server and transmission issues
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264417_3
- `C11`: Decrease A3 Offset threshold for 3264417_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264417_3
- `C13`: Add neighbor relationship between 3234509_1 and 3264417_3
- `C14`: Decrease transmission power for 3264417_3
- `C15`: Increase transmission power for 3215533_2
- `C16`: Increase A3 Offset threshold for 3264417_3
- `C17`: Adjust the azimuth of 3234509_1 by 50 degrees
- `C18`: Press down the tilt angle  of 3234509_1 by 6 degrees
- `C19`: Adjust the azimuth of 3215533_2 by 20 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215533_2
- `C21`: Lift the tilt angle of 3215533_2 by 4 degrees
- `C22`: Press down the tilt angle of 3215533_2 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.709 | MS1 | 121.4656748619 | 31.1446211747 | 629 | 504990 | -90.41 | 16.07 | 311.34 | 0.19 | 2.63 | 1561 |
| 2024-09-20 22:21:32.442 | MS1 | 121.4656617226 | 31.1446340916 | 629 | 504990 | -89.22 | 15.22 | 549.44 | 0.06 | 2.60 | 1598 |
| 2024-09-20 22:21:33.940 | MS1 | 121.4656773554 | 31.1446281344 | 629 | 504990 | -89.97 | 15.31 | 499.14 | 0.09 | 2.66 | 1595 |
| 2024-09-20 22:21:34.678 | MS1 | 121.4656656850 | 31.1446205965 | 629 | 504990 | -85.99 | 16.62 | 87.77 | 0.16 | 2.92 | 1576 |
| 2024-09-20 22:21:35.557 | MS1 | 121.4656756096 | 31.1446258603 | 629 | 504990 | -86.98 | 17.16 | 78.40 | 0.05 | 2.36 | 1600 |
| 2024-09-20 22:21:36.223 | MS1 | 121.4656685602 | 31.1446229553 | 629 | 504990 | -91.59 | 16.00 | 79.52 | 0.06 | 2.47 | 1591 |
| 2024-09-20 22:21:37.914 | MS1 | 121.4656746308 | 31.1446279575 | 629 | 504990 | -90.57 | 7.84 | 68.42 | 0.11 | 2.90 | 1599 |
| 2024-09-20 22:21:38.639 | MS1 | 121.4656705081 | 31.1446190554 | 629 | 504990 | -90.68 | 10.03 | 46.21 | 0.15 | 2.41 | 1590 |
| 2024-09-20 22:21:39.536 | MS1 | 121.4656715313 | 31.1446329108 | 629 | 504990 | -90.48 | 9.85 | 83.76 | 0.13 | 2.81 | 1573 |
| 2024-09-20 22:21:40.828 | MS1 | 121.4656740148 | 31.1446182862 | 629 | 504990 | -92.55 | 8.61 | 374.09 | 0.15 | 2.02 | 1592 |
| 2024-09-20 22:21:41.992 | MS1 | 121.4656715464 | 31.1446199220 | 629 | 504990 | -91.72 | 10.78 | 481.58 | 0.07 | 2.84 | 1567 |
| 2024-09-20 22:21:42.478 | MS1 | 121.4656770552 | 31.1446246229 | 629 | 504990 | -90.92 | 7.95 | 416.81 | 0.19 | 2.92 | 1561 |

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
| 3215533 | 2 | 121.4744296984 | 31.1538001626 | 199 | 3 | 8 | 28.1 | TDD | 629 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3234509 | 1 | 121.4656661165 | 31.1514300763 | 102 | 8 | 2 | 30.3 | TDD | 305 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3241582 | 4 | 121.4705577335 | 31.1484204169 | 179 | 9 | 0 | 49.6 | TDD | 645 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3264417 | 3 | 121.4666478884 | 31.1528499172 | 78 | 3 | 12 | 49.7 | TDD | 590 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.381 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.400 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.507 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.507 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.229 | NREventA3 | measId:2;ServCellPCI:705;Se... |
| 2024-09-20 22:21:38.469 | NRHandoverAttempt | SourcePCI:705;SourceNR-ARFC... |
| 2024-09-20 22:21:38.504 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.514 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.641 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.641 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234509 | 1 | 7.1986 | 19.5124 | -117.7678 | 11.1325 | 153.4071 | 0.0080 | 0.0012 |
| 2024_09_20 22:00 | 3215533 | 2 | 75.6732 | 88.3089 | -115.4183 | 18.4848 | 181.8804 | 0.0066 | 0.0080 |
| 2024_09_20 22:00 | 3264417 | 3 | 11.4638 | 19.8797 | -116.3446 | 17.6282 | 148.7193 | 0.0158 | 0.0175 |
| 2024_09_20 22:00 | 3241582 | 4 | 12.0260 | 15.9534 | -114.2802 | 15.1970 | 124.9011 | 0.0164 | 0.0198 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415069_561F457E | 504990 | 629 | -84.9 | 504990 | 590 | -93.0 | 504990 | 305 | -96.8 | 504990 | 645 |
| MR_1774415069_9DDF578C | 504990 | 629 | -87.5 | 504990 | 590 | -95.6 | 504990 | 305 | -96.3 | 504990 | 645 |
| MR_1774415069_451A9198 | 504990 | 629 | -85.6 | 504990 | 590 | -95.4 | 504990 | 305 | -99.4 | 504990 | 645 |
| MR_1774415069_AE4440AC | 504990 | 629 | -87.9 | 504990 | 590 | -93.6 | 504990 | 305 | -98.9 | 504990 | 645 |
| MR_1774415069_D6110471 | 504990 | 629 | -85.4 | 504990 | 590 | -96.3 | 504990 | 305 | -97.7 | 504990 | 645 |
| MR_1774415069_667531FC | 504990 | 629 | -87.4 | 504990 | 590 | -93.9 | 504990 | 305 | -97.6 | 504990 | 645 |
| MR_1774415069_8BC45DCF | 504990 | 629 | -85.1 | 504990 | 590 | -95.3 | 504990 | 305 | -98.2 | 504990 | 645 |
| MR_1774415069_F305B058 | 504990 | 629 | -84.2 | 504990 | 590 | -95.7 | 504990 | 305 | -96.2 | 504990 | 645 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 133: `34b6af83-1e7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `34b6af83-1e75-4959-ace9-8630c7456306` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230901_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[133] topology](images/train_0133.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3230901_1 by 3 degrees
- `C2`: Decrease A3 Offset threshold for 3230901_1
- `C3`: Increase A3 Offset threshold for 3219263_6
- `C4`: Decrease transmission power for 3230901_1
- `C5`: Lift the tilt angle of 3230901_1 by 3 degrees
- `C6`: Add neighbor relationship between 3230901_1 and 3219263_6
- `C7`: Increase A3 Offset threshold for 3230901_1
- `C8`: Increase transmission power for 3230901_1
- `C9`: Lift the tilt angle  of 3219263_6 by 4 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230901_1 **← 정답**
- `C11`: Adjust the azimuth of 3219263_6 by 23 degrees
- `C12`: Press down the tilt angle  of 3219263_6 by 4 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219263_6
- `C14`: Add neighbor relationship between 3272681_13 and 3219263_6
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219263_6
- `C16`: Decrease transmission power for 3219263_6
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase transmission power for 3219263_6
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230901_1
- `C20`: Decrease A3 Offset threshold for 3219263_6
- `C21`: Check test server and transmission issues
- `C22`: Adjust the azimuth of 3230901_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.130 | MS1 | 121.4656696712 | 31.1446201510 | 899 | 504990 | -94.92 | 11.03 | 356.21 | 0.04 | 2.02 | 1600 |
| 2024-09-20 22:21:32.457 | MS1 | 121.4656699173 | 31.1446208417 | 441 | 504990 | -94.91 | 10.64 | 501.18 | 0.19 | 2.26 | 1571 |
| 2024-09-20 22:21:33.710 | MS1 | 121.4656621620 | 31.1446302732 | 112 | 504990 | -94.72 | 12.91 | 340.52 | 0.02 | 2.74 | 1576 |
| 2024-09-20 22:21:34.781 | MS1 | 121.4656665696 | 31.1446262290 | 442 | 152650 | -87.65 | 6.87 | 100.53 | 0.16 | 1.90 | 911 |
| 2024-09-20 22:21:35.610 | MS1 | 121.4656724680 | 31.1446285302 | 358 | 152650 | -93.34 | 5.80 | 68.27 | 0.08 | 1.96 | 985 |
| 2024-09-20 22:21:36.339 | MS1 | 121.4656726919 | 31.1446238453 | 604 | 152650 | -87.09 | 2.06 | 55.25 | 0.09 | 1.80 | 924 |
| 2024-09-20 22:21:37.553 | MS1 | 121.4656760014 | 31.1446283024 | 32 | 152650 | -87.49 | 2.93 | 103.97 | 0.10 | 1.98 | 953 |
| 2024-09-20 22:21:38.364 | MS1 | 121.4656583206 | 31.1446375774 | 442 | 152650 | -94.45 | 4.38 | 50.34 | 0.07 | 1.72 | 922 |
| 2024-09-20 22:21:39.207 | MS1 | 121.4656693567 | 31.1446299179 | 358 | 152650 | -93.96 | 4.57 | 67.58 | 0.18 | 1.88 | 961 |
| 2024-09-20 22:21:40.120 | MS1 | 121.4656645235 | 31.1446196088 | 604 | 152650 | -88.33 | 5.14 | 77.60 | 0.06 | 2.02 | 1566 |
| 2024-09-20 22:21:41.281 | MS1 | 121.4656633919 | 31.1446246614 | 32 | 152650 | -89.08 | 4.66 | 85.98 | 0.14 | 2.72 | 1563 |
| 2024-09-20 22:21:42.833 | MS1 | 121.4656757829 | 31.1446275892 | 442 | 152650 | -91.82 | 5.63 | 49.07 | 0.02 | 2.79 | 1562 |

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
| 3215309 | 7 | 121.4752367561 | 31.1479455807 | 294 | 7 | 4 | 29.8 | FDD | 32 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3219263 | 6 | 121.4756896962 | 31.1494594104 | 264 | 3 | 5 | 19.1 | TDD | 251 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3223023 | 8 | 121.4747635662 | 31.1504248848 | 37 | 15 | 8 | 8.2 | FDD | 674 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3223764 | 5 | 121.4641651136 | 31.1531948968 | 154 | 14 | 3 | 22.8 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3224139 | 2 | 121.4707054807 | 31.1533260218 | 273 | 13 | 10 | 11.2 | TDD | 559 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3230901 | 1 | 121.4739899176 | 31.1551109034 | 264 | 3 | 7 | 3.5 | TDD | 899 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3233826 | 3 | 121.4673000454 | 31.1528743065 | 54 | 9 | 10 | 27.8 | TDD | 112 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3243716 | 11 | 121.4689278042 | 31.1515074715 | 335 | 15 | 6 | 20.3 | FDD | 16 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3261722 | 10 | 121.4663963924 | 31.1516141308 | 147 | 13 | 11 | 29.4 | FDD | 231 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3268007 | 9 | 121.4733960728 | 31.1452013992 | 158 | 6 | 6 | 27.6 | FDD | 358 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3272681 | 13 | 121.4690414645 | 31.1491706274 | 127 | 15 | 9 | 4.5 | FDD | 604 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3274659 | 12 | 121.4663646296 | 31.1546387207 | 96 | 14 | 9 | 3.8 | FDD | 442 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3277738 | 4 | 121.4741602731 | 31.1497138837 | 117 | 15 | 9 | 6.6 | TDD | 984 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.964 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.980 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.119 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.119 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.807 | NREventA2 | measId:1;ServCellPCI:482;Se... |
| 2024-09-20 22:21:34.934 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.189 | NREventA5 | measId:3;ServCellPCI:482;Se... |
| 2024-09-20 22:21:35.220 | NRHandoverAttempt | SourcePCI:482;SourceNR-ARFC... |
| 2024-09-20 22:21:35.255 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.265 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.401 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.401 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230901 | 1 | 17.9701 | 10.0264 | -114.5138 | 12.8443 | 159.6600 | 0.0002 | 0.0172 |
| 2024_09_20 22:00 | 3224139 | 2 | 6.6438 | 19.9045 | -114.5208 | 13.2939 | 163.6055 | 0.0070 | 0.0088 |
| 2024_09_20 22:00 | 3233826 | 3 | 9.4604 | 5.1772 | -117.2426 | 15.1746 | 108.2195 | 0.0196 | 0.0077 |
| 2024_09_20 22:00 | 3277738 | 4 | 15.7607 | 18.2582 | -117.6916 | 11.2706 | 93.1271 | 0.0122 | 0.0044 |
| 2024_09_20 22:00 | 3223764 | 5 | 8.8146 | 8.9945 | -114.6421 | 8.9467 | 142.1158 | 0.0010 | 0.0044 |
| 2024_09_20 22:00 | 3219263 | 6 | 13.9502 | 15.7611 | -117.9881 | 8.3524 | 118.7542 | 0.0148 | 0.0107 |
| 2024_09_20 22:00 | 3215309 | 7 | 19.1613 | 10.7532 | -115.1571 | 3.5737 | 52.8261 | 0.0055 | 0.0032 |
| 2024_09_20 22:00 | 3223023 | 8 | 6.2280 | 12.8792 | -116.3909 | 3.5261 | 55.6180 | 0.0052 | 0.0130 |
| 2024_09_20 22:00 | 3268007 | 9 | 16.3668 | 18.4812 | -114.5642 | 4.0574 | 57.4635 | 0.0191 | 0.0031 |
| 2024_09_20 22:00 | 3261722 | 10 | 16.1509 | 7.0308 | -114.8382 | 3.9631 | 27.4305 | 0.0071 | 0.0014 |
| 2024_09_20 22:00 | 3243716 | 11 | 9.1531 | 13.0681 | -116.8303 | 4.5018 | 51.8701 | 0.0043 | 0.0168 |
| 2024_09_20 22:00 | 3274659 | 12 | 7.7260 | 14.9056 | -116.9240 | 4.3218 | 33.1326 | 0.0143 | 0.0198 |
| 2024_09_20 22:00 | 3272681 | 13 | 6.2912 | 18.0192 | -114.6544 | 4.8966 | 51.2899 | 0.0148 | 0.0129 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415678_4F617546 | 504990 | 112 | -93.3 | 504990 | 251 | -93.8 | 504990 | 984 | -93.5 | 504990 | 559 |
| MR_1774415678_28B2F833 | 504990 | 112 | -96.3 | 504990 | 251 | -93.5 | 504990 | 984 | -94.7 | 504990 | 559 |
| MR_1774415678_6EAD5344 | 152650 | 358 | -93.3 | 152650 | 16 | -97.5 | 152650 | 674 | -103.7 | 152650 | 231 |
| MR_1774415678_654DA06D | 504990 | 112 | -93.8 | 504990 | 251 | -92.9 | 504990 | 984 | -93.7 | 504990 | 559 |
| MR_1774415678_A0845D26 | 504990 | 112 | -96.4 | 504990 | 251 | -95.8 | 504990 | 984 | -95.7 | 504990 | 559 |
| MR_1774415678_146E6F1B | 152650 | 358 | -92.1 | 152650 | 16 | -96.8 | 152650 | 674 | -103.8 | 152650 | 231 |
| MR_1774415678_1087C0D5 | 152650 | 358 | -92.0 | 152650 | 16 | -96.7 | 152650 | 674 | -102.7 | 152650 | 231 |
| MR_1774415678_1FFE4538 | 152650 | 358 | -94.9 | 152650 | 16 | -99.3 | 152650 | 674 | -101.1 | 152650 | 231 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 134: `d590a22a-a3b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d590a22a-a3b5-4407-b1a2-525d5733755a` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3247715_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[134] topology](images/train_0134.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247715_3 **← 정답**
- `C2`: Increase transmission power for 3238407_4
- `C3`: Press down the tilt angle  of 3238407_4 by 10 degrees
- `C4`: Lift the tilt angle of 3247715_3 by 2 degrees
- `C5`: Increase A3 Offset threshold for 3247715_3
- `C6`: Decrease A3 Offset threshold for 3247715_3
- `C7`: Check test server and transmission issues
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease transmission power for 3238407_4
- `C10`: Increase A3 Offset threshold for 3238407_4
- `C11`: Add neighbor relationship between 3211894_2 and 3238407_4
- `C12`: Decrease transmission power for 3247715_3
- `C13`: Adjust the azimuth of 3238407_4 by 50 degrees
- `C14`: Lift the tilt angle  of 3238407_4 by 10 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238407_4
- `C16`: Increase transmission power for 3247715_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238407_4
- `C18`: Add neighbor relationship between 3247715_3 and 3238407_4
- `C19`: Adjust the azimuth of 3247715_3 by 6 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247715_3
- `C21`: Decrease A3 Offset threshold for 3238407_4
- `C22`: Press down the tilt angle of 3247715_3 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.552 | MS1 | 121.4656761398 | 31.1446270347 | 787 | 504990 | -90.47 | 13.66 | 475.45 | 0.19 | 2.91 | 1587 |
| 2024-09-20 22:21:32.760 | MS1 | 121.4656632774 | 31.1446367750 | 787 | 504990 | -89.82 | 13.90 | 451.60 | 0.18 | 2.64 | 1575 |
| 2024-09-20 22:21:33.192 | MS1 | 121.4656721798 | 31.1446339845 | 787 | 504990 | -89.34 | 16.15 | 506.20 | 0.00 | 2.75 | 1574 |
| 2024-09-20 22:21:34.181 | MS1 | 121.4656591719 | 31.1446214860 | 787 | 504990 | -89.82 | 14.71 | 43.93 | 0.53 | 2.92 | 517 |
| 2024-09-20 22:21:35.880 | MS1 | 121.4656739078 | 31.1446213800 | 787 | 504990 | -90.15 | 12.21 | 87.18 | 0.59 | 2.51 | 502 |
| 2024-09-20 22:21:36.473 | MS1 | 121.4656771259 | 31.1446229796 | 787 | 504990 | -89.63 | 13.04 | 79.95 | 0.60 | 2.03 | 592 |
| 2024-09-20 22:21:37.220 | MS1 | 121.4656695064 | 31.1446351891 | 787 | 504990 | -91.76 | 12.08 | 63.84 | 0.51 | 2.59 | 637 |
| 2024-09-20 22:21:38.723 | MS1 | 121.4656643448 | 31.1446365868 | 787 | 504990 | -89.47 | 7.80 | 79.99 | 0.54 | 2.98 | 630 |
| 2024-09-20 22:21:39.922 | MS1 | 121.4656618421 | 31.1446355351 | 787 | 504990 | -92.17 | 12.15 | 63.42 | 0.53 | 2.17 | 511 |
| 2024-09-20 22:21:40.981 | MS1 | 121.4656649044 | 31.1446304461 | 787 | 504990 | -92.74 | 8.23 | 365.64 | 0.00 | 2.32 | 1596 |
| 2024-09-20 22:21:41.858 | MS1 | 121.4656667028 | 31.1446305859 | 787 | 504990 | -92.15 | 10.56 | 544.92 | 0.11 | 2.81 | 1592 |
| 2024-09-20 22:21:42.583 | MS1 | 121.4656684084 | 31.1446374009 | 787 | 504990 | -90.99 | 7.38 | 473.75 | 0.01 | 2.56 | 1585 |

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
| 3211894 | 2 | 121.4726167422 | 31.1523542710 | 95 | 12 | 11 | 46.3 | TDD | 394 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3216756 | 1 | 121.4736983945 | 31.1532062059 | 196 | 9 | 5 | 23.3 | TDD | 865 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3238407 | 4 | 121.4644144945 | 31.1502557325 | 10 | 11 | 9 | 31.4 | TDD | 662 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3247715 | 3 | 121.4745108748 | 31.1515038344 | 234 | 1 | 0 | 17.7 | TDD | 787 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.131 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.146 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.283 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.283 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.952 | NREventA3 | measId:2;ServCellPCI:498;Se... |
| 2024-09-20 22:21:38.192 | NRHandoverAttempt | SourcePCI:498;SourceNR-ARFC... |
| 2024-09-20 22:21:38.232 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.247 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.348 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.348 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216756 | 1 | 16.4410 | 11.5564 | -116.5138 | 5.4530 | 141.4758 | 0.0129 | 0.0168 |
| 2024_09_20 22:00 | 3211894 | 2 | 11.7895 | 9.4834 | -116.6956 | 13.8372 | 193.5596 | 0.0104 | 0.0058 |
| 2024_09_20 22:00 | 3247715 | 3 | 17.7353 | 9.3625 | -115.8344 | 6.1775 | 86.3460 | 0.0003 | 0.0049 |
| 2024_09_20 22:00 | 3238407 | 4 | 5.7614 | 9.4347 | -114.0378 | 10.7142 | 167.8447 | 0.0105 | 0.0042 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414511_41BF4D08 | 504990 | 787 | -90.1 | 504990 | 662 | -94.9 | 504990 | 394 | -104.3 | 504990 | 865 |
| MR_1774414511_C5F444A5 | 504990 | 787 | -90.0 | 504990 | 662 | -96.4 | 504990 | 394 | -102.4 | 504990 | 865 |
| MR_1774414511_72734481 | 504990 | 787 | -91.4 | 504990 | 662 | -94.1 | 504990 | 394 | -101.8 | 504990 | 865 |
| MR_1774414511_C0E7B871 | 504990 | 787 | -88.8 | 504990 | 662 | -94.4 | 504990 | 394 | -104.1 | 504990 | 865 |
| MR_1774414511_A3A6AE5E | 504990 | 787 | -90.2 | 504990 | 662 | -94.7 | 504990 | 394 | -101.5 | 504990 | 865 |
| MR_1774414511_A8F8075F | 504990 | 787 | -91.4 | 504990 | 662 | -94.6 | 504990 | 394 | -101.1 | 504990 | 865 |
| MR_1774414511_F17B4BE1 | 504990 | 787 | -87.8 | 504990 | 662 | -96.0 | 504990 | 394 | -101.8 | 504990 | 865 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 135: `4d60edd6-b73...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4d60edd6-b73e-4a39-bf18-0112791e97bf` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3278831_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[135] topology](images/train_0135.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3278831_2
- `C2`: Decrease transmission power for 3241504_1
- `C3`: Adjust the azimuth of 3278831_2 by 29 degrees
- `C4`: Decrease A3 Offset threshold for 3241504_1
- `C5`: Adjust the azimuth of 3241504_1 by 50 degrees
- `C6`: Add neighbor relationship between 3230127_4 and 3241504_1
- `C7`: Press down the tilt angle of 3278831_2 by 5 degrees
- `C8`: Lift the tilt angle of 3278831_2 by 5 degrees
- `C9`: Decrease A3 Offset threshold for 3278831_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241504_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241504_1
- `C12`: Press down the tilt angle  of 3241504_1 by 1 degrees
- `C13`: Check test server and transmission issues
- `C14`: Increase A3 Offset threshold for 3241504_1
- `C15`: Lift the tilt angle  of 3241504_1 by 1 degrees
- `C16`: Increase A3 Offset threshold for 3278831_2
- `C17`: Increase transmission power for 3241504_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Add neighbor relationship between 3278831_2 and 3241504_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278831_2
- `C21`: Decrease transmission power for 3278831_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278831_2 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.990 | MS1 | 121.4656614100 | 31.1446354768 | 154 | 504990 | -87.03 | 15.76 | 313.39 | 0.04 | 2.90 | 1592 |
| 2024-09-20 22:21:32.741 | MS1 | 121.4656733004 | 31.1446349135 | 154 | 504990 | -86.91 | 14.28 | 547.07 | 0.12 | 2.06 | 1600 |
| 2024-09-20 22:21:33.640 | MS1 | 121.4656621079 | 31.1446218131 | 154 | 504990 | -89.97 | 12.78 | 361.78 | 0.18 | 2.02 | 1600 |
| 2024-09-20 22:21:34.947 | MS1 | 121.4656775447 | 31.1446336326 | 154 | 504990 | -91.66 | 14.96 | 69.66 | 0.53 | 2.13 | 526 |
| 2024-09-20 22:21:35.276 | MS1 | 121.4656596556 | 31.1446279386 | 154 | 504990 | -90.68 | 13.12 | 49.79 | 0.67 | 2.50 | 607 |
| 2024-09-20 22:21:36.940 | MS1 | 121.4656611836 | 31.1446322988 | 154 | 504990 | -86.17 | 15.05 | 91.68 | 0.57 | 2.10 | 557 |
| 2024-09-20 22:21:37.461 | MS1 | 121.4656745686 | 31.1446198926 | 154 | 504990 | -90.88 | 11.58 | 95.61 | 0.58 | 2.68 | 677 |
| 2024-09-20 22:21:38.182 | MS1 | 121.4656644957 | 31.1446195312 | 154 | 504990 | -89.14 | 11.62 | 71.89 | 0.59 | 2.94 | 679 |
| 2024-09-20 22:21:39.998 | MS1 | 121.4656635141 | 31.1446369753 | 154 | 504990 | -90.16 | 12.09 | 57.63 | 0.55 | 2.21 | 547 |
| 2024-09-20 22:21:40.814 | MS1 | 121.4656673801 | 31.1446341472 | 154 | 504990 | -89.99 | 9.44 | 591.52 | 0.08 | 2.55 | 1562 |
| 2024-09-20 22:21:41.927 | MS1 | 121.4656752880 | 31.1446351832 | 154 | 504990 | -91.69 | 10.70 | 526.21 | 0.17 | 2.68 | 1579 |
| 2024-09-20 22:21:42.976 | MS1 | 121.4656772185 | 31.1446238760 | 154 | 504990 | -89.20 | 8.74 | 542.85 | 0.19 | 2.53 | 1578 |

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
| 3230127 | 4 | 121.4720215528 | 31.1557584700 | 180 | 12 | 1 | 41.1 | TDD | 305 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3241504 | 1 | 121.4745154924 | 31.1483274988 | 313 | 0 | 7 | 15.5 | TDD | 737 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3264722 | 3 | 121.4697305610 | 31.1496515404 | 29 | 1 | 4 | 36.9 | TDD | 586 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3278831 | 2 | 121.4654958763 | 31.1520905610 | 150 | 3 | 4 | 28.4 | TDD | 154 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.417 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.432 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.564 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.564 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.296 | NREventA3 | measId:2;ServCellPCI:671;Se... |
| 2024-09-20 22:21:38.536 | NRHandoverAttempt | SourcePCI:671;SourceNR-ARFC... |
| 2024-09-20 22:21:38.586 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.597 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.704 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.704 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241504 | 1 | 14.9038 | 9.8877 | -114.7566 | 13.1253 | 115.6772 | 0.0009 | 0.0155 |
| 2024_09_20 22:00 | 3278831 | 2 | 5.8471 | 18.8495 | -116.7346 | 15.0507 | 97.1170 | 0.0123 | 0.0182 |
| 2024_09_20 22:00 | 3264722 | 3 | 14.9862 | 17.8245 | -114.7177 | 6.4551 | 162.3848 | 0.0134 | 0.0110 |
| 2024_09_20 22:00 | 3230127 | 4 | 6.0828 | 16.9488 | -114.2255 | 10.2959 | 83.3532 | 0.0074 | 0.0052 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415698_65541004 | 504990 | 154 | -90.9 | 504990 | 737 | -99.0 | 504990 | 305 | -100.5 | 504990 | 586 |
| MR_1774415698_FCB15546 | 504990 | 154 | -93.1 | 504990 | 737 | -97.4 | 504990 | 305 | -102.9 | 504990 | 586 |
| MR_1774415698_DB6F31A6 | 504990 | 154 | -90.8 | 504990 | 737 | -97.5 | 504990 | 305 | -101.3 | 504990 | 586 |
| MR_1774415698_12F3675C | 504990 | 154 | -91.5 | 504990 | 737 | -98.5 | 504990 | 305 | -101.5 | 504990 | 586 |
| MR_1774415698_7A9B98D1 | 504990 | 154 | -90.4 | 504990 | 737 | -97.5 | 504990 | 305 | -100.9 | 504990 | 586 |
| MR_1774415698_CBD85BF9 | 504990 | 154 | -90.7 | 504990 | 737 | -95.9 | 504990 | 305 | -103.1 | 504990 | 586 |
| MR_1774415698_B2FF2EA9 | 504990 | 154 | -92.1 | 504990 | 737 | -95.5 | 504990 | 305 | -99.5 | 504990 | 586 |
| MR_1774415698_AAD712F7 | 504990 | 154 | -92.2 | 504990 | 737 | -98.7 | 504990 | 305 | -100.1 | 504990 | 586 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 136: `9677f010-52f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9677f010-52fc-49d3-9573-963d36e6ecd1` |
| Tag | **multiple-answer** |
| 정답 | **C10|C18** |
| C10 의미 | Adjust the azimuth of 3279005_4 by 29 degrees |
| C18 의미 | Increase transmission power for 3279005_4 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[136] topology](images/train_0136.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3279005_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240731_1
- `C3`: Check test server and transmission issues
- `C4`: Increase A3 Offset threshold for 3240731_1
- `C5`: Decrease A3 Offset threshold for 3279005_4
- `C6`: Increase A3 Offset threshold for 3279005_4
- `C7`: Decrease A3 Offset threshold for 3240731_1
- `C8`: Lift the tilt angle  of 3240731_1 by 5 degrees
- `C9`: Decrease transmission power for 3240731_1
- `C10`: Adjust the azimuth of 3279005_4 by 29 degrees **← 정답**
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Add neighbor relationship between 3223312_2 and 3240731_1
- `C13`: Press down the tilt angle of 3279005_4 by 10 degrees
- `C14`: Lift the tilt angle of 3279005_4 by 10 degrees
- `C15`: Increase transmission power for 3240731_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279005_4
- `C17`: Add neighbor relationship between 3279005_4 and 3240731_1
- `C18`: Increase transmission power for 3279005_4 **← 정답**
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279005_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240731_1
- `C21`: Press down the tilt angle  of 3240731_1 by 5 degrees
- `C22`: Adjust the azimuth of 3240731_1 by 18 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.459 | MS1 | 121.4656763204 | 31.1446368783 | 863 | 504990 | -87.74 | 13.21 | 312.96 | 0.16 | 2.01 | 1581 |
| 2024-09-20 22:21:32.764 | MS1 | 121.4656701456 | 31.1446193602 | 863 | 504990 | -93.45 | 15.63 | 337.22 | 0.18 | 2.69 | 1580 |
| 2024-09-20 22:21:33.484 | MS1 | 121.4656652198 | 31.1446184660 | 863 | 504990 | -88.21 | 17.92 | 417.90 | 0.09 | 2.88 | 1590 |
| 2024-09-20 22:21:34.914 | MS1 | 121.4656681528 | 31.1446190320 | 863 | 504990 | -102.02 | -0.62 | 33.41 | 0.04 | 1.03 | 1579 |
| 2024-09-20 22:21:35.790 | MS1 | 121.4656758579 | 31.1446302288 | 863 | 504990 | -101.58 | -0.46 | 31.47 | 0.04 | 1.44 | 1598 |
| 2024-09-20 22:21:36.932 | MS1 | 121.4656748594 | 31.1446310735 | 863 | 504990 | -106.16 | -0.32 | 20.12 | 0.11 | 1.31 | 1584 |
| 2024-09-20 22:21:37.643 | MS1 | 121.4656631996 | 31.1446257511 | 863 | 504990 | -100.11 | -1.35 | 45.13 | 0.20 | 1.42 | 1565 |
| 2024-09-20 22:21:38.371 | MS1 | 121.4656774704 | 31.1446188202 | 863 | 504990 | -101.28 | 1.99 | 75.85 | 0.20 | 1.26 | 1598 |
| 2024-09-20 22:21:39.555 | MS1 | 121.4656639110 | 31.1446319476 | 863 | 504990 | -100.84 | -0.61 | 79.45 | 0.04 | 1.16 | 1582 |
| 2024-09-20 22:21:40.146 | MS1 | 121.4656695668 | 31.1446291847 | 863 | 504990 | -94.68 | 17.68 | 313.28 | 0.00 | 2.56 | 1564 |
| 2024-09-20 22:21:41.590 | MS1 | 121.4656688553 | 31.1446255426 | 863 | 504990 | -93.56 | 12.75 | 355.22 | 0.16 | 2.91 | 1592 |
| 2024-09-20 22:21:42.803 | MS1 | 121.4656773751 | 31.1446350076 | 863 | 504990 | -87.36 | 16.31 | 374.11 | 0.07 | 2.30 | 1575 |

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
| 3223312 | 2 | 121.4724992841 | 31.1488222886 | 226 | 10 | 2 | 41.9 | TDD | 794 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3240731 | 1 | 121.4640961012 | 31.1537645680 | 190 | 3 | 0 | 42.0 | TDD | 368 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3265236 | 3 | 121.4744763236 | 31.1450293288 | 256 | 1 | 12 | 41.3 | TDD | 634 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3279005 | 4 | 121.4730969396 | 31.1454330596 | 234 | 15 | 3 | 41.5 | TDD | 863 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.283 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.305 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.424 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.424 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.657 | NREventA2 | measId:1;ServCellPCI:626;Se... |
| 2024-09-20 22:21:34.790 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240731 | 1 | 7.8147 | 15.4971 | -117.4455 | 15.6710 | 195.7966 | 0.0026 | 0.0028 |
| 2024_09_20 22:00 | 3223312 | 2 | 13.5643 | 9.2634 | -115.6060 | 14.2708 | 95.0709 | 0.0135 | 0.0042 |
| 2024_09_20 22:00 | 3265236 | 3 | 15.5236 | 19.6321 | -116.4692 | 9.3992 | 87.8318 | 0.0132 | 0.0126 |
| 2024_09_20 22:00 | 3279005 | 4 | 12.8613 | 15.7688 | -116.3422 | 10.1864 | 107.2407 | 0.1824 | 0.0011 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416019_99E14738 | 504990 | 863 | -102.0 | 504990 | 368 | -104.4 | 504990 | 794 | -112.8 | 504990 | 634 |
| MR_1774416019_A5C3C916 | 504990 | 863 | -101.0 | 504990 | 368 | -105.5 | 504990 | 794 | -109.8 | 504990 | 634 |
| MR_1774416019_7EBB9704 | 504990 | 863 | -100.4 | 504990 | 368 | -105.8 | 504990 | 794 | -109.6 | 504990 | 634 |
| MR_1774416019_E80C7A01 | 504990 | 863 | -101.9 | 504990 | 368 | -106.1 | 504990 | 794 | -109.3 | 504990 | 634 |
| MR_1774416019_ED81E431 | 504990 | 863 | -103.7 | 504990 | 368 | -103.8 | 504990 | 794 | -109.7 | 504990 | 634 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 137: `c099aacc-732...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c099aacc-7328-4101-bcce-beb711905190` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3275089_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[137] topology](images/train_0137.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3275089_4 by 5 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262931_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275089_4
- `C4`: Increase transmission power for 3262931_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Adjust the azimuth of 3275089_4 by 4 degrees
- `C7`: Lift the tilt angle  of 3262931_1 by 2 degrees
- `C8`: Adjust the azimuth of 3262931_1 by 50 degrees
- `C9`: Decrease transmission power for 3262931_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275089_4 **← 정답**
- `C11`: Increase A3 Offset threshold for 3262931_1
- `C12`: Decrease A3 Offset threshold for 3275089_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262931_1
- `C14`: Increase transmission power for 3275089_4
- `C15`: Increase A3 Offset threshold for 3275089_4
- `C16`: Decrease transmission power for 3275089_4
- `C17`: Lift the tilt angle of 3275089_4 by 5 degrees
- `C18`: Check test server and transmission issues
- `C19`: Add neighbor relationship between 3275089_4 and 3262931_1
- `C20`: Add neighbor relationship between 3257498_3 and 3262931_1
- `C21`: Press down the tilt angle  of 3262931_1 by 2 degrees
- `C22`: Decrease A3 Offset threshold for 3262931_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.267 | MS1 | 121.4656771912 | 31.1446320819 | 774 | 504990 | -85.40 | 17.69 | 315.20 | 0.07 | 2.06 | 1584 |
| 2024-09-20 22:21:32.568 | MS1 | 121.4656676078 | 31.1446330829 | 774 | 504990 | -85.75 | 14.93 | 386.08 | 0.06 | 2.78 | 1583 |
| 2024-09-20 22:21:33.733 | MS1 | 121.4656779822 | 31.1446186346 | 774 | 504990 | -89.39 | 17.73 | 505.10 | 0.00 | 2.26 | 1590 |
| 2024-09-20 22:21:34.478 | MS1 | 121.4656708501 | 31.1446259006 | 774 | 504990 | -85.67 | 17.12 | 49.12 | 0.63 | 2.55 | 575 |
| 2024-09-20 22:21:35.964 | MS1 | 121.4656730509 | 31.1446186599 | 774 | 504990 | -85.07 | 12.63 | 46.06 | 0.62 | 2.72 | 545 |
| 2024-09-20 22:21:36.250 | MS1 | 121.4656650923 | 31.1446229317 | 774 | 504990 | -85.27 | 16.28 | 77.46 | 0.62 | 2.72 | 689 |
| 2024-09-20 22:21:37.245 | MS1 | 121.4656767482 | 31.1446291205 | 774 | 504990 | -91.66 | 8.77 | 57.48 | 0.69 | 2.58 | 644 |
| 2024-09-20 22:21:38.229 | MS1 | 121.4656744869 | 31.1446288585 | 774 | 504990 | -90.75 | 10.34 | 98.79 | 0.53 | 2.71 | 696 |
| 2024-09-20 22:21:39.212 | MS1 | 121.4656596431 | 31.1446253764 | 774 | 504990 | -90.87 | 11.66 | 58.59 | 0.60 | 2.02 | 612 |
| 2024-09-20 22:21:40.229 | MS1 | 121.4656666910 | 31.1446253236 | 774 | 504990 | -93.85 | 8.35 | 505.84 | 0.07 | 2.22 | 1592 |
| 2024-09-20 22:21:41.376 | MS1 | 121.4656698357 | 31.1446186585 | 774 | 504990 | -89.93 | 7.21 | 379.68 | 0.06 | 2.54 | 1578 |
| 2024-09-20 22:21:42.802 | MS1 | 121.4656700508 | 31.1446313619 | 774 | 504990 | -89.15 | 7.65 | 315.00 | 0.07 | 2.93 | 1590 |

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
| 3255707 | 2 | 121.4676300250 | 31.1467534203 | 254 | 1 | 2 | 39.5 | TDD | 210 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3257498 | 3 | 121.4674069199 | 31.1548883537 | 137 | 13 | 12 | 37.4 | TDD | 811 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3262931 | 1 | 121.4699596493 | 31.1555078130 | 307 | 1 | 6 | 31.0 | TDD | 473 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3275089 | 4 | 121.4642796008 | 31.1511543948 | 174 | 3 | 0 | 27.7 | TDD | 774 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.673 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.673 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.391 | NREventA3 | measId:2;ServCellPCI:128;Se... |
| 2024-09-20 22:21:38.631 | NRHandoverAttempt | SourcePCI:128;SourceNR-ARFC... |
| 2024-09-20 22:21:38.674 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.689 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.820 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.820 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262931 | 1 | 12.0147 | 7.6944 | -117.1429 | 11.7598 | 155.4908 | 0.0082 | 0.0091 |
| 2024_09_20 22:00 | 3255707 | 2 | 17.7277 | 15.3453 | -114.1895 | 15.3662 | 152.7787 | 0.0077 | 0.0075 |
| 2024_09_20 22:00 | 3257498 | 3 | 8.7605 | 8.7603 | -114.3980 | 7.9158 | 179.1089 | 0.0191 | 0.0079 |
| 2024_09_20 22:00 | 3275089 | 4 | 14.5376 | 12.5301 | -114.9435 | 17.5930 | 192.0552 | 0.0092 | 0.0051 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414850_6E098E3C | 504990 | 774 | -87.6 | 504990 | 473 | -93.6 | 504990 | 811 | -95.7 | 504990 | 210 |
| MR_1774414850_B504C9C7 | 504990 | 774 | -86.7 | 504990 | 473 | -94.0 | 504990 | 811 | -94.0 | 504990 | 210 |
| MR_1774414850_800498FB | 504990 | 774 | -83.7 | 504990 | 473 | -91.1 | 504990 | 811 | -95.7 | 504990 | 210 |
| MR_1774414850_5CE3A5F5 | 504990 | 774 | -86.2 | 504990 | 473 | -92.6 | 504990 | 811 | -93.2 | 504990 | 210 |
| MR_1774414850_E6C8AB14 | 504990 | 774 | -86.5 | 504990 | 473 | -90.5 | 504990 | 811 | -93.1 | 504990 | 210 |
| MR_1774414850_7AC9CC48 | 504990 | 774 | -84.9 | 504990 | 473 | -91.0 | 504990 | 811 | -93.9 | 504990 | 210 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 138: `4ad88a7d-acb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4ad88a7d-acb2-4cc0-bd46-650731073814` |
| Tag | **multiple-answer** |
| 정답 | **C3|C10|C12|C15** |
| C3 의미 | Decrease transmission power for 3262839_2 |
| C10 의미 | Press down the tilt angle  of 3262839_2 by 2 degrees |
| C12 의미 | Increase A3 Offset threshold for 3212434_5 |
| C15 의미 | Increase A3 Offset threshold for 3262839_2 |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[138] topology](images/train_0138.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3212434_5
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262839_2
- `C3`: Decrease transmission power for 3262839_2 **← 정답**
- `C4`: Adjust the azimuth of 3262839_2 by 26 degrees
- `C5`: Add neighbor relationship between 3212434_5 and 3262839_2
- `C6`: Decrease A3 Offset threshold for 3212434_5
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212434_5
- `C8`: Press down the tilt angle of 3212434_5 by 6 degrees
- `C9`: Add neighbor relationship between 3262219_1 and 3262839_2
- `C10`: Press down the tilt angle  of 3262839_2 by 2 degrees **← 정답**
- `C11`: Lift the tilt angle of 3212434_5 by 6 degrees
- `C12`: Increase A3 Offset threshold for 3212434_5 **← 정답**
- `C13`: Adjust the azimuth of 3212434_5 by 4 degrees
- `C14`: Check test server and transmission issues
- `C15`: Increase A3 Offset threshold for 3262839_2 **← 정답**
- `C16`: Increase transmission power for 3262839_2
- `C17`: Decrease A3 Offset threshold for 3262839_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262839_2
- `C19`: Lift the tilt angle  of 3262839_2 by 2 degrees
- `C20`: Increase transmission power for 3212434_5
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212434_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.952 | MS1 | 121.4656687129 | 31.1446316985 | 991 | 504990 | -78.03 | 16.11 | 505.54 | 0.12 | 2.47 | 1591 |
| 2024-09-20 22:21:32.368 | MS1 | 121.4656766338 | 31.1446207145 | 991 | 504990 | -77.15 | 16.80 | 328.93 | 0.15 | 2.92 | 1587 |
| 2024-09-20 22:21:33.827 | MS1 | 121.4656747082 | 31.1446235297 | 991 | 504990 | -78.58 | 15.95 | 356.28 | 0.03 | 2.36 | 1583 |
| 2024-09-20 22:21:34.894 | MS1 | 121.4656743045 | 31.1446323456 | 190 | 504990 | -86.75 | 3.68 | 27.39 | 0.16 | 1.14 | 1584 |
| 2024-09-20 22:21:35.620 | MS1 | 121.4656586324 | 31.1446285446 | 190 | 504990 | -81.71 | 4.36 | 34.00 | 0.13 | 1.39 | 1572 |
| 2024-09-20 22:21:36.793 | MS1 | 121.4656722174 | 31.1446278181 | 991 | 504990 | -85.64 | 3.85 | 42.72 | 0.12 | 1.39 | 1564 |
| 2024-09-20 22:21:37.160 | MS1 | 121.4656628203 | 31.1446293762 | 991 | 504990 | -86.94 | 3.71 | 48.03 | 0.06 | 1.34 | 1573 |
| 2024-09-20 22:21:38.858 | MS1 | 121.4656696506 | 31.1446234845 | 190 | 504990 | -80.65 | 2.94 | 56.42 | 0.13 | 1.06 | 1600 |
| 2024-09-20 22:21:39.355 | MS1 | 121.4656706201 | 31.1446303553 | 190 | 504990 | -81.94 | 4.38 | 49.89 | 0.13 | 1.15 | 1578 |
| 2024-09-20 22:21:40.623 | MS1 | 121.4656616738 | 31.1446300000 | 190 | 504990 | -83.38 | 13.62 | 469.33 | 0.02 | 2.38 | 1570 |
| 2024-09-20 22:21:41.911 | MS1 | 121.4656767043 | 31.1446280382 | 190 | 504990 | -82.93 | 16.27 | 485.22 | 0.03 | 2.14 | 1580 |
| 2024-09-20 22:21:42.820 | MS1 | 121.4656678526 | 31.1446203593 | 190 | 504990 | -84.28 | 13.31 | 374.24 | 0.14 | 2.00 | 1565 |

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
| 3212434 | 5 | 121.4701494180 | 31.1457895205 | 249 | 0 | 1 | 43.5 | TDD | 991 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3215447 | 3 | 121.4665046563 | 31.1538471312 | 4 | 0 | 1 | 41.5 | TDD | 190 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3262219 | 1 | 121.4741526943 | 31.1468931052 | 327 | 7 | 0 | 46.6 | TDD | 933 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3262839 | 2 | 121.4737956843 | 31.1525916419 | 195 | 0 | 9 | 42.1 | TDD | 949 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3277467 | 4 | 121.4758770093 | 31.1442732741 | 15 | 5 | 10 | 33.5 | TDD | 606 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.540 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.558 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.702 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.702 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.357 | NREventA3 | measId:2;ServCellPCI:237;Se... |
| 2024-09-20 22:21:34.597 | NRHandoverAttempt | SourcePCI:237;SourceNR-ARFC... |
| 2024-09-20 22:21:34.635 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.648 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:34.791 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.791 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.357 | NREventA3 | measId:2;ServCellPCI:885;Se... |
| 2024-09-20 22:21:36.597 | NRHandoverAttempt | SourcePCI:885;SourceNR-ARFC... |
| 2024-09-20 22:21:36.642 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.653 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.803 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.803 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.357 | NREventA3 | measId:2;ServCellPCI:237;Se... |
| 2024-09-20 22:21:38.597 | NRHandoverAttempt | SourcePCI:237;SourceNR-ARFC... |
| 2024-09-20 22:21:38.638 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.649 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.799 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.799 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262219 | 1 | 9.1845 | 8.5957 | -116.4890 | 7.4326 | 186.3851 | 0.0023 | 0.0170 |
| 2024_09_20 22:00 | 3262839 | 2 | 19.0395 | 10.2131 | -116.6712 | 13.1421 | 143.7841 | 0.0067 | 0.0164 |
| 2024_09_20 22:00 | 3215447 | 3 | 7.5986 | 5.7379 | -115.9189 | 16.4332 | 196.4002 | 0.0109 | 0.0143 |
| 2024_09_20 22:00 | 3277467 | 4 | 10.0646 | 17.2110 | -115.1140 | 16.7756 | 199.6209 | 0.0139 | 0.0187 |
| 2024_09_20 22:00 | 3212434 | 5 | 17.8962 | 15.2484 | -117.6083 | 10.5966 | 147.1270 | 0.0038 | 0.0152 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415435_DBD38DE4 | 504990 | 991 | -88.1 | 504990 | 190 | -83.1 | 504990 | 949 | -88.7 | 504990 | 933 |
| MR_1774415435_2DE0C4B6 | 504990 | 190 | -86.3 | 504990 | 991 | -83.8 | 504990 | 949 | -88.1 | 504990 | 933 |
| MR_1774415435_6F31EAC0 | 504990 | 991 | -87.8 | 504990 | 190 | -83.2 | 504990 | 949 | -86.1 | 504990 | 933 |
| MR_1774415435_F52AC05B | 504990 | 991 | -88.3 | 504990 | 190 | -84.9 | 504990 | 949 | -86.5 | 504990 | 933 |
| MR_1774415435_C770693D | 504990 | 190 | -85.9 | 504990 | 991 | -85.2 | 504990 | 949 | -86.7 | 504990 | 933 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 139: `00a9aa39-51b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `00a9aa39-51b3-458f-a6a2-7c41b69cca04` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Add neighbor relationship between 3262760_2 and 3275750_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[139] topology](images/train_0139.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3262760_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262760_2
- `C3`: Decrease transmission power for 3275750_3
- `C4`: Decrease A3 Offset threshold for 3262760_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275750_3
- `C6`: Add neighbor relationship between 3218639_1 and 3275750_3
- `C7`: Lift the tilt angle  of 3275750_3 by 5 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Press down the tilt angle  of 3275750_3 by 5 degrees
- `C10`: Add neighbor relationship between 3262760_2 and 3275750_3 **← 정답**
- `C11`: Increase A3 Offset threshold for 3275750_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275750_3
- `C13`: Check test server and transmission issues
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262760_2
- `C15`: Lift the tilt angle of 3262760_2 by 2 degrees
- `C16`: Adjust the azimuth of 3275750_3 by 13 degrees
- `C17`: Press down the tilt angle of 3262760_2 by 2 degrees
- `C18`: Increase A3 Offset threshold for 3262760_2
- `C19`: Adjust the azimuth of 3262760_2 by 50 degrees
- `C20`: Decrease transmission power for 3262760_2
- `C21`: Decrease A3 Offset threshold for 3275750_3
- `C22`: Increase transmission power for 3275750_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.481 | MS1 | 121.4656766849 | 31.1446364843 | 476 | 504990 | -77.94 | 17.83 | 347.66 | 0.14 | 2.07 | 1590 |
| 2024-09-20 22:21:32.768 | MS1 | 121.4656777597 | 31.1446324527 | 476 | 504990 | -78.40 | 13.67 | 582.52 | 0.13 | 2.64 | 1597 |
| 2024-09-20 22:21:33.190 | MS1 | 121.4656661115 | 31.1446180462 | 476 | 504990 | -78.65 | 17.98 | 339.39 | 0.13 | 2.58 | 1589 |
| 2024-09-20 22:21:34.290 | MS1 | 121.4656618164 | 31.1446365623 | 476 | 504990 | -93.57 | -1.46 | 30.97 | 0.04 | 1.46 | 1565 |
| 2024-09-20 22:21:35.295 | MS1 | 121.4656762442 | 31.1446284215 | 476 | 504990 | -91.70 | -0.84 | 66.32 | 0.02 | 1.46 | 1581 |
| 2024-09-20 22:21:36.975 | MS1 | 121.4656766178 | 31.1446228366 | 476 | 504990 | -93.88 | -2.10 | 54.34 | 0.20 | 1.44 | 1576 |
| 2024-09-20 22:21:37.812 | MS1 | 121.4656663440 | 31.1446293582 | 476 | 504990 | -88.16 | -1.71 | 35.10 | 0.19 | 1.30 | 1593 |
| 2024-09-20 22:21:38.353 | MS1 | 121.4656745989 | 31.1446274438 | 476 | 504990 | -77.94 | 13.18 | 391.10 | 0.16 | 1.46 | 1575 |
| 2024-09-20 22:21:39.861 | MS1 | 121.4656699144 | 31.1446329976 | 476 | 504990 | -81.37 | 12.90 | 461.93 | 0.14 | 1.27 | 1569 |
| 2024-09-20 22:21:40.490 | MS1 | 121.4656723092 | 31.1446247942 | 476 | 504990 | -76.30 | 14.71 | 572.69 | 0.17 | 2.56 | 1562 |
| 2024-09-20 22:21:41.704 | MS1 | 121.4656711588 | 31.1446357902 | 476 | 504990 | -84.01 | 16.59 | 407.35 | 0.15 | 2.46 | 1595 |
| 2024-09-20 22:21:42.319 | MS1 | 121.4656693032 | 31.1446221438 | 476 | 504990 | -76.41 | 12.28 | 435.94 | 0.08 | 2.97 | 1576 |

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
| 3218639 | 1 | 121.4704465325 | 31.1463954287 | 162 | 6 | 7 | 42.9 | TDD | 287 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3262760 | 2 | 121.4750321838 | 31.1527195005 | 290 | 1 | 0 | 32.3 | TDD | 476 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3275750 | 3 | 121.4640077970 | 31.1543190336 | 185 | 4 | 4 | 15.8 | TDD | 772 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3279720 | 4 | 121.4681361387 | 31.1509943136 | 248 | 6 | 6 | 34.1 | TDD | 863 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.257 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.273 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.419 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.419 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.076 | NREventA3 | measId:2;ServCellPCI:164;Se... |
| 2024-09-20 22:21:36.076 | NREventA3 | measId:2;ServCellPCI:164;Se... |
| 2024-09-20 22:21:37.076 | NREventA3 | measId:2;ServCellPCI:164;Se... |
| 2024-09-20 22:21:39.576 | NRRRCReestablishAttempt | PCI:164 |
| 2024-09-20 22:21:39.594 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.608 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.754 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.754 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218639 | 1 | 19.4639 | 15.6331 | -117.6162 | 8.2742 | 195.5745 | 0.0006 | 0.0077 |
| 2024_09_20 22:00 | 3262760 | 2 | 15.7755 | 7.0119 | -116.7117 | 15.1233 | 87.6516 | 0.0145 | 0.1552 |
| 2024_09_20 22:00 | 3275750 | 3 | 9.3836 | 13.9130 | -116.9606 | 5.6392 | 141.4249 | 0.0067 | 0.0048 |
| 2024_09_20 22:00 | 3279720 | 4 | 8.6730 | 5.5431 | -116.2823 | 10.8835 | 119.2410 | 0.0035 | 0.0019 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413291_EE3093FA | 504990 | 476 | -94.4 | 504990 | 772 | -89.1 | 504990 | 287 | -97.0 | 504990 | 863 |
| MR_1774413291_24B703E2 | 504990 | 476 | -93.0 | 504990 | 772 | -89.6 | 504990 | 287 | -96.2 | 504990 | 863 |
| MR_1774413291_622F1FF6 | 504990 | 772 | -88.8 | 504990 | 476 | -94.1 | 504990 | 287 | -98.4 | 504990 | 863 |
| MR_1774413291_E5E0ADBF | 504990 | 772 | -90.3 | 504990 | 476 | -95.2 | 504990 | 287 | -95.1 | 504990 | 863 |
| MR_1774413291_B0C13261 | 504990 | 476 | -93.0 | 504990 | 772 | -88.9 | 504990 | 287 | -96.1 | 504990 | 863 |
| MR_1774413291_C416075E | 504990 | 772 | -89.4 | 504990 | 476 | -95.2 | 504990 | 287 | -95.5 | 504990 | 863 |

> *... 2개 열 생략 (전체 14열)*

---
