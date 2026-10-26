# Vinayack — Cybersecurity Notes & Automation

University cybersecurity study notes (Tamil explanations + English technical terms).
These notes are **Phase 1** of the project; **Phase 2** will build an automated cybersecurity project on top of them.

> All tool usage is for **your own lab or systems you are authorized to test**. See [`notes/05_Study_Resources/SAFE_LAB_SETUP.md`](notes/05_Study_Resources/SAFE_LAB_SETUP.md).

---

## Repository structure

```
.
├── README.md                         ← you are here
└── notes/
    ├── START_HERE.md                 ← how to study these notes
    ├── 00_Kali_Lab_Basics/           (2)   Kali setup + Linux/testing commands
    ├── 01_Kali_Tools/                (17)  one reference guide per Kali tool
    ├── 02_Computer_Networking/       (217) 22 chapters, basics → advanced
    ├── 03_Malware_Analysis_Defense/  (30)  malware types, detection, incident response
    ├── 04_IP_Investigation/          (26)  IP tracing, OSINT, log analysis, ethics
    └── 05_Study_Resources/           (10)  study plan, lab setup, worked examples
```

### Naming convention

- Folders and files start with a **two-digit number** (`01_`, `02_` …) to set the study order.
- No spaces or `&` in file names (`Topic_Name.md`), so the files are easy to process with scripts.
- Every chapter folder follows the same layout:
  - `README.md` — chapter overview
  - `00_…md` — integrated deep dive (where present)
  - `01_…md` – `NN_…md` — subtopic lessons
  - `98_Practice_Lab.md` — hands-on lab
  - `99_Quiz_Answers.md` — quiz + answer key

---

## Table of contents

### 00 · Kali Lab Basics
| # | Note |
|---:|---|
| 01 | [Introduction & Lab Setup](notes/00_Kali_Lab_Basics/01_Introduction_Lab_Setup.md) |
| 02 | [Testing Commands](notes/00_Kali_Lab_Basics/02_Testing_Commands.md) |

### 01 · Kali Tools
| # | Tool | Category |
|---:|---|---|
| 01 | [Metasploit Framework](notes/01_Kali_Tools/01_Metasploit_Framework.md) | Exploitation |
| 02 | [THC-Hydra](notes/01_Kali_Tools/02_THC-Hydra.md) | Password attacks (online) |
| 03 | [Nmap](notes/01_Kali_Tools/03_Nmap.md) | Scanning / discovery |
| 04 | [Wireshark & TShark](notes/01_Kali_Tools/04_Wireshark_TShark.md) | Packet analysis |
| 05 | [Aircrack-ng Suite](notes/01_Kali_Tools/05_Aircrack-ng_Suite.md) | Wireless |
| 06 | [Burp Suite](notes/01_Kali_Tools/06_Burp_Suite.md) | Web app testing |
| 07 | [John the Ripper](notes/01_Kali_Tools/07_John_the_Ripper.md) | Password cracking (offline) |
| 08 | [Hashcat](notes/01_Kali_Tools/08_Hashcat.md) | Password cracking (GPU) |
| 09 | [SQLMap](notes/01_Kali_Tools/09_SQLMap.md) | Web — SQL injection |
| 10 | [Nikto](notes/01_Kali_Tools/10_Nikto.md) | Web server scanning |
| 11 | [Gobuster & Dirb](notes/01_Kali_Tools/11_Gobuster_Dirb.md) | Web — directory brute force |
| 12 | [WPScan](notes/01_Kali_Tools/12_WPScan.md) | Web — WordPress |
| 13 | [theHarvester & Netcat](notes/01_Kali_Tools/13_theHarvester_Netcat.md) | OSINT / networking utility |
| 14 | [Enum4linux & SMBclient](notes/01_Kali_Tools/14_Enum4linux_SMBclient.md) | SMB enumeration |
| 15 | [Searchsploit & Recon-ng](notes/01_Kali_Tools/15_Searchsploit_Recon-ng.md) | Exploit search / recon |
| 16 | [Ettercap](notes/01_Kali_Tools/16_Ettercap.md) | MITM / sniffing |
| 17 | [Social Engineering Toolkit (SET)](notes/01_Kali_Tools/17_Social_Engineering_Toolkit_SET.md) | Social engineering |

### 02 · Computer Networking (22 chapters)
Full index with descriptions: [`NETWORKING_22_TOPIC_INDEX.md`](notes/05_Study_Resources/NETWORKING_22_TOPIC_INDEX.md)

