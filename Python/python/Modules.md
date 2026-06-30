# What is Module
1. Python mein har .py file ek Module hoti hai.
2. Import ka Maltab hai Ek file ya Module ka code dusri file me use karna

## 4 Types of Modules:
1. **Built-in Modules**
- `Ye modules Python ke installation ke saath hi aate hain`
  
2. **User-defined Modules**
- `yeah Modules Hum khud banate hain`

- `yeah wo modules hote hain jo hum apni python file .py mein create karte hai in files ko hum module ki tarah import karke use kar sakte hain`

## `Example 01:`
- `my_module.py mein jo bhe likha hoga wo hum main.py mein use kar sekhte hai`
```py
# my_module.py

def greet(name):
    return f"Hello {name}"
```
```py
# main.py
import my_module

print(my_module.greet("Ali"))
```

3. **Third-party Modules**
- `Ye Python me default nahi aate isa Hum pip se install karte hain`

- `Usually community ne banaye hote hain aur common tasks ke liye use hote hain`

- `Internet se download kar ke use karne wale ready-made modules`

## `Example 01:`

```py
# pip install requests

import requests

response = requests.get("https://www.google.com")
print(response.status_code)
```
## Different Examples:
- `isme sirf add() function se Import hoga multiply() wala nahe hoga`
```py
# math_functions.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```
```py
# main.py
from math_functions import add
result = add(5, 3)  
print(result)
```