# 17 — Integrated Deep-Dive Textbook: Server Networking DNS DHCP Web

## Big Picture: what makes this chapter important?

Operate core infrastructure services safely. DNS maps names to records; authoritative and recursive DNS servers serve different roles. DHCP leases addresses, but an off-subnet relay is required when the DHCP server is elsewhere. Reverse proxies terminate and route HTTP while apps run business logic. This division of responsibility is essential for maintenance, high availability and forensic logging.

## Architecture / Packet Path Diagram

```text
Client --DNS--> hostname/IP
Client --HTTP/TLS--> Reverse proxy --API--> DB
Client --DHCP--> IPv4 config
```

**Interpretation:** DNS is not a web server; a successful TCP handshake is not application readiness; accurate NTP is essential for log correlation.

## Deep worked learning sequence

Read each lesson below as a connected narrative. For detailed individual exam Q&A, use the numbered subtopic files; for assignments do the Lab Workbook.

### 1. DNS Server Roles and Zones

**Definition and intuition:** Authoritative servers host records; recursive servers answer clients via cache/lookup.

**Mechanism in plain terms:** Zone SOA, NS, A, AAAA, CNAME, MX, TXT; TTL controls caching.

**Industry situation:** School domain records point portal to load balancer and email to provider.

**Rare/advanced case to study next:** DNSSEC validates data authenticity; DNS views/split-horizon for internal use.

**How you prove/disprove your first guess:** Wrong authoritative delegation causes persistent failure despite local changes.

**Mini exercise:** Design a sample zone file for lab.example.test with web and mail (fictional).

### 2. DHCP Server Scopes and Relay

**Definition and intuition:** DHCP provides address/gateway/resolver; relay forwards between VLANs.

**Mechanism in plain terms:** DORA, lease renew/rebind; server chooses available address in scope.

**Industry situation:** Staff VLAN gateway relays DHCP requests to central server.

**Rare/advanced case to study next:** DHCP snooping prevents rogue servers; options for PXE/VoIP.

**How you prove/disprove your first guess:** Competing DHCP servers make intermittent wrong gateway.

**Mini exercise:** Write scope table with reserved range, lease time, router and DNS.

### 3. Linux Web Server Reverse Proxy

**Definition and intuition:** Web server terminates HTTP/TLS, reverse proxy routes to services and enforces headers.

**Mechanism in plain terms:** Listener 443 → TLS → HTTP host/path routing → app upstream.

**Industry situation:** Campus portal API proxied by Nginx/Apache to app service.

**Rare/advanced case to study next:** HTTP/2/3, mTLS backend, caching, WAF integration, rate limit.

**How you prove/disprove your first guess:** Expose app only on internal interface; proxy upstream health matters.

**Mini exercise:** Using own machine, python3 -m http.server 8000 then curl localhost; stop after.

### 4. SSH SFTP Remote Management

**Definition and intuition:** SSH secure shell and file transfer; restrict accounts and keys.

**Mechanism in plain terms:** Client verifies server host key; user authenticates by public key or password.

**Industry situation:** Admin accesses company Linux VM through VPN + SSH.

**Rare/advanced case to study next:** FIDO2-backed SSH keys, short-lived certificates, bastion host, JIT access.

**How you prove/disprove your first guess:** Never ignore changed SSH host-key warning without verification.

**Mini exercise:** Write sshd hardening checklist: keys, updates, MFA gateway, audit.

### 5. Time Synchronization NTP Logging

**Definition and intuition:** Aligned clocks make authentication and incident timelines reliable.

**Mechanism in plain terms:** NTP synchronizes time to reference; offsets/drift monitored.

**Industry situation:** Firewall at 12:00, app at 12:07 causes forensic timeline confusion.

**Rare/advanced case to study next:** NTS Network Time Security, monotonic vs wall time, leap seconds.

**How you prove/disprove your first guess:** Time zone vs UTC differences can look like malicious activity.

**Mini exercise:** Make 5-event log timeline in UTC with consistent timezone annotations.

### 6. Backups Storage and Availability

**Definition and intuition:** RAID improves uptime, backup restores data, replication improves recovery; not synonyms.

**Mechanism in plain terms:** Set RPO/RTO, immutable offsite backups, regular restore tests.

**Industry situation:** Ransomware encrypted file share; backup recovery must be independent.

**Rare/advanced case to study next:** 3-2-1-1-0 backup strategy, snapshots vs air-gapped copies, quorum.

**How you prove/disprove your first guess:** RAID is not a backup; replication can replicate corruption instantly.

**Mini exercise:** Choose RPO/RTO for university exam system and restoration exercise.

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
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
