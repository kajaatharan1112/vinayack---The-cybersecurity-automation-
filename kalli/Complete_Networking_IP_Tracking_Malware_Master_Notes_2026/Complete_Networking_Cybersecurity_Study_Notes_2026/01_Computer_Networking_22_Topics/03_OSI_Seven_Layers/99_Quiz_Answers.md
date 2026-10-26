# 03 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **Layer 1 Physical:** Define, draw its workflow, give a real example and identify one important limitation.

2. **Layer 2 Data Link:** Define, draw its workflow, give a real example and identify one important limitation.

3. **Layer 3 Network:** Define, draw its workflow, give a real example and identify one important limitation.

4. **Layer 4 Transport:** Define, draw its workflow, give a real example and identify one important limitation.

5. **Layers 5 and 6 Session Presentation:** Define, draw its workflow, give a real example and identify one important limitation.

6. **Layer 7 Application:** Define, draw its workflow, give a real example and identify one important limitation.

7. **Cross Layer Troubleshooting:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **Layer 1 Physical — Model answer:** Layer 1 bits மற்றும் signal (copper, fibre, radio), voltage/light spectrum கவனிக்கிறது. **Working:** Transceiver encodes bit stream; cable/optic carries signal; receiver interprets. **Example:** Bad cable அல்லது weak Wi-Fi RSSI காரணமாக errors. **Nuance:** Optical power budgets, FEC, PAM4, auto-negotiation ஆகியவை uncommon ஆனால் production முக்கியம். **Avoid:** Link down என்றால் முதலில் cable, port, optics, duplex/speed negotiation பாருங்கள்.

2. **Layer 2 Data Link — Model answer:** Ethernet/Wi-Fi frames, MAC addresses, switching, VLAN ஆகியவை L2. **Working:** Switch MAC learning மூலம் same broadcast domain-ல் frames deliver செய்கிறது. **Example:** ARP broadcast local LAN-இல்; Internet முழுவதும் broadcast ஆகாது. **Nuance:** 802.1Q tagging, LACP, STP; overlay fabric-இல் L2 adjacency virtualise ஆகலாம். **Avoid:** VLAN mismatch L2 connectivity cut; collision domain மற்றும் broadcast domain வேறு.

3. **Layer 3 Network — Model answer:** IP address மற்றும் router hop-by-hop packet forwarding Layer 3. **Working:** Routing table longest prefix match செய்கிறது; TTL/Hop Limit decrements. **Example:** 192.168.1.5 இருந்து 8.8.8.8 செல்ல router தேவை. **Nuance:** ECMP, segment routing, policy-based routing, IPv6 flow labels advanced L3. **Avoid:** Default route இல்லாவிட்டால் local LAN works, remote network fails.

4. **Layer 4 Transport — Model answer:** TCP/UDP endpoint ports மூலம் process-to-process communication; TCP reliability, UDP minimal transport. **Working:** TCP seq/ack/retransmission/congestion control; UDP datagrams independent. **Example:** HTTPS over TCP/443 அல்லது QUIC over UDP/443. **Nuance:** QUIC transport functionality UDP மேலே user-space இல்; OSI categorization approximate. **Avoid:** Open port என்றால் app healthy என்று அர்த்தமில்லை; handshake மட்டும் போதாது.

5. **Layers 5 and 6 Session Presentation — Model answer:** Session continuity, data representation, encoding, compression, encryption conceptual functions; Internet stacks-இல் boundary neat அல்ல. **Working:** TLS session/security, serialization JSON/Protobuf, charset transformations application அருகில். **Example:** Application sends UTF-8 JSON via TLS to API. **Nuance:** OSI 5/6 discrete hardware modules என்று நினைக்க வேண்டாம்; TLS layering context-dependent. **Avoid:** Decode failure network outage போல தோன்றலாம்; bytes arrive ஆனாலும் protocol mismatch இருக்கலாம்.

6. **Layer 7 Application — Model answer:** Human application protocols HTTP, DNS, SMTP, SSH semantics. **Working:** Client requests actions; server parses fields and applies auth/business logic. **Example:** Web browser GET /courses sends HTTP request; response 200 அல்லது 404. **Nuance:** gRPC over HTTP/2, WebSockets, GraphQL protocols மற்றும் application APIs. **Avoid:** 200 OK response இருந்தும் wrong data என்றால் L7 bug; packet loss அல்ல.

7. **Cross Layer Troubleshooting — Model answer:** Layering is troubleshooting model, not exact real implementation blueprint. **Working:** Test interface then gateway then route then DNS then port/TLS then app. **Example:** App fail: ping gateway fine, DNS NXDOMAIN → DNS layer issue. **Nuance:** Encrypted DNS, tunnels, proxies layers-ஐ blur செய்கின்றன. **Avoid:** Ping failure = host down என்று conclusively முடிவு செய்ய முடியாது; ICMP blocked இருக்கலாம்.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
