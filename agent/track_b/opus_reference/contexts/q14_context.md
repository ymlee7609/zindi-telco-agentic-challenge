# Q14: PATH — Addressing Path Trace

**scenario_id**: c03fb42a-863f-4154-bfdc-e05fdf73b958
**v12 answer**: Delta-Node-02->Delta-Axis-01->Delta-Portal-01->Alpha-Center-01->Gamma-Portal-01->Gamma-Axis-01->Gamm
**deterministic solver**: 'Delta-Node-02->Delta-Axis-02->Delta-Portal-02->Alpha-Center-02->Gamma-Portal-02->Gamma-Axis-02->Gamma-Node-02' (conf=H)

## Question (from test.json)

Delta-Node-02 addressing the destination GE1/0/2 of Gamma-Node-02, Gamma-Node-02 is connected to Gamma-Node-01, Gamma-Axis-02, and Gamma-Axis-01
The path from Delta-Node-02 addressing the destination Gamma-Node-02's GE1/0/2. Use the -> symbol to connect between node names, output in one line, with no extra whitespace characters in the middle, at the beginning, or at the end.

## Path Info Extracted

- src_node: `Delta-Node-02`
- dst_node: `Gamma-Node-02`
- dst_ip: `None`
- dst_port: `GE1/0/2`

## Devices in Scenario

총 33개 장비 (관련 장비 5개 중점 분석)
관련: Gamma-Node-01, Gamma-Node-02, Gamma-Axis-01, Delta-Node-02, Gamma-Axis-02

## Topology Snapshot — LLDP (관련 장비)

  Gamma-Node-01 GE1/0/1 <-> Gamma-Axis-01 GE1/0/1
  Gamma-Node-01 GE1/0/2 <-> Gamma-Axis-02 GE1/0/1
  Gamma-Node-01 GE1/0/3 <-> Gamma-Node-02 GE1/0/3
  Gamma-Node-02 GE1/0/1 <-> Gamma-Axis-01 GE1/0/2
  Gamma-Node-02 GE1/0/2 <-> Gamma-Axis-02 GE1/0/2
  Gamma-Axis-01 GE1/0/3 <-> Gamma-Node-03 GE1/0/1
  Gamma-Axis-01 GE1/0/4 <-> Gamma-Node-04 GE1/0/1
  Gamma-Axis-01 GE1/0/5 <-> Gamma-Portal-01 GE1/0/1
  Gamma-Axis-01 GE1/0/6 <-> Gamma-Portal-02 GE1/0/1
  Delta-Node-02 GE1/0/1 <-> Delta-Axis-01 GE1/0/2
  Delta-Node-02 GE1/0/2 <-> Delta-Axis-02 GE1/0/2
  Delta-Node-02 GE1/0/3 <-> Delta-Node-01 GE1/0/3
  Gamma-Axis-02 GE1/0/3 <-> Gamma-Node-03 GE1/0/2
  Gamma-Axis-02 GE1/0/4 <-> Gamma-Node-04 GE1/0/2
  Gamma-Axis-02 GE1/0/5 <-> Gamma-Portal-01 GE1/0/2
  Gamma-Axis-02 GE1/0/6 <-> Gamma-Portal-02 GE1/0/2

## Interface Status (IP 주소 포함)

  **Gamma-Node-01**:
    GE1/0/1: 192.168.70.18/30
    GE1/0/2: 192.168.70.22/30
    GE1/0/3: 192.168.70.85/30
    LoopBack1: 192.168.70.164/32

  **Gamma-Node-02**:
    GE1/0/1: 192.168.70.26/30
    GE1/0/2: 192.168.70.30/30
    GE1/0/3: 192.168.70.86/30
    LoopBack1: 192.168.70.165/32

  **Gamma-Axis-01**:
    GE1/0/1: 192.168.70.17/30
    GE1/0/2: 192.168.70.25/30
    GE1/0/3: 192.168.70.33/30
    GE1/0/4: 192.168.70.41/30
    GE1/0/5: 192.168.70.1/30
    GE1/0/6: 192.168.70.9/30
    LoopBack1: 192.168.70.160/32

  **Delta-Node-02**:
    GE1/0/1: 192.168.72.26/30
    GE1/0/2: 192.168.72.30/30
    GE1/0/3: 192.168.72.86/30
    LoopBack1: 192.168.72.185/32

  **Gamma-Axis-02**:
    GE1/0/1: 192.168.70.21/30
    GE1/0/2: 192.168.70.29/30
    GE1/0/3: 192.168.70.37/30
    GE1/0/4: 192.168.70.45/30
    GE1/0/5: 192.168.70.5/30
    GE1/0/6: 192.168.70.13/30
    LoopBack1: 192.168.70.161/32


