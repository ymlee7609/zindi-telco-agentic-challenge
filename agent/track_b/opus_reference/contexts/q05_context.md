# Q5: TOPO — Link Restore (Delta-Node-01)

**scenario_id**: 50bb98fe-22f7-4f09-935d-8d53dc2f10f0
**v12 answer**: Delta-Node-01(GE1/0/1)->Delta-Axis-01(GE1/0/1)\nDelta-Node-01(GE1/0/2)->Delta-Axis-02(GE1/0/1)\nDelta-Node-01(GE1/0/3)->Delta-Node-02(GE1/0/3)
**deterministic solver**: confidence=H, method=mixed, resolved=3/3 ports

## Question (from test.json)

The planned data of Delta-Node-01 has been accidentally deleted, and it is necessary to restore the link status of the interfaces whose state is UP on this node. The link status of interfaces can be queried through several methods: 1. Query the link state; 2. Query the interface description (which contains the remote node and remote port), and then confirm the link state through the port and IP correspondence information in the ARP tables of this node and the remote node. If the interface description and the ARP table port information are different, the ARP table port information shall prevail. Link state query is the preferred query method. When this state cannot be queried, use the second method to confirm the port link status.
Based on the actual network topology, supplement and plan the topology links for Delta-Node-01. Format requirement: local-end node name(local-end port number)->remote-end node name(remote-end port number). Each line represents one link, with no extra blank lines in the middle or at the end, and no extra whitespace characters before, after, or within each line.

## Devices in Scenario

총 33개 장비: Alpha-Center-01, Alpha-Center-02, Beta-Aegis-01, Beta-Aegis-02, Beta-Axis-01, Beta-Axis-02, Beta-Node-01, Beta-Node-02, Beta-Node-03, Beta-Node-04 ... 외 23개

**Target**: `Delta-Node-01`

## Topology Snapshot — LLDP Graph

### 타겟 장비 직접 LLDP neighbors

  Delta-Node-01 GE1/0/1 <-> Delta-Axis-01 GE1/0/1
  Delta-Node-01 GE1/0/2 <-> Delta-Axis-02 GE1/0/1
  Delta-Node-01 GE1/0/3 <-> Delta-Node-02 GE1/0/3

### 역방향 LLDP (타겟이 neighbor로 등장)

  Delta-Axis-01 GE1/0/1 <-> Delta-Node-01 GE1/0/1
  Delta-Axis-02 GE1/0/1 <-> Delta-Node-01 GE1/0/2
  Delta-Node-02 GE1/0/3 <-> Delta-Node-01 GE1/0/3

## Interface Description (타겟 장비)

  GE1/0/1: From_Delta-Node-01_GE1/0/1_To_Delta-Axis-01_GE1/0/1
  GE1/0/2: From_Delta-Node-01_GE1/0/2_To_Delta-Axis-02_GE1/0/1
  GE1/0/3: From_Delta-Node-01_GE1/0/3_To_Delta-Node-02_GE1/0/3

## Interface Status

**Delta-Node-01** UP interfaces:
  GE1/0/1 [192.168.72.18/30]
  GE1/0/2 [192.168.72.22/30]
  GE1/0/3 [192.168.72.85/30]

## ARP Mappings


  [Delta-Node-01]
  192.168.72.18   3800-3511-0101        I               GE1/0/1
  192.168.72.22   3800-3511-0102        I               GE1/0/2
  192.168.72.85   3800-3511-0103        I               GE1/0/3

  [Delta-Node-02]
  192.168.72.26   3814-2011-0101        I               GE1/0/1
  192.168.72.30   3814-2011-0102        I               GE1/0/2
  192.168.72.86   3814-2011-0103        I               GE1/0/3

  [Delta-Axis-02]
  192.168.72.21   3897-0711-0101        I               GE1/0/1
  192.168.72.29   3897-0711-0102        I               GE1/0/2
  192.168.72.37   3897-0711-0103        I               GE1/0/3
  192.168.72.45   3897-0711-0104        I               GE1/0/4
  192.168.72.5    3897-0711-0105        I               GE1/0/5
  192.168.72.13   3897-0711-0106        I               GE1/0/6

  [Delta-Axis-01]
  192.168.72.17   3804-2011-0101        I               GE1/0/1
  192.168.72.25   3804-2011-0102        I               GE1/0/2
  192.168.72.33   3804-2011-0103        I               GE1/0/3
  192.168.72.41   3804-2011-0104        I               GE1/0/4
  192.168.72.1    3804-2011-0105        I               GE1/0/5
  192.168.72.9    3804-2011-0106        I               GE1/0/6

## Raw File References

  data/Track B/devices_outputs/5/Delta-Node-01/display_interface_brief.txt
  data/Track B/devices_outputs/5/Delta-Node-01/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/5/Delta-Node-01/display_interface_description.txt
  data/Track B/devices_outputs/5/Delta-Node-01/display_arp.txt
  data/Track B/devices_outputs/5/Delta-Node-02/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/5/Delta-Axis-02/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/5/Delta-Axis-01/display_lldp_neighbor_brief.txt

## Deterministic Solver Result

```
Delta-Node-01(GE1/0/1)->Delta-Axis-01(GE1/0/1)
Delta-Node-01(GE1/0/2)->Delta-Axis-02(GE1/0/1)
Delta-Node-01(GE1/0/3)->Delta-Node-02(GE1/0/3)
```

## v12 Answer (검증 대상)

```
Delta-Node-01(GE1/0/1)->Delta-Axis-01(GE1/0/1)\nDelta-Node-01(GE1/0/2)->Delta-Axis-02(GE1/0/1)\nDelta-Node-01(GE1/0/3)->Delta-Node-02(GE1/0/3)
```