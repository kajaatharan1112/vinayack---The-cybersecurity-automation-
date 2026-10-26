# 04 — Integrated Deep-Dive Textbook: TCP IP Model Encapsulation

## Big Picture: what makes this chapter important?

Real protocol stack and packet trip through home/Internet/cloud. A TCP connection negotiates sequence numbers and acknowledges bytes; receiving all bytes does not guarantee application success. UDP sends datagrams without retransmission semantics, while QUIC builds reliable streams and encryption on UDP. Trace one flow end-to-end and watch MAC headers change at hops. Fragmentation and PMTU problems explain cases where a tiny ping works but a large encrypted response stalls.

## Architecture / Packet Path Diagram

```text
HTTP request --> TLS record --> TCP byte stream --> IP packet --> Ethernet frame
HTTP/3 --> QUIC+TLS over UDP --> IP --> link frame
```

**Interpretation:** At each routed hop, the L2 header changes. With NAT, source or destination IP/port can also change, so packet captures at two vantage points differ.

## Deep worked learning sequence

Read each lesson below as a connected narrative. For detailed individual exam Q&A, use the numbered subtopic files; for assignments do the Lab Workbook.

### 1. Four Layer TCP IP Model

**Definition and intuition:** Link, Internet, Transport, Application நான்கு logical layers; சில textbooks 5-layer model.

**Mechanism in plain terms:** Application data -> TCP segment -> IP packet -> Ethernet frame; receiver decapsulates.

**Industry situation:** DNS query UDP, server response ஆகியவை stack-இல் பயணம் செய்கின்றன.

**Rare/advanced case to study next:** Modern QUIC UDP மீது reliable secure streams தருவதால் mapping strict அல்ல.

**How you prove/disprove your first guess:** OSI மற்றும் TCP/IP one-to-one exact mapping எதிர்பார்க்காதீர்கள்.

**Mini exercise:** 4-layer table மற்றும் 7-layer mapping உருவாக்கவும்.

### 2. Ethernet IPv4 TCP Frame Anatomy

**Definition and intuition:** Ethernet dst/src MAC, EtherType; IPv4 src/dst TTL; TCP src/dst port flags sequence.

**Mechanism in plain terms:** NIC frame receives; router removes L2 header and adds next-hop L2 frame.

**Industry situation:** Laptop-to-router MAC changes hop-இல்; destination IP பெரும்பாலும் stable (NAT இல்லாவிட்டால்).

**Rare/advanced case to study next:** Checksums may appear invalid due to NIC offload on host capture.

**How you prove/disprove your first guess:** Packet capture-ல் bad checksum என்றால் physical corruption என உடனே கருத வேண்டாம்.

**Mini exercise:** Wireshark trace-ல் IP vs MAC lifetime compare செய்யவும்.

### 3. TCP Connection Lifecycle

**Definition and intuition:** Three-way handshake SYN SYN-ACK ACK; established transfer; FIN close அல்லது RST abort.

**Mechanism in plain terms:** Seq/ACK sliding window, retransmission timeouts, congestion window, receive window.

**Industry situation:** Browser opens TLS connection before HTTPS request if HTTP/1.1 over TCP.

**Rare/advanced case to study next:** SYN cookies, selective acknowledgements, BBR/CUBIC, TCP Fast Open tradeoffs.

**How you prove/disprove your first guess:** RST = reset; retransmissions = possible loss or reordering; high RTT = queue/route.

**Mini exercise:** Local server இருந்தால் curl -v http://127.0.0.1:8000 மற்றும் capture observe செய்யவும்.

### 4. UDP and QUIC

**Definition and intuition:** UDP low-overhead datagrams; QUIC adds encryption, streams, loss recovery, mobility.

**Mechanism in plain terms:** QUIC typically UDP/443, TLS1.3 handshake integrated, stream-level multiplexing.

**Industry situation:** Video app real-time media uses UDP; HTTP/3 uses QUIC.

**Rare/advanced case to study next:** 0-RTT replay risk, connection IDs, path migration, anti-amplification limit.

**How you prove/disprove your first guess:** UDP packet loss diagnostic ICMP/UDP behavior differs; no TCP handshake.

**Mini exercise:** Browser DevTools protocol column-ல் h3 vs h2 observe செய்யவும் (availability varies).

### 5. MTU MSS Fragmentation PMTUD

**Definition and intuition:** MTU maximum frame payload; TCP MSS segment payload; Path MTU smallest path.

**Mechanism in plain terms:** DF/Packet Too Big signals enable PMTUD; IPv6 routers do not fragment forwarded packets.

**Industry situation:** VPN adds overhead; 1500 MTU link tunnel carries smaller inner packets.

**Rare/advanced case to study next:** PLPMTUD avoids ICMP black holes by probing; GSO/TSO offloads confuse captures.

**How you prove/disprove your first guess:** Small ping works but large TLS stalls → suspect MTU black hole.

**Mini exercise:** ping payload sizes on own gateway with platform-specific flags; stop before disruption.

### 6. Connection States and Sockets

**Definition and intuition:** Socket 5-tuple srcIP:srcPort dstIP:dstPort protocol identifies a flow; TIME_WAIT protects re-use.

**Mechanism in plain terms:** OS associates flows with processes; NAT may rewrite srcIP:port.

**Industry situation:** Browser multiple tabs share or reuse connections; server socket LISTEN.

**Rare/advanced case to study next:** Ephemeral-port exhaustion and conntrack table saturation occur at scale.

**How you prove/disprove your first guess:** netstat output with LISTEN does not prove remote firewall path open.

**Mini exercise:** ss -tunap (Linux) or Get-NetTCPConnection (Windows) and record local vs remote.

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
- [RFC 9114 HTTP/3](https://www.rfc-editor.org/rfc/rfc9114)
