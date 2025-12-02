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
1. jab hum Django Project Create karte hai tu wo By Default 2 folders create karta hai oisi naam ka jo humne django Project Create karte time diya tha.

```py
firstSite/ # Outer Folder
│
├── manage.py 
|
└── firstSite/ # Inner Folder
    |
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

# Outer Folder
- `Outer folder` isko `Root folder` bhe bolte hai kue ka iska andar hum `Django App` create karte hai.
- `Static Folder` isme Image , Css or JS ki file hoti hai
- `Templates Folter` isme Html ki files hoti hai
- `manage.py` yeah file bhe outer folder mein hoti hai jo project ko run karte hai

# Inner Folder

- `Inner Folder` isko (Project Configuration Folder) bolte hai
- iska andar humari Actual Files hoti hai Django ki jaise `urls.py` , `settings.py`
- Inner folder mein jo files hoti hai waha se humera project Operate hota hai.

## `settings.py`
- Ye sabse important file hai. Isme project ki configuration / settings hoti hain.

## `urls.py`
- Ye project ke routes (links / paths) control karta hai.

## `asgi.py`
- Ye file Django ko ASGI (Asynchronous Server Gateway Interface) mode me chalane ke liye hoti hai.

- Iska kaam backend level par hota hai —
ye real-time features (jaise chat apps, live updates) ke liye use hoti hai.

## `wsgi.py`
- Ye file Django ko WSGI (Web Server Gateway Interface) mode me chalane ke liye hoti hai.

- Ye mainly production servers ke liye use hoti hai — jab project live karte ho (deploy karte ho).




