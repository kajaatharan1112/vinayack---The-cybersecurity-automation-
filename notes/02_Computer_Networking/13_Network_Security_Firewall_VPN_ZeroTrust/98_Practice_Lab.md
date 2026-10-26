# 13 — Practical Lab and Troubleshooting Workbook

## Objective

Identity-centric protection and secure access.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | Threat Model CIA and Defence in Depth | Write simple data-flow diagram for campus LMS and identify 3 risks. | Diagram + observation + uncertainty |
| 2 | Firewalls ACL Stateful NGFW | Build five-rule matrix for DMZ, staff, guest, DB, management. | Diagram + observation + uncertainty |
| 3 | VPN IPsec WireGuard ZTNA | Diagram remote laptop → tunnel endpoint → permitted internal service. | Diagram + observation + uncertainty |
| 4 | Zero Trust Architecture | Write policy: HR staff managed device, MFA, only payroll service, log access. | Diagram + observation + uncertainty |
| 5 | TLS PKI Certificates mTLS | Open browser certificate details of trusted sample site, identify issuer and validity. | Diagram + observation + uncertainty |
| 6 | IDS IPS SIEM SOC | Write detection rule pseudocode for abnormal failed logins with threshold + exceptions. | Diagram + observation + uncertainty |

## Detailed sample walkthrough: Threat Model CIA and Defence in Depth

**1 — Scenario:** Payroll DB needs encrypt, role checks, backup, incident logging.

**2 — Predict:** Confidentiality, Integrity, Availability guide choices; threat model assets and attack paths.

**3 — Explain network behaviour:** Inventory critical data; identify threats; choose preventive/detective/recovery controls.

**4 — Advanced complication:** Attack surface management and threat-informed defence connect technique to control.

**5 — Important limitation:** Single firewall does not solve stolen credentials or insecure apps.

**6 — Practical task:** Write simple data-flow diagram for campus LMS and identify 3 risks.

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
