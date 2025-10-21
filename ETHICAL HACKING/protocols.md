# Protocols
Protocol = Rules/Language jo computers ek doosre se baat karne ke liye use karte hain.<br>
Agar sab apni apni language use karenge to communication possible hi nahi hoga. Protocol ensure karta hai ke dono (sender aur receiver) ek hi tarike se data ko samjhein.<br>

## Example of Protocols
1. HTTP / HTTPS - (Websites open karne ke liye)
2. FTP - (Files transfer karna (upload/download)
3. SMTP / IMAP / POP3 (Emails bhejne/receive karne ke liye)
4. TCP / UDP (Ye transport layer protocols hain (data bhejne ka tareeqa)

# Flags

1. Har protocol ke apne rules hote hain.
2. Kuch protocols ke paas flags hote hain (jaise TCP).
3. Kuch protocols ke paas flags bilkul nahi hote (jaise UDP).
4. Flags = signals/Indicators hote hai jo packets ke sath jaate hain, aur computer ko batate hain ke yeh packet kis purpose ke liye bheja gaya hai (start, confirm, end, urgent, cancel, etc.) yeah Chhote signals batate hain "iska kya kaam hai".

# What is Packet?
1. Packet = humara data ka ek chhota tukda hota hai jo network ke through travel karta hai.
2. Agar tum ek file, message ya video bhejte ho → usko ek saath nahi bheja jata.
3. Usko chhote-chhote parts (packets) me tod diya jata hai.
4. Har packet me tumhara data ka ek hissa + address + instructions hote hain.
5. Jab ye packets destination (dusre computer/server) pe pohanch jaate hain → wahan dubara jod diye jaate hain → aur tumhe poora data mil jata hai.

## TCP - (Important Flags)
## 1. SYN (Synchronize)

* **Purpose:** Connection start karne ke liye.
* **Example:** Browser: "Server bhai, connection shuru karna hai."

## 2. ACK (Acknowledge)

* **Purpose:** Packet receive hone ki confirmation.
* **Example:** Server: "Theek hai, tumhara message mil gaya."

## 3. FIN (Finish)

* **Purpose:** Connection close karne ke liye.
* **Example:** Browser: "Ab kaam khatam, connection band kar do."

## 4. RST (Reset)

* **Purpose:** Turant connection rokne ke liye.
* **Example:** Server: "Ye galat request hai, turant cancel kar do."

## 5. PSH (Push)

* **Purpose:** Data turant bhejne ke liye (buffer ka wait mat karo).
* **Example:** Chat message: "Abhi bhejo, delay mat karo."

## 6. URG (Urgent)

* **Purpose:** Jaldi deliver karne wala data.
* **Example:** Emergency signal: "Yeh packet urgent hai, sabse pehle process karo."
