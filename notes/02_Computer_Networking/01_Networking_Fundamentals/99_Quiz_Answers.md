# 01 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **What Is a Computer Network:** Define, draw its workflow, give a real example and identify one important limitation.

2. **LAN WAN MAN PAN Internet Intranet:** Define, draw its workflow, give a real example and identify one important limitation.

3. **Bandwidth Throughput Latency Jitter Loss:** Define, draw its workflow, give a real example and identify one important limitation.

4. **Client Server Peer to Peer:** Define, draw its workflow, give a real example and identify one important limitation.

5. **Packet Switching and Encapsulation:** Define, draw its workflow, give a real example and identify one important limitation.

6. **Network Roles and Documentation:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **What Is a Computer Network — Model answer:** Network என்பது தகவலை பரிமாற rules உடன் இணைக்கப்பட்ட devices கூட்டம்; Internet என்பது interconnected networks, ஒரு தனி computer அல்ல. **Working:** Sender data உருவாக்குகிறது; NIC bits அனுப்புகிறது; intermediate devices forward செய்கின்றன; receiver application பொருளை மீட்டெடுக்கிறது. **Example:** University LMS site திறக்கும் laptop, campus Wi-Fi, ISP, web server ஆகியவற்றுக்கிடையில் பல networks கடக்கிறது. **Nuance:** End-to-end principle: network transport செய்வது, reliability/encryption பெரும்பாலும் endpoints இல்; middleboxes இதை சிக்கலாக்கலாம். **Avoid:** Wi-Fi connected என்றால் Internet works என்பதில்லை: default gateway, DNS, external reachability தனித்தனியாகச் சோதிக்கவும்.

2. **LAN WAN MAN PAN Internet Intranet — Model answer:** LAN ஒரு கட்டிடம் போன்ற local area, WAN தூர இடங்கள், PAN personal devices, MAN நகரளவு; Intranet நிறுவன internal services. **Working:** Local switch forwards frames; router links different IP networks; ISP interconnects regional and global routing domains. **Example:** கல்லூரி lab LAN, university WAN link, mobile PAN Bluetooth ஆகியவற்றை வரைபடமாக அமைக்கவும். **Nuance:** SD-WAN overlays multiple underlays; network type-ஐ physical length மட்டும் வைத்து தீர்மானிக்க முடியாது. **Avoid:** LAN=secure என்று நம்ப வேண்டாம்; guest devices கூட LAN-இல் தாக்குதலாகலாம்.

3. **Bandwidth Throughput Latency Jitter Loss — Model answer:** Bandwidth=capacity, Throughput=actual transferred data, Latency=delay, Jitter=delay variation, Loss=காணாமல் போன packets. **Working:** Queue உருவானால் delay கூடும்; congested links packets drop செய்கின்றன; TCP retransmits செய்கிறது. **Example:** 100 Mbps link இருந்தும் video call freezes என்றால் upload saturation அல்லது jitter காரணமாக இருக்கலாம். **Nuance:** Bufferbloat: பெரிய buffers loss-ஐ குறைத்தாலும் latency-ஐ மோசமாக்கும்; AQM/SQM (FQ-CoDel, CAKE) உதவும். **Avoid:** Speed test Mbps மட்டும் பார்க்காமல் RTT, p95 latency, jitter, packet loss ஆகியவற்றை அளவிடவும்.

4. **Client Server Peer to Peer — Model answer:** Client service கேட்கும்; server response தரும்; P2P-இல் nodes client மற்றும் server ஆக செயல்படலாம். **Working:** Client DNS resolve செய்கிறது; TCP/TLS/QUIC connection உருவாக்குகிறது; request-response அல்லது stream நடக்கிறது. **Example:** Browser/API server என்பது client-server; file-sharing சில networks P2P topology பயன்படுத்தும். **Nuance:** CDN edge caches மற்றும் serverless functions user-க்கு அருகே இருப்பதால் simple one-server model துல்லியமில்லை. **Avoid:** ஒரே server என்றால் single point of failure; multiple replicas இருந்தாலும் shared DB bottleneck இருக்கலாம்.

5. **Packet Switching and Encapsulation — Model answer:** Message சிறு units ஆக பிரிந்து frame, packet, segment, application data என அடுக்குகளாக செல்கிறது. **Working:** Application bytes; transport header; IP header; Ethernet frame; switch/router forwarding; reverse decapsulation. **Example:** ஒரு webpage load பல TCP/QUIC packets மற்றும் image/API requests ஆக உடைகிறது. **Nuance:** Path MTU மற்றும் fragmentation/segmentation offload காரணமாக capture-ல் packet size வேறுபடும். **Avoid:** Packet order எல்லா நேரமும் preserved என்று கருத வேண்டாம்; UDP ordering guarantee இல்லை.

6. **Network Roles and Documentation — Model answer:** Endpoint, access switch, distribution/core, edge router, firewall, DNS, DHCP, NTP ஆகியவை network ecosystem. **Working:** Inventory வைத்திருப்பதால் address ownership, change impact, incident response தெளிவாகும். **Example:** College lab-இல் PC → switch → firewall/router → ISP → Internet topology. **Nuance:** Source-of-truth IPAM மற்றும் topology automation, CMDB, NetBox போன்ற tools large networks இல் முக்கியம். **Avoid:** Unknown uplink, undocumented VLAN changes outages ஏற்படுத்தும்; வரைபடம் version-control செய்யவும்.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
