# Q6: TOPO — Link Restore (Delta-Axis-01)

**scenario_id**: a4a771dd-bf78-485d-bc8a-6c69e966c4df
**v12 answer**: Delta-Axis-01(GE1/0/1)->Delta-Node-01(GE1/0/1)\nDelta-Axis-01(GE1/0/2)->Delta-Node-02(GE1/0/1)\nDelta-Axis-01(GE1/0/3)->Delta-Node-03(GE1/0/1)\nDelta-Axis-01(GE1/0/4)->Delta-Node-04(GE1/0/1)\nDelta-Axis-01(GE1/0/5)->Delta-Portal-01(GE1/0/1)\nDelta-Axis-01(GE1/0/6)->Delta-Portal-02(GE1/0/1)
**deterministic solver**: confidence=H, method=mixed, resolved=6/6 ports

## Question (from test.json)

The planning data of Delta-Axis-01 within the management area has been accidentally deleted, and the link status of this node needs to be restored. The link status of interfaces can be queried through several methods: 1. Query the link status; 2. Query the interface description (which contains the remote node and remote port), and then confirm the link status through the port and IP correspondence information in the ARP tables of the local node and the remote node. If the interface description and the port information in the ARP table are different, the ARP table port information shall prevail. Link status query is the preferred query method; when the status cannot be queried through this method, use the second method to confirm the port link status.
Based on the actual network topology, supplement the topology links of Delta-Axis-01 in the plan. Format requirement: local-end-node-name(local-end-port-number)->remote-end-node-name(remote-end-port-number). Each line represents one link, with no extra blank lines in the middle or at the end, and no extra whitespace characters before, after, or within each line.

## Devices in Scenario

총 33개 장비: Alpha-Center-01, Alpha-Center-02, Beta-Aegis-01, Beta-Aegis-02, Beta-Axis-01, Beta-Axis-02, Beta-Node-01, Beta-Node-02, Beta-Node-03, Beta-Node-04 ... 외 23개

**Target**: `Delta-Axis-01`

## Topology Snapshot — LLDP Graph

### 타겟 장비 직접 LLDP neighbors

  Delta-Axis-01 GE1/0/1 <-> Delta-Node-01 GE1/0/1
  Delta-Axis-01 GE1/0/2 <-> Delta-Node-02 GE1/0/1
  Delta-Axis-01 GE1/0/3 <-> Delta-Node-03 GE1/0/1
  Delta-Axis-01 GE1/0/4 <-> Delta-Node-04 GE1/0/1
  Delta-Axis-01 GE1/0/5 <-> Delta-Portal-01 GE1/0/1
  Delta-Axis-01 GE1/0/6 <-> Delta-Portal-02 GE1/0/1

### 역방향 LLDP (타겟이 neighbor로 등장)

  Delta-Node-01 GE1/0/1 <-> Delta-Axis-01 GE1/0/1
  Delta-Node-02 GE1/0/1 <-> Delta-Axis-01 GE1/0/2
  Delta-Node-03 GE1/0/1 <-> Delta-Axis-01 GE1/0/3
  Delta-Node-04 GE1/0/1 <-> Delta-Axis-01 GE1/0/4
  Delta-Portal-01 GE1/0/1 <-> Delta-Axis-01 GE1/0/5
  Delta-Portal-02 GE1/0/1 <-> Delta-Axis-01 GE1/0/6

## Interface Description (타겟 장비)

  GE1/0/1: From_Delta-Axis-01_GE1/0/1_To_Delta-Node-01_GE1/0/1
  GE1/0/2: From_Delta-Axis-01_GE1/0/2_To_Delta-Node-02_GE1/0/1
  GE1/0/3: From_Delta-Axis-01_GE1/0/3_To_Delta-Node-03_GE1/0/1
  GE1/0/4: From_Delta-Axis-01_GE1/0/4_To_Delta-Node-04_GE1/0/1
  GE1/0/5: From_Delta-Axis-01_GE1/0/5_To_Delta-Portal-01_GE1/0/1
  GE1/0/6: From_Delta-Axis-01_GE1/0/6_To_Delta-Portal-02_GE1/0/1

## Interface Status

