# What is urls.py?
- ab user browser me `/home/` likhega
- to Django `views.py` file ke andar `home()` function ko call karega.

## Example 01:
```py
from home import views

urlpatterns = [
    path('home/', views.home),
]
```
# What is View?
1. User ki request lene ke baad, usko kya response (page ya message) dekhta hai means.
2. Jab user koi website page open karta hai (jaise `/home` ya `/about`) to Django ko ye decide karna hota hai ka User ko konsa Page dikhaya jaye Ye decision View karta hai.
3. jab hum koi app create karte hai tu `views.py` yeah file lazmi hoti hai
4. is file mein Python function hote hai jo decide karta hai ke user ko kya dikhana hai. 

## Exmaple 01:
```py
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello World")
```

## `Types of View`
| Type                          | Matlab                          | Kaha likhte hain |
| ----------------------------- | ------------------------------- | ---------------- |
| **Function-based View (FBV)** | Normal Python function hota hai | `views.py`       |
| **Class-based View (CBV)**    | Python class hoti hai           | `views.py`       |