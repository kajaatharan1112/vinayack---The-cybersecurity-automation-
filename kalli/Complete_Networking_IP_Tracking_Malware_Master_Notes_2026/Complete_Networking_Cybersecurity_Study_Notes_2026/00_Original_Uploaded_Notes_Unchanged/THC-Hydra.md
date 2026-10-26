# Kali Linux Inbuilt Package #2: THC-Hydra (`thc-hydra`) Technical Reference Guide

---

## 1. Deep Technical Introduction & Architecture (ஆழ்ந்த தொழில்நுட்ப அறிமுகம்)

**THC-Hydra** என்பது Kali Linux OS-ல் இயல்பாகவே (Inbuilt) வரும் உலகின் மிக அதிவேகமான மற்றும் நெட்வொர்க் அடிப்படையிலான **Online Credential Testing & Password Auditing Tool** ஆகும். 

ஒரு நெட்வொர்க்கில் இயங்கும் சர்வர்கள், ரவுட்டர்கள், ஃபயர்வால் மற்றும் டேட்டாபேஸ்கள் ஆகியவற்றின் உள்நுழைவுப் பாதுகாப்பை (Authentication Mechanism) சோதிக்க இது உலகளவில் பயன்படுத்தப்படுகிறது.

### ஆழமான தொழில்நுட்பக் கூறுகள் (Core Architecture & Mechanics):

* **Online Cracking vs Offline Cracking:**
  * **Offline Cracking (John the Ripper / Hashcat):** என்ட்ரிப்ட் செய்யப்பட்ட கடவுச்சொல் ஹேஷ்களை (Hashes) லோக்கலில் எடுத்துக்கொண்டு GPU வேகத்தில் உடைப்பது.
  * **Online Cracking (Hydra):** நேரலையில் இயங்கிக்கொண்டிருக்கும் ஒரு சேவைக்கு (Active Daemon / Service) நெட்வொர்க் வழியாகத் தொடர்புகொண்டு, பயனர்பெயர் மற்றும் பாஸ்வேர்டு சேர்க்கைகளைத் தொடர்ச்சியாக அனுப்பிச் சோதிப்பது.

* **Multi-Threaded Parallel Execution Engine:**
  * Hydra தனது பணிகளை மிக வேகமாக முடிக்க **Parallel Socket Connections**-ஐப் பயன்படுத்துகிறது. ஒரே நேரத்தில் பல நூறு Sockets-ஐத் திறந்து, ஒரே விநாடியில் பல நூறு கடவுச்சொல் முயற்சிகளைச் செலுத்தும் திறன் கொண்டது.

* **Multi-Protocol Support (50+ Protocols):**
  * SSH, FTP, Telnet, HTTP-GET, HTTP-POST, HTTPS, SMB, RDP (Windows Remote Desktop), VNC, MySQL, PostgreSQL, Oracle, Redis, MongoDB, POP3, IMAP, SNMP போன்ற 50-க்கும் மேற்பட்ட சர்வதேச நெட்வொர்க் புரோட்டோகால்களை இது ஆதரிக்கிறது.

* **Stateful Session Restore Mechanism:**
  * பெரிய அளவிலான பாஸ்வேர்ட் அகராதிகளை (Wordlists) சோதிக்கும் போது மின்சாரம் துண்டிக்கப்பட்டாலோ அல்லது நெட்வொர்க் ரத்தானாலோ, கடைசியாக நின்ற இடத்திலிருந்தே சோதனையை மீண்டும் தொடங்கும் **`hydra.restore`** கோப்பு முறையைக் கொண்டுள்ளது.

* **Infrastructure Use Case (உங்கள் லேப் / கடையின் சர்வர் சோதனைக்கு):**
  * உங்கள் கேமிங் சென்டர் லோக்கல் நெட்வொர்க்கில் உள்ள Switches, Routers, Linux Servers அல்லது Windows RDP பிசிக்களில் பலவீனமான Default Passwords (உதா: `admin/admin`, `root/123456`) உள்ளதா என்பதைத் திறந்து பார்க்காமலேயே சில விநாடிகளில் கண்டறிய Hydra பயன்படுகிறது.

---

## 2. Categorized Command Reference & Syntax (முக்கியமான கட்டளைகள் மற்றும் விளக்கங்கள்)

Hydra கட்டளையின் அடிப்படை வடிவம்: `hydra [options] [target_IP] [protocol]`

---

### A. Target & Credential Specification (பயனர் மற்றும் கடவுச்சொல் தேர்வு)

