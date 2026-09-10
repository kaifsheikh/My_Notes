# PHP Essential Functions (Superglobals ke liye)

Jab hum Superglobals use karte hain, toh in functions ki zaroorat padti hai taake hum data ko sahi aur safe tarike se handle kar sakein.

---

## 1. `isset()` - "Check Karna"
*   **Purpose:** Yeh check karta hai ke kya variable ya array mein data maujood hai ya nahi.
*   **Simple Example (HTML + PHP):**
```html
<form method="GET">
    <input type="text" name="name" placeholder="Enter name">
    <button type="submit">Submit</button>
</form>

<?php
if (isset($_GET['name'])) {
    echo "Haan, name mil gaya: " . $_GET['name'];
}
?>
```

---

## 2. `htmlspecialchars()` - "Security Guard"
*   **Purpose:** Yeh HTML tags ko normal text mein badal deta hai taake website hack na ho (XSS protection).
*   **Simple Example (HTML + PHP):**
```html
<form method="POST">
    <input type="text" name="comment" placeholder="Comment likhein">
    <button type="submit">Post</button>
</form>

<?php
if (isset($_POST['comment'])) {
    // Yeh script tag ko as a text dikhayega, run nahi karega
    echo "User comment: " . htmlspecialchars($_POST['comment']);
}
?>
```

---

## 3. `filter_var()` - "Data Cleaner"
*   **Purpose:** Yeh user ke input data ko check ya saaf (clean) karta hai.
*   **Simple Example (HTML + PHP):**
```html
<form method="POST">
    <input type="email" name="user_email" placeholder="Email daalein">
    <button type="submit">Save</button>
</form>

<?php
if (isset($_POST['user_email'])) {
    // Sirf email ke sahi characters rakhega
    $clean_email = filter_var($_POST['user_email'], FILTER_SANITIZE_EMAIL);
    echo "Cleaned Email: " . $clean_email;
}
?>
```

---

## 4. `session_start()` - "Session Ka Switch"
*   **Purpose:** Session ko start karna taake user ka data yaad rahe.
*   **Simple Example (HTML + PHP):**
```html
<form method="POST">
    <input type="text" name="user" placeholder="Username">
    <button type="submit">Login</button>
</form>

<?php
session_start(); // Session use karne se pehle ye likhna zaroori hai
if (isset($_POST['user'])) {
    $_SESSION['username'] = $_POST['user'];
    echo "Session mein name save ho gaya: " . $_SESSION['username'];
}
?>
```

---

## 5. `setcookie()` - "User Yaad Rakhna"
*   **Purpose:** Browser mein choti si file (cookie) save karna.
*   **Simple Example (HTML + PHP):**
```html
<form method="POST">
    <button type="submit" name="set_theme">Dark Theme Set Karein</button>
</form>

<?php
if (isset($_POST['set_theme'])) {
    // 1 ghante ke liye cookie banao
    setcookie("theme", "dark", time() + 3600, "/");
    echo "Cookie set ho gayi!";
}
?>
```

---

## 6. `move_uploaded_file()` - "File Save Karna"
*   **Purpose:** Upload hui file ko temporary jagah se apni folder mein laana.
*   **Simple Example (HTML + PHP):**
```html
<!-- enctype="multipart/form-data" zaroori hai file upload ke liye -->
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="my_file">
    <button type="submit">Upload</button>
</form>

<?php
if (isset($_FILES['my_file'])) {
    $target = "uploads/" . $_FILES['my_file']['name'];
    if (move_uploaded_file($_FILES['my_file']['tmp_name'], $target)) {
        echo "File upload ho gayi!";
    }
}
?>
```
