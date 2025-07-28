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
# mysqli_num_rows($result);
Ye function batata hai ke query ka result me kitni rows aayi hain.
yeah number of orws return karta hai 1 ka maltab hai ka 1 row <br>
or 0 ka matlab hai kch nahe hai
```php
$sql = "SELECT * FROM users WHERE email= 'test@example.com'";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    echo "User already exists!"; // TRUE because 1 or more rows
} else {
    echo "You can register."; // FALSE because 0 rows
}
```
# mysqli_real_escape_string()

Ye function user ke input se dangerous characters (like ', ", \, ;, etc.) hata deta hai jo SQL injection karne ke liye use ho sakte hain.

```php
$user_input = "' OR 1=1 --";
$clean_input = mysqli_real_escape_string($conn, $user_input);
```
# hash_password()

Ye function user ke password ko encrypt (hash) karta hai — taake actual password database mein safe tareeke se store ho. <br>
<b>PASSWORD_DEFAULT</b> <br>
Ye ek constant hai jo password_hash() ke sath use hota hai. Ye batata hai ke PHP konsa algorithm use kare password ko encrypt karne ke liye.

```php
$password = "hello123";
$hashed_password = password_hash($password, PASSWORD_DEFAULT);

echo $hashed_password;
```
# password_verify()

Jab user register karta hai, uska password encrypt karke store kiya jata hai using password_hash().
Login ke time, us hashed password ko decode nahi kar sakte — isliye hum user ka plain password le kar password_verify() se check karte hain ke match karta hai ya nahi.

Jab user register karta hai, uska password encrypt karke store kiya jata hai using password_hash().
Login ke time, us hashed password ko decode nahi kar sakte — isliye hum user ka plain password le kar password_verify() se check karte hain ke match karta hai ya nahi.

```php
$enteredPassword = "mypassword123"; // User ne form me dala
$dbPassword = '$2y$10$8ZbYJti2v9zK3lvC1V7kpuLki3kkwl7T1ZkCZXKOKhFaPL9m5qaeq'; // from DB

if (password_verify($enteredPassword, $dbPassword)) {
    echo "Login successful ✅";
} else {
    echo "Wrong password ❌";
}
```
