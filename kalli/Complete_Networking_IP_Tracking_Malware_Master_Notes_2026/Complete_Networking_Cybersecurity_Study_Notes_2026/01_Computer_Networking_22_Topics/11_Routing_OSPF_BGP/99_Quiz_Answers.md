# 11 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **Routing Table Longest Prefix Match:** Define, draw its workflow, give a real example and identify one important limitation.

2. **Static Routes and Default Route:** Define, draw its workflow, give a real example and identify one important limitation.

3. **OSPF Link State Protocol:** Define, draw its workflow, give a real example and identify one important limitation.

4. **BGP Between Autonomous Systems:** Define, draw its workflow, give a real example and identify one important limitation.

5. **Routing Protocol Comparisons:** Define, draw its workflow, give a real example and identify one important limitation.

6. **Multihoming and Routing Security:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **Routing Table Longest Prefix Match — Model answer:** Router picks most specific matched network then resolves next hop/interface. **Working:** Connected, static, learned routes compete by preference/metric. **Example:** 10.0.1.55 matches 10.0.1.0/24 over default /0. **Nuance:** Policy based routing can override traditional destination lookup. **Avoid:** A route exists but return path missing causes asymmetric failure.

2. **Static Routes and Default Route — Model answer:** Static routes manually configured; default /0 used when no specific route. **Working:** Router resolves next hop and ARP/NDP on outgoing interface. **Example:** Small office default route to ISP router. **Nuance:** Floating static routes provide failover when primary dynamic route removed. **Avoid:** Blackhole from wrong next-hop; route health tests required.

3. **OSPF Link State Protocol — Model answer:** OSPF exchanges link state, computes shortest path with SPF per area. **Working:** Hello neighborship; LSDB synced; Dijkstra selects cost paths. **Example:** Enterprise core runs OSPF across many routers. **Nuance:** Area 0 backbone, summarization, LSA types, ECMP, fast reroute. **Avoid:** MTU mismatch, authentication or area mismatch block adjacency.

4. **BGP Between Autonomous Systems — Model answer:** BGP exchanges reachability and policy across ASNs; not shortest geographic path. **Working:** Neighbors advertise prefixes with attributes; local policy chooses route. **Example:** ISP A advertises its network to ISP B; Internet exchange connects many ASNs. **Nuance:** RPKI origin validation, route leaks, communities, MED/local-pref, graceful restart. **Avoid:** BGP misconfiguration can leak routes globally; peer filters & RPKI needed.

5. **Routing Protocol Comparisons — Model answer:** RIP distance-vector legacy; OSPF/IS-IS link-state; BGP path-vector; ECMP multiple next hops. **Working:** Convergence depends topology, failure detection, timers and policy. **Example:** LAN within organization OSPF; external provider interconnect BGP. **Nuance:** Segment Routing MPLS/SRv6, BFD and TI-LFA used by modern operators. **Avoid:** Don't equate hop count with delay/cost; dynamic metrics differ.

6. **Multihoming and Routing Security — Model answer:** Multiple ISPs provide resilience; secure prefix origin and avoid unintended announcements. **Working:** Edge filters announced prefixes, tracks provider health, validates origin with RPKI. **Example:** University uses two ISP uplinks; failover without inbound outage ideally. **Nuance:** BGP hijacking vs route leak vs prefix deaggregation, RPKI ROA nuances. **Avoid:** RPKI validates origin ASN, not full AS path; not total BGP security.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
