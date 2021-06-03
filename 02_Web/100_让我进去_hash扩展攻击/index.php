<html>
<body>
<?php
$flag = "XXXXXXXXXXXXXXXXXXXXXXX";
$secret = "XXXXXXXXXXXXXXX"; // This secret is 15 characters long for security!

$username = $_POST["username"];
$password = $_POST["password"];

if (!empty($_COOKIE["getmein"])) {
    if (urldecode($username) === "admin" && urldecode($password) != "admin") {
        if ($COOKIE["getmein"] === md5($secret . urldecode($username . $password))) {
            echo "Congratulations! You are a registered user.\n";
            die ("The flag is ". $flag);
        }
        else {
            die ("Your cookies don't match up! STOP HACKING THIS SITE.");
        }
    }
    else {
        die ("You are not an admin! LEAVE.");
    }
}

setcookie("sample-hash", md5($secret . urldecode("admin" . "admin")), time() + (60 * 60 * 24 * 7));

if (empty($_COOKIE["source"])) {
    setcookie("source", 0, time() + (60 * 60 * 24 * 7));
}
else {
    if ($_COOKIE["source"] != 0) {
        echo '<pre>$flag = "XXXXXXXXXXXXXXXXXXXXXXX";
        $secret = "XXXXXXXXXXXXXXX"; // This secret is 15 characters long for security!
        
        $username = $_POST["username"];
        $password = $_POST["password"];
        
        if (!empty($_COOKIE["getmein"])) {
            if (urldecode($username) === "admin" && urldecode($password) != "admin") {
                if ($COOKIE["getmein"] === md5($secret . urldecode($username . $password))) {
                    echo "Congratulations! You are a registered user.\n";
                    die ("The flag is ". $flag);
                }
                else {
                    die ("Your cookies don\'t match up! STOP HACKING THIS SITE.");
                }
            }
            else {
                die ("You are not an admin! LEAVE.");
            }
        }
        
        setcookie("sample-hash", md5($secret . urldecode("admin" . "admin")), time() + (60 * 60 * 24 * 7));
        
        if (empty($_COOKIE["source"])) {
            setcookie("source", 0, time() + (60 * 60 * 24 * 7));
        }
        else {
            if ($_COOKIE["source"] != 0) {
                echo ""; // This source code is outputted here
            }
        }</pre>'; // This source code is outputted here
    }
}
?>
<h1>Admins Only!</h1>
<p>If you have the correct credentials, log in below. If not, please LEAVE.</p>
<form method="POST">
    Username: <input type="text" name="username"> <br>
    Password: <input type="password" name="password"> <br>
    <button type="submit">Submit</button>
</form>

</body>
</html>