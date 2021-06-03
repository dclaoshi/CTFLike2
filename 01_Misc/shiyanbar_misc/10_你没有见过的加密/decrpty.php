<?php


	function encrypt($str)
	{
		$cryptedstr = "";
		srand(3284724);
		for ($i =0; $i < strlen($str); $i++)
		{
			$tmp = rand(0, 255);
			$temp = ord(substr($str,$i,1)) ^ $tmp;
			while(strlen($temp)<3)
			{
				$temp = "0".$temp;
			}
			$cryptedstr .= $temp. "";
		}
		return base64_encode($cryptedstr);
	}

	function decrypt($str)
	{
		srand(3284724);
		if(preg_match('%^[a-zA-Z0-9/+]*={0,2}$%',$str))
		{
			$str = base64_decode($str);
			if ($str != "" && $str != null && $str != false)
			{
				$decStr = "";
				for ($i=0; $i < strlen($str); $i+=3)
				{
					$array[$i/3] = substr($str,$i,3);
				}
				foreach($array as $s)
				{
					$tmp = rand(0, 255);
					$a = intval($s) ^ $tmp ;
					$decStr .= chr($a);
				}
				return $decStr;
			}
			return false;
		}
		return false;
	}
	echo encrypt("flag{you_are_successful}");
	echo "\n";
	echo decrypt("MjUyMTUxMDQzMDI3MDQwMTg3MTc2MTQ3MTU2MTMyMDQzMDI5MDM3MjE0MDg4MTExMDE1MDU4MjM3MjE3MTIyMDQxMjM2MTQz");
	echo "\n";
	echo decrypt("MDEzMjE5MDAyMTg0MTUzMjQwMTQ0MDc3MjUzMDk2MTc1MTUzMTE4MTg4MDEwMDA2MTg4MDA0MjM4MDI1MTA3MTU4MTc5MTM4");
	
?>