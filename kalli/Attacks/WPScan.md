# Kali Linux Inbuilt Package #12: WPScan (`wpscan`) Technical Reference & Setup Guide

---

## 1. Deep Technical Introduction & Architecture (ஆழ்ந்த தொழில்நுட்ப அறிமுகம்)

**WPScan** என்பது Kali Linux-ல் இயல்பாகவே (Inbuilt) வரும் **WordPress-குறிப்பிட்ட Vulnerability Scanner** ஆகும். உலகின் வெப்சைட்களில் 40%-க்கும் மேல் WordPress-ல் இயங்குவதால், இந்தப் பிளாட்ஃபார்மின் Core, Plugins, மற்றும் Themes-ல் உள்ள பாதுகாப்பு பலவீனங்களை மட்டும் குறிவைத்துச் சோதிக்க இந்தத் டூல் உருவாக்கப்பட்டது.

### ஆழமான தொழில்நுட்பக் கூறுகள் (Core Architecture & Mechanics):

* **WPVulnDB / WPScan Vulnerability Database:**
  * ஒவ்வொரு ஸ்கேனும் WPScan-ன் ஆன்லைன் பாதுகாப்பு டேட்டாபேஸுடன் (WPVulnDB) இணைந்து, கண்டறியப்பட்ட Plugin/Theme/Core பதிப்புகளுக்கு ஏற்ற அறியப்பட்ட CVE பலவீனங்களை ஒப்பிட்டுக் காட்டும் (இதற்கு API Token தேவைப்படும்).

* **Version & Fingerprint Detection:**
  * Meta Tags, readme.html, static கோப்புகளின் Hash மதிப்புகள் ஆகியவற்றை பகுப்பாய்வு செய்து, WordPress Core, Plugins மற்றும் Themes-ன் சரியான பதிப்பு எண்ணை துல்லியமாகக் கண்டறியும்.

* **User Enumeration Engine:**
  * `/?author=1` போன்ற URL Redirects, JSON REST API (`/wp-json/wp/v2/users`), மற்றும் Login Error செய்திகள் மூலம் WordPress சைட்டில் பதிவு செய்யப்பட்ட பயனர்பெயர்களைக் கண்டறியும்.

* **Password Brute-Force Module:**
  * `wp-login.php` மற்றும் XML-RPC (`xmlrpc.php`) வழியாக, கண்டறியப்பட்ட பயனர்பெயர்களுக்கு அகராதி (Wordlist) அடிப்படையிலான பாஸ்வேர்டு சோதனையை இயக்கும்.

* **Infrastructure Use Case (உங்கள் லேப் / கடையின் நெட்வொர்க் சோதனைக்கு):**
  * உங்கள் கேமிங் சென்டருக்காகவோ அல்லது வாடிக்கையாளருக்காகவோ WordPress-ல் உருவாக்கிய வெப்சைட்டில், பழைய Plugin/Theme பதிப்புகள் காரணமாக பாதுகாப்பு ஓட்டை உள்ளதா எனச் சோதிக்க இது பயன்படுகிறது.

---

## 2. Package Setup & Update Guide (நிறுவும் மற்றும் புதுப்பிக்கும் முறை)

Kali Linux-ல் WPScan ஏற்கனவே இன்ஸ்டால் செய்யப்பட்டிருக்கும்.

# 1. WPScan இன்ஸ்டால் செய்யப்பட்டுள்ளதா மற்றும் பதிப்பைச் சரிபார்க்க
wpscan --version

# 2. System Packages மற்றும் WPScan-ஐ புதுப்பிக்க
sudo apt update && sudo apt install wpscan -y

# 3. WPVulnDB-யின் முழு பலவீனப் பட்டியலைப் பார்க்க WPScan.com-ல் இருந்து இலவச API Token பதிவு செய்து பின்வருமாறு பயன்படுத்தவும்
wpscan --api-token YOUR_API_TOKEN_HERE --url http://192.168.1.100

## WPScan கட்டளையின் அடிப்படை வடிவம்:
wpscan --url [Target_URL] [Options]

---

## Categorized Command Reference & Syntax (கருவிகள் மற்றும் விளக்கங்கள்)

# A. Basic & Core Scanning (அடிப்படை ஸ்கேனிங்)
wpscan --url http://192.168.1.100 : இலக்கு WordPress சைட்டின் Core பதிப்பு மற்றும் அடிப்படை பாதுகாப்பு தலைப்புகளைச் சோதிக்கும் (--url = Target).
wpscan --url http://192.168.1.100 --random-user-agent : ஒவ்வொரு கோரிக்கையிலும் வேறுபட்ட Browser User-Agent-ஐப் பயன்படுத்தி கண்டறியப்படாமல் சோதிக்கும்.

# B. Plugin & Theme Enumeration (பிளக்-இன் மற்றும் தீம் கண்டுபிடிப்பு)
wpscan --url http://192.168.1.100 --enumerate p : இன்ஸ்டால் செய்யப்பட்டுள்ள அனைத்து Plugins-ஐயும் கண்டறியும் (--enumerate p = Plugins).
wpscan --url http://192.168.1.100 --enumerate vp : பாதுகாப்பு பலவீனம் உள்ள (Vulnerable) Plugins-ஐ மட்டும் கண்டறியும் (vp = Vulnerable Plugins).
wpscan --url http://192.168.1.100 --enumerate t : இன்ஸ்டால் செய்யப்பட்டுள்ள Theme-ஐக் கண்டறியும் (t = Themes).

# C. User Enumeration (பயனர்பெயர் கண்டுபிடிப்பு)
wpscan --url http://192.168.1.100 --enumerate u : WordPress-ல் பதிவு செய்யப்பட்டுள்ள அனைத்து பயனர்பெயர்களையும் கண்டறியும் (u = Users).
wpscan --url http://192.168.1.100 --enumerate u1-10 : குறிப்பிட்ட User ID வரம்பில் (1 முதல் 10 வரை) பயனர்களைத் தேடும்.

# D. Password Brute-Forcing (கடவுச்சொல் சோதனை)
wpscan --url http://192.168.1.100 --passwords /usr/share/wordlists/rockyou.txt --usernames admin : `admin` பயனர்பெயருக்கு rockyou.txt அகராதியைப் பயன்படுத்திக் கடவுச்சொல்லைச் சோதிக்கும்.
wpscan --url http://192.168.1.100 -U users.txt -P pass.txt : பல பயனர்பெயர்கள் மற்றும் பாஸ்வேர்டு கோப்புகளை ஒருங்கே பயன்படுத்திச் சோதிக்கும் (-U = Usernames File, -P = Passwords File).

# E. Output & API Token Options (முடிவுகளைச் சேமித்தல்)
wpscan --url http://192.168.1.100 --api-token YOUR_TOKEN -o report.txt : WPVulnDB CVE தகவல்களுடன் முழு அறிக்கையை ஒரு கோப்பில் சேமிக்கும் (-o = Output File).
wpscan --url http://192.168.1.100 -f json -o report.json : முடிவுகளை JSON வடிவில் சேமித்து, மற்ற Automation டூல்களில் Import செய்ய வசதியாக்கும் (-f = Format).
