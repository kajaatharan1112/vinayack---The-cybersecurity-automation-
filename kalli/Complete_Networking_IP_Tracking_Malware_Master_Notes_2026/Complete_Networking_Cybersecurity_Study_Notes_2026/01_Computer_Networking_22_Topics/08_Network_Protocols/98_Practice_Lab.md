# 08 — Practical Lab and Troubleshooting Workbook

## Objective

How common networking protocols fit together.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | TCP vs UDP | Run ss -tu or netstat -an to compare TCP/UDP sockets. | Diagram + observation + uncertainty |
| 2 | DNS Lookup Journey | nslookup example.com and nslookup -type=MX example.com; compare record purposes. | Diagram + observation + uncertainty |
| 3 | DHCP DORA and DHCPv6 | Inspect lease obtained/expires and DNS servers with ipconfig /all. | Diagram + observation + uncertainty |
| 4 | ARP ICMP NTP | ping 127.0.0.1 and traceroute or tracert documentation example. | Diagram + observation + uncertainty |
| 5 | HTTP HTTPS TLS | curl -I https://example.com and record status/security headers if exposed. | Diagram + observation + uncertainty |
| 6 | Mail and Remote Administration | Create secure configuration checklist for SSH, mail and SNMP (no live login). | Diagram + observation + uncertainty |

## Detailed sample walkthrough: TCP vs UDP

**1 — Scenario:** File download needs reliable data; live voice prefers timely packets.

**2 — Predict:** TCP connection-oriented reliable byte stream; UDP connectionless datagrams no delivery guarantee.

**3 — Explain network behaviour:** TCP seq/ack, flow and congestion control; UDP application decides reliability.

**4 — Advanced complication:** QUIC builds reliability and encryption atop UDP; RTP media can use FEC/jitter buffers.

**5 — Important limitation:** TCP reliable ≠ instant; retransmissions increase latency.

**6 — Practical task:** Run ss -tu or netstat -an to compare TCP/UDP sockets.

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
