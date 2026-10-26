# 21 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **QUIC HTTP3 TLS13 ECH:** Define, draw its workflow, give a real example and identify one important limitation.

2. **BGP RPKI ROV and Route Security:** Define, draw its workflow, give a real example and identify one important limitation.

3. **Segment Routing MPLS SRv6:** Define, draw its workflow, give a real example and identify one important limitation.

4. **eBPF XDP Linux Networking:** Define, draw its workflow, give a real example and identify one important limitation.

5. **SASE SSE ZTNA Identity:** Define, draw its workflow, give a real example and identify one important limitation.

6. **Post Quantum Crypto Network Migration:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **QUIC HTTP3 TLS13 ECH — Model answer:** HTTP/3 maps HTTP semantics over QUIC; TLS1.3 secures; ECH aims encrypt sensitive ClientHello parts. **Working:** QUIC UDP transport manages streams and recovery; ALPN and HTTPS RR may advertise protocol. **Example:** Mobile user swaps Wi-Fi to LTE; QUIC connection migration may preserve session. **Nuance:** 0-RTT replay constraints, anti-amplification, connection IDs, ALPN and SVCB HTTPS records. **Avoid:** QUIC traffic isn't inspectable like plaintext HTTP; troubleshooting needs endpoints/metadata.

2. **BGP RPKI ROV and Route Security — Model answer:** Route Origin Validation checks BGP prefix originated by expected ASN using ROA data. **Working:** Signed ROAs via RPKI; router marks valid/invalid/not-found and applies policy. **Example:** ISP rejects forged route-origin announcements for protected prefix. **Nuance:** ROV doesn't validate whole AS path; ASPA/BGPsec research and deployment status vary. **Avoid:** Missing ROA may be not-found, not automatically attack.

3. **Segment Routing MPLS SRv6 — Model answer:** Segment Routing steers packets along network functions/paths using segment identifiers. **Working:** SR-MPLS labels or SRv6 segments encode desired handling for traffic engineering. **Example:** Carrier steers latency-sensitive traffic around congested region. **Nuance:** TI-LFA rapid repair, SR Policies, SRv6 uSID compressed SID discussions. **Avoid:** SRv6 headers/MTU and operational interop need careful planning.

4. **eBPF XDP Linux Networking — Model answer:** eBPF verified programs run at kernel hooks to observe/filter traffic; XDP executes early on receive path. **Working:** Hooks process packet metadata; maps share state; user-space programs read telemetry. **Example:** Kubernetes Cilium uses eBPF network policy and observability. **Nuance:** CO-RE portability, verifier limits, tc vs XDP, AF_XDP, offload options. **Avoid:** Kernel-version/driver support differs; eBPF not automatically faster for every workload.

5. **SASE SSE ZTNA Identity — Model answer:** SASE integrates networking and security via distributed cloud; SSE security services; ZTNA app-granular access. **Working:** Identity/device posture gates user-to-app sessions via policy enforcement edge. **Example:** Remote staff connects protected HRMS through identity-aware service without full LAN VPN. **Nuance:** CASB, SWG, DLP, RBI, continuous access evaluation and data sovereignty. **Avoid:** Marketing SASE != complete zero trust; evaluate real auth and device policy.

6. **Post Quantum Crypto Network Migration — Model answer:** Quantum-resistant KEM/signatures are standardized; deployment needs inventory and staged testing. **Working:** Identify RSA/ECDH dependencies; assess TLS/VPN PKI; plan ML-KEM or approved algorithms carefully. **Example:** Company inventories gateways whose TLS stacks will need future PQ support. **Nuance:** NIST FIPS 203 ML-KEM, 204 ML-DSA, 205 SLH-DSA; hybrid exchanges migration. **Avoid:** Never replace working crypto with experimental home-built scheme; follow vetted implementations.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
