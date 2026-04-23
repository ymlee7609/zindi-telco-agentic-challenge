# Q4: TOPO — Link Restore (Beta-Portal-02)

**scenario_id**: c2effbaf-f3ce-4101-8f4b-e4412ba27e2c
**v12 answer**: Beta-Portal-02(GE1/0/1)->Beta-Axis-01(GE1/0/6)\nBeta-Portal-02(GE1/0/2)->Beta-Axis-02(GE1/0/6)\nBeta-Portal-02(GE1/0/3)->Beta-Portal-01(GE1/0/3)\nBeta-Portal-02(GE1/0/4)->Beta-Aegis-01(GE1/0/1)\nBeta-Portal-02(GE1/0/5)->Beta-Aegis-02(GE1/0/1)\nBeta-Portal-02(GE1/0/6)->Alpha-Center-01(GE1/0/2)\nBeta-Portal-02(GE1/0/7)->Alpha-Center-02(GE1/0/2)
**deterministic solver**: confidence=H, method=mixed, resolved=7/7 ports

## Question (from test.json)

The planning data of Beta-Portal-02 within the Development and Testing Zone has been accidentally deleted, and the link status of this node needs to be restored. The link status of interfaces can be queried through several methods: 1. Query the link status, 2. Query the interface description (which contains the remote node and remote port), and then confirm the link status through the port and IP correspondence information in the ARP tables of this node and the remote node. If the interface description and the ARP table port information are different, the ARP table port information shall prevail. Link status query is the preferred query method; when the status cannot be queried through this method, use the second method to confirm the port link status.
Based on the actual network topology, supplement the topology links for Beta-Portal-02 in the plan. Format requirement: local node name(local port number)->remote node name(remote port number). Each line represents one link, with no extra blank lines in the middle or at the end, and no extra whitespace characters before, after, or within each line.

## Devices in Scenario

총 33개 장비: Alpha-Center-01, Alpha-Center-02, Beta-Aegis-01, Beta-Aegis-02, Beta-Axis-01, Beta-Axis-02, Beta-Node-01, Beta-Node-02, Beta-Node-03, Beta-Node-04 ... 외 23개

**Target**: `Beta-Portal-02`

## Topology Snapshot — LLDP Graph

### 타겟 장비 직접 LLDP neighbors

  Beta-Portal-02 GE1/0/1 <-> Beta-Axis-01 GE1/0/6
  Beta-Portal-02 GE1/0/2 <-> Beta-Axis-02 GE1/0/6
  Beta-Portal-02 GE1/0/3 <-> Beta-Portal-01 GE1/0/3
  Beta-Portal-02 GE1/0/4 <-> Beta-Aegis-01 GE1/0/1
  Beta-Portal-02 GE1/0/5 <-> Beta-Aegis-02 GE1/0/1
  Beta-Portal-02 GE1/0/6 <-> Alpha-Center-01 GE1/0/2
  Beta-Portal-02 GE1/0/7 <-> Alpha-Center-02 GE1/0/2

### 역방향 LLDP (타겟이 neighbor로 등장)

  Alpha-Center-01 GE1/0/2 <-> Beta-Portal-02 GE1/0/6
  Alpha-Center-02 GE1/0/2 <-> Beta-Portal-02 GE1/0/7
  Beta-Aegis-01 GE1/0/1 <-> Beta-Portal-02 GE1/0/4
  Beta-Aegis-02 GE1/0/1 <-> Beta-Portal-02 GE1/0/5
  Beta-Axis-01 GE1/0/6 <-> Beta-Portal-02 GE1/0/1
  Beta-Axis-02 GE1/0/6 <-> Beta-Portal-02 GE1/0/2
  Beta-Portal-01 GE1/0/3 <-> Beta-Portal-02 GE1/0/3

## Interface Description (타겟 장비)

  GE1/0/1: From_Beta-Portal-02_GE1/0/1_To_Beta-Axis-01_GE1/0/1
  GE1/0/2: From_Beta-Portal-02_GE1/0/2_To_Beta-Axis-02_GE1/0/1
  GE1/0/3: From_Beta-Portal-02_GE1/0/3_To_Beta-Portal-01_GE1/0/3
  GE1/0/4: From_Beta-Portal-02_GE1/0/4_To_Beta-Aegis-01_GE0/0/1
  GE1/0/5: From_Beta-Portal-02_GE1/0/5_To_Beta-Aegis-02_GE0/0/1
  GE1/0/6: From_Beta-Portal-02_GE1/0/6_To_Alpha-Center-01_GE1/0/2
  GE1/0/7: From_Beta-Portal-02_GE1/0/7_To_Alpha-Center-02_GE1/0/2

## Interface Status

**Beta-Portal-02** UP interfaces:
  GE1/0/1 [192.168.65.138/30]
  GE1/0/2 [192.168.65.142/30]
  GE1/0/3 [192.168.65.206/30]
  GE1/0/4 [192.168.65.193/30]
  GE1/0/5 [192.168.65.201/30]
  GE1/0/6 [192.168.74.10/30]
  GE1/0/7 [192.168.74.14/30]

