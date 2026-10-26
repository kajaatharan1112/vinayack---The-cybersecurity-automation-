# 03 — Practical Lab and Troubleshooting Workbook

## Objective

ஒரு IP-ஐப் பற்றித் தெரிந்து கொள்ளக்கூடிய பொது தகவல் என்ன? Own network telemetry-யில் என்ன evidence கிடைக்கும்? Attribution எங்கே முடிகிறது?

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | IP Address and Identity Limits | Create diagram 3 private clients → campus NAT → same external IP and timestamps. | Diagram + observation + uncertainty |
| 2 | Passive vs Active Reconnaissance | Build passive-only checklist for a documentation address, no active contact. | Diagram + observation + uncertainty |
| 3 | RIR RDAP WHOIS IP Ownership | Record fields network handle, start/end, org and timestamp from a public example. | Diagram + observation + uncertainty |
| 4 | ASN BGP Origin and Prefixes | Draw prefix 198.51.100.0/24 announced by fictional AS64500 (private-use ASN). | Diagram + observation + uncertainty |
| 5 | Geolocation Country Region City Accuracy | Compare hypothetical conflicting city results, write uncertainty statement. | Diagram + observation + uncertainty |
| 6 | DNS A AAAA PTR Reverse DNS | nslookup -type=A example.com; nslookup -type=AAAA example.com; document what DNS doesn't tell. | Diagram + observation + uncertainty |
| 7 | Route Tracing Traceroute MTR | Run tracert example.com from own machine; annotate * not conclusively unreachable. | Diagram + observation + uncertainty |
| 8 | Latency Measurement and Network Distance | Create latency decomposition 2ms access + 20ms transit + 15ms queues etc. | Diagram + observation + uncertainty |
| 9 | Public Ports and Service Exposure | On own localhost, use ss -tuln and explain each listening socket. | Diagram + observation + uncertainty |
| 10 | IP Reputation Blocklists OSINT Confidence | Write minimal IOC record IP, observed_at, evidence, severity, expiry, confidence. | Diagram + observation + uncertainty |
| 11 | Threat Intelligence Enrichment Workflow | Plan reversible response: rate-limit, monitor, verify owner, expire if false positive. | Diagram + observation + uncertainty |
| 12 | Server Access Logs and IP Activity | Create synthetic log with 3 GET and 2 POST events; label reliable and unreliable fields. | Diagram + observation + uncertainty |
| 13 | Firewall NAT VPN Proxy Logs | Sketch joined records firewall time/source-port → NAT → owned endpoint → auth. | Diagram + observation + uncertainty |
| 14 | Flow Telemetry NetFlow IPFIX sFlow | Create 4 synthetic flow rows and rank volume; flag possible backup vs anomaly. | Diagram + observation + uncertainty |
| 15 | DNS Logs and Encrypted DNS Limits | List three alternative explanations for repeated DNS queries. | Diagram + observation + uncertainty |
| 16 | Endpoint EDR and Browser Evidence | Design 5 log fields for opt-in managed-device connection monitoring. | Diagram + observation + uncertainty |
| 17 | Detecting Scanning and Abuse on Owned Systems | Create detection pseudocode with threshold, allowlist and false-positive review. | Diagram + observation + uncertainty |
| 18 | Attribution Evidence Chain of Custody | Create sample evidence table field, collected_by, timestamp, hash, purpose. | Diagram + observation + uncertainty |
| 19 | Privacy Laws Ethics Authorization | Write data minimization policy: what captured, why, access, retention, deletion. | Diagram + observation + uncertainty |
| 20 | Case Study Suspicious IP on Own API | Write 1-page case report with verdict unknown/suspicious/benign and evidence. | Diagram + observation + uncertainty |
| 21 | Live Network Monitoring Dashboard Design | Sketch tiles for p95 RTT, DNS success, NAT exhaustion, auth failures and packet loss. | Diagram + observation + uncertainty |
| 22 | Limits of Remote Investigation Summary | Write five allowed conclusions and five unsupported conclusions from one IP. | Diagram + observation + uncertainty |

## Detailed sample walkthrough: IP Address and Identity Limits

**1 — Scenario:** Three students behind campus NAT visit the same site and appear as one public IP.

**2 — Predict:** IP is a routing locator, not a person ID. Public IP may be shared by household, university, VPN or cloud tenants.

**3 — Explain network behaviour:** Private hosts can be mapped to public address via NAT; different users can share same egress.

**4 — Advanced complication:** IPv6 temporary addresses, carrier NAT, anycast and mobile roaming break simple attribution.

**5 — Important limitation:** Never call a geolocation result a person's precise address; avoid stalking or unwarranted inference.

**6 — Practical task:** Create diagram 3 private clients → campus NAT → same external IP and timestamps.

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
