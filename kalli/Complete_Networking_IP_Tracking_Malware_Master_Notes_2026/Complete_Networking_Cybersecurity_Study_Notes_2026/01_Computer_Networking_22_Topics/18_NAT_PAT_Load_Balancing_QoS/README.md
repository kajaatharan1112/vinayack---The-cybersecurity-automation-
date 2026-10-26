# Chapter 18 — NAT PAT Load Balancing QoS

## இந்த Chapter-ன் நோக்கம்

Address translation, scale and traffic guarantees.

**Learning path:** முதலில் definitions, பிறகு actual packet/service flow, real use case, advanced behaviour, பின்னர் safe lab. ஒவ்வொரு `.md` file-லும் இந்த முறையில் முழு lesson உள்ளது.

## Learning outcomes

- NAT PAT and Connection Tracking, Port Forwarding and DMZ, L4 and L7 Load Balancing, CDN Anycast and Caching ஆகியவற்றை விளக்க இயலும்.
- ஒவ்வொரு concept-க்கும் input → mechanism → output வரைபடம் வரைய இயலும்.
- Practical output மற்றும் common misconceptions வேறுபடுத்த இயலும்.
- Industry advanced variants ஏன் உருவானது, எந்த trade-off உள்ளது என்று கூற இயலும்.
- Exam question-க்கு definition, step-by-step example, diagram, limitation எழுத இயலும்.

## எல்லா subtopics-க்கும் தனித்தனி Markdown Notes

1. [NAT PAT and Connection Tracking](01_NAT_PAT_and_Connection_Tracking.md)
2. [Port Forwarding and DMZ](02_Port_Forwarding_and_DMZ.md)
3. [L4 and L7 Load Balancing](03_L4_and_L7_Load_Balancing.md)
4. [CDN Anycast and Caching](04_CDN_Anycast_and_Caching.md)
5. [QoS DSCP Traffic Shaping](05_QoS_DSCP_Traffic_Shaping.md)
6. [Capacity Planning and Scale](06_Capacity_Planning_and_Scale.md)

**Additional chapter files:** [Practical Lab](98_Practice_Lab.md) · [Quiz & Answers](99_Quiz_Answers.md)

## Four-minute chapter review

1. இந்த chapter-இன் ஒவ்வொரு tool/protocol-க்கும் **who communicates with whom** எழுதுங்கள்.
2. ஒரு normal path மற்றும் ஒரு failure path வரைந்து விளக்குங்கள்.
3. "What is observable? What remains encrypted/private?" என்று கேளுங்கள்.
4. ஒன்றே ஒரு root cause-ஐ ஆதாரம் இல்லாமல் அறிவிக்காமல், alternate cause ஒன்றைச் சேருங்கள்.
5. Advanced concept practical deploy ஆகும் போது version/support/dependency சரிபார்க்கவும்.

## Authoritative background

- [RFC 9293 TCP](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 9000 QUIC](https://www.rfc-editor.org/rfc/rfc9000)
