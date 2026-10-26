# Kali Linux Inbuilt Package #6: Burp Suite (`burpsuite`) Technical Reference & Setup Guide

---

## 1. Deep Technical Introduction & Architecture (ஆழ்ந்த தொழில்நுட்ப அறிமுகம்)

**Burp Suite** என்பது Kali Linux-ல் இயல்பாகவே (Inbuilt) வரும் இணையப் பயன்பாட்டு பாதுகாப்பு மற்றும் தணிக்கைக்கான (Web Application Security Testing & Vulnerability Assessment) உலகளாவிய முதன்மை மென்பொருளாகும். இது ஒரு வெப் பிரவுசருக்கும் (Browser) இலக்கு இணையதளத்திற்கும் (Target Web Server) இடையே நின்று, இருமுனைத் தரவுப் போக்குவரத்தையும் இடைமறித்து (Intercept) அனலைஸ் செய்ய பயன்படும் **Intercepting HTTP/HTTPS Proxy Engine** ஆகும்.

### ஆழமான தொழில்நுட்பக் கூறுகள் (Core Architecture & Mechanics):

* **Intercepting Proxy Engine:**
  * பிரவுசரில் இருந்து இணையதளத்திற்கு அனுப்பப்படும் ஒவ்வொரு HTTP/HTTPS கோரிக்கையையும் (HTTP Requests & Responses) சேருமிடத்திற்குச் செல்லும் முன்பே நடுவில் தடுத்து நிறுத்தி, அதன் Header, Body, Parameters மற்றும் Cookies ஆகியவற்றை மாற்றியமைத்துச் சோதிக்க உதவுகிறது.

* **SSL/TLS Decryption & Custom CA Certificate:**
  * HTTPS நெட்வொர்க் டிராஃபிக் என்கிரிப்ட் செய்யப்பட்டிருக்கும். Burp Suite தனது சொந்த **PortSwigger CA Certificate** மூலம் "Man-in-the-Middle" நுட்பத்தைப் பயன்படுத்தி, Encrypted HTTPS பாக்கெட்டுகளை Unencrypted Plain Text-ஆக மாற்றி அனலைஸ் செய்கிறது.

* **Core Sub-Modules & Tools:**
  * **Target / Site Map:** இணையதளத்தின் அனைத்து கோப்புகள், டைரக்டரிகள் மற்றும் URL அமைப்புகளை வரைகலை மரப் படிநிலையாக (Tree Structure) வரைபடமாக்கும்.
  * **Proxy Intercept:** நேரலை HTTP Request-களை இடைமறித்து மாற்ற உதவும் முதன்மை தொகுதி.
  * **Repeater:** ஒரே HTTP கோரிக்கையை மீண்டும் மீண்டும் பல்வேறு அளவுருக்களுடன் (Parameters) கைமுறையாக அனுப்பி, சர்வரின் பதில்களைச் சோதிக்கும் தொகுதி.
  * **Intruder:** தானியங்கு முறையில் வெப் படிவங்களில் (Login Forms, URL Parameters) Fuzzing மற்றும் Parameter Manipulation சோதனைகளைச் செய்யும் இன்ஜின்.
  * **Decoder & Comparer:** Base64, URL Encoding போன்ற தரவுகளை மாற்றிப்படிக்கவும், இரண்டு HTTP Response-களுக்கு இடையே உள்ள வித்தியாசங்களைக் கண்டறியவும் பயன்படும் கருவிகள்.

* **Infrastructure Use Case (உங்கள் லேப் / கடையின் நெட்வொர்க் சோதனைக்கு):**
  * உங்கள் கேமிங் சென்டர் அல்லது நிறுவனத்திற்கான லோக்கல் வெப் போர்ட்டல்கள், பில்லிங் சாஃப்ட்வேர் அல்லது உள்நாட்டு இணையதளங்களில் XSS (Cross-Site Scripting), SQL Injection மற்றும் Session Hijacking போன்ற ஆபத்துகள் உள்ளனவா என்பதைச் சோதிக்க இது பயன்படுகிறது.

---

## 2. Package Setup & Execution Guide (நிறுவும் மற்றும் அமைக்கும் முறை)

