# 10 — Practical Lab and Troubleshooting Workbook

## Objective

Local network frames, loops, virtualization and defence.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | Ethernet Switching MAC Tables | Sketch learning sequence for three hosts on four-port switch. | Diagram + observation + uncertainty |
| 2 | Access Trunk VLAN 8021Q | Design port table: access VLAN and tagged uplinks. | Diagram + observation + uncertainty |
| 3 | STP RSTP Loop Prevention | Draw triangle switch topology and indicate one blocked path. | Diagram + observation + uncertainty |
| 4 | Link Aggregation LACP | Explain why 2x1Gbps does not guarantee a single 2Gbps TCP download. | Diagram + observation + uncertainty |
| 5 | 8021X NAC and Device Trust | Draw supplicant → authenticator → authentication server trust path. | Diagram + observation + uncertainty |
| 6 | VXLAN EVPN Modern L2 Over L3 | Diagram inner Ethernet + VXLAN + UDP + outer IP packet. | Diagram + observation + uncertainty |

## Detailed sample walkthrough: Ethernet Switching MAC Tables

**1 — Scenario:** PC-A sends frame to PC-B, initially flooded then unicast.

**2 — Predict:** Switch learns source MAC to port, forwards known destination, floods unknown/broadcast.

**3 — Explain network behaviour:** MAC table entries age out; one broadcast domain spans VLAN member ports.

**4 — Advanced complication:** Storm control, MAC move detection, port-security mitigate layer-2 abuse.

**5 — Important limitation:** MAC spoofing or loops cause MAC flapping; observe logs.

**6 — Practical task:** Sketch learning sequence for three hosts on four-port switch.

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
