# Q23: FAULT — Routing/Port Fault Detection

**scenario_id**: 936127eb-695a-4c3f-8705-23ce467c81f7
**v12 answer**: Delta-Axis-02;192.168.74.61;missing static route
**deterministic solver**: conf=H, scenarios=1개

## Question (from test.json)

The question involves two major categories of faults: routing faults and port faults. Output format requirements: each line represents one fault, no blank lines between lines, no extra whitespace before, after, or within each line, all symbols use English characters.
Routing fault output format: fault-node;destination-IP;fault-reason. Fault reasons include: (1) blackhole route; (2) missing static route; (3) static route error; (4) ARP configuration error; (5) routing loop; (6) BGP configuration error; (7) OSPF configuration error; (8) loopback IP configuration conflict; (9) VXLAN configuration error; (10) L3VPN configuration error; (11) L2VPN configuration error; (12) IS-IS configuration error; (13) SRV6-Policy tunnel planning error; if there are multiple fault reasons, output each on a new line separated by a line break.
Port fault output format: fault-node;fault-port;fault-reason. Fault reasons include: (1) shutdown; (2) interface IP error; (3) traffic congestion on port bandwidth; (4) MAC address configuration error; (5) VPN configuration missing; (6) OSPF configuration error; (7) MTU value configuration error; if there are multiple fault reasons, output each on a new line separated by a line break.
Routing fault examples:
Beta-Axis-01;192.168.1.1;blackhole route
Alpha-Center-02;192.168.1.2;missing static route
Alpha-Center-02;192.168.1.2;ARP configuration error
Port fault examples:
Beta-Portal-01;GE1/0/1;shutdown
Beta-Node-01;GE1/0/2;traffic congestion on port bandwidth
Beta-Node-01;GE1/0/2;interface IP error
Delta-Node-01 is addressing an external destination IP of 192.168.74.61, mask 30, and traffic is currently interrupted.
Please analyze the cause of traffic interruption. For path fault type questions, please answer according to the unified format requirements.

## Fault Scenarios Extracted

  Scenario 1: src=Delta-Node-01 dst_ip=192.168.74.61 suspects=[]

## Devices in Scenario

총 33개 장비 (의심 장비 5개 중점 분석)
의심: Beta-Node-01, Alpha-Center-02, Delta-Node-01, Beta-Portal-01, Beta-Axis-01

## Topology Snapshot — LLDP (의심 장비)

  Beta-Node-01 GE1/0/1 <-> Beta-Axis-01 GE1/0/1
  Beta-Node-01 GE1/0/2 <-> Beta-Axis-02 GE1/0/1
  Beta-Node-01 GE1/0/3 <-> Beta-Node-02 GE1/0/3
  Beta-Node-01 GE1/0/4 <-> Beta-Node-02 GE1/0/4
  Alpha-Center-02 GE1/0/1 <-> Beta-Portal-01 GE1/0/7
  Alpha-Center-02 GE1/0/2 <-> Beta-Portal-02 GE1/0/7
  Alpha-Center-02 GE1/0/3 <-> Delta-Portal-01 GE1/0/7
  Alpha-Center-02 GE1/0/4 <-> Delta-Portal-02 GE1/0/7
  Alpha-Center-02 GE1/0/5 <-> Gamma-Portal-01 GE1/0/7
  Alpha-Center-02 GE1/0/6 <-> Gamma-Portal-02 GE1/0/7
  Delta-Node-01 GE1/0/1 <-> Delta-Axis-01 GE1/0/1
  Delta-Node-01 GE1/0/2 <-> Delta-Axis-02 GE1/0/1
  Delta-Node-01 GE1/0/3 <-> Delta-Node-02 GE1/0/3
  Beta-Axis-01 GE1/0/2 <-> Beta-Node-02 GE1/0/1
  Beta-Axis-01 GE1/0/3 <-> Beta-Node-03 GE1/0/1
  Beta-Axis-01 GE1/0/4 <-> Beta-Node-04 GE1/0/1
  Beta-Axis-01 GE1/0/5 <-> Beta-Portal-01 GE1/0/1
  Beta-Axis-01 GE1/0/6 <-> Beta-Portal-02 GE1/0/1

