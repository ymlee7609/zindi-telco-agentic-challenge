# Q31: TOPO — Link Restore (Janus-Prime-01)

**scenario_id**: a346ef65-4abd-4e27-b7c6-06fc70a4f1c0
**v12 answer**: Janus-Prime-01(GE1/0/0)->Atlas-Prime-01(GE1/0/0)\nJanus-Prime-01(GE1/0/1)->Atlas-Prime-02(GE1/0/0)\nJanus-Prime-01(GE1/0/2)->PX1(GE1/0/0)\nJanus-Prime-01(GE1/0/4)->Janus-Prime-02(GE1/0/4)\nJanus-Prime-01(GE1/0/5)->Aegis-Prime-01(GE1/0/2)
**deterministic solver**: confidence=M, method=mixed, resolved=5/6 ports

## Question (from test.json)

The planning data of Janus-Prime-01 in the PJ area has been accidentally deleted, and the UP link connections of this node need to be restored. The link status of interfaces can be queried through several methods: 1. Query link neighbor status; 2. Query interface descriptions (which contain the peer node and peer port), then confirm the link status through the port and IP information contained in the ARP tables of the local node and the peer node. If the interface description and the ARP table port information are different, the ARP table port information shall prevail. Link neighbor status query is the preferred query method. When this status cannot be queried, use the second method to confirm the port connection situation. Format requirement: LocalNodeName(LocalPortNumber)->PeerNodeName(PeerPortNumber). Each line represents one link, with no extra blank lines in the middle or at the end, and no extra whitespace characters before, after, or in the middle of each line.

## Devices in Scenario

총 23개 장비: Aegis-Node-01, Aegis-Prime-01, Aegis-Prime-02, Atlas-Node-01, Atlas-Node-02, Atlas-Prime-01, Atlas-Prime-02, Demeter-Node-01, Demeter-Node-02, Demeter-Prime-01 ... 외 13개

**Target**: `Janus-Prime-01`

## Topology Snapshot — LLDP Graph

### 타겟 장비 직접 LLDP neighbors

  (LLDP 정보 없음)

### 역방향 LLDP (타겟이 neighbor로 등장)

  (역방향 LLDP 없음)

## Interface Description (타겟 장비)

  GE1/0/0: To-Spine1-GE1/0/0
  GE1/0/1: To-Spine2-GE1/0/0
  GE1/0/2: To-PX1
  GE1/0/4: To-Janus-Prime-02-GE1/0/4
  GE1/0/5: To-Aegis-Prime-01-GE1/0/2
  GE1/0/7: To-LB1-Eth1/0/0
  GE1/0/8: To-LB2-Eth1/0/0
  GE1/0/9: To-Aegis-Prime-02-GE1/0/2

## Interface Status

**Janus-Prime-01** UP interfaces:
  Eth-Trunk1
  GE1/0/4
  Eth-Trunk3
  GE1/0/3
  GE1/0/0 [192.168.1.2/30]
  GE1/0/1 [192.168.1.10/30]
  GE1/0/2 [10.101.1.1/24]
  GE1/0/5
  Nve1
  Vbdif5000 [10.100.1.1/24]
  Vbdif8010 [10.1.6.3/28]
  Vbdif8020 [10.1.6.21/28]
  Vbdif8030 [10.1.6.38/28]
  Vbdif8040 [10.1.6.53/28]
  Vbdif8050 [10.60.1.1/24]
  ... 외 2개

## ARP Mappings


  [Janus-Prime-01]
  192.168.1.2     3840-1811-0100        I               GE1/0/0
  192.168.1.1     3844-0411-0100   16   D               GE1/0/0
  192.168.1.10    3840-1811-0101        I               GE1/0/1
  192.168.1.9     3843-2811-0100   16   D               GE1/0/1
  10.101.1.1      3840-1811-0102        I               GE1/0/2
  10.100.1.1      0000-1000-0001        I               Vbdif5000        lb-vpn
  10.100.1.2      3840-8411-0100   17   D/BD5000        GE1/0/2.1        lb-vpn
  10.1.6.3        0000-00f0-0002        I               Vbdif8010        vpn1
  10.1.6.21       0000-00f0-0003        I               Vbdif8020        vpn2
  10.1.6.38       0000-00f0-0003        I               Vbdif8030        vpn3

## Raw File References

  data/Track B/devices_outputs/31/Janus-Prime-01/display_interface_brief.txt
  data/Track B/devices_outputs/31/Janus-Prime-01/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/31/Janus-Prime-01/display_interface_description.txt
  data/Track B/devices_outputs/31/Janus-Prime-01/display_arp.txt

## Deterministic Solver Result

```
Janus-Prime-01(GE1/0/0)->Atlas-Prime-01(GE1/0/0)
Janus-Prime-01(GE1/0/1)->Atlas-Prime-02(GE1/0/0)
Janus-Prime-01(GE1/0/2)->PX1(GE1/0/0)
Janus-Prime-01(GE1/0/4)->Janus-Prime-02(GE1/0/4)
Janus-Prime-01(GE1/0/5)->Aegis-Prime-01(GE1/0/2)
```

## v12 Answer (검증 대상)

```
Janus-Prime-01(GE1/0/0)->Atlas-Prime-01(GE1/0/0)\nJanus-Prime-01(GE1/0/1)->Atlas-Prime-02(GE1/0/0)\nJanus-Prime-01(GE1/0/2)->PX1(GE1/0/0)\nJanus-Prime-01(GE1/0/4)->Janus-Prime-02(GE1/0/4)\nJanus-Prime-01(GE1/0/5)->Aegis-Prime-01(GE1/0/2)
```