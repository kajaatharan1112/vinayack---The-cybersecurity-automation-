# Modern Industry Networking & Security Topics — Evidence Map (Oct 2026)

These are concepts and official documentation references, **not** forecasts or claims that every organization has deployed them.

| Advanced concept | Why a real engineer cares | Basis |
|---|---|---|
| QUIC + HTTP/3 | multiplex streams over UDP, connection migration, TLS integration | RFC 9000, RFC 9114 |
| DNS HTTPS/SVCB records | service binding and connection hints, privacy/performance | RFC 9460 |
| Zero Trust | user/device/workload identity rather than implicit LAN trust | NIST SP 800-207 |
| Microsegmentation | reduces lateral movement between workloads | CISA July 2025 guidance |
| eBPF & Cilium / Hubble | Linux datapath policy and observability for cloud workloads | Cilium official docs |
| Gateway API | Kubernetes role-oriented L4/L7 ingress and service traffic | Kubernetes Gateway API docs |
| Wi-Fi 7 MLO | multiple compatible wireless links, latency and capacity benefits | Wi-Fi vendor/Alliance guidance |
| IPv6-only/NAT64 | transition away from scarce IPv4 space | IPv6 architecture and provider designs |
| RPKI / BGP origin validation | reject incorrect route-origin claims | RIR routing-security guidance |
| Post-quantum cryptography | inventory TLS/PKI/VPN dependencies before migration | NIST FIPS 203 / NIST PQC |
| ATT&CK enterprise framework | organize defense by adversary behaviors, version-sensitive | MITRE ATT&CK website |
| NIST Incident Response r3 | prepare/detect/respond/recover through broader risk program | April 2025 NIST SP 800-61r3 |
| IP geo accuracy limits | provider egress does not identify a precise person/location | ARIN FAQ, APNIC Sept 2026 |

## Official sources

- [RFC 1918 Private IPv4](https://www.rfc-editor.org/rfc/rfc1918)
- [RFC 8200 IPv6](https://www.rfc-editor.org/rfc/rfc8200)
- [RFC 9293 TCP](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 9000 QUIC](https://www.rfc-editor.org/rfc/rfc9000)
- [RFC 9114 HTTP/3](https://www.rfc-editor.org/rfc/rfc9114)
- [RFC 9460 DNS SVCB/HTTPS](https://www.rfc-editor.org/rfc/rfc9460)
- [Wi-Fi Alliance (Standards and Certification)](https://www.wi-fi.org/)
- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [NIST SP 800-61 Revision 3 (April 2025)](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
- [NIST SP 800-86 Forensics](https://csrc.nist.gov/pubs/sp/800/86/final)
- [ARIN: IP record location limitations](https://www.arin.net/about/relations/law_enforcement/faq/)
- [APNIC 2026: Geolocation evidence not certainty](https://blog.apnic.net/2026/09/24/ip-geolocation-at-apnic-62-challenges-geofeeds-and-data-quality-perspectives/)
- [Kubernetes Gateway API Documentation](https://gateway-api.sigs.k8s.io/docs/introduction/)
- [Cilium eBPF Networking and Service Mesh](https://docs.cilium.io/en/stable/network/servicemesh/index.html)
- [RIPE NCC RPKI Documentation](https://www.ripe.net/manage-ips-and-asns/resource-management/certification/)
- [NIST FIPS 203 ML-KEM](https://csrc.nist.gov/pubs/fips/203/final)
- [MITRE ATT&CK Enterprise Tactics](https://attack.mitre.org/tactics/enterprise/)
- [CISA 2025 Microsegmentation Guidance](https://www.cisa.gov/news-events/alerts/2025/07/29/cisa-releases-part-one-zero-trust-microsegmentation-guidance)
- [IANA Protocol Registries](https://www.iana.org/protocols)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [Microsoft Learn: Windows networking and diagnostics](https://learn.microsoft.com/en-us/windows-server/networking/)
- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [Wireshark User Guide](https://www.wireshark.org/docs/wsug_html_chunked/)

## Terminology traps
1. **Encryption ≠ safety of the website**: a phishing website can still serve HTTPS.
2. **MAC != Internet-wide ID**: switched Ethernet MAC is local link-layer info and can be spoofed/randomized.
3. **Geolocation != exact location**: a coordinate/pin is an estimate.
4. **Port open != vulnerable**: proof needs service/auth/version/context and authorization.
5. **RPKI != BGP completely solved**: RPKI origin validation checks a subset of route correctness.
6. **Wi-Fi 7 != universal 320 MHz**: local regulations, compatible bands and clients matter.
7. **eBPF != always fast and safe by magic**: kernel/driver and verifier support are prerequisites.
8. **Zero trust != one product**: control design, identity and policy enforcement matter.
