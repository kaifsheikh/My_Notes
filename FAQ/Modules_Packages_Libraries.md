# 🔹 Module
1. `Module` aik single file hoti hai jisme related code jaise (functions, classes, variables) hote hai, taake usay bar bar reuse kiya ja sake yeah specific kaam ke liye use hota hai.

```bash
# math.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# main.py
import math_utils
```

# 🔹 Package 
1. `Package` aik folder hota hai jisme multiple `modules` hote hain, taake related code ko organize kiya ja sake jisa import karna easy ho jata hai.

```bash
myapp/
 ├── utils.py
 ├── helpers.py
 └── validators.py

# from myapp import utils
```

# 🔹 Library
1. Library multiple `packages` aur `modules` ka complete collection hoti hai jo mil kar aik full functionality provide karti hai jo kisi specific kaam ko asaan banati hai yeah collection hota hai Packages + Modules ka.

---

# 🔹 What is Package Manager in Programming?

* `Package Manager` ek tool hota hai jo aapke liye ready-made code jaise `libraries` , `Packages`or `Modules` ko download, install, update aur remove karne ka liya use hota hai her Language ka apna alag Package Manager ho sekhta hai.

| Language  | Package Manager | Example Command                      |
| -------------------- | --------------- | ------------------------------------ |
| Python               | pip             | `pip install requests`               |
| Python (virtual env) | pipenv          | `pipenv install django`              |
| JavaScript           | npm             | `npm install express`                |
| JavaScript           | yarn            | `yarn add react`                     |
| PHP                  | composer        | `composer require laravel/framework` |
| Java                 | Maven           | `mvn install`                        |
| Linux                | apt / yum       | `sudo apt install python3`           |
