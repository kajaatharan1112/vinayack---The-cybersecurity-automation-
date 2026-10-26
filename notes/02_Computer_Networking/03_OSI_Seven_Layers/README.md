# Chapter 03 — OSI Seven Layers

## இந்த Chapter-ன் நோக்கம்

7-layer mental model, encapsulation, failure isolation, modern encryption.

**Learning path:** முதலில் definitions, பிறகு actual packet/service flow, real use case, advanced behaviour, பின்னர் safe lab. ஒவ்வொரு `.md` file-லும் இந்த முறையில் முழு lesson உள்ளது.

## Learning outcomes

- Layer 1 Physical, Layer 2 Data Link, Layer 3 Network, Layer 4 Transport ஆகியவற்றை விளக்க இயலும்.
- ஒவ்வொரு concept-க்கும் input → mechanism → output வரைபடம் வரைய இயலும்.
- Practical output மற்றும் common misconceptions வேறுபடுத்த இயலும்.
- Industry advanced variants ஏன் உருவானது, எந்த trade-off உள்ளது என்று கூற இயலும்.
- Exam question-க்கு definition, step-by-step example, diagram, limitation எழுத இயலும்.

## எல்லா subtopics-க்கும் தனித்தனி Markdown Notes

1. [Layer 1 Physical](01_Layer_1_Physical.md)
2. [Layer 2 Data Link](02_Layer_2_Data_Link.md)
3. [Layer 3 Network](03_Layer_3_Network.md)
4. [Layer 4 Transport](04_Layer_4_Transport.md)
5. [Layers 5 and 6 Session Presentation](05_Layers_5_and_6_Session_Presentation.md)
6. [Layer 7 Application](06_Layer_7_Application.md)
7. [Cross Layer Troubleshooting](07_Cross_Layer_Troubleshooting.md)

**Additional chapter files:** [Practical Lab](98_Practice_Lab.md) · [Quiz & Answers](99_Quiz_Answers.md)

## Four-minute chapter review

1. இந்த chapter-இன் ஒவ்வொரு tool/protocol-க்கும் **who communicates with whom** எழுதுங்கள்.
2. ஒரு normal path மற்றும் ஒரு failure path வரைந்து விளக்குங்கள்.
3. "What is observable? What remains encrypted/private?" என்று கேளுங்கள்.
4. ஒன்றே ஒரு root cause-ஐ ஆதாரம் இல்லாமல் அறிவிக்காமல், alternate cause ஒன்றைச் சேருங்கள்.
5. Advanced concept practical deploy ஆகும் போது version/support/dependency சரிபார்க்கவும்.

## Authoritative background

- [RFC 9293 TCP](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 8200 IPv6](https://www.rfc-editor.org/rfc/rfc8200)
