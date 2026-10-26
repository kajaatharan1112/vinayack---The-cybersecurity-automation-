# 18 — Integrated Deep-Dive Textbook: NAT PAT Load Balancing QoS

## Big Picture: what makes this chapter important?

Address translation, scale and traffic guarantees. Source NAT/PAT creates a translation binding from a private tuple to a shared public address/port; return packets must match it. Load balancers decide where an application request should go based on health, policy and algorithms. QoS shapes or schedules traffic on scarce links; it does not add bandwidth. Large queues can raise latency without noticeable packet loss.

## Architecture / Packet Path Diagram

```text
LAN 192.168.1.10:51422 --> NAT 203.0.113.10:63001 --> Web 198.51.100.2:443
                        [translation table + timeout]
```

**Interpretation:** NAT rewrites addresses/ports; CDN and load balancers may split one logical service into many endpoints. Queueing and shaping determine congestion behavior.

## Deep worked learning sequence

Read each lesson below as a connected narrative. For detailed individual exam Q&A, use the numbered subtopic files; for assignments do the Lab Workbook.

### 1. NAT PAT and Connection Tracking

**Definition and intuition:** NAT rewrites addresses, PAT also ports to share external IP; table tracks flows.

**Mechanism in plain terms:** LAN client source 192.168.x:50000 becomes public:40001; return maps back.

**Industry situation:** Home 20 devices share one WAN address when browsing.

**Rare/advanced case to study next:** NAT444/CGNAT, endpoint-independent mappings, hairpin NAT, NAT64.

**How you prove/disprove your first guess:** Public IP can't uniquely identify home device/time absent NAT logs.

**Mini exercise:** Draw before/after PAT tuple with source port and time.

### 2. Port Forwarding and DMZ

**Definition and intuition:** Destination NAT maps WAN port to private service; DMZ ideally isolated network segment.

**Mechanism in plain terms:** Edge firewall restricts ingress and forwards only approved service.

**Industry situation:** Host public website through hardened reverse proxy, not direct database.

**Rare/advanced case to study next:** Reverse proxies/tunnels replace risky inbound port forwards in many settings.

**How you prove/disprove your first guess:** UPnP automatic port forwards can unintentionally expose services.

**Mini exercise:** Design secure public web + private DB network diagram.

### 3. L4 and L7 Load Balancing

**Definition and intuition:** L4 selects upstream using connection tuples; L7 routes by host/path/headers.

**Mechanism in plain terms:** Health probes remove failed nodes; algorithms round-robin/least-connections/weight.

**Industry situation:** University registration spikes spread across four servers.

**Rare/advanced case to study next:** Consistent hashing, retries can amplify load, circuit breakers, locality-aware routing.

**How you prove/disprove your first guess:** Sticky sessions vs stateless apps; health probe 200 not enough if DB down.

**Mini exercise:** Sketch request route and list health-check criteria.

### 4. CDN Anycast and Caching

**Definition and intuition:** CDN caches/static content near users; Anycast announces same address from multiple sites.

**Mechanism in plain terms:** Routing picks nearby reachable PoP; cache hit avoids origin call.

**Industry situation:** Student downloads lecture PDF served from local CDN edge.

**Rare/advanced case to study next:** Cache keys, stale-while-revalidate, request coalescing and cache poisoning defenses.

**How you prove/disprove your first guess:** Anycast closest in BGP topology not always geographically nearest.

**Mini exercise:** Draw DNS/CDN edge/origin path and cache miss process.

### 5. QoS DSCP Traffic Shaping

**Definition and intuition:** QoS chooses classes and schedules queues when link congested; cannot create bandwidth.

**Mechanism in plain terms:** Classify traffic, mark DSCP, shape egress, apply fair queueing.

**Industry situation:** VoIP latency stays low while backup runs with low priority.

**Rare/advanced case to study next:** DiffServ trust boundary, AQM ECN, CAKE/FQ-CoDel, bufferbloat mitigations.

**How you prove/disprove your first guess:** QoS marks ignored upstream; excessive strict priority starves other traffic.

**Mini exercise:** Create queue classes for voice/video/backup/regular web.

### 6. Capacity Planning and Scale

**Definition and intuition:** Plan p95 load, bandwidth peaks, concurrent connections, failure headroom.

**Mechanism in plain terms:** Measure traffic trends; model single-link failure; stress staging not production.

**Industry situation:** Exam week traffic 5× normal load; design safe reserve.

**Rare/advanced case to study next:** Little's law L=lambda*W, queueing theory, load-shed and backpressure.

**How you prove/disprove your first guess:** Average daily utilization hides 10-second microburst losses.

**Mini exercise:** Compute time to send 100MB on 100Mbps theoretical link; discuss overhead.

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

- [RFC 9293 TCP](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 9000 QUIC](https://www.rfc-editor.org/rfc/rfc9000)
