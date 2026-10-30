# 📖 PROPER DEFINITION

> "Destructor ek **special method** hai jo class ke andar hota hai aur **object destroy hote waqt automatic chal jata hai** — chahe object `unset()` se destroy ho, function ka scope khatam ho, ya script end ho jaye. Iska kaam hai **safai (cleanup)** karna — jaise file band karna, database connection band karna, ya memory free karna."

Destructor ka matlab hai: **"Kaam khatam hone par safai karna"** 🧹

# PURPOSE:

> **Resources ko free karna aur safai karna jab object ki zaroorat khatam ho jaye.**

### Detailed Purpose Points:

| #   | Purpose                             | Explanation                          |
| --- | ----------------------------------- | ------------------------------------ |
| 1   | **File close karna**                | Agar object ne file open ki thi      |
| 2   | **Database connection close karna** | Connection free karna                |
| 3   | **Memory free karna**               | Resources release karna              |
| 4   | **Logging**                         | Object destroy hone ka record rakhna |
| 5   | **Temporary data delete karna**     | Cleanup karna                        |
| 6   | **Network connection band karna**   | Socket close karna                   |
| 7   | **Cache clear karna**               | Temporary data hatana                |

---

# 💻 SYNTAX

```php
class ClassName {
    public function __destruct() {
        // cleanup code
    }
}
```

### 📌 Important Points:

- Naam **hamesha** `__destruct` hota hai (do underscore)
- **`public`** hota hai
- **Parameters nahi** le sakta (khali hota hai)
- **Return value nahi** hoti
- Object destroy hote hi **automatic** chalta hai

---

# 🔄 DESTRUCTOR KAB CHALTA HAI? (3 Situations)

| #   | Situation                     | Example                                        |
| --- | ----------------------------- | ---------------------------------------------- |
| 1   | **Object `unset()` ho jaye**  | `unset($obj);`                                 |
| 2   | **Object ka scope khatam ho** | Function ke andar object bana, function khatam |
| 3   | **Script end ho jaye**        | PHP script ka end                              |

---

# 📌 KEY POINTS (Ek Nazar Mein — 20 Points)

| #   | Key Point                    | Detail                                                                   |
| --- | ---------------------------- | ------------------------------------------------------------------------ |
| 1   | **Special method**           | Normal method nahi — magic method hai                                    |
| 2   | **Naam fix hai**             | Hamesha `__destruct` (do underscore)                                     |
| 3   | **Automatic chalta hai**     | Object destroy hote hi khud chalta hai                                   |
| 4   | **Manual call nahi karte**   | Aap call nahi karte, PHP karta hai                                       |
| 5   | **Ek class mein sirf 1**     | Ek hi destructor ho sakta hai                                            |
| 6   | **Return value nahi**        | Kuch return nahi karta (void)                                            |
| 7   | **Parameters nahi le sakta** | `__destruct()` khali hota hai                                            |
| 8   | **Public hota hai**          | Usually `public`                                                         |
| 9   | **Inheritance mein**         | Child class parent ka destructor call karti hai (`parent::__destruct()`) |
| 10  | **Default destructor**       | Agar na likhein, PHP khud ek khali destructor deta hai                   |
| 11  | **Purpose**                  | Resources free karna, cleanup                                            |
| 12  | **Kab chalta hai**           | Object destroy / script end                                              |
| 13  | **Order**                    | Script end par objects **reverse order** mein destroy hote hain          |
| 14  | **Exception nahi**           | Destructor mein exception throw karna **avoid** karein                   |
| 15  | **Call stack**               | Destructor ke andar naye objects bana sakte hain                         |
| 16  | **PHP 5+**                   | Modern PHP mein kaam karta hai                                           |
| 17  | **Manual call**              | `$obj->__destruct()` possible, **lekin** galat practice                  |
| 18  | **`exit()` par**             | `exit()` call karne par bhi destructor chalta hai                        |
| 19  | **Fatal error par**          | Fatal error par destructor **nahi** chalta (mostly)                      |
| 20  | **Constructor ka jodi**      | Constructor = start, Destructor = end                                    |

