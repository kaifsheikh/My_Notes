## Context:
1. Context ek dictionary hoti hai jisme woh data hota hai jo hum apni view (Python file) se template (HTML file) ko bhejna chahte hain.
2. hum Direct koi Data pass kar kar sekhte hai jo bhe Data hoga wo Dictionary mein he Pass hoga.
2. Jo data Python mein hota hai (name, list, database results), woh HTML tak nahi jata tu isliye hum Context ko aza bridge ki terha use karte hai jisa View se HTML tak data bhejne ja sakay jiska liye hum“context” ka use karte hai.
3. Context sirf render() function ke andar use hota hai or render() mein 3 parameters expect karta hai.

## Example 01:
```py
# views.py
from django.shortcuts import render # HTML page ko render karne ka liye import kiya hai

def home(request):

    person = {
        "name": "Kaif",
        "age": 22,
        "city": "Karachi"
    } # Dictionary

    context = { "stu_data" : person }
    
    return render(request , "index.html" , context)

# templates/index.html
<ul>
    <li>Name : {{ stu_data.name }}</li>
    <li>Age : {{ stu_data.age }}</li>
    <li>City : {{ stu_data.city }}</li>
</ul>

# urls.py
from home import views # home app se views ko import kiya hai

urlpatterns = [
    path('homePage/', views.home) # homePage/ ka route per run hoga yah 
]
```

https://youtu.be/oAitS1e2UsI?si=iR5-BxhO5lMJZgeC&t=423