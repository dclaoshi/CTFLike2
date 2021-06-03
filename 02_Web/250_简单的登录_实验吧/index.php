<?php
define("SECRET_KEY", '***********');
define("METHOD", "aes-128-cbc");
error_reporting(0);
include('conn.php');
function sqliCheck($str){
	if(preg_match("/\\\|,|-|#|=|~|union|like|procedure/i",$str)){
		return 1;
	}
	return 0;
}
function get_random_iv(){
    $random_iv='';
    for($i=0;$i<16;$i++){
        $random_iv.=chr(rand(1,255));
    }
    return $random_iv;
}
function login($info){
	$iv = get_random_iv();
	$plain = serialize($info);
    $cipher = openssl_encrypt($plain, METHOD, SECRET_KEY, OPENSSL_RAW_DATA, $iv);
    setcookie("iv", base64_encode($iv));
    setcookie("cipher", base64_encode($cipher));
}
function show_homepage(){
	global $link;
    if(isset($_COOKIE['cipher']) && isset($_COOKIE['iv'])){
        $cipher = base64_decode($_COOKIE['cipher']);
        $iv = base64_decode($_COOKIE["iv"]);
        if($plain = openssl_decrypt($cipher, METHOD, SECRET_KEY, OPENSSL_RAW_DATA, $iv)){
            $info = unserialize($plain) or die("<p>base64_decode('".base64_encode($plain)."') can't unserialize</p>");
            $sql="select * from users limit ".$info['id'].",0";
            $result=mysqli_query($link,$sql);
            
            if(mysqli_num_rows($result)>0  or die(mysqli_error($link))){
            	$rows=mysqli_fetch_array($result);
				echo '<h1><center>Hello!'.$rows['username'].'</center></h1>';
			}
			else{
				echo '<h1><center>Hello!</center></h1>';
			}
        }else{
            die("ERROR!");
        }
    }
}
if(isset($_POST['id'])){
    $id = (string)$_POST['id'];
    if(sqliCheck($id))
		die("<h1 style='color:red'><center>sql inject detected!</center></h1>");
    $info = array('id'=>$id);
    login($info);
    echo '<h1><center>Hello!</center></h1>';
}else{
    if(isset($_COOKIE["iv"])&&isset($_COOKIE['cipher'])){
        show_homepage();
    }else{
        echo '<body class="login-body" style="margin:0 auto">
                <div id="wrapper" style="margin:0 auto;width:800px;">
                    <form name="login-form" class="login-form" action="" method="post">
                        <div class="header">
                        <h1>Login Form</h1>
                        <span>input id to login</span>
                        </div>
                        <div class="content">
                        <input name="id" type="text" class="input id" value="id" onfocus="this.value=\'\'" />
                        </div>
                        <div class="footer">
                        <p><input type="submit" name="submit" value="Login" class="button" /></p>
                        </div>
                    </form>
                </div>
            </body>';
    }
}
?>