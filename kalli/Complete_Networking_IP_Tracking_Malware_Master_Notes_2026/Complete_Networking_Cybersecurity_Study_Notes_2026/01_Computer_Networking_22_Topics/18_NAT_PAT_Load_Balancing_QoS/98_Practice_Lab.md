# 18 — Practical Lab and Troubleshooting Workbook

## Objective

Address translation, scale and traffic guarantees.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | NAT PAT and Connection Tracking | Draw before/after PAT tuple with source port and time. | Diagram + observation + uncertainty |
| 2 | Port Forwarding and DMZ | Design secure public web + private DB network diagram. | Diagram + observation + uncertainty |
| 3 | L4 and L7 Load Balancing | Sketch request route and list health-check criteria. | Diagram + observation + uncertainty |
| 4 | CDN Anycast and Caching | Draw DNS/CDN edge/origin path and cache miss process. | Diagram + observation + uncertainty |
| 5 | QoS DSCP Traffic Shaping | Create queue classes for voice/video/backup/regular web. | Diagram + observation + uncertainty |
| 6 | Capacity Planning and Scale | Compute time to send 100MB on 100Mbps theoretical link; discuss overhead. | Diagram + observation + uncertainty |

## Detailed sample walkthrough: NAT PAT and Connection Tracking

**1 — Scenario:** Home 20 devices share one WAN address when browsing.

**2 — Predict:** NAT rewrites addresses, PAT also ports to share external IP; table tracks flows.

**3 — Explain network behaviour:** LAN client source 192.168.x:50000 becomes public:40001; return maps back.

**4 — Advanced complication:** NAT444/CGNAT, endpoint-independent mappings, hairpin NAT, NAT64.

**5 — Important limitation:** Public IP can't uniquely identify home device/time absent NAT logs.

**6 — Practical task:** Draw before/after PAT tuple with source port and time.

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
