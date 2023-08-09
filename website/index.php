<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="viewport" content="width=device-width">
        <link rel="stylesheet" href="index.css">
        <title>Lost and found</title>
    </head>
    <?php
        $hostName = "localhost";
        $userName = "root";
        $password = "";
        $database = "crud";

        $conn = mysqli_connect($hostName, $userName, $password, $database)
            //Host name, User name, password, database names

        //$db = $conn
        //$table = ""

        if(isset($_POST['insert_btn'])){
            $name = $_POST['user_name']
            $place = $_POST['place']
            $date = $_POST['date']
            $object = $_POST['object']
            $discript = $_POST['discription']

            $insert = "INSERT INTO 
            information(date,object,place)
            VALUES('$name', '$place', '$date', '$object', '$discript')";

            $run_insert = mysqli_query($conn, $insert);

            if($run_insert) {
                echo "Record inserted";
            }
            else {
                echo "Try again";
            }
        echo file_get_contents("header.html");
        echo file_get_contents("body.html");
        echo file_get_contents("footer.html");
        }
    ?>

</html>