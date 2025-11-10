# WHat is Django

# Purpose of Learning Django

# Installation of Django
```cmd
pip install django
django-admin --version
```
## isa new project create hoga
```cmd
1. django-admin startproject mysite

2. yeah humera Project ka Structure hai:

mysite/
│
├── manage.py
└── mysite/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py

3. python manage.py runserver -> http://127.0.0.1:8000/
4. python manage.py runserver 4444 -> isa Default Port Number change hokar 4444 hojayga
```

# Understanding File Structure:
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




