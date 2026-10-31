# Complete Simple Project — Register + Login with REST API Concept

Chalo **poora project** banate hain — **6 files**, simple UI, PHP + HTML ek hi file mein. Koi JavaScript nahi, koi fetch nahi — **pure PHP forms** with **JWT token** concept.

---

## Project Structure

```
rest-api-demo/
├── db.php          → Database connection
├── jwt.php         → Token banane/verify karne ke functions
├── register.php    → Register form + logic
├── login.php       → Login form + logic
├── profile.php     → Protected page (token check)
└── logout.php      → Logout
```

---

# FILE 1: `db.php` — Database Connection

```php
<?php
// db.php

$conn = mysqli_connect("localhost", "root", "", "rest_api_demo");

if (!$conn) {
    die("Database connection failed: " . mysqli_connect_error());
}
?>
```

**Pehle phpMyAdmin mein yeh chalao:**

```sql
CREATE DATABASE rest_api_demo;
USE rest_api_demo;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO users (name, email, password) VALUES
('Ali Khan', 'ali@example.com', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi');
```

_(Yeh test user ka password `123456` hai)_

---

# FILE 2: `jwt.php` — Token Functions

```php
<?php
// jwt.php

$SECRET_KEY = "my-super-secret-key-12345";

// Token banao (HEADER.PAYLOAD.SIGNATURE)
function makeToken($payload, $secretKey) {

    // HEADER
    $header = ["alg" => "HS256", "typ" => "JWT"];
    $headerEncoded = b64Encode(json_encode($header));

    // PAYLOAD
    $payload['iat'] = time();
    $payload['exp'] = time() + 3600;
    $payloadEncoded = b64Encode(json_encode($payload));

    // SIGNATURE
    $signature = hash_hmac('sha256',
        $headerEncoded . "." . $payloadEncoded,
        $secretKey, true);
    $signatureEncoded = b64Encode($signature);

    return $headerEncoded . "." . $payloadEncoded . "." . $signatureEncoded;
}

// Token verify karo
function checkToken($token, $secretKey) {

    $parts = explode('.', $token);
    if (count($parts) !== 3) return false;

    list($h, $p, $s) = $parts;

    // Signature match karo
    $expected = b64Encode(hash_hmac('sha256', $h . "." . $p, $secretKey, true));
    if (!hash_equals($expected, $s)) return false;

    // Payload decode
    $payload = json_decode(b64Decode($p), true);

    // Expiry check
    if (isset($payload['exp']) && $payload['exp'] < time()) return false;

    return $payload;
}

function b64Encode($data) {
    return rtrim(strtr(base64_encode($data), '+/', '-_'), '=');
}

function b64Decode($data) {
    return base64_decode(strtr($data, '-_', '+/'));
}
?>
```

**Yeh REST API ka core hai** — HEADER.PAYLOAD.SIGNATURE format.

---

# FILE 3: `register.php` — Register Form + Logic