* **`hydra -l admin 192.168.1.1 ssh`** : `admin` என்ற ஒரு குறிப்பிட்ட பயனர்பெயருக்கு மட்டும் பாஸ்வேர்டுகளைச் சோதிக்கும் (`-l` = Single Login).
* **`hydra -L users.txt 192.168.1.1 ssh`** : ஒரு கோப்பில் உள்ள அனைத்து பயனர்பெயர்களையும் வரிசையாக எடுத்துச் சோதிக்கும் (`-L` = User List File).
* **`hydra -l admin -p Password123 192.168.1.1 ssh`** : குறிப்பிட்ட ஒரு பயனர்பெயர் மற்றும் ஒரு பாஸ்வேர்டை வைத்து இணைப்பு சரியாகிறதா எனச் சரிபார்க்கும் (`-p` = Single Password).
* **`hydra -l admin -P /usr/share/wordlists/rockyou.txt 192.168.1.1 ssh`** : Kali-ல் உள்ள மில்லியன் கணக்கான பாஸ்வேர்டுகள் கொண்ட `rockyou.txt` அகராதியைப் பயன்படுத்திச் சோதிக்கும் (`-P` = Password List File).
* **`hydra -C credentials.txt 192.168.1.1 ftp`** : `username:password` வடிவத்தில் உள்ள பட்டியலை நேரடியாகச் சோதிக்கும் (`-C` = Combo File).

---

### B. Thread & Performance Tuning (வேகம் மற்றும் பிணையக் கட்டுப்பாடு)

* **`hydra -t 16 -l root -P pass.txt 192.168.1.100 ssh`** : ஒரே நேரத்தில் 16 Parallel Threads மூலம் அதிவேகமாகச் சோதிக்கும் (`-t` = Thread Count).
* **`hydra -s 2222 -l admin -P pass.txt 192.168.1.100 ssh`** : இயல்புநிலை போர்ட்டிற்குப் (Default Port 22) பதிலாக மாற்று போர்ட் எண்ணை குறிப்பிடும் (`-s` = Custom Service Port).
* **`hydra -W 3 -l admin -P pass.txt 192.168.1.100 ssh`** : ஒவ்வொரு முயற்சிக்கும் இடையே 3 விநாடிகள் இடைவெளி விட்டுச் சோதித்து, நெட்வொர்க் பிளாக்கிங் மற்றும் Rate Limiting-ஐத் தவிர்க்கும் (`-W` = Wait Time).
* **`hydra -c 10 -l root -P pass.txt 192.168.1.100 ftp`** : ஒவ்வொரு முயற்சியின் போதும் எத்தனை விநாடிகள் Socket Connection காத்திருக்க வேண்டும் என்பதை நிர்ணயிக்கும் (`-c` = Timeout in Seconds).

---

### C. Execution Controls & Output Options (முடிவுகள் மற்றும் செயல்பாட்டு மேலாண்மை)

* **`hydra -vV -l admin -P pass.txt 192.168.1.1 ssh`** : திரையில் ஒவ்வொரு பாஸ்வேர்டு முயற்சியையும் விரிவாக நேரலையில் காட்டும் (`-vV` = Very Verbose Mode).
* **`hydra -f -l admin -P pass.txt 192.168.1.1 ssh`** : சரியான பாஸ்வேர்டு கிடைத்தவுடன் சோதனையை உடனடியாக நிறுத்தி வெளியேறும் (`-f` = Exit on First Found).
* **`hydra -o valid_passwords.txt -l admin -P pass.txt 192.168.1.1 ssh`** : கண்டுபிடிக்கப்பட்ட சரியான பாஸ்வேர்டுகளை ஒரு உரைக் கோப்பில் சேமிக்கும் (`-o` = Output File).
* **`hydra -R`** : பாதியில் நின்ற சோதனையை `hydra.restore` கோப்பைப் பயன்படுத்தி மீண்டும் தொடங்கும் (`-R` = Restore Session).

---

### D. Practical Protocol Examples (முக்கியமான சேவைகள் மீதான சோதனைக் கட்டளைகள்)

* **`hydra -l Administrator -P rockyou.txt rdp://192.168.1.50 -t 4`** : விண்டோஸ் ரிமோட் டெஸ்க்டாப் (Windows RDP) சேவையில் `Administrator` கணக்கிற்கான பாஸ்வேர்டை 4 Threads மூலம் சோதிக்கும் (Windows RDP Cracking).
* **`hydra -l User1 -P pass.txt smb://192.168.1.100`** : நெட்வொர்க்கில் பகிரப்பட்ட Windows SMB கோப்புறைகளுக்கான (Shared Drive) உள்நுழைவு விவரங்களைச் சோதிக்கும் (SMB / Shared Drive Cracking).
* **`hydra -l admin -P pass.txt 192.168.1.1 http-post-form "/login.php:user=^USER^&pass=^PASS^:Invalid password"`** : வெப் அட்மின் பேனலின் (Web Admin Panel) HTTP POST Login படிவத்தை இலக்காகக் கொண்டு, `Invalid password` என்ற தோல்வி செய்தியை அடிப்படையாக வைத்துக் கடவுச்சொல்லைச் சோதிக்கும்.

