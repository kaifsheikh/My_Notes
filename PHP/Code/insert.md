## MySQL — Create Database & Table

```sql
-- DATABASE CREATE QUERY

CREATE DATABASE school_db;


-- DATABASE CHECK QUERY

USE school_db;


-- TABLE CREATE QUERY

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    age INT NOT NULL,
    course VARCHAR(100) NOT NULL
);
```

---

## `index.php`

```html

    <h2>Add Student</h2>

    <form action="insert.php" method="POST">

        <label>Name:</label>
        <input type="text" name="name" required>

        <br><br>

        <label>Email:</label>
        <input type="email" name="email" required>

        <br><br>

        <label>Age:</label>
        <input type="number" name="age" required>

        <br><br>

        <label>Course:</label>
        <input type="text" name="course" required>

        <br><br>

        <button type="submit">Insert Student</button>

    </form>
```

---

## `database.php`

```php
<?php

$conn = mysqli_connect(
    "localhost",
    "root",
    "",
    "school_db"
);

// Connection check
if (!$conn) {

    die("Connection failed: " . mysqli_connect_error());
}

?>
```

---

## `insert.php`

```php
<?php

// Database connection
$conn = mysqli_connect(
    "localhost",
    "root",
    "",
    "school_db"
);


// Connection check
if (!$conn) {

    die("Connection failed: " . mysqli_connect_error());

}

// Check request method
if ($_SERVER["REQUEST_METHOD"] == "POST") {


    // Form se data lena

    $name = $_POST["name"];
    $email = $_POST["email"];
    $age = $_POST["age"];
    $course = $_POST["course"];


    // INSERT query

    $sql = "INSERT INTO students (name, email, age, course)
            VALUES ('$name', '$email', '$age', '$course')";


    // Query execute

    if (mysqli_query($conn, $sql)) {

        echo "Student inserted successfully!";

    } else {

        echo "Error: " . mysqli_error($conn);

    }

}


// Connection close

mysqli_close($conn);

?>
```

---

# Flow

```text
index.php
    ↓
<form action="insert.php" method="POST">
    ↓
User form fill karta hai
    ↓
Submit
    ↓
insert.php
    ↓
$_SERVER["REQUEST_METHOD"] == "POST"
    ↓
$_POST se data
    ↓
INSERT query
    ↓
mysqli_query()
    ↓
MySQL Database
```

### Important

`action="insert.php"` ka matlab hai ke form submit hone par request **`insert.php`** ko jayegi.

```php
if ($_SERVER["REQUEST_METHOD"] == "POST")
```

Iska matlab hai ke **INSERT wala code sirf tab execute hoga jab form `POST` request ke through submit hoga.**

### File Structure

```text
student-project/
│
├── index.php
├── database.php
└── insert.php
```
