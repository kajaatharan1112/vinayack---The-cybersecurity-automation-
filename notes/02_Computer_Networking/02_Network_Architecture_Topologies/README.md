# Chapter 02 — Network Architecture Topologies

## இந்த Chapter-ன் நோக்கம்

கட்டமைப்பு, redundancy, control plane/data plane, campus மற்றும் data-centre patterns.

**Learning path:** முதலில் definitions, பிறகு actual packet/service flow, real use case, advanced behaviour, பின்னர் safe lab. ஒவ்வொரு `.md` file-லும் இந்த முறையில் முழு lesson உள்ளது.

## Learning outcomes

- Star Bus Ring Mesh Tree, Three Tier and Spine Leaf, Control Plane Data Plane Management Plane, High Availability and Failure Domains ஆகியவற்றை விளக்க இயலும்.
- ஒவ்வொரு concept-க்கும் input → mechanism → output வரைபடம் வரைய இயலும்.
- Practical output மற்றும் common misconceptions வேறுபடுத்த இயலும்.
- Industry advanced variants ஏன் உருவானது, எந்த trade-off உள்ளது என்று கூற இயலும்.
- Exam question-க்கு definition, step-by-step example, diagram, limitation எழுத இயலும்.

## எல்லா subtopics-க்கும் தனித்தனி Markdown Notes

1. [Star Bus Ring Mesh Tree](01_Star_Bus_Ring_Mesh_Tree.md)
2. [Three Tier and Spine Leaf](02_Three_Tier_and_Spine_Leaf.md)
3. [Control Plane Data Plane Management Plane](03_Control_Plane_Data_Plane_Management_Plane.md)
4. [High Availability and Failure Domains](04_High_Availability_and_Failure_Domains.md)
5. [Network Segmentation Zones](05_Network_Segmentation_Zones.md)
6. [Underlay Overlay SDN](06_Underlay_Overlay_SDN.md)

**Additional chapter files:** [Practical Lab](98_Practice_Lab.md) · [Quiz & Answers](99_Quiz_Answers.md)

## Four-minute chapter review

1. இந்த chapter-இன் ஒவ்வொரு tool/protocol-க்கும் **who communicates with whom** எழுதுங்கள்.
2. ஒரு normal path மற்றும் ஒரு failure path வரைந்து விளக்குங்கள்.
3. "What is observable? What remains encrypted/private?" என்று கேளுங்கள்.
4. ஒன்றே ஒரு root cause-ஐ ஆதாரம் இல்லாமல் அறிவிக்காமல், alternate cause ஒன்றைச் சேருங்கள்.
5. Advanced concept practical deploy ஆகும் போது version/support/dependency சரிபார்க்கவும்.

## Authoritative background

- [Kubernetes Gateway API Documentation](https://gateway-api.sigs.k8s.io/docs/introduction/)
- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
