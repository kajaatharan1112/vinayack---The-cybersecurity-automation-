# Chapter 11 — Routing OSPF BGP

## இந்த Chapter-ன் நோக்கம்

Forwarding decisions, dynamic routes and Internet operations.

**Learning path:** முதலில் definitions, பிறகு actual packet/service flow, real use case, advanced behaviour, பின்னர் safe lab. ஒவ்வொரு `.md` file-லும் இந்த முறையில் முழு lesson உள்ளது.

## Learning outcomes

- Routing Table Longest Prefix Match, Static Routes and Default Route, OSPF Link State Protocol, BGP Between Autonomous Systems ஆகியவற்றை விளக்க இயலும்.
- ஒவ்வொரு concept-க்கும் input → mechanism → output வரைபடம் வரைய இயலும்.
- Practical output மற்றும் common misconceptions வேறுபடுத்த இயலும்.
- Industry advanced variants ஏன் உருவானது, எந்த trade-off உள்ளது என்று கூற இயலும்.
- Exam question-க்கு definition, step-by-step example, diagram, limitation எழுத இயலும்.

## எல்லா subtopics-க்கும் தனித்தனி Markdown Notes

1. [Routing Table Longest Prefix Match](01_Routing_Table_Longest_Prefix_Match.md)
2. [Static Routes and Default Route](02_Static_Routes_and_Default_Route.md)
3. [OSPF Link State Protocol](03_OSPF_Link_State_Protocol.md)
4. [BGP Between Autonomous Systems](04_BGP_Between_Autonomous_Systems.md)
5. [Routing Protocol Comparisons](05_Routing_Protocol_Comparisons.md)
6. [Multihoming and Routing Security](06_Multihoming_and_Routing_Security.md)

**Additional chapter files:** [Practical Lab](98_Practice_Lab.md) · [Quiz & Answers](99_Quiz_Answers.md)

## Four-minute chapter review

1. இந்த chapter-இன் ஒவ்வொரு tool/protocol-க்கும் **who communicates with whom** எழுதுங்கள்.
2. ஒரு normal path மற்றும் ஒரு failure path வரைந்து விளக்குங்கள்.
3. "What is observable? What remains encrypted/private?" என்று கேளுங்கள்.
4. ஒன்றே ஒரு root cause-ஐ ஆதாரம் இல்லாமல் அறிவிக்காமல், alternate cause ஒன்றைச் சேருங்கள்.
5. Advanced concept practical deploy ஆகும் போது version/support/dependency சரிபார்க்கவும்.

## Authoritative background

- [RIPE NCC RPKI Documentation](https://www.ripe.net/manage-ips-and-asns/resource-management/certification/)
