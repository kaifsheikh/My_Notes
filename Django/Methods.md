## Context:
1. Context ek dictionary hoti hai jisme woh data hota hai jo hum apni view (Python file) se template (HTML file) ko bhejna chahte hain.
2. hum Direct koi Data pass nahe kar sekhte hai jo bhe Data hoga wo Dictionary mein he Pass hoga.
3. Jo data Python mein hota hai (name, list, database results), woh HTML tak nahi jata tu isliye hum Context ko aza bridge ki terha use karte hai jisa View se HTML tak data bhejne ja sakay jiska liye hum“context” ka use karte hai.
4. Context sirf render() function ke andar use hota hai or render() mein 3 parameters expect karta hai.

## Example 01:
```py
# home/views.py
from django.http import HttpResponse
from django.shortcuts import render

def home(request):

    persons = [
        {'id': 2345, 'name': 'John Doe', 'email': 'johndoe@example.com', 'age': 28, 'city': 'New York'},
        {'id': 7856, 'name': 'Alice Smith', 'email': 'alice.smith@example.com', 'age': 35, 'city': 'Los Angeles'},
        {'id': 4567, 'name': 'Bob Johnson', 'email': 'bob.johnson@example.com', 'age': 42, 'city': 'Chicago'}
    ]

    context = { "person" : persons }

    return render(request , 'index.html' , context)

# home/templates/index.html
<table border="1">
            <tr>
                <th>Id</th>
                <th>Name</th>
                <th>Email</th>
                <th>Age</th>
                <th>City</th>
            </tr>

            {% for a in person %}
            <tr>
                <td>{{ forloop.counter }}</td>
                <td>{{ a.name }}</td>
                <td>{{ a.email }}</td>
                <td>{{ a.age }}</td>
                <td>{{ a.city }}</td>
            </tr>
            {% endfor %}

</table>

# project_name/urls.py
from Home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.home)
]
```

# A way to redirect to another page after clicking a link?
1. `urls.py` file mein `name='products'` iska naam humne use kiya hai.
2. `templates/base.html` is file mein `href="{% url 'product' %}"` use kiya hai

```py
# urls.py
urlpatterns = [
    path('products/' , views.products , name='product'),
]
```

```py
# views.py
def products(request):
    return render(request , 'products.html')
```

```py
# templates/base.html
<li class="nav-item">
    <a class="nav-link" href="{% url 'product' %}">Products</a>
</li>
```

## If we want to display dynamic code between the header and footer, but we only want to show a limited portion of the dynamic code (meaning not all of it), then for that

1. iska matlab hai jab ap `sigup.html` or `products.html` files per jaogay tu oisme `hide_extra_code` yeah wala code nahe ayga in files mein kue ka humne waha per if condition lagai hue hai or oinhe `products function` mein or `sigup function` mein use kiya hua hai. 
```py
# urls.py
urlpatterns = [
    path('products/' , views.products , name='product'),
    path('sigup/' , views.sigup , name='register')
]
```
```py
# views.py
def products(request):
    return render(request , 'products.html' , {'hide_extra_code' : True})

def sigup(request):
    return render(request , 'register/sigup.html' , {'hide_extra_code' : True})
```
```py
# templates/base.html
  {% if not hide_extra_code %}

    # Categories ka code

    # Banner Code

    # etc...

  {% endif %}
```