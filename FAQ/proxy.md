# Proxy Kaise Kaam Karta Hai?

Normal halat mein, jab aap internet par koi website (jaise `google.com`) kholte hain, tou aap ka computer seedha us website ke server se connect hota hai. Is tarah us website ko aap ka **IP Address** aur location pata chal jati hai.

Lekin jab aap **Proxy** ka istemal karte hain, tou kahani badal jati hai:

1. **Request Bhejna:** Aap apne browser mein koi website open karte hain.
2. **Proxy ka Role:** Yeh request seedha website par jane ke bajaye pehle **Proxy Server** ke paas jati hai.
3. **Forwarding:** Proxy server aap ki request ko apne naam aur apne IP address ke sath agay us website ko bhej deta hai.
4. **Response:** Website proxy server ko data wapas bhejti hai, aur proxy server woh data aap ki screen par show kar deta hai.

> **Asaan Misaal:** karein aap ko kisi shop se koi cheez mangwani hai lekin aap nahi chahte ke dukan dar ko pata chale ke yeh cheez aap ne mangwayi hai. Aap apne dost (Proxy) ko paise de kar dukan bhejte hain. Dukan dar dost ko cheez deta hai, aur dost woh cheez aap ko la kar de deta hai. Dukan dar ko lagta hai ke khareedar aap ka dost tha!

---

# Purpose of Proxy:

Asaan alfaz mein, **Proxy** ka matlab hota hai kisi ke behalf par (kisi ki jagah) kaam karna.

Agar real life ki baat karein, tou jab aap college mein apni jagah apne dost se attendance lagwate hain, tou usay hum kehte hain ke dost ne aap ki **"proxy"** laga di. Yani kaam aap ka tha, par kiya aap ke dost ne.

## Proxy Ka Asli Purpose (Maqsad) Kya Hai?

Internet par proxy lagane ke 4 sab se bare maqsad (purposes) hote hain:

### 1. Identity Chupana (Privacy)

Normal internet chalate huay har website ko pata hota hai ke aap ka **IP Address** (aap ke internet connection ka home address) kya hai aur aap kis city/country se online hain.

* **Proxy ka faida:** Jab aap proxy use karte hain, tou website ko aap ka nahi balkay proxy server ka IP address aur location nazar aati hai. Aap ki identity chupi rehti hai.

### 2. Blocked Websites ko Kholna (Bypassing)

Agar aap ke mulk, college, ya office mein koi website ya video block hai (jaise school wale YouTube block kar dete hain):

* **Proxy ka faida:** Aap proxy server ke zariye request bhejte hain. Office ke network ko lagta hai ke aap proxy server open kar rahe hain (jo ke allowed hota hai), aur proxy agay se aap ko block hui website ka data la kar dikha deti hai.

### 3. Speed Barhana (Caching)

Bari companies aur institutions proxies ko internet speed tez karne ke liye lagate hain.

* **Proxy ka faida:** Agar college ke 500 bache aik hi website open karte hain, tou proxy server pehli baar internet se us website ka data download karke apne paas save (cache) kar leta hai. Baqi 499 bacho ko woh internet par dobara bhejne ke bajaye apne paas se hi micro-seconds mein page dikha deta hai. Is se internet bandwidth bhi bachti hai aur speed bhi tez milti hai.

### 4. Traffic Control aur Security (Firewall)

Offices aur universities nahi chahte ke un ke employees ya students ghalt ya unsafe websites kholin.

* **Proxy ka faida:** Saara internet traffic proxy ke raste se guzarta hai. Proxy aik security guard ki tarah kaam karti hai; jaise hi koi ghalt website open karne ki koshish karta hai, proxy usay wahin block kar deti hai.

---

# Proxy Server Kyun Istemal Kiya Jata Hai? (Benefits)

Log aur bari companies proxies ka istemal mukhtalif maqasid ke liye karti hain:

* **Privacy aur Anonymity:** Aap ka asli IP address hide ho jata hai, jis se websites aap ko track nahi kar saktin.
* **Bypass Geo-Restrictions:** Agar koi website ya video aap ke country (Pakistan) mein block hai, tou aap kisi aisi country ka proxy server use kar sakte hain jahan woh allowed ho.
* **Speed aur Bandwidth Saving (Caching):** Proxy servers aksar visit hone wali websites ka data apne paas save (cache) kar lete hain. Jab dobara koi wahi page mangta hai, tou proxy internet se download karne ke bajaye apne paas se hi jaldi de deta hai.
* **Access Control (Security):** Offices aur schools mein proxy laga kar kuch websites (jaise Facebook, YouTube) ko block kar diya jata hai taake log dhyan se kaam karein.

---

# 1. Proxy Dekhti Kaise Hai? (What does it look like?)

Proxy koi physical cheez nahi hoti jise aap hath mein pakar sakein. Yeh aam taur par **Text (numbers aur alphabets)** ki format mein hoti hai.

Jab bhi aap koi proxy download ya configure karte hain, tou woh aap ko is tarah ke format mein dikhti hai:

```text
IP Address : Port Number

```

## Proxy in Actual Shape:

1. **Numeric Format (IP:Port):**
> `185.23.141.2:8080`


* **`185.23.141.2`** -> Yeh us proxy server ka **IP Address** hai (yani uski location hai).
* **`8080`** -> Yeh **Port** number hai (yani us server ka woh darwaza jahan se aap ka connection enter hoga).


2. **Domain/Alphanumeric Format:**
Aksar premium ya paid proxies IP ke bajaye website ke name ki tarah dikhti hain:
> `us-register.proxyprovider.com:3128`


