## What is Function?

1.  function aik "band dabbi" ki tarah hota hai.
2.  Iske andar hum jo bhe variable or coding karte hai wo function ka bahir wale code se bilkul alag thalag hoti hai.
3.  Parameter Ye wo variable hai jinhe sirf function ka Brackets `()` mein define kiya jata hai taake bahir se ane wali `Values` ko store kare apne andar
4.  Function sirf wahi kaam karega jis ke liye usay banaya gaya hai (Single Responsibility).
5.      Code ko aik dafa likh kar poore program mein kahin bhi baar baar chalaya ja sakta hai.
6.  Function apna kaam mukammal karne ke baad jo jawab (output) wapas bhejta hai.
7.  Statements" ka matlab hai programming ki lines (instructions). "Block" ka matlab hai un lines ka ek group.

## Agar main function ke andar koi variable banau (e.g., x = 10), to kya main function ke bahar usay use kar sakta hoon?

1. Nahi! Isay kehte hain `Local Scope`. Function ke andar ki cheez sirf function ke andar ki hai.

## Agar function bahar ki dunya se bilkul alag hai, to phir hum bahar ka data usay dete kaise hain?

1. Yehi wo jagah hai jahan Parameters kaam aate hain. Parameters wo (Window) hain jis ke zariye bahar se data function ka andar ata hai.

## Agar Function ka andar ki coding bahar nazar nahi aati, to jo function se "Result" nikalta hai, wo humein kaise milta hai?

1. Iske liye `return` ka keyword use hota hai.
2. Ye function ke khatam hone par final result ko Function se bahir nikal dyta hai .

# Local Variables in Function:

1. Jo variable function ke andar create hai usay `local variable` kehte hain.
2. **Local** means sirf us function tak limited
3. `x` or `y` yeah Local Variables hai inha Function ka bahir access nahi kar sakta hai.

```py
def add():
    x = 10        # local variable
    y = 20        # local variable
    print(x + y)

add()
```

### `Local variable` function ke bahar access nahi hota.

```py
def add():
    x = 10        # local variable
    print(x)

add() # 10

print(x) # NameError: name 'x' is not defined
```

### `Local variable` ko return karna.

1. is terha `Local Variable` ko bahir Access kar sekhte hai

```py
def add():
    x = 5
    y = 3
    return x + y

result = add()
print(result)
```

# Global Variables in Function:

1. Jo variable function ke bahar banaya jaye, wo `global variable` hota hai.
2. `num` yeah Global Variable hai isa Funtion ka andar Access kar sekhte hai lakin sirf Read kar sekhte hai.

```py
num = 50   # global variable

def show():
    print(num)

show() # 50
```

### Global variable ko function ke andar Modify karna ho tu:

1. Agar hume `global variable` ko `modify` karna ho, function ka inside tu `global` keywoard use karna hota hai Function ka Inside.

```py
count = 5   # global variable

def increase():
    global count
    count = count + 1

increase()

print(count) # 6
```

# Same naam ka variable (local vs global):

1. Local variable global ko override nahi karta, sirf function ke andar use hota hai.

```py
x = 100       # global

def demo():
    x = 50    # local
    print(x)

demo()   # 50
print(x) # 100
```

# Function with Parameter:

1. Parameter wo variable hota hai jo function banate waqt brackets ke andar likhte hain.
2. **Purpose** Jab function ko call karega, to value `Parameter` ka pass ayge.

```py
def greet(name):
    print("Hello", name)

greet("Ali") # Ali
```

1. `Ali` -> Value ko `Argument` bhe bolte hai.
2. Function call karte waqt hum Argument pass karte hai jo Parameter ka pass jata hai.

```py
def make_juice(fruit):
    print(fruit, "juice ready")

make_juice("Apple") # Apple juice ready
make_juice("Mango") # Mango juice ready
```

### Default Parameter:

1. Agar argument na mile to default use hota hai.

```py
def greet(name="Guest"):
    print("Hello", name)

greet()        # Hello Guest
greet("Kaif")  # Hello Kaif
```

