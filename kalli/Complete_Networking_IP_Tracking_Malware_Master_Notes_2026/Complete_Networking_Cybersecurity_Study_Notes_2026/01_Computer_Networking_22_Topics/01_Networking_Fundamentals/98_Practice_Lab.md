# 01 — Practical Lab and Troubleshooting Workbook

## Objective

இரண்டு devices எப்படி data exchange செய்கின்றன என்பதிலிருந்து தொடங்கும் அடித்தளம்.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | What Is a Computer Network | உங்கள் device-ல் ipconfig /all அல்லது ip a பார்க்கவும்; ஒவ்வொரு field-ன் role எழுதவும். | Diagram + observation + uncertainty |
| 2 | LAN WAN MAN PAN Internet Intranet | உங்கள் வீடு/கல்லூரி network-க்கு LAN-WAN boundary diagram வரைந்து NAT எங்கு நடக்கிறது குறிக்கவும். | Diagram + observation + uncertainty |
| 3 | Bandwidth Throughput Latency Jitter Loss | பாதுகாப்பான local ping 127.0.0.1 செய்து round-trip min/avg/max வேறுபாட்டைப் பதிவு செய்யவும். | Diagram + observation + uncertainty |
| 4 | Client Server Peer to Peer | Browser DevTools Network tab-ல் request/response status, duration, remote address உள்ளதா பாருங்கள். | Diagram + observation + uncertainty |
| 5 | Packet Switching and Encapsulation | Wireshark sample capture-ல் Ethernet/IP/TCP/HTTP layers expand செய்து fields எழுதவும். | Diagram + observation + uncertainty |
| 6 | Network Roles and Documentation | உங்கள் சொந்த network-க்கு 6-device topology, IP plan, device owner, services table உருவாக்கவும். | Diagram + observation + uncertainty |

## Detailed sample walkthrough: What Is a Computer Network

**1 — Scenario:** University LMS site திறக்கும் laptop, campus Wi-Fi, ISP, web server ஆகியவற்றுக்கிடையில் பல networks கடக்கிறது.

**2 — Predict:** Network என்பது தகவலை பரிமாற rules உடன் இணைக்கப்பட்ட devices கூட்டம்; Internet என்பது interconnected networks, ஒரு தனி computer அல்ல.

**3 — Explain network behaviour:** Sender data உருவாக்குகிறது; NIC bits அனுப்புகிறது; intermediate devices forward செய்கின்றன; receiver application பொருளை மீட்டெடுக்கிறது.

**4 — Advanced complication:** End-to-end principle: network transport செய்வது, reliability/encryption பெரும்பாலும் endpoints இல்; middleboxes இதை சிக்கலாக்கலாம்.

**5 — Important limitation:** Wi-Fi connected என்றால் Internet works என்பதில்லை: default gateway, DNS, external reachability தனித்தனியாகச் சோதிக்கவும்.

**6 — Practical task:** உங்கள் device-ல் ipconfig /all அல்லது ip a பார்க்கவும்; ஒவ்வொரு field-ன் role எழுதவும்.

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
