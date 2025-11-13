# WHat is Django

# Purpose of Learning Django

# Installation of Django

| **Step** | **Command** | **Description (Easy Words)** |
|-----------|--------------|-------------------------------|
| **1** | `pip install django` | Ye command Django ko install karti hai Python environment mein. (Internet se Django download aur setup hota hai.) |
| **2** | `django-admin --version` | Ye check karta hai ke Django install hua hai ya nahi, aur agar hua hai to kaunsa version hai. |
| **3** | `django-admin startproject mysite` | Ye ek naya Django project create karta hai jiska naam “mysite” hoga. |
| **4** | `python manage.py runserver` | Ye command Django ka development server start karti hai. Default address hota hai **http://127.0.0.1:8000/** |
| **5** | `python manage.py runserver 4444` | Is command se server **port 8000** ki jagah **4444** pe run hota hai. (Address: **http://127.0.0.1:4444/**) |
| **6** | `python manage.py startapp home` | Ye command ek “App” create karti hai. |

---

✅ **Note:**  
- App Django ke project ka aik chhota part (module) hota hai — jo specific kaam karta hai.
- App → us website ke andar ek “feature” ya “section” banana ka liye use hote hai hai
- App banana ka reason ye hai ke hum apni website ke har feature (kaam) ko alag-alag rakh sakein.
Taake project organized, clean, aur reusable rahe.



# Understanding File Structure:
1. yeah humera Project ka root Structure hai:
   
```cmd
firstSite/
│
├── manage.py
└── firstSite/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py

```

## `firstSite/`
1. Outer Folder: `firstSite/` (Project Root Folder)
2. iska andar aik file hoti hai `manage.py`
3. Ye Django ka project manager file hai.
4. Isse hum project ke commands run karte hain.

## `firstSite/`
1. Inner Folder: `firstSite/` (Project Configuration Folder)
2. Ye folder project ke settings aur configuration rakhta hai.
3. matlab ye bataata hai Django ko tumhara project kaise run karna hai
4. Iske andar `5 main files` hoti hain.

## `settings.py`
1. Ye sabse important file hai. Isme project ki configuration / settings hoti hain.


## `urls.py`
1. Ye project ke routes (links / paths) control karta hai.

## `asgi.py`
1. Ye file Django ko ASGI (Asynchronous Server Gateway Interface) mode me chalane ke liye hoti hai.

2. Iska kaam backend level par hota hai —
ye real-time features (jaise chat apps, live updates) ke liye use hoti hai.

## `wsgi.py`
1. Ye file Django ko WSGI (Web Server Gateway Interface) mode me chalane ke liye hoti hai.

2. Ye mainly production servers ke liye use hoti hai — jab project live karte ho (deploy karte ho).

## Why we Create Template or Static Folder?
1. Django backend Manage karta hai,
2. lekin frontend (HTML, CSS, JS or Images) ko Manage karne ka liya oisa Read karne ka liya hum `Templates` or `Static` folder create karte hai.

## `Templates` (HTML ke liye):
1. Templates wo folder hota hai jisme HTML files rakhi jaati hain —
ye files website ka page structure dikhati hain (like Home, About, Contact).

## `Static` (CSS, JS, Images ke liye):
1. Static folder mein CSS, JavaScript, aur images rakhi jaati hain ye files website ka design aur look banati hain.




