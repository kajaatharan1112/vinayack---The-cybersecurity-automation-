# Advanced Infrastructure, Networking & Security Guide

---

## 0. Essential Linux Commands (அடிப்படை லினக்ஸ் கட்டளைகள் - Missing Commands Restored)

இந்தப் பகுதியில் இதற்கு முன் Notes-ல் Mix ஆகி காணாமல் போன அடிப்படை Linux Commands அனைத்தும் தெளிவாக, Category வாரியாக, Package Setup தகவலுடன் சேர்க்கப்பட்டுள்ளது.

### A. Navigation & File System (கோப்பு அமைப்பில் நகர்தல்)

* **`pwd`** : தற்போதைய டைரக்டரியின் முழு பாதையைக் (Full Path) காட்டும் (Print Working Directory).
* **`ls -la`** : மறைக்கப்பட்ட கோப்புகள் உட்பட அனைத்து Files/Folders-ஐயும் விரிவான தகவலுடன் (Permissions, Size, Date) பட்டியலிடும்.
* **`cd /path/to/folder`** : குறிப்பிட்ட டைரக்டரிக்கு மாறும் (Change Directory). `cd ..` முந்தைய Folder-க்குச் செல்லும், `cd ~` Home Directory-க்குச் செல்லும்.
* **`mkdir project_name`** : புதிய Folder ஒன்றை உருவாக்கும் (`-p` flag வைத்தால் Nested Folders ஒரே நேரத்தில் உருவாகும்: `mkdir -p a/b/c`).
* **`rmdir folder_name`** : காலியான (Empty) Folder-ஐ நீக்கும்.
* **`rm -rf folder_name`** : Folder மற்றும் அதனுள் உள்ள அனைத்தையும் முழுமையாக நீக்கும் (⚠️ மீட்க முடியாது, மிக எச்சரிக்கையுடன் பயன்படுத்தவும்).
* **`cp source destination`** : கோப்பு/Folder-ஐ நகலெடுக்கும் (Folder-க்கு `-r` flag தேவை).
* **`mv source destination`** : கோப்பு/Folder-ஐ நகர்த்தவும் அல்லது பெயர் மாற்றவும் பயன்படும்.
* **`find / -name "filename"`** : முழு சிஸ்டத்திலும் ஒரு கோப்பைப் பெயர் வைத்துத் தேடும்.
* **`locate filename`** : Database Index-ஐப் பயன்படுத்தி மிக வேகமாகக் கோப்பைத் தேடும் (Package: `mlocate` — `sudo apt install mlocate && sudo updatedb`).

### B. Viewing & Editing Files (கோப்புகளைப் பார்த்தல் / திருத்துதல்)

* **`cat filename.txt`** : கோப்பின் முழு உள்ளடக்கத்தையும் Terminal-ல் காட்டும்.
* **`less filename.txt`** : பெரிய கோப்புகளை பக்கம் பக்கமாக (Scroll செய்து) படிக்க உதவும் (`q` press செய்து வெளியேறலாம்).
* **`head -n 20 filename.txt`** : கோப்பின் முதல் 20 வரிகளைக் காட்டும்.
* **`tail -n 20 filename.txt`** : கோப்பின் கடைசி 20 வரிகளைக் காட்டும் (`-f` flag வைத்தால் Log File-ஐ Live-ஆகக் கண்காணிக்கலாம்: `tail -f /var/log/syslog`).
* **`nano filename.txt`** : எளிமையான Text Editor-ஐத் திறந்து கோப்பைத் திருத்தும் (Package: `nano` — பொதுவாக Pre-installed).
* **`vim filename.txt`** : Advanced Terminal Text Editor (Package: `vim` — `sudo apt install vim -y`).
* **`grep -i "keyword" filename.txt`** : கோப்பிற்குள் ஒரு குறிப்பிட்ட வார்த்தையைத் தேடும் (`-i` = Case-Insensitive, `-r` = Recursive Folder Search).

### C. Permissions & Ownership (அனுமதிகள் மற்றும் உரிமை)

* **`chmod +x script.sh`** : ஸ்கிரிப்ட் கோப்புக்கு இயக்கும் அனுமதியை (Executable Permission) வழங்கும்.
* **`chmod 755 filename`** : Owner-க்கு Read/Write/Execute, Group & Others-க்கு Read/Execute மட்டும் கொடுக்கும் (Numeric Permission Mode).
* **`chown user:group filename`** : கோப்பின் Owner மற்றும் Group-ஐ மாற்றும் (Root Permission தேவை).
* **`sudo command`** : ஒரு கட்டளையை Administrator (Root) அதிகாரத்துடன் இயக்கும் (Super User DO).

