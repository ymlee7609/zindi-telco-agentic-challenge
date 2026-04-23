# Q42: FAULT — Routing/Port Fault Detection

**scenario_id**: 7f9d4a00-9e4a-40c6-becb-c2c770972aba
**v12 answer**: Demeter-Prime-02;GE1/0/5;MAC address configuration error
**deterministic solver**: conf=H, scenarios=1개

## Question (from test.json)

The exam involves two major categories of faults: routing faults and port faults. Output format requirements: each line represents one fault, no blank lines between lines, no extra whitespace before, after, or within each line, all symbols use English characters.
Routing fault output format: fault node;destination IP;fault reason. Fault reasons include: (1) blackhole route; (2) missing static route; (3) static route error; (4) ARP configuration error; (5) routing loop; (6) BGP configuration error; (7) OSPF configuration error; (8) loopback IP configuration conflict; (9) VXLAN configuration error; (10) L3VPN configuration error; (11) L2VPN configuration error; (12) IS-IS configuration error; (13) SRV6-Policy tunnel planning error; if there are multiple fault reasons, output each on a new line.
Port fault output format: fault node;fault port;fault reason. Fault reasons include: (1) shutdown; (2) interface IP error; (3) traffic congestion on port bandwidth; (4) MAC address configuration error; (5) VPN configuration missing; (6) OSPF configuration error; (7) MTU value configuration error; (8) host information collection function missing; if there are multiple fault reasons, output each on a new line.
Routing fault examples:
Beta-Axis-01;192.168.1.1;blackhole route
Alpha-Center-02;192.168.1.2;missing static route
Alpha-Center-02;192.168.1.2;ARP configuration error
Port fault examples:
Beta-Portal-01;GE1/0/1;shutdown
Beta-Node-01;GE1/0/2;traffic congestion on port bandwidth
Beta-Node-01;GE1/0/2;interface IP error
PJ area, a Demeter-Prime-02 received a MAC address conflict alarm

## Fault Scenarios Extracted

  Scenario 1: src=Demeter-Prime-02 dst_ip=None suspects=[]

## Devices in Scenario

총 23개 장비 (의심 장비 1개 중점 분석)
의심: Demeter-Prime-02

## Topology Snapshot — LLDP (의심 장비)

  Demeter-Prime-02 GE1/0/0 <-> Atlas-Prime-01 GE1/0/3
  Demeter-Prime-02 GE1/0/1 <-> Atlas-Prime-02 GE1/0/3
  Demeter-Prime-02 GE1/0/5 <-> Hermes-Prime-02 GE1/0/4

## Interface Status (의심 장비 — DOWN 포함)

  **Demeter-Prime-02**:
    GE1/0/0              UP                             192.168.2.6/30
    GE1/0/1              UP                             192.168.2.14/30
    GE1/0/2              DOWN(phy=down,proto=down)      
    GE1/0/3              DOWN(phy=down,proto=down)      
    GE1/0/4              DOWN(phy=down,proto=down)      
    GE1/0/6              DOWN(phy=down,proto=down)      
    GE1/0/7              DOWN(phy=down,proto=down)      
    GE1/0/8              DOWN(phy=down,proto=down)      
    GE1/0/9              DOWN(phy=down,proto=down)      
    GE1/1/0              DOWN(phy=*down,proto=down)     
    GE1/1/1              DOWN(phy=*down,proto=down)     
    GE1/1/2              DOWN(phy=*down,proto=down)     


## Routing Context (의심 장비)

  **Demeter-Prime-02** routing table:
  1.1.1.1/32           OSPF     via 192.168.2.5     dev GE1/0/0
  1.1.1.2/32           OSPF     via 192.168.2.13    dev GE1/0/1
  1.1.2.1/32           OSPF     via 192.168.2.13    dev GE1/0/1
  1.1.2.2/32           Direct   via 127.0.0.1       dev LoopBack0
  1.1.5.1/32           OSPF     via 192.168.2.13    dev GE1/0/1
  1.1.5.2/32           OSPF     via 192.168.2.13    dev GE1/0/1
  10.3.1.0/24          OSPF     via 192.168.2.13    dev GE1/0/1
  10.3.1.1/32          OSPF     via 192.168.2.13    dev GE1/0/1
  10.101.1.0/24        OSPF     via 192.168.2.13    dev GE1/0/1
  127.0.0.0/8          Direct   via 127.0.0.1       dev InLoopBack0
  127.0.0.1/32         Direct   via 127.0.0.1       dev InLoopBack0
  127.255.255.255/32   Direct   via 127.0.0.1       dev InLoopBack0
  192.168.1.0/30       OSPF     via 192.168.2.5     dev GE1/0/0
  192.168.1.4/30       OSPF     via 192.168.2.5     dev GE1/0/0
  192.168.1.8/30       OSPF     via 192.168.2.13    dev GE1/0/1
  192.168.1.12/30      OSPF     via 192.168.2.13    dev GE1/0/1
  192.168.2.0/30       OSPF     via 192.168.2.5     dev GE1/0/0
  192.168.2.4/30       Direct   via 192.168.2.6     dev GE1/0/0
  192.168.2.6/32       Direct   via 127.0.0.1       dev GE1/0/0
  192.168.2.7/32       Direct   via 127.0.0.1       dev GE1/0/0


