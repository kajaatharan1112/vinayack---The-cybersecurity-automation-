# 14 — Practical Lab and Troubleshooting Workbook

## Objective

Packet-level observability and evidence-based diagnosis.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | Packet Capture Fundamentals | Open safe sample PCAP and label packet src/dst/protocol. | Diagram + observation + uncertainty |
| 2 | Capture vs Display Filters | Practice display: dns; tcp.analysis.retransmission; ip.addr == 192.0.2.10. | Diagram + observation + uncertainty |
| 3 | TCP Analysis RTT Retransmission | Compare two example time plots: normal RTT vs spiking RTT. | Diagram + observation + uncertainty |
| 4 | DNS HTTP TLS Metadata | Record what is visible and not visible for HTTPS versus HTTP captures. | Diagram + observation + uncertainty |
| 5 | Flows NetFlow IPFIX sFlow | Create sample 5-tuple flow row and describe investigative questions. | Diagram + observation + uncertainty |
| 6 | Network Performance Indicators | Write dashboard spec with latency, loss, interface errors, DNS time, TLS time. | Diagram + observation + uncertainty |

## Detailed sample walkthrough: Packet Capture Fundamentals

**1 — Scenario:** Record own lab test HTTP request and inspect SYN/ACK fields.

**2 — Predict:** PCAP records packets at a vantage point; capture != full network visibility.

**3 — Explain network behaviour:** NIC mirror/SPAN/tap or host capture collects frames; dissectors parse layers.

**4 — Advanced complication:** Offloads, sampling, packet loss, clock drift, capture position change meaning.

**5 — Important limitation:** Promiscuous mode on switched Ethernet does not reveal all traffic everywhere.

**6 — Practical task:** Open safe sample PCAP and label packet src/dst/protocol.

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
