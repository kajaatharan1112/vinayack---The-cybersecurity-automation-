# 12 — Practical Lab and Troubleshooting Workbook

## Objective

802.11 radio, safe deployment and Wi-Fi 6/6E/7.

**Rule:** Simulated / owned / explicitly authorized environment. Never attack, infect or spy on unrelated systems. Log all changes and rollback steps.

## Preparation

- Machine: Windows PowerShell / Kali Linux VM / Linux host; VM network Host-only/Internal for security experiments.
- Documentation: write exact starting IP, subnet, gateway, date/time, expected result.
- Safe observations: `ipconfig /all` (Windows), `ip a` (Linux), `ip route`, `ping 127.0.0.1`, `nslookup example.com`, own-device log viewer.
- Note: some commands require permissions/tools and could be absent. A diagram or a synthetic trace counts as successful conceptual practice when environment is unavailable.

## Tasks

| # | Learning concept | Exercise | Deliverable |
|---|---|---|---|
| 1 | WiFi Radio Fundamentals | Use OS Wi-Fi network settings to read band/channel/RSSI for own AP. | Diagram + observation + uncertainty |
| 2 | 80211 MAC CSMA CA | Draw two stations and one AP, identify hidden node scenario. | Diagram + observation + uncertainty |
| 3 | WPA2 WPA3 Authentication | Create safe campus Wi-Fi security checklist including EAP certificate validation. | Diagram + observation + uncertainty |
| 4 | WiFi 6 6E 7 Features | Compare 2.4/5/6 GHz tradeoffs signal, capacity and regulation. | Diagram + observation + uncertainty |
| 5 | Roaming Channels and Planning | Draw two AP coverage areas and plan non-overlapping channels. | Diagram + observation + uncertainty |
| 6 | Wireless Troubleshooting and Security | Collect own AP device stats (channel utilization, retries) without sniffing others. | Diagram + observation + uncertainty |

## Detailed sample walkthrough: WiFi Radio Fundamentals

**1 — Scenario:** Busy lecture hall Wi-Fi capacity depends airtime not just router Mbps label.

**2 — Predict:** SSID network name, BSSID access point MAC, channels radio frequencies; RSSI signal strength.

**3 — Explain network behaviour:** Clients scan, authenticate/associate and transfer frames over shared medium.

**4 — Advanced complication:** SNR, channel width, adjacent channel interference, DFS radar, regulatory domains.

**5 — Important limitation:** Strong signal with high interference can be slower than moderate signal clean channel.

**6 — Practical task:** Use OS Wi-Fi network settings to read band/channel/RSSI for own AP.

**7 — Debrief:** Compare what you predicted to the evidence. Include one legitimate alternative explanation and one recommended next non-invasive test.

## Marking rubric (100 points)

| Area | Marks | Target |
|---|---:|---|
| Concept explanation | 20 | Correct and understandable |
| Architecture/diagram | 20 | Endpoints, intermediate stages and protocols |
| Practical method | 20 | Safe, reproducible, authorized |
| Evidence and troubleshooting | 20 | Expected/actual and alternative hypothesis |
| Advanced insight | 10 | Correct trade-off or uncommon case |
| Ethics and limitations | 10 | No unsupported attribution, privacy and change control |

**பாதுகாப்பு:** Practical-கள் உங்களுக்குச் சொந்தமான device, தனிமைப்படுத்தப்பட்ட lab, அல்லது எழுத்துப்பூர்வமாக அனுமதி பெற்ற network-இல் மட்டுமே. Public IP பதிவு அல்லது scan உங்கள் அனுமதியைத் தானாக நிரூபிக்காது. Malware sample-ஐ everyday PC-ல் இயக்காதீர்கள்.
