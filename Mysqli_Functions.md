# mysqli_connect()
MySQL database ke saath connection banata hai.
```php
$conn = mysqli_connect("localhost", "root", "", "database_name");

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
```

# mysqli_connect_error()
Agar database connection fail ho jaye to yeh function error ka reason (message) return karta hai. <br>
Iske andar koi argument nahi hota.
```php
<?php
$conn = mysqli_connect("localhost", "root", "", "wrong_db");

if (!$conn) {
    echo "Connection failed: " . mysqli_connect_error();
}
?>
```

# mysqli_query()
Aap database ko kuch kaam karne ka liye (query) dete ho, aur mysqli_query() us Query ko MySQL ko bhejta hai. <br>
ager SELECT ki Query likhte hai tu yeah Object return karta hai jisme Rows hoti hai <br>
werna dosre Queries mein yeah True or False return karta hai. ager true hai tu 1 return karayga<br>
isme 2 paramters hote hai 1 connection or dosra Query
```php
$result = mysqli_query($conn, $query);
```

# mysqli_error($conn)
Jab aapki SQL query fail ho jaye, to mysqli_error() aapko exact error message batata hai — kya galti hui.
```php
if (mysqli_query($conn, $sql)) {
    echo "Data inserted!";
} else {
    echo "Query failed: " . mysqli_error($conn);
}
```

# mysqli_close($conn)
Jab kaam complete ho jaye (query waghera), to mysqli_close() use karke connection properly band kar dete hain.
```php
mysqli_close($conn);
```

# mysqli_fetch_assoc($result);
mysqli_fetch_assoc() ek associative array return karta hai, jisme key-value pairs hote hain. <br>
name - yeah Key hai jisa (Column Name) bhe bolte hai. <br>
"Ali" - yeah Key ki (Value) hai jisa Data bolte hai.  
```php
[
  "name" => "Ali",
  "email" => "ali@example.com"
]
```