# Return Statement:

# What is `*args`?

1. \*args ek special syntax hai jo aapko function mein jitne chahe utne arguments pass karne ki freedom deta hai.
2. Iska matlab hai - aap function banaate time nahi jante ki kitne arguments aayenge, toh \*args use karke aap flexible function bana sakte hain.

## Breakdown:

1. `*` → Ye batata hai ke "yeh special hai, multiple values lega"

2. `args` → yeh arguments ka short form hai (aap koi bhi naam de sakte hain, par convention hai args)

## Example:

```py
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2))
print(add_all(1, 2, 3, 4))

# Using with Conditions:

## Example 2: Name Validation

```py
name = input("Enter your name: ")

if name.strip() == "":
    print("Name cannot be empty")
elif len(name) < 3:
    print("Name is too short")
else:
    print("Your name is:", name.title())
```

## Example 3: Search System

```py
message = "Welcome to Python Programming"

search = input("What do you want to find? ")

if message.find(search) != -1:
    print("Word found!")
else:
    print("Word not found!")
```

`find()` agar word nahi milta to `-1` return karta hai.

# 2. List Functions + If Else

```py
cart = ["Mobile", "Laptop", "Mouse"]

product = input("Enter product name: ").title()

if product in cart:
    print("Product already exists in cart")

else:
    cart.append(product)
    print("Product added successfully")

print("Your Cart:", cart)
```

Yahan `append()` new product add karta hai.

## Example 2: Product Remove System

```py
cart = ["Mobile", "Laptop", "Mouse"]

product = input("Which product do you want to remove? ").title()

if product in cart:
    cart.remove(product)
    print("Product removed successfully")

else:
    print("Product not found!")

print(cart)
```

## Example 3: Stock Management

```py
products = ["Mobile", "Laptop", "Mouse", "Keyboard"]

if len(products) > 0:
    print("Products available")

else:
    print("Out of stock!")
```

## Example 4: Product Sorting

```py
products = ["Laptop", "Mobile", "Apple", "Keyboard"]

products.sort()

if products[0] == "Apple":
    print("Apple is first in alphabetical order")

print(products)
```

# 3. Dictionary Functions + If Else

Dictionary real-world projects mein bohot important hai, especially:

- Login systems
- User profiles
- Admin panels
- Student management
- Product information
- API data

## Example 1: Login Authentication

```py
users = {
    "kaif": "12345",
    "ali": "abc123",
    "ahmed": "786786"
}

username = input("Enter username: ").lower()
password = input("Enter password: ")

if username in users:

    if users.get(username) == password:
        print("Login successful!")

    else:
        print("Incorrect password!")

else:
    print("User does not exist!")
```

## Example 2: Student Management System

```py
student = {
    "name": "Kaif",
    "age": 20,
    "marks": 85
}

if student.get("marks", 0) >= 50:

    print("Student Passed")

else:

    print("Student Failed")

print(student)
```

## Example 3: User Profile Update

```py
student = {
    "name": "Kaif",
    "age": 20
}

if "age" in student:

    student.update({"age": 21})
    print("Age updated successfully")

else:

    print("Age not found")

print(student)
```

## Example 4: Admin Panel

```py
user = {
    "name": "Kaif",
    "role": "admin",
    "status": "active"
}

if user.get("role") == "admin" and user.get("status") == "active":

    print("Access granted")

else:

    print("Access denied")
```

# 4. Combined Real-World Project

```py
students = [
    {"name": "Kaif Shaikh", "marks": 85},
    {"name": "Ali Ahmed", "marks": 40},
    {"name": "Ahmed Khan", "marks": 65}
]

name = input("Enter student name: ").strip().title()

found = False

for student in students:

    if student.get("name") == name:

        found = True

        print("Student Found!")

        print("Name:", student.get("name"))
        print("Marks:", student.get("marks"))

        if student.get("marks") >= 50:
            print("Result: Pass")

        else:
            print("Result: Fail")

        break

if not found:
    print("Student does not exist!")
```
