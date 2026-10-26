# Kali Linux Inbuilt Package #8: Hashcat (`hashcat`) Technical Reference & Setup Guide

---

## 1. Deep Technical Introduction & Architecture (ஆழ்ந்த தொழில்நுட்ப அறிமுகம்)

**Hashcat** என்பது Kali Linux-ல் இயல்பாகவே (Inbuilt) வரும் உலகின் மிக அதிவேகமான **GPU-Accelerated Password Recovery & Offline Hash Cracking Engine** ஆகும். இது CPU-வை விட பல நூறு மடங்கு வேகத்தில் இயங்கக்கூடிய கணினியின் கிராபிக்ஸ் கார்டுகளின் (NVIDIA CUDA / AMD OpenCL / Intel Compute Engines) வன்பொருள் ஆற்றலைப் பயன்படுத்தி, என்கிரிப்ட் செய்யப்பட்ட பாஸ்வேர்ட் ஹேஷ்களை (Hashes) ஆஃப்லைனில் சோதித்து மீட்டெடுக்கப் பயன்படுகிறது.

### ஆழமான தொழில்நுட்பக் கூறுகள் (Core Architecture & Mechanics):

* **GPU Compute Acceleration Engine (CUDA / OpenCL / Metal):**
  * சாதாரண CPU ஒரு விநாடிக்கு சில ஆயிரம் ஹேஷ்களை மட்டுமே சோதிக்கும் போது, Hashcat கணினியின் GPU Cores (Thousands of Parallel Cores) மூலம் ஒரு விநாடிக்கு பல பில்லியன் (Billions of Hashes/sec) ஹேஷ்களை கணக்கிட்டுச் சோதிக்கும் திறன் கொண்டது.

* **Attack Modes Subsystem (`-a` Parameter):**
  * **Straight / Wordlist Mode (`-a 0`):** அகராதியில் உள்ள வார்த்தைகளை நேரடியாக ஹேஷாக மாற்றி சோதிக்கும் முறை.
  * **Combination Mode (`-a 1`):** இரண்டு வெவ்வேறு அகராதிகளில் உள்ள வார்த்தைகளை ஒன்றுசேர்த்து (Word + Word) சோதிக்கும் முறை.
  * **Mask Attack Mode (`-a 3`):** குறிப்பிட்ட பாஸ்வேர்ட் வடிவத்தை (உதா: முதல் எழுத்து Capital, 4 எண்கள், 1 சிறப்பு குறியீடு) வரையறுத்து Brute-Force செய்யும் அதிவேக முறை.
  * **Hybrid Mode (`-a 6` / `-a 7`):** அகராதி வார்த்தைகளுடன் எண்கள்/குறியீடுகளை முன்னும் பின்னும் இணைத்து சோதிக்கும் முறை.

* **Hash Type Engine (`-m` Parameter):**
  * 400-க்கும் மேற்பட்ட சர்வதேச ஹேஷ் வடிவங்களை (MD5, SHA-256, SHA-512, Windows NTLM, Linux sha512crypt, WPA/WPA2 PBKDF2, ZIP, RAR, BitLocker) Hashcat ஆதரிக்கிறது.

* **Rule-Based Mutation Engine:**
  * அகராதியில் உள்ள வார்த்தைகளை தானியங்கு விதிகளின் (Rules - உதா: `best64.rule`) மூலம் உருமாற்றி (Capitalize, Append numbers, Leet speak) பில்லியன் கணக்கான புதிய சேர்க்கைகளை உருவாக்கக்கூடியது.

* **Infrastructure Use Case (உங்கள் லேப் / கடையின் நெட்வொர்க் சோதனைக்கு):**
  * உங்கள் கேமிங் சென்டர் நெட்வொர்க்கில் உள்ள விண்டோஸ் சிஸ்டங்களின் NTLM பாஸ்வேர்ட் ஹேஷ்கள், வைஃபை WPA2 Handshake ஹேஷ்கள் மற்றும் என்கிரிப்ட் செய்யப்பட்ட சிஸ்டம் பேக்-அப் கோப்புகளின் கடவுச்சொல் வலிமையை (Password Complexity) ஆஃப்லைனில் சோதிக்க Hashcat பயன்படுகிறது.


## 2. Package Setup & Benchmark Guide (நிறுவும் மற்றும் அமைக்கும் முறை)

**Hashcat பதிப்பைச் சரிபார்க்க:**
hashcat --version

# கணினியில் உள்ள GPU / CPU வன்பொருள் சாதனங்களை அறிய:
hashcat -I 

# Hashcat வன்பொருள் வேகச் சோதனை (General Benchmark)
hashcat -I

