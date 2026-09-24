<?php

if (isset($_POST['login'])) {

    $username = $_POST['username'];
    $password = $_POST['password'];

    if ($username === "kaif" && $password === "12345") {

        header("Location: dashboard.php?user=" . urlencode($username));
        exit;

    } else {
        $error = "Invalid Credentails";
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