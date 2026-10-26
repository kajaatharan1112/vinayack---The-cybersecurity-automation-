# Cyber Security Lab Setup - அடிப்படை அறிமுகம் (Introduction)

---

## 1. Kali Linux Initial Setup (தொடக்க அமைப்பு)

* **`sudo apt update && sudo apt upgrade -y`** : சிஸ்டத்தின் Package List-ஐப் புதுப்பித்து, இன்ஸ்டால் செய்யப்பட்ட அனைத்து Software-ஐயும் Latest Version-க்கு Upgrade செய்யும்.
* **`pwd`** : தற்போதைய டைரக்டரியைக் காட்டும் (Print Working Directory).
* **`ls -la`** : மறைக்கப்பட்ட கோப்புகள் உட்பட ஃபைல்கள் மற்றும் போல்டர்களை அனைத்தையும் பட்டியலிடும்.
* **`ip a`** : சாதனத்தின் நெட்வொர்க் IP முகவரியை அறிய உதவும்.
* **`nmap -sV scanme.nmap.org`** : ஒரு வெப்சைட் அல்லது IP-யின் Open Ports-ஐ ஸ்கேன் செய்ய, ஒரு நெட்வொர்க்கில் என்னென்ன சாதனங்கள் மற்றும் Open Ports உள்ளன என்பதைக் கண்டறிய (Package: Kali-ல் Pre-installed, இல்லை என்றால் `sudo apt install nmap -y`).
* **`wireshark`** : நெட்வொர்க்கில் செல்லும் டேட்டா பாக்கெட்டுகளை நேரலையில் கண்காணிக்க திறக்கும் GUI Tool (Package: `sudo apt install wireshark -y`).
* **`burpsuite`** : இணையதளங்களில் உள்ள Bugs மற்றும் Vulnerabilities-ஐக் கண்டறியும் Proxy Tool-ஐத் திறக்கும் (Package: Kali-ல் Pre-installed; Community Edition `sudo apt install burpsuite -y`).

---

## 2. Terminal-க்கான அடிப்படை கட்டளைகள் (Essential Command Line Interface - CLI)

### A. சிஸ்டத்தைப் புதுப்பிக்க (System Updates)

* **`sudo apt update && sudo apt upgrade -y`** : System Packages அனைத்தையும் புதுப்பிக்கும்.

### B. கோப்பு அமைப்பில் நகர்வதற்கு (File System Navigation)

* **`pwd`** : தற்போதைய டைரக்டரியைக் காட்டும் (Print Working Directory).
* **`ls -la`** : மறைக்கப்பட்ட கோப்புகள் உட்பட அனைத்தையும் பட்டியலிடும் (List all files, including hidden).
* **`cd /path/to/folder`** : குறிப்பிட்ட டைரக்டரிக்கு மாறும் (Change Directory).
* **`mkdir project_name`** : புதிய போல்டரை உருவாக்கும் (Create Folder).

### C. நெட்வொர்க் அமைப்புகளை அறிய (Network Configuration)

* **`ip a`** : சாதனத்தின் IP முகவரியைக் காட்டும் (Check IP Address).
* **`ping -c 4 8.8.8.8`** : நெட்வொர்க் இணைப்பு இருக்கிறதா என 4 முறை சோதிக்கும் (Test Network Connection).

### D. கோப்பு மேலாண்மை மற்றும் அனுமதிகள் (File Management & Permissions)

* **`nano filename.txt`** : எளிய Text Editor-ஐத் திறந்து கோப்பைத் திருத்தும் (Package: `nano`, பொதுவாக Pre-installed).
* **`chmod +x script.sh`** : ஸ்கிரிப்ட் கோப்புக்கு இயக்கும் அனுமதியை (Executable Permission) வழங்கும்.

> இன்னும் விரிவான அடிப்படை Linux Commands (Process Monitoring, Package Management, Compression, User Management போன்றவை) [`02_Testing_Commands.md`](02_Testing_Commands.md) கோப்பின் **Section 0: Essential Linux Commands**-ல் முழுமையாகக் கொடுக்கப்பட்டுள்ளது.

---

## 3. Nmap (Network Mapper)

நெட்வொர்க்கில் உள்ள திறந்த போர்ட்டுகள் (Open Ports) மற்றும் இயங்கும் சேவைகளைக் கண்டறிய:

* **`nmap 192.168.1.1`** : அடிப்படை IP ஸ்கேன் (Basic IP Scan).
* **`nmap -A -v 192.168.1.100`** : விரிவான OS மற்றும் சேவை பதிப்பு ஸ்கேன் (Detailed OS and Service Version Scan).

> Nmap-ஐப் பற்றிய முழுமையான Command Reference [`01_Kali_Tools/03_Nmap.md`](../01_Kali_Tools/03_Nmap.md) கோப்பில் உள்ளது.

---

## 4. Kali Linux-ல் Pre-installed Security Tools-ஐப் பார்க்க

* **`dpkg -l | grep -i kali-tools`** : Kali Linux Virtual Machine-ஐத் திறந்து Terminal-ல் இந்தக் கட்டளையைத் தட்டச்சு செய்தால், OS-உடன் சேர்ந்தே வந்த அத்தனை Security/Attack Packages-ஐயும் வரிசையாகப் பார்க்க முடியும்.
