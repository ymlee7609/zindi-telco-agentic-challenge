# Network Topology

## 개요

이 문서는 Zindi Telco Troubleshooting Challenge Track B (Phase 1)에서 사용되는 네트워크 토폴로지를 설명합니다. 챌린지에는 **두 개의 독립적인 네트워크**가 존재합니다.

| 네트워크 | 용도 | 노드 수 | 아키텍처 | 프로토콜 |
|----------|------|---------|----------|----------|
| **금융 네트워크** | 금융기관의 데이터센터 네트워크 | 32 | 전통적 3-Tier (Core-Aggregation-Access) | Static Route, OSPF |
| **클라우드 컴퓨팅 네트워크 (PJ Area)** | 클라우드 서비스 인프라 | 22 | Spine-Leaf VXLAN Fabric | VXLAN, BGP EVPN, OSPF |

### 두 네트워크의 관계
- **완전히 독립된 네트워크**: 금융 네트워크와 PJ Area는 직접 연결되어 있지 않습니다.
- **별도의 문제 세트**: Q1~Q28은 금융 네트워크, Q29~Q50은 PJ Area 문제입니다.
- **같은 장비 제조사**: 모든 장비는 Huawei CE12800 시리즈 (일부 Cisco PSS).
- PJ Area의 PX1 장비는 외부 네트워크(인터넷/WAN) 게이트웨이 역할.

---

## 1. 금융 네트워크 (32노드)

금융기관의 데이터센터를 시뮬레이션한 전통적 3-Tier 네트워크입니다.

### 구조
- **Core Layer** (코어): Alpha-Center-01/02 — 모든 Zone을 연결하는 백본 라우터
- **Aggregation Layer** (집선): Portal — Zone별 상위 집선 스위치, Aegis — 방화벽/보안 장비
- **Access Layer** (액세스): Axis — 서버 접속 스위치, Node — 서버/호스트

### Zone 설명

| Zone | 접두사 | 용도 | 구성 |
|------|--------|------|------|
| **Core** | Alpha-Center | 백본 라우팅, Zone 간 트래픽 중계 | 2대 (이중화) |
| **Dev/Test Zone** | Beta-* | 개발/테스트 환경 | Portal 2 + Aegis 2 + Axis 2 + Node 4 = 10대 |
| **Big Data Zone** | Gamma-* | 빅데이터 처리 환경 | Portal 2 + Aegis 2 + Axis 2 + Node 4 = 10대 |
| **Management Zone** | Delta-* | 운영 관리 환경 | Portal 2 + Axis 2 + Node 4 = 8대 |

### 라우팅
- Zone 내부: 직접 연결 (L2) + Static Route
- Zone 간: Alpha-Center를 경유하는 Static Route (예: Beta→Gamma는 Beta-Portal→Alpha-Center→Gamma-Portal)
- 일부 구간 OSPF 사용

### 해당 문제
- **Q1~Q6**: Topology (링크 복원)
- **Q7~Q16**: Path (경로 추적) — Zone 간 hop-by-hop 라우팅
- **Q17~Q28**: Fault (장애 진단) — 용의 노드에서 missing route, shutdown 등

## 전체 네트워크 구조 (Zone 간 연결)

