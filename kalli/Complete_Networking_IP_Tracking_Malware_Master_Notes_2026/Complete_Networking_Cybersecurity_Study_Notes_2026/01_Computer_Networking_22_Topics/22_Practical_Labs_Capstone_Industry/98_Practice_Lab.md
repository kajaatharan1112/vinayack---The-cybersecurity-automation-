# 22 — Practical Lab and Troubleshooting Workbook

## Objective

Projects turn concepts into demonstrable networking competence.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | Build a Virtual Network Lab | Create topology 2 subnets, 1 router, 2 endpoints and connectivity checklist. | Diagram + observation + uncertainty |
| 2 | Subnet Routing VLAN Project | Submit IP plan, ASCII topology, access matrix and test outcomes. | Diagram + observation + uncertainty |
| 3 | Analyze PCAP and Troubleshoot | Make incident note observation, evidence, alternative hypotheses, corrective step. | Diagram + observation + uncertainty |
| 4 | Deploy Secure Three Tier Demo | Draw request path and produce firewall rules design, no secrets. | Diagram + observation + uncertainty |
| 5 | Cloud Native Capstone | Document manifests needed, failure testing, SLI, access matrix. | Diagram + observation + uncertainty |
| 6 | Network Engineer Real Time Workflow | Create 30-minute mock incident ticket with timestamps, decision log, proof of restore. | Diagram + observation + uncertainty |
| 7 | Career Roadmap and Assessment | Write self-assessment: explain, draw, configure safely, troubleshoot, document for 22 topics. | Diagram + observation + uncertainty |

## Detailed sample walkthrough: Build a Virtual Network Lab

**1 — Scenario:** Subnet A 192.168.10.0/24 to subnet B 192.168.20.0/24 via lab router.

**2 — Predict:** Isolated virtual networks support safe experimentation without touching neighbors.

**3 — Explain network behaviour:** Create two client VMs and one router VM, internal networks, static/DHCP and firewall.

**4 — Advanced complication:** Network namespaces, Linux bridges, virtual switches, container networks allow low-cost labs.

**5 — Important limitation:** Bridged adapter may accidentally expose tests to office network; prefer host-only/internal.

**6 — Practical task:** Create topology 2 subnets, 1 router, 2 endpoints and connectivity checklist.

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
