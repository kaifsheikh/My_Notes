# Constructor (`__construct`)

## 📖 Proper Definition

> "Constructor ek **special method** hai jo class ke andar hota hai aur **object banate hi automatic chal jata hai**. Iska kaam hai object ki properties ko **(initial values)** dena. Aap ise call nahi karte — PHP khud call karta hai jab aap `new` se object banate hain."

- **Naya mobile** kharidte hi **SIM daalna** → constructor
- **Naya ghar** lete hi **bijli connection** lena → constructor
- **Nayi car** lete hi **petrol daalna** → constructor

Object bante hi jo **zaroori kaam** ho, woh constructor karta hai! 😊

### Detailed Purpose Points:

| #   | Purpose                      | Explanation                                           |
| --- | ---------------------------- | ----------------------------------------------------- |
| 1   | **Initial values set karna** | Object bante hi properties ko value do                |
| 2   | **Validation lagana**        | Galat values rokna (jaise negative age)               |
| 3   | **Zaroori setup karna**      | Database connection, file open, etc.                  |
| 4   | **Code short karna**         | Har object ke liye alag se values set na karni parein |
| 5   | **Consistency**              | Har object ek hi tareeqe se bane                      |

## 💻 Syntax

```php
class ClassName {
    public function __construct($param1, $param2) {
        // initialization code
    }
}
```

### 📌 Important Points:

- Naam **hamesha** `__construct` hota hai (do underscore)
- **`public`** hota hai (mostly)
- **Return value nahi** hoti (void)
- Object banate hi **automatic** chalta hai

---

## Example 1:

### wihtout - Constructor:

```php
<?php
class Student {
    public $name;
    public $age;
}

$s1 = new Student();
$s1->name = "Ali";      // har baar set karna parega
$s1->age  = 20;

$s2 = new Student();
$s2->name = "Sara";     // phir se
$s2->age  = 22;

$s3 = new Student();
$s3->name = "Ahmed";    // phir se
$s3->age  = 25;
?>
```

> **Problem:** Har object ke liye alag se properties set karni parein. **Code lamba aur repeat** ho raha hai.

### Exmaple with Constructor:

```php
<?php
class Student {
    public $name;
    public $age;

    // CONSTRUCTOR — object bante hi chalega
    public function __construct($name, $age) {
        $this->name = $name;
        $this->age  = $age;
    }
}

// Object banao — values seedha constructor mein do
$s1 = new Student("Ali", 20);
$s2 = new Student("Sara", 22);
$s3 = new Student("Ahmed", 25);

echo $s1->name . " — " . $s1->age . "<br>";   // Ali — 20
echo $s2->name . " — " . $s2->age . "<br>";   // Sara — 22
echo $s3->name . " — " . $s3->age . "<br>";   // Ahmed — 25
?>
```

> Ab **ek line** mein object bana aur values bhi set ho gayi. `new Student("Ali", 20)` likhte hi `__construct` khud chal gaya. **Code short, clean, aur repeat nahi!** ✅

## Example Constructor:

```php
<?php
class Student {
    public $name;
    public $age;

    public function __construct($name, $age) {
        $this->name = $name;

        // Validation — galat age rok do
        if ($age >= 5 && $age <= 100) {
            $this->age = $age;
        } else {
            echo "Age must bhe uder 100 <br>";
            $this->age = 0;
        }
    }

    public function showInfo() {
        echo "Naam: " . $this->name . " | Age: " . $this->age . "<br>";
    }
}

$s1 = new Student("Ali", 20);     // ✅ Sahi
$s1->showInfo();                   // Naam: Ali | Age: 20

$s2 = new Student("Sara", -5);    // ❌ Galat age!
$s2->showInfo();                   // Naam: Sara | Age: 0
?>
```

# Key Points:

| #   | Key Point                         | Detail                                                                      |
| --- | --------------------------------- | --------------------------------------------------------------------------- |
| 1   | **Special method**                | Normal method nahi — magic method hai                                       |
| 2   | **Naam fix hai**                  | Hamesha `__construct` (do underscore)                                       |
| 3   | **Automatic chalta hai**          | `new` se object bante hi khud chalta hai                                    |
| 4   | **Manual call nahi karte**        | Aap call nahi karte, PHP karta hai                                          |
| 5   | **Ek class mein sirf 1**          | Ek hi constructor ho sakta hai                                              |
| 6   | **Return value nahi**             | Kuch return nahi karta (void)                                               |
| 7   | **Parameters le sakta hai**       | Values pass kar sakte hain                                                  |
| 8   | **Public hota hai**               | Usually `public` (private/protected bhi ho sakta hai — advanced)            |
| 9   | **Inheritance mein**              | Child class parent ka constructor call karti hai (`parent::__construct()`)  |
| 10  | **Default constructor**           | Agar aap na likhein, PHP khud ek khali constructor deta hai                 |
| 11  | **Purpose**                       | Properties ko initial values dena                                           |
| 12  | **Validation**                    | Galat values rok sakta hai                                                  |
| 13  | **Setup ka kaam**                 | File open, DB connect, etc.                                                 |
| 14  | **Overloading nahi**              | PHP mein constructor overloading nahi hoti (ek hi allowed)                  |
| 15  | **Default parameters**            | `$color = "White"` de sakte hain                                            |
| 16  | **Promoted properties (PHP 8+)**  | `public function __construct(public $name)` — short syntax                  |
| 17  | **Old PHP (4) mein**              | Constructor ka naam **class ke naam** jaisa hota tha (ab deprecated)        |
| 18  | **Calling order**                 | Parent constructor pehle, phir child (agar `parent::__construct()` call ho) |
| 19  | **Exception throw kar sakta hai** | Galat input par exception throw kar sakte hain                              |
| 20  | **Destructor ka jodi**            | Constructor = start, Destructor = end                                       |
