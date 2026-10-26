# 03 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **IP Address and Identity Limits:** Define, draw its workflow, give a real example and identify one important limitation.

2. **Passive vs Active Reconnaissance:** Define, draw its workflow, give a real example and identify one important limitation.

3. **RIR RDAP WHOIS IP Ownership:** Define, draw its workflow, give a real example and identify one important limitation.

4. **ASN BGP Origin and Prefixes:** Define, draw its workflow, give a real example and identify one important limitation.

5. **Geolocation Country Region City Accuracy:** Define, draw its workflow, give a real example and identify one important limitation.

6. **DNS A AAAA PTR Reverse DNS:** Define, draw its workflow, give a real example and identify one important limitation.

7. **Route Tracing Traceroute MTR:** Define, draw its workflow, give a real example and identify one important limitation.

8. **Latency Measurement and Network Distance:** Define, draw its workflow, give a real example and identify one important limitation.

9. **Public Ports and Service Exposure:** Define, draw its workflow, give a real example and identify one important limitation.

10. **IP Reputation Blocklists OSINT Confidence:** Define, draw its workflow, give a real example and identify one important limitation.

11. **Threat Intelligence Enrichment Workflow:** Define, draw its workflow, give a real example and identify one important limitation.

12. **Server Access Logs and IP Activity:** Define, draw its workflow, give a real example and identify one important limitation.

13. **Firewall NAT VPN Proxy Logs:** Define, draw its workflow, give a real example and identify one important limitation.

14. **Flow Telemetry NetFlow IPFIX sFlow:** Define, draw its workflow, give a real example and identify one important limitation.

15. **DNS Logs and Encrypted DNS Limits:** Define, draw its workflow, give a real example and identify one important limitation.

16. **Endpoint EDR and Browser Evidence:** Define, draw its workflow, give a real example and identify one important limitation.

17. **Detecting Scanning and Abuse on Owned Systems:** Define, draw its workflow, give a real example and identify one important limitation.

18. **Attribution Evidence Chain of Custody:** Define, draw its workflow, give a real example and identify one important limitation.

19. **Privacy Laws Ethics Authorization:** Define, draw its workflow, give a real example and identify one important limitation.

20. **Case Study Suspicious IP on Own API:** Define, draw its workflow, give a real example and identify one important limitation.

21. **Live Network Monitoring Dashboard Design:** Define, draw its workflow, give a real example and identify one important limitation.

22. **Limits of Remote Investigation Summary:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **IP Address and Identity Limits — Model answer:** IP is a routing locator, not a person ID. Public IP may be shared by household, university, VPN or cloud tenants. **Working:** Private hosts can be mapped to public address via NAT; different users can share same egress. **Example:** Three students behind campus NAT visit the same site and appear as one public IP. **Nuance:** IPv6 temporary addresses, carrier NAT, anycast and mobile roaming break simple attribution. **Avoid:** Never call a geolocation result a person's precise address; avoid stalking or unwarranted inference.

2. **Passive vs Active Reconnaissance — Model answer:** Passive intelligence reads already published data; active probes send traffic to target and require authority. **Working:** RDAP/DNS/BGP public lookups generally don't scan target; TCP probing does. **Example:** Investigate institution-owned web IP: registration data first, then approved owner-side checks. **Nuance:** Intelligence should note collection date, permissible use, accuracy and scope. **Avoid:** Public data not always current; no authorization to compromise or harvest private activity.

3. **RIR RDAP WHOIS IP Ownership — Model answer:** Regional Internet Registries allocate IP blocks and offer RDAP records with contacts/netname/ASN info. **Working:** Given IP determine covering prefix/RIR; access RDAP server; compare allocated org and actual service. **Example:** 203.0.113.8 is reserved documentation IP; real allocation lookups should use a legitimate chosen test address. **Nuance:** Reallocations/leased address ranges and CDN fronting mean registry org need not host owner. **Avoid:** Registry mailing address is not physical user location.

4. **ASN BGP Origin and Prefixes — Model answer:** ASN is an administrative routing domain number; BGP origin ASN advertises reachability for IP prefix. **Working:** BGP views show announcements and AS paths; traceroute reveals some forwarding hops only. **Example:** A hosting provider AS announces /24 used by many customer websites. **Nuance:** RPKI ROAs and route collectors help verify routing claims, not person attribution. **Avoid:** AS path is not proof of physical transit or user identity.

