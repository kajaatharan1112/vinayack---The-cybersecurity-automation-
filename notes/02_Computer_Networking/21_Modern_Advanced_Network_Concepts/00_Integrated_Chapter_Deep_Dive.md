# 21 — Integrated Deep-Dive Textbook: Modern Advanced Network Concepts

## Big Picture: what makes this chapter important?

Less-common yet increasingly useful production-grade concepts. HTTP/3 and QUIC streamline transport and secure session behavior for modern web applications; DNS HTTPS RR can advertise supported service parameters. Route-origin validation protects BGP against one class of origin spoofing. eBPF/XDP enables programmable observation and filtering on supported Linux systems. Post-quantum migration is a crypto inventory and interoperability program, not a single configuration flag.

## Architecture / Packet Path Diagram

```text
Browser --HTTPS RR/ALPN--> HTTP/3(QUIC/TLS1.3) --> Edge
Data center --> eBPF/XDP + EVPN/BGP-RPKI + workload identity
```

**Interpretation:** Modern features coexist with older networks. Adoption is conditional on client/server versions, DNS, hardware, policies and regulations.

## Deep worked learning sequence

Read each lesson below as a connected narrative. For detailed individual exam Q&A, use the numbered subtopic files; for assignments do the Lab Workbook.

### 1. QUIC HTTP3 TLS13 ECH

**Definition and intuition:** HTTP/3 maps HTTP semantics over QUIC; TLS1.3 secures; ECH aims encrypt sensitive ClientHello parts.

**Mechanism in plain terms:** QUIC UDP transport manages streams and recovery; ALPN and HTTPS RR may advertise protocol.

**Industry situation:** Mobile user swaps Wi-Fi to LTE; QUIC connection migration may preserve session.

**Rare/advanced case to study next:** 0-RTT replay constraints, anti-amplification, connection IDs, ALPN and SVCB HTTPS records.

**How you prove/disprove your first guess:** QUIC traffic isn't inspectable like plaintext HTTP; troubleshooting needs endpoints/metadata.

**Mini exercise:** Compare h2 over TCP/TLS with h3 over QUIC in browser DevTools where supported.

### 2. BGP RPKI ROV and Route Security

**Definition and intuition:** Route Origin Validation checks BGP prefix originated by expected ASN using ROA data.

**Mechanism in plain terms:** Signed ROAs via RPKI; router marks valid/invalid/not-found and applies policy.

**Industry situation:** ISP rejects forged route-origin announcements for protected prefix.

**Rare/advanced case to study next:** ROV doesn't validate whole AS path; ASPA/BGPsec research and deployment status vary.

**How you prove/disprove your first guess:** Missing ROA may be not-found, not automatically attack.

**Mini exercise:** Create conceptual ROA prefix, maxLength, origin-ASN and validation examples.

### 3. Segment Routing MPLS SRv6

**Definition and intuition:** Segment Routing steers packets along network functions/paths using segment identifiers.

**Mechanism in plain terms:** SR-MPLS labels or SRv6 segments encode desired handling for traffic engineering.

**Industry situation:** Carrier steers latency-sensitive traffic around congested region.

**Rare/advanced case to study next:** TI-LFA rapid repair, SR Policies, SRv6 uSID compressed SID discussions.

**How you prove/disprove your first guess:** SRv6 headers/MTU and operational interop need careful planning.

**Mini exercise:** Draw preferred route vs backup route using segments.

### 4. eBPF XDP Linux Networking

**Definition and intuition:** eBPF verified programs run at kernel hooks to observe/filter traffic; XDP executes early on receive path.

**Mechanism in plain terms:** Hooks process packet metadata; maps share state; user-space programs read telemetry.

**Industry situation:** Kubernetes Cilium uses eBPF network policy and observability.

**Rare/advanced case to study next:** CO-RE portability, verifier limits, tc vs XDP, AF_XDP, offload options.

**How you prove/disprove your first guess:** Kernel-version/driver support differs; eBPF not automatically faster for every workload.

**Mini exercise:** Read-only lab: list concept hooks, explain what policy check would do.

### 5. SASE SSE ZTNA Identity

**Definition and intuition:** SASE integrates networking and security via distributed cloud; SSE security services; ZTNA app-granular access.

**Mechanism in plain terms:** Identity/device posture gates user-to-app sessions via policy enforcement edge.

**Industry situation:** Remote staff connects protected HRMS through identity-aware service without full LAN VPN.

**Rare/advanced case to study next:** CASB, SWG, DLP, RBI, continuous access evaluation and data sovereignty.

**How you prove/disprove your first guess:** Marketing SASE != complete zero trust; evaluate real auth and device policy.

**Mini exercise:** Build comparison table MPLS WAN/VPN/SD-WAN/SASE for branch + remote employees.

### 6. Post Quantum Crypto Network Migration

**Definition and intuition:** Quantum-resistant KEM/signatures are standardized; deployment needs inventory and staged testing.

**Mechanism in plain terms:** Identify RSA/ECDH dependencies; assess TLS/VPN PKI; plan ML-KEM or approved algorithms carefully.

**Industry situation:** Company inventories gateways whose TLS stacks will need future PQ support.

**Rare/advanced case to study next:** NIST FIPS 203 ML-KEM, 204 ML-DSA, 205 SLH-DSA; hybrid exchanges migration.

**How you prove/disprove your first guess:** Never replace working crypto with experimental home-built scheme; follow vetted implementations.

**Mini exercise:** Draft asset inventory fields protocol, cert lifetime, crypto algorithm, upgrade owner.

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

- [RFC 9000 QUIC](https://www.rfc-editor.org/rfc/rfc9000)
- [RFC 9114 HTTP/3](https://www.rfc-editor.org/rfc/rfc9114)
- [RFC 9460 DNS SVCB/HTTPS](https://www.rfc-editor.org/rfc/rfc9460)
- [RIPE NCC RPKI Documentation](https://www.ripe.net/manage-ips-and-asns/resource-management/certification/)
- [NIST FIPS 203 ML-KEM](https://csrc.nist.gov/pubs/fips/203/final)
