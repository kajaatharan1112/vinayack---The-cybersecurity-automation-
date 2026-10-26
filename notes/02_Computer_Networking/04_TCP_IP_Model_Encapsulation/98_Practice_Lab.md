# 04 — Practical Lab and Troubleshooting Workbook

## Objective

Real protocol stack and packet trip through home/Internet/cloud.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | Four Layer TCP IP Model | 4-layer table மற்றும் 7-layer mapping உருவாக்கவும். | Diagram + observation + uncertainty |
| 2 | Ethernet IPv4 TCP Frame Anatomy | Wireshark trace-ல் IP vs MAC lifetime compare செய்யவும். | Diagram + observation + uncertainty |
| 3 | TCP Connection Lifecycle | Local server இருந்தால் curl -v http://127.0.0.1:8000 மற்றும் capture observe செய்யவும். | Diagram + observation + uncertainty |
| 4 | UDP and QUIC | Browser DevTools protocol column-ல் h3 vs h2 observe செய்யவும் (availability varies). | Diagram + observation + uncertainty |
| 5 | MTU MSS Fragmentation PMTUD | ping payload sizes on own gateway with platform-specific flags; stop before disruption. | Diagram + observation + uncertainty |
| 6 | Connection States and Sockets | ss -tunap (Linux) or Get-NetTCPConnection (Windows) and record local vs remote. | Diagram + observation + uncertainty |

## Detailed sample walkthrough: Four Layer TCP IP Model

**1 — Scenario:** DNS query UDP, server response ஆகியவை stack-இல் பயணம் செய்கின்றன.

**2 — Predict:** Link, Internet, Transport, Application நான்கு logical layers; சில textbooks 5-layer model.

**3 — Explain network behaviour:** Application data -> TCP segment -> IP packet -> Ethernet frame; receiver decapsulates.

**4 — Advanced complication:** Modern QUIC UDP மீது reliable secure streams தருவதால் mapping strict அல்ல.

**5 — Important limitation:** OSI மற்றும் TCP/IP one-to-one exact mapping எதிர்பார்க்காதீர்கள்.

**6 — Practical task:** 4-layer table மற்றும் 7-layer mapping உருவாக்கவும்.

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
