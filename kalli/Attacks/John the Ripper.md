# Kali Linux Inbuilt Package #7: John the Ripper (`john`) Technical Reference & Setup Guide

---

## 1. Deep Technical Introduction & Architecture (ஆழ்ந்த தொழில்நுட்ப அறிமுகம்)

**John the Ripper** என்பது Kali Linux-ல் இயல்பாகவே (Inbuilt) வரும் உலகின் மிகப்பிரபலமான **Offline Password Hash Cracking & Security Auditing Tool** ஆகும். இது நெட்வொர்க் வழியாக இயங்காமல், லோக்கல் கணினியில் உள்ள என்கிரிப்ட் செய்யப்பட்ட பாஸ்வேர்ட் ஹேஷ்களை (Linux `/etc/shadow`, Windows SAM, ZIP, PDF, SSH Private Keys) அதிவேகமாக அனலைஸ் செய்து உடைக்கப்பயன்படும் ஒரு பிரதான தடயவியல் மற்றும் பாதுகாப்பு சோதனைக் கருவியாகும்.

### ஆழமான தொழில்நுட்பக் கூறுகள் (Core Architecture & Mechanics):

* **Offline Hash Analysis Engine:**
  * இது நெட்வொர்க் தொடர்பைப் பயன்படுத்தாது. சிஸ்டத்திலிருந்து சேகரிக்கப்பட்ட Encrypted Password Hashes-ஐக் கொண்டு, CPU வளங்களைப் பயன்படுத்தி (Multi-Core Processing) ஆஃப்லைனில் சோதனைகளை இயக்கும்.

* **Cracking Modes & Mutation Mechanics:**
  * **Single Crack Mode:** பயனர்பெயர் (Username) மற்றும் முகவரித் தகவல்களைக் கொண்டு பாஸ்வேர்டை யூகிக்கும் மிக வேகமான முறை.
  * **Wordlist Mode:** அகராதியில் (Wordlist) உள்ள வார்த்தைகளை ஹேஷாக மாற்றி, இலக்கு ஹேஷுடன் ஒப்பிடும் முறை.
  * **Incremental Mode (Brute-Force):** அனைத்து எழுத்துக்கள், எண்கள் மற்றும் சிறப்பு குறியீடுகளின் சாத்தியமான சேர்க்கைகளையும் (All Combinations) வரிசையாகச் சோதிக்கும் முறை.
  * **Rules Engine (`john.conf`):** அகராதியில் உள்ள சாதாரண வார்த்தைகளை உருமாற்றி (Mutations - உதா: `admin` என்பதை `Adm!n2024` என மாற்றி) சோதிக்கும் சக்திவாய்ந்த இன்ஜின்.

* **`2john` Conversion Utilities Subsystem:**
  * வெவ்வேறு கோப்பு வடிவங்களில் உள்ள கடவுச்சொற்களை John the Ripper புரிந்து கொள்ளும் ஹேஷ் வடிவத்திற்கு மாற்ற பல துணைக்கருவிகள் இதனுடன் இணைந்து வருகின்றன (உதா: `zip2john`, `pdf2john`, `ssh2john`, `unshadow`).

* **Infrastructure Use Case (உங்கள் லேப் / கடையின் நெட்வொர்க் சோதனைக்கு):**
  * உங்கள் கேமிங் சென்டர் லினக்ஸ் சர்வர்கள் அல்லது விண்டோஸ் பிசிகளில் உள்ள பயனர் கணக்குகளுக்குப் பலவீனமான கடவுச்சொற்கள் அமைக்கப்பட்டுள்ளவா என்பதை ஆஃப்லைனில் சோதிக்கவும், என்கிரிப்ட் செய்யப்பட்ட Backup ZIP/RAR கோப்புகளின் கடவுச்சொற்களை மீட்டெடுக்கவும் இது பயன்படுகிறது.

---

## 2. Package Setup & Execution Guide (நிறுவும் மற்றும் அமைக்கும் முறை)

John the Ripper Kali Linux-ல் இயல்பாகவே நிறுவப்பட்டிருக்கும்.