### D. Process & System Monitoring (செயல்பாடு மற்றும் சிஸ்டம் கண்காணிப்பு)

* **`ps aux`** : தற்போது இயங்கும் அனைத்து Processes-ஐயும் விரிவாகப் பட்டியலிடும்.
* **`top`** / **`htop`** : CPU/RAM பயன்பாட்டை Live-ஆகக் காண்பிக்கும் (`htop` இன்னும் வண்ணமயமானது — Package: `sudo apt install htop -y`).
* **`kill -9 PID`** : Process ID (PID) வைத்து ஒரு Process-ஐ கட்டாயமாக நிறுத்தும்.
* **`killall process_name`** : பெயர் வைத்து ஒரு Process-ஐ நிறுத்தும்.
* **`systemctl status service_name`** : ஒரு Service (உதா: `ssh`, `apache2`) இயங்குகிறதா எனப் பார்க்கும்.
* **`systemctl start/stop/restart service_name`** : Service-ஐ தொடங்க/நிறுத்த/மீள்தொடங்க பயன்படும்.
* **`df -h`** : Disk Space பயன்பாட்டை Human-Readable வடிவில் (GB/MB) காட்டும்.
* **`du -sh folder_name`** : ஒரு Folder எவ்வளவு Space எடுத்துள்ளது எனக் காட்டும்.
* **`free -h`** : RAM மற்றும் Swap Memory பயன்பாட்டைக் காட்டும்.

### E. Networking Basics (நெட்வொர்க் அடிப்படைக் கட்டளைகள்)

* **`ip a`** : சாதனத்தின் Network Interfaces மற்றும் IP முகவரிகளைக் காட்டும்.
* **`ping -c 4 8.8.8.8`** : நெட்வொர்க் இணைப்பு இருக்கிறதா என 4 முறை சோதிக்கும்.
* **`traceroute google.com`** : ஒரு Packet இலக்கை அடைய எந்தெந்த Routers வழியாகச் செல்கிறது எனக் காட்டும் (Package: `sudo apt install traceroute -y`).
* **`netstat -tulnp`** : திறந்திருக்கும் Ports மற்றும் அவற்றை Use செய்யும் Processes-ஐக் காட்டும் (Package: `sudo apt install net-tools -y`; புதிய systems-ல் `ss -tulnp` பயன்படுத்தப்படுகிறது).
* **`ssh user@192.168.1.100`** : தொலைதூர Linux சர்வர் ஒன்றுடன் பாதுகாப்பாக இணையும் (Package: `sudo apt install openssh-client -y`).
* **`scp file.txt user@192.168.1.100:/path/`** : SSH மூலம் கோப்புகளை Remote Server-க்கு பாதுகாப்பாக அனுப்பும்.
* **`wget https://example.com/file.zip`** : இணையத்திலிருந்து கோப்பைப் பதிவிறக்கும் (Package: `sudo apt install wget -y`).
* **`curl -I https://example.com`** : ஒரு Website-ன் HTTP Headers-ஐ Terminal-லிருந்தே சோதிக்கும் (Package: `sudo apt install curl -y`).

### F. Package & System Management (பேக்கேஜ் மேலாண்மை)

* **`sudo apt update && sudo apt upgrade -y`** : Package List-ஐப் புதுப்பித்து, இன்ஸ்டால் செய்யப்பட்ட அனைத்து Software-ஐயும் Latest Version-க்கு Upgrade செய்யும்.
* **`sudo apt install package_name -y`** : புதிய Package ஒன்றை Install செய்யும்.
* **`sudo apt remove package_name -y`** : Package-ஐ Uninstall செய்யும் (Config Files மிஞ்சும்).
* **`sudo apt purge package_name -y`** : Package-ஐ அதன் Config Files உடன் முழுமையாக நீக்கும்.
* **`dpkg -l | grep -i kali-tools`** : Kali Linux OS-உடன் Pre-installed-ஆக வந்த அனைத்து Security/Attack Packages-ஐயும் பட்டியலிடும்.
* **`dpkg -l | grep package_name`** : ஒரு குறிப்பிட்ட Package Install செய்யப்பட்டுள்ளதா எனச் சரிபார்க்கும்.

