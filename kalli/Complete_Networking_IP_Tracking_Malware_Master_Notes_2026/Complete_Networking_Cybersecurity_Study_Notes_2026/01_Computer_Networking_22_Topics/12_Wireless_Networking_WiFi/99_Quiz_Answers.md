# 12 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **WiFi Radio Fundamentals:** Define, draw its workflow, give a real example and identify one important limitation.

2. **80211 MAC CSMA CA:** Define, draw its workflow, give a real example and identify one important limitation.

3. **WPA2 WPA3 Authentication:** Define, draw its workflow, give a real example and identify one important limitation.

4. **WiFi 6 6E 7 Features:** Define, draw its workflow, give a real example and identify one important limitation.

5. **Roaming Channels and Planning:** Define, draw its workflow, give a real example and identify one important limitation.

6. **Wireless Troubleshooting and Security:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **WiFi Radio Fundamentals — Model answer:** SSID network name, BSSID access point MAC, channels radio frequencies; RSSI signal strength. **Working:** Clients scan, authenticate/associate and transfer frames over shared medium. **Example:** Busy lecture hall Wi-Fi capacity depends airtime not just router Mbps label. **Nuance:** SNR, channel width, adjacent channel interference, DFS radar, regulatory domains. **Avoid:** Strong signal with high interference can be slower than moderate signal clean channel.

2. **80211 MAC CSMA CA — Model answer:** Wi-Fi stations listen before transmission, backoff on busy medium; hidden nodes are challenge. **Working:** ACK, retransmission and contention manage shared radio; collisions not eliminated. **Example:** Many phones upload in same room leading to contention. **Nuance:** OFDMA, MU-MIMO, BSS coloring improve dense deployments with compatible clients. **Avoid:** Wi-Fi cannot behave like full-duplex wired Ethernet under congestion.

3. **WPA2 WPA3 Authentication — Model answer:** WPA2 Personal PSK; WPA3 Personal SAE; Enterprise often 802.1X/EAP and certificates. **Working:** Handshake derives encryption keys; modern configs protect management frames. **Example:** Campus secure Wi-Fi with EAP-TLS credentials rather than shared password. **Nuance:** OWE encrypts open networks without authentication; PMF required in WPA3 contexts. **Avoid:** WPA3 does not automatically fix rogue AP and user phishing; validate certs.

4. **WiFi 6 6E 7 Features — Model answer:** Wi-Fi 6 uses OFDMA, 6E adds 6GHz where permitted; Wi-Fi 7 offers MLO, 320MHz channels, 4K QAM under conditions. **Working:** Multi-Link Operation enables compatible AP/client to use multiple links; performance depends radio/regulation. **Example:** Modern Wi-Fi 7 classroom AP may reduce delay for many users with matching clients. **Nuance:** MLO modes differ; 320MHz needs eligible 6GHz spectrum and low interference. **Avoid:** Marketing max PHY Mbps not actual throughput; client capability and backhaul constrain.

5. **Roaming Channels and Planning — Model answer:** AP coverage overlapping for seamless roaming; channel planning reduces co-channel contention. **Working:** Client chooses roaming; 802.11k/v/r can assist; controller coordinates RF policy. **Example:** Walking between classrooms keeps voice call stable with sufficient coverage. **Nuance:** Sticky clients, band steering tradeoffs, 802.11r security compatibility. **Avoid:** Too many APs at max TX power may worsen airtime congestion.

6. **Wireless Troubleshooting and Security — Model answer:** Observe association, DHCP, DNS, authentication, interference, backhaul independently. **Working:** Test local gateway loss, RSSI/SNR, retries and client roaming events. **Example:** Phone connects Wi-Fi but captive portal blocks Internet. **Nuance:** Rogue AP detection vs evil twin, wireless IDS and spectrum analytics. **Avoid:** Deauthentication management frames and captive portals create misleading state.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
