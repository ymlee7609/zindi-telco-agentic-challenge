# Q33: TOPO — Link Restore (Janus-Node-02)

**scenario_id**: 212e5d0c-4377-45da-b3f5-3d0725db8f1e
**v12 answer**: Janus-Node-02(GE1/0/2)->Atlas-Node-01(GE1/0/2)\nJanus-Node-02(GE1/0/3)->Atlas-Node-02(GE1/0/2)\nJanus-Node-02(GE1/0/4)->Aegis-Node-01(GE1/0/1)\nJanus-Node-02(GE1/0/5)->Janus-Node-01(GE1/0/5)
**deterministic solver**: confidence=H, method=mixed, resolved=4/4 ports

## Question (from test.json)

The planned data of Janus-Node-02 in the PJGFA area was accidentally deleted, and the UP link connections of this node need to be restored. The link status of interfaces can be queried through several methods: 1. Query link neighbor status; 2. Query interface descriptions (which contain the remote node and remote port), and then confirm the link status through the port and IP information contained in the ARP tables of the local node and remote node. If the interface description and the ARP table port information are different, the ARP table port information shall prevail. Link neighbor status query is the preferred query method. When this status cannot be queried, use the second method to confirm port connection status. Format requirement: LocalNodeName(LocalPortNumber)->RemoteNodeName(RemotePortNumber).Each line represents one link, with no extra blank lines in the middle or at the end, and no extra whitespace characters before, after, or in the middle of each line.

## Devices in Scenario

총 23개 장비: Aegis-Node-01, Aegis-Prime-01, Aegis-Prime-02, Atlas-Node-01, Atlas-Node-02, Atlas-Prime-01, Atlas-Prime-02, Demeter-Node-01, Demeter-Node-02, Demeter-Prime-01 ... 외 13개

**Target**: `Janus-Node-02`

## Topology Snapshot — LLDP Graph

### 타겟 장비 직접 LLDP neighbors

  (LLDP 정보 없음)

### 역방향 LLDP (타겟이 neighbor로 등장)

  (역방향 LLDP 없음)

## Interface Description (타겟 장비)

  GE1/0/0: To-Aegis-Node-01-GE1/0/1
  GE1/0/1: To-Gaia-Node-01-ETH1/0/5
  GE1/0/2: To-Atlas-Node-01-GE1/0/2
  GE1/0/3: To-Atlas-Node-02-GE1/0/2
  GE1/0/4: To-Aegis-Node-01-GE1/0/1
  GE1/0/5: To-Janus-Node-01-GE1/0/5

## Interface Status

**Janus-Node-02** UP interfaces:
  Eth-Trunk1
  GE1/0/5
  Eth-Trunk3
  GE1/0/4
  GE1/0/2 [182.158.1.6/30]
  GE1/0/3 [182.158.1.14/30]
  Nve1
  Vbdif8010 [20.1.6.1/28]
  Vbdif8020 [20.1.6.17/28]
  Vbdif8030 [20.1.6.33/28]
  Vbdif8040 [20.1.6.49/28]
  Vbdif8050 [20.60.1.1/24]
  Vbdif8060 [20.70.1.1/24]
  Vlanif1001 [20.3.1.22/24]

## ARP Mappings


  [Janus-Node-02]
  91.80.1.5       3890-0611-0101        I               GE1/0/1
  182.158.1.6     3890-0611-0102        I               GE1/0/2
  182.158.1.5     3821-2411-0102   17   D               GE1/0/2
  182.158.1.14    3890-0611-0103        I               GE1/0/3
  182.158.1.13    3849-1911-0102   17   D               GE1/0/3
  20.1.6.1        0000-00a0-0001        I               Vbdif8010        vpn1
  20.1.6.17       0000-00a0-0002        I               Vbdif8020        vpn2
  20.1.6.33       0000-00a0-0003        I               Vbdif8030        vpn3
  20.1.6.49       0000-00a0-0004        I               Vbdif8040        vpn4
  20.60.1.1       0000-0000-0005        I               Vbdif8050        vpn5

## Raw File References

  data/Track B/devices_outputs/33/Janus-Node-02/display_interface_brief.txt
  data/Track B/devices_outputs/33/Janus-Node-02/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/33/Janus-Node-02/display_interface_description.txt
  data/Track B/devices_outputs/33/Janus-Node-02/display_arp.txt

## Deterministic Solver Result

```
Janus-Node-02(GE1/0/2)->Atlas-Node-01(GE1/0/2)
Janus-Node-02(GE1/0/3)->Atlas-Node-02(GE1/0/2)
Janus-Node-02(GE1/0/4)->Aegis-Node-01(GE1/0/1)
Janus-Node-02(GE1/0/5)->Janus-Node-01(GE1/0/5)
```

## v12 Answer (검증 대상)

```
Janus-Node-02(GE1/0/2)->Atlas-Node-01(GE1/0/2)\nJanus-Node-02(GE1/0/3)->Atlas-Node-02(GE1/0/2)\nJanus-Node-02(GE1/0/4)->Aegis-Node-01(GE1/0/1)\nJanus-Node-02(GE1/0/5)->Janus-Node-01(GE1/0/5)
```