<html>
<head>
	<title>Guess Next Session</title>
</head>
<body><br/>
<center>
<?php
session_start(); 
if (isset ($_GET['password'])) {
    if ($_GET['password'] == $_SESSION['password'])
        die ('Flag: '.$flag);
    else
        echo '<p>Wrong guess.</p>';
}

mt_srand((microtime() ^ rand(1, 10000)) % rand(1, 10000) + rand(1, 10000));
?>


<li>289913</li><li>3382055</li><li>7149288</li><br />

<form method="get">
	<input type="text" name="password" placeholder="Next number" /><br /><br/>
	<input type="submit" value="Guess"/>
</form>

<hr /><br/>
<input type="button" name="View" value="View the source code" onClick="document.all.table.style.display=(document.all.table.style.display =='none')?'':'none'"/>
<table width="100%" border="0" cellspacing="0" cellpadding="0" bordercolor="#D5DEF9" id=table style="display:none">
<td><br />
<center><textarea name="viewTheSourseCode" cols="45" rows="15">

&lt?php
session_start(); 
if (isset ($_GET['password'])) {
    if ($_GET['password'] == $_SESSION['password'])
        die ('Flag: '.$flag);
    else
        print '<p>Wrong guess.</p>';
}

mt_srand((microtime() ^ rand(1, 10000)) % rand(1, 10000) + rand(1, 10000));
?&gt;
</textarea></center></td></table>

</center>
</body>
</html>
