# Track A 무선 5G 네트워크 토폴로지

> Track A 시뮬레이션 도메인의 무선 RAN(Radio Access Network) 구조 설명
> Track B 의 IP 네트워크 토폴로지와는 완전히 다른 무선 RF 도메인
> 최종 업데이트: 2026-04-22

---

## 1. 개요

Track A 는 **5G NR (New Radio)** 무선 네트워크의 **드라이브 테스트 (Drive Test)** 시나리오를 다룬다. 사용자 단말 (UE) 이 차량에 탑재되어 일정 구역을 이동하면서 측정한 RF 데이터를 기반으로 throughput 저하의 원인을 진단하고 무선 파라미터 최적화를 결정한다.

각 scenario 는 다음 구조:
- **5개 내외의 5G 기지국 (gNodeB)** 이 일정 영역 커버
- 각 gNodeB 는 1~6개 **Cell (Sector)** 보유, 셀별 PCI/방향각/틸트
- UE 가 차량 이동 중 약 10초 구간의 throughput / RSRP / SINR 시계열 수집
- 그 중 일부 구간에서 throughput 이 < 100 Mbps 로 저하 → **이 저하 원인이 문제**

---

## 2. 핵심 구성 요소 용어

### 2.1 기지국과 셀 (Cell)

| 개념 | 설명 |
|------|------|
| **gNodeB ID** | 5G 기지국 고유 ID (예: `3225568`). 한 위치에 여러 cell sector 보유 |
| **Cell ID** | 한 gNodeB 내 sector 번호 (1, 2, 3, 4, ...). `gNodeB_Cell` 표기 (`3225568_1`) |
| **PCI** (Physical Cell ID) | 0~1007 의 RF layer 식별자. UE 가 신호 측정에 사용 |
| **ARFCN** | NR 채널 주파수 번호 (`504990` 대역 = 3500 MHz n41) |
| **DL ARFCN** | Downlink 캐리어 주파수 번호 |

### 2.2 안테나 파라미터

| 파라미터 | 단위 | 의미 | 범위 |
|---------|------|------|------|
| **Mechanical Azimuth** | 도 | 안테나가 물리적으로 향한 방위각 (북=0, 동=90, 남=180, 서=270) | 0~360 |
| **Mechanical Downtilt** | 도 | 물리적으로 빔이 아래로 기울어진 각도 | 0~15 |
| **Digital Tilt** | 도 | 빔 forming 으로 추가 적용된 downtilt | 0~12 |
| **Total Downtilt** | 도 | `Mechanical Downtilt + Digital Tilt`. ≥20° 이면 매우 좁은 영역만 커버 |
| **Transmission Power** | dBm | 송신 전력 (보통 11~30, max=32) |
| **TxRx Mode** | — | 안테나 구성 (예: `64T64R` = 64 송수신 안테나, massive MIMO) |
| **Height** | m | 안테나 설치 고도 |
| **BW [MHz]** | MHz | 채널 대역폭 (보통 100M) |

### 2.3 RF 측정값

| 측정값 | 단위 | 의미 | 정상 범위 |
|--------|------|------|----------|
| **SS-RSRP** (Synchronization Signal Reference Signal Received Power) | dBm | UE 가 측정한 신호 강도 | -60 (강함) ~ -120 (매우 약함) |
| **SS-SINR** (Signal-to-Interference plus Noise Ratio) | dB | 신호 대 간섭+잡음 비율 | -5 (간섭) ~ +30 (양호). > 10 = healthy |
| **DL Throughput** | Mbps | 다운링크 전송속도 | 0 ~ 1000+ |
| **CCE Fail Rate** | 비율 | Control Channel Element 실패율 | 정상 < 0.5 |
| **Avg MCS** | 인덱스 | Modulation and Coding Scheme 평균 | 0~28 |
| **Initial / Residual BLER** | % | Block Error Rate, 재전송 전후 | < 10% |

---

## 3. Handover 메커니즘 (가장 자주 등장하는 진단 포인트)

### 3.1 A2 / A3 / A5 Event 정의 (3GPP TS 38.331)

| 이벤트 | 정의 | 활용 |
|--------|------|------|
| **A2** | `Serving < Threshold` | UE 가 inter-frequency 측정 시작 |
| **A3** | `Neighbor > Serving + Offset + Hyst` | Intra-frequency handover 트리거 |
| **A5** | `Serving < Threshold1 AND Neighbor > Threshold2` | Inter-frequency handover 트리거 |

### 3.2 A3 Handover 공식 (Track A 의 핵심)

```
A3 trigger 조건: Neighbor_RSRP  >  Serving_RSRP  +  A3Offset×0.5 dB  +  A3Hyst×0.5 dB
                                                  └─────────┬─────────┘
                                                       실효 dB 임계
```

Cell config 의 `IntraFreqHoA3Offset` 와 `IntraFreqHoA3Hyst` 는 **0.5 dB 단위 정수**:

| Config 값 | 실효 dB |
|-----------|---------|
| 2  | 1.0 dB |
| 4  | 2.0 dB |
| 6  | 3.0 dB |
| 10 | 5.0 dB |

A3Offset 이 너무 높으면 Late handover (UE 가 약한 셀에 머물러 throughput 저하).
너무 낮으면 Ping-pong (인접 두 셀 사이를 빈번하게 왕복).

### 3.3 Inter-frequency 임계값

