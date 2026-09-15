# MYSQL CODE:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    gender VARCHAR(20)
);
```

---

# DROPDOWN FORM:

```html
<form action="insert.php" method="POST">

    <input type="text" name="name" placeholder="Name">

    <select name="gender">
        <option disable selected>Select Gender</option>
        <option value="Male">Male</option>
        <option value="Female">Female</option>
    </select>

    <button type="submit" name="submit">Save</button>

</form>

<a href="read.php">Read Data</a>
```

---

# PHP INSERT:

```php
<?php

include "conn.php";

if ($_SERVER['REQUEST_METHOD'] == "POST") {

    $name = $_POST['name'] ?? '';
    $gender = $_POST['gender'] ?? '';

    // Name validation
    if (empty($name)) {
        echo "Please enter your name";
        exit;
    }

    // Dropdown validation
    if (empty($gender)) {
        echo "Please select gender";
        exit;
    }

    $query = "INSERT INTO users (name, gender)
              VALUES ('$name', '$gender')";

    $result = mysqli_query($conn, $query);

    if ($result) {
        echo "Data inserted successfully";
    } else {
        echo "Data not inserted";
    }
}

?>
```

# PHP READ:

```php
<?php

include "conn.php";
$query = "SELECT * FROM users";
$result = mysqli_query($conn, $query);
?>

<table border="1" cellpadding="10">

    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Gender</th>
    </tr>

    <?php while ($row = mysqli_fetch_assoc($result)): ?>

        <tr>
            <td><?php echo $row['id']; ?></td>
            <td><?php echo $row['name']; ?></td>
            <td><?php echo $row['gender']; ?></td>
        </tr>

    <?php endwhile ?>

</table>
```