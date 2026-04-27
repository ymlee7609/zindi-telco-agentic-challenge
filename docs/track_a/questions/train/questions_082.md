# Track A 문제 분석 — train[810]~train[819]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[810] ~ train[819] (10개)

## 목차

1. [문제 810: `005746cc-c81...`](#810) — single-answer, 정답: C20
2. [문제 811: `a70589c7-784...`](#811) — single-answer, 정답: C13
3. [문제 812: `d62b4f9c-db9...`](#812) — single-answer, 정답: C3
4. [문제 813: `308f5e12-a89...`](#813) — single-answer, 정답: C11
5. [문제 814: `3c04f44e-62a...`](#814) — single-answer, 정답: C16
6. [문제 815: `9f4a3f00-689...`](#815) — single-answer, 정답: C11
7. [문제 816: `71cfd2e5-75e...`](#816) — multiple-answer, 정답: C12|C18
8. [문제 817: `4694a279-62f...`](#817) — single-answer, 정답: C2
9. [문제 818: `01f99e5f-6a0...`](#818) — multiple-answer, 정답: C2|C3
10. [문제 819: `239d4c76-163...`](#819) — single-answer, 정답: C14

---

### 문제 810: `005746cc-c81...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `005746cc-c812-4c1d-b9fc-ef6578364163` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[810] topology](images/train_0810.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3260418_3
- `C2`: Decrease A3 Offset threshold for 3260418_3
- `C3`: Increase transmission power for 3224350_4
- `C4`: Lift the tilt angle of 3224350_4 by 5 degrees
- `C5`: Add neighbor relationship between 3224350_4 and 3260418_3
- `C6`: Check test server and transmission issues
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224350_4
- `C8`: Press down the tilt angle of 3224350_4 by 5 degrees
- `C9`: Decrease A3 Offset threshold for 3224350_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260418_3
- `C11`: Increase A3 Offset threshold for 3224350_4
- `C12`: Decrease transmission power for 3260418_3
- `C13`: Adjust the azimuth of 3224350_4 by 50 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260418_3
- `C15`: Decrease transmission power for 3224350_4
- `C16`: Add neighbor relationship between 3225334_2 and 3260418_3
- `C17`: Adjust the azimuth of 3260418_3 by 44 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224350_4
- `C19`: Increase A3 Offset threshold for 3260418_3
- `C20`: Insufficient data; more data is needed for judgment. **← 정답**
- `C21`: Press down the tilt angle  of 3260418_3 by 10 degrees
- `C22`: Lift the tilt angle  of 3260418_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.777 | MS1 | 121.4656763646 | 31.1446247593 | 781 | 504990 | -91.79 | 14.38 | 468.83 | 0.05 | 2.52 | 1575 |
| 2024-09-20 22:21:32.478 | MS1 | 121.4656759406 | 31.1446356062 | 781 | 504990 | -87.86 | 12.87 | 314.51 | 0.18 | 2.31 | 1591 |
| 2024-09-20 22:21:33.980 | MS1 | 121.4656622518 | 31.1446238925 | 781 | 504990 | -88.50 | 17.36 | 444.61 | 0.08 | 2.92 | 1574 |
| 2024-09-20 22:21:34.691 | MS1 | 121.4656631772 | 31.1446249715 | 781 | 504990 | -90.94 | 13.09 | 82.97 | 0.12 | 2.45 | 1567 |
| 2024-09-20 22:21:35.245 | MS1 | 121.4656757365 | 31.1446291354 | 781 | 504990 | -88.10 | 14.52 | 81.48 | 0.08 | 2.60 | 1574 |
| 2024-09-20 22:21:36.834 | MS1 | 121.4656678840 | 31.1446370595 | 781 | 504990 | -89.75 | 12.97 | 85.62 | 0.09 | 2.59 | 1585 |
| 2024-09-20 22:21:37.718 | MS1 | 121.4656618949 | 31.1446225119 | 781 | 504990 | -93.33 | 12.95 | 69.19 | 0.01 | 2.61 | 1591 |
| 2024-09-20 22:21:38.511 | MS1 | 121.4656711302 | 31.1446247247 | 781 | 504990 | -93.98 | 10.05 | 60.23 | 0.12 | 2.62 | 1572 |
| 2024-09-20 22:21:39.908 | MS1 | 121.4656693715 | 31.1446324306 | 781 | 504990 | -90.86 | 9.65 | 74.30 | 0.16 | 2.61 | 1573 |
| 2024-09-20 22:21:40.420 | MS1 | 121.4656775700 | 31.1446207804 | 781 | 504990 | -93.67 | 7.76 | 309.40 | 0.16 | 2.94 | 1568 |
| 2024-09-20 22:21:41.695 | MS1 | 121.4656652189 | 31.1446257115 | 781 | 504990 | -90.80 | 10.58 | 530.45 | 0.05 | 2.24 | 1567 |
| 2024-09-20 22:21:42.303 | MS1 | 121.4656728713 | 31.1446275654 | 781 | 504990 | -90.56 | 7.78 | 524.93 | 0.11 | 2.67 | 1579 |

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
| 3222625 | 1 | 121.4654479984 | 31.1535012789 | 194 | 10 | 2 | 23.2 | TDD | 336 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3224350 | 4 | 121.4715197032 | 31.1443985890 | 185 | 2 | 12 | 28.4 | TDD | 781 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3225334 | 2 | 121.4671049422 | 31.1518231798 | 153 | 12 | 4 | 16.1 | TDD | 378 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3260418 | 3 | 121.4712411280 | 31.1512350309 | 260 | 12 | 8 | 41.3 | TDD | 763 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.001 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.022 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.129 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.129 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.808 | NREventA3 | measId:2;ServCellPCI:684;Se... |
| 2024-09-20 22:21:38.048 | NRHandoverAttempt | SourcePCI:684;SourceNR-ARFC... |
| 2024-09-20 22:21:38.095 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.109 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.256 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.256 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3222625 | 1 | 88.4068 | 84.5986 | -115.8127 | 19.7387 | 148.3038 | 0.0005 | 0.0033 |
| 2024_09_19 22:00 | 3225334 | 2 | 93.4991 | 90.4054 | -116.2246 | 15.6017 | 91.8618 | 0.0161 | 0.0088 |
| 2024_09_19 22:00 | 3260418 | 3 | 77.9908 | 80.3624 | -115.9897 | 11.7633 | 190.3715 | 0.0035 | 0.0036 |
| 2024_09_19 22:00 | 3224350 | 4 | 81.4041 | 92.9013 | -117.4740 | 14.5760 | 125.3487 | 0.0074 | 0.0200 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413614_F28E9C09 | 504990 | 781 | -90.6 | 504990 | 763 | -99.8 | 504990 | 378 | -100.7 | 504990 | 336 |
| MR_1774413614_A5EE05A7 | 504990 | 781 | -91.7 | 504990 | 763 | -98.4 | 504990 | 378 | -100.7 | 504990 | 336 |
| MR_1774413614_523EA4EB | 504990 | 781 | -92.5 | 504990 | 763 | -101.1 | 504990 | 378 | -99.4 | 504990 | 336 |
| MR_1774413614_16A108EE | 504990 | 781 | -89.1 | 504990 | 763 | -98.6 | 504990 | 378 | -101.0 | 504990 | 336 |
| MR_1774413614_D0123896 | 504990 | 781 | -89.0 | 504990 | 763 | -99.9 | 504990 | 378 | -101.3 | 504990 | 336 |
| MR_1774413614_588DB52D | 504990 | 781 | -89.9 | 504990 | 763 | -101.0 | 504990 | 378 | -98.8 | 504990 | 336 |
| MR_1774413614_BC03C1E5 | 504990 | 781 | -91.9 | 504990 | 763 | -99.3 | 504990 | 378 | -101.8 | 504990 | 336 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 811: `a70589c7-784...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a70589c7-784a-4275-9f2f-dd961aad03a0` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Lift the tilt angle  of 3256579_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[811] topology](images/train_0811.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263412_4
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Add neighbor relationship between 3256579_2 and 3257574_3
- `C4`: Increase A3 Offset threshold for 3257574_3
- `C5`: Adjust the azimuth of 3256579_2 by 50 degrees
- `C6`: Increase transmission power for 3263412_4
- `C7`: Increase transmission power for 3257574_3
- `C8`: Increase A3 Offset threshold for 3263412_4
- `C9`: Decrease transmission power for 3263412_4
- `C10`: Press down the tilt angle  of 3256579_2 by 10 degrees
- `C11`: Check test server and transmission issues
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263412_4
- `C13`: Lift the tilt angle  of 3256579_2 by 10 degrees **← 정답**
- `C14`: Add neighbor relationship between 3263412_4 and 3257574_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257574_3
- `C16`: Lift the tilt angle of 3263412_4 by 3 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257574_3
- `C18`: Decrease A3 Offset threshold for 3263412_4
- `C19`: Decrease A3 Offset threshold for 3257574_3
- `C20`: Decrease transmission power for 3257574_3
- `C21`: Adjust the azimuth of 3263412_4 by 29 degrees
- `C22`: Press down the tilt angle of 3263412_4 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.215 | MS1 | 121.4656717746 | 31.1446232554 | 758 | 504990 | -85.18 | 15.15 | 449.37 | 0.17 | 2.75 | 1590 |
| 2024-09-20 22:21:32.749 | MS1 | 121.4656611951 | 31.1446202135 | 758 | 504990 | -88.34 | 16.08 | 483.78 | 0.03 | 2.80 | 1562 |
| 2024-09-20 22:21:33.589 | MS1 | 121.4656609838 | 31.1446267816 | 758 | 504990 | -89.38 | 13.16 | 358.01 | 0.09 | 2.05 | 1562 |
| 2024-09-20 22:21:34.322 | MS1 | 121.4656678109 | 31.1446340267 | 758 | 504990 | -85.37 | 17.98 | 58.93 | 0.05 | 2.43 | 1600 |
| 2024-09-20 22:21:35.927 | MS1 | 121.4656607371 | 31.1446282055 | 758 | 504990 | -89.70 | 12.57 | 104.09 | 0.14 | 2.28 | 1583 |
| 2024-09-20 22:21:36.307 | MS1 | 121.4656594333 | 31.1446288120 | 758 | 504990 | -87.09 | 16.00 | 46.13 | 0.14 | 2.72 | 1600 |
| 2024-09-20 22:21:37.748 | MS1 | 121.4656779283 | 31.1446206485 | 758 | 504990 | -90.39 | 8.34 | 85.33 | 0.11 | 2.55 | 1574 |
| 2024-09-20 22:21:38.793 | MS1 | 121.4656598991 | 31.1446332395 | 758 | 504990 | -92.62 | 10.75 | 84.90 | 0.03 | 2.88 | 1561 |
| 2024-09-20 22:21:39.750 | MS1 | 121.4656662332 | 31.1446323317 | 758 | 504990 | -92.72 | 11.75 | 94.23 | 0.03 | 2.34 | 1563 |
| 2024-09-20 22:21:40.541 | MS1 | 121.4656699350 | 31.1446248850 | 758 | 504990 | -91.38 | 7.58 | 545.08 | 0.11 | 2.67 | 1560 |
| 2024-09-20 22:21:41.561 | MS1 | 121.4656611577 | 31.1446225527 | 758 | 504990 | -93.21 | 9.00 | 415.35 | 0.13 | 2.15 | 1599 |
| 2024-09-20 22:21:42.976 | MS1 | 121.4656614389 | 31.1446235404 | 758 | 504990 | -89.77 | 7.55 | 483.35 | 0.10 | 2.38 | 1586 |

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
| 3256579 | 2 | 121.4659701175 | 31.1533535902 | 1 | 3 | 8 | 33.4 | TDD | 420 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3257574 | 3 | 121.4659264337 | 31.1518654079 | 241 | 13 | 2 | 43.5 | TDD | 102 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3263412 | 4 | 121.4658650348 | 31.1551855375 | 210 | 2 | 0 | 20.3 | TDD | 758 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3273300 | 1 | 121.4742144359 | 31.1538471043 | 202 | 3 | 3 | 37.6 | TDD | 890 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.108 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.210 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.210 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.906 | NREventA3 | measId:2;ServCellPCI:855;Se... |
| 2024-09-20 22:21:38.146 | NRHandoverAttempt | SourcePCI:855;SourceNR-ARFC... |
| 2024-09-20 22:21:38.186 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.201 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.335 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.335 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273300 | 1 | 8.1286 | 10.2211 | -115.6747 | 9.0872 | 80.6739 | 0.0155 | 0.0045 |
| 2024_09_20 22:00 | 3256579 | 2 | 6.6675 | 10.1060 | -115.9086 | 10.5816 | 133.3412 | 0.0072 | 0.0066 |
| 2024_09_20 22:00 | 3257574 | 3 | 9.3643 | 17.8616 | -114.2696 | 15.4699 | 133.4673 | 0.0053 | 0.0009 |
| 2024_09_20 22:00 | 3263412 | 4 | 94.2569 | 83.3670 | -115.0412 | 12.6076 | 143.3369 | 0.0156 | 0.0160 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413203_27DFFD48 | 504990 | 758 | -83.8 | 504990 | 102 | -93.4 | 504990 | 420 | -93.9 | 504990 | 890 |
| MR_1774413203_96AA42A8 | 504990 | 758 | -86.8 | 504990 | 102 | -91.3 | 504990 | 420 | -92.5 | 504990 | 890 |
| MR_1774413203_3F75B4F3 | 504990 | 758 | -83.9 | 504990 | 102 | -91.1 | 504990 | 420 | -93.9 | 504990 | 890 |
| MR_1774413203_7727460B | 504990 | 758 | -84.0 | 504990 | 102 | -93.5 | 504990 | 420 | -94.3 | 504990 | 890 |
| MR_1774413203_FF590294 | 504990 | 758 | -86.8 | 504990 | 102 | -92.3 | 504990 | 420 | -92.6 | 504990 | 890 |
| MR_1774413203_78FA06AD | 504990 | 758 | -87.2 | 504990 | 102 | -91.8 | 504990 | 420 | -92.8 | 504990 | 890 |
| MR_1774413203_24F60BB2 | 504990 | 758 | -86.9 | 504990 | 102 | -93.7 | 504990 | 420 | -95.0 | 504990 | 890 |
| MR_1774413203_8A90A0C1 | 504990 | 758 | -86.3 | 504990 | 102 | -92.5 | 504990 | 420 | -95.8 | 504990 | 890 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 812: `d62b4f9c-db9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d62b4f9c-db93-43f6-b204-7ab76e53b6c1` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262572_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[812] topology](images/train_0812.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3262572_3 by 1 degrees
- `C2`: Increase A3 Offset threshold for 3262572_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262572_3 **← 정답**
- `C4`: Adjust the azimuth of 3260485_2 by 30 degrees
- `C5`: Decrease transmission power for 3262572_3
- `C6`: Increase transmission power for 3262572_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260485_2
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Adjust the azimuth of 3262572_3 by 29 degrees
- `C10`: Increase A3 Offset threshold for 3260485_2
- `C11`: Press down the tilt angle  of 3260485_2 by 2 degrees
- `C12`: Check test server and transmission issues
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260485_2
- `C14`: Decrease A3 Offset threshold for 3262572_3
- `C15`: Decrease A3 Offset threshold for 3260485_2
- `C16`: Decrease transmission power for 3260485_2
- `C17`: Lift the tilt angle  of 3260485_2 by 2 degrees
- `C18`: Add neighbor relationship between 3262572_3 and 3260485_2
- `C19`: Lift the tilt angle of 3262572_3 by 1 degrees
- `C20`: Add neighbor relationship between 3225790_10 and 3260485_2
- `C21`: Increase transmission power for 3260485_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262572_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.253 | MS1 | 121.4656674306 | 31.1446312976 | 903 | 504990 | -95.73 | 14.87 | 463.42 | 0.09 | 2.66 | 1571 |
| 2024-09-20 22:21:32.694 | MS1 | 121.4656720651 | 31.1446345934 | 671 | 504990 | -95.11 | 9.92 | 505.89 | 0.02 | 2.84 | 1575 |
| 2024-09-20 22:21:33.919 | MS1 | 121.4656765733 | 31.1446338631 | 758 | 504990 | -95.05 | 11.77 | 558.84 | 0.14 | 2.52 | 1594 |
| 2024-09-20 22:21:34.976 | MS1 | 121.4656651066 | 31.1446302308 | 204 | 152650 | -92.69 | 3.65 | 85.73 | 0.19 | 1.61 | 934 |
| 2024-09-20 22:21:35.187 | MS1 | 121.4656659524 | 31.1446189619 | 722 | 152650 | -87.84 | 7.64 | 89.72 | 0.14 | 1.93 | 969 |
| 2024-09-20 22:21:36.491 | MS1 | 121.4656750231 | 31.1446373471 | 47 | 152650 | -87.31 | 5.72 | 78.80 | 0.14 | 1.75 | 927 |
| 2024-09-20 22:21:37.530 | MS1 | 121.4656695475 | 31.1446202032 | 453 | 152650 | -89.64 | 7.97 | 94.02 | 0.17 | 1.77 | 955 |
| 2024-09-20 22:21:38.351 | MS1 | 121.4656599463 | 31.1446301398 | 204 | 152650 | -92.36 | 4.45 | 72.64 | 0.11 | 1.61 | 969 |
| 2024-09-20 22:21:39.273 | MS1 | 121.4656644403 | 31.1446358921 | 722 | 152650 | -90.65 | 4.35 | 84.99 | 0.13 | 1.72 | 951 |
| 2024-09-20 22:21:40.340 | MS1 | 121.4656582738 | 31.1446204762 | 47 | 152650 | -96.24 | 5.31 | 86.40 | 0.01 | 2.18 | 1574 |
| 2024-09-20 22:21:41.746 | MS1 | 121.4656733793 | 31.1446300516 | 453 | 152650 | -89.73 | 4.03 | 66.39 | 0.03 | 2.99 | 1595 |
| 2024-09-20 22:21:42.198 | MS1 | 121.4656627761 | 31.1446291762 | 204 | 152650 | -92.22 | 7.62 | 94.53 | 0.15 | 2.83 | 1584 |

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
| 3217593 | 7 | 121.4709506356 | 31.1449856961 | 202 | 10 | 12 | 17.2 | FDD | 609 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3225790 | 10 | 121.4650486959 | 31.1508254352 | 21 | 6 | 1 | 4.1 | FDD | 47 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3231329 | 6 | 121.4751339567 | 31.1533205442 | 42 | 12 | 5 | 9.9 | TDD | 671 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3232872 | 8 | 121.4707797847 | 31.1504592474 | 87 | 7 | 10 | 6.8 | FDD | 453 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3236727 | 11 | 121.4705538243 | 31.1453231713 | 241 | 2 | 8 | 14.7 | FDD | 722 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3243634 | 5 | 121.4676404563 | 31.1496597542 | 177 | 6 | 0 | 28.0 | TDD | 758 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3251154 | 4 | 121.4641464518 | 31.1454956343 | 126 | 5 | 0 | 13.9 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3251331 | 12 | 121.4683084584 | 31.1462476124 | 310 | 0 | 0 | 17.0 | FDD | 859 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3260485 | 2 | 121.4673794273 | 31.1555339259 | 158 | 2 | 0 | 9.7 | TDD | 293 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3260842 | 9 | 121.4722453331 | 31.1463659252 | 100 | 13 | 6 | 8.5 | FDD | 204 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3262572 | 3 | 121.4653430302 | 31.1545751997 | 207 | 0 | 0 | 17.5 | TDD | 903 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3264698 | 13 | 121.4742875801 | 31.1463560380 | 94 | 1 | 9 | 11.6 | FDD | 990 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3270203 | 1 | 121.4736743947 | 31.1460617810 | 252 | 13 | 11 | 2.2 | TDD | 386 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.364 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.382 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.485 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.485 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.187 | NREventA2 | measId:1;ServCellPCI:864;Se... |
| 2024-09-20 22:21:35.301 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.553 | NREventA5 | measId:3;ServCellPCI:864;Se... |
| 2024-09-20 22:21:35.589 | NRHandoverAttempt | SourcePCI:864;SourceNR-ARFC... |
| 2024-09-20 22:21:35.626 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.636 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.748 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.748 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270203 | 1 | 11.0762 | 15.9050 | -115.5156 | 11.1013 | 178.6307 | 0.0132 | 0.0134 |
| 2024_09_20 22:00 | 3260485 | 2 | 18.8097 | 18.9460 | -114.7591 | 10.6182 | 191.9111 | 0.0047 | 0.0153 |
| 2024_09_20 22:00 | 3262572 | 3 | 7.8719 | 10.5936 | -115.7912 | 11.7690 | 117.7881 | 0.0091 | 0.0065 |
| 2024_09_20 22:00 | 3251154 | 4 | 5.6327 | 13.9433 | -115.7321 | 18.9850 | 81.4745 | 0.0190 | 0.0115 |
| 2024_09_20 22:00 | 3243634 | 5 | 7.1584 | 7.7127 | -117.2694 | 13.7837 | 132.8125 | 0.0184 | 0.0060 |
| 2024_09_20 22:00 | 3231329 | 6 | 9.1756 | 12.2534 | -117.7064 | 11.5568 | 110.4043 | 0.0187 | 0.0182 |
| 2024_09_20 22:00 | 3217593 | 7 | 13.9524 | 9.8222 | -117.8168 | 4.1091 | 47.8971 | 0.0020 | 0.0143 |
| 2024_09_20 22:00 | 3232872 | 8 | 11.5766 | 11.0240 | -115.5760 | 3.7315 | 58.0239 | 0.0080 | 0.0152 |
| 2024_09_20 22:00 | 3260842 | 9 | 7.8456 | 16.3122 | -114.7507 | 3.1532 | 43.5116 | 0.0100 | 0.0033 |
| 2024_09_20 22:00 | 3225790 | 10 | 19.0513 | 17.5098 | -115.0605 | 4.4229 | 50.1733 | 0.0054 | 0.0047 |
| 2024_09_20 22:00 | 3236727 | 11 | 10.6380 | 6.2250 | -114.2734 | 3.9284 | 44.6863 | 0.0169 | 0.0091 |
| 2024_09_20 22:00 | 3251331 | 12 | 6.2529 | 18.9483 | -116.3981 | 4.1359 | 23.4092 | 0.0093 | 0.0126 |
| 2024_09_20 22:00 | 3264698 | 13 | 7.7462 | 10.5904 | -114.6760 | 4.0697 | 47.8097 | 0.0018 | 0.0101 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415208_25965D97 | 504990 | 758 | -93.3 | 504990 | 293 | -95.0 | 504990 | 309 | -97.5 | 504990 | 386 |
| MR_1774415208_4E77CF70 | 504990 | 758 | -94.6 | 504990 | 293 | -96.8 | 504990 | 309 | -98.2 | 504990 | 386 |
| MR_1774415208_8B548D12 | 504990 | 758 | -96.3 | 504990 | 293 | -96.6 | 504990 | 309 | -98.7 | 504990 | 386 |
| MR_1774415208_682A0D7E | 504990 | 758 | -94.0 | 504990 | 293 | -97.8 | 504990 | 309 | -97.0 | 504990 | 386 |
| MR_1774415208_84A4DE60 | 504990 | 758 | -93.4 | 504990 | 293 | -98.2 | 504990 | 309 | -99.4 | 504990 | 386 |
| MR_1774415208_8EC2459C | 504990 | 758 | -93.5 | 504990 | 293 | -95.5 | 504990 | 309 | -98.9 | 504990 | 386 |
| MR_1774415208_4A80E83D | 504990 | 758 | -95.0 | 504990 | 293 | -97.5 | 504990 | 309 | -99.5 | 504990 | 386 |
| MR_1774415208_5A82FDFE | 504990 | 758 | -93.9 | 504990 | 293 | -95.2 | 504990 | 309 | -99.1 | 504990 | 386 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 813: `308f5e12-a89...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `308f5e12-a89c-4060-941e-c22c46362a9b` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3260248_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[813] topology](images/train_0813.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3260248_4 by 3 degrees
- `C2`: Decrease A3 Offset threshold for 3271719_3
- `C3`: Increase transmission power for 3271719_3
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease transmission power for 3260248_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271719_3
- `C7`: Decrease A3 Offset threshold for 3260248_4
- `C8`: Lift the tilt angle of 3260248_4 by 3 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260248_4
- `C10`: Adjust the azimuth of 3260248_4 by 7 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260248_4 **← 정답**
- `C12`: Check test server and transmission issues
- `C13`: Decrease transmission power for 3271719_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271719_3
- `C15`: Adjust the azimuth of 3271719_3 by 50 degrees
- `C16`: Add neighbor relationship between 3260248_4 and 3271719_3
- `C17`: Add neighbor relationship between 3241287_1 and 3271719_3
- `C18`: Lift the tilt angle  of 3271719_3 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3260248_4
- `C20`: Increase A3 Offset threshold for 3271719_3
- `C21`: Increase transmission power for 3260248_4
- `C22`: Press down the tilt angle  of 3271719_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.723 | MS1 | 121.4656762199 | 31.1446376985 | 31 | 504990 | -91.43 | 14.93 | 525.51 | 0.06 | 2.74 | 1584 |
| 2024-09-20 22:21:32.409 | MS1 | 121.4656698515 | 31.1446356530 | 31 | 504990 | -88.07 | 16.28 | 318.02 | 0.01 | 2.77 | 1579 |
| 2024-09-20 22:21:33.629 | MS1 | 121.4656656797 | 31.1446355881 | 31 | 504990 | -91.59 | 15.53 | 375.99 | 0.04 | 2.88 | 1595 |
| 2024-09-20 22:21:34.472 | MS1 | 121.4656661655 | 31.1446294088 | 31 | 504990 | -88.47 | 14.77 | 80.05 | 0.66 | 2.21 | 618 |
| 2024-09-20 22:21:35.248 | MS1 | 121.4656759620 | 31.1446200992 | 31 | 504990 | -85.39 | 15.57 | 76.97 | 0.65 | 2.60 | 673 |
| 2024-09-20 22:21:36.510 | MS1 | 121.4656583550 | 31.1446239713 | 31 | 504990 | -88.79 | 15.58 | 71.59 | 0.63 | 2.93 | 589 |
| 2024-09-20 22:21:37.763 | MS1 | 121.4656686608 | 31.1446308614 | 31 | 504990 | -92.90 | 8.41 | 77.34 | 0.66 | 2.86 | 597 |
| 2024-09-20 22:21:38.632 | MS1 | 121.4656717928 | 31.1446306965 | 31 | 504990 | -92.29 | 8.67 | 75.86 | 0.64 | 2.23 | 543 |
| 2024-09-20 22:21:39.593 | MS1 | 121.4656600254 | 31.1446250822 | 31 | 504990 | -93.35 | 12.90 | 73.30 | 0.66 | 2.51 | 516 |
| 2024-09-20 22:21:40.638 | MS1 | 121.4656741417 | 31.1446296536 | 31 | 504990 | -93.49 | 8.60 | 432.96 | 0.07 | 2.59 | 1562 |
| 2024-09-20 22:21:41.436 | MS1 | 121.4656762673 | 31.1446244539 | 31 | 504990 | -93.72 | 12.19 | 363.46 | 0.18 | 2.92 | 1596 |
| 2024-09-20 22:21:42.558 | MS1 | 121.4656608102 | 31.1446282801 | 31 | 504990 | -92.77 | 7.49 | 365.27 | 0.19 | 2.10 | 1568 |

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
| 3236676 | 2 | 121.4649800819 | 31.1547712429 | 305 | 6 | 3 | 35.4 | TDD | 171 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3241287 | 1 | 121.4708942434 | 31.1448111957 | 134 | 11 | 5 | 17.8 | TDD | 209 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3260248 | 4 | 121.4720024403 | 31.1522578547 | 222 | 1 | 3 | 44.1 | TDD | 31 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3271719 | 3 | 121.4688593371 | 31.1453566813 | 119 | 10 | 2 | 31.2 | TDD | 502 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.235 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.259 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.379 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.379 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.074 | NREventA3 | measId:2;ServCellPCI:878;Se... |
| 2024-09-20 22:21:38.314 | NRHandoverAttempt | SourcePCI:878;SourceNR-ARFC... |
| 2024-09-20 22:21:38.359 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.373 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.486 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.486 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241287 | 1 | 14.6618 | 5.8170 | -114.6014 | 11.1749 | 147.1411 | 0.0031 | 0.0086 |
| 2024_09_20 22:00 | 3236676 | 2 | 17.6860 | 14.8238 | -114.5373 | 11.3858 | 169.4988 | 0.0125 | 0.0030 |
| 2024_09_20 22:00 | 3271719 | 3 | 7.2732 | 9.9015 | -114.1186 | 5.6344 | 138.2677 | 0.0159 | 0.0134 |
| 2024_09_20 22:00 | 3260248 | 4 | 14.9504 | 16.7126 | -114.3321 | 13.4745 | 165.5266 | 0.0048 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416656_D7F37BD7 | 504990 | 31 | -90.1 | 504990 | 502 | -92.8 | 504990 | 209 | -96.1 | 504990 | 171 |
| MR_1774416656_B9641E13 | 504990 | 31 | -88.7 | 504990 | 502 | -93.7 | 504990 | 209 | -96.1 | 504990 | 171 |
| MR_1774416656_A98EB4B1 | 504990 | 31 | -88.1 | 504990 | 502 | -93.3 | 504990 | 209 | -94.8 | 504990 | 171 |
| MR_1774416656_5D902BB1 | 504990 | 31 | -87.2 | 504990 | 502 | -93.4 | 504990 | 209 | -93.6 | 504990 | 171 |
| MR_1774416656_5134B4B4 | 504990 | 31 | -89.8 | 504990 | 502 | -92.4 | 504990 | 209 | -93.5 | 504990 | 171 |
| MR_1774416656_119A89D6 | 504990 | 31 | -89.4 | 504990 | 502 | -91.6 | 504990 | 209 | -96.4 | 504990 | 171 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 814: `3c04f44e-62a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3c04f44e-62a7-4b28-8901-68515c389f79` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222413_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[814] topology](images/train_0814.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase transmission power for 3222413_4
- `C3`: Decrease transmission power for 3222413_4
- `C4`: Press down the tilt angle of 3222413_4 by 5 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222413_4
- `C6`: Adjust the azimuth of 3213544_6 by 14 degrees
- `C7`: Increase A3 Offset threshold for 3222413_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213544_6
- `C9`: Adjust the azimuth of 3222413_4 by 15 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213544_6
- `C11`: Decrease transmission power for 3213544_6
- `C12`: Increase A3 Offset threshold for 3213544_6
- `C13`: Add neighbor relationship between 3222413_4 and 3213544_6
- `C14`: Check test server and transmission issues
- `C15`: Lift the tilt angle  of 3213544_6 by 6 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222413_4 **← 정답**
- `C17`: Lift the tilt angle of 3222413_4 by 5 degrees
- `C18`: Decrease A3 Offset threshold for 3222413_4
- `C19`: Add neighbor relationship between 3245713_12 and 3213544_6
- `C20`: Press down the tilt angle  of 3213544_6 by 6 degrees
- `C21`: Decrease A3 Offset threshold for 3213544_6
- `C22`: Increase transmission power for 3213544_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.290 | MS1 | 121.4656638733 | 31.1446363433 | 462 | 504990 | -95.29 | 13.88 | 503.79 | 0.09 | 2.43 | 1560 |
| 2024-09-20 22:21:32.330 | MS1 | 121.4656738388 | 31.1446299694 | 807 | 504990 | -93.42 | 12.46 | 592.44 | 0.04 | 2.62 | 1569 |
| 2024-09-20 22:21:33.285 | MS1 | 121.4656685116 | 31.1446325784 | 898 | 504990 | -93.03 | 13.12 | 376.21 | 0.13 | 2.46 | 1574 |
| 2024-09-20 22:21:34.748 | MS1 | 121.4656675159 | 31.1446280921 | 127 | 152650 | -95.21 | 3.30 | 64.06 | 0.02 | 1.75 | 925 |
| 2024-09-20 22:21:35.610 | MS1 | 121.4656641844 | 31.1446320415 | 39 | 152650 | -92.12 | 3.43 | 64.13 | 0.02 | 1.85 | 927 |
| 2024-09-20 22:21:36.911 | MS1 | 121.4656765341 | 31.1446328351 | 829 | 152650 | -95.05 | 3.92 | 65.50 | 0.12 | 1.65 | 903 |
| 2024-09-20 22:21:37.603 | MS1 | 121.4656749299 | 31.1446309529 | 908 | 152650 | -96.74 | 3.94 | 43.79 | 0.17 | 1.88 | 991 |
| 2024-09-20 22:21:38.617 | MS1 | 121.4656655116 | 31.1446246037 | 127 | 152650 | -95.72 | 6.01 | 48.79 | 0.17 | 1.93 | 924 |
| 2024-09-20 22:21:39.956 | MS1 | 121.4656613004 | 31.1446251928 | 39 | 152650 | -96.61 | 2.32 | 91.59 | 0.20 | 1.67 | 965 |
| 2024-09-20 22:21:40.210 | MS1 | 121.4656745585 | 31.1446266995 | 829 | 152650 | -94.53 | 6.68 | 48.44 | 0.07 | 2.92 | 1583 |
| 2024-09-20 22:21:41.597 | MS1 | 121.4656750408 | 31.1446213333 | 908 | 152650 | -89.83 | 4.04 | 49.54 | 0.13 | 2.51 | 1589 |
| 2024-09-20 22:21:42.450 | MS1 | 121.4656669300 | 31.1446314417 | 127 | 152650 | -88.85 | 4.75 | 77.18 | 0.02 | 2.21 | 1592 |

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
| 3213544 | 6 | 121.4697951975 | 31.1455560972 | 269 | 2 | 12 | 26.0 | TDD | 378 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3217694 | 13 | 121.4653426969 | 31.1484934671 | 113 | 15 | 12 | 0.7 | FDD | 127 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3218045 | 11 | 121.4732294748 | 31.1555624111 | 70 | 12 | 9 | 16.5 | FDD | 475 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3222413 | 4 | 121.4726029878 | 31.1456312528 | 245 | 4 | 3 | 15.3 | TDD | 462 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3225334 | 10 | 121.4735965211 | 31.1550201086 | 255 | 4 | 2 | 4.2 | FDD | 121 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3226690 | 8 | 121.4655081376 | 31.1549610389 | 108 | 8 | 9 | 2.3 | FDD | 908 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3238491 | 7 | 121.4656205309 | 31.1446316898 | 317 | 2 | 11 | 5.7 | FDD | 39 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3240039 | 9 | 121.4720149223 | 31.1503280398 | 177 | 4 | 11 | 7.3 | FDD | 315 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3245713 | 12 | 121.4659745007 | 31.1521466121 | 16 | 0 | 6 | 8.0 | FDD | 829 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3246028 | 3 | 121.4695688043 | 31.1465923119 | 264 | 14 | 0 | 14.5 | TDD | 807 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3246092 | 2 | 121.4678446218 | 31.1506727240 | 76 | 6 | 1 | 13.6 | TDD | 581 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3263588 | 1 | 121.4741574860 | 31.1463568240 | 127 | 7 | 3 | 14.5 | TDD | 898 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3269811 | 5 | 121.4751191358 | 31.1508599692 | 105 | 2 | 2 | 10.0 | TDD | 502 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.075 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.097 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.227 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.227 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.885 | NREventA2 | measId:1;ServCellPCI:222;Se... |
| 2024-09-20 22:21:35.034 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.304 | NREventA5 | measId:3;ServCellPCI:222;Se... |
| 2024-09-20 22:21:35.345 | NRHandoverAttempt | SourcePCI:222;SourceNR-ARFC... |
| 2024-09-20 22:21:35.375 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.389 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.530 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.530 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263588 | 1 | 17.6834 | 15.5852 | -116.7031 | 6.6158 | 94.6181 | 0.0122 | 0.0007 |
| 2024_09_20 22:00 | 3246092 | 2 | 15.9952 | 10.7250 | -114.3430 | 8.7291 | 166.4172 | 0.0163 | 0.0178 |
| 2024_09_20 22:00 | 3246028 | 3 | 10.5241 | 19.3500 | -114.8628 | 15.9613 | 88.5048 | 0.0154 | 0.0183 |
| 2024_09_20 22:00 | 3222413 | 4 | 12.4367 | 18.0425 | -115.7711 | 5.2995 | 149.6742 | 0.0053 | 0.0021 |
| 2024_09_20 22:00 | 3269811 | 5 | 13.3150 | 7.7210 | -115.3251 | 5.1734 | 139.5763 | 0.0001 | 0.0034 |
| 2024_09_20 22:00 | 3213544 | 6 | 16.3210 | 17.5387 | -116.0787 | 5.3319 | 191.6488 | 0.0032 | 0.0009 |
| 2024_09_20 22:00 | 3238491 | 7 | 5.3907 | 6.1876 | -115.2266 | 4.1072 | 37.8545 | 0.0179 | 0.0117 |
| 2024_09_20 22:00 | 3226690 | 8 | 9.4096 | 17.0546 | -114.0208 | 4.9849 | 59.7442 | 0.0126 | 0.0029 |
| 2024_09_20 22:00 | 3240039 | 9 | 9.5394 | 9.7739 | -116.6816 | 4.4272 | 52.3037 | 0.0004 | 0.0056 |
| 2024_09_20 22:00 | 3225334 | 10 | 6.9850 | 17.1842 | -114.5344 | 4.8811 | 30.5771 | 0.0018 | 0.0190 |
| 2024_09_20 22:00 | 3218045 | 11 | 14.0767 | 10.7644 | -114.4440 | 3.1349 | 23.0080 | 0.0010 | 0.0144 |
| 2024_09_20 22:00 | 3245713 | 12 | 18.6662 | 17.4063 | -116.7703 | 4.3757 | 47.5746 | 0.0120 | 0.0108 |
| 2024_09_20 22:00 | 3217694 | 13 | 7.5119 | 17.2256 | -116.2203 | 3.5029 | 55.8046 | 0.0066 | 0.0090 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414842_CF8AA8CF | 152650 | 127 | -94.4 | 152650 | 475 | -102.3 | 152650 | 121 | -101.2 | 152650 | 315 |
| MR_1774414842_6399D075 | 504990 | 898 | -93.1 | 504990 | 378 | -91.4 | 504990 | 502 | -92.2 | 504990 | 581 |
| MR_1774414842_32AA7B4B | 152650 | 127 | -96.7 | 152650 | 475 | -101.3 | 152650 | 121 | -101.9 | 152650 | 315 |
| MR_1774414842_0EB16A80 | 504990 | 898 | -91.8 | 504990 | 378 | -88.7 | 504990 | 502 | -93.7 | 504990 | 581 |
| MR_1774414842_7BA859A6 | 152650 | 127 | -94.8 | 152650 | 475 | -100.7 | 152650 | 121 | -104.6 | 152650 | 315 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 815: `9f4a3f00-689...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9f4a3f00-689e-4661-9fcf-f8f210699ed8` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214924_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[815] topology](images/train_0815.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3235390_6 by 3 degrees
- `C2`: Lift the tilt angle of 3214924_3 by 6 degrees
- `C3`: Add neighbor relationship between 3214924_3 and 3235390_6
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235390_6
- `C5`: Adjust the azimuth of 3235390_6 by 19 degrees
- `C6`: Add neighbor relationship between 3276613_9 and 3235390_6
- `C7`: Increase A3 Offset threshold for 3214924_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235390_6
- `C9`: Increase A3 Offset threshold for 3235390_6
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214924_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214924_3 **← 정답**
- `C12`: Decrease A3 Offset threshold for 3235390_6
- `C13`: Decrease A3 Offset threshold for 3214924_3
- `C14`: Decrease transmission power for 3235390_6
- `C15`: Increase transmission power for 3235390_6
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Check test server and transmission issues
- `C18`: Press down the tilt angle of 3214924_3 by 6 degrees
- `C19`: Decrease transmission power for 3214924_3
- `C20`: Increase transmission power for 3214924_3
- `C21`: Lift the tilt angle  of 3235390_6 by 3 degrees
- `C22`: Adjust the azimuth of 3214924_3 by 18 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.330 | MS1 | 121.4656769947 | 31.1446361852 | 427 | 504990 | -93.07 | 13.45 | 339.00 | 0.02 | 2.02 | 1562 |
| 2024-09-20 22:21:32.129 | MS1 | 121.4656581542 | 31.1446250383 | 140 | 504990 | -94.16 | 11.45 | 582.57 | 0.06 | 2.22 | 1574 |
| 2024-09-20 22:21:33.687 | MS1 | 121.4656711429 | 31.1446233204 | 528 | 504990 | -93.71 | 9.68 | 346.02 | 0.19 | 2.69 | 1569 |
| 2024-09-20 22:21:34.624 | MS1 | 121.4656612639 | 31.1446203160 | 119 | 152650 | -92.24 | 5.02 | 78.02 | 0.17 | 1.75 | 920 |
| 2024-09-20 22:21:35.754 | MS1 | 121.4656674800 | 31.1446185912 | 243 | 152650 | -92.95 | 4.30 | 85.20 | 0.04 | 1.92 | 974 |
| 2024-09-20 22:21:36.400 | MS1 | 121.4656612837 | 31.1446271575 | 686 | 152650 | -95.06 | 4.33 | 78.36 | 0.19 | 1.91 | 946 |
| 2024-09-20 22:21:37.219 | MS1 | 121.4656679534 | 31.1446222637 | 564 | 152650 | -95.21 | 4.70 | 91.60 | 0.12 | 1.85 | 996 |
| 2024-09-20 22:21:38.280 | MS1 | 121.4656622550 | 31.1446211058 | 119 | 152650 | -96.64 | 3.65 | 47.29 | 0.07 | 1.71 | 991 |
| 2024-09-20 22:21:39.926 | MS1 | 121.4656680216 | 31.1446248570 | 243 | 152650 | -90.01 | 7.69 | 77.78 | 0.01 | 1.57 | 970 |
| 2024-09-20 22:21:40.524 | MS1 | 121.4656663671 | 31.1446278216 | 686 | 152650 | -87.78 | 6.53 | 75.01 | 0.16 | 2.73 | 1598 |
| 2024-09-20 22:21:41.996 | MS1 | 121.4656768078 | 31.1446352663 | 564 | 152650 | -93.50 | 6.52 | 86.44 | 0.12 | 2.37 | 1599 |
| 2024-09-20 22:21:42.428 | MS1 | 121.4656693331 | 31.1446346494 | 119 | 152650 | -95.80 | 2.22 | 85.90 | 0.10 | 2.35 | 1592 |

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
| 3214642 | 13 | 121.4683162885 | 31.1483117442 | 111 | 14 | 7 | 7.0 | FDD | 538 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3214924 | 3 | 121.4704723299 | 31.1486896528 | 243 | 5 | 10 | 8.9 | TDD | 427 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3233780 | 1 | 121.4696414554 | 31.1540751196 | 174 | 13 | 3 | 27.4 | TDD | 544 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3234707 | 2 | 121.4738961029 | 31.1531414918 | 151 | 11 | 8 | 6.3 | TDD | 512 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3235390 | 6 | 121.4656399871 | 31.1506251118 | 199 | 2 | 4 | 6.3 | TDD | 606 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3237625 | 10 | 121.4683026035 | 31.1456711422 | 23 | 5 | 5 | 4.2 | FDD | 243 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3252945 | 5 | 121.4737006883 | 31.1503622484 | 134 | 10 | 1 | 9.8 | TDD | 528 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3254530 | 7 | 121.4690000971 | 31.1516960035 | 226 | 14 | 10 | 20.8 | FDD | 200 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3262131 | 4 | 121.4734683036 | 31.1495038768 | 193 | 10 | 8 | 6.4 | TDD | 140 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3276026 | 12 | 121.4728849716 | 31.1511535529 | 16 | 5 | 1 | 1.1 | FDD | 119 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3276613 | 9 | 121.4719365148 | 31.1503788656 | 327 | 3 | 6 | 22.8 | FDD | 686 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3277904 | 11 | 121.4729079372 | 31.1492751775 | 118 | 9 | 0 | 22.2 | FDD | 564 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3278270 | 8 | 121.4681913433 | 31.1558419863 | 33 | 1 | 3 | 14.5 | FDD | 346 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |

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
| 2024-09-20 22:21:30.816 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.840 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.982 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.982 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.645 | NREventA2 | measId:1;ServCellPCI:630;Se... |
| 2024-09-20 22:21:34.769 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.057 | NREventA5 | measId:3;ServCellPCI:630;Se... |
| 2024-09-20 22:21:35.111 | NRHandoverAttempt | SourcePCI:630;SourceNR-ARFC... |
| 2024-09-20 22:21:35.151 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.162 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.300 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.300 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233780 | 1 | 8.2711 | 12.7657 | -114.9957 | 11.7322 | 163.2875 | 0.0070 | 0.0026 |
| 2024_09_20 22:00 | 3234707 | 2 | 9.9114 | 19.5105 | -115.5433 | 11.1798 | 115.8014 | 0.0065 | 0.0084 |
| 2024_09_20 22:00 | 3214924 | 3 | 8.5631 | 8.0026 | -115.2456 | 7.5043 | 87.6628 | 0.0099 | 0.0100 |
| 2024_09_20 22:00 | 3262131 | 4 | 19.4162 | 12.0951 | -116.9367 | 19.1051 | 138.1868 | 0.0038 | 0.0161 |
| 2024_09_20 22:00 | 3252945 | 5 | 19.3534 | 8.6282 | -115.4040 | 8.0164 | 131.8248 | 0.0080 | 0.0103 |
| 2024_09_20 22:00 | 3235390 | 6 | 8.9482 | 7.3052 | -117.7757 | 12.8756 | 154.4114 | 0.0190 | 0.0055 |
| 2024_09_20 22:00 | 3254530 | 7 | 5.3417 | 8.0928 | -115.5301 | 4.4561 | 21.0247 | 0.0173 | 0.0029 |
| 2024_09_20 22:00 | 3278270 | 8 | 15.5053 | 7.6808 | -117.7112 | 3.7360 | 57.6840 | 0.0160 | 0.0044 |
| 2024_09_20 22:00 | 3276613 | 9 | 18.2789 | 19.0520 | -116.8743 | 3.9434 | 40.6802 | 0.0172 | 0.0107 |
| 2024_09_20 22:00 | 3237625 | 10 | 14.6025 | 11.4914 | -116.3664 | 3.8993 | 25.0972 | 0.0030 | 0.0191 |
| 2024_09_20 22:00 | 3277904 | 11 | 12.3981 | 8.2215 | -116.8178 | 4.7535 | 22.5940 | 0.0121 | 0.0119 |
| 2024_09_20 22:00 | 3276026 | 12 | 9.0220 | 5.1133 | -114.5347 | 3.5761 | 57.2274 | 0.0168 | 0.0075 |
| 2024_09_20 22:00 | 3214642 | 13 | 5.3692 | 6.9765 | -116.4606 | 4.8817 | 49.0524 | 0.0039 | 0.0023 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415551_AE8200E1 | 504990 | 528 | -92.5 | 504990 | 606 | -91.2 | 504990 | 544 | -102.0 | 504990 | 512 |
| MR_1774415551_30347ED0 | 504990 | 528 | -93.7 | 504990 | 606 | -89.4 | 504990 | 544 | -100.6 | 504990 | 512 |
| MR_1774415551_1AAE0CDC | 152650 | 119 | -92.9 | 152650 | 200 | -94.0 | 152650 | 538 | -103.1 | 152650 | 346 |
| MR_1774415551_53472C1E | 504990 | 528 | -91.7 | 504990 | 606 | -90.1 | 504990 | 544 | -101.8 | 504990 | 512 |
| MR_1774415551_4A4881AC | 504990 | 528 | -94.6 | 504990 | 606 | -90.4 | 504990 | 544 | -101.3 | 504990 | 512 |
| MR_1774415551_5BD43CDA | 152650 | 119 | -90.4 | 152650 | 200 | -93.8 | 152650 | 538 | -103.2 | 152650 | 346 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 816: `71cfd2e5-75e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `71cfd2e5-75ea-4861-be54-6ca221ff02d6` |
| Tag | **multiple-answer** |
| 정답 | **C12|C18** |
| C12 의미 | Press down the tilt angle  of 3258071_1 by 5 degrees |
| C18 의미 | Decrease transmission power for 3258071_1 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[816] topology](images/train_0816.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3258071_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233199_2
- `C3`: Decrease A3 Offset threshold for 3233199_2
- `C4`: Lift the tilt angle of 3233199_2 by 3 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258071_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233199_2
- `C7`: Lift the tilt angle  of 3258071_1 by 5 degrees
- `C8`: Check test server and transmission issues
- `C9`: Decrease A3 Offset threshold for 3258071_1
- `C10`: Add neighbor relationship between 3233199_2 and 3258071_1
- `C11`: Press down the tilt angle of 3233199_2 by 3 degrees
- `C12`: Press down the tilt angle  of 3258071_1 by 5 degrees **← 정답**
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Add neighbor relationship between 3269995_3 and 3258071_1
- `C15`: Adjust the azimuth of 3233199_2 by 17 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258071_1
- `C17`: Increase transmission power for 3233199_2
- `C18`: Decrease transmission power for 3258071_1 **← 정답**
- `C19`: Increase A3 Offset threshold for 3258071_1
- `C20`: Decrease transmission power for 3233199_2
- `C21`: Increase A3 Offset threshold for 3233199_2
- `C22`: Adjust the azimuth of 3258071_1 by 12 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.850 | MS1 | 121.4656645032 | 31.1446221503 | 855 | 504990 | -82.43 | 12.45 | 537.84 | 0.01 | 2.12 | 1598 |
| 2024-09-20 22:21:32.415 | MS1 | 121.4656722913 | 31.1446299179 | 855 | 504990 | -81.15 | 14.84 | 438.61 | 0.16 | 2.21 | 1561 |
| 2024-09-20 22:21:33.155 | MS1 | 121.4656678446 | 31.1446362007 | 855 | 504990 | -75.12 | 16.74 | 406.29 | 0.11 | 2.93 | 1571 |
| 2024-09-20 22:21:34.363 | MS1 | 121.4656602115 | 31.1446330379 | 855 | 504990 | -88.93 | 2.29 | 93.57 | 0.18 | 1.07 | 1581 |
| 2024-09-20 22:21:35.457 | MS1 | 121.4656686733 | 31.1446261386 | 855 | 504990 | -88.24 | 0.55 | 79.43 | 0.11 | 1.46 | 1586 |
| 2024-09-20 22:21:36.532 | MS1 | 121.4656623718 | 31.1446347713 | 855 | 504990 | -85.52 | 0.65 | 72.83 | 0.07 | 1.17 | 1590 |
| 2024-09-20 22:21:37.659 | MS1 | 121.4656705489 | 31.1446243603 | 855 | 504990 | -92.51 | 0.40 | 51.84 | 0.00 | 1.34 | 1573 |
| 2024-09-20 22:21:38.728 | MS1 | 121.4656730715 | 31.1446367031 | 855 | 504990 | -85.56 | 1.04 | 90.59 | 0.20 | 1.47 | 1560 |
| 2024-09-20 22:21:39.767 | MS1 | 121.4656613405 | 31.1446216607 | 855 | 504990 | -85.60 | 1.41 | 47.06 | 0.17 | 1.43 | 1571 |
| 2024-09-20 22:21:40.314 | MS1 | 121.4656755379 | 31.1446257325 | 855 | 504990 | -82.57 | 17.92 | 475.17 | 0.04 | 2.27 | 1580 |
| 2024-09-20 22:21:41.483 | MS1 | 121.4656628773 | 31.1446229921 | 855 | 504990 | -83.43 | 15.99 | 599.04 | 0.07 | 2.67 | 1586 |
| 2024-09-20 22:21:42.736 | MS1 | 121.4656598464 | 31.1446210239 | 855 | 504990 | -78.26 | 15.52 | 295.19 | 0.12 | 2.88 | 1562 |

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
| 3233199 | 2 | 121.4757505538 | 31.1552162881 | 236 | 2 | 12 | 28.1 | TDD | 855 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3242073 | 4 | 121.4740144503 | 31.1551761771 | 171 | 9 | 8 | 39.1 | TDD | 415 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3258071 | 1 | 121.4715410972 | 31.1521281055 | 226 | 4 | 5 | 18.7 | TDD | 481 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3269995 | 3 | 121.4713939208 | 31.1454446439 | 345 | 3 | 5 | 41.3 | TDD | 265 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.274 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.290 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.390 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.390 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258071 | 1 | 16.1309 | 16.4885 | -117.2352 | 16.3963 | 185.2934 | 0.0064 | 0.0023 |
| 2024_09_20 22:00 | 3233199 | 2 | 11.8957 | 8.3234 | -108.4778 | 17.9157 | 179.6785 | 0.0050 | 0.0134 |
| 2024_09_20 22:00 | 3269995 | 3 | 7.5823 | 11.8013 | -117.2674 | 17.1484 | 93.9626 | 0.0168 | 0.0020 |
| 2024_09_20 22:00 | 3242073 | 4 | 15.9273 | 18.7772 | -117.1758 | 11.6554 | 141.6726 | 0.0035 | 0.0110 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414115_8B04CC60 | 504990 | 481 | -90.3 | 504990 | 855 | -86.6 | 504990 | 265 | -87.6 | 504990 | 415 |
| MR_1774414115_4EFCE4FA | 504990 | 481 | -87.9 | 504990 | 855 | -85.2 | 504990 | 265 | -86.1 | 504990 | 415 |
| MR_1774414115_17401CF0 | 504990 | 855 | -90.3 | 504990 | 481 | -88.1 | 504990 | 265 | -88.6 | 504990 | 415 |
| MR_1774414115_A90DAAD2 | 504990 | 855 | -87.6 | 504990 | 481 | -88.2 | 504990 | 265 | -88.3 | 504990 | 415 |
| MR_1774414115_74956FEA | 504990 | 481 | -90.5 | 504990 | 855 | -87.0 | 504990 | 265 | -86.6 | 504990 | 415 |
| MR_1774414115_344FDF7A | 504990 | 481 | -90.2 | 504990 | 855 | -88.0 | 504990 | 265 | -89.2 | 504990 | 415 |
| MR_1774414115_2CBADC8B | 504990 | 481 | -90.2 | 504990 | 855 | -87.4 | 504990 | 265 | -87.7 | 504990 | 415 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 817: `4694a279-62f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4694a279-62f4-4d99-8eb3-83488bd667ba` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Lift the tilt angle  of 3264152_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[817] topology](images/train_0817.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3271161_3
- `C2`: Lift the tilt angle  of 3264152_4 by 10 degrees **← 정답**
- `C3`: Increase transmission power for 3268837_2
- `C4`: Increase A3 Offset threshold for 3268837_2
- `C5`: Increase A3 Offset threshold for 3271161_3
- `C6`: Adjust the azimuth of 3271161_3 by 21 degrees
- `C7`: Lift the tilt angle of 3271161_3 by 5 degrees
- `C8`: Increase transmission power for 3271161_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268837_2
- `C10`: Decrease A3 Offset threshold for 3268837_2
- `C11`: Press down the tilt angle  of 3264152_4 by 10 degrees
- `C12`: Press down the tilt angle of 3271161_3 by 5 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271161_3
- `C14`: Check test server and transmission issues
- `C15`: Add neighbor relationship between 3271161_3 and 3268837_2
- `C16`: Decrease A3 Offset threshold for 3271161_3
- `C17`: Decrease transmission power for 3268837_2
- `C18`: Adjust the azimuth of 3264152_4 by 50 degrees
- `C19`: Add neighbor relationship between 3264152_4 and 3268837_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268837_2
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271161_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.863 | MS1 | 121.4656706467 | 31.1446260493 | 4 | 504990 | -88.85 | 15.30 | 315.99 | 0.04 | 2.21 | 1597 |
| 2024-09-20 22:21:32.293 | MS1 | 121.4656669789 | 31.1446368216 | 4 | 504990 | -89.06 | 14.91 | 513.98 | 0.12 | 2.17 | 1569 |
| 2024-09-20 22:21:33.466 | MS1 | 121.4656639271 | 31.1446271448 | 4 | 504990 | -87.00 | 15.93 | 329.10 | 0.19 | 2.95 | 1590 |
| 2024-09-20 22:21:34.491 | MS1 | 121.4656746032 | 31.1446261039 | 4 | 504990 | -89.33 | 15.50 | 44.80 | 0.14 | 2.53 | 1563 |
| 2024-09-20 22:21:35.905 | MS1 | 121.4656745130 | 31.1446182140 | 4 | 504990 | -88.78 | 12.48 | 77.56 | 0.15 | 2.79 | 1588 |
| 2024-09-20 22:21:36.515 | MS1 | 121.4656745934 | 31.1446271153 | 4 | 504990 | -87.38 | 15.09 | 71.86 | 0.02 | 2.92 | 1579 |
| 2024-09-20 22:21:37.232 | MS1 | 121.4656737695 | 31.1446364595 | 4 | 504990 | -92.55 | 10.87 | 71.83 | 0.12 | 2.18 | 1586 |
| 2024-09-20 22:21:38.261 | MS1 | 121.4656622255 | 31.1446322010 | 4 | 504990 | -91.85 | 11.03 | 73.47 | 0.08 | 2.12 | 1576 |
| 2024-09-20 22:21:39.780 | MS1 | 121.4656629511 | 31.1446247707 | 4 | 504990 | -90.15 | 10.02 | 89.03 | 0.15 | 2.34 | 1586 |
| 2024-09-20 22:21:40.384 | MS1 | 121.4656683558 | 31.1446320711 | 4 | 504990 | -92.54 | 11.59 | 355.19 | 0.17 | 2.41 | 1568 |
| 2024-09-20 22:21:41.515 | MS1 | 121.4656610268 | 31.1446278835 | 4 | 504990 | -92.79 | 11.09 | 308.90 | 0.19 | 2.54 | 1600 |
| 2024-09-20 22:21:42.603 | MS1 | 121.4656672189 | 31.1446223070 | 4 | 504990 | -91.80 | 9.44 | 471.09 | 0.19 | 2.74 | 1579 |

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
| 3244172 | 1 | 121.4684427424 | 31.1469827335 | 4 | 1 | 11 | 35.2 | TDD | 672 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3264152 | 4 | 121.4640676963 | 31.1468621090 | 55 | 7 | 9 | 19.8 | TDD | 207 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3268837 | 2 | 121.4754314262 | 31.1474190283 | 38 | 13 | 12 | 18.8 | TDD | 955 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3271161 | 3 | 121.4705315726 | 31.1550722454 | 223 | 4 | 6 | 19.9 | TDD | 4 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.555 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.579 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.716 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.716 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.397 | NREventA3 | measId:2;ServCellPCI:38;Ser... |
| 2024-09-20 22:21:38.637 | NRHandoverAttempt | SourcePCI:38;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.681 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.694 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.841 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.841 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244172 | 1 | 17.0257 | 18.8039 | -114.5060 | 17.9710 | 90.9923 | 0.0116 | 0.0168 |
| 2024_09_20 22:00 | 3268837 | 2 | 13.6770 | 10.8109 | -115.0819 | 6.5869 | 142.3384 | 0.0126 | 0.0101 |
| 2024_09_20 22:00 | 3271161 | 3 | 79.8306 | 78.8401 | -115.1302 | 11.5977 | 141.8483 | 0.0160 | 0.0182 |
| 2024_09_20 22:00 | 3264152 | 4 | 14.5383 | 5.7655 | -117.6886 | 16.7248 | 138.0385 | 0.0157 | 0.0105 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415940_0884374C | 504990 | 4 | -88.3 | 504990 | 955 | -97.5 | 504990 | 207 | -101.8 | 504990 | 672 |
| MR_1774415940_4F60548B | 504990 | 4 | -88.5 | 504990 | 955 | -98.2 | 504990 | 207 | -101.1 | 504990 | 672 |
| MR_1774415940_0E2EF195 | 504990 | 4 | -87.4 | 504990 | 955 | -99.4 | 504990 | 207 | -102.3 | 504990 | 672 |
| MR_1774415940_CCE5F791 | 504990 | 4 | -88.0 | 504990 | 955 | -97.8 | 504990 | 207 | -102.5 | 504990 | 672 |
| MR_1774415940_42F94D3C | 504990 | 4 | -88.2 | 504990 | 955 | -98.5 | 504990 | 207 | -102.2 | 504990 | 672 |
| MR_1774415940_A753403A | 504990 | 4 | -89.9 | 504990 | 955 | -99.9 | 504990 | 207 | -102.4 | 504990 | 672 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 818: `01f99e5f-6a0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `01f99e5f-6a09-4a18-8d39-60c8b9cb1171` |
| Tag | **multiple-answer** |
| 정답 | **C2|C3** |
| C2 의미 | Adjust the azimuth of 3260495_3 by 50 degrees |
| C3 의미 | Increase transmission power for 3260495_3 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[818] topology](images/train_0818.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3278524_2 by 5 degrees
- `C2`: Adjust the azimuth of 3260495_3 by 50 degrees **← 정답**
- `C3`: Increase transmission power for 3260495_3 **← 정답**
- `C4`: Lift the tilt angle of 3260495_3 by 10 degrees
- `C5`: Lift the tilt angle  of 3278524_2 by 5 degrees
- `C6`: Decrease A3 Offset threshold for 3260495_3
- `C7`: Increase A3 Offset threshold for 3278524_2
- `C8`: Press down the tilt angle of 3260495_3 by 10 degrees
- `C9`: Decrease transmission power for 3278524_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260495_3
- `C11`: Check test server and transmission issues
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278524_2
- `C13`: Increase A3 Offset threshold for 3260495_3
- `C14`: Decrease transmission power for 3260495_3
- `C15`: Decrease A3 Offset threshold for 3278524_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278524_2
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Add neighbor relationship between 3260495_3 and 3278524_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260495_3
- `C20`: Adjust the azimuth of 3278524_2 by 30 degrees
- `C21`: Increase transmission power for 3278524_2
- `C22`: Add neighbor relationship between 3265299_4 and 3278524_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.901 | MS1 | 121.4656628795 | 31.1446291679 | 643 | 504990 | -85.06 | 17.18 | 530.75 | 0.19 | 2.52 | 1586 |
| 2024-09-20 22:21:32.547 | MS1 | 121.4656702805 | 31.1446348319 | 643 | 504990 | -85.30 | 14.58 | 413.85 | 0.08 | 2.98 | 1576 |
| 2024-09-20 22:21:33.482 | MS1 | 121.4656750462 | 31.1446217228 | 643 | 504990 | -89.64 | 17.03 | 464.59 | 0.11 | 2.80 | 1580 |
| 2024-09-20 22:21:34.712 | MS1 | 121.4656688954 | 31.1446225361 | 643 | 504990 | -108.92 | -1.22 | 75.39 | 0.17 | 1.18 | 1574 |
| 2024-09-20 22:21:35.914 | MS1 | 121.4656639626 | 31.1446231973 | 643 | 504990 | -105.06 | 0.65 | 25.06 | 0.13 | 1.32 | 1592 |
| 2024-09-20 22:21:36.300 | MS1 | 121.4656619058 | 31.1446291200 | 643 | 504990 | -108.89 | -0.76 | 60.29 | 0.13 | 1.40 | 1576 |
| 2024-09-20 22:21:37.276 | MS1 | 121.4656683092 | 31.1446308702 | 643 | 504990 | -104.26 | 0.58 | 61.51 | 0.15 | 1.46 | 1597 |
| 2024-09-20 22:21:38.453 | MS1 | 121.4656730453 | 31.1446257294 | 643 | 504990 | -106.23 | 0.64 | 54.06 | 0.12 | 1.00 | 1595 |
| 2024-09-20 22:21:39.227 | MS1 | 121.4656719321 | 31.1446189008 | 643 | 504990 | -109.99 | 1.40 | 31.36 | 0.00 | 1.44 | 1590 |
| 2024-09-20 22:21:40.234 | MS1 | 121.4656716531 | 31.1446232240 | 643 | 504990 | -88.06 | 16.50 | 381.01 | 0.11 | 2.02 | 1599 |
| 2024-09-20 22:21:41.525 | MS1 | 121.4656705412 | 31.1446186790 | 643 | 504990 | -90.25 | 15.51 | 481.52 | 0.05 | 2.13 | 1581 |
| 2024-09-20 22:21:42.415 | MS1 | 121.4656710932 | 31.1446211954 | 643 | 504990 | -87.06 | 15.37 | 459.97 | 0.00 | 2.89 | 1594 |

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
| 3260495 | 3 | 121.4664647022 | 31.1482225843 | 116 | 6 | 12 | 37.9 | TDD | 643 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3265299 | 4 | 121.4678050493 | 31.1555620871 | 267 | 3 | 1 | 20.8 | TDD | 765 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3278524 | 2 | 121.4748894832 | 31.1472299100 | 282 | 3 | 10 | 32.8 | TDD | 402 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3278669 | 1 | 121.4715447344 | 31.1446765660 | 147 | 5 | 5 | 18.9 | TDD | 1000 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.595 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.702 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.702 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.946 | NREventA2 | measId:1;ServCellPCI:754;Se... |
| 2024-09-20 22:21:35.058 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278669 | 1 | 17.5199 | 7.3969 | -117.0001 | 11.9912 | 197.1703 | 0.0033 | 0.0036 |
| 2024_09_20 22:00 | 3278524 | 2 | 15.5484 | 7.3777 | -116.3040 | 15.2480 | 188.0790 | 0.0031 | 0.0004 |
| 2024_09_20 22:00 | 3260495 | 3 | 5.3661 | 17.9191 | -117.5360 | 16.2959 | 122.0113 | 0.1101 | 0.0174 |
| 2024_09_20 22:00 | 3265299 | 4 | 7.8315 | 12.3085 | -114.0661 | 13.4596 | 107.8103 | 0.0108 | 0.0178 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413496_2B820083 | 504990 | 643 | -110.9 | 504990 | 402 | -114.1 | 504990 | 765 | -121.1 | 504990 | 1000 |
| MR_1774413496_7207BA7E | 504990 | 643 | -110.9 | 504990 | 402 | -113.0 | 504990 | 765 | -120.7 | 504990 | 1000 |
| MR_1774413496_3538616D | 504990 | 643 | -110.4 | 504990 | 402 | -113.1 | 504990 | 765 | -117.5 | 504990 | 1000 |
| MR_1774413496_4494ABC3 | 504990 | 643 | -107.0 | 504990 | 402 | -114.6 | 504990 | 765 | -118.9 | 504990 | 1000 |
| MR_1774413496_5F32B4C9 | 504990 | 643 | -107.0 | 504990 | 402 | -113.6 | 504990 | 765 | -121.1 | 504990 | 1000 |
| MR_1774413496_5EA34076 | 504990 | 643 | -110.8 | 504990 | 402 | -112.6 | 504990 | 765 | -119.2 | 504990 | 1000 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 819: `239d4c76-163...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `239d4c76-163d-4f07-b354-df3edd1ae8e3` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Lift the tilt angle  of 3264667_3 by 4 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[819] topology](images/train_0819.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3241707_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229781_2
- `C3`: Press down the tilt angle  of 3264667_3 by 4 degrees
- `C4`: Increase A3 Offset threshold for 3241707_1
- `C5`: Increase A3 Offset threshold for 3229781_2
- `C6`: Press down the tilt angle of 3229781_2 by 6 degrees
- `C7`: Lift the tilt angle of 3229781_2 by 6 degrees
- `C8`: Add neighbor relationship between 3264667_3 and 3241707_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229781_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Adjust the azimuth of 3264667_3 by 50 degrees
- `C12`: Check test server and transmission issues
- `C13`: Decrease A3 Offset threshold for 3229781_2
- `C14`: Lift the tilt angle  of 3264667_3 by 4 degrees **← 정답**
- `C15`: Increase transmission power for 3241707_1
- `C16`: Add neighbor relationship between 3229781_2 and 3241707_1
- `C17`: Decrease transmission power for 3229781_2
- `C18`: Decrease transmission power for 3241707_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241707_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241707_1
- `C21`: Adjust the azimuth of 3229781_2 by 26 degrees
- `C22`: Increase transmission power for 3229781_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.660 | MS1 | 121.4656673362 | 31.1446257222 | 267 | 504990 | -91.35 | 16.58 | 532.90 | 0.01 | 2.51 | 1586 |
| 2024-09-20 22:21:32.460 | MS1 | 121.4656611873 | 31.1446249005 | 267 | 504990 | -86.54 | 13.07 | 573.16 | 0.14 | 2.37 | 1579 |
| 2024-09-20 22:21:33.336 | MS1 | 121.4656620954 | 31.1446216899 | 267 | 504990 | -87.06 | 12.83 | 506.78 | 0.02 | 2.80 | 1597 |
| 2024-09-20 22:21:34.435 | MS1 | 121.4656710225 | 31.1446258432 | 267 | 504990 | -87.74 | 13.16 | 87.30 | 0.16 | 2.98 | 1575 |
| 2024-09-20 22:21:35.282 | MS1 | 121.4656779695 | 31.1446328831 | 267 | 504990 | -90.81 | 16.90 | 57.47 | 0.14 | 2.93 | 1572 |
| 2024-09-20 22:21:36.844 | MS1 | 121.4656696646 | 31.1446348556 | 267 | 504990 | -87.10 | 13.73 | 57.43 | 0.02 | 2.79 | 1586 |
| 2024-09-20 22:21:37.349 | MS1 | 121.4656584436 | 31.1446196977 | 267 | 504990 | -89.22 | 9.69 | 68.68 | 0.16 | 2.84 | 1597 |
| 2024-09-20 22:21:38.931 | MS1 | 121.4656633131 | 31.1446342054 | 267 | 504990 | -90.67 | 10.74 | 68.00 | 0.02 | 2.86 | 1598 |
| 2024-09-20 22:21:39.452 | MS1 | 121.4656740445 | 31.1446217040 | 267 | 504990 | -92.57 | 11.50 | 86.93 | 0.12 | 2.85 | 1562 |
| 2024-09-20 22:21:40.905 | MS1 | 121.4656624748 | 31.1446273976 | 267 | 504990 | -90.50 | 7.96 | 335.13 | 0.18 | 2.54 | 1598 |
| 2024-09-20 22:21:41.806 | MS1 | 121.4656755828 | 31.1446377083 | 267 | 504990 | -90.25 | 11.75 | 364.31 | 0.19 | 2.60 | 1561 |
| 2024-09-20 22:21:42.771 | MS1 | 121.4656589716 | 31.1446299223 | 267 | 504990 | -92.40 | 11.40 | 311.08 | 0.11 | 2.23 | 1572 |

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
| 3224076 | 4 | 121.4716519023 | 31.1499439588 | 200 | 14 | 2 | 42.8 | TDD | 553 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3229781 | 2 | 121.4688537817 | 31.1528822941 | 172 | 4 | 9 | 33.6 | TDD | 267 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3241707 | 1 | 121.4701474535 | 31.1533467043 | 305 | 3 | 1 | 20.9 | TDD | 289 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3264667 | 3 | 121.4642740165 | 31.1471384372 | 348 | 9 | 3 | 24.1 | TDD | 980 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.679 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.702 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.804 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.804 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.480 | NREventA3 | measId:2;ServCellPCI:538;Se... |
| 2024-09-20 22:21:38.720 | NRHandoverAttempt | SourcePCI:538;SourceNR-ARFC... |
| 2024-09-20 22:21:38.766 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.781 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.892 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.892 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241707 | 1 | 19.5021 | 13.2242 | -117.5518 | 17.4333 | 105.5093 | 0.0135 | 0.0035 |
| 2024_09_20 22:00 | 3229781 | 2 | 93.8755 | 91.6445 | -115.2225 | 7.3422 | 144.0239 | 0.0101 | 0.0084 |
| 2024_09_20 22:00 | 3264667 | 3 | 10.2314 | 13.8813 | -114.1059 | 17.9803 | 133.8692 | 0.0012 | 0.0094 |
| 2024_09_20 22:00 | 3224076 | 4 | 18.1666 | 10.0586 | -115.0609 | 16.4990 | 177.5202 | 0.0088 | 0.0030 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411992_AECDA35B | 504990 | 267 | -86.8 | 504990 | 289 | -93.3 | 504990 | 980 | -95.9 | 504990 | 553 |
| MR_1774411992_13656D32 | 504990 | 267 | -89.6 | 504990 | 289 | -95.1 | 504990 | 980 | -98.2 | 504990 | 553 |
| MR_1774411992_E808B1FA | 504990 | 267 | -89.6 | 504990 | 289 | -94.6 | 504990 | 980 | -97.4 | 504990 | 553 |
| MR_1774411992_608A2F04 | 504990 | 267 | -86.7 | 504990 | 289 | -93.5 | 504990 | 980 | -96.4 | 504990 | 553 |
| MR_1774411992_D391CF30 | 504990 | 267 | -86.6 | 504990 | 289 | -93.7 | 504990 | 980 | -95.2 | 504990 | 553 |
| MR_1774411992_D6F69842 | 504990 | 267 | -89.1 | 504990 | 289 | -95.2 | 504990 | 980 | -97.8 | 504990 | 553 |
| MR_1774411992_1A57BCA8 | 504990 | 267 | -87.4 | 504990 | 289 | -95.8 | 504990 | 980 | -98.1 | 504990 | 553 |

> *... 2개 열 생략 (전체 14열)*

---
