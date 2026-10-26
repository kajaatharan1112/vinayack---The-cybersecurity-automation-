# 05 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **Hub Bridge Switch:** Define, draw its workflow, give a real example and identify one important limitation.

2. **Router and Default Gateway:** Define, draw its workflow, give a real example and identify one important limitation.

3. **Firewall IDS IPS:** Define, draw its workflow, give a real example and identify one important limitation.

4. **Modem ONT Access Point:** Define, draw its workflow, give a real example and identify one important limitation.

5. **Proxy Load Balancer Gateway:** Define, draw its workflow, give a real example and identify one important limitation.

6. **Physical Cabling Transceivers:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **Hub Bridge Switch — Model answer:** Hub repeats bits, bridge learns MAC, switch forwards frames in LAN; hubs obsolete. **Working:** Switch learns source MAC on arrival; floods unknown unicast until learned. **Example:** Lab switch connects PCs; same subnet traffic avoids router. **Nuance:** CAM table pressure, port security, storm control modern defensive mechanisms. **Avoid:** Broadcast storm = loop/MAC churn; STP/LACP config inspect.

2. **Router and Default Gateway — Model answer:** Router joins IP networks and applies forwarding based on longest prefix. **Working:** Host compares destination IP with own prefix; off-subnet sends to gateway MAC. **Example:** Laptop 192.168.1.20 sends to cloud IP via 192.168.1.1. **Nuance:** VRF isolates multiple routing tables on same router; hardware FIB accelerates forwarding. **Avoid:** Wrong default gateway = local resources reachable but Internet not.

3. **Firewall IDS IPS — Model answer:** Firewall allows/blocks; IDS alerts; IPS inline blocks suspicious packets/flows. **Working:** Stateless rules use IP/port; stateful tracks sessions; L7 NGFW adds app identity. **Example:** Only HTTPS to public API while DB port kept private. **Nuance:** TLS encryption limits payload inspection without decryption; mTLS and SNI privacy matter. **Avoid:** IPS false positives block valid services; use staged detection modes.

4. **Modem ONT Access Point — Model answer:** Modem translates physical access medium, ONT terminates fibre, AP bridges wireless clients. **Working:** ISP CPE terminates provider link; Wi-Fi AP authenticates station and bridges frames. **Example:** Home fibre ONT → router → AP → phone. **Nuance:** Wi-Fi controller/cloud management separates radio control from packet forwarding. **Avoid:** Connected Wi-Fi with no DHCP lease is L2 association success but L3 failure.

5. **Proxy Load Balancer Gateway — Model answer:** Proxy mediates requests; reverse proxy fronts services; load balancer distributes traffic; gateway policy. **Working:** L4 balancing based on tuples, L7 balancing based on HTTP routes/header/health. **Example:** api.example.com behind reverse proxy serves three application replicas. **Nuance:** Anycast, consistent hashing, global load balancing, TLS termination tradeoffs. **Avoid:** Health check green but end-user failing when dependent database down.

6. **Physical Cabling Transceivers — Model answer:** Cat copper, fibre single/multimode, SFP/QSFP optics have distance/speed budgets. **Working:** Tx/Rx optical pairing, connector cleanliness, link negotiation matter. **Example:** Campus building backbone single-mode fibre; desk copper Ethernet. **Nuance:** FEC, LAG breakout cables and DOM optical monitoring advanced skills. **Avoid:** CRC errors suggest L1 problems even if link stays up.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
