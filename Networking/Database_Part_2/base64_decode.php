<!DOCTYPE html>
<html>
    <body>
      <?php
        foreach($_REQUEST as $key => $value){
            echo "Received coded meesage: $key <br>\n";
        }
        $myDecodedString = base64_decode($key);
        echo "Received decoded meesage: $myDecodedString <br>\n";
        $varArray = array();
        
        while(strlen($myDecodedString) > 0){
            $posEqu = 0;
            $posAnd = 0;
            
            $string2Cut = $myDecodedString;
            $posEqu = strpos($string2Cut, '=') + 1;
            $posAnd = strpos($string2Cut, '&');
            
            if($posAnd > 0){
                $temp = substr($string2Cut, $posEqu, $posAnd - $posEqu);
                array_push($varArray, $temp);
                $myDecodedString = substr($myDecodedString, $posAnd + 1);
            }else{
                $temp = substr($string2Cut, $posEqu);
                array_push($varArray, $temp);
                break;
            }
        }
        
        $spacePos = strpos($varArray[1], '%20');
        $time = substr($varArray[1], 0, $spacePos);
        $time .= ' ';
        $time .= substr($varArray[1], $spacePos + 3);
        
        
        echo "<br>";
        echo "node_name = $varArray[0] <br>";
        echo "time_recieved = $time <br>";
        echo "temperature = $varArray[2] <br>";
        echo "humidity = $varArray[3] <br>";
      ?> 
    </body>
</html>