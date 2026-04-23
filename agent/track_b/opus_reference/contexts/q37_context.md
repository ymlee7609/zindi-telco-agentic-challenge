# Q37: PATH — Addressing Path Trace

**scenario_id**: 66a84648-2cde-4026-be8f-29a1b52cd70f
**v12 answer**: Hermes-Node-01->Demeter-Node-01->Atlas-Node-01->Demeter-Node-02->Hermes-Node-02
**deterministic solver**: 'Hermes-Node-01->Demeter-Node-01->Atlas-Node-01->Demeter-Node-02->Hermes-Node-02' (conf=M)

## Question (from test.json)

PJGFA area, the path from Hermes-Node-01 to address 20.1.1.20
Format requirement: Connect node names using the -> symbol, output in one line, with no extra whitespace characters in the middle, at the beginning, or at the end.

## Path Info Extracted

- src_node: `Hermes-Node-01`
- dst_node: `None`
- dst_ip: `20.1.1.20`
- dst_port: `None`

## Devices in Scenario

총 23개 장비 (관련 장비 1개 중점 분석)
관련: Hermes-Node-01

## Topology Snapshot — LLDP (관련 장비)

  Hermes-Node-01 GE1/0/0 <-> Demeter-Node-01 GE1/0/3

## Interface Status (IP 주소 포함)

  **Hermes-Node-01**:
    Vlanif10: 20.1.1.10/24
    Vlanif20: 20.1.2.10/24
    Vlanif30: 20.1.3.10/24
    Vlanif40: 20.1.4.10/24
    Vlanif50: 20.1.5.10/24
    Vlanif60: 22.1.1.10/24


## Routing Context

  **Hermes-Node-01** routing table (관련 경로):
  20.1.1.255/32        Direct   via 127.0.0.1       dev Vlanif10


## Raw File References

  data/Track B/devices_outputs/37/Hermes-Node-01/display_ip_routing-table.txt
  data/Track B/devices_outputs/37/Hermes-Node-01/display_ip_interface_brief.txt

## Deterministic Solver Result

```
Hermes-Node-01->Demeter-Node-01->Atlas-Node-01->Demeter-Node-02->Hermes-Node-02
```

## v12 Answer (검증 대상)

```
Hermes-Node-01->Demeter-Node-01->Atlas-Node-01->Demeter-Node-02->Hermes-Node-02
```