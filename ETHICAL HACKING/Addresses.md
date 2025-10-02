# Total Address in Communication Devices?
1. IP Address ( Private / Public )
2. MAC Address ( Hardware MAC Address )
3. Localhost Address - 127.0.0.1 ( Inrternal Processing Address ) yeah subka pass same hota hai.

# Type of Type

# DHCP or ARP

# SIP or DIP

1. SIP ( Source IP Address ) = Sender ka ghar ka address.
2. DIP ( Destination IP Address ) = Receiver ka ghar ka address.

3. ager mein apne laptop ka IP Address se 192.168.1.10 Google.com ko request bhejte ho → tu yeah mera laptop ka SIP Address hai jo mena google.com ka server per bheja hai means (Sender mein ho)

4. or google.com ne mera SIP ko Recive kiya hai tu google.com DIP address hai kue ka oisne mera SIP Address ko Receive kiya hai

# Examples

# 🌐 YouTube Access Karne Ka Safar (NAT)

Jab aapne apne mobile mein YouTube.com likhkar enter kiya, to yeh request is tarah aage badhi:

---

## 1. 📱 Aapke Mobile Se Router Tak (Private Network)

* Aapka Mobile aapke Router se Private Network par connected hai.
* Aapke Mobile aur Router, dono ka Private IP Address hota hai (jaisa ke: 192.168.1.5 aur 192.168.1.1).

Jab aap YouTube kholte hain, to aapka mobile request bhejta hai ke "Mujhe YouTube.com ka server chahiye". Yeh request pehle aapke Router ke paas jaati hai.

Router jaanta hai ke is request ko Internet par aage bhejna hai, isliye woh isay tayyar karta hai.

---

## 2. 📡 Router Se Internet Tak (Public Network)

* NAT (Network Address Translation) ka kaam yahan shuru hota hai.

* Router jaanta hai ke Internet par Private IP Address kaam nahi karte, sirf Public IP Address chalte hain.

* Router aapke mobile ki Private IP ko chupa deta hai aur uski jagah apni Public IP Address (jo aapko Internet Service Provider – ISP ne di hai) lagata hai.

* Router is request ko "Translation Table" mein record kar leta hai (yaad rakhne ke liye ke yeh request kis Private IP se aayi thi).

* Ab, yeh request aapke Router ke Public IP ke saath YouTube.com ke server ki taraf Internet par bhej di jaati hai.

---

## 3. 🖥️ YouTube Server Se Wapas Router Tak

* YouTube.com ka server request dekhta hai.
* Woh sochta hai ke "Yeh request Public IP 'X' (aapke router ki Public IP) se aayi hai".
* Server YouTube ka data is Public IP 'X' par wapas bhej deta hai.

---

## 4. ↩️ Router Se Wapas Mobile Tak

* Request jab aapke Router ke paas wapas aati hai, to Router apne Translation Table mein dekhta hai ke "Acha! Yeh data to Private IP 'Y' (aapke mobile ki Private IP) ke liye manga gaya tha".
* Router dobara NAT ka istemaal karta hai aur Public IP 'X' ko hata kar Mobile ki Private IP 'Y' laga deta hai.
* Aakhir mein, YouTube ka data aapke Mobile tak pahunch jaata hai aur aapko video dikhai dene lagti hai!
