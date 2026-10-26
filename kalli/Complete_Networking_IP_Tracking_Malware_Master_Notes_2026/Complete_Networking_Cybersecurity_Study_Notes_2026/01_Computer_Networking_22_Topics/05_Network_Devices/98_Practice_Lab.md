# 05 — Practical Lab and Troubleshooting Workbook

## Objective

Understand how packets physically and logically travel.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | Hub Bridge Switch | Draw 4-PC switch MAC learning table after two exchanges. | Diagram + observation + uncertainty |
| 2 | Router and Default Gateway | ip route or route print trace default gateway path. | Diagram + observation + uncertainty |
| 3 | Firewall IDS IPS | Write inbound/outbound least-privilege rules for app + DB. | Diagram + observation + uncertainty |
| 4 | Modem ONT Access Point | List actual home devices and who owns DHCP/NAT/AP roles. | Diagram + observation + uncertainty |
| 5 | Proxy Load Balancer Gateway | Draw client → reverse proxy → API → DB including which node terminates TLS. | Diagram + observation + uncertainty |
| 6 | Physical Cabling Transceivers | Describe speed, cable category, link distance and spare paths for example office. | Diagram + observation + uncertainty |

## Detailed sample walkthrough: Hub Bridge Switch

**1 — Scenario:** Lab switch connects PCs; same subnet traffic avoids router.

**2 — Predict:** Hub repeats bits, bridge learns MAC, switch forwards frames in LAN; hubs obsolete.

**3 — Explain network behaviour:** Switch learns source MAC on arrival; floods unknown unicast until learned.

**4 — Advanced complication:** CAM table pressure, port security, storm control modern defensive mechanisms.

**5 — Important limitation:** Broadcast storm = loop/MAC churn; STP/LACP config inspect.

**6 — Practical task:** Draw 4-PC switch MAC learning table after two exchanges.

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
