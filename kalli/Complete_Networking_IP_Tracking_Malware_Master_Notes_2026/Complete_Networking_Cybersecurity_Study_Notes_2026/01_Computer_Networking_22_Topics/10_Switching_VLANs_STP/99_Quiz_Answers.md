# 10 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **Ethernet Switching MAC Tables:** Define, draw its workflow, give a real example and identify one important limitation.

2. **Access Trunk VLAN 8021Q:** Define, draw its workflow, give a real example and identify one important limitation.

3. **STP RSTP Loop Prevention:** Define, draw its workflow, give a real example and identify one important limitation.

4. **Link Aggregation LACP:** Define, draw its workflow, give a real example and identify one important limitation.

5. **8021X NAC and Device Trust:** Define, draw its workflow, give a real example and identify one important limitation.

6. **VXLAN EVPN Modern L2 Over L3:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **Ethernet Switching MAC Tables — Model answer:** Switch learns source MAC to port, forwards known destination, floods unknown/broadcast. **Working:** MAC table entries age out; one broadcast domain spans VLAN member ports. **Example:** PC-A sends frame to PC-B, initially flooded then unicast. **Nuance:** Storm control, MAC move detection, port-security mitigate layer-2 abuse. **Avoid:** MAC spoofing or loops cause MAC flapping; observe logs.

2. **Access Trunk VLAN 8021Q — Model answer:** VLAN logically partitions broadcast domains; access carries single VLAN; trunk tags many VLANs. **Working:** 802.1Q header adds VLAN ID in frame; switch enforces membership. **Example:** Staff VLAN 10, Guest VLAN 20, Server VLAN 30 on same cabling. **Nuance:** Native VLAN mismatch and double-tagging are nuanced security/operation risks. **Avoid:** Inter-VLAN communication requires L3 routing and appropriate firewall rules.

3. **STP RSTP Loop Prevention — Model answer:** Layer 2 loops multiply broadcasts; Spanning Tree blocks redundant paths logically. **Working:** Root bridge elected; port roles choose forwarding/discarding. **Example:** Two access switches with backup link don't create endless packet loop. **Nuance:** MSTP, RSTP, BPDU guard, root guard; data-centre EVPN may reduce L2 stretch. **Avoid:** Do not randomly disable STP in bridged network; outages spread quickly.

4. **Link Aggregation LACP — Model answer:** LACP bundles physical links as logical aggregate to gain resilience/capacity. **Working:** Flows hashed onto members, not always per-packet load spread. **Example:** 2x1Gbps uplinks can support multiple flows but one flow often still 1Gbps. **Nuance:** LACP timers, hashing asymmetry and MLAG add complexity. **Avoid:** Misconfigured member links blackhole traffic or cause out-of-order frames.

5. **8021X NAC and Device Trust — Model answer:** Network access control validates user/device before assigning connectivity. **Working:** Supplicant authenticates via AP/switch to RADIUS; authorization chooses VLAN/policy. **Example:** University staff laptop access secure VLAN after certificate auth. **Nuance:** EAP-TLS, dynamic VLAN assignment, posture checks, MACsec link security. **Avoid:** MAC address filtering alone weak identity; guests need limited zone.

6. **VXLAN EVPN Modern L2 Over L3 — Model answer:** VXLAN encapsulates L2 frames inside UDP over routed IP fabric, 24-bit VNI. **Working:** VTEPs add outer UDP/IP; EVPN/BGP distributes MAC/IP reachability. **Example:** Data-centre virtual machines on same logical subnet across racks. **Nuance:** ARP suppression, anycast gateway, BGP EVPN route types, multihoming. **Avoid:** Overlay adds bytes reducing effective MTU; troubleshoot underlay and VTEPs.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
