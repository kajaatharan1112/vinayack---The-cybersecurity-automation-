# Kali Linux Inbuilt Package #15: Searchsploit & Recon-ng (`searchsploit` / `recon-ng`) Technical Reference & Setup Guide

---

## 1. Deep Technical Introduction & Architecture (ஆழ்ந்த தொழில்நுட்ப அறிமுகம்)

**Searchsploit** என்பது Kali Linux-ல் இயல்பாகவே (Inbuilt) வரும் **Exploit-DB-ன் Offline Command Line Search Tool** ஆகும். இணையத்தை நாடாமலேயே, லோக்கலில் சேமிக்கப்பட்டுள்ள ஆயிரக்கணக்கான Exploits, Shellcodes மற்றும் Papers-ஐ வேகமாகத் தேட உதவுகிறது.

**Recon-ng** என்பது Kali Linux-ல் இயல்பாகவே வரும் ஒரு **Modular Web Reconnaissance Framework** ஆகும். Metasploit-ன் Interface போலவே, Modules, Workspaces மற்றும் Database ஆதரவுடன் OSINT தரவுகளை ஒழுங்கமைப்பாகச் சேகரித்து நிர்வகிக்க இது பயன்படுகிறது.

### ஆழமான தொழில்நுட்பக் கூறுகள் (Core Architecture & Mechanics):

* **Searchsploit-ன் Local Exploit-DB Mirror:**
  * `/usr/share/exploitdb/` என்ற இடத்தில் முழு Exploit-DB Database-ன் Offline நகலை வைத்திருக்கும். இதனால் இணைய இணைப்பு இல்லாத Isolated Lab சூழல்களிலும் வேகமாகத் தேடல் செய்ய முடியும்.

* **Keyword & CVE-Based Matching:**
  * மென்பொருள் பெயர், பதிப்பு எண் (உதா: `vsftpd 2.3.4`), அல்லது CVE ஐடி மூலம் பொருத்தமான Exploit Code-ஐக் கண்டறியும்.

* **Recon-ng-ன் Module & Marketplace Architecture:**
  * `MODULE_SEARCH`, `MARKETPLACE INSTALL` போன்ற கட்டளைகள் மூலம் தேவையான Modules-ஐ (Netcraft, Whois, Shodan, Hacker Target போன்ற Public APIs) தேவைக்கேற்ப நிறுவிக்கொள்ளலாம்.

* **Workspace-Based Data Persistence:**
  * ஒவ்வொரு இலக்கிற்கும் (Target) தனி Workspace உருவாக்கி, அதில் சேகரிக்கப்படும் Domains, Hosts, Contacts, Credentials ஆகியவற்றை உள்ளமைக்கப்பட்ட SQLite Database-ல் சேமித்து வைத்துக்கொள்ளும்.

* **Infrastructure Use Case (உங்கள் லேப் / கடையின் நெட்வொர்க் சோதனைக்கு):**
  * Nmap/Nikto மூலம் கண்டறியப்பட்ட ஒரு சேவையின் பதிப்பு எண்ணுக்கு ஏற்கனவே Public ஆக வெளியான Exploit உள்ளதா என Searchsploit மூலம் உடனடியாகச் சரிபார்க்கலாம்; Recon-ng மூலம் உங்கள் கேமிங் சென்டரின் டொமைன் தொடர்பான பகிரங்கத் தகவல்களை ஒழுங்கமைப்பாகச் சேகரிக்கலாம்.

---

## 2. Package Setup & Update Guide (நிறுவும் மற்றும் புதுப்பிக்கும் முறை)

Kali Linux-ல் Searchsploit மற்றும் Recon-ng ஆகிய இரண்டும் ஏற்கனவே இன்ஸ்டால் செய்யப்பட்டிருக்கும்.

# 1. Searchsploit மற்றும் Recon-ng பதிப்புகளைச் சரிபார்க்க
searchsploit -h
recon-ng --version

# 2. Searchsploit-ன் Local Exploit-DB Database-ஐப் புதுப்பிக்க
sudo searchsploit -u

# 3. System Packages மற்றும் Recon-ng-ஐ புதுப்பிக்க
sudo apt update && sudo apt install exploitdb recon-ng -y

## அடிப்படை கட்டளை வடிவம்:
searchsploit [Search_Term]
recon-ng (பின்னர் Console-க்குள் Modules-ஐ இயக்கவும்)

---

## Categorized Command Reference & Syntax (கருவிகள் மற்றும் விளக்கங்கள்)

# A. Searchsploit — Basic Search (அடிப்படை தேடல்)
searchsploit vsftpd 2.3.4 : குறிப்பிட்ட மென்பொருள் பெயர் மற்றும் பதிப்பிற்கான Exploits-ஐத் தேடும்.
searchsploit apache 2.4 : Apache Web Server-ன் குறிப்பிட்ட பதிப்பிற்கான பலவீனங்களைத் தேடும்.
searchsploit -w wordpress : முடிவுகளுடன் Exploit-DB-யின் நேரடி வலை URL-ஐயும் காட்டும் (-w = Show URL).

# B. Searchsploit — Filtering & Details (வடிகட்டுதல் மற்றும் விரிவான தகவல்)
searchsploit --exclude="dos" sql injection : "dos" (Denial of Service) என்ற வார்த்தை உள்ள முடிவுகளைத் தவிர்த்துத் தேடும்.
searchsploit -t joomla : தலைப்பில் (Title) மட்டும் குறிப்பிட்ட வார்த்தையைக் கொண்ட Exploits-ஐத் தேடும் (-t = Title Only).
searchsploit -x 12345 : குறிப்பிட்ட Exploit ID-யின் முழுமையான Source Code-ஐத் திரையில் காட்டும் (-x = Examine).
searchsploit -m 12345 : குறிப்பிட்ட Exploit கோப்பை நமது தற்போதைய டைரக்டரிக்கு நகலெடுக்கும் (-m = Mirror/Copy).

# C. Recon-ng — Workspace & Module Setup (பணியிடம் மற்றும் மாட்யூல் அமைத்தல்)
workspaces create gamingcenter : `gamingcenter` என்ற பெயரில் புதிய Workspace ஒன்றை உருவாக்கும்.
marketplace search whois : Whois தொடர்பான கிடைக்கக்கூடிய Modules-ஐத் தேடும்.
marketplace install recon/domains-hosts/hackertarget : குறிப்பிட்ட Module-ஐ நிறுவும்.
modules load recon/domains-hosts/hackertarget : நிறுவப்பட்ட Module-ஐப் பயன்படுத்த ஏற்றும் (Load).

# D. Recon-ng — Running Modules & Viewing Results (மாட்யூல்களை இயக்குதல் மற்றும் முடிவுகளைப் பார்த்தல்)
options set SOURCE example.com : தேடலுக்கான இலக்கு டொமைனை நிர்ணயிக்கும்.
run : ஏற்றப்பட்ட Module-ஐ இயக்கி தகவல் சேகரிப்பைத் தொடங்கும்.
show hosts : இதுவரை சேகரிக்கப்பட்ட அனைத்து Hosts/Subdomains-ஐயும் பட்டியலிடும்.
show contacts : சேகரிக்கப்பட்ட Email/Contact தகவல்களைப் பட்டியலிடும்.
