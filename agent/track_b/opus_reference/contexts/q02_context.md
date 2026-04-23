# Q2: TOPO — Link Restore (Gamma-Axis-02)

**scenario_id**: 8ec59f8b-1a5a-4fb3-80ad-f0e2aaf6a499
**v12 answer**: Gamma-Axis-02(GE1/0/1)->Gamma-Node-01(GE1/0/2)\nGamma-Axis-02(GE1/0/2)->Gamma-Node-02(GE1/0/2)\nGamma-Axis-02(GE1/0/3)->Gamma-Node-03(GE1/0/2)\nGamma-Axis-02(GE1/0/4)->Gamma-Node-04(GE1/0/2)\nGamma-Axis-02(GE1/0/5)->Gamma-Portal-01(GE1/0/2)\nGamma-Axis-02(GE1/0/6)->Gamma-Portal-02(GE1/0/2)
**deterministic solver**: confidence=H, method=mixed, resolved=6/6 ports

## Question (from test.json)

The planning data of Gamma-Axis-02 within the Big Data Zone has been accidentally deleted. It is necessary to restore the link status of the interfaces whose state is UP on this node. However, the link status cannot be queried from the Gamma-Axis-02 node itself. It is known that the nodes connected to Gamma-Axis-02 are among these 9 nodes: Gamma-Portal-01/Gamma-Portal-02/Gamma-Aegis-01/Gamma-Aegis-02/Gamma-Axis-01/Gamma-Node-01/Gamma-Node-02/Gamma-Node-03/Gamma-Node-04. The link status can be queried through several methods: 1. Query the link status directly. 2. Query the interface description (which contains the remote node and remote port), and then confirm the link status by checking the port and IP correspondence information in the ARP tables of the local node and the remote node. If the interface description and the ARP table port information are different, the ARP table port information shall prevail. Querying the link status is the preferred method. When the status cannot be queried through that method, use the second method to confirm the port link status.
Please based on the link status of surrounding nodes, supplement the link information for the UP interfaces of the Gamma-Axis-02 node. Format requirement: local node name(local port number)->remote node name(remote port number). Each line represents one link, with no extra blank lines in the middle or at the end, and no extra whitespace characters before, after, or within each line.

## Devices in Scenario

총 33개 장비: Alpha-Center-01, Alpha-Center-02, Beta-Aegis-01, Beta-Aegis-02, Beta-Axis-01, Beta-Axis-02, Beta-Node-01, Beta-Node-02, Beta-Node-03, Beta-Node-04 ... 외 23개

**Target**: `Gamma-Axis-02`

## Topology Snapshot — LLDP Graph

### 타겟 장비 직접 LLDP neighbors

  Gamma-Axis-02 GE1/0/1 <-> Gamma-Node-01 GE1/0/2
  Gamma-Axis-02 GE1/0/2 <-> Gamma-Node-02 GE1/0/2
  Gamma-Axis-02 GE1/0/3 <-> Gamma-Node-03 GE1/0/2
  Gamma-Axis-02 GE1/0/4 <-> Gamma-Node-04 GE1/0/2
  Gamma-Axis-02 GE1/0/5 <-> Gamma-Portal-01 GE1/0/2
  Gamma-Axis-02 GE1/0/6 <-> Gamma-Portal-02 GE1/0/2

### 역방향 LLDP (타겟이 neighbor로 등장)

  Gamma-Node-01 GE1/0/2 <-> Gamma-Axis-02 GE1/0/1
  Gamma-Node-02 GE1/0/2 <-> Gamma-Axis-02 GE1/0/2
  Gamma-Node-03 GE1/0/2 <-> Gamma-Axis-02 GE1/0/3
  Gamma-Node-04 GE1/0/2 <-> Gamma-Axis-02 GE1/0/4
  Gamma-Portal-01 GE1/0/2 <-> Gamma-Axis-02 GE1/0/5
  Gamma-Portal-02 GE1/0/2 <-> Gamma-Axis-02 GE1/0/6

## Interface Description (타겟 장비)

  GE1/0/1: From_Gamma-Axis-02_GE1/0/1_To_Gamma-Node-01_GE1/0/2
  GE1/0/2: From_Gamma-Axis-02_GE1/0/2_To_Gamma-Node-02_GE1/0/2
  GE1/0/3: From_Gamma-Axis-02_GE1/0/3_To_Gamma-Node-03_GE1/0/2
  GE1/0/4: From_Gamma-Axis-02_GE1/0/4_To_Gamma-Node-04_GE1/0/2
  GE1/0/5: From_Gamma-Axis-02_GE1/0/5_To_Gamma-Portal-01_GE1/0/2
  GE1/0/6: From_Gamma-Axis-02_GE1/0/6_To_Gamma-Portal-02_GE1/0/2

