<html>
<head>
<title>Forms</title>
</head>
<body>

<?php 

if(isset($_POST["showsource"])){
    $showsource = $_POST["showsource"];
    if($showsource == 1){
        echo '<pre>$a = $_POST["PIN"];
        if ($a == -19827747736161128312837161661727773716166727272616149001823847) {
            echo "Congratulations! The flag is $flag";
        } else {
            echo "User with provided PIN not found."; 
        }</pre>';
    }
}

if(isset($_POST["PIN"])){
    $a = $_POST["PIN"];
    if ($a == -19827747736161128312837161661727773716166727272616149001823847) {
        echo "Congratulations! The flag is $flag";
    } else {
        echo "User with provided PIN not found."; 
    }
}
?>    
<form action="" method="post">
    PIN:<br>
    <input type="password" name="PIN" value="">
    <input type="hidden" name="showsource" value=0>
    <button type="submit">Enter</button>
</form>
</body>
</html>