## Interface Status (의심 장비 — DOWN 포함)

  **Beta-Node-01**:
    GE1/0/0              DOWN(phy=*down,proto=down)     
    GE1/0/1              UP                             192.168.65.146/30
    GE1/0/2              UP                             192.168.65.150/30
    GE1/0/3              UP                             192.168.65.209/30
    GE1/0/4              UP                             192.168.65.217/30
    GE1/0/5              DOWN(phy=*down,proto=down)     
    GE1/0/6              DOWN(phy=*down,proto=down)     
    GE1/0/7              DOWN(phy=*down,proto=down)     
    GE1/0/8              DOWN(phy=*down,proto=down)     
    GE1/0/9              DOWN(phy=*down,proto=down)     
    GE1/1/0              DOWN(phy=*down,proto=down)     
    GE1/1/1              DOWN(phy=*down,proto=down)     

  **Alpha-Center-02**:
    GE1/0/0              DOWN(phy=*down,proto=down)     
    GE1/0/1              UP                             192.168.74.5/30
    GE1/0/2              UP                             192.168.74.13/30
    GE1/0/3              UP                             192.168.74.53/30
    GE1/0/4              UP                             192.168.74.61/30
    GE1/0/5              UP                             192.168.74.37/30
    GE1/0/6              UP                             192.168.74.45/30
    GE1/0/7              DOWN(phy=*down,proto=down)     
    GE1/0/8              DOWN(phy=*down,proto=down)     
    GE1/0/9              DOWN(phy=*down,proto=down)     
    GE1/1/0              DOWN(phy=*down,proto=down)     
    GE1/1/1              DOWN(phy=*down,proto=down)     

  **Delta-Node-01**:
    GE1/0/0              DOWN(phy=*down,proto=down)     
    GE1/0/1              UP                             192.168.72.18/30
    GE1/0/2              UP                             192.168.72.22/30
    GE1/0/3              UP                             192.168.72.85/30
    GE1/0/4              DOWN(phy=*down,proto=down)     
    GE1/0/5              DOWN(phy=*down,proto=down)     
    GE1/0/6              DOWN(phy=*down,proto=down)     
    GE1/0/7              DOWN(phy=*down,proto=down)     
    GE1/0/8              DOWN(phy=*down,proto=down)     
    GE1/0/9              DOWN(phy=*down,proto=down)     
    GE1/1/0              DOWN(phy=*down,proto=down)     
    GE1/1/1              DOWN(phy=*down,proto=down)     

  **Beta-Axis-01**:
    GE1/0/0              DOWN(phy=*down,proto=down)     
    GE1/0/1              UP                             192.168.65.145/30
    GE1/0/2              UP                             192.168.65.153/30
    GE1/0/3              UP                             192.168.65.161/30
    GE1/0/4              UP                             192.168.65.169/30
    GE1/0/5              UP                             192.168.65.129/30
    GE1/0/6              UP                             192.168.65.137/30
    GE1/0/7              DOWN(phy=*down,proto=down)     
    GE1/0/8              DOWN(phy=*down,proto=down)     
    GE1/0/9              DOWN(phy=*down,proto=down)     
    GE1/1/0              DOWN(phy=*down,proto=down)     
    GE1/1/1              DOWN(phy=*down,proto=down)     