3. **Protocol ke Sath:**
Aksar code ya settings mein iske aage protocol bhi likha hota hai:
> `socks5://185.23.141.2:8080` ya `[http://185.23.141.2:8080](http://185.23.141.2:8080)`

---

## 2. Proxy Paid Hoti Hai Ya Publically Free?

**Yeh dono tarah ki hoti hai!** Internet par free proxies bhi milti hain aur paid (premium) proxies bhi milti hain. Lekin dono ke kaam, speed aur security mein zameen-asman ka farq hota hai.

Chalein in dono ka comparison dekhte hain taake aap ko clear ho jaye:

### A. Free / Public Proxies:

Internet par aisi saikron websites hain (jaise *ProxyScrape*, *Spys.one* wagera) jahan free proxies ki lambi lists mil jati hain.

* **Paisa:** Bilkul muft ($0). Kisi account ya signup ki zaroorat nahi hoti.
* **Masla (Downside):**
* **Bohat Slow:** Aik hi free proxy ko dunya ke hazaron log aik sath use kar rahe hote hain, jis se speed bohat slow ho jati hai.
* **Unstable:** Yeh proxies chand ghante ya aik din chalti hain aur phir band (die) ho jati hain.
* **Khatarnak (Unsafe):** Yeh kisi anjan bande ne setup ki hoti hai. Agar aap is par apna bank account ya social media login karein ge, tou woh aap ka password chura sakta hai.

### B. Paid / Private Proxies (Kharidi hui Proxies)

Yeh woh proxies hoti hain jo badi companies (jaise *Bright Data*, *Webshare*, ya *Oxylabs*) se paise de kar kharidi jati hain.

* **Paisa:** Monthly ya usage (GBs) ke hisab se paise dene parte hain.
* **Faide (Benefits):**
* **Super Fast:** Yeh sirf aap ke liye hoti hain (ya bohat kam logo mein share hoti hain), is liye speed tez hoti hai.
* **Highly Secure:** Yeh companies certified hoti hain aur aap ka data secure rakhti hain.
* **99% Uptime:** Yeh kabhi band nahi hotin, hamesha chalti rehti hain.
* **Authentication:** Inhein use karne ke liye aap ko **Username** aur **Password** milta hai taake aap ke ilawa koi aur usay use na kar sake.

---

## Summary (Aap ke Liye Kaunsi Best Hai?)

* **Free Proxy** sirf tab use karein jab aap ko koi aam blocked website check karni ho aur aap ko data security ka koi masla na ho (koi login wagera na karna ho).
* **Paid Proxy** tab zaroori hoti hai jab aap professional kaam kar rahe hon, jaise data scraping (coding ke zariye data nikalna) ya koi sensitive business work karna.

---

# Types of Proxies (Proxy ki Iqsas)

Proxies ki bohat si types hain, jinhein un ke kaam aur anonymity level ke hisab se divide kiya jata hai:

### 1. Connection ke Flow ke Hisab Se:

* **Forward Proxy:** Yeh client-side par hoti hai. Jab users ko internet access karna ho aur apni identity chupani ho, tab yeh use hoti hai (jo aam taur par hum log use karte hain).
* **Reverse Proxy:** Yeh server-side par hoti hai. Yeh website ke servers ke aage lagi hoti hai taake aane wale traffic ko manage (Load Balancing) kar sake aur servers ko hackers se bacha sake.

### 2. Anonymity (Pardadari) ke Level ke Hisab Se:

* **Transparent Proxy:** Yeh aap ki identity bilkul nahi chupata. Yeh sirf traffic filter karne ya caching ke liye schools/offices mein use hota hai.
* **Anonymous Proxy (Non-Transparent):** Yeh website ko yeh tou batata hai ke main proxy hoon, lekin aap ka asli IP address chupa leta hai.
* **Distorting Proxy:** Yeh website ko galat (fake) IP address bhejta hai taake aap ki location galat show ho.
* **High Anonymity (Elite) Proxy:** Yeh sab se secure hoti hai. Yeh website ko yeh bhi nahi pata chalne deti ke yeh koi proxy server hai, aur aap ka IP bhi bilkul safe rehta hai.

---

# Proxy vs VPN: Kya Farq Hai?

Bohat se log Proxy aur VPN (Virtual Private Network) ko aik hi samajhte hain, lekin in mein farq hai:

| Feature | Proxy Server | VPN (Virtual Private Network) |
| --- | --- | --- |
| **Working Level** | Sirf specific app ya browser par kaam karta hai. | Poore operating system ka traffic secure karta hai. |
| **Encryption** | Data encrypt nahi hota (mostly), is liye secure kam hota hai. | Data ko end-to-end encrypt karta hai, jo ke super secure hai. |
| **Speed** | Thora fast hota hai kyunki encryption nahi hoti. | Encryption ki wajah se speed thori slow ho sakti hai. |
| **Cost** | Aksar free mil jati hain. | Achhi aur secure VPN services paid hoti hain. |

---

# Kya Proxy Use Karna Safe Hai? (Risks)

Har chamakti cheez sona nahi hoti! Agar aap **Free Proxies** use kar rahe hain, tou kuch baaton ka khayal rakhna zaroori hai:

* **Data Logging:** Jo proxy server ka owner hai, woh aap ka saara traffic dekh sakta hai (aap ne kya search kiya, kaun si site kholi).
* **No Encryption:** Agar aap HTTPS ke bina koi sensitive data (passwords, credit card) bhej rahe hain, tou proxy owner usay chura sakta hai.
* **Slow Speed:** Free proxies par load zyada hota hai, is liye internet slow ho jata hai.

Kya aap kisi specific project (jaise web scraping ya API integrations) ke liye proxy ka use seekhna chahte hain, ya general knowledge ke liye pooch rahe the?