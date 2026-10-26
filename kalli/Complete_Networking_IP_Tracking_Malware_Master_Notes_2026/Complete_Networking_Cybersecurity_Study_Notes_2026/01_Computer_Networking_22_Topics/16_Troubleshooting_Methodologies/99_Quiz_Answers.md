# 16 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **Top Down Bottom Up Divide Conquer:** Define, draw its workflow, give a real example and identify one important limitation.

2. **Windows Linux Mac Diagnostics:** Define, draw its workflow, give a real example and identify one important limitation.

3. **DNS Troubleshooting:** Define, draw its workflow, give a real example and identify one important limitation.

4. **Packet Loss Jitter Latency Diagnosis:** Define, draw its workflow, give a real example and identify one important limitation.

5. **TLS VPN App Failure Analysis:** Define, draw its workflow, give a real example and identify one important limitation.

6. **Incident Change Management Runbooks:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **Top Down Bottom Up Divide Conquer — Model answer:** Troubleshoot OSI layers: bottom-up physical first, top-down application first or middle-out at network layer. **Working:** Form hypothesis; run lowest-risk test; compare expected/actual; isolate; document fix. **Example:** Website fails: determine only one site vs all, then DNS, gateway, TLS. **Nuance:** Differential diagnosis and binary-search fault isolation reduce wasted work. **Avoid:** Changing 5 settings at once prevents knowing cause and risks making outage worse.

2. **Windows Linux Mac Diagnostics — Model answer:** ipconfig /all, Test-NetConnection, Get-NetTCPConnection on Windows; ip, ss, dig, curl on Linux. **Working:** Commands reveal local config, routes, DNS, socket state and HTTP response. **Example:** IT support remotely guides employee through non-invasive tests. **Nuance:** Namespace/container context matters: a container has its own routes/DNS. **Avoid:** Different OS commands and permissions vary; check usage before applying.

3. **DNS Troubleshooting — Model answer:** Client may cache, resolver may be unreachable, authoritative zone may be wrong. **Working:** Check local resolver config; query records; compare recursive and authoritative responses. **Example:** LMS works by IP but hostname NXDOMAIN → DNS issue. **Nuance:** Negative caching TTL, DNSSEC validation, split-horizon DNS, HTTPS records. **Avoid:** Flushing cache without diagnosis may hide root issue.

4. **Packet Loss Jitter Latency Diagnosis — Model answer:** Loss from congestion/radio/physical; RTT from propagation/queue/processing; jitter variation. **Working:** Check interface CRC/discards, ping path, throughput, utilization and recent changes. **Example:** Upload saturation causes video conference stutter. **Nuance:** Microbursts can evade 1-minute polling; fine-grained telemetry and ECN help. **Avoid:** Single traceroute hop latency spike may be ICMP rate limit not forwarding issue.

5. **TLS VPN App Failure Analysis — Model answer:** Separate connection refused, timeout, certificate error, authentication failure, HTTP 4xx/5xx. **Working:** TCP reachable → TLS identity checked → auth → application DB; each stage distinct. **Example:** API gives 401 bad token while network healthy; 503 indicates service issue. **Nuance:** SNI routing, ALPN negotiation, TLS 1.3, QUIC path differences. **Avoid:** Disabling TLS validation masks problem and reduces security.

6. **Incident Change Management Runbooks — Model answer:** Document baseline, owner, severity, rollback, timestamps, evidence and postmortem. **Working:** Detect anomaly → triage → mitigate → validate recovery → blameless review. **Example:** Office firewall rule change unexpectedly blocks cloud payroll. **Nuance:** SLO-based alerts, error budgets and canary rollout are modern reliability skills. **Avoid:** Fix without rollback plan may create second outage.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
