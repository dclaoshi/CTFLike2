<?php
if(isset($_GET[id])){
    if(eregi("hackerDJ",$_GET[id])) {
    echo("<p>not allowed!</p>");
    exit();
    }

    $_GET[id] = urldecode($_GET[id]);
    if($_GET[id] == "hackerDJ")
    {
    echo "<p>Access granted!</p>";
    echo "<p>flag: *****************} </p>";
    }
}
?>


<br><br>
Can you authenticate to this website?
