# 02 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **Star Bus Ring Mesh Tree:** Define, draw its workflow, give a real example and identify one important limitation.

2. **Three Tier and Spine Leaf:** Define, draw its workflow, give a real example and identify one important limitation.

3. **Control Plane Data Plane Management Plane:** Define, draw its workflow, give a real example and identify one important limitation.

4. **High Availability and Failure Domains:** Define, draw its workflow, give a real example and identify one important limitation.

5. **Network Segmentation Zones:** Define, draw its workflow, give a real example and identify one important limitation.

6. **Underlay Overlay SDN:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **Star Bus Ring Mesh Tree — Model answer:** Topology என்பது devices link ஆகும் physical அல்லது logical pattern; star பொதுவான Ethernet LAN. **Working:** Star-இல் endpoints switch-க்கு இணைகின்றன; mesh alternate paths; ring protocol loop control தேவை. **Example:** Office PCs star topology, enterprise spine-leaf fabric scalable mesh pattern. **Nuance:** Physical topology மற்றும் logical routing path வேறுபடலாம்; virtual overlay packet path மாற்றும். **Avoid:** Single switch fault முழு star segment-ஐ பாதிக்கும்; topology choice resilience-ஐ தீர்மானிக்கும்.

2. **Three Tier and Spine Leaf — Model answer:** Traditional campus core-distribution-access; data centres leaf-spine, predictable low-hop east-west traffic. **Working:** Leaf எல்லா spines-க்கும் uplink; ECMP hash மூலம் பல equal-cost paths distribute. **Example:** Microservices data-centre racks இடையே traffic நிறைய செல்கிறது: leaf-spine ஏற்றது. **Nuance:** Clos fabrics, EVPN/VXLAN மற்றும் ECMP modern scale architecture-ஐ enable செய்கின்றன. **Avoid:** ECMP load balancing பெரும்பாலும் per-flow, ஒவ்வொரு packet-க்கும் அல்ல; hot flows இருக்கும்.

3. **Control Plane Data Plane Management Plane — Model answer:** Control plane routes/adjacencies கற்கிறது; data plane packets forward செய்கிறது; management plane configure/observe. **Working:** BGP/OSPF control; ASIC/FIB forwarding; SSH/API/telemetry management. **Example:** Route established ஆனாலும் ACL data plane traffic block செய்யலாம். **Nuance:** Programmable dataplanes P4/eBPF, SDN controllers separation-ஐ தெளிவாக பயன்படுத்துகின்றன. **Avoid:** Management interface Internet-exposed ஆக இருப்பது high risk; dedicated management plane உருவாக்கவும்.

4. **High Availability and Failure Domains — Model answer:** Redundancy என்பது backup links/devices, HA என்பது failure போது service தொடருதல். **Working:** Dual power, dual uplink, VRRP, dynamic routing, health checks combined resilience. **Example:** ஒரு fibre cut ஆனாலும் office traffic alternate ISP வழியாக செல்ல வேண்டும். **Nuance:** Fault domains, split-brain avoidance, quorum and blast radius design கற்றல் அவசியம். **Avoid:** Two firewalls இருந்தும் same power circuit என்றால் shared failure மீண்டும் உள்ளது.

5. **Network Segmentation Zones — Model answer:** Users, servers, guests, IoT, management போன்ற security zones பிரிக்கப்படுகின்றன. **Working:** VLAN/subnet/firewall policy வழியாக east-west access கட்டுப்படுகிறது. **Example:** Guest Wi-Fi-க்கு payroll DB அணுகல் இல்லை; printer access மட்டும் approved segment. **Nuance:** Macrosegmentation vs workload microsegmentation vs identity-aware policies differ. **Avoid:** Different VLAN = automatically secure அல்ல; routing firewall permit all இருந்தால் isolation இல்லை.

6. **Underlay Overlay SDN — Model answer:** Underlay physical IP reachability; overlay virtual tunnel/encapsulation; SDN control programmable interfaces. **Working:** Tunnel endpoints packets-ஐ புதிய outer header-ல் encapsulate செய்கின்றன; control plane mapping பரப்புகிறது. **Example:** Hybrid office-to-cloud VPN அல்லது Kubernetes cluster overlay. **Nuance:** Overlay MTU reduction, ECMP hashing, EVPN route-type details advanced operations இல் முக்கியம். **Avoid:** Overlay route fine இருந்தும் underlay loss இருந்தால் apps slow; இரு planes-யும் தனித்தனியாகச் சரிபார்க்கவும்.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
