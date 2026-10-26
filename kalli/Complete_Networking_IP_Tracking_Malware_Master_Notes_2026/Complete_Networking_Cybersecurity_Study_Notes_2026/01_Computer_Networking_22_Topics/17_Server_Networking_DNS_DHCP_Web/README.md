# Chapter 17 — Server Networking DNS DHCP Web

## இந்த Chapter-ன் நோக்கம்

Operate core infrastructure services safely.

**Learning path:** முதலில் definitions, பிறகு actual packet/service flow, real use case, advanced behaviour, பின்னர் safe lab. ஒவ்வொரு `.md` file-லும் இந்த முறையில் முழு lesson உள்ளது.

## Learning outcomes

- DNS Server Roles and Zones, DHCP Server Scopes and Relay, Linux Web Server Reverse Proxy, SSH SFTP Remote Management ஆகியவற்றை விளக்க இயலும்.
- ஒவ்வொரு concept-க்கும் input → mechanism → output வரைபடம் வரைய இயலும்.
- Practical output மற்றும் common misconceptions வேறுபடுத்த இயலும்.
- Industry advanced variants ஏன் உருவானது, எந்த trade-off உள்ளது என்று கூற இயலும்.
- Exam question-க்கு definition, step-by-step example, diagram, limitation எழுத இயலும்.

## எல்லா subtopics-க்கும் தனித்தனி Markdown Notes

1. [DNS Server Roles and Zones](01_DNS_Server_Roles_and_Zones.md)
2. [DHCP Server Scopes and Relay](02_DHCP_Server_Scopes_and_Relay.md)
3. [Linux Web Server Reverse Proxy](03_Linux_Web_Server_Reverse_Proxy.md)
4. [SSH SFTP Remote Management](04_SSH_SFTP_Remote_Management.md)
5. [Time Synchronization NTP Logging](05_Time_Synchronization_NTP_Logging.md)
6. [Backups Storage and Availability](06_Backups_Storage_and_Availability.md)

**Additional chapter files:** [Practical Lab](98_Practice_Lab.md) · [Quiz & Answers](99_Quiz_Answers.md)

## Four-minute chapter review

1. இந்த chapter-இன் ஒவ்வொரு tool/protocol-க்கும் **who communicates with whom** எழுதுங்கள்.
2. ஒரு normal path மற்றும் ஒரு failure path வரைந்து விளக்குங்கள்.
3. "What is observable? What remains encrypted/private?" என்று கேளுங்கள்.
4. ஒன்றே ஒரு root cause-ஐ ஆதாரம் இல்லாமல் அறிவிக்காமல், alternate cause ஒன்றைச் சேருங்கள்.
5. Advanced concept practical deploy ஆகும் போது version/support/dependency சரிபார்க்கவும்.

## Authoritative background

- [RFC 9460 DNS SVCB/HTTPS](https://www.rfc-editor.org/rfc/rfc9460)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
