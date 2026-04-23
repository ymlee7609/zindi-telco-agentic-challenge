# Q3: TOPO — Link Restore (Beta-Aegis-02)

**scenario_id**: e4e23bbb-78c1-47f0-897b-e227ba8914d4
**v12 answer**: Beta-Aegis-02(GE1/0/0)->Beta-Portal-01(GE1/0/5)\nBeta-Aegis-02(GE1/0/1)->Beta-Portal-02(GE1/0/5)\nBeta-Aegis-02(GE1/0/2)->Beta-Aegis-01(GE1/0/2)
**deterministic solver**: confidence=H, method=mixed, resolved=3/3 ports

## Question (from test.json)

The link planning data of Beta-Aegis-02 within the Development and Testing Zone has been accidentally deleted, and it is necessary to restore the link status of the interfaces whose state is UP on this node. The link status of interfaces can be queried through several methods: 1. Query the link status; 2. Query the interface description (which contains the remote node and remote port), and then confirm the link status through the port and IP correspondence information in the ARP tables of the local node and the remote node. If the interface description and the ARP table port information are different, the ARP table port information shall prevail. Link status query is the preferred query method; when this status cannot be queried, use the second method to confirm the port link status.
Based on the actual network topology, supplement the topology links for the UP interfaces of Beta-Aegis-02 in the plan. Format requirement: LocalNodeName(LocalPortNumber)->RemoteNodeName(RemotePortNumber)". Each line represents one link, with no extra blank lines in the middle or at the end, and no extra whitespace characters before, after, or within each line

## Devices in Scenario

총 33개 장비: Alpha-Center-01, Alpha-Center-02, Beta-Aegis-01, Beta-Aegis-02, Beta-Axis-01, Beta-Axis-02, Beta-Node-01, Beta-Node-02, Beta-Node-03, Beta-Node-04 ... 외 23개

**Target**: `Beta-Aegis-02`

## Topology Snapshot — LLDP Graph

### 타겟 장비 직접 LLDP neighbors

  Beta-Aegis-02 GE1/0/0 <-> Beta-Portal-01 GE1/0/5
  Beta-Aegis-02 GE1/0/1 <-> Beta-Portal-02 GE1/0/5
  Beta-Aegis-02 GE1/0/2 <-> Beta-Aegis-01 GE1/0/2

### 역방향 LLDP (타겟이 neighbor로 등장)

  Beta-Aegis-01 GE1/0/2 <-> Beta-Aegis-02 GE1/0/2
  Beta-Portal-01 GE1/0/5 <-> Beta-Aegis-02 GE1/0/0
  Beta-Portal-02 GE1/0/5 <-> Beta-Aegis-02 GE1/0/1

## Interface Description (타겟 장비)

  GE1/0/0: From_Beta-Aegis-02_GE1/0/0_To_Beta-Portal-01_GE1/0/5
  GE1/0/1: From_Beta-Aegis-02_GE1/0/1_To_Beta-Portal-02_GE1/0/5
  GE1/0/2: From_Beta-Aegis-02_GE1/0/2_To_Beta-Aegis-01_GE0/0/2

## Interface Status

**Beta-Aegis-02** UP interfaces:
  GE1/0/0 [192.168.65.186/30]
  GE1/0/1 [192.168.65.202/30]
  GE1/0/2 [192.168.65.234/30]

## ARP Mappings


  [Beta-Aegis-02]
  192.168.65.186  3854-5211-0100        I               GE1/0/0
  192.168.65.202  3854-5211-0101        I               GE1/0/1
  192.168.65.234  3854-5211-0102        I               GE1/0/2

  [Beta-Portal-01]
  192.168.65.130  3808-7711-0101        I               GE1/0/1
  192.168.65.134  3808-7711-0102        I               GE1/0/2
  192.168.65.205  3808-7711-0103        I               GE1/0/3
  192.168.65.177  3808-7711-0104        I               GE1/0/4
  192.168.65.185  3808-7711-0105        I               GE1/0/5
  192.168.74.2    3808-7711-0106        I               GE1/0/6
  192.168.74.6    3808-7711-0107        I               GE1/0/7

  [Beta-Aegis-01]
  192.168.65.178  3877-9311-0100        I               GE1/0/0
  192.168.65.194  3877-9311-0101        I               GE1/0/1
  192.168.65.233  3877-9311-0102        I               GE1/0/2

  [Beta-Portal-02]
  192.168.65.138  3875-9511-0101        I               GE1/0/1
  192.168.65.142  3875-9511-0102        I               GE1/0/2
  192.168.65.206  3875-9511-0103        I               GE1/0/3
  192.168.65.193  3875-9511-0104        I               GE1/0/4
  192.168.65.201  3875-9511-0105        I               GE1/0/5
  192.168.74.10   3875-9511-0106        I               GE1/0/6
  192.168.74.14   3875-9511-0107        I               GE1/0/7

## Raw File References

  data/Track B/devices_outputs/3/Beta-Aegis-02/display_interface_brief.txt
  data/Track B/devices_outputs/3/Beta-Aegis-02/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/3/Beta-Aegis-02/display_interface_description.txt
  data/Track B/devices_outputs/3/Beta-Aegis-02/display_arp.txt
  data/Track B/devices_outputs/3/Beta-Portal-01/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/3/Beta-Aegis-01/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/3/Beta-Portal-02/display_lldp_neighbor_brief.txt

## Deterministic Solver Result

```
Beta-Aegis-02(GE1/0/0)->Beta-Portal-01(GE1/0/5)
Beta-Aegis-02(GE1/0/1)->Beta-Portal-02(GE1/0/5)
Beta-Aegis-02(GE1/0/2)->Beta-Aegis-01(GE1/0/2)
```

## v12 Answer (검증 대상)

```
Beta-Aegis-02(GE1/0/0)->Beta-Portal-01(GE1/0/5)\nBeta-Aegis-02(GE1/0/1)->Beta-Portal-02(GE1/0/5)\nBeta-Aegis-02(GE1/0/2)->Beta-Aegis-01(GE1/0/2)
```