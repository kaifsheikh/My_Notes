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