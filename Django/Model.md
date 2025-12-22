# What is Model?
1. Model ek Python class hoti hai jime hum likhte hain kaunse fields (columns) honge aur unka data type kya hoga
   
2. Model decide karta hai ke database mein kya information store karne hai jaise (name, age, email) aur Data kis Type ka hoga jaise (text, number, email)
   
3. Model Django ka wo part hai jo database ke table ko represent/Describe karta hai ka oisme kitne Column hongay or Datatype kia hoge.

4. Django mein model ko create karna sirf `app` ke andar possible hai, kyunki Django project directly models ko nahi samajhta. App ke andar hi migrations aur database commands chalti hain.

## Exmaple of Model:
```py
from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField()
    file = models.FileField()

# yeah aik Model hai jo abhe sirf python code hai
```
# What is Schema?
1. Schema = Database ka blueprint, jo batata hai:
- Kaunse tables honge (jaise User, Products, Orders)
- Har table mein kaunse columns honge (jaise name, email, price)
- Kya datatype hoga (text, number, date)
- Aur tables ke beech relation kaise hoga (ForeignKey)
- Schema table ka structure (columns + Datatype) ko he Schema bolte hai.

# How to Define Rules in Model?
- `max_length = 100` -> Yeh sirf CharField aur EmailField jaisay text fields ke liye hota hai.
- `null=True` -> Yeh database ko batata hai ka “Is field ko database mein empty (NULL) rehne do, koi masla nahi.
- `blank=null` -> Yeh forms ko batata hai User form mein yeh field khaali chhor sakta hai means form validation error nahi dega.

# What is Migration?
1. Django mein jab hum model banate hain, toh woh sirf Python code hota hai jo database table ka design (structure) describe karta hai. <br>
2. Lekin yeh model khud-ba-khud database mein table nahi banata. Is design ko actual database ki table mein convert karne ke liye, hum migration commands use karte hain.
3. `python manage.py makemigrations` -> is command se migrations folder ka andar aik `0001_initial.py` file create hoti hai jo humera model ko describe karti hai
   
4. `python manage.py migrate` -> or is command se ois model ki actual Database mein Table create ho jati hai 

## Process

1. Django mein agar hum pehli baar ek model create karte hain tu `python manage.py makemigrations` chalate hain, toh Django us model ko detect karke ek initial migration file `0001_initial.py` banata hai jo database ke liye blueprint hoti hai.

2. lekin abhi table database mein create nahi hota; actual table tab create hota hai jab hum `python manage.py migrate` is command ko run karte hai tu actual Table create hoti hai.
   
3. ab Agar hum baad mein koi naya model create karte hain ya existing model mein koi change karte hain (jaise naya field add karna , rename karna , datatype change karna), tu phir se `makemigrations` wali command run karte hain, toh Django phir se nayi migration file banata hai `0002_auto_xyz.py`) jo pehli migration file ka upar depend karti hai aur batati hai ke database mein kya changes karne hain, phir jab hum `migrate` command run karte hai tu wo changes actual tables mein implement hote jate hai.
   
4. Is tarah Django ka migration system har nayi model creation ya changes ko track karta hai aur iterative process ke through database ko sync rakhta hai, jahan har change ke liye ek nayi migration file banti hai aur usko apply karne ke liye migrate chalana padta hai, aur ye process tab tak repeat hota hai jab tak hum models mein naye changes karte rehte hain.

5. maan lu jab humne first model create kara oisa makemigrations command run ki tu apke app mein migrations folder ka andar 0001_initial.py name se file create hoti hai ab ager muje ois model mein kch change karna hai jasise ka `rename , remove , add column , change datatype , etc` tu hum model mein change karke phir se makemigrations run karte hai command lakin ager 0001_initial.py file delete hogai yeah kch kisi bhe waja se wo file nhe hoti tu migrations nahe hoge kue ka new Migrations apki purane file per depend hoti hai. 

# What is Migrate?

1. Migrate Django ka command hai jo actually database me changes apply karta hai.
2. Migrate ka use karke table database me create hota hai.

# `Commands for Migrate:`

```cmd
1. python manage.py migrate
2. python manage.py createsuperuser
```