# 1. John the Ripper இன்ஸ்டால் செய்யப்பட்டுள்ளதா மற்றும் பதிப்பைச் சரிபார்க்க
john --head
# அல்லது
john --list=build-info

# 2. Kali Linux-ல் உள்ள பிரதான Wordlist கோப்பை (rockyou.txt) பிரித்தெடுக்க
sudo gunzip /usr/share/wordlists/rockyou.txt.gz

# 3. John ஆதரவு அளிக்கும் Hash Formats பட்டியலைப் பார்க்க
john --list=formats

## Categorized Command Reference & Syntax (கருவிகள் மற்றும் விளக்கங்கள்)
John கட்டளையின் அடிப்படை வடிவம்: john [options] [hash_file]

# A. Helper Tools (ஹேஷை பிரித்தெடுக்கும் 2john கருவிகள்)
unshadow /etc/passwd /etc/shadow > passwords.hashes : லினக்ஸ் OS-ல் உள்ள /etc/passwd மற்றும் /etc/shadow கோப்புகளை ஒன்றுசேர்த்து John வாசிக்கும் ஹேஷ் கோப்பாக மாற்றும்.
zip2john protected.zip > zip.hash : பாஸ்வேர்ட் பாதுகாக்கப்பட்ட ZIP கோப்பிலிருந்து ஹேஷைப் பிரித்தெடுக்கும்.
pdf2john document.pdf > pdf.hash : பாஸ்வேர்ட் வைக்கப்பட்ட PDF கோப்பிலிருந்து ஹேஷைப் பிரித்தெடுக்கும்.
ssh2john id_rsa > ssh.hash : என்கிரிப்ட் செய்யப்பட்ட SSH Private Key கோப்பிலிருந்து ஹேஷைப் பிரித்தெடுக்கும்.

# B. Basic Cracking Modes (அடிப்படை சோதனைகள்)
john passwords.hashes : தானியங்கி முறையில் (Auto-detect format) ஹேஷை அனலைஸ் செய்து சோதனையைத் தொடங்கும்.
john --single passwords.hashes : பயனர்பெயர் மற்றும் சிஸ்டம் விபரங்களை வைத்து வேகமாகச் சோதிக்கும் (Single Crack Mode).
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt : rockyou.txt அகராதியைப் பயன்படுத்தி ஹேஷை உடைக்க முயற்சிக்கும் (Wordlist Mode).
john --incremental hash.txt : அனைத்து சாத்தியமான குறியீடுகளையும் பயன்படுத்தி Brute-Force சோதனையை இயக்கும் (Incremental Mode).

# C. Specific Hash Formats & Rules (குறிப்பிட்ட ஹேஷ் வடிவங்கள் & விதிகள் - --format & --rules)
john --format=raw-md5 hash.txt : குறிப்பிட்ட MD5 ஹேஷ் வடிவத்தை மட்டும் தேர்வு செய்து சோதிக்கும்
john --format=NT hash.txt : Windows NTLM பாஸ்வேர்ட் ஹேஷ்களைச் சோதிக்கும்.
john --format=sha512crypt passwords.hashes : நவீன Linux (Ubuntu/Debian) SHA-512 பாஸ்வேர்ட் ஹேஷ்களைச் சோதிக்கும்.
john --wordlist=words.txt --rules hash.txt : அகராதியில் உள்ள வார்த்தைகளுக்கு john.conf-ல் உள்ள உருமாற்ற விதிகளைத் (Rules/Mutations) தழுவி சோதிக்கும்.

# D. Session Management & Output Controls (முடிவுகள் மற்றும் மேலாண்மை)
john --show hash.txt : ஏற்கனவே கண்டுபிடிக்கப்பட்ட பாஸ்வேர்டுகளைத் திரையில் தெளிவான உரையாகக் (Plaintext) காட்டும்.
john --status : பின்புலத்தில் ஓடிக்கொண்டிருக்கும் சோதனையின் தற்போதைய நிலையை (Progress/Speed) காட்டும்.
john --restore : பாதியில் நின்ற பாஸ்வேர்ட் சோதனையை மீண்டும் தொடங்கும்.