## Log Buffer Snippet (오류 관련)

**Demeter-Prime-02** log (관련 항목):
  Mar 24 2026 22:42:40 Demeter-Prime-02 %%01NVO3/4/NVO3_TUNNEL_DOWN(l):CID=0x81a1044b;The status of the vxlan tunnel changed to down. (SourceIpAddress=1.1.2.2, DestinationIpAddress=1.1.5.2, TunnelStatus=DOWN)
  Mar 24 2026 22:42:40 Demeter-Prime-02 %%01NVO3/2/IPv4VxlanTunnelDown_clear(l):CID=0x81a1044b-alarmID=0x0a112005-clearType=service_resume;The IPv4 vxlan tunnel status changes. (SourceIpAddress=1.1.2.2, DestinationIpAddress=1.1.5.2, TunnelStatus=UP)
  Mar 24 2026 22:42:38 Demeter-Prime-02 %%01NVO3/4/NVO3_TUNNEL_DOWN(l):CID=0x81a1044b;The status of the vxlan tunnel changed to down. (SourceIpAddress=1.1.2.2, DestinationIpAddress=1.1.2.1, TunnelStatus=DOWN)
  Mar 24 2026 22:42:38 Demeter-Prime-02 %%01NVO3/4/NVO3_TUNNEL_DOWN(l):CID=0x81a1044b;The status of the vxlan tunnel changed to down. (SourceIpAddress=1.1.2.2, DestinationIpAddress=1.1.5.1, TunnelStatus=DOWN)
  Mar 24 2026 22:42:38 Demeter-Prime-02 %%01NVO3/2/IPv4VxlanTunnelDown_clear(l):CID=0x81a1044b-alarmID=0x0a112005-clearType=service_resume;The IPv4 vxlan tunnel status changes. (SourceIpAddress=1.1.2.2, DestinationIpAddress=1.1.2.1, TunnelStatus=UP)
  Mar 24 2026 22:42:38 Demeter-Prime-02 %%01NVO3/2/IPv4VxlanTunnelDown_clear(l):CID=0x81a1044b-alarmID=0x0a112005-clearType=service_resume;The IPv4 vxlan tunnel status changes. (SourceIpAddress=1.1.2.2, DestinationIpAddress=1.1.5.1, TunnelStatus=UP)
  Mar 24 2026 22:42:37 Demeter-Prime-02 %%01BGP/2/bgpBackwardTransition_clear(l):CID=0x8013044e-alarmID=0x0879000f-clearType=service_resume;The BGP FSM enters the Established state. (BgpPeerRemoteAddr=1.1.1.1, BgpPeerLastError=0 , BgpPeerState=6, LocalIfName=-, Reason=Alarm clear, Description=)
  Mar 24 2026 22:42:37 Demeter-Prime-02 %%01BGP/2/PEER_ESTABLISHED_NOTIFICATION(l):CID=0x8013044e;The BGP FSM enters the Established state. (BgpPeerRemoteAddr=1.1.1.1, BgpPeerLastError=0, BgpPeerState=6,VpnInstance=_public_)
  Mar 24 2026 22:42:19 Demeter-Prime-02 %%01BGP/2/bgpBackwardTransition_clear(l):CID=0x8013044e-alarmID=0x0879000f-clearType=service_resume;The BGP FSM enters the Established state. (BgpPeerRemoteAddr=1.1.1.2, BgpPeerLastError=0 , BgpPeerState=6, LocalIfName=-, Reason=Alarm clear, Description=)
  Mar 24 2026 22:42:19 Demeter-Prime-02 %%01BGP/2/PEER_ESTABLISHED_NOTIFICATION(l):CID=0x8013044e;The BGP FSM enters the Established state. (BgpPeerRemoteAddr=1.1.1.2, BgpPeerLastError=0, BgpPeerState=6,VpnInstance=_public_)

## Raw File References

  data/Track B/devices_outputs/42/Demeter-Prime-02/display_ip_routing-table.txt
  data/Track B/devices_outputs/42/Demeter-Prime-02/display_interface_brief.txt
  data/Track B/devices_outputs/42/Demeter-Prime-02/display_ip_interface_brief.txt

## Deterministic Solver Result

```
Demeter-Prime-02;GE1/0/5;MAC address configuration error
```

## v12 Answer (검증 대상)

```
Demeter-Prime-02;GE1/0/5;MAC address configuration error
```