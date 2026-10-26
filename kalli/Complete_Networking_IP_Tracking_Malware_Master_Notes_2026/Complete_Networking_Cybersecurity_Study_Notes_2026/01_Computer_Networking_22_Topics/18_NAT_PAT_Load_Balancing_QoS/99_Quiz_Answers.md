# 18 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **NAT PAT and Connection Tracking:** Define, draw its workflow, give a real example and identify one important limitation.

2. **Port Forwarding and DMZ:** Define, draw its workflow, give a real example and identify one important limitation.

3. **L4 and L7 Load Balancing:** Define, draw its workflow, give a real example and identify one important limitation.

4. **CDN Anycast and Caching:** Define, draw its workflow, give a real example and identify one important limitation.

5. **QoS DSCP Traffic Shaping:** Define, draw its workflow, give a real example and identify one important limitation.

6. **Capacity Planning and Scale:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **NAT PAT and Connection Tracking — Model answer:** NAT rewrites addresses, PAT also ports to share external IP; table tracks flows. **Working:** LAN client source 192.168.x:50000 becomes public:40001; return maps back. **Example:** Home 20 devices share one WAN address when browsing. **Nuance:** NAT444/CGNAT, endpoint-independent mappings, hairpin NAT, NAT64. **Avoid:** Public IP can't uniquely identify home device/time absent NAT logs.

2. **Port Forwarding and DMZ — Model answer:** Destination NAT maps WAN port to private service; DMZ ideally isolated network segment. **Working:** Edge firewall restricts ingress and forwards only approved service. **Example:** Host public website through hardened reverse proxy, not direct database. **Nuance:** Reverse proxies/tunnels replace risky inbound port forwards in many settings. **Avoid:** UPnP automatic port forwards can unintentionally expose services.

3. **L4 and L7 Load Balancing — Model answer:** L4 selects upstream using connection tuples; L7 routes by host/path/headers. **Working:** Health probes remove failed nodes; algorithms round-robin/least-connections/weight. **Example:** University registration spikes spread across four servers. **Nuance:** Consistent hashing, retries can amplify load, circuit breakers, locality-aware routing. **Avoid:** Sticky sessions vs stateless apps; health probe 200 not enough if DB down.

4. **CDN Anycast and Caching — Model answer:** CDN caches/static content near users; Anycast announces same address from multiple sites. **Working:** Routing picks nearby reachable PoP; cache hit avoids origin call. **Example:** Student downloads lecture PDF served from local CDN edge. **Nuance:** Cache keys, stale-while-revalidate, request coalescing and cache poisoning defenses. **Avoid:** Anycast closest in BGP topology not always geographically nearest.

5. **QoS DSCP Traffic Shaping — Model answer:** QoS chooses classes and schedules queues when link congested; cannot create bandwidth. **Working:** Classify traffic, mark DSCP, shape egress, apply fair queueing. **Example:** VoIP latency stays low while backup runs with low priority. **Nuance:** DiffServ trust boundary, AQM ECN, CAKE/FQ-CoDel, bufferbloat mitigations. **Avoid:** QoS marks ignored upstream; excessive strict priority starves other traffic.

6. **Capacity Planning and Scale — Model answer:** Plan p95 load, bandwidth peaks, concurrent connections, failure headroom. **Working:** Measure traffic trends; model single-link failure; stress staging not production. **Example:** Exam week traffic 5× normal load; design safe reserve. **Nuance:** Little's law L=lambda*W, queueing theory, load-shed and backpressure. **Avoid:** Average daily utilization hides 10-second microburst losses.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
