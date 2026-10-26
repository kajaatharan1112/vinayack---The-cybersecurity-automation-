# 11 — Integrated Deep-Dive Textbook: Routing OSPF BGP

## Big Picture: what makes this chapter important?

Forwarding decisions, dynamic routes and Internet operations. A route is not chosen by geographic distance. The local forwarding table compares destination with announced/connected prefixes and selects most-specific routes. OSPF advertises topology within a routing domain; BGP advertises paths and route policies between domains and at scale within networks. RPKI ROAs validate a prefix origin ASN, not the complete AS path or end host identity.

## Architecture / Packet Path Diagram

```text
AS64501 ---- eBGP ---- AS64502 ---- Internet
   | OSPF within enterprise |
Prefix route choice = policy + reachability + attributes
```

**Interpretation:** OSPF aims internal topology-based routing; BGP carries inter-AS reachability and policy. BGP paths are NOT guaranteed geographically shortest.

## Deep worked learning sequence

Read each lesson below as a connected narrative. For detailed individual exam Q&A, use the numbered subtopic files; for assignments do the Lab Workbook.

### 1. Routing Table Longest Prefix Match

**Definition and intuition:** Router picks most specific matched network then resolves next hop/interface.

**Mechanism in plain terms:** Connected, static, learned routes compete by preference/metric.

**Industry situation:** 10.0.1.55 matches 10.0.1.0/24 over default /0.

**Rare/advanced case to study next:** Policy based routing can override traditional destination lookup.

**How you prove/disprove your first guess:** A route exists but return path missing causes asymmetric failure.

**Mini exercise:** Write lookup results for dest 10.1.2.9 with /8, /16, /24 choices.

### 2. Static Routes and Default Route

**Definition and intuition:** Static routes manually configured; default /0 used when no specific route.

**Mechanism in plain terms:** Router resolves next hop and ARP/NDP on outgoing interface.

**Industry situation:** Small office default route to ISP router.

**Rare/advanced case to study next:** Floating static routes provide failover when primary dynamic route removed.

**How you prove/disprove your first guess:** Blackhole from wrong next-hop; route health tests required.

**Mini exercise:** Read ip route or route print; explain default and directly connected routes.

### 3. OSPF Link State Protocol

**Definition and intuition:** OSPF exchanges link state, computes shortest path with SPF per area.

**Mechanism in plain terms:** Hello neighborship; LSDB synced; Dijkstra selects cost paths.

**Industry situation:** Enterprise core runs OSPF across many routers.

**Rare/advanced case to study next:** Area 0 backbone, summarization, LSA types, ECMP, fast reroute.

**How you prove/disprove your first guess:** MTU mismatch, authentication or area mismatch block adjacency.

**Mini exercise:** List 4 OSPF adjacency prerequisites and simulated fault cause.

### 4. BGP Between Autonomous Systems

**Definition and intuition:** BGP exchanges reachability and policy across ASNs; not shortest geographic path.

**Mechanism in plain terms:** Neighbors advertise prefixes with attributes; local policy chooses route.

**Industry situation:** ISP A advertises its network to ISP B; Internet exchange connects many ASNs.

**Rare/advanced case to study next:** RPKI origin validation, route leaks, communities, MED/local-pref, graceful restart.

**How you prove/disprove your first guess:** BGP misconfiguration can leak routes globally; peer filters & RPKI needed.

**Mini exercise:** Read a public route-collector screenshot or docs; identify prefix, ASN, AS path.

### 5. Routing Protocol Comparisons

**Definition and intuition:** RIP distance-vector legacy; OSPF/IS-IS link-state; BGP path-vector; ECMP multiple next hops.

**Mechanism in plain terms:** Convergence depends topology, failure detection, timers and policy.

**Industry situation:** LAN within organization OSPF; external provider interconnect BGP.

**Rare/advanced case to study next:** Segment Routing MPLS/SRv6, BFD and TI-LFA used by modern operators.

**How you prove/disprove your first guess:** Don't equate hop count with delay/cost; dynamic metrics differ.

**Mini exercise:** Make matrix: static/OSPF/BGP use-case, scale, convergence, security.

### 6. Multihoming and Routing Security

**Definition and intuition:** Multiple ISPs provide resilience; secure prefix origin and avoid unintended announcements.

**Mechanism in plain terms:** Edge filters announced prefixes, tracks provider health, validates origin with RPKI.

**Industry situation:** University uses two ISP uplinks; failover without inbound outage ideally.

**Rare/advanced case to study next:** BGP hijacking vs route leak vs prefix deaggregation, RPKI ROA nuances.

**How you prove/disprove your first guess:** RPKI validates origin ASN, not full AS path; not total BGP security.

**Mini exercise:** Create disaster checklist for losing one ISP and validating return path.

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

- [RIPE NCC RPKI Documentation](https://www.ripe.net/manage-ips-and-asns/resource-management/certification/)
