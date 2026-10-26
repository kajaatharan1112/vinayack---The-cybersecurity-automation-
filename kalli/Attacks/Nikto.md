# Kali Linux Inbuilt Package #10: Nikto (`nikto`) Technical Reference & Setup Guide

---

## 1. Deep Technical Introduction & Architecture (ஆழ்ந்த தொழில்நுட்ப அறிமுகம்)

**Nikto** என்பது Kali Linux-ல் இயல்பாகவே (Inbuilt) வரும் ஒரு **Open-Source Web Server Vulnerability Scanner** ஆகும். ஒரு இணைய சர்வரில் (Web Server) பழைய/பாதுகாப்பற்ற சாஃப்ட்வேர் பதிப்புகள், ஆபத்தான கோப்புகள் மற்றும் தவறான அமைப்புகள் (Misconfigurations) உள்ளனவா எனக் விரைவாகக் கண்டறிய இது பயன்படுகிறது.

### ஆழமான தொழில்நுட்பக் கூறுகள் (Core Architecture & Mechanics):

* **Signature-Based Scanning Engine:**
  * Nikto தனது உள்ளமைக்கப்பட்ட டேட்டாபேஸில் (`nikto_db`) 6000-க்கும் மேற்பட்ட ஆபத்தான கோப்புகள்/CGI-கள், 1250-க்கும் மேற்பட்ட பழைய சர்வர் பதிப்புகள், மற்றும் 270-க்கும் மேற்பட்ட சர்வர்-குறிப்பிட்ட பிரச்சினைகளின் பட்டியலை வைத்துக்கொண்டு, இலக்கு சர்வரிடமிருந்து வரும் HTTP பதில்களை ஒப்பிட்டுப் பரிசோதிக்கிறது.

* **Server & Header Fingerprinting:**
  * HTTP Response Headers-ல் உள்ள `Server`, `X-Powered-By` போன்ற தலைப்புகளை வாசித்து, இலக்கு சர்வர் எந்த மென்பொருள் (Apache/Nginx/IIS) மற்றும் எந்தப் பதிப்பில் இயங்குகிறது என்பதைக் கண்டறியும்.

* **Plugin-Based Modular Design:**
  * SSL சோதனை, Cookie பகுப்பாய்வு, HTTP Methods சோதனை (PUT/DELETE/TRACE) போன்ற பல தனிப் பணிகளை செய்ய தனித்தனி Plugins-ஐக் கொண்டுள்ளது; `-Plugins` option மூலம் குறிப்பிட்ட Plugin-ஐ மட்டும் இயக்கலாம்.

* **Evasion Techniques (`-evasion`):**
  * Intrusion Detection Systems (IDS) கண்டுபிடிக்காமல் இருக்க, URL Encoding, Directory Self-Reference போன்ற 9 வகையான Evasion நுட்பங்களை ஆதரிக்கிறது.

* **Infrastructure Use Case (உங்கள் லேப் / கடையின் நெட்வொர்க் சோதனைக்கு):**
  * உங்கள் கேமிங் சென்டரில் உள்ள லோக்கல் பில்லிங் வெப் பேனல் அல்லது ரவுட்டர் Admin Panel பழைய/பாதுகாப்பற்ற சாஃப்ட்வேர் பதிப்பில் இயங்குகிறதா, அல்லது வெளியில் தெரியக்கூடாத Backup/Config கோப்புகள் வெளிப்படையாக உள்ளனவா என்பதை நிமிடங்களில் கண்டறிய இது பயன்படுகிறது.

---

## 2. Package Setup & Update Guide (நிறுவும் மற்றும் புதுப்பிக்கும் முறை)

Kali Linux-ல் Nikto ஏற்கனவே இன்ஸ்டால் செய்யப்பட்டிருக்கும்.

# 1. Nikto இன்ஸ்டால் செய்யப்பட்டுள்ளதா மற்றும் பதிப்பைச் சரிபார்க்க
nikto -Version

# 2. System Packages மற்றும் Nikto-ஐ புதுப்பிக்க
sudo apt update && sudo apt install nikto -y

# 3. Nikto-ன் உள்ளமைக்கப்பட்ட பாதுகாப்பு டேட்டாபேஸைப் புதுப்பிக்க
nikto -update

## Nikto கட்டளையின் அடிப்படை வடிவம்:
nikto -h [Target_URL_or_IP] [Options]

---

## Categorized Command Reference & Syntax (கருவிகள் மற்றும் விளக்கங்கள்)

# A. Basic Scanning (அடிப்படை ஸ்கேனிங்)
nikto -h http://192.168.1.100 : குறிப்பிட்ட வெப் சர்வரில் முழுமையான Default Scan-ஐ இயக்கும் (-h = Host).
nikto -h 192.168.1.100 -p 8080 : இயல்புநிலை 80 போர்ட்டிற்குப் பதிலாக குறிப்பிட்ட போர்ட்டில் (8080) சோதனையை இயக்கும் (-p = Port).
nikto -h https://example.com -ssl : HTTPS/SSL பாதுகாப்புடன் இயங்கும் வெப்சைட்டை இலக்காகக் கொண்டு சோதிக்கும்.

# B. Scan Tuning & Scope Control (சோதனையின் எல்லையை நிர்ணயித்தல்)
nikto -h 192.168.1.100 -Tuning 1,2,3 : குறிப்பிட்ட வகையான சோதனைகளை மட்டும் தேர்வு செய்து இயக்கும் (உதா: 1=File Upload, 2=Misconfig, 3=Info Disclosure).
nikto -h 192.168.1.100 -Tuning x6 : XSS தொடர்பான சோதனைகளை மட்டும் தவிர்த்து மற்ற அனைத்தையும் இயக்கும் (-Tuning x = Exclude).
nikto -h 192.168.1.100 -timeout 10 : ஒவ்வொரு கோரிக்கைக்கும் எத்தனை விநாடிகள் பதிலுக்காகக் காத்திருக்க வேண்டும் என நிர்ணயிக்கும்.

# C. Evasion & Stealth Options (கண்டறியப்படாமல் சோதிக்கும் முறை)
nikto -h 192.168.1.100 -evasion 1 : URL Encoding மூலம் IDS/Firewall கண்டுபிடிக்காமல் மறைவாகச் சோதனையை இயக்கும்.
nikto -h 192.168.1.100 -useproxy http://127.0.0.1:8080 : Burp Suite போன்ற Proxy Tool வழியாகத் தரவைச் செலுத்தி பாக்கெட்டுகளை ஆராயவும் இடைமறிக்கவும் உதவும்.

# D. Output Reporting Options (முடிவுகளைச் சேமிக்கும் முறை)
nikto -h 192.168.1.100 -o report.txt : ஸ்கேன் முடிவுகளை ஒரு உரைக் கோப்பில் சேமிக்கும் (-o = Output File).
nikto -h 192.168.1.100 -o report.html -Format htm : முடிவுகளை பார்வைக்கு ஏற்ற HTML அறிக்கையாக சேமிக்கும்.
nikto -h 192.168.1.100 -o report.xml -Format xml : முடிவுகளை XML வடிவில் சேமித்து, மற்ற Automation டூல்களில் Import செய்ய வசதியாக்கும்.
