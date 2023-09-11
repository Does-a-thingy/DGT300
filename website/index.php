<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="viewport" content="width=device-width">
        <link rel="stylesheet" href="index.css">
        <title>Lost and found</title>
    </head>
    <?php
    
    $conn =mysqli_connect('localhost','root','','crud');
    if(isset($_POST['insert_btn'])){
        $user_name=$_POST['user_name'];
        $place=$_POST['place'];
        $date=$_POST['date'];
        $object=$_POST['object'];
        $details=$_POST['details'];

        $insert ="INSERT INTO information(user_name,place,date,object_name,description)
        VALUES('$user_name','$place','$date','$object','$details')";
        $run_insert =mysqli_query($conn,$insert);
        if($run_insert){
            echo "record inserted";
        }
        else{
            echo "try again";
        }

    }
    
    $conn = mysqli_connect('localhost','root','','crud');
    $select="SELECT * FROM information"; // select all data from table and store it under select variable
    $run =mysqli_query($conn,$select); // this command is to establish the connection and run the query
    while($row_user =mysqli_fetch_array($run)){// this command will store the data in the form of array
        $record_id=$row_user['record_ID'];
        $user_name=$row_user['user_name'];
        $place=$row_user['place'];
        $date=$row_user['date'];
        $details=$row_user['description'];
    }
    ?>
    
    <header><?php echo file_get_contents("header.html");?></header>
    <body><?php echo file_get_contents("body.php");   ?></body>
    <footer><?php echo file_get_contents("footer.html");?></footer>

</html>