---

## Example 1: Basic Destructor

```php
<?php
class Test {
    public function __construct() {
        echo "✅ Object bana (constructor chala).<br>";
    }

    public function __destruct() {
        echo "🧹 Object destroy hua (destructor chala).<br>";
    }
}

$obj = new Test();       // Constructor chala
echo "Kaam ho raha hai...<br>";
unset($obj);              // Destructor chala (object destroy)
echo "Script khatam.<br>";
?>
```

---

## Example 2: Script End Par Automatic Destructor

```php
<?php
class Test {
    public function __construct() {
        echo "Object bana.<br>";
    }

    public function __destruct() {
        echo "Object destroy hua (script end).<br>";
    }
}

$obj1 = new Test();
$obj2 = new Test();

echo "Kaam chal raha hai...<br>";
// Script end — dono objects destroy honge
?>
```

> 📌 **Important:** Script end par **saare objects** automatic destroy ho gaye — destructor khud chala. Aapne kuch nahi kiya! ✅

---

## Example 3: Scope Khatam Hone Par Destructor

```php
<?php
class Test {
    public $name;

    public function __construct($name) {
        $this->name = $name;
        echo "✅ " . $name . " object bana.<br>";
    }

    public function __destruct() {
        echo "🧹 " . $this->name . " object destroy hua.<br>";
    }
}

function myFunction() {
    $obj = new Test("Function Wala");   // Constructor
    echo "Function ke andar kaam...<br>";
    // Function khatam → $obj ka scope khatam → destructor chala
}

myFunction();    // Function call

echo "Function ke bahar.<br>";
$obj2 = new Test("Bahar Wala");     // Constructor
echo "Script khatam.<br>";
// Script end → $obj2 destroy → destructor chala
?>
```

**Output:**

```
✅ Function Wala object bana.
Function ke andar kaam...
🧹 Function Wala object destroy hua.
Function ke bahar.
✅ Bahar Wala object bana.
Script khatam.
🧹 Bahar Wala object destroy hua.
```

> 📌 **Dekho:** `myFunction()` khatam hote hi `$obj` ka scope khatam → destructor chal gaya. `$obj2` script end par destroy hua. ✅

---

## Example 4: Real-Life — File Handling

```php
<?php
class FileHandler {
    private $file;
    private $filename;

    public function __construct($filename) {
        $this->filename = $filename;
        $this->file = fopen($filename, "w");    // file open
        echo "✅ File khuli: " . $filename . "<br>";
    }

    public function write($text) {
        fwrite($this->file, $text);
        echo "✍️ Likh diya: " . $text . "<br>";
    }

    public function __destruct() {
        fclose($this->file);                     // file close
        echo "🧹 File band ho gayi: " . $this->filename . "<br>";
    }
}

$fh = new FileHandler("data.txt");
$fh->write("Hello World");
$fh->write("PHP OOP");
unset($fh);    // destructor chala → file close

echo "Script khatam.<br>";
?>
```

**Output:**

```
✅ File khuli: data.txt
✍️ Likh diya: Hello World
✍️ Likh diya: PHP OOP
🧹 File band ho gayi: data.txt
Script khatam.
```

> 📌 **Yahi destructor ka asli faida:** File **automatically close** ho gayi jab object destroy hua. Agar destructor na hota, to file **open hi rehti** — memory leak ho sakta tha! 🔒

---

## Example 5: Real-Life — Database Connection

```php
<?php
class Database {
    private $connection;

    public function __construct() {
        // Connection khola (example ke liye simple)
        $this->connection = "DB Connected";
        echo "✅ " . $this->connection . "<br>";
    }

    public function query($sql) {
        echo "🔍 Query chal rahi: " . $sql . "<br>";
    }

    public function __destruct() {
        // Connection band karo
        $this->connection = null;
        echo "🧹 DB Connection band ho gaya.<br>";
    }
}

$db = new Database();
$db->query("SELECT * FROM users");
$db->query("INSERT INTO students VALUES (1, 'Ali')");
unset($db);    // destructor → connection close

echo "Script khatam.<br>";
?>
```

