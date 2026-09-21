## 1. Mysql Code:

```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    city VARCHAR(100) NOT NULL
);

INSERT INTO users (name, email, city) VALUES
('Ali', 'ali@gmail.com', 'Karachi'),
('Sara', 'sara@gmail.com', 'Lahore'),
('Hamza', 'hamza@gmail.com', 'Islamabad');
```

---

## 2. Database code `db.php`:

```php
$conn = mysqli_connect("localhost", "root", "", "your_database_name");

if (!$conn) {
    die("Database connection failed: " . mysqli_connect_error());
}
```

---


## 2. Update Form `update.php`:

```php
<?php

include "db.php";

$id = $_GET['id'];

$query = "SELECT * FROM users WHERE id = '$id'";
$result = mysqli_query($conn, $query);

$user = mysqli_fetch_assoc($result);
?>

<!DOCTYPE html>
<html>
<head>
    <title>Update User</title>
</head>
<body>

<h2>Update User</h2>

<form action="insert.php" method="POST">

    <input type="hidden" name="id" value="<?php echo $user['id']; ?>">

    <label>Name:</label>
    <input type="text" name="name" value="<?php echo $user['name']; ?>">
    <br><br>

    <label>Email:</label>
    <input type="email" name="email" value="<?php echo $user['email']; ?>">
    <br><br>

    <label>City:</label>
    <input type="text" name="city" value="<?php echo $user['city']; ?>">
    <br><br>

    <button type="submit" name="update">Update</button>

</form>

</body>
</html>
```

---

## 3. Php Code `insert.php`

```php
<?php

require_once "db.php";

if (isset($_POST['update'])) {

    $id = $_POST['id'];

    $name = trim($_POST['name']);
    $email = trim($_POST['email']);
    $city = trim($_POST['city']);

    if (empty($name) || empty($email) || empty($city)) {
        die("All fields are required.");
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email address.");
    }

    $query = "UPDATE users 
              SET name = '$name', 
                  email = '$email', 
                  city = '$city'
              WHERE id = '$id'";

    $result = mysqli_query($conn, $query);

    if ($result) {
        echo "User updated successfully.";
    } else {
        echo "Update failed: " . mysqli_error($conn);
    }
}

?>
```

## 4. read Data `read.php`:

```php
<?php

include "db.php";

$query = "SELECT * FROM users";

$result = mysqli_query($conn, $query);

?>

<!DOCTYPE html>
<html>
<head>
    <title>Users</title>
</head>
<body>

<h2>Users List</h2>

<table border="1" cellpadding="10" cellspacing="0">

    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Email</th>
        <th>City</th>
        <th>Action</th>
    </tr>

    <?php

    while ($row = mysqli_fetch_assoc($result)) {

    ?>

        <tr>
            <td><?php echo $row['id']; ?></td>
            <td><?php echo $row['name']; ?></td>
            <td><?php echo $row['email']; ?></td>
            <td><?php echo $row['city']; ?></td>

            <td>
                <a href="update.php?id=<?php echo $row['id']; ?>">
                    Edit
                </a>
            </td>
        </tr>

    <?php

    }

    ?>

</table>

</body>
</html>
```