```mermaid
graph TB
    subgraph CoreZone[Core Zone]
        AC01[Alpha-Center-01]
        AC02[Alpha-Center-02]
    end
    subgraph BetaZone[Dev/Test Zone - Beta]
        BP01[Beta-Portal-01]
        BP02[Beta-Portal-02]
        BA01[Beta-Aegis-01]
        BA02[Beta-Aegis-02]
        BX01[Beta-Axis-01]
        BX02[Beta-Axis-02]
        BN01[Beta-Node-01]
        BN02[Beta-Node-02]
        BN03[Beta-Node-03]
        BN04[Beta-Node-04]
    end
    subgraph GammaZone[Big Data Zone - Gamma]
        GP01[Gamma-Portal-01]
        GP02[Gamma-Portal-02]
        GA01[Gamma-Aegis-01]
        GA02[Gamma-Aegis-02]
        GX01[Gamma-Axis-01]
        GX02[Gamma-Axis-02]
        GN01[Gamma-Node-01]
        GN02[Gamma-Node-02]
        GN03[Gamma-Node-03]
        GN04[Gamma-Node-04]
    end
    subgraph DeltaZone[Management Zone - Delta]
        DP01[Delta-Portal-01]
        DP02[Delta-Portal-02]
        DX01[Delta-Axis-01]
        DX02[Delta-Axis-02]
        DN01[Delta-Node-01]
        DN02[Delta-Node-02]
        DN03[Delta-Node-03]
        DN04[Delta-Node-04]
    end

    %% Core-to-Zone connections
    AC01 --- BP01
    AC01 --- GP01
    AC01 --- DP01
    AC02 --- BP02
    AC02 --- GP02
    AC02 --- DP02

    %% Beta internal
    BP01 --- BX01
    BP01 --- BX02
    BP01 --- BP02
    BP01 --- BA01
    BP01 --- BA02
    BP02 --- BX01
    BP02 --- BX02
    BP02 --- BA01
    BP02 --- BA02
    BA01 --- BA02
    BX01 --- BN01
    BX01 --- BN02
    BX01 --- BN03
    BX01 --- BN04
    BX02 --- BN01
    BX02 --- BN02
    BX02 --- BN03
    BX02 --- BN04
    BN01 --- BN02
    BN03 --- BN04

    %% Gamma internal
    GP01 --- GX01
    GP01 --- GX02
    GP01 --- GP02
    GP01 --- GA01
    GP01 --- GA02
    GP02 --- GX01
    GP02 --- GX02
    GP02 --- GA01
    GP02 --- GA02
    GA01 --- GA02
    GX01 --- GN01
    GX01 --- GN02
    GX01 --- GN03
    GX01 --- GN04
    GX02 --- GN01
    GX02 --- GN02
    GX02 --- GN03
    GX02 --- GN04
    GN01 --- GN02
    GN03 --- GN04

    %% Delta internal
    DP01 --- DX01
    DP01 --- DX02
    DP01 --- DP02
    DP02 --- DX01
    DP02 --- DX02
    DX01 --- DN01
    DX01 --- DN02
    DX01 --- DN03
    DX01 --- DN04
    DX02 --- DN01
    DX02 --- DN02
    DX02 --- DN03
    DX02 --- DN04
    DN01 --- DN02
    DN03 --- DN04
```

---

## 2. 클라우드 컴퓨팅 네트워크 — PJ Area (22노드)

클라우드 서비스 인프라를 시뮬레이션한 현대적 Spine-Leaf VXLAN Fabric입니다.

### 구조
최신 데이터센터 아키텍처인 **Spine-Leaf** 구조를 채택하고, **VXLAN**으로 L2 오버레이 네트워크를 구성합니다.

| 계층 | 장비 | 역할 |
|------|------|------|
| **Spine** | Janus-Prime-01/02 | Fabric 백본 — Leaf 간 트래픽 중계 |
| **Leaf** | Atlas-Prime-01/02, Aegis-Prime-01/02 | Spine에 연결, VTEP으로 트래픽 라우팅 |
| **VTEP (Leaf-Edge)** | Demeter-Prime-01/02 | VXLAN 터널 종단점, L2/L3 게이트웨이 |
| **Access** | Hermes-Prime-01/02 | 서버/호스트 접속 스위치 |
| **External** | PX1 | WAN/인터넷 게이트웨이 (Janus-Prime-01과 연결) |

### PJGFA 서브영역
PJ Area 내의 별도 소규모 네트워크로, 동일한 Spine-Leaf 패턴을 따릅니다.

| 역할 | 장비 |
|------|------|
| Spine | Janus-Node-01/02 |
| Leaf | Atlas-Node-01/02, Aegis-Node-01 |
| VTEP | Demeter-Node-01/02 |
| Access | Hermes-Node-01/02 |

### 프로토콜
- **언더레이**: OSPF (Spine-Leaf 간 IP 라우팅)
- **오버레이**: VXLAN + BGP EVPN (L2 확장, MAC 학습)
- **VPN**: VRF 기반 테넌트 분리 (vpn1~vpn6)
- **VLAN**: 테넌트별 VLAN (10, 20, 30, 40, 50, 60 등)

### 데이터 흐름 (예: Hermes-Prime-01 → Hermes-Prime-02)
```
Hermes-Prime-01 (VLAN 10)
  → Demeter-Prime-01 (VTEP: VXLAN 캡슐화)
    → [OSPF 언더레이: Atlas-Prime → 경유]
      → Demeter-Prime-02 (VTEP: VXLAN 디캡슐화)
        → Hermes-Prime-02 (VLAN 10)
```

### 해당 문제
- **Q29~Q33**: Topology (링크 복원)
- **Q34~Q38**: Path (경로 추적) — VXLAN 오버레이/언더레이 경로
- **Q39~Q50**: Fault (장애 진단) — missing route, MAC 충돌, VXLAN 설정 오류 등

## PJ Area 토폴로지

