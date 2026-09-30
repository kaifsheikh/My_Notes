### Databse:

```sql
CREATE DATABASE auth_system;

USE auth_system;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### includes/header.php:

```php
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="public/css/style.css" />
</head>
<body>

<?php session_start(); ?>

<nav>

    <?php if (isset($_SESSION['role']) && $_SESSION['role'] == 'admin'): ?>
        <a href="admin_dashboard.php">Admin Dashboard</a>

    <?php elseif (isset($_SESSION['role']) && $_SESSION['role'] == 'user'): ?>
        <a href="user_dashboard.php">User Dashboard</a>

    <?php endif; ?>


    <?php if (isset($_SESSION['user_id'])): ?>
        <a href="logout.php">Logout</a>

    <?php else: ?>
        <a href="login.php">Login</a>
        <a href="register.php">Register</a>

    <?php endif; ?>

</nav>

<div class="container">
```

### includes/footer.php:

```html
</div>

<footer style="text-align: center; padding: 20px;">
    <p>&copy; 2026 Auth System</p>
</footer>

</body>
</html>
```

### public/css/style.css

```css
  * {
      box-sizing: border-box;
  }

  body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: #f4f4f4;
  }

  nav {
      background: #222;
      padding: 15px 30px;
  }

  nav a {
      color: white;
      text-decoration: none;
      margin-right: 20px;
  }

  nav a:hover {
      color: #ddd;
  }

  .container {
      width: 90%;
      max-width: 800px;
      margin: 40px auto;
      background: white;
      padding: 25px;
      border-radius: 8px;
  }

  input,
  select {
      padding: 10px;
      width: 100%;
      margin-bottom: 10px;
  }

  button {
      padding: 10px 20px;
      border: none;
      background: #222;
      color: white;
      cursor: pointer;
  }

  button:hover {
      background: #444;
  }
```

### conn.php:

```php
<?php

$conn = mysqli_connect("localhost","root","","auth_system");

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
    $role = $_POST['role'];

    $password = password_hash($_POST['password'], PASSWORD_DEFAULT);

    $check = mysqli_query($conn, "SELECT * FROM users WHERE email='$email'");

    if (mysqli_num_rows($check) > 0) {

        echo "Email already exists";

    } else {

        $sql = "INSERT INTO users (name, email, password, role)
                VALUES ('$name', '$email', '$password', '$role')";

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

    <input type="text" name="name" placeholder="Name" required>
    <br><br>

    <input type="email" name="email" placeholder="Email" required>
    <br><br>

    <input type="password" name="password" placeholder="Password" required>
    <br><br>

    <select name="role" required>
        <option disable selected>---Select Role---</option>
        <option value="user">User</option>
        <option value="admin">Admin</option>
    </select>

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
            $_SESSION['role'] = $user['role'];

            if ($user['role'] == 'admin') {

                header("Location: admin_dashboard.php");
                exit;

            } else {

                header("Location: user_dashboard.php");
                exit;

            }

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

### admin_dashboard.php:

```php
<?php
include "includes/header.php";

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit;
}

if ($_SESSION['role'] != 'admin') {
    header("Location: user_dashboard.php");
    exit;
}
?>

<h1>Admin Dashboard</h1>

<p>Welcome, <?php echo htmlspecialchars($_SESSION['name']); ?></p>

<p>You are logged in as Admin.</p>

<?php include "includes/footer.php"; ?>
```

### user_dashboard.php:

```php
<?php
include "includes/header.php";

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit;
}

if ($_SESSION['role'] != 'user') {
    header("Location: admin_dashboard.php");
    exit;
}
?>

<h1>User Dashboard</h1>

<p>Welcome, <?php echo htmlspecialchars($_SESSION['name']); ?></p>

<p>You are logged in as User.</p>

<?php include "includes/footer.php"; ?>
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