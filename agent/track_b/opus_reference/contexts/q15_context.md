# Q15: PATH — Addressing Path Trace

**scenario_id**: c78207f0-3ea9-492f-8262-e97f6d759341
**v12 answer**: Gamma-Node-04->Gamma-Axis-01->Gamma-Portal-01->Alpha-Center-01->Delta-Portal-01->Delta-Axis-01->Delt
**deterministic solver**: 'Gamma-Node-04->Gamma-Axis-02->Gamma-Portal-02->Alpha-Center-02->Delta-Portal-02->Delta-Axis-02->Delta-Node-01' (conf=H)

## Question (from test.json)

Big Data Zone Gamma-Node-04 addressing Management Zone Delta-Node-01's GE1/0/2, the subnet mask of this interface is 30, Delta-Axis-02 route is not reachable, this node is connected to Delta-Node-01, Delta-Node-02, Delta-Axis-01
Please find the path from Gamma-Node-04 to GE1/0/2 of Delta-Node-01. Use the -> symbol to connect node names, output in one line, with no extra whitespace characters in the middle, at the beginning, or at the end.

## Path Info Extracted

- src_node: `Gamma-Node-04`
- dst_node: `Delta-Node-01`
- dst_ip: `None`
- dst_port: `GE1/0/2`

## Devices in Scenario

총 33개 장비 (관련 장비 5개 중점 분석)
관련: Delta-Node-01, Delta-Axis-02, Delta-Axis-01, Gamma-Node-04, Delta-Node-02

## Topology Snapshot — LLDP (관련 장비)

  Delta-Node-01 GE1/0/1 <-> Delta-Axis-01 GE1/0/1
  Delta-Node-01 GE1/0/2 <-> Delta-Axis-02 GE1/0/1
  Delta-Node-01 GE1/0/3 <-> Delta-Node-02 GE1/0/3
  Delta-Axis-02 GE1/0/2 <-> Delta-Node-02 GE1/0/2
  Delta-Axis-02 GE1/0/3 <-> Delta-Node-03 GE1/0/2
  Delta-Axis-02 GE1/0/4 <-> Delta-Node-04 GE1/0/2
  Delta-Axis-02 GE1/0/5 <-> Delta-Portal-01 GE1/0/2
  Delta-Axis-02 GE1/0/6 <-> Delta-Portal-02 GE1/0/2
  Delta-Axis-01 GE1/0/2 <-> Delta-Node-02 GE1/0/1
  Delta-Axis-01 GE1/0/3 <-> Delta-Node-03 GE1/0/1
  Delta-Axis-01 GE1/0/4 <-> Delta-Node-04 GE1/0/1
  Delta-Axis-01 GE1/0/5 <-> Delta-Portal-01 GE1/0/1
  Delta-Axis-01 GE1/0/6 <-> Delta-Portal-02 GE1/0/1
  Gamma-Node-04 GE1/0/1 <-> Gamma-Axis-01 GE1/0/4
  Gamma-Node-04 GE1/0/2 <-> Gamma-Axis-02 GE1/0/4
  Gamma-Node-04 GE1/0/3 <-> Gamma-Node-03 GE1/0/3

## Interface Status (IP 주소 포함)

  **Delta-Node-01**:
    GE1/0/1: 192.168.72.18/30
    GE1/0/2: 192.168.72.22/30
    GE1/0/3: 192.168.72.85/30
    LoopBack1: 192.168.72.184/32

  **Delta-Axis-02**:
    GE1/0/1: 192.168.72.21/30
    GE1/0/2: 192.168.72.29/30
    GE1/0/3: 192.168.72.37/30
    GE1/0/4: 192.168.72.45/30
    GE1/0/5: 192.168.72.5/30
    GE1/0/6: 192.168.72.13/30
    LoopBack1: 192.168.72.181/32

  **Delta-Axis-01**:
    GE1/0/1: 192.168.72.17/30
    GE1/0/2: 192.168.72.25/30
    GE1/0/3: 192.168.72.33/30
    GE1/0/4: 192.168.72.41/30
    GE1/0/5: 192.168.72.1/30
    GE1/0/6: 192.168.72.9/30
    LoopBack1: 192.168.72.180/32

  **Gamma-Node-04**:
    GE1/0/1: 192.168.70.42/30
    GE1/0/2: 192.168.70.46/30
    GE1/0/3: 192.168.70.94/30
    LoopBack1: 192.168.70.167/32

  **Delta-Node-02**:
    GE1/0/1: 192.168.72.26/30
    GE1/0/2: 192.168.72.30/30
    GE1/0/3: 192.168.72.86/30
    LoopBack1: 192.168.72.185/32


