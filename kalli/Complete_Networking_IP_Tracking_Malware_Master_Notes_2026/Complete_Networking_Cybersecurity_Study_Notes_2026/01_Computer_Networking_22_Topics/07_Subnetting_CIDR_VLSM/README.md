# Chapter 07 — Subnetting CIDR VLSM

## இந்த Chapter-ன் நோக்கம்

Practice /24 to /30 calculations and advanced address allocation.

**Learning path:** முதலில் definitions, பிறகு actual packet/service flow, real use case, advanced behaviour, பின்னர் safe lab. ஒவ்வொரு `.md` file-லும் இந்த முறையில் முழு lesson உள்ளது.

## Learning outcomes

- Binary and Subnet Mask, CIDR Network Broadcast Hosts, VLSM Address Allocation, Supernetting Route Aggregation ஆகியவற்றை விளக்க இயலும்.
- ஒவ்வொரு concept-க்கும் input → mechanism → output வரைபடம் வரைய இயலும்.
- Practical output மற்றும் common misconceptions வேறுபடுத்த இயலும்.
- Industry advanced variants ஏன் உருவானது, எந்த trade-off உள்ளது என்று கூற இயலும்.
- Exam question-க்கு definition, step-by-step example, diagram, limitation எழுத இயலும்.

## எல்லா subtopics-க்கும் தனித்தனி Markdown Notes

1. [Binary and Subnet Mask](01_Binary_and_Subnet_Mask.md)
2. [CIDR Network Broadcast Hosts](02_CIDR_Network_Broadcast_Hosts.md)
3. [VLSM Address Allocation](03_VLSM_Address_Allocation.md)
4. [Supernetting Route Aggregation](04_Supernetting_Route_Aggregation.md)
5. [IPv6 Prefix Planning](05_IPv6_Prefix_Planning.md)
6. [Subnetting Exam Patterns](06_Subnetting_Exam_Patterns.md)

**Additional chapter files:** [Practical Lab](98_Practice_Lab.md) · [Quiz & Answers](99_Quiz_Answers.md)

## Four-minute chapter review

1. இந்த chapter-இன் ஒவ்வொரு tool/protocol-க்கும் **who communicates with whom** எழுதுங்கள்.
2. ஒரு normal path மற்றும் ஒரு failure path வரைந்து விளக்குங்கள்.
3. "What is observable? What remains encrypted/private?" என்று கேளுங்கள்.
4. ஒன்றே ஒரு root cause-ஐ ஆதாரம் இல்லாமல் அறிவிக்காமல், alternate cause ஒன்றைச் சேருங்கள்.
5. Advanced concept practical deploy ஆகும் போது version/support/dependency சரிபார்க்கவும்.

## Authoritative background

- [RFC 1918 Private IPv4](https://www.rfc-editor.org/rfc/rfc1918)
- [RFC 8200 IPv6](https://www.rfc-editor.org/rfc/rfc8200)
