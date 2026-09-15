# MYSQL CODE:
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# HTML FORM:

```html
<form action="register.php" method="POST">

    <input type="text" name="name" placeholder="Name" required>
    <input type="email" name="email" placeholder="Email" required>
    <input type="password" name="password" placeholder="Password" required>

    <button type="submit" name="register">Register</button>

</form>
```

---

# PHP CODE:

```php
<?php

include "conn.php";

if ($_SERVER['REQUEST_METHOD'] == "POST") {

    $name = $_POST['name'] ?? '';
    $email = $_POST['email'] ?? '';
    $password = $_POST['password'] ?? '';


    // Name validation
    if (empty($name)) {
        echo "Name is required";
        exit;
    }


    // Email validation
    if (empty($email)) {
        echo "Email is required";
        exit;
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "Please enter a valid email";
        exit;
    }


    // Password empty check
    if (empty($password)) {
        echo "Password is required";
        exit;
    }


    // Minimum 8 characters
    if (strlen($password) < 8) {
        echo "Password must be at least 8 characters";
        exit;
    }


    // Password hash
    $password = password_hash($password, PASSWORD_DEFAULT);


    // Insert data
    $query = "INSERT INTO users (name, email, password)
              VALUES ('$name', '$email', '$password')";

    $result = mysqli_query($conn, $query);


    if ($result) {
        echo "Registration successful";
    } else {
        echo "Registration failed";
    }
}

?>
```
