<?php
$hostName = "localhost";
$dbuser = "root";
$dbPassword = "";
$dbName = "login_register";
$conn = mysqli_connect($hostName, $dbuser, $dbPassword, $dbName);
if (!$conn) {
die("Something went wrong;");
}