# What is urls.py?

1. `urls.py` file ka kaam hai ke jab user koi URL open kare, to us URL par kis `Function` ko call karna hai - yeh kaam `urls.py` ka hai.

2. Wo `Functions` hum `views.py` file mein define karte hain.

3. Ab user browser mein `/books/` likhega to Django `books_list()` function ko call karega jo `views.py` file ke andar define karte hain.

---

# Import Lines in urls.py File:

## 3 Types of Import:

| Type | Explanation |
|------|-------------|
| **Absolute Import** | Yeh absolute path hai - bilkul root se batata hai ke folder kahan hai |
| **Relative Import** | Yeh current folder se import kar raha hai. Dot (.) ka matlab "jahan main hoon wahi se" |
| **Direct Import** | Yeh Python ki built-in library se import karta hai |

---

## Examples with Types:

| Import Statement | Type | Reason |
|-----------------|------|--------|
| `from django.contrib import admin` | Absolute Import | Poora path root se diya hai |
| `from django.urls import path` | Absolute Import | Poora path root se diya hai |
| `from . import views` | Relative Import | Dot (.) se current folder bata raha hai |

---

## Code Example:

```python
from django.contrib import admin
from django.urls import path
from . import views
```

---

## Visual Breakdown:

```
from django.contrib import admin
        │      │             │
        │      │             └── (admin) - yeh bhi folder hai, also package bhi
        │      │
        │      └── Folder name (contrib) - yeh bhi folder hai, also package bhi
        │
        └── Main package (django) - yeh bhi folder hai, also package bhi


from django.urls import path
        │    │           │
        │    │           └── (path) - yeh FUNCTION hai
        │    │
        │    └── Folder name (urls) - yeh bhi folder hai, also package bhi
        │
        └── Main package (django) - yeh bhi folder hai, also package bhi
```

---

# How to Check Either is Function or Module:

```bash
python manage.py shell
```

```python
>>> from django.urls import path
>>> print(type(path))
# Output: <class 'functools.partial'>

>>> from django.contrib import admin
>>> print(type(admin))
# Output: <class 'module'>
```

---

# 3 Types - Ek Dum Simple Words Mein:

| Type | Python Mein | Example | Iske Saath Kya Karte Hain? |
|------|-------------|---------|---------------------------|
| **Function** | `function` | `render`, `path` | **Call** karte hain (brackets lagate hain) |
| **Class** | `type` | `HttpResponse`, `HttpRequest` | **Object** banate hain (instance create karte hain) |
| **Module** | `module` | `admin`, `models`, `os` | **Dot (.)** laga kar uske andar ki cheezein use karte hain |

# What is Routes?

Django mein Route jise URL Dispatcher ya URLconf kehte hain, aik kism ka URL hota hai. Jaise `www.example.com/contact/` jo user ki request ko sahi View Function tak pahunchana hota hai - yeh kaam Route ka hota hai.

---

# Types of Routes:

| Type | Explanation |
|------|-------------|
| **Fix Routes** | Yeh **fixed** URLs hote hain - change nahi hote, ekdum same rehte hain. `/about/`, `/contact/` |
| **Dynamic Routes** | Yeh **change hote hain** - URL mein variable hota hai jo alag-alag values leta hai. `/user/5/`, `/post/2024/` |
| **Slug Routes** | Slug ka matlab hai: URL-friendly text - spaces ki jagah - (hyphen) hota hai. `/blog/my-first-post/` |
| **API Routes** | Yeh **data send/receive** karne ke liye use hote hain. Normal websites HTML return karti hain, APIs JSON return karti hain. |
| **Router Routes** | Yeh **automatic** routes hote hain - aapko manually sab routes likhne ki zaroorat nahi hai. Django REST Framework ka feature hai.
 |

---

## Example of Routes:

```python
from django.urls import path
from . import views 

# Fix Route
path('about/', views.about , name="about")

# Dynamic Route
path('user/<int:id>/', views.user_profile , name="user")

# Slug Route
path('blog/<slug:title>/', views.blog_post , name="blog")
path('blog/<slug:post_slug>/', views.blog_detail, name='blog_detail'),
```

---