## Routing Context

  **Gamma-Node-01** routing table (관련 경로):
  127.0.0.0/8          Direct   via 127.0.0.1       dev InLoopBack0
  127.0.0.1/32         Direct   via 127.0.0.1       dev InLoopBack0
  127.255.255.255/32   Direct   via 127.0.0.1       dev InLoopBack0
  192.168.65.1/32      Static   via 192.168.70.21   dev GE1/0/2
  192.168.65.2/32      Static   via 192.168.70.21   dev GE1/0/2
  192.168.65.128/30    Static   via 192.168.70.21   dev GE1/0/2
  192.168.65.132/30    Static   via 192.168.70.21   dev GE1/0/2
  192.168.65.136/30    Static   via 192.168.70.21   dev GE1/0/2
  192.168.65.140/30    Static   via 192.168.70.21   dev GE1/0/2
  192.168.65.144/30    Static   via 192.168.70.21   dev GE1/0/2
  192.168.65.148/30    Static   via 192.168.70.21   dev GE1/0/2
  192.168.65.152/30    Static   via 192.168.70.21   dev GE1/0/2
  192.168.65.156/30    Static   via 192.168.70.21   dev GE1/0/2
  192.168.65.160/30    Static   via 192.168.70.21   dev GE1/0/2
  192.168.65.164/30    Static   via 192.168.70.21   dev GE1/0/2

  **Gamma-Node-02** routing table (관련 경로):
  127.0.0.0/8          Direct   via 127.0.0.1       dev InLoopBack0
  127.0.0.1/32         Direct   via 127.0.0.1       dev InLoopBack0
  127.255.255.255/32   Direct   via 127.0.0.1       dev InLoopBack0
  192.168.65.1/32      Static   via 192.168.70.29   dev GE1/0/2
  192.168.65.2/32      Static   via 192.168.70.29   dev GE1/0/2
  192.168.65.128/30    Static   via 192.168.70.29   dev GE1/0/2
  192.168.65.132/30    Static   via 192.168.70.29   dev GE1/0/2
  192.168.65.136/30    Static   via 192.168.70.29   dev GE1/0/2
  192.168.65.140/30    Static   via 192.168.70.29   dev GE1/0/2
  192.168.65.144/30    Static   via 192.168.70.29   dev GE1/0/2
  192.168.65.148/30    Static   via 192.168.70.29   dev GE1/0/2
  192.168.65.152/30    Static   via 192.168.70.29   dev GE1/0/2
  192.168.65.156/30    Static   via 192.168.70.29   dev GE1/0/2
  192.168.65.160/30    Static   via 192.168.70.29   dev GE1/0/2
  192.168.65.164/30    Static   via 192.168.70.29   dev GE1/0/2

  **Gamma-Axis-01** routing table (관련 경로):
  127.0.0.0/8          Direct   via 127.0.0.1       dev InLoopBack0
  127.0.0.1/32         Direct   via 127.0.0.1       dev InLoopBack0
  127.255.255.255/32   Direct   via 127.0.0.1       dev InLoopBack0
  192.168.65.1/32      Static   via 192.168.70.10   dev GE1/0/6
  192.168.65.2/32      Static   via 192.168.70.10   dev GE1/0/6
  192.168.65.128/30    Static   via 192.168.70.10   dev GE1/0/6
  192.168.65.132/30    Static   via 192.168.70.10   dev GE1/0/6
  192.168.65.136/30    Static   via 192.168.70.10   dev GE1/0/6
  192.168.65.140/30    Static   via 192.168.70.10   dev GE1/0/6
  192.168.65.144/30    Static   via 192.168.70.10   dev GE1/0/6
  192.168.65.148/30    Static   via 192.168.70.10   dev GE1/0/6
  192.168.65.152/30    Static   via 192.168.70.10   dev GE1/0/6
  192.168.65.156/30    Static   via 192.168.70.10   dev GE1/0/6
  192.168.65.160/30    Static   via 192.168.70.10   dev GE1/0/6
  192.168.65.164/30    Static   via 192.168.70.10   dev GE1/0/6

  **Delta-Node-02** routing table (관련 경로):
  127.0.0.0/8          Direct   via 127.0.0.1       dev InLoopBack0
  127.0.0.1/32         Direct   via 127.0.0.1       dev InLoopBack0
  127.255.255.255/32   Direct   via 127.0.0.1       dev InLoopBack0
  192.168.65.1/32      Static   via 192.168.72.29   dev GE1/0/2
  192.168.65.2/32      Static   via 192.168.72.29   dev GE1/0/2
  192.168.65.128/30    Static   via 192.168.72.29   dev GE1/0/2
  192.168.65.132/30    Static   via 192.168.72.29   dev GE1/0/2
  192.168.65.136/30    Static   via 192.168.72.29   dev GE1/0/2
  192.168.65.140/30    Static   via 192.168.72.29   dev GE1/0/2
  192.168.65.144/30    Static   via 192.168.72.29   dev GE1/0/2
  192.168.65.148/30    Static   via 192.168.72.29   dev GE1/0/2
  192.168.65.152/30    Static   via 192.168.72.29   dev GE1/0/2
  192.168.65.156/30    Static   via 192.168.72.29   dev GE1/0/2
  192.168.65.160/30    Static   via 192.168.72.29   dev GE1/0/2
  192.168.65.164/30    Static   via 192.168.72.29   dev GE1/0/2

  **Gamma-Axis-02** routing table (관련 경로):
  127.0.0.0/8          Direct   via 127.0.0.1       dev InLoopBack0
  127.0.0.1/32         Direct   via 127.0.0.1       dev InLoopBack0
  127.255.255.255/32   Direct   via 127.0.0.1       dev InLoopBack0
  192.168.65.1/32      Static   via 192.168.70.14   dev GE1/0/6
  192.168.65.2/32      Static   via 192.168.70.14   dev GE1/0/6
  192.168.65.128/30    Static   via 192.168.70.14   dev GE1/0/6
  192.168.65.132/30    Static   via 192.168.70.14   dev GE1/0/6
  192.168.65.136/30    Static   via 192.168.70.14   dev GE1/0/6
  192.168.65.140/30    Static   via 192.168.70.14   dev GE1/0/6
  192.168.65.144/30    Static   via 192.168.70.14   dev GE1/0/6
  192.168.65.148/30    Static   via 192.168.70.14   dev GE1/0/6
  192.168.65.152/30    Static   via 192.168.70.14   dev GE1/0/6
  192.168.65.156/30    Static   via 192.168.70.14   dev GE1/0/6
  192.168.65.160/30    Static   via 192.168.70.14   dev GE1/0/6
  192.168.65.164/30    Static   via 192.168.70.14   dev GE1/0/6


