### logout.php - Without `setcookie()`

```php
<?php
session_start();
session_unset();
session_destroy();

header("Location: login.php");
exit;
?>
```

```text
┌─────────────────────────────────────────────────────────┐
│                    WITHOUT setcookie()                  │
└─────────────────────────────────────────────────────────┘

BEFORE LOGIN
Browser Cookie:
PHPSESSID = 35c4n8p30dfnqdm9vkvrun6t5l
        │
        ▼
Server Session:
35c4n8p30dfnqdm9vkvrun6t5l
        │
        └── No logged-in user


AFTER LOGIN
Browser Cookie:
PHPSESSID = 35c4n8p30dfnqdm9vkvrun6t5l
        │
        ▼
Server Session:
35c4n8p30dfnqdm9vkvrun6t5l
        │
        ├── user_id = 10
        └── username = Kaif


AFTER LOGOUT
Browser Cookie:
PHPSESSID = 35c4n8p30dfnqdm9vkvrun6t5l  ← Cookie still exists
        │
        ▼
Server Session:
35c4n8p30dfnqdm9vkvrun6t5l
        │
        └── ❌ Session destroyed
```

**Important:** Logout ke baad same `PHPSESSID` browser mein reh sakti hai, lekin us ID se linked **server-side session destroy ho chuki hoti hai**.

---

### 2. logout.php - With `setcookie()`

```php
<?php

session_start();

$_SESSION = [];

session_destroy();

setcookie(
    session_name(),
    '',
    time() - 3600,
    '/'
);

header("Location: login.php");
exit;

?>
```

```text
┌─────────────────────────────────────────────────────────┐
│                     WITH setcookie()                    │
└─────────────────────────────────────────────────────────┘

BEFORE LOGIN
Browser Cookie:
PHPSESSID = 35c4n8p30dfnqdm9vkvrun6t5l
        │
        ▼
Server Session:
35c4n8p30dfnqdm9vkvrun6t5l
        │
        └── No logged-in user


AFTER LOGIN
Browser Cookie:
PHPSESSID = 35c4n8p30dfnqdm9vkvrun6t5l
        │
        ▼
Server Session:
35c4n8p30dfnqdm9vkvrun6t5l
        │
        ├── user_id = 10
        └── username = Kaif


AFTER LOGOUT
        │
        ├── session_destroy()
        │        ↓
        │   Server Session ❌
        │
        └── setcookie(...)
                 ↓
           Browser PHPSESSID Cookie ❌ Removed


Browser:
PHPSESSID = removed

Server:
Old Session = destroyed
```
