# 04 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **Four Layer TCP IP Model:** Define, draw its workflow, give a real example and identify one important limitation.

2. **Ethernet IPv4 TCP Frame Anatomy:** Define, draw its workflow, give a real example and identify one important limitation.

3. **TCP Connection Lifecycle:** Define, draw its workflow, give a real example and identify one important limitation.

4. **UDP and QUIC:** Define, draw its workflow, give a real example and identify one important limitation.

5. **MTU MSS Fragmentation PMTUD:** Define, draw its workflow, give a real example and identify one important limitation.

6. **Connection States and Sockets:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **Four Layer TCP IP Model — Model answer:** Link, Internet, Transport, Application நான்கு logical layers; சில textbooks 5-layer model. **Working:** Application data -> TCP segment -> IP packet -> Ethernet frame; receiver decapsulates. **Example:** DNS query UDP, server response ஆகியவை stack-இல் பயணம் செய்கின்றன. **Nuance:** Modern QUIC UDP மீது reliable secure streams தருவதால் mapping strict அல்ல. **Avoid:** OSI மற்றும் TCP/IP one-to-one exact mapping எதிர்பார்க்காதீர்கள்.

2. **Ethernet IPv4 TCP Frame Anatomy — Model answer:** Ethernet dst/src MAC, EtherType; IPv4 src/dst TTL; TCP src/dst port flags sequence. **Working:** NIC frame receives; router removes L2 header and adds next-hop L2 frame. **Example:** Laptop-to-router MAC changes hop-இல்; destination IP பெரும்பாலும் stable (NAT இல்லாவிட்டால்). **Nuance:** Checksums may appear invalid due to NIC offload on host capture. **Avoid:** Packet capture-ல் bad checksum என்றால் physical corruption என உடனே கருத வேண்டாம்.

3. **TCP Connection Lifecycle — Model answer:** Three-way handshake SYN SYN-ACK ACK; established transfer; FIN close அல்லது RST abort. **Working:** Seq/ACK sliding window, retransmission timeouts, congestion window, receive window. **Example:** Browser opens TLS connection before HTTPS request if HTTP/1.1 over TCP. **Nuance:** SYN cookies, selective acknowledgements, BBR/CUBIC, TCP Fast Open tradeoffs. **Avoid:** RST = reset; retransmissions = possible loss or reordering; high RTT = queue/route.

4. **UDP and QUIC — Model answer:** UDP low-overhead datagrams; QUIC adds encryption, streams, loss recovery, mobility. **Working:** QUIC typically UDP/443, TLS1.3 handshake integrated, stream-level multiplexing. **Example:** Video app real-time media uses UDP; HTTP/3 uses QUIC. **Nuance:** 0-RTT replay risk, connection IDs, path migration, anti-amplification limit. **Avoid:** UDP packet loss diagnostic ICMP/UDP behavior differs; no TCP handshake.

5. **MTU MSS Fragmentation PMTUD — Model answer:** MTU maximum frame payload; TCP MSS segment payload; Path MTU smallest path. **Working:** DF/Packet Too Big signals enable PMTUD; IPv6 routers do not fragment forwarded packets. **Example:** VPN adds overhead; 1500 MTU link tunnel carries smaller inner packets. **Nuance:** PLPMTUD avoids ICMP black holes by probing; GSO/TSO offloads confuse captures. **Avoid:** Small ping works but large TLS stalls → suspect MTU black hole.

6. **Connection States and Sockets — Model answer:** Socket 5-tuple srcIP:srcPort dstIP:dstPort protocol identifies a flow; TIME_WAIT protects re-use. **Working:** OS associates flows with processes; NAT may rewrite srcIP:port. **Example:** Browser multiple tabs share or reuse connections; server socket LISTEN. **Nuance:** Ephemeral-port exhaustion and conntrack table saturation occur at scale. **Avoid:** netstat output with LISTEN does not prove remote firewall path open.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
