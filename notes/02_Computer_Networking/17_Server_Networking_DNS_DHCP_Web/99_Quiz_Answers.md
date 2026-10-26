# 17 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **DNS Server Roles and Zones:** Define, draw its workflow, give a real example and identify one important limitation.

2. **DHCP Server Scopes and Relay:** Define, draw its workflow, give a real example and identify one important limitation.

3. **Linux Web Server Reverse Proxy:** Define, draw its workflow, give a real example and identify one important limitation.

4. **SSH SFTP Remote Management:** Define, draw its workflow, give a real example and identify one important limitation.

5. **Time Synchronization NTP Logging:** Define, draw its workflow, give a real example and identify one important limitation.

6. **Backups Storage and Availability:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **DNS Server Roles and Zones — Model answer:** Authoritative servers host records; recursive servers answer clients via cache/lookup. **Working:** Zone SOA, NS, A, AAAA, CNAME, MX, TXT; TTL controls caching. **Example:** School domain records point portal to load balancer and email to provider. **Nuance:** DNSSEC validates data authenticity; DNS views/split-horizon for internal use. **Avoid:** Wrong authoritative delegation causes persistent failure despite local changes.

2. **DHCP Server Scopes and Relay — Model answer:** DHCP provides address/gateway/resolver; relay forwards between VLANs. **Working:** DORA, lease renew/rebind; server chooses available address in scope. **Example:** Staff VLAN gateway relays DHCP requests to central server. **Nuance:** DHCP snooping prevents rogue servers; options for PXE/VoIP. **Avoid:** Competing DHCP servers make intermittent wrong gateway.

3. **Linux Web Server Reverse Proxy — Model answer:** Web server terminates HTTP/TLS, reverse proxy routes to services and enforces headers. **Working:** Listener 443 → TLS → HTTP host/path routing → app upstream. **Example:** Campus portal API proxied by Nginx/Apache to app service. **Nuance:** HTTP/2/3, mTLS backend, caching, WAF integration, rate limit. **Avoid:** Expose app only on internal interface; proxy upstream health matters.

4. **SSH SFTP Remote Management — Model answer:** SSH secure shell and file transfer; restrict accounts and keys. **Working:** Client verifies server host key; user authenticates by public key or password. **Example:** Admin accesses company Linux VM through VPN + SSH. **Nuance:** FIDO2-backed SSH keys, short-lived certificates, bastion host, JIT access. **Avoid:** Never ignore changed SSH host-key warning without verification.

5. **Time Synchronization NTP Logging — Model answer:** Aligned clocks make authentication and incident timelines reliable. **Working:** NTP synchronizes time to reference; offsets/drift monitored. **Example:** Firewall at 12:00, app at 12:07 causes forensic timeline confusion. **Nuance:** NTS Network Time Security, monotonic vs wall time, leap seconds. **Avoid:** Time zone vs UTC differences can look like malicious activity.

6. **Backups Storage and Availability — Model answer:** RAID improves uptime, backup restores data, replication improves recovery; not synonyms. **Working:** Set RPO/RTO, immutable offsite backups, regular restore tests. **Example:** Ransomware encrypted file share; backup recovery must be independent. **Nuance:** 3-2-1-1-0 backup strategy, snapshots vs air-gapped copies, quorum. **Avoid:** RAID is not a backup; replication can replicate corruption instantly.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
