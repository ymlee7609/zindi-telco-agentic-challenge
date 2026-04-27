# Track A 문제 분석 — test[370]~test[379]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[370] ~ test[379] (10개)

## 목차

1. [문제 370: `5e1fcdd2-93f...`](#370) — single-answer
2. [문제 371: `ac75112c-b99...`](#371) — single-answer
3. [문제 372: `87b4d91d-d25...`](#372) — multiple-answer
4. [문제 373: `3aaf006c-159...`](#373) — single-answer
5. [문제 374: `122ed1ed-155...`](#374) — single-answer
6. [문제 375: `469f3384-ec8...`](#375) — single-answer
7. [문제 376: `5efefb61-041...`](#376) — multiple-answer
8. [문제 377: `9e483a6b-b7c...`](#377) — single-answer
9. [문제 378: `5a677dca-8d7...`](#378) — single-answer
10. [문제 379: `8349aaea-ebe...`](#379) — single-answer

---

### 문제 370: `5e1fcdd2-93f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5e1fcdd2-93f9-4d95-94b1-11984382157b` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[370] topology](images/test_0370.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3246483_3 and 3274438_1
- `C2`: Decrease transmission power for 3246483_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246483_3
- `C4`: Lift the tilt angle of 3246483_3 by 10 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246483_3
- `C6`: Increase A3 Offset threshold for 3246483_3
- `C7`: Increase A3 Offset threshold for 3274438_1
- `C8`: Add neighbor relationship between 3258095_4 and 3274438_1
- `C9`: Increase transmission power for 3274438_1
- `C10`: Press down the tilt angle of 3246483_3 by 10 degrees
- `C11`: Increase transmission power for 3246483_3
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease transmission power for 3274438_1
- `C14`: Press down the tilt angle  of 3274438_1 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3274438_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274438_1
- `C17`: Decrease A3 Offset threshold for 3246483_3
- `C18`: Lift the tilt angle  of 3274438_1 by 10 degrees
- `C19`: Adjust the azimuth of 3274438_1 by 50 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274438_1
- `C21`: Check test server and transmission issues
- `C22`: Adjust the azimuth of 3246483_3 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.775 | MS1 | 121.4656667557 | 31.1446374303 | 782 | 504990 | -89.87 | 16.95 | 305.13 | 0.05 | 2.50 | 1567 |
| 2024-09-20 22:21:32.351 | MS1 | 121.4656654661 | 31.1446318271 | 782 | 504990 | -86.38 | 14.54 | 564.81 | 0.16 | 2.15 | 1568 |
| 2024-09-20 22:21:33.688 | MS1 | 121.4656642512 | 31.1446312942 | 782 | 504990 | -91.15 | 15.83 | 294.41 | 0.14 | 2.95 | 1594 |
| 2024-09-20 22:21:34.262 | MS1 | 121.4656654376 | 31.1446183212 | 782 | 504990 | -90.76 | 13.72 | 97.72 | 0.02 | 2.31 | 339 |
| 2024-09-20 22:21:35.597 | MS1 | 121.4656597630 | 31.1446204759 | 782 | 504990 | -87.32 | 16.95 | 64.93 | 0.15 | 2.16 | 393 |
| 2024-09-20 22:21:36.333 | MS1 | 121.4656752508 | 31.1446239628 | 782 | 504990 | -89.29 | 13.61 | 87.83 | 0.09 | 2.60 | 312 |
| 2024-09-20 22:21:37.569 | MS1 | 121.4656779942 | 31.1446246430 | 782 | 504990 | -90.79 | 7.21 | 57.41 | 0.20 | 2.54 | 413 |
| 2024-09-20 22:21:38.430 | MS1 | 121.4656710019 | 31.1446369055 | 782 | 504990 | -91.96 | 11.89 | 79.69 | 0.00 | 2.79 | 487 |
| 2024-09-20 22:21:39.588 | MS1 | 121.4656747882 | 31.1446289799 | 782 | 504990 | -90.65 | 11.75 | 53.09 | 0.11 | 2.38 | 429 |
| 2024-09-20 22:21:40.100 | MS1 | 121.4656699176 | 31.1446358810 | 782 | 504990 | -91.26 | 9.86 | 510.56 | 0.05 | 2.13 | 1561 |
| 2024-09-20 22:21:41.584 | MS1 | 121.4656672629 | 31.1446180211 | 782 | 504990 | -90.42 | 8.45 | 497.59 | 0.01 | 2.27 | 1588 |
| 2024-09-20 22:21:42.962 | MS1 | 121.4656692808 | 31.1446336400 | 782 | 504990 | -89.43 | 9.83 | 602.73 | 0.06 | 2.62 | 1587 |

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
| 3246483 | 3 | 121.4668168001 | 31.1453306185 | 117 | 11 | 5 | 18.1 | TDD | 782 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3258095 | 4 | 121.4663383794 | 31.1540835342 | 309 | 2 | 11 | 42.6 | TDD | 343 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3261012 | 2 | 121.4747309876 | 31.1479553134 | 9 | 12 | 0 | 28.9 | TDD | 13 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3274438 | 1 | 121.4738476641 | 31.1507880261 | 327 | 14 | 9 | 45.3 | TDD | 290 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.995 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.018 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.118 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.118 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.837 | NREventA3 | measId:2;ServCellPCI:164;Se... |
| 2024-09-20 22:21:38.077 | NRHandoverAttempt | SourcePCI:164;SourceNR-ARFC... |
| 2024-09-20 22:21:38.124 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.138 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.288 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.288 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274438 | 1 | 19.8814 | 12.2864 | -114.8518 | 17.4003 | 110.4929 | 0.0121 | 0.0019 |
| 2024_09_20 22:00 | 3261012 | 2 | 16.8671 | 10.8278 | -114.1171 | 16.8477 | 117.1717 | 0.0171 | 0.0142 |
| 2024_09_20 22:00 | 3246483 | 3 | 5.3498 | 10.2497 | -117.0462 | 6.8699 | 146.0382 | 0.0187 | 0.0166 |
| 2024_09_20 22:00 | 3258095 | 4 | 11.0881 | 16.1827 | -114.5017 | 19.5621 | 182.3239 | 0.0129 | 0.0079 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414165_6F9D73C9 | 504990 | 782 | -91.1 | 504990 | 290 | -98.6 | 504990 | 343 | -103.4 | 504990 | 13 |
| MR_1774414165_431BB92E | 504990 | 782 | -90.5 | 504990 | 290 | -99.4 | 504990 | 343 | -104.9 | 504990 | 13 |
| MR_1774414165_7A430DFA | 504990 | 782 | -89.0 | 504990 | 290 | -101.8 | 504990 | 343 | -105.8 | 504990 | 13 |
| MR_1774414165_9DB153A5 | 504990 | 782 | -89.4 | 504990 | 290 | -98.8 | 504990 | 343 | -103.0 | 504990 | 13 |
| MR_1774414165_207855EF | 504990 | 782 | -89.3 | 504990 | 290 | -99.9 | 504990 | 343 | -106.0 | 504990 | 13 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 371: `ac75112c-b99...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ac75112c-b997-437e-8619-bf142281c12e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[371] topology](images/test_0371.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3247857_1 by 50 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247857_1
- `C4`: Decrease transmission power for 3223602_4
- `C5`: Increase transmission power for 3223602_4
- `C6`: Decrease A3 Offset threshold for 3223602_4
- `C7`: Adjust the azimuth of 3223602_4 by 13 degrees
- `C8`: Decrease transmission power for 3247857_1
- `C9`: Press down the tilt angle  of 3247857_1 by 10 degrees
- `C10`: Check test server and transmission issues
- `C11`: Add neighbor relationship between 3223602_4 and 3247857_1
- `C12`: Increase A3 Offset threshold for 3247857_1
- `C13`: Add neighbor relationship between 3242965_3 and 3247857_1
- `C14`: Lift the tilt angle  of 3247857_1 by 10 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223602_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223602_4
- `C17`: Increase transmission power for 3247857_1
- `C18`: Press down the tilt angle of 3223602_4 by 7 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247857_1
- `C20`: Decrease A3 Offset threshold for 3247857_1
- `C21`: Increase A3 Offset threshold for 3223602_4
- `C22`: Lift the tilt angle of 3223602_4 by 7 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.738 | MS1 | 121.4656718947 | 31.1446361065 | 679 | 504990 | -91.53 | 15.92 | 370.18 | 0.18 | 2.42 | 1568 |
| 2024-09-20 22:21:32.355 | MS1 | 121.4656685777 | 31.1446288197 | 679 | 504990 | -86.56 | 14.13 | 452.54 | 0.19 | 2.29 | 1572 |
| 2024-09-20 22:21:33.922 | MS1 | 121.4656774442 | 31.1446234130 | 679 | 504990 | -88.26 | 17.06 | 374.26 | 0.16 | 2.13 | 1583 |
| 2024-09-20 22:21:34.140 | MS1 | 121.4656622979 | 31.1446222993 | 679 | 504990 | -91.74 | 12.03 | 70.93 | 0.02 | 2.42 | 449 |
| 2024-09-20 22:21:35.767 | MS1 | 121.4656681392 | 31.1446364313 | 679 | 504990 | -90.20 | 12.39 | 94.20 | 0.07 | 2.46 | 460 |
| 2024-09-20 22:21:36.620 | MS1 | 121.4656763946 | 31.1446283612 | 679 | 504990 | -91.39 | 16.79 | 90.03 | 0.01 | 2.77 | 431 |
| 2024-09-20 22:21:37.364 | MS1 | 121.4656701425 | 31.1446360030 | 679 | 504990 | -89.10 | 8.02 | 72.81 | 0.19 | 2.87 | 309 |
| 2024-09-20 22:21:38.103 | MS1 | 121.4656601767 | 31.1446225716 | 679 | 504990 | -91.79 | 12.99 | 82.01 | 0.05 | 2.95 | 363 |
| 2024-09-20 22:21:39.228 | MS1 | 121.4656756292 | 31.1446377444 | 679 | 504990 | -90.14 | 10.94 | 73.10 | 0.07 | 2.90 | 499 |
| 2024-09-20 22:21:40.806 | MS1 | 121.4656589959 | 31.1446338054 | 679 | 504990 | -93.54 | 8.34 | 583.36 | 0.19 | 2.94 | 1567 |
| 2024-09-20 22:21:41.183 | MS1 | 121.4656770249 | 31.1446236846 | 679 | 504990 | -89.55 | 9.54 | 447.81 | 0.07 | 2.51 | 1561 |
| 2024-09-20 22:21:42.753 | MS1 | 121.4656678691 | 31.1446223769 | 679 | 504990 | -89.52 | 8.36 | 607.15 | 0.09 | 2.37 | 1561 |

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
| 3223602 | 4 | 121.4675169805 | 31.1554454419 | 201 | 5 | 9 | 40.2 | TDD | 679 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3224044 | 2 | 121.4708739471 | 31.1475940194 | 298 | 6 | 8 | 37.4 | TDD | 290 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3242965 | 3 | 121.4657613257 | 31.1551124643 | 164 | 11 | 12 | 15.7 | TDD | 771 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3247857 | 1 | 121.4724734848 | 31.1547571763 | 357 | 12 | 2 | 23.1 | TDD | 785 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.744 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.762 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.874 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.874 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.644 | NREventA3 | measId:2;ServCellPCI:123;Se... |
| 2024-09-20 22:21:37.884 | NRHandoverAttempt | SourcePCI:123;SourceNR-ARFC... |
| 2024-09-20 22:21:37.916 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.930 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.050 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.050 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247857 | 1 | 7.4633 | 8.0327 | -117.4548 | 12.0251 | 189.9845 | 0.0195 | 0.0011 |
| 2024_09_20 22:00 | 3224044 | 2 | 5.3579 | 5.6450 | -115.2891 | 10.3623 | 104.9646 | 0.0052 | 0.0114 |
| 2024_09_20 22:00 | 3242965 | 3 | 13.8189 | 18.9743 | -117.2615 | 8.9758 | 189.3530 | 0.0024 | 0.0005 |
| 2024_09_20 22:00 | 3223602 | 4 | 5.4306 | 17.6404 | -114.6047 | 19.1819 | 152.2854 | 0.0188 | 0.0084 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416132_888BC1AB | 504990 | 679 | -91.9 | 504990 | 785 | -97.5 | 504990 | 771 | -106.3 | 504990 | 290 |
| MR_1774416132_6DD2B0F8 | 504990 | 679 | -92.6 | 504990 | 785 | -97.5 | 504990 | 771 | -105.0 | 504990 | 290 |
| MR_1774416132_8455BBC9 | 504990 | 679 | -93.2 | 504990 | 785 | -95.9 | 504990 | 771 | -107.9 | 504990 | 290 |
| MR_1774416132_54EA1976 | 504990 | 679 | -92.6 | 504990 | 785 | -98.0 | 504990 | 771 | -105.4 | 504990 | 290 |
| MR_1774416132_055F07E7 | 504990 | 679 | -92.8 | 504990 | 785 | -98.7 | 504990 | 771 | -107.0 | 504990 | 290 |
| MR_1774416132_8198757D | 504990 | 679 | -92.5 | 504990 | 785 | -98.2 | 504990 | 771 | -104.9 | 504990 | 290 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 372: `87b4d91d-d25...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `87b4d91d-d25d-46a9-92a8-1bcdba6226cf` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[372] topology](images/test_0372.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3258582_2 by 3 degrees
- `C2`: Decrease A3 Offset threshold for 3262050_5
- `C3`: Increase transmission power for 3258582_2
- `C4`: Add neighbor relationship between 3257712_1 and 3258582_2
- `C5`: Adjust the azimuth of 3262050_5 by 26 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Lift the tilt angle of 3262050_5 by 3 degrees
- `C8`: Press down the tilt angle of 3262050_5 by 3 degrees
- `C9`: Press down the tilt angle  of 3258582_2 by 3 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258582_2
- `C11`: Check test server and transmission issues
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258582_2
- `C13`: Decrease transmission power for 3258582_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262050_5
- `C15`: Decrease A3 Offset threshold for 3258582_2
- `C16`: Decrease transmission power for 3262050_5
- `C17`: Increase A3 Offset threshold for 3262050_5
- `C18`: Add neighbor relationship between 3262050_5 and 3258582_2
- `C19`: Increase A3 Offset threshold for 3258582_2
- `C20`: Adjust the azimuth of 3258582_2 by 4 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262050_5
- `C22`: Increase transmission power for 3262050_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.701 | MS1 | 121.4656748525 | 31.1446316436 | 158 | 504990 | -75.96 | 14.56 | 490.01 | 0.07 | 2.34 | 1586 |
| 2024-09-20 22:21:32.397 | MS1 | 121.4656769448 | 31.1446221883 | 158 | 504990 | -77.79 | 17.84 | 585.31 | 0.05 | 2.09 | 1577 |
| 2024-09-20 22:21:33.989 | MS1 | 121.4656584021 | 31.1446200934 | 158 | 504990 | -83.73 | 12.68 | 349.45 | 0.05 | 2.92 | 1563 |
| 2024-09-20 22:21:34.916 | MS1 | 121.4656744437 | 31.1446370195 | 630 | 504990 | -85.42 | 1.02 | 48.51 | 0.10 | 1.24 | 1578 |
| 2024-09-20 22:21:35.117 | MS1 | 121.4656687099 | 31.1446286758 | 630 | 504990 | -84.70 | 2.34 | 29.40 | 0.18 | 1.25 | 1590 |
| 2024-09-20 22:21:36.735 | MS1 | 121.4656602713 | 31.1446330865 | 158 | 504990 | -80.04 | 2.65 | 66.91 | 0.14 | 1.41 | 1584 |
| 2024-09-20 22:21:37.737 | MS1 | 121.4656707194 | 31.1446302568 | 158 | 504990 | -81.71 | 3.42 | 60.16 | 0.10 | 1.41 | 1587 |
| 2024-09-20 22:21:38.712 | MS1 | 121.4656636113 | 31.1446227005 | 630 | 504990 | -86.96 | 4.34 | 62.66 | 0.01 | 1.14 | 1586 |
| 2024-09-20 22:21:39.979 | MS1 | 121.4656648235 | 31.1446364393 | 630 | 504990 | -87.12 | 3.37 | 27.48 | 0.00 | 1.27 | 1595 |
| 2024-09-20 22:21:40.517 | MS1 | 121.4656619485 | 31.1446191954 | 630 | 504990 | -75.07 | 13.07 | 450.24 | 0.17 | 2.01 | 1568 |
| 2024-09-20 22:21:41.608 | MS1 | 121.4656744516 | 31.1446183589 | 630 | 504990 | -77.71 | 15.12 | 551.75 | 0.02 | 2.83 | 1581 |
| 2024-09-20 22:21:42.691 | MS1 | 121.4656674799 | 31.1446186906 | 630 | 504990 | -81.85 | 16.36 | 551.07 | 0.04 | 2.07 | 1587 |

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
| 3220787 | 4 | 121.4663563945 | 31.1545332423 | 219 | 0 | 3 | 30.9 | TDD | 58 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3229910 | 3 | 121.4675287177 | 31.1462936952 | 221 | 0 | 7 | 23.7 | TDD | 630 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3257712 | 1 | 121.4668219598 | 31.1487385549 | 145 | 7 | 8 | 23.3 | TDD | 193 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3258582 | 2 | 121.4738680083 | 31.1559005951 | 208 | 2 | 1 | 17.8 | TDD | 932 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3262050 | 5 | 121.4694074622 | 31.1554061514 | 223 | 1 | 9 | 43.5 | TDD | 158 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.312 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.327 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.474 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.474 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.177 | NREventA3 | measId:2;ServCellPCI:71;Ser... |
| 2024-09-20 22:21:34.417 | NRHandoverAttempt | SourcePCI:71;SourceNR-ARFCN... |
| 2024-09-20 22:21:34.463 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.474 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:34.581 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.581 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.177 | NREventA3 | measId:2;ServCellPCI:886;Se... |
| 2024-09-20 22:21:36.417 | NRHandoverAttempt | SourcePCI:886;SourceNR-ARFC... |
| 2024-09-20 22:21:36.454 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.464 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:36.583 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.583 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.177 | NREventA3 | measId:2;ServCellPCI:71;Ser... |
| 2024-09-20 22:21:38.417 | NRHandoverAttempt | SourcePCI:71;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.450 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.464 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.576 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.576 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257712 | 1 | 12.6726 | 12.9039 | -114.2803 | 7.4526 | 123.4563 | 0.0095 | 0.0060 |
| 2024_09_20 22:00 | 3258582 | 2 | 16.0614 | 9.6328 | -115.1756 | 5.7260 | 184.7809 | 0.0182 | 0.0121 |
| 2024_09_20 22:00 | 3229910 | 3 | 16.1245 | 17.7310 | -114.9611 | 12.4250 | 137.5836 | 0.0069 | 0.0198 |
| 2024_09_20 22:00 | 3220787 | 4 | 11.9831 | 19.6430 | -116.4015 | 11.8354 | 154.0691 | 0.0015 | 0.0141 |
| 2024_09_20 22:00 | 3262050 | 5 | 16.3078 | 15.8426 | -114.2750 | 16.5624 | 100.0480 | 0.0077 | 0.0073 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414279_7C5F7B55 | 504990 | 158 | -84.1 | 504990 | 630 | -87.2 | 504990 | 932 | -86.6 | 504990 | 193 |
| MR_1774414279_84751D5E | 504990 | 630 | -87.2 | 504990 | 158 | -86.2 | 504990 | 932 | -84.8 | 504990 | 193 |
| MR_1774414279_A4DFB360 | 504990 | 630 | -84.7 | 504990 | 158 | -83.7 | 504990 | 932 | -83.9 | 504990 | 193 |
| MR_1774414279_7A453A5B | 504990 | 630 | -86.3 | 504990 | 158 | -86.8 | 504990 | 932 | -85.8 | 504990 | 193 |
| MR_1774414279_0DB05529 | 504990 | 158 | -86.6 | 504990 | 630 | -86.7 | 504990 | 932 | -83.9 | 504990 | 193 |
| MR_1774414279_611C390D | 504990 | 158 | -85.5 | 504990 | 630 | -87.2 | 504990 | 932 | -85.0 | 504990 | 193 |
| MR_1774414279_B6200BA8 | 504990 | 158 | -86.5 | 504990 | 630 | -86.0 | 504990 | 932 | -84.0 | 504990 | 193 |
| MR_1774414279_A8B5D7E0 | 504990 | 158 | -83.5 | 504990 | 630 | -84.1 | 504990 | 932 | -85.9 | 504990 | 193 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 373: `3aaf006c-159...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3aaf006c-159a-4211-bd78-88a52315e268` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[373] topology](images/test_0373.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3224246_4 by 10 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224427_3
- `C3`: Increase A3 Offset threshold for 3231068_2
- `C4`: Decrease transmission power for 3224427_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224427_3
- `C6`: Check test server and transmission issues
- `C7`: Adjust the azimuth of 3224246_4 by 50 degrees
- `C8`: Decrease A3 Offset threshold for 3231068_2
- `C9`: Increase A3 Offset threshold for 3224427_3
- `C10`: Lift the tilt angle  of 3224246_4 by 10 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231068_2
- `C12`: Decrease transmission power for 3231068_2
- `C13`: Press down the tilt angle of 3224427_3 by 4 degrees
- `C14`: Decrease A3 Offset threshold for 3224427_3
- `C15`: Lift the tilt angle of 3224427_3 by 4 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Adjust the azimuth of 3224427_3 by 39 degrees
- `C18`: Increase transmission power for 3231068_2
- `C19`: Increase transmission power for 3224427_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231068_2
- `C21`: Add neighbor relationship between 3224246_4 and 3231068_2
- `C22`: Add neighbor relationship between 3224427_3 and 3231068_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.156 | MS1 | 121.4656622774 | 31.1446305632 | 506 | 504990 | -90.28 | 16.42 | 322.22 | 0.08 | 2.76 | 1577 |
| 2024-09-20 22:21:32.909 | MS1 | 121.4656765952 | 31.1446210366 | 506 | 504990 | -86.06 | 12.76 | 427.26 | 0.13 | 2.69 | 1596 |
| 2024-09-20 22:21:33.970 | MS1 | 121.4656681760 | 31.1446248722 | 506 | 504990 | -86.63 | 12.17 | 488.69 | 0.02 | 2.34 | 1587 |
| 2024-09-20 22:21:34.223 | MS1 | 121.4656721177 | 31.1446310918 | 506 | 504990 | -89.02 | 17.81 | 90.27 | 0.04 | 2.80 | 1600 |
| 2024-09-20 22:21:35.732 | MS1 | 121.4656635570 | 31.1446207143 | 506 | 504990 | -86.95 | 13.35 | 51.93 | 0.20 | 2.95 | 1595 |
| 2024-09-20 22:21:36.237 | MS1 | 121.4656678384 | 31.1446280284 | 506 | 504990 | -86.75 | 12.44 | 82.93 | 0.02 | 2.72 | 1570 |
| 2024-09-20 22:21:37.228 | MS1 | 121.4656647220 | 31.1446260359 | 506 | 504990 | -90.54 | 9.51 | 96.04 | 0.04 | 2.46 | 1583 |
| 2024-09-20 22:21:38.531 | MS1 | 121.4656639813 | 31.1446368322 | 506 | 504990 | -91.46 | 12.64 | 58.61 | 0.02 | 2.28 | 1590 |
| 2024-09-20 22:21:39.423 | MS1 | 121.4656725738 | 31.1446321640 | 506 | 504990 | -90.09 | 7.13 | 101.57 | 0.04 | 2.05 | 1584 |
| 2024-09-20 22:21:40.142 | MS1 | 121.4656595778 | 31.1446353414 | 506 | 504990 | -90.83 | 10.76 | 490.35 | 0.05 | 2.35 | 1569 |
| 2024-09-20 22:21:41.441 | MS1 | 121.4656580149 | 31.1446186912 | 506 | 504990 | -90.85 | 9.05 | 545.36 | 0.04 | 2.57 | 1575 |
| 2024-09-20 22:21:42.862 | MS1 | 121.4656616836 | 31.1446370613 | 506 | 504990 | -92.33 | 7.39 | 363.18 | 0.01 | 2.36 | 1563 |

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
| 3222564 | 1 | 121.4758965302 | 31.1540798866 | 126 | 10 | 11 | 20.7 | TDD | 600 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3224246 | 4 | 121.4644186759 | 31.1466634962 | 342 | 7 | 0 | 34.8 | TDD | 284 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3224427 | 3 | 121.4704543189 | 31.1542811951 | 242 | 2 | 11 | 49.7 | TDD | 506 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3231068 | 2 | 121.4722184681 | 31.1469737086 | 136 | 13 | 11 | 42.2 | TDD | 225 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.646 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.783 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.783 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.423 | NREventA3 | measId:2;ServCellPCI:564;Se... |
| 2024-09-20 22:21:38.663 | NRHandoverAttempt | SourcePCI:564;SourceNR-ARFC... |
| 2024-09-20 22:21:38.701 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.711 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.838 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.838 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222564 | 1 | 12.9810 | 5.2968 | -114.5247 | 8.6488 | 122.6305 | 0.0090 | 0.0128 |
| 2024_09_20 22:00 | 3231068 | 2 | 9.2083 | 13.1442 | -114.9614 | 13.1160 | 110.1966 | 0.0097 | 0.0012 |
| 2024_09_20 22:00 | 3224427 | 3 | 76.8218 | 80.8191 | -117.8409 | 14.9585 | 127.7703 | 0.0040 | 0.0044 |
| 2024_09_20 22:00 | 3224246 | 4 | 17.8299 | 13.8672 | -115.2005 | 19.1939 | 140.6367 | 0.0035 | 0.0038 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416674_46ED4143 | 504990 | 506 | -89.6 | 504990 | 225 | -93.7 | 504990 | 284 | -94.6 | 504990 | 600 |
| MR_1774416674_0BC99F78 | 504990 | 506 | -90.9 | 504990 | 225 | -96.0 | 504990 | 284 | -95.0 | 504990 | 600 |
| MR_1774416674_B0728834 | 504990 | 506 | -90.2 | 504990 | 225 | -96.3 | 504990 | 284 | -94.1 | 504990 | 600 |
| MR_1774416674_FF0B73A3 | 504990 | 506 | -89.7 | 504990 | 225 | -93.5 | 504990 | 284 | -96.9 | 504990 | 600 |
| MR_1774416674_04BF3618 | 504990 | 506 | -91.0 | 504990 | 225 | -94.2 | 504990 | 284 | -95.5 | 504990 | 600 |
| MR_1774416674_585F4C89 | 504990 | 506 | -88.4 | 504990 | 225 | -93.3 | 504990 | 284 | -93.8 | 504990 | 600 |
| MR_1774416674_11B1465D | 504990 | 506 | -90.9 | 504990 | 225 | -94.4 | 504990 | 284 | -96.1 | 504990 | 600 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 374: `122ed1ed-155...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `122ed1ed-155f-47e1-a4e0-d9e7ca9d8fb2` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[374] topology](images/test_0374.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3241782_1 by 50 degrees
- `C2`: Add neighbor relationship between 3273508_4 and 3273789_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241782_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273789_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273789_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241782_1
- `C7`: Decrease transmission power for 3241782_1
- `C8`: Decrease transmission power for 3273789_2
- `C9`: Increase A3 Offset threshold for 3273789_2
- `C10`: Increase transmission power for 3241782_1
- `C11`: Lift the tilt angle  of 3273789_2 by 10 degrees
- `C12`: Check test server and transmission issues
- `C13`: Add neighbor relationship between 3241782_1 and 3273789_2
- `C14`: Adjust the azimuth of 3273789_2 by 15 degrees
- `C15`: Increase A3 Offset threshold for 3241782_1
- `C16`: Press down the tilt angle  of 3273789_2 by 10 degrees
- `C17`: Decrease A3 Offset threshold for 3273789_2
- `C18`: Lift the tilt angle of 3241782_1 by 10 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease A3 Offset threshold for 3241782_1
- `C21`: Press down the tilt angle of 3241782_1 by 10 degrees
- `C22`: Increase transmission power for 3273789_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.368 | MS1 | 121.4656774159 | 31.1446206136 | 171 | 504990 | -86.60 | 12.63 | 308.55 | 0.03 | 2.48 | 1561 |
| 2024-09-20 22:21:32.422 | MS1 | 121.4656650355 | 31.1446364400 | 171 | 504990 | -85.66 | 15.00 | 348.92 | 0.12 | 2.61 | 1579 |
| 2024-09-20 22:21:33.981 | MS1 | 121.4656585990 | 31.1446255237 | 171 | 504990 | -88.09 | 12.58 | 396.78 | 0.00 | 2.57 | 1575 |
| 2024-09-20 22:21:34.448 | MS1 | 121.4656645912 | 31.1446209859 | 171 | 504990 | -91.03 | 14.10 | 99.03 | 0.16 | 2.94 | 1578 |
| 2024-09-20 22:21:35.423 | MS1 | 121.4656590331 | 31.1446311299 | 171 | 504990 | -88.82 | 12.71 | 63.78 | 0.05 | 2.81 | 1598 |
| 2024-09-20 22:21:36.455 | MS1 | 121.4656616740 | 31.1446282011 | 171 | 504990 | -87.07 | 13.79 | 78.60 | 0.07 | 2.27 | 1576 |
| 2024-09-20 22:21:37.209 | MS1 | 121.4656616250 | 31.1446346343 | 171 | 504990 | -92.60 | 7.91 | 85.03 | 0.15 | 2.82 | 1579 |
| 2024-09-20 22:21:38.758 | MS1 | 121.4656674259 | 31.1446199895 | 171 | 504990 | -92.02 | 7.79 | 70.15 | 0.09 | 2.44 | 1587 |
| 2024-09-20 22:21:39.681 | MS1 | 121.4656726117 | 31.1446339951 | 171 | 504990 | -93.98 | 9.80 | 69.26 | 0.03 | 2.12 | 1574 |
| 2024-09-20 22:21:40.745 | MS1 | 121.4656713125 | 31.1446321567 | 171 | 504990 | -90.89 | 9.25 | 365.17 | 0.13 | 2.51 | 1586 |
| 2024-09-20 22:21:41.509 | MS1 | 121.4656722295 | 31.1446257159 | 171 | 504990 | -89.84 | 7.09 | 337.11 | 0.11 | 2.11 | 1580 |
| 2024-09-20 22:21:42.276 | MS1 | 121.4656697837 | 31.1446310200 | 171 | 504990 | -90.81 | 11.71 | 431.46 | 0.14 | 2.10 | 1569 |

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
| 3241782 | 1 | 121.4692508546 | 31.1479825811 | 341 | 14 | 5 | 37.7 | TDD | 171 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3255262 | 3 | 121.4646256335 | 31.1448045477 | 5 | 6 | 4 | 30.9 | TDD | 403 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3273508 | 4 | 121.4731552561 | 31.1452516596 | 239 | 2 | 2 | 35.3 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3273789 | 2 | 121.4652392181 | 31.1449205131 | 114 | 5 | 8 | 44.8 | TDD | 740 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.397 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.413 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.534 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.534 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.286 | NREventA3 | measId:2;ServCellPCI:625;Se... |
| 2024-09-20 22:21:38.526 | NRHandoverAttempt | SourcePCI:625;SourceNR-ARFC... |
| 2024-09-20 22:21:38.560 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.571 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.681 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.681 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3241782 | 1 | 78.1589 | 77.5361 | -117.3136 | 19.9189 | 91.0043 | 0.0017 | 0.0032 |
| 2024_09_19 22:00 | 3273789 | 2 | 77.7798 | 89.8991 | -114.9011 | 6.9093 | 89.4933 | 0.0131 | 0.0095 |
| 2024_09_19 22:00 | 3255262 | 3 | 77.8742 | 91.9488 | -115.7724 | 7.7884 | 181.1725 | 0.0087 | 0.0176 |
| 2024_09_19 22:00 | 3273508 | 4 | 81.0346 | 88.6366 | -116.0243 | 18.3097 | 128.2737 | 0.0147 | 0.0029 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414984_9BC58B01 | 504990 | 171 | -90.1 | 504990 | 740 | -98.5 | 504990 | 382 | -99.0 | 504990 | 403 |
| MR_1774414984_BD5CC41F | 504990 | 171 | -92.1 | 504990 | 740 | -96.0 | 504990 | 382 | -99.3 | 504990 | 403 |
| MR_1774414984_6907C7A9 | 504990 | 171 | -90.9 | 504990 | 740 | -97.4 | 504990 | 382 | -99.6 | 504990 | 403 |
| MR_1774414984_9732C0A6 | 504990 | 171 | -92.6 | 504990 | 740 | -95.8 | 504990 | 382 | -98.7 | 504990 | 403 |
| MR_1774414984_48ED9D1B | 504990 | 171 | -90.9 | 504990 | 740 | -99.1 | 504990 | 382 | -97.0 | 504990 | 403 |
| MR_1774414984_614738DB | 504990 | 171 | -91.8 | 504990 | 740 | -96.7 | 504990 | 382 | -98.1 | 504990 | 403 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 375: `469f3384-ec8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `469f3384-ec85-4ce0-a15a-dc00059a7075` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[375] topology](images/test_0375.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3214877_3
- `C2`: Increase transmission power for 3251498_1
- `C3`: Decrease A3 Offset threshold for 3251498_1
- `C4`: Adjust the azimuth of 3251498_1 by 50 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214877_3
- `C6`: Increase transmission power for 3214877_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214877_3
- `C8`: Lift the tilt angle  of 3251498_1 by 10 degrees
- `C9`: Decrease transmission power for 3251498_1
- `C10`: Add neighbor relationship between 3214877_3 and 3251498_1
- `C11`: Check test server and transmission issues
- `C12`: Add neighbor relationship between 3217090_2 and 3251498_1
- `C13`: Adjust the azimuth of 3214877_3 by 28 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Lift the tilt angle of 3214877_3 by 5 degrees
- `C16`: Press down the tilt angle of 3214877_3 by 5 degrees
- `C17`: Decrease A3 Offset threshold for 3214877_3
- `C18`: Decrease transmission power for 3214877_3
- `C19`: Increase A3 Offset threshold for 3251498_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251498_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251498_1
- `C22`: Press down the tilt angle  of 3251498_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.614 | MS1 | 121.4656727871 | 31.1446347637 | 430 | 504990 | -85.00 | 13.44 | 504.69 | 0.05 | 2.96 | 1584 |
| 2024-09-20 22:21:32.127 | MS1 | 121.4656650250 | 31.1446338220 | 430 | 504990 | -91.26 | 12.75 | 590.73 | 0.15 | 2.39 | 1599 |
| 2024-09-20 22:21:33.262 | MS1 | 121.4656695636 | 31.1446372021 | 430 | 504990 | -89.65 | 17.49 | 354.31 | 0.18 | 2.23 | 1575 |
| 2024-09-20 22:21:34.148 | MS1 | 121.4656742349 | 31.1446259622 | 430 | 504990 | -88.65 | 13.11 | 80.93 | 0.53 | 2.98 | 515 |
| 2024-09-20 22:21:35.167 | MS1 | 121.4656716635 | 31.1446311975 | 430 | 504990 | -91.33 | 16.78 | 88.90 | 0.67 | 2.45 | 542 |
| 2024-09-20 22:21:36.921 | MS1 | 121.4656625678 | 31.1446337803 | 430 | 504990 | -90.36 | 15.03 | 75.03 | 0.67 | 2.20 | 675 |
| 2024-09-20 22:21:37.900 | MS1 | 121.4656736980 | 31.1446379357 | 430 | 504990 | -93.82 | 7.15 | 57.67 | 0.67 | 2.41 | 631 |
| 2024-09-20 22:21:38.829 | MS1 | 121.4656691232 | 31.1446188510 | 430 | 504990 | -93.46 | 12.58 | 100.03 | 0.66 | 2.80 | 589 |
| 2024-09-20 22:21:39.597 | MS1 | 121.4656598087 | 31.1446197849 | 430 | 504990 | -93.17 | 11.07 | 69.91 | 0.67 | 2.80 | 581 |
| 2024-09-20 22:21:40.427 | MS1 | 121.4656672383 | 31.1446287537 | 430 | 504990 | -91.00 | 11.17 | 390.87 | 0.03 | 2.04 | 1575 |
| 2024-09-20 22:21:41.389 | MS1 | 121.4656738596 | 31.1446263201 | 430 | 504990 | -93.43 | 8.46 | 352.36 | 0.04 | 2.96 | 1572 |
| 2024-09-20 22:21:42.805 | MS1 | 121.4656695838 | 31.1446226407 | 430 | 504990 | -89.75 | 11.16 | 556.92 | 0.18 | 2.78 | 1583 |

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
| 3214877 | 3 | 121.4685240920 | 31.1472466119 | 251 | 2 | 2 | 18.2 | TDD | 430 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3217090 | 2 | 121.4740089713 | 31.1521842817 | 43 | 7 | 5 | 30.0 | TDD | 573 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3222172 | 4 | 121.4660589352 | 31.1449187931 | 307 | 1 | 2 | 45.0 | TDD | 951 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3251498 | 1 | 121.4661928092 | 31.1461190567 | 94 | 2 | 2 | 49.5 | TDD | 906 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.785 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.809 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.936 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.936 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.643 | NREventA3 | measId:2;ServCellPCI:993;Se... |
| 2024-09-20 22:21:37.883 | NRHandoverAttempt | SourcePCI:993;SourceNR-ARFC... |
| 2024-09-20 22:21:37.920 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.931 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.077 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.077 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251498 | 1 | 15.5397 | 8.0413 | -116.9956 | 8.5487 | 180.8546 | 0.0092 | 0.0180 |
| 2024_09_20 22:00 | 3217090 | 2 | 7.7683 | 8.4083 | -117.9546 | 7.1744 | 110.0471 | 0.0104 | 0.0030 |
| 2024_09_20 22:00 | 3214877 | 3 | 16.5648 | 7.4067 | -116.7541 | 9.0628 | 124.7827 | 0.0165 | 0.0075 |
| 2024_09_20 22:00 | 3222172 | 4 | 13.6463 | 12.8311 | -116.2814 | 12.0768 | 135.5182 | 0.0133 | 0.0179 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414213_38D82723 | 504990 | 430 | -90.0 | 504990 | 906 | -94.3 | 504990 | 573 | -102.1 | 504990 | 951 |
| MR_1774414213_5D66B152 | 504990 | 430 | -88.2 | 504990 | 906 | -91.9 | 504990 | 573 | -102.7 | 504990 | 951 |
| MR_1774414213_430AB50C | 504990 | 430 | -86.7 | 504990 | 906 | -95.8 | 504990 | 573 | -103.6 | 504990 | 951 |
| MR_1774414213_C7251A2F | 504990 | 430 | -88.4 | 504990 | 906 | -93.5 | 504990 | 573 | -102.7 | 504990 | 951 |
| MR_1774414213_C2CD4971 | 504990 | 430 | -87.0 | 504990 | 906 | -95.2 | 504990 | 573 | -101.7 | 504990 | 951 |
| MR_1774414213_BEDE2EE7 | 504990 | 430 | -86.9 | 504990 | 906 | -93.5 | 504990 | 573 | -102.5 | 504990 | 951 |
| MR_1774414213_4E234C74 | 504990 | 430 | -89.2 | 504990 | 906 | -92.3 | 504990 | 573 | -101.5 | 504990 | 951 |
| MR_1774414213_8BC598BA | 504990 | 430 | -86.9 | 504990 | 906 | -94.2 | 504990 | 573 | -103.9 | 504990 | 951 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 376: `5efefb61-041...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5efefb61-0415-44da-9ff6-6038d549969c` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[376] topology](images/test_0376.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3223294_2
- `C2`: Decrease transmission power for 3223294_2
- `C3`: Decrease A3 Offset threshold for 3223294_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210682_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223294_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223294_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Adjust the azimuth of 3210682_3 by 36 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210682_3
- `C10`: Add neighbor relationship between 3210682_3 and 3223294_2
- `C11`: Increase transmission power for 3210682_3
- `C12`: Press down the tilt angle  of 3223294_2 by 6 degrees
- `C13`: Decrease A3 Offset threshold for 3210682_3
- `C14`: Lift the tilt angle  of 3223294_2 by 6 degrees
- `C15`: Adjust the azimuth of 3223294_2 by 36 degrees
- `C16`: Decrease transmission power for 3210682_3
- `C17`: Increase A3 Offset threshold for 3210682_3
- `C18`: Lift the tilt angle of 3210682_3 by 3 degrees
- `C19`: Check test server and transmission issues
- `C20`: Add neighbor relationship between 3272804_5 and 3223294_2
- `C21`: Press down the tilt angle of 3210682_3 by 3 degrees
- `C22`: Increase transmission power for 3223294_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.781 | MS1 | 121.4656772931 | 31.1446206078 | 328 | 504990 | -79.26 | 14.12 | 481.80 | 0.10 | 2.20 | 1565 |
| 2024-09-20 22:21:32.646 | MS1 | 121.4656697119 | 31.1446207734 | 328 | 504990 | -75.10 | 17.21 | 599.26 | 0.13 | 2.27 | 1568 |
| 2024-09-20 22:21:33.469 | MS1 | 121.4656768601 | 31.1446187515 | 328 | 504990 | -77.77 | 17.82 | 470.93 | 0.10 | 2.96 | 1584 |
| 2024-09-20 22:21:34.624 | MS1 | 121.4656672199 | 31.1446193455 | 255 | 504990 | -89.23 | 1.84 | 48.55 | 0.15 | 1.03 | 1572 |
| 2024-09-20 22:21:35.872 | MS1 | 121.4656779729 | 31.1446182475 | 255 | 504990 | -84.87 | 1.53 | 56.47 | 0.16 | 1.23 | 1594 |
| 2024-09-20 22:21:36.790 | MS1 | 121.4656754252 | 31.1446291314 | 328 | 504990 | -80.81 | 4.23 | 45.43 | 0.07 | 1.38 | 1583 |
| 2024-09-20 22:21:37.721 | MS1 | 121.4656728775 | 31.1446184658 | 328 | 504990 | -89.26 | 4.47 | 86.25 | 0.03 | 1.38 | 1590 |
| 2024-09-20 22:21:38.524 | MS1 | 121.4656737386 | 31.1446354507 | 255 | 504990 | -87.60 | 1.65 | 64.97 | 0.18 | 1.29 | 1569 |
| 2024-09-20 22:21:39.545 | MS1 | 121.4656690408 | 31.1446291820 | 255 | 504990 | -81.42 | 1.65 | 81.70 | 0.10 | 1.05 | 1599 |
| 2024-09-20 22:21:40.605 | MS1 | 121.4656744158 | 31.1446312939 | 255 | 504990 | -81.40 | 12.54 | 513.11 | 0.09 | 2.93 | 1575 |
| 2024-09-20 22:21:41.585 | MS1 | 121.4656627529 | 31.1446341954 | 255 | 504990 | -81.35 | 12.95 | 467.63 | 0.01 | 2.76 | 1594 |
| 2024-09-20 22:21:42.886 | MS1 | 121.4656612673 | 31.1446290249 | 255 | 504990 | -82.68 | 15.11 | 426.49 | 0.10 | 2.74 | 1581 |

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
| 3210682 | 3 | 121.4671407914 | 31.1540024109 | 152 | 1 | 8 | 28.4 | TDD | 328 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3213783 | 4 | 121.4754711178 | 31.1445500379 | 204 | 14 | 8 | 28.5 | TDD | 172 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3223294 | 2 | 121.4682773778 | 31.1467446624 | 190 | 2 | 12 | 22.5 | TDD | 39 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3225346 | 1 | 121.4675728722 | 31.1521835207 | 4 | 14 | 3 | 24.0 | TDD | 255 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3272804 | 5 | 121.4685735169 | 31.1466525338 | 16 | 11 | 5 | 29.0 | TDD | 479 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.278 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.303 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.416 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.416 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.127 | NREventA3 | measId:2;ServCellPCI:597;Se... |
| 2024-09-20 22:21:34.367 | NRHandoverAttempt | SourcePCI:597;SourceNR-ARFC... |
| 2024-09-20 22:21:34.399 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.409 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:34.558 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.558 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.127 | NREventA3 | measId:2;ServCellPCI:917;Se... |
| 2024-09-20 22:21:36.367 | NRHandoverAttempt | SourcePCI:917;SourceNR-ARFC... |
| 2024-09-20 22:21:36.412 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.426 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.557 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.557 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.127 | NREventA3 | measId:2;ServCellPCI:597;Se... |
| 2024-09-20 22:21:38.367 | NRHandoverAttempt | SourcePCI:597;SourceNR-ARFC... |
| 2024-09-20 22:21:38.411 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.425 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.573 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.573 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225346 | 1 | 18.8657 | 11.1797 | -116.2215 | 5.1954 | 98.4051 | 0.0042 | 0.0190 |
| 2024_09_20 22:00 | 3223294 | 2 | 19.2635 | 15.5698 | -117.7729 | 6.3439 | 144.0978 | 0.0011 | 0.0100 |
| 2024_09_20 22:00 | 3210682 | 3 | 16.4005 | 6.3192 | -115.7075 | 5.7010 | 142.8309 | 0.0181 | 0.0167 |
| 2024_09_20 22:00 | 3213783 | 4 | 9.9632 | 13.0276 | -114.4963 | 15.9939 | 191.5963 | 0.0009 | 0.0019 |
| 2024_09_20 22:00 | 3272804 | 5 | 8.2391 | 17.4560 | -116.1682 | 11.9932 | 108.7342 | 0.0058 | 0.0062 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414238_AD4A5BCE | 504990 | 328 | -88.9 | 504990 | 255 | -88.1 | 504990 | 39 | -95.9 | 504990 | 479 |
| MR_1774414238_82A70514 | 504990 | 255 | -87.6 | 504990 | 328 | -88.9 | 504990 | 39 | -95.5 | 504990 | 479 |
| MR_1774414238_092F25CF | 504990 | 328 | -87.6 | 504990 | 255 | -88.5 | 504990 | 39 | -97.1 | 504990 | 479 |
| MR_1774414238_02D0581E | 504990 | 328 | -87.5 | 504990 | 255 | -86.0 | 504990 | 39 | -95.2 | 504990 | 479 |
| MR_1774414238_ACF250A0 | 504990 | 328 | -88.8 | 504990 | 255 | -89.0 | 504990 | 39 | -95.2 | 504990 | 479 |
| MR_1774414238_94FFDAF9 | 504990 | 255 | -88.3 | 504990 | 328 | -87.3 | 504990 | 39 | -96.4 | 504990 | 479 |
| MR_1774414238_A07979DE | 504990 | 328 | -90.0 | 504990 | 255 | -86.3 | 504990 | 39 | -95.0 | 504990 | 479 |
| MR_1774414238_9C900976 | 504990 | 255 | -90.1 | 504990 | 328 | -86.7 | 504990 | 39 | -96.3 | 504990 | 479 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 377: `9e483a6b-b7c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9e483a6b-b7cf-4a6e-821e-1c46e642b075` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[377] topology](images/test_0377.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213646_4
- `C2`: Add neighbor relationship between 3246789_2 and 3251340_3
- `C3`: Adjust the azimuth of 3246789_2 by 50 degrees
- `C4`: Decrease transmission power for 3251340_3
- `C5`: Lift the tilt angle of 3213646_4 by 2 degrees
- `C6`: Decrease transmission power for 3213646_4
- `C7`: Press down the tilt angle of 3213646_4 by 2 degrees
- `C8`: Add neighbor relationship between 3213646_4 and 3251340_3
- `C9`: Check test server and transmission issues
- `C10`: Increase A3 Offset threshold for 3251340_3
- `C11`: Lift the tilt angle  of 3246789_2 by 10 degrees
- `C12`: Decrease A3 Offset threshold for 3213646_4
- `C13`: Adjust the azimuth of 3213646_4 by 50 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251340_3
- `C15`: Press down the tilt angle  of 3246789_2 by 10 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251340_3
- `C17`: Increase transmission power for 3251340_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213646_4
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase A3 Offset threshold for 3213646_4
- `C21`: Increase transmission power for 3213646_4
- `C22`: Decrease A3 Offset threshold for 3251340_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.705 | MS1 | 121.4656586941 | 31.1446329002 | 430 | 504990 | -86.30 | 13.64 | 468.18 | 0.15 | 2.30 | 1577 |
| 2024-09-20 22:21:32.975 | MS1 | 121.4656743535 | 31.1446364823 | 430 | 504990 | -90.63 | 12.64 | 332.55 | 0.09 | 2.64 | 1579 |
| 2024-09-20 22:21:33.822 | MS1 | 121.4656690222 | 31.1446347719 | 430 | 504990 | -87.09 | 15.13 | 459.66 | 0.12 | 2.52 | 1590 |
| 2024-09-20 22:21:34.534 | MS1 | 121.4656595652 | 31.1446311029 | 430 | 504990 | -91.14 | 15.04 | 65.15 | 0.18 | 2.98 | 1592 |
| 2024-09-20 22:21:35.266 | MS1 | 121.4656581656 | 31.1446307328 | 430 | 504990 | -86.65 | 14.97 | 47.76 | 0.18 | 2.94 | 1600 |
| 2024-09-20 22:21:36.124 | MS1 | 121.4656711220 | 31.1446278426 | 430 | 504990 | -87.07 | 14.81 | 83.53 | 0.13 | 2.45 | 1570 |
| 2024-09-20 22:21:37.116 | MS1 | 121.4656664697 | 31.1446265005 | 430 | 504990 | -89.73 | 8.74 | 101.95 | 0.10 | 2.76 | 1590 |
| 2024-09-20 22:21:38.367 | MS1 | 121.4656775124 | 31.1446352648 | 430 | 504990 | -93.12 | 12.25 | 59.36 | 0.03 | 2.08 | 1572 |
| 2024-09-20 22:21:39.258 | MS1 | 121.4656767567 | 31.1446267900 | 430 | 504990 | -89.92 | 8.10 | 72.09 | 0.12 | 2.60 | 1568 |
| 2024-09-20 22:21:40.609 | MS1 | 121.4656649890 | 31.1446186461 | 430 | 504990 | -91.66 | 9.10 | 564.70 | 0.03 | 2.33 | 1594 |
| 2024-09-20 22:21:41.903 | MS1 | 121.4656581148 | 31.1446215688 | 430 | 504990 | -90.16 | 12.96 | 512.00 | 0.04 | 2.96 | 1597 |
| 2024-09-20 22:21:42.600 | MS1 | 121.4656734733 | 31.1446198631 | 430 | 504990 | -89.33 | 12.47 | 329.06 | 0.19 | 2.55 | 1577 |

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
| 3213646 | 4 | 121.4747477592 | 31.1511657513 | 180 | 0 | 2 | 35.0 | TDD | 430 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3246789 | 2 | 121.4718823539 | 31.1461544230 | 63 | 5 | 8 | 17.4 | TDD | 811 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3251340 | 3 | 121.4660257404 | 31.1464773329 | 68 | 9 | 9 | 23.7 | TDD | 133 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3272333 | 1 | 121.4737638069 | 31.1466202527 | 126 | 6 | 0 | 23.2 | TDD | 496 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.979 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.997 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.140 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.140 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.787 | NREventA3 | measId:2;ServCellPCI:866;Se... |
| 2024-09-20 22:21:38.027 | NRHandoverAttempt | SourcePCI:866;SourceNR-ARFC... |
| 2024-09-20 22:21:38.074 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.084 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.232 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.232 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272333 | 1 | 5.4938 | 19.3377 | -116.1986 | 13.4115 | 131.2601 | 0.0110 | 0.0140 |
| 2024_09_20 22:00 | 3246789 | 2 | 12.3870 | 19.9704 | -114.9623 | 13.4612 | 199.2814 | 0.0197 | 0.0158 |
| 2024_09_20 22:00 | 3251340 | 3 | 9.0284 | 16.1477 | -116.2054 | 7.8781 | 111.2939 | 0.0098 | 0.0158 |
| 2024_09_20 22:00 | 3213646 | 4 | 89.7624 | 77.4629 | -115.0517 | 16.4825 | 82.0448 | 0.0023 | 0.0028 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416512_18A00342 | 504990 | 430 | -90.2 | 504990 | 133 | -101.6 | 504990 | 811 | -102.0 | 504990 | 496 |
| MR_1774416512_06A6E83C | 504990 | 430 | -92.1 | 504990 | 133 | -102.1 | 504990 | 811 | -103.4 | 504990 | 496 |
| MR_1774416512_B11F9B0D | 504990 | 430 | -92.9 | 504990 | 133 | -101.1 | 504990 | 811 | -102.6 | 504990 | 496 |
| MR_1774416512_F8993FE9 | 504990 | 430 | -90.9 | 504990 | 133 | -101.8 | 504990 | 811 | -104.0 | 504990 | 496 |
| MR_1774416512_01210109 | 504990 | 430 | -91.5 | 504990 | 133 | -102.8 | 504990 | 811 | -103.3 | 504990 | 496 |
| MR_1774416512_E7304006 | 504990 | 430 | -90.4 | 504990 | 133 | -101.1 | 504990 | 811 | -102.6 | 504990 | 496 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 378: `5a677dca-8d7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5a677dca-8d7a-4d51-8714-0b066e4e3fbe` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[378] topology](images/test_0378.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3218975_3
- `C2`: Lift the tilt angle of 3254295_1 by 6 degrees
- `C3`: Increase transmission power for 3218975_3
- `C4`: Add neighbor relationship between 3269976_4 and 3218975_3
- `C5`: Decrease transmission power for 3254295_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218975_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254295_1
- `C8`: Adjust the azimuth of 3254295_1 by 9 degrees
- `C9`: Decrease A3 Offset threshold for 3218975_3
- `C10`: Increase A3 Offset threshold for 3254295_1
- `C11`: Increase transmission power for 3254295_1
- `C12`: Adjust the azimuth of 3269976_4 by 50 degrees
- `C13`: Check test server and transmission issues
- `C14`: Press down the tilt angle of 3254295_1 by 6 degrees
- `C15`: Press down the tilt angle  of 3269976_4 by 10 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease transmission power for 3218975_3
- `C18`: Add neighbor relationship between 3254295_1 and 3218975_3
- `C19`: Decrease A3 Offset threshold for 3254295_1
- `C20`: Lift the tilt angle  of 3269976_4 by 10 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254295_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218975_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.852 | MS1 | 121.4656716666 | 31.1446329395 | 561 | 504990 | -86.51 | 17.61 | 574.23 | 0.10 | 2.92 | 1579 |
| 2024-09-20 22:21:32.823 | MS1 | 121.4656702568 | 31.1446267424 | 561 | 504990 | -85.42 | 12.19 | 441.16 | 0.00 | 2.23 | 1570 |
| 2024-09-20 22:21:33.913 | MS1 | 121.4656690500 | 31.1446253400 | 561 | 504990 | -89.86 | 15.53 | 393.96 | 0.05 | 2.19 | 1579 |
| 2024-09-20 22:21:34.650 | MS1 | 121.4656703062 | 31.1446195095 | 561 | 504990 | -90.48 | 14.77 | 93.75 | 0.01 | 2.05 | 1594 |
| 2024-09-20 22:21:35.140 | MS1 | 121.4656701043 | 31.1446352238 | 561 | 504990 | -90.66 | 12.30 | 65.12 | 0.14 | 2.85 | 1566 |
| 2024-09-20 22:21:36.977 | MS1 | 121.4656692953 | 31.1446247804 | 561 | 504990 | -88.88 | 13.31 | 104.25 | 0.07 | 2.69 | 1566 |
| 2024-09-20 22:21:37.553 | MS1 | 121.4656640860 | 31.1446253025 | 561 | 504990 | -93.54 | 7.57 | 70.54 | 0.19 | 2.75 | 1581 |
| 2024-09-20 22:21:38.170 | MS1 | 121.4656581805 | 31.1446221263 | 561 | 504990 | -93.51 | 9.01 | 60.43 | 0.14 | 2.06 | 1564 |
| 2024-09-20 22:21:39.601 | MS1 | 121.4656688517 | 31.1446190368 | 561 | 504990 | -90.53 | 8.36 | 69.31 | 0.17 | 2.70 | 1573 |
| 2024-09-20 22:21:40.309 | MS1 | 121.4656694310 | 31.1446261022 | 561 | 504990 | -89.72 | 10.65 | 529.64 | 0.04 | 2.40 | 1575 |
| 2024-09-20 22:21:41.367 | MS1 | 121.4656612458 | 31.1446306034 | 561 | 504990 | -89.42 | 8.55 | 531.81 | 0.03 | 2.55 | 1600 |
| 2024-09-20 22:21:42.254 | MS1 | 121.4656743476 | 31.1446243494 | 561 | 504990 | -92.07 | 7.96 | 565.30 | 0.17 | 2.89 | 1575 |

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
| 3218975 | 3 | 121.4700762933 | 31.1477545463 | 343 | 15 | 8 | 17.7 | TDD | 103 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3252921 | 2 | 121.4650113352 | 31.1543320946 | 147 | 2 | 3 | 32.8 | TDD | 956 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3254295 | 1 | 121.4737286390 | 31.1530642454 | 228 | 4 | 5 | 40.2 | TDD | 561 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3269976 | 4 | 121.4738171303 | 31.1456763954 | 19 | 10 | 6 | 44.6 | TDD | 575 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.504 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.637 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.637 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.375 | NREventA3 | measId:2;ServCellPCI:464;Se... |
| 2024-09-20 22:21:38.615 | NRHandoverAttempt | SourcePCI:464;SourceNR-ARFC... |
| 2024-09-20 22:21:38.649 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.662 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.786 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.786 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254295 | 1 | 85.1452 | 81.3812 | -117.2813 | 18.6744 | 132.4895 | 0.0198 | 0.0081 |
| 2024_09_20 22:00 | 3252921 | 2 | 16.3331 | 15.2717 | -115.4133 | 10.4667 | 153.6944 | 0.0041 | 0.0149 |
| 2024_09_20 22:00 | 3218975 | 3 | 8.7733 | 18.5490 | -115.6990 | 9.0015 | 193.3239 | 0.0144 | 0.0015 |
| 2024_09_20 22:00 | 3269976 | 4 | 11.9388 | 18.0388 | -116.7241 | 13.0904 | 164.6246 | 0.0107 | 0.0100 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415159_CB8686A4 | 504990 | 561 | -92.4 | 504990 | 103 | -96.1 | 504990 | 575 | -99.3 | 504990 | 956 |
| MR_1774415159_71E3A595 | 504990 | 561 | -90.8 | 504990 | 103 | -98.0 | 504990 | 575 | -97.7 | 504990 | 956 |
| MR_1774415159_4B79BF30 | 504990 | 561 | -90.7 | 504990 | 103 | -95.4 | 504990 | 575 | -96.7 | 504990 | 956 |
| MR_1774415159_B7F89685 | 504990 | 561 | -92.3 | 504990 | 103 | -96.0 | 504990 | 575 | -96.9 | 504990 | 956 |
| MR_1774415159_49365702 | 504990 | 561 | -92.3 | 504990 | 103 | -95.5 | 504990 | 575 | -98.3 | 504990 | 956 |
| MR_1774415159_35F5668F | 504990 | 561 | -92.0 | 504990 | 103 | -96.0 | 504990 | 575 | -96.7 | 504990 | 956 |
| MR_1774415159_80E7A5C2 | 504990 | 561 | -88.6 | 504990 | 103 | -95.8 | 504990 | 575 | -96.8 | 504990 | 956 |
| MR_1774415159_0C6F941B | 504990 | 561 | -91.0 | 504990 | 103 | -96.7 | 504990 | 575 | -95.9 | 504990 | 956 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 379: `8349aaea-ebe...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8349aaea-ebe7-4e8f-93b7-4c3c01f6564b` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[379] topology](images/test_0379.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease transmission power for 3223239_1
- `C3`: Add neighbor relationship between 3223239_1 and 3228135_5
- `C4`: Press down the tilt angle of 3223239_1 by 3 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease A3 Offset threshold for 3223239_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228135_5
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223239_1
- `C9`: Lift the tilt angle  of 3228135_5 by 6 degrees
- `C10`: Press down the tilt angle  of 3228135_5 by 6 degrees
- `C11`: Increase A3 Offset threshold for 3223239_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223239_1
- `C13`: Increase A3 Offset threshold for 3228135_5
- `C14`: Increase transmission power for 3223239_1
- `C15`: Adjust the azimuth of 3228135_5 by 29 degrees
- `C16`: Lift the tilt angle of 3223239_1 by 3 degrees
- `C17`: Decrease A3 Offset threshold for 3228135_5
- `C18`: Add neighbor relationship between 3210324_8 and 3228135_5
- `C19`: Adjust the azimuth of 3223239_1 by 30 degrees
- `C20`: Increase transmission power for 3228135_5
- `C21`: Decrease transmission power for 3228135_5
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228135_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.118 | MS1 | 121.4656688182 | 31.1446291886 | 548 | 504990 | -94.68 | 11.72 | 405.55 | 0.14 | 2.37 | 1589 |
| 2024-09-20 22:21:32.579 | MS1 | 121.4656621891 | 31.1446310007 | 293 | 504990 | -93.28 | 10.07 | 453.94 | 0.13 | 2.80 | 1574 |
| 2024-09-20 22:21:33.679 | MS1 | 121.4656617243 | 31.1446220136 | 766 | 504990 | -95.34 | 10.44 | 487.96 | 0.13 | 2.77 | 1564 |
| 2024-09-20 22:21:34.246 | MS1 | 121.4656753876 | 31.1446367905 | 667 | 152650 | -94.12 | 3.02 | 79.68 | 0.12 | 2.00 | 985 |
| 2024-09-20 22:21:35.402 | MS1 | 121.4656619551 | 31.1446271297 | 82 | 152650 | -93.62 | 4.13 | 64.06 | 0.05 | 1.94 | 979 |
| 2024-09-20 22:21:36.511 | MS1 | 121.4656722526 | 31.1446345701 | 716 | 152650 | -96.54 | 6.79 | 67.63 | 0.18 | 1.60 | 942 |
| 2024-09-20 22:21:37.229 | MS1 | 121.4656676578 | 31.1446281456 | 492 | 152650 | -96.15 | 3.76 | 82.69 | 0.04 | 1.70 | 905 |
| 2024-09-20 22:21:38.183 | MS1 | 121.4656727845 | 31.1446311900 | 667 | 152650 | -95.20 | 4.26 | 78.72 | 0.07 | 2.00 | 945 |
| 2024-09-20 22:21:39.432 | MS1 | 121.4656718648 | 31.1446359318 | 82 | 152650 | -87.55 | 5.84 | 40.94 | 0.12 | 1.91 | 909 |
| 2024-09-20 22:21:40.776 | MS1 | 121.4656591706 | 31.1446320725 | 716 | 152650 | -96.30 | 7.25 | 57.19 | 0.19 | 2.83 | 1580 |
| 2024-09-20 22:21:41.109 | MS1 | 121.4656584216 | 31.1446355256 | 492 | 152650 | -95.19 | 2.60 | 84.39 | 0.19 | 2.48 | 1584 |
| 2024-09-20 22:21:42.911 | MS1 | 121.4656582135 | 31.1446249606 | 667 | 152650 | -87.57 | 7.87 | 66.01 | 0.03 | 2.86 | 1566 |

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
| 3210324 | 8 | 121.4725507316 | 31.1559276775 | 148 | 9 | 6 | 5.8 | FDD | 716 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3223239 | 1 | 121.4713094166 | 31.1500546233 | 252 | 1 | 6 | 28.4 | TDD | 548 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3226773 | 3 | 121.4747141257 | 31.1460921298 | 353 | 13 | 3 | 0.0 | TDD | 718 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3228135 | 5 | 121.4686337948 | 31.1544095110 | 166 | 5 | 9 | 13.1 | TDD | 217 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3228175 | 4 | 121.4677354199 | 31.1445758323 | 200 | 2 | 7 | 18.8 | TDD | 305 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3230408 | 2 | 121.4659238404 | 31.1523530507 | 27 | 9 | 5 | 25.9 | TDD | 293 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3231272 | 11 | 121.4725145134 | 31.1441160655 | 58 | 2 | 6 | 12.9 | FDD | 82 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3242759 | 13 | 121.4695836477 | 31.1539528191 | 177 | 1 | 0 | 21.6 | FDD | 31 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3249148 | 7 | 121.4662680347 | 31.1456469889 | 140 | 10 | 0 | 18.4 | FDD | 1001 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3255287 | 9 | 121.4668107031 | 31.1485330904 | 196 | 0 | 2 | 19.1 | FDD | 492 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3256888 | 10 | 121.4693389820 | 31.1492007378 | 173 | 2 | 10 | 21.7 | FDD | 944 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3267417 | 6 | 121.4717675052 | 31.1534302033 | 301 | 7 | 10 | 26.8 | TDD | 766 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3278816 | 12 | 121.4706205976 | 31.1499630725 | 277 | 2 | 9 | 11.4 | FDD | 667 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |

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
| 2024-09-20 22:21:31.620 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.645 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.780 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.780 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.484 | NREventA2 | measId:1;ServCellPCI:114;Se... |
| 2024-09-20 22:21:35.625 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.839 | NREventA5 | measId:3;ServCellPCI:114;Se... |
| 2024-09-20 22:21:35.912 | NRHandoverAttempt | SourcePCI:114;SourceNR-ARFC... |
| 2024-09-20 22:21:35.955 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.969 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.099 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.099 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223239 | 1 | 8.1294 | 18.1637 | -115.5243 | 18.1763 | 106.3777 | 0.0133 | 0.0025 |
| 2024_09_20 22:00 | 3230408 | 2 | 12.7149 | 7.6622 | -116.8181 | 16.3159 | 107.8978 | 0.0144 | 0.0117 |
| 2024_09_20 22:00 | 3226773 | 3 | 17.0229 | 16.2649 | -114.5248 | 7.2842 | 124.2809 | 0.0182 | 0.0119 |
| 2024_09_20 22:00 | 3228175 | 4 | 8.3719 | 17.1143 | -117.9829 | 12.1138 | 160.3436 | 0.0029 | 0.0020 |
| 2024_09_20 22:00 | 3228135 | 5 | 7.5847 | 8.8189 | -116.9514 | 8.0093 | 184.3948 | 0.0157 | 0.0034 |
| 2024_09_20 22:00 | 3267417 | 6 | 16.1379 | 12.0586 | -116.7979 | 16.4497 | 132.9900 | 0.0096 | 0.0019 |
| 2024_09_20 22:00 | 3249148 | 7 | 7.8518 | 17.7375 | -117.1821 | 4.5715 | 21.4256 | 0.0050 | 0.0094 |
| 2024_09_20 22:00 | 3210324 | 8 | 13.7131 | 13.8516 | -116.4646 | 3.6728 | 52.5376 | 0.0038 | 0.0112 |
| 2024_09_20 22:00 | 3255287 | 9 | 8.8402 | 15.5546 | -114.8012 | 4.6953 | 52.5042 | 0.0112 | 0.0066 |
| 2024_09_20 22:00 | 3256888 | 10 | 16.4350 | 10.9734 | -115.8650 | 3.5843 | 50.4636 | 0.0078 | 0.0083 |
| 2024_09_20 22:00 | 3231272 | 11 | 14.2144 | 16.7390 | -114.6698 | 3.3117 | 21.7723 | 0.0062 | 0.0133 |
| 2024_09_20 22:00 | 3278816 | 12 | 19.1234 | 12.1267 | -115.7736 | 4.6872 | 37.5087 | 0.0113 | 0.0010 |
| 2024_09_20 22:00 | 3242759 | 13 | 5.0248 | 13.1673 | -117.0960 | 4.5144 | 54.4497 | 0.0006 | 0.0063 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412852_4CFDAF57 | 152650 | 667 | -95.9 | 152650 | 1001 | -99.4 | 152650 | 31 | -107.3 | 152650 | 944 |
| MR_1774412852_1C078BF8 | 504990 | 766 | -96.2 | 504990 | 217 | -89.5 | 504990 | 305 | -97.2 | 504990 | 718 |
| MR_1774412852_1904F9E4 | 152650 | 667 | -96.0 | 152650 | 1001 | -98.7 | 152650 | 31 | -106.0 | 152650 | 944 |
| MR_1774412852_11D0DA24 | 152650 | 667 | -92.3 | 152650 | 1001 | -98.5 | 152650 | 31 | -104.9 | 152650 | 944 |
| MR_1774412852_AD9F0377 | 504990 | 766 | -96.2 | 504990 | 217 | -92.7 | 504990 | 305 | -98.4 | 504990 | 718 |
| MR_1774412852_112A1AD6 | 504990 | 766 | -95.3 | 504990 | 217 | -93.0 | 504990 | 305 | -96.2 | 504990 | 718 |

> *... 2개 열 생략 (전체 14열)*

---