# Windows NTLM (Mode 1000) ஹேஷ் வேகத்தைச் மட்டும் சோதிக்க:
hashcat -b -m 1000

# Categorized Command Reference & Syntax (முக்கியமான கட்டளைகள் மற்றும் விளக்கங்கள்)
# A. Device & Performance Tuning (ஹார்டுவேர் மேலாண்மை)
குறிப்பிட்ட GPU சாதனத்தை மட்டும் தேர்வு செய்து இயக்க (-d):
hashcat -m 1000 -a 0 hashes.txt wordlist.txt -d 1

GPU வெப்பநிலை 80°C எட்டினால் சோதனையைத் தானாக நிறுத்த (--gpu-temp-abort):
hashcat -m 1000 -a 0 hashes.txt wordlist.txt --gpu-temp-abort=80

வேலைப்பளுவை அதிகரித்து அதிகபட்ச GPU ஆற்றலைப் பயன்படுத்த (-w 3 Workload Profile):
hashcat -m 1000 -a 0 hashes.txt wordlist.txt -w 3

# B. Wordlist & Combination Attacks (அகராதி வழி சோதனைகள்)
MD5 Hashes-ஐ (Mode 0) Rockyou அகராதி கொண்டு உடைக்க:
hashcat -m 0 -a 0 md5_hashes.txt /usr/share/wordlists/rockyou.txt

Windows NTLM Hashes-ஐ (Mode 1000) உடைக்க:
hashcat -m 1000 -a 0 ntlm_hashes.txt /usr/share/wordlists/rockyou.txt

Linux SHA-512 /etc/shadow Hashes-ஐ (Mode 1800) உடைக்க:
hashcat -m 1800 -a 0 linux_hashes.txt /usr/share/wordlists/rockyou.txt

Wi-Fi WPA/WPA2 PMKID / Handshake-ஐ (Mode 22000) உடைக்க:
hashcat -m 22000 -a 0 wpa.hc22000 /usr/share/wordlists/rockyou.txt

இரண்டு அகராதிகளை இணைத்து (Combination Mode -a 1) சோதிக்க:
hashcat -m 1000 -a 1 ntlm_hashes.txt dict1.txt dict2.txt

# C. Mask Attacks & Brute-Force (அனுமான முறையிலான தாக்குதல் - -a 3)
Mask குறியீடுகளின் விளக்கம் (Mask Symbols Reference):
?l = a-z சிற்றெழுத்துகள் | ?u = A-Z பேரெழுத்துகள் | ?d = 0-9 எண்கள் | ?s = Special Chars சிறப்புக் குறியீடுகள் | ?a = All Chars அனைத்து வகை எழுத்துகளும்

8 எண்கள் கொண்ட பாஸ்வேர்டுகளை மட்டும் வேகமாக Brute-force செய்ய (உதா: 12345678):
hashcat -m 1000 -a 3 ntlm_hashes.txt ?d?d?d?d?d?d?d?d

1 Capital + 5 Small + 2 Digits பாஸ்வேர்டுகளைச் சோதிக்க (உதா: Server12):
hashcat -m 1000 -a 3 ntlm_hashes.txt ?u?l?l?l?l?l?d?d

Custom Character Set வரையறுத்து 6 எழுத்து பாஸ்வேர்டுகளைச் சோதிக்க:
hashcat -m 1000 -a 3 -1 ?l?d?s ntlm_hashes.txt ?1?1?1?1?1?1

# D. Rule-Based Attacks (உருமாற்ற விதிகள்)
best64 விதிகளைப் பயன்படுத்தி அகராதி வார்த்தைகளை உருமாற்றிச் சோதிக்க (-r):
hashcat -m 1000 -a 0 ntlm_hashes.txt wordlist.txt -r /usr/share/hashcat/rules/best64.rule

அகராதி வார்த்தைகளின் பின்னால் 4 எண்களை இணைத்துச் சோதிக்க (Hybrid Mode -a 6):
hashcat -m 1000 -a 6 ntlm_hashes.txt wordlist.txt ?d?d?d?d

# E. Session Control & Output Commands (முடிவுகள் மற்றும் மேலாண்மை)
கண்டுபிடிக்கப்பட்ட பாஸ்வேர்டுகளை மட்டும் தெளிவாகத் திரையில் பார்க்க (--show):
hashcat -m 1000 hashes.txt --show

பாதியில் நின்ற Hashcat சோதனையை மீண்டும் தொடர (--restore):
hashcat --restore

ஓடிக்கொண்டிருக்கும் சோதனையின் நேரலை முன்னேற்றத்தைப் பார்க்க (--status):
hashcat -m 1000 hashes.txt --status