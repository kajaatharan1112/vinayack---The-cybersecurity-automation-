# 09 — Practical Lab and Troubleshooting Workbook

## Objective

Well-known ports, listening sockets, encrypted protocols and checks.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | Port Basics and IANA Ranges | Use ss -tuln or netstat -ano and identify self-owned listening ports. | Diagram + observation + uncertainty |
| 2 | Common Service Ports | Map 12 common ports to protocol, TCP/UDP, encryption and purpose. | Diagram + observation + uncertainty |
| 3 | Ephemeral Ports and Five Tuple | netstat -ano find local ephemeral ports and remote service ports. | Diagram + observation + uncertainty |
| 4 | Service Discovery and Banners | On own localhost only: curl -I http://127.0.0.1:8000 if a test server running. | Diagram + observation + uncertainty |
| 5 | Firewall Reachability and Health | Draft layered troubleshooting table for timeout/refused/TLS alert/HTTP 500. | Diagram + observation + uncertainty |

## Detailed sample walkthrough: Port Basics and IANA Ranges

**1 — Scenario:** HTTPS commonly 443, DNS 53, SSH 22.

**2 — Predict:** Ports identify transport endpoints; 0-1023 well-known, 1024-49151 registered, 49152-65535 dynamic IANA ranges.

**3 — Explain network behaviour:** TCP/UDP have separate port spaces; socket and IP tuple identify connection.

**4 — Advanced complication:** Applications can use alternate ports; port number does not prove protocol identity.

**5 — Important limitation:** Port open ≠ vulnerability; exposure, patch level and auth determine risk.

**6 — Practical task:** Use ss -tuln or netstat -ano and identify self-owned listening ports.

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
