# 1. What is Session:

1. **PHP Session** ek **server-side** mechanism hai jo kisi user ki information ko multiple web pages/requests ke darmiyan temporarily store aur access karne ke liye use hota hai.

2. Session PHP ko yaad rakhne mein help karta hai ke website par current user kaun hai aur uske baare mein kya information temporarily Store karni hai.

3. Normally HTTP requests independent hoti hain means.

## Purpose:
1. Session ka purpose website ko ye yaad rakhwana hai ke user kaun hai aur uski temporary information kya hai.

1. **Maan lo tum login karte ho**.

```text
login.php
   ↓
Username: kaif
Password: ****
   ↓
Login successful
```

Ab PHP hume `dashboard.php` par redirect karti hai.

```text
dashboard.php
```

tu Problem ye hai ka, **dashboard.php ko kaise pata chalega ke Kaif login kar chuka hai yeah nhe?**

HTTP requests normally independent hoti hain.

```text
Request 1 → login.php

Request 2 → dashboard.php

Request 3 → profile.php
```

1. PHP automatically ye assume nahi karta ke **Request 2** wala user wahi hai jo **Request 1** mein login hua tha. yeah jo **Request 1** wala user jisne login kiya tha kia wahi user **Request 3** mein hai yeah koi or PHP ko iska koi idea nhe hota hai kue ka HTTP requests normally independent hoti hain.

## Example:

```text
Login.php → after successfull login
  ↓
Session create hua → or user ki info session mein save hue.
  ↓
Dashboard.php → session read hua or check kiya
  ↓
profile.php → same here session read & check
  ↓
logout.php → session destory & redirect login.php
```

Iska flow:

```text
             login.php
                  |
                  ↓
           session_start()
                  |
                  ↓
        Login successful?
             /        \
           YES         NO
            |           |
            ↓           ↓
     Session create   Error
            |
            ↓
   $_SESSION['user_id']
   $_SESSION['name']
            |
            ↓
        dashboard.php
            |
            ↓
       session_start()
            |
            ↓
   $_SESSION['user_id'] ?
          /           \
        YES            NO
         |              |
         ↓              ↓
    Dashboard        login.php
```

---

# What is Session Identifier:

1. **Session Identifier** ek unique **Session ID** hoti hai jo **String** format mein hoti hai.

2. is **Session_Id** ka kam hai server ko batana ke ye request kis user's session se related hai.

## Example: 

1. Jab hum PHP mein session start karte hai **session_start();yeah session create karta hai tu ois time aik **session_id** generate hoti hai.

2. ois session_id ko hum **Session Identifier / Session ID** kehte hain.

```text
Session ID
    ↓
ABC123XYZ789
```

3. yeah session_id tab ati hai jab hum session ko start karte hai **session_start();**

4. Agar current browser ke liye pehle se session nahi hai, to PHP **new session start/create** karta hai aur us session ke liye ek unique Session ID generate karta hai.

Simple flow:

```text
session_start()
      ↓
New Session ID generate hue
      ↓
Session ID client ka browser mein cookie mein store hoti hai.
      ↓
Cookie ka naam usually PHPSESSID hota hai jisa Key bolte hai
```

Lekin agar session pehle se exist karti hai, to:

```text
session_start()
      ↓
Existing session identify
      ↓
Wahi existing Session ID
      ↓
client Browser mein Cookie mein stored hoti hai
      ↓
PHPSESSID = Session ID
```

Isliye **har page par new Session ID create nahi hoti.**

---

# 9. Tumhare Auth System ka Complete Flow

```text
login.php
    ↓
User login karta hai
    ↓
Login successful
    ↓
Session create/start hota hai
    ↓
User ki info session mein save hoti hai
    ↓
Session ki ek unique ID hoti hai
    ↓
dashboard.php
    ↓
session_start()
    ↓
Wahi existing session access hota hai
    ↓
Session ki ID same rehti hai
    ↓
Session se user ki information mil jaati hai
```

---

1. Jab user dashboard.php par jata hai after login, to PHP browser mein stored **PHPSESSID** ko kis ke saath match/identify karta hai jisa wo dashboard.php mein allow karta hai?

Simple flow:

```text
login.php
   ↓
session_start()
   ↓
Session ID generate hui
   ↓
Browser Cookie mein store
   ↓
PHPSESSID = ABC123
```

Phir user `dashboard.php` par jata hai:

```text
dashboard.php
    ↓
session_start()
    ↓
Browser se PHPSESSID = ABC123 mila
    ↓
PHP server par bhe ABC123 wali Session Data mila
    ↓
Browser PHPSESSID & PHP Server - ager dono match
    ↓
YES → Session Data Access karo:
    ↓
user_id = 5
name = Kaif
    ↓
Dashboard
Welcome, Kaif
```