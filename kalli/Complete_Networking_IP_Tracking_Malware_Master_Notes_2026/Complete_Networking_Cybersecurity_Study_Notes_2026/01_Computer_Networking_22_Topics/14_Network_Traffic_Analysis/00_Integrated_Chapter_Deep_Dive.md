# 14 — Integrated Deep-Dive Textbook: Network Traffic Analysis

## Big Picture: what makes this chapter important?

Packet-level observability and evidence-based diagnosis. A network operator observing TCP/443 flows sees connection timing, endpoints, volumes and flags, but not necessarily visited page or request body. A packet capture retains packets, while IPFIX/sFlow contains summaries/samples; EDR adds the device process/user connection context if access is approved. Correlate multiple sources and respect encryption, privacy and instrument limits.

## Architecture / Packet Path Diagram

```text
NIC / SPAN / Tap --> PCAP or Flow exporter --> Analyzer --> Evidence / Alert
       |                    |
    packet detail       5-tuple+bytes+time
```

**Interpretation:** Packet capture, flow logs and endpoint telemetry answer DIFFERENT questions. Encryption and sampling limit what observers can infer.

## Deep worked learning sequence

Read each lesson below as a connected narrative. For detailed individual exam Q&A, use the numbered subtopic files; for assignments do the Lab Workbook.

### 1. Packet Capture Fundamentals

**Definition and intuition:** PCAP records packets at a vantage point; capture != full network visibility.

**Mechanism in plain terms:** NIC mirror/SPAN/tap or host capture collects frames; dissectors parse layers.

**Industry situation:** Record own lab test HTTP request and inspect SYN/ACK fields.

**Rare/advanced case to study next:** Offloads, sampling, packet loss, clock drift, capture position change meaning.

**How you prove/disprove your first guess:** Promiscuous mode on switched Ethernet does not reveal all traffic everywhere.

**Mini exercise:** Open safe sample PCAP and label packet src/dst/protocol.

### 2. Capture vs Display Filters

**Definition and intuition:** Capture filter BPF reduces saved packets; display filter applies after capture.

**Mechanism in plain terms:** Capture syntax 'tcp port 443'; Wireshark display 'tcp.port == 443' different.

**Industry situation:** Store only DNS packets on own network sample for smaller file.

**Rare/advanced case to study next:** eBPF capture at kernel vs classic BPF filters conceptually differ.

**How you prove/disprove your first guess:** Using Wireshark display syntax in capture field yields parse error.

**Mini exercise:** Practice display: dns; tcp.analysis.retransmission; ip.addr == 192.0.2.10.

### 3. TCP Analysis RTT Retransmission

**Definition and intuition:** TCP stream analysis finds handshake RTT, retransmissions, zero-window, out-of-order.

**Mechanism in plain terms:** Seq/ack and ACK timing reveal transport symptoms; app time adds after transfer.

**Industry situation:** API slow from packet retransmission on lossy Wi-Fi.

**Rare/advanced case to study next:** SACK, DSACK, duplicate ACK, congestion control; capture loss can fake retransmission.

**How you prove/disprove your first guess:** A duplicate packet at SPAN doesn't always mean actual retransmission.

**Mini exercise:** Compare two example time plots: normal RTT vs spiking RTT.

### 4. DNS HTTP TLS Metadata

**Definition and intuition:** Encrypted TLS conceals HTTP payload but timing, IP, DNS (if unencrypted), handshake metadata may remain.

**Mechanism in plain terms:** Inspect query/response, status for plain HTTP; TLS handshake metadata only where visible.

**Industry situation:** DNS NXDOMAIN explains domain failure even while IP route works.

**Rare/advanced case to study next:** ECH/DoH reduce passive metadata exposure; CDN/shared IP attribution weaker.

**How you prove/disprove your first guess:** Cannot infer exact visited page from remote IP/port on modern HTTPS shared hosts.

**Mini exercise:** Record what is visible and not visible for HTTPS versus HTTP captures.

### 5. Flows NetFlow IPFIX sFlow

**Definition and intuition:** Flow telemetry summarizes src/dst/ports/bytes/time; packet captures retain packet details.

**Mechanism in plain terms:** Routers export flow records; collectors aggregate and detect outliers.

**Industry situation:** Top talkers bandwidth dashboard without recording full payload.

**Rare/advanced case to study next:** sFlow samples packets; NetFlow/IPFIX creates flow records; exporter sampling matters.

**How you prove/disprove your first guess:** High bytes to cloud CDN ≠ malware automatically; destination could be legitimate.

**Mini exercise:** Create sample 5-tuple flow row and describe investigative questions.

### 6. Network Performance Indicators

**Definition and intuition:** Measure throughput, p50/p95/p99 latency, loss, jitter, utilization, queue and retransmits.

**Mechanism in plain terms:** Correlate timestamped network/app telemetry instead of one average.

**Industry situation:** Video call p95 jitter high while download speeds fine.

**Rare/advanced case to study next:** RED/ECN, queue management and RTT decomposition; high cardinality labels risk observability.

**How you prove/disprove your first guess:** Average hides intermittent spikes; compare percentiles and error budgets.

**Mini exercise:** Write dashboard spec with latency, loss, interface errors, DNS time, TLS time.

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

- [Wireshark User Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
- [NIST SP 800-86 Forensics](https://csrc.nist.gov/pubs/sp/800/86/final)