## Routing Context (의심 장비)

  **Beta-Node-01** routing table:
  192.168.65.1/32      Static   via 192.168.65.149  dev GE1/0/2
  192.168.65.2/32      Static   via 192.168.65.149  dev GE1/0/2
  192.168.65.128/30    Static   via 192.168.65.145  dev GE1/0/1
  192.168.65.132/30    Static   via 192.168.65.149  dev GE1/0/2
  192.168.65.136/30    Static   via 192.168.65.145  dev GE1/0/1
  192.168.65.140/30    Static   via 192.168.65.149  dev GE1/0/2
  192.168.65.144/30    Direct   via 192.168.65.146  dev GE1/0/1
  192.168.65.146/32    Direct   via 127.0.0.1       dev GE1/0/1
  192.168.65.147/32    Direct   via 127.0.0.1       dev GE1/0/1
  192.168.65.148/30    Direct   via 192.168.65.150  dev GE1/0/2
  192.168.65.150/32    Direct   via 127.0.0.1       dev GE1/0/2
  192.168.65.151/32    Direct   via 127.0.0.1       dev GE1/0/2
  192.168.65.152/30    Static   via 192.168.65.145  dev GE1/0/1
  192.168.65.156/30    Static   via 192.168.65.149  dev GE1/0/2
  192.168.65.160/30    Static   via 192.168.65.145  dev GE1/0/1
  192.168.65.164/30    Static   via 192.168.65.149  dev GE1/0/2
  192.168.65.168/30    Static   via 192.168.65.145  dev GE1/0/1
  192.168.65.172/30    Static   via 192.168.65.149  dev GE1/0/2
  192.168.65.176/30    Static   via 192.168.65.149  dev GE1/0/2
  192.168.65.184/30    Static   via 192.168.65.149  dev GE1/0/2

  **Alpha-Center-02** routing table:
  192.168.65.1/32      Static   via 192.168.74.46   dev GE1/0/6
  192.168.65.2/32      Direct   via 127.0.0.1       dev LoopBack1
  192.168.65.128/30    Static   via 192.168.74.6    dev GE1/0/1
  192.168.65.132/30    Static   via 192.168.74.6    dev GE1/0/1
  192.168.65.136/30    Static   via 192.168.74.14   dev GE1/0/2
  192.168.65.140/30    Static   via 192.168.74.14   dev GE1/0/2
  192.168.65.144/30    Static   via 192.168.74.14   dev GE1/0/2
  192.168.65.148/30    Static   via 192.168.74.14   dev GE1/0/2
  192.168.65.152/30    Static   via 192.168.74.14   dev GE1/0/2
  192.168.65.156/30    Static   via 192.168.74.14   dev GE1/0/2
  192.168.65.160/30    Static   via 192.168.74.14   dev GE1/0/2
  192.168.65.164/30    Static   via 192.168.74.14   dev GE1/0/2
  192.168.65.168/30    Static   via 192.168.74.14   dev GE1/0/2
  192.168.65.172/30    Static   via 192.168.74.14   dev GE1/0/2
  192.168.65.176/30    Static   via 192.168.74.6    dev GE1/0/1
  192.168.65.184/30    Static   via 192.168.74.6    dev GE1/0/1
  192.168.65.192/30    Static   via 192.168.74.14   dev GE1/0/2
  192.168.65.200/30    Static   via 192.168.74.14   dev GE1/0/2
  192.168.65.204/30    Static   via 192.168.74.14   dev GE1/0/2
  192.168.65.208/30    Static   via 192.168.74.14   dev GE1/0/2

  **Delta-Node-01** routing table:
  192.168.65.1/32      Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.2/32      Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.128/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.132/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.136/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.140/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.144/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.148/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.152/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.156/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.160/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.164/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.168/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.172/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.176/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.184/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.192/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.200/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.204/30    Static   via 192.168.72.21   dev GE1/0/2
  192.168.65.208/30    Static   via 192.168.72.21   dev GE1/0/2

  **Beta-Portal-01** routing table:
  Beta-Portal-01: 라우팅 테이블 없음

  **Beta-Axis-01** routing table:
  192.168.65.1/32      Static   via 192.168.65.138  dev GE1/0/6
  192.168.65.2/32      Static   via 192.168.65.138  dev GE1/0/6
  192.168.65.128/30    Direct   via 192.168.65.129  dev GE1/0/5
  192.168.65.129/32    Direct   via 127.0.0.1       dev GE1/0/5
  192.168.65.131/32    Direct   via 127.0.0.1       dev GE1/0/5
  192.168.65.132/30    Static   via 192.168.65.130  dev GE1/0/5
  192.168.65.136/30    Direct   via 192.168.65.137  dev GE1/0/6
  192.168.65.137/32    Direct   via 127.0.0.1       dev GE1/0/6
  192.168.65.139/32    Direct   via 127.0.0.1       dev GE1/0/6
  192.168.65.140/30    Static   via 192.168.65.138  dev GE1/0/6
  192.168.65.144/30    Direct   via 192.168.65.145  dev GE1/0/1
  192.168.65.145/32    Direct   via 127.0.0.1       dev GE1/0/1
  192.168.65.147/32    Direct   via 127.0.0.1       dev GE1/0/1
  192.168.65.148/30    Static   via 192.168.65.146  dev GE1/0/1
  192.168.65.152/30    Direct   via 192.168.65.153  dev GE1/0/2
  192.168.65.153/32    Direct   via 127.0.0.1       dev GE1/0/2
  192.168.65.155/32    Direct   via 127.0.0.1       dev GE1/0/2
  192.168.65.156/30    Static   via 192.168.65.154  dev GE1/0/2
  192.168.65.160/30    Direct   via 192.168.65.161  dev GE1/0/3
  192.168.65.161/32    Direct   via 127.0.0.1       dev GE1/0/3


## Log Buffer Snippet (오류 관련)