## ARP Mappings


  [Beta-Portal-02]
  192.168.65.138  3875-9511-0101        I               GE1/0/1
  192.168.65.142  3875-9511-0102        I               GE1/0/2
  192.168.65.206  3875-9511-0103        I               GE1/0/3
  192.168.65.193  3875-9511-0104        I               GE1/0/4
  192.168.65.201  3875-9511-0105        I               GE1/0/5
  192.168.74.10   3875-9511-0106        I               GE1/0/6
  192.168.74.14   3875-9511-0107        I               GE1/0/7

  [Alpha-Center-02]
  192.168.74.5    3850-2311-0101        I               GE1/0/1
  192.168.74.13   3850-2311-0102        I               GE1/0/2
  192.168.74.53   3850-2311-0103        I               GE1/0/3
  192.168.74.61   3850-2311-0104        I               GE1/0/4
  192.168.74.37   3850-2311-0105        I               GE1/0/5
  192.168.74.45   3850-2311-0106        I               GE1/0/6

  [Alpha-Center-01]
  192.168.74.1    3822-6611-0101        I               GE1/0/1
  192.168.74.9    3822-6611-0102        I               GE1/0/2
  192.168.74.49   3822-6611-0103        I               GE1/0/3
  192.168.74.57   3822-6611-0104        I               GE1/0/4
  192.168.74.33   3822-6611-0105        I               GE1/0/5
  192.168.74.41   3822-6611-0106        I               GE1/0/6

  [Beta-Axis-02]
  192.168.65.149  3894-9011-0101        I               GE1/0/1
  192.168.65.157  3894-9011-0102        I               GE1/0/2
  192.168.65.165  3894-9011-0103        I               GE1/0/3
  192.168.65.173  3894-9011-0104        I               GE1/0/4
  192.168.65.133  3894-9011-0105        I               GE1/0/5
  192.168.65.141  3894-9011-0106        I               GE1/0/6

  [Beta-Portal-01]
  192.168.65.130  3808-7711-0101        I               GE1/0/1
  192.168.65.134  3808-7711-0102        I               GE1/0/2
  192.168.65.205  3808-7711-0103        I               GE1/0/3
  192.168.65.177  3808-7711-0104        I               GE1/0/4
  192.168.65.185  3808-7711-0105        I               GE1/0/5
  192.168.74.2    3808-7711-0106        I               GE1/0/6
  192.168.74.6    3808-7711-0107        I               GE1/0/7

  [Beta-Axis-01]
  192.168.65.145  3865-4911-0101        I               GE1/0/1
  192.168.65.153  3865-4911-0102        I               GE1/0/2
  192.168.65.161  3865-4911-0103        I               GE1/0/3
  192.168.65.169  3865-4911-0104        I               GE1/0/4
  192.168.65.129  3865-4911-0105        I               GE1/0/5
  192.168.65.137  3865-4911-0106        I               GE1/0/6

## Raw File References

  data/Track B/devices_outputs/4/Beta-Portal-02/display_interface_brief.txt
  data/Track B/devices_outputs/4/Beta-Portal-02/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/4/Beta-Portal-02/display_interface_description.txt
  data/Track B/devices_outputs/4/Beta-Portal-02/display_arp.txt
  data/Track B/devices_outputs/4/Alpha-Center-02/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/4/Alpha-Center-01/display_lldp_neighbor_brief.txt
  data/Track B/devices_outputs/4/Beta-Axis-02/display_lldp_neighbor_brief.txt

## Deterministic Solver Result

```
Beta-Portal-02(GE1/0/1)->Beta-Axis-01(GE1/0/6)
Beta-Portal-02(GE1/0/2)->Beta-Axis-02(GE1/0/6)
Beta-Portal-02(GE1/0/3)->Beta-Portal-01(GE1/0/3)
Beta-Portal-02(GE1/0/4)->Beta-Aegis-01(GE1/0/1)
Beta-Portal-02(GE1/0/5)->Beta-Aegis-02(GE1/0/1)
Beta-Portal-02(GE1/0/6)->Alpha-Center-01(GE1/0/2)
Beta-Portal-02(GE1/0/7)->Alpha-Center-02(GE1/0/2)
```

## v12 Answer (검증 대상)

```
Beta-Portal-02(GE1/0/1)->Beta-Axis-01(GE1/0/6)\nBeta-Portal-02(GE1/0/2)->Beta-Axis-02(GE1/0/6)\nBeta-Portal-02(GE1/0/3)->Beta-Portal-01(GE1/0/3)\nBeta-Portal-02(GE1/0/4)->Beta-Aegis-01(GE1/0/1)\nBeta-Portal-02(GE1/0/5)->Beta-Aegis-02(GE1/0/1)\nBeta-Portal-02(GE1/0/6)->Alpha-Center-01(GE1/0/2)\nBeta-Portal-02(GE1/0/7)->Alpha-Center-02(GE1/0/2)
```