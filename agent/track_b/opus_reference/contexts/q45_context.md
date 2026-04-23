# Q45: FAULT — Routing/Port Fault Detection

**scenario_id**: b20f9906-9180-4ba0-a97a-75256abc0206
**v12 answer**: Aegis-Prime-02;Eth-Trunk2.60;shutdown
**deterministic solver**: conf=M, scenarios=1개

## Question (from test.json)

The exam involves two major categories of faults: routing faults and port faults. Output format requirements: each line represents one fault, no blank lines between lines, no extra whitespace characters before, after, or within each line, all symbols use English characters.
Routing fault output format: fault-node;destination-IP;fault-reason. Fault reasons include: (1) blackhole route; (2) missing static route; (3) static route error; (4) ARP configuration error; (5) routing loop; (6) BGP configuration error; (7) OSPF configuration error; (8) loopback IP configuration conflict; (9) VXLAN configuration error; (10) L3VPN configuration error; (11) L2VPN configuration error; (12) IS-IS configuration error; (13) SRV6-Policy tunnel planning error; if there are multiple fault reasons, output each on a new line.
Port fault output format: fault-node;fault-port;fault-reason. Fault reasons include: (1) shutdown; (2) interface IP error; (3) traffic congestion on port bandwidth; (4) MAC address configuration error; (5) VPN configuration missing; (6) OSPF configuration error; (7) MTU value configuration error; (8) host information collection function missing; if there are multiple fault reasons, output each on a new line.
Routing fault examples:
Beta-Axis-01;192.168.1.1;blackhole route
Alpha-Center-02;192.168.1.2;missing static route
Alpha-Center-02;192.168.1.2;ARP configuration error
Port fault examples:
Beta-Portal-01;GE1/0/1;shutdown
Beta-Node-01;GE1/0/2;traffic congestion on port bandwidth
Beta-Node-01;GE1/0/2;interface IP error
PJ area, Hermes-Prime-01 pings an external address and finds it unreachable, ping 10.60.1.2

## Fault Scenarios Extracted

  Scenario 1: src=Hermes-Prime-01 dst_ip=10.60.1.2 suspects=[]

## Devices in Scenario

총 23개 장비 (의심 장비 1개 중점 분석)
의심: Hermes-Prime-01

## Topology Snapshot — LLDP (의심 장비)

  Hermes-Prime-01 GE1/0/4 <-> Demeter-Prime-01 GE1/0/5

## Interface Status (의심 장비 — DOWN 포함)

  **Hermes-Prime-01**:
    GE1/0/0              DOWN(phy=*down,proto=down)     
    GE1/0/1              DOWN(phy=*down,proto=down)     
    GE1/0/2              DOWN(phy=*down,proto=down)     
    GE1/0/3              DOWN(phy=*down,proto=down)     
    GE1/0/5              DOWN(phy=*down,proto=down)     
    GE1/0/6              DOWN(phy=*down,proto=down)     
    GE1/0/7              DOWN(phy=*down,proto=down)     
    GE1/0/8              DOWN(phy=*down,proto=down)     
    GE1/0/9              DOWN(phy=*down,proto=down)     
    GE1/1/0              DOWN(phy=*down,proto=down)     
    GE1/1/1              DOWN(phy=*down,proto=down)     
    GE1/1/2              DOWN(phy=*down,proto=down)     


## Routing Context (의심 장비)

  **Hermes-Prime-01** routing table:
  10.60.1.0/24         Static   via 10.1.5.1        dev Vlanif50


## Log Buffer Snippet (오류 관련)

**Hermes-Prime-01** log (관련 항목):
  Mar 24 2026 23:27:24 Hermes-Prime-01 %%01CONFIGURATION/3/ROLLBACK_FAIL(l):CID=0x80cb000c;Configuration rollback finished, but some warnings occurred or there are still several differences.
  Mar 24 2026 23:27:24 Hermes-Prime-01 %%01IFNET/2/linkDown_clear(l):CID=0x807a0408-alarmID=0x08520003-clearType=service_resume;The interface status changes. (ifName=Vlanif70, AdminStatus=UP, OperStatus=UP, Reason=Interface physical link is up, mainIfname=Vlanif70)
  Mar 24 2026 23:27:24 Hermes-Prime-01 %%01IFNET/2/linkDown_clear(l):CID=0x807a0408-alarmID=0x08520003-clearType=service_resume;The interface status changes. (ifName=Vlanif60, AdminStatus=UP, OperStatus=UP, Reason=Interface physical link is up, mainIfname=Vlanif60)
  Mar 24 2026 23:27:24 Hermes-Prime-01 %%01IFNET/2/linkDown_clear(l):CID=0x807a0408-alarmID=0x08520003-clearType=service_resume;The interface status changes. (ifName=Vlanif50, AdminStatus=UP, OperStatus=UP, Reason=Interface physical link is up, mainIfname=Vlanif50)
  Mar 24 2026 23:27:24 Hermes-Prime-01 %%01IFNET/2/linkDown_clear(l):CID=0x807a0408-alarmID=0x08520003-clearType=service_resume;The interface status changes. (ifName=Vlanif40, AdminStatus=UP, OperStatus=UP, Reason=Interface physical link is up, mainIfname=Vlanif40)
  Mar 24 2026 23:27:24 Hermes-Prime-01 %%01IFNET/2/linkDown_clear(l):CID=0x807a0408-alarmID=0x08520003-clearType=service_resume;The interface status changes. (ifName=Vlanif30, AdminStatus=UP, OperStatus=UP, Reason=Interface physical link is up, mainIfname=Vlanif30)
  Mar 24 2026 23:27:24 Hermes-Prime-01 %%01IFNET/2/linkDown_clear(l):CID=0x807a0408-alarmID=0x08520003-clearType=service_resume;The interface status changes. (ifName=Vlanif20, AdminStatus=UP, OperStatus=UP, Reason=Interface physical link is up, mainIfname=Vlanif20)
  Mar 24 2026 23:27:24 Hermes-Prime-01 %%01IFNET/2/linkDown_clear(l):CID=0x807a0408-alarmID=0x08520003-clearType=service_resume;The interface status changes. (ifName=Vlanif10, AdminStatus=UP, OperStatus=UP, Reason=Interface physical link is up, mainIfname=Vlanif10)
  Mar 24 2026 23:27:24 Hermes-Prime-01 %%01IFNET/2/linkDown_clear(l):CID=0x807a0408-alarmID=0x08520003-clearType=service_resume;The interface status changes. (ifName=GE1/0/4, AdminStatus=UP, OperStatus=UP, Reason=Interface physical link is up, mainIfname=GE1/0/4)
  Mar 24 2026 23:27:24 Hermes-Prime-01 %%01IFNET/2/linkDown_active(l):CID=0x807a0408-alarmID=0x08520003;The interface status changes. (ifName=GE1/0/4, AdminStatus=UP, OperStatus=DOWN, Reason=Interface physical link is down, mainIfname=GE1/0/4)

## Raw File References

  data/Track B/devices_outputs/45/Hermes-Prime-01/display_ip_routing-table.txt
  data/Track B/devices_outputs/45/Hermes-Prime-01/display_interface_brief.txt
  data/Track B/devices_outputs/45/Hermes-Prime-01/display_ip_interface_brief.txt

## Deterministic Solver Result

```
Aegis-Prime-02;Eth-Trunk2.60;shutdown
```

## v12 Answer (검증 대상)

```
Aegis-Prime-02;Eth-Trunk2.60;shutdown
```