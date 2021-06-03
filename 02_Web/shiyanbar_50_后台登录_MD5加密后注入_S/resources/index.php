<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body style="background-color: #999">
	<div style="position:relative;margin:0 auto;width:300px;height:200px;padding-top:100px;font-size:20px;">
	<form action="" method="post">
		<table>
			<tr>
				请用管理员密码进行登录~~
			</tr>
			<tr>
				<td>密码：</td><td><input type="text" name='password'></td>
			</tr>
			<tr>
				<td><input type="submit" name='submit' style="margin-left:30px;"></td>
			</tr>
		</table>
	</form>
<?php 
error_reporting(0);
if(isset($_POST['password'])){
    $link = mysql_connect('localhost', 'root', '');
    if (!$link) { 
    die('Could not connect to MySQL: ' . mysql_error()); 
    } 
    // 选择数据库
    $db = mysql_select_db("test", $link);
    if(!$db)
    {
    echo 'select db error';
    exit();
    }
    // 执行sql
    $password=$_POST['password'];
    $sql = "SELECT * FROM admin WHERE username = 'admin' and password = '".md5($password,true)."'";
    $result=mysqli_query($link,$sql);
    if(mysqli_num_rows($result)>0){
        echo 'flag is :'.$flag;
    }
    else{
        echo '密码错误!';
    } 
}
?>
	</div>
	<!-- $password=$_POST['password'];
	$sql = "SELECT * FROM admin WHERE username = 'admin' and password = '".md5($password,true)."'";
	$result=mysqli_query($link,$sql);
		if(mysqli_num_rows($result)>0){
			echo 'flag is :'.$flag;
		}
		else{
			echo '密码错误!';
		} -->
</body>
</html>