```mermaid
graph TB
    subgraph Spine[Spine Layer]
        JP01[Janus-Prime-01]
        JP02[Janus-Prime-02]
    end
    subgraph Leaf[Leaf Layer]
        AP01[Atlas-Prime-01]
        AP02[Atlas-Prime-02]
        AE01[Aegis-Prime-01]
    end
    subgraph VTEP[VTEP / Leaf-Edge]
        DP01p[Demeter-Prime-01]
        DP02p[Demeter-Prime-02]
    end
    subgraph Access[Access / Host]
        HP01[Hermes-Prime-01]
        HP02[Hermes-Prime-02]
    end
    subgraph PJGFA[PJGFA Sub-Area]
        JN01[Janus-Node-01]
        JN02[Janus-Node-02]
        AN01[Atlas-Node-01]
        AN02[Atlas-Node-02]
        AEN01[Aegis-Node-01]
        DN01p[Demeter-Node-01]
        DN02p[Demeter-Node-02]
        HN01[Hermes-Node-01]
        HN02[Hermes-Node-02]
    end

    %% Spine-Leaf
    JP01 --- AP01
    JP01 --- AP02
    JP01 --- AE01
    JP01 --- JP02
    JP02 --- AP01
    JP02 --- AP02
    JP02 --- AE01

    %% Leaf-VTEP
    AP01 --- DP01p
    AP01 --- DP02p
    AP02 --- DP01p
    AP02 --- DP02p

    %% VTEP-Access
    DP01p --- HP01
    DP02p --- HP02

    %% PJGFA sub-area
    JN01 --- JN02
    JN01 --- AN01
    JN01 --- AN02
    JN01 --- AEN01
    JN02 --- AN01
    JN02 --- AN02
    JN02 --- AEN01
    DN01p --- HN01
    DN02p --- HN02

    %% External
    JP01 -.- PX1[External/PX1]
```

---

## 3. 장비 공통 정보

### 제조사 및 모델
| 장비 | 제조사 | 모델 | OS |
|------|--------|------|----|
| 대부분 (Alpha~Hermes) | Huawei | CE12800 시리즈 | VRP V800R023C10 |
| PSS | Cisco | - | IOS |

### 데이터 소스 (NOC API가 제공하는 정보)
서버(server.py)는 `devices_outputs/{question_number}/{device_name}/` 디렉토리의 사전 생성된 텍스트 파일을 반환합니다. 각 문제마다 독립적인 데이터를 가지며, 같은 장비라도 문제에 따라 다른 설정/상태를 반환합니다 (장애 시뮬레이션).

### 연결 정보 확인 방법
1. **description 필드** (가장 신뢰): `display current-configuration`에서 `From_NodeA_PortX_To_NodeB_PortY`
2. **LLDP**: `display lldp neighbor brief` (일부 문제에서 "No permission" 반환)
3. **ARP**: `display arp`로 IP-MAC-포트 매핑

## 네트워크 계층 구조

```
┌─────────────────────────────────────────────────────────────────┐
│                        Core Layer                               │
│              Alpha-Center-01    Alpha-Center-02                  │
├──────────┬──────────────────────────────┬───────────────────────┤
│ Beta     │         Gamma                │ Delta                 │
│ (Dev/Test)│       (Big Data)             │ (Management)          │
│          │                              │                       │
│ Portal-01│ Portal-01    Portal-02       │ Portal-01  Portal-02  │
│ Portal-02│ Aegis-01     Aegis-02        │                       │
│ Aegis-01 │ Axis-01      Axis-02         │ Axis-01    Axis-02    │
│ Aegis-02 │   │Node-01     │Node-01      │   │Node-01   │Node-01│
│ Axis-01  │   │Node-02     │Node-02      │   │Node-02   │Node-02│
│ Axis-02  │   │Node-03     │Node-03      │   │Node-03   │Node-03│
│  │Node-01│   │Node-04     │Node-04      │   │Node-04   │Node-04│
│  │Node-02│                              │                       │
│  │Node-03│                              │                       │
│  │Node-04│                              │                       │
└──────────┴──────────────────────────────┴───────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                     PJ Area (VXLAN Fabric)                       │
│ Spine:  Janus-Prime-01 ──── Janus-Prime-02                      │
│ Leaf:   Atlas-Prime-01  Atlas-Prime-02  Aegis-Prime-01          │
│ VTEP:   Demeter-Prime-01              Demeter-Prime-02          │
│ Access: Hermes-Prime-01                Hermes-Prime-02          │
│                                                                  │
│ PJGFA Sub:  Janus-Node-01/02, Atlas-Node-01/02, Aegis-Node-01  │
│             Demeter-Node-01/02, Hermes-Node-01/02              │
└─────────────────────────────────────────────────────────────────┘
```
