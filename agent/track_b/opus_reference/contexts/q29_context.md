# Q29: TOPO — Link Restore (Demeter-Prime-01)

**scenario_id**: dd11da6b-0ded-4417-bfd5-e36d996e1189
**v12 answer**: Demeter-Prime-01(GE1/0/0)->Atlas-Prime-01(GE1/0/2)\nDemeter-Prime-01(GE1/0/1)->Atlas-Prime-02(GE1/0/2)
**deterministic solver**: confidence=M, method=mixed, resolved=2/3 ports

## Question (from test.json)

The planning data of Demeter-Prime-01 in the PJ area was accidentally deleted, and the UP link connections of this node need to be restored. The link status of interfaces can be queried through several methods: 1. Query link neighbor status; 2. Query interface descriptions (which contain the peer node and peer port), then confirm the link status through the port and IP information contained in the ARP tables of both the local node and the peer node. If the interface description and the ARP table port information are different, the ARP table port information shall prevail. Link neighbor status query is the preferred query method. When this status cannot be queried, use the second method to confirm port connection status. Format requirement: LocalNodeName(LocalPortNumber)->PeerNodeName(PeerPortNumber). Each line represents one link, with no extra blank lines in the middle or at the end, and no extra whitespace characters before, after, or within each line.

## Devices in Scenario

총 23개 장비: Aegis-Node-01, Aegis-Prime-01, Aegis-Prime-02, Atlas-Node-01, Atlas-Node-02, Atlas-Prime-01, Atlas-Prime-02, Demeter-Node-01, Demeter-Node-02, Demeter-Prime-01 ... 외 13개

**Target**: `Demeter-Prime-01`

## Topology Snapshot — LLDP Graph

### 타겟 장비 직접 LLDP neighbors

  (LLDP 정보 없음)

### 역방향 LLDP (타겟이 neighbor로 등장)

  (역방향 LLDP 없음)

## Interface Description (타겟 장비)

  GE1/0/0: To-Spine2-GE1/0/2
  GE1/0/1: To-Spine1-GE1/0/2
  GE1/0/2: To-PX1
  GE1/0/3: To-Janus-Prime-02-GE1/0/3
  GE1/0/4: To-Janus-Prime-02-GE1/0/4
  GE1/0/5: To-PC1-GE1/0/4
  GE1/0/6: To-server
  GE1/0/7: To-LB1-Eth1/0/0
  GE1/0/8: To-LB2-Eth1/0/0
  GE1/0/9: To-Aegis-Prime-02-GE1/0/2

## Interface Status

**Demeter-Prime-01** UP interfaces:
  GE1/0/0 [192.168.2.2/30]
  GE1/0/1 [192.168.2.10/30]
  GE1/0/5
  Nve1
  Vbdif10 [10.1.1.1/24]
  Vbdif20 [10.1.2.1/24]
  Vbdif30 [10.1.3.1/24]
  Vbdif40 [10.1.4.1/24]
  Vbdif50 [10.1.5.1/24]
  Vbdif60 [11.1.1.1/24]
  Vbdif500 [10.1.100.1/24]

## ARP Mappings


  [Demeter-Prime-01]
  10.1.1.1        0000-00e0-0001        I               Vbdif10          vpn1
  10.1.2.1        0000-00e0-0001        I               Vbdif20          vpn2
  10.1.3.1        0000-00e0-0001        I               Vbdif30          vpn3
  10.1.4.1        0000-00e0-0001        I               Vbdif40          vpn4
  10.1.5.1        0000-0000-0060        I               Vbdif50          vpn5
  11.1.1.1        0000-0000-1111        I               Vbdif60          vpn6
  10.1.100.1      0000-0001-1001        I               Vbdif500         lb-vpn
  192.168.2.2     3877-7111-0100        I               GE1/0/0
  192.168.2.1     3844-0411-0102   16   D               GE1/0/0
  192.168.2.10    3877-7111-0101        I               GE1/0/1

## Raw File References

  data/Track B/devices_outputs/29/Demeter-Prime-01/display_interface_brief.txt
  data/Track B/devices_outputs/29/Demeter-Prime-01/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/29/Demeter-Prime-01/display_interface_description.txt
  data/Track B/devices_outputs/29/Demeter-Prime-01/display_arp.txt

## Deterministic Solver Result

```
Demeter-Prime-01(GE1/0/0)->Atlas-Prime-01(GE1/0/2)
Demeter-Prime-01(GE1/0/1)->Atlas-Prime-02(GE1/0/2)
```

## v12 Answer (검증 대상)

```
Demeter-Prime-01(GE1/0/0)->Atlas-Prime-01(GE1/0/2)\nDemeter-Prime-01(GE1/0/1)->Atlas-Prime-02(GE1/0/2)
```