# Chapter 14 — Network Traffic Analysis

## இந்த Chapter-ன் நோக்கம்

Packet-level observability and evidence-based diagnosis.

**Learning path:** முதலில் definitions, பிறகு actual packet/service flow, real use case, advanced behaviour, பின்னர் safe lab. ஒவ்வொரு `.md` file-லும் இந்த முறையில் முழு lesson உள்ளது.

## Learning outcomes

- Packet Capture Fundamentals, Capture vs Display Filters, TCP Analysis RTT Retransmission, DNS HTTP TLS Metadata ஆகியவற்றை விளக்க இயலும்.
- ஒவ்வொரு concept-க்கும் input → mechanism → output வரைபடம் வரைய இயலும்.
- Practical output மற்றும் common misconceptions வேறுபடுத்த இயலும்.
- Industry advanced variants ஏன் உருவானது, எந்த trade-off உள்ளது என்று கூற இயலும்.
- Exam question-க்கு definition, step-by-step example, diagram, limitation எழுத இயலும்.

## எல்லா subtopics-க்கும் தனித்தனி Markdown Notes

1. [Packet Capture Fundamentals](01_Packet_Capture_Fundamentals.md)
2. [Capture vs Display Filters](02_Capture_vs_Display_Filters.md)
3. [TCP Analysis RTT Retransmission](03_TCP_Analysis_RTT_Retransmission.md)
4. [DNS HTTP TLS Metadata](04_DNS_HTTP_TLS_Metadata.md)
5. [Flows NetFlow IPFIX sFlow](05_Flows_NetFlow_IPFIX_sFlow.md)
6. [Network Performance Indicators](06_Network_Performance_Indicators.md)

**Additional chapter files:** [Practical Lab](98_Practice_Lab.md) · [Quiz & Answers](99_Quiz_Answers.md)

## Four-minute chapter review

1. இந்த chapter-இன் ஒவ்வொரு tool/protocol-க்கும் **who communicates with whom** எழுதுங்கள்.
2. ஒரு normal path மற்றும் ஒரு failure path வரைந்து விளக்குங்கள்.
3. "What is observable? What remains encrypted/private?" என்று கேளுங்கள்.
4. ஒன்றே ஒரு root cause-ஐ ஆதாரம் இல்லாமல் அறிவிக்காமல், alternate cause ஒன்றைச் சேருங்கள்.
5. Advanced concept practical deploy ஆகும் போது version/support/dependency சரிபார்க்கவும்.

## Authoritative background

- [Wireshark User Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
- [NIST SP 800-86 Forensics](https://csrc.nist.gov/pubs/sp/800/86/final)
