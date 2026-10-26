# 18.04 — CDN Anycast and Caching

> **பிரிவு:** NAT_PAT_Load_Balancing_QoS  
> **Level:** Foundations → Practical → Advanced  
> **கற்றல் முறை:** Simple explanation + working mechanism + real-world case + modern concept + practical + exam.

## 1. எளிமையாகப் புரிந்துகொள்வோம் (Simple meaning)

CDN caches/static content near users; Anycast announces same address from multiple sites.

**நினைவில் வைத்துக்கொள்ளுங்கள்:** இந்த topic-இல் முக்கியம் பெயர்களை மனப்பாடம் செய்வது மட்டுமல்ல; data எங்கிருந்து எங்கு செல்கிறது, எந்த component எந்த முடிவு எடுக்கிறது, அந்த முடிவை எந்த evidence மூலம் நிரூபிக்கலாம் என்பதே. “CDN Anycast and Caching” ஒரு network/system problem-க்கு எப்படி உதவுகிறது என்று கீழே பார்க்கலாம்.

## 2. இந்த concept-ன் தேவை (Why teams use it)

- **முக்கியக் கேள்வி:** “CDN Anycast and Caching” என்ன செய்கிறது; செய்யாதது என்ன?
- **Problem it addresses:** CDN caches/static content near users; Anycast announces same address from multiple sites.
- **Expected output:** கருத்தின் architecture, flow, operational evidence அல்லது safe measurement-ஐ விளக்கத் தெரிந்திருக்க வேண்டும்.
- **Engineer view:** ஒரு observation வந்தால் முன்கூட்டியே முடிவு சொல்லாமல் supporting logs, configuration மற்றும் alternate explanations-ஐச் சரிபார்க்க வேண்டும்.

## 3. எப்படி வேலை செய்கிறது? (Working mechanism)

1. **Step 1:** Routing picks nearby reachable PoP.
2. **Step 2:** cache hit avoids origin call.

**Technical detail:** Routing picks nearby reachable PoP; cache hit avoids origin call.  
**எளிய mental model:** Input → rule/protocol/process → outcome → observable evidence. இந்த 4 பாகங்களையும் தனித்தனியாகக் கண்டறிந்தால் பெரிய network architecture-களும் புரியும்.

## 4. Real-world / Industry Example (நிஜ வாழ்க்கை உதாரணம்)

> Student downloads lecture PDF served from local CDN edge.

**நீங்கள் network engineer என்றால்:** அந்த situation-இல் எந்த endpoint, intermediate device, service மற்றும் log source இருக்கும் என்று எழுதுங்கள். **Successful behaviour** மற்றும் **failed behaviour** ஆகிய இரண்டுக்கும் தனித்தனியான evidence தேவை. ஒரே command-ன் output-ஐ வைத்து அனைத்தையும் உறுதி செய்ய வேண்டாம்.

### Example walkthrough

1. **Situation:** Student downloads lecture PDF served from local CDN edge.
2. **Observe:** protocol/data path, current configuration, network timing மற்றும் relevant system logs ஆகியவற்றை note எடுக்கவும்.
3. **Interpret:** CDN caches/static content near users; Anycast announces same address from multiple sites.
4. **Verify:** Anycast closest in BGP topology not always geographically nearest.
5. **Conclude carefully:** ஒரு result-ஐ root cause என்று அறிவிக்கும் முன் independent evidence ஒன்றையாவது ஒப்பிடவும்.

## 5. Advanced / Rare / Modern concepts (ஆழமாகக் கற்போம்)

Cache keys, stale-while-revalidate, request coalescing and cache poisoning defenses.

**Why it matters in industry:** Modern deployments-ல் multiple networks, encryption, identity policy, virtual overlays, cloud/CDN போன்ற இடைநிலைகள் இருக்கலாம். அதனால் இந்த advanced behaviour புரிந்தால்தான் paper-design-க்கும் real deployment-க்கும் உள்ள வித்தியாசம் தெரிய வரும். Modern support என்பது product/version/policy-ஐப் பொறுத்தது; universally enabled என்று கருத வேண்டாம்.

## 6. Common confusion & Troubleshooting (தவிர்க்க வேண்டிய தவறுகள்)

**குறிப்பிட்ட சிக்கல்:** Anycast closest in BGP topology not always geographically nearest.

