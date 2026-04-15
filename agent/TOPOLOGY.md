# Network Topology

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
