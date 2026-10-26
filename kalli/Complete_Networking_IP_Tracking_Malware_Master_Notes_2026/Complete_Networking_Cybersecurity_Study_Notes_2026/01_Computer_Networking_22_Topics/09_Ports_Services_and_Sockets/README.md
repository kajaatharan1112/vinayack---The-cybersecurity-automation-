# Chapter 09 — Ports Services and Sockets

## இந்த Chapter-ன் நோக்கம்

Well-known ports, listening sockets, encrypted protocols and checks.

**Learning path:** முதலில் definitions, பிறகு actual packet/service flow, real use case, advanced behaviour, பின்னர் safe lab. ஒவ்வொரு `.md` file-லும் இந்த முறையில் முழு lesson உள்ளது.

## Learning outcomes

- Port Basics and IANA Ranges, Common Service Ports, Ephemeral Ports and Five Tuple, Service Discovery and Banners ஆகியவற்றை விளக்க இயலும்.
- ஒவ்வொரு concept-க்கும் input → mechanism → output வரைபடம் வரைய இயலும்.
- Practical output மற்றும் common misconceptions வேறுபடுத்த இயலும்.
- Industry advanced variants ஏன் உருவானது, எந்த trade-off உள்ளது என்று கூற இயலும்.
- Exam question-க்கு definition, step-by-step example, diagram, limitation எழுத இயலும்.

## எல்லா subtopics-க்கும் தனித்தனி Markdown Notes

1. [Port Basics and IANA Ranges](01_Port_Basics_and_IANA_Ranges.md)
2. [Common Service Ports](02_Common_Service_Ports.md)
3. [Ephemeral Ports and Five Tuple](03_Ephemeral_Ports_and_Five_Tuple.md)
4. [Service Discovery and Banners](04_Service_Discovery_and_Banners.md)
5. [Firewall Reachability and Health](05_Firewall_Reachability_and_Health.md)

**Additional chapter files:** [Practical Lab](98_Practice_Lab.md) · [Quiz & Answers](99_Quiz_Answers.md)

## Four-minute chapter review

1. இந்த chapter-இன் ஒவ்வொரு tool/protocol-க்கும் **who communicates with whom** எழுதுங்கள்.
2. ஒரு normal path மற்றும் ஒரு failure path வரைந்து விளக்குங்கள்.
3. "What is observable? What remains encrypted/private?" என்று கேளுங்கள்.
4. ஒன்றே ஒரு root cause-ஐ ஆதாரம் இல்லாமல் அறிவிக்காமல், alternate cause ஒன்றைச் சேருங்கள்.
5. Advanced concept practical deploy ஆகும் போது version/support/dependency சரிபார்க்கவும்.

## Authoritative background

- [IANA Protocol Registries](https://www.iana.org/protocols)
- [RFC 9293 TCP](https://www.rfc-editor.org/rfc/rfc9293)
