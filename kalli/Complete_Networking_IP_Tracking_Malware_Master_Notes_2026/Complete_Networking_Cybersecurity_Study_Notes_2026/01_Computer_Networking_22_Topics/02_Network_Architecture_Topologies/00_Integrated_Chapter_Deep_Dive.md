# 02 — Integrated Deep-Dive Textbook: Network Architecture Topologies

## Big Picture: what makes this chapter important?

கட்டமைப்பு, redundancy, control plane/data plane, campus மற்றும் data-centre patterns. For an office, a hierarchical campus design clarifies which switch connects users and where security boundaries lie. For data centers, leaf-spine fabrics reduce unpredictable hop differences among racks and support many parallel links. The underlay is physical/routed reachability, while overlays can create virtual tenant networks. Redundant hardware must also use independent power paths and appropriate control-plane failover.

## Architecture / Packet Path Diagram

```text
Users --> Access switches --> Distribution/Core --> Edge --> WAN
Servers --> Leaf-1/Leaf-2 --> Spine-1/Spine-2 --> DC edge
```

**Interpretation:** Choose topology using fault-domain boundaries: redundant links do not help if every switch depends on one power circuit or control-plane device.

## Deep worked learning sequence

Read each lesson below as a connected narrative. For detailed individual exam Q&A, use the numbered subtopic files; for assignments do the Lab Workbook.

### 1. Star Bus Ring Mesh Tree

**Definition and intuition:** Topology என்பது devices link ஆகும் physical அல்லது logical pattern; star பொதுவான Ethernet LAN.

**Mechanism in plain terms:** Star-இல் endpoints switch-க்கு இணைகின்றன; mesh alternate paths; ring protocol loop control தேவை.

**Industry situation:** Office PCs star topology, enterprise spine-leaf fabric scalable mesh pattern.

**Rare/advanced case to study next:** Physical topology மற்றும் logical routing path வேறுபடலாம்; virtual overlay packet path மாற்றும்.

**How you prove/disprove your first guess:** Single switch fault முழு star segment-ஐ பாதிக்கும்; topology choice resilience-ஐ தீர்மானிக்கும்.

**Mini exercise:** Single-switch மற்றும் dual-switch diagrams வரைந்து failure domain ஒப்பிடவும்.

### 2. Three Tier and Spine Leaf

**Definition and intuition:** Traditional campus core-distribution-access; data centres leaf-spine, predictable low-hop east-west traffic.

**Mechanism in plain terms:** Leaf எல்லா spines-க்கும் uplink; ECMP hash மூலம் பல equal-cost paths distribute.

**Industry situation:** Microservices data-centre racks இடையே traffic நிறைய செல்கிறது: leaf-spine ஏற்றது.

**Rare/advanced case to study next:** Clos fabrics, EVPN/VXLAN மற்றும் ECMP modern scale architecture-ஐ enable செய்கின்றன.

**How you prove/disprove your first guess:** ECMP load balancing பெரும்பாலும் per-flow, ஒவ்வொரு packet-க்கும் அல்ல; hot flows இருக்கும்.

**Mini exercise:** 3-leaf 2-spine ASCII diagram வரைந்து leaf-to-leaf பாதைகள் எண்ணவும்.

### 3. Control Plane Data Plane Management Plane

**Definition and intuition:** Control plane routes/adjacencies கற்கிறது; data plane packets forward செய்கிறது; management plane configure/observe.

**Mechanism in plain terms:** BGP/OSPF control; ASIC/FIB forwarding; SSH/API/telemetry management.

**Industry situation:** Route established ஆனாலும் ACL data plane traffic block செய்யலாம்.

**Rare/advanced case to study next:** Programmable dataplanes P4/eBPF, SDN controllers separation-ஐ தெளிவாக பயன்படுத்துகின்றன.

**How you prove/disprove your first guess:** Management interface Internet-exposed ஆக இருப்பது high risk; dedicated management plane உருவாக்கவும்.

**Mini exercise:** ஒரு router-ல் route config, packet forwarding, admin login ஒவ்வொன்றை தனியாக எழுதவும்.

### 4. High Availability and Failure Domains

**Definition and intuition:** Redundancy என்பது backup links/devices, HA என்பது failure போது service தொடருதல்.

**Mechanism in plain terms:** Dual power, dual uplink, VRRP, dynamic routing, health checks combined resilience.

**Industry situation:** ஒரு fibre cut ஆனாலும் office traffic alternate ISP வழியாக செல்ல வேண்டும்.

**Rare/advanced case to study next:** Fault domains, split-brain avoidance, quorum and blast radius design கற்றல் அவசியம்.

**How you prove/disprove your first guess:** Two firewalls இருந்தும் same power circuit என்றால் shared failure மீண்டும் உள்ளது.

**Mini exercise:** Topology-யில் 3 single points of failure கண்டறிந்து மாற்றுத் திட்டம் உருவாக்கவும்.

### 5. Network Segmentation Zones

**Definition and intuition:** Users, servers, guests, IoT, management போன்ற security zones பிரிக்கப்படுகின்றன.

**Mechanism in plain terms:** VLAN/subnet/firewall policy வழியாக east-west access கட்டுப்படுகிறது.

**Industry situation:** Guest Wi-Fi-க்கு payroll DB அணுகல் இல்லை; printer access மட்டும் approved segment.

**Rare/advanced case to study next:** Macrosegmentation vs workload microsegmentation vs identity-aware policies differ.

**How you prove/disprove your first guess:** Different VLAN = automatically secure அல்ல; routing firewall permit all இருந்தால் isolation இல்லை.

**Mini exercise:** Guest/Staff/Servers zones-க்கு allow/deny matrix உருவாக்கவும்.

### 6. Underlay Overlay SDN

**Definition and intuition:** Underlay physical IP reachability; overlay virtual tunnel/encapsulation; SDN control programmable interfaces.

**Mechanism in plain terms:** Tunnel endpoints packets-ஐ புதிய outer header-ல் encapsulate செய்கின்றன; control plane mapping பரப்புகிறது.

**Industry situation:** Hybrid office-to-cloud VPN அல்லது Kubernetes cluster overlay.

**Rare/advanced case to study next:** Overlay MTU reduction, ECMP hashing, EVPN route-type details advanced operations இல் முக்கியம்.

**How you prove/disprove your first guess:** Overlay route fine இருந்தும் underlay loss இருந்தால் apps slow; இரு planes-யும் தனித்தனியாகச் சரிபார்க்கவும்.

**Mini exercise:** Packet encapsulation drawing: inner IP + UDP/VXLAN + outer IP + Ethernet.

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

- [Kubernetes Gateway API Documentation](https://gateway-api.sigs.k8s.io/docs/introduction/)
- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
