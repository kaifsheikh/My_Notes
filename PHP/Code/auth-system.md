### Databse:

```sql
CREATE DATABASE auth_system;

USE auth_system;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### conn.php:

```php
<?php

$conn = mysqli_connect(
    "localhost",
    "root",
    "",
    "auth_system"
);

if (!$conn) {
    die("Database connection failed");
}

?>
```

### register.php:

```php
<?php
include "conn.php";

if (isset($_POST['register'])) {

    $name = $_POST['name'];
    $email = $_POST['email'];
    $password = password_hash(
        $_POST['password'],
        PASSWORD_DEFAULT
    );

    $check = mysqli_query(
        $conn, "SELECT * FROM users WHERE email='$email'"
    );

    if (mysqli_num_rows($check) > 0) {

        echo "Email already exists";

    } else {

        $sql = "INSERT INTO users (name, email, password)
                VALUES ('$name', '$email', '$password')";

        if (mysqli_query($conn, $sql)) {
            header("Location: login.php");
            exit;
        } else {
            echo "Registration failed";
        }
    }
}
?>

<h2>Register</h2>

<form method="POST">
    <input type="text" name="name"
           placeholder="Name" required>
    <br><br>

    <input type="email" name="email"
           placeholder="Email" required>
    <br><br>

    <input type="password" name="password"
           placeholder="Password" required>
    <br><br>

    <button type="submit" name="register">
        Register
    </button>
</form>

<a href="login.php">Login</a>
```

### login.php:

```php
<?php
session_start();
include "conn.php";

if (isset($_POST['login'])) {

    $email = $_POST['email'];
    $password = $_POST['password'];

    $sql = "SELECT * FROM users WHERE email='$email'";
    $result = mysqli_query($conn, $sql);

    if (mysqli_num_rows($result) > 0) {

        $user = mysqli_fetch_assoc($result);

        if (password_verify($password, $user['password'])) {

            session_regenerate_id(true);

            $_SESSION['user_id'] = $user['id'];
            $_SESSION['name'] = $user['name'];

            header("Location: dashboard.php");
            exit;

        } else {
            echo "Wrong password";
        }

    } else {
        echo "User not found";
    }
}
?>

<h2>Login</h2>

<form method="POST">
    <input type="email" name="email"
           placeholder="Email" required>
    <br><br>

    <input type="password" name="password"
           placeholder="Password" required>
    <br><br>

    <button type="submit" name="login">
        Login
    </button>
</form>

<a href="register.php">Register</a>
```

### dashboard.php:

```php 
<?php
session_start();

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit;
}
?>

<h1>
    Welcome, <?php echo htmlspecialchars($_SESSION['name']); ?>
</h1>

<p>You are logged in successfully.</p>

<a href="logout.php">Logout</a>
```

### index.php:

```php 
<?php

header("Location: login.php");
exit;

?>
```

### logout.php:

```php 
<?php
session_start();

session_unset();
session_destroy();

header("Location: login.php");
exit;
?>
```