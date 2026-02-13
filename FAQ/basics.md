# 🔹 Compiler vs Interpreter vs Command Line Scripting

* jitne bhe programming languages hoti hai jo human se create kare hoti hai wo sirf machine ko instructions deti hai kue ka humera Computer sirf Binary language samajta hai isme sirf 0 or 1 hota hai

* is liya humein translator ki need parti hai jo programming languages ko convert karti hai machine language mein or wo translation ka kam in teno ka hai 

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

# 🔹 URL (Uniform Resource Locator)

**Format:**

```
protocol://domain/path?query#fragment
```

### Example:

```
https://www.youtube.com/contact?name=Ali&age=25
```

### URL Parts:

1. **Protocol** → `https://`

   * Batata hai kaise connect karna hai (http, https, ftp).

2. **Domain** → `www.youtube.com`

   * Asaan naam jo insaan yaad rakhte hain.
   * Asli address hota hai IP (jaise `142.250.64.78`).
   * Conversion ka kaam **DNS (Domain Name System)** karta hai.

3. **Path** → `/contact`

   * Website ke andar ka page ya resource dikhata hai.

   | Path              | Meaning             |
   | ----------------- | ------------------- |
   | `/`               | Homepage            |
   | `/contact`        | Contact page        |
   | `/contact/mobile` | Mobile contact page |

4. **Query Parameters** → `?name=Ali&age=25`

   * Extra info bhejne ke liye hota hai.
   * `?` ke baad start hota hai.
   * `&` se multiple parameters separate hote hain.

   Example:

   ```
   http://localhost:3000/?name=Ali&age=25
   ```

5. **Fragment** → `#section1`

   * Page ke specific part tak scroll kar deta hai.

---

# 🔹 Semantic Versioning (SemVer)

jab bhe hum kisi language ko use karte hai programming mein yeah koi packages ho yeah koi application ho oisme oinke `Versions` hote hai old bhe latest bhe tu oisme jo numbers hote hai oiska kch matlab hota hai.

**Format:**

```
MAJOR.MINOR.PATCH
```

Example:

```
"express": "^4.18.2"
```

1. **MAJOR (4)**

   * Badi update.
   * Purana code kaam na kare.

2. **MINOR (18)**

   * Naye features add hue.
   * Purana code abhi bhi chalega.

3. **PATCH (2)**

   * Chhoti bug fixes aur improvements.

---
