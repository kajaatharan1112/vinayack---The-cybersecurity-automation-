# 21 — Practical Lab and Troubleshooting Workbook

## Objective

Less-common yet increasingly useful production-grade concepts.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | QUIC HTTP3 TLS13 ECH | Compare h2 over TCP/TLS with h3 over QUIC in browser DevTools where supported. | Diagram + observation + uncertainty |
| 2 | BGP RPKI ROV and Route Security | Create conceptual ROA prefix, maxLength, origin-ASN and validation examples. | Diagram + observation + uncertainty |
| 3 | Segment Routing MPLS SRv6 | Draw preferred route vs backup route using segments. | Diagram + observation + uncertainty |
| 4 | eBPF XDP Linux Networking | Read-only lab: list concept hooks, explain what policy check would do. | Diagram + observation + uncertainty |
| 5 | SASE SSE ZTNA Identity | Build comparison table MPLS WAN/VPN/SD-WAN/SASE for branch + remote employees. | Diagram + observation + uncertainty |
| 6 | Post Quantum Crypto Network Migration | Draft asset inventory fields protocol, cert lifetime, crypto algorithm, upgrade owner. | Diagram + observation + uncertainty |

## Detailed sample walkthrough: QUIC HTTP3 TLS13 ECH

**1 — Scenario:** Mobile user swaps Wi-Fi to LTE; QUIC connection migration may preserve session.

**2 — Predict:** HTTP/3 maps HTTP semantics over QUIC; TLS1.3 secures; ECH aims encrypt sensitive ClientHello parts.

**3 — Explain network behaviour:** QUIC UDP transport manages streams and recovery; ALPN and HTTPS RR may advertise protocol.

**4 — Advanced complication:** 0-RTT replay constraints, anti-amplification, connection IDs, ALPN and SVCB HTTPS records.

**5 — Important limitation:** QUIC traffic isn't inspectable like plaintext HTTP; troubleshooting needs endpoints/metadata.

**6 — Practical task:** Compare h2 over TCP/TLS with h3 over QUIC in browser DevTools where supported.

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
