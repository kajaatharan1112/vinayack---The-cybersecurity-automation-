# 06 — Practical Lab and Troubleshooting Workbook

## Objective

Addressing fundamentals with modern IPv6 practice.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | IPv4 Structure and Special Ranges | ipconfig /all பார்க்கவும்; range public/private/loopback வகை எழுதவும். | Diagram + observation + uncertainty |
| 2 | IPv6 Address Types | ip -6 addr அல்லது ipconfig பார்த்து IPv6 prefixes identify செய்யவும். | Diagram + observation + uncertainty |
| 3 | Public Private Static Dynamic | WAN IP மற்றும் host IP வேறுபாட்டை private vs public terms-ல் எழுதவும். | Diagram + observation + uncertainty |
| 4 | ARP NDP Neighbor Discovery | arp -a அல்லது ip neigh மூலம் local neighbor records பட்டியலிடவும். | Diagram + observation + uncertainty |
| 5 | IPv6 Transition and Dual Stack | nslookup -type=AAAA example.com and -type=A compare செய்யவும். | Diagram + observation + uncertainty |
| 6 | Address Planning IPAM and DHCP | Three subnet address inventory and documentation plan எழுதவும். | Diagram + observation + uncertainty |

## Detailed sample walkthrough: IPv4 Structure and Special Ranges

**1 — Scenario:** 192.168.10.20/24 belongs to 192.168.10.0/24.

**2 — Predict:** IPv4 32 bits dotted decimal; private RFC1918 ranges; loopback 127/8; documentation 192.0.2/24.

**3 — Explain network behaviour:** Network prefix determines routing; host part endpoint within subnet.

**4 — Advanced complication:** CGNAT 100.64.0.0/10 shared address space used provider side; public != fixed.

**5 — Important limitation:** 192.168 address-ஐ public Internet route ஆக பயன்படுத்த முடியாது.

**6 — Practical task:** ipconfig /all பார்க்கவும்; range public/private/loopback வகை எழுதவும்.

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
