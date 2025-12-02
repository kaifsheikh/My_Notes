# What is urls.py?
- `urls.py` is file ka kam hai ka jab User koi URL open karay tu ois URL per kis `Function` ko call karna hai yeah kam `urls.py` ka hai.

- or wo `Functions` hum `views.py` file mein define karte hai

- ab user browser me `/books/` likhega to Django `books_list()` ko function ko call karega jo ka `views.py` file ka andar define karte ha.

# What is Views?
1. `views.py` is file mein hum Python functions define karte hai jiska andar hum logics likhte hai jo yeah decide karta hai ke user ki request layne ka bad isko kia response (page yeah Message) show karna hai.

2. Jab user koi website page open karta hai (jaise `/books` ya `/about`) to Django ko ye decide karna hota hai ka User ko konsa Page show kiya jay Ye decision View karta hai.

3. or jo Response hum User ko Show karwate hai wo kam bhe View ka hai kue ka jo Response User ko show hota hai wo kam bhe view ka hai

3. ager hum `Wihtout App` create kare kam karte hai tu hume `Inner Folder` mein `views.py` file khud se create karne hoti hai jaha per hum Functions ko define karte hai

3. lakin jab hum koi `app create` karte hai tu waha per `views.py` phela se create hoti hai or yeh her App ka andar lazmi hoti hai

4. 

## `Types of View`
| Type                          | Matlab                          | Kaha likhte hain |
| ----------------------------- | ------------------------------- | ---------------- |
| **Function-based View (FBV)** | Normal Python function hota hai | `views.py`       |
| **Class-based View (CBV)**    | Python class hoti hai           | `views.py`       |

# What is Template?
1. HTML page banana
2. View se aaya hua data show karna
3. Page ko design karna (CSS, Bootstrap, Tailwind)
4. Loops & conditions (sirf display ke liye)


## Example 01 ( Without using Model only `VT` ):
```py
# urls.py
urlpatterns = [
    path('books/', views.books_list),
]

#views.py
def books_list(request):
    books = [
        {"title": "Python", "author": "Guido"},
        {"title": "Django", "author": "Adrian"},
    ]

    return render(request, 'books.html', {'books': books})

# templates/books.html
<h1>Books List</h1>

<ul>
  {% for b in books %}
    <li>{{ b.title }} - {{ b.author }}</li>
  {% endfor %}
</ul>
```
> - jab user ne Browser mein `/book/` likha. <br>
> - tu yeah `views.py` file ka andar `books_list()` naam ka function ko call kiya. <br>
> - ois function mein `books` ka data laykar `render` kardiya `templates` folder mein `books.html` file ka andar.

# What is Model?
1. Model decide karta hai ke database mein kya information store karne hai jaise (name, age, email) aur Data kis Type ka hoga jaise (text, number, email)
2. Model Django ka wo part hai jo database or tables ko Manage karta hai
3. her app ka andar aik `models.py` naam ki file hoti hai jisme hum apne models create karte hai

## Example 01 (MVT):

1. Browser opens `/patients/` → `urls.py` → `views.py` (`patients_list`) → `models.py` (DB query) → `views.py` → `templates/patients.html` → Browser shows HTML

## Example 01:
```py
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.patients_list),
]

# views.py
from django.shortcuts import render
from .models import Patient

def patients_list(request):
    patients = Patient.objects.all()  # Model se database ka data fetch
    return render(request, 'patients.html', {'patients': patients})

# models.py
from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

# templates/patients.html
<h1>Patients List</h1>

<ul>
  {% for p in patients %}
    <li>{{ p.name }} - {{ p.age }} years - {{ p.email }}</li>
  {% endfor %}
</ul>
```