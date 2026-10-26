# 02 — Practical Lab and Troubleshooting Workbook

## Objective

கட்டமைப்பு, redundancy, control plane/data plane, campus மற்றும் data-centre patterns.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | Star Bus Ring Mesh Tree | Single-switch மற்றும் dual-switch diagrams வரைந்து failure domain ஒப்பிடவும். | Diagram + observation + uncertainty |
| 2 | Three Tier and Spine Leaf | 3-leaf 2-spine ASCII diagram வரைந்து leaf-to-leaf பாதைகள் எண்ணவும். | Diagram + observation + uncertainty |
| 3 | Control Plane Data Plane Management Plane | ஒரு router-ல் route config, packet forwarding, admin login ஒவ்வொன்றை தனியாக எழுதவும். | Diagram + observation + uncertainty |
| 4 | High Availability and Failure Domains | Topology-யில் 3 single points of failure கண்டறிந்து மாற்றுத் திட்டம் உருவாக்கவும். | Diagram + observation + uncertainty |
| 5 | Network Segmentation Zones | Guest/Staff/Servers zones-க்கு allow/deny matrix உருவாக்கவும். | Diagram + observation + uncertainty |
| 6 | Underlay Overlay SDN | Packet encapsulation drawing: inner IP + UDP/VXLAN + outer IP + Ethernet. | Diagram + observation + uncertainty |

## Detailed sample walkthrough: Star Bus Ring Mesh Tree

**1 — Scenario:** Office PCs star topology, enterprise spine-leaf fabric scalable mesh pattern.

**2 — Predict:** Topology என்பது devices link ஆகும் physical அல்லது logical pattern; star பொதுவான Ethernet LAN.

**3 — Explain network behaviour:** Star-இல் endpoints switch-க்கு இணைகின்றன; mesh alternate paths; ring protocol loop control தேவை.

**4 — Advanced complication:** Physical topology மற்றும் logical routing path வேறுபடலாம்; virtual overlay packet path மாற்றும்.

**5 — Important limitation:** Single switch fault முழு star segment-ஐ பாதிக்கும்; topology choice resilience-ஐ தீர்மானிக்கும்.

**6 — Practical task:** Single-switch மற்றும் dual-switch diagrams வரைந்து failure domain ஒப்பிடவும்.

**7 — Debrief:** Compare what you predicted to the evidence. Include one legitimate alternative explanation and one recommended next non-invasive test.

## Marking rubric (100 points)

| Area | Marks | Target |
|---|---:|---|
| Concept explanation | 20 | Correct and understandable |
| Architecture/diagram | 20 | Endpoints, intermediate stages and protocols |
| Practical method | 20 | Safe, reproducible, authorized |
| Evidence and troubleshooting | 20 | Expected/actual and alternative hypothesis |
| Advanced insight | 10 | Correct trade-off or uncommon case |
| Ethics and limitations | 10 | No unsupported attribution, privacy and change control |

**பாதுகாப்பு:** Practical-கள் உங்களுக்குச் சொந்தமான device, தனிமைப்படுத்தப்பட்ட lab, அல்லது எழுத்துப்பூர்வமாக அனுமதி பெற்ற network-இல் மட்டுமே. Public IP பதிவு அல்லது scan உங்கள் அனுமதியைத் தானாக நிரூபிக்காது. Malware sample-ஐ everyday PC-ல் இயக்காதீர்கள்.
