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
    is_approved TINYINT(1) NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Agar database pehle se bana hai to ye chala do:
-- ALTER TABLE users ADD is_approved TINYINT(1) NOT NULL DEFAULT 0;
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

        // First admin auto-approved, baqi sab pending (is_approved = 0)
        $adminCount = mysqli_query($conn, "SELECT COUNT(*) AS total FROM users WHERE role='admin' AND is_approved=1");
        $adminCount = mysqli_fetch_assoc($adminCount)['total'];

        $approved = 0;
        if ($role == 'admin' && $adminCount == 0) {
            $approved = 1;
        }

        $sql = "INSERT INTO users (name, email, password, role, is_approved)
                VALUES ('$name', '$email', '$password', '$role', '$approved')";

        if (mysqli_query($conn, $sql)) {

            header("Location: login.php?registered=1");
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

            if (!$user['is_approved']) {

                echo "Your account is pending admin approval. Please try again later.";

            } else {

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

            }

        } else {
            echo "Wrong password";
        }

    } else {
        echo "User not found";
    }
}
?>

<?php if (isset($_GET['registered'])): ?>
    <p>Registration successful! Please wait for admin approval, then login.</p>
<?php endif; ?>

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
include "conn.php";

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

<?php if (isset($_GET['approved'])): ?>
    <p>User approved successfully!</p>
<?php endif; ?>

<h2>Pending Approvals</h2>

<?php
$pending = mysqli_query($conn, "SELECT * FROM users WHERE is_approved = 0");

if (mysqli_num_rows($pending) > 0):

    while ($row = mysqli_fetch_assoc($pending)):
?>

        <p>
            <?php echo htmlspecialchars($row['name']); ?>
            (<?php echo htmlspecialchars($row['email']); ?>)
            - <?php echo htmlspecialchars($row['role']); ?>

            <form method="POST" action="approve.php" style="display: inline;">
                <input type="hidden" name="user_id" value="<?php echo $row['id']; ?>">
                <button type="submit">Approve</button>
            </form>
        </p>

    <?php endwhile; ?>

<?php else: ?>

    <p>No pending users.</p>

<?php endif; ?>

<?php include "includes/footer.php"; ?>
```

### approve.php:

```php
<?php
session_start();
include "conn.php";

if (!isset($_SESSION['user_id']) || $_SESSION['role'] != 'admin') {
    header("Location: login.php");
    exit;
}

if (isset($_POST['user_id'])) {

    $id = $_POST['user_id'];

    $sql = "UPDATE users SET is_approved=1 WHERE id='$id'";

    if (mysqli_query($conn, $sql)) {

        header("Location: admin_dashboard.php?approved=1");
        exit;

    } else {
        echo "Approval failed";
    }
}
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