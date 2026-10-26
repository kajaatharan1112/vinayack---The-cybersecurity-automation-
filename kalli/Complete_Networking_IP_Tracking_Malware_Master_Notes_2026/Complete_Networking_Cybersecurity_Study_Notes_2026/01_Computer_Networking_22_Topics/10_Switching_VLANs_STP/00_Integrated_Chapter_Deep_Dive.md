# 10 — Integrated Deep-Dive Textbook: Switching VLANs STP

## Big Picture: what makes this chapter important?

Local network frames, loops, virtualization and defence. Switches learn source MAC addresses and forward by destination, but broadcast/unknown traffic is flooded within a VLAN. A loop without proper spanning-tree or loop-avoiding fabric floods exponentially. A VLAN is a broadcast isolation tool; it needs Layer 3 policy for secure communication between user, guest and database networks. Tagged trunks and access ports must agree on VLAN assignments.

## Architecture / Packet Path Diagram

```text
Host A (VLAN10) --[Access port]--> Switch ==[802.1Q trunk]== Switch <-- Host B (VLAN20)
                                \--> Router/L3 firewall for inter-VLAN traffic
```

**Interpretation:** VLAN separation limits broadcasts, but firewall/ACL policy enforces cross-segment security. Redundant bridging must avoid loops.

## Deep worked learning sequence

Read each lesson below as a connected narrative. For detailed individual exam Q&A, use the numbered subtopic files; for assignments do the Lab Workbook.

### 1. Ethernet Switching MAC Tables

**Definition and intuition:** Switch learns source MAC to port, forwards known destination, floods unknown/broadcast.

**Mechanism in plain terms:** MAC table entries age out; one broadcast domain spans VLAN member ports.

**Industry situation:** PC-A sends frame to PC-B, initially flooded then unicast.

**Rare/advanced case to study next:** Storm control, MAC move detection, port-security mitigate layer-2 abuse.

**How you prove/disprove your first guess:** MAC spoofing or loops cause MAC flapping; observe logs.

**Mini exercise:** Sketch learning sequence for three hosts on four-port switch.

### 2. Access Trunk VLAN 8021Q

**Definition and intuition:** VLAN logically partitions broadcast domains; access carries single VLAN; trunk tags many VLANs.

**Mechanism in plain terms:** 802.1Q header adds VLAN ID in frame; switch enforces membership.

**Industry situation:** Staff VLAN 10, Guest VLAN 20, Server VLAN 30 on same cabling.

**Rare/advanced case to study next:** Native VLAN mismatch and double-tagging are nuanced security/operation risks.

**How you prove/disprove your first guess:** Inter-VLAN communication requires L3 routing and appropriate firewall rules.

**Mini exercise:** Design port table: access VLAN and tagged uplinks.

### 3. STP RSTP Loop Prevention

**Definition and intuition:** Layer 2 loops multiply broadcasts; Spanning Tree blocks redundant paths logically.

**Mechanism in plain terms:** Root bridge elected; port roles choose forwarding/discarding.

**Industry situation:** Two access switches with backup link don't create endless packet loop.

**Rare/advanced case to study next:** MSTP, RSTP, BPDU guard, root guard; data-centre EVPN may reduce L2 stretch.

**How you prove/disprove your first guess:** Do not randomly disable STP in bridged network; outages spread quickly.

**Mini exercise:** Draw triangle switch topology and indicate one blocked path.

### 4. Link Aggregation LACP

**Definition and intuition:** LACP bundles physical links as logical aggregate to gain resilience/capacity.

**Mechanism in plain terms:** Flows hashed onto members, not always per-packet load spread.

**Industry situation:** 2x1Gbps uplinks can support multiple flows but one flow often still 1Gbps.

**Rare/advanced case to study next:** LACP timers, hashing asymmetry and MLAG add complexity.

**How you prove/disprove your first guess:** Misconfigured member links blackhole traffic or cause out-of-order frames.

**Mini exercise:** Explain why 2x1Gbps does not guarantee a single 2Gbps TCP download.

### 5. 8021X NAC and Device Trust

**Definition and intuition:** Network access control validates user/device before assigning connectivity.

**Mechanism in plain terms:** Supplicant authenticates via AP/switch to RADIUS; authorization chooses VLAN/policy.

**Industry situation:** University staff laptop access secure VLAN after certificate auth.

**Rare/advanced case to study next:** EAP-TLS, dynamic VLAN assignment, posture checks, MACsec link security.

**How you prove/disprove your first guess:** MAC address filtering alone weak identity; guests need limited zone.

**Mini exercise:** Draw supplicant → authenticator → authentication server trust path.

### 6. VXLAN EVPN Modern L2 Over L3

**Definition and intuition:** VXLAN encapsulates L2 frames inside UDP over routed IP fabric, 24-bit VNI.

**Mechanism in plain terms:** VTEPs add outer UDP/IP; EVPN/BGP distributes MAC/IP reachability.

**Industry situation:** Data-centre virtual machines on same logical subnet across racks.

**Rare/advanced case to study next:** ARP suppression, anycast gateway, BGP EVPN route types, multihoming.

**How you prove/disprove your first guess:** Overlay adds bytes reducing effective MTU; troubleshoot underlay and VTEPs.

**Mini exercise:** Diagram inner Ethernet + VXLAN + UDP + outer IP packet.

## Production-level decision checklist

1. **Boundary:** Which component has ownership of the behavior? Clarify endpoint, device, service and provider.
2. **Baseline:** What is expected when the system works? Record concrete route, protocol, log fields and time.
3. **Observation:** Which evidence supports the suspected cause and what is merely correlation?
4. **Security:** Which minimum privileges, segmented paths, keys and logging are required?
5. **Modern dependency:** What version/hardware/standard/vendor limitations change behavior?
6. **Roll-back plan:** Could a proposed fix break other users? Test in lab first.

## Chapter exam challenge

Explain at least three subtopics using a diagram; then provide one failure that could be misdiagnosed, the correct measurement, a modern industry exception, and an ethically safe lab demonstration.

## Official background

- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [CISA 2025 Microsegmentation Guidance](https://www.cisa.gov/news-events/alerts/2025/07/29/cisa-releases-part-one-zero-trust-microsegmentation-guidance)
