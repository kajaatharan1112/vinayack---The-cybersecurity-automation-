# Chapter 13 — Network Security Firewall VPN ZeroTrust

## இந்த Chapter-ன் நோக்கம்

Identity-centric protection and secure access.

**Learning path:** முதலில் definitions, பிறகு actual packet/service flow, real use case, advanced behaviour, பின்னர் safe lab. ஒவ்வொரு `.md` file-லும் இந்த முறையில் முழு lesson உள்ளது.

## Learning outcomes

- Threat Model CIA and Defence in Depth, Firewalls ACL Stateful NGFW, VPN IPsec WireGuard ZTNA, Zero Trust Architecture ஆகியவற்றை விளக்க இயலும்.
- ஒவ்வொரு concept-க்கும் input → mechanism → output வரைபடம் வரைய இயலும்.
- Practical output மற்றும் common misconceptions வேறுபடுத்த இயலும்.
- Industry advanced variants ஏன் உருவானது, எந்த trade-off உள்ளது என்று கூற இயலும்.
- Exam question-க்கு definition, step-by-step example, diagram, limitation எழுத இயலும்.

## எல்லா subtopics-க்கும் தனித்தனி Markdown Notes

1. [Threat Model CIA and Defence in Depth](01_Threat_Model_CIA_and_Defence_in_Depth.md)
2. [Firewalls ACL Stateful NGFW](02_Firewalls_ACL_Stateful_NGFW.md)
3. [VPN IPsec WireGuard ZTNA](03_VPN_IPsec_WireGuard_ZTNA.md)
4. [Zero Trust Architecture](04_Zero_Trust_Architecture.md)
5. [TLS PKI Certificates mTLS](05_TLS_PKI_Certificates_mTLS.md)
6. [IDS IPS SIEM SOC](06_IDS_IPS_SIEM_SOC.md)

**Additional chapter files:** [Practical Lab](98_Practice_Lab.md) · [Quiz & Answers](99_Quiz_Answers.md)

## Four-minute chapter review

1. இந்த chapter-இன் ஒவ்வொரு tool/protocol-க்கும் **who communicates with whom** எழுதுங்கள்.
2. ஒரு normal path மற்றும் ஒரு failure path வரைந்து விளக்குங்கள்.
3. "What is observable? What remains encrypted/private?" என்று கேளுங்கள்.
4. ஒன்றே ஒரு root cause-ஐ ஆதாரம் இல்லாமல் அறிவிக்காமல், alternate cause ஒன்றைச் சேருங்கள்.
5. Advanced concept practical deploy ஆகும் போது version/support/dependency சரிபார்க்கவும்.

## Authoritative background

- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [CISA 2025 Microsegmentation Guidance](https://www.cisa.gov/news-events/alerts/2025/07/29/cisa-releases-part-one-zero-trust-microsegmentation-guidance)
- [NIST FIPS 203 ML-KEM](https://csrc.nist.gov/pubs/fips/203/final)
