# 08 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **TCP vs UDP:** Define, draw its workflow, give a real example and identify one important limitation.

2. **DNS Lookup Journey:** Define, draw its workflow, give a real example and identify one important limitation.

3. **DHCP DORA and DHCPv6:** Define, draw its workflow, give a real example and identify one important limitation.

4. **ARP ICMP NTP:** Define, draw its workflow, give a real example and identify one important limitation.

5. **HTTP HTTPS TLS:** Define, draw its workflow, give a real example and identify one important limitation.

6. **Mail and Remote Administration:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **TCP vs UDP — Model answer:** TCP connection-oriented reliable byte stream; UDP connectionless datagrams no delivery guarantee. **Working:** TCP seq/ack, flow and congestion control; UDP application decides reliability. **Example:** File download needs reliable data; live voice prefers timely packets. **Nuance:** QUIC builds reliability and encryption atop UDP; RTP media can use FEC/jitter buffers. **Avoid:** TCP reliable ≠ instant; retransmissions increase latency.

2. **DNS Lookup Journey — Model answer:** DNS maps domain names to records; recursive resolver queries authoritative hierarchy and caches TTL. **Working:** Stub resolver → recursive → root/TLD/authoritative → A/AAAA answer. **Example:** Browser needs IP for example.com, caches answer until expiry. **Nuance:** CNAME, MX, TXT, DNSSEC, HTTPS/SVCB, DoH/DoT/DoQ, QNAME minimization. **Avoid:** DNS answer varies with CDN/geo/cache; one nslookup not global truth.

3. **DHCP DORA and DHCPv6 — Model answer:** DHCP leases IP config; IPv4 DORA Discover Offer Request Acknowledge. **Working:** Broadcast initially; DHCP server/relay provides IP, gateway, DNS, lease time. **Example:** Device joins office LAN and automatically receives 192.168.x IP. **Nuance:** DHCP option 82, reservations, PXE boot, DHCPv6 and SLAAC differ. **Avoid:** 169.254/16 on Windows often indicates IPv4 DHCP issue; do not treat as Internet IP.

4. **ARP ICMP NTP — Model answer:** ARP IPv4 local neighbor lookup; ICMP sends network feedback; NTP synchronizes time. **Working:** ICMP echo is diagnostic, destination unreachable/error guide troubleshooting. **Example:** Ping gateway RTT; NTP keeps log timestamps consistent. **Nuance:** ICMP Packet Too Big essential for PMTU, NTP auth/NTS protects time integrity. **Avoid:** Blocking all ICMP can break PMTUD; ICMP echo ≠ all ICMP.

5. **HTTP HTTPS TLS — Model answer:** HTTP application request-response; HTTPS = HTTP protected by TLS; TLS authenticates server and encrypts traffic. **Working:** DNS resolve → TCP/TLS or QUIC → HTTP request → response. **Example:** Login POST must use HTTPS and validate certificate. **Nuance:** HSTS, ECH adoption, HTTPS records, Certificate Transparency, HTTP/2 multiplex, HTTP/3. **Avoid:** HTTPS does not guarantee safe website: it secures transport, not page honesty.

6. **Mail and Remote Administration — Model answer:** SMTP sends mail; IMAP reads mail; SSH remote administration; RDP desktop; SNMP telemetry. **Working:** Each uses ports and authentication; mail domain MX routes to receiving servers. **Example:** IT admin uses SSH to manage authorized Linux host. **Nuance:** SMTPS/STARTTLS, DMARC SPF DKIM, SNMPv3, SSH keys and host key pinning. **Avoid:** SMTP 25 vs submission 587, IMAP 993; TLS setup matters.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