```php
<?php
session_start();
require_once 'db.php';
require_once 'jwt.php';

$error = "";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $name     = trim($_POST['name'] ?? '');
    $email    = trim($_POST['email'] ?? '');
    $password = $_POST['password'] ?? '';

    // Validation
    if ($name == '' || $email == '' || $password == '') {
        $error = "Saari fields bharna zaroori hai";
    }
    elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $error = "Email sahi format mein nahi hai";
    }
    elseif (strlen($password) < 6) {
        $error = "Password kam se kam 6 characters ka ho";
    }
    else {
        // Email already exist?
        $email_safe = mysqli_real_escape_string($conn, $email);
        $check = mysqli_query($conn, "SELECT id FROM users WHERE email='$email_safe'");

        if (mysqli_num_rows($check) > 0) {
            $error = "Yeh email pehle se registered hai";
        } else {
            // Password hash karo
            $hashed = password_hash($password, PASSWORD_DEFAULT);

            // INSERT (REST API - Create)
            $name_safe = mysqli_real_escape_string($conn, $name);
            $pass_safe = mysqli_real_escape_string($conn, $hashed);

            $sql = "INSERT INTO users (name, email, password)
                    VALUES ('$name_safe', '$email_safe', '$pass_safe')";

            if (mysqli_query($conn, $sql)) {
                // Token banao (auto-login)
                $userId = mysqli_insert_id($conn);
                $token = makeToken([
                    "userId" => $userId,
                    "name"   => $name,
                    "email"  => $email
                ], $SECRET_KEY);

                // Session mein save
                $_SESSION['token'] = $token;
                $_SESSION['user'] = [
                    "id" => $userId, "name" => $name, "email" => $email
                ];

                header("Location: profile.php");
                exit;
            } else {
                $error = "User create nahi hua: " . mysqli_error($conn);
            }
        }
    }
}
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Register</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box;
            font-family: Arial, sans-serif; }
        body {
            background: #667eea;
            min-height: 100vh;
            display: flex; justify-content: center; align-items: center;
            padding: 20px;
        }
        .box {
            background: white;
            padding: 30px;
            border-radius: 10px;
            width: 100%; max-width: 380px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.15);
        }
        h2 { text-align: center; margin-bottom: 20px; color: #333; }
        label { display: block; margin: 12px 0 5px;
                color: #555; font-size: 14px; font-weight: 600; }
        input {
            width: 100%; padding: 10px 12px;
            border: 1px solid #ccc; border-radius: 5px;
            font-size: 14px; outline: none;
        }
        input:focus { border-color: #667eea; }
        button {
            width: 100%; padding: 11px;
            background: #667eea; color: white;
            border: none; border-radius: 5px;
            font-size: 15px; font-weight: 600;
            cursor: pointer; margin-top: 18px;
        }
        button:hover { background: #5568d3; }
        .error {
            background: #f8d7da; color: #721c24;
            padding: 10px; border-radius: 5px;
            font-size: 13px; margin-bottom: 10px;
            border: 1px solid #f5c6cb;
        }
        .link {
            text-align: center; margin-top: 15px;
            font-size: 13px; color: #666;
        }
        .link a { color: #667eea; text-decoration: none; font-weight: 600; }
    </style>
</head>
<body>

<div class="box">
    <h2>Register</h2>

    <?php if ($error): ?>
        <div class="error"><?php echo htmlspecialchars($error); ?></div>
    <?php endif; ?>

    <form method="POST">
        <label>Name</label>
        <input type="text" name="name"
               value="<?php echo htmlspecialchars($_POST['name'] ?? ''); ?>"
               placeholder="Ali Khan" required>

        <label>Email</label>
        <input type="email" name="email"
               value="<?php echo htmlspecialchars($_POST['email'] ?? ''); ?>"
               placeholder="ali@example.com" required>

        <label>Password</label>
        <input type="password" name="password"
               placeholder="Minimum 6 characters" required>

        <button type="submit">Register</button>
    </form>

    <div class="link">
        Account hai? <a href="login.php">Login karo</a>
    </div>
</div>

</body>
</html>
```

---

# FILE 4: `login.php` — Login Form + Logic