5. **Geolocation Country Region City Accuracy — Model answer:** IP geolocation returns inferred location from databases/measurements, never GPS precision by itself. **Working:** ISP allocations, geofeeds, measurement and commercial estimates can disagree. **Example:** VPN exit in Singapore while user physically in Sri Lanka produces misleading result. **Nuance:** Latency triangulation has assumptions; mobile provider central egress causes apparent city drift. **Avoid:** Two services disagreeing is normal; show confidence and data source rather than one pin.

6. **DNS A AAAA PTR Reverse DNS — Model answer:** Forward DNS hostname→IP; PTR reverse IP→hostname, names require no direct ownership proof beyond zone control. **Working:** Recursive DNS, caching, PTR delegation, forward-confirmed reverse DNS used in mail contexts. **Example:** PTR for mail server may differ from customer website domain. **Nuance:** DNSSEC authenticity of DNS answers and SVCB/HTTPS DNS changes client endpoints. **Avoid:** A PTR entry cannot prove server purpose or the human behind it.

7. **Route Tracing Traceroute MTR — Model answer:** Traceroute TTL probes estimate router path; MTR samples repeated hop RTT and loss. **Working:** TTL increments cause routers to send ICMP Time Exceeded if allowed. **Example:** VPN can change path; some hops don't reply and appear *. **Nuance:** Paris traceroute reduces ECMP confusion; asymmetric paths mean reply route differs. **Avoid:** One hop showing 80% probe loss followed by healthy final hop ≠ forwarding loss.

8. **Latency Measurement and Network Distance — Model answer:** Round-trip time includes physical propagation, serialization, queueing, processing and return path. **Working:** Speed of light in fibre gives lower-bound delay, not exact distance. **Example:** Sri Lanka→Europe round trip can be far higher than a nearby server. **Nuance:** Anycast/CDN traffic engineering confounds geographic latency inference. **Avoid:** You cannot triangulate a person's exact address from simple ping/traceroute reliably.

9. **Public Ports and Service Exposure — Model answer:** Public services may listen on permitted TCP/UDP ports; scanning third-party IP without permission is excluded. **Working:** Owner can enumerate inventory and validate exposed firewall rules from approved vantage. **Example:** Company discovers SSH unintentionally exposed to the Internet. **Nuance:** Certificate transparency, Censys-like inventories, SBOM match service inventory but can be stale. **Avoid:** Open port is not automatic compromise; service version and security context matter.

10. **IP Reputation Blocklists OSINT Confidence — Model answer:** Reputation feeds contain observations of suspicious events with timestamps and confidence. **Working:** Evaluate source, indicator freshness, type, shared-hosting and false positives. **Example:** An IP flagged yesterday could belong to new cloud customer today. **Nuance:** Indicators decay quickly; evidence chain and business context required. **Avoid:** Do not publicly accuse an individual based on a single blacklist hit.

11. **Threat Intelligence Enrichment Workflow — Model answer:** Enrichment combines registry, DNS, BGP, threat feeds and owner's log evidence for triage. **Working:** Normalize indicator → gather metadata → corroborate → classify → act → expire. **Example:** Firewall logs spike of denied connections; enrich destination IP and decide if expected monitoring. **Nuance:** STIX/TAXII sharing, MITRE technique mappings, confidence scoring and operational feedback. **Avoid:** Automated blocklists can block CDN shared IP and cause outages.

12. **Server Access Logs and IP Activity — Model answer:** Your owned web service can log client address, method, URI, status, user-agent, time; proxy may alter observed IP. **Working:** Reverse proxy can set forwarded headers with trusted chain; never blindly trust client-supplied X-Forwarded-For. **Example:** University portal sees 10 failed login POSTs from same egress IP at 09:00 UTC. **Nuance:** Pseudonymous data still personal; minimize collection and retain according to policy. **Avoid:** IP log proves request arrived, not who physically typed it or exact browsing history.

13. **Firewall NAT VPN Proxy Logs — Model answer:** Firewall tracks allowed/denied flows; NAT maps private tuple to external tuple; VPN adds login session mapping. **Working:** Correlate accurate timestamps, addresses, source ports and NAT translation with asset inventory. **Example:** 100.64.1.2:50321 mapped to public:61234 for 30-second connection. **Nuance:** NAT binding logs crucial for CGNAT investigations; encrypted proxy and IPv6 alter path. **Avoid:** Without the owner/ISP logs, public source IP generally can't identify endpoint.

