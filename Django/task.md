```py
# urls.py
from django.contrib import admin 
from django.urls import path
from . import views 

urlpatterns = [
    path('home/' , views.home , name='home')
]

# views.py
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {
        'person': {
            'name': 'Ahmed Raza',
            'age': 28,
            'address': {
                'city': 'Karachi',
                'country': 'Pakistan',
                'zip_code': '75500'
            },

            'contacts': {
                'email': 'ahmed@example.com',
                'phone': '+92 300 1234567'
            }
        }
    }
    return render(request, 'header/index.html', context)

# template/header/index.html
<h1>{{ person.name }}</h1>
<p>Age: {{ person.age }}</p>

<p>City: {{ person.address.city }}</p>
<p>Country: {{ person.address.country }}</p>
<p>Email: {{ person.contacts.email }}</p>
<p>Phone: {{ person.contacts.phone }}</p>
```


# Data with Model

```py
# app/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)      # Student ka naam
    email = models.EmailField()                   # Email address
    phone = models.CharField(max_length=15)       # Phone number
    age = models.IntegerField()                   # Age
    course = models.CharField(max_length=100)     # Course name
    
    def __str__(self):
        return self.name

# python manage.py makemigrations
# python manage.py migrate
```

```html
<!-- student_form.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Student Registration</title>
</head>
<body>
    <h2>Student Registration Form</h2>
    
    <!-- Form jahan student data bharega -->
    <form method="POST" action="{% url 'save_student' %}">
        {% csrf_token %}
        
        <label>Name:</label>
        <input type="text" name="name" required>
        <br><br>
        
        <label>Email:</label>
        <input type="email" name="email" required>
        <br><br>
        
        <label>Phone:</label>
        <input type="text" name="phone" required>
        <br><br>
        
        <label>Age:</label>
        <input type="number" name="age" required>
        <br><br>
        
        <label>Course:</label>
        <input type="text" name="course" required>
        <br><br>
        
        <button type="submit">Save Data</button>
    </form>
</body>
</html>
```

```py
# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student

def student_form(request):
    return render(request, 'student_form.html')

# Yeh function data save karne ke liye
def save_student(request):
    
    if request.method == 'POST':
        
        student_name = request.POST.get('name')
        student_email = request.POST.get('email')
        student_phone = request.POST.get('phone')
        student_age = request.POST.get('age')
        student_course = request.POST.get('course')
        
        Student.objects.create(
            name=student_name,
            email=student_email,
            phone=student_phone,
            age=student_age,
            course=student_course
        )
        
        messages.success(request, "Student registered successfully!")
        
        return redirect('student_form')
    
    return redirect('student_form')
```

```py
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.student_form, name='student_form'),
    path('save/', views.save_student, name='save_student'),
]
```
