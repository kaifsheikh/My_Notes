# What is urls.py?
1. `urls.py` is file ka kam hai ka jab User koi URL open karay tu ois URL per kis `Function` ko call karna hai yeah kam `urls.py` ka hai.
2. or wo `Functions` hum `views.py` file mein define karte hai
3. ab user browser me `/books/` likhega to Django `books_list()` ko function ko call karega jo ka `views.py` file ka andar define karte ha.

# What is Views?
1. `views.py` is file mein hum Python functions define karte hai jiska andar hum logics likhte hai jo yeah decide karta hai ke user ki request layne ka bad isko kia response (page yeah Message) show karna hai.
2. Jab user koi website page open karta hai (jaise `/books` ya `/about`) to Django ko ye decide karna hota hai ka User ko konsa Page show kiya jay Ye decision View karta hai.
3. or jo Response hum User ko Show karwate hai wo kam bhe View ka hai kue ka jo Response User ko show hota hai wo kam bhe view ka hai
3. ager hum `Wihtout App` create kare kam karte hai tu hume `Inner Folder` mein `views.py` file khud se create karne hoti hai jaha per hum Functions ko define karte hai
3. lakin jab hum koi `app create` karte hai tu waha per `views.py` phela se create hoti hai or yeh her App ka andar lazmi hoti hai.

## `Types of View`
| Type                          | Matlab                          | Kaha likhte hain |
| ----------------------------- | ------------------------------- | ---------------- |
| **Function-based View (FBV)** | Normal Python function hota hai | `views.py`       |
| **Class-based View (CBV)**    | Python class hoti hai           | `views.py`       |

# What is Template?
[Template](./MVT/Template_Static.md)

# What is Model?
1. Model decide karta hai ke database mein kya information store karne hai jaise (name, age, email) aur Data kis Type ka hoga jaise (text, number, email)
2. Model Django ka wo part hai jo database or tables ko Manage karta hai
3. her app ka andar aik `models.py` naam ki file hoti hai jisme hum apne models create karte hai.
4. Django mein model ko create karna sirf `app` ke andar possible hai, kyunki Django project directly models ko nahi samajhta. App ke andar hi migrations aur database commands chalti hain.
5. [Model](./MVT/Model.md)