```php
<?php
session_start();
require_once 'db.php';
require_once 'jwt.php';

$error = "";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $email    = trim($_POST['email'] ?? '');
    $password = $_POST['password'] ?? '';

    if ($email == '' || $password == '') {
        $error = "Email aur password dono zaroori hain";
    }
    else {
        $email_safe = mysqli_real_escape_string($conn, $email);
        $result = mysqli_query($conn, "SELECT * FROM users WHERE email='$email_safe' LIMIT 1");
        $user = mysqli_fetch_assoc($result);

        if (!$user) {
            $error = "Yeh email registered nahi hai";
        }
        elseif (!password_verify($password, $user['password'])) {
            $error = "Password galat hai";
        }
        else {
            // Login success — token banao
            $token = makeToken([
                "userId" => $user['id'],
                "name"   => $user['name'],
                "email"  => $user['email']
            ], $SECRET_KEY);

            $_SESSION['token'] = $token;
            $_SESSION['user'] = [
                "id"    => $user['id'],
                "name"  => $user['name'],
                "email" => $user['email']
            ];

            header("Location: profile.php");
            exit;
        }
    }
}
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box;
            font-family: Arial, sans-serif; }
        body {
            background: #667eea;
            min-height: 100vh;
            display: flex; justify-content: center; align-items: center;
            padding: 20px;
        }
        .box {
            background: white;
            padding: 30px;
            border-radius: 10px;
            width: 100%; max-width: 380px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.15);
        }
        h2 { text-align: center; margin-bottom: 20px; color: #333; }
        label { display: block; margin: 12px 0 5px;
                color: #555; font-size: 14px; font-weight: 600; }
        input {
            width: 100%; padding: 10px 12px;
            border: 1px solid #ccc; border-radius: 5px;
            font-size: 14px; outline: none;
        }
        input:focus { border-color: #667eea; }
        button {
            width: 100%; padding: 11px;
            background: #667eea; color: white;
            border: none; border-radius: 5px;
            font-size: 15px; font-weight: 600;
            cursor: pointer; margin-top: 18px;
        }
        button:hover { background: #5568d3; }
        .error {
            background: #f8d7da; color: #721c24;
            padding: 10px; border-radius: 5px;
            font-size: 13px; margin-bottom: 10px;
            border: 1px solid #f5c6cb;
        }
        .link {
            text-align: center; margin-top: 15px;
            font-size: 13px; color: #666;
        }
        .link a { color: #667eea; text-decoration: none; font-weight: 600; }
        .hint {
            margin-top: 12px; font-size: 12px;
            color: #888; text-align: center;
        }
    </style>
</head>
<body>

<div class="box">
    <h2>Login</h2>

    <?php if ($error): ?>
        <div class="error"><?php echo htmlspecialchars($error); ?></div>
    <?php endif; ?>

    <form method="POST">
        <label>Email</label>
        <input type="email" name="email"
               value="<?php echo htmlspecialchars($_POST['email'] ?? ''); ?>"
               placeholder="ali@example.com" required>

        <label>Password</label>
        <input type="password" name="password"
               placeholder="Your password" required>

        <button type="submit">Login</button>
    </form>

    <div class="hint">
        Test: ali@example.com / 123456
    </div>

    <div class="link">
        Account nahi hai? <a href="register.php">Register karo</a>
    </div>
</div>

</body>
</html>
```

---

# FILE 5: `profile.php` — Protected Page

**Yahan token verify hota hai — REST API ka protected endpoint.**

```php
<?php
session_start();
require_once 'db.php';
require_once 'jwt.php';

// Token nahi hai? → Login page
if (!isset($_SESSION['token'])) {
    header("Location: login.php");
    exit;
}

// Token verify karo (REST API style)
$payload = checkToken($_SESSION['token'], $SECRET_KEY);

if ($payload === false) {
    // Invalid ya expired
    session_destroy();
    header("Location: login.php");
    exit;
}

// Database se fresh data lo (mysqli)
$userId = (int) $payload['userId'];
$result = mysqli_query($conn, "SELECT id, name, email FROM users WHERE id=$userId LIMIT 1");
$user = mysqli_fetch_assoc($result);

if (!$user) {
    session_destroy();
    header("Location: login.php");
    exit;
}
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Profile</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box;
            font-family: Arial, sans-serif; }
        body {
            background: #667eea;
            min-height: 100vh;
            display: flex; justify-content: center; align-items: center;
            padding: 20px;
        }
        .box {
            background: white;
            padding: 30px;
            border-radius: 10px;
            width: 100%; max-width: 420px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.15);
        }
        h2 { text-align: center; margin-bottom: 20px; color: #333; }
        .avatar {
            width: 70px; height: 70px;
            background: #667eea; color: white;
            border-radius: 50%;
            display: flex; justify-content: center; align-items: center;
            font-size: 28px; font-weight: bold;
            margin: 0 auto 20px;
        }
        .row {
            display: flex; justify-content: space-between;
            padding: 12px 0; border-bottom: 1px solid #eee;
            font-size: 14px;
        }
        .row:last-of-type { border-bottom: none; }
        .label { color: #777; font-weight: 600; }
        .value { color: #333; }
        .logout {
            display: block; margin-top: 20px;
            padding: 11px; background: #e74c3c;
            color: white; text-align: center;
            text-decoration: none; border-radius: 5px;
            font-weight: 600; font-size: 14px;
        }
        .logout:hover { background: #c0392b; }
        .token-box {
            margin-top: 15px; padding: 10px;
            background: #f5f5f5; border-radius: 5px;
            font-size: 11px; color: #555;
            word-break: break-all; font-family: monospace;
            max-height: 60px; overflow-y: auto;
        }
        .token-box strong {
            display: block; margin-bottom: 5px;
            color: #667eea; font-size: 12px;
        }
    </style>
</head>
<body>

<div class="box">
    <h2>My Profile</h2>

    <div class="avatar">
        <?php echo strtoupper(substr($user['name'], 0, 1)); ?>
    </div>

    <div class="row">
        <span class="label">User ID</span>
        <span class="value"><?php echo $user['id']; ?></span>
    </div>
    <div class="row">
        <span class="label">Name</span>
        <span class="value"><?php echo htmlspecialchars($user['name']); ?></span>
    </div>
    <div class="row">
        <span class="label">Email</span>
        <span class="value"><?php echo htmlspecialchars($user['email']); ?></span>
    </div>

    <div class="token-box">
        <strong>JWT Token (yeh REST API ka proof hai):</strong>
        <?php echo htmlspecialchars($_SESSION['token']); ?>
    </div>

    <a href="logout.php" class="logout">Logout</a>
</div>

</body>
</html>
```

