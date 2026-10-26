# Chapter 08 — Network Protocols

## இந்த Chapter-ன் நோக்கம்

How common networking protocols fit together.

**Learning path:** முதலில் definitions, பிறகு actual packet/service flow, real use case, advanced behaviour, பின்னர் safe lab. ஒவ்வொரு `.md` file-லும் இந்த முறையில் முழு lesson உள்ளது.

## Learning outcomes

- TCP vs UDP, DNS Lookup Journey, DHCP DORA and DHCPv6, ARP ICMP NTP ஆகியவற்றை விளக்க இயலும்.
- ஒவ்வொரு concept-க்கும் input → mechanism → output வரைபடம் வரைய இயலும்.
- Practical output மற்றும் common misconceptions வேறுபடுத்த இயலும்.
- Industry advanced variants ஏன் உருவானது, எந்த trade-off உள்ளது என்று கூற இயலும்.
- Exam question-க்கு definition, step-by-step example, diagram, limitation எழுத இயலும்.

## எல்லா subtopics-க்கும் தனித்தனி Markdown Notes

1. [TCP vs UDP](01_TCP_vs_UDP.md)
2. [DNS Lookup Journey](02_DNS_Lookup_Journey.md)
3. [DHCP DORA and DHCPv6](03_DHCP_DORA_and_DHCPv6.md)
4. [ARP ICMP NTP](04_ARP_ICMP_NTP.md)
5. [HTTP HTTPS TLS](05_HTTP_HTTPS_TLS.md)
6. [Mail and Remote Administration](06_Mail_and_Remote_Administration.md)

**Additional chapter files:** [Practical Lab](98_Practice_Lab.md) · [Quiz & Answers](99_Quiz_Answers.md)

## Four-minute chapter review

1. இந்த chapter-இன் ஒவ்வொரு tool/protocol-க்கும் **who communicates with whom** எழுதுங்கள்.
2. ஒரு normal path மற்றும் ஒரு failure path வரைந்து விளக்குங்கள்.
3. "What is observable? What remains encrypted/private?" என்று கேளுங்கள்.
4. ஒன்றே ஒரு root cause-ஐ ஆதாரம் இல்லாமல் அறிவிக்காமல், alternate cause ஒன்றைச் சேருங்கள்.
5. Advanced concept practical deploy ஆகும் போது version/support/dependency சரிபார்க்கவும்.

## Authoritative background

- [RFC 9460 DNS SVCB/HTTPS](https://www.rfc-editor.org/rfc/rfc9460)
- [RFC 9293 TCP](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 9114 HTTP/3](https://www.rfc-editor.org/rfc/rfc9114)