**Delta-Axis-01** UP interfaces:
  GE1/0/1 [192.168.72.17/30]
  GE1/0/2 [192.168.72.25/30]
  GE1/0/3 [192.168.72.33/30]
  GE1/0/4 [192.168.72.41/30]
  GE1/0/5 [192.168.72.1/30]
  GE1/0/6 [192.168.72.9/30]

## ARP Mappings


  [Delta-Axis-01]
  192.168.72.17   3804-2011-0101        I               GE1/0/1
  192.168.72.25   3804-2011-0102        I               GE1/0/2
  192.168.72.33   3804-2011-0103        I               GE1/0/3
  192.168.72.41   3804-2011-0104        I               GE1/0/4
  192.168.72.1    3804-2011-0105        I               GE1/0/5
  192.168.72.9    3804-2011-0106        I               GE1/0/6

  [Delta-Node-01]
  192.168.72.18   3800-3511-0101        I               GE1/0/1
  192.168.72.22   3800-3511-0102        I               GE1/0/2
  192.168.72.85   3800-3511-0103        I               GE1/0/3

  [Delta-Portal-01]
  192.168.72.2    3844-6211-0101        I               GE1/0/1
  192.168.72.6    3844-6211-0102        I               GE1/0/2
  192.168.72.101  3844-6211-0103        I               GE1/0/3
  192.168.72.53   3844-6211-0104        I               GE1/0/4
  192.168.72.61   3844-6211-0105        I               GE1/0/5
  192.168.74.50   3844-6211-0106        I               GE1/0/6
  192.168.74.54   3844-6211-0107        I               GE1/0/7

  [Delta-Portal-02]
  192.168.72.10   3897-1811-0101        I               GE1/0/1
  192.168.72.14   3897-1811-0102        I               GE1/0/2
  192.168.72.102  3897-1811-0103        I               GE1/0/3
  192.168.72.69   3897-1811-0104        I               GE1/0/4
  192.168.72.77   3897-1811-0105        I               GE1/0/5
  192.168.74.58   3897-1811-0106        I               GE1/0/6
  192.168.74.62   3897-1811-0107        I               GE1/0/7

  [Delta-Node-02]
  192.168.72.26   3814-2011-0101        I               GE1/0/1
  192.168.72.30   3814-2011-0102        I               GE1/0/2
  192.168.72.86   3814-2011-0103        I               GE1/0/3

  [Delta-Node-03]
  192.168.72.34   3876-9511-0101        I               GE1/0/1
  192.168.72.38   3876-9511-0102        I               GE1/0/2
  192.168.72.93   3876-9511-0103        I               GE1/0/3

## Raw File References

  data/Track B/devices_outputs/6/Delta-Axis-01/display_interface_brief.txt
  data/Track B/devices_outputs/6/Delta-Axis-01/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/6/Delta-Axis-01/display_interface_description.txt
  data/Track B/devices_outputs/6/Delta-Axis-01/display_arp.txt
  data/Track B/devices_outputs/6/Delta-Node-01/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/6/Delta-Portal-01/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/6/Delta-Portal-02/display_lldp_neighbor_brief.txt

## Deterministic Solver Result

```
Delta-Axis-01(GE1/0/1)->Delta-Node-01(GE1/0/1)
Delta-Axis-01(GE1/0/2)->Delta-Node-02(GE1/0/1)
Delta-Axis-01(GE1/0/3)->Delta-Node-03(GE1/0/1)
Delta-Axis-01(GE1/0/4)->Delta-Node-04(GE1/0/1)
Delta-Axis-01(GE1/0/5)->Delta-Portal-01(GE1/0/1)
Delta-Axis-01(GE1/0/6)->Delta-Portal-02(GE1/0/1)
```

## v12 Answer (검증 대상)

```
Delta-Axis-01(GE1/0/1)->Delta-Node-01(GE1/0/1)\nDelta-Axis-01(GE1/0/2)->Delta-Node-02(GE1/0/1)\nDelta-Axis-01(GE1/0/3)->Delta-Node-03(GE1/0/1)\nDelta-Axis-01(GE1/0/4)->Delta-Node-04(GE1/0/1)\nDelta-Axis-01(GE1/0/5)->Delta-Portal-01(GE1/0/1)\nDelta-Axis-01(GE1/0/6)->Delta-Portal-02(GE1/0/1)
```