### G. Compression & Archiving (கோப்புகளை Compress செய்தல்)

* **`tar -czvf archive.tar.gz folder_name/`** : Folder ஒன்றை Compress செய்து `.tar.gz` கோப்பாக உருவாக்கும்.
* **`tar -xzvf archive.tar.gz`** : `.tar.gz` கோப்பை Extract செய்யும்.
* **`unzip file.zip`** : `.zip` கோப்பை Extract செய்யும் (Package: `sudo apt install unzip -y`).

### H. User Management (பயனர் மேலாண்மை)

* **`whoami`** : தற்போது Login ஆகியிருக்கும் Username-ஐக் காட்டும்.
* **`id`** : தற்போதைய User-ன் UID, GID மற்றும் Groups-ஐக் காட்டும்.
* **`sudo adduser newuser`** : புதிய User Account உருவாக்கும்.
* **`sudo passwd username`** : ஒரு User-ன் Password-ஐ மாற்றும்.
* **`su - username`** : மற்றொரு User Account-க்கு Switch செய்யும்.

---

## 1. Linux Kernel & Network Performance Tuning (லினக்ஸ் கர்னல் & நெட்வொர்க் வேக அமைப்பு)

* **`sysctl net.core.somaxconn=65535`** : High-concurrency கேமிங் சூழலில், TCP Socket Connection Queue வரம்பை 128-ல் இருந்து 65,535 ஆக உயர்த்தி Packet Latency-ஐக் குறைக்கும்.
* **`sysctl net.ipv4.tcp_tw_reuse=1`** : `TIME_WAIT` நிலையில் உள்ள Sockets-ஐ புதிய இணைப்புகளுக்கு உடனடியாக Reuse செய்து, Port Exhaustion ஏற்படுவதைத் தடுக்கும்.
* **`sysctl net.ipv4.tcp_congestion_control=bbr`** : கூகுளின் BBR Congestion Control Algorithm-ஐ ஆக்டிவேட் செய்து, High-bandwidth / Low-latency நெட்வொர்க் பயன்பாட்டை உறுதி செய்யும்.
* **`ethtool -G eth0 rx 4096 tx 4096`** : NIC (Network Interface Card) Ring Buffer அளவை அதிகரித்து, 10GbE லோக்கல் நெட்வொர்க்கில் Packet Drops ஏற்படுவதை முழுமையாகத் தடுக்கும் (Package: `sudo apt install ethtool -y`).
* **`taskset -c 0,1 /usr/sbin/irqbalance`** : Network Interface-ன் Interrupt-களை பிரத்யேக CPU Cores-க்கு ஒதுக்கி (CPU Affinity), Core Throttling இல்லாமல் லேக்-ஃப்ரீ கேமிங் சூழலைத் தரும் (Package: `sudo apt install util-linux irqbalance -y`).

---

## 2. Enterprise Diskless Boot Architecture (டிஸ்க் இல்லாமல் பூட் செய்யும் அமைப்பு - PXE + iSCSI + CoW)

* **iPXE Chainloading** : மெதுவான TFTP Protocol-க்கு பதிலாக, iPXE ROM வழியாக HTTP/iSCSI Protocol மூலம் Boot Image-ஐ லோட் செய்து, OS Boot நேரத்தை 80% குறைக்கும் முறை (Package: `ipxe`, `sudo apt install ipxe -y`).
* **`targetcli`** (LIO Target) : Linux Kernel-level iSCSI Subsystem. 20+ Windows Client PC-களுக்கு ஒரே Master C: Drive Storage LUN-ஐ SAN/iSCSI வழியாக நெட்வொர்க்கில் பரிமாறும் (Package: `sudo apt install targetcli-fb -y`).
* **OverlayFS / Btrfs CoW (Copy-on-Write)** : ஒரே Master Windows VHD Image-ஐ வைத்துக்கொண்டு, ஒவ்வொரு Client PC-க்கும் தனித்தனி "Write-Overlay Layer" உருவாக்கி, Storage Space செலவை 90% குறைக்கும் (Package: `sudo apt install btrfs-progs -y`).
* **Jumbo Frames (MTU 9000)** : Switch மற்றும் Linux Server-ல் `sudo ip link set eth0 mtu 9000` எனப் பயன்படுத்தி MTU 9000 அமைப்பதன் மூலம், Network Overhead-ஐக் குறைத்து Diskless OS Loading வேகத்தை 1Gbps-ல் இருந்து 10Gbps லெவலுக்கு உயர்த்தும்.

