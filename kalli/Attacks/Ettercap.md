# Kali Linux Inbuilt Package #16: Ettercap (`ettercap`) Technical Reference & Setup Guide

---

## 1. Deep Technical Introduction & Architecture (ஆழ்ந்த தொழில்நுட்ப அறிமுகம்)

**Ettercap** என்பது Kali Linux-ல் இயல்பாகவே (Inbuilt) வரும் **Man-in-the-Middle (MITM) Attack & Network Sniffing Tool** ஆகும். ஒரு லோக்கல் நெட்வொர்க்கில் (LAN) இரு சாதனங்களுக்கு இடையே நடுவில் நின்று, அவற்றுக்கிடையே பரிமாறப்படும் தரவைக் கண்காணிக்கவும் (Sniff), மாற்றியமைக்கவும் (Modify) இது பயன்படுகிறது.

### ஆழமான தொழில்நுட்பக் கூறுகள் (Core Architecture & Mechanics):

* **ARP Cache Poisoning Mechanism:**
  * Local Network-ல் உள்ள இரு சாதனங்களுக்கும் (உதா: Victim & Router) போலியான ARP Reply பாக்கெட்டுகளை அனுப்பி, அவற்றின் ARP Cache-ல் Attacker கணினியின் MAC Address-ஐப் பதிவு செய்ய வைக்கும். இதனால் இரு சாதனங்களுக்கும் இடையே செல்லும் அனைத்துத் தரவும் முதலில் Attacker கணினி வழியாகவே பாயும்.

* **Protocol Dissection Engine:**
  * HTTP, FTP, Telnet, DNS போன்ற Plaintext Protocols-ல் பரிமாறப்படும் தரவை (உதா: Login Credentials) நேரலையில் படித்துக் காட்டும் திறன் கொண்டது.

* **Filter & Content Injection (Etterfilter):**
  * `etterfilter` மொழியில் எழுதப்பட்ட Custom Scripts மூலம், இடைமறிக்கப்படும் தரவுப் பாக்கெட்டுகளில் குறிப்பிட்ட உரையை மாற்றியமைக்கவோ (Content Replacement) அல்லது இணைப்பை முழுமையாகத் துண்டிக்கவோ (Connection Killing) முடியும்.

* **DNS Spoofing Plugin:**
  * `dns_spoof` Plugin மூலம், இலக்கு சாதனம் ஒரு குறிப்பிட்ட டொமைனைத் தேடும்போது (உதா: `example.com`), உண்மையான IP-க்குப் பதிலாக Attacker நிர்ணயிக்கும் போலி IP-க்கு திருப்பி விடலாம்.

* **Infrastructure Use Case (உங்கள் லேப் / கடையின் நெட்வொர்க் சோதனைக்கு):**
  * உங்கள் கேமிங் சென்டர் நெட்வொர்க்கில் ARP Spoofing தாக்குதல்களை யாரேனும் வெளிநபர் செய்ய முடியுமா, HTTPS இல்லாத பழைய பில்லிங் சாஃப்ட்வேர் வழியாக Plaintext பாஸ்வேர்டுகள் கசிகின்றனவா என்பதைச் சோதிக்க இது பயன்படுகிறது — இந்தச் சோதனைகள் உங்கள் சொந்த லேப்/நெட்வொர்க்கில் மட்டுமே, முன் அனுமதியுடன் செய்யப்பட வேண்டும்.

---

## 2. Package Setup & Update Guide (நிறுவும் மற்றும் புதுப்பிக்கும் முறை)

Kali Linux-ல் Ettercap ஏற்கனவே இன்ஸ்டால் செய்யப்பட்டிருக்கும் (GUI மற்றும் CLI இரண்டு பதிப்புகளிலும்).

# 1. Ettercap இன்ஸ்டால் செய்யப்பட்டுள்ளதா மற்றும் பதிப்பைச் சரிபார்க்க
ettercap --version

# 2. System Packages மற்றும் Ettercap-ஐ புதுப்பிக்க
sudo apt update && sudo apt install ettercap-graphical ettercap-text-only -y

# 3. IP Forwarding-ஐ இயக்க (MITM-க்குப் பின் தரவு இலக்கை அடைய இது அவசியம்)
sudo sysctl -w net.ipv4.ip_forward=1

## Ettercap கட்டளையின் அடிப்படை வடிவம்:
ettercap [Mode] [Options] // [Target1] // [Target2]

---

## Categorized Command Reference & Syntax (கருவிகள் மற்றும் விளக்கங்கள்)

# A. Network Discovery (நெட்வொர்க்கில் உள்ள சாதனங்களைக் கண்டறிதல்)
ettercap -T -q -i eth0 // // : Text Mode-ல் (-T) நெட்வொர்க்கில் உள்ள அனைத்து சாதனங்களையும் ஸ்கேன் செய்து பட்டியலிடும் (-q = Quiet).
ettercap -T -i eth0 -P list : கிடைக்கக்கூடிய அனைத்து Ettercap Plugins-ஐயும் பட்டியலிடும் (-P = Plugin).

# B. ARP Poisoning & MITM Attack (ARP விஷம் ஏற்றுதல் & MITM தாக்குதல்)
ettercap -T -q -i eth0 -M arp:remote /192.168.1.1// /192.168.1.50// : ரவுட்டர் (192.168.1.1) மற்றும் இலக்கு சாதனம் (192.168.1.50) இடையே ARP Poisoning மூலம் MITM நிலையை ஏற்படுத்தும் (-M = MITM Method).
ettercap -T -q -M arp:remote /192.168.1.1// // : ஒரு குறிப்பிட்ட ரவுட்டருக்கும் நெட்வொர்க்கில் உள்ள அனைத்துச் சாதனங்களுக்கும் இடையே MITM செய்யும் (இரண்டாவது Target காலியாக விடப்படுகிறது).

# C. Sniffing & Credential Capture (தரவுக் கண்காணிப்பு & கடவுச்சொல் பிடிப்பு)
ettercap -T -q -i eth0 -M arp:remote /192.168.1.1// /192.168.1.50// -w capture.pcap : இடைமறிக்கப்படும் பாக்கெட்டுகளை ஒரு .pcap கோப்பில் சேமித்து பின்னர் Wireshark-ல் ஆராயும் (-w = Write File).

# D. DNS Spoofing (dns_spoof Plugin)
ettercap -T -q -i eth0 -P dns_spoof -M arp:remote /192.168.1.1// /192.168.1.50// : `/etc/ettercap/etter.dns` கோப்பில் நிர்ணயிக்கப்பட்டுள்ள போலி IP-க்கு DNS கோரிக்கைகளைத் திருப்பி விடும் (-P dns_spoof = DNS Spoofing Plugin).

# E. GUI Mode & Clean-Up (கிராஃபிகல் பயன்முறை மற்றும் முடித்தல்)
ettercap -G : Ettercap-ன் Graphical User Interface (GUI) பதிப்பைத் திறக்கும் (-G = Graphical).
sudo sysctl -w net.ipv4.ip_forward=0 : சோதனை முடிந்தவுடன் IP Forwarding-ஐ அணைத்து, சாதாரண நெட்வொர்க் நிலைக்குத் திரும்பும்.
