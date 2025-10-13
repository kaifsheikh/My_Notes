# Download Open Source PHPMailor Code:
https://github.com/PHPMailer/PHPMailer

# PHPMailor Form
```html
<!DOCTYPE html>
<html>
<head>
    <title>Send Email Form</title>
</head>
<body>
    <h2>Contact Form</h2>
    <form action="sendmail.php" method="POST">
        <label>Name:</label><br>
        <input type="text" name="name" required><br><br>

        <label>Email:</label><br>
        <input type="email" name="email" required><br><br>

        <label>Message:</label><br>
        <textarea name="message" required></textarea><br><br>

        <button type="submit">Send Email</button>
    </form>
</body>
</html>
```

# PHPMailor php Code
```php
<?php

// PHPMailer include files
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;


require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/SMTP.php';

// Form se data lena
$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];

// PHPMailer ka object
$mail = new PHPMailer(true);

try {

    // SMTP settings
    $mail->isSMTP();
    $mail->Host = 'smtp.gmail.com';
    $mail->SMTPAuth = true;
    $mail->Username = 'shahkaif327@gmail.com'; // Apna Gmail id
    $mail->Password = 'akfq dxvq rtpr zdor';   // App password (normal password nahi chalega)
    $mail->SMTPSecure = 'tls';
    $mail->Port = 587;


    // Sender
    $mail->setFrom($email, $name); // user ne jo form me likha

    // Receiver
    $mail->addAddress('shahkaif327@gmail.com', 'Kaif Sheikh'); // tumhara khud ka Gmail

    // Email content
    $mail->isHTML(true);
    $mail->Subject = "New message from $name";
    $mail->Body    = "<h3>Name: $name</h3>
                      <h3>Email: $email</h3>
                      <p>Message: $message</p>";

    // Send Email
    $mail->send();
    echo "Email successfully sent!";
} catch (Exception $e) {
    echo "Error: {$mail->ErrorInfo}";
}
```
# Explanation:

## PHPMailer Include Karna

```php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/SMTP.php';
```
* **PHPMailer.php** → email bhejne ka main system
* **SMTP.php** → SMTP server se connect hone ke liye
* **Exception.php** → agar koi error aaye to handle kar sake

---

## 🔹 Step 2: Form Se Data Lena

```php
$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];
```

👉 Yeh code HTML form se user ka data receive karta hai:

* `name` = user ka naam
* `email` = user ka email address
* `message` = user ka likha hua message

---
## PHPMailer Object Banana

```php
$mail = new PHPMailer(true);
```
Is line se hum ek **PHPMailer ka object** bana rahe hain jisse hum email ke options set kar sakein.

---

## SMTP Settings

```php
$mail->isSMTP();
$mail->Host = 'smtp.gmail.com';
$mail->SMTPAuth = true;
$mail->Username = 'shahkaif327@gmail.com';
$mail->Password = 'akfq dxvq rtpr zdor';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;
```
| Setting      | Explanation                                                      |
| ------------ | ---------------------------------------------------------------- |
| `isSMTP()`   | Batata hai ke hum SMTP use kar rahe hain                         |
| `Host`       | Gmail ka SMTP server address                                     |
| `SMTPAuth`   | Authentication enable karta hai (email/password verify hota hai) |
| `Username`   | Tumhara Gmail address (jisse email send hogi)                    |
| `Password`   | Tumhara Gmail App Password (normal password nahi chalega)        |
| `SMTPSecure` | Security ke liye TLS encryption use karta hai                    |
| `Port`       | Gmail SMTP ka port number (587)                                  |

---

## Sender:

```php
$mail->setFrom($email, $name);
```
1. Yeh line batati hai ke email **kis naam aur kis email se bheji ja rahi hai**.
2. Yani sender hai **user** jo form bhar raha hai.

---

## Receiver (Email Lene Wala)

```php
$mail->addAddress('shahkaif327@gmail.com', 'Kaif Sheikh');
```
1. Yeh line batati hai ke email **kisko** jaayegi.
2. Yahan tumhara khud ka Gmail diya hua hai.

---

## Email Content (Subject + Body)

```php
$mail->isHTML(true);
$mail->Subject = "New message from $name";
$mail->Body    = "<h3>Name: $name</h3>
                  <h3>Email: $email</h3>
                  <p>Message: $message</p>";
```
* `isHTML(true)` → batata hai ke email me HTML likh sakte ho.
* `Subject` → email ka topic ya title.
* `Body` → email ke andar ka text (HTML format me likha gaya).
---

## Email Send Karna

```php
$mail->send();
echo "Email successfully sent!";
```
Yeh line actual me email bhejti hai.
Agar sab kuch theek ho to message show hoga: ✅ **Email successfully sent!**

---

## Error Handle Karna

```php
} catch (Exception $e) {
    echo "Error: {$mail->ErrorInfo}";
}
```
Agar email bhejte waqt koi problem aaye (like wrong password, internet issue, etc.) to error show karega.

```
Error: SMTP connect() failed.
```
---
