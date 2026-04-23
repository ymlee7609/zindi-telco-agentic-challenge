# Q30: TOPO — Link Restore (Atlas-Prime-01)

**scenario_id**: dad1f1ad-a21e-4831-a6b2-763e8eebd026
**v12 answer**: Atlas-Prime-01(GE1/0/0)->Janus-Prime-01(GE1/0/0)\nAtlas-Prime-01(GE1/0/1)->Janus-Prime-02(GE1/0/0)\nAtlas-Prime-01(GE1/0/2)->Demeter-Prime-01(GE1/0/0)\nAtlas-Prime-01(GE1/0/3)->Demeter-Prime-02(GE1/0/0)
**deterministic solver**: confidence=H, method=self_desc, resolved=4/4 ports

## Question (from test.json)

The planning data of Atlas-Prime-01 in the PJ area was accidentally deleted, and the UP link connections of this node need to be restored. The link status of interfaces can be queried through several methods: 1. Query link neighbor status; 2. Query interface descriptions (which contain the remote node and remote port), and then confirm the link status through the port and IP information contained in the ARP tables of the local node and the remote node. If the interface description and the ARP table port information are different, the ARP table port information shall prevail. Link neighbor status query is the preferred query method. When this status cannot be queried, use the second method to confirm the port connection situation. Format requirement: LocalNodeName(LocalPortNumber)->RemoteNodeName(RemotePortNumber).Each line represents one link, with no extra blank lines in the middle or at the end, and no extra whitespace characters before, after, or in the middle of each line.

## Devices in Scenario

총 23개 장비: Aegis-Node-01, Aegis-Prime-01, Aegis-Prime-02, Atlas-Node-01, Atlas-Node-02, Atlas-Prime-01, Atlas-Prime-02, Demeter-Node-01, Demeter-Node-02, Demeter-Prime-01 ... 외 13개

**Target**: `Atlas-Prime-01`

## Topology Snapshot — LLDP Graph

### 타겟 장비 직접 LLDP neighbors

  (LLDP 정보 없음)

### 역방향 LLDP (타겟이 neighbor로 등장)

  (역방향 LLDP 없음)

## Interface Description (타겟 장비)

  GE1/0/0: To-Janus-Prime-01-GE1/0/0
  GE1/0/1: To-Janus-Prime-02-GE1/0/0
  GE1/0/2: To-Demeter-Prime-01-GE1/0/0
  GE1/0/3: To-Demeter-Prime-02-GE1/0/0
  GE1/0/5: To-H3C-BL3-GE1/0

## Interface Status

**Atlas-Prime-01** UP interfaces:
  GE1/0/0 [192.168.1.1/30]
  GE1/0/1 [192.168.1.5/30]
  GE1/0/2 [192.168.2.1/30]
  GE1/0/3 [192.168.2.5/30]

## ARP Mappings


  [Atlas-Prime-01]
  192.168.1.1     3844-0411-0100        I               GE1/0/0
  192.168.1.2     3840-1811-0100   16   D               GE1/0/0
  192.168.1.5     3844-0411-0101        I               GE1/0/1
  192.168.1.6     3886-9911-0100   16   D               GE1/0/1
  192.168.2.1     3844-0411-0102        I               GE1/0/2
  192.168.2.2     3877-7111-0100   16   D               GE1/0/2
  192.168.2.5     3844-0411-0103        I               GE1/0/3
  192.168.2.6     3889-3511-0100   16   D               GE1/0/3
  192.168.3.1     3844-0411-0105        I               GE1/0/5

## Raw File References

  data/Track B/devices_outputs/30/Atlas-Prime-01/display_interface_brief.txt
  data/Track B/devices_outputs/30/Atlas-Prime-01/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/30/Atlas-Prime-01/display_interface_description.txt
  data/Track B/devices_outputs/30/Atlas-Prime-01/display_arp.txt

## Deterministic Solver Result

```
Atlas-Prime-01(GE1/0/0)->Janus-Prime-01(GE1/0/0)
Atlas-Prime-01(GE1/0/1)->Janus-Prime-02(GE1/0/0)
Atlas-Prime-01(GE1/0/2)->Demeter-Prime-01(GE1/0/0)
Atlas-Prime-01(GE1/0/3)->Demeter-Prime-02(GE1/0/0)
```

## v12 Answer (검증 대상)

```
Atlas-Prime-01(GE1/0/0)->Janus-Prime-01(GE1/0/0)\nAtlas-Prime-01(GE1/0/1)->Janus-Prime-02(GE1/0/0)\nAtlas-Prime-01(GE1/0/2)->Demeter-Prime-01(GE1/0/0)\nAtlas-Prime-01(GE1/0/3)->Demeter-Prime-02(GE1/0/0)
```