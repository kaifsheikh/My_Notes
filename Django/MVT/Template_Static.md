## Why we Create Template or Static Folder?
1. Django backend Manage karta hai,
2. lekin frontend (HTML, CSS, JS or Images) ko Manage karne ka liya oisa Read karne ka liya hum `Templates` or `Static` folder create karte hai.

## `Templates` (HTML ke liye):
1. Templates wo folder hota hai jisme HTML files rakhi jaati hain —
2. ye files website ka page structure dikhati hain (like Home, About, Contact).

## `Static` (CSS, JS, Images ke liye):
1. Static folder mein CSS, JavaScript, images yeah Fonts ki Files rakhi jaati hain ye files website ka design aur look banati hain.


dehko aik tu yeah terika hai ka mein her app ka andar static or template folder create  karo or waha per images image or html ki files rekho right oiska liya kia settings.py mein changes karne hoge iska batao

yeh phir mein aik static or templates ka folder banao apne root folder mein oiska liye kia process hoga iska bhe batao easy karke

# 2 terika se hum Static or Templates folder ka use karte hai:

## Option 01:
1. Har `App` ke andar `static` aur `templates` folder create karna jisa humera code boht organize ho jata hai.
2. ager hum option 1 pattern se project create kar reha hai tu jo settings.py file mein options hote hai wo default set hote hai.

## Option 02:
1. yeah phir `Root` folder me ek hi `static` aur ek hi `templates` folder create kardyna.
2. jisa sara Static Data aik he folder mein hota hai like images or js ka code or HTML ki sari file aik he folder mein hoge templates mein.
3. isme kch settings ko change karna hota hai `settings.py` file ka andar.

```py
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",   # <-- root-level static folder
]

'DIRS': [BASE_DIR / "templates"],

# ager yeah code nahe hai settings.py file mein tu iska add karna hota hai bs
```