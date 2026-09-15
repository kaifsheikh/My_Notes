## `read.php`

```php id="k8m4p2"
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


// SELECT query
$sql = "SELECT * FROM students";


// Query execute
$result = mysqli_query($conn, $sql);

?>

<h2>Students List</h2>

<table border="1" cellpadding="10">

    <tr>

        <th>ID</th>
        <th>Name</th>
        <th>Email</th>
        <th>Age</th>
        <th>Course</th>

    </tr>


    <?php if (mysqli_num_rows($result) > 0) : ?>


        <?php while ($row = mysqli_fetch_assoc($result)) : ?>

            <tr>

                <td>
                    <?= $row["id"]; ?>
                </td>

                <td>
                    <?= $row["name"]; ?>
                </td>

                <td>
                    <?= $row["email"]; ?>
                </td>

                <td>
                    <?= $row["age"]; ?>
                </td>

                <td>
                    <?= $row["course"]; ?>
                </td>

            </tr>

        <?php endwhile; ?>


    <?php else : ?>


        <tr>

            <td colspan="5">
                No students found.
            </td>

        </tr>


    <?php endif; ?>

</table>


<?php

// Connection close
mysqli_close($conn);

?>
```