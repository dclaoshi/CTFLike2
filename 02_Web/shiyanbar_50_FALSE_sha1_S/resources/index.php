<html>
<head>
	<title>PHP Code Audit</title>
</head>
<body><br/>
<center>
<?php
if (isset($_GET['name']) and isset($_GET['password'])) {
    if ($_GET['name'] == $_GET['password'])
        echo '<p>Your password can not be your name!</p>';
    else if (sha1($_GET['name']) === sha1($_GET['password']))
      die('Flag: '.$flag);
    else
        echo '<p>Invalid password.</p>';
}
else{
	echo '<p>Login first!</p>';
?>
<br/>
<form method="Get">
	<input type="text" name="name" /><br/>
	<input type="password" name="password"  /><br/><br/>
	<input type="submit" value="Login"/>
</form>

<hr /><br/>
<input type="button" name="View" value="View the source code" onClick="document.all.table.style.display=(document.all.table.style.display =='none')?'':'none'"/>
<table width="100%" border="0" cellspacing="0" cellpadding="0" bordercolor="#D5DEF9" id=table style="display:none">
<td><br />
<center><textarea name="viewTheSourseCode" cols="60" rows="14">

&lt?php
if (isset($_GET['name']) and isset($_GET['password'])) {
    if ($_GET['name'] == $_GET['password'])
        echo '<p>Your password can not be your name!</p>';
    else if (sha1($_GET['name']) === sha1($_GET['password']))
      die('Flag: '.$flag);
    else
        echo '<p>Invalid password.</p>';
}
else{
	echo '<p>Login first!</p>';
?&gt;
</textarea></center></td></table>
</center>
</body>
</html>