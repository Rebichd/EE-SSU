<!DOCTYPE HTML>
<html>
<head>
        <title>Project_B2</title>
</head>

<body>
        <form action="project_B2.php" method="get">
                Color: <input type="text" name="color"><br>
                Plural Noun: <input type="text" name="pluralNoun"><br>
                Celebrity: <input type="text"   name="celebrity"><br>
                <input type="submit"><br><br>
        </form>

        <?php
                $color = $_GET["color"];
                $pluralNoun = $_GET["pluralNoun"];
                $celebrity = $_GET["celebrity"];

                echo "Roses are " .$color. "<br>";
                echo $pluralNoun. " are blue <br>";
                echo "I love " .$celebrity;
        ?>
</body>
</html>
