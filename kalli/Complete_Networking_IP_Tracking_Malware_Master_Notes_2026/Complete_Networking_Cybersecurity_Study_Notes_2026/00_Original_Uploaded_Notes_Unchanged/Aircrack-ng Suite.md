# Kali Linux Inbuilt Package #5: Aircrack-ng Suite (`aircrack-ng`) Technical Reference & Setup Guide

---

## 1. Deep Technical Introduction & Architecture (ஆழ்ந்த தொழில்நுட்ப அறிமுகம்)

**Aircrack-ng** என்பது Kali Linux-ல் இயல்பாகவே (Inbuilt) வரும் 802.11 ஒயர்லெஸ் பிணையப் பாதுகாப்பு மற்றும் தணிக்கைக்கான (Wireless Network Security & Auditing) உலகின் முன்னணி மென்பொருள் தொகுப்பாகும் (Suite). இது ஒரே ஒரு டூல் அல்ல; Wi-Fi பாக்கெட்டுகளைப் பிடிக்க, நெட்வொர்க் சிக்னல்களை அனலைஸ் செய்ய, போலி அணுகல் புள்ளிகளைப் பிரிக்க (Deauthentication), மற்றும் WPA/WPA2/WPA3 கடவுச்சொற்களின் பாதுகாப்பைச் சோதிக்க பயன்படும் பல பிரத்யேக டூல்களின் தொகுப்பாகும்.

### ஆழமான தொழில்நுட்பக் கூறுகள் (Core Architecture & Mechanics):

* **Managed Mode vs Monitor Mode (rfmon):**
  * சாதாரண நிலையில் (Managed Mode) Wi-Fi கார்டு தனது BSSID-க்கு வரும் தரவை மட்டுமே படிக்கும். 
  * Aircrack-ng தொகுப்பில் உள்ள **`airmon-ng`** மூலம் Wi-Fi கார்டை **Monitor Mode (RFMON)**-க்கு மாற்றும்போது, காற்றில் பாயும் அத்தனை 802.11 Wireless Frames (Management, Control, Data Frames) அனைத்தையும் பிடிக்கும் திறன் பெறுகிறது.

* **Packet Injection Engine:**
  * **`aireplay-ng`** இன்ஜின் மூலம் வழக்கமான பாக்கெட்டுகளை மட்டும் படிக்காமல், போலி 802.11 Frames-ஐ (உதா: Deauthentication Frames, ARP Requests) காற்றில் செலுத்தி (Packet Injection), வைஃபை நெட்வொர்க்கில் உள்ள சாதனங்களை இணைப்பிலிருந்து துண்டிக்கவோ அல்லது புதிய Handshake-ஐ உருவாக்க தூண்டவோ முடியும்.

* **WPA/WPA2 4-Way Handshake Capture Mechanism:**
  * ஒரு சாதனம் (Client) வைஃபை ரவுட்டருடன் இணையும்போது நடைபெறும் **EAPOL 4-Way Handshake** பரிமாற்றத்தை **`airodump-ng`** மூலம் பிடித்து சேமிக்கிறது. இந்த Handshake-ல் கடவுச்சொல்லின் Cryptographic Hash (HMAC-SHA1 / PBKDF2) அடங்கியிருக்கும்.

* **Dictionary Attack & Hash Cracking Engine:**
  * **`aircrack-ng`** இன்ஜின், பிடிக்கப்பட்ட 4-Way Handshake கோப்பில் உள்ள Hash-ஐ, நாம் கொடுக்கும் அகராதியில் (Wordlist) உள்ள கடவுச்சொற்களுடன் ஒப்பிட்டு (PBKDF2 Key Derivation Function) சரியான Wi-Fi கடவுச்சொல்லைக் கண்டறியும்.

* **Infrastructure Use Case (உங்கள் லேப் / கடையின் நெட்வொர்க் சோதனைக்கு):**
  * உங்கள் கேமிங் சென்டரின் Enterprise Wi-Fi நெட்வொர்க்கில் பலவீனமான கடவுச்சொற்கள் உள்ளனவா, கடையின் வாடிக்கையாளர்கள் பயன்படுத்தும் Wi-Fi நெட்வொர்க்கை யாராவது வெளிநபர்கள் துண்டிக்கிறார்களா (Deauth Attacks), அல்லது கடையின் பெயரில் யாராவது போலி Wi-Fi (Rogue AP / Evil Twin) அமைத்துள்ளார்களா என்பதை ஆராய இது பயன்படுகிறது.

---

## 2. Package Setup & Execution Guide (நிறுவும் மற்றும் அமைக்கும் முறை)

Aircrack-ng Kali Linux-ல் இயல்பாகவே நிறுவப்பட்டிருக்கும். ஒயர்லெஸ் சோதனைகளுக்கு Packet Injection மற்றும் Monitor Mode-ஐ ஆதரிக்கும் Wi-Fi Adapter (உதா: Alfa AWUS036ACH / Atheros/Realtek Chipsets) தேவை.


# 1. Aircrack-ng தொகுப்பின் பதிப்பைச் சரிபார்க்க
aircrack-ng --help

# 2. Wi-Fi Adapter-ன் இடைமுகப் பெயரை (Interface Name) அறிய
iwconfig
# அல்லது
ip link show

# 3. Monitor Mode-க்கு இடையூறாக இருக்கும் பின்புலச் சேவைகளை நிறுத்துதல்
sudo airmon-ng check kill

