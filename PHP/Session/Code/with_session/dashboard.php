<?php

session_start();

if (!isset($_SESSION['user_id'])) {

    header("Location: login.php");
    exit;
}

?>

<h1>Dashboard</h1>

<h2> Welcome <?php echo $_SESSION['username']; ?> </h2>

<p> Your User ID: <?php echo $_SESSION['user_id']; ?> </p>

<a href="logout.php">Logout</a>