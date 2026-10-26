# 12 — Integrated Deep-Dive Textbook: Wireless Networking WiFi

## Big Picture: what makes this chapter important?

802.11 radio, safe deployment and Wi-Fi 6/6E/7. Radio airtime is shared; every retry consumes capacity for other clients. Band choice trades coverage, interference and capacity: 2.4 GHz often covers farther but has fewer clean channels, while 5/6 GHz can support wider channels where permitted. Wi-Fi 7 Multi-Link Operation can use multiple compatible radio links but cannot bypass inadequate backhaul, bad RF planning or client limitations.

## Architecture / Packet Path Diagram

```text
Client 2.4/5/6 GHz ))) AP --PoE switch --LAN --Internet
RF airtime shared by all stations
```

**Interpretation:** Wi-Fi throughput depends on airtime, interference, client quality, radio width and backhaul, not only access point marketing speeds.

## Deep worked learning sequence

Read each lesson below as a connected narrative. For detailed individual exam Q&A, use the numbered subtopic files; for assignments do the Lab Workbook.

### 1. WiFi Radio Fundamentals

**Definition and intuition:** SSID network name, BSSID access point MAC, channels radio frequencies; RSSI signal strength.

**Mechanism in plain terms:** Clients scan, authenticate/associate and transfer frames over shared medium.

**Industry situation:** Busy lecture hall Wi-Fi capacity depends airtime not just router Mbps label.

**Rare/advanced case to study next:** SNR, channel width, adjacent channel interference, DFS radar, regulatory domains.

**How you prove/disprove your first guess:** Strong signal with high interference can be slower than moderate signal clean channel.

**Mini exercise:** Use OS Wi-Fi network settings to read band/channel/RSSI for own AP.

### 2. 80211 MAC CSMA CA

**Definition and intuition:** Wi-Fi stations listen before transmission, backoff on busy medium; hidden nodes are challenge.

**Mechanism in plain terms:** ACK, retransmission and contention manage shared radio; collisions not eliminated.

**Industry situation:** Many phones upload in same room leading to contention.

**Rare/advanced case to study next:** OFDMA, MU-MIMO, BSS coloring improve dense deployments with compatible clients.

**How you prove/disprove your first guess:** Wi-Fi cannot behave like full-duplex wired Ethernet under congestion.

**Mini exercise:** Draw two stations and one AP, identify hidden node scenario.

### 3. WPA2 WPA3 Authentication

**Definition and intuition:** WPA2 Personal PSK; WPA3 Personal SAE; Enterprise often 802.1X/EAP and certificates.

**Mechanism in plain terms:** Handshake derives encryption keys; modern configs protect management frames.

**Industry situation:** Campus secure Wi-Fi with EAP-TLS credentials rather than shared password.

**Rare/advanced case to study next:** OWE encrypts open networks without authentication; PMF required in WPA3 contexts.

**How you prove/disprove your first guess:** WPA3 does not automatically fix rogue AP and user phishing; validate certs.

**Mini exercise:** Create safe campus Wi-Fi security checklist including EAP certificate validation.

### 4. WiFi 6 6E 7 Features

**Definition and intuition:** Wi-Fi 6 uses OFDMA, 6E adds 6GHz where permitted; Wi-Fi 7 offers MLO, 320MHz channels, 4K QAM under conditions.

**Mechanism in plain terms:** Multi-Link Operation enables compatible AP/client to use multiple links; performance depends radio/regulation.

**Industry situation:** Modern Wi-Fi 7 classroom AP may reduce delay for many users with matching clients.

**Rare/advanced case to study next:** MLO modes differ; 320MHz needs eligible 6GHz spectrum and low interference.

**How you prove/disprove your first guess:** Marketing max PHY Mbps not actual throughput; client capability and backhaul constrain.

**Mini exercise:** Compare 2.4/5/6 GHz tradeoffs signal, capacity and regulation.

### 5. Roaming Channels and Planning

**Definition and intuition:** AP coverage overlapping for seamless roaming; channel planning reduces co-channel contention.

**Mechanism in plain terms:** Client chooses roaming; 802.11k/v/r can assist; controller coordinates RF policy.

**Industry situation:** Walking between classrooms keeps voice call stable with sufficient coverage.

**Rare/advanced case to study next:** Sticky clients, band steering tradeoffs, 802.11r security compatibility.

**How you prove/disprove your first guess:** Too many APs at max TX power may worsen airtime congestion.

**Mini exercise:** Draw two AP coverage areas and plan non-overlapping channels.

### 6. Wireless Troubleshooting and Security

**Definition and intuition:** Observe association, DHCP, DNS, authentication, interference, backhaul independently.

**Mechanism in plain terms:** Test local gateway loss, RSSI/SNR, retries and client roaming events.

**Industry situation:** Phone connects Wi-Fi but captive portal blocks Internet.

**Rare/advanced case to study next:** Rogue AP detection vs evil twin, wireless IDS and spectrum analytics.

**How you prove/disprove your first guess:** Deauthentication management frames and captive portals create misleading state.

**Mini exercise:** Collect own AP device stats (channel utilization, retries) without sniffing others.

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

- [Wi-Fi Alliance (Standards and Certification)](https://www.wi-fi.org/)
