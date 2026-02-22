# 🔹 Compiler vs Interpreter vs Command Line Scripting

* jitne bhe programming languages hoti hai jo human se create kare hoti hai wo sirf machine ko instructions deti hai kue ka humera Computer sirf Binary language samajta hai isme sirf 0 or 1 hota hai

* is liya humein translator ki need parti hai jo programming languages ko convert karti hai machine language mein or wo translation ka kam in teno ka hai 

* jitne bhe Languages hoti hai kaise python , php , or Java etc inhe hum HLL (High Level Language) bolte hai kue ka yeah Human Readable hoti hai 

* 1️⃣ Compiler
* 2️⃣ Interpreter
* 3️⃣ Command Line Scripting (CLI Scripting)

* Har programming language ka apna compiler ya interpreter hota hai
kyon ke har language ki grammar, rules, aur syntax alag hoti hai.

1. **Compiler**

   * Compiler pura code ek sath read karta hai.
   * Usko machine language mein convert karta hai.
   * Ek alag **executable file** banata hai jo baad mein run hoti hai.
   * Example: C, C++

2. **Interpreter**

   * Interpreter code ko **line by line** read karta hai.
   * Har line ka output turant deta hai.
   * Example: Python, JavaScript

3. **Command Line Scripting**

   * Command Line Scripting ka matlab hai ke aap code bina browser/server ke, direct **terminal ya cmd** se run kar sako.
   * Example: PHP script ko `php file.php` ke zariye chalana.

| Language   | Compiler / Interpreter | Naam             |
| ---------- | ---------------------- | ---------------- |
| C          | Compiler               | GCC, Clang       |
| C++        | Compiler               | G++, MSVC        |
| Python     | Interpreter            | CPython          |
| Java       | Compiler + VM          | javac + JVM      |
| JavaScript | Interpreter            | V8, SpiderMonkey |
| PHP        | Interpreter            | Zend Engine      |

---

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

---

## 🔹 Dependencies vs DevDependencies

1. **Dependencies**

   * Ye woh packages hote hain jo project ko **chalane ke liye zaroori** hote hain.
   * Example:

     * `express` (server ke liye)
     * `mongoose` (database ke liye)
     * `axios` (API calls ke liye)

2. **DevDependencies**

   * Ye sirf **development ke time** use hote hain, production (live server) pe zaroori nahi hote.
   * Ye mainly developer ki madad karte hain.
   * Example:

     * Testing tools (jest, mocha)
     * Code linting (eslint)
     * Auto-reload tools (nodemon)

---