| நீங்கள் பார்க்கும் நிலை | உடனடியாக செய்ய வேண்டியது | ஏன்? |
|---|---|---|
| Unexpected output | Observation time, topology, IP/port/protocol அல்லது file source-ஐப் பதிவு செய் | மீண்டும் reproduce செய்ய முடிய வேண்டும் |
| Expected output வரவில்லை | Host, route, name resolution, auth மற்றும் app dependency இதில் பொருத்தமான layer-ஐத் தனியாகச் சோதி | Wrong layer fix தவிர்க்க |
| பல explanations இருக்கின்றன | Baseline comparison + independent evidence சேர் | False attribution தவிர்க்க |
| Change செய்ய வேண்டும் | Permission, backup, test, rollback திட்டம் வைத்துக்கொள் | Production outage தவிர்க்க |

## 7. Safe Hands-on Practical (செய்து கற்போம்)

**Task:** Draw DNS/CDN edge/origin path and cache miss process.

**Lab procedure:**
1. உங்களுக்குச் சொந்தமான/அனுமதிக்கப்பட்ட system மட்டும் தேர்வு செய்யுங்கள். Real traffic வேண்டாமெனில் synthetic output அல்லது diagram பயன்படுத்துங்கள்.
2. Starting state (IP, OS, route, device owner, timestamp) note செய்யுங்கள்.
3. Task-ஐச் செய்து **expected vs observed** என்ற இரு வரிசைகளில் எழுதுங்கள்.
4. One failure condition சிந்தியுங்கள்: என்ன output வரும், எந்த layer-க்கு அது பொருந்தும்?
5. Screenshot/diagram/short write-up போதும். Unknown third-party systems-ஐ probe செய்ய வேண்டாம்.

**Practical record template:**

```text
Experiment: CDN Anycast and Caching
Environment: owned device / host-only virtual lab / synthetic data
Goal: Draw DNS/CDN edge/origin path and cache miss process.
Expected observation:
Actual observation:
Evidence and timestamps:
Alternative explanation:
Conclusion + uncertainty:
Next safe step:
```

## 8. Exam Preparation / Revision

### Questions (நீங்களே பதில் சொல்லிப் பாருங்கள்)
1. **Define:** “CDN Anycast and Caching” என்றால் என்ன? எந்த problem-ஐ solve செய்கிறது?
2. **Mechanism:** இது வேலை செய்யும் படிகளை ஒரு diagram-ஆக வரையுங்கள்.
3. **Application:** “Student downloads lecture PDF served from local CDN edge.” என்ற situation-இல் இதன் role என்ன?
4. **Advanced:** “Cache keys, stale-while-revalidate, request coalescing and cache poisoning defenses.” ஏன் முக்கியம்?
5. **Troubleshooting:** “Anycast closest in BGP topology not always geographically nearest.” என்ற நிலையில் என்ன conclusion செய்யக் கூடாது?

<details><summary>Suggested Answer Key — பார்க்கக் கிளிக் செய்யுங்கள்</summary>

- **1:** CDN caches/static content near users; Anycast announces same address from multiple sites.
- **2:** Routing picks nearby reachable PoP; cache hit avoids origin call.
- **3:** Student downloads lecture PDF served from local CDN edge.
- **4:** Cache keys, stale-while-revalidate, request coalescing and cache poisoning defenses.
- **5:** Anycast closest in BGP topology not always geographically nearest.

</details>

## 9. One-minute Revision (மீள்பார்வை)

- **What:** CDN caches/static content near users; Anycast announces same address from multiple sites.
- **How:** Routing picks nearby reachable PoP; cache hit avoids origin call.
- **Where used:** Student downloads lecture PDF served from local CDN edge.
- **Advanced:** Cache keys, stale-while-revalidate, request coalescing and cache poisoning defenses.
- **Avoid:** Anycast closest in BGP topology not always geographically nearest.

## 10. Further Reading (மூல references)

- [RFC 9293 TCP](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 9000 QUIC](https://www.rfc-editor.org/rfc/rfc9000)

---

**பாதுகாப்பு:** Practical-கள் உங்களுக்குச் சொந்தமான device, தனிமைப்படுத்தப்பட்ட lab, அல்லது எழுத்துப்பூர்வமாக அனுமதி பெற்ற network-இல் மட்டுமே. Public IP பதிவு அல்லது scan உங்கள் அனுமதியைத் தானாக நிரூபிக்காது. Malware sample-ஐ everyday PC-ல் இயக்காதீர்கள்.
