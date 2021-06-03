<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>Game 19</title>
<link href="templatemo_style.css" rel="stylesheet" type="text/css" />
</head>
<body>
<div id="templatemo_container">
    <div id="templatemo_header">
        <div id="website_title">

        </div>
    </div> 

    <div id="templatemo_menu">
        <ul>
            <li><a href="#" class="current">Tips</a></li>
            <li><b>View the source code</b></li>
        </ul> 
    </div>  
    
    <div id="templatemo_content_wrapper">
    
        <div id="templatemo_content">
        	
            <div class="content_title_01">PHP代码审计</div>
			<div class="horizontal_divider_01">&nbsp;</div>
			<div class="cleaner">&nbsp;</div>
			<center>
				<p><?php
function GetIP(){
if(!empty($_SERVER["HTTP_CLIENT_IP"]))
	$cip = $_SERVER["HTTP_CLIENT_IP"];
else if(!empty($_SERVER["HTTP_X_FORWARDED_FOR"]))
	$cip = $_SERVER["HTTP_X_FORWARDED_FOR"];
else if(!empty($_SERVER["REMOTE_ADDR"]))
	$cip = $_SERVER["REMOTE_ADDR"];
else
	$cip = "0.0.0.0";
return $cip;
}

$GetIPs = GetIP();
if ($GetIPs=="1.1.1.1"){
echo "Great! Key is *********";
}
else{
echo "错误！你的IP不在访问列表之内！";
}
?></p>				
                <input type="button" name="Submit3" value="View the source code" onClick="document.all.table.style.display=(document.all.table.style.display =='none')?'':'none'"/>
				<table width="100%" border="0" cellspacing="0" cellpadding="0" bordercolor="#D5DEF9" id=table style="display:none">
				<td>
				<br>
				<center><textarea name="textarea" cols="80%" rows="26">
&lt?php
function GetIP(){
if(!empty($_SERVER["HTTP_CLIENT_IP"]))
	$cip = $_SERVER["HTTP_CLIENT_IP"];
else if(!empty($_SERVER["HTTP_X_FORWARDED_FOR"]))
	$cip = $_SERVER["HTTP_X_FORWARDED_FOR"];
else if(!empty($_SERVER["REMOTE_ADDR"]))
	$cip = $_SERVER["REMOTE_ADDR"];
else
	$cip = "0.0.0.0";
return $cip;
}

$GetIPs = GetIP();
if ($GetIPs=="1.1.1.1"){
echo "Great! Key is *********";
}
else{
echo "错误！你的IP不在访问列表之内！";
}
?&gt;
				</textarea></center></td>
			</table>
			<br><br>
			</center>
			
	
            
             
             <div class="cleaner">&nbsp;</div>
        </div>
        <div class="cleaner">&nbsp;</div>
    </div>
    
    <div id="templatemo_footer">
		
	</div>
</div>
</body>
</html>