14. **Flow Telemetry NetFlow IPFIX sFlow — Model answer:** Network flow data describes traffic metadata volume, not full app content or person's complete activity. **Working:** Aggregate 5-tuples, bytes, packets, first/last seen; some formats sample. **Example:** Identify sudden 5 GB upload from company laptop to new destination. **Nuance:** Encrypted ClientHello and DoH reduce hostname visibility; sFlow sampling uncertainty. **Avoid:** Cannot infer pages, chat text, passwords from metadata-only flows.

15. **DNS Logs and Encrypted DNS Limits — Model answer:** DNS resolver logs show queries it handles; clients may use local cache or encrypted external DNS. **Working:** Authoritative log ≠ every lookup; DoH/DoT can bypass enterprise DNS if allowed. **Example:** Managed device asks internal DNS for payroll.example.test prior to web access. **Nuance:** DNS rebinding defenses, DNS logging privacy, ECH and HTTPS RR emerging behaviors. **Avoid:** DNS query doesn't prove a user opened website; prefetch/background app may query.

16. **Endpoint EDR and Browser Evidence — Model answer:** Endpoint security telemetry can reveal process→connection relationships on managed systems with permission. **Working:** EDR records process tree, DNS, socket metadata; browser history belongs to authorized user/device context. **Example:** SOC investigates unexpected process connecting to newly registered domain on managed PC. **Nuance:** Process identity, signed binary trust, Sysmon event collection, tamper detection. **Avoid:** Remote third-party IP cannot remotely reveal installed apps, screen or browsing history.

17. **Detecting Scanning and Abuse on Owned Systems — Model answer:** Analyze your own logs for repeated port hits, anomalous user agents, bad auth and traffic spikes. **Working:** Baseline normal → thresholds/correlation → rate limits/alert → analyst review. **Example:** Web app sees 100 invalid login responses from a subnet in 60 s. **Nuance:** Distributed low-and-slow traffic evades single-IP thresholds; watch per account/user-device. **Avoid:** One false password doesn't mean malicious; shared NAT needs careful handling.

18. **Attribution Evidence Chain of Custody — Model answer:** Attribution needs multiple corroborating records, not geolocation alone; legal/ethical authority matters. **Working:** Clock-sync → event collection → hash/evidence custody → correlation → documented confidence. **Example:** For internal incident, correlate VPN sign-in, endpoint user, app request and NAT tuple. **Nuance:** UTC times, retention and privileged access approvals preserve defensible evidence. **Avoid:** Do not attempt to identify or surveil unknown private individuals via covert means.

19. **Privacy Laws Ethics Authorization — Model answer:** Personal data handling requires legitimate purpose, minimization, notification when applicable and safe retention. **Working:** Define scope, authorized telemetry sources, access control, retention/deletion. **Example:** Course lab analyzes synthetic log instead of real students' private browsing. **Nuance:** Cross-border data transfers and provider contractual limits matter. **Avoid:** Public Internet is not a free monitoring space; logs need governance.

20. **Case Study Suspicious IP on Own API — Model answer:** Use only owned example API logs and fabricated IPs; investigate, don't infer personal details. **Working:** Trigger → gather access logs → correlate auth/app/proxy → enrich RDAP → judge → respond. **Example:** Synthetic log 203.0.113.24 has repeated 401; could be misconfigured integration not attacker. **Nuance:** False-positive reduction, time windows, account-based rate limiting, response reproducibility. **Avoid:** Never confuse documentation IP with real malicious actor; no real scan necessary.

21. **Live Network Monitoring Dashboard Design — Model answer:** Dashboard combines interface utilization, top flows, DNS failures, TLS errors, alarms with retention limits. **Working:** Collect authorized telemetry into time series + logs; use asset context and alerts. **Example:** University ICT detects 8-minute Internet uplink degradation before classes fail. **Nuance:** OpenTelemetry, flow exporters and SIEM correlation, p95/p99 indicators. **Avoid:** Monitoring network metadata is not secret endpoint screen access.

22. **Limits of Remote Investigation Summary — Model answer:** An IP address can suggest network/service context but cannot prove exact location, individual identity or complete actions. **Working:** Public lookups → hypotheses; private endpoint/ISP logs → restricted evidence; legal authorization where required. **Example:** A NAT egress IP cannot tell whether it was student A or B. **Nuance:** VPN exit nodes, shared IP/CGNAT, ECH, rotating IPs all increase ambiguity. **Avoid:** Even matching geo/ASN/reputation is not proof; report uncertainty clearly.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
