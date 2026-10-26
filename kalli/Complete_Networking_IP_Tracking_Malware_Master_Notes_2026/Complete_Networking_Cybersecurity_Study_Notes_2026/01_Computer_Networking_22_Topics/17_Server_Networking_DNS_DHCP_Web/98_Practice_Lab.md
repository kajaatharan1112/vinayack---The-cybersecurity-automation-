# 17 — Practical Lab and Troubleshooting Workbook

## Objective

Operate core infrastructure services safely.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | DNS Server Roles and Zones | Design a sample zone file for lab.example.test with web and mail (fictional). | Diagram + observation + uncertainty |
| 2 | DHCP Server Scopes and Relay | Write scope table with reserved range, lease time, router and DNS. | Diagram + observation + uncertainty |
| 3 | Linux Web Server Reverse Proxy | Using own machine, python3 -m http.server 8000 then curl localhost; stop after. | Diagram + observation + uncertainty |
| 4 | SSH SFTP Remote Management | Write sshd hardening checklist: keys, updates, MFA gateway, audit. | Diagram + observation + uncertainty |
| 5 | Time Synchronization NTP Logging | Make 5-event log timeline in UTC with consistent timezone annotations. | Diagram + observation + uncertainty |
| 6 | Backups Storage and Availability | Choose RPO/RTO for university exam system and restoration exercise. | Diagram + observation + uncertainty |

## Detailed sample walkthrough: DNS Server Roles and Zones

**1 — Scenario:** School domain records point portal to load balancer and email to provider.

**2 — Predict:** Authoritative servers host records; recursive servers answer clients via cache/lookup.

**3 — Explain network behaviour:** Zone SOA, NS, A, AAAA, CNAME, MX, TXT; TTL controls caching.

**4 — Advanced complication:** DNSSEC validates data authenticity; DNS views/split-horizon for internal use.

**5 — Important limitation:** Wrong authoritative delegation causes persistent failure despite local changes.

**6 — Practical task:** Design a sample zone file for lab.example.test with web and mail (fictional).

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
