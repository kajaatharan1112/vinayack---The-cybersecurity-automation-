# 09 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **Port Basics and IANA Ranges:** Define, draw its workflow, give a real example and identify one important limitation.

2. **Common Service Ports:** Define, draw its workflow, give a real example and identify one important limitation.

3. **Ephemeral Ports and Five Tuple:** Define, draw its workflow, give a real example and identify one important limitation.

4. **Service Discovery and Banners:** Define, draw its workflow, give a real example and identify one important limitation.

5. **Firewall Reachability and Health:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **Port Basics and IANA Ranges — Model answer:** Ports identify transport endpoints; 0-1023 well-known, 1024-49151 registered, 49152-65535 dynamic IANA ranges. **Working:** TCP/UDP have separate port spaces; socket and IP tuple identify connection. **Example:** HTTPS commonly 443, DNS 53, SSH 22. **Nuance:** Applications can use alternate ports; port number does not prove protocol identity. **Avoid:** Port open ≠ vulnerability; exposure, patch level and auth determine risk.

2. **Common Service Ports — Model answer:** 22 SSH, 53 DNS, 80 HTTP, 123 NTP, 443 HTTPS, 445 SMB, 3389 RDP; services may differ. **Working:** Server process listens; firewall decides network reachability. **Example:** Website open 443, DB private 5432; best practices block DB from Internet. **Nuance:** Modern protocols QUIC UDP/443, DNS over TLS TCP/853, DNS over HTTPS TCP/443. **Avoid:** Some ports are multiplexed; reverse proxy hosts many domains on same 443.

3. **Ephemeral Ports and Five Tuple — Model answer:** Client uses transient src port to distinguish flows; service listens stable destination port. **Working:** Outbound connection often src 50000 → dst 443; NAT may change src port. **Example:** Multiple browsers on one PC connect to same server without collision. **Nuance:** NAT conntrack exhaustion/ephemeral port exhaustion under heavy request load. **Avoid:** Port 443 in local endpoint can be remote or local; inspect both sides.

4. **Service Discovery and Banners — Model answer:** DNS SRV/mDNS/LLDP plus probes reveal services; banner may show software. **Working:** Application greeting or TLS handshake metadata indicates protocol/version. **Example:** SSH server sends version line; HTTP response has Server header sometimes. **Nuance:** Encrypted protocols reduce readable metadata; default banners can mislead. **Avoid:** Banner says old version not proof exploit works; vendor backports patches.

5. **Firewall Reachability and Health — Model answer:** Path requires DNS, routing, ACL, listening socket, healthy application. **Working:** SYN permitted and server replies; app/TLS layer can still fail. **Example:** API port open but 503 due overloaded DB. **Nuance:** L4 vs L7 health checks give different readiness; K8s probes affect routing. **Avoid:** Ping blocked != TCP blocked; zero response != definite port closed.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