## Routing Context

  **Delta-Node-01** routing table (관련 경로):
  127.0.0.0/8          Direct   via 127.0.0.1       dev InLoopBack0
  127.0.0.1/32         Direct   via 127.0.0.1       dev InLoopBack0
  127.255.255.255/32   Direct   via 127.0.0.1       dev InLoopBack0
  192.168.65.1/32      Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.2/32      Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.128/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.132/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.136/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.140/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.144/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.148/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.152/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.156/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.160/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.164/30    Static   via 192.168.72.21   dev GE1/0/2

  **Delta-Axis-02** routing table (관련 경로):
  127.0.0.0/8          Direct   via 127.0.0.1       dev InLoopBack0
  127.0.0.1/32         Direct   via 127.0.0.1       dev InLoopBack0
  127.255.255.255/32   Direct   via 127.0.0.1       dev InLoopBack0
  192.168.65.1/32      Static   via 192.168.72.14   dev GE1/0/6
  192.168.65.2/32      Static   via 192.168.72.14   dev GE1/0/6
  192.168.65.128/30    Static   via 192.168.72.14   dev GE1/0/6
  192.168.65.132/30    Static   via 192.168.72.14   dev GE1/0/6
  192.168.65.136/30    Static   via 192.168.72.14   dev GE1/0/6
  192.168.65.140/30    Static   via 192.168.72.14   dev GE1/0/6
  192.168.65.144/30    Static   via 192.168.72.14   dev GE1/0/6
  192.168.65.148/30    Static   via 192.168.72.14   dev GE1/0/6
  192.168.65.152/30    Static   via 192.168.72.14   dev GE1/0/6
  192.168.65.156/30    Static   via 192.168.72.14   dev GE1/0/6
  192.168.65.160/30    Static   via 192.168.72.14   dev GE1/0/6
  192.168.65.164/30    Static   via 192.168.72.14   dev GE1/0/6

  **Delta-Axis-01** routing table (관련 경로):
  127.0.0.0/8          Direct   via 127.0.0.1       dev InLoopBack0
  127.0.0.1/32         Direct   via 127.0.0.1       dev InLoopBack0
  127.255.255.255/32   Direct   via 127.0.0.1       dev InLoopBack0
  192.168.65.1/32      Static   via 192.168.72.10   dev GE1/0/6
  192.168.65.2/32      Static   via 192.168.72.10   dev GE1/0/6
  192.168.65.128/30    Static   via 192.168.72.10   dev GE1/0/6
  192.168.65.132/30    Static   via 192.168.72.10   dev GE1/0/6
  192.168.65.136/30    Static   via 192.168.72.10   dev GE1/0/6
  192.168.65.140/30    Static   via 192.168.72.10   dev GE1/0/6
  192.168.65.144/30    Static   via 192.168.72.10   dev GE1/0/6
  192.168.65.148/30    Static   via 192.168.72.10   dev GE1/0/6
  192.168.65.152/30    Static   via 192.168.72.10   dev GE1/0/6
  192.168.65.156/30    Static   via 192.168.72.10   dev GE1/0/6
  192.168.65.160/30    Static   via 192.168.72.10   dev GE1/0/6
  192.168.65.164/30    Static   via 192.168.72.10   dev GE1/0/6

  **Gamma-Node-04** routing table (관련 경로):
  127.0.0.0/8          Direct   via 127.0.0.1       dev InLoopBack0
  127.0.0.1/32         Direct   via 127.0.0.1       dev InLoopBack0
  127.255.255.255/32   Direct   via 127.0.0.1       dev InLoopBack0
  192.168.65.1/32      Static   via 192.168.70.45   dev GE1/0/2
  192.168.65.2/32      Static   via 192.168.70.45   dev GE1/0/2
  192.168.65.128/30    Static   via 192.168.70.45   dev GE1/0/2
  192.168.65.132/30    Static   via 192.168.70.45   dev GE1/0/2
  192.168.65.136/30    Static   via 192.168.70.45   dev GE1/0/2
  192.168.65.140/30    Static   via 192.168.70.45   dev GE1/0/2
  192.168.65.144/30    Static   via 192.168.70.45   dev GE1/0/2
  192.168.65.148/30    Static   via 192.168.70.45   dev GE1/0/2
  192.168.65.152/30    Static   via 192.168.70.45   dev GE1/0/2
  192.168.65.156/30    Static   via 192.168.70.45   dev GE1/0/2
  192.168.65.160/30    Static   via 192.168.70.45   dev GE1/0/2
  192.168.65.164/30    Static   via 192.168.70.45   dev GE1/0/2

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


## Raw File References

  data/Track B/devices_outputs/15/Delta-Node-01/display_ip_routing-table.txt
  data/Track B/devices_outputs/15/Delta-Node-01/display_ip_interface_brief.txt
  data/Track B/devices_outputs/15/Delta-Axis-02/display_ip_routing-table.txt
  data/Track B/devices_outputs/15/Delta-Axis-02/display_ip_interface_brief.txt
  data/Track B/devices_outputs/15/Delta-Axis-01/display_ip_routing-table.txt
  data/Track B/devices_outputs/15/Delta-Axis-01/display_ip_interface_brief.txt
  data/Track B/devices_outputs/15/Gamma-Node-04/display_ip_routing-table.txt
  data/Track B/devices_outputs/15/Gamma-Node-04/display_ip_interface_brief.txt
  data/Track B/devices_outputs/15/Delta-Node-02/display_ip_routing-table.txt
  data/Track B/devices_outputs/15/Delta-Node-02/display_ip_interface_brief.txt

## Deterministic Solver Result

```
Gamma-Node-04->Gamma-Axis-02->Gamma-Portal-02->Alpha-Center-02->Delta-Portal-02->Delta-Axis-02->Delta-Node-01
```

## v12 Answer (검증 대상)

```
Gamma-Node-04->Gamma-Axis-01->Gamma-Portal-01->Alpha-Center-01->Delta-Portal-01->Delta-Axis-01->Delta-Node-01
```