# 06 — Integrated Deep-Dive Textbook: IP Addressing IPv4 IPv6

## Big Picture: what makes this chapter important?

Addressing fundamentals with modern IPv6 practice. For 192.168.10.20/24, the /24 prefix places 192.168.10.0 through 192.168.10.255 into the same IPv4 subnet. For destination 192.168.10.50, the sender tries ARP directly; for 203.0.113.1, it ARPs the default gateway instead. IPv6 uses Neighbor Discovery, link-local addresses and router advertisements, and has no broadcast. IPv6 temporary addresses and IPv4 NAT make personal identification from an IP unreliable.

## Architecture / Packet Path Diagram

```text
IPv4: 192.168.10.20/24 --gateway 192.168.10.1--> outside
IPv6: 2001:db8:10::20/64 --link-local gateway--> outside
```

**Interpretation:** The IP prefix tells who is on-link; default route tells where to send off-link traffic. A shared public address or IPv6 temporary address is not a human identity.

## Deep worked learning sequence

Read each lesson below as a connected narrative. For detailed individual exam Q&A, use the numbered subtopic files; for assignments do the Lab Workbook.

### 1. IPv4 Structure and Special Ranges

**Definition and intuition:** IPv4 32 bits dotted decimal; private RFC1918 ranges; loopback 127/8; documentation 192.0.2/24.

**Mechanism in plain terms:** Network prefix determines routing; host part endpoint within subnet.

**Industry situation:** 192.168.10.20/24 belongs to 192.168.10.0/24.

**Rare/advanced case to study next:** CGNAT 100.64.0.0/10 shared address space used provider side; public != fixed.

**How you prove/disprove your first guess:** 192.168 address-ஐ public Internet route ஆக பயன்படுத்த முடியாது.

**Mini exercise:** ipconfig /all பார்க்கவும்; range public/private/loopback வகை எழுதவும்.

### 2. IPv6 Address Types

**Definition and intuition:** IPv6 128 bits hex; global unicast, link-local fe80::/10, unique-local fc00::/7, multicast ff00::/8.

**Mechanism in plain terms:** Hosts use NDP and SLAAC/DHCPv6; routers advertise prefixes; no broadcast in IPv6.

**Industry situation:** Phone receives IPv6 global address and link-local gateway.

**Rare/advanced case to study next:** Privacy temporary IPv6 interface addresses, stable opaque IIDs, extension headers.

**How you prove/disprove your first guess:** IPv6 enabled ஆனதால் automatically Internet reachable அல்ல; firewall and routing still matter.

**Mini exercise:** ip -6 addr அல்லது ipconfig பார்த்து IPv6 prefixes identify செய்யவும்.

### 3. Public Private Static Dynamic

**Definition and intuition:** Public globally routable prefix; private internally scoped; static reserved or manually assigned; dynamic leased.

**Mechanism in plain terms:** DHCP assigns IPv4 network config, ISP can renew public IP; NAT remaps flow.

**Industry situation:** Home ISP public IP may change after reconnection; many clients share it.

**Rare/advanced case to study next:** A public IP can represent NAT, load balancer, VPN or proxy rather than person.

**How you prove/disprove your first guess:** IP address-ஐ single user identity என்று கருதுவது தவறு.

**Mini exercise:** WAN IP மற்றும் host IP வேறுபாட்டை private vs public terms-ல் எழுதவும்.

### 4. ARP NDP Neighbor Discovery

**Definition and intuition:** IPv4 ARP maps local IP→MAC; IPv6 Neighbor Discovery ICMPv6 fulfills neighbor/router discovery.

**Mechanism in plain terms:** Host broadcasts ARP (IPv4) or sends solicited-node multicast (IPv6) for neighbor.

**Industry situation:** Gateway MAC learn செய்து first packet forward செய்கிறது.

**Rare/advanced case to study next:** ARP spoofing defense: DHCP snooping + dynamic ARP inspection; IPv6 RA guard requires care.

**How you prove/disprove your first guess:** ARP cannot resolve remote Internet server MAC; local next-hop மட்டும்.

**Mini exercise:** arp -a அல்லது ip neigh மூலம் local neighbor records பட்டியலிடவும்.

### 5. IPv6 Transition and Dual Stack

**Definition and intuition:** Dual-stack carries IPv4+IPv6; NAT64/DNS64 helps IPv6 clients reach IPv4-only targets; 464XLAT mobile.

**Mechanism in plain terms:** Client chooses candidate addresses (Happy Eyeballs); DNS AAAA/A both available.

**Industry situation:** Mobile operator IPv6 core, NAT64 for legacy server.

**Rare/advanced case to study next:** IPv6-only enterprise and provider transition aims reduce IPv4 scarcity; NAT64 breaks embedded IPv4 literals.

**How you prove/disprove your first guess:** IPv4 works, IPv6 fails unnoticed due to fallback; test both address families.

**Mini exercise:** nslookup -type=AAAA example.com and -type=A compare செய்யவும்.

### 6. Address Planning IPAM and DHCP

**Definition and intuition:** An IP address plan reserves subnets for users, servers, IoT, guests and management; DHCP lease lifecycle.

**Mechanism in plain terms:** Scope, reservation, exclusions and relay agents coordinate address allocations.

**Industry situation:** Office needs distinct /24 VLANs and static gateway addresses.

**Rare/advanced case to study next:** IPAM reconciles DHCP/DNS/cloud resources; overlapping CIDRs hurt mergers/peering.

**How you prove/disprove your first guess:** Duplicate IP symptoms intermittent ARP changes; check DHCP scopes and reservations.

**Mini exercise:** Three subnet address inventory and documentation plan எழுதவும்.

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
- [RFC 8200 IPv6](https://www.rfc-editor.org/rfc/rfc8200)
