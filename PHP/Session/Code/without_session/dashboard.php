<h1>Dashboard</h1>

<?php if ($username = $_GET['user'] ?? ''): ?>

    <h2>Welcome <?= htmlspecialchars($username) ?></h2>
    <a href="logout.php">Logout</a>

<?php else: ?>

    <p>You are not logged in.</p>
    <a href="login.php">Go to Login</a>

<?php endif; ?>

</body>
</html>