---

## 3. Advanced Active Defense & Penetration Testing Tools (மேம்பட்ட தற்காப்பு & பென்டெஸ்டிங் கருவிகள்)

* **`responder -I eth0 -dwv`** : Internal Network-ல் LLMNR / NBT-NS Poisoning செய்து, விண்டோஸ் சிஸ்டம்கள் இடையே மாறும் NTLMv2 Password Hashes-ஐக் கைப்பற்றும் Advanced Sniffing Tool (Package: `sudo apt install responder -y`).
* **`bloodhound-python` / `SharpHound.exe`** : Active Directory / Local Network-ல் உள்ள Privilege Escalation Paths மற்றும் Hidden Trust Relationships-ஐ Graph Database மூலம் கண்டறியும் டூல் (Package: `sudo apt install bloodhound -y`, GUI-க்கு `neo4j` database தேவை).
* **`cme smb 192.168.1.0/24`** (CrackMapExec) : Subnet முழுவதிலும் உள்ள SMB, WinRM, SSH போர்ட்டுகளில் Lateral Movement சோதனைகள் செய்து, ஒரு PC பாதிக்கப்பட்டால் மற்ற PC-களுக்கு பரவுமா என ஆராயும் டூல் (Package: `pipx install crackmapexec` அல்லது `sudo apt install crackmapexec -y`).
* **`scapy`** (Python Framework) : Custom IP/TCP/UDP Packets-ஐ சொந்தமாக ஸ்கிரிப்ட் செய்து எழுதி, Router/Firewall-ன் Stateful Inspection மற்றும் Anti-DDoS திறனைச் சோதிக்கும் Python Library (Package: `pip install scapy` அல்லது `sudo apt install python3-scapy -y`).

---

## 4. Kernel-Level Security & Traffic Filtering (கர்னல் மட்ட பாதுகாப்பு & ட்ராஃபிக் வடிகட்டுதல் - eBPF & Hardening)

* **XDP / eBPF (Express Data Path)** : Linux Kernel Space-க்குள்ளேயே (Network Driver Level) தீங்கிழைக்கும் Packet-களை கண்டறிந்து Drop செய்யும் சிஸ்டம். CPU Usage 0% ஆக இருக்கும்போதே DDoS-ஐத் தடுக்கும் (Package: `sudo apt install bpfcc-tools linux-headers-$(uname -r) -y`).
* **`iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP`** : Null Packets மூலம் ஹேக்கர்கள் செய்யும் Stealth Port Scanning (NULL Scan) தாக்குதல்களை லினக்ஸ் கர்னல் மட்டத்தில் கண்டறிந்து துண்டிக்கும் (Package: `sudo apt install iptables -y`).
* **Linux cgroups v2 (Control Groups)** : Server-ல் ஓடும் Background Services (PXE/DNS/iSCSI) ஒவ்வொன்றும் குறிப்பிட்ட அளவு RAM/CPU-க்கு மேல் பயன்படுத்தாதவாறு வன்பொருள் கட்டுப்பாட்டை விதிக்கும் (Kernel-built-in, `cgroup-tools` package-ல் manual control கிடைக்கும்: `sudo apt install cgroup-tools -y`).
* **AppArmor / SELinux Mandatory Access Control** : Linux-ல் Admin (Root) Access கிடைத்தாலும், குறிப்பிட்ட Daemon processes (உதா: DNS/DHCP) மற்ற System Directories-ஐ அணுகாதவாறு Isolation செய்யும் பாதுகாப்பு அடுக்கு (Package: `sudo apt install apparmor apparmor-utils -y`; Kali/Debian-ல் AppArmor Default, RHEL-ல் SELinux Default).

---

## 5. Quick Package Install Cheat-Sheet (இந்த Note-ல் உள்ள அனைத்து Tools-க்குமான Install Commands)

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install nano vim htop net-tools traceroute wget curl unzip -y
sudo apt install ethtool util-linux irqbalance -y
sudo apt install ipxe targetcli-fb btrfs-progs -y
sudo apt install responder bloodhound crackmapexec python3-scapy -y
sudo apt install bpfcc-tools iptables cgroup-tools apparmor apparmor-utils -y
```
