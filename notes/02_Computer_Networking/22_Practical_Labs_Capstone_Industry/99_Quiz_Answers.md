# 22 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **Build a Virtual Network Lab:** Define, draw its workflow, give a real example and identify one important limitation.

2. **Subnet Routing VLAN Project:** Define, draw its workflow, give a real example and identify one important limitation.

3. **Analyze PCAP and Troubleshoot:** Define, draw its workflow, give a real example and identify one important limitation.

4. **Deploy Secure Three Tier Demo:** Define, draw its workflow, give a real example and identify one important limitation.

5. **Cloud Native Capstone:** Define, draw its workflow, give a real example and identify one important limitation.

6. **Network Engineer Real Time Workflow:** Define, draw its workflow, give a real example and identify one important limitation.

7. **Career Roadmap and Assessment:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **Build a Virtual Network Lab — Model answer:** Isolated virtual networks support safe experimentation without touching neighbors. **Working:** Create two client VMs and one router VM, internal networks, static/DHCP and firewall. **Example:** Subnet A 192.168.10.0/24 to subnet B 192.168.20.0/24 via lab router. **Nuance:** Network namespaces, Linux bridges, virtual switches, container networks allow low-cost labs. **Avoid:** Bridged adapter may accidentally expose tests to office network; prefer host-only/internal.

2. **Subnet Routing VLAN Project — Model answer:** Design addressing, assign VLANs and inter-VLAN firewall permission. **Working:** Plan prefix → configure gateway → route → restrict by zone → validate. **Example:** University network students, lecturers, exam server isolated. **Nuance:** IPv6 dual stack and DHCP snooping/RA guard are modern stretch tasks. **Avoid:** Ping works but security isolation absent if ACL permits all.

3. **Analyze PCAP and Troubleshoot — Model answer:** Use recorded safe PCAP to recognize DNS resolution, TCP/TLS handshake, retransmission and application response. **Working:** Timestamp flows; correlate RTT and errors; form multiple hypotheses. **Example:** Slow HTTPS caused by DNS timeout rather than packet loss. **Nuance:** Capture position/clock skew, QUIC encryption limit full visibility. **Avoid:** Packet missing from capture could be collection loss, not wire loss.

4. **Deploy Secure Three Tier Demo — Model answer:** Frontend reverse proxy, API and database separated; enforce least privilege and TLS. **Working:** Private DB binds internal interface, firewall permits only app, public HTTPS at edge. **Example:** Simple student portal test application with local dummy data. **Nuance:** Zero trust workload identities, secrets rotation, SBOM supply-chain awareness. **Avoid:** Default DB password and publicly exposed admin port ruin network segmentation.

5. **Cloud Native Capstone — Model answer:** Deploy conceptual Kubernetes app with pod/service/network policy/gateway; observe HTTP metrics. **Working:** Ingress HTTPRoute → web service → API → DB service; policy restricts flows. **Example:** Scale API replicas during simulated class registration surge. **Nuance:** eBPF visibility, mTLS, GitOps and progressive delivery advanced phases. **Avoid:** Complexity grows fast; start with local mini lab before managed cloud.

6. **Network Engineer Real Time Workflow — Model answer:** Production engineer checks change tickets, monitoring, incidents, diagrams and verifies rollback. **Working:** Baseline → deploy controlled change → observe user impact → audit/retrospective. **Example:** Morning incident: VPN DNS outage; test affected users, bypass invalid resolver, restore. **Nuance:** Runbooks, on-call, postmortems, capacity forecasts, fault injection. **Avoid:** Guessing and changing live routers under pressure can worsen blast radius.

7. **Career Roadmap and Assessment — Model answer:** Networking fundamentals, hands-on proof, security mindset and modern cloud fluency reinforce one another. **Working:** Build lab portfolio, practice binary subnetting, explain packet paths, troubleshoot systematically. **Example:** Interview: explain why browser says DNS_PROBE_FINISHED_NXDOMAIN despite Wi-Fi. **Nuance:** CCNA-level foundations then specialist tracks cloud networking, NRE, SRE, SOC, blue team. **Avoid:** Cert memorization without labs creates fragile understanding.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