| # | Chapter | # | Chapter |
|---:|---|---:|---|
| 01 | [Networking Fundamentals](notes/02_Computer_Networking/01_Networking_Fundamentals/README.md) | 12 | [Wireless Networking / Wi-Fi](notes/02_Computer_Networking/12_Wireless_Networking_WiFi/README.md) |
| 02 | [Network Architecture & Topologies](notes/02_Computer_Networking/02_Network_Architecture_Topologies/README.md) | 13 | [Network Security: Firewall, VPN, Zero Trust](notes/02_Computer_Networking/13_Network_Security_Firewall_VPN_ZeroTrust/README.md) |
| 03 | [OSI Seven Layers](notes/02_Computer_Networking/03_OSI_Seven_Layers/README.md) | 14 | [Network Traffic Analysis](notes/02_Computer_Networking/14_Network_Traffic_Analysis/README.md) |
| 04 | [TCP/IP Model & Encapsulation](notes/02_Computer_Networking/04_TCP_IP_Model_Encapsulation/README.md) | 15 | [IP Tracing, Reputation & Route Analysis](notes/02_Computer_Networking/15_IP_Tracing_Reputation_Route_Analysis/README.md) |
| 05 | [Network Devices](notes/02_Computer_Networking/05_Network_Devices/README.md) | 16 | [Troubleshooting Methodologies](notes/02_Computer_Networking/16_Troubleshooting_Methodologies/README.md) |
| 06 | [IP Addressing IPv4/IPv6](notes/02_Computer_Networking/06_IP_Addressing_IPv4_IPv6/README.md) | 17 | [Server Networking: DNS, DHCP, Web](notes/02_Computer_Networking/17_Server_Networking_DNS_DHCP_Web/README.md) |
| 07 | [Subnetting, CIDR, VLSM](notes/02_Computer_Networking/07_Subnetting_CIDR_VLSM/README.md) | 18 | [NAT/PAT, Load Balancing, QoS](notes/02_Computer_Networking/18_NAT_PAT_Load_Balancing_QoS/README.md) |
| 08 | [Network Protocols](notes/02_Computer_Networking/08_Network_Protocols/README.md) | 19 | [Cloud, Hybrid & Multicloud Networking](notes/02_Computer_Networking/19_Cloud_Networking_Hybrid_Multicloud/README.md) |
| 09 | [Ports, Services & Sockets](notes/02_Computer_Networking/09_Ports_Services_and_Sockets/README.md) | 20 | [Network Automation, Telemetry, SRE](notes/02_Computer_Networking/20_Network_Automation_Telemetry_SRE/README.md) |
| 10 | [Switching, VLANs, STP](notes/02_Computer_Networking/10_Switching_VLANs_STP/README.md) | 21 | [Modern Advanced Network Concepts](notes/02_Computer_Networking/21_Modern_Advanced_Network_Concepts/README.md) |
| 11 | [Routing: OSPF, BGP](notes/02_Computer_Networking/11_Routing_OSPF_BGP/README.md) | 22 | [Practical Labs, Capstone & Industry](notes/02_Computer_Networking/22_Practical_Labs_Capstone_Industry/README.md) |

### 03 · Malware Analysis & Defense
Start: [README](notes/03_Malware_Analysis_Defense/README.md) · [Virus vs Malware comparison](notes/03_Malware_Analysis_Defense/00_VIRUS_VS_MALWARE_FULL_COMPARISON.md) — 26 lessons + lab + quiz.

### 04 · IP Investigation
Start: [README](notes/04_IP_Investigation/README.md) · [What is possible with a remote IP](notes/04_IP_Investigation/00_REMOTE_IP_ACTIVITIES_WHAT_IS_POSSIBLE.md) — 22 lessons + lab + quiz.

### 05 · Study Resources
| Resource | |
|---|---|
| [16-Week Study Plan](notes/05_Study_Resources/16_WEEK_STUDY_PLAN.md) | Week-by-week roadmap |
| [Safe Lab Setup](notes/05_Study_Resources/SAFE_LAB_SETUP.md) | Isolated practice environment |
| [Subnetting Worked Examples](notes/05_Study_Resources/SUBNETTING_FULLY_WORKED_EXAMPLES.md) | Step-by-step calculations |
| [Packet Journey: DNS → TCP → TLS → QUIC](notes/05_Study_Resources/PACKET_JOURNEY_DNS_TCP_TLS_QUIC.md) | End-to-end walkthrough |
| [IP Investigation Case](notes/05_Study_Resources/IP_INVESTIGATION_FABRICATED_CASE.md) | Practice case (fabricated data) |
| [Malware Defensive Case Study](notes/05_Study_Resources/MALWARE_DEFENSIVE_CASE_STUDY.md) | Incident walkthrough |
| [Industry Trends & Sources (Oct 2026)](notes/05_Study_Resources/INDUSTRY_TRENDS_AND_SOURCE_MAP_OCT_2026.md) | Reference map |
| [Differences from Original Notes](notes/05_Study_Resources/IMPORTANT_DIFFERENCES_FROM_YOUR_UPLOADED_NOTES.md) | What was added/changed |
| [Package Stats](notes/05_Study_Resources/PACKAGE_STATS.md) | Generated file counts |

---

## Known gaps

These lessons are listed in their chapter `README.md` but the files do not exist yet:

- `02_Computer_Networking/02_Network_Architecture_Topologies/03_Control_Plane_Data_Plane_Management_Plane.md`
- `02_Computer_Networking/13_Network_Security_Firewall_VPN_ZeroTrust/01_Threat_Model_CIA_and_Defence_in_Depth.md`
- `02_Computer_Networking/15_IP_Tracing_Reputation_Route_Analysis/05_Remote_Activities_and_Log_Ownership.md`
- `02_Computer_Networking/15_IP_Tracing_Reputation_Route_Analysis/06_Ethical_Remote_Investigation_Workflow.md`

---

## Roadmap

- [x] **Phase 1 — Structure the notes** (this layout)
- [ ] **Phase 2 — Automation project** built on top of these notes (to be designed)
