# 19 — Practical Lab and Troubleshooting Workbook

## Objective

VPC primitives, private access and distributed networks.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | Cloud VPC VNet Subnets | Design three-tier cloud app IP plan and exposure matrix. | Diagram + observation + uncertainty |
| 2 | Cloud Security Groups NACL | Write SG policy for web→API→DB and outbound DNS. | Diagram + observation + uncertainty |
| 3 | Hybrid VPN Private Connections | Diagram campus edge → VPN → cloud network → private service. | Diagram + observation + uncertainty |
| 4 | Cloud NAT Endpoints and Egress | Trace outbound flow private server to patch repository. | Diagram + observation + uncertainty |
| 5 | Kubernetes Networking Services CNI | Draw pod → service → endpoint pod and DNS discovery. | Diagram + observation + uncertainty |
| 6 | Gateway API Service Mesh eBPF | Describe north-south vs east-west and write conceptual HTTPRoute mapping. | Diagram + observation + uncertainty |

## Detailed sample walkthrough: Cloud VPC VNet Subnets

**1 — Scenario:** Frontend public subnet; API private subnet; DB private subnet.

**2 — Predict:** VPC/VNet isolated virtual IP network; subnets and route tables segment cloud resources.

**3 — Explain network behaviour:** Cloud fabric maps virtual NICs and routes to gateways and endpoints.

**4 — Advanced complication:** Account boundaries, shared VPC, transit routing, overlapping CIDRs.

**5 — Important limitation:** Public subnet name alone doesn't give public IP or firewall access.

**6 — Practical task:** Design three-tier cloud app IP plan and exposure matrix.

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