## Interface Status

**Gamma-Axis-02** UP interfaces:
  GE1/0/1 [192.168.70.21/30]
  GE1/0/2 [192.168.70.29/30]
  GE1/0/3 [192.168.70.37/30]
  GE1/0/4 [192.168.70.45/30]
  GE1/0/5 [192.168.70.5/30]
  GE1/0/6 [192.168.70.13/30]

## ARP Mappings


  [Gamma-Axis-02]
  192.168.70.21   3821-8911-0101        I               GE1/0/1
  192.168.70.29   3821-8911-0102        I               GE1/0/2
  192.168.70.37   3821-8911-0103        I               GE1/0/3
  192.168.70.45   3821-8911-0104        I               GE1/0/4
  192.168.70.5    3821-8911-0105        I               GE1/0/5
  192.168.70.13   3821-8911-0106        I               GE1/0/6

  [Gamma-Portal-02]
  192.168.70.10   3825-0611-0101        I               GE1/0/1
  192.168.70.14   3825-0611-0102        I               GE1/0/2
  192.168.70.82   3825-0611-0103        I               GE1/0/3
  192.168.70.69   3825-0611-0104        I               GE1/0/4
  192.168.70.77   3825-0611-0105        I               GE1/0/5
  192.168.74.42   3825-0611-0106        I               GE1/0/6
  192.168.74.46   3825-0611-0107        I               GE1/0/7

  [Gamma-Node-01]
  192.168.70.18   3832-4011-0101        I               GE1/0/1
  192.168.70.22   3832-4011-0102        I               GE1/0/2
  192.168.70.85   3832-4011-0103        I               GE1/0/3

  [Gamma-Node-02]
  192.168.70.26   3857-8711-0101        I               GE1/0/1
  192.168.70.30   3857-8711-0102        I               GE1/0/2
  192.168.70.86   3857-8711-0103        I               GE1/0/3

  [Gamma-Portal-01]
  192.168.70.2    3834-8211-0101        I               GE1/0/1
  192.168.70.6    3834-8211-0102        I               GE1/0/2
  192.168.70.81   3834-8211-0103        I               GE1/0/3
  192.168.70.53   3834-8211-0104        I               GE1/0/4
  192.168.70.61   3834-8211-0105        I               GE1/0/5
  192.168.74.34   3834-8211-0106        I               GE1/0/6
  192.168.74.38   3834-8211-0107        I               GE1/0/7

  [Gamma-Node-04]
  192.168.70.42   3803-2511-0101        I               GE1/0/1
  192.168.70.46   3803-2511-0102        I               GE1/0/2
  192.168.70.94   3803-2511-0103        I               GE1/0/3

## Raw File References

  data/Track B/devices_outputs/2/Gamma-Axis-02/display_interface_brief.txt
  data/Track B/devices_outputs/2/Gamma-Axis-02/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/2/Gamma-Axis-02/display_interface_description.txt
  data/Track B/devices_outputs/2/Gamma-Axis-02/display_arp.txt
  data/Track B/devices_outputs/2/Gamma-Portal-02/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/2/Gamma-Node-01/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/2/Gamma-Node-02/display_lldp_neighbor_brief.txt

## Deterministic Solver Result

```
Gamma-Axis-02(GE1/0/1)->Gamma-Node-01(GE1/0/2)
Gamma-Axis-02(GE1/0/2)->Gamma-Node-02(GE1/0/2)
Gamma-Axis-02(GE1/0/3)->Gamma-Node-03(GE1/0/2)
Gamma-Axis-02(GE1/0/4)->Gamma-Node-04(GE1/0/2)
Gamma-Axis-02(GE1/0/5)->Gamma-Portal-01(GE1/0/2)
Gamma-Axis-02(GE1/0/6)->Gamma-Portal-02(GE1/0/2)
```

## v12 Answer (검증 대상)

```
Gamma-Axis-02(GE1/0/1)->Gamma-Node-01(GE1/0/2)\nGamma-Axis-02(GE1/0/2)->Gamma-Node-02(GE1/0/2)\nGamma-Axis-02(GE1/0/3)->Gamma-Node-03(GE1/0/2)\nGamma-Axis-02(GE1/0/4)->Gamma-Node-04(GE1/0/2)\nGamma-Axis-02(GE1/0/5)->Gamma-Portal-01(GE1/0/2)\nGamma-Axis-02(GE1/0/6)->Gamma-Portal-02(GE1/0/2)
```