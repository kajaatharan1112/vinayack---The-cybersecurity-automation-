# 08 — Integrated Deep-Dive Textbook: Network Protocols

## Big Picture: what makes this chapter important?

How common networking protocols fit together. Name resolution (DNS), address assignment (DHCP), neighbor discovery (ARP/NDP), IP routing, transport reliability (TCP/QUIC), time sync (NTP), application authentication (TLS/SSH) are separate mechanisms. A client can have a correct IPv4 address yet fail DNS, or resolve a domain correctly while the endpoint rejects TCP. Treat each protocol outcome as one piece of evidence.

## Architecture / Packet Path Diagram

```text
Client --> DNS resolver --> A/AAAA
Client --TCP+TLS or QUIC--> HTTPS server
Client --DHCP--> obtains local IP/gateway/DNS
```

**Interpretation:** Different protocols solve different problems: DNS naming, DHCP configuration, IP routing, TCP/QUIC transfer, TLS authentication/encryption, HTTP application semantics.

## Deep worked learning sequence

Read each lesson below as a connected narrative. For detailed individual exam Q&A, use the numbered subtopic files; for assignments do the Lab Workbook.

### 1. TCP vs UDP

**Definition and intuition:** TCP connection-oriented reliable byte stream; UDP connectionless datagrams no delivery guarantee.

**Mechanism in plain terms:** TCP seq/ack, flow and congestion control; UDP application decides reliability.

**Industry situation:** File download needs reliable data; live voice prefers timely packets.

**Rare/advanced case to study next:** QUIC builds reliability and encryption atop UDP; RTP media can use FEC/jitter buffers.

**How you prove/disprove your first guess:** TCP reliable ≠ instant; retransmissions increase latency.

**Mini exercise:** Run ss -tu or netstat -an to compare TCP/UDP sockets.

### 2. DNS Lookup Journey

**Definition and intuition:** DNS maps domain names to records; recursive resolver queries authoritative hierarchy and caches TTL.

**Mechanism in plain terms:** Stub resolver → recursive → root/TLD/authoritative → A/AAAA answer.

**Industry situation:** Browser needs IP for example.com, caches answer until expiry.

**Rare/advanced case to study next:** CNAME, MX, TXT, DNSSEC, HTTPS/SVCB, DoH/DoT/DoQ, QNAME minimization.

**How you prove/disprove your first guess:** DNS answer varies with CDN/geo/cache; one nslookup not global truth.

**Mini exercise:** nslookup example.com and nslookup -type=MX example.com; compare record purposes.

### 3. DHCP DORA and DHCPv6

**Definition and intuition:** DHCP leases IP config; IPv4 DORA Discover Offer Request Acknowledge.

**Mechanism in plain terms:** Broadcast initially; DHCP server/relay provides IP, gateway, DNS, lease time.

**Industry situation:** Device joins office LAN and automatically receives 192.168.x IP.

**Rare/advanced case to study next:** DHCP option 82, reservations, PXE boot, DHCPv6 and SLAAC differ.

**How you prove/disprove your first guess:** 169.254/16 on Windows often indicates IPv4 DHCP issue; do not treat as Internet IP.

**Mini exercise:** Inspect lease obtained/expires and DNS servers with ipconfig /all.

### 4. ARP ICMP NTP

**Definition and intuition:** ARP IPv4 local neighbor lookup; ICMP sends network feedback; NTP synchronizes time.

**Mechanism in plain terms:** ICMP echo is diagnostic, destination unreachable/error guide troubleshooting.

**Industry situation:** Ping gateway RTT; NTP keeps log timestamps consistent.

**Rare/advanced case to study next:** ICMP Packet Too Big essential for PMTU, NTP auth/NTS protects time integrity.

**How you prove/disprove your first guess:** Blocking all ICMP can break PMTUD; ICMP echo ≠ all ICMP.

**Mini exercise:** ping 127.0.0.1 and traceroute or tracert documentation example.

### 5. HTTP HTTPS TLS

**Definition and intuition:** HTTP application request-response; HTTPS = HTTP protected by TLS; TLS authenticates server and encrypts traffic.

**Mechanism in plain terms:** DNS resolve → TCP/TLS or QUIC → HTTP request → response.

**Industry situation:** Login POST must use HTTPS and validate certificate.

**Rare/advanced case to study next:** HSTS, ECH adoption, HTTPS records, Certificate Transparency, HTTP/2 multiplex, HTTP/3.

**How you prove/disprove your first guess:** HTTPS does not guarantee safe website: it secures transport, not page honesty.

**Mini exercise:** curl -I https://example.com and record status/security headers if exposed.

### 6. Mail and Remote Administration

**Definition and intuition:** SMTP sends mail; IMAP reads mail; SSH remote administration; RDP desktop; SNMP telemetry.

**Mechanism in plain terms:** Each uses ports and authentication; mail domain MX routes to receiving servers.

**Industry situation:** IT admin uses SSH to manage authorized Linux host.

**Rare/advanced case to study next:** SMTPS/STARTTLS, DMARC SPF DKIM, SNMPv3, SSH keys and host key pinning.

**How you prove/disprove your first guess:** SMTP 25 vs submission 587, IMAP 993; TLS setup matters.

**Mini exercise:** Create secure configuration checklist for SSH, mail and SNMP (no live login).

## Production-level decision checklist

1. **Boundary:** Which component has ownership of the behavior? Clarify endpoint, device, service and provider.
2. **Baseline:** What is expected when the system works? Record concrete route, protocol, log fields and time.
3. **Observation:** Which evidence supports the suspected cause and what is merely correlation?
4. **Security:** Which minimum privileges, segmented paths, keys and logging are required?
5. **Modern dependency:** What version/hardware/standard/vendor limitations change behavior?
6. **Roll-back plan:** Could a proposed fix break other users? Test in lab first.

## Chapter exam challenge

Explain at least three subtopics using a diagram; then provide one failure that could be misdiagnosed, the correct measurement, a modern industry exception, and an ethically safe lab demonstration.

## Official background

- [RFC 9460 DNS SVCB/HTTPS](https://www.rfc-editor.org/rfc/rfc9460)
- [RFC 9293 TCP](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 9114 HTTP/3](https://www.rfc-editor.org/rfc/rfc9114)
