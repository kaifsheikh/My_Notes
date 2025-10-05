# 🖥️ Compiler, URL aur Semantic Versioning Cheat Sheet

Yeh document basic programming aur web concepts ko simple **Roman Urdu** mein explain karta hai.

---

## 🔹 Compiler vs Interpreter vs Command Line Scripting

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

---

## 🔹 URL (Uniform Resource Locator)

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

## 🔹 Semantic Versioning (SemVer)

Jab hum package install karte hain (jaise `express`), to uska version `package.json` mein likha hota hai.

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
