<?php
/*
    This file is part of Futurice Taxi Button package. 

    Futurice Taxi Button is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License version 3 as published by
    the Free Software Foundation.

    Futurice Taxi Button is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Futurice Taxi Button.  If not, see <http://www.gnu.org/licenses/>.
*/


// Settings
$folder = "/var/run/taxi/";
$lock = $folder."lock";
$messages = $folder."messages";

// count lines from messages file
$messageLines = explode(" ",exec("wc -l ".$messages));

// If there's too many lines, rotate message file
if($messageLines[0] + 1 > 500){
  rename($messages, $folder."old_messages/messagesTo".time());
}

// This typically goes to syslog, depending on system configuration
error_log("Incoming message: ".$_GET["message"]);

// Split message to parts for parsing
$words = explode(" ", $_GET["message"]);

// Default values for parsing
$key = "ERROR";
$value = "-1";

if($words[0] == "Tilaus"){ // First message
  $key = "TILAUS";
  $value = $words[count($words)-1];
}else if($words[0] == "Taksi"){ // Taxi confirmed the order
  $key = "TAKSI";
  $value = $words[2];
  unlink($lock);
}else if($words[0] == "Kaikki"){ // All taxis are reserved
  $key = "VARATTU";
  unlink($lock);
}else{ // Unknown message
  unlink($lock);
}

// Write status to messages file
$file = fopen($messages, "a");
fwrite($file,time() .":". $key ." ". $value ."\n");
fclose($file);
?>
