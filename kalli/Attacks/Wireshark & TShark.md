# Kali Linux Inbuilt Package #4: Wireshark & TShark (`wireshark` / `tshark`) Technical Reference & Setup Guide

---

## 1. Deep Technical Introduction & Architecture (ஆழ்ந்த தொழில்நுட்ப அறிமுகம்)

**Wireshark** (மற்றும் அதன் Command Line பதிப்பான **TShark**) என்பது Kali Linux-ல் இயல்பாகவே (Inbuilt) வரும் உலகின் மிகப்பிரபலமான **Network Packet Analyzer & Deep Packet Inspection (DPI) Tool** ஆகும். ஒரு கணினி பிணையத்தில் (Network) நிகழும் ஒவ்வொரு தரவுப் பரிமாற்றத்தையும் (Network Packets) நேரலையில் பிடித்து, அதில் உள்ள தகவல்களை ஆழமாக ஆராய இது பயன்படுகிறது.

### ஆழமான தொழில்நுட்பக் கூறுகள் (Core Architecture & Mechanics):

* **Packet Capture Driver (`libpcap` / `dumpcap`):**
  * Wireshark நேரடியாக Network Interface Card (NIC)-உடன் பேசாமல், பின்புலத்தில் **`dumpcap`** என்ற குறைந்த சலுகை கொண்ட (Low-Privilege) இன்ஜின் மற்றும் **`libpcap`** லைப்ரரி வழியே பாக்கெட்டுகளை பிடிக்கும்.

* **Promiscuous Mode:**
  * சாதாரண முறையில் ஒரு NIC தனக்கு அனுப்பப்படும் பாக்கெட்டுகளை மட்டுமே ஏற்கும். ஆனால் Wireshark-ல் **Promiscuous Mode** ஆன் செய்யப்படும்போது, அந்த Network Switch வழியே செல்லக்கூடிய அனைத்து பாக்கெட்டுகளையும் (Target Unicast/Broadcast) பிடித்து ஆராயும் திறன் பெறும்.

* **Protocol Dissectors Engine:**
  * பிடிபட்ட Raw Hexadecimal Binary Data-வை மனிதர்கள் படிக்கும் வடிவில் (Ethernet Frame -> IP Header -> TCP Header -> Application Data) பிரித்துக் காட்ட 3,000-க்கும் மேற்பட்ட **Protocol Dissectors** பயன்படுகின்றன.

* **CLI Equivalent (`tshark`):**
  * GUI இல்லாத Headless Linux Servers மற்றும் Remote SSH Sessions-ல் Wireshark-ன் அனைத்து வசதிகளையும் இயக்க **TShark** பயன்படுத்தப்படுகிறது.

* **Infrastructure Use Case (உங்கள் லேப் / கடையின் நெட்வொர்க் பயன்பாடு):**
  * கேமிங் சென்டர் நெட்வொர்க்கில் எந்த பிசி அதிக டேட்டாவை நுகர்கிறது, நெட்வொர்க்கில் Packet Loss அல்லது Ping Latency எங்கு ஏற்படுகிறது, மற்றும் லோக்கல் நெட்வொர்க்கில் ARP Spoofing அல்லது Suspicious Traffic நடக்கிறதா என்பதைத் துல்லியமாகக் கண்டுபிடிக்க Wireshark பயன்படுகிறது.

---

## 2. Package Setup & Execution Guide (நிறுவும் மற்றும் இயக்கும் முறை)

Kali Linux-ல் Wireshark மற்றும் TShark இயல்பாகவே நிறுவப்பட்டிருக்கும்.

# 1. Root அனுமதி இல்லாமல் சாதாரண பயனராக Wireshark இயக்க அமைத்தல்
sudo dpkg-reconfigure wireshark-common
sudo usermod -aG wireshark $USER

# 2. TShark பதிப்பைச் சரிபார்க்க
tshark --version

# 3. Wireshark GUI இடைமுகத்தைத் தொடங்க
wireshark &

# 4. TShark CLI-ஐத் தொடங்க
tshark -i eth0

## TShark கட்டளையின் அடிப்படை வடிவம்
tshark [options] [capture/display filters]

