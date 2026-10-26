# 20 — Practical Lab and Troubleshooting Workbook

## Objective

Practical operations: repeatability, safety and observability.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | Automation Basics CLI API Python | Write pseudocode for read-only IP inventory from your own lab. | Diagram + observation + uncertainty |
| 2 | Infrastructure as Code | Create conceptual version-controlled config and approval checklist. | Diagram + observation + uncertainty |
| 3 | Network Observability SNMP Streaming | Define dashboard widgets: interface drops, utilization, route flaps, DNS RTT. | Diagram + observation + uncertainty |
| 4 | Logging Metrics Traces Correlation | Draw trace spans browser, gateway, API, DB and annotate delays. | Diagram + observation + uncertainty |
| 5 | SRE SLO Alerting and Incident Review | Define two SLIs for University LMS and appropriate alert thresholds. | Diagram + observation + uncertainty |
| 6 | NetDevOps CI Policy Validation | Write three network invariants and test cases for a proposed route change. | Diagram + observation + uncertainty |

## Detailed sample walkthrough: Automation Basics CLI API Python

**1 — Scenario:** Script collects versions/status from 30 switches for patch planning.

**2 — Predict:** Automate inventory checks and configuration with repeatable scripts, not ad hoc changes.

**3 — Explain network behaviour:** Read desired state; compare to live; propose diff; apply approved change; verify.

**4 — Advanced complication:** Idempotency, GitOps, Jinja templates, dry-run, audit trails.

**5 — Important limitation:** Blindly loop config commands over all switches can cause widespread outage.

**6 — Practical task:** Write pseudocode for read-only IP inventory from your own lab.

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
