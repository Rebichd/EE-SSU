<!DOCTYPE html>
<html>
  <head>
    <title> Sensor Data & Register </title>
    
    <!-- For CSS styling the page -->
    <style>
        table {margin: 0 auto; font-size: medium; border: 1px solid black;}
 
        h1 {text-align: center; color:#000000; font-size: x-large; font-family: 'Gill Sans', 'Gill Sans MT', ' Calibri', 'Trebuchet MS', 'sans-serif';}
        
        h2{text-align: center; color: #000000; font-size: large;}
 
        td {background-color: #FFFFFF; border: 1px solid black;}
 
        th,td {font-weight: bold; border: 1px solid black; padding: 10px; text-align: center;}
 
        td {font-weight: lighter;}
        
        /* odd rows are grey */
        tr:nth-child(odd) td{background-color: #D3D3D3;}
        
        
        /* Used for bar graph*/
        #chart-container {
            width: 640px;
            height: auto;
            display: block;
            margin: 0 auto;
        }
        
        
    </style>
    <!-- End of CSS styling -->
  </head>
  
  <body>
    <?php //database
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
        $queryReg = sprintf("SELECT node_name, manufacturer, longitude, latitude FROM sensor_register");

        //execute query
        $result = $mysqli->query($query);
        $resultReg = $mysqli->query($queryReg);
 
        //close connection
        $mysqli->close();

        //now print the data
        //print json_encode($data);
        ?>
    <h1> Welcome to SSU IoT Lab </h1>  
    <hr></hr>
    
    <h2><br></h2>
    
    <h2> Registered Sensor Nodes </h2>
    <table>
        <tr>
            <th>Node Name</th>
            <th>Manufacturer</th>
            <th>Longitude</th>
            <th>Latitude</th>
        </tr>
        <tr>
        <!-- PHP CODE TO FETCH DATA FROM ROWS -->
        <?php 
            // LOOP TILL END OF DATA
            while($rows=$resultReg->fetch_assoc())
            {
                switch ($rows['node_name']){
                    case "node_1":
                        $color = "#FFFFCC";
                        break;
                    case "node_2":
                        $color = "#FFCCCC";
                        break;
                    case "node_3":
                        $color = "#CCFFCC";
                        break;
                    case "node_4":
                        $color = "#CCFFFF";
                        break;
                    case "node_5":
                        $color = "#CC99CC";
                        break;
                }
        ?>    
        <tr bgcolor=<?php echo $color; ?>>
            <th><?php echo $rows['node_name'];?></th> <!-- This is a header to change color based on node name-->
            <td><?php echo $rows['manufacturer'];?></td>
            <td><?php echo $rows['longitude'];?></td>
            <td><?php echo $rows['latitude'];?></td>
        </tr>
        <?php } ?>
    </table> 
    
    <h2><br></h2>
    <h2> Sensor Data Table </h2>
    
    
    <table>
        <!-- Column Title Row -->
        <tr>
            <th>Node Name</th>
            <th>Time Stamp</th>
            <th>Temperature</th>
            <th>Humidity</th>
        </tr>
        <tr>
        <!-- PHP CODE TO FETCH DATA FROM ROWS -->
        <?php 
            // LOOP TILL END OF DATA
            $count = 0;
            $sumTemp = 0;
            $sumHumi = 0;
            while($rows=$result->fetch_assoc())
            {
                switch ($rows['node_name']){
                    case "node_1":
                        $color = "#FFFFCC";
                        break;
                    case "node_2":
                        $color = "#FFCCCC";
                        break;
                    case "node_3":
                        $color = "#CCFFCC";
                        break;
                    case "node_4":
                        $color = "#CCFFFF";
                        break;
                    case "node_5":
                        $color = "#CC99CC";
                        break;
                } ?>    
        <tr bgcolor=<?php echo $color; ?>>
            <th><?php echo $rows['node_name'];?></th> <!-- This is a header to change color based on node name-->
            <td><?php echo $rows['time_received'];?></td>
            <td><?php echo $rows['temperature'];?></td>
            <td><?php echo $rows['humidity'];?></td>
        </tr>
        <?php
            
            if($rows['node_name'] == "node_1"){
                $count++;
                $sumTemp = $sumTemp + $rows['temperature'];
                $averageTemp = $sumTemp / $count;
                $sumHumi = $sumHumi + $rows['humidity'];
                $averageHumi = $sumHumi / $count;
            }
       
            
         } ?>
    </table> 
    
    <h2><br></h2>
    <h2> The Average Temperature for node_1 is: <?php echo $averageTemp; ?> C </h2>
    <h2> The Average Humidity for node_1 is: <?php echo $averageHumi; ?> % </h2>
    
    
    <h2><br></h2>
    <!-- Bar Graph -->
    <div id="chart-container">
      <canvas id="mycanvas"></canvas>
    </div>

    <!-- javascript -->
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- This is the location of app.js file - we are assuming it is in the same folder as this file-->
    <script type="text/javascript" src="Chartjs/app.js"></script>
    
    
    
  </body>
</html>
