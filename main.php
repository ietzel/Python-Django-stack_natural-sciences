<?php

print "<head>\n";
print "  <title>Mars Simulator</title>\n";
print "</head>\n";
print "<body>\n";
print "  <p>Driver, Flier, Slitherer, Hopper, Crawler, and Runner meet up for the cave exploration mission. The first one drives the other 5 to the cavity, and hoists them down. They find traces of water, and a big place for settlement. Findings reported...\")</p>\n";
print "</body>";

$servername = "localhost";
$username = "username";
$password = "password";

$conn = new mysqli($servername, $username, $password);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>
