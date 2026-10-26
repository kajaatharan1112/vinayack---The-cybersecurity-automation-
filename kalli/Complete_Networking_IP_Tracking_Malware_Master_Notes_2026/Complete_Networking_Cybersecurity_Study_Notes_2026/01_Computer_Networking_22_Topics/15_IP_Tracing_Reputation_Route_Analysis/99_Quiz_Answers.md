# 15 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **Traceroute and Hops:** Define, draw its workflow, give a real example and identify one important limitation.

2. **WHOIS RDAP Registry and ASN:** Define, draw its workflow, give a real example and identify one important limitation.

3. **IP Geolocation Limits:** Define, draw its workflow, give a real example and identify one important limitation.

4. **IP Reputation Threat Intelligence:** Define, draw its workflow, give a real example and identify one important limitation.

5. **Remote Activities and Log Ownership:** Define, draw its workflow, give a real example and identify one important limitation.

6. **Ethical Remote Investigation Workflow:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **Traceroute and Hops — Model answer:** Traceroute estimates Layer 3 path with TTL-expired responses; it does not track a person's movement. **Working:** Probes increasing TTL; intermediate router may reply ICMP Time Exceeded. **Example:** tracert example.com shows some network hops if permitted. **Nuance:** ECMP causes path changes; Paris traceroute and MTR are more nuanced. **Avoid:** Missing hop (* * *) often ICMP filtering, not proof of failure.

2. **WHOIS RDAP Registry and ASN — Model answer:** RIR RDAP shows allocation and network organization, ASN maps routing domain; not owner of device. **Working:** Use public allocation records; resolve ASN via BGP origin information. **Example:** Cloud hosted IP belongs to provider even when website belongs to tenant. **Nuance:** RPKI origin authorization, IP delegation and transferred allocations require context. **Avoid:** Registrant address not geolocation of current device.

3. **IP Geolocation Limits — Model answer:** Commercial IP location uses heuristics, databases, operator geofeeds; estimated not GPS. **Working:** ISP geo ranges, active measurements and user-provided signals may improve estimate. **Example:** Mobile network egress may appear in other city than subscriber. **Nuance:** CGNAT, VPN, roaming and anycast make attribution more uncertain. **Avoid:** Exact home or person cannot be found from public IP alone.

4. **IP Reputation Threat Intelligence — Model answer:** Reputation lists report scanning, abuse or known bad activity; time/context matter. **Working:** Combine source, last-seen, indicator type, false positive review. **Example:** A public cloud IP appears on abuse feed, but tenant change invalidates assumption. **Nuance:** Threat intel expiration, shared hosting and stale indicators require scoring. **Avoid:** Blacklist entry is not legal proof that current user performed attack.

5. **Remote Activities and Log Ownership — Model answer:** Remote IP address by itself reveals no device screen, file list or full browsing history. **Working:** Only owned servers/firewalls/flows/endpoint logs provide observations about traffic passing through them. **Example:** Your API access log records IP, timestamp, request path, status for visitors. **Nuance:** NAT/CGNAT logging plus source port, time sync and lawful process important for attribution. **Avoid:** IP=person inference false; TLS payload not freely visible.

6. **Ethical Remote Investigation Workflow — Model answer:** Define permission, purpose, retention, public passive checks and owner-side telemetry. **Working:** Observe public DNS/RDAP; correlate your own firewall/app logs; verify before conclusions. **Example:** Investigate repeated failed login IP in your own university lab service. **Nuance:** Confidence scoring, triage workflow, legal hold and minimal collection. **Avoid:** Do not probe unauthorized third-party IPs or attempt covert monitoring.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