**Output:**

```
✅ DB Connected
🔍 Query chal rahi: SELECT * FROM users
🔍 Query chal rahi: INSERT INTO students VALUES (1, 'Ali')
🧹 DB Connection band ho gaya.
Script khatam.
```

> 📌 **Real projects mein** yahi hota hai — database connection ko **automatically close** karna taake server par load na pare. ✅

---

## Example 6: Constructor + Destructor Saath Mein

```php
<?php
class ShoppingCart {
    public $customerName;
    private $items = [];

    // CONSTRUCTOR — object bante hi chala
    public function __construct($customerName) {
        $this->customerName = $customerName;
        echo "🛒 Cart bana: " . $customerName . "<br>";
    }

    public function addItem($item) {
        $this->items[] = $item;
        echo "➕ " . $item . " add hua.<br>";
    }

    // DESTRUCTOR — object destroy hote hi chala
    public function __destruct() {
        echo "🧹 " . $this->customerName . " ka cart band ho gaya. (Items: "
             . count($this->items) . ")<br>";
    }
}

$cart1 = new ShoppingCart("Ali");
$cart1->addItem("Laptop");
$cart1->addItem("Mouse");

$cart2 = new ShoppingCart("Sara");
$cart2->addItem("Mobile");

echo "--- Kaam khatam ---<br>";
unset($cart1);    // Ali ka cart destroy → destructor chala
// Script end → Sara ka cart destroy → destructor chala
?>
```

**Output:**

```
🛒 Cart bana: Ali
➕ Laptop add hua.
➕ Mouse add hua.
🛒 Cart bana: Sara
➕ Mobile add hua.
--- Kaam khatam ---
🧹 Ali ka cart band ho gaya. (Items: 2)
🧹 Sara ka cart band ho gaya. (Items: 1)
```

> 📌 **Dekho:** Har object ka **apna destructor** chala. `$cart1` pehle destroy hua (unset), phir script end par `$cart2`. ✅

---

## Example 7: Order of Destruction (Reverse Order)

```php
<?php
class Test {
    public $name;

    public function __construct($name) {
        $this->name = $name;
        echo "✅ " . $name . " bana.<br>";
    }

    public function __destruct() {
        echo "🧹 " . $this->name . " destroy.<br>";
    }
}

$obj1 = new Test("First");
$obj2 = new Test("Second");
$obj3 = new Test("Third");

echo "--- Script end ---<br>";
// Script end par destructor REVERSE order mein chalega
?>
```

**Output:**

```
✅ First bana.
✅ Second bana.
✅ Third bana.
--- Script end ---
🧹 Third destroy.
🧹 Second destroy.
🧹 First destroy.
```

> 📌 **Important Rule:** Script end par objects **ultee tarteeb (reverse order)** mein destroy hote hain — jo **last bana**, woh **pehle** destroy hota hai (stack ki tarah: LIFO). ✅

---

# 📊 CONSTRUCTOR VS DESTRUCTOR — Complete Comparison

| Point              | **Constructor**                   | **Destructor**                 |
| ------------------ | --------------------------------- | ------------------------------ |
| **Naam**           | `__construct`                     | `__destruct`                   |
| **Kab chalta hai** | Object **banate waqt**            | Object **destroy** hote waqt   |
| **Kaam**           | Initialization (values set)       | Cleanup (safai)                |
| **Parameters**     | ✅ Le sakta hai                   | ❌ Nahi le sakta               |
| **Return value**   | ❌ Nahi                           | ❌ Nahi                        |
| **Kab use**        | Initial values, validation, setup | File close, DB close, cleanup  |
| **Real-life**      | Naya mobile — SIM daalna          | Ghar chhorte — lights off      |
| **Ek class mein**  | 1                                 | 1                              |
| **Call**           | Automatic (`new` par)             | Automatic (destroy/script end) |
| **Order**          | Jab object bane                   | Reverse order (LIFO)           |
| **Purpose**        | Object ko ready karna             | Resources free karna           |

