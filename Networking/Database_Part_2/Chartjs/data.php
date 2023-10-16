<?php
//setting header to json
header('Content-Type: application/json');

//database
define('DB_HOST', 'localhost');
define('DB_USERNAME', 'id21358706_db_danielrebich');
define('DB_PASSWORD', 'Mypassword12$');
define('DB_NAME', 'id21358706_danielrebich');

//get connection
$mysqli = new mysqli(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME);

if(!$mysqli){
  die("Connection failed: " . $mysqli->error);
}

//query to get data from the table
$query = sprintf("SELECT node_name, time_received, temperature, humidity FROM sensor_data");

//execute query
$result = $mysqli->query($query);

//loop through the returned data
$data = array();
foreach ($result as $row) {
    if($row['node_name'] == "node_1"){
        $data[] = $row;
    }
}

//close connection
$mysqli->close();

//now print the data
print json_encode($data);