**Beta-Node-01** log (관련 항목):
  Mar 27 2026 07:33:23 Beta-Node-01 %%01IFNET/2/linkDown_clear(l):CID=0x807a040f-alarmID=0x08520003-clearType=service_resume;The interface status changes. (ifName=GE1/0/1, AdminStatus=UP, OperStatus=UP, Reason=Interface physical link is up, mainIfname=GE1/0/1)
  Mar 27 2026 07:33:23 Beta-Node-01 %%01IFNET/2/linkDown_clear(l):CID=0x807a040f-alarmID=0x08520003-clearType=service_resume;The interface status changes. (ifName=GE1/0/2, AdminStatus=UP, OperStatus=UP, Reason=Interface physical link is up, mainIfname=GE1/0/2)
  Mar 27 2026 07:33:23 Beta-Node-01 %%01IFNET/2/linkDown_clear(l):CID=0x807a040f-alarmID=0x08520003-clearType=service_resume;The interface status changes. (ifName=GE1/0/4, AdminStatus=UP, OperStatus=UP, Reason=Interface physical link is up, mainIfname=GE1/0/4)
  Mar 27 2026 07:33:23 Beta-Node-01 %%01IFNET/2/linkDown_clear(l):CID=0x807a040f-alarmID=0x08520003-clearType=service_resume;The interface status changes. (ifName=GE1/0/3, AdminStatus=UP, OperStatus=UP, Reason=Interface physical link is up, mainIfname=GE1/0/3)
  Mar 27 2026 07:33:23 Beta-Node-01 %%01IFNET/2/linkDown_active(l):CID=0x807a040f-alarmID=0x08520003;The interface status changes. (ifName=GE1/0/4, AdminStatus=UP, OperStatus=DOWN, Reason=Interface physical link is down, mainIfname=GE1/0/4)
  Mar 27 2026 07:33:23 Beta-Node-01 %%01IFNET/2/linkDown_active(l):CID=0x807a040f-alarmID=0x08520003;The interface status changes. (ifName=GE1/0/3, AdminStatus=UP, OperStatus=DOWN, Reason=Interface physical link is down, mainIfname=GE1/0/3)
  Mar 27 2026 07:33:23 Beta-Node-01 %%01IFNET/2/linkDown_active(l):CID=0x807a040f-alarmID=0x08520003;The interface status changes. (ifName=GE1/0/2, AdminStatus=UP, OperStatus=DOWN, Reason=Interface physical link is down, mainIfname=GE1/0/2)
  Mar 27 2026 07:33:23 Beta-Node-01 %%01IFNET/2/linkDown_active(l):CID=0x807a040f-alarmID=0x08520003;The interface status changes. (ifName=GE1/0/1, AdminStatus=UP, OperStatus=DOWN, Reason=Interface physical link is down, mainIfname=GE1/0/1)
  Mar 27 2026 07:28:45 Beta-Node-01 %%01CONFIGURATION/3/ROLLBACK_FAIL(l):CID=0x80cb000c;Configuration rollback finished, but some warnings occurred or there are still several differences.
  Mar 27 2026 07:28:44 Beta-Node-01 %%01IFNET/2/linkDown_active(l):CID=0x807a040f-alarmID=0x08520003;The interface status changes. (ifName=GE1/0/1, AdminStatus=DOWN, OperStatus=DOWN, Reason=The interface is shut down, mainIfname=GE1/0/1)

## Raw File References

  data/Track B/devices_outputs/23/Beta-Node-01/display_ip_routing-table.txt
  data/Track B/devices_outputs/23/Beta-Node-01/display_interface_brief.txt
  data/Track B/devices_outputs/23/Beta-Node-01/display_ip_interface_brief.txt
  data/Track B/devices_outputs/23/Alpha-Center-02/display_ip_routing-table.txt
  data/Track B/devices_outputs/23/Alpha-Center-02/display_interface_brief.txt
  data/Track B/devices_outputs/23/Alpha-Center-02/display_ip_interface_brief.txt
  data/Track B/devices_outputs/23/Delta-Node-01/display_ip_routing-table.txt
  data/Track B/devices_outputs/23/Delta-Node-01/display_interface_brief.txt
  data/Track B/devices_outputs/23/Delta-Node-01/display_ip_interface_brief.txt
  data/Track B/devices_outputs/23/Beta-Portal-01/display_ip_routing-table.txt
  data/Track B/devices_outputs/23/Beta-Portal-01/display_interface_brief.txt
  data/Track B/devices_outputs/23/Beta-Portal-01/display_ip_interface_brief.txt
  data/Track B/devices_outputs/23/Beta-Axis-01/display_ip_routing-table.txt
  data/Track B/devices_outputs/23/Beta-Axis-01/display_interface_brief.txt
  data/Track B/devices_outputs/23/Beta-Axis-01/display_ip_interface_brief.txt

## Deterministic Solver Result

```
Delta-Axis-02;192.168.74.61;missing static route
```

## v12 Answer (검증 대상)

```
Delta-Axis-02;192.168.74.61;missing static route
```