# Kali Linux Inbuilt Package #14: Enum4linux & SMBclient (`enum4linux` / `smbclient`) Technical Reference & Setup Guide

---

## 1. Deep Technical Introduction & Architecture (ஆழ்ந்த தொழில்நுட்ப அறிமுகம்)

**Enum4linux** மற்றும் **SMBclient** என்பவை Kali Linux-ல் இயல்பாகவே (Inbuilt) வரும் **SMB/CIFS Enumeration Tools** ஆகும். Windows நெட்வொர்க்குகள் மற்றும் Samba சர்வர்களில் இயங்கும் **SMB (Server Message Block) Protocol** வழியாக பகிரப்படும் Shares, பயனர்கள் (Users), குழுக்கள் (Groups) மற்றும் பாஸ்வேர்டு கொள்கைகளை (Password Policies) கண்டறிய இவை பயன்படுகின்றன.

### ஆழமான தொழில்நுட்பக் கூறுகள் (Core Architecture & Mechanics):

* **NULL Session Enumeration:**
  * பழைய/தவறாக அமைக்கப்பட்ட Windows சர்வர்களில், எந்த Credentials-மும் இல்லாமலேயே (Anonymous/NULL Session) SMB சேவையுடன் இணைந்து, உள்ளே இருக்கும் தகவல்களை வெளியே எடுக்க முடியும் என்பது Enum4linux-ன் முதன்மை கொள்கை.

* **RPC (Remote Procedure Call) Queries:**
  * `rpcclient` Engine-ஐ உள்ளமைவாகக் கொண்டு, `LSA (Local Security Authority)` மற்றும் `SAM (Security Account Manager)` Database-களை வினவி, பயனர்பெயர்கள், Group Membership, மற்றும் Domain/Workgroup தகவல்களைப் பெறும்.

* **SMBclient-ன் Interactive File Share Access:**
  * ஒரு FTP Client போலவே, கண்டறியப்பட்ட SMB Share-க்குள் நேரடியாக உள்நுழைந்து (Login), கோப்புகளைப் பட்டியலிடவும் (`ls`), பதிவிறக்கம் (`get`) செய்யவும் இயலும்.

* **Password Policy & Lockout Discovery:**
  * Minimum Password Length, Lockout Threshold போன்ற Domain Password Policy விவரங்களைக் கண்டறிந்து, Brute-Force சோதனையின்போது Account Lockout ஏற்படாமல் திட்டமிட உதவும்.

* **Infrastructure Use Case (உங்கள் லேப் / கடையின் நெட்வொர்க் சோதனைக்கு):**
  * உங்கள் கேமிங் சென்டரின் Windows Server-ல் உள்ள Shared Folders (பில்லிங் டேட்டா, கேம் இன்ஸ்டாலர்கள்) யாரும் அங்கீகாரம் இல்லாமலேயே அணுக முடியுமா என்பதைச் சோதிக்க இது பயன்படுகிறது.

---

## 2. Package Setup & Update Guide (நிறுவும் மற்றும் புதுப்பிக்கும் முறை)

Kali Linux-ல் Enum4linux மற்றும் SMBclient ஆகிய இரண்டும் ஏற்கனவே இன்ஸ்டால் செய்யப்பட்டிருக்கும்.

# 1. Enum4linux மற்றும் SMBclient பதிப்புகளைச் சரிபார்க்க
enum4linux -h
smbclient --version

# 2. System Packages மற்றும் இரு டூல்களையும் புதுப்பிக்க
sudo apt update && sudo apt install smbclient samba-common-bin -y

# 3. Enum4linux-ன் மேம்பட்ட பதிப்பு (enum4linux-ng) தேவைப்பட்டால் நிறுவ
sudo apt install enum4linux-ng -y

## அடிப்படை கட்டளை வடிவம்:
enum4linux [Options] [Target_IP]
smbclient //[Target_IP]/[Share_Name] [Options]

---

## Categorized Command Reference & Syntax (கருவிகள் மற்றும் விளக்கங்கள்)

# A. Enum4linux — Basic & Full Enumeration (அடிப்படை தகவல் சேகரிப்பு)
enum4linux -a 192.168.1.100 : அனைத்து வகையான தகவல்களையும் (Users, Shares, Policy, OS) ஒரே கட்டளையில் முழுமையாகச் சேகரிக்கும் (-a = All).
enum4linux -U 192.168.1.100 : இலக்கு சர்வரில் பதிவு செய்யப்பட்டுள்ள பயனர்பெயர்களை மட்டும் பட்டியலிடும் (-U = Users).
enum4linux -S 192.168.1.100 : பகிரப்பட்டுள்ள Shares (Folders) பட்டியலை மட்டும் காட்டும் (-S = Shares).

# B. Enum4linux — Policy & Domain Info (கொள்கை மற்றும் டொமைன் தகவல்)
enum4linux -P 192.168.1.100 : கணக்கு Lockout மற்றும் Password Policy விவரங்களைக் காட்டும் (-P = Password Policy).
enum4linux -G 192.168.1.100 : Domain/Workgroup-ல் உள்ள குழுக்களையும் (Groups) அவற்றின் உறுப்பினர்களையும் பட்டியலிடும் (-G = Groups).
enum4linux -o 192.168.1.100 : இலக்கு கணினியின் ஆப்பரேட்டிங் சிஸ்டம் தகவலைக் கண்டறியும் (-o = OS Info).

# C. SMBclient — Share Listing & Access (பகிர்வுகளைப் பட்டியலிடுதல்)
smbclient -L //192.168.1.100 -N : அனுமதி எதுவும் கேட்காமல் (-N = No Password) கிடைக்கக்கூடிய அனைத்து Shares-ஐயும் பட்டியலிடும் (-L = List).
smbclient //192.168.1.100/Public -N : `Public` என்ற Share-க்குள் Anonymous ஆக உள்நுழையும்.
smbclient //192.168.1.100/Users -U administrator : `administrator` பயனர் பெயரில் பாஸ்வேர்டு கேட்டு Share-க்குள் உள்நுழையும்.

# D. SMBclient — File Transfer Commands (கோப்பு பரிமாற்றக் கட்டளைகள் - Share-க்குள் நுழைந்த பின்)
ls : Share-க்குள் உள்ள கோப்புகள் மற்றும் கோப்புறைகளைப் பட்டியலிடும்.
get filename.txt : குறிப்பிட்ட கோப்பை நமது கணினிக்கு பதிவிறக்கம் செய்யும்.
put localfile.txt : நமது கணினியில் உள்ள கோப்பை Share-க்குள் பதிவேற்றும் (எழுத அனுமதி இருந்தால் மட்டும்).
recurse ON ; prompt OFF ; mget * : Share-ல் உள்ள அனைத்து கோப்புகளையும் உறுதிப்படுத்தல் கேட்காமல் ஒரே நேரத்தில் பதிவிறக்கும்.