---

# 🧠 DONO KA RELATION — Ek Line Mein

```
Constructor = "Start karo kaam"  ⚡
Destructor  = "Khatam karo safai"  🧹
```

**Lifecycle:**

```
Object bana  →  Constructor chala  →  Kaam hua  →  Object destroy  →  Destructor chala
```

---

# ⚠️ COMMON MISTAKES (Naye Logon Ki Galtiyan)

### ❌ Galti 1: Destructor Mein Parameters Dena

```php
class Test {
    public function __destruct($param) {   // ❌ ERROR!
        // Destructor parameters nahi leta
    }
}
```

### ❌ Galti 2: Destructor Se Return Karna

```php
class Test {
    public function __destruct() {
        return "Hello";   // ❌ Destructor return nahi karta
    }
}
```

### ❌ Galti 3: Destructor Mein Exception Throw Karna

```php
class Test {
    public function __destruct() {
        throw new Exception("Error!");   // ❌ Avoid karein!
        // Destructor mein exception = unpredictable behavior
    }
}
```

### ❌ Galti 4: Ek Se Zyada Destructor

```php
class Test {
    public function __destruct() {}
    public function __destruct() {}   // ❌ ERROR! Duplicate
}
```

### ❌ Galti 5: `$this` Ko Galat Use Karna

```php
class Test {
    public function __destruct() {
        echo $this->name;   // ⚠️ Object destroy ho raha hai — properties
        //                      access karna risky ho sakta hai
    }
}
```

---

# ✅ BEST PRACTICES (Inhe Follow Karein)

| #   | Best Practice                             | Kyun?                              |
| --- | ----------------------------------------- | ---------------------------------- |
| 1   | **Sirf cleanup karo**                     | Heavy kaam mat karo                |
| 2   | **Exception avoid karo**                  | Unpredictable behavior se bachao   |
| 3   | **File/DB close zaroor karo**             | Resources leak na hon              |
| 4   | **`parent::__destruct()` call karo**      | Inheritance mein parent ka cleanup |
| 5   | **Logging ke liye use karo**              | Debugging aasan                    |
| 6   | **Manual call mat karo**                  | PHP khud chalata hai               |
| 7   | **`$this` se properties access mat karo** | Object destroy ho raha hota hai    |

---

# 🧬 INHERITANCE MEIN DESTRUCTOR (Important!)

```php
class ParentClass {
    public function __destruct() {
        echo "Parent destructor chala.<br>";
    }
}

class ChildClass extends ParentClass {
    public function __destruct() {
        parent::__destruct();   // ⬅️ Parent ka destructor call kiya
        echo "Child destructor chala.<br>";
    }
}

$c = new ChildClass();
unset($c);
// Output:
// Parent destructor chala.
// Child destructor chala.
```

### 📌 Rule:

> **Agar child class apna destructor banaye, to parent ka destructor automatic nahi chalta — `parent::__destruct()` manually call karna parta hai.**

---

# 🎯 KAHAN USE HOTA HAI? (Real-Life Use Cases)

| Use Case                   | Example                 |
| -------------------------- | ----------------------- |
| **File close**             | `fclose($file)`         |
| **DB connection close**    | `$pdo = null`           |
| **Socket close**           | Network connection band |
| **Memory free**            | Large arrays delete     |
| **Logging**                | Object destroy record   |
| **Cache clear**            | Temporary data delete   |
| **Temporary files delete** | Upload ke baad          |

---

# 🎓 INTERVIEW QUESTIONS (Aksar Pooche Jaate Hain)

