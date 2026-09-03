# Python OOP - Class aur Object Ka Complete Concept (Easy Roman Urdu)

---

# OOP Kya Hai? (Object Oriented Programming)

OOP ek programming style hai jisme hum **code ko real world ki tarah organize karte hain**.

Simple idea:

```
Real World → Code
Car → Object
Student → Object
Phone → Object
```

Har cheez ka **blueprint** hota hai aur us blueprint se **objects** bante hain.

---

# Class Kya Hai?

Class ek **blueprint ya template** hai.

Jaise ghar banane se pehle **naksha (map)** banta hai, waise hi object banane se pehle **class** banti hai.

Class mein hum define karte hain:

* **Data** (kya kya information hogi)
* **Functions** (kya kya kaam hoga)

Example:

```python
class Student:
    pass
```

Yeh ek simple class hai abhi kuch nahi hai isme.

---

# Object Kya Hai?

Object class ka **practical version** hai.

Jaise class = naksha, to object = **asli ghar**

Class se object banane ka tarika:

```python
class Student:
    pass

# Object banana
student1 = Student()
student2 = Student()
```

Ab `student1` aur `student2` dono **Student class ke objects** hain.

---

# Class Mein Data Kaise Dalein (Attributes)

Class ke andar **variables** bana sakte hain jo data store karein.

Inko bolte hain **attributes** ya **properties**.

Example:

```python
class Student:
    name = "Ali"
    age = 20
    grade = "A"
```

Ab jab object banayenge to yeh data uske paas hoga:

```python
student1 = Student()

print(student1.name)  # Output: Ali
print(student1.age)   # Output: 20
print(student1.grade) # Output: A
```

---

# Object Mein Data Kaise Badlein

Ek object ka data change kar sakte hain:

```python
student1 = Student()
student1.name = "Ahmed"
print(student1.name)  # Output: Ahmed
```

Ab `student1` ka naam `Ali` se `Ahmed` ho gaya.

Important baat:

* `student2` ka naam abhi bhi `Ali` hai
* Har object ka **alag data** hota hai

---

# __init__ Method (Constructor)

Jab object banta hai to automatically ek function chalta hai.

Usko bolte hain **constructor** ya **__init__ method**.

Yeh method object initialize karta hai.

Example:

```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
```

Yahan:

* `__init__` = constructor function
* `self` = current object (jo object ban raha hai uska reference)
* `name, age, grade` = parameters jo hum denge

Ab object aise banayenge:

```python
student1 = Student("Ali", 20, "A")
student2 = Student("Ahmed", 22, "B")

print(student1.name)  # Output: Ali
print(student2.name)  # Output: Ahmed
```

---

# Self Kya Hai?

`self` ka matlab hai **current object**.

Jab hum `student1 = Student("Ali", 20, "A")` likhte hain to:

* `self` automatically `student1` ban jata hai
* `self.name = "Ali"` matlab `student1.name = "Ali"`

Jab `student2` banega to `self` woh `student2` ban jayega.

Simple rule:

```
self = jo object abhi use ho raha hai
```

---

# Methods (Class Mein Functions)

Class ke andar functions banate hain.

Inko bolte hain **methods**.

Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, mera naam {self.name} hai aur meri age {self.age} hai")
    
    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False
```

Ab object banakar methods call karein:

```python
student1 = Student("Ali", 20)

student1.greet()
# Output: Hello, mera naam Ali hai aur meri age 20 hai

print(student1.is_adult())
# Output: True
```

---

# Class Variable vs Instance Variable

**Instance Variable** = Har object ka alag data hota hai

**Class Variable** = Sab objects ka common data hota hai

Example:

```python
class Student:
    school = "ABC School"  # Class variable (sabke liye same)
    
    def __init__(self, name):
        self.name = name  # Instance variable (har alag hai)
```

```python
student1 = Student("Ali")
student2 = Student("Ahmed")