# Interface & Live Capture Control (நேரலை பாக்கெட் கண்காணிப்பு)
tshark -D : கணினியில் உள்ள அனைத்து Network Interfaces (eth0, wlan0, lo) பட்டியலைக் காட்டும்.
tshark -i eth0 : eth0 இன்டர்ஃபேஸ் வழியே செல்லும் அனைத்து நெட்வொர்க் பாக்கெட்டுகளையும் நேரலையில் பிடிக்கும்.
tshark -i eth0 -c 100 : முதன்மையாக வரும் 100 பாக்கெட்டுகளை மட்டும் பிடித்துவிட்டுத் தானாக இயங்குவதை நிறுத்தும் (-c = Packet Count).
tshark -i eth0 -a duration:60 : 60 விநாடிகள் மட்டும் பாக்கெட்டுகளைப் பிடிக்கும் (-a = Autostop Condition).

# File Read & Write Operations (கோப்புகளில் சேமித்தல் மற்றும் வாசித்தல்)
tshark -i eth0 -w capture.pcap : பிடிபடும் பாக்கெட்டுகளை பின்னர் ஆராய்வதற்காக capture.pcap கோப்பில் சேமிக்கும் (-w = Write File).
tshark -r capture.pcap : சேமிக்கப்பட்ட .pcap கோப்பில் உள்ள பாக்கெட்டுகளைத் திரையில் வாசித்துக் காட்டும் (-r = Read File).
tshark -r capture.pcap -c 20 : .pcap கோப்பில் உள்ள முதல் 20 பாக்கெட்டுகளை மட்டும் காட்டும்.

# Capture Filters (பிடிக்கும் போதே வடிகட்டும் Filters - BPF - Berkeley Packet Filters)
tshark -i eth0 -f "host 192.168.1.100" : குறிப்பிட்ட IP முகவரிக்கு வரும்/போகும் பாக்கெட்டுகளை மட்டும் பிடிக்கும்.
tshark -i eth0 -f "port 80" : HTTP (Port 80) தரவுப் போக்குவரத்தை மட்டும் பிடிக்கும்.
tshark -i eth0 -f "not port 22" : SSH (Port 22) பாக்கெட்டுகளைத் தவிர்த்து மற்றவற்றை மட்டும் பிடிக்கும்.
tshark -i eth0 -f "icmp" : Ping (ICMP) பாக்கெட்டுகளை மட்டும் சோதிக்கும்.

## Display Filters (ஆழமான அனாலிசிஸ் வடிகட்டிகள்)
# பிடிக்கப்பட்ட பாக்கெட்டுகளில் இருந்து குறிப்பிட்ட தகவல்களை மட்டும் பிரித்தெடுக்க பயன்படும் Display Filters (-Y):
tshark -r capture.pcap -Y "ip.addr == 192.168.1.100" : குறிப்பிட்ட IP தொடர்புடைய பாக்கெட்டுகளை வடிகட்டும்.
tshark -r capture.pcap -Y "tcp.flags.syn == 1 and tcp.flags.ack == 0" : நெட்வொர்க்கில் தொடங்கும் புதிய TCP 3-Way Handshake இணைப்புகளை மட்டும் காட்டும்.
tshark -r capture.pcap -Y "http.request.method == GET" : HTTP GET கோரிக்கைகளை மட்டும் காட்டும்.
tshark -r capture.pcap -Y "dns.flags.response == 1" : DNS Response பாக்கெட்டுகளை மட்டும் வடிகட்டும்.

# Statistics & Export Options (புள்ளிவிவரங்கள் மற்றும் தரவு பிரித்தெடுத்தல்)
tshark -r capture.pcap -q -z io,phs : நெட்வொர்க்கில் எந்தெந்த புரோட்டோகால்கள் (IPv4, TCP, UDP, HTTP) எவ்வளவு சதவீதம் பயன்பாட்டில் உள்ளன என்ற படிநிலை அறிக்கையைத் தரும் (Protocol Hierarchy Statistics).
tshark -r capture.pcap -q -z conv,ip : எந்தெந்த IP முகவரிகளுக்கு இடையே அதிக அளவு தரவுப் பரிமாற்றம் நடந்துள்ளது என்ற உரையாடல்களைப் (IP Conversations) பட்டியலிடும்.
tshark -r capture.pcap -T fields -e ip.src -e ip.dst -e tcp.dstport : பாக்கெட்டுகளில் இருந்து Source IP, Destination IP, மற்றும் Destination Port ஆகிய குறிப்பிட்ட புலன்களை (Fields) மட்டும் CSV வடிவில் பிரித்தெடுக்கும்.

