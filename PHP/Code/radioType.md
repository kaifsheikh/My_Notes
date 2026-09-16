### 1. HTML Form:

```html
<form action="save.php" method="POST">

    <label>Gender:</label>

    <input type="radio" name="gender" value="Male">
    <label>Male</label>

    <input type="radio" name="gender" value="Female">
    <label>Female</label>

    <button type="submit">Save</button>

</form>
```

---

### 2. Database:

Example MySQL table:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    gender VARCHAR(20)
);
```

---

### 3. `save.php`

```php
<?php

if ($_SERVER["REQUEST_METHOD"] === "POST") {

    if (!isset($_POST['gender'])) {
        die("Please select your gender.");
    }

    $gender = trim($_POST['gender']);

    if ($gender === "") {
        die("Please select your gender.");
    }

    if ($gender !== "Male" && $gender !== "Female") {
        die("Invalid gender selected.");
    }

    // Insert query
    $sql = "INSERT INTO users (gender) VALUES ('$gender')";

    // Query execute
    if (mysqli_query($conn, $sql)) {

        echo "Data saved successfully!";

    } else {

        echo "Data could not be saved";
    }

    // Connection close
    mysqli_close($conn);

} else {

    echo "Invalid request.";

}

?>
```