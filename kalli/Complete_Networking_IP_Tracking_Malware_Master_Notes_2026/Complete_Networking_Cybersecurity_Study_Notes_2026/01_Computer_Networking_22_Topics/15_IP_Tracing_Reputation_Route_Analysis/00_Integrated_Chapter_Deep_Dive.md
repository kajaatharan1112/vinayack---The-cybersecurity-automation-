# 15 — Integrated Deep-Dive Textbook: IP Tracing Reputation Route Analysis

## Big Picture: what makes this chapter important?

Safe and realistic IP intelligence foundations; extended dedicated section included. Traceroute estimates route hops through TTL and may show stars because routers filter or rate-limit diagnostic replies. RDAP gives registry allocation, ASN describes routing, geolocation predicts rough network geography, and reputation suggests abuse reports. None provides complete browsing history, exact street location, device screen or person identity. Authorized server/endpoint/NAT logs are needed for investigation.

## Architecture / Packet Path Diagram

```text
IP --> RDAP/ASN/DNS/reputation (public hints)
   --> owner logs and NAT/VPN records (restricted evidence)
   --> cautious conclusion (never identity from IP alone)
```

**Interpretation:** Remote public IP investigation is not surveillance. A traceroute path, geo estimate and abuse feed are all incomplete evidence.

## Deep worked learning sequence

Read each lesson below as a connected narrative. For detailed individual exam Q&A, use the numbered subtopic files; for assignments do the Lab Workbook.

### 1. Traceroute and Hops

**Definition and intuition:** Traceroute estimates Layer 3 path with TTL-expired responses; it does not track a person's movement.

**Mechanism in plain terms:** Probes increasing TTL; intermediate router may reply ICMP Time Exceeded.

**Industry situation:** tracert example.com shows some network hops if permitted.

**Rare/advanced case to study next:** ECMP causes path changes; Paris traceroute and MTR are more nuanced.

**How you prove/disprove your first guess:** Missing hop (* * *) often ICMP filtering, not proof of failure.

**Mini exercise:** Run tracert example.com or traceroute example.com non-invasive and document caveats.

### 2. WHOIS RDAP Registry and ASN

**Definition and intuition:** RIR RDAP shows allocation and network organization, ASN maps routing domain; not owner of device.

**Mechanism in plain terms:** Use public allocation records; resolve ASN via BGP origin information.

**Industry situation:** Cloud hosted IP belongs to provider even when website belongs to tenant.

**Rare/advanced case to study next:** RPKI origin authorization, IP delegation and transferred allocations require context.

**How you prove/disprove your first guess:** Registrant address not geolocation of current device.

**Mini exercise:** Look up 1.1.1.1 using authorized public RDAP and note organization only.

### 3. IP Geolocation Limits

**Definition and intuition:** Commercial IP location uses heuristics, databases, operator geofeeds; estimated not GPS.

**Mechanism in plain terms:** ISP geo ranges, active measurements and user-provided signals may improve estimate.

**Industry situation:** Mobile network egress may appear in other city than subscriber.

**Rare/advanced case to study next:** CGNAT, VPN, roaming and anycast make attribution more uncertain.

**How you prove/disprove your first guess:** Exact home or person cannot be found from public IP alone.

**Mini exercise:** Prepare confidence rating low/medium/high for sample location claims.

### 4. IP Reputation Threat Intelligence

**Definition and intuition:** Reputation lists report scanning, abuse or known bad activity; time/context matter.

**Mechanism in plain terms:** Combine source, last-seen, indicator type, false positive review.

**Industry situation:** A public cloud IP appears on abuse feed, but tenant change invalidates assumption.

**Rare/advanced case to study next:** Threat intel expiration, shared hosting and stale indicators require scoring.

**How you prove/disprove your first guess:** Blacklist entry is not legal proof that current user performed attack.

**Mini exercise:** Design a report with evidence source, time, confidence and remediation.

### 5. Remote Activities and Log Ownership

**Definition and intuition:** Remote IP address by itself reveals no device screen, file list or full browsing history.

**Mechanism in plain terms:** Only owned servers/firewalls/flows/endpoint logs provide observations about traffic passing through them.

**Industry situation:** Your API access log records IP, timestamp, request path, status for visitors.

**Rare/advanced case to study next:** NAT/CGNAT logging plus source port, time sync and lawful process important for attribution.

**How you prove/disprove your first guess:** IP=person inference false; TLS payload not freely visible.

**Mini exercise:** Draft allowed data fields for your own website visitor analytics with privacy retention.

### 6. Ethical Remote Investigation Workflow

**Definition and intuition:** Define permission, purpose, retention, public passive checks and owner-side telemetry.

**Mechanism in plain terms:** Observe public DNS/RDAP; correlate your own firewall/app logs; verify before conclusions.

**Industry situation:** Investigate repeated failed login IP in your own university lab service.

**Rare/advanced case to study next:** Confidence scoring, triage workflow, legal hold and minimal collection.

**How you prove/disprove your first guess:** Do not probe unauthorized third-party IPs or attempt covert monitoring.

**Mini exercise:** Make 1-page investigation record with evidence/time/authorization/uncertainty.

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

- [ARIN: IP record location limitations](https://www.arin.net/about/relations/law_enforcement/faq/)
- [APNIC 2026: Geolocation evidence not certainty](https://blog.apnic.net/2026/09/24/ip-geolocation-at-apnic-62-challenges-geofeeds-and-data-quality-perspectives/)
- [NIST SP 800-86 Forensics](https://csrc.nist.gov/pubs/sp/800/86/final)
