# Chapter 10 — Switching VLANs STP

## இந்த Chapter-ன் நோக்கம்

Local network frames, loops, virtualization and defence.

**Learning path:** முதலில் definitions, பிறகு actual packet/service flow, real use case, advanced behaviour, பின்னர் safe lab. ஒவ்வொரு `.md` file-லும் இந்த முறையில் முழு lesson உள்ளது.

## Learning outcomes

- Ethernet Switching MAC Tables, Access Trunk VLAN 8021Q, STP RSTP Loop Prevention, Link Aggregation LACP ஆகியவற்றை விளக்க இயலும்.
- ஒவ்வொரு concept-க்கும் input → mechanism → output வரைபடம் வரைய இயலும்.
- Practical output மற்றும் common misconceptions வேறுபடுத்த இயலும்.
- Industry advanced variants ஏன் உருவானது, எந்த trade-off உள்ளது என்று கூற இயலும்.
- Exam question-க்கு definition, step-by-step example, diagram, limitation எழுத இயலும்.

## எல்லா subtopics-க்கும் தனித்தனி Markdown Notes

1. [Ethernet Switching MAC Tables](01_Ethernet_Switching_MAC_Tables.md)
2. [Access Trunk VLAN 8021Q](02_Access_Trunk_VLAN_8021Q.md)
3. [STP RSTP Loop Prevention](03_STP_RSTP_Loop_Prevention.md)
4. [Link Aggregation LACP](04_Link_Aggregation_LACP.md)
5. [8021X NAC and Device Trust](05_8021X_NAC_and_Device_Trust.md)
6. [VXLAN EVPN Modern L2 Over L3](06_VXLAN_EVPN_Modern_L2_Over_L3.md)

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
