<?php

session_start();
session_unset();
session_destroy();

header("Location: login.php");
exit;

// -------------------------------

# Professional Approach:

// session_start();

// $_SESSION = [];

// session_destroy();

// setcookie(
//     session_name(),
//     '',
//     time() - 3600,
//     '/'
// );

// header("Location: login.php");
// exit;

?>