| 파라미터 | 단위 | 일반 값 | 의미 |
|----------|------|---------|------|
| `CovInterFreqA2RsrpThld` | dBm | -105 | A2 트리거 RSRP 임계 |
| `InterFreqA2Hyst` | 0.5dB | 2 | A2 히스테리시스 |
| `CovInterFreqA5RsrpThld1` | dBm | -105 | A5 Serving 임계 |
| `CovInterFreqA5RsrpThld2` | dBm | -100 | A5 Neighbor 임계 |
| `InterFreqHoEventType` | 문자열 | `EVENT_A5` | Inter-frequency handover 트리거 이벤트 |

### 3.4 PdcchOccupiedSymbolNum

PDCCH (Physical Downlink Control Channel) 가 OFDM symbol 몇 개를 점유하는가.

- `1SYM`: control 채널 적게 → user data 공간 많음 → throughput 양호
- `2SYM`: control 채널 더 많음 → user data 공간 감소 → 그러나 control 부하 큰 셀에서 필요

---

## 4. 시나리오 데이터 구조

각 train/test scenario `data` 필드 (모두 inline pipe-separated string):

| 필드 | 내용 | 예시 행 수 |
|------|------|-----------|
| `user_plane_data` | 시계열 RF + Throughput + Top 5 Neighbor 측정 | 12 |
| `network_configuration_data` | 이 scenario 내 5개 cell 의 안테나 설정 | 5 |
| `signaling_plane_data` | A2/A3/A5 + Handover Attempt 이벤트 | 10~25 |
| `traffic_data` | 시간당 Cell 별 PRB / Throughput / CCE | 4~5 |
| `mr_data` | Mobile Report 샘플 (다른 사용자) | 5~10 |
| `notes` | 운영자 메모 (대부분 비어있음) | — |
| `collection_method` | "real" 또는 "synthesized" | — |

서버는 `X-Scenario-Id` 헤더로 시나리오 격리하여 같은 tool 호출이 다른 데이터 반환.

---

## 5. 토폴로지 시각화 (예시: train[0])

```mermaid
graph TB
    subgraph "Drive Test Area"
        UE[("UE on Vehicle<br/>22:21:31~39")]
    end

    subgraph "5 cells (PCI / Az / Tilt / Pwr / A3Off)"
        PCI362["3239189_4<br/>PCI=362<br/>Az=217° M=10° D=2°<br/>Pwr=12 A3Off=6"]
        PCI166["3239249_3<br/>PCI=166<br/>Az=67° M=3° D=11°<br/>Pwr=16 <b>A3Off=2</b>"]
        PCI966["3267220_2<br/>PCI=966<br/>Az=292° M=1° D=3°<br/>Pwr=21 <b>A3Off=2</b>"]
        PCI240["3272070_5<br/>PCI=240<br/>Az=234° M=6° D=0°<br/>Pwr=29 A3Off=6"]
        PCI420["3279943_1<br/>PCI=420<br/>Az=237° <b>M=1°</b> D=10°<br/>Pwr=18 A3Off=6<br/>※ overshoot"]
    end

    UE -- "ping-pong" --> PCI166
    UE -- "ping-pong" --> PCI966
    PCI420 -. "interfering<br/>(top neighbor RSRP -83~-89)" .-> UE

    style PCI166 fill:#FFE0E0
    style PCI966 fill:#FFE0E0
    style PCI420 fill:#FFD0D0,stroke:#f00,stroke-width:2px
```

이 scenario 의 정답 (`C2|C8|C11|C16`):
- PCI 420 overshoot → Power down + Tilt down + A3 Offset up
- PCI 166/966 ping-pong → 한쪽 A3 Offset up

---

## 6. 정답 옵션 카테고리

22개 안팎의 옵션 (C1~C22) 은 거의 모두 다음 카테고리 중 하나:

| 카테고리 | 동작 | 자주 매칭되는 패턴 |
|---------|------|-------------------|
| Tilt 조정 | `Lift` (들어올림) / `Press down` | P3 Overshoot, P6 Excessive downtilt, P4 Coverage hole |
| Azimuth 조정 | `Adjust azimuth by N degrees` | P3 Overshoot 방향, P4 Coverage hole |
| 송신 전력 | `Increase` / `Decrease transmission power` | P3 Overshoot, P4 Coverage hole |
| A3 Offset | `Increase` / `Decrease A3 Offset threshold` | P1 Late handover, P2 Ping-pong, P3 Overshoot |
| Cov Threshold | `Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1` | Inter-frequency 보강 |
| PdcchOccupiedSymbolNum | `Modify to 2SYM` | 컨트롤 채널 부하 |
| Neighbor 관계 | `Add neighbor relationship between X and Y` | 누락된 handover 후보 추가 |
| 서버/전송 | `Check test server and transmission issues` | P5 Server issue (SINR 양호 + throughput 변동) |
| 데이터 부족 | `Insufficient data; more data is needed for judgment.` | P7 — 어떤 패턴도 매칭 안 됨 |

각 scenario 의 옵션은 위 카테고리에서 무작위로 22개 정도 선택. 동일 cell 에 대해 상반된 동작 (예: tilt up vs tilt down) 이 함께 등장.

---

## 7. 다른 공식 참고자료

본 문서의 RF 공식과 임계값은 3GPP TS 38.331 (Radio Resource Control) 와 38.213 (Physical Layer Procedures for Control) 에 근거. Track A 시뮬레이터의 정확한 모델은 `data/Track A/server.py` 에 구현.

관련 문서:
- 패턴 라이브러리: `.moai/plans/track-a-opus-solutions.md` §4 (P1~P7)
- 문제 분석: `03-3_problems.md`
- 에이전트 구조: `03-1_architecture.md`
