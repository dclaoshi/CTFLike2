<?php


$info = ""; 
$req = [];
$flag="xxxxxxxxxx";

ini_set("display_error", false); 
error_reporting(0); 


if(!isset($_POST['number'])){
   header("hint:6c525af4059b4fe7d8c33a.txt");

   die("have a fun!!"); 
}

foreach([$_POST] as $global_var) { 
    foreach($global_var as $key => $value) { 
        $value = trim($value); 
        is_string($value) && $req[$key] = addslashes($value); 
    } 
} 


function is_palindrome_number($number) { 
    $number = strval($number); 
    $i = 0; 
    $j = strlen($number) - 1; 
    while($i < $j) { 
        if($number[$i] !== $number[$j]) { 
            return false; 
        } 
        $i++; 
        $j--; 
    } 
    return true; 
} 


if(is_numeric($_REQUEST['number'])){
    
   $info="sorry, you cann't input a number!";

}elseif($req['number']!=strval(intval($req['number']))){
      
     $info = "number must be equal to it's integer!! ";  

}else{

     $value1 = intval($req["number"]);
     $value2 = intval(strrev($req["number"]));  

     if($value1!=$value2){
          $info="no, this is not a palindrome number!";
     }else{
          
          if(is_palindrome_number($req["number"])){
              $info = "nice! {$value1} is a palindrome number!"; 
          }else{
             $info=$flag;
          }
     }

}

echo $info;



