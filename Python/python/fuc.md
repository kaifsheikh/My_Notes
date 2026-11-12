# Examples of Custom Functions:

```py
name = "kaif shaikh"

name.upper()                 # KAIF SHAIKH
name.lower()                 # kaif shaikh
name.title()                 # Kaif Shaikh
name.capitalize()            # Kaif shaikh
name.strip()                 # Extra spaces remove
name.replace("kaif", "Ali")  # Ali shaikh
name.split()                 # ['kaif', 'shaikh']
name.find("shaikh")          # 5

# ---------------------------------------------------------

fruits = ["Apple", "Mango", "Banana"]

fruits.append("Orange")     # Item add
fruits.insert(1, "Grapes")  # Position par add
fruits.remove("Apple")      # Item delete
fruits.pop()                # Last item remove
fruits.sort()               # Alphabetical sort
fruits.reverse()            # Reverse list
fruits.count("Mango")       # Item count
fruits.index("Mango")       # Item position

# ---------------------------------------------------------

student = {"name": "Kaif", "age": 20}

student.keys()                # dict_keys(['name', 'age'])
student.values()              # dict_values(['Kaif', 20])
student.items()               # Key aur value dono
student.get("name")           # Kaif
student.update({"age": 21})   # Value update
student.pop("age")            # Key delete
student.copy()                # Dictionary copy
student.clear()               # Dictionary empty

```

# Example 2:

```py
name = "kaif shaikh"

# Case checking
name.isupper()             # False
name.islower()             # True
name.istitle()             # False
name.isspace()             # False
name.isalpha()             # False (space ki wajah se)
name.isalnum()             # False

# Searching
name.startswith("kaif")   # True
name.endswith("shaikh")   # True
name.count("a")           # 2
name.rfind("a")           # Last occurrence index
```

# Example 3:

```py
numbers = [10, 20, 30, 40, 50]

# Adding
numbers.extend([60, 70, 80])

# Copying
new_numbers = numbers.copy()

# Sorting
numbers.sort(reverse=True)
numbers.sort(key=None)

# Removing
numbers.pop()   # Last item removed
numbers.clear() # All items removed

# Searching
numbers.index(30)
numbers.count(20)
```

# Example 4:

```py
numbers = [10, 20, 30, 40, 50]

len(numbers)       # Total items
max(numbers)       # Largest value
min(numbers)       # Smallest value
sum(numbers)       # Total sum
sorted(numbers)    # New sorted list
reversed(numbers)  # Reverse iterator
any(numbers)       # Kya koi value True hai?
all(numbers)       # Kya sab values True hain?
```

# Example 5:

```py
numbers = [10, 20, 30, 40, 50, 60]

numbers[1:4]       # [20, 30, 40]
numbers[:3]        # [10, 20, 30]
numbers[2:]        # [30, 40, 50, 60]
numbers[-1]        # 60
numbers[-3:]       # [40, 50, 60]
numbers[::-1]      # Reverse list
numbers[::2]       # Every second item
```

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
