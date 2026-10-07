# Download Open Source PHPMailor Code:
https://github.com/PHPMailer/PHPMailer

# PHPMailor Form
## `index.html`
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
## `sendmail.php`
```php
<?php
// PHPMailer include files
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/SMTP.php';

// Form se data lena
$name    = $_POST['name'];
$email   = $_POST['email'];
$message = $_POST['message'];

// PHPMailer ka object
$mail = new PHPMailer(true);

try {
    // SMTP settings
    $mail->isSMTP();
    $mail->Host       = 'smtp.gmail.com';
    $mail->SMTPAuth   = true;
    $mail->Username   = 'shahkaif327@gmail.com'; // Aapki apni Gmail id
    $mail->Password   = 'khrj xecd bnok gzmi';   // Aapka App Password
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
    $mail->Port       = 587;

    // SENDER: yeah sender ki gmail ayge jo email send kar reha hai.
    $mail->setFrom('shahkaif327@gmail.com', 'Kaif Sheikh');

    // RECEIVER: jisko send kiya ja reha hai oiski gmail ayge.
    $mail->addAddress($email, $name); 

    // Email content (Jo message user ko jayega)
    $mail->isHTML(true);
    $mail->Subject = "Thank you for contacting us, $name!";
    $mail->Body    = "<h3>Hello $name,</h3>
                      <p>Humay aapka message mil gaya hai. Shukriya!</p>
                      <p><b>Aapka Message:</b> $message</p>";

    // Send Email
    $mail->send();
    echo "Email successfully sended";
} catch (Exception $e) {
    echo "Error: {$mail->ErrorInfo}";
}
?>
```