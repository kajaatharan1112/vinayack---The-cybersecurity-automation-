# Chapter 20 — Network Automation Telemetry SRE

## இந்த Chapter-ன் நோக்கம்

Practical operations: repeatability, safety and observability.

**Learning path:** முதலில் definitions, பிறகு actual packet/service flow, real use case, advanced behaviour, பின்னர் safe lab. ஒவ்வொரு `.md` file-லும் இந்த முறையில் முழு lesson உள்ளது.

## Learning outcomes

- Automation Basics CLI API Python, Infrastructure as Code, Network Observability SNMP Streaming, Logging Metrics Traces Correlation ஆகியவற்றை விளக்க இயலும்.
- ஒவ்வொரு concept-க்கும் input → mechanism → output வரைபடம் வரைய இயலும்.
- Practical output மற்றும் common misconceptions வேறுபடுத்த இயலும்.
- Industry advanced variants ஏன் உருவானது, எந்த trade-off உள்ளது என்று கூற இயலும்.
- Exam question-க்கு definition, step-by-step example, diagram, limitation எழுத இயலும்.

## எல்லா subtopics-க்கும் தனித்தனி Markdown Notes

1. [Automation Basics CLI API Python](01_Automation_Basics_CLI_API_Python.md)
2. [Infrastructure as Code](02_Infrastructure_as_Code.md)
3. [Network Observability SNMP Streaming](03_Network_Observability_SNMP_Streaming.md)
4. [Logging Metrics Traces Correlation](04_Logging_Metrics_Traces_Correlation.md)
5. [SRE SLO Alerting and Incident Review](05_SRE_SLO_Alerting_and_Incident_Review.md)
6. [NetDevOps CI Policy Validation](06_NetDevOps_CI_Policy_Validation.md)

**Additional chapter files:** [Practical Lab](98_Practice_Lab.md) · [Quiz & Answers](99_Quiz_Answers.md)

## Four-minute chapter review

1. இந்த chapter-இன் ஒவ்வொரு tool/protocol-க்கும் **who communicates with whom** எழுதுங்கள்.
2. ஒரு normal path மற்றும் ஒரு failure path வரைந்து விளக்குங்கள்.
3. "What is observable? What remains encrypted/private?" என்று கேளுங்கள்.
4. ஒன்றே ஒரு root cause-ஐ ஆதாரம் இல்லாமல் அறிவிக்காமல், alternate cause ஒன்றைச் சேருங்கள்.
5. Advanced concept practical deploy ஆகும் போது version/support/dependency சரிபார்க்கவும்.

## Authoritative background

- [Cilium eBPF Networking and Service Mesh](https://docs.cilium.io/en/stable/network/servicemesh/index.html)
- [Kubernetes Gateway API Documentation](https://gateway-api.sigs.k8s.io/docs/introduction/)
