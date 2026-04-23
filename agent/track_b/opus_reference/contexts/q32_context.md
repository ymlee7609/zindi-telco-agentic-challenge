# Q32: TOPO — Link Restore (Aegis-Prime-01)

**scenario_id**: d5a0f37b-4042-4570-ba17-7677fc7ebe01
**v12 answer**: Aegis-Prime-01(GE1/0/0)->Janus-Prime-02(GE1/0/5)\nAegis-Prime-01(GE1/0/1)->Aegis-Prime-02(GE1/0/1)\nAegis-Prime-01(GE1/0/3)->Eon-Node-01(GE1/0/1)
**deterministic solver**: confidence=H, method=mixed, resolved=3/3 ports

## Question (from test.json)

The planned data of Aegis-Prime-01 in the PJ area was accidentally deleted, and the UP link connections of this node need to be restored. The link status of interfaces can be queried through several methods: 1. Query link neighbor status; 2. Query interface descriptions (which contain the remote node and remote port), and then confirm the link status through the port and IP information contained in the ARP tables of the local node and the remote node. If the interface description and the ARP table port information are different, the ARP table port information shall prevail. Link neighbor status query is the preferred query method. When this status cannot be queried, use the second method to confirm the port connection status. Format requirement: LocalNodeName(LocalPortNumber)->RemoteNodeName(RemotePortNumber).Each line represents one link, with no extra blank lines in the middle or at the end, and no extra whitespace characters before, after, or within each line.

## Devices in Scenario

총 23개 장비: Aegis-Node-01, Aegis-Prime-01, Aegis-Prime-02, Atlas-Node-01, Atlas-Node-02, Atlas-Prime-01, Atlas-Prime-02, Demeter-Node-01, Demeter-Node-02, Demeter-Prime-01 ... 외 13개

**Target**: `Aegis-Prime-01`

## Topology Snapshot — LLDP Graph

### 타겟 장비 직접 LLDP neighbors

  (LLDP 정보 없음)

### 역방향 LLDP (타겟이 neighbor로 등장)

  (역방향 LLDP 없음)

## Interface Description (타겟 장비)

  Eth-Trunk1: Huawei, USG6000V2 Series, Eth-Tru
  Eth-Trunk2: To-BL2-Eth-Trunk3
  Eth-Trunk2.1: Huawei, USG6000V2 Series, Eth-Tru
  Eth-Trunk2.2: Huawei, USG6000V2 Series, Eth-Tru
  Eth-Trunk2.3: Huawei, USG6000V2 Series, Eth-Tru
  Eth-Trunk2.4: Huawei, USG6000V2 Series, Eth-Tru
  Eth-Trunk2.60: Huawei, USG6000V2 Series, Eth-Tru
  Eth-Trunk2.70: Huawei, USG6000V2 Series, Eth-Tru
  Eth-Trunk2.500: Huawei, USG6000V2 Series, Eth-Tru
  Eth-Trunk4: Huawei, USG6000V2 Series, Eth-Tru
  GE0/0/0(10G): Huawei, USG6000V2 Series, Gigabit
  GE1/0/0(10G): To-BorderLeaf2-GE1/0/5
  GE1/0/1(10G): To-Aegis-Prime-02-GE1/0/1
  GE1/0/2(10G): to Janus-Prime-01-GE1/0/5
  GE1/0/3(10G): To-PJlAN-01-GE1/0/1
  GE1/0/4: Huawei, USG6000V2 Series, Gigabit
  GE1/0/5: Huawei, USG6000V2 Series, Gigabit
  GE1/0/6: Huawei, USG6000V2 Series, Gigabit
  GE1/0/7: Huawei, USG6000V2 Series, Gigabit
  GE1/0/8: Huawei, USG6000V2 Series, Gigabit

## Interface Status

**Aegis-Prime-01** UP interfaces:
  Eth-Trunk1 [75.40.1.2/24]
  Eth-Trunk2

## ARP Mappings


  [Aegis-Prime-01]
  20.0.0.2        0ce6-43bb-0000            I -  GE0/0/0
  10.3.1.31       0ce6-43bb-0000            I -  Vlanif1001
  10.4.1.11       0ce6-43bb-0000            I -  Vlanif1101
  75.40.1.2       0ce6-43bb-0000            I -  Eth-Trunk1
  75.40.1.1       3813-0011-1200  18        D-0  Eth-Trunk1
  10.1.6.6        0ce6-43bb-0000            I -  Eth-Trunk2.1
  10.1.6.1        0000-5e00-0101  19        D-0  Eth-Trunk2.1
  10.1.6.20       0ce6-43bb-0000            I -  Eth-Trunk2.2
  10.1.6.17       0000-5e00-0102  19        D-0  Eth-Trunk2.2
  10.1.6.36       0ce6-43bb-0000            I -  Eth-Trunk2.3

## Raw File References

  data/Track B/devices_outputs/32/Aegis-Prime-01/display_interface_brief.txt
  data/Track B/devices_outputs/32/Aegis-Prime-01/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/32/Aegis-Prime-01/display_interface_description.txt
  data/Track B/devices_outputs/32/Aegis-Prime-01/display_arp.txt

## Deterministic Solver Result

```
Aegis-Prime-01(GE1/0/0)->Janus-Prime-02(GE1/0/5)
Aegis-Prime-01(GE1/0/1)->Aegis-Prime-02(GE1/0/1)
Aegis-Prime-01(GE1/0/3)->Eon-Node-01(GE1/0/1)
```

## v12 Answer (검증 대상)

```
Aegis-Prime-01(GE1/0/0)->Janus-Prime-02(GE1/0/5)\nAegis-Prime-01(GE1/0/1)->Aegis-Prime-02(GE1/0/1)\nAegis-Prime-01(GE1/0/3)->Eon-Node-01(GE1/0/1)
```