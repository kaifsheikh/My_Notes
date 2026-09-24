<?php
session_start();

if (isset($_POST['login'])) {

    $username = $_POST['username'];
    $password = $_POST['password'];

    // Simple example credentials
    if ($username === "kaif" && $password === "12345") {

        // Session data
        $_SESSION['user_id'] = 10;
        $_SESSION['username'] = $username;

        header("Location: dashboard.php");
        exit;

    } else {
        $error = "Invalid Credentials";
    }
}

?>

<h2>Login</h2>

<?php if (isset($error)): ?>
    <p style="color: red;"><?= htmlspecialchars($error) ?></p>
<?php endif; ?>

<form method="POST">

    <input type="text" name="username" placeholder="Username">
    <br><br>

    <input type="password" name="password" placeholder="Password">
    <br><br>

    <button type="submit" name="login">Login</button>

</form>