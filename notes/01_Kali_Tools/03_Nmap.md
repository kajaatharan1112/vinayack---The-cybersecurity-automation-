# Kali Linux Inbuilt Package #3: Nmap (`nmap`) Technical Reference & Setup Guide

---

## 1. Deep Technical Introduction & Architecture (ஆழ்ந்த தொழில்நுட்ப அறிமுகம்)

**Nmap (Network Mapper)** என்பது Kali Linux-ல் இயல்பாகவே (Inbuilt) வரும் உலகின் மிக சக்திவாய்ந்த **Network Discovery & Vulnerability Scanning Tool** ஆகும். ஒரு நெட்வொர்க்கில் என்னென்ன சாதனங்கள் (Hosts) இயங்குகின்றன, அவற்றில் என்னென்ன போர்ட்டுகள் (Ports) திறந்திருக்கின்றன, மற்றும் என்ன வகையான ஆப்பரேட்டிங் சிஸ்டம் மற்றும் சேவைகள் (Services) இயங்குகின்றன என்பதைக் கண்டறிய இது பயன்படுகிறது.

### ஆழமான தொழில்நுட்பக் கூறுகள் (Core Architecture & Mechanics):

* **Raw Socket & Packet Crafting Engine:**
  * Nmap சாதாரண ஆப்பரேட்டிங் சிஸ்டத்தின் வழக்கமான Sockets வழியே மட்டும் இயங்காமல், **`libpcap` / Raw Sockets** மூலம் சொந்தமாக TCP/UDP/ICMP பாக்கெட்டுகளை (Custom Crafted Packets) உருவாக்கி நெட்வொர்க்கிற்குள் செலுத்துகிறது.

* **Port Scanning Mechanics (இயங்கும் விதம்):**
  * **SYN Stealth Scan (`-sS`):** 3-Way Handshake-ஐ முழுமையாக முடிக்காமல் (SYN -> SYN-ACK -> RST), இணைப்பை பாதியில் துண்டித்து விட்டு, இலக்கு கணினிக்குத் தெரியாமல் போர்ட் திறந்திருக்கிறதா (`Open`) அல்லது மூடியிருக்கிறதா (`Closed`) என்பதைக் கண்டறியும்.
  * **TCP Connect Scan (`-sT`):** Raw Socket அனுமதி இல்லாதபோது (Non-Root User), OS Kernel வழியே முழுமையான 3-Way Handshake-ஐச் செய்து இணைப்பைச் சோதிக்கும்.
  * **UDP Scanning (`-sU`):** Connectionless-ஆக இயங்கும் DNS, DHCP, SNMP போன்ற UDP போர்ட்டுகளுக்கு ICMP Port Unreachable பாக்கெட்டுகளை அனுப்பி நிலையைத் தெரிந்துகொள்ளும்.

* **OS Fingerprinting Engine:**
  * இலக்கு கணினியில் இருந்து வரும் TCP Window Size, TTL (Time To Live), IP ID, மற்றும் TCP Options பதில்களைத் தனியாகப் பிரித்து, Nmap-ன் பிரம்மாண்டமான `nmap-os-db` டேட்டாபேஸுடன் ஒப்பிட்டு (Pattern Matching), இலக்கு கணினி விண்டோஸா, லினக்ஸா அல்லது நெட்வொர்க் ரவுட்டரா என்பதைக் துல்லியமாகக் கணிக்கும்.

* **Nmap Scripting Engine (NSE):**
  * **Lua Programming Language** மூலம் எழுதப்பட்ட 600-க்கும் மேற்பட்ட பிரத்யேக ஸ்கிரிப்டுகளைக் கொண்டது. இதன் மூலம் வெறும் போர்ட் ஸ்கேனிங் மட்டுமின்றி, சிஸ்டத்தில் உள்ள பாதுகாப்பு பலவீனங்கள் (Vulnerabilities) மற்றும் தவறான அமைப்புகளைப் (Misconfigurations) பெற முடியும்.

* **Infrastructure Use Case (உங்கள் லேப் / கடையின் நெட்வொர்க் சோதனைக்கு):**
  * உங்கள் கேமிங் சென்டரின் 20+ PC-கள், Switch, மற்றும் Router ஆகியவற்றுள் ஏதேனும் ஒரு கணினியில் தேவையற்ற போர்ட்டுகள் திறந்துள்ளனவா, அல்லது அங்கீகரிக்கப்படாத சாதனங்கள் (Rogue Devices) நெட்வொர்க்கில் இணைந்துள்ளனவா என்பதை நொடிப்பொழுதில் கண்டறியலாம்.

---

## 2. Package Setup & Update Guide (நிறுவும் மற்றும் புதுப்பிக்கும் முறை)

Kali Linux-ல் Nmap ஏற்கனவே இன்ஸ்டால் செய்யப்பட்டிருக்கும். இருப்பினும் அதைச் சரிபார்க்கவும் புதுப்பிக்கவும் தேவையான கட்டளைகள்:
# 1. Nmap இன்ஸ்டால் செய்யப்பட்டுள்ளதா மற்றும் பதிப்பைச் சரிபார்க்க
nmap --version
# 2. System Packages மற்றும் Nmap-ஐ புதுப்பிக்க
sudo apt update && sudo apt install nmap -y
# 3. Nmap Scripting Engine (NSE) ஸ்கிரிப்டுகளைப் புதுப்பிக்க
sudo nmap --script-updatedb


