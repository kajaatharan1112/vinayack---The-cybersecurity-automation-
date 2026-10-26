# 05 — Integrated Deep-Dive Textbook: Network Devices

## Big Picture: what makes this chapter important?

Understand how packets physically and logically travel. Switches are forwarders inside broadcast domains; routers choose paths between IP subnets; firewalls make authorization decisions; reverse proxies choose backend applications. A DNS resolver does none of these forwarding roles. A physical device may implement several roles, so classify function rather than box branding. Logs and counters should align with the role you are diagnosing.

## Architecture / Packet Path Diagram

```text
Laptop --AP-- Switch --Firewall/Router-- ISP
                       |
                 Reverse proxy --> API pool --> private DB
```

**Interpretation:** L2 switch selects output using MAC learning; L3 router uses IP prefix; reverse proxy interprets HTTP routes and service health.

## Deep worked learning sequence

Read each lesson below as a connected narrative. For detailed individual exam Q&A, use the numbered subtopic files; for assignments do the Lab Workbook.

### 1. Hub Bridge Switch

**Definition and intuition:** Hub repeats bits, bridge learns MAC, switch forwards frames in LAN; hubs obsolete.

**Mechanism in plain terms:** Switch learns source MAC on arrival; floods unknown unicast until learned.

**Industry situation:** Lab switch connects PCs; same subnet traffic avoids router.

**Rare/advanced case to study next:** CAM table pressure, port security, storm control modern defensive mechanisms.

**How you prove/disprove your first guess:** Broadcast storm = loop/MAC churn; STP/LACP config inspect.

**Mini exercise:** Draw 4-PC switch MAC learning table after two exchanges.

### 2. Router and Default Gateway

**Definition and intuition:** Router joins IP networks and applies forwarding based on longest prefix.

**Mechanism in plain terms:** Host compares destination IP with own prefix; off-subnet sends to gateway MAC.

**Industry situation:** Laptop 192.168.1.20 sends to cloud IP via 192.168.1.1.

**Rare/advanced case to study next:** VRF isolates multiple routing tables on same router; hardware FIB accelerates forwarding.

**How you prove/disprove your first guess:** Wrong default gateway = local resources reachable but Internet not.

**Mini exercise:** ip route or route print trace default gateway path.

### 3. Firewall IDS IPS

**Definition and intuition:** Firewall allows/blocks; IDS alerts; IPS inline blocks suspicious packets/flows.

**Mechanism in plain terms:** Stateless rules use IP/port; stateful tracks sessions; L7 NGFW adds app identity.

**Industry situation:** Only HTTPS to public API while DB port kept private.

**Rare/advanced case to study next:** TLS encryption limits payload inspection without decryption; mTLS and SNI privacy matter.

**How you prove/disprove your first guess:** IPS false positives block valid services; use staged detection modes.

**Mini exercise:** Write inbound/outbound least-privilege rules for app + DB.

### 4. Modem ONT Access Point

**Definition and intuition:** Modem translates physical access medium, ONT terminates fibre, AP bridges wireless clients.

**Mechanism in plain terms:** ISP CPE terminates provider link; Wi-Fi AP authenticates station and bridges frames.

**Industry situation:** Home fibre ONT → router → AP → phone.

**Rare/advanced case to study next:** Wi-Fi controller/cloud management separates radio control from packet forwarding.

**How you prove/disprove your first guess:** Connected Wi-Fi with no DHCP lease is L2 association success but L3 failure.

**Mini exercise:** List actual home devices and who owns DHCP/NAT/AP roles.

### 5. Proxy Load Balancer Gateway

**Definition and intuition:** Proxy mediates requests; reverse proxy fronts services; load balancer distributes traffic; gateway policy.

**Mechanism in plain terms:** L4 balancing based on tuples, L7 balancing based on HTTP routes/header/health.

**Industry situation:** api.example.com behind reverse proxy serves three application replicas.

**Rare/advanced case to study next:** Anycast, consistent hashing, global load balancing, TLS termination tradeoffs.

**How you prove/disprove your first guess:** Health check green but end-user failing when dependent database down.

**Mini exercise:** Draw client → reverse proxy → API → DB including which node terminates TLS.

### 6. Physical Cabling Transceivers

**Definition and intuition:** Cat copper, fibre single/multimode, SFP/QSFP optics have distance/speed budgets.

**Mechanism in plain terms:** Tx/Rx optical pairing, connector cleanliness, link negotiation matter.

**Industry situation:** Campus building backbone single-mode fibre; desk copper Ethernet.

**Rare/advanced case to study next:** FEC, LAG breakout cables and DOM optical monitoring advanced skills.

**How you prove/disprove your first guess:** CRC errors suggest L1 problems even if link stays up.

**Mini exercise:** Describe speed, cable category, link distance and spare paths for example office.

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

- [IANA Protocol Registries](https://www.iana.org/protocols)
- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
