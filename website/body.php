<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="viewport" content="width=device-width">
        <link rel="stylesheet" href="O_index.css">
        <title>body</title>
    </head>
    <div class='middle'>
        <div class='left'>
            <form action="" method="post" enctype="multipart/form-data">
                <div class='name'>
                    <label>Name:</label>
                    <input type="varchar" class="form-control" placeholder="Enter name" name="user_name">
                </div>
                <div class='place'>
                    <label>Place:</label>
                    <input type="text" class="form-control" placeholder="Enter place" name="place">
                </div>
                <div class='date'>
                    <label>Date:</label>
                    <input type="date" class="form-control" placeholder="Enter date" name="date">
                </div>
                <div class='object'>
                    <label>Object:</label>
                    <input type="text" class="form-control" placeholder="Enter object" name="object">
                </div>
                <div class='discription'>
                    <label>Discription:</label>
                    <input type="text" class="form-control" placeholder="Details" name="details">
                </div>
                <div class="button">
                    <input type="submit" name="insert_btn" class="btn btn-primary" ><br>
                    <a class="btn btn-primary", href='index_2.php'>View updated info</a>
                </div>
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
                            $user_name=NULL;
                            $place=NULL;
                            $date=NULL;
                            $object=NULL;
                            $details=NULL;
                        }
                    }
                ?>
            </form>
        </div>
        <div class="right">   
            <table>
                <tr class='info'>
                    <th>Log Id</th>
                    <th>Name</th>
                    <th>Place</th>
                    <th>Date</th>
                    <th>Object</th>
                    <th>Details</th>
                </tr>
                <?php
                    $conn = mysqli_connect('localhost','root','','crud');
                // web assisted fetching of many values
                $sql = "SELECT * FROM information";
                $result = $conn->query($sql);

                if ($result->num_rows > 0) {
                  // output data of each row
                  while($row = $result->fetch_assoc()) {
                    echo "<tr> <td>" . $row["record_ID"]. "</td> <td>" . $row["user_name"]. "</td> <td>" . $row["place"]. "</td> <td>" . $row["date"].  "</td> <td>" . $row["object_name"].  "</td> <td>" . $row["description"].   "</td></tr>";
                  }
                } else {
                  echo "<tr><th>0 results</th></tr>";
                }
                ?>
            </table>
        </div>
    </div>
</html>