## Nmap கட்டளையின் அடிப்படை வடிவம்:
nmap [Scan Type] [Options] [Target_IP_or_Subnet]

## Host Discovery & Ping Sweeps (நெட்வொர்க்கில் உள்ள சாதனங்களைக் கண்டறிதல்)
nmap -sn 192.168.1.0/24 : போர்ட்டுகளை ஸ்கேன் செய்யாமல், Subnet-ல் ஆன்லைனில் உள்ள சாதனங்களை (Live Hosts) மட்டும் பட்டியலிடும் (Ping Sweep).
nmap -PR 192.168.1.1 : லோக்கல் நெட்வொர்க்கில் (LAN) ARP Request அனுப்பி சாதனத்தின் MAC Address மற்றும் இருப்பை துல்லியமாகக் கண்டறியும் (-PR = ARP Scan).
nmap -PU 192.168.1.1 : ICMP பிளாக் செய்யப்பட்ட சிஸ்டங்களுக்கு UDP Packets அனுப்பி சாதனங்கள் இயங்குகின்றனவா எனச் சோதிக்கும் (-PU = UDP Ping).

## Port Scanning Techniques (போர்ட் ஸ்கேனிங் முறைகள்)
nmap -sS 192.168.1.100 : stealthy SYN Scan மூலம் 1000 பிரதான போர்ட்டுகளைச் சோதிக்கும் (Root/Sudo permissions தேவை).
nmap -sT 192.168.1.100 : சாதா பயனர் கணக்கிலிருந்து முழுமையான TCP Connection மூலம் ஸ்கேன் செய்யும்.
nmap -sU 192.168.1.100 : UDP போர்ட்டுகளை (DNS, DHCP, TFTP) ஸ்கேன் செய்யும் (-sU = UDP Scan).
nmap -p 80,443,3389 192.168.1.100 : குறிப்பிட்ட போர்ட் எண்களை மட்டும் தேர்வு செய்து சோதிக்கும் (-p = Specific Ports).
nmap -p 1-65535 192.168.1.100 : சிஸ்டத்தில் உள்ள அனைத்து 65,535 போர்ட்டுகளையும் முழுமையாக ஸ்கேன் செய்யும் (-p-).

## Service Version & OS Detection (சேவை மற்றும் ஆப்பரேட்டிங் சிஸ்டம் கண்டறிதல்)
nmap -sV 192.168.1.100 : திறந்திருக்கும் போர்ட்டுகளில் என்ன சாஃப்ட்வேர் மற்றும் அதன் பதிப்பு (உதா: Apache 2.4.41, OpenSSH 8.2) இயங்குகிறது என அறியும் (-sV = Version Detection).
nmap -O 192.168.1.100 : இலக்கு கணினியின் ஆப்பரேட்டிங் சிஸ்டத்தைக் (Windows/Linux/Router OS) கண்டறியும் (-O = OS Detection).
nmap -A 192.168.1.100 : OS Detection, Version Detection, Script Scanning மற்றும் Traceroute ஆகிய நான்கையும் ஒரே நேரத்தில் இயக்கும் Aggressive Scan (-A = Advanced/Aggressive Scan)

## Timing & Performance Optimization (வேகத்தைக் கட்டுப்படுத்துதல்)
nmap -T4 192.168.1.100 : வேகமான நெட்வொர்க்குகளுக்கு ஸ்கேனிங் வேகத்தை அதிகரிக்கும் (-T0 மெதுவானது முதல் -T5 மிக வேகமானது வரை).
nmap --min-rate 1000 192.168.1.0/24 : ஒரு விநாடிக்குக் குறைந்தபட்சம் 1000 பாக்கெட்டுகளை அனுப்பி ஸ்கேன் வேகத்தை உச்சத்திற்குக் கொண்டுசெல்லும்.

## Nmap Scripting Engine (NSE) & Vulnerability Scanning (NSE ஸ்கிரிப்டிங் இன்ஜின் & பாதுகாப்பு பலவீன ஸ்கேனிங்)
nmap --script=default 192.168.1.100 : அடிப்படை பாதுகாப்பு சோதனைகளுக்கான Standard NSE ஸ்கிரிப்டுகளை இயக்கும்.
nmap --script=vuln 192.168.1.100 : இலக்கு கணினியில் அறியப்பட்ட பாதுகாப்பு லூப்ஹோல்கள் (Known Vulnerabilities) உள்ளனவா என NSE ஸ்கிரிப்டுகள் மூலம் பரிசோதிக்கும்.
nmap --script=smb-vuln-ms17-010 -p 445 192.168.1.100 : குறிப்பிட்ட EternalBlue (MS17-010) பலவீனம் விண்டோஸ் சிஸ்டத்தில் உள்ளதா எனப் பார்க்கும்.

## Output Reporting Options (முடிவுகளைச் சேமிக்கும் முறை)
nmap -oN scan_results.txt 192.168.1.100 : ஸ்கேன் முடிவுகளைச் சாதாரண உரைக்கோப்பில் (Normal Text File) சேமிக்கும்.
nmap -oX scan_results.xml 192.168.1.100 : முடிவுகளை XML வடிவில் சேமிக்கும் (மற்ற டூல்களில் Import செய்ய வசதியாக).
nmap -oA my_scan_output 192.168.1.100 : Text, XML, மற்றும் Grepable என மூன்று வடிவங்களிலும் ஒரே நேரத்தில் சேமிக்கும் (-oA = Output All).

