# 03 — Practical Lab and Troubleshooting Workbook

## Objective

7-layer mental model, encapsulation, failure isolation, modern encryption.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | Layer 1 Physical | ஒரு broken-cable scenario-க்கு L1 symptoms எழுதவும். | Diagram + observation + uncertainty |
| 2 | Layer 2 Data Link | Frame fields destination/source MAC, EtherType வரைபடம் செய்யவும். | Diagram + observation + uncertainty |
| 3 | Layer 3 Network | ip route அல்லது route print output-ல் default route கண்டறியவும். | Diagram + observation + uncertainty |
| 4 | Layer 4 Transport | TCP flags SYN/SYN-ACK/ACK drawing செய்து QUIC handshake வேறுபாடு எழுதவும். | Diagram + observation + uncertainty |
| 5 | Layers 5 and 6 Session Presentation | HTTP body UTF-8 vs invalid encoding உதாரணம் விளக்கவும். | Diagram + observation + uncertainty |
| 6 | Layer 7 Application | HTTP method, URL, headers, body, status code parts label செய்யவும். | Diagram + observation + uncertainty |
| 7 | Cross Layer Troubleshooting | Failure tree உருவாக்கவும்: cable, local IP, gateway, DNS, TLS, application. | Diagram + observation + uncertainty |

## Detailed sample walkthrough: Layer 1 Physical

**1 — Scenario:** Bad cable அல்லது weak Wi-Fi RSSI காரணமாக errors.

**2 — Predict:** Layer 1 bits மற்றும் signal (copper, fibre, radio), voltage/light spectrum கவனிக்கிறது.

**3 — Explain network behaviour:** Transceiver encodes bit stream; cable/optic carries signal; receiver interprets.

**4 — Advanced complication:** Optical power budgets, FEC, PAM4, auto-negotiation ஆகியவை uncommon ஆனால் production முக்கியம்.

**5 — Important limitation:** Link down என்றால் முதலில் cable, port, optics, duplex/speed negotiation பாருங்கள்.

**6 — Practical task:** ஒரு broken-cable scenario-க்கு L1 symptoms எழுதவும்.

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
