# 16 — Practical Lab and Troubleshooting Workbook

## Objective

Repeatable root-cause approaches used by professional network engineers.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | Top Down Bottom Up Divide Conquer | Write diagnostic flow: DNS failure vs packet loss vs cert expiry. | Diagram + observation + uncertainty |
| 2 | Windows Linux Mac Diagnostics | Compare Windows and Linux equivalents for IP, route, DNS and sockets. | Diagram + observation + uncertainty |
| 3 | DNS Troubleshooting | nslookup example.com then compare response server and query types. | Diagram + observation + uncertainty |
| 4 | Packet Loss Jitter Latency Diagnosis | Make table symptom / likely layer / verify metric / safest next step. | Diagram + observation + uncertainty |
| 5 | TLS VPN App Failure Analysis | curl -Iv https://example.com and annotate DNS/connect/TLS/status phases. | Diagram + observation + uncertainty |
| 6 | Incident Change Management Runbooks | Write maintenance plan with change window, tests, abort criteria, rollback. | Diagram + observation + uncertainty |

## Detailed sample walkthrough: Top Down Bottom Up Divide Conquer

**1 — Scenario:** Website fails: determine only one site vs all, then DNS, gateway, TLS.

**2 — Predict:** Troubleshoot OSI layers: bottom-up physical first, top-down application first or middle-out at network layer.

**3 — Explain network behaviour:** Form hypothesis; run lowest-risk test; compare expected/actual; isolate; document fix.

**4 — Advanced complication:** Differential diagnosis and binary-search fault isolation reduce wasted work.

**5 — Important limitation:** Changing 5 settings at once prevents knowing cause and risks making outage worse.

**6 — Practical task:** Write diagnostic flow: DNS failure vs packet loss vs cert expiry.

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
