# 13 — University Exam Questions with Answers

## Part A — Long/Short Answer Questions

1. **Threat Model CIA and Defence in Depth:** Define, draw its workflow, give a real example and identify one important limitation.

2. **Firewalls ACL Stateful NGFW:** Define, draw its workflow, give a real example and identify one important limitation.

3. **VPN IPsec WireGuard ZTNA:** Define, draw its workflow, give a real example and identify one important limitation.

4. **Zero Trust Architecture:** Define, draw its workflow, give a real example and identify one important limitation.

5. **TLS PKI Certificates mTLS:** Define, draw its workflow, give a real example and identify one important limitation.

6. **IDS IPS SIEM SOC:** Define, draw its workflow, give a real example and identify one important limitation.

## Part B — Suggested Answer Key

1. **Threat Model CIA and Defence in Depth — Model answer:** Confidentiality, Integrity, Availability guide choices; threat model assets and attack paths. **Working:** Inventory critical data; identify threats; choose preventive/detective/recovery controls. **Example:** Payroll DB needs encrypt, role checks, backup, incident logging. **Nuance:** Attack surface management and threat-informed defence connect technique to control. **Avoid:** Single firewall does not solve stolen credentials or insecure apps.

2. **Firewalls ACL Stateful NGFW — Model answer:** ACL filters packets by tuple; stateful firewall tracks permitted connection; NGFW uses application signals. **Working:** Default deny with specific allowlist reduces exposure. **Example:** Only app servers may reach DB port; guest subnet denied. **Nuance:** Identity-aware policy, policy shadowing, TLS inspection legal/privacy tradeoffs. **Avoid:** Rule ordered top-down; broad earlier allow makes later deny ineffective.

3. **VPN IPsec WireGuard ZTNA — Model answer:** VPN creates encrypted tunnel, often broad network access; ZTNA grants app-level access by identity/device. **Working:** Tunnel keys established; encapsulated traffic routed over public Internet. **Example:** Remote employee securely reaches internal HR dashboard. **Nuance:** Split tunnel vs full tunnel, IPsec IKEv2, WireGuard cryptokey routing, MTU. **Avoid:** VPN connected does not mean DNS routes right; identity revocation and posture matter.

4. **Zero Trust Architecture — Model answer:** Trust isn't granted merely because device sits on LAN; authenticate/authorize per resource and context. **Working:** Identity, device posture, policy enforcement point and continuous monitoring work together. **Example:** Contractor gets access to ticket app not full subnet. **Nuance:** CISA microsegmentation, NIST SP800-207, workload identities, continuous evaluation. **Avoid:** Zero trust isn't one product or turning off perimeter; network and identity layers cooperate.

5. **TLS PKI Certificates mTLS — Model answer:** TLS protects connections and uses certificates/keys to authenticate; mTLS verifies both parties. **Working:** Certificate chain to trust anchor, hostname match, expiry/revocation checks. **Example:** API gateway HTTPS; internal service mesh mTLS service identity. **Nuance:** Certificate Transparency, automated ACME, short-lived certs, post-quantum migration planning. **Avoid:** Expired or wrong-hostname cert causes browser block; don't simply disable verification.

6. **IDS IPS SIEM SOC — Model answer:** IDS detects signatures/anomalies; IPS inline blocks; SIEM correlates logs; SOC investigates. **Working:** Data from endpoints/network/cloud → normalized events → rules → alert → triage. **Example:** Repeated failed logins + impossible travel triggers analyst review. **Nuance:** EDR/XDR vs NDR, UEBA, detection engineering and false-positive management. **Avoid:** One alert ≠ breach; require timestamps, asset context and corroboration.

## How to write a high-mark answer

**Definition (2 marks) → diagram/protocol sequence (3 marks) → real case (2 marks) → advanced trade-off (2 marks) → limitation (1 mark).**

Try to answer first without opening the solutions.
