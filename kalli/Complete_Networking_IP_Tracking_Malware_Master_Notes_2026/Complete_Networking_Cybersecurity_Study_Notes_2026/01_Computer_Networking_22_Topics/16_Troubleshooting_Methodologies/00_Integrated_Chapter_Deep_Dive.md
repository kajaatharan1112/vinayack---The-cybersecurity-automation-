# 16 — Integrated Deep-Dive Textbook: Troubleshooting Methodologies

## Big Picture: what makes this chapter important?

Repeatable root-cause approaches used by professional network engineers. The first question is scope: all sites or one site, all devices or one, wired or wireless, and when did it start? Hypothesize one layer and test only that layer. For example, IP connectivity with failed DNS points at name resolution, but an application 503 points to overloaded service despite successful connection. Use UTC timestamps and record a reversible fix.

## Architecture / Packet Path Diagram

```text
Symptom --> Scope --> Hypothesis --> Test --> Evidence --> Fix --> Verify --> Document
   L1 link | L2 VLAN | L3 route | DNS | TCP/TLS | HTTP/App
```

**Interpretation:** Bottom-up, top-down and divide-and-conquer all work; choose the least disruptive tests and preserve expected/observed values.

## Deep worked learning sequence

Read each lesson below as a connected narrative. For detailed individual exam Q&A, use the numbered subtopic files; for assignments do the Lab Workbook.

### 1. Top Down Bottom Up Divide Conquer

**Definition and intuition:** Troubleshoot OSI layers: bottom-up physical first, top-down application first or middle-out at network layer.

**Mechanism in plain terms:** Form hypothesis; run lowest-risk test; compare expected/actual; isolate; document fix.

**Industry situation:** Website fails: determine only one site vs all, then DNS, gateway, TLS.

**Rare/advanced case to study next:** Differential diagnosis and binary-search fault isolation reduce wasted work.

**How you prove/disprove your first guess:** Changing 5 settings at once prevents knowing cause and risks making outage worse.

**Mini exercise:** Write diagnostic flow: DNS failure vs packet loss vs cert expiry.

### 2. Windows Linux Mac Diagnostics

**Definition and intuition:** ipconfig /all, Test-NetConnection, Get-NetTCPConnection on Windows; ip, ss, dig, curl on Linux.

**Mechanism in plain terms:** Commands reveal local config, routes, DNS, socket state and HTTP response.

**Industry situation:** IT support remotely guides employee through non-invasive tests.

**Rare/advanced case to study next:** Namespace/container context matters: a container has its own routes/DNS.

**How you prove/disprove your first guess:** Different OS commands and permissions vary; check usage before applying.

**Mini exercise:** Compare Windows and Linux equivalents for IP, route, DNS and sockets.

### 3. DNS Troubleshooting

**Definition and intuition:** Client may cache, resolver may be unreachable, authoritative zone may be wrong.

**Mechanism in plain terms:** Check local resolver config; query records; compare recursive and authoritative responses.

**Industry situation:** LMS works by IP but hostname NXDOMAIN → DNS issue.

**Rare/advanced case to study next:** Negative caching TTL, DNSSEC validation, split-horizon DNS, HTTPS records.

**How you prove/disprove your first guess:** Flushing cache without diagnosis may hide root issue.

**Mini exercise:** nslookup example.com then compare response server and query types.

### 4. Packet Loss Jitter Latency Diagnosis

**Definition and intuition:** Loss from congestion/radio/physical; RTT from propagation/queue/processing; jitter variation.

**Mechanism in plain terms:** Check interface CRC/discards, ping path, throughput, utilization and recent changes.

**Industry situation:** Upload saturation causes video conference stutter.

**Rare/advanced case to study next:** Microbursts can evade 1-minute polling; fine-grained telemetry and ECN help.

**How you prove/disprove your first guess:** Single traceroute hop latency spike may be ICMP rate limit not forwarding issue.

**Mini exercise:** Make table symptom / likely layer / verify metric / safest next step.

### 5. TLS VPN App Failure Analysis

**Definition and intuition:** Separate connection refused, timeout, certificate error, authentication failure, HTTP 4xx/5xx.

**Mechanism in plain terms:** TCP reachable → TLS identity checked → auth → application DB; each stage distinct.

**Industry situation:** API gives 401 bad token while network healthy; 503 indicates service issue.

**Rare/advanced case to study next:** SNI routing, ALPN negotiation, TLS 1.3, QUIC path differences.

**How you prove/disprove your first guess:** Disabling TLS validation masks problem and reduces security.

**Mini exercise:** curl -Iv https://example.com and annotate DNS/connect/TLS/status phases.

### 6. Incident Change Management Runbooks

**Definition and intuition:** Document baseline, owner, severity, rollback, timestamps, evidence and postmortem.

**Mechanism in plain terms:** Detect anomaly → triage → mitigate → validate recovery → blameless review.

**Industry situation:** Office firewall rule change unexpectedly blocks cloud payroll.

**Rare/advanced case to study next:** SLO-based alerts, error budgets and canary rollout are modern reliability skills.

**How you prove/disprove your first guess:** Fix without rollback plan may create second outage.

**Mini exercise:** Write maintenance plan with change window, tests, abort criteria, rollback.

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

- [Microsoft Learn: Windows networking and diagnostics](https://learn.microsoft.com/en-us/windows-server/networking/)
- [Wireshark User Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
