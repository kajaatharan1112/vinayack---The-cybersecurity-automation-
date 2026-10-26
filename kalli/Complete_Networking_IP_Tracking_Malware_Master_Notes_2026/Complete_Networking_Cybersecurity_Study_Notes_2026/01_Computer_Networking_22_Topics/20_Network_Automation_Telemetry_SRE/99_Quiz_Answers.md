# 20 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **Automation Basics CLI API Python:** Define, draw its workflow, give a real example and identify one important limitation.

2. **Infrastructure as Code:** Define, draw its workflow, give a real example and identify one important limitation.

3. **Network Observability SNMP Streaming:** Define, draw its workflow, give a real example and identify one important limitation.

4. **Logging Metrics Traces Correlation:** Define, draw its workflow, give a real example and identify one important limitation.

5. **SRE SLO Alerting and Incident Review:** Define, draw its workflow, give a real example and identify one important limitation.

6. **NetDevOps CI Policy Validation:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **Automation Basics CLI API Python — Model answer:** Automate inventory checks and configuration with repeatable scripts, not ad hoc changes. **Working:** Read desired state; compare to live; propose diff; apply approved change; verify. **Example:** Script collects versions/status from 30 switches for patch planning. **Nuance:** Idempotency, GitOps, Jinja templates, dry-run, audit trails. **Avoid:** Blindly loop config commands over all switches can cause widespread outage.

2. **Infrastructure as Code — Model answer:** Terraform/OpenTofu, Ansible, declarative APIs manage network/cloud objects. **Working:** Versioned desired state → plan diff → approval → controlled rollout. **Example:** Recreate lab firewall rules and cloud subnet consistently. **Nuance:** State locking, drift detection, secret management, policy as code. **Avoid:** IaC state can contain sensitive fields; encrypt and restrict access.

3. **Network Observability SNMP Streaming — Model answer:** SNMP polls counters; streaming telemetry pushes updates; syslog reports events. **Working:** Measure interface bytes/errors, route changes, temperature and latency. **Example:** Office detects uplink drops from interface error counters. **Nuance:** OpenTelemetry traces, Prometheus counters/histograms, gNMI/OpenConfig streaming. **Avoid:** Polling intervals can miss burst failures; cardinality/memory budgets matter.

4. **Logging Metrics Traces Correlation — Model answer:** Logs describe events, metrics show trends, traces show path of one request. **Working:** Shared trace ID and synchronized UTC timestamps connect network/app/services. **Example:** User checkout slow; trace reveals DB latency vs DNS time. **Nuance:** RED/USE golden signals, SLO, exemplars and distributed tracing sampling. **Avoid:** High metric average hides p99 slowness; clocks must align.

5. **SRE SLO Alerting and Incident Review — Model answer:** SLI measures behavior, SLO target reliability, error budget limits risky releases. **Working:** Alert meaningful user impact; incident runbook; postmortem improvement loop. **Example:** Campus login availability target 99.9%, monitor 5xx and login success. **Nuance:** Burn-rate multiwindow alerts outperform simple static thresholds for SLO incidents. **Avoid:** Every packet loss alert does not mean service down; alerts must prioritize users.

6. **NetDevOps CI Policy Validation — Model answer:** Validate config changes before merging and deploying; tests simulate network intent. **Working:** Lint configs; validate routes/prefixes; evaluate ACL diff; staged rollout; auto rollback. **Example:** Change to guest VLAN policy tested in virtual lab first. **Nuance:** Digital twins, Batfish-style route verification, formal invariants and chaos engineering. **Avoid:** Successful syntax check doesn't prove reachability or security objective.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
