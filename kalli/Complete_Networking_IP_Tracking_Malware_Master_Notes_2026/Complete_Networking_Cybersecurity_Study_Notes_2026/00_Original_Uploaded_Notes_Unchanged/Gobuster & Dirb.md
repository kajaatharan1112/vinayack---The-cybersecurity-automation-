# Kali Linux Inbuilt Package #11: Gobuster & Dirb (`gobuster` / `dirb`) Technical Reference & Setup Guide

---

## 1. Deep Technical Introduction & Architecture (ஆழ்ந்த தொழில்நுட்ப அறிமுகம்)

**Gobuster** மற்றும் **Dirb** என்பவை Kali Linux-ல் இயல்பாகவே (Inbuilt) வரும் **Directory & File Brute-Forcing Tools** ஆகும். ஒரு வெப்சைட்டில் பகிரங்கமாகத் தெரியாத (Hidden) கோப்புறைகள், கோப்புகள், மற்றும் Subdomains-ஐ அகராதி (Wordlist) அடிப்படையில் கண்டறிய இவை பயன்படுகின்றன.

### ஆழமான தொழில்நுட்பக் கூறுகள் (Core Architecture & Mechanics):

* **Wordlist-Based URL Guessing:**
  * இலக்கு URL-ன் முடிவில் ஒரு அகராதியில் (உதா: `/usr/share/wordlists/dirb/common.txt`) உள்ள ஒவ்வொரு வார்த்தையையும் இணைத்து (உதா: `example.com/admin`), ஒவ்வொரு கோரிக்கைக்கும் வரும் HTTP Status Code (200, 403, 404) அடிப்படையில் அந்த பாதை (Path) உண்மையில் இருக்கிறதா என்பதைக் கண்டறியும்.

* **Gobuster-ன் Go Language Concurrency Engine:**
  * `Go` நிரலாக்க மொழியில் எழுதப்பட்டதால், Gobuster பல Threads-ஐ ஒரே நேரத்தில் இயக்கி (Goroutines), Dirb-ஐ விட பல மடங்கு வேகமாக பெரிய அகராதிகளைச் சோதிக்க முடியும்.

* **Multiple Operating Modes:**
  * **`dir` mode:** கோப்புறைகள் மற்றும் கோப்புகளைக் கண்டறிய.
  * **`dns` mode:** Subdomains-ஐக் கண்டறிய (உதா: `mail.example.com`, `dev.example.com`).
  * **`vhost` mode:** ஒரே IP-யில் வேறுபட்ட Virtual Hosts/Domains இயங்குகின்றனவா எனக் கண்டறிய.

* **Response Filtering & Extensions:**
  * Status Code, Content-Length அடிப்படையில் தேவையற்ற பதில்களை வடிகட்டவும், `.php`, `.txt`, `.bak` போன்ற Extensions-ஐ இணைத்துத் தேடவும் முடியும்.

* **Infrastructure Use Case (உங்கள் லேப் / கடையின் நெட்வொர்க் சோதனைக்கு):**
  * உங்கள் கேமிங் சென்டரின் லோக்கல் பில்லிங் வெப் பேனலில் யாரும் அறியாமல் விட்டுவிட்ட `/backup`, `/admin`, `/.git` போன்ற ஆபத்தான கோப்புறைகள் வெளிப்படையாக உள்ளனவா என்பதைக் கண்டறிய இது பயன்படுகிறது.

---

## 2. Package Setup & Update Guide (நிறுவும் மற்றும் புதுப்பிக்கும் முறை)

Kali Linux-ல் Gobuster மற்றும் Dirb ஆகிய இரண்டும் ஏற்கனவே இன்ஸ்டால் செய்யப்பட்டிருக்கும்.

# 1. Gobuster மற்றும் Dirb பதிப்புகளைச் சரிபார்க்க
gobuster version
dirb

# 2. System Packages மற்றும் இரு டூல்களையும் புதுப்பிக்க
sudo apt update && sudo apt install gobuster dirb -y

# 3. இயல்புநிலை அகராதிகள் Kali-ல் எங்கே சேமிக்கப்பட்டுள்ளன என அறிய
ls /usr/share/wordlists/dirb/
ls /usr/share/wordlists/dirbuster/

## அடிப்படை கட்டளை வடிவம்:
gobuster dir -u [Target_URL] -w [Wordlist_Path]
dirb [Target_URL] [Wordlist_Path]

---

## Categorized Command Reference & Syntax (கருவிகள் மற்றும் விளக்கங்கள்)

# A. Directory & File Discovery (கோப்புறை மற்றும் கோப்பு கண்டுபிடிப்பு)
gobuster dir -u http://192.168.1.100 -w /usr/share/wordlists/dirb/common.txt : Common அகராதியைப் பயன்படுத்தி மறைந்துள்ள கோப்புறைகளைக் கண்டறியும் (-u = URL, -w = Wordlist).
dirb http://192.168.1.100 /usr/share/wordlists/dirb/common.txt : அதே பணியை Dirb மூலம் மெதுவான ஆனால் எளிமையான முறையில் செய்யும்.
gobuster dir -u http://192.168.1.100 -w big.txt -x php,txt,bak : `.php`, `.txt`, `.bak` Extensions-ஐச் சேர்த்து ஒவ்வொரு வார்த்தையையும் சோதிக்கும் (-x = Extensions).

# B. Response Filtering & Tuning (பதில்களை வடிகட்டுதல்)
gobuster dir -u http://192.168.1.100 -w big.txt -s 200,301 : 200 (Found) மற்றும் 301 (Redirect) Status Codes மட்டும் உள்ள முடிவுகளைக் காட்டும் (-s = Status Codes).
gobuster dir -u http://192.168.1.100 -w big.txt -b 403,404 : 403/404 Status Codes கொண்ட முடிவுகளைத் தவிர்த்து மற்றவற்றைக் காட்டும் (-b = Blacklist).
gobuster dir -u http://192.168.1.100 -w big.txt -t 50 : ஒரே நேரத்தில் 50 Threads மூலம் வேகமாகச் சோதிக்கும் (-t = Threads).

# C. Subdomain & Virtual Host Enumeration (சப்டொமைன் கண்டுபிடிப்பு)
gobuster dns -d example.com -w subdomains.txt : குறிப்பிட்ட டொமைனின் சப்டொமைன்களை (mail., dev., test. etc.) கண்டறியும் (-d = Domain).
gobuster vhost -u http://192.168.1.100 -w vhosts.txt : ஒரே IP முகவரியில் மறைந்துள்ள வெவ்வேறு Virtual Hosts-ஐக் கண்டறியும்.

# D. Authenticated & HTTPS Scanning (அங்கீகரிக்கப்பட்ட சோதனை)
gobuster dir -u https://192.168.1.100 -w big.txt -k : SSL Certificate சரிபார்ப்பைத் தவிர்த்து (Self-Signed Certs-க்கு) HTTPS சோதனையை இயக்கும் (-k = No TLS Validation).
gobuster dir -u http://192.168.1.100 -w big.txt -U admin -P pass123 : Basic Authentication (Username/Password) கொண்ட வெப் பக்கங்களையும் சோதிக்கும்.

# E. Output Reporting Options (முடிவுகளைச் சேமிக்கும் முறை)
gobuster dir -u http://192.168.1.100 -w big.txt -o results.txt : முடிவுகளை ஒரு உரைக் கோப்பில் சேமிக்கும் (-o = Output File).
dirb http://192.168.1.100 common.txt -o dirb_results.txt : Dirb-ன் முடிவுகளையும் அதேபோல் கோப்பில் சேமிக்கும்.
