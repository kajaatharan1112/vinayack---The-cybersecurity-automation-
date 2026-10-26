# 11 — Practical Lab and Troubleshooting Workbook

## Objective

Forwarding decisions, dynamic routes and Internet operations.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | Routing Table Longest Prefix Match | Write lookup results for dest 10.1.2.9 with /8, /16, /24 choices. | Diagram + observation + uncertainty |
| 2 | Static Routes and Default Route | Read ip route or route print; explain default and directly connected routes. | Diagram + observation + uncertainty |
| 3 | OSPF Link State Protocol | List 4 OSPF adjacency prerequisites and simulated fault cause. | Diagram + observation + uncertainty |
| 4 | BGP Between Autonomous Systems | Read a public route-collector screenshot or docs; identify prefix, ASN, AS path. | Diagram + observation + uncertainty |
| 5 | Routing Protocol Comparisons | Make matrix: static/OSPF/BGP use-case, scale, convergence, security. | Diagram + observation + uncertainty |
| 6 | Multihoming and Routing Security | Create disaster checklist for losing one ISP and validating return path. | Diagram + observation + uncertainty |

## Detailed sample walkthrough: Routing Table Longest Prefix Match

**1 — Scenario:** 10.0.1.55 matches 10.0.1.0/24 over default /0.

**2 — Predict:** Router picks most specific matched network then resolves next hop/interface.

**3 — Explain network behaviour:** Connected, static, learned routes compete by preference/metric.

**4 — Advanced complication:** Policy based routing can override traditional destination lookup.

**5 — Important limitation:** A route exists but return path missing causes asymmetric failure.

**6 — Practical task:** Write lookup results for dest 10.1.2.9 with /8, /16, /24 choices.

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