Burp Suite Community Edition Kali Linux-ல் இயல்பாகவே சேர்க்கப்பட்டிருக்கும்.

# 1. Burp Suite மென்பொருளைத் தொடங்க
burpsuite &

# 2. Browser Proxy Setting அமைத்தல் (Firefox / Chromium)
# Proxy Host: 127.0.0.1
# Proxy Port: 8080

# 3. Burp CA Certificate இன்ஸ்டால் செய்ய
# பிரவுசரில் http://burp என்ற முகவரிக்குச் சென்று 'CA Certificate' டவுன்லோட் செய்து,
# Browser Settings -> Certificates -> Import -> Trust for Websites என அமைக்க வேண்டும்.

## Categorized Command & Module Reference (கருவிகள் மற்றும் விளக்கங்கள்)
# A. Core CLI & Launch Commands (இயக்கும் கட்டளைகள்)
burpsuite : Burp Suite Graphical User Interface (GUI)-ஐத் தொடங்கும் முதன்மைக் கட்டளை.
burpsuite --project-file=my_audit.burp : முந்தைய சோதனையின் தரவுகள் சேமிக்கப்பட்ட பிராஜெக்ட் கோப்பை திறக்கும்.

# B. Proxy & Intercept Module (தரவு இடைமறிப்பு மேலாண்மை)
Proxy -> Intercept -> Intercept is ON : பிரவுசரில் இருந்து செல்லும் அனைத்து HTTP கோரிக்கைகளையும் தடுத்து நிறுத்தும்.
Forward : இடைமறிக்கப்பட்ட கோரிக்கையை (Request) திருத்திய பின் அல்லது மாற்றாமல் இலக்கு வெப் சர்வருக்கு அனுப்பி வைக்கும்.
Drop : இடைமறிக்கப்பட்ட கோரிக்கையை வெப் சர்வருக்கு அனுப்பாமல் பாதியிலேயே ரத்து செய்யும்.
Action -> Send to Repeater (Ctrl + R) : தேர்ந்தெடுக்கப்பட்ட கோரிக்கையை கைமுறை சோதனைக்காக Repeater தொகுதிக்கு அனுப்பும்.
Action -> Send to Intruder (Ctrl + I) : தேர்ந்தெடுக்கப்பட்ட கோரிக்கையை தானியங்கு Fuzzing சோதனைக்காக Intruder தொகுதிக்கு அனுப்பும்.

# C. Repeater Module (கைமுறை லூப்ஹோல் பரிசோதனை)
Send : மாற்றியமைக்கப்பட்ட HTTP Request-ஐ சர்வருக்கு அனுப்பி உடனடியாக Response-ஐப் பெறும்.
Request / Response Viewers : Raw, Pretty, Hex, Render ஆகிய வடிவங்களில் HTTP பாக்கெட்டுகளை பார்வையிடும் வசதி.

# D. Intruder Module Attack Types (தானியங்கு Fuzzing முறைகள்)
Sniper : ஒரு நேரத்தில் ஒரு Parameter-ஐ மட்டும் தேர்வு செய்து அகராதியில் உள்ள வார்த்தைகளைச் செலுத்திச் சோதிக்கும்.
Battering Ram : அனைத்து Parameters-களிலும் ஒரே நேரத்தில ஒரே வார்த்தையைச் செலுத்திச் சோதிக்கும்.
Pitchfork : பல அகராதிகளைப் பயன்படுத்தி, ஒவ்வொரு Parameter-க்கும் இணையான வார்த்தைகளை ஒரே நேரத்தில் சோதிக்கும்.
Cluster Bomb : பல அகராதிகளில் உள்ள அனைத்து வார்த்தைகளின் சாத்தியமான சேர்க்கைகளையும் (All Combinations) முழுமையாக சோதிக்கும்.

# E. Decoder & Utility Tools (தரவு மாற்றுக் கருவிகள்)
Decode as -> Base64 / URL / Hex : என்கோட் செய்யப்பட்ட உரைத் தரவை இயல்பான உரையாக மாற்றிப் படிக்கும்.
Encode as -> URL / Base64 : சாதாரண உரையை வெப் அப்ளிகேஷன் புரிந்து கொள்ளும் வடிவத்திற்கு மாற்றும்.