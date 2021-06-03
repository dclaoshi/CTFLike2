<html>
<head>
	<title>Once More</title>
</head>
<body><br />
<center>
<?php
$flag = "ctf{xckvhnksahdfkshjadkfjhaskjdhf}";
if (isset ($_GET['password'])) {
	if (ereg ("^[a-zA-Z0-9]+$", $_GET['password']) === FALSE)
	{
		echo '<p>You password must be alphanumeric</p>';
	}
	else if (strlen($_GET['password']) < 8 && $_GET['password'] > 9999999)
	{
		if (strpos ($_GET['password'], '*-*') !== FALSE)
		{
			die('Flag: ' . $flag);
		}
		else
		{
			echo('<p>*-* have not been found</p>');
		}
	}
	else
	{
		echo '<p>Invalid password</p>';
	}
}
?>
<br />
<form method="get">
	<input type="text" name="password" placeholder="Password" /><br/><br />
	<input type="submit" value="Check"/>
</form>

<hr /><br/>
<input type="button" name="View" value="View the source code" onClick="document.all.table.style.display=(document.all.table.style.display =='none')?'':'none'"/>
<table width="100%" border="0" cellspacing="0" cellpadding="0" bordercolor="#D5DEF9" id=table style="display:none">
<td><br />
<center><textarea name="viewTheSourseCode" cols="80" rows="20">
&lt?php
if (isset ($_GET['password'])) {
	if (ereg ("^[a-zA-Z0-9]+$", $_GET['password']) === FALSE)
	{
		echo '<p>You password must be alphanumeric</p>';
	}
	else if (strlen($_GET['password']) < 8 && $_GET['password'] > 9999999)
	{
		if (strpos ($_GET['password'], '*-*') !== FALSE)
		{
			die('Flag: ' . $flag);
		}
		else
		{
			echo('<p>*-* have not been found</p>');
		}
	}
	else
	{
		echo '<p>Invalid password</p>';
	}
}
?&gt;
</textarea></center></td></table>
</center>
</body>
</html>