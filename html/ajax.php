<?php
if(isset($_GET["r"])){
	$r = $_GET["r"];
	$text = $_GET["t"];
	$voice = $_GET["v"];
	switch($r){
		case "u":
			shell_exec("sudo echo 1=-10 > /dev/servoblaster");
		break;
		case "d":
			shell_exec("sudo echo 1=+10 > /dev/servoblaster");
        	break;
        	case "l":
			shell_exec("sudo echo 0=+10 > /dev/servoblaster");
        	break;
        	case "r":
			shell_exec("sudo echo 0=-10 > /dev/servoblaster");
        	break;
		case "s":
			shell_exec("sudo espeak '$text' -v $voice");
        	break;
		case "led":
                        shell_exec("sudo python /home/pi/led.py");
                break;
	}
	echo $r;
}
	echo "ok";
?>
