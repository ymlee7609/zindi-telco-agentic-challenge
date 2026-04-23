# Q1: TOPO — Link Restore (Gamma-Aegis-01)

**scenario_id**: 535afb0d-fa81-419b-9bcc-b456d032df5d
**v12 answer**: Gamma-Aegis-01(GE1/0/0)->Gamma-Portal-01(GE1/0/4)\nGamma-Aegis-01(GE1/0/1)->Gamma-Portal-02(GE1/0/4)\nGamma-Aegis-01(GE1/0/2)->Gamma-Aegis-02(GE1/0/2)
**deterministic solver**: confidence=H, method=mixed, resolved=3/3 ports

## Question (from test.json)

The link planning data of Gamma-Aegis-01 within the Big Data Zone has been accidentally deleted, and it is necessary to restore the link connections of the interfaces whose status is UP on the Gamma-Aegis-01 node. The link status of interfaces can be queried through several methods: 1. Query the link status directly. 2. Query the interface description (which contains the remote node and remote port), and then confirm the link status through the port and IP correspondence information in the ARP tables of the local node and the remote node. If the interface description and the ARP table port information are different, the ARP table port information shall prevail. Link status query is the preferred query method. When the status cannot be queried through that method, use the second method to confirm the port connections.
Based on the actual network topology, supplement the link information for the interfaces that are UP on the Gamma-Aegis-01 node in the plan. Format requirement: local node name(local port number)->remote node name(remote port number). Each line represents one link, with no extra blank lines in the middle or at the end, and no extra whitespace characters before, after, or within each line.

## Devices in Scenario

총 33개 장비: Alpha-Center-01, Alpha-Center-02, Beta-Aegis-01, Beta-Aegis-02, Beta-Axis-01, Beta-Axis-02, Beta-Node-01, Beta-Node-02, Beta-Node-03, Beta-Node-04 ... 외 23개

**Target**: `Gamma-Aegis-01`

## Topology Snapshot — LLDP Graph

### 타겟 장비 직접 LLDP neighbors

  Gamma-Aegis-01 GE1/0/0 <-> Gamma-Portal-01 GE1/0/4
  Gamma-Aegis-01 GE1/0/1 <-> Gamma-Portal-02 GE1/0/4
  Gamma-Aegis-01 GE1/0/2 <-> Gamma-Aegis-02 GE1/0/2

### 역방향 LLDP (타겟이 neighbor로 등장)

  Gamma-Aegis-02 GE1/0/2 <-> Gamma-Aegis-01 GE1/0/2
  Gamma-Portal-01 GE1/0/4 <-> Gamma-Aegis-01 GE1/0/0
  Gamma-Portal-02 GE1/0/4 <-> Gamma-Aegis-01 GE1/0/1

## Interface Description (타겟 장비)

  GE1/0/0: From_Gamma-Aegis-01_GE1/0/0_To_Gamma-Portal-01_GE1/0/4
  GE1/0/1: From_Gamma-Aegis-01_GE1/0/1_To_Gamma-Portal-02_GE1/0/4
  GE1/0/2: From_Gamma-Aegis-01_GE1/0/2_To_Gamma-Aegis-02_GE0/0/2

## Interface Status

**Gamma-Aegis-01** UP interfaces:
  GE1/0/0 [192.168.70.54/30]
  GE1/0/1 [192.168.70.70/30]
  GE1/0/2 [192.168.70.105/30]

## ARP Mappings


  [Gamma-Aegis-01]
  192.168.70.54   3885-9511-0100        I               GE1/0/0
  192.168.70.70   3885-9511-0101        I               GE1/0/1
  192.168.70.105  3885-9511-0102        I               GE1/0/2

  [Gamma-Portal-02]
  192.168.70.10   3825-0611-0101        I               GE1/0/1
  192.168.70.14   3825-0611-0102        I               GE1/0/2
  192.168.70.82   3825-0611-0103        I               GE1/0/3
  192.168.70.69   3825-0611-0104        I               GE1/0/4
  192.168.70.77   3825-0611-0105        I               GE1/0/5
  192.168.74.42   3825-0611-0106        I               GE1/0/6
  192.168.74.46   3825-0611-0107        I               GE1/0/7

  [Gamma-Aegis-02]
  192.168.70.62   3859-7411-0100        I               GE1/0/0
  192.168.70.78   3859-7411-0101        I               GE1/0/1
  192.168.70.106  3859-7411-0102        I               GE1/0/2

  [Gamma-Portal-01]
  192.168.70.2    3834-8211-0101        I               GE1/0/1
  192.168.70.6    3834-8211-0102        I               GE1/0/2
  192.168.70.81   3834-8211-0103        I               GE1/0/3
  192.168.70.53   3834-8211-0104        I               GE1/0/4
  192.168.70.61   3834-8211-0105        I               GE1/0/5
  192.168.74.34   3834-8211-0106        I               GE1/0/6
  192.168.74.38   3834-8211-0107        I               GE1/0/7

## Raw File References

  data/Track B/devices_outputs/1/Gamma-Aegis-01/display_interface_brief.txt
  data/Track B/devices_outputs/1/Gamma-Aegis-01/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/1/Gamma-Aegis-01/display_interface_description.txt
  data/Track B/devices_outputs/1/Gamma-Aegis-01/display_arp.txt
  data/Track B/devices_outputs/1/Gamma-Portal-02/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/1/Gamma-Aegis-02/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/1/Gamma-Portal-01/display_lldp_neighbor_brief.txt

## Deterministic Solver Result

```
Gamma-Aegis-01(GE1/0/0)->Gamma-Portal-01(GE1/0/4)
Gamma-Aegis-01(GE1/0/1)->Gamma-Portal-02(GE1/0/4)
Gamma-Aegis-01(GE1/0/2)->Gamma-Aegis-02(GE1/0/2)
```

## v12 Answer (검증 대상)

```
Gamma-Aegis-01(GE1/0/0)->Gamma-Portal-01(GE1/0/4)\nGamma-Aegis-01(GE1/0/1)->Gamma-Portal-02(GE1/0/4)\nGamma-Aegis-01(GE1/0/2)->Gamma-Aegis-02(GE1/0/2)
```