# Python OOP

1. OOP (Object-Oriented Programming) ek aisa **programming style** hai jismein hum apne code ko real-world ki cheezon **objects** ke hisaab se design karte hain.

2. Jab hum barra software banate hain, toh simple code mushkil aur messy ho jata hai. OOP hamare code ko organize, saaf, aur re-usable banane mein madad karta hai.

# OOP Purpose:

1. **Reusability (Dobara Istemaal):** Ek baar code likh lo, phir usko baar baar bina dobara likhe istemaal karo.
2. **Organization:** Code chote chote hisson (classes aur objects) mein taqseem ho jata hai, jisse samjhna aasan hota hai.
3. **Easy Maintenance:** Agar kisi ek hisse mein bug ya masla aaye, toh poore program ko chede bina sirf us hisse ko theek kiya ja sakta hai.
4. **Security & Structure:** Real-world concepts ko code mein laana aasan ho jata hai.

---

# Class?

1. Class ek **blueprint ya template** hai.
2. Yeh asli cheez nahi hoti, balki yeh sirf yeh bataati hai ke jab koi real object bad mein banega, toh uske paas kya kya data hoga aur woh kya kya kaam kar sakegi.
3. Class ka andar 2 cheezay hoti hai.
    - Attributes **Variables**: Cheez ki khususiyaat (e.g., Naam, Rang, Qeemat).
    - Methods **Functions**: Cheez ke kaam ya actions (e.g., Chalna, Bolna, On/Off hona).

# Object:

1. Object class ka **practical version** aik Real Instance hota hai.
2. Aapke aas paas jo bhi asli cheez majood hai jisko aap dekh, chhoo, ya istemaal kar sakte hain — programming mein woh ek **Object** hai.

# Class vs Object (Direct Comparison):

| Feature | Class | Object |
| --- | --- | --- |
| **Defination** | Yeh ek **Blueprint / Naqsha** hai jo bataata hai ke cheez kaisi hogi. | Yeh class se bani **Asli Cheez (Real Instance)** hoti hai. |
| **Physical Existence** | Yeh sirf code/concept hota hai, memory mein jagah nahi leta. | Yeh computer ki memory mein jagah (RAM) leta hai. |
| **Example (Real Life)** | Car ka paper par bana design. | Aap ke ghar ke bahar khadi asli Car. |
| **Example (Python)** | `class Car:` | `my_car = Car("Honda", "Black")` |
| **Quantity** | Class poore program mein ek hi baar banai jaati hai. | Ek hi class se aap **unlimited objects** bana sakte hain. |

### Example: 

```py
class Phone: # Class
    def __init__(self, brand_name):
        self.brand = brand_name

my_phone = Phone("Samsung") # Object
print(my_phone.brand)  # Output: Samsung
```
### Step-by-Step Easy Explanation

#### 1. `def __init__(self, brand_name):`
* `__init__()` isko Initialization bolte hai yeah new object ko ready karta hai.

* ab aap class se naya object banate hain, toh Python is function ko **automatically** chala deta hai. Aap ko isey alag se call karne ki zaroorat nahi parti.

* `self`: Yeh object ki api pehchan hai. Yeh Python ko batata hai ke "Yeh jo data aa raha hai, yeh IS KHASS object ka hai".

* `brand_name`: Yeh woh khali jagah **variable** hai jismein hum bahar se koi naam bhejenge (jaise "Samsung", "iPhone").

* `my_phone = Phone("Sumsung")` Yeh woh line hai jahan humne class ka asli Object banaya hai `Phone("Sumsung")` yeah class ka naam hai or `my_phone` yeah asli object hai.

### Example:
```py
class Mobile:
    def __init__(self, brand_name, car_color):
        self.b = brand_name
        self.c = car_color
        
obj1 = Mobile("Samsung", "Red")

# Sahi Tareeqah:
print(obj1.b)  # Output: Samsung
print(obj1.c)  # Output: Red
```
---

## Create Multiple Objects:

```py
class Mobile:
    def __init__(self, brand_name, color):
        self.a = brand_name
        self.b = color

    def show_info(self):
        print(f"Mobile Brand: {self.a} | Color: {self.b}")
        
# Object 1
phone1 = Mobile("Samsung", "Black")

# Object 2
phone2 = Mobile("Apple", "White")

# Object 3
phone3 = Mobile("Redmi", "Blue")

phone1.show_info()
phone2.show_info() 
phone3.show_info()
```

```py
class Product:
    def __init__(self, title, price, stock):
        self.tit = title
        self.pri = price
        self.sto = stock

    def buy(self, quantity):

        if quantity <= self.sto:

            self.sto -= quantity
            total = quantity * self.pri
            print(f"{quantity}x {self.tit} Total Bill: Rs. {total}")
        
        else:
            print(f"Sorry! Out of Stock only {self.sto} Available")

# Objects
p1 = Product("Wireless Mouse", 1500, 10)
p2 = Product("Mechanical Keyboard", 4500, 2)

# Real-time Actions
p1.buy(2)
p2.buy(2)
```