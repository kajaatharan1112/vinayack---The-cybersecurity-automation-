# 06 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **IPv4 Structure and Special Ranges:** Define, draw its workflow, give a real example and identify one important limitation.

2. **IPv6 Address Types:** Define, draw its workflow, give a real example and identify one important limitation.

3. **Public Private Static Dynamic:** Define, draw its workflow, give a real example and identify one important limitation.

4. **ARP NDP Neighbor Discovery:** Define, draw its workflow, give a real example and identify one important limitation.

5. **IPv6 Transition and Dual Stack:** Define, draw its workflow, give a real example and identify one important limitation.

6. **Address Planning IPAM and DHCP:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **IPv4 Structure and Special Ranges — Model answer:** IPv4 32 bits dotted decimal; private RFC1918 ranges; loopback 127/8; documentation 192.0.2/24. **Working:** Network prefix determines routing; host part endpoint within subnet. **Example:** 192.168.10.20/24 belongs to 192.168.10.0/24. **Nuance:** CGNAT 100.64.0.0/10 shared address space used provider side; public != fixed. **Avoid:** 192.168 address-ஐ public Internet route ஆக பயன்படுத்த முடியாது.

2. **IPv6 Address Types — Model answer:** IPv6 128 bits hex; global unicast, link-local fe80::/10, unique-local fc00::/7, multicast ff00::/8. **Working:** Hosts use NDP and SLAAC/DHCPv6; routers advertise prefixes; no broadcast in IPv6. **Example:** Phone receives IPv6 global address and link-local gateway. **Nuance:** Privacy temporary IPv6 interface addresses, stable opaque IIDs, extension headers. **Avoid:** IPv6 enabled ஆனதால் automatically Internet reachable அல்ல; firewall and routing still matter.

3. **Public Private Static Dynamic — Model answer:** Public globally routable prefix; private internally scoped; static reserved or manually assigned; dynamic leased. **Working:** DHCP assigns IPv4 network config, ISP can renew public IP; NAT remaps flow. **Example:** Home ISP public IP may change after reconnection; many clients share it. **Nuance:** A public IP can represent NAT, load balancer, VPN or proxy rather than person. **Avoid:** IP address-ஐ single user identity என்று கருதுவது தவறு.

4. **ARP NDP Neighbor Discovery — Model answer:** IPv4 ARP maps local IP→MAC; IPv6 Neighbor Discovery ICMPv6 fulfills neighbor/router discovery. **Working:** Host broadcasts ARP (IPv4) or sends solicited-node multicast (IPv6) for neighbor. **Example:** Gateway MAC learn செய்து first packet forward செய்கிறது. **Nuance:** ARP spoofing defense: DHCP snooping + dynamic ARP inspection; IPv6 RA guard requires care. **Avoid:** ARP cannot resolve remote Internet server MAC; local next-hop மட்டும்.

5. **IPv6 Transition and Dual Stack — Model answer:** Dual-stack carries IPv4+IPv6; NAT64/DNS64 helps IPv6 clients reach IPv4-only targets; 464XLAT mobile. **Working:** Client chooses candidate addresses (Happy Eyeballs); DNS AAAA/A both available. **Example:** Mobile operator IPv6 core, NAT64 for legacy server. **Nuance:** IPv6-only enterprise and provider transition aims reduce IPv4 scarcity; NAT64 breaks embedded IPv4 literals. **Avoid:** IPv4 works, IPv6 fails unnoticed due to fallback; test both address families.

6. **Address Planning IPAM and DHCP — Model answer:** An IP address plan reserves subnets for users, servers, IoT, guests and management; DHCP lease lifecycle. **Working:** Scope, reservation, exclusions and relay agents coordinate address allocations. **Example:** Office needs distinct /24 VLANs and static gateway addresses. **Nuance:** IPAM reconciles DHCP/DNS/cloud resources; overlapping CIDRs hurt mergers/peering. **Avoid:** Duplicate IP symptoms intermittent ARP changes; check DHCP scopes and reservations.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
