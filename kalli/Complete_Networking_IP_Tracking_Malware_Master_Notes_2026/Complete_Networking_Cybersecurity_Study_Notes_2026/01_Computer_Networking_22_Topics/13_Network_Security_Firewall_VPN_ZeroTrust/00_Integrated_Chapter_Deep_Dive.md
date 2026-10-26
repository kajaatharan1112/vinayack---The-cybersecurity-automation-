# 13 — Integrated Deep-Dive Textbook: Network Security Firewall VPN ZeroTrust

## Big Picture: what makes this chapter important?

Identity-centric protection and secure access. A firewall rule may allow a packet yet an identity policy may deny the user. Zero Trust requires verifying identity and posture for the requested resource instead of assuming LAN location is safe. Workload microsegmentation reduces lateral movement, but implementation needs clear application dependency maps: deny-all without mapping DNS, identity and database flows can break valid work.

## Architecture / Packet Path Diagram

```text
User+Managed device --IdP/MFA--> Policy Engine --> App
                                        |
                              Segmented service network
```

**Interpretation:** Zero Trust moves access decisions toward user/device/resource context. Firewalls and identity controls work together rather than replacing one another.

## Deep worked learning sequence

Read each lesson below as a connected narrative. For detailed individual exam Q&A, use the numbered subtopic files; for assignments do the Lab Workbook.

### 1. Threat Model CIA and Defence in Depth

**Definition and intuition:** Confidentiality, Integrity, Availability guide choices; threat model assets and attack paths.

**Mechanism in plain terms:** Inventory critical data; identify threats; choose preventive/detective/recovery controls.

**Industry situation:** Payroll DB needs encrypt, role checks, backup, incident logging.

**Rare/advanced case to study next:** Attack surface management and threat-informed defence connect technique to control.

**How you prove/disprove your first guess:** Single firewall does not solve stolen credentials or insecure apps.

**Mini exercise:** Write simple data-flow diagram for campus LMS and identify 3 risks.

### 2. Firewalls ACL Stateful NGFW

**Definition and intuition:** ACL filters packets by tuple; stateful firewall tracks permitted connection; NGFW uses application signals.

**Mechanism in plain terms:** Default deny with specific allowlist reduces exposure.

**Industry situation:** Only app servers may reach DB port; guest subnet denied.

**Rare/advanced case to study next:** Identity-aware policy, policy shadowing, TLS inspection legal/privacy tradeoffs.

**How you prove/disprove your first guess:** Rule ordered top-down; broad earlier allow makes later deny ineffective.

**Mini exercise:** Build five-rule matrix for DMZ, staff, guest, DB, management.

### 3. VPN IPsec WireGuard ZTNA

**Definition and intuition:** VPN creates encrypted tunnel, often broad network access; ZTNA grants app-level access by identity/device.

**Mechanism in plain terms:** Tunnel keys established; encapsulated traffic routed over public Internet.

**Industry situation:** Remote employee securely reaches internal HR dashboard.

**Rare/advanced case to study next:** Split tunnel vs full tunnel, IPsec IKEv2, WireGuard cryptokey routing, MTU.

**How you prove/disprove your first guess:** VPN connected does not mean DNS routes right; identity revocation and posture matter.

**Mini exercise:** Diagram remote laptop → tunnel endpoint → permitted internal service.

### 4. Zero Trust Architecture

**Definition and intuition:** Trust isn't granted merely because device sits on LAN; authenticate/authorize per resource and context.

**Mechanism in plain terms:** Identity, device posture, policy enforcement point and continuous monitoring work together.

**Industry situation:** Contractor gets access to ticket app not full subnet.

**Rare/advanced case to study next:** CISA microsegmentation, NIST SP800-207, workload identities, continuous evaluation.

**How you prove/disprove your first guess:** Zero trust isn't one product or turning off perimeter; network and identity layers cooperate.

**Mini exercise:** Write policy: HR staff managed device, MFA, only payroll service, log access.

### 5. TLS PKI Certificates mTLS

**Definition and intuition:** TLS protects connections and uses certificates/keys to authenticate; mTLS verifies both parties.

**Mechanism in plain terms:** Certificate chain to trust anchor, hostname match, expiry/revocation checks.

**Industry situation:** API gateway HTTPS; internal service mesh mTLS service identity.

**Rare/advanced case to study next:** Certificate Transparency, automated ACME, short-lived certs, post-quantum migration planning.

**How you prove/disprove your first guess:** Expired or wrong-hostname cert causes browser block; don't simply disable verification.

**Mini exercise:** Open browser certificate details of trusted sample site, identify issuer and validity.

### 6. IDS IPS SIEM SOC

**Definition and intuition:** IDS detects signatures/anomalies; IPS inline blocks; SIEM correlates logs; SOC investigates.

**Mechanism in plain terms:** Data from endpoints/network/cloud → normalized events → rules → alert → triage.

**Industry situation:** Repeated failed logins + impossible travel triggers analyst review.

**Rare/advanced case to study next:** EDR/XDR vs NDR, UEBA, detection engineering and false-positive management.

**How you prove/disprove your first guess:** One alert ≠ breach; require timestamps, asset context and corroboration.

**Mini exercise:** Write detection rule pseudocode for abnormal failed logins with threshold + exceptions.

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

- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [CISA 2025 Microsegmentation Guidance](https://www.cisa.gov/news-events/alerts/2025/07/29/cisa-releases-part-one-zero-trust-microsegmentation-guidance)
- [NIST FIPS 203 ML-KEM](https://csrc.nist.gov/pubs/fips/203/final)
