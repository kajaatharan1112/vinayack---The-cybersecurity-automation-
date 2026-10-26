# Chapter 03 — IP Tracking IP Tracing Remote Activity Analysis

## இந்த Chapter-ன் நோக்கம்

ஒரு IP-ஐப் பற்றித் தெரிந்து கொள்ளக்கூடிய பொது தகவல் என்ன? Own network telemetry-யில் என்ன evidence கிடைக்கும்? Attribution எங்கே முடிகிறது?

**Learning path:** முதலில் definitions, பிறகு actual packet/service flow, real use case, advanced behaviour, பின்னர் safe lab. ஒவ்வொரு `.md` file-லும் இந்த முறையில் முழு lesson உள்ளது.

## Learning outcomes

- IP Address and Identity Limits, Passive vs Active Reconnaissance, RIR RDAP WHOIS IP Ownership, ASN BGP Origin and Prefixes ஆகியவற்றை விளக்க இயலும்.
- ஒவ்வொரு concept-க்கும் input → mechanism → output வரைபடம் வரைய இயலும்.
- Practical output மற்றும் common misconceptions வேறுபடுத்த இயலும்.
- Industry advanced variants ஏன் உருவானது, எந்த trade-off உள்ளது என்று கூற இயலும்.
- Exam question-க்கு definition, step-by-step example, diagram, limitation எழுத இயலும்.

## எல்லா subtopics-க்கும் தனித்தனி Markdown Notes

1. [IP Address and Identity Limits](01_IP_Address_and_Identity_Limits.md)
2. [Passive vs Active Reconnaissance](02_Passive_vs_Active_Reconnaissance.md)
3. [RIR RDAP WHOIS IP Ownership](03_RIR_RDAP_WHOIS_IP_Ownership.md)
4. [ASN BGP Origin and Prefixes](04_ASN_BGP_Origin_and_Prefixes.md)
5. [Geolocation Country Region City Accuracy](05_Geolocation_Country_Region_City_Accuracy.md)
6. [DNS A AAAA PTR Reverse DNS](06_DNS_A_AAAA_PTR_Reverse_DNS.md)
7. [Route Tracing Traceroute MTR](07_Route_Tracing_Traceroute_MTR.md)
8. [Latency Measurement and Network Distance](08_Latency_Measurement_and_Network_Distance.md)
9. [Public Ports and Service Exposure](09_Public_Ports_and_Service_Exposure.md)
10. [IP Reputation Blocklists OSINT Confidence](10_IP_Reputation_Blocklists_OSINT_Confidence.md)
11. [Threat Intelligence Enrichment Workflow](11_Threat_Intelligence_Enrichment_Workflow.md)
12. [Server Access Logs and IP Activity](12_Server_Access_Logs_and_IP_Activity.md)
13. [Firewall NAT VPN Proxy Logs](13_Firewall_NAT_VPN_Proxy_Logs.md)
14. [Flow Telemetry NetFlow IPFIX sFlow](14_Flow_Telemetry_NetFlow_IPFIX_sFlow.md)
15. [DNS Logs and Encrypted DNS Limits](15_DNS_Logs_and_Encrypted_DNS_Limits.md)
16. [Endpoint EDR and Browser Evidence](16_Endpoint_EDR_and_Browser_Evidence.md)
17. [Detecting Scanning and Abuse on Owned Systems](17_Detecting_Scanning_and_Abuse_on_Owned_Systems.md)
18. [Attribution Evidence Chain of Custody](18_Attribution_Evidence_Chain_of_Custody.md)
19. [Privacy Laws Ethics Authorization](19_Privacy_Laws_Ethics_Authorization.md)
20. [Case Study Suspicious IP on Own API](20_Case_Study_Suspicious_IP_on_Own_API.md)
21. [Live Network Monitoring Dashboard Design](21_Live_Network_Monitoring_Dashboard_Design.md)
22. [Limits of Remote Investigation Summary](22_Limits_of_Remote_Investigation_Summary.md)

**Additional chapter files:** [Practical Lab](98_Practice_Lab.md) · [Quiz & Answers](99_Quiz_Answers.md)

## Four-minute chapter review

1. இந்த chapter-இன் ஒவ்வொரு tool/protocol-க்கும் **who communicates with whom** எழுதுங்கள்.
2. ஒரு normal path மற்றும் ஒரு failure path வரைந்து விளக்குங்கள்.
3. "What is observable? What remains encrypted/private?" என்று கேளுங்கள்.
4. ஒன்றே ஒரு root cause-ஐ ஆதாரம் இல்லாமல் அறிவிக்காமல், alternate cause ஒன்றைச் சேருங்கள்.
5. Advanced concept practical deploy ஆகும் போது version/support/dependency சரிபார்க்கவும்.

## Authoritative background

- [ARIN: IP record location limitations](https://www.arin.net/about/relations/law_enforcement/faq/)
- [APNIC 2026: Geolocation evidence not certainty](https://blog.apnic.net/2026/09/24/ip-geolocation-at-apnic-62-challenges-geofeeds-and-data-quality-perspectives/)
- [NIST SP 800-86 Forensics](https://csrc.nist.gov/pubs/sp/800/86/final)
- [MITRE ATT&CK Enterprise Tactics](https://attack.mitre.org/tactics/enterprise/)