print(student1.school)  # Output: ABC School
print(student2.school)  # Output: ABC School
print(student1.name)    # Output: Ali
print(student2.name)    # Output: Ahmed
```

---

# Inheritance (Virasat)

Ek class doosri class se **data aur methods le sakti hai**.

Isko bolte hain **inheritance**.

Example:

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} bol raha hai")

class Dog(Animal):  # Dog, Animal se inherit kar raha hai
    def bark(self):
        print("Bhau Bhau!")
```

```python
dog1 = Dog("Tommy")

dog1.speak()   # Output: Tommy bol raha hai
dog1.bark()    # Output: Bhau Bhau!
```

Yahan `Dog` ko `Animal` ka `name` aur `speak()` method **free mein mil gaya**.

---

# Encapsulation (Data Chupana)

Hum data ko **bahar se access hone se rok sakte hain**.

Isko bolte hain **encapsulation**.

Private variables banane ke liye **double underscore** lagate hain:

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit ho gaya! Naya balance: {self.__balance}")
```

```python
account = BankAccount(1000)

print(account.get_balance())  # Output: 1000
account.deposit(500)          # Output: Deposit ho gaya! Naya balance: 1500

# account.__balance  # Error! Direct access nahi ho sakta
```

---

# Polymorphism (Ek Hi Naam, Alag Kaam)

Ek hi function **alag alag objects par alag kaam karta hai**.

Example:

```python
class Cat:
    def speak(self):
        print("Meow Meow!")

class Dog:
    def speak(self):
        print("Bhau Bhau!")
```

```python
animals = [Cat(), Dog()]

for animal in animals:
    animal.speak()
```

Output:

```
Meow Meow!
Bhau Bhau!
```

Dekha? `speak()` function dono mein hai lekin **alag alag kaam kar raha hai**.

---

# Practical Example - Purana Example

Ek complete example jo sab kuch cover kare:

```python
class Car:
    # Class variable
    wheels = 4
    
    def __init__(self, brand, model, year):
        # Instance variables
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    
    def start(self):
        print(f"{self.brand} {self.model} start ho raha hai!")
    
    def accelerate(self, increase):
        self.speed += increase
        print(f"Speed ab {self.speed} km/h hai")
    
    def brake(self, decrease):
        self.speed -= decrease
        if self.speed < 0:
            self.speed = 0
        print(f"Speed ab {self.speed} km/h hai")
    
    def info(self):
        print(f"{self.year} {self.brand} {self.model}")
```

```python
# Objects banana
car1 = Car("Toyota", "Corolla", 2023)
car2 = Car("Honda", "Civic", 2024)

# Methods use karna
car1.start()
car1.accelerate(60)
car1.accelerate(20)
car1.brake(30)
car1.info()

print()

car2.start()
car2.accelerate(80)
car2.info()
```

Output:

```
Toyota Corolla start ho raha hai!
Speed ab 60 km/h hai
Speed ab 80 km/h hai
Speed ab 50 km/h hai
2023 Toyota Corolla

Honda Civic start ho raha hai!
Speed ab 80 km/h hai
2024 Honda Civic
```

---

# Summary (Short Version)

| Concept | Kya Hai | Example |
|---------|---------|---------|
| Class | Blueprint/Template | `class Student:` |
| Object | Class ka practical version | `student1 = Student()` |
| __init__ | Constructor (object setup) | `def __init__(self, name):` |
| self | Current object ka reference | `self.name = name` |
| Method | Class ka function | `def greet(self):` |
| Inheritance | Class se class banana | `class Dog(Animal):` |
| Encapsulation | Data ko private karna | `self.__balance` |
| Polymorphism | Same function, alag kaam | `animal.speak()` |

---

# Real Life Analogy

```
Class = Car ka naksha (blueprint)
Object = Asli Car jo road par chal rahi hai
__init__ = Car ka setup (color, model, etc.)
Method = Car ke kaam (start, brake, accelerate)
Inheritance = ElectricCar, Car ki tarah hai lekin extra features hain
Encapsulation = Engine andar hai, bahar se directly access nahi ho sakta
Polymorphism = Sab gaadiyan chal sakti hain lekin alag alag tareeqe se
```

---
