# What is Array:

1. Array ek linear data structure hai jo ek hi datatype yeah different datatype ke multiple values ko contiguously (ek ke baad ek sequential memory location par) store karta hai, jahan har value ko uske Index number ke zariya identify aur access kiya jata hai or index 0 se start hota hai.

## **Main Purpose**

* **Memory Efficiency & Organization:** Alag alag variables banane ke bajaye (`student1`, `student2`, `student3`), hazaron elements ko ek single variable ke andar organize karke store karna.
* **Fast Data Retrieval:** Memory continuous hone ki waja se index number ke zariya kisi bhi element ko instant (O(1) time complexity mein) access karna.
* **Automation via Loops:** Multi-data items par ek sath operation perform karne ke liye (jaise sabhi values ko print karna, search karna, ya sort karna) loops ka use aasan banana.

---

# Array ka Major 3 types hai?

## 1. Indexed Array

### Definition

**Indexed Array** woh array hota hai jisme values ko **numeric indexes** ke through store aur access kiya jata hai. PHP mein indexing normally **0 se start** hoti hai.

### Purpose

Jab tumhare paas **same type ya related values ki simple list** ho aur har value ko naam dene ki zaroorat na ho, Indexed Array use karte hain.

### Example

```php
$fruits = ["Apple", "Banana", "Mango"];
```

Iska structure:

```text
Index     Value
  0       Apple
  1       Banana
  2       Mango
```

Value access karna:

```php
echo $fruits[0];
```

Output:

```text
Apple
```

### Real-life use

* Fruits ki list
* Students ke names
* Product names
* Numbers ki list
* Categories ki list

---

## 2. Associative Array

### Definition

**Associative Array** woh array hota hai jisme values ko **custom/named keys** ke saath store kiya jata hai, jaise `"name"`, `"age"`, `"email"`.

### Purpose

Jab data ki har value ka **specific meaning** ho, to Associative Array use karte hain. Isse code readable aur understandable hota hai.

### Example

```php
$student = [
    "name" => "Ali",
    "age" => 22,
    "city" => "Karachi"
];
```

Structure:

```text
Key       Value
name      Ali
age       22
city      Karachi
```

Value access:

```php
echo $student["name"];
```

Output:

```text
Ali
```

Age:

```php
echo $student["age"];
```

Output:

```text
22
```

### Real-life use

* Student ki information
* User profile
* Product details
* Login information
* Employee details

For example:

```php
$user = [
    "username" => "kaif",
    "email" => "kaif@example.com",
    "role" => "admin"
];
```

Yahan har value ka clear meaning hai.

---

## 3. Multidimensional Array

### Definition

**Multidimensional Array** woh array hota hai jiske andar **ek ya multiple arrays** hote hain.

Simple words mein:

> **Array ke andar array = Multidimensional Array**

### Purpose

Jab hume **multiple records** store karne hon aur har record ke andar multiple pieces of information hon, tab Multidimensional Array use hota hai.

### Example

```php
$students = [
    [
        "name" => "Ali",
        "age" => 22
    ],
    [
        "name" => "Ahmed",
        "age" => 20
    ],
    [
        "name" => "Usman",
        "age" => 21
    ]
];
```

Structure:

```text
students
   |
   |-- Student 0
   |     name → Ali
   |     age  → 22
   |
   |-- Student 1
   |     name → Ahmed
   |     age  → 20
   |
   |-- Student 2
         name → Usman
         age  → 21
```

Ali ka naam:

```php
echo $students[0]["name"];
```

Output:

```text
Ali
```

Ahmed ki age:

```php
echo $students[1]["age"];
```

Output:

```text
20
```

### Real-life use

* Multiple students ka data
* Multiple products
* Multiple users
* Quiz questions
* Database se aaye multiple records

For example, quiz system:

```php
$questions = [
    [
        "question" => "What is PHP?",
        "answer" => "Programming Language"
    ],
    [
        "question" => "What is HTML?",
        "answer" => "Markup Language"
    ]
];
```

Yahan **multiple questions** hain aur har question ke andar multiple values hain.

---

## Short Comparison

| Type                 | Keys              | Purpose                          | Example           |
| -------------------- | ----------------- | -------------------------------- | ----------------- |
| **Indexed**          | `0, 1, 2...`      | Simple list                      | Fruits            |
| **Associative**      | `"name"`, `"age"` | Single entity ka meaningful data | Student           |
| **Multidimensional** | Multiple arrays   | Multiple entities/records        | Multiple students |

