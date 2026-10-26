# 01 — Integrated Deep-Dive Textbook: Networking Fundamentals

## Big Picture: what makes this chapter important?

இரண்டு devices எப்படி data exchange செய்கின்றன என்பதிலிருந்து தொடங்கும் அடித்தளம். A network does not transmit “websites” directly. The browser serializes requests, the OS applies transport and internet protocols, and NIC/radio transmits symbols. The receiving device decodes them. Different failure types live at different points: a damaged cable can drop frames, an ISP route can lose connectivity, a DNS resolver can return the wrong address and an application can return an error even though transport works. Learn to locate the exact boundary that failed.

## Architecture / Packet Path Diagram

```text
Laptop/Phone --> Wi-Fi AP --> LAN switch --> Router/Firewall --> ISP --> DNS/CDN/Server
```

**Interpretation:** End-host apps generate bytes; links carry frames; routers forward packets. Network connection and working app service are distinct states.

## Deep worked learning sequence

Read each lesson below as a connected narrative. For detailed individual exam Q&A, use the numbered subtopic files; for assignments do the Lab Workbook.

### 1. What Is a Computer Network

**Definition and intuition:** Network என்பது தகவலை பரிமாற rules உடன் இணைக்கப்பட்ட devices கூட்டம்; Internet என்பது interconnected networks, ஒரு தனி computer அல்ல.

**Mechanism in plain terms:** Sender data உருவாக்குகிறது; NIC bits அனுப்புகிறது; intermediate devices forward செய்கின்றன; receiver application பொருளை மீட்டெடுக்கிறது.

**Industry situation:** University LMS site திறக்கும் laptop, campus Wi-Fi, ISP, web server ஆகியவற்றுக்கிடையில் பல networks கடக்கிறது.

**Rare/advanced case to study next:** End-to-end principle: network transport செய்வது, reliability/encryption பெரும்பாலும் endpoints இல்; middleboxes இதை சிக்கலாக்கலாம்.

**How you prove/disprove your first guess:** Wi-Fi connected என்றால் Internet works என்பதில்லை: default gateway, DNS, external reachability தனித்தனியாகச் சோதிக்கவும்.

**Mini exercise:** உங்கள் device-ல் ipconfig /all அல்லது ip a பார்க்கவும்; ஒவ்வொரு field-ன் role எழுதவும்.

### 2. LAN WAN MAN PAN Internet Intranet

**Definition and intuition:** LAN ஒரு கட்டிடம் போன்ற local area, WAN தூர இடங்கள், PAN personal devices, MAN நகரளவு; Intranet நிறுவன internal services.

**Mechanism in plain terms:** Local switch forwards frames; router links different IP networks; ISP interconnects regional and global routing domains.

**Industry situation:** கல்லூரி lab LAN, university WAN link, mobile PAN Bluetooth ஆகியவற்றை வரைபடமாக அமைக்கவும்.

**Rare/advanced case to study next:** SD-WAN overlays multiple underlays; network type-ஐ physical length மட்டும் வைத்து தீர்மானிக்க முடியாது.

**How you prove/disprove your first guess:** LAN=secure என்று நம்ப வேண்டாம்; guest devices கூட LAN-இல் தாக்குதலாகலாம்.

**Mini exercise:** உங்கள் வீடு/கல்லூரி network-க்கு LAN-WAN boundary diagram வரைந்து NAT எங்கு நடக்கிறது குறிக்கவும்.

### 3. Bandwidth Throughput Latency Jitter Loss

**Definition and intuition:** Bandwidth=capacity, Throughput=actual transferred data, Latency=delay, Jitter=delay variation, Loss=காணாமல் போன packets.

**Mechanism in plain terms:** Queue உருவானால் delay கூடும்; congested links packets drop செய்கின்றன; TCP retransmits செய்கிறது.

**Industry situation:** 100 Mbps link இருந்தும் video call freezes என்றால் upload saturation அல்லது jitter காரணமாக இருக்கலாம்.

**Rare/advanced case to study next:** Bufferbloat: பெரிய buffers loss-ஐ குறைத்தாலும் latency-ஐ மோசமாக்கும்; AQM/SQM (FQ-CoDel, CAKE) உதவும்.

**How you prove/disprove your first guess:** Speed test Mbps மட்டும் பார்க்காமல் RTT, p95 latency, jitter, packet loss ஆகியவற்றை அளவிடவும்.

**Mini exercise:** பாதுகாப்பான local ping 127.0.0.1 செய்து round-trip min/avg/max வேறுபாட்டைப் பதிவு செய்யவும்.

### 4. Client Server Peer to Peer

**Definition and intuition:** Client service கேட்கும்; server response தரும்; P2P-இல் nodes client மற்றும் server ஆக செயல்படலாம்.

**Mechanism in plain terms:** Client DNS resolve செய்கிறது; TCP/TLS/QUIC connection உருவாக்குகிறது; request-response அல்லது stream நடக்கிறது.

**Industry situation:** Browser/API server என்பது client-server; file-sharing சில networks P2P topology பயன்படுத்தும்.

**Rare/advanced case to study next:** CDN edge caches மற்றும் serverless functions user-க்கு அருகே இருப்பதால் simple one-server model துல்லியமில்லை.

**How you prove/disprove your first guess:** ஒரே server என்றால் single point of failure; multiple replicas இருந்தாலும் shared DB bottleneck இருக்கலாம்.

**Mini exercise:** Browser DevTools Network tab-ல் request/response status, duration, remote address உள்ளதா பாருங்கள்.

### 5. Packet Switching and Encapsulation

**Definition and intuition:** Message சிறு units ஆக பிரிந்து frame, packet, segment, application data என அடுக்குகளாக செல்கிறது.

**Mechanism in plain terms:** Application bytes; transport header; IP header; Ethernet frame; switch/router forwarding; reverse decapsulation.

**Industry situation:** ஒரு webpage load பல TCP/QUIC packets மற்றும் image/API requests ஆக உடைகிறது.

**Rare/advanced case to study next:** Path MTU மற்றும் fragmentation/segmentation offload காரணமாக capture-ல் packet size வேறுபடும்.

**How you prove/disprove your first guess:** Packet order எல்லா நேரமும் preserved என்று கருத வேண்டாம்; UDP ordering guarantee இல்லை.

**Mini exercise:** Wireshark sample capture-ல் Ethernet/IP/TCP/HTTP layers expand செய்து fields எழுதவும்.

### 6. Network Roles and Documentation

**Definition and intuition:** Endpoint, access switch, distribution/core, edge router, firewall, DNS, DHCP, NTP ஆகியவை network ecosystem.

**Mechanism in plain terms:** Inventory வைத்திருப்பதால் address ownership, change impact, incident response தெளிவாகும்.

**Industry situation:** College lab-இல் PC → switch → firewall/router → ISP → Internet topology.

**Rare/advanced case to study next:** Source-of-truth IPAM மற்றும் topology automation, CMDB, NetBox போன்ற tools large networks இல் முக்கியம்.

**How you prove/disprove your first guess:** Unknown uplink, undocumented VLAN changes outages ஏற்படுத்தும்; வரைபடம் version-control செய்யவும்.

**Mini exercise:** உங்கள் சொந்த network-க்கு 6-device topology, IP plan, device owner, services table உருவாக்கவும்.

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

- [RFC 1918 Private IPv4](https://www.rfc-editor.org/rfc/rfc1918)
- [Wireshark User Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