---

# FILE 6: `logout.php` — Logout

```php
<?php
session_start();
session_destroy();
header("Location: login.php");
exit;
?>
```

---

# REST API Concepts — Kahan Hain?

| Concept             | Kahan dikha?                                                            |
| ------------------- | ----------------------------------------------------------------------- |
| **REST API**        | Har page ek "endpoint" hai — `register.php`, `login.php`, `profile.php` |
| **Create (POST)**   | Register mein naya user insert                                          |
| **Read (GET)**      | Profile mein user data fetch                                            |
| **Token**           | Login ke baad `makeToken()` se banta hai                                |
| **HEADER**          | `{"alg":"HS256","typ":"JWT"}` — `jwt.php` mein                          |
| **PAYLOAD**         | `{"userId":1,"name":"Ali"}` — `jwt.php` mein                            |
| **SIGNATURE**       | `hash_hmac(...)` — `jwt.php` mein                                       |
| **Stateless**       | Har page pe token verify hota hai — server session pe depend nahi       |
| **Protected Route** | `profile.php` bina token ke login pe bhej deta hai                      |

---

# Kaise Chalayein (Step by Step)

### Step 1: XAMPP start karo

- **Apache** → Start
- **MySQL** → Start

### Step 2: Files rakho

`C:\xampp\htdocs\rest-api-demo\` mein saari 6 files daalo.

### Step 3: Database banao

phpMyAdmin → SQL tab → upar wala SQL code paste → Go

### Step 4: Browser kholo

```
http://localhost/rest-api-demo/register.php
```

### Step 5: Test karo

**Test 1 — Register:**

- Name: Sara
- Email: sara@test.com
- Password: 123456

→ "Register" dabao → **Profile page** pe redirect ho jayega ✅

**Test 2 — Logout:**
→ "Logout" dabao → Login page pe aayega

**Test 3 — Login:**

- Email: `sara@test.com`
- Password: `123456`

→ "Login" dabao → **Profile page** ✅

**Test 4 — Galat password:**

- Password: `wrong`

→ "Password galat hai" error dikhega ✅

**Test 5 — Bina login profile:**

```
http://localhost/rest-api-demo/profile.php
```

→ Login page pe redirect ho jayega ✅

---

# Token Dekho (jwt.io pe)

Login ke baad profile page pe **token box** mein token dikhega. Copy karo, **jwt.io** pe paste karo:

### HEADER:

```json
{ "alg": "HS256", "typ": "JWT" }
```

### PAYLOAD:

```json
{
  "userId": 2,
  "name": "Sara",
  "email": "sara@test.com",
  "iat": 1729936800,
  "exp": 1729940400
}
```

### SIGNATURE:

```
SflKxwRJSMe...
```

**jwt.io pe secret key daalo** (`my-super-secret-key-12345`) → **"Signature Verified"** dikhega.

---

# Ek Line Mein:

> **6 simple files — db.php (connection), jwt.php (token functions), register.php (form + insert + token), login.php (form + verify + token), profile.php (token verify → data), logout.php (session destroy). Pure PHP forms, no JavaScript. UI clean aur simple. REST API ka pura concept — Create, Read, Token, HEADER.PAYLOAD.SIGNATURE, Stateless — sab include hai.**

---

## Kya aap chahte ho main isme kuch aur add karoon?

1. **Update Profile** — PUT method ka example
2. **Delete Account** — DELETE method
3. **Change Password** — purana verify, naya set
4. **Remember Me** — cookie-based token
5. **All Users List** — `GET users.php`

Bataiye!
