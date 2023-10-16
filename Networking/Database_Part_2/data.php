<!DOCTYPE html>
<html>
    <body>
       <?php
        foreach($_REQUEST as $key => $value){
            echo "$key: $value<br>\n";
        }
        $varNode_name = $_GET['nodeID'];
        $varTimeStamp = $_GET['nodeTime'];
        $varTemp = $_GET['nodeTemp'];
        $varHumi = $_GET['nodeHumi'];
       
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
        $query = "INSERT INTO sensor_data (node_name, time_received, temperature, humidity) VALUES ('$varNode_name', '$varTimeStamp', '$varTemp', '$varHumi')";
  
        //execute query
        if($mysqli->query($query) === TRUE){
            echo "New record created successfully \n";
        }else{
            echo "Error: " .$query. "<br>" .$mysqli;
        }
        
        //close connection
        $mysqli->close();

        ?> 
    </body>
</html>