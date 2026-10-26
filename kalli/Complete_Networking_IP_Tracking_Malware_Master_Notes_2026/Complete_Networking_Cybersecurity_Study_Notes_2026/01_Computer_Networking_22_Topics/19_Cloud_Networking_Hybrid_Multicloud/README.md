# Chapter 19 — Cloud Networking Hybrid Multicloud

## இந்த Chapter-ன் நோக்கம்

VPC primitives, private access and distributed networks.

**Learning path:** முதலில் definitions, பிறகு actual packet/service flow, real use case, advanced behaviour, பின்னர் safe lab. ஒவ்வொரு `.md` file-லும் இந்த முறையில் முழு lesson உள்ளது.

## Learning outcomes

- Cloud VPC VNet Subnets, Cloud Security Groups NACL, Hybrid VPN Private Connections, Cloud NAT Endpoints and Egress ஆகியவற்றை விளக்க இயலும்.
- ஒவ்வொரு concept-க்கும் input → mechanism → output வரைபடம் வரைய இயலும்.
- Practical output மற்றும் common misconceptions வேறுபடுத்த இயலும்.
- Industry advanced variants ஏன் உருவானது, எந்த trade-off உள்ளது என்று கூற இயலும்.
- Exam question-க்கு definition, step-by-step example, diagram, limitation எழுத இயலும்.

## எல்லா subtopics-க்கும் தனித்தனி Markdown Notes

1. [Cloud VPC VNet Subnets](01_Cloud_VPC_VNet_Subnets.md)
2. [Cloud Security Groups NACL](02_Cloud_Security_Groups_NACL.md)
3. [Hybrid VPN Private Connections](03_Hybrid_VPN_Private_Connections.md)
4. [Cloud NAT Endpoints and Egress](04_Cloud_NAT_Endpoints_and_Egress.md)
5. [Kubernetes Networking Services CNI](05_Kubernetes_Networking_Services_CNI.md)
6. [Gateway API Service Mesh eBPF](06_Gateway_API_Service_Mesh_eBPF.md)

**Additional chapter files:** [Practical Lab](98_Practice_Lab.md) · [Quiz & Answers](99_Quiz_Answers.md)

## Four-minute chapter review

1. இந்த chapter-இன் ஒவ்வொரு tool/protocol-க்கும் **who communicates with whom** எழுதுங்கள்.
2. ஒரு normal path மற்றும் ஒரு failure path வரைந்து விளக்குங்கள்.
3. "What is observable? What remains encrypted/private?" என்று கேளுங்கள்.
4. ஒன்றே ஒரு root cause-ஐ ஆதாரம் இல்லாமல் அறிவிக்காமல், alternate cause ஒன்றைச் சேருங்கள்.
5. Advanced concept practical deploy ஆகும் போது version/support/dependency சரிபார்க்கவும்.

## Authoritative background

- [Kubernetes Gateway API Documentation](https://gateway-api.sigs.k8s.io/docs/introduction/)
- [Cilium eBPF Networking and Service Mesh](https://docs.cilium.io/en/stable/network/servicemesh/index.html)