## Raw File References

  data/Track B/devices_outputs/14/Gamma-Node-01/display_ip_routing-table.txt
  data/Track B/devices_outputs/14/Gamma-Node-01/display_ip_interface_brief.txt
  data/Track B/devices_outputs/14/Gamma-Node-02/display_ip_routing-table.txt
  data/Track B/devices_outputs/14/Gamma-Node-02/display_ip_interface_brief.txt
  data/Track B/devices_outputs/14/Gamma-Axis-01/display_ip_routing-table.txt
  data/Track B/devices_outputs/14/Gamma-Axis-01/display_ip_interface_brief.txt
  data/Track B/devices_outputs/14/Delta-Node-02/display_ip_routing-table.txt
  data/Track B/devices_outputs/14/Delta-Node-02/display_ip_interface_brief.txt
  data/Track B/devices_outputs/14/Gamma-Axis-02/display_ip_routing-table.txt
  data/Track B/devices_outputs/14/Gamma-Axis-02/display_ip_interface_brief.txt

## Deterministic Solver Result

```
Delta-Node-02->Delta-Axis-02->Delta-Portal-02->Alpha-Center-02->Gamma-Portal-02->Gamma-Axis-02->Gamma-Node-02
```

## v12 Answer (검증 대상)

```
Delta-Node-02->Delta-Axis-01->Delta-Portal-01->Alpha-Center-01->Gamma-Portal-01->Gamma-Axis-01->Gamma-Node-02
```