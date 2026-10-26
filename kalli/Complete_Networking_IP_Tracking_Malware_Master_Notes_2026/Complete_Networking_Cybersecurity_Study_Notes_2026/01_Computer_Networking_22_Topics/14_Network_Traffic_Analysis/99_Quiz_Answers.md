# 14 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **Packet Capture Fundamentals:** Define, draw its workflow, give a real example and identify one important limitation.

2. **Capture vs Display Filters:** Define, draw its workflow, give a real example and identify one important limitation.

3. **TCP Analysis RTT Retransmission:** Define, draw its workflow, give a real example and identify one important limitation.

4. **DNS HTTP TLS Metadata:** Define, draw its workflow, give a real example and identify one important limitation.

5. **Flows NetFlow IPFIX sFlow:** Define, draw its workflow, give a real example and identify one important limitation.

6. **Network Performance Indicators:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **Packet Capture Fundamentals — Model answer:** PCAP records packets at a vantage point; capture != full network visibility. **Working:** NIC mirror/SPAN/tap or host capture collects frames; dissectors parse layers. **Example:** Record own lab test HTTP request and inspect SYN/ACK fields. **Nuance:** Offloads, sampling, packet loss, clock drift, capture position change meaning. **Avoid:** Promiscuous mode on switched Ethernet does not reveal all traffic everywhere.

2. **Capture vs Display Filters — Model answer:** Capture filter BPF reduces saved packets; display filter applies after capture. **Working:** Capture syntax 'tcp port 443'; Wireshark display 'tcp.port == 443' different. **Example:** Store only DNS packets on own network sample for smaller file. **Nuance:** eBPF capture at kernel vs classic BPF filters conceptually differ. **Avoid:** Using Wireshark display syntax in capture field yields parse error.

3. **TCP Analysis RTT Retransmission — Model answer:** TCP stream analysis finds handshake RTT, retransmissions, zero-window, out-of-order. **Working:** Seq/ack and ACK timing reveal transport symptoms; app time adds after transfer. **Example:** API slow from packet retransmission on lossy Wi-Fi. **Nuance:** SACK, DSACK, duplicate ACK, congestion control; capture loss can fake retransmission. **Avoid:** A duplicate packet at SPAN doesn't always mean actual retransmission.

4. **DNS HTTP TLS Metadata — Model answer:** Encrypted TLS conceals HTTP payload but timing, IP, DNS (if unencrypted), handshake metadata may remain. **Working:** Inspect query/response, status for plain HTTP; TLS handshake metadata only where visible. **Example:** DNS NXDOMAIN explains domain failure even while IP route works. **Nuance:** ECH/DoH reduce passive metadata exposure; CDN/shared IP attribution weaker. **Avoid:** Cannot infer exact visited page from remote IP/port on modern HTTPS shared hosts.

5. **Flows NetFlow IPFIX sFlow — Model answer:** Flow telemetry summarizes src/dst/ports/bytes/time; packet captures retain packet details. **Working:** Routers export flow records; collectors aggregate and detect outliers. **Example:** Top talkers bandwidth dashboard without recording full payload. **Nuance:** sFlow samples packets; NetFlow/IPFIX creates flow records; exporter sampling matters. **Avoid:** High bytes to cloud CDN ≠ malware automatically; destination could be legitimate.

6. **Network Performance Indicators — Model answer:** Measure throughput, p50/p95/p99 latency, loss, jitter, utilization, queue and retransmits. **Working:** Correlate timestamped network/app telemetry instead of one average. **Example:** Video call p95 jitter high while download speeds fine. **Nuance:** RED/ECN, queue management and RTT decomposition; high cardinality labels risk observability. **Avoid:** Average hides intermittent spikes; compare percentiles and error budgets.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