# 4. Wi-Fi கார்டை Monitor Mode-க்கு மாற்ற
sudo airmon-ng start wlan0


## Categorized Command Reference & Syntax (கருவிகள் மற்றும் விளக்கங்கள்)

# A. Monitor Mode Management (மானிட்டர் மோடை நிர்வகித்தல் - airmon-ng)
airmon-ng : கணினியில் இணைக்கப்பட்டுள்ள அனைத்து ஒயர்லெஸ் நெட்வொர்க் கார்டுகளையும் பட்டியலிடும்.
airmon-ng check : Monitor Mode இயங்குவதைத் தடுக்கும் பின்புலச் சேவைகளைக் (NetworkManager, wpa_supplicant) கண்டறியும்.
airmon-ng check kill : இடையூறாக உள்ள அனைத்து பின்புலச் சேவைகளையும் பலவந்தமாக நிறுத்தும்.
airmon-ng start wlan0 : wlan0 என்ற கார்டை Monitor Mode-க்கு மாற்றும் (wlan0mon எனப் பெயர் மாறும்).
airmon-ng stop wlan0mon : Monitor Mode-ஐ நிறுத்தி இயல்பான Managed Mode-க்கு மாற்றும்.

# B. Wireless Reconnaissance & Packet Sniffing (ஒயர்லெஸ் உளவு பார்த்தல் & பாக்கெட் பிடித்தல் - airodump-ng)
airodump-ng wlan0mon : சுற்றியுள்ள அனைத்து Wi-Fi நெட்வொர்க்குகள் (SSID), BSSID (MAC Address), சிக்னல் வலிமை (PWR), சேனல் (CH), மற்றும் இணைக்கப்பட்டுள்ள சாதனங்களை நேரலையில் திரையிடும்.
airodump-ng -c 6 --bssid 00:11:22:33:44:55 -w wifi_capture wlan0mon : குறிப்பிட்ட சேனல் (Channel 6) மற்றும் குறிப்பிட்ட BSSID கொண்ட ரவுட்டரை மட்டும் இலக்கு வைத்து, அதன் அனைத்து பாக்கெட்டுகளையும் wifi_capture என்ற கோப்பில் சேமிக்கும் (-w = Write File).
airodump-ng --encrypt wpa wlan0mon : WPA/WPA2 பாதுகாப்பு கொண்ட வைஃபை நெட்வொர்க்குகளை மட்டும் வடிகட்டி காட்டும்.

# C. Packet Injection & Deauthentication Attacks (பாக்கெட் இன்ஜெக்ஷன் & இணைப்பு துண்டிக்கும் தாக்குதல்கள் - aireplay-ng)
aireplay-ng --test wlan0mon : உங்கள் Wi-Fi கார்டு பாக்கெட் இன்ஜெக்ஷனை (Packet Injection) சரியாக ஆதரிக்கிறதா எனச் சோதிக்கும்.
aireplay-ng --deauth 10 -a 00:11:22:33:44:55 wlan0mon : குறிப்பிட்ட ரவுட்டருடன் இணைக்கப்பட்டுள்ள அனைத்து சாதனங்களுக்கும் 10 Deauthentication பாக்கெட்டுகளை அனுப்பி, அவற்றின் இணைப்பைத் தற்காலிகமாகத் துண்டிக்கும் (-a = Target AP BSSID).
aireplay-ng --deauth 5 -a 00:11:22:33:44:55 -c AA:BB:CC:DD:EE:FF wlan0mon : குறிப்பிட்ட ஒரு குறிப்பிட்ட சாதனத்தை மட்டும் ரவுட்டரில் இருந்து துண்டிக்கும் (-c = Client MAC Address).

# D. WPA/WPA2 Handshake Cracking (WPA/WPA2 ஹேண்ட்ஷேக் உடைத்தல் - aircrack-ng)
aircrack-ng -w /usr/share/wordlists/rockyou.txt wifi_capture-01.cap : பிடிக்கப்பட்ட .cap கோப்பில் உள்ள WPA/WPA2 Handshake-ஐ rockyou.txt அகராதியைக் கொண்டு உடைக்க முயற்சிக்கும்.
aircrack-ng -b 00:11:22:33:44:55 -w passlist.txt wifi_capture-01.cap : பல வைஃபை நெட்வொர்க் தகவல்கள் கொண்ட கோப்பிலிருந்து குறிப்பிட்ட BSSID-க்கு மட்டும் பாஸ்வேர்ட் சோதனையை இயக்கும் (-b = BSSID Filter).
aircrack-ng -s wifi_capture-01.cap : பிடிக்கப்பட்ட பாக்கெட் கோப்பில் செல்லுபடியாகும் WPA Handshake உள்ளதா என்பதை மட்டும் சரிபார்க்கும்.

# E. Decryption & Analysis (டிக்ரிப்ஷன் & பகுப்பாய்வு - airdecap-ng)
airdecap-ng -e "MyWiFiName" -p "MyPassword123" wifi_capture-01.cap : வைஃபை பாஸ்வேர்டு தெரிந்தவுடன், என்கிரிப்ட் செய்யப்பட்ட .cap கோப்பை திறந்தநிலைக் கோப்பாக (Decrypted PCAP) மாற்றி Wireshark-ல் வாசிக்க வைக்கும் (-e = ESSID, -p = Password).
airdecap-ng -l wifi_capture-01.cap : என்கிரிப்ட் செய்யப்படாத திறந்தநிலை (Open Network) பாக்கெட்டுகளை மட்டும் பிரித்தெடுக்கும்.