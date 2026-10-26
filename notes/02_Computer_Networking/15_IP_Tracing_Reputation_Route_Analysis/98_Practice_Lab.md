# 15 — Practical Lab and Troubleshooting Workbook

## Objective

Safe and realistic IP intelligence foundations; extended dedicated section included.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | Traceroute and Hops | Run tracert example.com or traceroute example.com non-invasive and document caveats. | Diagram + observation + uncertainty |
| 2 | WHOIS RDAP Registry and ASN | Look up 1.1.1.1 using authorized public RDAP and note organization only. | Diagram + observation + uncertainty |
| 3 | IP Geolocation Limits | Prepare confidence rating low/medium/high for sample location claims. | Diagram + observation + uncertainty |
| 4 | IP Reputation Threat Intelligence | Design a report with evidence source, time, confidence and remediation. | Diagram + observation + uncertainty |
| 5 | Remote Activities and Log Ownership | Draft allowed data fields for your own website visitor analytics with privacy retention. | Diagram + observation + uncertainty |
| 6 | Ethical Remote Investigation Workflow | Make 1-page investigation record with evidence/time/authorization/uncertainty. | Diagram + observation + uncertainty |

## Detailed sample walkthrough: Traceroute and Hops

**1 — Scenario:** tracert example.com shows some network hops if permitted.

**2 — Predict:** Traceroute estimates Layer 3 path with TTL-expired responses; it does not track a person's movement.

**3 — Explain network behaviour:** Probes increasing TTL; intermediate router may reply ICMP Time Exceeded.

**4 — Advanced complication:** ECMP causes path changes; Paris traceroute and MTR are more nuanced.

**5 — Important limitation:** Missing hop (* * *) often ICMP filtering, not proof of failure.

**6 — Practical task:** Run tracert example.com or traceroute example.com non-invasive and document caveats.

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