| #   | Question                                              | Short Answer                                          |
| --- | ----------------------------------------------------- | ----------------------------------------------------- |
| 1   | Destructor kya hai?                                   | Special method jo object destroy hote waqt chalta hai |
| 2   | Destructor ka naam kya hota hai?                      | `__destruct`                                          |
| 3   | Ek class mein kitne destructors?                      | Sirf 1                                                |
| 4   | Destructor return karta hai?                          | Nahi                                                  |
| 5   | Destructor parameters le sakta hai?                   | Nahi                                                  |
| 6   | Destructor kab chalta hai?                            | Object destroy / script end                           |
| 7   | Destructor ka purpose?                                | Resources free karna, cleanup                         |
| 8   | Inheritance mein parent destructor kaise call karein? | `parent::__destruct()`                                |
| 9   | Agar destructor na likhein to?                        | PHP default (khali) destructor deta hai               |
| 10  | Destructor mein exception throw karein?               | Nahi — avoid karein                                   |
| 11  | Script end par destructor ka order?                   | Reverse order (LIFO)                                  |
| 12  | `exit()` par destructor chalta hai?                   | Haan                                                  |

---

# 📌 EK LINE MEIN SUMMARY

> **Destructor** = **"Object destroy hote hi automatic chalne wala method jo resources free karta hai aur safai karta hai — file close, DB close, memory free."** 🧹

---

# 🔑 FINAL KEY POINTS (Yaad Rakhne Ke Liye)

```
1️⃣  Naam: __destruct (do underscore)
2️⃣  Automatic: object destroy / script end par chalta hai
3️⃣  Sirf 1: ek class mein
4️⃣  Return: nahi karta
5️⃣  Parameters: nahi le sakta
6️⃣  Purpose: cleanup + resources free
7️⃣  Inheritance: parent::__destruct() call karo
8️⃣  Default: na likhein to PHP khud deta hai
9️⃣  Manual call: nahi karte
🔟  Order: script end par reverse (LIFO)
1️⃣1️⃣  Exception: avoid karein
1️⃣2️⃣  Jodi: Constructor ke saath (start + end)
```

---

# 📊 QUICK REFERENCE TABLE

| Situation                   | Destructor Chalega?            |
| --------------------------- | ------------------------------ |
| `unset($obj)`               | ✅ Haan                        |
| Function scope khatam       | ✅ Haan                        |
| Script end                  | ✅ Haan                        |
| `exit()` call               | ✅ Haan                        |
| Fatal error                 | ❌ Nahi (mostly)               |
| Manual `$obj->__destruct()` | ✅ Haan (lekin galat practice) |

---

# 🎯 Constructor + Destructor — Complete Lifecycle

```php
<?php
class Lifecycle {
    public function __construct() {
        echo "1️⃣ CONSTRUCTOR chala — object bana<br>";
    }

    public function doWork() {
        echo "2️⃣ KAAM chala — method call hua<br>";
    }

    public function __destruct() {
        echo "3️⃣ DESTRUCTOR chala — object destroy<br>";
    }
}

$obj = new Lifecycle();   // 1️⃣
$obj->doWork();            // 2️⃣
unset($obj);               // 3️⃣
?>
```

**Output:**

```
1️⃣ CONSTRUCTOR chala — object bana
2️⃣ KAAM chala — method call hua
3️⃣ DESTRUCTOR chala — object destroy
```

> 📌 **Yahi poora lifecycle hai:** Constructor → Kaam → Destructor. ✅

---

## 📚 Aage Kya?

Destructor complete! Ab agla topic:

| Topic                       | Kya Sikhoge                            |
| --------------------------- | -------------------------------------- |
| **Inheritance** (`extends`) | OOP ka sabse important topic ⭐        |
| **`parent::` keyword**      | Parent class ko call karna             |
| **`protected`**             | Access modifier (private vs protected) |
| **Encapsulation**           | Data hiding ka poora concept           |

---

Agar aap chahein to main **destructor ke advanced points** bhi bata sakta hoon — jaise:

- 🔹 **Destructor + Singleton pattern**
- 🔹 **Destructor + Exception handling** (detail)
- 🔹 **Destructor vs `finally` block** (modern PHP)
- 🔹 **Destructor + Reference counting**

Ya phir **Inheritance** ka lesson shuru karein? Bata dein! 😊
