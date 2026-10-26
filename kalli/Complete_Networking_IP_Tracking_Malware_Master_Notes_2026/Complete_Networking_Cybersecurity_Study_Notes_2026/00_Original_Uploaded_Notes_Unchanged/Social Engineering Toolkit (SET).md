# Kali Linux Inbuilt Package #17: Social Engineering Toolkit (`setoolkit`) Technical Reference & Setup Guide

---

## 1. Deep Technical Introduction & Architecture (ஆழ்ந்த தொழில்நுட்ப அறிமுகம்)

**Social Engineering Toolkit (SET)** என்பது Kali Linux-ல் இயல்பாகவே (Inbuilt) வரும் **Python அடிப்படையிலான Social Engineering Attack Simulation Framework** ஆகும். கணினி பாதுகாப்பு பலவீனங்களை அல்ல, மனிதர்களின் நம்பிக்கையைப் பயன்படுத்தி (Human Trust Exploitation) தாக்குதல்களை உருவகப்படுத்த (Simulate) இது பயன்படுகிறது — பொதுவாக ஊழியர்களுக்கான **Phishing Awareness Training** மற்றும் அங்கீகரிக்கப்பட்ட Red Team Engagements-ல் பயன்படுத்தப்படுகிறது.

> **முக்கிய குறிப்பு:** SET-ஐ உங்கள் சொந்த நிறுவனம்/நெட்வொர்க்கில், எழுத்துப்பூர்வ அனுமதியுடன் (Written Authorization) மட்டுமே பயன்படுத்த வேண்டும். மூன்றாம் தரப்பினரை இலக்காகக் கொண்டு அனுமதியின்றி Phishing செய்வது சட்டப்படி குற்றமாகும்.

### ஆழமான தொழில்நுட்பக் கூறுகள் (Core Architecture & Mechanics):

* **Menu-Driven Attack Vector Selection:**
  * Spear-Phishing, Website Cloning, Infectious Media Generator, Mass Mailer போன்ற பல்வேறு தாக்குதல் வகைகளை Interactive Text Menu மூலம் படிப்படியாகத் தேர்வு செய்யும் வகையில் வடிவமைக்கப்பட்டுள்ளது.

* **Website Attack Vectors (Credential Harvester):**
  * ஒரு உண்மையான Login பக்கத்தை (உதா: Company Portal) அப்படியே நகலெடுத்து (Clone), பயனர் அதில் தட்டச்சு செய்யும் Username/Password-ஐப் பதிவு செய்து, பின்னர் உண்மையான சைட்டிற்கு திருப்பிவிடும் Web Server Engine கொண்டது.

* **Spear-Phishing Attack Vector:**
  * SMTP Server வழியாக, தனிப்பயனாக்கப்பட்ட (Personalized) Email Templates மற்றும் Payload-இணைக்கப்பட்ட கோப்புகளை (PDF/DOC Exploit) இலக்கு பட்டியலுக்கு அனுப்பும் Module.

* **Integration with Metasploit:**
  * உருவாக்கப்படும் Payloads, Metasploit-ன் `multi/handler` உடன் நேரடியாக இணைந்து, Reverse Connection-ஐக் கையாளும் வகையில் வடிவமைக்கப்பட்டுள்ளது.

* **Infrastructure Use Case (உங்கள் லேப் / நிறுவனத்தின் பாதுகாப்பு விழிப்புணர்வு சோதனைக்கு):**
  * உங்கள் கேமிங் சென்டர்/நிறுவன ஊழியர்கள் சந்தேகத்திற்குரிய Login Links-ஐ அடையாளம் கண்டு தவிர்க்கிறார்களா என்பதை ஒரு கட்டுப்படுத்தப்பட்ட, அனுமதி பெற்ற Simulated Phishing பயிற்சி மூலம் மதிப்பிட இது பயன்படுகிறது.

---

## 2. Package Setup & Update Guide (நிறுவும் மற்றும் புதுப்பிக்கும் முறை)

Kali Linux-ல் SET ஏற்கனவே இன்ஸ்டால் செய்யப்பட்டிருக்கும்.

# 1. SET இன்ஸ்டால் செய்யப்பட்டுள்ளதா எனச் சரிபார்க்க
setoolkit --version

# 2. System Packages மற்றும் SET-ஐ புதுப்பிக்க
sudo apt update && sudo apt install set -y

# 3. SET-ஐத் தொடங்க (Root அனுமதி தேவை)
sudo setoolkit

## பயன்பாட்டு வடிவம்:
SET ஒரு Interactive Menu Tool — கீழே உள்ள எண்களை Console-க்குள் வரிசையாகத் தேர்வு செய்யவும்.

---

## Categorized Menu Reference & Workflow (மெனு விவரங்கள் மற்றும் செயல்முறை)

# A. Main Menu Navigation (முதன்மை மெனு வழிசெலுத்தல்)
1) Social-Engineering Attacks : மனிதர்களை இலக்காகக் கொண்ட தாக்குதல் வகைகளைத் தேர்வு செய்யும் பிரிவுக்குச் செல்லும்.
2) Penetration Testing (Fast-Track) : தானியங்கு Penetration Testing Scripts அடங்கிய பிரிவு.
99) Exit the Social-Engineer Toolkit : SET-லிருந்து வெளியேறும்.

# B. Website Attack Vectors (வெப்சைட் தாக்குதல் வழிமுறைகள்)
1) Java Applet Attack Method : Java Applet மூலம் Payload-ஐ பரப்பும் பழைய முறை (தற்போதைய Browsers-ல் வெகுவாகக் கட்டுப்படுத்தப்பட்டுள்ளது).
3) Credential Harvester Attack Method : Login பக்கத்தை நகலெடுத்து பயனர்பெயர்/பாஸ்வேர்டைச் சேகரிக்கும் முறை.
2) Site Cloner : இலக்கு வெப்சைட்டை முழுமையாக நகலெடுக்க URL-ஐக் கேட்கும்.

# C. Credential Harvester Workflow (பாஸ்வேர்ட் சேகரிப்பு செயல்முறை — லேப் சூழலில் மட்டும்)
set:webattack> IP address for the POST back in Harvester/Tabnabbing : சேகரிக்கப்படும் தரவு திரும்பப் பெறப்பட வேண்டிய Attacker கணினியின் IP முகவரியைக் கேட்கும்.
set:webattack> Enter the url to clone : நகலெடுக்கப்பட வேண்டிய உண்மையான Login பக்கத்தின் URL-ஐக் கேட்கும்.
[*] SET is now listening... : Clone செய்யப்பட்ட பக்கத்தில் யாரேனும் உள்நுழைந்தவுடன், அந்தத் தரவு Terminal-ல் நேரலையில் பதிவாகும்.

# D. Payload & Listener Setup (பேலோடு & கேட்பான் அமைத்தல்)
4) Create a Payload and Listener : ஒரு Standalone Payload-ஐ உருவாக்கி, அதற்கான Metasploit Listener-ஐ தானாகவே அமைக்கும்.
set:payloads> IP address for the reverse connection : Payload திரும்ப இணைக்க வேண்டிய Attacker கணினியின் IP முகவரியைக் கேட்கும்.

# E. Logs & Clean-Up (பதிவுகள் மற்றும் முடித்தல்)
சேகரிக்கப்பட்ட Credentials `/root/.set/reports/` கோப்புறையில் தானாகவே சேமிக்கப்படும் — பயிற்சி முடிந்தவுடன் இந்த Logs-ஐ பாதுகாப்பாக அழித்து, Participants-க்கு Awareness Debrief வழங்குவது சிறந்த நடைமுறையாகும்.
